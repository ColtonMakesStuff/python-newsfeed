import re
from data import data

exampleData = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''

def getlines(data):
    lines = data.split('\n')
    return lines

def convertNumbers(data):
   # Define a dictionary mapping words to digits
   word_to_digit = {
       'zerone': '01',
       'twone': '21',
       'oneight': '18',
       'threeight': '38',
       'eightwo': '82',
       'eighthree': '83',
       'sevenine': '79',
       'fiveight': '58',
       'nineight': '98',
       'zero': '0',
       'one': '1',
       'two': '2',
       'three': '3',
       'four': '4',
       'five': '5',
       'six': '6',
       'seven': '7',
       'eight': '8',
       'nine': '9'
   }

   # Iterate over the dictionary and replace each word with its corresponding digit
   for word, digit in word_to_digit.items():
         data = re.sub(word, digit, data)
   return data


def getnumbers(lines):
   
   total = 0
   for line in lines:
       numbers = []
       current_number = ''
       for char in line:
           if re.search('\d', char):
               current_number += char
           else:
               if current_number:
                  numbers.append(current_number)
                  current_number = ''
       if current_number:
           numbers.append(current_number)
       numb1 = str(numbers[0])
       if len(numbers) > 1:
        numb2 = str(numbers[-1])
       else:
        numb2 = numb1
       numberToAdd = numb1 + numb2
    #    print(numberToAdd)   
       total += int(numberToAdd)
   return total

def getAllNumbers(data):
    convertedData = convertNumbers(data)
    lines = getlines(convertedData)
    
    numbers = []
    total = 0
    for line in lines:
         new_string = "".join(re.findall('\d+', line))
        #  print(new_string)
         numbers.append(new_string)
         if new_string:
            firstDigit = new_string[0]
            lastDigit = new_string[-1]
            total += int(firstDigit + lastDigit)   

    return total


print(getAllNumbers(data))

# print(getnumbers(getlines(exampleData)))
# print(getlines(data))
# print(getnumbers(getlines(data)))
# now i need to convert all of the written out numbers in the string to numbers
# lets start with just looking for the number one in a string and replacing it with 1



print(convertNumbers(exampleData))