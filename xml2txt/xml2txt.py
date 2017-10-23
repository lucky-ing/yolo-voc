import os
import re
import cv2
import sys
#the source folder that you will read the .jpg and .xml from
src0='/home/lucky/open/wires/1017wire/'
#the destation folder that you will save the .jpg files and .txt files, which are rename and transformed
dst0='/home/lucky/open/wires/picture_voc/10.21/'
#the num of the class that your cutting picture described in your .xml file belong to
voc_name0='/home/lucky/yolo/labelImg-master/data/predefined_classes.txt'
if __name__=='__main__':
    if len(sys.argv)<4:
        print('yolo-voc program need 5 argv.you must input command like\n   python 123.py [start_num] [source folder name] [deststion folder name] [voc name file]')
    else:
        p=int(sys.argv[1])
        src=sys.argv[2]+'/'
        dst=sys.argv[3]+'/'
        if len(sys.argv)>4:
            voc_name=sys.argv[4]
            voc_flag=True
        else:
            voc_name=''
            voc_flag=False
        '''src=input('please input the path of source:\n')
        if src=='':
            src=src0
            dst=dst0
            voc_name=voc_name0
        else:
            dst=input('please input the path of destination:\n')
            if dst=='':
                dst = dst0
                voc_name = voc_name0
            else:
                voc_name = input('please input the class_name file:\n')
                if dst=='':
                    voc_name = voc_name0'''
        listd=os.listdir(src)
        txt=re.compile(r'.*(xml)')
        listdir=[]
        for i in listd:
            if re.findall(txt,i):
                listdir.append(i)

        cc=r'<xmin>(.*)</xmin>'

        xxmin=re.compile(r'<xmin>(.*)</xmin>')
        yymin=re.compile(r'<ymin>(.*)</ymin>')
        xxmax=re.compile(r'<xmax>(.*)</xmax>')
        yymax=re.compile(r'<ymax>(.*)</ymax>')
        wwidth=re.compile(r'<width>(.*)</width>')
        hheight=re.compile(r'<height>(.*)</height>')
        nname=re.compile(r'<name>(.*)</name>')
        if voc_flag==True:
            f=open(voc_name)
            listname=f.read()
            f.close()

        p=0
        for i in listdir:
            i_file=open(src+i,'r')
            i_content=i_file.read()
            i_file.close()
            print(i)
            #print(i_content)
            name = (re.findall(nname, i_content)[0])
            if voc_flag==True:
                index = listname.index(name)
            else:
                index = 0
            txtname0 = dst + str(p).zfill(4) + '.txt'
            f = open(txtname0, 'w')
            width=int(re.findall(wwidth,i_content)[0])
            height=int(re.findall(hheight,i_content)[0])
            for j in range(re.findall(xxmin,i_content).__len__()):

                xmin=int(re.findall(xxmin,i_content)[j])
                ymin=int(re.findall(yymin,i_content)[j])
                xmax=int(re.findall(xxmax,i_content)[j])
                ymax=int(re.findall(yymax,i_content)[j])



            #txtname=dst+i
            #txtname0=txtname.replace('xml','txt')

                if j!=0:
                    f.write('\n')
                f.write(str(index)+' '+'%0.4f'%((float(xmin)+float(xmax))/float(width)/2)+' '+'%0.4f'%((float(ymin)+float(ymax))/float(height)/2)+' '+'%0.4f'%(float(xmax-xmin)/float(width))+' '+'%0.4f'%(float(ymax-ymin)/float(height)))
            f.close()
            imgsource=src+i
            imgname0 = imgsource.replace('xml', 'jpg')
            img=cv2.imread(imgname0)
            #print(img)

            if img is None:
                imgname0=imgname0.replace('jpg','JPG')
                img = cv2.imread(imgname0)
            if img is None:
                imgname0 = imgname0.replace('JPG', 'png')
                img = cv2.imread(imgname0)
            imgdst=dst+str(p).zfill(4)+'.jpg'
            #imgname1 = imgdst.replace('xml', 'jpg')
            cv2.imwrite(imgdst,img)
            p+=1
