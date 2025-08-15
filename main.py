import sys
from pathlib import Path
from modules.system.system_command import SystemCommands

def main():

    current_file = Path(__file__).resolve()
    sys.path.insert(0, str(current_file.parent.parent.parent))

    print("PC Ассистент запущен (введите 'help' для списка команд)")
    system = SystemCommands.systemcommands()


    while True:
        try:
            user_input = input("> ").strip().lower()  
            
            if user_input in ('exit', 'выход'):
                print("Завершение работы...")
                break
            
            if user_input in ('help', 'помощь'):
                print("\nДоступные команды:")
                print(" - процессы (список процессов)")
                print(" - cpu (загрузка процессора)")
                print(" - ram (использование памяти)")
                print(" - диск (дисковая активность)")
                print(" - hardware (полный отчет)")
                print(" - выключи (завершить процесс)")
                print(" - exit (выход)\n")
                continue
                
            if not user_input:
                continue
                
            result = system.execute(user_input)
            if result:
                print(result)
                
        except KeyboardInterrupt:
            print("\nЗавершение работы...")
            break

if __name__ == "__main__":
    main()
