
# regex = r'(\/\/).*(?=\s)|(\/\*\*)[.|\\n|\\r]*(\/\*\*)'
# regex = r"^/.+/$"
# regex =r"/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/"
# regex = r"/\*[\s\S]+?\*/|//[\s\S]*?$"

import sys
import re
regex = r'(?s)(?m)(//.*?$|/\*.*?\*/)'



pattern = re.compile( regex, re.DOTALL|re.MULTILINE)

if __name__ == '__main__':



    input_str = sys.stdin.read()

    # re.sub is to remvoe redundant whitespace character \n \t \r\ f in test case_#4
    print(
        "\n".join(
            re.sub(r"\n\s+", "\n", comment)
            for comment in re.findall(pattern, input_str)
        )
    )

