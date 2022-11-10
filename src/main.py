#!/usr/bin/env python3
import os
from dotenv import load_dotenv
import requests
from trackerUtils import get_courses

# loads API tokens from .env file
load_dotenv()
USER = os.environ['PUSHOVER_USER_TOKEN']
API = os.environ['PUSHOVER_API_TOKEN']

# sections to track
indexes = []
with open('indexes.md', 'r') as f:
    for line in f:
        indexes.append(line.strip())
f.close()

# webreg initial url with empty indexList param
webreg_url = "https://sims.rutgers.edu/webreg/editSchedule.htm?"
webreg_params = "login=cas&semesterSelection=12023&indexList="

# gets course data from API
courses = get_courses("198", "12023", "NB", "UG")


# checks if tracked course is open
for course in courses:
    for section in course['sections']:
        if section['index'] in indexes and section['openStatus'] == True:
            print(course['title'] + " " + section['index'] + " is open!")

            # appends index to webreg url
            final_url = webreg_url + webreg_params + section['index']

            # push notification prep
            message = course['title'] + " " + section['index'] + " is open!"
            payload = {
                "token": API,
                "user": USER,
                "message": message,
                "url": final_url,
            }
            headers = {
                "User-Agent": "Python"
            }

            # sends push notification
            r = requests.post(
                "https://api.pushover.net/1/messages.json", data=payload, headers=headers)
            if (r.status_code == 200):
                print("Push notification sent!")
                indexes.remove(section['index'])
                with open("indexes.md", "w") as f:
                    for line in indexes:
                        f.write(line)
            else:
                print(r.text)
