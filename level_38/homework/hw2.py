num=[12,2,15,55,12,71,64]

def big_num(num_list):
    max_number=num_list[0]

    for i in range(len(num_list)):
        if max_number > num_list[i]:
            max_number = num_list[i]

    return max_number

print(big_num(num))