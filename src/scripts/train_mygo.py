from ultralytics import YOLO

if __name__ == '__main__':

    print("正在加载 YOLOv11m (Medium) ...")
    model = YOLO('yolo11m.pt')

    print("MyGO!!!!!启动...")


    model.train(
        data='config/mygo.yaml',
        epochs=150,
        imgsz=640,
        device='0',


        batch=8,


        augment=True,
        mosaic=1.0,
        mixup=0.15,


        degrees=15.0,
        fliplr=0.5,
        scale=0.5,
        patience=0,
        workers=0
    )