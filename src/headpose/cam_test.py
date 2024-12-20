from picamera2 import Picamera2

picam2 = Picamera2()

# 静止画モードの設定
#picam2.configure(picam2.create_still_configuration(main={"size": (640, 480)}))

# 画像をキャプチャ
picam2.start()
picam2.capture_file("test.jpg")
picam2.stop()