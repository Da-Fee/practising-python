"""(from Hackerrank) You are given a positive integer N.
   Your task is to print a palindromic triangle of size N. """


def main():

    my_int = int(input())
    my_dict = {}
    my_list = list(range(1, my_int + 1))
    for n in range(1, my_int + 1):
        if n in my_list:
            my_dict[n] = my_list[0:n]
            my_dict[n] += list(range(n-1, 0, -1))
            for l in range(0, len(my_dict[n])):
                my_dict[n][l] = my_dict[n][l] * ((10) ** (len(my_dict[n]) - 1 - l))
            my_dict[n] = sum(my_dict[n])
            print(my_dict[n])

if __name__ == "__main__":
	main()