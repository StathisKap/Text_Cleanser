def Read_File(name):
    try:
        file = open(name, "rt", encoding="ISO-8859-1")
        return file
    except:
        print("Error: Couldn't open file")
        exit(1)

def Capitilise(string):
    sentences = string.split(".")
    for i in range(len(sentences)):
        if i == len(sentences) - 1:
            break
        sentences[i] = sentences[i].strip()
        if sentences[i][0].isalpha():
            sentences[i] = sentences[i][0].upper() + sentences[i][1:]
    
    return ".".join(sentences)

def Space(string):
    for i in range(len(string)):
        if string[i] == ".":
            string = string[:i+1] +  " " * 2 + string[i+1:]
        elif string[i] == ",":
            string = string[:i+1] + " " + string[i+1:]
    return string

def Replace(string):
    return string.translate({ ord(";") : ord(".")})

def Remove_Dupes(string):
    for i in range(len(string)):
        if i+1 == len(string):
            break
        if string[i] == "." and string[i+1] == ".":
            string = string[:i] + string[i+1:]
    return string

def Lookup_List(string):
    name_list = ["Jill", "Jack"]

    for name in name_list:
        start = 0
        end = len(string) - 1
        while True:
            if string.lower().find(name.lower(), start, end) != -1:
                index = string.lower().find(name.lower(), start, end)
                string = string[:index] + name +  string[index + len(name):]
                start += index + len(name)
                end -= index + len(name)
            else:
               break 
    return string


        

file = Read_File("../Text Sample 1.txt") # Opening the text file
content = file.read() # Reading the file
content_processed = content
content_processed = Replace(content_processed)
content_processed = Remove_Dupes(content_processed)
content_processed = Capitilise(content_processed)
content_processed = Space(content_processed)
content_processed = Lookup_List(content_processed)

print(content_processed)

outfile = open("./Corrected Text Sample 1.txt", "wt") # Opening an output text file
outfile.write(content_processed) # Writting to it