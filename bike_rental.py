import datetime

class Shop:

    def __init__ (self, stock = 0):
        self.stock = stock

    def display_stock():
        print("We currently have " + self.stock + " available")

    def rent_H (self, n_bikes):

        if int(n_bikes) <= 0:
            print("Please pick a number greater than 0.")
            return None

        elif int(n_bikes) > self.stock:
            print("We do not have that many bikes.")
            return None

        elif 0 < int(n_bikes) < self.stock:
            hour = datetime.datetime.now()
            print("You have rented " + n_bikes + "bikes. You will be charged 5€ per hour. Starting rental hour: " + str(hour.hour))
            self.stock -= int(n_bikes)
            return hour

    def rent_D (self, n_bikes):

        if int(n_bikes) <= 0:
            print("Please pick a number greater than 0.")
            return None

        elif int(n_bikes) > self.stock:
            print("We do not have that many bikes.")
            return None

        elif 0 < int(n_bikes) < self.stock:
            hour = datetime.datetime.now()
            print("You have rented " + n_bikes + "bikes. You will be charged 20€ per day. Starting rental hour: " + str(hour.hour))
            self.stock -= int(n_bikes)
            return hour

    def rent_W (self, n_bikes):

        if int(n_bikes) <= 0:
            print("Please pick a number greater than 0.")
            return None

        elif int(n_bikes) > self.stock:
            print("We do not have that many bikes.")
            return None

        elif 0 < int(n_bikes) < self.stock:
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
        rental_period = return_time - rental_time
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

    def rent_bikes(self):
        self.rented_bikes = 0
        while int(self.rented_bikes) <= 0:
            self.rented_bikes = input("How many bikes do you want to rent? ")

        self.rental_basis = input("""   Request options:

                1.  hourly basis
                2.  daily basis
                3.  weekly basis

            Please select your option: """)
        

