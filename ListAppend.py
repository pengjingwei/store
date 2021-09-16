# 1)	将中国所有省会城市添加到上述列表中
# 2)	广东成为第二大发达城市，将广东排在上海前面
# 3)  统计前8城市的GDP总和，平均GDP
listCity = ["北京","上海","广州"]
gdp = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
listCity.extend(["天津 ","重庆","哈尔滨","长春","沈阳","呼和浩特","石家庄","乌鲁木齐","兰州","西宁","西安",\
                 "银川","郑州","济南","太原","合肥","长沙","武汉","南京","成都","贵阳","昆明","南宁","拉萨","杭州","南昌","福州",\
                 "台北","海口","香港","澳门"])
print("中国省会城市：",end="")
for i in range(len(listCity)):
    print(listCity[i],end=" ")
print("")
listCity[1],listCity[2]=listCity[2],listCity[1]
print("广东排在上海前面：",end=" ")
for i in range(len(listCity)):
    print(listCity[i],end=" ")
print("")
sum = 0
for i in range(len(gdp)):
    sum += gdp[i]
print("GDP总和:{0:.2f}".format(sum))
print("平均GDP:{0:.2f}".format(sum/8))
