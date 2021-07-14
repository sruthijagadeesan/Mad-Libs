#Receiving all the input from the user
person = input("Your favourite person's name?? :")
verb = input("Some cool verb please :")
adjective = input("Shoot a unique adjective :")
verb2 = input("Some cool verb again please :")
weird_creature = input("What is you favourite weird creature?? :")
place = input("Your favourite or unfavourite place :")
thing = input("Something like a thing!! :")
punch_line = input("Finally say a punch line.. :")

#Using a 'f' string to concatenate the input variables
madlib = f"One day {person} was {verb}," "\n" f"and suddenly a {adjective} aeroplane flew above" "\n" f"the sky {verb2} millions of {weird_creature} from {place}" "\n" f"and also a box of {thing} with a letter" "\n" f"prompting {punch_line}!!!"

#Some Beautification
print("-------------------------")
print("Here's your Madlib!!!... Enjoy reading...!")
print("-------------------------")

#Prints out the madlib variable
print(madlib)