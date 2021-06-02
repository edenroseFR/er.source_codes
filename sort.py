
import db




def mergeSort(nlist):
    # from w3resource.com
    # https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1

    return nlist


def byID():
    unsorted_id = db.get_IDs()
    sorted_id = mergeSort(unsorted_id)
    sorted_student = []

    for id in sorted_id:
        student = db.get_student(id)
        if student[2] != '':
            student = [student[0], student[1] + ' ' + student[2][0] + '. ' + student[3], student[4], student[5], student[6]]
        else:
            student = [student[0], student[1] + ' ' + student[3], student[4], student[5], student[6]]
        sorted_student.append(student)


    return sorted_student


def byLastName():
    unsorted_lastName = db.get_StudentLastname()
    sorted_lastName = mergeSort(unsorted_lastName)
    sorted_student = []

    for i in sorted_lastName:
        students = db.get_lastname(i)
        for j in students:
            sorted_student.append(j)

    return sorted_student

