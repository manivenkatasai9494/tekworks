projectMarks = int(input("Enter Project Marks = "))
internalMarks = int(input("Enter Internal Marks = "))
ExternalMarks = int(input("Enter External Marks = "))
totalMarks = 0


if projectMarks >= 50 and internalMarks >= 50 and ExternalMarks >=50 :
    totalMarks = projectMarks*(70/100) + internalMarks * (10/100) + ExternalMarks * (20/100)
    if totalMarks >= 90:
        print("A Grade")
    elif totalMarks > 80 and totalMarks <= 90 :
        print("B grade")
    elif totalMarks >50 and totalMarks <=80 :
        print("C Grade")
else :
    if projectMarks <50:
        print(f"Failed in  project  marks {projectMarks}")
    if internalMarks <50:
        print(f"Failed in  internalMarks  marks {internalMarks}")
    if ExternalMarks < 50:
        print(f"Failed in  ExternalMarks  marks {ExternalMarks}")

