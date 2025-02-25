import textEncoder

class Problem5:

    def __init__(self):
        self.params = {}

    def printFile(self, file):
        self.openFile(file)
        print("Params ", self.params)
    
    def openFile(self, file):
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                key, value = line.strip().split("=")
                key = key.strip()
                value = value.strip()

                if key.lower() == "plaintext":
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1].strip()

                self.params[key] = value 


    

    def computeSecret(self, publicB, privateA, primeNum):
        return pow(publicB, privateA, primeNum)
    
    def computeCipherText(self):
        a = int(self.params['a']) # private 
        b = int(self.params['B']) # public
        p = int(self.params['p']) #prime num
        g = int(self.params['g']) # 
        plaintext = self.params['plaintext']


        return (textEncoder.encode_text(plaintext) * self.computeSecret(b, a, p)) % p
    

    def decryptCipherText(self, cipherText):
        a = int(self.params['a'])  
        b = int(self.params['B']) 
        p = int(self.params['p']) 
        

        invS = pow(self.computeSecret(b, a, p), -1, p)
        return (cipherText * invS) % p

    def decodeCipherText(self, cipherText):
        textEncoder.decode_number(self.decryptCipherText(cipherText))


    




