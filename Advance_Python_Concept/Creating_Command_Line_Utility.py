import argparse

def find_mul(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

if __name__ == '__main__':
    # Create a parser object
    parser = argparse.ArgumentParser(description="A program for addition and multiplication.")

    # Add arguments for addition and multiplication
    parser.add_argument("--add", nargs='*', metavar="num", type=int,
                        help="All the numbers separated by spaces will be added.")
    
    parser.add_argument("--mul", nargs='*', metavar="multiply", type=int,
                        help="All the numbers separated by spaces will be multiplied.")

    # Parse the arguments from standard input
    args = parser.parse_args()

    # Check if add argument has any input data and print the sum
    if args.add:
        print("Sum of the numbers:", sum(args.add))
    
    # Check if mul argument has any input data and print the product
    if args.mul:
        print("Product of the numbers:", find_mul(args.mul))
