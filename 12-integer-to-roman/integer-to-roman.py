class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
                0:{1:"I", 5:"V"},
                1:{1: "X", 5: "L"},
                2:{1: "C", 5: "D"},
                3:{1: "M"}
                }
        result = ""
        level =0
        while num>0:
            curr = num % 10
            num  = num//10
            if curr in roman_dict[level].keys():
                result =  roman_dict[level][curr] + result
            elif curr == 9:
                result =  roman_dict[level][1] + roman_dict[level+1][1] + result
            elif curr == 4:
                result =  roman_dict[level][1] + roman_dict[level][5] + result
            elif curr >5:
                result = roman_dict[level][5] + (curr-5) * roman_dict[level][1] + result
            else:
                result = curr * roman_dict[level][1] + result

            level +=1
        return result
            

