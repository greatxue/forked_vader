import json

input_json_file = '/home/wenhao/Project/greatxue/MJ-Bench-2.0/gen_video/json/json_backup/input_part_4.json'
output_txt_file = '/home/wenhao/Project/greatxue/mj_models/VADER/assets/video4.txt'

with open(input_json_file, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
    if isinstance(data, dict):
        for key, value in data.items():
            txt_file.write(f'{key}: {value}\n')
    elif isinstance(data, list):
        for item in data:
            txt_file.write(f'{item}\n')

print(f'JSON has been converted to txt at {output_txt_file}.')