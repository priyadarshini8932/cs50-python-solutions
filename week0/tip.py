def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #todo
    x=float(d[1:])
    return round(x,1)

def percent_to_float(p):
    #todo
    x=float(p[:-1])
    return x/100


main()