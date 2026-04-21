#1
#a)
temperatures = [72, 75, 68, 79, 71, 73, 78]
sum(temperatures())
total_value = sum(temperatures)
print(total_value)

#b)
counter = 0
for i in temperatures:
    counter += i
print(counter)

#c)
my_list = []
for i in temperatures:
    if i > 74:
        my_list.append(i)
print(my_list)

#2]

my_friend = "Julie"
def friend_calling(name):
    print("Old friend inside function: ", my_friend)
    print("New friend inside function: ", name)
friend_calling(name = "Kate")



#3

def collect_number_list():
    positive_list = [] #empty list for storing positives
    while True:
        input_val = int(input("Please type a non-negative integer: "))
        if input_val > 0:
            positive_list.append(input_val)
        elif input_val < 0:
            print("got a negative integer.")
            break

    #calc min, max, and how many nums in list
    count = len(positive_list) #len will return non-negative value
    if count > 0:
        min_val = min(positive_list)
        max_val = max(positive_list)
    else: #empty
        print("positive list is empty")
        min_val = None
        max_val = None

    return min_val, max_val, count

output1, output2, output3 = collect_number_list()
print(output1, output2, output3)