# class userprofile():
#     def __init__(self, username, profession, budget, description): 
#         self.name = username
#         self.profession = profession
#         self.budget = budget
#         self.description = description

    
# def createUser(username,profession,budget,description):
#     user = userprofile(username,profession,budget,description)
#     return user

class userprofile():
    def __init__(self, username, profession, budget, description, graphics_requirement):
        self.name = username
        self.profession = profession
        self.budget = budget
        self.description = description
        self.graphics_requirement = graphics_requirement  # New attribute for graphics requirement


def createUser(username, profession, budget, description, graphics_requirement):
    user = userprofile(username, profession, budget, description, graphics_requirement)
    return user

