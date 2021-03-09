#! python3

import re, pyperclip

#TODO: create a regex object for phone numbers
phoneregex = re.compile(r'''
(
\d\d\d       #area code
\d\d\d        #first 3 digits
\d\d\d\d        #last 4 digits
(((ext(\.)?\s)|x)    #extension (optional)
(\d{2,5}))?       #extension (numbers optional)
)
''',re.VERBOSE)

#TODO: create a regex object for emails

emailregex = re.compile(r'''
# some.+_things@something.com
[a-zA-Z0-9_.+]+       #name part
@                     #@symbol
[a-zA-Z0-9_.+]+        #domain part


''', re.VERBOSE)

#TODO: get the text off clipboard
text = pyperclip.paste()

#TODO: extract email/phone number from this text
extractedemail = emailregex.findall(text)
extractedphone = phoneregex.findall(text)

allphonenumbers = []
for phonenumber in extractedphone:
    allphonenumbers.append(phonenumber[0])
    
#TODO: copy extracted email/number to clipboard
results = '\n'.join(allphonenumbers) + '\n' + '\n'.join(extractedemail)
pyperclip.copy(results)
