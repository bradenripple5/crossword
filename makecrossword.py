import numpy as np
import random,sys,re,copy,json
np.set_printoptions(linewidth=2000)    # default = 75

with open("wordlist.txt") as f:
	words = f.read().split("\n")
	
commonletters = {}
for word in words:
	for letter in word:
		if letter in commonletters:
			commonletters[letter][0] += 1
		else:
			commonletters[letter]  = [1]
for word in words:
	for letter in set(word):
		if len(commonletters[letter]) ==1:
			commonletters[letter] += [1]
		else:
			commonletters[letter][1]  += 1
sorted_dict = sorted(commonletters.items(),reverse=True,key=lambda item: item[1][0])

occupied_coordinates = []
wordlist = {}
random_words = []
wordslength = 2
random_words = np.random.choice(words,wordslength).tolist()
dim = 20

random_words = sorted(random_words, key= lambda i: sum([commonletters[k][0] for k in i]),reverse=True)
dim = max(dim,10+max([len(i) for i in random_words]))
print(random_words,len(random_words))

m = [[chr(random.randint(ord('a'),ord('z'))) for i in range(dim)] for i in range(dim)]
m = [[" " for i in range(dim)] for i in range(dim)]
m = np.matrix(m)

first_word = random_words.pop(0)
random_row = random.choice([i for i in range(1,m.shape[0]-1)])
random_col = random.choice([i for i in range(1,m.shape[1]-len(first_word)-1)])

for index, letter in enumerate(first_word):
	m[random_row,random_col+index] = letter

def valid_crossword(matrix,complete_list_of_words):
	columns = [matrix[:, i] for i in range(matrix.shape[1])]
	columns = [re.sub(" +", " ","".join([k[0] for k in i.tolist()])) for i in columns]
	for column in columns:
		words = column.split(" ")
		for word in words:
			if word not in complete_list_of_words:
				return False
	rows = [i for i in matrix]
	rows = [re.sub(" +", " ","".join(i.tolist()[0])) for i in rows]
	for row in rows:
		words = row.split(" ")
		for word in words:
			if word not in complete_list_of_words:
				return False
	return True

def slice_match(slice_,word):
	if len(word) > len(slice_):
		return -1

	for i in range(len(slice_)-len(word)+1):
		returnindex = 0
		if slice_[i:i+len(word)] != " "*len(word):
			for j in range(len(word)):
				if slice_[i+j] not in (word[j], " "):
					returnindex = -1
			if returnindex != -1:
				return i
	return -1

random_words = [np.random.choice(words)]	

words_to_add_total = 45
while  random_words:
	word_to_add = random_words[0]
	pickcolumn = np.random.choice([True, False])
	if pickcolumn:
		column_indices = [i for i in range(m.shape[1])]
		np.random.shuffle(column_indices)
		for i in column_indices:
			index =  slice_match("".join([h[0] for h in m[:,i].tolist()]), word_to_add)
			if index!= -1:
				previous_slice = copy.deepcopy(m[index:index+len(word_to_add),i])
				m[index:index+len(word_to_add),i] = np.matrix([[z]for z in word_to_add])
				if not valid_crossword(m,words):
					m[index:index+len(word_to_add),i]  = previous_slice
				else:
					random_words.remove(word_to_add)
					words_to_add_total -=1
					break
	else:
		row_indices = [i for i in range(m.shape[0])]
		np.random.shuffle(row_indices)
		for i in row_indices:
			index =  slice_match("".join([h.tolist() for h in m[i]][0][0]), word_to_add)
			if index!= -1:
				previous = copy.deepcopy(m[i,index:index+len(word_to_add)] )
				m[i,index:index+len(word_to_add)] = np.matrix([z for z in word_to_add])
				if not valid_crossword(m,words):
					m[i,index:index+len(word_to_add)]  = previous
				else:
					random_words.remove(word_to_add)
					words_to_add_total -=1

					break
	if words_to_add_total>0:
		random_words = [np.random.choice(words)]	
	else:
		random_words == []

		
print(m)
print(valid_crossword(m,words))


# def find(s, ch):
#     return [i for i, ltr in enumerate(s) if ltr == ch]

# def see_if_word_fits_in_slice(slice_,word):
# 	if len(word)> len(slice_):
# 		return False
# 	#slide word along slice_, comparing letters:
# 	for i in range(len(slice_)-len(word)):
# 		if slice_[i:i+len(word)] != " "*len(word):
# 			for j in range(len(word)):
# 				if slice_[i+j] != " ":
# 					if slice_[i+j] != word[j]:
# 						return False
# 			return i
# 	return False

# def can_add_word(word_chosen,matrix,vacant_intersections,direction):
# 	print(word_chosen,"= word_chosen")
# 	perpendicular_direction = (direction == "vertical")*"horizontal"+(direction == "horizontal")*"vertical"
# 	for word_placed in vacant_intersections[direction]:
# 		print(word_placed)
# 		for row,col in vacant_intersections[direction][word_placed]:
# 			print(row,col)
# 			possible_matching_letter = matrix[row,col]
# 			print(possible_matching_letter, " - possible_matching_letter")
# 			if possible_matching_letter in word_chosen:
# 				print(possible_matching_letter, "= is a matching letter")
# 				if perpendicular_direction == "horizontal":
# 					column_or_row = np.array(matrix[row,:])[0]
# 				else:
# 					column_or_row = [i[0] for i in np.array(m[:,col])]
# 				if see_if_word_fits_in_slice(column_or_row,word_placed)
# 				#now that you have a matching letter, you need to see if the word_chosen can fit, i.e. properly overlap


# 	# find placement of word_to_be_placed


# # you try to keep the direction the same until you can't add a word in that direction
# # if you can't add a word by changing the direction, the next step is to remove a word
# # while random_words:
# # 	word_chosen = random.choice(random_words)
# print(can_add_word(random_words[0],m,vacant_intersections,direction))