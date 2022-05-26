import yaml

my_file = '01_basics/basics-structure-4-indentation.yaml'

with  open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():            
            print(f'key: {key} \nvalue: {value}\n')
            for k, v in value.items():
                print(f'key: {k}. \nvalue: {v}\n')
    except yaml.YAMLError as err:
        print(err)