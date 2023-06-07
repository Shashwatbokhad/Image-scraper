import os
import requests
from bs4 import BeautifulSoup

url= "https://www.google.com/search?q=cat&tbm=isch&sxsrf=APwXEdfZxzvQOglsxjqEGJ4KCldb4q-TPw%3A1685895788758&source=hp&biw=1366&bih=625&ei=bLp8ZJ-RLL6VseMPgISt8AY&iflsig=AOEireoAAAAAZHzIfNfADnf8pH88pd-KLF1O0av6nM0R&ved=0ahUKEwif9_Wcg6r_AhW-SmwGHQBCC24Q4dUDCAc&uact=5&oq=dog&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQM6BwgjEOoCECc6BAgjECdQpA1YpBFg2hJoAXAAeACAAcQBiAGGA5IBAzAuMpgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img"
main_d = os.getcwd()
def image_scrapper(url,key):
    r = requests.get(url)
    htmldata = r.text
    soup = BeautifulSoup(htmldata, 'html.parser')
    k=0
    ##change directery
    try:
        directory = key + "images"
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        os.chdir(path)
        print(path)
    except:
        print("cannot create new folder ")
        pass

    for item in soup.find_all('img'):
        #print(item['src'])
        k=k+1
        name = key + str(k) + '.jpg'
        try:
            f = open(name,'wb')
            im = requests.get(item['src'])
            f.write(im.content)
            print("done saving ", name)

        except:
            pass

while(1):
    query = input("write the query for scrapper to scrape image: ")
    query = query.replace(' ','')
    url = "https://www.google.com/search?q="+ query +"&tbm=isch&sxsrf=APwXEdfZxzvQOglsxjqEGJ4KCldb4q-TPw%3A1685895788758&source=hp&biw=1366&bih=625&ei=bLp8ZJ-RLL6VseMPgISt8AY&iflsig=AOEireoAAAAAZHzIfNfADnf8pH88pd-KLF1O0av6nM0R&ved=0ahUKEwif9_Wcg6r_AhW-SmwGHQBCC24Q4dUDCAc&uact=5&oq=dog&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQM6BwgjEOoCECc6BAgjECdQpA1YpBFg2hJoAXAAeACAAcQBiAGGA5IBAzAuMpgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img"
    key = query
    image_scrapper(url,key)
    os.chdir(main_d)


