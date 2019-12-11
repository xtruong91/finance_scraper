import shutil
import schedule
import time

from scraper import USScraper

DATA_DIR = "../finance_data/"


class Scraper():

    def __init__(self):
        self.us = USScraper()

    def clean_all(self):
        shutil.rmtree(DATA_DIR, ignore_errors=True)

    def scrape_all(self):
        self.us.scrape()


def job(app):
    app.clean_all()
    app.scrape_all()


def main():
    app = Scraper()
    job(app)
    schedule.every().day.at("08:00").do(job, app)
    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == '__main__':
    main()
