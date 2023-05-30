import csv
from fractions import Fraction
from datetime import datetime

def parse_fraction(fraction_str):
    if "&" in fraction_str:
        whole, fraction = fraction_str.split("&")
        numerator, denominator = fraction.split("/")

        return Fraction(int(whole)) + Fraction(int(numerator), int(denominator))
    else:
        return Fraction(fraction_str)

def perform_operation(operand1, operator, operand2):
    if operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return operand1 / operand2
    elif operator == '+':
        result = operand1 + operand2
        if result >= 1:  # Check if the result is an improper fraction
            whole_part = int(result)
            fractional_part = result - whole_part
            if fractional_part == 0:  # If no fractional part, return the whole number
                return whole_part
            else:  # Convert to mixed fraction format
                return f"{whole_part}&{fractional_part}"
        else:
            return result
    elif operator == '-':
        result = operand1 - operand2
        if result >= 1:  # Check if the result is an improper fraction
            whole_part = int(result)
            fractional_part = result - whole_part
            if fractional_part == 0:  # If not fractional part, return the whole number
                return whole_part
            else:  # Convert to mixed fraction format
                return f"{whole_part}&{fractional_part}"
        else:
            return result


def main():
    error_file = open("errors.csv", "w")
    error_writer = csv.writer(error_file)
    error_writer.writerow(["Error Messages"])

    while True:
        user_input = input("? ")
        if user_input == "exit":
            break

        try:
            tokens = user_input.split()
            operand1 = parse_fraction(tokens[0])
            operator = tokens[1]
            operand2 = parse_fraction(tokens[2])

            result = perform_operation(operand1, operator, operand2)
            print("= " + str(result))
        except Exception as e:
            current_time = datetime.now()
            current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
            error_writer.writerow([current_time_str, str(e)])
            print("Error:", str(e))

    error_file.close()

if __name__ == "__main__":
    main()
