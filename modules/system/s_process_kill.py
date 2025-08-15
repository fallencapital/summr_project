import psutil

class SoftProcessKiller:
    
    @staticmethod
    def kill_process(identifier):
        try:
            if isinstance(identifier, int) or str(identifier).isdigit():
                psutil.Process(int(identifier)).terminate()
                return True
            
            killed = False
            for proc in psutil.process_iter(['pid', 'name']):
                if str(identifier).lower() in proc.info['name'].lower():
                    proc.terminate()
                    killed = True
            return killed
        
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return False
