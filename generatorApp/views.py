from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,redirect)
from django.http import HttpResponse
import random
import string
import base64


def home(request):
  if request.method=='POST':
    password=request.POST['pw']

    sample_string_bytes = password.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    # newpw=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(len(password)))
    return HttpResponse(base64_string)
  return render(request,'generatorApp/home.html')    