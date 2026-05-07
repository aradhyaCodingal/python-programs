class Roman:

    def __init__(self, number):
        self.number = number

    def convert(self):

        value = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbol = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        roman = ""

        num = self.number

        for i in range(len(value)):
            while num >= value[i]:
                roman += symbol[i]
                num -= value[i]

        return roman


n = int(input("Enter an integer: "))

obj = Roman(n)

print("Roman Numeral:", obj.convert())