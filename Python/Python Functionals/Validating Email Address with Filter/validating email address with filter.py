def fun(s):
    # return True if s is a valid email, else return False
    '''

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The maximum length of the extension is 3.
    '''

    #print("current email to be judged: {}".format(s) )
    # check @ and . existance
    if s.find('@') == -1 or s.find('.') == -1 :
        return False
    # screen out repetition of '@' or '.'
    if s.count('@') > 1 or s.count('.') > 1:
        return False

    tokens = s.split('@')
    username, tail = tokens[0], tokens[1]

    # avoid empty string in username or tail
    if len(username) == 0 or len(tail) == 0 :
        return False


    for x in username:

        if( x.isalpha() is not True and x.isdigit() is not True and x != '-' and x != '_'):
            return False


    buf = tail.split('.')
    website, extension = buf[0], buf[1]

    for x in website:

        if( x.isalpha() is not True and x.isdigit() is not True):
            return False

    if len(extension) > 3:
        return False


    return True



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)