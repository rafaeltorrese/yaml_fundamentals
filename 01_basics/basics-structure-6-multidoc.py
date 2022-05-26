import yaml

my_file = '01_basics/basics-structure-6-multidoc.yaml'

with  open(my_file, 'r', encoding='utf8') as stream:
    try:
        data = yaml.safe_load_all(stream)
        count = 0
        for yaml_doc in data:
            doc_no = count + 1
            print('<' * 5, ' ' * 4, f'YAML Document: {doc_no}', ' ' * 4,  '>' * 5)            
            print(yaml_doc, '\n')
            for key, value in yaml_doc.items():
                print(f'key: {key}.\nvalue: {value}\n')
            count += 1
    except yaml.YAMLError as err:
        print(err)