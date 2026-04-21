def main():
    x=input("What time is it?")


    ans=convert(x)
    if 7<=ans<=8:
        print("breakfast time")
    elif 12<=ans<=13:
        print("lunch time")
    elif 18<=ans<=19:
        print("dinner time")

def convert(time):
    time.split(":")
    x=time.split(":")[0]
    y=time.split(":")[1]
    ans=float(x)+float(float(y)/60)
    return ans



if __name__ == "__main__":
    main()
