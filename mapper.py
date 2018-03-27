kar=set()
for line in sys.stdin:
		a=line.split(", ")[2]
		kar.add(a)
for a in kar:
	print(a)

