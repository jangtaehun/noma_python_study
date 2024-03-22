import requests
from bs4 import BeautifulSoup


def extract_jobs_web3(term):
  url = f"https://web3.career/{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  results = []

  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # find_all은 list를 반환하기 때문에 for loop를 통해 광고를 제거
    for tr in soup.find_all('tr', class_="border-paid-table"):
      tr.decompose()
    jobs = soup.find_all('tr', class_="table_row")

    for job in jobs:
      table = job.find_all("td")[0]
      table_detail = table.find("div", class_="job-title-mobile")

      link = table_detail.find("a")["href"].strip()
      title = table_detail.get_text().strip()
      company = job.find_all("td")[1].get_text().strip()

      positions = job.find_all("td")[-1]
      total_position = positions.find_all("a")
      position_list = []
      for position_detail in total_position:
        position_list.append(position_detail.string.strip())

      position = ", ".join(position_list)

      job_data = {
          "title": title,
          "company": company,
          "position": position,
          "link": f"https://remoteok.com{link}"
      }
      results.append(job_data)
  else:
    print("Can't get jobs.")
  return results
