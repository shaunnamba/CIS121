class Dog:
    def __init__(self,name,size,breed="unknown"):
        self.name=name
        self.breed=breed
        self.size=size
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_breed(self):
        return self.breed
    def set_breed(self,breed):
        self.breed=breed
    def get_size(self):
        return self.size
    def set_size(self,size):
        self.size=size
    def speak(self):
        if self.size==1:
            print("Yip")
        elif self.size==2:
            print("Bark")
        elif self.size==3:
            print("Bow wow")
       

class DogPark:
    def __init__(self,name):
        self.name=name
        self.dogs=[]
    def add_dog(self,dog):
        self.dogs.append(dog)
    def show_dogs(self):
        for dog in self.dogs:
            print(dog.get_name())

    def change_dog_name(self,old_name,new_name):
        for dog in self.dogs:
            if dog.get_name() == old_name:
                dog.set_name(new_name)
    
    def find_dog(self,dog_name):
        for dog in self.dogs:
            if dog.get_name()==dog_name:
                dog.speak()
    
    def call_dog(self,dog_name):
        for dog in self.dogs:
            if dog.get_name()==dog_name:
                self.dogs.remove(dog)
       
        
park1=DogPark('Bark Zone')

park1.add_dog(Dog('Spoot',2,'lab'))
park1.add_dog(Dog('Rover',3,'Mastiff'))
park1.add_dog(Dog('Fluffy',1))

#park1.show_dogs()
park1.change_dog_name("Spoot","Spot")
#park1.show_dogs()
#park1.find_dog("Fluffy")
park1.show_dogs()
park1.call_dog("Fluffy")
park1.show_dogs()
    