import torch #pytorch (.pt)
import pandas as pd # a library for types of dataframes

def count(img):
    mdl = torch.hub.load("ultralytics/yolov5", "yolov5x", pretrained = True)
    pics = [img]
    res = mdl(pics)
    res.print() #or res.show  specific for torch  predicting what the item is

    df = res.pandas().xyxy[0]

    items = {}

    for index, row in df.iterrows():
        if(row["name"] in items.keys()):
            items[row["name"]] += 1
        else:
            items[row["name"]] = 1
    
    return items
