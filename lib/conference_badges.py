def badge_maker(name):
     return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [badge_maker(name) for name in names]
# speaker_names = ["Arel", "Carol", "Certo"]
# badges = batch_badge_creator(speaker_names)

# for badge in badges:
#     print(badge)

def assign_rooms(names):
     room_assignments = []
     for i, name in enumerate(names, start=1):
        room_assignment = f"Hello, {name}! You'll be assigned to room {i}!"
        room_assignments.append(room_assignment)
    
     return room_assignments

# names = ["Arel", "Carol", "John"]
# room_assignments = assign_rooms(names)

# for assignment in room_assignments:
#     print(assignment)

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)

