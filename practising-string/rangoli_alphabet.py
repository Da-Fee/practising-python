def main():


    def print_rangoli(size):
        import string

        alphabet = list(string.ascii_lowercase)
        alphabet_slice = alphabet[:size]
        alphabet_slice.reverse()
        z_a_module = '-'.join(alphabet_slice)


        if size >= 2 and size < 27:
            for x in range(0, (size * 2), 2):
                if x < (size * 2) - 2:
                    part1 = ("-" * ((2 * (size - 1)) - x)) + z_a_module[:(x + 2)]
                    part_temp = part1[:-3]
                    part2 = part_temp[len(part_temp)::-1]
                    print(part1 + part2)
                elif x == (size * 2) - 2:
                    part1 = ("-" * ((2 * (size - 1)) - x)) + z_a_module[:(x + 2)] + "-"
                    part_temp = part1[:-3]
                    part2 = part_temp[len(part_temp)::-1]
                    print(part1 + part2)
                    for x in reversed(range(0, (size * 2) - 2, 2)):
                        if x < (size * 2) - 2:
                            part1 = ("-" * ((2 * (size - 1)) - x)) + z_a_module[:(x + 2)]
                            part_temp = part1[:-3]
                            part2 = part_temp[len(part_temp)::-1]
                            print(part1 + part2)
                        elif x == (size * 2) - 2:
                            part1 = ("-" * ((2 * (size - 1)) - x)) + z_a_module[:(x + 2)] + "-"
                            part_temp = part1[:-3]
                            part2 = part_temp[len(part_temp)::-1]
                            print(part1 + part2)
        elif size == 1:
            print("a")
        else:
            print("The smallest possible size is 1, the biggest is 26. Please try again.")
            pass


    size = int(input("Please provide the size of the desired Ragoli Alphabet: "))
    print_rangoli(size)


if __name__=="__main__":
    main()
