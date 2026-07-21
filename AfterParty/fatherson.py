father_age = int(input("Enter father's age: "))
son_age = int(input("Enter son's age: "))

if father_age > son_age:

    age_ratio = int(father_age / son_age) 

father_age_years_ago = father_age - son_age
print(f"The father was that age {father_age_years_ago} years ago.")

