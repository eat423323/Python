"""
This program generates passages that are generated in mad-lib format
Author: Katherin
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs has started!"

name = raw_input("Enter a name: ")

adjective_1= raw_input("adjective 1? ")
adjective_2= raw_input("adjective 2? ")
adjective_3= raw_input("adjective 3? ")

verb= raw_input("verb? ")

noun_1= raw_input("noun 1? ")
noun_2= raw_input("noun 2? ")
animal = raw_input("animal? ")
food = raw_input("food?")
fruit = raw_input("fruit? ")
superhero = raw_input("superhero? ")
country = raw_input("country? ")
dessert = raw_input("dessert? ")
year = raw_input("year? ")

print STORY % (name, adjective_1, adjective_2, animal, food, verb, noun_1, fruit, adjective_3, name, country, dessert, name, year, noun_2)
