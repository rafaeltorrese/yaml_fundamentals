import yaml

my_file = '01_basics/basics-structure-1.yaml'

with  open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print(f'key: {key}')
            print(f'value: {value}. \ndatatype: {type(value)} \n')
    except yaml.YAMLError as err:
        print(err)

print(data)
print(type(data))