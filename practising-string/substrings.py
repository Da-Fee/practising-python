
"""

Consider the following exercise (Merge the tools) from Hackerrank:

A string, S, of length N
An integer, K, where K is a factor of N.
We can split S into N/K substrings where each subtring, T, consists of
a contiguous block of K characters in S. Then, use each T to create string U
such that:

The characters in U are a subsequence of the characters in T.
Any repeat occurrence of a character is removed from the string such that
each character in U occurs exactly once. In other words, if the character
at some index J in T occurs at a previous index <J in T, then do not include 
the character in string U.
Given S and K, print N/K lines where each line I denotes string u.


"""

def main():

	string = input()
	sub_len = int(input()) # asking the user the length of the sub-strings
	sub_num = int(len(string)/sub_len) # getting the number of sub-strings

	if sub_len == 1: 
		for s in string:
			print(s)
	else:
		for enum, ran in enumerate(range(0, sub_num), start=1): # creating two ranges of identical length but ...
		                                                        # ... different starting point to use in the for loop
			sub_string = (string[(sub_len*ran):(sub_len*enum)]) # the elements of the ranges above are used to slice ...
			                                                    # ... the string and make the substrings
			my_list = []
			for l in sub_string:
				if l in my_list:
					continue
				else:
					my_list.append(l)
			print(''.join(my_list))


if __name__ == '__main__':
	main()












