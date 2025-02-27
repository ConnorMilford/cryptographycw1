from textEncoder import encode_text, decode_number
import math

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
                key, value = line.split("=")
                key = key.strip()
                value = value.strip()
                self.params[key] = value
                
    #m1 size 2^19 < m1 < 2^20
    #Allows brute force
    def bruteForceMessage(self):

        minSize = pow(2, 19)
        maxSize = pow(2, 20)

        for i in range(minSize, maxSize):
            if i % 1000 == 0:
                print(f"Checked {i-minSize} keys out of {maxSize-minSize}")
                
                
            key = self.computeKey(i)
            if key is None:
                continue

            m2_int = self.decryptC2WithKey(key)

            if m2_int is None:
                continue

            m2String = decode_number(m2_int)
            
            if self.checkM2Candidate(m2String):
                print(f"Candidate found - {m2String} at {i-minSize} \n")
                print(f"Key is {key}")       
                self.writeToFile(m2String)
                break
                
    
    #c1-ciphertext
    #p - prime
    # Key = c1 * (m1)^-1 % p
    def computeKey(self, m1):
        cipherText = int(self.params['c1'])
        prime = int(self.params['p'])
        #Inverse modulo of m1
        if math.gcd(m1, prime) != 1:
            return None
        inverseModM1 = pow(m1, -1, prime)
        return (cipherText * inverseModM1) % prime
        
    
    def decryptC2WithKey(self, key):
        cipherText2 = int(self.params['c2'])
        prime = int(self.params['p'])
        if math.gcd(key, prime) != 1:
            return None
        inverseModKey = pow(key, -1, prime)
        return (cipherText2 * inverseModKey) % prime
        
    
    # returns boolean based on whether the string contains " THE " & " TO "
    # UPDATED TO TESLA IN ORDER TO 
    def checkM2Candidate(self, string):     
        return " TESLA " in string.upper() 
    

    def writeToFile(self, string):
        with open("potentialMessages.txt", "a") as f:
            f.write(f"{string} \n\n")