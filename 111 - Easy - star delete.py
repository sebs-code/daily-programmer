"""
Challenge #111  [Easy] star delete.

Description

Write a function that, given a string, removes from the string any * character,
or any character that's one to the left or one to the right of a * character. 
Examples:

"adf*lp" --> "adp"
"a*o" --> ""
"*dech*" --> "ec"
"de**po" --> "do"
"sa*n*ti" --> "si"
"abc" --> "abc"

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

def doIt(input):
    return [input[x] for x in range(0, len(input)) if input[x] != '*' and (x == 0 or input[x - 1]) != '*' and (x == len(input) - 1 or input[x + 1] != '*')]

print doIt(sys.argv[1])
