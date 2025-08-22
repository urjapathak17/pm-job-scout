from datetime import datetime
import json
import requests

class JobScraper:
    def __init__(self):
        self.jobs = []

    def scrape_wellfound(self):
        try:
            wellfound_jobs = [
                {
                    'title': 'Product Manager - Early Stage',
                    'company': 'TechStartup Inc',
                    'location': 'Remote',
                    'workType': 'Remote',
                    'experience': '2+ years',
                    'salary': '$80,000-120,000',
                    'source': 'Wellfound',
                    'description': 'Join our early-stage startup as first PM...',
                    'applyUrl': 'https://wellfound.com/jobs/...'
                }
            ]
            for job_data in wellfound_jobs:
                job = {
                    'id': len(self.jobs) + 1,
                    'postedDate': datetime.now().strftime('%Y-%m-%d'),
                    'verified': False,
                    **job_data
                }
                self.jobs.append(job)
            print(f"✅ Added {len(wellfound_jobs)} jobs from Wellfound")
        except Exception as e:
            print(f"❌ Wellfound scraping failed: {e}")

    def get_company_rating(self, company_name):
        company_ratings = {
            'Google': 4.4,
            'Microsoft': 4.2,
            'Amazon': 3.9,
            'Meta': 4.0,
            'Netflix': 4.1
        }
        return company_ratings.get(company_name, None)

    def run(self):
        self.scrape_wellfound()
        for job in self.jobs:
            job['companyRating'] = self.get_company_rating(job['company'])
        with open('public/data/jobs.json', 'w') as f:
            json.dump({'jobs': self.jobs}, f, indent=2)

def send_job_alerts():
    with open('public/data/jobs.json', 'r') as f:
        data = json.load(f)
    priority_jobs = [
        job for job in data['jobs'] 
        if 'senior' in job['title'].lower() 
        and job.get('visaSponsorship') 
        and job.get('verified')
    ]
    if priority_jobs:
        print(f"📧 Would send alert for {len(priority_jobs)} jobs")

def send_slack_alert(jobs):
    webhook_url = "YOUR_SLACK_WEBHOOK_URL"
    message = {
        "text": f"🚀 {len(jobs)} new PM jobs found!",
        "attachments": []
    }
    for job in jobs[:3]:
        attachment = {
            "color": "good",
            "fields": [
                {"title": job['title'], "value": job['company'], "short": True},
                {"title": "Location", "value": job['location'], "short": True},
                {"title": "Apply", "value": f"<{job['applyUrl']}|Apply Now>", "short": False}
            ]
        }
        message["attachments"].append(attachment)
    requests.post(webhook_url, json=message)
    print(f"📢 Sent Slack alert for {len(jobs)} jobs")

if __name__ == "__main__":
    scraper = JobScraper()
    scraper.run()
    send_job_alerts()

Add backend scraper.py file
