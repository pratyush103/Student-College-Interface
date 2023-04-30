def calculate_gpa(lade_marks, qsp_marks, eob_marks, pem_marks):
    lade_grade = "F" if lade_marks < 20 else "D" if lade_marks < 35 else "C" if lade_marks < 45 else "B" if lade_marks < 50 else "A"
    qsp_grade = "F" if qsp_marks < 20 else "D" if qsp_marks < 35 else "C" if qsp_marks < 45 else "B" if qsp_marks < 50 else "A"
    eob_grade = "F" if eob_marks < 20 else "D" if eob_marks < 35 else "C" if eob_marks < 45 else "B" if eob_marks < 50 else "A"
    pem_grade = "F" if pem_marks < 20 else "D" if pem_marks < 35 else "C" if pem_marks < 45 else "B" if pem_marks < 50 else "A"
    
    lade_points = 0 if lade_grade == "F" else 1 if lade_grade == "D" else 2 if lade_grade == "C" else 3 if lade_grade == "B" else 4
    qsp_points = 0 if qsp_grade == "F" else 1 if qsp_grade == "D" else 2 if qsp_grade == "C" else 3 if qsp_grade == "B" else 4
    eob_points = 0 if eob_grade == "F" else 1 if eob_grade == "D" else 2 if eob_grade == "C" else 3 if eob_grade == "B" else 4
    pem_points = 0 if pem_grade == "F" else 1 if pem_grade == "D" else 2 if pem_grade == "C" else 3 if pem_grade == "B" else 4
    
    total_credits = 4 + 3 + 3 + 3
    total_points = lade_points * 4 + qsp_points * 3 + eob_points * 3 + pem_points * 3
    gpa = total_points / total_credits
    approxgpa=round(gpa,2)
    
    return approxgpa

def percent(lade_marks, qsp_marks, eob_marks, pem_marks):
    total = lade_marks + qsp_marks + eob_marks + pem_marks
    perc= str((total/200)*100)
    pc= "%"
    percentage=str(perc+pc)
    return percentage
    

def grade(gpa):
    grade = "F" if gpa<=1.49 else "D" if gpa<=1.99 else "C-" if gpa<=2.24 else "C" if gpa<=2.49  else "C+" if gpa<=2.74 else "B-" if gpa<=2.99 else "B" if gpa<=3.24  else "B+" if gpa<=3.49 else "A-" if gpa<=3.74 else "A" if gpa<=3.9  else "A+" 

    return grade

