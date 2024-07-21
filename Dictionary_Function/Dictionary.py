dic = { "Prateek" : "He Is A Good Boy",
        "Vishal" : "He Is TL Of RIPL",
        "Vaishali" : "She Is A Girl",
        "Kuldeep" : {"Father" : "He Is Father Of Vaishal,Vaishali,Prateek",
                        "Husband" : "He Is Husband Of Mrs. Sunita Yadav"},
        "Sunita" : { "Mother" : "She Is Mother Of Vaishal,Vaishali,Prateek",
                        "Wife" : " She Is Wife Of Mr. Kuldeep Yadav"}
    }
    
#print(dic)

#copy a Dictionery To Another Dictionary
dic2=dic.copy()

print(dic["Sunita"]["Mother"])

#This Function Is Use To update Key value
# This Is Function Type update Key Value 
dic.update({"Chootu":"He is Prateek"})
print(dic["Chootu"])

#This is Without Function update key Value
dic["Golu"]="He Is Vishal Yadav"
print(dic["Golu"])

#this Function Use To Delete Some Key Value
del dic["Chootu"]
#print(dic2)

#Only Print Key Of Dictionary
print(dic.keys())

#Only print Item Of Dictionary mean print Key And Value
print(dic.items())

print(dic)