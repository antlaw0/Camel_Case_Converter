#Camel case converter
#ask user for a string
text = input("Enter text to convert: ")
#initialize some counters
i=0
spaceCounter=0
convertedString=""
firstLetter=True

#loop through string adding letters as necessary
while(i<len(text)):
	if text[i] != ' ': #if index is not a space
		if spaceCounter != 0: #if first letter
			convertedString+=text[i].lower()
			
		else:
			convertedString+=text[i].upper()
		spaceCounter+=1
	else:
		spaceCounter=0 #reset spaceCounter because encountered a space
	
	i+=1 #advance index counter

#get first leter of convertedString
c=convertedString[0]
c=c.lower() #convert first letter to lower case
convertedString=convertedString[1:] #remove first letter from convertedString
convertedString=c+convertedString #add first letter back to string
#print convertedString

print(convertedString)
