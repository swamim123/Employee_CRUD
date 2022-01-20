from django.http import HttpResponse


def index(request):
    return HttpResponse('''<h1>My Bookmarked Website</h1> <a href="https://www.tutorialspoint.com/django/django_environment.htm"> django code with swami </a><br>
    <a href="https://www.google.co.in/?pli=1"> Google</a><br>
    <a href="https://www.youtube.com/"> YouTube</a><br>
    <a href="https://drive.google.com/drive/folders/10dpBBd3gbDG2Wfkw_pKRayOZkgLxi7Wj">Drive Code</a><br>
    <a href="https://www.edureka.co/blog/interview-questions/python-interview-questions/#WhatarethekeyfeaturesofPython?">Python Interview Question Answer</a>''')