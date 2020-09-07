from pyecharts import options as opts

from pyecharts.charts import  *
from random import randint
page = Page()
def pie_base() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(['好评','差评'],
                                       [99,1])])
        .set_global_opts(title_opts=opts.TitleOpts(title="手机的好评与差评"))

        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    page.add(c)
    a=(
        Pie()
        .add("", [list(z) for z in zip(['好评','差评'],
                                       [99,1])])
        .set_global_opts(title_opts=opts.TitleOpts(title="手机的好评与差评"))

        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    page.add(a)
    b= (
        Pie()
            .add("", [list(z) for z in zip(['好评', '差评'],
                                           [99, 1])])
            .set_global_opts(title_opts=opts.TitleOpts(title="手机的好评与差评"))

            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    page.add(b)
    d = (
        Pie()
            .add("", [list(z) for z in zip(['好评', '差评'],
                                           [99, 1])])
            .set_global_opts(title_opts=opts.TitleOpts(title="手机的好评与差评"))

            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    page.add(d)


    return page


pie_base().render('good_or_bad.html')
