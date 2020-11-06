"""The first three functions are just used for testing purposes for this assignment. You also saw them in the last programming problem set. list_strings gives a list of all strings of length n, string_to_nat and nat_to_string convert back and forth between binary strings and natural numbers."""

def list_strings(n):
    """lists all binary strings of length n, do not modify this function"""
    if n == 0:
        return [""]
    else:
        strings = []
        for b in list_strings(n-1):
            strings.append(b+"0")
            strings.append(b+"1")
        return strings
        
def string_to_nat(b):
    """Given a binary string, converts it into a natural number.  Do not modify this function."""
    if b == "":
        return 0
    else:
        return 2 * string_to_nat(b[:-1]) + int(b[-1])
        

def nat_to_string(x):
    """Given a natural number, converts it into a binary string  Do not modify this function."""
    assert(x >= 0)
    if x == 0:
        return ""
    else:
        return nat_to_string(x//2) + str(x % 2)
        
"""This next block of functions is setting us up to program in AON-Straightline. The is_binary function checks that we are only computing on binary inputs/outputs (the only data type that AON-Straightlin can handle). The AND, OR, and NOT functions implement the corresponding boolean operators in python. """

def is_binary(b):
    return b == '1' or b == '0'

def AND(a,b):
    assert(is_binary(a) and is_binary(b))
    return str(int(a)*int(b))

def OR(a,b):
    assert(is_binary(a) and is_binary(b))
    return str(int(a)+int(b) - int(a)*int(b))

def NOT(a):
    assert(is_binary(a))
    return str(1-int(a))
    
"""FOr this assignment we're programming in NAND-Straightline in for some functions, and NAND-Straightline with sugar for others. We start out by implementing some of the functions in class in AON-Straightline: XOR, NAND, and MAJ (you saw these last week). Recall that each line in the program should consist of a new variable declaration on the left-hand side and a NAND operation (or the permitted sugary operation for some problems) on the right-hand side, or else a return statement. Please note that you cannot have multiple operations nested (e.g. NOT(AND(a,b)) is not permitted), and you cannot re-assign and already assigned variable (e.g. a = NOT(a) is not permitted)."""
    
def XOR(a,b):
    not_a = NOT(a)
    not_b = NOT(b)
    a_not_b = AND(a, not_b)
    b_not_a = AND(b, not_a)
    return OR(a_not_b, b_not_a)

def NAND(a,b):
    a_and_b = AND(a,b)
    return NOT(a_and_b)
    
def MAJ(a,b,c):
    assert(is_binary(a) and is_binary(b) and is_binary(c))
    first_two = AND(a,b)
    last_two = AND(b,c)
    first_last = AND(a,c)
    temp = OR(first_two, last_two)
    return OR(temp, first_last)

"""For this assignment you'll be building arithmetic (specifically, addition) using straightline programs. Keep in mind that straightline programs can be easily converted into boolean gates, meaning that you're actually starting to build components of real integrated circuits here. How neat is that?!

These are going to be using a similar recursive definition of functions as what you saw with LOOKUP from lecture. You'll be able to build "larger" versions of functions out of smaller versions of the same functions.

To begin, we will implement a half adder. Sometimes when adding n-bit numbers together, the result will be n+1 bits long. Consider the sum (in binary) 10+11=101. A half adder is an adder which takes as input two n-bit natural numbers and returns the least significant n bits of their sum. For the previous example, a half-adder would return 01.

Implement a 2-bit half adder below. You may only use NAND
"""

def HADD2(a0, a1, b0, b1):
    return '0','0'

assert(HADD2('1','0','1','0') == ('0','0'))
assert(HADD2('1','1','1','0') == ('0','1'))
assert(HADD2('0','0','0','0') == ('0','0'))
assert(HADD2('1','1','0','1') == ('0','0'))

"""A Full Adder is a function that takes in three bits as input and gives their sum as output. For example, FADD(0,1,1) = 1,0. The idea of a full adder is that two of the bits will represent input bits in the addition, and the third bit will represent the carry value of the addition of a less-significant bit.

Implement a Full Adder below. You may use only NAND."""

def FADD(a,b,c):
    return '0','0'
    
assert(FADD('0','1','1') == ('1','0'))
assert(FADD('0','0','0') == ('0','0'))
assert(FADD('1','1','1') == ('1','1'))

"""Use the HADD2 and FADD procedures to implement a function that adds together two 4-bit numbers. You may use NAND, XOR, MAJ, or any other procedures as syntactic sugar if you wish (you must follow these same rules when implementing your own procedures)."""

def ADD4(a0, a1, a2, a3, b0, b1, b2, b3):
    return '0' # you must figure out how many bits you actually need to return
    
"""The next problem is a challenge problem. These are problems whose difficulty is so high that we do not necessarily expect most students will be able to do them within the time constraints of this assignment. We do, though, believe that they will be good practice. You are not required to complete or even attempt any challenge problems, but if you do, please let you Cohort Coach know. Successful completion of challenge problems will very much impress the course staff, and can also improve your community score.

CHALLENGE: Implement a function which computes the product of two 4-bit numbers"""

def MULT4(a0, a1, a2, a3, b0, b1, b2, b3):
    return '0' # you must figure out how many bits you actually need to return


