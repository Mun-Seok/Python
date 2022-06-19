MILES=0.621371
POUND=0.00220462

def kilometer_to_miles(killometer):
    return killometer*MILES

def gram_to_pounds(gram):
    return gram*POUND

miles=kilometer_to_miles(160)
print(miles)
pounds=gram_to_pounds(1000)
print(pounds)