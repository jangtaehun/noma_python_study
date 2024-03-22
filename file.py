import csv


def save_wework(keyword, jobs_db):
    file = open(f"wework_{keyword}.csv", "w", encoding="CP949")
    writter = csv.writer(file)
    writter.writerow(
        ["Title", "Company", "Position", "url", "location"]
    )  # writerow는 list를 넣어줘야 한다.
    for job in jobs_db:
        writter.writerow(job.values())
    file.close()


def save_web3(keyword, jobs_db):
    file = open(f"web3_{keyword}.csv", "w", encoding="CP949")
    writter = csv.writer(file)
    writter.writerow(["Title", "Company", "Position", "url"])
    for job in jobs_db:
        writter.writerow(job.values())
    file.close()


def save_berlin(keyword, jobs_db):
    file = open(f"berlin_{keyword}.csv", "w", encoding="utf-8")
    writter = csv.writer(file)
    writter.writerow(["Title", "Company", "Position", "url", "description"])
    for job in jobs_db:
        writter.writerow(job.values())
    file.close()
