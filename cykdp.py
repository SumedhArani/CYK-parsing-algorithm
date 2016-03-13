start_state =[]
prod_rule ={}
table = []

def read_file(filename):
	global start_state, prod_rule
	fin =open(filename)
	non_terminal=fin.readline().split()
	terminal=fin.readline().split()
	start_state=fin.readline().split()
	#initializing the dictionary
	for state in non_terminal:
		if state not in prod_rule:
			prod_rule[state]=[]
	rule = list(map(lambda x: x[:-1], filter(lambda x:x!='\n', fin.readlines())))
	for x in rule:
		temp = list(map(str.strip, x.split("->")))
		prod_rule[temp[0]] = prod_rule[temp[0]]+[z.strip() for z in temp[1].split('|')]

def create_table(n):
	global table
	table = [[None for y in range(n-z)] for z in range(n)]

def fill_table(str):
	global table
	for ind in range(len(str)): #fills base line
		table[0][ind] = [x[0] for x in prod_rule.items() if str[ind] in x[1]] 
	#rest of the table
	for m in range(1,len(str)):
		for n in range(len(str) - m):
			table[m][n] = find_val(n, m+n)

def find_val(p,q):
	x1 = [(p, p+z)for z in range(q-p)]
	x2 = [(z+p+1, q) for z in range(q-p)]
	temp = list(zip(x1, x2))
	cross_union = product_union(temp)
	res = check(cross_union)
	return res

def check(union):
	temp = []
	for tups in union:
		restr = tups[0]+tups[1]
		temp.append([x[0] for x in prod_rule.items() if restr in x[1]])
	rvals = [w for v in temp if v!=[] for w in v]
	return(rvals)

def product_union(a):
	cross =[]
	for vals in a: 
		t1 = table[vals[0][1]-vals[0][0]][vals[0][0]] #n-m, n
		t2 = table[vals[1][1]-vals[1][0]][vals[1][0]] #n-m, n
		cross.append([(x,y) for x in t1 for y in t2])
	cross_res = [ y for x in cross for y in x]
	return (cross_res)

def main():
	filename = input()
	read_file(filename)
	input_str =input()
	create_table(len(input_str))
	fill_table(input_str)
	if(start_state[0] in table[len(input_str)-1][0]):
		print("Input is in the langauage of the given grammar")
	else: 
		print("Input is not in the langauage of the given grammar")

if __name__ == '__main__':
	main()