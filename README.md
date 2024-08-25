# jira_issue_transition_script
## Description
I could be lazy sometimes and won't go to Jira and change the status for my tickets but certainly I could do that from terminal being less lazy.
The script is made so that an alias could be added in .bashrc and I just write something like `issue 11923 p` and issue 11923 is put in progress but that is something for yours to customize so I will leave it to just a command-line run.

## Where to get your api key
[here](https://id.atlassian.com/manage-profile/security/api-tokens)

## What are transition_ids??
well they sort of correspond to the keys for different status for an issue.
Something like 
`{
1:"Done",
2:"In-Progress"
}`

You can get them [here](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-transitions-get).
