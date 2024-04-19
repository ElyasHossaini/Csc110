import doctest

# input file column information:
NAME   = 0
RATING = 1
PRICE  = 2
TYPES  = 3

# represents a restaurant rating as (rating, name)
# where 0 <= rating <= 5
RestaurantRating = tuple[float, str]

def recommend(filename: str, price: str, food_types: list[str]
              ) -> list[RestaurantRating]:
    """
    return a list of RestaurantRating of only restaurants in filename 
    with given price category and that serve at least one food in food_types.
    The returned list should be in sorted order by rating then restaurant name.
    
    >>> recommend('empty.txt', '$$$', ['Canadian', 'Breakfast and Brunch'])
    []
    >>> recommend('restaurant_data.txt', '$$$', \
                  ['Canadian', 'Breakfast and Brunch'] \
                 )  # doctest: +NORMALIZE_WHITESPACE
    [(4.0, 'The Pacific Restaurant'), 
     (4.5, 'Blue Fox Cafe'),
     (4.5, 'Clarke&Co')]
    """
    name_to_rating, price_to_names, food_to_names = populate_dicts(filename)
    # TODO - finish this function
    
    
    
def populate_dicts(filename: str) -> (dict[str, float],
                                      dict[str, list[str]],
                                      dict[str, list[str]]):
    """ populates and returns 3 dictionaries based on data in file
    - dict[restaurant name, rating]
    - dict[price, list[restaurant names]]
    - dict[food type, list[restaurant names]]
    
    Precondition: filename exists and contains lines of restaurant data as:
    name, rating, price point, food types separated by commas

    >>> populate_dicts('empty.txt')
    ({}, {'$': [], '$$': [], '$$$': [], '$$$$': [], '$$$$$': []}, {})

    >>> populate_dicts('restaurant_data.txt') # doctest: +NORMALIZE_WHITESPACE
    ({'Clarke&Co': 4.5, 
      'Red Fish Blue Fish': 4.5, 
      'Blue Fox Cafe': 4.5, 
      'Jam Cafe': 4.5, 
      'Il Terrazzo Ristorante': 4.5, 
      'Il Covo Trattoria': 4.0,
      'Nautical Nellies': 4.0, 
      "Cora's": 4.0, 
      'The Pacific Restaurant': 4.0,
      'Kuma Noodles Japan': 4.0, 
      'The Tartan Toque': 3.5},
     {'$': ['Kuma Noodles Japan'], 
      '$$': ['Red Fish Blue Fish', 'Jam Cafe', 'Il Covo Trattoria', 
             'Nautical Nellies', "Cora's", 'The Tartan Toque'],
      '$$$': ['Clarke&Co', 'Blue Fox Cafe', 'Il Terrazzo Ristorante', 
              'The Pacific Restaurant'], 
      '$$$$': [], 
      '$$$$$': []},
     {'Canadian': ['Clarke&Co', 'Blue Fox Cafe', 
                   'The Pacific Restaurant', 'The Tartan Toque'],
      'Fish and Chips': ['Red Fish Blue Fish'],
      'Seafood': ['Red Fish Blue Fish', 'Nautical Nellies'],
      'Breakfast and Brunch': ['Blue Fox Cafe', 'Jam Cafe', "Cora's"],
      'Italian': ['Il Terrazzo Ristorante', 'Il Covo Trattoria'],
      'Steakhouses': ['Nautical Nellies'], 
      'Ramen': ['Kuma Noodles Japan']})
    """
    # TODO - complete this function
