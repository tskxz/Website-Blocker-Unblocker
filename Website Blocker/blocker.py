Blue = "\33[34m"
Yellow = "\33[33m"
Green = "\33[32m"
none = "\33[0m"

def blocker():
    print(
        Blue + "\n\n\nType the url with www and without www\n\n Example: www.youtube.com youtube.com www.facebook.com facebook.com\n"" Another example: www.randomweb.com randomweb.com www.youcan_addmoresites.com\n\n\n" + none)
    import application
    application.block_website()


blocker()
