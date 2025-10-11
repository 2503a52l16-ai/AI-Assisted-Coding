# legacy_student_db.py

students = []

def add_student(name, sid):
    students.append([name, sid])

def find_student(sid):
    for s in students:
        if s[1] == sid:
            return s
    return None

add_student("Alice", 1)
add_student("Bob", 2)
print(find_student(1))
print(find_student(3))# refactored_student_db.py