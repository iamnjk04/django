from django.http import HttpResponse
def index(request):
    return HttpResponse('''<h1>Heading 1:<br>I am NJK</h1>
    <h2>nabin.jk7512@gmail.com</h2>
    <a href="https://www.linkedin.com/in/nabin-jung-kunwar-897a4622a/">LinkedIn</a>''')
def About(request):
    return HttpResponse('''<h1>About me is NJK</h1><h2>I live in KTM</h2>
    <a href="https://github.com/iamnjk04">GitHub</a>''')