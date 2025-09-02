print("Welcome to Report Card System :")
studentCount = int (input("Enter the No of Student:"))
def createStudent():
    name=input("Enter the Student Name:")
    age=int(input("Enter the Student Age:"))
    std=int(input("Enter the Student Standard Number:"))
    physics=int(input("Enter Physics Mark:"))
    math=int(input("Enter Math Mark:"))
    chemistry=int(input("Enter Chemistry Mark:"))
    english=int(input("Enter English Mark:"))
    tamil=int(input("Enter Tamil Mark:"))
    python=int(input("Enter Python Mark:"))
    pmssScore = physics+chemistry+math/3;
    cutOff=(physics+chemistry/2)+math
    totalMark=python+math+chemistry+english+tamil+physics;
    percentage =totalMark/6;
    print("Your Total Mark is: ",totalMark)
    print("Your Percentage Mark is: ",percentage)
    print("Student Cut off",cutOff)
    print("Pmss Score",pmssScore)

for i in range(studentCount):
    createStudent()
