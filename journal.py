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


def highest_average(journal):
    """
    Displays the Max_avergae in the students Journal
    """

    dict_average = {}
    for students in journal:
        dict_average[students] = student_average(journal[students])

    max_avg = 0
    name = ""

    for student in dict_average:
        if dict_average[student] > max_avg:
            max_avg = dict_average[student]
            name = student

    print(f"Student : {name} Average : {max_avg : .2f}")


def max_min(grades):
    """
    return a list of [Max,Min] of list grades
    """
    max_grade = 0
    lowest_grade = 100

    for grade in grades:
        if grade > max_grade:
            max_grade = grade
    for grade in grades:
        if grade < lowest_grade:
            lowest_grade = grade
    return [max_grade, lowest_grade]


def consistent_performance(journal):
    """
    Displays the Performance in the students Journal
    """

    dict_perf = {}
    for students in journal:
        perf = max_min(journal[students])
        dict_perf[students] = perf[0] - perf[1]

    max_perf = 100
    name = ""
    for student in dict_perf:
        if dict_perf[student] < max_perf:
            max_perf = dict_perf[student]
            name = student

    print(f"Student : {name} Perfomance : {max_perf : .2f}")


def failed_students(journal):
    """
    Displays students with grade below 70.
    """
    failed = []
    for students in journal:
        if max_min(journal[students])[1] < 70:
            failed.append(students)

    print(f"students that have a grade below 70 : {failed}")


def total_grades(journal):
    """
    Displays how many total grades were enetred in  class
    """
    grade_count = 0
    for students in journal:
        grade_count += len(journal[students])

    print(grade_count)


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

# Part 1: Rebuilding the Journal
class_journal = students_dict(records)

print(class_journal)


# Part 2: The Basic Report
student_report(class_journal)

highest_average(class_journal)
consistent_performance(class_journal)
failed_students(class_journal)
total_grades(class_journal)
