# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.

# Rules:

# Children under 14 old.
# Teens under 18 old.
# Young adults under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"

# Input of an age -> integer
# Output -> string - "drink _____"

# Look at the input integer
# Determine what age group it falls under
    # 0-13 -> child
    # 14-17 -> teen
    # 18-20 -> young adult
    # 21+ -> adult
# Once I have the age group, determine the drink choice
# return a string with the word "drink" and the drink choice

def solution(age):
    if age < 14:
        drink_choice = 'toddy'
    elif age < 18:
        drink_choice = 'coke'
    elif age < 21:
        drink_choice = 'beer'
    else:
        drink_choice = 'whisky'
    return 'drink ' + drink_choice
