"""The goal of this exercise is to develop your understanding of universality by building the EVAL function discussed in class. For better readability, we will be using bitstrings as inputs rather than individual bits. To keep this as formal as the algorithm discussed in class, avoid maninpulating substrings longer than just a single bit. You may not use any for loops or if statements in your implementation, but you may invoke functions that are provided or that you define (so long as this also abide by the above rules). If your function should return multiple bits as output, return those as a string."""



""" This function enumerates all binary strings of a certain length. This will primarily be used for testing purposes."""
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

""" This function converts a given natural number into a bit string, where the length of the bit string is fixed to be the second argument."""
def nat_to_string(number, num_bits):
    binary = ""
    for i in range(num_bits):
        bit = str(number % 2)
        number = number // 2
        binary = bit + binary
    return binary

def is_binary(b):
    return b == '1' or b == '0'
    
"""Here are the definitions of a bunch of functions you've seen before, and may be helpful in this exercise. Feel free to use any of them."""
        
def NAND(a,b):
    assert(is_binary(a) and is_binary(b))
    return str(1-int(a)*int(b))
    
def NOT(a):
    return NAND(a, a)

def AND(a, b):
    temp = NAND(a, b)
    return NAND(temp, temp)

def OR(a, b):
    temp1 = NAND(a,a)
    temp2 = NAND(b,b)
    return NAND(temp1, temp2)

def XOR(a, b):
    or_ab = OR(a, b)
    and_ab = AND(a, b)
    not_and_ab = NOT(and_ab)
    return AND(or_ab, not_and_ab)

def IF(cond,a,b):
    not_cond = NAND(cond, cond)
    temp1 = NAND(cond, a)
    temp2 = NAND(not_cond, b)
    return NAND(temp1, temp2)

def LOOKUP_1(x0, x1, i0):
    return IF(i0, x1, x0)

def LOOKUP_2(x0,x1,x2,x3,i0,i1):
    first_half = LOOKUP_1(x0, x1, i1)
    second_half = LOOKUP_1(x2, x3, i1)
    return IF(i0, second_half, first_half)

def LOOKUP_3(x0,x1,x2,x3,x4,x5,x6,x7,i0,i1,i2):
    first_half = LOOKUP_2(x0, x1, x2, x3, i1, i2)
    second_half = LOOKUP_2(x4, x5, x6, x7, i1, i2)
    return IF(i0, second_half, first_half)
    


"""This next function will take a NAND-Straightline program as described by a list of triples of natural numbers, and will return a bitstring to represent that list of triples"""
    
def prog2bits(prog, num_bits):
    bits_prog = ""
    for triple in prog:
        bits0 = nat_to_string(triple[0], num_bits)
        bits1 = nat_to_string(triple[1], num_bits)
        bits2 = nat_to_string(triple[2], num_bits)
        triple_bits = bits0 + bits1 + bits2
        bits_prog += triple_bits
    return bits_prog

"""This is IF as a list-of-triples representation"""
if_program = [(3,0,0),(4,0,1),(5,3,2),(6,4,5)]

if_program = prog2bits(if_program, 3)
print(if_program)


'''We will not begin building up the components necessary to eventually implement EVAL. The first new function we'll need is GET_7, which will index into the table `T` of 7 rows (since the programs we're evaluating will have 7 variables). This function gives you an idea for how we can take bit strings as input and consider it as if it was several inputs of a single bit each.'''

def GET_7(T, i):
    assert(len(T) == 7 and len(i) == 3)
    # gives the value of the variable indexed by the length 3 bitstring i from a 7-bit table T
    return LOOKUP_3(T[0], T[1], T[2], T[3], T[4], T[5], T[6], "0", i[0], i[1], i[2])


"""This is test code, so you can see what GET_7 is meant to do"""
for t in list_strings(7):
    for i in range(7):
        assert(t[i] == GET_7(t, nat_to_string(i, 3)))
    
"""TODO: Implement the function EQUAL_3 below, which will return 1 if two given 3-bit numbers are the same, and 0 otherwise."""

def EQUAL_3(i, j):
    assert(len(i) == len(j) == 3)
    #TODO: Replace the body of this function to implement EQUAL_3 correctly
    return "0"

for s1 in list_strings(3):
    for s2 in list_strings(3):
        if s1 == s2:
            assert(EQUAL_3(s1, s2) == '1')
        else:
            assert(EQUAL_3(s1, s2) == '0')
print("Bravo!")


"""TODO: Implement the function UPDATE_7 below, which will change the given index (given by the triple of bits i) of the 7-row table T to become the bit b. You will likely need EQUAL_3 and IF to do this."""
    
def UPDATE_7(T, b, i):
    assert(len(T) == 7)
    #TODO: Replace the body of this function to implement UPDATE_7 correctly
    t0 = T[0]
    t1 = T[1]
    t2 = T[2]
    t3 = T[3]
    t4 = T[4]
    t5 = T[5]
    t6 = T[6]
    return t0+t1+t2+t3+t4+t5+t6


def pseudo_update_7(T, b, i):
    """This update works by manipulating indices directly. It is meant to show you what your update should return, and to use for the assert below."""
    index = int(i[2]) + 2*int(i[1]) + 4*int(i[0])
    return T[:index] + b + T[index+1:]

for t in list_strings(7):
    for i in range(7):
        for b in range(2):
            assert(pseudo_update_7(t, str(b), nat_to_string(i, 3)) == UPDATE_7(t, str(b), nat_to_string(i, 3)))
print("You got it!")


"""TODO: Now we have all the pieces we need in order to implement EVAL_3_7_4_1. This is a function that will take 2 inputs: a bitstring representing a NAND-Straightline program, and a bitstring to be given as input to that program. The output of EVAL_3_7_4_1 should be the same as the output of that program running on that input. The 3,7,4,1 refer to the number of input bits, variables, lines, and output bits of the program (respectively)."""
def EVAL_3_7_4_1(program, input_bits):
    assert(len(program) == 4*3*3) # the length of the program is lines * 3 * log_2(variables)
    assert(len(input_bits) == 3)
    T0 = "0"
    T1 = "0"
    T2 = "0"
    T3 = "0"
    T4 = "0"
    T5 = "0"
    T6 = "0"
    # TODO: fill in the body of this function.
    return T6

cond,a,b = "0","1","0"
assert(EVAL_3_7_4_1(if_program, cond+a+b) == IF(cond,a,b))
print("Gucci!")

cond,a,b = "1","1","0"
assert(EVAL_3_7_4_1(if_program, cond+a+b) == IF(cond,a,b))
print("Sweet!")

cond,a,b = "0", "0","1"
assert(EVAL_3_7_4_1(if_program, cond+a+b) == IF(cond,a,b))
print("Cool Beans!")

cond,a,b = "1","0","1"
assert(EVAL_3_7_4_1(if_program, cond+a+b) == IF(cond,a,b))
print("You Rock!")


"""If we were to slightly modify our procedure for converting programs into a list of triples, we can use `EVAL_3_7_4_1` to evaluate any program that uses no more than 3 inputs, 7 variables, 4 lines, and 1 output."""

"""TODO: Write OR as a list of triples so that we can evaluate it using EVAL_3_7_4_1 above. Note that OR requires fewer inputs, variables, and lines of code than IF does. You'll need to do something about that. You may use the prog2bits function we provided above."""

or_program = [] # TODO: fill this in as a list of triples of natural numbers

a,b = "0","0"
assert(EVAL_3_7_4_1(or_program, a+b+"0") == OR(a,b))
a,b = "0","1"
assert(EVAL_3_7_4_1(or_program, a+b+"0") == OR(a,b))
a,b = "1","0"
assert(EVAL_3_7_4_1(or_program, a+b+"0") == OR(a,b))
a,b = "1","1"
assert(EVAL_3_7_4_1(or_program, a+b+"0") == OR(a,b))

print("You did it!!")

