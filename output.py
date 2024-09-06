def read_fl(fle):
    with open(fle) as fl:
        return fl.readlines()
    
# print(read_fl('input_file1.txt'))

# files = read_fl('input_file1.txt')
def sepr(sep_f):
    list_data = []
    for i in sep_f:
        list_data += [i.split(':')]
        for i in list_data:
            if '' in i:
                i = i.remove('')
    return list_data
# print(sepr(files))

# print(sepr(files))
# print(sepr('input_file1.txt'))

def user_n(sep_f):
    # проверка на кол-во слов в списке
    stri = sepr(sep_f)
    us_n = []
    for i in stri:
        # print(i)
        len_list = len(i)
        if len_list == 5:
            user_name = i[1][0] + i[2][0] + i[3]
        else:
            user_name = i[1][0] + i[3]
        i.insert(1, user_name[0:8].lower())
        us_n.append(i)
    return us_n
# print(user_n(files))
# ready = user_n(files)

def instr_file(ready, output):
    with open(output, 'a') as fl:
        for i in ready:
            i = ':'.join(i)
            fl.write(i)
# instr_file(ready, 'output.txt')

def main(output_file, input_files):
    for i in input_files:
        files = read_fl(i)
        done = user_n(files)
        instr_file(done, output_file)

main('output.txt', ['input_file1.txt', 'input_file2.txt', 'input_file3.txt'])

# print(user_n('4567:Milan:Rastislav:Stefanik:Defence'))