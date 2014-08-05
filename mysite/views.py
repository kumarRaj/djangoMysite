from django.http import HttpResponse
import datetime
from django.template import Template,Context
from django.template.loader import get_template
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now %s</html></body>" % now
    return HttpResponse(html)

def hello(request):
    t = get_template('home.html')
    html = t.render(Context())
    return HttpResponse(html)

def hours_ahead(request,offset):
    offset = int(offset)
    now = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template('hoursAhead.html')
    html = t.render(Context({"numberOfHours":offset,"time":now}))
    return HttpResponse(html)
