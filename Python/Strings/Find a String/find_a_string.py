def count_substring(string, sub_string):

    occurrence_of_substr = 0

    while True:

        start_index_of_substr = string.find( sub_string)
        if  start_index_of_substr != -1:

            # update occurrence of substring
            occurrence_of_substr += 1

            # truncate the current finding, string keeps searching forward
            string = string[ start_index_of_substr+1: ]

        else:
            break

    return occurrence_of_substr

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)