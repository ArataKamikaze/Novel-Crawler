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
