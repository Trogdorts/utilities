import logging
import os
from logging.handlers import RotatingFileHandler

class CustomLogger(logging.Logger):
    def __init__(self, name=None, main_dir=None, lf_enabled=True, lc_enabled=True, log_level=logging.INFO, debugging=False, logging_module=logging):
        super().__init__(name)
        self.log_level = logging_module.DEBUG if debugging else log_level
        self.setLevel(self.log_level)
        self.log_format = logging_module.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if not name:
            # Get the name of the calling script/module
            frame = logging.currentframe()
            caller_globals = frame.f_back.f_globals
            name = os.path.splitext(os.path.basename(caller_globals['__file__']))[0]
            del frame

        if not main_dir:
            # Get the main directory of the calling script
            frame = logging.currentframe()
            main_dir = os.path.dirname(frame.f_back.f_globals['__file__'])
            del frame

        if lf_enabled:
            # setup logfile
            log_dir = os.path.join(main_dir, 'logs')
            os.makedirs(log_dir, exist_ok=True)
            log_file = os.path.join(log_dir, f'{name}.log')
            loggerfile = RotatingFileHandler(
                log_file,
                maxBytes=5000000,
                backupCount=5,
                encoding='utf-8'  # Set UTF-8 encoding for the log file
            )
            loggerfile.setLevel(self.log_level)
            loggerfile.set_name('FileHandler')
            loggerfile.setFormatter(self.log_format)
            self.addHandler(loggerfile)

        if lc_enabled:
            # setup console log
            loggerconsole = logging.StreamHandler()
            loggerconsole.setLevel(self.log_level)
            loggerconsole.set_name('StreamHandler')
            loggerconsole.setFormatter(self.log_format)
            self.addHandler(loggerconsole)

    def set_log_level(self, log_level_str):
        log_level = getattr(logging, log_level_str.upper(), None)
        if log_level is None:
            raise ValueError(f"Invalid log level: {log_level_str}")

        self.log_level = log_level
        for handler in self.handlers:
            handler.setLevel(log_level)

        print(f"Log level updated to: {log_level_str}")


