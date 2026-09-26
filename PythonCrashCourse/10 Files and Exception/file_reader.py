from pathlib import Path

path = Path('pi_digits.txt')

contents = path.read_text()

contents = contents.rstrip()
contents = contents.lstrip()

# print(contents)

lines = contents.splitlines()
pi_string = ''
for line in lines :
    pi_string += line.lstrip().rstrip()
    # print (line)

print(pi_string)
print(len(pi_string))