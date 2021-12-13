import requests
import cloudscraper
from selenium.common.exceptions import NoSuchElementException


def file_writer(chapter, name):
    try:
        with open("output"):
            with open("output/" + name + ".html", 'a+', encoding="utf-8") as textfile:
                for e in chapter:
                    textfile.write(e)
                    print("true")

    except IOError:
        with open("output/" + name + ".html", 'a+', encoding="utf-8") as textfile:
            for e in chapter:
                textfile.write(e)


def pageGetter(driver_path, chapters, url, name):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    DRIVER_PATH = driver_path

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")


    for i in range(chapters):

        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

        #driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get(url)
        print(driver.page_source)

        text = driver.find_elements(By.CLASS_NAME, 'h4.title', )

        chapter = []

        for e in text:
            chapter = ["<h1>" + e.text.split("\n")[0] + "</h1>\n"]
        text = driver.find_element(By.ID, 'arrticle', )
        text = text.find_elements(By.TAG_NAME,"p" )
        for e in text:
            chapter.append(e.get_attribute('outerHTML')+"\n")
        file_writer(chapter, name)

        try:
            text = driver.find_element(By.ID,'next')
        except NoSuchElementException:
            return

        url = text.get_attribute('href')