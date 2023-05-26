import csv
# this is a programme that updates the leaderboard of a drone racing club.

# the first step is choosing what leaderboard you want to update, we need a system where you can choose what type of leaderboard you want to update.

# below are the preexisting leaderboards

#tinywhoop1
#tinywhoop2
#tinywhoop3
def formatting():
	print("-"*20)

def viewLeaderboard():
	with open('tinywhoop1.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		formatting()
		for row in csv_reader:
			print(f'{row[0]} {row[1]} raced a {row[2]} second time on course {row[3]}')
			formatting()
			
def view_entriesUser(fname, lname):
	with open('tinywhoop1.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		print(fname, lname + "'s race times:")
		formatting()
		total_times = 0
		total_time = 0
		for row in csv_reader:
			if str(fname) == str(row[0]) and str(lname) == str(row[1]):
				print(f'{row[2]} second time on course {row[3]}')
				total_times +=1
				total_time += int(row[2])
				mean = round(total_time/total_times, 2)
				formatting()
				
		print("average time (in seconds): " + str(mean))
		print("times raced: " + str(total_times))
		print("total time racing (in minutes): " + str(round(total_time/60, 2)))
				

def main():
	formatting()
	print("- Welcome to the leaderboards -")
	print("- Enter '1' to view all existing leaderboard times or enter '2' to view all existing times for a particular user")
	formatting()
	user_input = input()
	
	if user_input == "1":
		viewLeaderboard()
		
	elif user_input == "2":
		first = input("User's first name (e.g. Shaun): ")
		formatting()
		last = input("User's last name (e.g. Cantwell): ")
		formatting()
		view_entriesUser(first, last)
		
	else:
		print("Not a valid input rip")
	
		
main()
		