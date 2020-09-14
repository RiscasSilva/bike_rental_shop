import datetime

class Shop:

    def __init__ (self, stock = 0):
        self.stock = stock

    def display_stock():

        print("We currently have " + self.stock + " available")


    def rent_H (self, n_bikes):

        hour = datetime.datetime.now()
        print("You have rented " + n_bikes + "bikes. You will be charged 5€ per hour. Starting rental hour: " + str(hour.hour))
        self.stock -= int(n_bikes)
        return hour


    def rent_D (self, n_bikes):

        hour = datetime.datetime.now()
        print("You have rented " + n_bikes + "bikes. You will be charged 20€ per day. Starting rental hour: " + str(hour.hour))
        self.stock -= int(n_bikes)
        return hour


    def rent_W (self, n_bikes):

        hour = datetime.datetime.now()
        print("You have rented " + n_bikes + "bikes. You will be charged 60€ per week. Starting rental hour: " + str(hour.hour))
        self.stock -= int(n_bikes)
        return hour


    def return_bikes(self, rental_time, rental_basis, n_bikes):

        #Replenishes inventory        
        bill = 0
        self.stock+=int(n_bikes)

        #bill calculation
        return_time = datetime.datetime.now()
        rental_period = return_time - datetime.datetime.strptime(rental_time, '%Y-%m-%d %H:%M:%S.%f')
        if int(rental_basis) == 1:   # hourly rental
            bill = round(rental_period.seconds/3600) * 5 * int(n_bikes) + 5
        elif int(rental_basis) == 2:   # daily rental
            bill = round(rental_period.days) * 20 * int(n_bikes) + 7
        elif int(rental_basis) == 3:   # weekly rental
            bill = round(rental_period.days/7) * 60 * int(n_bikes) + 10

        print("That would be: " + str(bill) + "€")



class Costumer:

    def __init__ (self, rented_bikes=0, rental_time=0, rental_basis=0, bill=0):
        self.rented_bikes = rented_bikes
        self.rental_time = rental_time
        self.rental_basis = rental_basis
        self.bill = bill

    def rent_bikes(self, stock):
        self.rented_bikes = 0
        while int(self.rented_bikes) <= 0 or int(self.rented_bikes) > stock:
            self.rented_bikes = input("How many bikes do you want to rent? ")

            if int(self.rented_bikes) <= 0:
                print("Please pick a number greater than 0.")

            elif int(self.rented_bikes) > stock:
                print("We do not have that many bikes.")

        self.rental_basis = input("""   Request options:

                1.  Hourly basis
                2.  Daily basis
                3.  Weekly basis

            Please select your option: """)



class Database:

    def __init__(self):
        self.id = []
        self.name = []
        self.rental_basis = []
        self.rental_time = []
        self.rented_bikes = []

    def check_database(self, ID):
        if ID in self.id:
            return 0
        else: 
            return 1

    def add(self, ID, costumer_name, rental_basis, rental_time, rented_bikes):
        if ID in self.id:
            return 0

        else: 
            self.id += ID
            self.name += [costumer_name]
            self.rental_basis += [rental_basis]
            self.rental_time += [str(rental_time)]
            self.rented_bikes += [rented_bikes]
            return 1

    def remove(self, ID):
        if ID not in self.id:
            return 0
        
        else:
            self.name.remove(self.name[self.id.index(ID)])
            self.rental_basis.remove(self.rental_basis[self.id.index(ID)])
            self.rental_time.remove(self.rental_time[self.id.index(ID)])
            self.rented_bikes.remove(self.rented_bikes[self.id.index(ID)])
            self.id.remove(ID)
            return 1

    