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
    git pull --no-rebase
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

