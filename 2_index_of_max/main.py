"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""
import json

class Solution:

    def find_max_index(self, numbers: list) -> int | str:
        pass

class Main(Solution):
    def find_max_index(self, list_of_number):
        if len(list_of_number) <= 0:
            # return message string type

            return "list can not blank"

        
        return list_of_number.index(max(list_of_number))

if __name__ == "__main__":
    try:
        input_list = json.loads(input("input = "))
        main = Main()
        result = main.find_max_index(input_list)
        print("output = ", result)

    except json.decoder.JSONDecodeError:
        print("output = invalid value!")
