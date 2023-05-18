def get_name(person):
    name = person["name"]
    return name
# anoswer can be simpler
# return person["name"]

def get_favourite_tv_show(person):
    tv_show = person["favourites"]["tv_show"]
    return tv_show

def likes_to_eat(person, food):
    if food in person["favourites"]["snacks"]:
        return True
    else:
        return False
    
# short answer
# return food in person["favourtie"]["snacks"]

# longer answer   
# for snacks in person["favourties"]["snacks"]
#     if snack == fiid:
#         return True
    
# return False
    
def add_friend(self, new_friend):
    self["friends"].append(new_friend)

def remove_friend(self, old_friend):
    self["friends"].remove(old_friend)

def total_money(self):
    money = 0
    for person in self:
        money += person["monies"]
    return money

def lend_money(person1, person2, borrowed):
    # person1 -= ["monies"] - borrowed
    # person2 = ["monies"][2 + 1]
    # borrowed = person1, person2
    # return borrowed
    person1["monies"] -= borrowed
    person2["monies"] += borrowed



def all_favourite_foods(self):
    favourite_foods = []
    for person in self:
        for snack in person["favourites"]["snacks"]:
            favourite_foods.append(snack)

    return favourite_foods
   


# def find_no_friends(self):
#     no_friends = []
#     for person in self:
#         if len(person["friends"]) == 0:
#             no_friends.append(person)

def find_no_friends(people):
  no_mates = []
  for person in people:
    if len(person["friends"]) == 0:
      no_mates.append(person)

    # OR

    # if not person["friends"]:
    #   no_mates.append(person)
    
  return no_mates


# def unique_favourtie_tv_shows(self):
#     unique_tv_shows = []
#     for person in self:
#         if person["favourites"]["tv_show"] not in unique_tv_shows:
#             unique_tv_shows.append(person["favourties"]["tv_show"])
        
#     return unique_tv_shows

def unique_favourite_tv_shows(people):
  unique_tv_shows = []
  for person in people:
    if person["favourites"]["tv_show"] not in unique_tv_shows:
        unique_tv_shows.append(person["favourites"]["tv_show"])
    
  return unique_tv_shows
 