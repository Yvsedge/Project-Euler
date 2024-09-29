l=[i for i in range(1,21)]
for i in range(len(l)):
	for j in range(1, 20):
		if l[j]%l[i]==0:
			l[j]=l[j]/l[i]
print()
m=1
for i in l:
	m*=i

print(int(m))