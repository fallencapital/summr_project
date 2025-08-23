#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

class FileManager:
    def __init__(self):
        self.supported_extensions = {'.pdf', '.jpg', '.png', '.txt', '.jpeg'}
    
    def find_files_everywhere(self, search_text):
        found_files = set()
        search_locations = [Path.home()]
        
        print("Начинаю поиск...")
        
        for location in search_locations:
            if location.exists():
                print(f"Ищу в: {location}")
                
                for root, dirs, files in os.walk(location):
                    try:
                        for file in files:
                            if search_text.lower() in file.lower():
                                full_path = Path(root) / file
                                found_files.add(str(full_path.resolve()))
                    except PermissionError:
                        continue
                    except KeyboardInterrupt:
                        print("Поиск прерван пользователем")
                        return list(found_files)
        
        return list(found_files)
    
    def is_supported_file(self, file_path):
        _, ext = os.path.splitext(file_path)
        return ext.lower() in self.supported_extensions
    
    def file_exists(self, file_path):
        return os.path.isfile(file_path)
    
    def open_file(self, file_path):
        try:
            subprocess.run(['xdg-open', file_path], check=True)
            print(f"Файл успешно открыт: {file_path}")
            return True
        except subprocess.CalledProcessError:
            print(f"Ошибка при открытии файла: {file_path}")
            return False
        except FileNotFoundError:
            print("Команда 'xdg-open' не найдена. Убедитесь, что вы используете Ubuntu/Linux")
            return False
    
    def display_files_menu(self, files):
        if not files:
            print("Файлы не найдены")
            return None
        
        print(f"\nНайдено файлов: {len(files)}")
        print("=" * 60)
        
        for i, file_path in enumerate(files, 1):
            file_name = os.path.basename(file_path)
            print(f"{i:2d}. {file_name}")
            print(f"    📍 {file_path}")
            print()
        
        print("=" * 60)
        return files
    
    def get_file_selection(self, files):
        while True:
            try:
                choice = input("\nВыберите номер файла для открытия (или 'назад' для нового поиска, 'выход' для завершения): ").strip().lower()
                
                if choice in ['назад', 'back', 'b']:
                    return 'back'
                elif choice in ['выход', 'exit', 'quit', 'q']:
                    return 'exit'
                elif not choice:
                    continue
                
                if choice.isdigit():
                    index = int(choice) - 1
                    if 0 <= index < len(files):
                        selected_file = files[index]
                        
                        if not self.is_supported_file(selected_file):
                            print("Неподдерживаемый формат файла!")
                            print(f"Поддерживаются только: {', '.join(self.supported_extensions)}")
                            continue
                        
                        if not self.file_exists(selected_file):
                            print(f"Файл не существует: {selected_file}")
                            continue
                        
                        return selected_file
                    else:
                        print(f"Пожалуйста, введите число от 1 до {len(files)}")
                else:
                    print("Пожалуйста, введите номер файла или команду")
                    
            except KeyboardInterrupt:
                print("\nОперация прервана")
                return 'exit'
            except Exception as e:
                print(f"Ошибка: {e}")
    
    def run_search_mode(self):
        print("=== Режим поиска файлов ===")
        print("Поддерживаемые форматы для открытия: PDF, JPG, PNG, TXT")
        print("=" * 50)
        
        while True:
            try:
                search_text = input("\nЧто ищем? (или 'выход' для завершения): ").strip()
                
                if search_text.lower() in ['выход', 'exit', 'quit', 'q']:
                    print("До свидания!")
                    return False
                    
                if not search_text:
                    print("Пожалуйста, введите текст для поиска")
                    continue
                
                files = self.find_files_everywhere(search_text)
                
                if not files:
                    print("\nФайлы не найдены")
                    continue
                
                self.display_files_menu(files)
                
                result = self.get_file_selection(files)
                
                if result == 'exit':
                    print("До свидания!")
                    return False
                elif result == 'back':
                    continue
                elif isinstance(result, str):
                    success = self.open_file(result)
                    if success:
                        input("\nНажмите Enter для продолжения поиска...")
                    
            except KeyboardInterrupt:
                print("\nДо свидания!")
                return False
            except Exception as e:
                print(f"Произошла ошибка: {e}")
    
    def run_direct_mode(self):
        print("=== Режим прямого открытия ===")
        print("Поддерживаемые форматы: PDF, JPG, PNG, TXT")
        print("=" * 40)
        
        while True:
            file_path = input("\nВведите полный путь к файлу (или 'поиск' для режима поиска, 'выход' для завершения): ").strip()
            
            if file_path.lower() in ['выход', 'exit', 'quit', 'q']:
                print("До свидания!")
                return False
            elif file_path.lower() in ['поиск', 'search', 's']:
                return True
            
            if not file_path:
                print("Путь не может быть пустым!")
                continue
            
            abs_path = os.path.abspath(file_path)
            
            if not self.file_exists(abs_path):
                print(f"Файл не существует: {abs_path}")
                continue
            
            if not self.is_supported_file(abs_path):
                print("Неподдерживаемый формат файла!")
                print(f"Поддерживаются только: {', '.join(self.supported_extensions)}")
                continue
            
            self.open_file(abs_path)
    
    def run_standalone(self):
        print("=== Файловый менеджер ===")
        print("1. Режим поиска файлов")
        print("2. Режим прямого открытия по пути")
        print("=" * 30)
        
        current_mode = 'search'
        
        while True:
            if current_mode == 'search':
                result = self.run_search_mode()
                if result is False:
                    break
                else:
                    current_mode = 'direct'
            else:
                result = self.run_direct_mode()
                if result is False:
                    break
                else:
                    current_mode = 'search'

def search_and_open_files(search_text=None):
    fm = FileManager()
    
    if search_text is None:
        search_text = input("Введите текст для поиска: ").strip()
    
    files = fm.find_files_everywhere(search_text)
    
    if not files:
        print("Файлы не найдены")
        return
    
    fm.display_files_menu(files)
    result = fm.get_file_selection(files)
    
    if isinstance(result, str) and result not in ['back', 'exit']:
        fm.open_file(result)
    
    return result

def open_file_directly(file_path):
    fm = FileManager()
    
    abs_path = os.path.abspath(file_path)
    
    if not fm.file_exists(abs_path):
        print(f"Файл не существует: {abs_path}")
        return False
    
    if not fm.is_supported_file(abs_path):
        print("Неподдерживаемый формат файла!")
        return False
    
    return fm.open_file(abs_path)
