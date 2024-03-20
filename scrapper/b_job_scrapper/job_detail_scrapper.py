import requests
from bs4 import BeautifulSoup


# 세부적인 job data 추출
class Job_detail_scrapper:

    # list를 전역변수로 선언
    global all_jobs
    all_jobs = []

    def __init__(self, url, skills):
        self.url = url
        self.skills = skills

    def get_jobs(self):
        for skill in self.skills:
            url = f"https://berlinstartupjobs.com/skill-areas/{skill}"

            response = requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                },
            )

            soup = BeautifulSoup(response.content, "html.parser")
            jobs = soup.find_all("li", class_="bjs-jlid")

            for job in jobs:
                title = job.find("a", class_="bjs-jlid__b").get_text()
                position = job.find("h4", class_="bjs-jlid__h").get_text()
                description = job.find("div", class_="bjs-jlid__description").get_text()
                link = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
                job_data = {
                    "title": title,
                    "position": position,
                    "description": description,
                    "link": link,
                }
                all_jobs.append(job_data)
        return all_jobs
