import json
import requests

# webhook_url = "https://hooks.slack.com/services/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"
webhook_url = "https://hooks.slack.com/services/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"
slack_data = {"text": "woop woop!"}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={"Content-Type": "application/json"}
)
if response.status_code != 200:
    raise ValueError(
        "Request to slack returned an erro %s, the response is:\n%s"
        % (response.status_code, response.test)
    )
# adding a comment
# adding a comment
# adding another comment
# adding another comment
# adding another comment
# adding another comment
# adding another comment
