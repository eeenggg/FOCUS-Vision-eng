import cv2
from ultralytics import YOLO


print("正在加载模型...")
model = YOLO('yolo11n.pt')


video_path = r'F:\focus\FOCUS-WinterCamp-2026\test_video.mp4'
cap = cv2.VideoCapture(video_path)


w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('output_result.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))


cv2.namedWindow("Video People Counting", cv2.WINDOW_NORMAL)

print(f"开始处理视频: {video_path}")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("视频处理结束")
        break


    results = model.predict(frame, conf=0.5, classes=[0], verbose=False)


    person_count = len(results[0].boxes)

    print(f"当前帧人数: {person_count}")


    annotated_frame = results[0].plot()


    text = f"People Count: {person_count}"
    cv2.putText(annotated_frame, text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 5)


    cv2.imshow("Video People Counting", annotated_frame)
    out.write(annotated_frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("处理完成！结果已保存为 output_result.mp4")