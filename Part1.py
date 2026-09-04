Part 1 

String1 = 'John Doe, 999-99-9999, 2-23-2003: 19.8973' #stores info

colon_pos = String1.find(':') #
extracted = String1[colon_pos + 1:].strip() #takes everything after :
number = float(extracted) #converts the number 19.8973 from string into a floating point number 

print number 
