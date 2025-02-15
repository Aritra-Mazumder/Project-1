import random
import string

def generate_username(add_numbers=True, add_special_chars=True, length=None, structure=None):
    adjectives = ["Swift", "Brave", "Clever", "Witty", "Fierce", "Mighty", "Jolly", "Lively", "Sneaky", "Vivid"]
    nouns = ["Panther", "Falcon", "Tiger", "Wolf", "Dragon", "Eagle", "Hawk", "Raven", "Cheetah", "Cobra"]
    special_chars = "!@#$%^&*"
    
    username = ""
    
    if structure:
        for char in structure:
            if char == "A":
                username += random.choice(adjectives)
            elif char == "N":
                username += random.choice(nouns)
            elif char == "#" and add_numbers:
                username += str(random.randint(0, 9))
            elif char == "S" and add_special_chars:
                username += random.choice(special_chars)
    else:
        username = f"{random.choice(adjectives)}{random.choice(nouns)}"
        
        if add_numbers:
            username += str(random.randint(10, 99))
        
        if add_special_chars:
            username += random.choice(special_chars)
    
    if length and len(username) > length:
        username = username[:length]
    
    return username

# Example usage
if __name__ == "__main__":
    print("Generated Username:", generate_username(add_numbers=True, add_special_chars=True, length=12, structure="AANS#S"))
