
class rocket:
    

    types = 'space rockets'
    


    def __init__(self, name, age):
        self.name = name
        self.age = age



rocket1 = rocket("Saturn 5", 1967)
rocket2 = rocket("Ariane 5", 1996)

#Access:
print("{} first launch was in {} and {} first launch was in {}.".format(
        rocket1.name,rocket1.age,rocket2.name,rocket2.age))

# Is it a rocket:
if rocket1.types == 'space rockets':
    print("{0} was launched in {1}!".format(rocket1.name,rocket1.age))
