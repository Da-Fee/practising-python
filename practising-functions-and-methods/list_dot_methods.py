def main():


    my_list = []
    actions = {0: {'pop': list.pop, 'print': print, 'reverse': list.reverse, 'sort': list.sort},
               1: {'append': list.append, 'remove': list.remove},
               2: {'insert': list.insert}}

    n_commands = int(input("""Here is an empty list and you can decide how many operations you would
                          like to run on it. Please enter the number here: """))

    print("""You can perform the following commands:
             1. insert i e: Insert integer e at position 1.
             2. print: Print the list.
             3. remove e: Delete the first occurrence of integer e.
             4. append e: Insert integer e at the end of the list.
             5. sort: Sort the list.
             6. pop: Pop the last element from the list.
             7. reverse: Reverse the list.""")


    for n in range(0, n_commands):
        [*args] = input().split()
        if len([*args]) == 1:
            actions[0][[*args][0]](my_list)
        elif len([*args]) == 2:
            actions[1][[*args][0]](my_list, (int([*args][1])))
        elif len([*args]) == 3:
            actions[2][[*args][0]](my_list, (int([*args][1])), (int([*args][2])))

    print(f"Here is your list {my_list}")


if __name__=='__main__':
    main()
