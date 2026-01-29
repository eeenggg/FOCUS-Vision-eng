from ultralytics import YOLO


model = YOLO('yolo11m.pt')

if __name__ == '__main__':
    print("开始训练日常生活物品模型...")


    model.train(
        data=r'F:\focus\FOCUS-WinterCamp-2026\config\common_obj.yaml',
        epochs=100,
        imgsz=640,
        batch=4,
        device='0',
        workers=0,
        name='train_common'  
    )