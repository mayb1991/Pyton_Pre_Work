#Question 1
def hello_name(user_name):
    name = input("Please enter your user name: ")
    user_name = name 
    print("Hello " + name)
hello_name("mayb1991")

#Question 2
def first_odd():
    for odd in range(1,101,2):
        print(odd)
first_odd()

#Question 3
def max_num_in_list(a_list):
    max_num = a_list[ 0 ]
    for i in a_list:
        if i > max_num:
            max_num = i
    return max_num
print(max_num_in_list([1, 2, 5, 10, 25, 800, 5000]))


#Question 4
def is_leap_year(a_year):
    leap_year = False
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        leap_year = True
    elif (a_year % 100 == 0) and (a_year % 400 != 0):
        leap_year = False
    elif (a_year % 400 == 0):
        leap_year = True
    else:
        leap_year = False
    return leap_year
print(is_leap_year(2024))

#question 5
def is_consecutive(a_list):
    if len(a_list) < 1:
        return False
    min_num = min(a_list)
    max_num = max(a_list)
    if max_num - min_num + 1 == len(a_list):
        for i in range(len(a_list)):
            if a_list[i] < 0:
                j = -a_list[i] - min_num
            else:
                j = a_list[i] - min_num
                if a_list[j] > 0:
                    a_list[j] = -a_list[j]
                else:
                    return False
                return True
    return False
nums = [1, 2, 3, 4, 5]
print(is_consecutive(nums))