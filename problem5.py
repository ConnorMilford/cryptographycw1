import textEncoder

class Problem5:

    def __init__(self):
        self.params = {}

    def printFile(self, file):
        self.openFile(file)
        print("Params ", self.params)
    
    #Opens file and reads into dict.
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

    # Computes shared secret
    # B^A % prime = Secret 
    def computeSharedSecret(self, publicB, privateA, primeNum):
        return pow(publicB, privateA, primeNum)
    

    #Returns encrypted cipherText 
    def encryptMessage(self):
        a = int(self.params['a'])  
        b = int(self.params['B']) 
        p = int(self.params['p']) 
        g = int(self.params['g']) 
        plaintext = self.params['plaintext']

        return (textEncoder.encode_text(plaintext) * self.computeSharedSecret(b, a, p)) % p
    
    # Use inverse modulo to decrypt
    def decryptCipherText(self, cipherText):
        a = int(self.params['a'])  
        b = int(self.params['B']) 
        p = int(self.params['p']) 
        

        invS = pow(self.computeSharedSecret(b, a, p), -1, p)
        return (cipherText * invS) % p

    #Decodes and decrpyts ciphertext
    def decodeAndDecryptCipherText(self, cipherText):
        return textEncoder.decode_number(self.decryptCipherText(cipherText))


    




