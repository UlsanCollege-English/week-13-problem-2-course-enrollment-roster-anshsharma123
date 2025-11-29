def build_roster(registrations):
    """
    Given a list of (student_id, course_id) pairs, build a course roster.

    The result should be a dictionary where:
      - each key is a course id (string)
      - each value is a sorted list of unique student ids (strings)
        enrolled in that course

    Duplicate registrations for the same (student_id, course_id) pair
    should appear only once in the output.
    """

    roster = {}  # course_id -> set of student_ids

    for student, course in registrations:
        if course not in roster:
            roster[course] = set()   # use a set to avoid duplicates
        roster[course].add(student)  # add student to this course

    # convert each set to a sorted list
    final_roster = {}
    for course, students in roster.items():
        final_roster[course] = sorted(students)

    return final_roster
