"""
Name: Royce Chai Sir Heng
Date: 30/5/2023
Brief Project Description:
"Develop a travel tracker application that allows users to track their visited and unvisited places."
GitHub URL: https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-royce-jcu
"""
# Create your main program in this file, using the TravelTrackerApp class
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout

from place import Place
from placecollection import PlaceCollection


class CustomButton(Button):
    """Custom button class with an additional place_id property."""
    place_id = ObjectProperty(None)  # Custom button property to store place ID


class TravelTrackerApp(App):
    """Kivy application class for the Travel Tracker app."""
    status_label = ObjectProperty(None)  # Object property to reference status label
    places_layout = ObjectProperty(None)  # Object property to reference places layout

    def __init__(self, **kwargs):
        """ Initialize the TravelTrackerApp class. """
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()  # Create an instance of PlaceCollection
        self.place_buttons = []  # List to store place buttons

    def build(self):
        """Build the Travel Tracker app GUI."""
        self.title = "Travel Tracker"
        self.place_collection.load_places("places.csv")  # Load places from CSV file
        main_layout = BoxLayout(orientation='horizontal')

        # Left side layout
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.5, 1))

        # Sort by dropdown
        sort_label = Label(text='Sort by:')
        sort_dropdown = Spinner(values=['Name', 'Country', 'Priority', 'Visited'], size_hint=(1, None), height=30)
        sort_dropdown.bind(on_text=self.sort_places)  # Bind sort_places method to dropdown

        # Input layout
        input_layout = self.create_input_layout()  # Create input layout

        # Add all elements to left layout
        left_layout.add_widget(sort_label)
        left_layout.add_widget(sort_dropdown)
        left_layout.add_widget(input_layout)

        # Right side layout
        right_layout = BoxLayout(orientation='vertical', size_hint=(0.5, 1))

        # Places to visit layout
        self.places_layout = self.create_places_layout()  # Create places layout

        # Program messages (status bar)
        self.status_label = Label(size_hint=(1, 0.1), pos_hint={'right': 1})

        # Add all elements to right layout
        right_layout.add_widget(self.places_layout)
        right_layout.add_widget(self.status_label)

        # Add left and right layouts to main layout
        main_layout.add_widget(left_layout)
        main_layout.add_widget(right_layout)

        self.update_place_buttons()  # Update place buttons
        self.root = main_layout

        return self.root

    def create_input_layout(self):
        """Create the input layout for adding new places."""
        input_layout = BoxLayout(orientation='vertical')

        # Create text inputs layout
        text_inputs_layout = BoxLayout(orientation='vertical', spacing=10)
        text_inputs_layout.add_widget(Label(text='Add New Place...'))
        text_inputs_layout.add_widget(Label(text='Name:'))
        name_input = TextInput(size_hint=(1, 10))
        text_inputs_layout.add_widget(name_input)
        text_inputs_layout.add_widget(Label())
        text_inputs_layout.add_widget(Label(text='Country:'))
        country_input = TextInput(size_hint=(1, 10))
        text_inputs_layout.add_widget(country_input)
        text_inputs_layout.add_widget(Label())
        text_inputs_layout.add_widget(Label(text='Priority:'))
        priority_input = TextInput(size_hint=(1, 10))
        text_inputs_layout.add_widget(priority_input)
        text_inputs_layout.add_widget(Label())
        input_layout.add_widget(text_inputs_layout)

        # Create button layout
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=30)

        add_button = Button(text='Add Place', size_hint=(0.3, 1))
        add_button.bind(on_press=lambda instance: self.add_place(name_input.text, country_input.text, priority_input.text))

        clear_button = Button(text='Clear', size_hint=(0.3, 1))
        clear_button.bind(on_press=self.clear_inputs)

        button_layout.add_widget(add_button)
        button_layout.add_widget(clear_button)

        input_layout.add_widget(button_layout)

        return input_layout

    def create_places_layout(self):
        """ Create the layout for displaying places."""
        Create the layout for d
        places_layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
        places_layout.bind(minimum_height=places_layout.setter('height'))

        return places_layout

    def update_place_buttons(self):
        """ Update the place buttons based on the places in the collection."""
        self.places_layout.clear_widgets()
        self.place_buttons.clear()

        for place in self.place_collection.places:
            place_text = f"{place.name} in {place.country} {place.priority}"
            place_button = CustomButton(text=place_text, background_color=self.get_button_color(place))
            place_button.place_id = place.id  # Set the place ID for the button
            place_button.bind(on_press=self.toggle_visited)  # Bind toggle_visited method to button
            self.places_layout.add_widget(place_button)
            self.place_buttons.append(place_button)

        self.update_status_bar()

    def sort_places(self, instance, text):
        """ Sort the places based on the selected sorting option."""
        self.place_collection.sort_places(text)
        self.update_place_buttons()

    def add_place(self, name, country, priority):
        """Add a new place to the collection."""
        if name == '' or country == '' or priority == '':
            self.status_label.text = 'All fields must be completed'
            return

        try:
            priority = int(priority)
            if priority < 1:
                self.status_label.text = 'Priority must be > 0'
                return
        except ValueError:
            self.status_label.text = 'Please enter a valid number'
            return

        place = Place(name, country, priority)  # Create a new Place object
        self.place_collection.add_place(place)  # Add the place to the collection
        self.update_place_buttons()  # Update place buttons
        self.clear_inputs()  # Clear input fields
        self.status_label.text = 'Place added successfully'

    def clear_inputs(self, instance=None):
        """Clear the input fields and status label."""
        self.root.ids.input_layout.name_input.text = ''
        self.root.ids.input_layout.country_input.text = ''
        self.root.ids.input_layout.priority_input.text = ''
        self.status_label.text = ''

    def toggle_visited(self, instance):
        """Toggle the visited status of a place."""
        place_id = instance.place_id
        place = self.place_collection.get_place_by_id(place_id)  # Get place object by ID
        place.visited = not place.visited  # Toggle visited status
        instance.background_color = self.get_button_color(place)  # Update button color
        self.update_status_bar()

    def get_button_color(self, place):
        if place.visited:
            return [0.2, 0.7, 0.2, 1]  # Green color if visited
        else:
            return [0.8, 0.2, 0.2, 1]  # Red color if not visited

    def update_status_bar(self):
        places_to_visit = self.place_collection.get_unvisited_places_count()
        self.status_label.text = f'Places to visit: {places_to_visit}'


if __name__ == '__main__':
    TravelTrackerApp().run()  # Run the TravelTrackerApp
