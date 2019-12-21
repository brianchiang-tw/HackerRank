import re


regex = r'''(?:(?:"|'|=)http(?:s?):\/\/)(?:www\.)?([-a-zA-Z0-9\.]*)(?=\/|\?|")'''

pattern = re.compile( regex )

if __name__ == '__main__':

    domain_list = []

    n = int( input() )

    for _ in range(n):

        input_str = input()

        result = re.findall( pattern, input_str )

        result = list( dict().fromkeys( result ) )

        domain_list += [ domain for domain in result if domain not in domain_list and domain.count('.') != 0 ]

    
    domain_list.sort()

    output_str = ';'.join( domain_list )

    print( output_str )



def debug_and_trace():

    domain_list = []

    find_domain_flag = False

    with open('.\\input_0.txt', 'r') as f :

        for line in f:
            


            result = re.findall( pattern, line )

            result = list( dict().fromkeys( result ) )
            domain_list += [ domain for domain in result if domain not in domain_list and domain.count('.') != 0 ]

    
        domain_list.sort()



        for d in domain_list:
            print( d )


    print()
    print()

    ## Corrected answer offered by online judge

    answer = '''b.scorecardresearch.com;books.rediff.com;careers.rediff.com;clients.rediff.com;datastore.rediff.com;datastore01.rediff.com;datastore04.rediff.com;datastore05.rediff.com;dealhojaye.rediff.com;hosting.rediff.com;ia.rediff.com;im.rediff.com;imshopping.rediff.com;imworld.rediff.com;investor.rediff.com;ishare.rediff.com;loc.rediff.com;login.rediff.com;mail.rediff.com;metric.ind.rediff.com;money.rediff.com;mypage.rediff.com;n01.rcdn.in;news.rediff.com;pages.rediff.com;realtime.rediff.com;rediff.com;register.rediff.com;search.rediff.com;shopping.rediff.com;simg.rcdn.in;simg03.rcdn.in;track.rediff.com;w3.org;zarabol.rediff.com'''

    answer_list = answer.split(';')

    for a in answer_list:

        print( a )