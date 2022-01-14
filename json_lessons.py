import json

c = {}
c['first_name'] = "Bill"
c['last_name'] = "Johnson"
c['cars'] = [{'brand': 'bmw',
              'model': 'impala',
              'color': 'red'},
             {'brand': 'mers',
              'model': 'bla',
              'color': 'black'}]
c['has_a_dog'] = True
c['money_in_pocket'] = 500

with open('c.json', 'w') as file_object:
    json.dump(c, file_object, indent=2)
# indent - отступы

with open('c.json', 'r') as file_object:
    k = json.load(file_object)

for k, v in k.items():
    print(k, ':', v)
