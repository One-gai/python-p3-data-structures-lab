spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [spicy["name"] for spicy in spicy_foods]
    return (names)

def get_spiciest_foods(spicy_foods):
    result_spicy = [spicyest for spicyest in spicy_foods if spicyest["heat_level"] > 5]
    return result_spicy

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
   
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None
        
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
    

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        if food["heat_level"] > 5 :
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")



    

def get_average_heat_level(spicy_foods):
   result_sum = sum(food["heat_level"]for food in spicy_foods)
   return result_sum / len(spicy_foods)
   
    


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

