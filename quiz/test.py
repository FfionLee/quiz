list=[]

f=open('sample.txt','r')
print(f)
for i in f:
    print(i)
    list.append(i)
f.close()

f=open('s.txt','a')
f.write('hellooo')
f.close()

print(list)