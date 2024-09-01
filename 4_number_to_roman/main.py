"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        pass


class Main(Solution):
    def number_to_roman(self, number):
        if int(number) <= 0:
            # return invalid value

            return "number can not less than 0"

        roman_number_list = {
            "1": "I",
            "5": "V",
            "10": "X",
            "50": "L",
            "100": "C",
            "500": "D",
            "1000": "M"
        }
        format_num = str(number)
        splited_num = list(format_num)
        len_of_splited_num = len(splited_num)
        roman_number = ""
        for i, n in enumerate(splited_num):
            # thousand
            if len_of_splited_num >= 4:
                for _ in range(1, int(n) + 1):
                    roman_number += "M"

            # houndred
            elif len_of_splited_num == 3:
                # equal 400
                if int(n) == 4:
                    roman_number += "CD"
                # equal or more than 500
                elif int(n) >= 5:
                    roman_number += "D"
                    for _ in range(1, int(n) - 5 + 1):
                        roman_number += "C"
                # equal 900
                elif int(n) == 9:
                    roman_number += "CM"
                else:
                    for _ in range(1, int(n) + 1):
                        roman_number += "C"

            elif len_of_splited_num == 2:
                # equal 40
                if int(n) == 4:
                    roman_number += "XL"
                # equal or more than 50
                elif int(n) >= 5:
                    roman_number += "L"
                    for _ in range(1, int(n) - 5 + 1):
                        roman_number += "X"
                # equal 90
                elif int(n) == 4:
                    roman_number += "CX"
                else:
                    for _ in range(1, int(n) + 1):
                        roman_number += "X"

            else:
                # equal 4
                if int(n) == 4:
                    roman_number += "IV"
                # equal or more than 5
                elif int(n) >= 5:
                    roman_number += "V"
                    for _ in range(1, int(n) - 5 + 1):
                        roman_number += "I"
                # equal 9
                elif int(n) == 4:
                    roman_number += "IX"
                else:
                    for _ in range(1, int(n) + 1):
                        roman_number += "I"

            len_of_splited_num -= 1

        return roman_number

if __name__ == "__main__":
    try:
        input_number = int(input("input = "))
        main = Main()
        result = main.number_to_roman(input_number)
        print("output = ", result)

    except ValueError:
        print("output = input only number please!")
