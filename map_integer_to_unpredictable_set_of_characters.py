import random

# usually I need to have a rather unpredictable public ID that maps 
# to an ID in the database so I don't reveal the ID directly from the database.

# a solution I found handy was as the code below.

# map the number of bits you need to represent your integer space

mapping = list(range(36)) # <- 36 is the number of chars in our charachter set
mapping.reverse()

# uncomment to create random mappings
# -------------------------------------
# random.shuffle(mapping) 

# alphabet for changing from base 10
chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

# shuffle the bits
def encode(n):
    result = 0
    for i, b in enumerate(mapping):
        b1 = 1 << i
        b2 = 1 << mapping[i]
        if n & b1:
            result |= b2
    return result

# unshuffle the bits
def decode(n):
    result = 0
    for i, b in enumerate(mapping):
        b1 = 1 << i
        b2 = 1 << mapping[i]
        if n & b2:
            result |= b1
    return result

# change the base
def enbase(x):
    x=int(x)
    n = len(chars)
    if x < n:
        return chars[x]
    return enbase(x/n) + chars[x%n]

# change back to base 10
def debase(x):
    n = len(chars)
    result = 0
    for i, c in enumerate(reversed(x)):
        result += chars.index(c) * (n**i)
    return result


# usage:

for a in range(250):
    b = encode(a)
    c = enbase(b)
    d = debase(c)
    e = decode(d)

    print ('id:{} encode:{}   enbase:{}    debase:{}    decode:{}'.format(a, b, c, d, e))

