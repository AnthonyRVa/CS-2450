08/29/25 - Subject: Github, In todays class we talked about linking our github's. To do this we use ssh keys. How it works is you and
github both have a public and private key. To be alble to trust eachother github sends an encrypted file that uses your public key. You then have to decrypt it with your private key to show the server that you are who you say you are. This is how ssh keys work.

09/3/25 - I faced an issue with ssh keys. I was able to clone, but not able to push commits to the online repo. The solution was to  make a new set of ssh keys in ubuntu instead of visual studios. Adding the new ssh key allowed me to push, commit, etc. 

09/9/25 - 
Data Structure Class

Recursion - In python it means to call a function inside that function
Factorio 5! = 5*4*3*2*1
6! = 6*5*4*3*2*1  == 6*5!
n! = n*(n-1)!  --> 1! = 1
--------------------------
Text Book way of Recursion
def main():
x = F(4)   #F means Factorio

#Calling a function inside the same function means it'll
#run the function inside first before returning the answer.
def F(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N*f(N-1) #4*F(3) * 3*F(2) * 2*F(1) ##F(1) = 1
-------------------------------------------------------------

def main():
A = [5, 1, 0, 4, 7, 2, 6, 1]
mergesort(A)

def mergesort(A-list):
    if len(A-list) <= 1:
        return
    mid = len(A-list)//2
    left = A-list[0:mid] #left contains [5, 1, 0, 4]
    right = A-list[mid:] # right contains [7, 2, 6, 1]
    mergesort(left) #Recursion: goes into mergesort([5, 1, 0, 4]) -> mergesort([5, 1]) -> mergesort([5])
    mergesort(right)
#merge two sorted half lists
#into one sorted full list
    i = 0 #index of left list
    j = 0 #index of right list
    k = 0 #where your copying the number
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A-list[k] = left[i]
            i += 1
            k += 1
        else:
            A-list[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        A-list[k] = left[i]
        k += 1
        i += 2
    while j < len(right):
        A-list[k] = right[j]
        k += 1
        j += 1

Merge Sort Big-O = N * log_2 N
-----------------------------------------

Quick Sort(recursive)

A = [4, 1, 0, 5, 7, 2, 6, 1]
#first item in the list (4 in our case) is your pivot item. Means 
#all smaller numbers then the first number are on the
#left and all the bigger numbers are right.




09/10/25 - Quick Sort & Modified Quick Sort

A = [3, 7, 5, 2, 0, 7, 6, 4]
def quicksort(A): # we made this bridge function so you don't have to pass variables to run quicksort
    quicksortrecursive(A, 0, len(A) - 1) # pivots index is low, first number, A[0] = 5
def quicksortrecursive(A, low, high):
    if high - low <= 0: #catches any list with only 1 item
        return
    leftmostgreaterthan = low + 1 # = 1
    for i in range(low + 1, high + 1):
        if A[i] < A[low]: # moves any value less then the pivot to before the greater thans
            A[i], A[leftmostgreaterthan] = A[leftmostgreaterthan], A[i]
            leftmostgreaterthan += 1
    pivotindex = leftmostgreaterthan - 1
    A[low], A[pivotindex] = A[pivotindex], A[low]
    quicksortrecursive(A, low, pivotindex-1) # Recursive part of code, the lower than pivots part
    quicksortrecursive(A, pivotindex+1, high) # the greater than pivots part

Big order
Quick sort with random data but with sorted data N^2 (N*N)
Mergesort is N*Log_2 *N Always


Modified Quick Sort
add after top if statement in regular quick sort:
    mid = (low+high)//2
    A[mid], A[low] = A[low], A[mid]
# this modification only works if people aren't atempting to break the code by making it
# super long. To be safe use merge sort which is more reliable


09/11/25 - User Stories

Format: As a _______ I want ______________, So that __________

09/17/25 - 

Abstract Data Type      VS.      Full Details
<-------------------------------------------->
(Teaching someone about a car)
Steering wheel                      Car engine
Gas petal               (Every part of engine)
Break petal                             Etc.
Ignition

Abstract data type - Main functions of a program

Full Details - How you'll make the main functions work
As a programer first worry about the big things to add, then how to add and make them work.


09/22/25 - Github Merging Branches, 

When encountering a merge conflict type this:
    git pull -no-rebase
This makes git attempt to merge automatically if possible.
Most the time this will work but when it won't is when two people have written on 
the same line on the same file.

If it can't an error message like this will be shown:
##################################################################
jeffcompas ~/UtahTech/CS2450 $ git pull --no-rebase
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 374 bytes | 62.00 KiB/s, done.
From github.com:JeffCompasClassrooms/testing-units-with-tdd-f25-jeffozozo

   d109c88..be8fc6c  main       -> origin/main

Auto-merging Requirements_spec.md
CONFLICT (content): Merge conflict in Requirements_spec.md
Automatic merge failed; fix conflicts and then commit the result.
##################################################################

At the bottom it shows "Automatic merge failed", this means git couldn't resolve the
merge conflict and has left it to us too. When this happens it'll make you go into the changed
files listed above in the 2nd to last line.

Go into that file and you'll see:
##################################
 15 <<<<<<< HEAD
 16 Four score and seven years ago...
 17 
 18 We hold these truths to be self evident... 
 19 =======
 20 Four score and seven years ago...
 21 
 22 Now is the time for all good men to come to the aid of their country
 23 >>>>>>> 75ad130f8df35f5603f2b1f8df7a1d023bd1e083
####################################################

The merge error is surroned by:
>>>>>> Head 
....
>>>>>> Memory location of error

Inside this you'll see two versions of the same part seperated by =====.
To solve the merge conflict you have to pick one to keep.
To do so you have to delete everything but the lines you want to keep,
even the <<<<<<, other version, and ===== so you should be just be left with:

 20 Four score and seven years ago...
 21
 22 Now is the time for all good men to come to the aid of their country

------------------------------------------------------
Data Structure Class: 
Bag Assignment:
    Containers for Bag Assignment
    Abstract Data Types Vs Implementation (Teaching the basics Vs Teaching how to make it/implement)
    ADT specifics for bag
    Student Objects (classes type)
    Main Function
    Implement Bag Using Python List
    File Structure

Containers(type of data/list) we'll use is: 
    unsorted 
    non repeat(no duplicates)

09-29-25

Adding Numbers: N
Multiplying Numbers: 2N^2 --> N^2 (same as 2N^2)
Matrix's (3x3): N^3
Exponential Algorithms/Intractible: Big O's that are to big/unsolvable
and the Big O's for them are: 2^N(SAT/Boolean Problem), N!(TSP), & 10^(n/2)(RSA)

NP - Non deterministic polynomial (Given the answer(not solving), you can verify it in polynomial time.)
    SAT(Boolean Problem), Traveling Sales Man Problem, RSA(Factoring Problem) are all verifyable in polynomial time(Not Solvable in polynomial time).

NP Complete - A portion of problems that can be converted to an SAT(Boolean Problem)

All the problems above can be converted into a SAT(Boolean Problem), meaning if anyone managed to solve SAT problem, They would be able to solve all NP(Problems not able to be solved in polynomial time) problems in polynomial time includingproblems like TSP, Factoring, etc.

To make NP = P you have to solve any problem in NP in P(polynomial) time

NP != NP Complete

10-01-25

CS-2420 - Topics

Big O's-
Array = python list
Array Lookups - Big O of 1 (index = number, A[index])
Array Append/Push - 1 (A.append[x])
Array Pop - 1 (A.pop())
Array Pop(index) - N (A.pop(index) bigger because you have to shift list for removed item)
    To Pop(index) = 1, flip last number of list with the index and then pop so you don't have to shift whole list.

NP Cirlce Vs NP Ring:

NP Circle - Problems that can be checked/verified in P-time
    P are the easy problems that can be done in polynomial time
    NP are the difficult problems that can't be solved in polynomial time but can be checked in polynomial time with given answers


NP Ring is problems that can be verified in P-time
    and we believe these problems take exponential time to solve

Remember anything in NP Complete, if solved in polynomial time, can make any problem in NP can solvable in P-time


Create unique random lists

def ranuniquelist(n): # big O of N^3
    A = []
    while len(A)<n: # one N^2 for Big O (since the more you have added the harder it'll be to pick a num that's not in the list already)
        num = random.randrange(0,n):
        if num is not in A: # Another N for Big O
            A.append(num)
    return A

Better version:

def ranuniquelist(n): # Big O of N
    A=[]
    for i in range(N):
        A.append(i)
    for i in range(N):
        R= -------
        A[i], A[R] = A[R], A[i]

> Binary Search

def binarysearch(A,x):
# A must be sorted or youll need to use linear search
low = 0
high = len(A)-1
while high-low >= 0:
    mid = (low+high)//2
    if A[mid] == x:
        return mid
    elif x < A[mid] # left of list
        high = mid-1
    else: # if x is bigger than mid right side of list
        low = mid + 1
return -1

log base 2 of 510,000,000 is 19

4^15 is 1 billion b/c (2^2)^15 -> 1 billion

binary search is Log of N
Shaker sort mostly sorted N (If unsorted would equal N^2)
Traveling sales person is N!
Factoring 10^(n/2)
Multiply NxN matrix N^3

When is Big O analysis most important:
When N is very large, When a program is slow

        Random, Worst,  Best
Shaker    N^2    N^2     N
Quick    N LogN  N^2    N Log N
merge   N Log N  N logN N Log N

Which would be best to prove, P=NP or P != NP,What proof would you need
P != NP is believed to be true, Prove any problem in NP will never be able to be solved in P

one pass of quick sort for list of 5 7 3 1 6 8 4 9 0
pivot = 5
5 3 1 4 0 8 7 9 6
0 3 1 4 5 8 7 9 6

for loop N time
    call function that does N^2
    for loop N times
        For loop N times
            call function that does N

N^2 * N^3 = N^3

N * N^3 = N^4

crete mostly sorted list code

def createmostlysortedlist(size):
    A = createRandomlist(size)
    A.sort()
    A[0],A[-1] = A[-1],A[0]
    return A

10-13-25 LINKED LIST

problems with python list:
requires continous memoery(ram)
order n to add or delete things

Linked list will solve this

Linked List (used for memory):
not continous(scattered randomly). It has a pointer that connects to first item from an unorganized list.
Holds the next address in memory for the next item.(keeping it organized but being able to be scattered out)

Linked List Advantages:
Can fill up all memory in ram
really easy to link and unlink
Holds the 4 byte address to the next item
Not expensive to delete something in the middle. (changes address route from previous item to a valid item after the deleted item)
The above is only true if we know where it is.
Really fast for Deque

When making an item you make two things:
4 byte pointer (an address that points two where the item is)
Item is the actual item you create in a random spot in memory(RAM)

10-20-25

Talk About: Linked List, variants of linked list, stacks, queues

Circular Linked List - A linked list that instead of having a none for the end of the list, you'll point back to the first node

Double Linked List - A linked list with the node having a previous address, item, and the next address. Simply a linked list with the node having the address of the node that came before it.

---------------------------------
A stack is an abstract data type(ADT).
It only serves to contain info with only four operations:
Push(add)
Pop(remove)
Top(look at top)
IsEmpty(Checks if is empty)
(You can use python list or linked list for this)

class Stack:

def __init__(self):
    self.items = []

def push(self,item):
    self.items.append(item)

def pop(self)

first item added, is the last one to get removed
last item in, is first item out
(just like a stack of papers)
----------------------------------
Queue
First item in, first item out (FILO)
last item in last item out (LILO)

Think of it as a line people line up for. Use Circular Linked List with a back pointer for this system

Queue uses:
deque, enqueue, 

class Queue:

    def __init__(self):
        self.items = []
        self.back =  # This is a pointer that sets the address to the end of the list

    def enqueue(self, item):
        n = Node(item, None) # Node is the class Node used for linked list
        n.nxt = self.back.nxt
        self.back.nxt = n
        self.back = n
    
    def dequeue(self):
        x = self.back.nxt.item # this is the first node(but only item so no .nxt) in the list
        self.back.nxt = self.back.nxt.nxt
        return x

        """
        x = self.back.nxt
        self.back.nxt = x.nxt
        return x
        """

10-22-25

BST (Binary Search Tree or Binary Sorted Tree)

Makes data sorted and organized. Which makes it easier to search through.

self.root = the first item inserted or none when there is nothing.

nodes in BST have left, item, and right. Anyhting to the left and right of an item is considered a descendent. Also, if you pass in organized data, the BTS just makes a super long Linked List.
No Duplicates are allowed for BST
Depth = the longest chain from self.root to the lowest node.
Big O of BST = log_2 N -> log N
Depth of BST < 2 Actual Depth of BST (check if the actual depth of the BST is under 2* the best depth)

BST Delete -
deleting leaf node - just set its parents connection to None
deleting a node with one child - set children to nodes parent
deleting node with two children - go down the left side of the node once to reach it's one child, then grab the furthest far right node there and swap it with the node to be deleted then delete it.

New node code:

class Node:
    
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

def delete(self, item):
    if not self.exists(item): # makes sure item is actually in list
        return False
    self.deleteR(item, self.root) #recursive part
    return True

def deleteR(self, item, current):
    if item < current.item: # which path to take, if the item were looking for is bigger or smaller
        self.deleteR(item, current.left)
    elif:
        self.deleteR(item, current.right)
    else:
        #delete

10-31-25

Do the BST tree assignment