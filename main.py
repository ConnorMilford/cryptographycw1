from problem5 import Problem5

def main():
    p5 = Problem5()
    
    p5.openFile("parameters.txt")
    p5.openFile("problem-5-data.txt")

    CIPHERTEXT = p5.computeCipherText()
    
    print("CIPHERTEXT = ", CIPHERTEXT)
    print("DECODED CIPHERTEXT = ", p5.decodeCipherText(CIPHERTEXT))


if __name__ == "__main__":
    main()    