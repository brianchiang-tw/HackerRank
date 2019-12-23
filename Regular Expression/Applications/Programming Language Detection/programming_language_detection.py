import sys
import re

regex_c = r'(#include)'
regex_java = r'(public static void main)|(import java)'
regex_python = r"__name__ == '__main__'"

pattern_c = re.compile( regex_c )
pattern_java = re.compile( regex_java )
pattern_python = re.compile( regex_python )



if __name__ == '__main__':

    input_str = sys.stdin.read()

    c_main = re.findall(pattern_c, input_str)
    java_main = re.findall(pattern_java, input_str)
    python_main = re.findall(pattern_python, input_str)

    if len(c_main) != 0:
        print("C")
    elif len(java_main) != 0:
        print("Java")
    #elif len(python_main) != 0:
    else:
        print("Python")
    #else:
    #    print("INVALID")
