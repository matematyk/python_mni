def wez_slowo(file): 
    with open(file) as f:
        for x in f:
            for word in x.split(" "):
                yield word
g = wez_slowo("test.txt")
print(next(g))
print(next(g))
print(next(g))
