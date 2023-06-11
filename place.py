"""..."""


# Create your Place class in this file


class Place:
    """ Represents a place with its name, country, priority, and visited status."""

    def __init__(self, name="", country="", priority=0, visited=False, place_id=None):
        """Initializes a new instance of the Place class."""
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited
        self.id = place_id

    def __str__(self):
        """Returns a string representation of the Place object."""
        return f"Place: {self.name}, Country: {self.country}, Priority: {self.priority}, Visited: {self.is_visited}"

    def mark_as_visited(self):
        """Marks the place as visited."""
        self.is_visited = True

    def mark_as_unvisited(self):
        """Marks the place as unvisited."""
        self.is_visited = False

    def is_important(self):
        """Determines if the place is considered important based on its priority level."""
        return self.priority <= 2

    def toggle_visited(self):
        """Toggles the visited status of the place."""
        self.visited = not self.visited
