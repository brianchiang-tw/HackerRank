# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt

if __name__ == '__main__':

    average_of_population = 500
    std_of_population = 80

    sample_size = 100

    z_score = 1.96

    std_of_sample_mean = std_of_population / sqrt(sample_size)
    avg_of_samepl_mean = average_of_population

    upper_bound = avg_of_samepl_mean + z_score * std_of_sample_mean
    lower_bound = avg_of_samepl_mean - z_score * std_of_sample_mean

    print( round(lower_bound, 2) )
    print( round(upper_bound, 2) )