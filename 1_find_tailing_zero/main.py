"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        pass

class Main(Solution):
    def find_tailing_zeroes(self, number):
        if int(number) < 0:

            # return message string type
            return "number can not be negative"

        sum_number = 1
        for n in range(1, number + 1):
            sum_number *= n

        format_num = str(sum_number)
        splited_num = list(format_num)
        count_tailing_zero = 0
        for i in range(len(splited_num)):
            tail_num = splited_num[-(i + 1)]
            if int(tail_num) != 0:
                break

            else:
                count_tailing_zero += 1

        # return result integer
        return count_tailing_zero

if __name__ == "__main__":
    try:
        input_number = int(input("input = "))
        main = Main()
        result = main.find_tailing_zeroes(input_number)
        print("output = ", result)

    except ValueError:
        print("output = input only number please!")
