# utils.py
import datetime

def log_event(message, logfile="log.txt"):
    timestamp = datetime.datetime.now().strftime("[%H:%M:%S]")
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {message}\n")
