# Loops, While Do
# i=1
# while i<10:
#     print("#")
#     i=i+1
# Break keyword
# from logging import logProcesses
# i=1
# while i<8:
#     x=20
#     print(x)
#     print(i)
#     if i==3:
#         continue
#         # break
#     i=i+1

# ----------29/10/22----------
# Loops 
    # student=["anurag","vishal","vishnu","binod"]
    # color=["red","blue","green"]
    # for i in student:
    #     print(i)
    # for j in student:
    #     if j==student[2]:
    #         break
    #     print(j)

    # for i in range(5,10):
    #     print(i)
        
    # for i in student:
    #     for j in color:
    #         print(i,j)
    
# DataTypes: Tuple(Ordered and Unchangable)
    # a = ("anurag","suphal","sai")
    # print(a[0],len(a),type(a))
    # print(a[1:2])
    # if "anurag" in a:
    #     print("ys it is")
    # b=list(a)
    # b[1]="virus"
    # a=tuple(b)
    # print(a)
    # x=(1,2,3)
    # c=a+x
    # print(c)
# Set
    # a = {"anurag","suphal","sai"}
    # a.add("virus")
    # b={1,2,3}
    # a=a.union(b)
    # print(a)

# DataTypes: Dictionary
# ordered , changable, no dublicate
# works on the concept of key and value
a={"name":"Suphal","company":"cipherschools","college":"LPU"}
# print(a)
print(a["name"])
a["degree"]=["engineering"]
print(a.keys())
if "name" in a:
    print("its therr")
    

