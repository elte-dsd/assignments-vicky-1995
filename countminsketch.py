import numpy as np

lookup = np.array([[0,1,3,4,2],[1,0,2,4,1],[0,3,2,1,4]])
print(lookup)

count_matrix = np.zeros((5,5))
print(count_matrix)

stream = ['A','B','C','A','C','A','B','B','C']

def ask_user():
	letter = input("input the letter you want to add to stream: ")
	if letter not in ['A','B','C']:
		print("Enter A, B or C")
		ask_user()
	else:
		stream.append(letter)
	return letter

letter = ask_user()
print(stream)

value = []
for s in stream:
	letter = s
	if letter == 'A':
		value.append(0)
	elif letter == 'B':
		value.append(1)
	elif letter == 'C':
		value.append(2)
print(value)

h1 = 0
h2 = 1
h3 = 2
h4 = 3
h5 = 4

for i in value:
	t1 = lookup[i][0]
	t2 = lookup[i][1]
	t3 = lookup[i][2]
	t4 = lookup[i][3]
	t5 = lookup[i][4]

	count_matrix[h1][t1] += 1
	count_matrix[h2][t2] += 1
	count_matrix[h3][t3] += 1
	count_matrix[h4][t4] += 1
	count_matrix[h5][t5] += 1

print(count_matrix)

current_letter = input("Input the letter in the stream you want to count the frequency of: ")
if current_letter == 'A':
	current_value = 0
elif current_letter == 'B':
	current_value = 1
elif current_letter == 'C':
	current_value = 2

current_t1 = lookup[current_value][0]
current_t2 = lookup[current_value][1]
current_t3 = lookup[current_value][2]
current_t4 = lookup[current_value][3]
current_t5 = lookup[current_value][4]

print(current_t1, current_t2, current_t3, current_t4, current_t5)

print("frequency of ",current_letter, " =", 
	int(min(count_matrix[0][current_t1],
		count_matrix[1][current_t2], 
		count_matrix[2][current_t3],
		count_matrix[3][current_t4],
		count_matrix[4][current_t5])))
