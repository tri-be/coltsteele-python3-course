# # Define list my_stuff, at least 4 elements long with 1 str and 1 float
# my_stuff = ['stuff', 11.11, 'guitar', 'synth']
# # Define list nums, with numbers 1 through 99
# nums = list(range(1,100))

# # Accessing List Data

# # Don't touch list
# people = ["Hanna", "Louisa", "Clauida", "Angela", "Geoffrey", "aparna"]
# # Change "Hannah" to "Hannah"
# people[0] = "Hannah"
# # Change Geoffrey to Jeffrey
# people[-2] = "Jeffrey"
# # Change "aparna" to "Aparna"
# people[-1] = "Aparna"
# print(people)

# # For loop to print elements in list
# colors = ["purple", "teal", "magenta", "olive green", "living coral", "vermillion"]
# for color in colors:
# 	print(color)

# # For loop to print doubled value of numbers in list
# numbers = list(range(1,11))
# for number in numbers:
# 	print(number * 2)

# # while loop using formatted string to indicate index
# colors = ["purple", "teal", "magenta", "olive green", "living coral", "vermillion"]
# index = 0
# while index < len(colors):
# 	print(f"{index}: {colors[index]}")
# 	index +=1

# loop through list sounds and add strings together, uppercase, saved to variable 'result'
sounds = ['super', 'cali', 'fragil', 'istic', 'expi', 'ali', 'docious']
result = ''
for sound in sounds:
	result += sound
result = result.upper()
