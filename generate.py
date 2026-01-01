import os
from datetime import datetime, timedelta

start = datetime(2025, 1, 1)

for i in range(100):
    date = start + timedelta(days=i)

    with open("activity.txt", "a") as f:
        f.write(f"Contribution {i}\n")

    os.system("git add activity.txt")

    d = date.strftime("%Y-%m-%dT12:00:00")
    os.environ["GIT_AUTHOR_DATE"] = d
    os.environ["GIT_COMMITTER_DATE"] = d

    os.system(f'git commit -m "Contribution {i}"')

print("Done!")
