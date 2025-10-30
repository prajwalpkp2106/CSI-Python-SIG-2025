# A file in Python is simply a named location on your computer where you can store data permanently — text, numbers, images, etc.

# Unlike variables (which store data temporarily in memory while the program runs),
# files store data even after the program ends.





# Mode	Description	       Pointer Position
# 'r'	Read	           Start of file
# 'w'	Write (overwrite)  Start of file
# 'a'	Append	           End of file
# 'r+'	Read & write	    Start of file
# 'wb'	Write binary	    Start of file
# 'rb'	Read binary	        Start of file
# 'ab'	Append binary	    End of file
# mode defines what operations (read/write/append) you can do and where the file pointer starts.


# # # Open a file in read mode
# f = open("example.txt", "r")

# # # Do operations
# content = f.read()
# print(content)

# # Close the file
# f.close()





# # # # Create and write something
with open("example.txt", "w") as f:
    f.write(
        "Learning Python is fun!\n"
        "File handling helps us store data permanently.\n"
        "We can read, write, and update files easily.\n"
        "Practice makes you perfect in Python."
    )



# # #  Reading Files

# # # Read Entire File
# with open("example.txt", "r") as f:
#     content = f.read()
#     print(content)

# # # Read Line by Line
# with open("example.txt", "r") as f:
#     line1 = f.readline()
#     line2=f.readline()  # reads first line
#     print(line1)
#     print(line2)
    
#     lines = f.readlines()  # reads remaining lines into list
#     print(lines)



# #If you want to print each line without newline issues, use:

# with open("example.txt", "r") as f:
#     for line in f:
#         print(line)    # removes '\n'






# # # Print first two lines:

# with open("example.txt", "r") as f:
#     for i in range(2):
#         print(f.readline())


# # # Print only specific line (say 3rd line):

# with open("example.txt", "r") as f:
#     lines = f.readlines()
#    # print(lines)
#     print(lines[2])  # line index starts from 0






# # Writing Files

# # Write Mode (w)
# with open("file.txt", "w") as f:
#     f.write("Hello Python\n")
#     f.write("File handling example")

# # # Note: 'w' overwrites the file if it exists.

# # # Append Mode (a)
# with open("file.txt", "a") as f:
#     f.write("\nAdding another  line")




# # 'r+' → Read & Write (text mode)
# # Opens file for both reading and writing.
# # r+ mode example
# with open("example.txt", "r+") as f:
#     content = f.read()              # Read existing content
#     print("Before:", content)
    
#     f.seek(0)                       # Move pointer to start
#     f.write("Updated first line") # Overwrites beginning







# # File Pointer / Seek

# # f.tell() → returns current pointer position
# # f.seek(pos) → moves pointer to pos

# with open("file.txt", "r") as f:
#     print(f.read(5))   # read first 5 chars
#     print(f.tell())    # 5
#     f.seek(3)
#     print(f.read(5))   # read first 5 chars again



# # Working with CSV Files(Comma Separated Values))
# A CSV file is a text file where each row represents a record and columns are separated by commas.
#import csv

# Writing CSV
# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "Branch"])
#     writer.writerow(["Kishor", 20, "CS"])

# # Reading CSV
# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)



# # Working with JSON Files((JavaScript Object Notation))

# import json

# data = {"name": "Kishor", "age": 20, "branch": "CS"}
# JSON keys must be strings

# Writing JSON
# with open("data.json", "w") as f:
#     json.dump(data, f)

# # Reading JSON
# with open("data.json", "r") as f:
#     info = json.load(f)
#     print(info)

# # Commonly used for APIs


# # # Checking File Existence
#import os

if os.path.exists("file3.txt"):
    print("File exists")
else:
    print("File does not exist")


# Deleting a File
import os

os.remove("file.txt")   # deletes file



