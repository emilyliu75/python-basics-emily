import csv
import json
from pathlib import Path

TRAINER_DEMO_FILES = 'demo_files'
current_dir = Path.cwd()
FILE_NAME = [
    'data.csv',
    'new_data.csv',
    'data.tsv',
    'new_data.tsv',
    'new_data.json'
]

demo_csv_file_path = current_dir / TRAINER_DEMO_FILES / FILE_NAME[0]

# with open(demo_csv_file_path) as csv_file:
#     read_csv = csv.reader(csv_file)
#     for row in read_csv:
#         print(row)
#         for cell in row:
#             print(cell)
#         print("=======")


# create our own CSV file
data = [
    ['name', 'age'],
    ['alice', 24]
]

new_file_path = current_dir/TRAINER_DEMO_FILES/FILE_NAME[1]

# with open(new_file_path, mode='w') as new_csv_file:
#     new_data = csv.writer(new_csv_file)
#     new_data.writerows(data)

# with open(new_file_path) as new_csv:
#     reader = csv.reader(new_csv)
#     for row in reader:
#         print(row)


# tsv
tsv_file_path = current_dir/TRAINER_DEMO_FILES/FILE_NAME[2]

with open(tsv_file_path) as tsv_file:
    tsv_data = csv.reader(tsv_file, delimiter='\t')
    for row in tsv_data:
        print(row)

new_tsv_file_path = current_dir/TRAINER_DEMO_FILES/FILE_NAME[3]

with open(new_tsv_file_path, mode='w') as new_tsv:
    tsv_data = csv.writer(new_tsv, delimiter='\t')
    tsv_data.writerows(data)

json_data = [{
    'name': 'alice',
    'age': 24,
    'address': {
        'street': '123 Fake st',
        'city': 'springfield'
    }
},  {
    'name': 'lily',
    'age': 25,
    'address': {
        'street': '21 Fake st',
        'city': 'springfield'
    }
}]
# json

# to write json file: json.dump(data, file)
new_json_file_path = current_dir/TRAINER_DEMO_FILES/FILE_NAME[4]
with open(new_json_file_path, mode='w') as j_file:
    j_data = json.dump(json_data, j_file)

#  to read json file: json.load(file)
with open(new_json_file_path) as read_json:
    data = json.load(read_json)
    print(data)
    print(type(data))
