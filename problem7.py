from textEncoder import decode_number, encode_text
from sympy import *

class Problem7:
        
    def __init__(self):
        
        self.params = {}
        
    
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
                
    def printParams(self):
        print(self.params)
        
        
    def calculateSharedSecret(self, alicesPrivateK):
        a = int(self.params['A']) #alices public
        prime = int(self.params['p'])
        return pow(a, alicesPrivateK, prime)
    
    
    def decrypt(self, secret):
        #message = c * inverseMod(secret) % p 
        cipherText = int(self.params['c'])
        prime = int(self.params['p'])
        inverseSecret = pow(secret, -1, prime)
        return cipherText * inverseSecret % prime
    
    def decode(self, decryptedNum):
        return decode_number(decryptedNum)
    
    def isSafePrime(self):
        p = int(self.params['p'])

        # Check if p is a safe prime (i.e., (p-1)/2 is also prime)
        q = (p - 1) // 2
        is_q_prime = isprime(q)

        # Factorize p - 1 to check smoothness
        factors = factorint(p - 1)

        # Output results
        return is_q_prime, factors
    
    def attemptKeyCalculation(self):
        c = int(self.params['c'])
        prime = int(self.params['p'])
        m1 = encode_text("BUY")
        m2 = encode_text("SELL")
        
        inverseM1 = pow(m1, -1, prime)
        inverseM2 = pow(m2, -1, prime)
        
        k1 = (inverseM1 * c) % prime
        k2 = (inverseM2 * c) % prime 
        return self.decryptWithKey(k1, k2, prime, c)
    
    def decryptWithKey(self, key1, key2, prime, c):
        A = int(self.params['A'])
        B = int(self.params['B'])
        invKey1 = pow(key1, -1, prime)
        invKey2 = pow(key2, -1, prime)
        
        m1 = (c * invKey1) % prime
        m2 = (c * invKey2) % prime
        
        print(f"Message 1: {m1}\n Key: {key1} \n")
        print(f"Message 2: {m2}\n Key: {key2}\n")
        self.compareKeys(key1, key2)
        
        
        

    def compareKeys(self, k1, k2):
        prime = int(self.params['p'])
        prob6Key = 64610768241945442473143647736286110811847728909995772183738878377682089709097566206433901206319502494043575455252252976340509074260675580359196833993207830840896191774107675852779742890012625377417435047520552248400328130230055319489435848498734961570069904551701970046350312851530717108998008147935082402458085686016556848870159513008050408159367430405049586018575916332567183108406569547622750697445670239098770329674536754453772458036632380203270288809384722735992920521114816891875580612873134895115998815314963688078482617937340866433410654948739885257161265409496206504223951505256276848559642083407533152415346
        
        if (k1 - prob6Key) % prime == 0:
            print("K1 candidate matches K6 modulo p")
        if (k2 - prob6Key) % prime == 0:
            print("K2 candidate matches K6 modulo p")
        else:
            print("neither candidates match")    

        

            

                    
                
                
            