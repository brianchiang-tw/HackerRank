import re

regex = r'^([0-9]{4,5}) ([A-Z]{1,10})$'
pattern = re.compile( regex )

lang_list = ['C', 'CPP', 'JAVA', 'PYTHON', 'PERL', 'PHP', 'RUBY', 'CSHARP', 'HASKELL', 'CLOJURE', 'BASH', 'SCALA', 'ERLANG', 'CLISP', 'LUA', 'BRAINFUCK', 'JAVASCRIPT', 'GO', 'D', 'OCAML', 'R', 'PASCAL', 'SBCL', 'DART', 'GROOVY', 'OBJECTIVEC']


if __name__ == '__main__':

    n = int( input() )

    for _ in range( n ):

        input_str = input()

        field = re.match( pattern, input_str )

        if field is None:
            print("INVALID")
            continue

        else:

            if not (100000 >= int( field.group(1) ) >= 10000):
                print("INVALID")
                continue

            if field.group(2) not in lang_list:
                print("INVALID")
                continue

            print("VALID")
