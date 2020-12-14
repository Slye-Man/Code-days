# Create a greeting for your program

greet = "Hello! Welcome to the Band Name Generator Project"
print(greet)
print (' ')

# Ask which city they are up in and what are the names of their first pet

ask = input('Would you like to generate a band name?: (y/n) \n')
if ask == 'y':
    city = input("Which city did you grow up in? \n")
    pet = input("What is the name of your first pet? \n")
# Combine their city and pet name and show them their band name

    bandName = 'The name of your band is {} {}'.format(city,pet)
    print(bandName)

else:
    print('Ahh, well we hope you find something better')

