import csv
from operator import attrgetter
from place import Place
# Create your PlaceCollection class in this file


class PlaceCollection:
    """Represents a collection of places."""

    def __init__(self):
        """Initializes a new instance of the PlaceCollection class."""
        self.places = []

    def load_places(self, filename):
        """Loads places from a CSV file into the collection."""
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, is_visited = row
                priority = int(priority)
                is_visited = True if is_visited.lower() == 'true' else False
                place = Place(name, country, priority, is_visited)
                self.places.append(place)

    def save_places(self, filename):
        """ Saves places from the collection to a CSV file."""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for place in self.places:
                writer.writerow([place.name, place.country, place.priority, place.is_visited])

    def add_place(self, place):
        """ Adds a Place object to the collection."""
        self.places.append(place)

    def get_place_by_name(self, name):
        """Retrieves a Place object from the collection"""
        for place in self.places:
            if place.name == name:
                return place
        return None

    def sort_places_by_name(self):
        self.places.sort(key=lambda place: place.name)

    def sort_places_by_country(self):
        self.places.sort(key=lambda place: place.country)

    def sort_places_by_priority(self):
        self.places.sort(key=lambda place: place.priority)

    def sort_places_by_visited(self):
        self.places.sort(key=lambda place: place.visited, reverse=True)

    def get_place_by_id(self, place_id):
        pass

    def sort_places(self, text):
        pass

    def get_places_to_visit(self):
        """Returns a list of places in the collection that have not been visited."""

        places_to_visit = []
        for place in self.places:
            if not place.is_visited:
                places_to_visit.append(place)
        return places_to_visit

    def get_unvisited_places_count(self):
        """Returns the count of unvisited places"""
        count = 0
        for place in self.places:
            if not place.visited:
                count += 1
        return count

    def sort_places(self, text):
        pass

