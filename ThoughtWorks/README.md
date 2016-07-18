## 运行

将文件graph.py, main.py, test.py, data.txt放在同一目录下，运行以下命令执行主程序：
	
	python main.py
	

运行以下命令执行测试程序：

	python test.py
	
使用的python环境为Python 2.7.10

## 简要说明

* data.txt为图的输入，里面的内容为"AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7"，data.txt中的内容将会被程序用来构建图，图使用临接矩阵来表示，data.txt中的内容将会构建出如下的图：

	{'A': {'B': '5', 'E': '7', 'D': '5'},
	 'B': {'C': '4'}
	 'C': {'E': '2', 'D': '8'}
	 'D': {'C': '8', 'E': '6'}}
	 'E': {'B': '3'}}
	 
* graph.py定义了Graph类，Graph类的初始化函数会读入data.txt中的内容构建图，在类Graph中使用字典表示图。在程序中主要使用了图的广度优先搜索和深度优先搜索的思想来解决各问题。
* main.py为主程序，调用了Graph类中的各方法解决问题。
* 程序的异常会记入日志文件log.txt，该文件与其它文件在同一目录下。
* 程序的单元测试用到了unittest。
