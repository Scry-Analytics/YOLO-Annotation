import glob
import os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

# current_dir = '/home/tairen/PycharmProjects/YOLO-Annotation-Tool-master/Images/001/'

current_dir = '/home/tairen/PycharmProjects/YOLO-Annotation-Tool-master/Labels/001'
images_dir = '/home/tairen/PycharmProjects/YOLO-Annotation-Tool-master/Images/001'
# Directory where the data will reside, relative to 'darknet.exe'
#path_data = './NFPAdataset/'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.txt")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(images_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(images_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1
