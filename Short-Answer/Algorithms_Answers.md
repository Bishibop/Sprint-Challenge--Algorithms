#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n): the limit of the while loop grows at a rate of n**3 while the body
of the loop adds n**2 each iteration. This means you would have to 
iterate through the loop n times to hit the limit. 

(n**3)/(n**2) = n

b)

O(nlog(n)): The outer loop is a simple iteration so that's n. The inner
loop is log(n) because the iterator is doubling each time up to a fixed
limit (fixed in each iteration of the outer loop). Multiply these together
because the one loop is inside the other and you get o(nlog(n))

c)

O(n): Each call we recurse on a value 1 less than the original value.
This means we will recurse n times. The body of the recursion only does
an addition operation, so that only adds O(1) time each iteration, which
we drop.

## Exercise II


I would start on the first floor and drop an egg. If doesn't break,
I would double the floor number I am on and drop another egg. Each floor
that the egg doesn't break, I would double the floor and test again until
I reached a floor that the egg broke on. From here I would descend halfway
to the previous floor and test again. If the egg breaks, descend half way
again, and if it doesn't, go back up halfway. I would stop when I ran a
test that was opposite of an adjacent floor. Which ever of these two floors
had the egg that didn't break would be the desired floor 'f'. 

Runtime O(logn): Going up the floors until an egg broke would be O(logn)
becase we are doubling our floor nunber each iteration. Identifying the
floor between this floor and the next is also O(logn) because we are halving
our search space each iteration (binary search). Add these two steps together,
because each is only being performed once, and you get 2O(logn) which is
just O(logn).
