# A program to calculate the number of vowels in a given string.
import re
from collections import Counter


def count_vowels(text):
    """"Return the number of occurrences of each vowel in a given string."""
    # Declare and initialize the counts.
    counta, counte, counti, counto, countu = 0, 0, 0, 0, 0
    # Define a regex containing the vowels.
    regex = re.compile(r'[aeiouAEIOU]')
    # Create a list containing the vowels.
    vowels = regex.findall(text)
    # Scan the list and determine the respective counts of each vowel.
    for i in vowels:
        if str(i).lower() == 'a':
            counta += 1
        elif str(i).lower() == 'e':
            counte += 1
        elif str(i).lower() == 'i':
            counti += 1
        elif str(i).lower() == 'o':
            counto += 1
        elif str(i).lower() == 'u':
            countu += 1
    # Compute the total sum of the vowels found.
    total = counta + counte + counti + counto + countu
    # Create a list of the counts.
    counts = ["# of A's = " + str(counta), "# of E's = " + str(counte),
              "# of I's = " + str(counti), "# of O's = " + str(counto),
              "# of U's = " + str(countu), "Total vowel count = " + str(total)]
    # Return the list of counts.
    return counts


def count_vowels_alt(text, charset='aeiou'):
    """Same as above function but using an alternative implementation."""
    counter = Counter(text.lower())
    return {vowel: counter[vowel] for vowel in charset}


# Test the function using a semi-large text file
file = open('C:\\Users\\Ahmed\\Documents\\Story.txt')
content = file.read()
print(count_vowels(content))
print(count_vowels_alt(content))
