import json
import pprint
import from courseDict *
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
                    'template_type': 'knowledge'
                    'recipient_email': 'travisvuong@hotmail.com'
                    'badge_template_id': 'c2d4fb9a-1769-47c3-9391-110092758f08'
                    'issued_to_first_name': 'Travis'
                    'issued_to_last_name': 'Vuong'
                    'expires_at': NULL
                   }]
}
"""
#userDict = json.dumps(userDict)
idLine   = 7  
nameLine = 8 
#counterCourse = 0

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
