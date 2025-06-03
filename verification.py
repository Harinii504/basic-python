def verification(a):
    dig =sim=up=lo= False
    if not (8<=len(a)<=10):
        return False
    for i in a:
        if i.isalpha():
            if i.isupper():  up = True
            else: lo = True
        dig= i.isdigit()
        if i in "@_":
            sim = True
    if sim and dig and up and lo:
        return True
    return False
a = input()
print( verification(a) )
