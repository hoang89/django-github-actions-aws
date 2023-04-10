from django.http import HttpResponse


def home(request):
    text = """<h1>our mind blowing home page is up and running</h1>"""
    return HttpResponse(text)
