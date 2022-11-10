#!/usr/bin/env python
import os
from dotenv import load_dotenv
from trackerUtils import get_courses

# loads API tokens from .env file
load_dotenv()
USER = os.environ['PUSHOVER_USER_TOKEN']
API = os.environ['PUSHOVER_API_TOKEN']

# sections to track
indexes = ["04703", "04704"]


# gets course data from API
courses = get_courses("198", "12023", "NB", "UG")

# checks if tracked course is open
for course in courses:
    for section in course['sections']:
        if section['index'] in indexes and section['openStatus'] == True:
            print(course['title'] + " " + section['index'] + " is open!")
            # TODO
            # send push notification
