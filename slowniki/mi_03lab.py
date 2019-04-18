# slowniki:
dic = {1:"ala", 2:"ela"}
dic.get(77, "default")
#del dic[1]
dic == dict([(7, "zosia"), (2, "ela")])

dic == dict([(7,"zosia"), (2,"ela")])
dic1 = {"ala":"kowalska", "ela":"nowak"}
dic1["jan"]="kowalski"
dic.update(dic1)


dic2 = {k:k*k for k in range(1,5)}

print([len(d) for d in (dic2,dic7)])