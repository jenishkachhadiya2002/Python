from datetime import date

def calculateAge (Birthdate):
    
    today=date.today()
    Age=today.year-Birthdate.year-((today.month,today.day)<(Birthdate.month,Birthdate.day))
    
    return Age

print(calculateAge(date(2002,8,21)),"year")