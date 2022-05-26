import yaml

my_file = '01_basics/basics-structure-5-nulls.yaml'

with  open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():            
            print(f'key: {key} \nvalue: {value}\nDatatype of {value} is {type(value)}\n')            
    except yaml.YAMLError as err:
        print(err)