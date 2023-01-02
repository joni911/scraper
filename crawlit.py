import requests, json, codecs
from bs4 import BeautifulSoup

for id in range(3424, 3478 + 1):
    try:
        sid = str(id)
        url = "https://inoveltranslation.com/chapters/" + sid
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        json_element = soup.select_one("#__NEXT_DATA__")
        json_text = json_element.get_text()
        data = json.loads(json_text)

        novel = data["props"]["pageProps"]["chapter"]["novel"]['id']
        title = data["props"]["pageProps"]["chapter"]["title"]
        volume = data["props"]["pageProps"]["chapter"]["volume"]
        chapter = data["props"]["pageProps"]["chapter"]["chapter"]

        # Mengubah tipe data volume dan chapter menjadi string
        volume = str(volume)
        chapter = str(chapter)

        # Menggabungkan string
        result = "Volume " + volume + " Chapter " + chapter
        
        if novel == 15:
            with codecs.open(result + " " +title+".txt", "w", "utf-8-sig") as file:
                # Menulis judul dan isi ke file
                file.write(result + " " +title + "\n\n")
                file.write(data["props"]["pageProps"]["chapter"]["content"])
        else:
            print('bukan 15')

            
        # Membuka file dengan mode write
        # with open(result + " " +title+".txt", "w") as file:
        #         # Menulis judul dan isi ke file
        #         file.write(result + " " +title + "\n\n")
        #         file.write(data["props"]["pageProps"]["chapter"]["content"])
        #         file.close()
        
    except Exception as e:
        print(e)
