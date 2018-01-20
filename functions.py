def rent_a_car():
    print('***Welcome to rent a Car***')
    car = True
    while car:
    #for choosing car
        car = input('Which car do you want to take in rent?\n')
    #for choosing the sentence to write on car
        print('select the sentence\n1.Hum chale dushman jale\n2.Dekh kar dua krna\n3.Himmat hai to pass kr warna bardash kr.')
    #selecting the sentence
        msg=int(input('What do you want to write on your car'))
    #asking the user for other car
        repeat = input('Do you want to choose an other car? (yes/no)\n')
    #For car name if it start from vowel sound or not
        if car[0] == 'a' or car[0] == 'e' or car[0] == 'i' or car[0] == 'o' or car[0] == 'u':
            print('Let me see if I could find you an', car.title())
        else:
            print('Let me see if could find you a', car.title())
    #printing sentence on the car
        if msg == 1:
            print('Congratulations! we\'ve your car and written'+' "Hum chale dushman jale"'+' for you on your '+car.title() )
        elif msg == 2:
            print('Congratulations! we\'ve your car and written'+' "Dekh kar dua krna"'+' for you on your '+car.title())
        elif msg == 3:
            print('Congratulations! we\'ve your car and written'+' "Himmat hai to pass kr warna bardash kr"'+' for you on your '+car.title())
    #ending condition
        if repeat == 'no':
            car = False
#Good bye msg
    print('\n ***Hum chale dushman jale***\n   ***Dekh kar dua karna***')
#calling function
rent_a_car()