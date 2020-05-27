"""
{ user1 : {스파이시 :0,
         솔티: 1,
         } ,
 user 2 : {스파이시 :0,
         솔티: 1,
         }        
         }"""


# 1. 맛 => [,,]


taste = ['a','b','c','f','g','d']

dic ={}
for i, j in enumerate(taste):
    print(i, j )
    dic[j] = i

print(dic)

taste1 = ['A','B','C','F','G','D']

di = {} 
for k,q in zip(taste1,taste):
    di[k] = di
    
    print(k,q )
