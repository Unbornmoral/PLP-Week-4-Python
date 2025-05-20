
def modify_file_content(input_filename, output_filename):
    #Reads a file, modifies its content, and writes to a new file with error handling.
    try:
        # Open and read the input file
        with open(input_filename, 'r') as file:
            content = file.read()

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"File successfully modified and saved as {output_filename}")

    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except PermissionError:
        print("Error: Insufficient permissions to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for input and output filenames
input_file = input("Enter the name of the file to read: ")
output_file = input("Enter the name of the new file to write to: ")

# Run the function
modify_file_content(input_file, output_file)
