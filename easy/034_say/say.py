d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
      6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
      11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 
      16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty',
      30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
      70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
k = 1000
m = 1000000
b = 1000000000
t = 1000000000000

def say(number: int):
    if len(str(number)) > 12 or number < 0:
        raise ValueError("Max number is 999.999.999.999 and cannot be less than zero")

    if number < 20:
        return d[number]

    elif number < 100:
        if number % 10 == 0:
            return d[number] 
        else:
            return d[number // 10 * 10] + "-" + d[number % 10]
    
    elif number < k:
        if number % 100 == 0:
            return d[number // 100] + " hundred"
        else:
            return d[number // 100] + " hundred " + say(number % 100)

    elif number < m:
        if number % k == 0:
            return say(number // k) + " thousand"
        else:
            return say(number // k) + " thousand " + say(number % k)

    elif number < b:
        if number % m == 0:
            return say(number // m) + " million"
        else:
            return say(number // m) + " million " + say(number % m)

    elif number < t:
        if number % b == 0:
            return say(number // b) + " billion"
        else:
            return say(number // b) + " billion " + say(number % b)

    elif number >= t:
        if number % t == 0:
            return say(number // t) + " trillion"
        else:
            return say(number // t) + " trillion " + say(number % t)

    # Alternatively, you can use moduls such as num2words and inflect