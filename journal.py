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


def student_average(grades):
    """
    Returns the avergae of a list of grades
    """

    sum_grades = 0
    for grade in grades:
        sum_grades += grade
    return sum_grades / len(grades)


def student_report(journal):
    """
    Display a student_report report of the students
    """
    for student_name, student_grades in journal.items():
        average = student_average(student_grades)
        print(f"{student_name}: {student_grades} : Average ({average : .2f})")


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

student_report(class_journal)
