"""This code contains a series of functions that can be used for statistical analysis"""
import random
import math

def arithmetic_mean(list_of_vals):
    """This function returns the arithmetic_mean of a list of values"""
    mean = 0.0
    for number in list_of_vals:
        mean+=number
    return mean/len(list_of_vals)

def pop_variance(population_list):
    """Returns the population variance of a list"""
    if(len(population_list)<1):
        return
    mean = arithmetic_mean(population_list)
    var_list=[]
    for person in population_list:
        var_list.append((person-mean)**2)
    return arithmetic_mean(var_list)

def sample_variance(population_list):
    """Returns pop_variance, multiplied by n/(n-1) where n is the sample size"""
    if(len(population_list)<1):
        return
    if(len(population_list)==1 and population_list[0]==0):
        return
    return pop_variance(population_list)*float(len(population_list))/float(len(population_list)-1)

def lower_median(median_list):
    """Returns the median, biased down if the list length is even"""
    return_val = 0
    sorted_list=sorted(median_list)
    length=len(sorted_list)
    if(length < 1):
        return
    if(length%2==0):
        return_val = (sorted_list[length/2-1])
    else:
        return_val = sorted_list[length/2]
    return return_val
#ajsfajdkljaslk
def random_sample(data,sample_size):
    """Returns a random sample of data, size of sample_size, no repeats"""
    return_list=[]
    data_list = list(data)
    for num in range(sample_size):
        print(num)
        return_list.append(data_list.pop(random.randrange(len(data_list))))
    return return_list

def hist_data(score_list):
    """Returns a histogram data list, first element of list is number of elements in sample within 1-20, second is 21-40, etc."""
    return_list=[0,0,0,0,0]
    for num in score_list:
        return_list[int(num / 20)]+=1
    return return_list

def sma(value_list,avg_size):
    """Returns a 'moving average' of size avg_size"""
    temp_list=[]
    return_list=[]
    if(len(value_list)<=avg_size):
        return_list.append(arithmetic_mean(value_list))
        return return_list
    for num in range(len(value_list) - avg_size + 1):
        temp_list=[]
        for iterator in range(num,num + avg_size):
            temp_list.append(value_list[iterator])
        return_list.append(arithmetic_mean(temp_list))
    return return_list

def one_sample_t_test(num_list, sample_size):
    """Returns the results of a one sample t test, using a random sample of sample_size. Returns the results of the test and the random sample"""
    if(len(num_list)<1 or sample_size<1):
        return (None,[])
    rand_sample = random_sample(num_list,sample_size)
    try:
        std_full_data_set = math.sqrt(pop_variance(num_list))
        standard_deviation = math.sqrt(sample_variance(rand_sample))
        sample_mean = arithmetic_mean(rand_sample)
        z_value = sample_mean / (std_full_data_set / math.sqrt(len(rand_sample)))
        t_value = z_value / standard_deviation
    except ZeroDivisionError:
        return (None, rand_sample)
    return t_value , rand_sample

