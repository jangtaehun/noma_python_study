from job_scrapper import Job_scrapper
from job_detail_scrapper import Job_detail_scrapper

# 회사 이름, 직무 제목, 설명 및 직무 링크

url = "https://berlinstartupjobs.com/engineering/"
skills = ["python", "typescript", "javascript", "rust"]

job_scrap = Job_scrapper(url, skills)
print(job_scrap.get_jobs())
print("\n\n")
detail = Job_detail_scrapper(url, skills)
print(detail.get_jobs())
