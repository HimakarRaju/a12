import re

pattern = f'hello'
string = "hello world"

if re.match(pattern, string):
    print("match found")
else:
    print("match not found")

# The findall() Function
text = "hello, I'm in India and in my home"
pattern = r"in"
matches = re.findall(pattern, text)
print(matches)

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# The search() Function

txt = "The rain in Spain"
x = re.search("s", txt)

print("The first white-space character is located in position:", x.start())
