1. Classes and Objects
   1. Classes in Python
     * A class is the blueprint from which specific objects are created.
     
| Class Variable | Instance Variable | Data Member |
| ----- | ----- | ----- |
| A variable that is shared by all instances of a class. | Instance variable unique to each instance | A class variable or instance variable that holds data associated with a class and its objects. |

#Code: /
class car():
    pass

honda = car()
tata = car()

honda.modelname = 'City'
honda.yearm = 2017
honda.price = 100000

tata.modelname = 'Bolt'
tata.yearm = 2016
tata.price = 600000

print(honda.price)
