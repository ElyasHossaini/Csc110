import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR,
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6



def create_date(date: str) -> Date:
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
    


def create_show(show_type: str, show_title: str, director_name: str, actor_name: str, date: str) -> NetflixShow:
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



def read_file(filename: str) -> list[NetflixShow]:
    """ Reads file at filename into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), \
    ('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
    ('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), \
    ('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
    ('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
    ('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    """
    # TODO: complete this method according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    new_list = []
    file_handle = open(f'{filename}', 'r', encoding='utf8')
    line = file_handle.readline()
    line = file_handle.readline()
    file_list = line.split(',')
    while line != '':
      new_list.append(create_show(file_list[INPUT_TYPE], file_list[INPUT_TITLE], file_list[INPUT_DIRECTORS], file_list[INPUT_CAST], file_list[INPUT_DATE]))
      line = file_handle.readline()
      file_list = line.split(',')
    file_handle.close()
    return (new_list)
    


def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    """ Returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    """
    # TODO: complete this function according to the documentation
    new_list = []
    num_elements = len(show_data)
    smallest_year = 999999999999
    smallest_month = 999999999999
    smallest_day = 999999999999
    
    for index in range(num_elements):
      if show_data[index][DATE][YEAR] < smallest_year:
        smallest_year = show_data[index][DATE][YEAR]
        smallest_month = show_data[index][DATE][MONTH]
        smallest_day = show_data[index][DATE][DAY]
      elif show_data[index][DATE][YEAR] == smallest_year:
        if show_data[index][DATE][MONTH] < smallest_month:
          smallest_month = show_data[index][DATE][MONTH]
          smallest_day = show_data[index][DATE][DAY]
        elif show_data[index][DATE][MONTH] == smallest_month:
          if show_data[index][DATE][DAY] < smallest_day:
            smallest_day = show_data[index][DATE][MONTH]
    
    for index in range(num_elements):
      if show_data[index][DATE][YEAR] == smallest_year and show_data[index][DATE][MONTH] == smallest_month and show_data[index][DATE][DAY] == smallest_day:
        new_list.append(show_data[index][TITLE])
    
    return (new_list)
    

      


def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    """ Returns a sorted list of actors that are in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts) # doctest: +NORMALIZE_WHITESPACE
    ['Emma Stone', 'Hugh Bonneville', 'Lily Travers', 'Michael Cera', \
    'Om Puri', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Jonah Hill', 'Om Puri']
    """
    # TODO: complete this function according to the documentation
    
    
    final_list = []
    list_all_actors = []
    num_elements = len(shows)
    for index in range(num_elements):
      list_all_actors += shows[index][CAST]
    
    list_all_actors.sort()
    
    num_elements_list_all_actors = len(list_all_actors)
    largest_count = 0
    count = 1
    for index in range(1,num_elements_list_all_actors):
      if list_all_actors[index] == list_all_actors[index-1]:
          count += 1
          if count > largest_count:
            largest_count = count
      else:
        count = 0
    
    count = 0
    for index in range(1, num_elements_list_all_actors):
      if list_all_actors[index] == list_all_actors[index-1]:
        count += 1
        if count == largest_count:
          final_list.append(list_all_actors[index])
      else:
        count = 0
    
    if largest_count == 0:
      for index in range(num_elements_list_all_actors):
        final_list.append(list_all_actors[index])
    

    return (final_list)
    



def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]
                                 ) -> list[NetflixShow]:
    """ returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    If terms is empty, all elements in show_data will be included in the returned list.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
     ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
      'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
      'Anupam Kher', 'Madhavan'],  \
     (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
     (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, []) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
       'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
       'Anupam Kher', 'Madhavan'],  \
      (2018, 8, 2)),\
     ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
      (2017, 12, 12)),\
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]
    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], 
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], 
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
        'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
        'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
       (2017, 12, 12)), \
      ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], \
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12)), \
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]
    """
    # TODO: complete this function according to the documentation
    new_list = []
    final_list = []
    terms_list_undercase = []
    num_elements_terms = len(terms)
    for index in range(num_elements_terms):
      terms_list_undercase.append(terms[index].lower())
    
    
    if not terms and not show_data:
      return final_list
    elif not terms and show_data:
      return show_data
    elif not terms:
      final_list = show_data
    else:
      num_elements = len(show_data)
      for index in range(num_elements):
        list_of_words_in_title = show_data[index][TITLE].split(' ')
        num_elements_in_list_of_words_in_title = len(list_of_words_in_title)
        for subindex in range(num_elements_in_list_of_words_in_title):
          len_terms_list_undeercase = len(terms_list_undercase)
          for subsubindex in range(len_terms_list_undeercase):
            if terms_list_undercase[subsubindex].lower() in list_of_words_in_title[subindex].lower():
              new_list.append(show_data[index])
      
      num_elements_new_list = len(new_list)
      if not new_list:
        return final_list
      else:
        final_list.append(new_list[0])       
        for index in range(1,num_elements_new_list):
          if new_list[index] != new_list[index-1]:
            final_list.append(new_list[index])
      return (final_list)






def query(show_data: list[NetflixShow]) -> list[str]:
    """
    Returns a sorted list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    """
    # TODO: complete this function according to the documentation
    list_actors_in_most_shows = get_actors_in_most_shows(show_data)
    new_list = []
    final_list = []
    num_elements = len(show_data)
    num_elements_in_list_actors_in_most_shows = len(list_actors_in_most_shows)
    for index in range(num_elements):
      for subindex in range(num_elements_in_list_actors_in_most_shows):
        if list_actors_in_most_shows[subindex] in show_data[index][CAST]:
          new_list.append(show_data[index][TITLE])
    new_list.sort()
    len_new_list = len(new_list)

    for index in range(len_new_list):
      if index == 0:
        final_list.append(new_list[index])
      elif new_list[index] != new_list[index-1]:
        final_list.append(new_list[index])
    return (final_list)
    
