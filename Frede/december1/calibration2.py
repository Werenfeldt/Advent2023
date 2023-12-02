import re

with open('test.txt') as s:
    lines = s.readlines()

def transform(word: str) -> int:
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    return numbers.get(word)

string_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum_list = []

for line in lines:
    numbers = []
    substring = ""
    for c in line:
        if not c.isdigit():
            substring += c
            if substring in string_numbers:
                numbers.append(transform(substring))
                substring = substring[-1]
            else:
                lol = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", substring)
                if lol:
                    last = lol[-1]
                    numbers.append(transform(last))
                    substring = last[-1]
                    
        else:
            numbers.append(c)
            substring = ""
    conc_str = str(numbers[0]) + str(numbers[-1])
    sum_list.append(int(conc_str))

print("Final count: ", sum(sum_list))