# user input roman numerals
num1 = input("Hello, welcome to the best Roman Numeral Calculator\nOptions are: I, V, X, L. C\nEnter first Roman Numeral: ")
num2 = input("Enter second Roman Numeral: ")
print()


# roman numeral dictionary
roman2int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
int2roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
             10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C'}


i = 0
rnum1 = 0
skiploop = False

while i < len(num1):
    if skiploop:
        i += 1
        skiploop = False
        continue
    if len(num1) == 1:
        rnum1 = roman2int[num1]
        break
    if i < len(num1) - 1 and roman2int[num1[i]] < roman2int[num1[i+1]]:
        rnum1 += roman2int[num1[i+1]] - roman2int[num1[i]]
        skiploop = True
    else:
        rnum1 += roman2int[num1[i]]
    i += 1


# converting num2 to number roman2int
i = 0
rnum2 = 0
skiploop = False

while i < len(num2):
    if skiploop:
        i += 1
        skiploop = False
        continue
    if len(num2) == 1:
        rnum2 = roman2int[num2]
        break
    if i < len(num2) - 1 and roman2int[num2[i]] < roman2int[num2[i+1]]:
        rnum2 += roman2int[num2[i+1]] - roman2int[num2[i]]
        skiploop = True
    else:
        rnum2 += roman2int[num2[i]]
    i += 1


# sum of inputs
rnum_sum = rnum1 + rnum2


# convert rnum_sum into roman numeral
i = 0
keys = list(int2roman.keys())
rnum_answer = ""
while rnum_sum > 0:
    i = len(keys) - 1
    while i >= 0:
        if keys[i] <= rnum_sum:
            rnum_answer += int2roman[keys[i]]
            rnum_sum -= keys[i]
            break
        else:
            i -= 1


# print solution
print(num1, "+", num2, "=", rnum_answer)
