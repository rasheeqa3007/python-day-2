from math import log2, floor

def findMinDenomin(n):

    return log2(n) + 1


if __name__ == '__main__':
    
    n = 10

   
    print(floor(findMinDenomin(n)))
