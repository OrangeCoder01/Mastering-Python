def additional_digit_detector(n_new):
    return len(str(n_new)) > 1
    
    
def digit_summming(n):
    n_int_arr = []
    n_str = str(n)

    for char in n_str:
        n_int_arr.append(int(char))   
    
    summing = sum(n_int_arr)
        
    return summing


def digit_root(n):
    final_sum = n
    
    while additional_digit_detector(final_sum):
        final_sum = digit_summming(final_sum)
        
    return final_sum
    
        

print(digit_root(458))
