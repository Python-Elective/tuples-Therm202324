"""
Write a function called skip_tuples. It has a tuple as input. 
It returns a new tuple as output, 
such as every second element of the input tuple is skipped, starting with the first one.
Put your testcases in main()
Test-case:
input_tuple (tuple): The input tuple to process.
Returns:
    - tuple: A new tuple with every second element skipped.
Example:
skip_tuples(('I', 'am', 'a', 'test', 'tuple'))
('I', 'a', 'tuple')
"""
# def skip_tuples(input_tuple):
#     new = input_tuple[::2]
#     return new
# # return input_tuple[::2]
# def main():
#     # Test cases
#     input_tuple_1 = ('I', 'am', 'a', 'test', 'tuple')
#     output_tuple_1 = skip_tuples(input_tuple_1)
#     print(f"Input: {input_tuple_1}\nOutput: {output_tuple_1}\n")
#     input_tuple_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#     output_tuple_2 = skip_tuples(input_tuple_2)
#     print(f"Input: {input_tuple_2}\nOutput: {output_tuple_2}\n")
#     input_tuple_3 = ('a', 'b', 'c', 'd', 'e', 'f')
#     output_tuple_3 = skip_tuples(input_tuple_3)
#     print(f"Input: {input_tuple_3}\nOutput: {output_tuple_3}\n")
# if __name__ == "__main__":
#         main()

def main():
    # Test cases
    input_tuple_1 = ('I', 'am', 'a', 'test', 'tuple')
    output_tuple_1 = skip_tuples(input_tuple_1)
    print(f"{output_tuple_1}")

    input_tuple_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    output_tuple_2 = skip_tuples(input_tuple_2)
    print(f"{output_tuple_2}")

    input_tuple_3 = ('a', 'b', 'c', 'd', 'e', 'f')
    output_tuple_3 = skip_tuples(input_tuple_3)
    print(f"{output_tuple_3}")

def skip_tuples(t):
    new = t[::2]
    return new

if __name__ == "__main__":
        main()