# Write your solution here
def number_to_words(n):
    ones = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]

    if 0 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n - 10]
    elif 20 <= n < 100:
        ten_part = tens[n // 10]
        one_part = "" if n % 10 == 0 else "-" + ones[n % 10]
        return ten_part + one_part

def dict_of_numbers():
    c = {}
    for x in range(0,100):
        bn = number_to_words(x)
        c[x] = bn
    return c

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
