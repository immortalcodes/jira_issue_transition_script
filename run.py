
import requests
from requests.auth import HTTPBasicAuth
import json
import sys

# Edit details here
EMAIL = "your_email"
API_TOKEN = "api_token"

# This differs for your org
transition_dict = {
    "T": "11",
    "P": "21",
    "IR": "31",
    "B": "41",
    "TBD": "51",
    "D": "61",
    "R": "71",
    "U": "81"
}
def transition_issue(issue_key, transition_id):
    url = f"https://warthogs.atlassian.net/rest/api/3/issue/{issue_key}/transitions"
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "transition": {
        "id": transition_id
    },
    } )
    try:
        response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
        )
        if response.status_code == 204:
            print("Successfully transitioned issue ", issue_key)
        else:
            print("Failed to transition issue ", issue_key)
    except Exception as e:
        print("Failed to transition issue")

def main():
    print("""Transition Issue : Follow the below steps to transition an issue
        "Triaged": T,
        "Progress": P,
        "In Review": IR,
        "Blocked": B,
        "To Be Deployed": TBD,
        "Done": D,
        "Rejected": R,
        "Untriaged": U
          
        Case does not matter for these codes
    """)
    # Issue might not be WD-123 for you
    input_issue_key = "WD-" + input("Enter issue key (e.g., 123): WD-")
    input_transition = input("Enter transition: ").strip().upper()
    transition_id = transition_dict.get(input_transition)
    
    if transition_id:
        transition_issue(input_issue_key, transition_id)
    else:
        print(f"Invalid transition code: {input_transition}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
