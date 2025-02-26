from problem5 import Problem5
from problem6 import Problem6

def runProblem5():
    p5 = Problem5()
    
    p5.openFile("parameters.txt")
    p5.openFile("problem-5-data.txt")

    CIPHERTEXT = p5.computeCipherText()
    
    print("CIPHERTEXT = ", CIPHERTEXT)
    print("DECODED CIPHERTEXT = ", p5.decodeCipherText(CIPHERTEXT))


def runProblem6():
    p6 = Problem6()
    p6.openFile("parameters.txt")
    p6.openFile("problem-6-data.txt")
    p6.printParams()



def main():
    #runProblem5()
    runProblem6()


if __name__ == "__main__":
    main()    