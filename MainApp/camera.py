import cv2

class VideoCamera:
  def __init__(self, id):
    self.video = cv2.VideoCapture(id)

  def get_frame(self):
    s, img = self.video.read()
    r, jpg = cv2.imencode('.jpg', img)
    frame = jpg.tobytes()
    return frame