import math
import ast

def _evaluate_expression_safely(expression: str):
    try:
        node = ast.parse(expression, mode='eval')
    except SyntaxError:
        return None, "Error: Invalid arithmetic expression syntax."

    for subnode in ast.walk(node):
        if not isinstance(subnode, (ast.Expression, ast.BinOp, ast.UnaryOp, 
                                     ast.Constant, ast.Load, 
                                     ast.operator)):
            return None, "Error: Disallowed operation found."

    try:
        result = eval(compile(node, filename='', mode='eval'))
        return result, None
    except ZeroDivisionError:
        return None, "Math Error: Division by zero is not allowed."
    except Exception as e:
        return None, f"Evaluation Error: {e}"


def calculate_expression():
    expression = input("Enter arithmetic expression: ")
    result, error = _evaluate_expression_safely(expression.strip())
    
    if error:
        print(error)
    else:
        print(f"Result: {result}")

# --------------------------------------------------------------------------------

def solve_linear():
    print("--- Solve ax + b = 0 ---")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter constant b: "))
        
        if a == 0:
            if b == 0:
                print("Solution: Infinitely many solutions.")
            else:
                print("Solution: No solution.")
        else:
            x = -b / a
            print(f"Solution: x = {x:.4f}")
    except ValueError:
        print("Input Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# --------------------------------------------------------------------------------

def solve_system():
    print("--- Solve System of Linear Equations (2 vars) ---")
    print("a1*x + b1*y = c1")
    print("a2*x + b2*y = c2")
    try:
        a1 = float(input("Enter a1: "))
        b1 = float(input("Enter b1: "))
        c1 = float(input("Enter c1: "))
        a2 = float(input("Enter a2: "))
        b2 = float(input("Enter b2: "))
        c2 = float(input("Enter c2: "))

        D = a1 * b2 - a2 * b1
        Dx = c1 * b2 - c2 * b1
        Dy = a1 * c2 - a2 * c1

        if abs(D) < 1e-9:
            if abs(Dx) < 1e-9 and abs(Dy) < 1e-9:
                print("Solution: Infinitely many solutions.")
            else:
                print("Solution: No unique solution.")
        else:
            x = Dx / D
            y = Dy / D
            print(f"Solution: x = {x:.4f}, y = {y:.4f}")
            
    except ValueError:
        print("Input Error: Please enter valid numbers.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# --------------------------------------------------------------------------------

def calculate_power_root():
    print("\n--- Power & Root (x^y or x^(1/n)) ---")
    try:
        base_x = float(input("Enter base number (x): "))
        exponent_input = input("Enter exponent (y) or root degree (1/n): ")

        if "/" in exponent_input:
            _, n_str = exponent_input.split('/')
            root_degree_n = int(n_str.strip())
            
            if root_degree_n == 0:
                raise ValueError("The root degree cannot be zero.")
                
            if base_x < 0 and root_degree_n % 2 == 0:
                print("Math Error: Cannot take an even root of a negative number (result is complex).")
                return

            result = base_x**(1/root_degree_n)
            print(f"Result: {result:.4f}")

        else:
            exponent_y = float(exponent_input)
            result = base_x**exponent_y
            print(f"Result: {result:.4f}")
            
    except ValueError as ve:
        print(f"Input/Math Error: {ve}. Ensure input is a number or in '1/n' format.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# --------------------------------------------------------------------------------

def main():
    while True:
        print("\n=== Advanced Python Calculator ===")
        print("1. Arithmetic Expression")
        print("2. Linear Equation (ax + b = 0)")
        print("3. System of Equations (2 vars)")
        print("4. Power & Root")
        print("0. Exit")
        
        choice = input("Select option: ")
        
        operations = {
            "1": calculate_expression,
            "2": solve_linear,
            "3": solve_system,
            "4": calculate_power_root
        }

        if choice in operations:
            operations[choice]()
        elif choice == "0":
            print("Exiting calculator. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()