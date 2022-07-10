import itertools
a_string = '123456789'
string_permutations = itertools.permutations(a_string)
string_permutations = list(string_permutations)
string_permutations = [''.join(permutation) for permutation in string_permutations]
print(string_permutations)