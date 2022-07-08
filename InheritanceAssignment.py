
    #parent class 
class vehicle:
    #defines attributes of class to inherite to child classes
    engine = ""
    physical_form = ""
    number_of_doors = ""
    speed = ""
    #child class inherites the attributes for "vehicle" parent class
class Airplane(vehicle):
    #attributes that only apply to "Airplane" child class
    number_of_wings: ""
    number_of_passangers: ""
    #child class inherites the attributes for "vehicle" parent class
class Helocopter(vehicle):
    #attributes that only apply to "Helocopter" child class
    number_of_propellers: ""
    number_of_engines: ""
