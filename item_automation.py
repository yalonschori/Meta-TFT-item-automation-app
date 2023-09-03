from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from collections import Counter

soup_content = ""


def get_webscrape_data():
    global soup_content
    url = "https://www.metatft.com/comps"
    os.environ["PATH"] += r"E:/Yalon Personal/CODE STUDIES"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-urlfetcher-cert-requests")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--ignore-ssl-errors")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url=url)
    driver.implicitly_wait(5)
    root_div = driver.find_element(By.ID, "root")
    content = root_div.get_attribute("innerHTML")
    soup = BeautifulSoup(content, "html.parser")
    soup_content = soup


def webscrape_items():
    global soup_content
    get_webscrape_data()
    item_names = []
    items_images = soup_content.findAll("img", attrs={"class": "Item_img"})
    for item in items_images:
        item_name = item.get("alt", "")
        item_names.append(item_name)

    word_counter = Counter(item_names)
    most_common_items = word_counter.most_common(6)
    return most_common_items


def webscrape_champion():
    global soup_content
    champion_names = []
    champion_images = soup_content.findAll("img", attrs={"class": "Unit_img"})
    for champion in champion_images:
        champion_name = champion.get("alt", "")
        cleared_name = champion_name.replace("TFT9_", "")
        champion_names.append(cleared_name)

    word_counter = Counter(champion_names)
    most_common_champions = word_counter.most_common(6)
    return most_common_champions
