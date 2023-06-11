"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from operator import attrgetter
from place import Place
from placecollection import PlaceCollection
import csv
import random

FILENAME = "places.csv"

# Column names of the CSV file
COLUMNS = ["Name", "Country", "Priority", "Visited"]


def main():
    """Runs the Travel Tracker program and display menu with the list of places. """
    print("Travel Tracker 2.0 - by <Royce>")
    # Create a PlaceCollection object
    place_collection = PlaceCollection()
    # Load the places from places.csv file
    place_collection.load_places(FILENAME)
    print(f"{len(place_collection.places)} places loaded from places.csv")
    # Display menu and ask user to input until the user input is quit
    while True:
        print("Menu:")
        print("L - List places")
        print("R - Recommend random place")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("Q - Quit")

        # Execute corresponding function based on the user input
        user_input = input(">>> ").strip().upper()
        if user_input == "L":
            list_places(place_collection)
        elif user_input == "A":
            add_place(place_collection)
        elif user_input == "R":
            recommend_place(place_collection)
        elif user_input == "M":
            mark_place_visited(place_collection)
        elif user_input == "Q":
            # Save places to file
            place_collection.save_places(FILENAME)
            print(f"{len(place_collection.places)} places saved to places.csv")
            print("Have a nice day :)")
            break
        else:
            # Notify if user input is invalid
            print("Invalid menu choice")


def list_places(place_collection):
    """List all the places in the travel tracker."""
    visited_places = []
    unvisited_places = []
    for place in place_collection.places:
        if not place.is_visited:
            unvisited_places.append(place)
        else:
            visited_places.append(place)
    # Sort the unvisited and visited places by priority
    unvisited_places = sorted(unvisited_places, key=lambda p: (p.priority, p.name))
    visited_places = sorted(visited_places, key=lambda p: (p.priority, p.name))
    # Combine the unvisited and visited places
    places = unvisited_places + visited_places

    num_unvisited_places = len(unvisited_places)
    if not places:
        print("No places in the list.")
    else:
        # Determine maximum length of the place names
        max_name_length = max(len(place.name) for place in places)
        # Repeat each place
        for i, place in enumerate(places):
            name = place.name
            country = place.country
            priority = place.priority
            visited = "v" if place.is_visited else "n"
            mark_unvisited = "*" if not place.is_visited else ""
            if not mark_unvisited:
                print(f" {i + 1}. {name:<{max_name_length}} in {country}  {priority}")
            else:
                # Display an asterisk if the place has not been visited
                print(f"{mark_unvisited}{i + 1}. {name:<{max_name_length}} in {country}        {priority}")
        if num_unvisited_places == 0:
            # Display a message to inform user to add a new place if there are no more unvisited places
            print(f"\n{len(places)} places. No places left to visit. Why not add a new place?")
        else:
            # Display a message to inform the user of how many unvisited places are left
            print(f"\n{len(places)} places. You still want to visit {num_unvisited_places} places.")


def recommend_place(place_collection):
    """Recommend a random unvisited place from the travel tracker."""
    unvisited_places = [place for place in place_collection.places if not place.is_visited]
    if not unvisited_places:
        print("No places left to visit!")
    else:
        print("Not sure where to visit next?")
        random_place = random.choice(unvisited_places)
        print(f"How about... {random_place.name} in {random_place.country}?")


def add_place(place_collection):
    name, country, priority = get_place_details()
    place = Place(name, country, priority)
    place_collection.add_place(place)
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def get_place_details():
    """Ask the user to input the details for adding a new place."""
    while True:
        name = input("Name: ").strip()
        if name == "":
            print("Input cannot be blank.")
        else:
            break

    while True:
        country = input("Country: ").strip()
        if country == "":
            print("Input cannot be blank.")
        else:
            break

    while True:
        priority = input("Priority: ").strip()
        if priority == "":
            print("Input cannot be blank.")
        else:
            try:
                priority = int(priority)
                break
            except ValueError:
                print("Priority must be a valid integer.")

    return name, country, priority


def mark_place_visited(place_collection):
    """Mark a place as visited in the travel tracker."""
    print("Mark a place as visited")
    list_places(place_collection)
    number_input = int(input("Enter the number of the place to mark as visited: "))
    if number_input < 0 or number_input >= len(place_collection.places):
        print("Invalid place index.")
    else:
        place = place_collection.places[number_input]
        place.mark_as_visited()
        print(f"Marked {place.name} in {place.country} as visited.")



if __name__ == "__main__":
    main()
