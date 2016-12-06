import itertools
'''
Uses cartesian production to bulk concatenate keywords from seperate text files
Significantly faster than concatenating keywords using Excel
'''
#Leave this empty
Lists = []

#Specify text files containing the columns of keywords you want to concatenate
#Uncomment or add in extra lines should you want to concatenate more columns
LeftList = [line.rstrip('\n') for line in open(r'newrightlist.txt')]

RightList = [line.rstrip('\n') for line in open(r'leftlist2.txt')]

FarRightList = [line.rstrip('\n') for line in open(r'rightlist.txt')]

#Uncomment or add in lines with your lists created above
#This creates a list of lists which we use to concatenate the keywords
Lists.append(LeftList)
Lists.append(RightList)
Lists.append(FarRightList)

for element in itertools.product(*Lists):
    #This returns a tuple - unpack the tuple as below depending on how many lists
    #Remember to update the string formatting statement as well to print your unpacked tuples out
    a,b,c = element
    output = '{} {} {}\n'.format(a,b,c)
    with open('Output.csv','a',encoding='utf-8') as file:
        file.write(output)

