import json

# first Function : json.loads()

# some JSON:
first_data =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
resuult_first = json.loads(first_data)

# the result is a Python dictionary: { mtlb Convert Kre dega JSON File Ko Dictionary me}
print(resuult_first["age"])


#second Function : json.dumps()

# some python Dictionary
second_data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
result_second = json.dumps(second_data)

# the result is a JSON string:
print(result_second)