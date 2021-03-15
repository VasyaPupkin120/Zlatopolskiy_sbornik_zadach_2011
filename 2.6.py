n = int(input())

minuts = 60
hours = minuts * 60

print('full hours have passed since the beginning of the day: ', n // hours)
print('full minutes have passed since the beginning of the next hour: ', 
        (n - ((n // hours) * hours)) // minuts)
print('full seconds have passed since the beginning of the next minutes',
        (n % hours) % minuts)
