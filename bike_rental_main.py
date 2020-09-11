from bike_rental import Shop, Costumer 

shop = Shop(100)
costumer = Costumer()

while True:

    action = input("Do you want to rent or to return bikes? ")

    if action == "rent":

        costumer.rent_bikes()

        if int(costumer.rental_basis) == 1:
            costumer.rental_time = shop.rent_H(costumer.rented_bikes)
            costumer.bill = 0

        elif int(costumer.rental_basis) == 2:
            costumer.rental_time = shop.rent_D(costumer.rented_bikes)
            costumer.bill = 0

        elif int(costumer.rental_basis) == 3:
            costumer.rental_time = shop.rent_W(costumer.rented_bikes)
            costumer.bill = 0

    if action == "return":

        shop.return_bikes(costumer.rental_time, costumer.rental_basis, costumer.rented_bikes)