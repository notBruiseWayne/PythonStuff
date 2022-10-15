import pprint
import pyperclip
print('Text copied from ClipBoard!')
a = str(pyperclip.paste())
s = '''{}'''.format(a)
count = {}
for character in s.upper():
    count.setdefault(character, 0)  # sets 0 value to a key(character) if it doesn't exist in the dictionary
    count[character] = count[character] + 1
print('Character : Number of times appeared')
pprint.pprint(count)  # pretty print module function sorts and prints the dictionary in a column like output
rjText = pprint.pformat(count)  # saves the putput of the pprint module in a variable

k = list(count.keys())
v = list(count.values())
maxValue = max(v)
characterMax = k[v.index(maxValue)]
print('Most used character: ' + characterMax + ', ' + ' used ' + str(maxValue) + ' times')
