#Программа получает дискретную эмпирическую последовательность
#и считает локальные минимумы

seq =[]
locmin = []
for i in 2:
	a = int(input())
	seq.append(a)
	print(i)	#отладчик
while true:
	a = int(input())
	seq.append(a)
	if seq[-2] < seq[-3] and seq[-2] < seq[-1]:
		locmin.append(seq[-2])
	print(seq)
	print(locmin)
