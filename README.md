# H.AI

# Python Version 3.10.10

## Folder information
1. code
    - image preprocessing
    - yolo webcam stream

2. model(customed yolov8n weight)
    - v1 : `stove, display, dresser, cat, closet, sofa` detection(4,444 Images)
    - v2 : `stove, cat` detection(3,091 Images)
    - v3 : `stove, cat` detection(6,097 Images)
    - v4 : `stove, cat` detection(5,415 Images)

3. Problem
    - v1 : `stove, display` class is confused
           `dresser, closet` class is unbalanced than other classes(Not enough images)
    - v2 : `stove` class data is not enough
    - v3 : gas stove image is confused with steel dishes → train with induction(black & 2 plates)
    - v4 : Model is confused with rear and side view of cats → train side and rear view of cats