"""
Day01 - Advent of code
@casfranco 

Part1  
Part2

"""
import numpy as np
import os
import sys

dir_path = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(dir_path)

def main():
    
    input = os.path.join(paths(),"input.txt")
    
    assert_part1()
    part1(input)
    
    assert_part2()
    part2(input)

    print("End day01")

def paths():
    a_f = os.path.abspath(__file__)
    head, tail = os.path.split(a_f)
    return head

def part1(input):
    data = np.loadtxt(input)
    total_fuel = compute_fuel(data)
    print("Part1 - Total fuel is: {}.".format(total_fuel))

def part2(input):
    data = np.loadtxt(input)
    
    ## Not vectorized solution (testing)
    #total_fuel = 0
    #for i in range(len(data)):
    #    temp_fuel=compute_additional_fuel(data[i])
    #    total_fuel = total_fuel + temp_fuel 
    
    vectorized_compute_additonal_fuel = np.vectorize(compute_additional_fuel)
    total_fuel = int(sum(vectorized_compute_additonal_fuel(data)))
    print("Part2 - Total fuel is: {}.".format(total_fuel))

def compute_fuel(mass):
    """
    Function por part1 problem
    """
    totalFuel = int(np.sum( np.floor_divide(mass,3) - 2)) 
    return totalFuel

def compute_additional_fuel(mass):
    """
    Function por part2 problem
    """
    additional_fuel = compute_fuel(mass) 
    remainig_fuel = compute_fuel(additional_fuel)

    while(remainig_fuel>=0):
         additional_fuel = additional_fuel + remainig_fuel
         remainig_fuel = compute_fuel(remainig_fuel)

    return additional_fuel 


def assert_part1():
    assert compute_fuel(12) == 2
    assert compute_fuel(14) == 2
    assert compute_fuel(1969) == 654
    assert compute_fuel(100756) == 33583

def assert_part2():
    assert compute_additional_fuel(14) == 2
    assert compute_additional_fuel(1969) == 966
    assert compute_additional_fuel(100756) == 50346

if __name__ == "__main__":
    main()


