import sys
from pathlib import Path

current_file = Path(__file__).resolve()
file_manager_path = current_file.parent / "file_manager.py"
sys.path.insert(0, str(file_manager_path.parent))

from file_searhcer import FileManager, search_and_open_files, open_file_directly

class FileCommands:
    @staticmethod
    def filecommands(core):
        
        def file_search():
            print("Режим поиска файлов")
            print("Введите текст для поиска файлов:")
            search_text = input().strip()
            
            if not search_text:
                print("Текст поиска не может быть пустым!")
                return

            search_and_open_files(search_text)
        
        def file_open():
            print("Режим открытия файла по пути")
            print("Введите полный путь к файлу:")
            file_path = input().strip()
            
            if not file_path:
                print("Путь не может быть пустым!")
                return

            open_file_directly(file_path)
        
        def file_manager_full():
            fm = FileManager()
            fm.run_standalone()
        

        core.register_command("поиск по файлам", file_search)
        core.register_command("открой", file_open)
        core.register_command("файлы", file_manager_full)
