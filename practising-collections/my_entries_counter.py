
def main():

    from collections import Counter

    number_of_words = int(input("How many entries would you like to enter? Please write a number here: "))

    my_dict = {}
    for n in range(0, number_of_words):
        my_dict[n]= input(f"Entry number {n+1}: ")
    my_counter = Counter(my_dict.values())
    print(f"You entered {len(my_counter.keys())} different entries")
    print("Here is the number of occurences for each entry according to their order of appearance in the input:", *my_counter.values())


if __name__=="__main__":
    main()