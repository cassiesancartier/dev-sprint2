# Enter your answers for chapter 6 here
# Name: Cassie Sancartier


# Ex. 6.6

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]        

middle('hi')
''

middle(' ')
''

def is_palindrome(word):
    if not isinstance (word, str):
        print "Please enter a string."
        return
    if len(word) < 2:
        return 'False'
    elif first(word) != last(word):
        return "False"
    while len(word) > 2:
      is_palindrome(middle(word))
      first(word) == last(word)
      return "True"  


# Ex 6.8

gcd(a, b) == gcd(b, r)

def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)        



















        

        