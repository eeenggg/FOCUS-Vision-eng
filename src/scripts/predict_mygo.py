from ultralytics import YOLO
import cv2


model_path = r'F:\focus\FOCUS-WinterCamp-2026\runs\detects\train9\weights\best.pt'

model = YOLO(model_path)


image_path = r'F:\focus\FOCUS-WinterCamp-2026\src\datasets\mygo_data\mygo66.jpg'


print(f"正在识别：{image_path} ...")

results = model.predict(
    image_path,
    save=True,
    conf=0.15,
    iou=0.6,
    agnostic_nms=True
)




result_img = results[0].plot()
cv2.imshow("MyGO Final", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()