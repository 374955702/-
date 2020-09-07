from pyecharts.charts import Bar
from pyecharts import options as opts

from pyecharts import options as opts
from pyecharts.charts import Graph, Page
from pyecharts.render import make_snapshot

# from snapshot_phantomjs import snapshot

bar = Bar()
bar.add_xaxis(["iPhone11", "华为mate30", "小米10", "三星s10"])
bar.add_yaxis("好评率", [99, 98, 96, 92])

bar.set_global_opts(title_opts=opts.TitleOpts(title="手机率排行"))
bar.render()
