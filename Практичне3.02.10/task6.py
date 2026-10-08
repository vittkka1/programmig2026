def get_daily_discont():
    number=random.randint(1,100)
    if 1<=number<=100:
        return "Знижка 50%"
    elif 11<=number<=30:
        return "Знижка 20%"
    else:
        return "Знижка 5%"