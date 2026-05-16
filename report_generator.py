student_name = input("Enter student name:")
backend_marks = int(input("Enter Backend marks:"))
frontend_marks = int(input("Enter Frontend marks:"))
design_marks = int(input("Enter Design marks:"))


def calculate_average(backend, frontend, design):
    total_marks = backend + frontend + design
    average = total_marks/3
    return average

def get_grade(average):
    if average >= 80:
       return "A"
    elif average >=70:
        return "B"
    elif average >=60 :
        return "C"    
    elif average >=50:
        return "D"
    else:
        return "E"

def student_report(name, backend, frontend, design):
    average_student_marks = calculate_average(backend,frontend,design) 
    graded = get_grade(average_student_marks)  

    report = {
        'name':  name,
        'Backend': backend,
        'Frontend': frontend,
        'Design': design,
        'Average': average_student_marks,
        'Grade': graded
    } 


    return report 

report = student_report(student_name, backend_marks, frontend_marks, design_marks)
print(report)


