# задание 1
str1 = [1,2,3,4,5,6,7,8,9,10]
su = 0
for i in range(len(str1)):
    su = su + str1[i]
print ("сумма элементов списка = " + str(su))

list1 = [1,2,3,4,5,6,7,8,9,10]
s = sum(list1)
print("сумма элементов списка = " + str(s))

# задание 2
list2 =['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'z', 'z', 'z', 'a' ]
from collections import Counter
c = Counter(list2)
print("дубликаты в списке:" +str([i for i, count in c.items() if count > 1]))
n = len(set(list2))
print("количество различных элементов: "+ str(n))
print("Топ-3: " + str(c.most_common(3)))

# задание 3
picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]
for i in range(len(picture)):
    l = len(picture[i])
    for j in range(l):
        if picture[i][j] == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print("")

   
