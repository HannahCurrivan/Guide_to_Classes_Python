
class rocket:
    

    types = 'space rockets'
    
    
    def _init_(self, name, year):
        self.name = name
        self.year = year 



rocket1 = rocket("Saturn_5", 1967)
rocket2 = rocket("Ariane_5", 1996)


print("{} first launch was in {} and {} first launch was in {}.".format(
        rocket1.name,rocket1.year,rocket2.name,rocket2.year))


if rocket1.types == 'space rockets':
    print("{0} is a {1}!".format(rocket1.name,rocket1.year))
