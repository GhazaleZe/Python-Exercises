import datetime


class person:
    count = 0
    def __init__(self, year_of_birth, first_name, last_name):
        self.year_of_birth = year_of_birth
        self.first_name = first_name
        self.last_name = last_name
    def get_first_name_and_last_name(self):
        print("The first name is %s" % self.first_name)
        print("The last name is %s" % self.last_name)

    def get_age(self):
        today = datetime.date.today()
        year = today.year
        self.age = year - self.year_of_birth
        print ("The age is %d" % self.age)
        

Katty = person(1998, 'Katty', 'Pron')
Katty.get_first_name_and_last_name()
Katty.get_age()
