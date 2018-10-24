def BalancedParen(str):

	bSet = {'(':')', '[':']', '{':'}'} # balanced set
	# print(bSet)

	# scan str
	pSet = []
	for c in str:
		# print(bSet[c])
		if c == '(' or c =='[' or c == '{': # open paren must before closing
			pSet.append(c)
		elif c == ')' or c ==']' or c == '}':
			if not pSet: # if there was no opening then it is imbalanced 
				print('imbalanced list: ' + str)
				return False
			elif bSet[pSet[-1]] == c:
				pSet.pop() # remove the last element				
			else:
				print('imbalanced list: ' + str)
				return False
	if not pSet:
		print('balanced list: ' + str)
		return True
