import re
from data import data

exampleData = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''

def getlines(data):
    lines = data.split('\n')
    return lines

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

print(getnumbers(getlines(exampleData)))
print(getnumbers(getlines(data)))