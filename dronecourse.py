import csv
import os
# this is a programme that updates the leaderboard of a drone racing club.

# the first step is choosing what leaderboard you want to update, we need a system where you can choose what type of leaderboard you want to update.

def formatting():
	print(" ")
	
def cont():
	print("\nPress enter to continue.")

# Get the directory of the Python script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path relative to the script directory
file_name = "tinywhoop1.csv"
tinywhoop_path = os.path.join(script_dir, file_name)

# the below function lets the user view every single time for every member

def viewLeaderboard():
	formatted_times = []
	with open(tinywhoop_path, encoding='utf-8') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		formatting()

		for row in csv_reader:
			formatted_times.append(row)

		def sort_key(time):
				return float(time[2])

		# sorting the times by lowest time to highest time
		formatted_times.sort(key=sort_key)

		# looping through all of the formatted times
		for row in formatted_times:
			print(f'{row[0]} {row[1]} raced a {row[2]} second time on course {row[3]}')
			formatting()


# the below function lets the user view individual members times and stuff
			
def view_entriesUser(fname, lname):
	with open(tinywhoop_path, encoding='utf-8') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		print(fname, lname + "'s race times:")
		formatting()

		total_times = 0
		total_time = 0
		formatted_times = []

		for row in csv_reader:
			if str(fname) == str(row[0]) and str(lname) == str(row[1]):
				formatted_times.append(row)
				total_times += 1
				total_time += int(row[2])

		def sort_key(time):
			return float(time[2])

		# sorting the times by lowest time to highest time
		formatted_times.sort(key=sort_key)

		# looping through all of the formatted times
		for row in formatted_times:
			print(f'{row[2]} second time on course {row[3]}')
			formatting()

		mean = round(total_time/total_times, 2)
		formatting()

		print("average time (in seconds): " + str(mean))
		formatting()
		print("times raced: " + str(total_times))
		formatting()
		print("total time racing (in minutes): " + str(round(total_time/60, 2)))

# function that straight up edits entries in the csv file.
def add_entryUser():
	formatting()
	newEntry = ""
	print("Make sure to capitlise first letter of all names!")
	fname = str(input("first name: "))
	lname = str(input("last name: "))
	time_in_seconds = int(input("time in seconds: "))
	race_course = str(input("course name: "))
	newEntry += str(fname + "," + lname + "," + str(time_in_seconds) + "," + race_course)
	formatting()
	print(f"{fname}'s time was uploaded to the leaderboard successfully!")

	with open('tinywhoop1.csv','a',) as csv_file:
		csv_file.write(newEntry)
		csv_file.write("\n")

# main function that's looped

def main():
	formatting()
	print("- Welcome to the leaderboards -")
	print("- Enter '1' to view all existing leaderboard times, enter '2' to view all existing times for a particular user or enter '3' to add a time to the leaderboard.")
	formatting()
	user_input = input()
	
	if user_input == "1":
		try:
			viewLeaderboard()
		except Exception as e:
			print("Error message: ", e)

	elif user_input == "2":
		formatting()
		first = input("User's first name (e.g. Britney): ")
		formatting()
		last = input("User's last name (e.g. Spears): ")
		formatting()
		try:
			view_entriesUser(first, last)
		except:
			print("Sorry, I can't find any entries under that name in the our database. Make sure the first letter of both the first and last name are capitalised with no extra spaces at the end.")
		
	elif user_input == "3":
		formatting()
		try:
			add_entryUser()
		except Exception as e:
			print("This isn't working right now, try again. Error message: ", e)
			
	else:
		print("You didn't enter a valid number, try again.")

while True:
	main()
	cont()
	input()
