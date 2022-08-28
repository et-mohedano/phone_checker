import pandas as pd
import re

def check_phone(phone):
    return re.findall(re.compile(r"(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}"), phone)
def format_cleaned(phone):
    items = [" ", "(", ")", "-", "[", "]"]
    for item in items:
        phone = phone.replace(item, "")
    return phone
File = pd.ExcelFile('numbers.xlsx')
dataFrame = File.parse('numbers')
validnumbers = []
Invalidnumbers = []
numbers_list = dataFrame['numbers']
msg_to_file = ""
msg_to_file = f"Total of phone numbers: {len(numbers_list)}\n"
msg_to_file = f"Total of phone duplicate numbers: {len(numbers_list) - len(list(set(numbers_list)))}\n"
numbers_list = list(set(numbers_list))
print("Process started")
for numberIn in numbers_list:
    numberIn = str(numberIn)
    numberIn = format_cleaned(numberIn)
    if check_phone(numberIn):
        validnumbers.append(numberIn)
    else:
        Invalidnumbers.append(numberIn)
filepath = f'bd_cleaned_valid.xlsx'
df = pd.DataFrame(zip(validnumbers), columns=["Valid numbers"])
df.to_excel(filepath, index=False)
filepath = f'bd_cleaned_invalid.xlsx'
df = pd.DataFrame(zip(Invalidnumbers), columns=["Invalid numbers"])
df.to_excel(filepath, index=False)
msg_to_file = f"Valid numbers: {len(validnumbers)}, Invalid numbers: {len(Invalidnumbers)}"
print("Process finished")
with open('overview.txt', 'w') as f:
    f.write('Create a new text file!')