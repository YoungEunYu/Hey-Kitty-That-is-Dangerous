import cv2
import math
import numpy as np
from ultralytics import YOLO
from seaborn import color_palette
import os
import pygame as pygame
import datetime


def load_class_names(file_name):
    """
    Returns a list of class names read from the file `file_name`.

    Args:
        file_name (str): The path to the file containing the class names.

    Returns:
        List[str]: A list of class names.
    """

    with open(file_name, 'r') as f:
        class_names = f.read().splitlines()
    return class_names


def draw_bbox(frame, boxes, class_names, colors):
    """
    Draws bounding boxes with labels on the input frame.

    Args:
        frame (numpy.ndarray): The input image frame.
        boxes (List[Object]): List of bounding boxes.
        class_names (List[str]): List of class names.
        colors (List[Tuple[int]]): List of RGB color values.

    Returns:
        None
    """
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    

        # Extracting the class label and name
        cls = int(box.cls[0])
        class_name = class_names[cls]

        # Retrieving the color for the class
        color = colors[cls]

        # Drawing the bounding box on the image
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)

        # Formatting the confidence level and label text
        conf = math.ceil((box.conf[0] * 100)) / 100
        label = f'{class_name} ({conf}%)'

        # Calculating the size of the label text
        text_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
        # Calculating the coordinates for the background rectangle of the label
        rect_coords = x1 + text_size[0], y1 - text_size[1] - 3

        # Drawing the background rectangle and the label text
        cv2.rectangle(frame, (x1, y1), rect_coords, color, -1, cv2.LINE_AA)
        cv2.putText(frame, label, (x1, y1 - 2), 0, 1, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)


def run_yolo(model_name='web/src/yolo_assets/Models/v4.pt', source=0, prediction_type='video',
             class_path="web/src/yolo_assets/Classes/classes.txt",
             outdir='web/src/yolo_assets/Detections',
             web_app=False):
    """
    Performs object detection on an image or video.

    Args:
        model_name (str): The name of the model to use for object detection. Default is 'yolov8s.pt'.
        source (Union[str, int]): The path to the image or video file or webcam index. Default is 0 (webcam).
        prediction_type (str): The type of prediction to make. Valid values are 'image' and 'video'. Default is 'video'.
        class_path (str): The path to the file containing class names. Default is 'classes.txt'.
        outdir (str): The output directory or file name. Default is 'output'.
        web_app (bool): Whether the output is for a web application. Default is False.

    Returns:
        If `web_app` is True and `prediction_type` is 'video', it yields each frame with object detection results.
    """
    # Initializing the YOLO model
    model = YOLO(model_name)
    output_directory = os.path.dirname(outdir)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # Loading the class names from the file
    classes = load_class_names(class_path)
    n_classes = len(classes)
    #  Generating colors for each class
    colors = {}
    #  Generate a color palette
    for i in range(n_classes):
        color = tuple((np.array(color_palette('hls', n_classes)) * 255)[i])
        colors[i] = color

    # Initialize alert sound
    pygame.init()
    pygame.mixer.init()
    alarm_played = False
    pygame.mixer.music.load(os.path.abspath('web/src/yolo_assets/alarm2.mp3'))
    
    # Checking the prediction type
    if prediction_type == 'video':
        # Capturing the video from the source
        cap = cv2.VideoCapture(source)
        fps_camera = cap.get(cv2.CAP_PROP_FPS)
        target_fps = 10
        n = int(fps_camera / target_fps)
        frame_counter, not_detected = 0, 0

        while True:
            # Reading a frame from the video
            ret, frame = cap.read()
            if not ret:
                break

            if frame_counter % n == 0:
                outs = model(frame, task='detect', iou=0.6, conf=0.1, show=False, save_conf=True, classes=[0, 1], boxes=False)

                pred_classes = [classes[int(i.item())] for i in outs[0].boxes.cls]
                pred_bbox = [i.tolist() for i in outs[0].boxes.xywh]

                length = len(pred_classes)
                cat_boxes = []
                stove_boxes = []
                cat_flag, stove_flag = 0, 0

                for i in range(length):
                    if pred_classes[i] in ['cat']:
                        cat_boxes.append((round(pred_bbox[i][0]), round(pred_bbox[i][1]), round(pred_bbox[i][0] + pred_bbox[i][2]), round(pred_bbox[i][1] + pred_bbox[i][3])))
                        cat_flag = 1
                    elif pred_classes[i] in ['stove']:
                        stove_boxes.append((round(pred_bbox[i][0]), round(pred_bbox[i][1]), round(pred_bbox[i][0] + pred_bbox[i][2]), round(pred_bbox[i][1] + pred_bbox[i][3])))
                        stove_flag = 1

                # Setting alarm lasting time
                if alarm_played and (not cat_flag or not stove_flag):
                    not_detected += 1
                    if not_detected > 15:
                        pygame.mixer.music.stop()
                        not_detected = 0
                        alarm_played = False

                # Define the condition of alarm
                for cat_box in cat_boxes:
                    for stove_box in stove_boxes:
                        if ((cat_box[1] > stove_box[1] and cat_box[1] < stove_box[3]) or (cat_box[3] > stove_box[1] and cat_box[3] < stove_box[3])) and ((cat_box[0] > stove_box[0] and cat_box[0] < stove_box[2]) or (cat_box[2] > stove_box[0] and cat_box[2] < stove_box[2])):
                            if not alarm_played:
                                pygame.mixer.music.play(-1)  # play in a loop
                                alarm_played = True
                                # Save the frame as an image
                                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                                image_name = f"web/src/static/warnings/cat_alert_{timestamp}.jpg"
                                cv2.imwrite(image_name, frame)
                                frame = False
                                
            frame_counter += 1
            
            # Iterating over the detected objects
            for i, result in enumerate(outs):
                # Extracting the bounding box coordinates
                boxes = result.boxes
                draw_bbox(frame, boxes, classes, colors)


            # Yielding the frame if web_app is True
            if web_app:
                yield frame



if __name__ == '__main__':
    # Run yolo on an camera
    func = run_yolo()

    # Consume the generator to avoid unexpected behavior
    for frame in func:
        pass
