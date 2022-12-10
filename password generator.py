import string
import random
while True:
    print("For Quitting, \"Enter Your Password Length: 50\"")
    print()
    if __name__ == "__main__":
        s1=string.ascii_lowercase
        s2=string.ascii_uppercase
        s3=string.digits
        s4=string.punctuation
        plen=int(input("Enter Your Password Length:  "))
        if plen==50:
            print("(\"Game Over\")")
            break
        else:
            s=[]
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            print("Your Password is: ")
            print("".join(random.sample(s,plen)))
            print("\n\n")