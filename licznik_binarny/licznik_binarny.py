
size = 4
arr = [0]*size
def licznik_binarny():
    i = 0
    global size
    while i < size and arr[i] == 1:
        arr[i] = 0 
        i += 1
    if i < size : 
        arr[i] = 1
    print(arr)
for x in range(7):
    licznik_binarny()