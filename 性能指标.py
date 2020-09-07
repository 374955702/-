from pyecharts.charts import Bar
from pyecharts.charts import Line

# 日期作为x轴/横轴
x_function = [
    '速度', '拍照','外观','服务','电池','音效'
]

# 各城市确诊病例数作为y轴数据
y_iPhone11 = [90, 31, 23, 70, 90, 93]
y_mate30=[73,52,61,40,45,98]
y_小米10=[83,75,31,51,77,66]
y_三星s10=[76,87,67,88,76,44]


bar=Bar()

bar.add_xaxis(x_function) # 添加x轴数据

bar.add_yaxis('iphone11',y_iPhone11) # 添加y轴数据
bar.add_yaxis('mata30',y_mate30)
bar.add_yaxis('小米10',y_小米10)
bar.add_yaxis('三星S10',y_三星s10)


bar.render('性能指标.html')