import argparse

def read_fl(fle: str) -> list[str] | None:
    """ Returns list with values from files
    Takes .txt -> returns list

    Args:
        fle (str): string with file's names

    Returns:
        list[str] | None: list with strings of values or None
    Exaple:
        >>> read_fl('output_file.txt')

        ['1234:Mark:Stanisla:Miloslaviks:Developer\n']
        or
        ['5482:Mark::Miloslavski:Workauter\n']
    """    
    try:
        if isinstance(fle, str) and fle[-4:] == '.txt':
            with open(fle) as fl:
                # print(fl.readlines())
                return fl.readlines()
    except FileNotFoundError as e:
        print(f'Ошибка {e}')


def sepr(sep_f):
    """Returns list of separated strings
    Takes list of strings

    Args:
        sep_f (list): list with strings like ['1234:Mark:Stanisla:Miloslaviks:Developer\n']

    Returns:
        list[str]: list with separated values like ['1234', 'Mark', 'Stanisla', 'Miloslaviks', 'Developer\n']

    Example:
        >>> sepr(['1234:Mark:Stanisla:Miloslaviks:Developer\n'], ['1234', 'Mark', '', 'Miloslaviks', 'Developer\n'])

        ['1234', 'Mark', 'Stanisla', 'Miloslaviks', 'Developer\n'], ['1234', 'Mark', '', 'Miloslaviks', 'Developer\n']
    """    
    list_data = []
    for i in sep_f:
        list_data += [i.split(':')]
    return list_data
# print(read_fl('input_file3.txt'))

def user_n(sep_f):
    """Returns list of lists with usernames
    Takes list of strings like ['1234:Mark:Stanisla:Miloslaviks:Developer\n']

    Args:
        sep_f (list[str]): list with strings

    Returns:
        list[list[str]]: list of lists with strings
    """    
    if sep_f != None:
        stri = sepr(sep_f)
        us_n = []
        global dict
        for i in stri:
            # print(i)
            len_list = len(i)
            if len_list == 5:
                user_name = i[1][0] + i[2][:1] + i[3]
                user_name = user_name[0:8].lower()
                if user_name not in dict:
                    dict[user_name] = 0
                else:
                    dict[user_name] += 1
                    user_name += str(dict[user_name])
                i.insert(1, user_name)
                us_n.append(i)    
            else:
                print('Некорректное кол-во данных')
            
 
    else:
        return 'incorrect data\n'
    print(us_n)
    return us_n


def instr_file(ready, output):
    print(ready)
    with open(output, 'a') as fl:
        for i in ready:
            i = ':'.join(i)
            fl.write(i)


def main(output_file, input_files):
    """Writes ready values in new txt file 
    Takes file name, files that must be written in output file

    Args:
        output_file (str): like 'name.txt'
        input_files (list[list[str]]): list of lists with strings like [['4563', 'phufnage', 'Pista', '', 'Hufnagel', 'Sales\n'], ['1111', 'phufnage1', 'Pista', '', 'Hufnagel', 'Sales\n']]
    """    
    try:
        args = parse.parse_args()
        if not args.output or not args.inputfiles:
            print('Не правильно введено одно или оба ожидаемых значений')
            parse.print_help()

    except Exception as e:
        print(f'Ошибка {e}')
        parse.print_help()

    for i in input_files:
        files = read_fl(i)
        done = user_n(files)
        # print(done, files)
        instr_file(done, output_file)

dict = {}
if __name__ == '__main__':
   
    # main('output.txt', ['input_file1', 'input_file2.txt', 'input_file3.txt'])

    parse = argparse.ArgumentParser(prog='output.py', description='Save names', epilog='Tetx me')

    parse.add_argument('-o', '--output')
    parse.add_argument('inputfiles', nargs='*')

    args = parse.parse_args()
    main(args.output, args.inputfiles)

