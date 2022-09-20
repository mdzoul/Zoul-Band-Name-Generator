#1. Create a greeting for your program.
print("Yo! Welcome to Zoul's Band Name Generator!\nWe are gonna make it simple and combine the name of your city and the name of a pet to create your very own band name!\n")
#2. Ask the user for the city that they grew up in.
city_name = input('So to start the ball rolling, what city did you grow up in?\n')
print('Awesome! You grew up in ' + city_name + '.\n')
#3. Ask the user for the name of a pet.
pet_name = input('Next question: What is the name of a pet you own?\n')
print('Wow! ' + pet_name + ' is a great name for a pet!\n')
#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + ' ' + pet_name
print('Congratulations! Your new band name is now ' + band_name + '!')
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end