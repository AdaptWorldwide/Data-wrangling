import re

list = []

print ("Insert Keywords Below. (Press Enter Twice when Finished)")
while True:
    word = input()
    if word == "":
        break
    else:
        list.append(word)

result = 0

countkeywords = len(list)

for i in list:
    match  = re.search(r'^[A-Z]',i)
    if match is not None:
        match = 'Capital'
        print(str(i)+','+str(match))
        result = result + 1
        
    else:
        print(str(i) + ',' + str(match))

        
print('There are '+str(countkeywords) +" keywords being checked and there are " + str(result) + " keywords with captialisation")

