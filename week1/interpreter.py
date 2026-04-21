def helper(val):
    x,y,z=val.split(" ")

    if y=="+":
        print(float(x)+float(z))
    elif y=="-":
        print(float(x)-float(z))
    elif y=="*":
        print(float(x)*float(z))
    elif y=="/":
        print(float(x)/float(z))

def main():
    val= input("Expression: ")
    helper(val)

main()
