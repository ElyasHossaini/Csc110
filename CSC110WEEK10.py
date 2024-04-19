#intro to dictionaries
#this is list
l = [1,2,3,4]
#access list with index
x = l[0]
print(x)

#dictionary is refered to a map. You map a key to a specific value
#key is on left {key:}
names_to_ages = { 'Chris':19 , 'joe':22 , 'julia':27 ,}
print(names_to_ages)
num_elements = len(names_to_ages)
#no index, you give key
chris_age = names_to_ages['Chris']

#this prints all keys
for name in names_to_ages:
    print(name)

#this prints all ages/ the key values
for name in names_to_ages:
    print(names_to_ages[name])
    
#dictionaries are mutible/ u can change items

#this is how to add to dictionary. name key and give value
names_to_ages['Tian'] = 42
print(names_to_ages)
#this chnages chris value
names_to_ages['Chris'] = 100
print(names_to_ages)
#you can do things to the values of keys
names_to_ages['Chris'] = names_to_ages['Chris'] + 5
print(names_to_ages)

#can have multiple keys with same value
names_to_ages['Joey'] = 27
print(names_to_ages)

#this is how to delete key
del names_to_ages['Joey']
print(names_to_ages)

#no more error if delete something that isnt in dictionary
if 'Abe' in names_to_ages:
    del names_to_ages['Abe']
    
    
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES
#KEYS ARE IMPUTABLE SO THEY CANT BE LISTS BUT THEY CAN BE TUPLES