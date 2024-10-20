FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)



def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return ((celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
         temp = float(input(f"enter the temperature you want to calculate: "))
         unit = input("is the unit of conversion? type Fahrenheit or Celsius? (F/C): ").strip().upper()

         if unit == 'F' :
            converted_output = convert_to_celsius(temp)
            print(f"{temp}°F in fahrenheit is {converted_output}°C")
         else : unit == 'C' 
         converted_output = convert_to_celsius(temp)
         print(f"{temp}°C in celsius is {converted_output}°F")
         
    except ValueError :
        print("invalid value, please try again" ) 

if __name__== "__main__":
    main()