import cv2
from ultralytics import YOLO

# model = YOLO('models/last_best_vehicle_model.pt')
model = YOLO('models/old.pt')

transport_classes = {
    0: 'car',
    1: 'truck',
    2: 'bus',
    3: 'motorcycle'
}

colors = {
    'car': (0, 255, 0),      
    'truck': (255, 0, 0),   
    'bus': (0, 0, 255),      
    'motorcycle': (255, 255, 0)  
}

def process_frame(frame):
    cars_on_frame = 0
    results = model(frame, conf=0.3, verbose=False)

    for result in results[0].boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        class_id = int(class_id)

        if class_id in transport_classes:
            class_name = transport_classes[class_id]
            color = colors[class_name]
            label = f'{class_name}: {score:.2f}'

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return frame, cars_on_frame
