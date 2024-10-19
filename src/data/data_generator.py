import random
import datetime
from faker import Faker

degree_programs = ["Computer Science", "Statistics", "Mathematics", "Sociology", "Philosophy", "Civil Engineering", "Nursing", "Business Administration", "Economics", "Veterinary Medicine"]
majors = ["Cybersecurity", "Economical Statistics", "Theory", "Social Psychology", "Database Systems", "Web Development", "Mobile Devleopment", "Maternal Health", "Marketing Management", "Business Management"]

fake = Faker()

f = open("student_table.csv", "w")

f.write("StudNo,StudentName,Birthday,Degree,Major,UnitsEarned\n")

for i in range(100000):
    studno = str(random.randint(2000,2024)) + "-" + str(random.randint(10000,99999))
    studname = fake.name()
    birthday = fake.date_between(start_date=datetime.date(1982,1,1), end_date=datetime.date(2006,12,31))
    degree = random.choice(degree_programs)
    major = random.choice(majors)
    units_earned = str(random.randint(3,150))

    f.write(studno+","+studname+","+str(birthday)+","+degree+","+major+","+units_earned+"\n")

f.close()