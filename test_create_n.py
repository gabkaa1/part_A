from output import read_fl, sepr, user_n, instr_file, main
import json

def read_data(test_name):
    with open('tests.json', 'r') as fl:
        data = json.load(fl)

    input_data = data[test_name]['input']
    output_data = data[test_name]['output']

    return input_data, output_data

def test_read_fl():
    input, output = read_data('read_fl')
    if len(input) == len(output):
        for i in range(len(input)):
            assert read_fl(input[i]) == output[i]
    else:
        raise ValueError('Не равное кол-во данных')


def test_sepr():
    input, output = read_data('sepr')
    if len(input) == len(output):
        for i in range(len(input)):
            assert sepr(input[i]) == output[i]
    else:
        raise ValueError('Не равное кол-во данных')

def test_user_n():
    input, output = read_data('user_n')
    if len(input) == len(output):
        for i in range(len(input)):
            assert user_n(input[i]) == output[i]
    else:
        raise ValueError('Не равное кол-во данных')

def test_instr_file():
    input, _ = read_data('instr_file')

    for i in range(len(input)):
        instr_file(input[i], 'output.txt')
    
def test_main():
    input, _ = read_data('main')
    
    for i in range(len(input)):
        instr_file(input[i], 'output.txt')
    
print(read_data('read_fl'))
print(read_fl('input_file1.txt'))