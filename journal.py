def students_dict(records):
    """
    This function return a class Journal
    """
    temp_records = {}

    for name, grade in records:
        if name in temp_records:
            temp_records[name].append(grade)
        else:
            temp_records[name] = [grade]

    return temp_records


records = [
    ["Layla", 89],
    ["Tariq", 77],
    ["Layla", 91],
    ["Jana", 100],
    ["Tariq", 84],
    ["Ziad", 62],
    ["Jana", 97],
    ["Tariq", 73],
    ["Ziad", 71],
    ["Layla", 86],
    ["Jana", 94],
    ["Ziad", 75],
]

class_journal = students_dict(records)

print(class_journal)
