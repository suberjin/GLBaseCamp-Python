# define objects
program_description = """
==============================================================================
  Hello. This program counts amount of holes in numbers. Input data should
contain the numbers only. Please note that incorrect input data will return
the "error". If the first symbol is zero, it will be ommited
==============================================================================
"""


# Function gets input string as argument and returns the number of holes
def count_holes(input_string):
    holes = {"0": 1, "1": 0, "2": 0, "3": 0, "4": 1,
             "5": 0, "6": 1, "7": 0, "8": 2, "9": 1}
    holes_sum = 0

    formatted_string = str(int(input_string))

    for i in range(len(formatted_string)):
        holes_sum += holes[formatted_string[i]]

    return holes_sum

print(program_description)

# Ask user to input the number
input_string = input("Enter number: ")

# Check if data has only digit symbols or rise the error.
if input_string.isdigit():
    print(f"Number has {count_holes(input_string)} holes.")
else:
    print("error")
    exit(128)
