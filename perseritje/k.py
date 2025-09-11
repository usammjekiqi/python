import logging

logging.basicConfig(
    filename='calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class InvalidOperatorError(Exception):
    pass


operators = {
    '+': lambda *args: sum(args),
    '-': lambda *args: args[0] - sum(args[1:]),
    '*': lambda *args: prod(args),
    '/': lambda *args: div(args),
    '**': lambda *args: exp(args),
    '//': lambda *args: floor_div(args)
}


def prod(args):
    result = 1
    for num in args:
        result *= num
    return result


def div(args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result /= num
    return result


def exp(args):
    result = args[0]
    for num in args[1:]:
        result **= num
    return result


def floor_div(args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Floor division by zero is not allowed.")
        result //= num
    return result


def calculate_from_input(user_input):
    try:
        tokens = user_input.strip().split()
        if len(tokens) < 2:
            raise ValueError("Insufficient input. Provide numbers followed by an operator.")

        *num_tokens, operator = tokens

        # Convert to float or int
        numbers = []
        for token in num_tokens:
            if '.' in token:
                numbers.append(float(token))
            else:
                numbers.append(int(token))

        if operator not in operators:
            raise InvalidOperatorError(f"Operator '{operator}' is not supported.")

        result = operators[operator](*numbers)
        logging.info(f"Operation: {' '.join(tokens)} = {result}")
        print(f"Result: {result}")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        print(f"Error: Invalid number input. {ve}")
    except ZeroDivisionError as zde:
        logging.error(f"ZeroDivisionError: {zde}")
        print(f"Error: {zde}")
    except InvalidOperatorError as ioe:
        logging.error(f"InvalidOperatorError: {ioe}")
        print(f"Error: {ioe}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Program finished. Check logs for details.")


if __name__ == "__main__":
    user_input = input("Enter numbers followed by operator (e.g., '10 20 30 *'): ")
    calculate_from_input(user_input)
