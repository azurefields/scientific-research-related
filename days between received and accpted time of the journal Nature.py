import re
import requests
import time
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

receiveds = []
accepteds = []
urls = []

for i in range(7721, 7742, 1):
    if i < 7725:
        url = "https://www.nature.com/nature/volumes/561/issues/"+str(i)
    elif i < 7729:
        url = "https://www.nature.com/nature/volumes/562/issues/"+str(i)
    elif i < 7734:
        url = "https://www.nature.com/nature/volumes/563/issues/"+str(i)
    elif i < 7737:
        url = "https://www.nature.com/nature/volumes/564/issues/"+str(i)
    else:
        url = "https://www.nature.com/nature/volumes/565/issues/"+str(i)

    response = requests.get(url=url, headers=headers)
    time.sleep(1)
    data = response.text
    article = re.findall(r'<span data-test=\"article\.type\">Article</span>\n                        \n                        \n                            <span class=\"pl6 pr6\"> \| </span>\n                            <time datetime=\"....-..-..\"\n                                  itemprop=\"datePublished\">.. .* 20..</time>\n                        \n                        \n                    </p>\n                    \n                    <h3 class=\"mb10 extra-tight-line-height\" itemprop=\"name headline\">\n                         <a href=\"(/articles/s.....-...-....-.)\"', data)

    print(article)

    for art in article:
        url2 = "https://www.nature.com"+art
        response = requests.get(url=url2, headers=headers)
        time.sleep(0.5)
        print("2")
        data2 = response.text
        received = re.findall(r'<h4>Received</h4><p class="standard-space-below"><time datetime="(20..-..-..)">', data2)
        accepted = re.findall(r'<h4>Accepted</h4><p class="standard-space-below"><time datetime="(20..-..-..)">', data2)

        print(received, accepted)

        receiveds.append(received)
        accepteds.append(accepted)
        urls.append(url2)

file = pd.DataFrame({'received time': receiveds, 'accepted time': accepteds, 'url': urls})
file.to_csv('days between accepted time and received time of Nature Articles based on 104 sample.csv')
