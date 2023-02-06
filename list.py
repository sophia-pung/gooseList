import random

to_do_items = [
    'Hide the remote control',
    'Honk at everyone in the room',
    'Hide someone\'s keys to prevent them from leaving',
    'Rearrange the decorations to make the party feel a little more chaotic.',
    'Pester the party photographer by getting in three shots',
    'Sneak up behind someone and honk loudly',
    'Steal someone\'s drink and hide it in the corner',
    'Pretend to be lost and ask for directions, then run away giggling',
    'Hijack the DJ\'s music selection and play your own tunes',
    'Grab a balloon and have a balloon fight with others',
    'Goose-block the door and prevent people from entering or leaving',
    'Stomp on a balloon and make it pop.',
    'Find someone with a camera and pose for a silly photo.',
    'Get four people to play a game of "duck, duck, goose"',
    'Ask someone if you can wear their shoes for the rest of the night.',
    'Interrupt a conversation by honking loudly',
    'Get someone to chase you by stealing their drink or food.',
    'Take a group photo with two others making a goose face',
    'Put on a performance of "The Goose Who Wanted to Fly" for two people',
    'Hiss at someone who gets too close to your territory.',
    'Take someone\'s food and gobble it up'
]

# Define the number of people in the party
num_people = 30

# Define the number of items for each party member
num_items = 10

# Create a list to store the to-do items for each party member
party_member_tasks = [[] for i in range(num_people)]

# Distribute the to-do items among the party members
for i in range(num_items):
    for j in range(num_people):
        task = random.choice(to_do_items)
        while task in party_member_tasks[j]:
            task = random.choice(to_do_items)
        party_member_tasks[j].append(task)
        # to_do_items.remove(task)

# Print the to-do items for each party member
for i, tasks in enumerate(party_member_tasks):
    print(f"Party Member {i+1}'s To-Do List:")
    for j, task in enumerate(tasks):
        if j == len(tasks) - 1:
            print(f'`{task}`')
        else:
            print(f'`{task}`,')
    print()





