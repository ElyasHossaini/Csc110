import doctest
from date import Date

class Pet:
    """ Pet: represents a domesticated pet with name, species and birthdate """

    def __init__(self, name: str, species: str, birthdate: Date) -> None:
        """ initializes attributes of Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> cat = Pet('Red', 'Cat', Date(1, 2, 2019))
        """
        self.__name      = name
        self.__species   = species
        self.__birthdate = birthdate

    def get_name(self) -> str:
        """ returns name of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> cat = Pet('Red', 'Cat', Date(1, 2, 2019))
        >>> dog.get_name()
        'Rover'
        >>> cat.get_name()
        'Red'
        """
        return self.__name

    def get_species(self) -> str:
        """ returns species of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> cat = Pet('Red', 'Cat', Date(1, 2, 2019))
        >>> dog.get_species()
        'Dog'
        >>> cat.get_species()
        'Cat'
        """
        return self.__species
    
    def get_birthdate(self) -> Date:
        """ returns date of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> cat = Pet('Red', 'Cat', Date(1, 2, 2019))
        >>> dog.get_birthdate()
        Date(12, 19, 2020)
        >>> cat.get_birthdate()
        Date(1, 2, 2019)
        """
        return self.__birthdate
    
    def __str__(self) -> str:
        """ returns a readable string with name, species, birthdate of Pet
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> cat = Pet('Red', 'Cat', Date(1, 2, 2019))
        >>> str(dog)
        'Rover is a Dog. Born: 12-19-2020'
        >>> str(cat)
        'Red is a Cat. Born: 1-2-2019'
        """
        return f'{self.__name} is a {self.__species}. Born: {self.__birthdate}'
    
    def __repr__(self) -> str:
        """ returns a string representation of self Pet
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> cat = Pet('Red', 'Cat', Date(1, 2, 2019))
        >>> repr(dog)
        "Pet('Rover', 'Dog', Date(12, 19, 2020))"
        >>> repr(cat)
        "Pet('Red', 'Cat', Date(1, 2, 2019))"
        """
        return (f"Pet({repr(self.__name)}, {repr(self.__species)}, "
                + f"{repr(self.__birthdate)})")


