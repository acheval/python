#!/bin/python3 

import re, pyperclip

# TODO: Create phone number regex

phone_regex = re.compile(
    r"""(
        (\d{3}|\(\d{3}\))?              #area code
        (\s|-|\.)?                      #separator
        (\d{3})                         #first 3 digits
        (\s|-|\.)?                      #separator
        (\d{4})                         #last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
        )""",
    re.VERBOSE,
)

# TODO: Create email regex

email_regex = re.compile(
    r"""(
        [a-zA-Z0-9._%+-]+               #username
        @                               #@ symbol
        [a-zA-Z0-9.-]+                  #domain name
        (\.[a-zA-Z])?                   #dot something
        )""",
    re.VERBOSE,
)

# TODO: Find matches in clipboard text

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_number = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phone_number += " x" + groups[8]
    matches.append(phone_number)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# TODO: copy results to clipboard

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard: ")
    print("\n".join(matches))
else:
    print("No phone number or email address found.")
