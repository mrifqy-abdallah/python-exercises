from operator import add, mul, sub, truediv
from re import findall

OPERATIONS_DICT = {
    "plus": add,
    "minus": sub,
    "multiplied": mul,
    "divided": truediv
}


def answer(question: str) -> int:
    question = question.lower()
    equation = findall(r'what is (.+)\?', question)

    if not equation:  
        raise ValueError("No equation is found")
    
    # `equation` is a list with only one string element, like this one: ['4 plus 4 minus 8']
    # Here we extract the element and split it
    # And in case of multiplication and division, we need to remove the 'by'-s
    equation = equation[0].split()
    while "by" in equation:
        equation.remove("by")

    result = 0
    operation = ""
    # This flag is set to check for equations where the number has no pair, like: '4 plus 5 minus'
    operation_is_used = False

    try:
        result = int(equation[0])
    except ValueError:
        raise ValueError("The question must be: 'What is <number> <operation> ... <number>?'")

    for i in range(1, len(equation)):
        operation_is_used = False
        if i % 2 == 0:
            try:
                result = OPERATIONS_DICT[operation](result, int(equation[i]))
                operation_is_used = True
            except:
                raise ValueError(f"Invalid input after {equation[i-1]}")
        else:
            if equation[i] in OPERATIONS_DICT:
                operation = equation[i]
            else:
                raise ValueError(f"Invalid input after {equation[i-1]}")
    
    # To avoid cases like 'What is 5?' gets an exception, `operation` needs to be added to the statement
    if operation and not operation_is_used:
        raise ValueError("Numbers being operated has no pair")
        
    return result