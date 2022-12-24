# This is study Python.
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]
s= sorted(subject_marks, key=lambda x: x[1], reverse=True)
for i in s:
    print(*i)