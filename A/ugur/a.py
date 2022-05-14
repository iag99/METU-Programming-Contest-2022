import re

N = input()
text = input()

print("---")
print( re.sub("\(.*\)", "...", text) )
