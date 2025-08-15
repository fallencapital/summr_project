class Core:
    def __init__(self):
        self._commands = {}
    
    def register_command(self, name, handler):
        if not callable(handler):
            return f"Ошибка: '{name}' не является вызываемым объектом"
        
        self._commands[name] = handler
        return f"Команда '{name}' успешно зарегистрирована"
        
    def execute(self, command_name):
        handler = self._commands.get(command_name)
        if handler is None:
            return f"Неизвестная команда: {command_name}"
        
        try:
            return handler()
        except TypeError:
            return f"Ошибка выполнения: обработчик команды '{command_name}' вызван неверно"
        except Exception as e:
            return f"Ошибка выполнения: {str(e)}"
