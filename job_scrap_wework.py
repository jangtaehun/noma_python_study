import requests
from bs4 import BeautifulSoup


def extract_jobs_we(term):
  url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={term}"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")

    for job_section in jobs:
      job_posts = job_section.find_all("li")
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all("a")
        anchor = anchors[1]
        title = anchor.find("span", class_="title")
        link = anchor["href"]
        company, kind, region = anchor.find_all("span", class_="company")
        position = job_section.find("h2").find("a").get_text()
        job_data = {
            "title": title.string.replace(",", " "),
            "company": company.string.replace(",", " "),
            "position": position,
            "link": f"https://remoteok.com{link}",
            "location": region.string.replace(",", " ")
        }
        results.append(job_data)
  else:
    print("Can't get jobs.")
  return results
