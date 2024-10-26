class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f"i am  a cat my name is {self.name}.i am {self.age} years old")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f"i am  a dog my name is {self.name}.i am {self.age} years old")
cat1=cat("simba", 6)
dog1=dog("tommy", 7)
for animal in(cat1,dog1):
    animal.intro()