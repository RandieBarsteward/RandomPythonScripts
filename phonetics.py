import types
import string

letters = list(string.ascii_letters)
phonetics = ['Alpha', 'Bravo','Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliet', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

#dictionary = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}

natophonetic = zip(letters,phonetics)
dictionary = dict(natophonetic)
print(dictionary)

print(letters)
input = input("Insert text here: ")

for i in input:
    #print (str.upper(i)) #converts to upper case
    i = (str.lower(i)) #converts to lower case
    if i in letters: #checks if letter and prints if found
        print("%s" %  dictionary.get(i))
    else:
        print("\n")
