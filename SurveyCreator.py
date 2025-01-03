from PIL import Image, ImageDraw, ImageFont
import random
import csv
import uuid
import os

#initialize file
EXPORT_INFORMATION = {
    "Group": 0,
    "ID": "123",
    "TopRightLane":0,
    "TopCentLane":0,
    "TopLeftLane":0,
    "LeftLeftLane":0,
    "LeftCentLane":0,
    "LeftRightLane":0,
    "BottomLeftLane":0,
    "BottomCentLane":0,
    "BottomRightLane":0,
    "RightRightLane":0,
    "RightCentLane":0,
    "RightLeftLane":0,
    "BottomRightUpwards": 0,
    "BottomLeftUpwards": 0,
    "TopLeftDownwards": 0,
    "TopRightDownwards": 0,
    "TopRightWestward": 0,
    "TopLeftEastward": 0,
    "BottomLeftEastward": 0,
    "BottomRightWestward": 0
}

base_path = r"C:\Users\visha\OneDrive\Desktop\SchoolRelated\Visual Studio Projects\Random_Stuff"

dpaths = []

# for i in range(1, 21):
#     directory_path = os.path.join(base_path, f"folder_{i}")
#     dpaths.append(directory_path)
#     os.makedirs(directory_path, exist_ok=True)

#f = open("imageids.csv", "a", newline="")
#writer = csv.writer(f)

#keys_tuple = tuple(EXPORT_INFORMATION.keys())
#writer.writerow(keys_tuple)



def draw_intersection(img1):
    #Drawing line segments from top to bottom (1 - left side)
    img1.line([(150,0), (150,150)], fill="gray", width=4)
    img1.line([(150,250), (150,400)], fill="gray", width=4)

    #Drawing line segments from top to bottom (2 - right side)
    img1.line([(250,0), (250,150)], fill="gray", width=4)
    img1.line([(250,250), (250,400)], fill="gray", width=4)

    #Draw dotted lines for top left lane
    for i in range(0, 135, 10):
        img1.line([(166, i), (166, i+4)], fill="white", width=1)

    for i in range(0, 135, 10):
        img1.line([(182, i), (182, i+4)], fill="white", width=1)

    #Draw dotted lines for bottom left lane
    for i in range(265, 400, 10):
        img1.line([(166, i), (166, i+4)], fill="white", width=1)

    for i in range(265, 400, 10):
        img1.line([(182, i), (182, i+4)], fill="white", width=1)

    for i in range(0, 135, 10):
        img1.line([(218, i), (218, i+4)], fill="white", width=1)
    
    for i in range(0, 135, 10):
        img1.line([(234, i), (234, i+4)], fill="white", width=1)

    for i in range(265, 400, 10):
        img1.line([(218, i), (218, i+4)], fill="white", width=1)
    
    for i in range(265, 400, 10):
        img1.line([(234, i), (234, i+4)], fill="white", width=1)

    #Drawing yellow lines to represent back and forth movement (mid top)
    img1.line([(202, 0), (202, 140)], fill="yellow", width=1)
    img1.line([(198, 0), (198, 140)], fill="yellow", width=1)

    #Drawing yellow lines to represent back and forth movement (mid bottom)
    img1.line([(202, 260), (202, 400)], fill="yellow", width=1)
    img1.line([(198, 260), (198, 400)], fill="yellow", width=1)

    #Drawing walkways (top side)
    for i in range(156, 250, 6):
        img1.line([(i, 150), (i, 140)], fill="white", width=3)

    #Drawing walkways (bottom side)
    for i in range(156, 250, 6):
        img1.line([(i, 250), (i, 260)], fill="white", width=3)

    #Drawing line segments from left to right (1 - top side)
    img1.line([(0,150), (150,150)], fill="gray", width=4)
    img1.line([(250,150), (400,150)], fill="gray", width=4)

    #Drawing line segments from left to right (2 - bottom side)
    img1.line([(0,250), (150,250)], fill="gray", width=4)
    img1.line([(250,250), (400,250)], fill="gray", width=4)

    #Draw dotted lines
    for i in range(0, 135, 10):
        img1.line([(i, 166), (i + 4, 166)], fill="white", width=1)
    
    for i in range(0, 135, 10):
        img1.line([(i, 182), (i + 4, 182)], fill="white", width=1)

    for i in range(265, 400, 10):
        img1.line([(i, 166), (i + 4, 166)], fill="white", width=1)
    
    for i in range(265, 400, 10):
        img1.line([(i, 182), (i + 4, 182)], fill="white", width=1)

    for i in range(0, 135, 10):
        img1.line([(i, 218), (i + 4, 218)], fill="white", width=1)
    
    for i in range(0, 135, 10):
        img1.line([(i, 234), (i + 4, 234)], fill="white", width=1)

    for i in range(265, 400, 10):
        img1.line([(i, 218), (i + 4, 218)], fill="white", width=1)
    
    for i in range(265, 400, 10):
        img1.line([(i, 234), (i + 4, 234)], fill="white", width=1)

    #Drawing yellow lines to represent back and forth movement (mid top)
    img1.line([(0, 202), (140, 202)], fill="yellow", width=1)
    img1.line([(0, 198), (140, 198)], fill="yellow", width=1)

    #Drawing yellow lines to represent back and forth movement (mid bottom)
    img1.line([(260, 202), (400, 202)], fill="yellow", width=1)
    img1.line([(260, 198), (400, 198)], fill="yellow", width=1)

    #Drawing walkways (left side)
    for i in range(156, 250, 6):
        img1.line([(150, i), (140, i)], fill="white", width=3)

    #Drawing walkways (right side)
    for i in range(156, 250, 6):
        img1.line([(250, i), (260, i)], fill="white", width=3)

    #Showcasing what lanes are what
    img1.line([(152, 134), (197, 134)], fill="white", width=2)
    img1.line([(203, 264), (248, 264)], fill="white", width=2)

    img1.line([(134, 203), (134, 248)], fill="white", width=2)
    img1.line([(264, 152), (264, 197)], fill="white", width=2)

def make_cars(img1):
    radius = 4.3

    STARTING_VALUES = {
        "TopRightLane" : [159, 125, -12], #done
        "TopCentLane": [174, 125, -12], #done
        "TopLeftLane" : [190,125, -12], #done
        "LeftLeftLane" : [125, 210, -12], #done
        "LeftCentLane": [125, 226, -12], #done
        "LeftRightLane" : [125, 242, -12], #done
        "BottomLeftLane" : [210,275, 12], #done
        "BottomCentLane": [226,275, 12], #done
        "BottomRightLane" : [242,275, 12], #done
        "RightRightLane" : [275, 159, 12], 
        "RightCentLane" : [275, 174, 12], 
        "RightLeftLane" : [275, 190, 12],
    }


    for location in STARTING_VALUES:
        amount = random.randint(0, 10)
        EXPORT_INFORMATION[location] = amount
        
        for i in range(0, amount):
            if location[0:3] == "Top" or location[0:3] == "Bot":
                img1.ellipse((STARTING_VALUES[location][0] - radius, STARTING_VALUES[location][1]-radius + (STARTING_VALUES[location][2] * i), STARTING_VALUES[location][0] + radius, STARTING_VALUES[location][1] + radius + (STARTING_VALUES[location][2] * i)), fill=(0,255,255))
            else:
                img1.ellipse((STARTING_VALUES[location][0]-radius + (STARTING_VALUES[location][2] * i), STARTING_VALUES[location][1]-radius, STARTING_VALUES[location][0] + radius + (STARTING_VALUES[location][2] * i), STARTING_VALUES[location][1] + radius), fill=(0,255,0))

def make_pedestrians(img1):
    PEDESTRIAN_VALUES = [
        (255, 243), #bottom right upwards
        (145, 243), #bottom left upwards
        (145, 158), #top left downwards
        (255, 158), #top right downwards
        (241, 145), #top right westward
        (159, 145), #top left eastward
        (159, 255), #bottom left eastward
        (241, 255) #bottom right westward
    ]

    COORDINATION = ["BottomRightUpwards", "BottomLeftUpwards", "TopLeftDownwards", "TopRightDownwards", "TopRightWestward", "TopLeftEastward", "BottomLeftEastward", "BottomRightWestward"]

    PED_RADIUS = 8.9
    FONT = ImageFont.truetype("arial.ttf", 15)

    for i in range(0, len(PEDESTRIAN_VALUES)):
        num = random.randint(0, 10)
        EXPORT_INFORMATION[COORDINATION[i]] = num
        if num != 0:
            img1.ellipse((PEDESTRIAN_VALUES[i][0] - PED_RADIUS, PEDESTRIAN_VALUES[i][1] - PED_RADIUS, PEDESTRIAN_VALUES[i][0] + PED_RADIUS, PEDESTRIAN_VALUES[i][1] + PED_RADIUS), fill=(255,165,0))
            if num > 9:
                img1.text((PEDESTRIAN_VALUES[i][0] - 9, PEDESTRIAN_VALUES[i][1] - 8), str(num), (0, 0, 0), font=FONT)
            else:
                img1.text((PEDESTRIAN_VALUES[i][0] - 5, PEDESTRIAN_VALUES[i][1] - 8), str(num), (0, 0, 0), font=FONT)


count = 0
num = 0
# for i in range(0, 400):  
#     if count % 20 == 0:
#        num = num+1
#        count = 0 
#     img = Image.new("RGB", (400,400), (0,0,0))
#     img1 = ImageDraw.Draw(img)
#     draw_intersection(img1)
#     make_cars(img1)
#     make_pedestrians(img1)
#     id = uuid.uuid4()
#     EXPORT_INFORMATION["ID"] = id
#     EXPORT_INFORMATION["Group"] = num
#     file_path = os.path.join(dpaths[num - 1], f"{id}.png")
#     img.save(file_path)
#     row = tuple(EXPORT_INFORMATION.values())
#     writer.writerow(row)
#     count = count + 1
    

#f.close()
img = Image.new("RGB", (400,400), (0,0,0))
img1 = ImageDraw.Draw(img)
draw_intersection(img1)
file_path = os.path.join("official.png")
img.save(file_path)
