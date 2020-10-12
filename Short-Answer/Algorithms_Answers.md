#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The running time is O(n) because n * n * n / n * n simplifies down to n.


b) The running time is O(nlog(n)) although the outer loop is O(n), the inner loop is O(log(n)) due to j doubling in every iteration.


c) The running time is O(n) because for each bunny there is one recursion.

## Exercise II

Use binary search to determine the value of f, by dividing by n, in a search for f where any f below will not break the eggs, but any floor above will break the eggs.

Start at floor n/2

If the egg breaks, go halfway down, to floor n/4

If the egg doesn't break, go to floor 3n/4

Do this until the egg does not break at floor f, and f+1 the egg does break
