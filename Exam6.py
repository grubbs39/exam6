import random
random.seed()

def did_anyone_have_a_birthday_match():
    birthdays_in_room_list = []
    for index in range(people_in_room):
        my_birthday = random.randint(1,367)
        birthdays_in_room_list.append(my_birthday)

    birthday_in_room_set = set(birthdays_in_room_list)
    if(len(birthday_in_room_set) != len(birthdays_in_room_list)):
        return True
    else:
        return False


if __name__ == "__main__":
    print("How many people are in the room?")
    people_in_room = int(input())
    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match()
        if (we_had_a_match):
            match_count += 1
    percent_match = (match_count / sample_size) * 100
    print("Out of a sample of {0}, we had {1} matches, or {2}%. {3} people in the room.".format(sample_size, match_count, percent_match, people_in_room))


    people_in_room = 23
    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match()
        if (we_had_a_match):
            match_count += 1
    percent_match = (match_count / sample_size) * 100
    print("Should be about 50%")
    print("Out of a sample of {0}, we had {1} matches, or {2}%. {3} people in the room.".format(sample_size, match_count, percent_match, people_in_room))

    people_in_room = 30
    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match()
        if (we_had_a_match):
            match_count += 1
    percent_match = (match_count / sample_size) * 100
    print("Should be about 70%")
    print("Out of a sample of {0}, we had {1} matches, or {2}%. {3} people in the room.".format(sample_size, match_count, percent_match, people_in_room))

    people_in_room = 35
    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match()
        if (we_had_a_match):
            match_count += 1
    percent_match = (match_count / sample_size) * 100
    print("Should be about 80%")
    print("Out of a sample of {0}, we had {1} matches, or {2}%. {3} people in the room.".format(sample_size, match_count, percent_match, people_in_room))

    people_in_room = 41
    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match()
        if (we_had_a_match):
            match_count += 1
    percent_match = (match_count / sample_size) * 100
    print("Should be about 90%")
    print("Out of a sample of {0}, we had {1} matches, or {2}%. {3} people in the room.".format(sample_size, match_count, percent_match, people_in_room))

    people_in_room = 47
    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match()
        if (we_had_a_match):
            match_count += 1
    percent_match = (match_count / sample_size) * 100
    print("Should be about 95%")
    print("Out of a sample of {0}, we had {1} matches, or {2}%. {3} people in the room.".format(sample_size, match_count, percent_match, people_in_room))

    people_in_room = 53
    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match()
        if (we_had_a_match):
            match_count += 1
    percent_match = (match_count / sample_size) * 100
    print("Should be about 98%")
    print("Out of a sample of {0}, we had {1} matches, or {2}%. {3} people in the room.".format(sample_size, match_count, percent_match, people_in_room))

    people_in_room = 58
    match_count = 0
    sample_size = 10000
    for index in range(sample_size):
        we_had_a_match = did_anyone_have_a_birthday_match()
        if (we_had_a_match):
            match_count += 1
    percent_match = (match_count / sample_size) * 100
    print("Should be about 99%")
    print("Out of a sample of {0}, we had {1} matches, or {2}%. {3} people in the room.".format(sample_size, match_count, percent_match, people_in_room))
