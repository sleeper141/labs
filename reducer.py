print('country','totalpayout')
for z in keys
	t=0
	for b in sys.stdin.readlines():
		if z==b.split(", ")[2]: 
			c=b.split(", ")[4]
			t=t + float(c.replace(' ', ''))
	print(z,str(t))
		

