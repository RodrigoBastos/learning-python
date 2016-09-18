# Example reading file

# Open File
# Using open function
# Params: directory file, mode
# mode: r equal read file, w equal write file
file = open("./rw_files/test_file.txt", "r")

# File is object
print file

# Using read function to read all lines
# return string
#print file.read()

# Using readline function to read all lines
# return array
print file.readlines()
