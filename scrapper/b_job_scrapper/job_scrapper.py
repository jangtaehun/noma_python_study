import requests
from bs4 import BeautifulSoup


# page 갯수 추출
class Get_pages:

    def __init__(self, url):
        self.url = url

    def get_pages(self):
        response = requests.get(
            self.url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            },
        )
        soup = BeautifulSoup(response.content, "html.parser")
        pages = soup.find("ul", class_="bsj-nav")
        page = pages.find_all("a")[:-1]
        return len(page)


# page에서 job data 추출
class Job_scrapper(Get_pages):

    # list를 전역변수로 선언
    global all_jobs
    all_jobs = []

    def __init__(self, url, skills):
        super().__init__(url)  # Get_pages 클래스의 __init__ 메서드 호출
        self.url = url
        self.skills = skills
        self.pages = self.get_pages()  # get_pages() 메서드 호출하여 페이지 수 얻기

    def get_jobs(self):
        for page in range(1, self.pages + 2):
            url = f"https://berlinstartupjobs.com/engineering/page/{page}"

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
