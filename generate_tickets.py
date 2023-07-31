import random
import time


def shuffle(numbers):
    #assuming all numbers are non-zero
    total = len(numbers)
    shifting_total = total
    output = [0 for _ in range (0, total)]

    for number in numbers:
        position = random.randint(0, shifting_total-1)#
        var_i = 0
        actual_pointer = 0
        while(var_i <= position):
            if(output[actual_pointer] != 0):
                pass
            else:
                var_i += 1
            actual_pointer += 1
        actual_pointer -= 1
        output[actual_pointer] = number
        shifting_total -= 1
    
    return output


def verify(numbers):
    #verify no repeats or zeros
    repeats = []
    carry = 1
    for number in numbers:
        if not number in repeats:
            if number in numbers[carry:]:
                repeats.append(number)
            if number == 0:
                repeats.append(0)
        carry += 1
    
    return repeats


def makeTwo(string):
    if(len(string) == 0):
        return "00"
    elif(len(string) == 1):
        return "0" + string
    else:
        return string

class SevenPointHypograph:

    def __init__(self):
        self.nodes = ["00,00" for _ in range (0, 7)]

    def draw(self):
        print("         " + self.nodes[0])
        print("        |  |  |")
        print("     " + self.nodes[1] + " | " + self.nodes[3])
        print("      | -  |  - |")
        print("     |   " + self.nodes[5] + "   |")
        print("    |   -  |  -   |")
        print("   |  -    |    -  |")
        print(self.nodes[2] + "----" + self.nodes[6] + "----" + self.nodes[4] + "\n")
        print("")

    def get_values(self, numbers):
        for i in range (0, 7):
            self.nodes[i] = makeTwo(str(numbers[i*2])) + "," + makeTwo(str(numbers[i*2+1]))
    
    def print_tickets(self):
        print(self.nodes[0] + "," + self.nodes[1] + "," + self.nodes[2])
        print(self.nodes[0] + "," + self.nodes[3] + "," + self.nodes[4])
        print(self.nodes[0] + "," + self.nodes[5] + "," + self.nodes[6])
        print(self.nodes[1] + "," + self.nodes[4] + "," + self.nodes[5])
        print(self.nodes[1] + "," + self.nodes[3] + "," + self.nodes[6])
        print(self.nodes[2] + "," + self.nodes[4] + "," + self.nodes[6])
        print(self.nodes[2] + "," + self.nodes[3] + "," + self.nodes[5])

    def write_to_file(self, f):
        f.write(self.nodes[0] + "," + self.nodes[1] + "," + self.nodes[2] + "\n")
        f.write(self.nodes[0] + "," + self.nodes[3] + "," + self.nodes[4] + "\n")
        f.write(self.nodes[0] + "," + self.nodes[5] + "," + self.nodes[6] + "\n")
        f.write(self.nodes[1] + "," + self.nodes[4] + "," + self.nodes[5] + "\n")
        f.write(self.nodes[1] + "," + self.nodes[3] + "," + self.nodes[6] + "\n")
        f.write(self.nodes[2] + "," + self.nodes[4] + "," + self.nodes[6] + "\n")
        f.write(self.nodes[2] + "," + self.nodes[3] + "," + self.nodes[5] + "\n")

class ThreePointHypograph:

    def __init__(self):
        self.nodes = ["00,00,00" for _ in range (0, 3)]

    def draw(self):
        print("        " + self.nodes[0])
        print("         |    |")
        print("        |      |")
        print("       |        |")
        print("      |          |")
        print("     |            |")
        print("    |              |")
        print(self.nodes[1] + "--------" + self.nodes[2] + "\n")
        print("")

    def get_values(self, numbers):
        for i in range (0, 3):
            self.nodes[i] = makeTwo(str(numbers[i*3])) + "," + makeTwo(str(numbers[i*3+1])) + "," + makeTwo(str(numbers[i*3+2]))

    def print_tickets(self):
        print(self.nodes[0] + "," + self.nodes[1])
        print(self.nodes[0] + "," + self.nodes[2])
        print(self.nodes[1] + "," + self.nodes[2])

    def write_to_file(self, f):
        f.write(self.nodes[0] + "," + self.nodes[1] + "\n")
        f.write(self.nodes[0] + "," + self.nodes[2] + "\n")
        f.write(self.nodes[1] + "," + self.nodes[2] + "\n")

class FourPointHypograph:

    def __init__(self):
        self.nodes = ["00,00" for _ in range (0, 4)]

    def draw(self):
        print("        " + self.nodes[0])
        print("        |   |")
        print("       |     |")
        print("      |       |")
        print("     |  " + self.nodes[3] + "  |")
        print("    |           |")
        print("   |             |")
        print(self.nodes[1] + "-----------" + self.nodes[2] + "\n")

    def get_values(self, numbers):
        for i in range (0, 4):
            self.nodes[i] = makeTwo(str(numbers[i*2])) + "," + makeTwo(str(numbers[i*2+1]))

    def print_tickets(self):
        print(self.nodes[0] + "," + self.nodes[1] + "," + self.nodes[3])
        print(self.nodes[0] + "," + self.nodes[2] + "," + self.nodes[3])
        print(self.nodes[1] + "," + self.nodes[2] + "," + self.nodes[3])

    def write_to_file(self, f):
        f.write(self.nodes[0] + "," + self.nodes[1] + "," + self.nodes[3] + "\n")
        f.write(self.nodes[0] + "," + self.nodes[2] + "," + self.nodes[3] + "\n")
        f.write(self.nodes[1] + "," + self.nodes[2] + "," + self.nodes[3] + "\n")

def make_triangles(numbers):
    #make the cool pattern matching triangles

    #verify list length
    if(len(numbers) != 59):
        print("number list wrong length")
        return
    
    #make objects
    SeTri1 = SevenPointHypograph()
    SeTri2 = SevenPointHypograph()
    SeTri3 = SevenPointHypograph()
    ThTri = ThreePointHypograph()
    FoTri = FourPointHypograph()

    #assign values from input
    SeTri1.get_values(numbers)
    SeTri2.get_values(numbers[14:])
    SeTri3.get_values(numbers[28:])
    ThTri.get_values(numbers[42:])
    FoTri.get_values(numbers[51:])

    #draw
    SeTri1.draw()
    SeTri2.draw()
    SeTri3.draw()
    ThTri.draw()
    FoTri.draw()
    
    #wait for user to move on
    print("\npress enter to continue...")
    input()

    #print tickets
    SeTri1.print_tickets()
    SeTri2.print_tickets()
    SeTri3.print_tickets()
    ThTri.print_tickets()
    FoTri.print_tickets()

    #open and write to file
    f = open("tickets.txt", 'w+')
    SeTri1.write_to_file(f)
    SeTri2.write_to_file(f)
    SeTri3.write_to_file(f)
    ThTri.write_to_file(f)
    FoTri.write_to_file(f)
    f.close()

    #wish luck
    print("\ngood luck :)")
    




if  __name__ == "__main__":
    #set random number seed
    random.seed(int(time.time()))

    #generate all possible lotto numbers
    lotto_numbers = [i for i in range (1, 60)]

    #shuffle
    shuffled = shuffle(lotto_numbers)
    #check for errors in the shuffle
    repeats = verify(shuffled)

    #print shuffled numbers
    print("shuffeled lotto numbers:")
    print(shuffled)

    #debug outputs a list of error values
    #by index of the shuffled list
    # print("debug", repeats)

    #wait for user to move on
    print("\npress enter to continue...")
    input()

    #make the hypergraphs
    make_triangles(shuffled)