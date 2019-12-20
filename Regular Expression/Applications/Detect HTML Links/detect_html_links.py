import re

def parse_link_and_text( s ):

    # for html link
    regex_link = r'(?<=<a href=\")([\S]*)(?=\")'


    # for html text for html link
    regex_text = r'(?<=\">)(?:<b>)*(.*?)(?=</)'

    pattern_link = re.compile( regex_link )
    pattern_text = re.compile( regex_text )

    #match_link = re.search(pattern_link, s)
    match_link = re.finditer( pattern_link, s)
    match_text = None
    
    for m_link in match_link:


        if m_link is not None:
            match_text = re.search(pattern_text, s[m_link.span()[1]:] )

            print( m_link.group(1) ,end = ',')

        if '="' in match_text.group(1):
            pass
        else:
            print( match_text.group(1).lstrip() )
        #if match_text is not None:
            


    return



if __name__ == '__main__':

    n = int( input() )
    # instantiate the parser and fed it some HTML


    for _ in range( n ):

        input_str = input()

        parse_link_and_text( input_str ) 
