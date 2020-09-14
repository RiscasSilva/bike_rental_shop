from bike_rental import Shop, Costumer, Database

shop = Shop(100)
database = Database()
db_file = open("/home/cliente/Desktop/Python/bike_rental_shop/rental_database.txt", "w")

while True:

    costumer = Costumer()

    action = input("Hello! Do you want to rent or to return bikes? ")


    if action == "rent":

        costumer.rent_bikes(shop.stock)

        if int(costumer.rental_basis) == 1:
            costumer.rental_time = shop.rent_H(costumer.rented_bikes)
            costumer.bill = 0

        elif int(costumer.rental_basis) == 2:
            costumer.rental_time = shop.rent_D(costumer.rented_bikes)
            costumer.bill = 0

        elif int(costumer.rental_basis) == 3:
            costumer.rental_time = shop.rent_W(costumer.rented_bikes)
            costumer.bill = 0

        rental_id = input("Please write a three digits number. This will be your rental ID: ")
        name = input("Please write your first and last name: ")

        database.add(rental_id, name, costumer.rental_basis, costumer.rental_time, costumer.rented_bikes)
        print(shop.stock)

        del costumer


    if action == "return":

        rental_id = input("What is your rental ID? ")

        while rental_id not in database.id:
            rental_id = input("That ID is not registered in our database. Try again: ")

        shop.return_bikes(database.rental_time[database.id.index(rental_id)], database.rental_basis[database.id.index(rental_id)], database.rented_bikes[database.id.index(rental_id)])
        print("We now have " + str(database.rented_bikes[database.id.index(rental_id)]) + " more bikes to rent. Total number of available bikes: " + str(shop.stock))
        
  
        database.remove(rental_id)
        print("Return value:" + str(database.remove(rental_id)))
    
        del costumer