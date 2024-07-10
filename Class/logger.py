import os
import datetime

class Logger:
    def __init__(self, base_log_path="/app/logs"):
        self.date_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.base_log_path = base_log_path
        self.log_files = {}
        self.general_log_path = os.path.join(self.base_log_path, "log", f"log-{self.date_str}.log")
        
        # Ensure the general log directory exists
        os.makedirs(os.path.dirname(self.general_log_path), exist_ok=True)
        self.log_files["log"] = self.general_log_path
    
    def get_log_file(self, log_type):
        if log_type not in self.log_files:
            log_directory = os.path.join(self.base_log_path, log_type)
            os.makedirs(log_directory, exist_ok=True)
            log_file_path = os.path.join(log_directory, f"{log_type}-{self.date_str}.log")
            self.log_files[log_type] = log_file_path
        return self.log_files[log_type]

    def log(self, log_type, message):
        timestamped_message = f"{datetime.datetime.now().isoformat()} - {message}\n"
        
        # Write to specific log file
        log_file_path = self.get_log_file(log_type)
        with open(log_file_path, 'a') as log_file:
            log_file.write(timestamped_message)
        
        # Write to general log file
        with open(self.general_log_path, 'a') as general_log:
            general_log.write(timestamped_message)

# # Utilisation de la classe Logger
# logger = Logger()

# # Exemple de logs
# logger.log("info", "Ceci est un message d'information.")
# logger.log("error", "Ceci est un message d'erreur.")
# logger.log("debug", "Ceci est un message de débogage.")
# logger.log("warning", "Ceci est un message d'avertissement.")
