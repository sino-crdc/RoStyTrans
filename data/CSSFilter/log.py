#'''author @Yakun'''
#Attention:before processing data,you can run this program in order to change the code in 'display_board.html',and the data must be in the file'img'.
#          if you want to change a fliter, you can write the fliter name in 'csstarget,class' from this file
import os
path='C:\pythonProject1\RoStyTrans\CSSFilter\img'
scriptlogpath='C:\pythonProject1\RoStyTrans\CSSFilter\scriptlog.txt'
csslogpath='C:\pythonProject1\RoStyTrans\CSSFilter\csslog.txt'

target='''var node1 = document.getElementById('img1')
  domtoimage.toJpeg(node1)
    .then(function (dataUrl) {
        var link = document.createElement('a');
        link.download = 'my-image-1.jpeg';
        link.href = dataUrl;
        link.click();
    });'''

csstarget='''<figure id='img1' class='_1977' style="margin:0px">
  <img src='./img/img1.jpg' alt="cannot display">
</figure>'''

old1='\'img1\''
old2='\'my-image-1.jpeg\''
old3='node1'
old4='img1.jpg'
names=os.listdir(path)
filepath=os.path.dirname(path)
k=1
with open(scriptlogpath,"w",encoding='utf-8') as f1:
    for i in names:
        scriptlog=target.replace(old1,'\''+i+'\'')
        scriptlog=scriptlog.replace(old2,'\''+i+'-1977.jpg'+'\'')
        scriptlog=scriptlog.replace(old3,'node'+str(k))
        k+=1
        f1.write(scriptlog)
        f1.write('\n')
        f1.write('\n')
with open(csslogpath,"w",encoding='utf-8') as f2:
    for i in names :
        csslog=csstarget.replace(old1,'\''+i+'\'')
        csslog=csslog.replace(old4,i)
        f2.write(csslog)
        f2.write('\n')
        f2.write('\n')
