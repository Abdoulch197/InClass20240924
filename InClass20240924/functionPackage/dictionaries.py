# dictionaries.py

from os import remove


def demo():
    """
    Demonstrate basic dictionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    
    # Iterate over the dictionary by key
    for key in myDictionary.keys():
        print(key)
    
    # Iterate by key/value
    for item in myDictionary.items():
        print(item)
        
    # Iterate by value
    for value in myDictionary.values():
        print(value)
        
    # Add a key/value pair to the dictionary
    myDictionary["Michigan State"] = "Spartans"  
    print(len(myDictionary))
    
    # Cause an exception. add the try/ except logci to gracefully handle this
    try:
      print(myDictionary["Ohio State"])
    except:
      # We end up here of the exception is thrown in the block
      print("Ohio State is an invalid key")
      
    # Remove Xavier by key and print the entire dictionary
    myDictionary.pop("Xavier")
    print(myDictionary)
    
    # Create another dictionary called newTeams
    # Add several key/value pairs
    # Combine that withe the myDictionary and print the results
    
    newTeams = {"Cinci":"Bengals" , "Cleveland":"Browns" , "Baltimore":"Ravens", "Dallas":"Cowboys"}
    myDictionary.update(newTeams)
    print(myDictionary)
      