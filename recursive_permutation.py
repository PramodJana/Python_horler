from itertools import permutations

def allPermutations(str):
     permList = permutations(str)

     for perm in list(permList):
         print (''.join(perm))

if __name__ == "__main__":
    str = str(input())
    allPermutations(str)
