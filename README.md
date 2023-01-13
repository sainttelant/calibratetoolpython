文件夹内部的文件先备份一份，不要随意删除，解压即用，无需安装。
打开后文件目录有以下文件；
 
其中标定需要准备的是 1.bmp图像，point.xlsx原始数据文件。


1、首先准备外参标定使用的数据，誊抄原始数据到point.xlsx里面，不要随意改变excel里面每行的名字（第一行英文）。准备好的数据样式为：


 

2、准备好数据之后，运行cmd，或者powershell 命令行至安装程序目录下，输入以下命令生成input.xml 文件，供下一步正式标定使用。
./readxlsx.exe -I point.xlsx -o input.xml
 
运行成功后，会在目录下生成input.xml 文件，这时候目录里面再准备好当前要标定的相机的原始图片，命名为1.bmp, 格式一定要为bmp格式，原始图片存下来改个名字后缀即可。

3、有了一副图1.bmp, 还有了input.xml之后，就可以双击运行roadsideCalibration.exe,就完成了外参标定工作。这时候，目录下会生成几个文件save.jpg， CalibrateLog.txt, calibration.xml,gps.KML, gpsGenerator.txt. 表示标定成功。运行成功后整个文件夹这样：
 
第二步运行成功多了input.xml,第三步之后，整个多了以上的文件，就完成了标定。



