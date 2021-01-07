# You'll need to use a couple of built in functions to alphabetize a string. 
# Try to avoid looking up the exact answer and look at built in functions for
# lists and strings instead.
string = input("what do you want to reverse?: ")

def sort_alpha(string):
    array = []
    for l in string:
        array.append(l)
    print(("").join(sorted(array)))

sort_alpha(string)