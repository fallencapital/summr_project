import sys
from pathlib import Path

current_file = Path(__file__).resolve()
invincible = current_file.parent.parent.parent
sys.path.insert(0, str(invincible))

from core.kernel import Core
from modules.system.hardware_monitor import HardwareMonitor
from modules.system.proc_monitor import ProcessMonitor
from modules.system.s_process_kill import SoftProcessKiller
from modules.system.h_process_kill import HardProcessKiller

class SystemCommands:
    @staticmethod
    def systemcommands():
        hmon = HardwareMonitor()
        pmon = ProcessMonitor()
        core = Core()
        sprockill = SoftProcessKiller()
        hprockill = HardProcessKiller()
        
        def full_report():
            report = []
            report.append("=== ПОЛНЫЙ ОТЧЕТ ===")
            
            methods = [
                ("Сеть", hmon.web_work),
                ("Диск", hmon.disk_work),
                ("CPU", hmon.cpu_work),
                ("RAM", hmon.ram_work)
            ]
            
            for name, method in methods:
                try:
                    result = method()
                    report.append(f"[{name}]\n{str(result)}")
                except:
                    report.append(f"[{name}]\n!ОШИБКА!")
            
            report.append("====================")
            return "\n".join(report)

        def killer():
            print("Как вы хотите завершить процесс: 9(SIGKILL) или 15(SIGTERM)?")
            choose = input(">>> ")
            
            if choose not in ("9", "15"):
                return "Неверный выбор сигнала"
            
            print("Введите name/PID процесса:")
            target = input(">>> ").strip()
            
            if not target:
                return "Пустой ввод"
            
            try:
                if choose == "9":
                    if target.isdigit():
                        return hprockill.kill_process(int(target))
                    return hprockill.kill_process(target)
                else:
                    if target.isdigit():
                        return sprockill.kill_process(int(target))
                    return sprockill.kill_process(target)
            except Exception as e:
                return f"Ошибка: {str(e)}"

        def help_command():
            return "Доступные команды: процессы, сеть, cpu, ram, диск, hardware, дай отчет по нагрузке на систему, выключи"

        core.register_command("help", help_command)
        core.register_command("помощь", help_command)
        core.register_command("процессы", pmon.own_htop)
        core.register_command("сеть", hmon.web_work)         
        core.register_command("cpu", hmon.cpu_work)
        core.register_command("ram", hmon.ram_work)
        core.register_command("диск", hmon.disk_work)
        core.register_command("hardware", full_report)
        core.register_command("дай отчет по нагрузке на систему", full_report)
        core.register_command("выключи", killer)

        return core
