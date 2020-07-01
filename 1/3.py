a,b,c=eval(input("a,b,c"))
if a>b:
    pass
    if b>c:
        print("a")
    else:
        if a>c:
            print("a")
        else:
            print("c")
else:
    if b>c:
        print("b")
    else:
        print("c")
