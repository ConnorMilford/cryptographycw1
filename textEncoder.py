code = {'A':1, 'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25, 'Z':26,' ':27}
letter = {0:' ',1:'A', 2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',27:' '}


def encode_text (s : str):
    result = 0
    power  = 1
    for i in range(0, len(s)):
        result += code[s[i]] * power
        power  *= 28
    return result


def decode_number (x):
    remaining = x
    result = ''
    while (remaining > 0):
        result =  result + letter[(remaining % 28)]
        remaining = (remaining - (remaining % 28))//28
    return result