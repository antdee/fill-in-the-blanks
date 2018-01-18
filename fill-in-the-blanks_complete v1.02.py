# IPND Stage 2 Final Project

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!
numbered_blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___", "___7___","___8___"]
data = {
		"easy":{				# Difficulty level.
		"phrase":				# Phrase with the blanks to fill.
			'''\nA ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
			adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
			don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
			tuple, and ___4___ or can be more complicated such as objects and lambda functions.''',
		"answers":				# The correct asnwers.
			["function", "parameters", "none", "list"],
		"blanks_to_fill": 4		# The number of the blanks to fill before the level is complete.
				},
		"medium":{
		"phrase":
		 	'''\n___1___ is often defined in terms of the three ___2___s or ___4___s that it provides. 
			___1___ serves as a medium of ___3___, as a store of value, and as a unit of account. Medium of ___3___. 
			___1___'s most important ___2___ is as a medium of ___3___ to facilitate ___5___. Without ___1___, all 
			___5___ would have to be conducted by barter, which involves direct ___3___ of one ___6___ or ___4___ 
			for another. The difficulty with a barter system is that in order to obtain a particular ___6___ or ___4___ 
			from a supplier, one has to possess a ___6___ or ___4___ of equal value, which the supplier also desires''',
		"answers":
			["money", "function", "exchange", "service", "transactions", "good"],
		"blanks_to_fill" : 6
				 },
		"hard":{
		"phrase":
			'''\n___1___ have played a major role in human's lives throughout history. Today, scientific research is trying 
			to ___2___ the positive aspects of living ___8___ companion ___1___. ___1___ have been used as an ___4___ form
			of treatment for many years. More recently it has been ___2___ed that owning a ___3___ can ___6___ lower ___5___'s
			blood pressure,  enhance the chances of living after a heart attack, keep ___5___ more active and ___7___ more 
			satisfaction ___8___ life. It is theorized that this happens because ___3___s ___6___ ___5___ become more social, 
			___7___ a means to give and receive affection, and ___6___ connect us ___8___ the natural world.''',
		"answers":
			["animals", "discover", "pet", "alternative", "people", "help", "provide", "with"],
		"blanks_to_fill": 8
				 }
		}


def difficulty_selection():			# Prompts the user to select adifficulty level and defines it for the rest of the program
	while True:
		level = raw_input("Please select the game difficulty level \nSelect from easy, medium or hard\n").lower()
		if level in data:			# Checks in our data library if the user selected a valid level.
			return level
		print "That is not a valid option!!! Try AGAIN!"	


def fill_in_the_blanks():								# Here we start the main code
	diff, index, tries = difficulty_selection(), 0, 5	# index : Counts how many blanks have filled already	
	while index <= data[diff]["blanks_to_fill"]:		# Stops the loop when the number of blanks filled is the same as the difficulty level
		while tries > 0:
			print data[diff]["phrase"], "\nPlease find the correct word to fill the blanks with \nNumber of tries remaining :", tries
			user_input = raw_input("type replacement for" + numbered_blanks[index]).lower()
			if user_input == data[diff]["answers"][index]:												# Here we check if the answer is correct
				data[diff]["phrase"] = data[diff]["phrase"].replace(numbered_blanks[index], user_input) # Replace the blank with the answer
				print "Good job! The answer", user_input, " is correct!!!\nHere is the updated text"
				index, tries = index + 1, 5																# Increase the index, reset the number of tries
				if index == data[diff]["blanks_to_fill"]:												# See if we filled all the blanks
					print "Congratulations! Quiz completed!! \nHere is the complete text!!"				
					return data[diff]["phrase"]															# End the function
			else:
				tries -= 1														# Lose a try
				print "Incorrect answer!"
				if tries <= 0:													# If tries go to zero, Game over, else repeat the loop.
					return "Game Over"


print fill_in_the_blanks()