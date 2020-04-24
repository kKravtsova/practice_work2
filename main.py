import cx_Oracle
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import chart_studio
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard

chart_studio.tools.set_credentials_file(username='kKravtsova', api_key='ZsoDFDqUDYzaPIAtQscH')
con = cx_Oracle.connect('test/passtest@//localhost:1521/xe')
cursor = con.cursor()


def fileId_from_url(url):
    url_raw = url.split('/')
    cleared = [s.strip('~') for s in url_raw]  # remove the ~
    nickname = cleared[3]
    id = cleared[4]
    fileId = nickname + ':' + id
    return fileId


# ----query1------
request_1 = """
select DESTINATION.DESTINATION,COUNT(*) as cnt
from PRODUCT_DETAILS
join DESTINATION on DESTINATION.DESTINATION=PRODUCT_DETAILS.DESTINATION_CODE
group by DESTINATION.DESTINATION
order by COUNT(*) desc
FETCH FIRST 10 ROWS ONLY;
"""

cursor.execute(request_1)

x_request_1 = list()
y_request_1 = list()

for DESTINATION_name, cnt in cursor:
    x_request_1.append(cnt)
    y_request_1.append(DESTINATION_name)
    print(x_request_1)
    print(y_request_1)

# ----end query1-----
# ----query2------
request_2 = """
select DISTRIBUTION_CHANNEL,COUNT(*)
from PRODUCT_DETAILS
GROUP BY DISTRIBUTION_CHANNEL;
"""

cursor.execute(request_2)

x_request_2 = list()
y_request_2 = list()

for DISTRIB_CHAN, cnt in cursor:
    x_request_2.append(cnt)
    y_request_2.append(DISTRIB_CHAN)

# ----end query2-----
# ----query3------

request_3 = """
select DESTINATION.DESTINATION,max(COMMISION)
from PRODUCT_DETAILS
join DESTINATION on DESTINATION.DESTINATION=PRODUCT_DETAILS.DESTINATION_CODE
group by DESTINATION.DESTINATION
having max(COMMISION) > 150;
"""

cursor.execute(request_3)

x_request_3 = list()
y_request_3 = list()

for DESTIN_1,max_value in cursor:
    x_request_3.append(ESTIN_1)
    y_request_3.append(max_value)

# ----end query3-----
bar = go.Bar(
    y=x_request_1,
    x=y_request_1
)
graph_request_1 = py.plot([bar], auto_open=False, filename='request_1')

pie = go.Pie(
    labels=x_request_2,
    values=y_request_2
)
graph_request_2 = py.plot([pie], auto_open=False, filename='request_2')

scatter = go.Scatter(
    x=x_request_3,
    y=y_request_3
)
graph_request_3 = py.plot([scatter], auto_open=False, filename='request_3')

cursor.close()
con.close()

# dashboard creation ---------------------------------------------------

MyBoard1 = dashboard.Dashboard()
dia_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(graph_request_1),
    'title': 'Запит 1: вивести топ 10 країн з максимальною відвідуваносю'
}
dia_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(graph_request_2),
    'title': 'Запит 2: вивести відсоток онлайн та офлайн страхувань',

}
dia_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_from_url(graph_request_3),
    'title': 'Запит 3: розподіл максимальної комісії за країною,де комісія більше за 150'
}

MyBoard1.insert(dia_1)
MyBoard1.insert(dia_2, 'below', 1)
MyBoard1.insert(dia_3, 'right', 2)

py.dashboard_ops.upload(MyBoard1, 'LAB2_Kravtsova')
