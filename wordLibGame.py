"""
Mad Libs is a phrasal template word game.
It consists of one player prompting others for a list of words to substitute for 
blanks in a story before reading aloud. 
The game is frequently played as a party game or as a pastime. - wikipedia

Inspired from: 12 Beginner Python Projects by FreeCodeCamp developed by Kylie Ying
"""

title = "Instructions for the baby-sitter"
print(title)

adj = input("Adjective: ")
pluralNoun1 = input("Plural Noun: ")
pluralNoun2 = input("Plural Noun: ")
pluralNoun3 = input("Plural Noun: ")
pluralNoun4 = input("Plural Noun: ")
noun1 = input("Noun: ")
adv = input("Adverb: ")
noun2 = input("Noun: ")

madlib = f"The boys can watch an hour of {adj} television before turning off the \
{pluralNoun1} in their room. Make sure they do not watch any violent {pluralNoun2} or adult \
{pluralNoun3}. If there are any phone {pluralNoun4} , do not identify yourself as the {noun1}-sitter. \
Take a message. Write it {adv} on the {noun2} provided."

print(madlib)