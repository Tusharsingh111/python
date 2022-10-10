import keyword
keys = ["class", "global", "finally", "not", "elif", "non", "break", "lambda", "def", "del"]

for i in range(len(keys)):
    if keyword.iskeyword(keys[i]):
        print(keys[i]+":True")
    else:
        print(keys[i]+":False")
        

