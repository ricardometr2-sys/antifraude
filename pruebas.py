while True:
    try:
        x=int(input("N: "))
        if x>10:
            raise Exception
        print(x)
        break
    except:
        print("Error")



