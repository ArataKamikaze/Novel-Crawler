from selenium.common.exceptions import NoSuchElementException

from src.file_writer import file_writer


def wuxiaworld(driver_path, chapters, url, name):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    DRIVER_PATH = driver_path

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_extension('chromedriver/uBlock-Origin.zip')
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

    for i in range(chapters):
        driver.get(url)

        content = driver.find_element(By.CLASS_NAME, 'reading-content', )
        check = False
        title = ""
        try:
           title = content.find_element(By.CLASS_NAME, "chapter-title").text
           print (title)
           check = True
        except NoSuchElementException:
            print("no title 1")
        if not check:
            try:
                title = content.find_element(By.CLASS_NAME, "cha-tit")
                title = title.find_element(By.TAG_NAME, "h3").text
                print(title)
                check = True
            except NoSuchElementException:
                print("no title 2")
        if not check:
            try:
                titles = content.find_elements(By.TAG_NAME, "p")
                for e in titles:
                    if e.text.startswith("Chapter"):
                        title = e.text
                        print(title)
                        check = True
            except NoSuchElementException:
                print("no title 3")
        if not check:
            try:
                title = content.find_element(By.ID, "wp-manga-current-chap").get_attribute("value")
                print(title)
                check = True
            except NoSuchElementException:
                print("no title 4")
        if not check:
            title = "unknown"
        if title.startswith("Chapter-"):
            title = "Chapter "+ title[8:]
        chapter = ["<h1>" + title + "</h1>\n"]
        paragraphs = content.find_elements(By.TAG_NAME, "p")

        for e in paragraphs:
            chapter.append(e.get_attribute('outerHTML')+"\n")
        file_writer(chapter, name)

        try:
            next = driver.find_element(By.CLASS_NAME,'btn.next_page')
        except NoSuchElementException:
            print("no next chapter")
            return

        url = next.get_attribute('href')