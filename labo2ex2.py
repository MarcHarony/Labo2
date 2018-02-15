import re
path ='coconut.txt'
pattern = r'-?\d+'
p = re.compile(pattern)
try :
    with open(path,'r') as file :
        i = 1
        for line in file :
            content = p.findall(line)
            if len(content) != 0 :
                n=0
                stringue =""
                while n<len(content) :
                    if n == len(content)-1 :
                        stringue += str(content[n])
                    else :
                        stringue += str(content[n] + ", ")
                    n += 1
                print("line " + str(i) + " : " + stringue)
            i+= 1
        file.close()
except IOError :
    pass
except FileNotFoundError :
    pass
