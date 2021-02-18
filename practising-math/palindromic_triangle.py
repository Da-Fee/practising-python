"""(from Hackerrank) You are given a positive integer N.
   Your task is to print a palindromic triangle of size N. """


def main():

    for n in range(1, int(input())+1):
        xx = list(range(1, n)) + list(range(n, 0, -1))
        print(sum([xx[l] * (10 ** (len(xx) - 1 - l)) for l in range(0, len(xx))]))

if __name__ == "__main__":
	main()