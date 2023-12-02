with open('test.txt') as s:
    lines = s.readlines()

def get_numbers(string: str) -> str:
    numbers = list()
    for c in string:
        if c.isdigit():
            numbers.append(c)
    return str(numbers[0]) + str(numbers[-1])            

count = int()

for line in lines:
    number = get_numbers(line)
    count += int(number)
print("Final count: ", count)