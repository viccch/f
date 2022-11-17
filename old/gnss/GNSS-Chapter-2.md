---
layout: post
title: "GNSS-Chapter 2 Coordinate and Time System"
categories: gnss
date:   2022-10-13 00:04:43 +0800
---


# Chapter 2 Coordinate and Time System

1.	Which several important stages have been experienced during the development of coordinate reference system?
（坐标参考系的发展过程中都经历了那几个重要阶段？）
`地心说、旋转椭球、大地水准面、参考椭球面、地心参考系`
2.	What is the direction of the development of coordinate reference system?(the mainline throughout the whole development of coordinate reference system)（贯穿整个坐标参考系发展的主线是什么？）
`更准确的认识地球，更精确的描述位置。`
3.	How to construct a coordinate reference system?
（如何构造一个坐标参考系）
	为了在地球表面确定一个准确的位置，必须知道地球本身的形状与大小。
	确定空间参考系的类型确定地球的原点、基准面（参考椭球）、基准线（坐标轴方向）等定义量算方法。

4.	How to construct a time reference system?
（如何构造一个时间参考系）
`确定时间间隔;确定时间起始点`
5.	What are the rules of establishing a ellipsoid reference system?
（建立一个椭球参考系的规则是什么）  

	1. The quality of ellipsoid is equal to that of the earth, and
	the rotating velocity at the same speed as the earth.  
	2. The size of ellipsoid is equal to that of the earth, and
	the surface is closest to that of the earth.  
	3. The center of ellipsoid coincides with that of the earth, 
	and b axis coincides with the earth’s axis of rotation.  
	椭球与地球的质量(mass)相等，具有相同的旋转速度。  
	尺寸大小和地球相等，表面和地球最接近。  
	椭球中心和地球重合，b轴作为地球的旋转轴。  

6.	What are the merits of geoid ellipsoid relative to geometry ellipsoid?
（相对于几何椭球，大地水准面椭球的优势是什么）  
	1.It is a clear determined and objective existence
	ellipsoid; (the one and only)  
	2.It has the physical meaning of ellipsoid, where the 
	gravity values of all points are same;  
	3.It can be used as the datum of altitude  
	1. 是明确确定的客观存在的椭球面。  
	2. 是有物理意义的椭球面，面上所有点的重力相等。  
	3. 能作为高程的基准。  
7.	How to convert the geodetic height to the altitude?
（如何将大地高转换成正高）
	Geodetic height：大地高，地面点到参考椭球面距离
	Altitude：即正高，地面点到大地水准面的距离。
	Geodetic height减去当地参考椭球面与大地水准面之间的距离得到Altitude。

8.	What are the differences between zero point and base point?
（零点和基点的区别）
`水准零点是位于平均海水面、高程为0的点。水准原点是国家测算地面高程点的起算依据。根据1982国家高程基准，水准原点的高程是72.260m。`
9.	Why we need to set up reference-centric ellipsoid reference system?
（为什么要建立参心椭球坐标系）
`参心椭球体与大地水准面具有确定的位置关系。是在局部范围内与大地水准面符合最好的理想椭球体。`
10.	What are the advantages and disadvantages of reference-centric ellipsoid and geocentric ellipsoid?
（参心椭球和地心椭球的优点和缺点）
`参心椭球缺点：精度低；误差累积；静止状态；更新慢；局部范围符合好；`
`地心椭球优点：精度高；无误差累积；动态状态；更新迅速；全球范围符合。`
11.	Which several important stage during the development of time reference system?
（时间参考坐标系的发展过程中的几个重要阶段）
`从沙漏计时、滴水计时、日晷计时，到机械表计时，石英表计时（quartz每秒32768次震荡）,原子钟计时。`
12.	What are the GPS coordinate and time reference system?
（GPS的坐标和时间参考系是什么）
	坐标参考系：WGS-84世界大地坐标系（World Geodetic System）。WGS-84 世界大地坐标系的几何定义是：原点是地球质心，Z 轴指 BIH1984.0 定义的协议地球极(CTP)方向，X 轴指向 BIH1984.0 的零子午面和 CTP 赤道的交点，Y 轴与 Z 轴、X 轴构成右手坐标系。上述 CTP 是协议地球极(Conventional Terrestrial Pole)的简称；由于极移现象的存在，地极的位置在地极平面坐标系中是一个连续的变量，其瞬时坐标由国际时间局(Bureau International de l’Heure 简称 BIH)定期向用户公布。WGS-84 世界大地坐标系就是以国际时间局 1984 年第一次公布的瞬时地极(BIH1984.0)作为基准建立的地球瞬时坐标系，严格来讲属于准协议地球坐标系。
	时间参考系：GPST 即GPS 时。GPS时间是GPS系统运作的时间基准，简称GPST，GPST本质还是原子时，其时间基准来源于GPS系统卫星上一些列的原子钟的测量频率。GPST的整秒进位时刻和UTC时间同步，虽然存在偏差但是这个偏差很小在10ns左右，与UTC不同的是，GPST是一个连续的时间系统，不存在跳秒问题，时间的起始是1980年1月6日0点0时0分0秒，所以GPST和UTC之间会存在一个偏差，并且该偏差会随着时间的变得越来越大，目前两者之间时间差异以达到19S。

13.	What kinds of coordinate reference system are often used? How do they be defined?
（常用坐标参考系及其定义）
	天球参考系：用以描述自然天体或者人造天体在空间中的位置或者方向的一种坐标系。基准面是大地水准面，基准线是铅垂线。
	大地坐标系：大地测量中以参考椭球面为基准面建立起来的坐标系。地面点的位置用大地经度L，大地维度B和大地高H（栏发现到椭球面的距离）表示。
	空间大地直角坐标系空间大地执教坐标系是与大地坐标系相对应的三维大地直角坐标系。以原点0为椭球中心，Z轴与椭球旋转轴一致，指向地球的北极，X轴与椭球赤道面和格林尼治平均子午面的郊县重合，Y轴与XZ平面正交，指向东方，X,Y,Z构成右手坐标系，P点的空间大地直角坐标用（X,Y,Z）表示。
	地心坐标系：建立大地坐标系时，如果选择的旋转椭球时总地球椭球，椭球中心就是地球之心，再定义坐标轴的指向，此时建立的大地坐标系就是地心坐标系。

14.	What kinds of time reference system are often used? How do they be defined?
（常用时间参考系及其定义）
	Universal Time System 世界时：基于地球自转运动，受到地球自转不均匀变化和极移影响，不稳定。
	Atomic Time System 原子时：基于原子中的能级跃迁和电子发射，非常稳定。
	Coordinated Universal Time, UTC 协调世界时：由于世界时对于高精度的时间应用来说不能满肚要求，而使用原子时又要参考世界时，为了适应需要产生了协调世界时。UTC以原子时度量，需要周期性的对其修正1秒，以保证UT-UTC不大于0.9s。
	GPS Time ：GPST 属于原子时系统，秒长与原子时相等，但是起始点不同于原子时。起始于1980年1月6日00:00:00。
	Julian Day 儒略日： 是在儒略周期内以连续的日数计算时间的计时法。起点是BC 4713年1月1日12:00:00。每一天赋予一个唯一的数字。儒略日数字位数太多，简化儒略日 MJD=JD-2400000.5，MJD的相应起点是1858年11月17日世界时0时。

15.	How to convert a atomic time to a universal time?
（如何将原子时转换成世界时）  
世界时（UT）基于地球的自转，由于地球自转不稳定，世界时（UT）与协调世界时（UTC）之间有小于0.9s的误差，因此世界时无法简单地与原子时相转换。
16.	How to convert a atomic time to a coordinate universal time?
（如何将原子时转换成协调世界时）
`UTC=TAI-1s * n`
17.	How to convert a GPS time to a atomic time?
（如何将GPS时间转换成原子时）
`GPST=TAI-19s`
18.	How to convert a GPS time to a coordinated universal time?
（如何将GPS时间转换成协调世界时）
`GPST=UTC+1s * n – 19s`
19.	How to convert a Gregorian calendar date to a Julian date?
（如何将公历日转换成儒略日）
	1. a=(14-month)/12  y=year+4800-a  m=month+12a-3
	2. JDN=day+(153m+2)/5+365y+y/4-y/100+y/400-32045
	（做除法时去掉小数部分）
	3. JD= JDN + (hour-12)/24 +minute/1440 + second/86400
	January 1, 2000 at 12:00:00 对应儒略日JD=2451545.0

20.	How to convert a Terrestrial coordinate to a Topocentric coordinate?
（如何将大地坐标转换成地心坐标）
`BLH -> XYZ`




