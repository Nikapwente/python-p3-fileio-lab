def write_file(file_name, file_content):
    # Add ".txt" extension to the file_name
    file_name_with_extension = f"{file_name}.txt"
    
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    pass
    # Add ".txt" extension to the file_name
    file_name_with_extension = f"{file_name}.txt"
    
    with open(file_name_with_extension, 'a') as file:
        file.write(f"{append_content}")

def read_file(file_name):
    pass
    # Add ".txt" extension to the file_name
    file_name_with_extension = f"{file_name}.txt"
    
    try:
        with open(file_name_with_extension, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"File {file_name_with_extension} not found."
    

# Testing
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

log_content = read_file(file_name="logfile")
print(log_content)
