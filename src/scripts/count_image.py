from ultralytics import YOLO
import cv2

print("正在加载 YOLOv11 模型...")
model = YOLO('yolo11n.pt')

image_path = 'test.jpg'

results = model.predict(image_path, save=True,conf=0.5)

person_count = 0
for box in results[0].boxes:
    if int(box.cls) == 0:
        person_count += 1

print("-" * 30)
print(f"检测完成！")
print(f"图片路径: {image_path}")
print(f"统计结果: 图中共有 {person_count} 个人")
print("-" * 30)


result_img = results[0].plot()
cv2.imshow("Detection Result", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()