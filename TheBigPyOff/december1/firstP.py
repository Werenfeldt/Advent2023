sum = 0

numbers = list()

def resetString(charDigits, number):
    #data might look like: tswoneight - therefore when "one" found all characters before "one" is removed along with the o in "one".
    #this way we wont find "one" again but can still use the e in "one" to find "eight". 
    sub = charDigits[charDigits.find(number):]
    charDigits = sub[1:]
    return charDigits

with open("input.txt", 'r') as file:
    for line in file:
        numbers = list()
        charDigits = ""
        for char in line.strip(): 
            #print(f"looking at char: {char}")
            if char.isnumeric():
                numbers.append(char)
            else: 
                charDigits += char
                if "zero" in charDigits:
                    numbers.append("0")
                    charDigits = resetString(charDigits, "zero")
                elif "one" in charDigits: 
                    numbers.append("1")
                    charDigits = resetString(charDigits, "one")
                elif "two" in charDigits: 
                    numbers.append("2")
                    charDigits = resetString(charDigits, "two")
                elif "three" in charDigits:
                    numbers.append("3")
                    charDigits = resetString(charDigits, "tree")
                elif "four" in charDigits: 
                    numbers.append("4")
                    charDigits = resetString(charDigits, "four")
                elif "five" in charDigits: 
                    numbers.append("5")
                    charDigits = resetString(charDigits, "five")
                elif "six" in charDigits: 
                    numbers.append("6")
                    charDigits = resetString(charDigits, "six")
                elif "seven" in charDigits: 
                    numbers.append("7")
                    charDigits = resetString(charDigits, "seven")
                elif "eight" in charDigits: 
                    numbers.append("8")
                    charDigits = resetString(charDigits, "eight")
                elif "nine" in charDigits: 
                    numbers.append("9") 
                    charDigits = resetString(charDigits, "nine")

        number = numbers[0] + numbers[-1]
        #print(number)
        sum += int(number)

print(sum)