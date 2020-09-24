import requests
from bs4 import BeautifulSoup
from art import text2art
from colorama import init
from termcolor import colored
import datetime


Scraped_Links = []


def m3u_Creator():
    x = datetime.datetime.now()

    print("[*]Creating m3u file..........")
    m3u_creator = open(f"{x.strftime('%d-%m-%y_%I-%M-%S %p')} IPTV.m3u8", "a", encoding="utf-8")
    for links in Scraped_Links:
        m3u_creator.write(f"{links}\n")

    print("[*]Created m3u File!")

init()
def random_iptv(no):
 page_no = 1
 for i in range(no):
    print(f"{page_no}/{no}")
    url = f"https://streamtest.in/logs/page/{str(page_no)}"
    result = requests.get(url).text
    soup = BeautifulSoup(result, "html.parser")
    scraped_links = soup.find_all('div',{'class':'url is-size-6'})

    for link in scraped_links:
        Scraped_Links.append(link.text)

    page_no = page_no +1


art= text2art("IPTV Scraper")
print(colored(art,"cyan"))
print(colored("Developed By Henry Richard J","blue"))

no_of_pages_to_scrape = int(input("How many pages to scrape: "))

random_iptv(no_of_pages_to_scrape)
m3u_Creator()
