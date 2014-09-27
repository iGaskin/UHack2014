import json
import pprint
import re
fname = "../APAS/Travis_APAS.html"


p = re.compile(r'^CSCI[0-9]{4}')
#courseDescription = ''
#userDict = defaultdict(dict) # dictionary to store class and grades
# probably should look like this
userDict = dict()
"""
userDict = {
                   0:
                   [{
                    'names': '',
                    'description':   '',
                    'template-type': 'knowledge'
                   }]
}
"""
#userDict = json.dumps(userDict)
idLine   = 7  
nameLine = 8 
#counterCourse = 0
descriptDict = {
                'CSCI1103': 'Java Programming MN West', 
                'CSCI1901': 'Computer Programming I',
                'CSCI1902': 'Computer Programming 2',
                'CSCI2011': 'Discrete Structures of Computer Science',
                'CSCI2011-evening': 'Discrete Structures of Computer Science',
                'CSCI2041': 'Advanced Programming Principles',
                'CSCI3081': 'Program Design and Development',
                'CSCI4011': 'Formal Languages and Automata Theory',
                'CSCI4041': 'Algorithms and Data Structures',
                'CSCI4041H':'Honors Algorithms and Data Structures',
                'CSCI4061': 'Intro to Operating Systems',
                'CSCI4131': 'Internet Programming',
                'CSCI4211': 'Introduction to Computer Networks',
                'CSCI4511W': 'Introduction to Artificial Intelligence',
                'CSCI4707': 'Principles of Database Systems',
                'CSCI5103': 'Operating Systems',
                'CSCI5106': 'Programming Languages',
                'CSCI5115': 'User Interface Design, Implementation and Evaluation',
                'CSCI5271': 'Introduction to Computer Security',
                'CSCI5304': 'Computational Aspects of Matrix Theory',
                'CSCI5421': 'Advanced Algorithms and Data Structures',
                'CSCI5511': 'Artificial Intelligence I',
                'CSCI5523': 'Introduction to Data Mining',
                'CSCI5525': 'Machine Learning',
                'CSCI5801': 'Software Engineering I',
                'CSCI5980-002': 'Topics in Computer Science: Distributed Computing',
                'CSCI5980-sf': 'Software Foundations',
                'CSCI8970': 'Computer Science Colloquium',
                'CSCI8980-sf': 'Software Foundations',
                'CSCI8980-vr': 'Current Research in Virtual and Augmented Reality',
}
f = open(fname, 'r')
for lineNumber, line in enumerate(f):
    """
    if lineNumber == idLine:
        userDict['student']['ID'] = line.split()[0][4:]
        #print("Found the id:", line)
    if lineNumber == nameLine:
        #print("Found the name:", line)
        userDict['student']['name'] = line.split()[0][4:]
    """
    if 'CSCI' in line:
        tokens = line.split()
        for course in range(len(tokens)):
            
            if re.match(p, tokens[course][1:]):  # regex to confirm that course 
                courseName = tokens[course][1:]
                # grab the course description
                """
                courseDescription = ''
                for course in range(len(tokens)):
                    if tokens[course] == '1.0' or tokens[course] == '2.0' or tokens[course] == '4.0' or tokens[course] == '4.0':
                        print("Found the credit at", course)
                        startIndex = course + 2
                    elif tokens[course] == '|':
                        print("Found the pipe at ", course)
                        endIndex = course
                for description in range(startIndex, endIndex):
                    print(tokens[description])
                    if description < len(tokens):
                        courseDescription += tokens[description] + ' '
                print("The description", courseDescription)
                """
                # update the dictionary 
                userDict[courseName] = dict()
                courseDescription = descriptDict[courseName]
                userDict[courseName]['name'] = courseName
                userDict[courseName]['description'] = courseDescription 
                userDict[courseName]['template_type'] = 'knowledge'
                

print(json.dumps(userDict, sort_keys=False, indent=4))
#studentInfo.json
with open('userDict.json', 'w') as outfile:
    json.dump(userDict, outfile)
