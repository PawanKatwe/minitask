
'''
You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?

Task 
Given everyone's name that showed up at the same time, determine how long it will take to get your new license.

Input Format 
Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces.

Output Format 
You will output an integer of the number of minutes that it will take to get your license.

Sample Input
'Eric'
2
'Adam Caroline Rebecca Frank'
'''

import math
name = str(input('Enter you name:'))
agents = int(input('Enter no. of agents available:'))
other_people = str(input('Enter names of other people:'))

people_list = other_people.split()
people_list.append(name)
people_list = sorted(people_list)

place = people_list.index(name) + 1

print(math.ceil(place/agents)*20)
