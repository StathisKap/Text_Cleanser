class Cleanser:
    def __init__(self, file_name, output_file):
        self.file = self.Read_File(file_name)
        content_processed = self.file.read()
        content_processed = self.Replace(content_processed)
        content_processed = self.Remove_Dupes(content_processed)
        content_processed = self.Capitilise(content_processed)
        content_processed = self.Space(content_processed)
        content_processed = self.Lookup_List(content_processed)
        print(content_processed)
        outfile = open(output_file, "wt") # Opening an output text file
        outfile.write(content_processed) # Writting to it


    def Read_File(self, name):
        try:
            file = open(name, "rt", encoding="ISO-8859-1") # Open the file for reading, otherwise just exit
            return file
        except:
            print("Error: Couldn't open file")
            exit(1)

    def Capitilise(self, string):
        sentences = string.split(".")
        for i in range(len(sentences)):
            if i == len(sentences) - 1:
                break
            sentences[i] = sentences[i].strip()
            if sentences[i][0].isalpha():
                sentences[i] = sentences[i][0].upper() + sentences[i][1:]

        return ".".join(sentences)

    def Space(self, string):
        for i in range(len(string)):
            if string[i] == ".":
                string = string[:i+1] +  " " * 2 + string[i+1:]
            elif string[i] == ",":
                string = string[:i+1] + " " + string[i+1:]
        return string

    def Replace(self, string):
        return string.translate({ ord(";") : ord(".")})

    def Remove_Dupes(self, string):
        for i in range(len(string)):
            if i+1 == len(string):
                break
            if string[i] == "." and string[i+1] == ".":
                string = string[:i] + string[i+1:]
        return string

    def Lookup_List(self, string):
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


cleanser = Cleanser("../Text Sample 1.txt", "./Corrected Text Sample 1.txt")