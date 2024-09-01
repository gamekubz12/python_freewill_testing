"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

class Solution:

    def number_to_thai(self, number: int) -> str:
        pass

class Main(Solution):
    def number_to_thai(self, number):
        if int(number) < 0:
            # return invalid value

            return "number can not less than 0"

        elif int(number) == 0:
            return "ศูนย์"
        
        elif int(number) > 10000000:
            return "number can not more than 10,000,000"

        thai_number_list = {
            "0": "",
            "1": "หนึ่ง",
            "2": "สอง",
            "3": "สาม",
            "4": "สี่",
            "5": "ห้า",
            "6": "หก",
            "7": "เจ็ด",
            "8": "แปด",
            "9": "เก้า"
        }
        thai_point_list = [
            "สิบ",
            "ร้อย",
            "พัน",
            "หมื่น",
            "แสน",
            "ล้าน",
        ]
        format_num = str(number)
        splited_num = list(format_num)
        len_of_splited_num = len(splited_num)

        thai_number = thai_number_list["0"]
        for i, n in enumerate(splited_num):
            row = i + 1
            len_of_point = len(splited_num[row:len_of_splited_num])

            if row > 1 and len_of_splited_num == row and int(n) == 1:
                thai_number += "เอ็ด"
                continue

            if row + 1 == len_of_splited_num:
                if int(n) == 2:
                    thai_number += "ยี่"

                elif int(n) != 1:
                    thai_number += thai_number_list[n]
            else:
                thai_number += thai_number_list[n]

            if int(n) > 0 and len_of_splited_num > 1 and len_of_point > 0:
                if len_of_splited_num <= 7:
                    thai_number += thai_point_list[len_of_point - 1]

                else:
                    # [10] [000000] len 8 - (6 + 2) = index 0
                    # [100] [000000] len 9 - (6 + 2) = index 1
                    thai_number += thai_point_list[len_of_splited_num - 6 - 2] + thai_point_list[-1]

        return thai_number

if __name__ == "__main__":
    try:
        input_number = int(input("input = "))
        main = Main()
        result = main.number_to_thai(input_number)
        print("output = ", result)

    except ValueError:
        print("output = input only number please!")
