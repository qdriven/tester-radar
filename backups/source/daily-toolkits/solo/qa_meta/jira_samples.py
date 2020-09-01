# -*- coding:utf-8 -*-
from collections import Counter

from jira import JIRA

options = {
    'server': 'http://jira.server.com'
}
jira = JIRA(options)

projects = jira.projects()
keys = sorted([project.key for project in projects])

# issue
issue = jira.issue("issue_no")
# login
jira = JIRA(basic_auth=('user','pwd'))
props = jira.application_properties()

# top3
issues = jira.search_issues('filter_fields=filter_value')
top_three = Counter([issue.fields.project.key for issue in issues]).most_common(3)

# GreenHopper

# issue operation
jira.assign_issue(issue="issue_no",assignee="new assignee")

issue_dict = {
    'project': {'id': 123},
    'summary': 'New issue from jira-python',
    'description': 'Look into this one',
    'issuetype': {'name': 'Bug'},
}
n_issue=jira.create_issue(issue_dict)
n_issue.update()

