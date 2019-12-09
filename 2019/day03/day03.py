"""
Day03 - Advent of code
@casfranco 

The distance between two points measured along axes at right angles.
The Manhattan distance between two vectors (or points) a and b is defined as ∑i|ai−bi| over the dimensions of the vectors.

Part1:
    - From start point (0,0), movement --> compute all visited coordinates (for each wire)
    - Get intersection points
    - Question: What is the Manhattan distance from the central port to the closest intersection?

"""
import os,sys
dir_path = os.path.dirname(os.path.realpath('__file__'))
sys.path.append(dir_path)

def main():
    input = os.path.join(paths(),"input.txt")
    with open(input) as text:
        wire_paths = [line.strip() for line in text]

    part1(wire_paths)
    part2(wire_paths)


def paths():
    a_f = os.path.abspath(__file__)
    head, tail = os.path.split(a_f)
    return head

def get_visited_coordinates(path: str) ->set():
    x = y = 0 #initial point
    visited_coordinates = set()

    for movement in path.split(","):
        direction = movement[0]
        steps = int(movement[1:])

        for _ in range(steps):
            if(direction == "R"):
                x += 1
            elif(direction == "L"):
                x -= 1
            elif(direction == "U"):
                y += 1
            elif(direction == "D"):
                y -= 1
            else:
                raise RuntimeError(f"Unknown direction {direction}")

            visited_coordinates.add((x,y))

    return visited_coordinates

def get_visited_coordinates_steps(path: str) ->dict:
    """
    Function for part2
    """
    x = y = total_steps = 0 #initial point
    visited_coordinates = {}

    for movement in path.split(","):
        direction = movement[0]
        steps = int(movement[1:])

        for _ in range(steps):
            total_steps += 1
            if(direction == "R"):
                x += 1
            elif(direction == "L"):
                x -= 1
            elif(direction == "U"):
                y += 1
            elif(direction == "D"):
                y -= 1
            else:
                raise RuntimeError(f"Unknown direction {direction}")

            coordinate = (x,y)
            if coordinate not in visited_coordinates:
                visited_coordinates[coordinate] = total_steps

    return visited_coordinates

def get_intersections(pathW1: str, pathW2: str) -> set():
    coordinates1 = get_visited_coordinates(pathW1)
    coordinates2 = get_visited_coordinates(pathW2)
    intersections = coordinates1.intersection(coordinates2)
    return intersections

def get_closet_md_intersection(intersections: set) -> int:
    mdistances = []
    for intersection in intersections:
        mdistance = get_MD_intersection_central(intersection)
        mdistances.append(mdistance)
    
    return min(mdistances)

def get_MD_intersection_central(coordinate) -> int:
    mdistance = abs(coordinate[0]) + abs(coordinate[1])
    return mdistance

def assert_closest_intersections(path1,path2,expected_result):  
    intersections = get_intersections(path1,path2)
    closestDistance = get_closet_md_intersection(intersections)
    assert(closestDistance==expected_result)

def assert_examples_part1():
    assert_closest_intersections("R8,U5,L5,D3","U7,R6,D4,L4",6)
    assert_closest_intersections("R75,D30,R83,U83,L12,D49,R71,U7,L72",
                                "U62,R66,U55,R34,D71,R55,D58,R83",
                                159)
    assert_closest_intersections("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                                "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
                                135)

def part1(wire_paths):
    intersections = get_intersections(wire_paths[0],wire_paths[1])
    closestDistance = get_closet_md_intersection(intersections)
    print(f"Part1 - Closest intersection: {closestDistance}")


def part2(wire_paths):
    coordinates1 = get_visited_coordinates_steps(wire_paths[0])
    coordinates2 = get_visited_coordinates_steps(wire_paths[1])
    intersections = set(coordinates1).intersection(set(coordinates2))

    sum_distances = []
    [sum_distances.append(coordinates1[coordinate] + coordinates2[coordinate]) for coordinate in intersections]

    print(f"Part 2 - {min(sum_distances)}")

if __name__ == "__main__":
    main()



