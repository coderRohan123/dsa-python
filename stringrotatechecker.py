class Solution(object):
 def rotateString(self, A, B):
     if len(A) != len(B):
          return False
     if len(A) == 0:
         return True
     for s in xrange(len(A)):
            if all(A[(s+i) % len(A)] == B[i] for i in xrange(len(A))):
                   return True
     return False
print(rotateString("abcde","cdeab"))

'''This code checks if string A can be rotated to match string B by iterating through all 
possible rotations of A and comparing each rotation to B.
This code snippet defines a class Solution with a method rotateString that takes two 
objects A and B as input. It checks if the length of each object 
is equal to or contains zero elements in both arrays, 
returning False otherwise. The function returns True'''