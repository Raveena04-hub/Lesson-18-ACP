from datetime import date

def age_counter(birth_year):
    """
    Function to calculate age based on birth year.
    Argument:
        birth_year (int): The year of birth.
    Returns:
        int: Current age.
    """
    current_year = date.today().year
    age = current_year - birth_year
    return age

# Example usage:
year = int(input("Enter your birth year: "))
print("Your age is:", age_counter(year))
