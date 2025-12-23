import csv

with open("grades.csv", "r") as f:
    reader = csv.reader(f)
    for (name,hw1,hw2,midterm,final) in list(reader)[1:]:
        scores = [int(hw1),int(hw2),int(midterm),int(final)]
        print(f"{name}: {hw1}, {hw2}, {midterm}, {final}, with an average of {sum(scores)/4}")