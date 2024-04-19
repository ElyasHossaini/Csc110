import doctest


class Date:
    """ Date: represents a date in the Gregorian calendar used worldwide.
    Precondition, month, day, year must make a valid calendar date.
    """   

    def __init__(self, month: int, day: int, year: int) -> None:
        """ initializes attributes of Date instance
        >>> dt1 = Date(12, 19, 2020)
        >>> dt2 = Date(1, 9, 2010)
        """
        self.__month  = month
        self.__day    = day
        self.__year   = year


    def get_month(self) -> int:
        """ returns month of self Date instance
        >>> dt1 = Date(12, 19, 2020)
        >>> dt2 = Date(1, 9, 2010)
        >>> dt1.get_month()
        12
        >>> dt2.get_month()
        1
        """
        return self.__month

    def get_day(self) -> int:
        """ returns day of self Date instance
        >>> dt1 = Date(12, 19, 2020)
        >>> dt2 = Date(1, 9, 2010)
        >>> dt1.get_day()
        19
        >>> dt2.get_day()
        9
        """        
        return self.__day
 
    def get_year(self) -> int:
        """ returns year of self Date instance
        >>> dt1 = Date(12, 19, 2020)
        >>> dt2 = Date(1, 9, 2010)
        >>> dt1.get_year()
        2020
        >>> dt2.get_year()
        2010
        """          
        return self.__year
    
    def __str__(self) -> str:
        """ returns a readable string with month, day, year of Date
        >>> dt1 = Date(12, 19, 2020)
        >>> dt2 = Date(1, 9, 2010)
        >>> str(dt1)
        '12-19-2020'
        >>> str(dt2)
        '1-9-2010'
        """
        return f'{self.__month}-{self.__day}-{self.__year}'
    
    def __repr__(self) -> str:
        """ returns a string representation of self Date
        >>> dt1 = Date(12, 19, 2020)
        >>> dt2 = Date(1, 9, 2010)
        >>> repr(dt1)
        'Date(12, 19, 2020)'
        >>> repr(dt2)
        'Date(1, 9, 2010)'
        """
        return f'Date({self.__month}, {self.__day}, {self.__year})'

    def __eq__(self, other: 'Date') -> bool:
        """ returns True if self Date has same month, day, year as 
        other Date, otherwise False
        >>> dt12192020a = Date(12, 19, 2020)
        >>> dt12192020b = Date(12, 19, 2020)
        >>> dt12192021  = Date(12, 19, 2021)
        >>> dt12182020  = Date(12, 18, 2020)
        >>> dt11192020  = Date(11, 19, 2020)
        
        >>> dt12192020a == dt12192020a
        True
        >>> dt12192020a == dt12192020b
        True
        >>> dt12192020a == dt12192021
        False
        >>> dt12192020a == dt12182020
        False
        >>> dt12192020a == dt11192020
        False
        """
        return (self.__month == other.__month 
                and self.__day == other.__day 
                and self.__year == other.__year)
    
    

    
