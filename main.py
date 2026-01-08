import pickle
import os
def main():

    planet_gravity = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Moon": 0.165,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 0.93,
        "Uranus": 0.92,
        "Neptune": 1.12,
        "Pluto": 0.066,
    }

    filename = "anPlanetaryWeights.db"
    dict_planet_history = {}
    

    try:
        if os.path.getsize(filename) > 0:
            with open(filename, "rb") as file:
                dict_planet_history = pickle.load(file)
        else:
            print("History file is empty. Creating a new one.")
            dict_planet_history = {}

    except FileNotFoundError:
        print("History file not found. Creating a new one.")
        dict_planet_history = {}
    except pickle.UnpicklingError:
        print("Error: History file is corrupted. Creating a new one.")
        dict_planet_history = {}
    except EOFError:
        print("Error: History file is incomplete or empty. Creating a new one.")
        dict_planet_history = {}

    history_choice = input("Do you want to see the history? (Y/N): ").lower()
    if history_choice == "y":
        for name, weights in dict_planet_history.items():
            print(f"\n{name}'s Planetary Weights:")
            for planet, weight in weights.items():
                print(f"{planet}: {weight:10.2f}")

    while True:
        s_name = input("Enter a unique name (blank to exit): ").strip()
        if not s_name:
            break

        if s_name.lower() in (name.lower() for name in dict_planet_history):
            print("Name already exists. Please enter a unique name.")
            continue

        while True:
            try:
                f_earth_weight = float(input("Enter Earth weight: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        dict_person_weights = {}
        for planet, gravity in planet_gravity.items():
            f_planet_weight = f_earth_weight * gravity
            dict_person_weights[planet] = f_planet_weight
            print(f"{planet}: {f_planet_weight:10.2f}")

        dict_planet_history[s_name] = dict_person_weights
        print(f"\n{s_name}'s Solar System's Weights Calculated.")

    try:
        with open(filename, "wb") as file:
            pickle.dump(dict_planet_history, file)
    except Exception as e:
        print(f"Error saving history: {e}")

if __name__ == "__main__":
    main()
    
    