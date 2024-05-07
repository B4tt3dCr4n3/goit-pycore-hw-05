'''
Task 3. Write a script that reads a log file and displays the number of logs
for each log level (INFO, DEBUG, ERROR, WARNING). The script should also allow
filtering logs by log level and displaying log details for the selected level.
'''

def parse_log_line(line: str) -> dict:
    """Parse a log line and return a dictionary with log details."""
    parts = line.split(' ', maxsplit=3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    """Load logs from a file."""
    logs = []
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError as e:
        print(f"An error occurred while reading a file: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by log level."""
    filtered_logs = [log for log in logs if log['level'] == level]
    return filtered_logs

def count_logs_by_level(logs: list) -> dict:
    """Calculate the number of logs for each log level."""
    log_counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0}
    for log in logs:
        level = log['level']
        if level in log_counts:
            log_counts[level] += 1
    return log_counts

def display_log_counts(counts: dict):
    """Displays the calculation results in a readable form."""
    print("Log level | Quantity")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main(file_path: str, log_level: str = None):
    """Main function to display log counts and details."""
    logs = load_logs(file_path)
    if logs:
        if log_level:
            filtered_logs = filter_logs_by_level(logs, log_level.upper())
            display_log_counts(count_logs_by_level(logs))
            print(f"\nLog details for the level '{log_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            display_log_counts(count_logs_by_level(logs))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [log_level]")
        sys.exit(1)
    FILE_PATH = sys.argv[1]
    LOG_LEVEL = sys.argv[2] if len(sys.argv) == 3 else None
    main(FILE_PATH, LOG_LEVEL)
