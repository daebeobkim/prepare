import sys
import datetime
from datetime import datetime as DT
now=DT.now()
DATE=str(now.date())
"""
x=0
y=0
c=0
n=4
list1 = []
List = []
for count in range(n):
    list1.append(str(input("이름을 입력하세요: ")))
    list.append(input("시각을 입력하시오: "))
    if count/2 == 0:
        z = "출근"
    else:
        z = "퇴근"
    c+=1
    x+=1
    y+=1


for x in range(n):
    print("{0},{1},{2},{3}".format(list1[x],now.date(),List[x],z[c]))
       
"""
"""
List = [["A", "C"], ["A", "C"],["A", "C"],["A", "C"]]
for index in range(len(List)):
    List[index].insert(1, "B")
print(List)



for index in range(): 
print("{0} {1}".format(List,List))

for x in range(n):
    print(list1[x],"회원,",now.date(),",",list[x],z)
  


"""

n=4
x=0
List = []
for index in range(n):
    List.append([input(str("이름을 입력하시오")),input("시간을 입력하시오")])
    List[index].insert(1,DATE)
     
    if index%2 == 0:
        List[index].insert(3,"출근")
    else:
        List[index].insert(3,"퇴근")

print(List)


with open("C:/Users/user/Desktop/파이썬/1.txt", 'w',encoding='UTF-8') as f:
    for index in List:
        f.write(str(index)+"\n")

sys.exit(1)

print("해치웠나")




