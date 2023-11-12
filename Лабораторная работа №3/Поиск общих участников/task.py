def find_common_participants(participants1, participants2, delimiter=','):

    participants_1 = participants1.split(delimiter)
    participants_2 = participants2.split(delimiter)

    set1 = set(participants_1)
    set2 = set(participants_2)

    common_participants = set1.intersection(set2)

    return sorted(list(common_participants))
