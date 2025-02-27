from problem5 import Problem5
from problem6 import Problem6
from textEncoder import decode_number, encode_text

def runProblem5():
    p5 = Problem5()
    
    p5.openFile("parameters.txt")
    p5.openFile("problem-5-data.txt")

    CIPHERTEXT = p5.encryptMessage()
    
    print("CIPHERTEXT = ", CIPHERTEXT)
    print("DECODED CIPHERTEXT = ", p5.decodeAndDecryptCipherText(CIPHERTEXT))


def runProblem6():
    p6 = Problem6()
    p6.openFile("parameters.txt")
    p6.openFile("problem-6-data.txt")
    p6.bruteForceMessage()

def test():
    str = "The cat went to the market"
    p6 = Problem6()
    enc = encode_text(str)
    p6.computeKey()  

def main():
    #runProblem5()
    #runProblem6()
    runProblem6()


if __name__ == "__main__":
    main()    