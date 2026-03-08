import requests
from bs4 import BeautifulSoup


def search_jobs(skill):

    url = f"https://www.indeed.com/jobs?q={skill}&l="

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job in soup.select("h2.jobTitle span")[:5]:
        jobs.append(job.text)

    return jobs