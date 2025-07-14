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
    print("Names of spicy foods:")
    print(result)
    # print(f"Type: {type(result)}")

# names = get_names(spicy_foods)
# print(names)
    


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]
if __name__ == "__main__":
    result = get_spiciest_foods(spicy_foods)
    print("Spiciest foods (heat > 5):")
    print (result)

    # print(f"\nType: {type(result)}")
    # print(f"Number of spicy foods: {len(result)}")


# print("\nSpicy foods details:")
# for food in result:
#     print(f"- {food['name']} ({food['cuisine']}) - Heat Level: {food['heat_level']}")





def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
         peppers = "🌶" * food['heat_level']
         print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")
if __name__ == "__main__":
    print("Spicy Foods:")
    print_spicy_foods(spicy_foods)
        


        



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
             return food
    return None
if __name__ == "__main__":
    cuisine = "Thai"
    result = get_spicy_food_by_cuisine(spicy_foods, cuisine)
    if result:
        print(f"Spicy food from {cuisine}: {result['name']} (Heat Level: {result['heat_level']})")
    else:
        print(f"No spicy food found for cuisine: {cuisine}")





def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            peppers = "🌶" * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {peppers}")


if __name__ == "__main__":
    print("Spiciest Foods (Heat Level > 5):")
    print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food['heat_level'] for food in spicy_foods)
    average_heat = total_heat / len(spicy_foods)
    return average_heat
if __name__ == "__main__":
    average_heat = get_average_heat_level(spicy_foods)
    print(f"Average Heat Level: {average_heat:.2f}")

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
if __name__ == "__main__":
    new_food = {
        "name": "Mexican fajitas",
        "cuisine": "Mexican",
        "heat_level": 8,
    }
    updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
    print("Updated Spicy Foods:")
    print_spicy_foods(updated_spicy_foods)

