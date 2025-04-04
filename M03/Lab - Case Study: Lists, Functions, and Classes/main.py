from Automobile import Automobile

def prompt_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an number.")

def prompt_string(prompt: str) -> str:
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a string.")

def main():
    year = prompt_integer("What is the year of the car? ")
    make = prompt_string("What is the make of the car? (e.g. Toyota, Honda, etc.) ")
    model = prompt_string("What is the model of the car? (e.g. Camry, Accord, etc.) ")

    def prompt_doors() -> int:
        while True:
            doors = prompt_integer("How many doors does the car have? (2 or 4) ")
            if doors != 2 and doors != 4:
                print("Invalid number of doors")
                return
            return doors
        
    doors = prompt_doors()

    def prompt_roof_type() -> str:
        while True:
            roof = prompt_string("What is the type of roof of the car? (solid or sun roof) ")
            if roof != "solid" and roof != "sun roof":
                print("Invalid roof type. Try again.")
                continue
            return roof

    roof = prompt_roof_type()
    car = Automobile(year, make, model, doors, roof)

    print(f"Your vehicle is a\n{car}")

if __name__ == "__main__":
    main()