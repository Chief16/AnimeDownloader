import requests
from bs4 import BeautifulSoup

while True:
    user_inp = input("Enter name of anime : ").lower()
    user_inp1 = user_inp.replace(" ","-")

    url = (f"https://animekisa.tv/{user_inp1}")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.title.text
    if title != "AnimeKisa: Find & Watch Anime, Subbed & Dubbed":
        a = soup.find_all('div',class_='centerv')[1].get_text()
        print(f"There are total {a} episodes available of {user_inp1}")
    else:
        print("We were unable to find...")
        break

    ep_inp = int(input("Enter number of Episode to download : "))
    if ep_inp > int(a):
        print("This episode isn't out yet")
        break

    url1 = (f"https://animekisa.tv/{user_inp1}-episode-{ep_inp}")
    r = requests.get(url1)
    soup = BeautifulSoup(r.text, 'html.parser')
    b = soup.prettify()

    with open('text2.txt','w+') as wf:
        wf.write(b)

    def check_if_string_in_file(file_name, string_to_search):
        with open(file_name, 'r') as read_obj:
            for line in read_obj:
                if string_to_search in line:
                    pure_link = line.strip()
                    link1 = pure_link[20:-2]
                    downloadUrl = link1.replace('load.php', 'download')
                    print(f"\nDOWNLOAD link of {user_inp1} episode {ep_inp} : {downloadUrl}")
                    print(f"Watch {user_inp1} {ep_inp} ONLINE : {link1}")

    check_if_string_in_file("text2.txt","var VidStreaming")
    break 

print("-----------------")