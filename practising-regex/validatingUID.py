# UID validator (from Hackerrank)

#A valid UID must follow the rules below:

#It must contain at least 2 uppercase English alphabet characters.
#It must contain at least 3 digits (0-9).
#It should only contain alphanumeric characters (0-9,a-z & A-Z).
#No character should repeat.
#There must be exactly  characters in a valid UID.


def main():
    
    import re

    tests = int(input("How many UIDs you would like to check? "))
    for _ in range(tests):
        text = input("Please insert your UID here: ")
        if re.search(r'^[0-9a-zA-Z]{10}$', text) and len(text) == len(set(text)):
            if re.search(r'[A-Z].*[A-Z]', text) and re.search(r'[0-9].*[0-9].*[0-9]', text):
                print('Valid')
            else:
                print('Invalid')
        else:
            print('Invalid')


if __name__ == "__main__":
    main()
