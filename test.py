import random

members = """KAVYASREE ANDE
ASFIYA BASITH
HANEEN
SKAND GUPTA
YESHASWINI BHEEMREDDY
SHAIK NIKHAT TARANNUM
RADHIKA JAIN
MEGHANA KALAKUNTLA
SHIVANI VERMA
SAMEER JHARIYA
GYANA SAI REDDY
AGARSHIKA RAMESH
JAYADEEP SRIKAR
G AKHIL REDDY
ANURAG
SHUBHAM PATTNAIK
PRASUN PARIJAT"""

members = members.splitlines()

groups = """DIAMOND JUBILEE
ALUMNI SECTION
CAMPUS LIFE
CAREER REVIEW/ RESEARCH/ STARTUP’S
FACULTY
SPORTS
STUDENTS
ACADEMIC LAURELS
CLUBS
POP CULTURE/ MISCELLANEOUS
VOLUNATARY ACTIVITIES
INTERNATIONAL SECTION"""

groups = groups.splitlines()

x = len(members)//len(groups)
print(x)

for group_name in groups:
    foo = []
    for i in range(x+1):
        participant = random.choice(members)
        foo.append(participant)
        members.remove(participant)
    print("group {} consists of: ".format(group_name))
    for z in foo:
        print(z)
    print("\n")