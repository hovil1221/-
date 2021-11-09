def suv():
    with open("data/data_suv1.txt", 'r', encoding="utf-8") as pp:
        s = pp.read().split("\n")
    data = []
    for i in s:
        print(i.split(),len(i.split()))
        rank,name,car_type,sale_6,sale= i.split()
        if "奔驰" in car_type:
            continue
        data.append([name,car_type,sale_6,sale])
    data = sorted(data,key=lambda arr:int(arr[2]),reverse=True)[:5]
    data = [" ".join(i) for i in data]
    with open("data/data_suv2.txt", 'w', encoding="UTF-8") as pp:
        pp.write("\n".join(data))


def weather():
    with open("data/data_weather1.txt", 'r', encoding="utf-8") as pp:
        s = pp.read().split("\n")[1:]

    data = []
    for i in s:
        day,date,weather,temperature = i.split()
        mouth,d = map(int,date.split("/"))
        date = "%d月%d日"%(mouth,d)
        avg_temp = 0
        for i in temperature[:-1].split("~"):
            avg_temp += int(i)
        avg_temp /= 2
        data.append(" ".join([day,date,weather,str(avg_temp)]))

    with open("data/data_weather2.txt",'w',encoding="UTF-8") as pp:
        pp.write("\n".join(data))


def movie():
    with open("data/data_movie1.txt", 'r', encoding="utf-8") as pp:
        data = pp.read().split("\n")

    res = []
    for i in data:
        name,date,score,nums = i.split()
        nums = nums[1:][:-1]
        if int(nums.split("人")[0]) < 10000:
            continue
        res.append([name,date,score,nums])
    def sort_by_date(arr):
        date = arr[1]
        #date = 2021-03-21
        return int(date.replace("-",""))
    res = sorted(res,key=sort_by_date)
    res = [" ".join(i) for i in res]

    with open("data/data_movie2.txt", 'w', encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def book():
    with open("data/data_book1.txt", 'r', encoding="utf-8") as pp:
        data = pp.read().split("\n")

    res = []
    for i in data:
        if len(i.split()) != 4:
            continue
        name, score, author, classifi = i.split()
        # if float(score) < 9.0:
        #     continue
        res.append([name, score, author, classifi])
    def sort_key(arr):
        score = arr[1]
        return float(score)
    res = sorted(res,key=sort_key)
    res = [" ".join(i) for i in res]

    with open("data/data_book2.txt", 'w', encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def phone():
    with open("data/data_phone1.txt", "r", encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    for i in data:
        name,price,score = i.split("|")
        name = name.split("（")[0]
        price = price[1:]
        score = score[:-1]
        if float(score) < 9.2:
            continue
        res.append("|".join([name,price,score]))
    # print(res)
    with open("data/data_phone2.txt", "w", encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def computer():
    with open("data/data_computer1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    sum_rate = 0
    for i in data:
        name,score,rate = i.split("|")
        rate = rate[:-1]
        if len(rate) < 1:
            continue
        if float(rate) < 2:
            continue
        sum_rate += float(rate)
        res.append("|".join([name,score,rate]))
    res.append("其它|70分|%.1f"%(100-sum_rate))
    print(res)
    with open("data/data_computer2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def air():
    with open("data/data_air1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    for i in data:
        name,price,score = i.split("|")
        name = name.split("/")[0]
        price = price[1:]
        if score == "无评分" :
            continue
        if float(price) > 10000:
            continue
        res.append("|".join([name,price,score]))
    res = res[:5]
    with open("data/data_air2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def fridge():
    with open("data/data_fridge1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    sum_rate = 0
    for i in data:
        name,score,rate = i.split("|")
        rate = rate[:-1]
        if len(rate) < 1:
            continue
        if float(rate) < 2:
            continue
        sum_rate += float(rate)
        res.append("|".join([name,score,rate]))
    res.append("其它|70分|%.1f"%(100-sum_rate))
    print(res)
    with open("data/data_fridge2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def desktop():
    with open("data/data_desktop1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    sum_rate = 0
    for i in data:
        name,score,rate = i.split("|")
        rate = rate[:-1]
        if len(rate) < 1:
            continue
        if float(rate) < 1:
            continue
        sum_rate += float(rate)
        res.append("|".join([name,score,rate]))
    res.append("其它|70分|%.1f"%(100-sum_rate))
    print(res)
    with open("data/data_desktop2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def huawei():
    with open("data/data_huawei1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    for i in data:
        name,price,score = i.split("|")
        name = name.split('（')[0]
        price = price[1:]
        score = score[:-1]
        if "产品" in price:
            continue
        if int(price) >10000:
            continue
        res.append("|".join([name,price,score]))
    res = sorted(res,key=lambda x:int(x.split("|")[1]))
    print(res)
    with open("data/data_huawei2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def camera():
    with open("data/data_camera1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    for i in data:
        name,price,score = i.split("|")
        # name = name.split("/")[0]
        if score == "无评分" :
            continue
        score = score[:-1]
        price = price[1:]

        res.append("|".join([name,price,score]))
    res = sorted(res,key=lambda x:float(x.split("|")[2]))[-5:]
    with open("data/data_camera2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def television():
    with open("data/data_television1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    sum_rate = 0
    for i in data:
        name,score,rate = i.split("|")
        rate = rate[:-1]
        if len(rate) < 1:
            continue
        if float(rate) < 2:
            continue
        sum_rate += float(rate)
        res.append("|".join([name,score,rate]))
    res.append("其它|70分|%.1f"%(100-sum_rate))
    print(res)
    with open("data/data_television2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def people():
    with open("data/data_people1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    for i in data:
        name,nums,rate,area = i.split("|")
        nums = nums.replace(",","")
        rate = rate[:-1]
        res.append("|".join([name,nums,rate,area]))
    print(res)
    res = res[:10]
    res = sorted(res,key=lambda x:int(x.split("|")[1]))
    with open("data/data_people2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def mp3():
    with open("data/data_mp31.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    sum_rate = 0
    for i in data:
        name,score,rate = i.split("|")
        rate = rate[:-1]
        if len(rate) < 1:
            continue
        if float(rate) < 2:
            continue
        sum_rate += float(rate)
        res.append("|".join([name,score,rate]))
    res.append("其它|70分|%.1f"%(100-sum_rate))
    print(res)
    with open("data/data_mp32.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

def headset():
    with open("data/data_headset1.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    sum_rate = 0
    for i in data:
        name,score,rate = i.split("|")
        rate = rate[:-1]
        if len(rate) < 1:
            continue
        if float(rate) < 1:
            continue
        sum_rate += float(rate)
        res.append("|".join([name,score,rate]))
    res.append("其它|70分|%.1f"%(100-sum_rate))
    print(res)
    with open("data/data_headset2.txt","w",encoding="UTF-8") as pp:
        pp.write("\n".join(res))

if __name__ == "__main__":
    # headset()
    with open("data/data_headset2.txt","r",encoding="UTF-8") as pp:
        data = pp.read().split("\n")
    res = []
    for i in data:
        a,b,c= i.split("|")
        # if int(b) > 10000:
        #     continue
        res.append("{value: %s, name: '%s'},"%(c,a))
    print("\n".join(res))
    # a = [1400050000,1354051854,326766748,266794980,210867954,200813818,195875237,166368149,143964709,130759074]
    # res = []
    # for i in range(len(a)-1,-1,-1):
    #     res.append(str(a[i]))
    # print(",".join(res))
