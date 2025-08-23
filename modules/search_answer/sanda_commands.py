import sys
from pathlib import Path
import asyncio

current_file = Path(__file__).resolve()
invincible = current_file.parent.parent.parent
sys.path.insert(0, str(invincible))

from modules.search_answer.auto_browser import AutoBrowser

class SandAcommands:
    @staticmethod
    def sanadcommands(core):

        def autobrowse():
            print("Введите поисковый запрос: ")
            search_query = input().strip()
            
            if not search_query:
                print("Запрос не может быть пустым!")
                return
            
            print(f"Выполняю поиск по запросу: '{search_query}'...")
            
            asyncio.run(AutoBrowser.wakeup(search_query))
            
            print("Поиск завершен. Результаты сохранены в файл itog.txt")
        core.register_command("браузер", autobrowse)
        core.register_command("поиск", autobrowse) 
        
        return core 
