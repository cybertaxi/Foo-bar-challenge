# Numbers Station Coded Messages
# ==============================

# When you went undercover in Commander Lambda's organization, you set up a coded messaging system with Bunny Headquarters to allow them to send you important mission updates. Now that you're here and promoted to Henchman, you need to make sure you can receive those messages - but since you need to sneak them past Commander Lambda's spies, it won't be easy!

# Bunny HQ has secretly taken control of two of the galaxy's more obscure numbers stations, and will use them to broadcast lists of numbers. They've given you a numerical key, and their messages will be encrypted within the first sequence of numbers that adds up to that key within any given list of numbers. 

# Given a non-empty list of positive integers l and a target positive integer t, write a function solution(l, t) which verifies if there is at least one consecutive sequence of positive integers within the list l (i.e. a contiguous sub-list) that can be summed up to the given target positive integer t (the key) and returns the lexicographically smallest list containing the smallest start and end indexes where this sequence can be found, or returns the array [-1, -1] in the case that there is no such sequence (to throw off Lambda's spies, not all number broadcasts will contain a coded message).

# For example, given the broadcast list l as [4, 3, 5, 7, 8] and the key t as 12, the function solution(l, t) would return the list [0, 2] because the list l contains the sub-list [4, 3, 5] starting at index 0 and ending at index 2, for which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4] and the key t as 15, the function solution(l, t) would return [-1, -1] because there is no sub-list of list l that can be summed up to the given target value t = 15.

# To help you identify the coded broadcasts, Bunny HQ has agreed to the following standards: 

# - Each list l will contain at least 1 element but never more than 100.
# - Each element of l will be between 1 and 100.
# - t will be a positive integer, not exceeding 250.
# - The first element of the list l has index 0. 
# - For the list returned by solution(l, t), the start index must be equal or smaller than the end index. 

# Remember, to throw off Lambda's spies, Bunny HQ might include more than one contiguous sublist of a number broadcast that can be summed up to the key. You know that the message will always be hidden in the first sublist that sums up to the key, so solution(l, t) should only return that sublist.

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution([1, 2, 3, 4], 15)
# Output:
#     -1,-1

# Input:
# solution.solution([4, 3, 10, 2, 8], 12)
# Output:
#     2,3

# -- Java cases --
# Input:
# Solution.solution({1, 2, 3, 4}, 15)
# Output:
#     -1,-1

# Input:
# Solution.solution({4, 3, 10, 2, 8}, 12)
# Output:
#     2,3

# Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

# Java
# ====
# Your code will be compiled using standard Java 8. All tests will be run by calling the solution() method inside the Solution class

# Execution time is limited.

# Wildcard imports and some specific classes are restricted (e.g. java.lang.ClassLoader). You will receive an error when you verify your solution if you have used a blacklisted class.

# Third-party libraries, input/output operations, spawning threads or processes and changes to the execution environment are not allowed.

# Your solution must be under 32000 characters in length including new lines and and other non-printing characters.

# Python
# ======
# Your code will run inside a Python 2.7.13 sandbox. All tests will be run by calling the solution() function.

# Standard libraries are supported except for bz2, crypt, fcntl, mmap, pwd, pyexpat, select, signal, termios, thread, time, unicodedata, zipimport, zlib.

# Input/output operations are not allowed.

# Your solution must be under 32000 characters in length including new lines and and other non-printing characters.




#I screw up on this one............

def solution(l,t):
    sum=0
    j=0
    for key,value in enumerate(l):
        sum = sum + value
        print(sum)
        while(sum>t and j < key ):
            sum = sum - l[j]
            j = j + 1
        if sum == t:
            return [j,key]

    return [-1,-1]

# def solution(num_list, number):
#     answer = []    
#     original_number = number
#     list_len = len(num_list)
#     for index, num in enumerate(num_list):
#         start = index + 1
#         number -= num
#         if number == 0:
#             answer = [index] + [index]
#             break
#         found_index = check(num_list[start:], number, start)
#         if index >= 0 and found_index >=0:
#             answer = [index] + [found_index]
#             break
#         if found_index < 0:
#             number = original_number
        
#         if start == list_len and found_index < 0 :
#             answer = [-1,-1]
#     return answer

def check(num_list, number, start):
    len_list = len(num_list)
    if len_list == 0:
        return -1
    for index, num in enumerate(num_list):
        number -= num
        if number == 0:
            return index + start
        if index + 1 == len_list:
            return -1
     

print(solution([1,2,3,4],15)) #[-1,-1]
# print(solution([4,3,5,7,8],12)) #[0,2]
# print(solution([4, 3, 10, 2, 8], 12)) #[2,3]
# print(solution([1,1,1],1)) #[0,0]
# print(solution([1,1],2)) #[0,1]
# print(solution([250],250)) #[0,0]
