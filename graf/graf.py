#1
#a = int(input())
#print(a,'вершины')
#m = []
#for i in range(a):
#  m.append(input().split())
#print('ввод окончен')

#for i in range(a):
#  sum = 0
#  k = ''
#  for j in range(a):
#    if(m[i][j] == '1'):
#      sum = sum + 1
#     k = k + str(j+1) + " "
#  print("sum =", sum,",", i+1, ":", k)

#2
# a = int(input())
#b = int(input())
#arr = []
#for i in range (a):
#  arr.append([])
#for i in range(b):
#  c = input().split()
#  first = int(s[0])-1
#  second = int(s[1])-1
#  arr[second].append(first+1)
#  arr[first].append(second+1)
#for i in range(a):
#  c = str(sorted(arr[i]))
#  c= k.replace('[', '')
#  c= k.replace(']', '')
#  print(i+1, ":", c)

#3
#a = int(input("введите количество вершин: "))
#lst = []
#pairs = []
#print("введите список смежности по типу '1:3,2' ")
#for i in range(a):
#  c = input().split(":")
#  c[1] = c[1].split(',')
#  lst.append(c[1])


#for i in range(a):
#  for j in range(len(lst[i])):
#    pairs.append([int(i+1),int(lst[i][j])])
#print("Ввод окончен")
#pairs2 = pairs.copy()
#for i in range(len(pairs)):
#  for j in range(len(pairs)):
#    f1 = int(pairs[i][0])
#    f2 = int(pairs[j][0])
#    z1 = int(pairs[i][1])
#    z2 = int(pairs[j][1])
#    if(f1 == z2 and z1 == f2):
#      pairs2.remove(pairs[i])
#      pairs[i].reverse()
#print("Список ребер:")
#for i in range(len(pairs2)):
#  print(pairs2[i])


#4
#s1 = input().split()

#a = int(s1[1]) # кол ребер
#b = int(s1[0]) # кол вершин

#arr = [] # список смежности
#for i in range (b):
#  arr.append([])

#for i in range(a):
#  s = input().split()
#  first = int(s[0])-1
#  second = int(s[1])-1
#  arr[second].append(first+1)
#  arr[first].append(second+1)

#c = int(input()) # нач точка

#arr_smezh = [False for i in range(len(arr))]
#output = []

#def dfs(node):
#  arr_smezh[node-1] = True
#  output.append(node)
#  count = 0
#  for neighbor in arr[node-1]:
#    if arr_smezh[neighbor-1]:
#      count = count + 1
#    if not arr_smezh[neighbor-1]:
#      dfs(neighbor)
#    if count == len(arr[node-1]):
 #     output.append(node-1)

#dfs(c)
#print("cписок смежности:")
#print(arr)
#print("количество ходов:")
#print(len(output))
#print("список точек:")
#print(output)

