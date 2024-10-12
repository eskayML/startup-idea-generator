
import mimetypes
import os
import subprocess
import sys


from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.template import Template

subprocess.call("grep -R {} .".format(sys.argv[1]), shell=True, cwd="/home/user")

def template_access(request):
    response = Template.render(request, 'vulnerable/xss/form.html', globals())
    response.set_cookie(key='monster test', value='omo!')
    return response

def file_access(request):
    msg = request.GET.get('msg', '')
    return render(request, 'vulnerable/injection/file_access.html',
            {'msg': msg}


SECRET_KEY = "django-insecure-i2(f^4emukw6o$4k0a^14g@&lu#fa+)5yjj@$_r%)fwoac0wlv"
