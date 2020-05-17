def translate_numeral(number):
	if type(number) == str:  # check type of input
		roman_numeral = number

		# ======enter code below======
		arabic_number = 0
		pups = {"I": 1, "X": 10, "C": 100, "M": 1000, "V": 5, "L": 50, "D": 500}
		translated_number = []
		for letter in roman_numeral:
			translated_number.append(pups[letter])

		print(translated_number)

		last_number = 0
		for current_number in translated_number:
			if current_number <= last_number:
				arabic_number = arabic_number + last_number
			else:
				arabic_number = arabic_number - last_number
			last_number = current_number
		arabic_number = arabic_number + last_number

		# ======enter code above======
		print('{0} translated to {1}!'.format(roman_numeral, arabic_number))  # print the result
		return arabic_number 

	else:
		print('Input not valid.')

if __name__ == '__main__':
	input_numerals = ['X', 'XXVIII', 'LXXI', 'XCIX', 'MCMXCIV']
	outputs = [10, 28, 71, 99, 1994]
	results = [True, True, True, True, True]

	for index in range(5):
		if translate_numeral(input_numerals[index]) != outputs[index]:
			results[index] = False

	if False in results:
		print('Not all numerals translated correctly. Try again.')
	else:
		print('Well done! All numerals translated correctly.')


