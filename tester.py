import subprocess
import os
import numpy as np
from numpy import random
INPUT_FILE="/home/dixit/Desktop/contest/input.txt"
def generate_test():

    #  x = random.randint(100)   : random int between 0 and 100
    # x=random.randint(100, size=(10))   : random array of size 10 between 0 and 100 , very useful
    # x = random.randint(100, size=(3, 5)) : random 2-d matrix
    # x = random.rand()  returns a random float between 0 and 1.
    # x = random.choice([3, 5, 7, 9])  returns  : a random value from specified array
    # write your code below #
    n=8
    test_case=str(n)+ "\n"
    line=""
    a=random.randint(10,size=(n))
    for i in range(n):
        line+=str(a[i])
        line+=' '
    test_case+=line
    test_case+='\n'
    print(test_case)
    Input=open(INPUT_FILE,'w')
    Input.write(test_case)
    Input.close()

def run(file1):
   cwd = "g++ " + file1 + " -o out2;./out2"
   Input=open(INPUT_FILE,'r')
   s = subprocess.check_output(cwd, stdin=Input,shell=True)
   return s.decode("utf-8")

def checker(file1,file2):
    for i in range(1000):
        generate_test()
        output1=run(file1)
        output2=run(file2)
        if output1 != output2:
            print("Your Code fails on Test case : \n")
            Input=open(INPUT_FILE,"r")
            print(Input.read())
            print()
            print("Correct output : ")
            print(output1)
            print("Your output : ")
            print(output2)
            print("Enjoy Debugging!!")
            return
    print("Not able to find mistake :(")
    return
if __name__ == "__main__":


    # generate_test()
    
    # correct code
    file1="/home/dixit/Desktop/contest/naive.cpp"
    # incorrect code
    #  file2=""
    file2="/home/dixit/Desktop/contest/1.cpp"
    checker(file1,file2)