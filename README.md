<h1 id="时间片轮转调度算法">时间片轮转调度算法</h1>
<h2 id="具体任务">具体任务</h2>
<ul>
<li>根据需要，合理设计 PCB 结构，以适用于时间片轮转调度算法。</li>
<li>设计模拟指令格式，并以文件形式存储，程序能够读取文件并自动生成指令序列。</li>
<li>根据文件内容，建立模拟进程队列，并能采用时间片轮转调度算法对模拟进程进行调度。</li>
</ul>
<h2 id="任务要求">任务要求</h2>
<ul>
<li>进程的个数，进程的内容（即进程的功能序列）来源于一个进程序列描述文件。</li>
<li>需将调度过程输出到一个运行日志文件。</li>
<li>开发平台及语言不限。</li>
<li>要求设计一个 Windows 可视化应用程序</li>
</ul>
<h2 id="总体设计">总体设计</h2>
<p>本次课程设计将通过从文本文档中导入指令到程序生成模拟进程和模拟指令，然后对模拟进程和模拟指令进行时间片轮转调度，并进行可视化设计。<br>
模拟指令的格式：操作命令+操作时间</p>
<blockquote>
<p>C：表示在CPU上计算<br>
I： 表示输入<br>
O： 表示输出<br>
W： 表示等待<br>
H： 表示进程结束</p>
</blockquote>
<p>操作时间代表该操作命令要执行多长时间。这里假设 I/O 设备的数量没有限制，I 和 O 设备都只有一类。<br>
每个进程中的指令是上下关联的，即每个进程中的指令只能按顺序执行，必须完成了该进程中的上一条指令，才能执行下一条指令。<br>
I，O，W 三条指令实际上是不占用 CPU 的，执行这三条指令就应该将进程放入对应的等待队列，例如：输入等待队列，输出等待队列 ，其他等待队列等……<br>
例如，有一虚拟程序文件prc.txt描述如下：</p>
<blockquote>
<p>P1<br>
C10<br>
I20<br>
C40<br>
I30<br>
C20<br>
O30<br>
H00<br>
P2<br>
I10<br>
C50<br>
O20<br>
H00<br>
P3<br>
C10<br>
I20<br>
W20<br>
C40<br>
O10<br>
H00</p>
</blockquote>
<h2 id="效果演示">效果演示</h2>
<ul>
<li>
<p>运行效果</p>
<p><img src="https://upload-images.jianshu.io/upload_images/3314844-e06bb0fe0cbda4b2.gif?imageMogr2/auto-orient/strip" alt="rr.gif"></p>
</li>
<li>
<p>日志文件<br>
<img src="https://upload-images.jianshu.io/upload_images/3314844-c43d74dfcc19e4ba.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="log.png"></p>
</li>
</ul>

