import yaml

my_file = '01_basics/basics-structure-2-newline-char.yaml'

with  open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for value in data.values():
            print('-' * 10 )            
            print(f'value: {value}')
    except yaml.YAMLError as err:
        print(err)