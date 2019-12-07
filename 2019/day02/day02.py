"""
Day02 - Advent of code
@casfranco 

Part1:
1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

replace iition 1 with the value 12 and replace iition 2 with the value 2. 
What value is left at iition 0 after the data halts?

Part2:
"With terminology out of the way, we're ready to proceed. To complete the gravity assist,
you need to determine what pair of inputs produces the output 19690720."

"""
import numpy as np
import os
import sys

def main():
    dir_path = os.path.dirname(os.path.realpath('__file__'))
    sys.path.append(dir_path)
    input = os.path.join(paths(),"input-2.txt")
    part1(input)
    target_output=19690720
    part2(input,target_output)

def paths():
    a_f = os.path.abspath(__file__)
    head, tail = os.path.split(a_f)
    return head

def run_data(data):

    i = 0

    while ((data[i] != 99)):  # halt
        opcode, loc1, loc2, loc3 = data[i], data[i + 1], data[i + 2], data[i + 3]
        #print(i)
        if opcode == 1:
            data[loc3] = data[loc1] + data[loc2]
        elif opcode == 2:
            data[loc3] = data[loc1] * data[loc2]
        else:
            pass
            raise RuntimeError(f"invalid opcode: {data[i]}")
        i += 4
    
    return data

def part1(input,noun=12,verb=2):
    data = np.loadtxt(input,delimiter=',').astype(int)
    data[1]=noun
    data[2]=verb
    new_data=run_data(data)
    print("Part1 : {}.".format(new_data[0]))

def part2(input,target_output):    
    for noun in range(100):
        for verb in range(100):
            data = np.loadtxt(input,delimiter=',').astype(int) #TODO -> Improve method, avoid read text at every step.
            data[1]=noun
            data[2]=verb
            new_data=run_data(data)
            output=new_data[0]
            if(output==target_output):
                print("Part2 : {}.".format(100 * noun + verb))
                #print(noun, verb, 100 * noun + verb)
                break

if __name__ == "__main__":
    main()


