******************for yolo cutting***************************
to transform the .xml files to the .txt files in the yolo training.
it will load the .xml files and transform they to .txt files. simultaneously (at the same time), the picture that the .xml match will be renamed, and be saved in folder of destination with the .txt file. 
first ,there are three paramters in this program.here they are:

#the source folder that you will read the .jpg and .xml from
src0='/home/lucky/open/renzituo/Untitled Folder 2/'
#the folder of destination that you will save the .jpg files and .txt files, which are rename and transformed
dst0='/home/lucky/open/renzituo/biaoding/'
#the train list have be list in the file, and the order of the list represent the num of the class that your cutting picture described in your .xml file belong to
voc_name0='/home/lucky/yolo/labelImg-master/data/predefined_classes.txt'

you can modify this three parameters in the program code, and you can also input it after you start it.be careful of this, the '/' must be included at the end of the path you input.
if have already modify this three patameters in the code, you can just enter the enter key, and it will load the defualt paramters.
