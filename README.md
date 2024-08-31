# Car-CarSeller
Car sorting project

The Car class creates a Car object based on the given row which then creates a "features" list of strings by comma separating the given row of the CSV file.
This list is then used to assign the variables utilizing the index of the associated feature since the ones we want will always be in the same place.

The paint, repair, and reupholster methods are all pretty simple they just replace the old string with the new one. For the drive and modify price functions they both involve turning the old value into a float in order to add or subtract with it, before reassigning the sum/difference to the variable.

The seller class is similar to the Car class in that it uses the given row to assign the name and rating variables based on their constant index in each row.

The buy and sell methods simply append or remove a car object from the inventory list, while the printInv method iterates through the list and prints each car in the Sellers inventory.

I also added at the bottom a for loop that creates lists of car and seller objects for a specified part of the CSV file to turn all of that data into the prespecified classes

I'm still unsure why but I could not get the Seller list to correctly make only the first instance of a specific seller name add a car to its inventory and then remove the duplicate Seller object from the list. The best code I could think of is block commented-out with a simple way to add each line's car to a new Seller object's inventory but it cannot remove duplicate sellers or add subsequent cars from them to a single Seller object.
