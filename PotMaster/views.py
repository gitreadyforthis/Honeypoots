from django.shortcuts import render
from graphos.renderers.gchart import LineChart
from graphos.sources.simple import SimpleDataSource


# Create your views here.


def mainpage(request):
    return render(request, 'base.html')

def dashboard(request):
    data = [
        ['Ports', 'ThreatIP', 'greg'],
        [2004, 1000, 400],
        [2005, 1170, 460],
        [2006, 660, 1120],
        [2007, 1030, 540]
    ]
    # DataSource object
    data_source = SimpleDataSource(data=data)
    # Chart object
    chart = LineChart(data_source)
    context = {'chart': chart}
    return render(request, 'dashboard.html', context)
