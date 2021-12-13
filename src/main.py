import pageGetter
chapter_number = 3
DRIVER_PATH = 'chromedriver/chromedriver.exe'
url = "https://ranobes.net/read-572431.html"
filename = "teste_apostrofo"
pageGetter.pageGetter(DRIVER_PATH, chapter_number, url, filename)