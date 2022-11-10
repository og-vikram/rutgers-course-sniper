import requests
import json


def get_courses(subject, semCode, campus, level):
    params = "subject=" + subject + "&semester=" + \
        semCode + "&campus=" + campus + "&level=" + level
    url = "http://sis.rutgers.edu/oldsoc/courses.json?" + params
    response = requests.get(url)
    parsed = json.loads(response.text)
    # print(url)
    return parsed


def get_sections(parsed, indexes):
    sections = []
    for course in parsed:
        for section in course['sections']:
            if section['index'] in indexes:
                sections.append(section)
    return sections


def webreg_url():
    return "https://sis.rutgers.edu/soc/register.json"
