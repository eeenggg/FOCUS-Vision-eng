import cv2
from ultralytics import YOLO


model_path = r'F:\focus\FOCUS-WinterCamp-2026\runs\detects\train_common2\weights\best.pt'
print(f"正在加载自定义模型: {model_path} ...")
model = YOLO(model_path)


image_path = r'F:\focus\FOCUS-WinterCamp-2026\test_custom.jpg'

print(f"正在读取图片: {image_path} ...")
frame = cv2.imread(image_path)


if frame is None:
    print(f"错误：无法读取图片，请检查路径是否正确：{image_path}")
    exit()


class_names = {0: 'Watch', 1: 'Cup', 2: 'Mouse', 3: 'Tissue'}


results = model.predict(frame, conf=0.5, verbose=False)


counts = {'Watch': 0, 'Cup': 0, 'Mouse': 0, 'Tissue': 0}

for box in results[0].boxes:
    cls_id = int(box.cls[0])
    if cls_id in class_names:
        name = class_names[cls_id]
        counts[name] += 1


annotated_frame = results[0].plot()


display_text = f"Cup:{counts['Cup']} Mouse:{counts['Mouse']} Watch:{counts['Watch']} Tissue:{counts['Tissue']}"


cv2.putText(annotated_frame, display_text, (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)


cv2.namedWindow("Custom Image Result", cv2.WINDOW_NORMAL)
cv2.imshow("Custom Image Result", annotated_frame)


save_path = 'result_custom.jpg'
cv2.imwrite(save_path, annotated_frame)
print(f"处理完成！结果已保存为: {save_path}")


cv2.waitKey(0)
cv2.destroyAllWindows()