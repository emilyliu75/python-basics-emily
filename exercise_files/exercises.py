from pathlib import Path
import os
import csv

# exercise 2

lines = [
    "Line 1: Hello, world!",
    "Line 2: Python file handling.",
    "Line 3: Goodbye!"
]

current_dir = Path.cwd()
FILE_NAME = 'output.txt'
file_path = current_dir / 'exercise_files' / FILE_NAME


#new_dir = current_dir / FILE_NAME
#new_dir.mkdir(exist_ok=True)
# print(file_path)
with open(file_path, mode='w') as file:

    for line in lines:
        file.write(line + "\n")

# exercise 3


FILE_NAME_3 = 'protected.txt'
file_path_3 = current_dir / 'exercise_files' / FILE_NAME_3



try:
    with open(file_path_3, mode='w') as file: # gives error
        for line in lines:
            file.write(line + "\n")
except PermissionError as PE:
    print(f'This file is read only {PE}')


os.chmod(file_path_3, 0o444)  # 0o444 sets the file to read-only for everyone


# exercise 4

FILE_NAME_4 = 'data.csv'
file_path_4 = current_dir / 'exercise_files' / FILE_NAME_4

try:
    a,b,c,d = [3,4,5]
    with open(file_path_4) as file:
        read_data = csv.reader(file)
        for row in read_data:
            print(row)

except FileNotFoundError as FnF:
    print(f'The file was not found: {FnF}')
except ValueError as ve:
    print(f'There was a value error: {ve}')
except Exception as e:
    print(f'There was an unknown error: {e}')

# exercise 5

FILE_NAME_5 = 'data.txt'
file_path_5 = current_dir / 'exercise_files' / FILE_NAME_5

with open(file_path_5, mode='w') as file:
    for line in lines:
        file.write(line + "\n")

try:
    file_5 = open(file_path_5)
    print(file_5.read())
except FileNotFoundError as FnF:
    print(f'The file was not found: {FnF}')
except Exception as e:
    print(f'There was an unknown error: {e}')
finally:
    file_5.close()

#print(file_5.read())


# exercise 6

FILE_NAME_6 = 'log.txt'
file_path_6 = current_dir / 'exercise_files' / FILE_NAME_6

# writing:
with open(file_path_6, mode='w') as file:
     for line in lines:
         file.write(line + "\n")

# Appending:
with open(file_path_6, mode='a') as file:
     for line in lines:
         file.write(line + "\n")

# exercise 7
print("exercise 7:")
FILE_NAME_7 = 'data.txt'
file_path_7 = current_dir / 'exercise_files' / FILE_NAME_7

try:
    with open(file_path_7) as file_7:
        print(file_7.read())

except FileNotFoundError as FnF:
    print(f'The file was not found: {FnF}')
except PermissionError as PE:
    print(f'This file is read only {PE}')
except ValueError as ve:
    print(f'There was a value error: {ve}')
except Exception as e:
    print(f'There was an unknown error: {e}')

os.chmod(file_path_7, 0o444)  # 0o444 sets the file to read-only for everyone