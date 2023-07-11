# H.AI

# Python Version 3.10.10

## Folder information
1. code
    - image preprocessing
    - yolo webcam stream

2. model(customed yolov8n weight)
    - v1 : `stove, display, dresser, cat, closet, sofa` detection(4,444 Images)
    - v2 : `stove, cat` detection(3,091 Images)

3. Problem
    - v1 : `stove, display` class is confused
           `dresser, closet` class is unbalanced than other classes(Not enough images)
    - v2 : 