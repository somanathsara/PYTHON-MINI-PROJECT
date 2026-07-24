# data = [{"name":"ram","age":12},{"name":"shyam","age":5}]
# for i in range(len(data)):
#     print(data[i]["name"])
#     print(data[i]["age"])
# import os
# print(os.listdir())
# FileNotFoundError
# a = "jaisri ram"
# j = a[3:]
# print(j,type(j))
# a = "hello ram gudu"
# part = a.split()
# print(part)
import os
# print(os.path.expanduser("~"))
# print(os.environ["USERPROFILE"])
def tree(path,prefix= ""):
    data = os.listdir(path) 
    for index,i in enumerate(data,start = 0):
        full_path = os.path.join(path,i)
        if len(data) - 1 == index:
            connector = "|____"
        else:
            connector = "|----"
        if len(data) - 1 == index:
            new_prefix = prefix + "      "
        else:
            new_prefix = prefix + "|     "
        if i.startswith("."):
            continue
        print(prefix+ connector + i)# concatenation
        # print(i)
        if os.path.isdir(full_path):
            tree(full_path,new_prefix)
cd = os.getcwd()
tree(cd,"")