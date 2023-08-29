def Task1(a,b):
    try:
        print(a+b)
    except:
        print("TypeError please provide integer values as parameters")

def Task2():
    try:
        a=int(input())
        print(f"The number is {a}")
    except KeyboardInterrupt:
        print("keyboard error")
    except:
        print("invalid input retry again")
    
def Task3(filename):
    try:
        fil=open(filename)
        for i in fil:
            print(i)
    except UnicodeDecodeError:
        print("Wrong Encoding of the file try giving txt files etc.")

def Task4():
    try:
        l=[1,2,3,4]
        print(l.indexOf(1,2))
        print(len(l))
    except AttributeError:
        print("Attribute error")

    finally:
        print(*l)