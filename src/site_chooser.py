import src.sites.ranobes as ranobes
import src.sites.wuxiaworld_site as wuxiaworld

def ranobes():
    print("Case 1 selected")

def function2():
    print("Case 2 selected")

def default():
    print("Value default")


def site_chooser(driver_path, chapters, url, name, site):
   match site:
        case "ranobes.net":
           ranobes.ranobes(driver_path, chapters, url, name)
        case "wuxiaworld.site":
            wuxiaworld.wuxiaworld(driver_path,chapters,url,name)
        case _:
            print("não foi possível encontrar o módulo desejado")



