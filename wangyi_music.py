import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}

sing_url = input('请输入你想下载的歌曲链接:')
url = sing_url.replace('/#', '')
response = requests.get(url=url, headers=headers)

html = etree.HTML(response.text)
music_label_list = html.xpath('//a[contains(@href,"/song?")]')

for music_label in music_label_list:
    href = music_label.xpath('./@href')[0]
    music_id = href.split('=')[1]
    music_name = music_label.xpath('./text()')[0]

    music_url = 'http://music.163.com/song/media/outer/url?id=' + music_id
    music = requests.get(music_url, headers=headers)
    try:
        with open('D:\桌面\music/%s.mp3' % music_name, 'wb') as file:
            file.write(music.content)
        print('《%s》 下载成功' % music_name)
    except:
        break

