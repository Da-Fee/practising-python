"""(from Hackerrank) You are given a positive integer N.
   Your task is to print a palindromic triangle of size N. """


def main():

    for n in range(1, int(input())+1):
        print(int(((10**n-1)/9)**2))

if __name__ == "__main__":
	main()