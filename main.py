import sys
from pathlib import Path
from modules.system.system_command import SystemCommands
from modules.search_answer.sanda_commands import SandAcommands
from modules.files.file_commands import FileCommands
from core.kernel import Core 

def main():
    current_file = Path(__file__).resolve()
    sys.path.insert(0, str(current_file.parent.parent.parent))

    print("PC Ассистент запущен (введите 'help' для списка команд)")

    core = Core()

    SystemCommands.systemcommands(core)
    SandAcommands.sanadcommands(core) 
    FileCommands.filecommands(core)

    while True:
        try:
            user_input = input("> ").strip().lower()  
            
            if user_input in ('exit', 'выход'):
                print("Завершение работы...")
                break
            
            if user_input in ('help', 'помощь'):
                print("\nДоступные команды:")
                print(" - процессы (список процессов)(Системный модуль)")
                print(" - cpu (загрузка процессора)(Системный модуль)")
                print(" - ram (использование памяти)(Системный модуль)")
                print(" - диск (дисковая активность)(Системный модуль)")
                print(" - hardware (полный отчет)(Системный модуль)")
                print(" - выключи (завершить процесс)(Системный модуль)")
                print(" - браузер (авто-браузер)(Поисково-ответный модуль)")
                print(" - поиск (авто-браузер)(Поисково-ответный модуль)")  
                print(" - поиск по файлам (файловы поиск)(Файловый модуль)")
                print(" - открой (открытие только jpg, jpe, png, txt, pdf)(Файловый модуль)")
                print(" - exit (выход)\n")
                continue
                
            if not user_input:
                continue
                
            result = core.execute(user_input)  
            if result:
                print(result)
                
        except KeyboardInterrupt:
            print("\nЗавершение работы...")
            break

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
