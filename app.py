from Person.Person import Person
from Admin import Admin
 
person = Person("Clark", 123456789)
admin = Admin("Marc", 987654321) 

def main():
    person.display_info()
    print(admin.__dict__)   

if __name__ == "__main__":
    main()