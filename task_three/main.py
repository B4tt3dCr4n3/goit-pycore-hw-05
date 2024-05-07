'''
Task 3. Write a script that reads a log file and displays the number of logs
for each log level (INFO, DEBUG, ERROR, WARNING). The script should also allow
filtering logs by log level and displaying log details for the selected level.
'''

def parse_log_line(line: str) -> dict:
    """Parse a log line and return a dictionary with log details."""
    parts = line.split(' ', maxsplit=3) # Split the line into parts
    return { 
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    } # Return a dictionary with log details

def load_logs(file_path: str) -> list:
    """Load logs from a file."""
    logs = [] # List to store logs
    try: # Try to open the file
        with open(file_path, 'r', encoding='UTF-8') as file: # Open the file
            for line in file: # Iterate over the lines in the file
                logs.append(parse_log_line(line)) # Parse the line and add the log to the list
    except FileNotFoundError: # Handle file not found errors 
        print(f"File '{file_path}' not found.") # Print an error message
    except IOError as e: # Handle I/O errors
        print(f"An error occurred while reading a file: {e}") # Print an error message
    return logs # Return the list of logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filter logs by log level."""
    filtered_logs = [log for log in logs if log['level'] == level] # Filter logs by level
    return filtered_logs # Return the filtered logs

def count_logs_by_level(logs: list) -> dict:
    """Calculate the number of logs for each log level."""
    log_counts = {'INFO': 0, 'DEBUG': 0, 'ERROR': 0, 'WARNING': 0} # Dictionary to store log counts
    for log in logs: # Iterate over the logs
        level = log['level'] # Get the log level
        if level in log_counts: # Check if the log level is in the dictionary
            log_counts[level] += 1 # Increment the log count
    return log_counts # Return the log counts

def display_log_counts(counts: dict):
    """Displays the calculation results in a readable form."""
    print("Log level | Quantity") # Print the header
    print("-----------------|----------") # Print the separator
    for level, count in counts.items(): # Iterate over the log counts
        print(f"{level:<16} | {count}") # Print the log level and count

def main(file_path: str, log_level: str = None):
    """Main function to display log counts and details."""
    logs = load_logs(file_path) # Load logs from the file
    if logs: # If logs were loaded successfully
        if log_level: # If a log level is specified
            filtered_logs = filter_logs_by_level(logs, log_level.upper()) # Filter logs by level
            display_log_counts(count_logs_by_level(logs)) # Display log counts
            print(f"\nLog details for the level '{log_level.upper()}':") # Print the log level
            for log in filtered_logs: # Iterate over the filtered logs
                print(f"{log['date']} {log['time']} - {log['message']}")
        else: # If no log level is specified
            display_log_counts(count_logs_by_level(logs)) # Display log counts

if __name__ == "__main__": # Run the script if it is executed directly
    import sys # Import the sys module
    if len(sys.argv) < 2: # Check if the number of arguments is less than 2
        print("Usage: python main.py /path/to/logfile.log [log_level]") # Print usage information
        sys.exit(1) # Exit the program with an error code
    FILE_PATH = sys.argv[1] # Get the file path from the command-line arguments
    LOG_LEVEL = sys.argv[2] if len(sys.argv) == 3 else None # Get the log level if specified
    main(FILE_PATH, LOG_LEVEL) # Run the main function with the file path and log level
