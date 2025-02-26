class Problem6:

    def __init__(self):
        self.params = {}


    def printParams(self):
        print(self.params)
    

    def openFile(self, file):
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                key, value = line.strip().split("=")
                key = key.strip()
                value = value.strip()

                self.params[key] = value 

    #Key of size 2^19 < k < 2^20
    #Allows brute force
    def bruteForceKey(self):
        return 0;