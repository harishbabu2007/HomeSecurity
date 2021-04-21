from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from .camera import VideoCamera

# Create your views here.
def index(request):
  if request.user.is_authenticated:
    return render(request, 'MainApp/index.html')
  return redirect("/login")

def gen(camera):
  while 1:
    frame = camera.get_frame()
    yield(b'--frame\r\n'
          b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
  if request.user.is_authenticated:
    return StreamingHttpResponse(gen(VideoCamera(0)), content_type='multipart/x-mixed-replace; boundary=frame')
  return redirect("/login")