import re

def main():
    regex_pattern = r"^(M{1,3})?(((C{0,3})|(CD)|(D(C{0,3}))|(CM))?((XC)|(L(X{0,3}))|XL|(X{1,3}))?((I{1,3})|" \
                    r"(IV)|(V(I{0,3}))|(IX))?)$"
    entry = input("Please enter the string here: ").upper()
    print(str(bool(re.match(regex_pattern, entry))))

if __name__ == '__main__':
    main()