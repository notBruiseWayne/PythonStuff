#! python3
import re
import pyperclip

# Regex for phone number
phoneRegex = re.compile(r'''(
    ((\d{4})|(\+\d{2}(-|\s)?\d{3}))# matches 0000 and +00-000 and +00 000 and +00000
    (-|\s)?# seprator - or space or none
    (\d{7})# matches 7 digits of a phone number
)
''', re.VERBOSE)

# Regex for email
emailRegex = re.compile('''(
[a-zA-Z0-9/+-_.]+           # letters both upper and lower case numbers and special characters i.e -+_.
@                           # @ symbol
[a-zA-Z0-9.-]+              # domain name letters numbers and . and -
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

# Input string from clipboard
message = str(pyperclip.paste())
# store the numbers in a list
extractedPhoneNumbers = phoneRegex.findall(message)
extractedEmails = emailRegex.findall(message)
phonedData = []
emailData=[]
for item in extractedPhoneNumbers:
    phonedData.append(item[0])
for item in extractedEmails:
        emailData.append(item[0])
# emailData=[]
# for item in emailRegex.findall(message):
# emailData.append(item[0])
# output the string VIA clipboard
outPut = '\n'.join(phonedData) + '\n'+'\n'.join(emailData)
print('Data copied from clipboard! \n Phone numbers and emails extracted! Ctrl+V in a word processor')
pyperclip.copy(outPut)
