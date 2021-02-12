def main():

    print("Hey handsome, I am a leap year calculator. Try me...")

    year = int(input("Please insert the year here: "))

    if year >= 1582:

        if year%4 == 0:
            if year%400 == 0:
                print(True)
            elif year%100 == 0 and year%400 != 0:
                print(False)
            else:
                print(True)
        else:
            print(False)

    else:
        print("The Gregorian calendar was only introduced in 1582.")
        print("Please try again.")


if __name__=='__main__':
    main()
