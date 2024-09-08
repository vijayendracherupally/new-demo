d=dict()
for i in range(5):
    try:
        age=int(input("Enter your age:"))
        if(age  < 0):
            if(d.get("invalid") == None):
                d["invalid"]=1
            else:
                d["invalid"]=d["invalid"]+1
            raise Exception("Age cannot be negative")
        elif():
            print
    except:
        print