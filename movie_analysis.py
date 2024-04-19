'''
movie_analysis_starter.py
We have defined the Movie class and the query function within this file
to consolidate it as opposed to defining the class in Movie.py
Both approaches are acceptable.
'''
TITLE = 2
CAST = 4
YEAR = 7
LENGTH = 9

class Movie:
    """ Movie with (examples taken from first movie information in 3lines.csv):
    - title (title)
      example: 'Bollywood Calling'
    - length in minutes (length)
      example: 102
    - year of release (year)
      example: 2001
    - list of cast member names (cast)
      example: ['Om Puri', 'Pat Cusick', 'Navin Nischol', 'Perizaad Zorabian']
    """

    def __init__(self, title: str, length: int, year: int, cast: list[str]
                 ) -> None:
        """
        initializes an instance of Movie with title, length, year and cast
        NOTE: completed for you with examples omitted intentionally
        DO NOT CHANGE the field names
        """
        self.__title = title
        self.__length = length
        self.__year = year
        self.__cast = cast
      
    def get_title(self) -> str:
        return self.__title
      
    def get_lenght(self) -> int:
      return self.__length
    
    def get_year(self) -> int:
      return self.__year
    
    def get_cast(self) -> list[str]:
      return self.__cast

    def __repr__(self) -> str:
       return f'Movie({repr(self.__title)}, {repr(self.__length)}, {repr(self.__year)}, {repr(self.__cast)})'
    # define the methods you feel are necessary for this Class....


def query(filename: str) -> list[Movie]:
    """
    returns a list of Movie instances of only those movies in filename that
    have the largest casts of all Movie type show in filename
    Precondition: filename exists and is in expected csv format where,
    the first line is a header specifying the data in each column and
    each subsequent line of filename has expected comma separated values

    >>> query('0lines_data.csv')
    []
    >>> query('11lines_data.csv')
    [Movie('Phobia 2', 125, 2009, \
    ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', \
    'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', \
    'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', \
    'Nattapong Chartpong']), \
    Movie('Super Monsters Save Halloween', 25, 2018, \
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', \
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', \
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'])]
    >>> query('large_data.csv')
    [Movie('Arthur Christmas', 98, 2011, \
    ['James McAvoy', 'Hugh Laurie', 'Bill Nighy', 'Jim Broadbent', \
    'Imelda Staunton', 'Ashley Jensen', 'Ramona Marquez', 'Marc Wootton', \
    'Laura Linney', 'Eva Longoria', 'Michael Palin', 'Joan Cusack', \
    'Deborah Findlay', 'Rich Fulcher', 'Sarah Smith', 'Clint Dyer', 'Kerry Shale', \
    'Stewart Lee', 'Bronagh Gallagher', 'Kevin Cecil', 'Alistair McGowan', \
    'David Menkin', 'Kris Pearn', 'Ian Ashpitel', 'Rich Hall', 'Seeta Indrani', \
    'Jane Horrocks', 'Peter Baynham', 'Emma Kennedy', 'Dominic West', \
    'Jerry Lambert', 'Julia Davis', 'Robbie Coltrane', 'Iain McKee', \
    'Sanjeev Bhaskar', 'Andy Serkis', 'Tamsin Greig', 'Rhys Darby', \
    'Seamus Malone', 'Cody Cameron', 'David Schneider', 'Kevin Eldon', \
    'Danny John-Jules', 'Brian Cummings'])]
    """
# TODO - complete this function
    final_list = []
    list_title = []
    list_length = []
    list_year = []
    list_cast = []
    file_handle = open(filename, 'r', encoding='utf8')
    line = file_handle.readline()
    line = file_handle.readline()
    largest_cast_number = 0
    while line != '':
      list_line = line.split(',')
      list_title.append(list_line[TITLE])
      titlel = list_line[LENGTH].split(' ')
      list_length.append(int(titlel[0]))
      list_year.append(int(list_line[YEAR]))
      castl = list_line[CAST].split(':')
      list_cast.append(castl)
      line = file_handle.readline()
    file_handle.close()
    
    len_list_cast = len(list_cast)
    for index in range(len_list_cast):
      len_cast = len(list_cast[index])
      if len_cast > largest_cast_number:
        largest_cast_number = len_cast
        
    for index in range(len_list_cast):
      if len(list_cast[index]) == largest_cast_number:
        final_list.append(Movie(list_title[index], list_length[index], list_year[index], list_cast[index]))
      
    return final_list