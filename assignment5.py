import doctest
import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5


def get_sequence(start: int, increment: int, max_val: int) -> str:
    '''
    takes three integer values representing the starting value, 
    the increment and the maximum value to append to the result sequence.
    >>> get_sequence(2, 5, 32)
    '2,7,12,17,22,27,32'
    >>> get_sequence(2, 5, 31)
    '2,7,12,17,22,27'
    '''
    range_val = int((max_val-start)//increment)
    result = ''
    for i in range(range_val+1): 
        increments = (start + (i * increment))
        result += str(increments) + ','
    return (result[:-1])
        
        
        
def digit_sum(digit: int) -> int:
    '''
    takes an integer and returns the sum of each digit in the integer. 
    If the integer is a negative value, the function should ignore the negative
    >>> digit_sum(0)
    0
    >>> digit_sum(1)
    1
    >>> digit_sum(12)
    3
    >>> digit_sum(123)
    6
    '''
    positive_digit = abs(digit)
    final_num = 0
    while positive_digit > 0:
        pos_num_modulo = positive_digit % 10
        positive_digit = positive_digit // 10
        final_num += pos_num_modulo
    print(final_num)


def sum_factors(n: int) -> int:
    '''
    takes a whole number (greater than zero). The function should return 
    the sum of the all the factors of that number excluding itself.
    >>> sum_factors(1)
    1
    >>> sum_factors(0)
    0
    >>> sum_factors(12)
    16
    '''
    total = 0
    for i in range(1, n+1):
        if n % i == 0:
            total += i
    return (total - n)


def is_perfect(n: int) -> bool:
    '''
    takes a whole number (greater than zero). The function should 
    determine whether the given number is a perfect number.
    >>> is_perfect(0)
    True
    >>> is_perfect(6)
    Ture
    >>> is_perfect(7)
    False
    '''
    if sum_factors(n) == n:
        return True
    else:
        return False



def n_perfect_numbers(n: int) -> str:
    '''
    takes a non-negative integer n. The function should return a 
    string containing the first n perfect numbers.
    >>> n_perfect_numbers(0)
    ''
    >>> n_perfect_numbers(1)
    '6'
    >>> n_perfect_numbers(4)
    '6,28,496,8128'
    '''
    result = ''
    count = 0
    num = 1
    
    while count < n:
        if is_perfect(num):
            if count > 0:
                result += ','
            result += str(num)
            count += 1
        num += 1
    
    return (result)

    
    






def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    # this line MUST be uncommented when submitting to PrairieLearn
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    # die = int(input('enter a simulated dice roll\n'))

    return die
    
    
def take_turn(player_name: str, player_points: int, round_number: int) -> int:
    '''
    The function should repeatedly simulate the roll of the three dice, calculate the roll 
    score and add the roll score to the players current points. The function will continue 
    to do this until the player has a roll score that is worth 0 or the player has accrued 
    at least 21 total points. The function should return the updated total number of points 
    the player has accrued.
    '''
    print('Player' , player_name , 'is taking a turn in round' , round_number)
    total_points = player_points
    scored_points = 1
    while (scored_points != 0) and (total_points < 21):
        roll_1 = roll_one_die()
        roll_2 = roll_one_die()
        roll_3 = roll_one_die()
        print('Three dice rolled:' , roll_1 , ',' , roll_2 , ',' , roll_3)
        if roll_1 == round_number and roll_2 == round_number and roll_3 == round_number:
            scored_points = 21
            total_points += scored_points
        elif roll_1 == roll_2 and roll_2 == roll_3:
            scored_points = 5
            total_points += scored_points
        elif roll_1 == round_number and roll_2 == round_number and roll_3 != round_number:
            scored_points = 2
            total_points += scored_points
        elif roll_1 == round_number and roll_3 == round_number and roll_2 != round_number:
            scored_points = 2
            total_points += scored_points
        elif roll_3 == round_number and roll_2 == round_number and roll_1 != round_number:
            scored_points = 2
            total_points += scored_points
        elif roll_1 == round_number and roll_2 != round_number and roll_3 != round_number:
            scored_points = 1
            total_points += scored_points
        elif roll_2 == round_number and roll_1 != round_number and roll_3 != round_number:
            scored_points = 1
            total_points += scored_points
        elif roll_3 == round_number and roll_2 != round_number and roll_1 != round_number:
            scored_points = 1
            total_points += scored_points
        else:
            scored_points = 0
            total_points += scored_points
        print('scored:' , scored_points)
        print('Total points:' , total_points)
    return (total_points)


def play_round(player_1: str, player_2: str, round_number: int) -> str:
    '''
    In simulating a round of the game the function has the given players alternate taking turns 
    rolling the dice for points (described above in 6.1). The function will alternate turns
    starting with the first player until one of the players reaches at least 21 points. The 
    round should stop immediately when a player reaches 21, not allowing the other player to
    have another turn. 
    '''
    total_1 = 0
    total_2 = 0
    game_on = True
    
    while total_1 < 21 and total_2 < 21 and game_on:
        total_1 = take_turn(player_1, total_1, round_number)
        if total_1 >= 21:
            game_on = False
        if game_on:
            total_2 = take_turn(player_2, total_2, round_number)
            if total_2 >= 21:
                game_on = False
        
    if total_1 > total_2:
        print('the winner of this round is' , player_1)
        winner = player_1
    else:
        print('the winner of this round is' , player_2)
        winner = player_2
    print(player_1 , 'has' , total_1 , 'points and' , player_2 , 'has' , total_2 , 'points')
    return winner


