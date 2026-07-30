def check_temperature(temperature_value, current_unit, threshold_limit):
    
    if current_unit == "Fahrenheit":
        converted = (temperature_value - 32) * 5 / 9
    else:
        converted = temperature_value 

    if converted < threshold_limit:
        return "Cold advisory"
    else:
        return "Heat alert"


temperature_value = float(input("Enter the temperature: "))
current_unit = input("Enter the current unit (Celsius/Fahrenheit): ")
threshold_limit = 30.0

result = check_temperature(temperature_value, current_unit, threshold_limit)
print("The result is:", result)
