#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
  The while loop has to run N times, because we are increasing A by n^2

b) log(n)
  Problem perfectly describes creating a limit and growing exponentially to the limit.
  What we care about is the heighth of the exponential tree we need to get to N.

c) O(n)
We don't call bunnyEars on 2 + bunnyEars(bunnies-1), we call it on bunnies - 1. The 2 + is ignored

## Exercise II

A building in this case is a sorted list, and we can treat broken eggs and not broken eggs as larger and smaller. I would find the midpoint between number of floors and first floor, check if breaks. If breaks, find the midpoint between mid and bottom, check again. Binary search. O(log n)


