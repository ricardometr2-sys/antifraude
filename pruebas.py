while True:
    try:
        x=int(input("N: "))
        if x>10:
            raise Exception
        break
    except:
        print("error")

print(x)



