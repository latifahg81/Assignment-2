filename = input() #enter file name 

if len(filename) < 1: #checks if anything was typed 
    filename = "mbox.short.txt" #file name 

try: 
    new_file = open(filename) #opens the file
    upper_file = open("mbox-upper-case.txt", "w")
    umich_file = open("mbox-umich.txt", "w")

    count = 0 #email counter, umich.edu email = +1 

    for line ine new_file: #goes through the file 
        upper_file.write(line.upper()) #changes to uppercase and writes it into the mbox-upper-case file


        words = line.split() #splitting up the lines 

        for word in words: 
            if word.endswith("umich.edu") #checks if emails end with umich.edu, then writes into new file and starts a new line each time 

            umich_file.write(word + "\n")
            count = count + 1 #counts the emails

    print("Number of umich.edu emails:", count) #print the statment and then total number of emails found
    
execpt:
    print("File not found") #just in case file can't be opened/not found
