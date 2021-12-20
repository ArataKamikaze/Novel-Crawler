from selenium.common.exceptions import NoSuchElementException

from src.file_writer import file_writer


def ranobes(driver_path, chapters, url, name):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    DRIVER_PATH = driver_path

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    for i in range(chapters):
        #driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get(url)


        text = driver.find_elements(By.CLASS_NAME, 'h4.title', )

        chapter = []

        for e in text:
            chapter = ["<h1>" + e.text.split("\n")[0] + "</h1>\n"]
            print(e.text.split("\n")[0])
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