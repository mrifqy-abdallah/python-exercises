from re import sub, match

class PhoneNumber:
    def __init__(self, number: str):
        self.number = self.clean_number(number)
        self.area_code = self.number[:3]

    def clean_number(self, number: str):
        clean = sub(r'\+1|1|[^\d]', "", number)

        if len(clean) > 11:
            raise ValueError("Number is too long.")
        elif len(clean) == 11:
            raise ValueError("Number with length of 11 must start with '1'.")
        
        # Check that the number now has exactly 10 digits long and has valid area codes
        m = match(r'[2-9][\d]{2}[2-9][\d]{6}', clean)
        if not m:
            raise ValueError("Invalid number. Try to check your area code.")

        return clean

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"