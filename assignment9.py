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


# column numbers of data within input csv file
INPUT_SID        = 0
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10


# values to access each dictionary
ID_AND_DATE = 0
ID_AND_ACTORS = 1
CATEGORY_AND_ID = 2
ID_AND_TITLE = 3

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
  
  
  
  
  
def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]],
                                 dict[str, str]):
    """
    Populates and returns a tuple with the following 4 dictionaries
    with data from valid filename.
    
    4 dictionaries returned as a tuple:
    - dict[show id: date added to Netflix]
    - dict[show id: list of unique actor names]
    - dict[category: list of unique show ids]
    - dict[show id: show title]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show id: list of unique actor names]

    The list of actors for each key in
      dict[show id: list of unique actor names]
      should be in the order they appear on the line in the input file.
      If the line has duplicated actor names, the unique actor name 
      is added once for the first time it occurs in the line.
    
    Precondition: file is csv with data in expected columns 
        and contains a header row with column titles
        Show ids within the file are unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {}, {})
    
    >>> read_file('11lines_data.csv')  # doctest: +NORMALIZE_WHITESPACE
    ({'81217749': (2019, 11, 15),
      '70303496': (2018, 9, 6),
      '70142798': (2018, 9, 5),
      '80999063': (2018, 10, 5),
      '80190843': (2018, 9, 7),
      '80119349': (2017, 9, 29),
      '70062814': (2018, 9, 5),
      '80182115': (2017, 9, 29),
      '80187722': (2018, 10, 12),
      '70213237': (2018, 10, 2),
      '70121522': (2019, 8, 1)},
     {'81217749': ['Naseeruddin Shah'],
      '70303496': ['Aamir Khan',
                   'Anuskha Sharma',
                   'Sanjay Dutt',
                   'Saurabh Shukla',
                   'Parikshat Sahni',
                   'Sushant Singh Rajput',
                   'Boman Irani',
                   'Rukhsar'],
      '70142798': ['Jirayu La-ongmanee',
                   'Charlie Trairat',
                   'Worrawech Danuwong',
                   'Marsha Wattanapanich',
                   'Nicole Theriault',
                   'Chumphorn Thepphithak',
                   'Gacha Plienwithi',
                   'Suteerush Channukool',
                   'Peeratchai Roompol',
                   'Nattapong Chartpong'],
      '80999063': ['Elyse Maloway',
                   'Vincent Tong',
                   'Erin Matthews',
                   'Andrea Libman',
                   'Alessandro Juliani',
                   'Nicole Anthony',
                   'Diana Kaarina',
                   'Ian James Corlett',
                   'Britt McKillip',
                   'Kathleen Barr'],
      '70062814': ['Ananda Everingham',
                   'Natthaweeranuch Thongmee',
                   'Achita Sikamana',
                   'Unnop Chanpaibool',
                   'Titikarn Tongprasearth',
                   'Sivagorn Muttamara',
                   'Chachchaya Chalemphol',
                   'Kachormsak Naruepatr'],
      '80187722': ['Frank Grillo'],
      '70213237': ['Graham Chapman',
                   'Eric Idle',
                   'John Cleese',
                   'Michael Palin',
                   'Terry Gilliam',
                   'Terry Jones'],
      '70121522': ['Aamir Khan',
                   'Kareena Kapoor',
                   'Madhavan',
                   'Sharman Joshi',
                   'Omi Vaidya',
                   'Boman Irani',
                   'Mona Singh',
                   'Javed Jaffrey']},
     {'Documentaries': ['81217749', '80119349', '80182115'],
      'International Movies': ['81217749',
                               '70303496',
                               '70142798',
                               '80119349',
                               '70062814',
                               '70121522'],
      'Comedies': ['70303496', '70121522'],
      'Dramas': ['70303496', '70121522'],
      'Horror Movies': ['70142798', '70062814'],
      'Children & Family Movies': ['80999063'],
      'Docuseries': ['80190843', '80187722', '70213237'],
      'British TV Shows': ['70213237']},
     {'81217749': 'SunGanges',
      '70303496': 'PK',
      '70142798': 'Phobia 2',
      '80999063': 'Super Monsters Save Halloween',
      '80190843': 'First and Last',
      '80119349': 'Out of Thin Air',
      '70062814': 'Shutter',
      '80182115': 'Long Shot',
      '80187722': 'FIGHTWORLD',
      '70213237': "Monty Python's Almost the Truth",
      '70121522': '3 Idiots'})
    """
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    final_list_to_tuple = []
    dictionary_id_date = {}
    dictionary_id_actor = {}
    dictionary_category_id = {}
    dictionary_id_title = {}
    file_handle = open(f'{filename}', 'r', encoding='utf8')
    line = file_handle.readline()
    line = file_handle.readline()
    
    while line != '':
      list_of_line = line.split(',')
      
      dictionary_id_date[list_of_line[INPUT_SID]] = create_date(list_of_line[INPUT_DATE])
      
      if not list_of_line[INPUT_CAST]:
       x = 0 
      else:
          list_actors = list_of_line[INPUT_CAST].split(':')
          list_unique_actors = []
          num_elements_actors = len(list_actors)
          for index in range(num_elements_actors):
            if list_actors[index] not in list_unique_actors:
              list_unique_actors.append(list_actors[index])
          dictionary_id_actor[list_of_line[INPUT_SID]] = list_unique_actors
          
      list_of_categories = list_of_line[INPUT_CATEGORIES].split(':')
      num_elements = len(list_of_categories)
      for index in range(num_elements):
        if list_of_categories[index] not in dictionary_category_id:
          dictionary_category_id[list_of_categories[index]] = list((list_of_line[INPUT_SID],))
        else:
          dictionary_category_id[list_of_categories[index]].append(list_of_line[INPUT_SID])
          
      dictionary_id_title[list_of_line[INPUT_SID]] = list_of_line[INPUT_TITLE]
      
      line = file_handle.readline()
      
    file_handle.close()
    final_list_to_tuple.append(dictionary_id_date)
    final_list_to_tuple.append(dictionary_id_actor)
    final_list_to_tuple.append(dictionary_category_id)
    final_list_to_tuple.append(dictionary_id_title)
    final_list_to_tuple = tuple(final_list_to_tuple)
    
    return (final_list_to_tuple)
    
    
    

    
def get_id_from_category(filename: str, category: str) -> list[str]:
  '''
  returns a list of show ids of only those shows that are of the given category
  >>> get_id_from_category('11lines_data.csv', 'Comedies')
  ['70303496', '70121522']
  >>> get_id_from_category('11lines_data.csv', 'Horror Movies')
  ['70142798', '70062814']
  '''
  final_list = []
  show_dictionaries = read_file(filename)
  for index in show_dictionaries[CATEGORY_AND_ID]:
    if index == category:
      final_list = show_dictionaries[CATEGORY_AND_ID][category]
  
  return (final_list)
  

def get_id_from_date(filename: str, date: Date) -> list[str]:
  '''
  returns a list of show ids of only those shows that are before the given date
  >>> get_id_from_date('11lines_data.csv', [2020,11,12])
  ['81217749', '70303496', '70142798', '80999063', '80190843', '80119349', '70062814', '80182115', '80187722', '70213237', '70121522']
  '''
  final_list = []
  show_dictionaries = read_file(filename)
  for index in show_dictionaries[ID_AND_DATE]:
    if show_dictionaries[ID_AND_DATE][index][YEAR] < date[YEAR]:
      final_list.append(index)
    elif show_dictionaries[ID_AND_DATE][index][YEAR] == date[YEAR]:
      if show_dictionaries[ID_AND_DATE][index][MONTH] < date[MONTH]:
        final_list.append(index)
      elif show_dictionaries[ID_AND_DATE][index][MONTH] == date[MONTH]:
        if show_dictionaries[ID_AND_DATE][index][DAY] < date[DAY]:
          final_list.append(index)
          
  return (final_list)
  

def get_id_from_actors(filename: str, actors: list[str]) -> list[str]:
  '''
  returns a list of show ids of only those shows that have the given actor/actors
  
  >>> get_id_from_actors('11lines_data.csv', ['Aamir Khan','Nicole Theriault'])
  ['70121522', '70142798', '70303496']
  >>> get_id_from_actors('11lines_data.csv', [])
  ['81217749', '70303496', '70142798', '80999063', '80190843', '80119349', '70062814', '80182115', '80187722', '70213237', '70121522']
  '''
  final_list = []
  show_dictionaries = read_file(filename)
  if not actors:
    for index in show_dictionaries[ID_AND_DATE]:
      final_list.append(index)
    return (final_list)
    
  else:
    new_list = []
    
    len_actors = len(actors)
    for index in show_dictionaries[ID_AND_ACTORS]:
      for subindex in range(len_actors):
        if actors[subindex] in show_dictionaries[ID_AND_ACTORS][index]:
          new_list.append(index)
          
    new_list.sort()
    
    len_new_list = len(new_list)
    for index in range(len_new_list):
      if new_list[index] not in final_list:
        final_list.append(new_list[index])
    
    return (final_list)
    
    


def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[tuple[str, str]]:
    """
    returns a list of sorted tuples containing (show title, show id) pairs 
    of only those shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
      If no actors are specified (empty list), all actors in library are valid;
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    [('3 Idiots', '70121522'), ('PK', '70303496')]
        
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Sanjay Dutt'])
    [('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('3 Idiots', '70121522'), ('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('PK', '70303496'), ('Shutter', '70062814')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'not found', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'Aamir Khan', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either', 'Aamir Khan']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('PK', '70303496')]
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'),
     ('PK', '70303496'), ('Zed Plus', '81213884')]
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'), 
     ('Dangal', '80166185'), ('Dhobi Ghat (Mumbai Diaries)', '70144331'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'), 
     ('Lagaan', '60020906'), ('Madness in the Desert', '80229953'),
     ('PK', '70303496'), ('Raja Hindustani', '17457962'), 
     ('Rang De Basanti', '70047320'), ('Secret Superstar', '80245408'), 
     ('Shutter', '70062814'), ('Taare Zameen Par', '70087087'),
     ('Talaash', '70262614'), ('Zed Plus', '81213884')]
    """
    # TODO: complete this function according to the documentation
    list_all_id = []
    list_id_with_specifications = []
    final_list = []
    show_dictionaries = read_file(filename)
    
    list_all_id += get_id_from_category(filename, category)
    list_all_id += get_id_from_date(filename, date)
    list_all_id += get_id_from_actors(filename, actors)
    
    list_all_id.sort()
    len_list_all_id = len(list_all_id)
    count = 1
    for index in range(1,len_list_all_id):
      if list_all_id[index] == list_all_id[index-1]:
        count += 1
        if count >= 3:
          list_id_with_specifications.append(list_all_id[index])
      else:
        count = 1
    
    for index in show_dictionaries[ID_AND_TITLE]:
      len_list_id_with_specifications = len(list_id_with_specifications)
      for subindex in range(len_list_id_with_specifications):
        mini_list = []
        if list_id_with_specifications[subindex] == index:
          mini_list.append(show_dictionaries[ID_AND_TITLE][index])
          mini_list.append(index)
          mini_list = tuple(mini_list)
          final_list.append(mini_list)
          
    final_list.sort()
    return (final_list)



    
    