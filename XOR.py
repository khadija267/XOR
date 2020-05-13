#AND GATE
def NAND(inputs):
    w1=1
    w2=1
    b=-2
    output_arr=[]
    for i in inputs:
        combination = w1 * i[0] + w2 * i[1] + b
        output = int(combination < 0)
        output_arr.append(output)
    return output_arr 
#OR GATE
def OR(inputs):
    w1=1.5
    w2=1.5
    b=-1
    output_arr=[]
    for i in inputs:
        combination = w1 * i[0] + w2 * i[1] + b
        output = int(combination >= 0)
        output_arr.append(output)
    return output_arr   
#XOR GATE
import numpy as np
def XOR(inp):
    inputs=np.column_stack(( NAND(inp),OR(inp) ))
    w1=.9
    w2=.9
    b=-1
    output_arr=[]
    for i in inputs:
        combination = w1 * i[0] + w2 * i[1] + b
        output = int(combination >= 0)
        output_arr.append(output)
    return output_arr    
i = [(0, 0), (0, 1), (1, 0), (1, 1)]
print(XOR(i))    
    
    
    
    