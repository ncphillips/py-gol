import os
import requests
import json

def main():
    slack_url = os.environ["PINGPONGURL"]
    repo_url = "https://github.com/mittonface/py-gol"
    text = "All of the tests are passing on %s. This will not stand." % repo_url

    r = requests.post(slack_url, data=json.dumps({'text': text,}))

if __name__ == "__main__":
    main()
