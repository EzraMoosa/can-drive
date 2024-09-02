import sys


class Adult:

    """Class for Adult"""

    def __init__(self, name, age, eye_colour, hair_colour):

        """
        Initialize an Adult with a name, age, eye and hair colour.

        Keyword arguments:
            - name (str) : The name of the person.
            - age (int) : The age of the person.
            - hair_colour (str) : The hair colour of the person.
            - eye_colour (str) : The eye colour of the person
        """

        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        """Print whether the person is old enough to drive."""

        print(f"{self.name} is old enough to drive.")


class Child(Adult):

    """Class for Child"""

    def can_drive(self):
        """Prints that this person is too young to drive"""

        print(f"{self.name} is too young to drive.")


def main():
    """Main function to get user inputs and check for age"""

    # Repeatedly validate user's inputs
    while True:
        try:
            name = input("Enter the name: ")
            if not name.strip():
                raise ValueError("Name cannot be blank.")

            age = int(input("Enter the age: "))
            if age < 0:
                raise ValueError("Age cannot be less than zero.")

            hair_colour = input("Enter the hair colour: ")
            if not hair_colour.strip():
                raise ValueError("Hair colour cannot be blank.")

            eye_colour = input("Enter the eye colour: ")
            if not eye_colour.strip():
                raise ValueError("Eye colour cannot be blank.")

            # Check age to see if person is an Adult or Child
            if age >= 18:
                person = Adult(name, age, hair_colour, eye_colour)
            else:
                person = Child(name, age, hair_colour, eye_colour)

            person.can_drive()
            sys.exit()

        except ValueError:
            print("Invalid input! Try again.")


if __name__ == "__main__":
    main()


# References:
# https://www.geeksforgeeks.org/python-program-to-check-if-string-is-empty-or-not/
