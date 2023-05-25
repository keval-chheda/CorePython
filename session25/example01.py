# import json
#
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["age"])


import json

with open('C:/Users/Admin/Desktop/jsonex.json') as f:
  state_data= json.load(f)

for state in state_data['states']:
  del state['name']

with open('C:/Users/Admin/Desktop/new_states.json', 'w') as f:
  json.dump(state_data, f, indent=2)