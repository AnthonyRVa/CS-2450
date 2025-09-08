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


