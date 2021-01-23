
def Fibonacci_loop_rabbits(months, offsprings):
    """
    1. Initially assign 1 parent and one child. This is the first set of offspring.
    2. Loop over the number of months (minus 1 - we already had the first month)
    3. The child becomes a parent, so given a new value (still 1)
    4. The child value is now the  parent, plus the previous child x the new offspring that they produce
    """
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    print(child)
    return child


Fibonacci_loop_rabbits(30, 2)

# o - small rabbits - have to mature and reporduce in the next cycle only
# O - mature rabits - They can reproduce and move to the next cycle

"""
Month 1: [o]
Month 2: [O]
Month 3: [O o o]
Month 4: [O o o O O]
Month 5: [O o o O O O o o O o o]

"""
