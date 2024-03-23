import requests
from bs4 import BeautifulSoup


def job_detail_scrapper(term):

    all_jobs = []
    url = f"https://berlinstartupjobs.com/skill-areas/{term}"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        },
    )

    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("li", class_="bjs-jlid")

    for job in jobs:
        company = job.find("a", class_="bjs-jlid__b").get_text()
        title = job.find("h4", class_="bjs-jlid__h").get_text()
        position = (
            job.find("div", class_="links-box")
            .get_text()
            .replace("\n", "")
            .replace("\t", " ")
        )
        description = (
            job.find("div", class_="bjs-jlid__description")
            .get_text()
            .replace("\t", "")
            .replace("\n", "")
        )
        link = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
        job_data = {
            "title": title,
            "company": company,
            "position": position.strip().replace(" ", ", "),
            "link": link,
            "description": description,
        }
        all_jobs.append(job_data)
    return all_jobs
