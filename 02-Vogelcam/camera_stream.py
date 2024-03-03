from flask import Flask, Response
import picamera
import threading
from io import BytesIO

# Initialize Flask
app = Flask(__name__)

# Camera settings
frame = None
lock = threading.Lock()

def capture_frames():
    global frame, lock
    with picamera.PiCamera() as camera:
        # Camera warm-up time
        camera.resolution = (640, 480)
        stream = BytesIO()
        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            with lock:
                frame = stream.read()
            stream.seek(0)
            stream.truncate()

@app.route('/video_stream')
def video_stream():
    """Route to stream video."""
    def generate():
        global frame, lock
        while True:
            with lock:
                if frame:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    """Video streaming home page."""
    return Response('<html><body><img src="/video_stream"></body></html>')

if __name__ == '__main__':
    # Start the frame capture thread
    t = threading.Thread(target=capture_frames)
    t.start()

    # Start Flask app
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
