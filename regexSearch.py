#! /usr/bin/env python3
# regexSearch.py - opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression.

import os, re
path = input('Enter path:')
if path == '':
    allFiles = os.listdir()
else:
    os.chdir(path)
    allFiles = os.listdir(path)
txtRegex = re.compile(r'(\.txt)$')
foundFiles = []
for file in allFiles:
    mo = txtRegex.search(file)
    if mo != None:
        foundFiles.append(file)
usrRegex = re.compile(input('Enter regular expression:'))
for txtFile in foundFiles:
    currentTxt = open(txtFile)
    content = currentTxt.readlines()
    for line in content:
        mo = usrRegex.search(line)
        if mo != None:
            print('Found in {}: {}'.format(txtFile, line))
    currentTxt.close()
