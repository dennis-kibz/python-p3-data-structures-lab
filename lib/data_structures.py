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
    names = [food['name'] for food in spicy_foods]
    return names

if __name__ == "__main__":
    result = get_names(spicy_foods)
    print(result)
    # print(f"Type: {type(result)}")

# names = get_names(spicy_foods)
# print(names)

# names = get_names(spicy_foods)
# print(names)
    


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
if __name__ == "__main__":
    result = get_spiciest_foods(spicy_foods)
    # print("Spiciest foods (heat > 5):")
    print (result)

#     print(f"\nType: {type(result)}")
#     print(f"Number of spicy foods: {len(result)}")


# print("\nSpicy foods details:")
# for food in result:
#     print(f"- {food['name']} ({food['cuisine']}) - Heat: {food['heat_level']}")





def print_spicy_foods(spicy_foods):
    pass

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     pass

# def print_spiciest_foods(spicy_foods):
#     pass

# def get_average_heat_level(spicy_foods):
#     pass

# def create_spicy_food(spicy_foods, spicy_food):
#     pass
