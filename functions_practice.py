def hello():
    print("Greetings! Welcome to the program.")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)

# Call the hello() function
hello()

# Call the pack() function with three arguments and print the result
result = pack("apple", "banana", "orange")
print(result)

# Call the eat_lunch() function with different food lists
eat_lunch([])
eat_lunch(["sandwich", "chips", "apple"])
eat_lunch(["salad"])
