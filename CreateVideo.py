import os
import cv2

path = "images/"
images = []
#vid = cv2.VideoWriter("Project.avi")




for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file
        print(file_name)

        images.append(file_name)

count = len(images)
""" 
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(height)
        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(width) """

frame = cv2.imread(images[0])
height,width,channels = frame.shape

size = (width, height)
print(size)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count):
       frame = cv2.imread(images[i])
       out.write(frame)


out.release( )
cv2.destroyAllWindows()     
          
