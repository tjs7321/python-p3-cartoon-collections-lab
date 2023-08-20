cheeses = ["cheddar", "gouda", "camembert"]

def roll_call_dwarves(dwarves):
    number = 1
    for dwarf in dwarves:
        print(f"{number}. {dwarf}")
        number +=1

def summon_captain_planet(calls):
    new_calls = [call.title()+'!' for call in calls]
    return new_calls

def long_planeteer_calls(calls):
    big_or_nah = False
    if len(max(calls, key=len)) > 4:
        big_or_nah = True
    return big_or_nah

def find_the_cheese(list):
    for food in list:
        if food in cheeses:
            return food
    return None