import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'

}

def suv():
    url = "http://www.515fa.com/che_22973.html"
    res = requests.get(url=url, headers=headers)
    res.encoding="utf-8"
    parse = etree.HTML(res.text)
    tr_list = parse.xpath('//div[@class="w_con"]/table/tbody/tr')[2:]
    data = []
    for i in tr_list:
        info_list = i.xpath("./td/text()")
        data.append(" ".join([j.strip() for j in info_list]))

    with open("data/data_suv1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def weather():
    res = requests.get("https://tianqi.2345.com/changsha/57687.htm",headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="seven-day"]/ul/li')
    data = []
    for li in li_list:
        day = li.xpath('./a/span[@class="how-day"]/text()')[0]
        date = li.xpath('./a/em/text()')[0]
        weather = li.xpath('./a/i/text()')[0]
        temperature = li.xpath('./a/span[@class="tem-show"]/text()')[0]
        print(day,date,weather,temperature)
        data.append( " ".join([day,date,weather,temperature]))

    with open("data/data_weather1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def movie():
    res = requests.get("http://127.0.0.1:5000/movie", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="indent"]//div[@class="pl2"]')
    data = []
    for li in li_list:
        name = li.xpath('./a/text()')[0]
        info = li.xpath('./p/text()')[0]
        score = li.xpath('.//span[@class="rating_nums"]/text()')[0]
        nums = li.xpath('.//span[@class="pl"]/text()')[0]
        name = name.split("/")[0].split()[0]
        info = info.split("(")[0]
        # print(name,info,score,nums)
        data.append(" ".join([name,info,score,nums]))

    with open("data/data_movie1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def book():
    res = requests.get("http://127.0.0.1:5000/book", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//ul[@class="list-col list-col2 list-summary s"]/li')
    data = []
    for li in li_list:
        name = li.xpath('./div[@class="info"]/h4/a/text()')[0].strip()
        score = li.xpath('./div[@class="info"]//span[@class="average-rating"]/text()')[0].strip()
        author = li.xpath('.//p[@class="author"]/text()')[0].strip().split("：")[1]
        classifi = li.xpath('.//p[@class="book-list-classification"]/text()')[0].strip().split(" /")[0]
        data.append(" ".join([name,score,author,classifi]))

    with open("data/data_book1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def phone():
    res = requests.get("https://top.zol.com.cn/compositor/57/cell_phone.html", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list"]/div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="rank__name"]/a/text()')[0].strip()
        price = li.xpath('.//div[@class="rank__price"]/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].strip()
        print(name,price,score)
        data.append("|".join([name,price, score, ]))

    with open("data/data_phone1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def computer():
    res = requests.get("http://127.0.0.1:5000/computer", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="brand_logo"]/p/a/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].strip()
        rate = li.xpath('.//div[@class="rank-list__cell cell-4"]/text()')[0].strip()

        print(name,score,rate)
        data.append("|".join([name, score,rate ]))

    with open("data/data_computer1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def air():
    res = requests.get("http://127.0.0.1:5000/air", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="rank__name"]/a/text()')[0].strip()
        price = li.xpath('.//div[@class="rank__price"]/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')
        if len(score) < 1:
            score = "无评分"
        else:
            score = score[0]

        print(name,price,score)
        data.append("|".join([name,price,score]))

    with open("data/data_air1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def fridge():
    res = requests.get("http://127.0.0.1:5000/fridge", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="brand_logo"]/p/a/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].strip()
        rate = li.xpath('.//div[@class="rank-list__cell cell-4"]/text()')[0].strip()

        print(name,score,rate)
        data.append("|".join([name, score,rate ]))
    with open("data/data_fridge1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def desktop():
    res = requests.get("http://127.0.0.1:5000/desktop", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="brand_logo"]/p/a/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].strip()
        rate = li.xpath('.//div[@class="rank-list__cell cell-4"]/text()')[0].strip()

        print(name,score,rate)
        data.append("|".join([name, score,rate ]))
    with open("data/data_desktop1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def huawei():
    res = requests.get("http://127.0.0.1:5000/huawei", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="rank__name"]/a/text()')[0].strip()
        price = li.xpath('.//div[@class="rank__price"]/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].strip()

        print(name,price,score)
        data.append("|".join([name,price, score ]))
    print(data)
    with open("data/data_huawei1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def camera():
    res = requests.get("http://127.0.0.1:5000/camera", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="rank__name"]/a/text()')[0].strip()
        price = li.xpath('.//div[@class="rank__price"]/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')
        if len(score) < 1:
            score = "无评分"
        else:
            score = score[0]

        print(name,price,score)
        data.append("|".join([name,price,score]))

    with open("data/data_camera1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def television():
    res = requests.get("http://127.0.0.1:5000/television", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="brand_logo"]/p/a/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].strip()
        rate = li.xpath('.//div[@class="rank-list__cell cell-4"]/text()')[0].strip()

        print(name,score,rate)
        data.append("|".join([name, score,rate ]))
    with open("data/data_television1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def people():
    res = requests.get("http://127.0.0.1:5000/people", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//table[@class="rank-table"]/tbody/tr')[1:]
    data = []
    for li in li_list:
        name = li.xpath('.//a[@class="cty"]/p/text()')[0].strip()
        nums = li.xpath('./td[3]/text()')[0].strip()
        rate = li.xpath('./td[4]/text()')[0].strip()
        area = li.xpath('./td[5]/text()')[0].strip()
        print(name,nums,rate,area)
        data.append("|".join([name,nums,rate,area ]))
    with open("data/data_people1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def mp3():
    res = requests.get("http://127.0.0.1:5000/mp3", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="brand_logo"]/p/a/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].strip()
        rate = li.xpath('.//div[@class="rank-list__cell cell-4"]/text()')[0].strip()

        print(name,score,rate)
        data.append("|".join([name, score,rate ]))
    with open("data/data_mp31.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

def headset():
    res = requests.get("http://127.0.0.1:5000/headset", headers=headers)
    parse = etree.HTML(res.text)
    li_list = parse.xpath('//div[@class="rank-list__item clearfix"]')
    data = []
    for li in li_list:
        name = li.xpath('.//div[@class="brand_logo"]/p/a/text()')[0].strip()
        score = li.xpath('.//div[@class="score clearfix"]/span/text()')[0].strip()
        rate = li.xpath('.//div[@class="rank-list__cell cell-4"]/text()')[0].strip()

        print(name,score,rate)
        data.append("|".join([name, score,rate ]))
    with open("data/data_headset1.txt", 'w', encoding="utf-8") as pp:
        pp.write("\n".join(data))

if __name__ == "__main__":
    phone()
