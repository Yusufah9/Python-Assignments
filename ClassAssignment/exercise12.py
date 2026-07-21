# The Initial investment values invested
p = 1000      
r = 0.07     
years = [10, 20, 30]

for n in years:
    a = p * (1 + r) ** n
    print(f"Amount after {n} years: ${a:.2f}")

