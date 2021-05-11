roman_numbers = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

def roman(number: int()):
    if number <= 0:
        raise ValueError("Number cannot be zero or less.")
        
    result = ""
    for numeric, romans in roman_numbers.items():
        factor, mod = divmod(number, numeric)
        result += romans * factor
        number -= numeric * factor
    
    return result
