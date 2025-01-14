import os
from datetime import datetime, timedelta

start = datetime(2025, 1, 1)

for i in range(100):
    date = start + timedelta(days=i)

    for j in range(3):  # add 3 more per day
        with open("activity.txt", "a") as f:
            f.write(f"Extra {i}-{j}\n")

        os.system("git add activity.txt")

        d = date.strftime("%Y-%m-%dT12:00:00")
        os.environ["GIT_AUTHOR_DATE"] = d
        os.environ["GIT_COMMITTER_DATE"] = d

        os.system(f'git commit -m "Extra contribution {i}-{j}"')

print("Done!")
