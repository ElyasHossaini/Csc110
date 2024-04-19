import doctest
from race_time import RaceTime
from race_result import RaceResult

# represents a racer as (name, country)
# where name and country != ''
RacerNameCountry = tuple[str, str]

# represents a time as (miliseconds, seconds, minutes)
Time = tuple[int,int,int]

# access Time tuple
MILISECONDS = 0
SECONDS = 1
MINUTES = 2

# columns of values in input file row and positions in RacerNameCountry
NAME = 0
COUNTRY = 1
TIME_MS = 2

def time_ms_to_mins(time: int) -> Time:
    '''
    takes a time in ms and converts it to mins secs and ms as a tuple.
    '''
    final_list_to_tuple = []
    seconds = (time//1000)%60
    minutes = (time//(1000*60))%60
    miliseconds = time - (minutes * 60 * 1000) - (seconds * 1000)
    final_list_to_tuple.append(miliseconds)
    final_list_to_tuple.append(seconds)
    final_list_to_tuple.append(minutes)
    final_list_to_tuple  = tuple(final_list_to_tuple)
    return (final_list_to_tuple)


def read_file(filename: str) -> list[RaceResult]:
    """ returns a list of RaceResults populated with data from filename
    Precondition: the file exists, is not empty, has the following
      information on each row separated by commas:
      racer's name, racer's country, race time in milliseconds>=0
      and contains a header row with the column titles.
      The header row is ignored.

    >>> read_file('0lines_data.csv')
    []
    >>> read_file('9lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Evan Jager', 'United States', RaceTime(450, 0, 8)), \
     RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7)), \
     RaceResult('Saif Saaeed Shaheen', 'Qatar', RaceTime(630, 53, 7)), \
     RaceResult('Wander Moura', 'Brazil', RaceTime(410, 14, 8)), \
     RaceResult('Mahiedine Mekhissi-Benabbad', 'France', RaceTime(90, 0, 8)), \
     RaceResult('Peter Renner', 'New Zealand', RaceTime(50, 14, 8))]
    """
    # TODO: complete this function
    final_list = []
    file_handle = open(filename, 'r', encoding='utf8')
    line = file_handle.readline()
    line = file_handle.readline()
    while line != '':
        mini_list = line.split(',')
        time = time_ms_to_mins(int(mini_list[TIME_MS]))
        final_list.append(RaceResult(mini_list[NAME], mini_list[COUNTRY], RaceTime(time[MILISECONDS], time[SECONDS], time[MINUTES])))
        line = file_handle.readline()
    file_handle.close()
    return final_list

def find_athlete(loresults: list[RaceResult], name: str) -> int:
    """ returns the position of RaceResult with given athlete name in loresults
    Returns -1 if name not found
    Returns the position of the first if there >1 RaceResult with given name
    Precondition: case sensitive (ie. 'Brad' != 'brad')

    >>> find_athlete([], 'Brimin Kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))],\
        'brimin kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Brimin Kipruto')
    1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Peter Renner')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Usain Bolt', 'Canada', RaceTime(1, 2, 2019))], \
        'Usain Bolt')
    0
    """
    # TODO: complete this function
    num_elements = len(loresults)
    count = 0
    for index in range(num_elements):
        if loresults[index].get_name() != name:
            count += 1
        else:
            break
    if num_elements == count:  
        return -1
    else:
        return count
        

def get_all_from_country(loresults: list[RaceResult], country: str
                         ) -> list[RaceResult]:
    """ returns a list of all results of the given country
    Precondition: case sensitive (ie. 'Canada' != 'canada')

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 12)), \
     RaceResult('Perrier', 'France', RaceTime(1, 23, 18)), \
     RaceResult('Perrieruels', 'Canada', RaceTime(3, 29, 0)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country([], 'Jamaica')
    []

    >>> get_all_from_country(results, 'jamaica')
    []

    >>> get_all_from_country(results, 'Jamaica') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country(results, 'Japan')
    []
    """
    # TODO: complete this function
    final_list = []
    num_elements = len(loresults)
    for index in range(num_elements):
        if loresults[index].get_country() == country:
            final_list.append(loresults[index])
    return final_list


def get_fastest_time(loresults: list[RaceResult]) -> RaceTime:
    """ returns the fastest RaceTime of all finish_times of 
    RaceResult instances in loresults
    Precondition: loresults is not empty

    >>> one_result = [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 9))]
    >>> results = \
    [RaceResult('Allen', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 16, 17)), \
     RaceResult('Barnes', 'Canada', RaceTime(3, 43, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 29, 9)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 48, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 17))]

    >>> get_fastest_time(one_result)
    RaceTime(12, 31, 9)
    >>> get_fastest_time(results)
    RaceTime(3, 29, 9)
    """
    # TODO: complete this function
    fastest = RaceTime(9999, 9999, 9999)
    for index in loresults:
        if index.get_finish_time().is_faster(fastest):
            fastest = index.get_finish_time()
    return (fastest)
    
    
    
    
        
def get_with_fastest_time(loresults: list[RaceResult]
                          ) -> list[RacerNameCountry]:
    """ returns a list tuples of fastest RaceResults in loresults

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 6)), \
     RaceResult('Barnes', 'Canada', RaceTime(1, 23, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 10, 7)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 15, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 6))]
     
    >>> get_with_fastest_time([])
    []
    >>> get_with_fastest_time(results)
    [('Zhou', 'China'), ('Davis', 'Jamaica')]
    """
    # TODO: complete this function
    final_list = []
    fastest_time = get_fastest_time(loresults)
    for index in loresults:
        if index.get_finish_time() == fastest_time:
            mini_list = []
            mini_list.append(index.get_name())
            mini_list.append(index.get_country())
            mini_list_to_tuple = tuple(mini_list)
            final_list.append(mini_list_to_tuple)
    return (final_list)


