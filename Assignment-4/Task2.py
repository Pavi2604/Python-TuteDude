# file_write_append.py
# This program writes and appends data to a file, then reads and displays its content

# Taking user input
data = input("Enter text to write to the file: ")

# Writing data to the file
with open("output.txt", "w") as file:
    file.write(data + "\n")
print("Data successfully written to output.txt.")

# Appending additional data
append_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_data + "\n")
print("Data successfully appended.")

# Reading and displaying the final content
print("\nFinal content of the file:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())