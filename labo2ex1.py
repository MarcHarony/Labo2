import re
chaine = input("entrez une chaîne de caractère : ")
phone = r'\+[0-9]{2}\ [0-9]{3}\ [0-9]{2}\ [0-9]{2}\ [0-9]{2}'
number = r'-?\+?[1-9][0-9]*'
plaque = r'[1-9][0-9]{3}[A-Z]{3}|[1-9][A-Z]{3}[0-9]{3}'
volume = r'C\:\\.+'
p = re.compile(phone)
c = re.compile(number)
b = re.compile(plaque)
s = re.compile(volume)
print(s.match(chaine))
