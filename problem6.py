class Problem6:

    def __init__(self):
        self.params = {}
        #Place holder till key is found
        self.key = 0 


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

    #m1 size 2^19 < m1 < 2^20
    #Allows brute force
    def bruteForceMessage(self):
        minSize = pow(2, 19)
        maxSize = pow(2, 20)
        

        for i in range(minSize, maxSize):    
            key = self.computeKey(i)
            
            if self.checkM2Candidate(self.decryptC2WithKey(key)):
                self.key = key
            


    #c1-ciphertext
    #p - prime
    # Key = c1 * (m1)^-1 % p
    def computeKey(self, m1):
        cipherText = int(self.params['c1'])
        prime = int(self.params['p'])
        #Inverse modulo of m1
        inverseModM1 = pow(m1, -1, prime)

        return (cipherText * inverseModM1) % prime
        
        
    
    def decryptC2WithKey(self, key):
        cipherText2 = int(self.params['c2'])
        prime = int(self.params['p'])
        inverseModKey = pow(key, -1, prime)

        return (cipherText2 * inverseModKey) % prime

    
    # returns boolean based on whether the string contains " THE " & " TO "
    def checkM2Candidate(self, string):
        if not isinstance(string, str):
            return False
        
        if (string.find(" THE ") + string.find(" TO ") > 0):
            return True
        else: 
            return False