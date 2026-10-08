import math
def calculate_trip_cost(distance,fuel_consumption, fuel_price):
    fuel=(distance/100)*fuel_consumption
    total=fuel*fuel_price
    return math.ceil(total)
