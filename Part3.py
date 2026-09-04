filename = input()

if len(filename) < 1: 
    filename = "Romeo-full.txt"

    words [] #create empty list --> store the unique words 

    for line in file: #read each line
        line_words = line.split() #break up lines into

        for word in line_words: #read each word by itself
            if word not in words: #checks if word is not in list
                words.append(word) #if not there, adds it 

    word_list = open("Shakespeare-Unique-Words-List.txt", "w")
    word_list.write(str(words)) #writes the list to file 
    word_list.close()

    word_tuple = open("Shakespeare-Unique-Words-Tuple.txt","w")
    word_tuple.write(str(tuple(words))) #turns list into tuple and write it to second file
    word.tuple.close() 

    except:
        print("File not found")
