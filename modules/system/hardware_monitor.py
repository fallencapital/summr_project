import psutil

class HardwareMonitor:
    def disk_work(self) -> dict:
        disk = psutil.disk_usage("/")
        return {
            "Название": "Дисковая память",
            "Всего": f"{disk.total / (1024**3):.1f} ГБ",
            "Свободно": f"{disk.free / (1024**3):.1f} ГБ",
            "Использовано": f"{disk.used / (1024**3):.1f} ГБ",
            "Заполнено": f"{disk.percent}%"
        }

    def cpu_work(self) -> dict:
        return {
            "Название": "Процессор",
            "Нагрузка": f"{psutil.cpu_percent(interval=1)}%",
            "Ядра": f"{psutil.cpu_count(logical=True)}",
            "Частота": f"{psutil.cpu_freq().current:.1f} МГц"
        }

    def ram_work(self) -> dict:
        ram = psutil.virtual_memory()
        return {
            "Название": "Оперативная память",
            "Использовано": f"{ram.used / (1024**3):.1f} ГБ",
            "Всего": f"{ram.total / (1024**3):.1f} ГБ",
            "Загрузка": f"{ram.percent}%"
        }

    def web_work(self) -> dict:
        net = psutil.net_io_counters()
        return {
            "Название": "Сетевая активность",
            "Отправлено": f"{net.bytes_sent / (1024**2):.1f} МБ",
            "Получено": f"{net.bytes_recv / (1024**2):.1f} МБ",
            "Активные подключения": len(psutil.net_connections())
        }

