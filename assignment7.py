# represent the following date information as a tuple date_info(YEAR, MONTH, DAY):
# the year number
# the month number
# the day number
date_info = tuple[int, int, int]
YEAR = 0
MONTH = 1
DAY = 2


# represent the following Netflix show information as a tuple show_info(SHOW_TYPE, SHOW_TITLE, DIRECTOR_NAME, ACTOR_NAME, DATE_INFO):
# The type of show
# The title of the show
# A list of show director names
# A list of show actor names
# The date the show was added
show_info = tuple[str, str, list[str], list[str], date_info]
SHOW_TYPE = 0
SHOW_TITLE = 1
DIRECTOR_NAME = 2
ACTOR_NAME = 3
DATE_INFO = 4


def raise_to_power(base: list[int], exponent: list[int]) -> None:
    '''
    takes two lists of integers as arguments. The lists are not guaranteed to be the same length.
    The function should raise every element in first list to the power of the value at the
    corresponding position in the second list. Does not return a value
    '''
    num_elements_base  = len(base)
    num_elements_exponent = len(exponent)
    num_elements = 1
    if num_elements_base > num_elements_exponent:
        num_elements = num_elements_exponent
    else:
        num_elements = num_elements_base
    for index in range(num_elements):
        base[index] = base[index] ** exponent[index]


def create_date(date: str) -> date_info:
    '''
    takes a string representing a valid date and returns a date tuple
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    '''
    new_list = []
    the_date = date.split('-')
    day = int(the_date[0])
    
    month = 0
    
    if the_date[1] == 'Jan':
        month = 1
    elif the_date[1] == 'Feb':
        month = 2
    elif the_date[1] == 'Mar':
        month = 3
    elif the_date[1] == 'Apr':
        month = 4
    elif the_date[1] == 'May':
        month = 5
    elif the_date[1] == 'Jun':
        month = 6
    elif the_date[1] == 'Jul':
        month = 7
    elif the_date[1] == 'Aug':
        month = 8
    elif the_date[1] == 'Sep':
        month = 9
    elif the_date[1] == 'Oct':
        month = 10
    elif the_date[1] == 'Nov':
        month = 11
    else:
        month = 12
    
    year = int('20' + the_date[2])
    
    new_list.append(year)
    new_list.append(month)
    new_list.append(day)
    
    new_list = tuple(new_list)
    return (new_list)
    

def create_show(show_type: str, show_title: str, director_name: str, actor_name: str, date: str) -> show_info:
    '''
    takes five strings as arguments and creates and returns a Netflix Show tuple
    >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', '', '23-Sep-16')
    ['Bonni Cohen', 'Jon Shenk'], [], (2016, 9, 23))
    >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
    'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', '1-Jul-19')
    ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
    ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
    'Sally Hawkins', 'David Walliams', 'Timothy Spall'], (2019, 7, 1))
    '''
    new_list = []
    
    if director_name == '':
        director_names = []
    else:
        director_names = director_name.split(':')
        
    if actor_name == '':
        actor_names = []
    else:
        actor_names = actor_name.split(':')
        
    date = create_date(date)
    
    new_list.append(show_type)
    new_list.append(show_title)
    new_list.append(director_names)
    new_list.append(actor_names)
    new_list.append(date)
    
    new_tuple = tuple(new_list)
    return new_tuple

def get_titles(netflix_shows: list[show_info]) -> list[str]:
    '''
    takes a list of Netflix show tuples (as described in specification 3). 
    The function should return a list of the titles of each of Netflix shows 
    in the list in the order they appear in the given list of Netflix show tuples.
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
     (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'],\
     (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
    ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
      'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_titles(loshows)
    ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']
    '''
    new_list = []
    num_elements = len(netflix_shows)
    for index in range(num_elements):
        new_list.append(netflix_shows[index][SHOW_TITLE])
    return (new_list)


def is_actor_in_show(netflix_show: show_info, actor: str):
    '''
    takes the following two arguments:
    a Netflix show tuple (as described in specification 3)
    the name of an actor
    The function should return True if the given actor is an actor in the given Netflix 
    show tuple and False otherwise. The function should ignore case in the comparison 
    of names
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
     'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
     'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Justin Bieber')
    False
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
     'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
     'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'Michael Cera')
    True
    >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
    ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
     'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
    'Joe Lo Truglio', 'Kevin Corrigan'], \
    (2019, 9, 1)), \
    'MichaEL cerA')
    True
    '''
    num_elements = len(netflix_show[ACTOR_NAME])
    actor_in = False
    count = 0
    while actor_in == False and count < num_elements:
        if netflix_show[ACTOR_NAME][count].lower() == actor.lower():
            actor_in = True
        else:
            actor_in = False
            count += 1
    return (actor_in)
        
        

        
def count_shows_before_date(netflix_shows: list[show_info], date: date_info) -> int:
    '''
    takes the following two arguments:
    a list of Netflix show tuples (as described in specification 3)
    a date tuple (as described in specification 2).
    The function should return a count of the number only the Netflix show tuples
    for which the date they were added is before the given date in the calendar.
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
     (2017, 2, 6)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'],\
     (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], 
     (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
     ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
      'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2017, 4, 18))]

    >>> count_shows_before_date(loshows, (2015, 1, 1))
    0

    >>> count_shows_before_date(loshows, (2018, 10, 20))
    3
    '''
    count = 0
    num_elements = len(netflix_shows)
    for index in range(num_elements):
        if netflix_shows[index][DATE_INFO][YEAR] < date[YEAR]:
            count += 1
        elif netflix_shows[index][DATE_INFO][YEAR] == date[YEAR]:
            if netflix_shows[index][DATE_INFO][MONTH] < date[MONTH]:
                count += 1
            elif netflix_shows[index][DATE_INFO][MONTH] == date[MONTH]:
                if netflix_shows[index][DATE_INFO][DAY] < date[DAY]:
                    count += 1
    return (count)



def get_shows_with_actor(netflix_shows: list[show_info], actor: str) -> list[show_info]:
    '''
    takes the following two arguments:
    a list of Netflix show tuples (as described in specification 3)
    the name of an actor.
    The function should return a list of only the Netflix show tuples that the given actor has acted in.
    >>> loshows = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
     (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'], \
     (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
     ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
      'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
    (2019, 12, 31))]

    >>> get_shows_with_actor(loshows, 'Jonah Hill')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'], \
     (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21))]

    >>> get_shows_with_actor(loshows, 'jonaH hiLL')  # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Superbad', ['Greg Mottola'], \
     ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
      'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
      'Joe Lo Truglio', 'Kevin Corrigan'], \
     (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], \
     ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
      'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
      'Jemima Kirke'], \
     (2018, 9, 21))]

    >>> get_shows_with_actor(loshows, 'Justin Bieber')
    []
    '''
    new_list = []
    num_elements = len(netflix_shows)
    for index in range(num_elements):
        if is_actor_in_show(netflix_shows[index], actor) == True:
            new_list.append(netflix_shows[index])
    return (new_list)


