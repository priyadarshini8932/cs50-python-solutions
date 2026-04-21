def helper(x):
    if x.strip()=='42' or x.lower()=='forty-two' or x.lower()=='forty two':
        print("Yes")
    else:
        print("No")
def main():
    x= input("What is the Answer to the Great Question of Life, the Universe, and Everything")
    helper(x)

main()

