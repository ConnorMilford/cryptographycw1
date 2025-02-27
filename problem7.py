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
        
        
    def findSharedSecret(self):
        a = int(self.params['A'])
        b = int(self.params['B'])
        prime = int(self.params['c'])
        return pow(a, b, prime)    
                    
                
                
            