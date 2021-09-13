'''
1.完成衣服销售数据的统计和分析
1.1计算总销售额
1.2计算平均每日销售数量
1.3 计算每个种类月销售量占比
'''
print("日期\t服装名称\t价格/件\t库存数量\t销售量/日")
print("1号\t羽绒服\t253.6\t500\t10")
print("2号\t牛仔裤\t86.3\t600\t60")
print("3号\t风衣\t96.8\t335\t43")
print("4号\t皮草\t135.9\t855\t63")
print("5号\tT恤\t65.8\t632\t63")
print("6号\t衬衫\t49.3\t562\t120")
print("7号\t牛仔裤\t86.3\t600\t72")
print("8号\t羽绒服\t253.6\t500\t69")
print("9号\t牛仔裤\t86.3\t600\t35")
print("10号\t羽绒服\t253.6\t500\t140")
print("11号\t牛仔裤\t86.3\t600\t90")
print("12号\t皮草\t135.9\t855\t24")
print("13号\tT恤\t65.8\t632\t45")
print("14号\t风衣\t96.8\t335\t25")
print("15号\t牛仔裤\t86.3\t600\t60")
print("16号\tT恤\t65.8\t632\t129")
print("17号\t羽绒服\t253.6\t500\t10")
print("18号\t风衣\t96.8\t335\t43")
print("19号\tT恤\t65.8\t632\t63")
print("20号\t牛仔裤\t86.3\t600\t60")
print("21号\t皮草\t135.9\t855\t63")
print("22号\t风衣\t96.8\t335\t60")
print("23号\tT恤\t65.8\t632\t58")
print("24号\t牛仔裤\t86.3\t600\t140")
print("25号\tT恤\t65.8\t632\t48")
print("26号\t风衣\t96.8\t335\t43")
print("27号\t皮草\t135.9\t855\t57")
print("28号\t羽绒服\t253.6\t500\t10")
print("29号\tT恤\t65.8\t632\t63")
print("30号\t风衣\t96.8\t335\t78")
print("==================================")
a=253.6*10+86.3*60+96.8*43+135.9*63+65.8*63+49.3*120+86.3*72+\
      253.6*69+86.3*35+253.6*140+86.3*90+135.9*24+65.8*45+96.8*25+86.3*60+\
      65.8*129+253.6*10+96.8*43+65.8*63+86.3*60+135.9*63+96.8*60+\
      65.8*58+86.3*140+65.8*48+96.8*43+135.9*57+253.6*10+65.8*63+96.8*78
print("总销售额：{0:.2f}".format(a))
b=10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+\
  48+43+57+10+63+78
print("平均每日销售数量：{0:.2f}".format(b/30))
yrf=10+69+140+10+10
nzk=60+72+35+90+60+60+140
fy=43+25+43+60+43+78
pc=63+24+63+78
ts=63+45+129+63+58+48+63
cs=120
print("羽绒服月销售占比：{0:.2%}".format(yrf/b))
print("牛仔裤月销售占比：{0:.2%}".format(nzk/b))
print("风衣月销售占比：{0:.2%}".format(fy/b))
print("皮草月销售占比：{0:.2%}".format(pc/b))
print("T恤月销售占比：{0:.2%}".format(ts/b))
print("衬衫月销售占比：{0:.2%}".format(cs/b))


