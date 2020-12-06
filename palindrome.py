# palindrome problem

s = "Able was I , ere I saw elba".lower()
# expression, loop, filter
s = "".join([st for st in s if st in "abcdefghijklmnopqrtsuvwxyz"])
print(s)
def isPal(s):
    if len(s)<=1:
        True
    else:
        return s[0]==s[-1] and isPal(s[1:-1])
isPal(s)
