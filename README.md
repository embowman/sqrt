# Square Root Algorithm

This is the culmination of a speck of curiosity in algorithms for finding
square roots. I've performed some light research and realized how decrepit
my math skills have become 😂

In the provided examples, I've arbitrarily decided to search
for a whole number that when squared is less than one quadrillion:
- 31,622,776^2 = 999,999,961,946,176

One could naively iterate through every number until that number squared
equals the radicand, but we can easily improve upon that with a simple
binary search. The binary method results in 50 iterations to find this
square root, which is obviously much better than the naive approach

Newton's method improves even further, requiring only 30 iterations

Finally, Halley's method solves the problem with only 19 iterations
