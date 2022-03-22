from Overwatch_database import Overwatch
import webbrowser

overwatch_output_file = open("Overwatch.txt", "w")
overwatch_output_file.write("3 is most highly recommended, 2 is recommended after three, so on and so forth \r\n \r\n")

while True:
    strat = input("Would you rather flank and be sneaky(1) play on the objective(2) or a little of both(3): \n")
    if not (strat == '1' or strat == '2' or strat == '3'):
        print("Please try again! You entered " + strat + " which we didn't recognize!\n")
    else:
        break

while True:
    team_play = input("Would you rather do most of the damage to the enemies(1) help your team stay alive(2) or a little of both(3): \n")
    if not (team_play == '1' or team_play == '2' or team_play == '3'):
        print("Please try again! You entered " + team_play + " which we didn't recognize!\n")
    else:
        break

while True:
    health = input("Would you rather be slow but have a lot of health(1) be fast with little health(2) or a mixture of the two(3): \n")
    if not (health == '1' or health == '2' or health == '3'):
        print("Please try again! You entered " + health + " which we didn't recognize!\n")
    else:
        break


user_list = [strat, team_play, health]
output_list = []


def open_web():
    buy_overwatch = input("Would you like to read more about the character(y/n): ")
    if buy_overwatch == "y" or buy_overwatch == "Y":
        webbrowser.open(Overwatch[key][1])
    else:
        print("Thank you for taking our test!")


for key in Overwatch:
    counter = 0
    for i in range(3):
        if user_list[i] == Overwatch[key][0][i]:
            counter += 1
        else:
            counter += 0
            break
    if counter == 3:
        print("\nBy taking this test we think that you should try playing " + key)
        print("Check for a file called Overwatch.txt that has your chachters name.")
        output_list.append("3.) " + key + "\r\n")
    elif counter == 2:
        output_list.append("2.) " + key + "\r\n")
    elif counter == 1:
        output_list.append("1.) " + key + "\r\n")
    elif counter == 0:
        output_list.append("0.) " + key + "\r\n")


output_list.sort()
output_list.reverse()
for char in output_list:
    overwatch_output_file.write(char)
overwatch_output_file.close()
open_web()