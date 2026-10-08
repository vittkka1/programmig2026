import datetime
def is_adult(birth_years):
    current_year=datetime.datetime.now().year
    age=current_year-birth_years
    return age>=18

