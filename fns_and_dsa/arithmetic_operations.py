def perform_operation(num1: float, num2: float, operation: str)->float:
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                print("Can not divide by zero!")
                return None
            else:
                return num1 / num2
        
        

