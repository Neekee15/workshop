cars=100
space_in_a_car=4.0
drivers=30
passangers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passanger_per_car=passangers/cars_driven

print("There are "+ str(cars)+" " + "cars available" , sep=" ")
print("There are ", cars , "cars available", sep="-")
print("There are %d cars available" %cars)
f="There are %d %s cars available" %(cars,"cars")
print(f)
value=(cars,"cars")
f="There are %d %s cars available" %value
print(f)


'''print(range(5))
def divide(number,divideby):
    print(divide(divideby=10,number=100))'''

def sum(*numbers):
    sum = 0
    i=0
    for i in numbers :
        sum += i
    return sum
    
print (sum(1))
print (sum(1,3))
print (sum(1,3,5))


def sum(*numbers):
    sum=1
    for number in numbers:
        sum*= number
    return sum

print(sum(1))
print(sum(2,4))

    


    
    




