import json

# first Function : json.loads()

# some JSON:
first_data =  '{ "name":"John", "age":30, "city":"New York"}'
print(type(first_data))

# parse x:
resuult_first = json.loads(first_data)

# the result is a Python dictionary: { mtlb Convert Kre dega JSON File Ko Dictionary me}
print(resuult_first["age"])


#second Function : json.dumps()

# some python Dictionary
second_data = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "married" : False
}

# convert into JSON:
result_second = json.dumps(second_data)
print(type(result_second))

# the result is a JSON string:
print(result_second)




# import json

# json_data = '{ "name": "prateek Yadav","class": ["MCA","BSc"], "ismarried" : false, "age" : 24, "parent": {"father" : "kuldeep", "mother": "sunita" }  }'

# pase_data=json.loads(json_data)

# print(pase_data)
# print(type(pase_data))
# print(pase_data["name"])
# print(pase_data["class"])
# print(pase_data["class"][1])
# print(pase_data["age"])
# print(pase_data["ismarried"])
# print(pase_data["parent"])
# print(pase_data["parent"]["father"])
# print(pase_data)


# import json 

# data = { 
# 	"name": "Satyam kumar", 
# 	"place": "patna", 
# 	"skills": [ 
# 		"Raspberry pi", 
# 		"Machine Learning", 
# 		"Web Development"
# 	], 
# 	"email": "xyz@gmail.com", 
# 	"projects": [ 
# 		"Python Data Mining", 
# 		"Python Data Science"
# 	] 
# } 
# with open( "data_file.json" , "w" ) as write: 
# 	json.dump( data , write ) 


# import json 

# with open( "data_file.json" , "r" ) as read_file: 
#   dict_data=json.load(read_file)
  
# print(dict_data["projects"])