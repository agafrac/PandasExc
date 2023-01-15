import justpy as jp

import pandas
#import matplotlib.pyplot as plt
#from datetime import datetime
#from pytz import utc
#import matplotlib.pyplot as plt

data=pandas.read_csv("/Users/agnieszka/Desktop/pandas/reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude',
        align: 'center'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model',
        align: 'center'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 q-pa-md text-center")
    p1 = jp.QDiv(a=wp, text="These graphs represents course review analysis", classes="text-h5 q-pa-md")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average temperature"
    hc.options.xAxis.categories = list(day_average.index)
    hc.options.series[0].data = list(day_average["Rating"])
    return wp


jp.justpy(app)
