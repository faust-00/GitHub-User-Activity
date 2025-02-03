import requests
import argparse

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return f"Error: User '{username}' not found."
    else:
        print(f"Error: {response.status_code}")
        return []


def display_activity(events):
    if not events:
        print("No activity found.")
        return

    for event in events[:5]:  # So'nggi 5 ta faoliyatni ko'rsatish
        event_type = event['type']
        repo_name = event['repo']['name']
        created_at = event['created_at']

        if event_type == 'CreateEvent':
            print(f"Created a new repository '{repo_name}' on {created_at}")
        elif event_type == 'PushEvent':
            commits = event['payload']['commits']
            commit_count = len(commits)
            print(f"Pushed {commit_count} commit(s) to {repo_name} on {created_at}")
        else:
            print(f"Event: {event_type} occurred in {repo_name} on {created_at}")

def main():
    parser = argparse.ArgumentParser(description="Fetch recent GitHub activity")
    parser.add_argument('username', type=str, help="GitHub username")
    args = parser.parse_args()

    events = fetch_activity(args.username)
    display_activity(events)

if __name__ == "__main__":
    main()


