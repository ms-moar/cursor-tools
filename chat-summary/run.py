#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Автоматический скрипт для создания саммари переписок с использованием DeepSeek API
"""

import os
import re
import json
import requests
from datetime import datetime
from pathlib import Path

class AutoChatSummaryProcessor:
    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.history_dir = self.base_dir.parent / ".specstory" / "history"
        self.chats_dir = self.base_dir.parent / ".specstory" / "chat-summary"
        self.index_file = self.base_dir / "chat-index.md"
        self.prompt_file = self.base_dir / "summary-prompt.md"
        self.config_file = self.base_dir / "config.json"
        
        # Создаем папку chat-summary если её нет
        self.chats_dir.mkdir(parents=True, exist_ok=True)
        
        # Загружаем конфигурацию
        self.config = self.load_config()
    
    def load_config(self):
        """Загружает конфигурацию из файла"""
        default_config = {
            "deepseek_api_key": "",
            "max_tokens": 4000,
            "model": "deepseek-chat",
            "temperature": 0.1,
            "api_base": "https://api.deepseek.com"
        }
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    return {**default_config, **config}
            except:
                pass
        
        # Обновляем файл конфигурации
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        
        return default_config
    
    def load_processed_chats(self):
        """Загружает список уже обработанных чатов из индекса"""
        processed = set()
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                content = f.read()
                for line in content.split('\n'):
                    if line.strip().startswith('- [') and '|' in line:
                        match = re.search(r'\] (.+?) \|', line)
                        if match:
                            processed.add(match.group(1))
        return processed
    
    def get_file_line_count(self, file_path):
        """Подсчитывает количество строк в файле"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return sum(1 for _ in f)
        except:
            return 0
    
    def extract_date_from_filename(self, filename):
        """Извлекает дату из имени файла"""
        match = re.match(r'(\d{4}-\d{2}-\d{2})_', filename)
        return match.group(1) if match else "unknown"
    
    def load_prompt_template(self):
        """Загружает шаблон промпта"""
        if self.prompt_file.exists():
            with open(self.prompt_file, 'r', encoding='utf-8') as f:
                return f.read()
        return "Создай подробное саммари этой переписки на русском языке:"
    
    def create_summary_with_deepseek_api(self, chat_content, prompt_template):
        """Создает саммари с помощью DeepSeek API"""
        api_key = self.config.get("deepseek_api_key", "")
        
        if not api_key:
            print("API ключ DeepSeek не настроен в config.json")
            return None
        
        # Обрезаем контент если он слишком длинный (DeepSeek поддерживает больше токенов)
        max_content_length = 100000  # Примерно 100k символов
        if len(chat_content) > max_content_length:
            chat_content = chat_content[:max_content_length] + "\n\n[КОНТЕНТ ОБРЕЗАН ДЛЯ СООТВЕТСТВИЯ ЛИМИТАМ API]"
        
        full_prompt = f"{prompt_template}\n\n{chat_content}"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        data = {
            "model": self.config.get("model", "deepseek-chat"),
            "messages": [
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            "max_tokens": self.config.get("max_tokens", 4000),
            "temperature": self.config.get("temperature", 0.1),
            "stream": False
        }
        
        api_base = self.config.get("api_base", "https://api.deepseek.com")
        url = f"{api_base}/chat/completions"
        
        try:
            print(f"Отправляю запрос к DeepSeek API...")
            response = requests.post(
                url,
                headers=headers,
                json=data,
                timeout=120  # Увеличиваем таймаут для больших текстов
            )
            
            if response.status_code == 200:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    return result["choices"][0]["message"]["content"]
                else:
                    print("Неожиданный формат ответа от API")
                    return None
            else:
                print(f"Ошибка API: {response.status_code}")
                try:
                    error_detail = response.json()
                    print(f"Детали ошибки: {error_detail}")
                except:
                    print(f"Текст ошибки: {response.text}")
                return None
                
        except Exception as e:
            print(f"Ошибка при обращении к API: {e}")
            return None
    
    def extract_project_name(self, summary):
        """Извлекает название проекта из саммари"""
        lines = summary.split('\n')
        
        # Ищем в разделе "Проект и метаданные"
        for i, line in enumerate(lines):
            line = line.strip()
            if '**Проект:**' in line:
                # Извлекаем название проекта после "Проект:"
                project_match = re.search(r'\*\*Проект:\*\*\s*(.+?)(?:\s*\(|$)', line)
                if project_match:
                    project_name = project_match.group(1).strip()
                    return self.create_project_abbreviation(project_name)
        
        # Если не нашли в метаданных, ищем в первых строках
        for line in lines[:10]:
            line = line.strip().lower()
            if 'проект' in line and any(proj in line for proj in ['cursor-memory-bank', 'jira-integration', 'notion-mcp', 'devops-tools']):
                if 'cursor-memory-bank' in line:
                    return 'cmb'
                elif 'jira-integration' in line:
                    return 'jira'
                elif 'notion-mcp' in line:
                    return 'notion'
                elif 'devops-tools' in line:
                    return 'devops'
        
        return 'proj'  # Дефолтное сокращение
    
    def create_project_abbreviation(self, project_name):
        """Создает сокращение для названия проекта"""
        if len(project_name) <= 3:
            return project_name.lower()
        
        # Известные проекты и их сокращения
        known_projects = {
            'cursor-memory-bank': 'cmb',
            'jira-integration': 'jira',
            'notion-mcp': 'notion',
            'devops-tools': 'devops',
            'optimization-journey': 'opt',
            'creative-mode': 'creative',
            'memory-bank': 'mb',
            'integration': 'int',
            'automation': 'auto',
            'configuration': 'config',
            'documentation': 'docs'
        }
        
        project_lower = project_name.lower()
        
        # Проверяем известные проекты
        for full_name, abbr in known_projects.items():
            if full_name in project_lower:
                return abbr
        
        # Создаем аббревиатуру из первых букв слов
        words = re.findall(r'\b\w+', project_name)
        if len(words) > 1:
            abbr = ''.join(word[0].lower() for word in words if len(word) > 0)
            return abbr[:4]  # Максимум 4 символа
        
        # Если одно слово, берем первые 3-4 символа
        return project_name[:4].lower()
    
    def generate_title_from_summary(self, summary):
        """Генерирует название на основе саммари - максимум 4 слова"""
        # Ищем ключевые слова в саммари
        lines = summary.split('\n')
        keywords = []
        
        # Сначала ищем в разделе "Все обсуждаемые темы"
        in_topics_section = False
        for line in lines:
            line = line.strip()
            if '## Все обсуждаемые темы' in line:
                in_topics_section = True
                continue
            elif line.startswith('##') and in_topics_section:
                break
            elif in_topics_section and line and not line.startswith('#') and not line.startswith('-'):
                # Извлекаем ключевые слова из описания тем
                words = line.split()
                for word in words:
                    word = word.lower().strip('.,!?:;()[]{}')
                    # Фильтруем только значимые слова
                    if (len(word) > 3 and 
                        word not in ['этой', 'была', 'были', 'будет', 'можно', 'нужно', 'также', 'после', 'перед', 'через', 'между', 'вместе', 'против', 'внутри', 'снаружи', 'сверху', 'снизу', 'справа', 'слева', 'переписки', 'обсуждались', 'которые']):
                        keywords.append(word)
                        if len(keywords) >= 4:
                            break
                if len(keywords) >= 4:
                    break
        
        # Если не нашли в темах, ищем в первых строках саммари
        if len(keywords) < 4:
            for line in lines[:15]:  # Смотрим первые 15 строк
                line = line.strip()
                if line and not line.startswith('#') and not line.startswith('-') and not line.startswith('*'):
                    words = line.split()
                    for word in words:
                        word = word.lower().strip('.,!?:;()[]{}')
                        if (len(word) > 3 and 
                            word not in ['этой', 'была', 'были', 'будет', 'можно', 'нужно', 'также', 'после', 'перед', 'через', 'между', 'вместе', 'против', 'внутри', 'снаружи', 'сверху', 'снизу', 'справа', 'слева', 'переписки', 'проект', 'хештеги']):
                            keywords.append(word)
                            if len(keywords) >= 4:
                                break
                    if len(keywords) >= 4:
                        break
        
        # Если все еще не хватает, берем из заголовков
        if len(keywords) < 4:
            for line in lines:
                if line.startswith('##') and not line.startswith('###'):
                    words = line.replace('#', '').strip().split()
                    for word in words:
                        word = word.lower().strip('.,!?:;()[]{}')
                        if len(word) > 3 and word not in ['обсуждаемые', 'ключевые', 'моменты', 'технические', 'детали', 'результаты', 'достижения', 'полезная', 'информация']:
                            keywords.append(word)
                            if len(keywords) >= 4:
                                break
                    if len(keywords) >= 4:
                        break
        
        # Берем максимум 4 слова
        title_words = keywords[:4]
        
        if not title_words:
            return "саммари"
        
        # Соединяем слова дефисами
        title = '-'.join(title_words)
        # Убираем специальные символы
        title = re.sub(r'[^\w\s-]', '', title)
        title = re.sub(r'\s+', '-', title)
        
        return title.lower()
    
    def update_index(self, filename, line_count):
        """Обновляет индексный файл"""
        date = self.extract_date_from_filename(filename)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        entry = f"- [{date}] {filename} | Строк: {line_count} | Обработан: {timestamp} (DeepSeek)\n"
        
        with open(self.index_file, 'a', encoding='utf-8') as f:
            f.write(entry)
    
    def process_single_chat(self, file_path):
        """Обрабатывает один файл переписки"""
        filename = file_path.name
        print(f"\nОбрабатываю: {filename}")
        
        # Читаем содержимое файла
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Ошибка чтения файла {filename}: {e}")
            return False
        
        line_count = self.get_file_line_count(file_path)
        print(f"Строк в файле: {line_count}")
        print(f"Размер контента: {len(content)} символов")
        
        # Загружаем шаблон промпта
        prompt_template = self.load_prompt_template()
        
        # Создаем саммари
        print("Создаю подробное саммари с помощью DeepSeek API...")
        summary = self.create_summary_with_deepseek_api(content, prompt_template)
        
        if not summary:
            print("Не удалось создать саммари через DeepSeek API")
            return False
        
        # Генерируем название и извлекаем проект
        title = self.generate_title_from_summary(summary)
        project = self.extract_project_name(summary)
        date = self.extract_date_from_filename(filename)
        
        # Создаем имя файла для саммари: дата_проект_описание.md
        summary_filename = f"{date}_{project}_{title}.md"
        summary_path = self.chats_dir / summary_filename
        
        # Сохраняем саммари
        try:
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(f"# Подробное саммари переписки: {filename}\n\n")
                f.write(f"**Дата:** {date}\n")
                f.write(f"**Исходный файл:** {filename}\n")
                f.write(f"**Строк в оригинале:** {line_count}\n")
                f.write(f"**Размер оригинала:** {len(content)} символов\n")
                f.write(f"**Обработано:** {datetime.now().strftime('%Y-%m-%d %H:%M')} (DeepSeek AI)\n\n")
                f.write("---\n\n")
                f.write(summary)
            
            print(f"✓ Подробное саммари сохранено: {summary_filename}")
            print(f"  Размер саммари: {len(summary)} символов")
            
            # Обновляем индекс
            self.update_index(filename, line_count)
            return True
            
        except Exception as e:
            print(f"Ошибка сохранения саммари: {e}")
            return False
    
    def process_all_chats(self):
        """Обрабатывает все файлы переписок"""
        print("=== Автоматический процессор подробных саммари (DeepSeek AI) ===\n")
        
        if not self.history_dir.exists():
            print(f"Папка {self.history_dir} не найдена!")
            return
        
        # Проверяем API ключ
        if not self.config.get("deepseek_api_key"):
            print("⚠️  API ключ DeepSeek не настроен!")
            print("Отредактируйте файл config.json и добавьте ваш API ключ DeepSeek.")
            print("Получить ключ можно на: https://platform.deepseek.com/")
            return
        
        # Загружаем список уже обработанных файлов
        processed_chats = self.load_processed_chats()
        print(f"Уже обработано файлов: {len(processed_chats)}")
        
        # Получаем список всех файлов истории
        history_files = list(self.history_dir.glob("*.md"))
        history_files.sort()  # Сортируем по имени (дате)
        
        print(f"Найдено файлов истории: {len(history_files)}")
        
        # Фильтруем необработанные файлы
        new_files = [f for f in history_files if f.name not in processed_chats]
        print(f"Новых файлов для обработки: {len(new_files)}")
        
        if not new_files:
            print("Все файлы уже обработаны!")
            return
        
        # Показываем настройки
        print(f"\nНастройки DeepSeek API:")
        print(f"  Модель: {self.config.get('model', 'deepseek-chat')}")
        print(f"  Макс. токенов: {self.config.get('max_tokens', 4000)}")
        print(f"  Температура: {self.config.get('temperature', 0.1)}")
        print()
        
        # Обрабатываем каждый новый файл
        processed_count = 0
        total_chars_processed = 0
        
        for file_path in new_files:
            print(f"\n{'='*60}")
            if self.process_single_chat(file_path):
                processed_count += 1
                # Подсчитываем статистику
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        total_chars_processed += len(f.read())
                except:
                    pass
            else:
                print(f"✗ Ошибка обработки: {file_path.name}")
        
        print(f"\n{'='*60}")
        print(f"=== Обработка завершена ===")
        print(f"Успешно обработано: {processed_count} файлов")
        print(f"Общий объем обработанного текста: {total_chars_processed:,} символов")
        if processed_count > 0:
            print(f"Среднее время на файл: ~{120/processed_count:.1f} сек")

def main():
    processor = AutoChatSummaryProcessor()
    processor.process_all_chats()

if __name__ == "__main__":
    main() 