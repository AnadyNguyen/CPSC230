def collect_number_list():
    positive_list = []
    while True:
        input_val = int(input("type in a non-negative integer"))
        if input_val > 0:
            positive_list.append(input_val)
        elif input_val <= 0:
            print("please type in a positive integer")
        count = len(positive_list)
        if not positive_list:
                print("positive_list is empty")
                min_val = None
                max_val = None
        else:  
            min_val = min(positive_list)
            max_val = max(positive_list)
        break
        print(positive_list)
    return min_val, max_val, count
        



collect_number_list()