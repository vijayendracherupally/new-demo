while(1):
    try:
        age=int(input())
        if(age >= 18):
            print("Eligible")
        else:
            print("Not eligble")
    except:
        print("Input is not numeric")