from problem5 import Problem5
from problem6 import Problem6
from problem7 import Problem7
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

def runProblem7():
    p7 = Problem7()
    p7.openFile("parameters.txt")
    p7.openFile("problem-7-data.txt")
    print(p7.findSharedSecret())

def main():
    runProblem7()


if __name__ == "__main__":
    main()    