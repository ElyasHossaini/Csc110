def print_longer(number1: str, number2: str):
    '''
    user inputs 2 words and the longer word is then printed
    >>>print_longer(monkey, dog)
    monkey
    >>>print_longer(cat, log)
    cat
    >>>print_longer(log, monkey)
    monkey
    '''
    if len(number1) >= len(number2):
        print(number1)
    else:
        print(number2)
        
        
        
def print_real_roots(a: float, b: float, c: float):
    '''
     takes three floating point values representing the values of a, b and c
     in a quadratic equation and calculates the real roots of that equation. 
     >>>print_real_roots(1, 2, -8)
     2.000 , -4.000
     >>>print_real_roots(0, 3, 4)
     ERROR
     >>>print_real_roots(1, 2, 3)
     NO REAL ROOTS
    '''
    discriminant = (b ** 2) - (4 * a * c)
    denominator = 2 * a
    if a == 0:
        print('ERROR')
    elif discriminant < 0:
        print('NO REAL ROOTS')
    else:
        root1 = ((-1 * b) + (discriminant ** 0.5)) / (denominator)
        root2 = ((-1 * b) - (discriminant ** 0.5)) / (denominator)
        print(f'{root1:1.3f} , {root2:1.3f}')
        
        
        
def print_zodiac_sign(month: str, day: int):
    '''
    takes a month(str) and date(int) from the user and prints their zodiac sign
    >>>print_zodiac_sign(January, 19)
    capricorn
    >>>print_zodiac_sign(January, 20)
    aquarius
    >>>print_zodiac_sign(February, 18)
    aquarius
    >>>print_zodiac_sign(February, 19)
    pisces
    >>>print_zodiac_sign(March, 20)
    pisces
    >>>print_zodiac_sign(March, 21)
    aries
    >>>print_zodiac_sign(April, 19)
    aries
    >>>print_zodiac_sign(April, 20)
    taurus
    >>>print_zodiac_sign(May, 20)
    taurus
    >>>print_zodiac_sign(May, 21)
    gemini
    >>>print_zodiac_sign(June, 20)
    gemini
    >>>print_zodiac_sign(June, 21)
    cancer
    >>>print_zodiac_sign(July, 22)
    cancer
    >>>print_zodiac_sign(July, 23)
    leo
    >>>print_zodiac_sign(Augest, 22)
    leo
    >>>print_zodiac_sign(Augest, 23)
    virgo
    >>>print_zodiac_sign(September, 22)
    virgo
    >>>print_zodiac_sign(September, 23)
    libra
    >>>print_zodiac_sign(October, 22)
    libra
    >>>print_zodiac_sign(October, 23)
    scorpio
    >>>print_zodiac_sign(November, 22)
    scorpio
    >>>print_zodiac_sign(November, 23)
    sagittarius
    >>>print_zodiac_sign(December, 22)
    sagittarius
    >>>print_zodiac_sign(December, 23)
    capricorn
    '''
    
    if month == 'January' and day >= 20:
        print('aquarius')
    elif month == 'February' and day <= 18:
        print('aquarius')
    elif month == 'February' and day >= 19:
        print('pisces')
    elif month == 'March' and day <= 20:
        print('pisces')
    elif month == 'March' and day >= 21:
        print('aries')
    elif month == 'April' and day <= 19:
        print('aries')
    elif month == 'April' and day >= 20:
        print('taurus')
    elif month == 'May' and day <= 20:
        print('taurus')
    elif month == 'May' and day >= 21:
        print('gemini')
    elif month == 'June' and day <= 20:
        print('gemini')
    elif month == 'June' and day >= 21:
        print('cancer')
    elif month == 'July' and day <= 22:
        print('cancer')
    elif month == 'July' and day >= 23:
        print('leo')
    elif month == 'August' and day <= 22:
        print('leo')
    elif month == 'August' and day >= 23:
        print('virgo')
    elif month == 'September' and day <= 22:
        print('virgo')
    elif month == 'September' and day >= 23:
        print('libra')
    elif month == 'October' and day <= 22:
        print('libra')
    elif month == 'October' and day >= 23:
        print('scorpio')
    elif month == 'November' and day <= 21:
        print('scorpio')
    elif month == 'November' and day >= 22:
        print('sagittarius')
    elif month == 'December' and day <= 21:
        print('sagittarius')
    elif month == 'December' and day >= 22:
        print('capricorn')
    elif month == 'January' and day <= 19:
        print('capricorn')
    else:
        print('You wrote some bull didn\'t you?')

    
    
        
        
  
    
    
    