def helper(x):
    if x.startswith("hello"):
        return "$0"
    elif x.startswith("h"):
        return "$20"
    else:
        return "$100"


def main():
    x=input("Greeting: ")
    x=x.lower().strip()
    y=helper(x)
    print(y)
main()
