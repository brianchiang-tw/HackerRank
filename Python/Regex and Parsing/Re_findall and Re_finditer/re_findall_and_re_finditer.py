# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':

    input_str = input()

    vowel = "aeiouAEIOU"
    consonant = "^aeiouAEIOU"

    result = re.finditer(r'((?<=[%s])[%s]{2,}(?=[%s]))'% (consonant, vowel, consonant), input_str )

    all_matches = list( map( lambda x:x.group(), result ) )

    if len(all_matches) != 0:

        for m in all_matches:

            print( m )

    else:
        print("-1")
