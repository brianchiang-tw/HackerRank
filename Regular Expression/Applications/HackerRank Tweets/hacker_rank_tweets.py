import re

regex = r'hackerrank'

pattern = re.compile( regex )

if __name__ == '__main__':

    n = int( input() )

    key_word_count = 0

    for _ in range(n):

        input_str = input().lower()

        result = re.findall( pattern, input_str )

        key_word_count += len(result)

    print( key_word_count )