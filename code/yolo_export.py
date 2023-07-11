from ultralytics import YOLO

model =YOLO("C:/dev/github/Playdata-Final-Project/model/v2.pt")  # load a custom trained

# Export the model
model.export(format='onnx')