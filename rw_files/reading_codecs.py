# Example reading file by codecs

# Encoders and Decoders
import codecs
# Open File by codecs
# params: directory file, mode, encode
# return object
file = codecs.open("./rw_files/test_file.txt", "r", encoding="utf-8")
print file

# using read function to read all lines
# return string
# print file.read()

# using readlines function to read all lines
# return array
for line in file.readlines():
    print line.encode("utf-8")