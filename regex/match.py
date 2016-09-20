# coding=utf-8
# The match function

import re

text = "<pattern>Qual seu nome?</pattern>"

# Using match function
# params: pattern, string, flags (op)
match_result = re.match(r'<pattern>(.*)</pattern>', text)

if match_result:
    print match_result.group()
    print match_result.group(1)
else:
    print "No Match!"
