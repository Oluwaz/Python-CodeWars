#Code Wars Challenges

#Challenge 1
#######################################
######Beginner Series #3 Sum of Numbers 7kyu
def get_sum(a,b):
    count = 0
    for i in range(min(a,b), max(a,b) + 1):
        count += i
    return count

#Challenge 2
#######################################
######Find the next perfect square! 7kyu   
import math
def find_next_square(sq):
    n = math.sqrt(sq)
    if n % 1 == 0:
        return (int(n+1) * int(n+1))
    return -1

#Challenge 3
#######################################
######Equal Sides Of An Array 6kyu  
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

#Challenge 4
#######################################
######Disemvowel Trolls 7kyu  
def disemvowel(string):
    return "".join([ch for ch in string if ch not in "aeiouAEIOU"])

#Challenge 5
#######################################
######Exes and Ohs 7kyu
def xo(s):
    return s.lower().count('x') == s.lower().count('o')





