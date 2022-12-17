#HW14-1, 12/10/2022
#Working on class.
#**************************************
class cat:
    def __init__(self,name,age,breed) :
        self.name= name
        self.age=age
        self.breed=breed
    #**********************************
    def walking(self):
        print( self.name+ " is walking.")
    #**********************************
    def meow(self):
        print( self.name+ " is meowing.")
    #**********************************
    def eating(self):
        print( self.name+ " is eating.")
    #**********************************
    def __str__(self) :
        return "Name: "+self.name+ ", Age: "+ str(self.age)+ ", Breed: "+self.breed
    #**********************************
#**************************************
cat1=cat("Pisho",2,"Persian")
print(cat1)
cat1.eating()
cat1.walking()
cat1.meow()