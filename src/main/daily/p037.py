def pset(s):
    p = [[]]
    for e in s:
        p += [x + [e] for x in p]
    return p


print(pset([1, 2, 3, 4]))
