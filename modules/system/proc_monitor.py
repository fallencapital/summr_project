import psutil

class ProcessMonitor:
    @staticmethod
    def own_htop(top_n=5):
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu': proc.info['cpu_percent'],
                    'ram': proc.info['memory_percent']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, AttributeError):
                continue

        processes.sort(key=lambda p: p['cpu'], reverse=True)

        print("┌─────────┬──────────────────┬───────┬───────┐")
        print("│   PID   │      NAME        │  CPU% │  RAM% │")
        print("├─────────┼──────────────────┼───────┼───────┤")
        
        for proc in processes[:top_n]:
            pid = proc['pid']
            name = (proc['name'][:15] if proc['name'] else 'unknown').ljust(15)
            cpu = f"{proc['cpu']:5.1f}"
            ram = f"{proc['ram']:5.1f}"
            print(f"│{pid:7}  │  {name} │ {cpu}%│{ram}% │")

        print("└─────────┴──────────────────┴───────┴───────┘")

if __name__ == "__main__":
    ProcessMonitor.own_htop()
