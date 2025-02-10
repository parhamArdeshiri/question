from os import listdir, mkdir, path

class Reader:
    def __init__(self, file):
        if "cache" not in listdir():
            mkdir("./cache")
        
        if "save.txt" not in listdir("./cache"):
            with open(f"{path.abspath("cache")}/save.txt", "x")as f:

                f.write(file.read())
        
        else:
            with open(f"{path.abspath("cache")}/save.txt", "w")as f:

                f.write(file.read())

        ##ic(self.__getFileData())
        #self.__nums = list("0123456789")
        self.__asciis = list("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
        self.__symbols = ["~", "!", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", ",", ".", "<", ">", "/", "?", " ", "'", '"']
    
    def __getFileData(self):
        with open("./cache/save.txt")as f:
            return f.read().split()
    
    @property
    def justAscii(self):
        output = []
        stat = False

        for element in self.__getFileData():
            ##ic(element)
            ##ic(list(element))
            for char in list(element):
                ##ic(char)
                if char in self.__asciis:
                    stat = True
                else:
                    stat = False
                    break
                ##ic(char in self.__symbols and char in self.__nums)
                ##ic(stat)
            if stat:
                output.append(element)
        
        return output
    
    @property
    def justNum(self):
        output = []
        

        for element in self.__getFileData():
            try:
                int(element)
                output.append(element)
            except:
                pass # continue
        
        return output
    
    @property
    def justSymbol(self):
        output = []
        stat = False

        for element in self.__getFileData():
            ##ic(element)
            ##ic(list(element))
            for char in list(element):
                ##ic(char)
                if char in self.__symbols:
                    stat = True
                else:
                    stat = False
                    break
                ##ic(char in self.__symbols and char in self.__nums)
                ##ic(stat)
            if stat:
                output.append(element)
        
        return output
    
    @property
    def asciiAndNum(self):
        
        output = self.__getFileData()
        asciis = self.justAscii
        nums = self.justNum
        symbols = self.justSymbol

        ##ic(output)

        for element in asciis:
            output.remove(element)

        ##ic(output)

        for element in nums:
            output.remove(element)

        ##ic(output)

        for element in symbols:
            output.remove(element)

        ##ic(output)

        for i in range(11):
            for element in output:
                ##ic(element)
                for char in list(element):
                    if char in self.__symbols:        
                        try:
                            output.remove(element)
                        except:
                                pass
                        

        ##ic(output)

        return output
    
    @property
    def symbolAndNum(self):
        
        output = self.__getFileData()
        asciis = self.justAscii
        nums = self.justNum
        symbols = self.justSymbol
        an = self.asciiAndNum

        #ic(self.__getFileData())

        for element in asciis:
            output.remove(element)

        #ic(output)

        for element in nums:
            output.remove(element)

        #ic(output)

        for element in symbols:
            output.remove(element)

        #ic(output)

        for element in an:
            output.remove(element)

        #ic(output)

        for i in range(11):
            for element in output:
                #ic(element)
                for char in list(element):
                    if char in self.__asciis:
                        try:
                            output.remove(element)
                        except:
                                pass
                        
        ##ic(output)

        """for element in output:
                #ic(element)
                for char in [",", "'", "]"]
                    element.replace("")"""
        return output
    
    @property
    def asciiAndSymbol(self):
        output = self.__getFileData()
        asciis = self.justAscii
        nums = self.justNum
        symbols = self.justSymbol
        an = self.asciiAndNum

        #ic(self.__getFileData())

        for element in asciis:
            output.remove(element)

        #ic(output)

        for element in nums:
            output.remove(element)

        #ic(output)

        for element in symbols:
            output.remove(element)

        #ic(output)

        for element in an:
            output.remove(element)

        #ic(output)

        for i in range(11):
            for element in output:
                #ic(element)
                for char in list(element):
                    if char in list("0123456789"):                        
                        try:
                            output.remove(element)
                        except:
                                pass

        return output
    
    @property
    def all(self):

        output = self.__getFileData()

        for eachGroup in [self.justAscii, self.justNum, self.justSymbol, self.asciiAndNum, self.symbolAndNum, self.asciiAndSymbol]:
            for eachElement in eachGroup:
                output.remove(eachElement)

        return output

    def __str__(self):
        return f"Just asciis: {self.justAscii}\nJust numbers: {self.justNum}\nJust symbols: {self.justSymbol}\nBoth asciis and numbers: {self.asciiAndNum}\nBoth symbols and numbers: {self.symbolAndNum}\nBoth ascii and symbols: {self.asciiAndSymbol}\nAll: {self.all}"