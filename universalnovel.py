import requests
from bs4 import BeautifulSoup

# URL halaman novel
novel_url = 'https://universalnovel.com/series/all-the-planes-knelt-and-begged-the-villainess-to-be-humane/'

# Mengirimkan permintaan HTTP ke halaman web dan mengambil konten HTML-nya
response = requests.get(novel_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Mencari daftar bab
chapter_list = soup.find('div', {'class': 'eplister eplisterfull'}).find_all('li')

# Loop melalui setiap bab dan mengambil teks dari setiap bab
with open('text.txt', 'w', encoding='utf-8') as f:
    for chapter in chapter_list:
        chapter_url = chapter.find('a')['href']
        chapter_title = chapter.find('div', {'class': 'epl-title'}).text
        print("Mengambil teks dari", chapter_url, "dengan judul:", chapter_title)
        
        # Mengirimkan permintaan HTTP ke halaman bab dan mengambil konten HTML-nya
        response = requests.get(chapter_url)
        html_content = response.text
        
        # Menguraikan struktur HTML dan menavigasi ke elemen div yang diinginkan
        soup = BeautifulSoup(html_content, 'html.parser')
        epcontent_div = soup.find('div', {'class': 'epcontent entry-content'})
        
        # Mengambil teks dari elemen div
        text = epcontent_div.text.strip()
        
        # Menampilkan teks yang diambil
        print(text)
        
        # Menyimpan teks ke dalam file
        f.write(chapter_title + '\n\n' + text + '\n\n')
