# import the necessary modules
import time
from datetime import datetime as dt
from termcolor import colored, cprint


website_list = list(map(str, input("Enter the url to block/unblock: ").strip().split()))
blockedwebsites = open("websites_blocked.txt", "w+")
blockedwebsites.read()
blockedwebsites.seek(0)
blockedwebsites.write(str(website_list))
blockedwebsites.close()


def block_website():
    while True:
        with open(hosts, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
            cprint('Blocked!', 'yellow', attrs=['blink'])
            time.sleep(5)


def unblock_website():
    with open(hosts, "r+") as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            global website_list
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()
        cprint('Unblocked!', 'yellow', attrs=['blink'])


# block
redirect = "127.0.0.1"

# Hosts file to block the sites
hosts = "/etc/hosts"

