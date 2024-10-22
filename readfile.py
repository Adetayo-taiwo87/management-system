"""
reads json file and print to the terminal
"""
import json


filename = input("Input json file to read: ")

with open(filename + ".json") as e:
    objects = json.load(e)
    if filename == 'students':
        for student in objects["students"]:
            print(student)
    else:
        for ent in objects["entrepreneurs"]:
            print(ent)
