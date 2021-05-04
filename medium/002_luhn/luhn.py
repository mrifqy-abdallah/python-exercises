class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) > 1 and self.card_num.isdigit():
            sum = 0
            reversed_card_num = [i for i in reversed(self.card_num)]
            for index, number in enumerate(reversed_card_num):
                number = int(number)
                # Second digits needs to be doubled first
                # Another digits will be added to sum directly
                if (index + 1) % 2 != 0:
                    sum += number
                    print(index, number, sum)
                    continue
                sum += number*2 - 9 if number*2 > 9 else number*2
                print(index, number, sum)
            if sum % 10 == 0:
                return True
            return False
        return False
