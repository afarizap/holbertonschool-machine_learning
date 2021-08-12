# INSTALL BS4 WITH ´pip install beautifulsoup4´
from bs4 import BeautifulSoup
import glob

file_name = glob.glob("*.html")[0]
f = open(file_name, "r")
soup = BeautifulSoup(f, features="lxml")

file = soup.find_all('body')

## Create initial files
print("||||||||| Files ||||||||||")
new = set()
for b in file:
    ulList = b.find_all('li')
    for li in ulList:
        x = li.text.strip()
        if x[:5] == "File:":
            new.add(x[6:])
for _ in new:
    print("----------------------------------------")
    with open(_, 'w+') as y:
        if _[-2:] == "py":
            y.write('#!/usr/bin/env python3\n')
            y.write(f'""" {_[:-3]} task """')
    print(f"{_} file created with this content:")
    with open(_, 'r') as z:
        for line in z:
            print(f"{line}" , end="")
    print()
## Create README
print("----------------------------------------")
with open("README.md", 'w+') as f:
    f.write("Hello README")
## Create mains
print("||||||||| Mains ||||||||||")
for m in file:
    main = m.find_all('pre')
    for main_line in main:
        if "-main." in main_line.text.strip():
            x = main_line.text.strip().split('\n')
            title = x[0].split(' ')[-2] #se debe cambiar por un find(.py) | cambiar entre[-2] si tiene funciones nomas [-1] si tiene clases
            author = x[0][:5]
            c = 0
            code = ""
            for y in x:
                if y[:5] != author:
                    code += y + '\n'
                else:
                    c += 1
                if c == 2:
                    break
            print("----------------------------------------")
            with open(title, 'w+') as y:
                for i in code:
                    y.write(i)
            print(f"{title} file created with this content:")
            with open(title, 'r') as z:
                for line in z:
                    print(f"{line}" , end="")
