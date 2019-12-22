import re
import sys

regex_question_num = r'(?<=question\-summary-).*?(?=">)'
regex_question_title = r'(?<=question\-hyperlink">).*?(?=<\/a>)'
regex_question_time = r'(?<=relativetime">).*(?=<\/span>)'

pattern_question_num = re.compile( regex_question_num )
pattern_question_title = re.compile( regex_question_title ) 
pattern_question_time = re.compile( regex_question_time )

if __name__ == '__main__':

    input_str = sys.stdin.read()

    result_qid = re.findall( pattern_question_num, input_str )
    result_qtitle = re.findall( pattern_question_title, input_str )
    result_qtime = re.findall( pattern_question_time, input_str )

    question_tuple = zip( result_qid, result_qtitle, result_qtime)

    for q in question_tuple:
        print( ';'.join(q) )
