from itertools import groupby
from redminelib import Redmine

def main():
    redmine = Redmine(
        'https://redmine.joestar.work/', 
        key='2a0c5d0b65736ea193e0a5071fdb6023020c7d98')

    issue = redmine.issue.get(387)
    print(issue.subject)
    open_child(issue)

def open_child(issue):
    for child in issue.children:
        print(child.subject)
        open_child(child)

main()