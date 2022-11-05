---
layout: post
title:  "GNSS-keypoint"
date:   2022-10-16 00:03:43 +0800
categories: gnss
author: viccch
mail: zhangshijie2002@gmail.com
---

# GNSS Principle and Application

## 题型 
选择 15\*2  
简答 10\*5  
综合计算 2\*10  
题目英文   
答题中文

## `考试时间 Oct,20,2022`  


#### 真题资料
[试卷1](GNSS-exam-1.md)  
[试卷2](GNSS-exam-2.md)  
[试卷3](GNSS-exam-3.md)   

#### 目录
[Chapter 1 Introduction](GNSS-Chapter-1.md)  
[Chapter 2 Coordinate and Time Systems](GNSS-Chapter-2.md)  
[Chapter 3 GNSS signal](GNSS-Chapter-3.md)  
[Chapter 4 GNSS Measurement and Linear combination](GNSS-Chapter-4.md)  
[Chapter 5 Satellite Orbits](GNSS-Chapter-5.md)  
[Chapter 6 Error Sources of GNSS Surceying](GNSS-Chapter-6.md)  
[Chapter 7 Observation Equation and Algorithm](GNSS-Chapter-7.md)  
[Chapter 8 Parameter Estimation](GNSS-Chapter-8.md)  
[Chapter 9 Cycle Slip Detection and Ambiguity Resolution](GNSS-Chapter-9.md)  
[Chapter 10 GNSS Augmentation Technique](GNSS-Chapter-10.md)  
[Chapter 11 GPS 测量设计与实践](GNSS-Chapter-11.md)  


# Chapter 2 : Coordinate and Timing System 
时间和空间参考系统

## Development of Space-time Reference System
### Development 
- Geodesic Domes    认识到地球是球形。
- Ratiation Ellipsoid   旋转椭球
- Geoid Ellipsoid   有物理意义的大地椭球
- Reference-centric Ellipsoid   参心椭球
- Geocentric Ellipsoid  地心椭球

#### Geodesic Domes
麦哲伦(Magellan)环球航行证明地球是个圆球  
墨卡托(Mercator)制作了全球地图
#### Ratiation Ellipsoid 
旋转椭球  
地球不是规则的球形（regular sphere），而是一个椭球（ellipsoid）。
#### Geoid Ellipsoid
大地水准面椭球  
大地水准面是平均海水面重合并延伸到大陆内部的水准面。因地球表面起伏不平和地球内部质量分布不均匀，大地水准面是一个略有起伏的不规则曲面。该面包围的形体近似于一个旋转椭球，成称为“大地体”（geoid）。
$$H^r=H-\zeta$$
- $H$: geodetic height(大地高)
- $H^r$:altitude(海拔)
- $\zeta$:height anomaly(高程异常)

##### base point & zero point
基点和零点

#### Reference-centric Ellipsoid
参考椭球

##### How to obtain a reference-centric ellipsoid ?
- Determination of the size and shape of ellipsoid. a,f,e(semi-major axis, flattening, eccenticity)
- Determiantion of the direction of he minor axis.
- Determiantion of the position of its centre.
  (确定椭球的大小和形状：长半轴，扁率，偏心率；确定短半轴的方向；确定球心的位置。)

##### The rule of determination of reference-centric ellipsoid
It is chosen to fit the geoid as closely as measurement technologies and computational abilities allowed.
选择测量技术和计算能力允许的与大地水准面最吻合的椭球面。

#### Geocentric Ellipsoid
地心椭球
##### Merit（优点）
- High Precision 高精度
- No Error Accumulation 没有误差累积
- Dynamic State 动态
- Update Quickly 更新迭代快
- Unity Worldwide 全球范围统一

##### International Terrestrial Reference Frame,ITRF

### Time System

#### Important Stages
Hourglass,sandglass 沙漏
sundial 日晷
Mechanical clock 机械表
quartz clock 石英表
Atomic clock 原子钟

#### Common Time Reference System

Universal Time System

Atomic Time System

Cordinated Universal Time

GPS Time

Julian Day

#### Universal Time System

#### Atomic Time System

#### Cordinated Universal Time

#### GPS Time

#### Julian Day

## Definition of Sapce-time Reference System
### Celestial Reference System
### Terrestrial Reference System
### Station Local Reference System
### Time System


## Application of Space-time Reference System




### how to transform the coordiantes in the different ITRF  and different epoch?


# Chapter 3 : GNSS Signal
### What is the code?
### What is the random code ?
### What is the pseudo random code?

### Generation  of Ranging Code


### Characters of Ranging Code(特征)

### Principle of Pseudorange Measurement

### Characters of Psuduorange Observation (伪距观测特征)

#### Advantages 

#### Disadvantages

#### Improvement

# Chapter 4 GNSS Measurement and Linear Combination

### why do we have Linear Combiantion of Measurements

### 目的
### 主要线性组合方式
#### 同类型不同频点
####
#### 不同类型观测值组合

### Station difference 
站间差分

#### Satellite difference 
 星间差分

### Epoch difference 
 历元间差分


# Chapter 5: Quality Analysis of Measurements


### Software
#### TEQC
### BNC
### CUMAC

### Basic Effect
### Data Integrity Rate 
数据完整率
### SNR 信噪比
信号功率和噪声功率之比
### 多路径
信号传播过程中受一些物体的反射发生了传播方向、振幅、相位、极化等改变，这些变化了的信号与直线到达接收机的信号叠加，产生了多路径效应。 
### 周跳比
某段时间内观测历元数与发生周跳历元数的比值。

# Chapter 6 : Errors

### classify 
### 卫星相关
### 传播路径相关
### 接收机相关

### Effect of Errors
### Ionospheric 
### 与 相关 位置 季节 频率 高度角
### Code Delay and Phase Advance


## Tropospheric Effects 对流层
### 高度角 气象
### 对流层与频率不相关
### 干延迟 湿延迟

### 如何消除
#### 差分 区域模型 参数估计

## 固体潮与海洋潮  
### 晚上大，中午小， 与电离层对流层相反

## Multipath Effects 
多路径 
### 反射产生

## Antenna Phase Centre Offset and Variation 天线相位中心

## Key issues

# Chapter 7 Observation Equations and Algorithm

## Difference between SPP & PPP
### Code  Phase 
### Broadcast Precise Epoch
### real time


## Observation Equation of SPP

###
原始观测方程 
线性化观测方程 (泰勒级数 展开)


### Precision Evalution of SPP
#### DOP  dilution of precision
精度评定指标
#### HDOP hirizontial DOP 平面坐标精度
#### VDOP vertical DOP 高程坐标精度
#### PDOP position DOP 三维坐标精度
#### TDOP time DOP 时间精度
#### GDOP Geometric 三维坐标与实践精度评定因子


# Chapter 7 基线向量解算
## 相对定位
 含义 优点 缺点
## 基线向量

## 周跳（整周跳变）
###  原因
#### 遮挡等

### 周跳特点
#### 只影响整周

### 周跳修复方法
####


## 差分

## 整周模糊度 固定
### 原因- （ignore)
### 解算步骤

### 固定技术
#### 测量域固定技术
#### 坐标域的搜索技术 
#### 直接 模糊度域搜索技术：FARA ,

# Chapter 8: 基线向量网平差 

### GNSS 数据处理最后阶段

## 网平差目的
### 消除由观测量、已知条件

## 分类
无约束 
约束
联合平差:加入常规观测值进行联合平差

三维平差与二维平差


## 步骤

 提取基线向量 协方差矩阵
 无约束
 约束
 质量分析与控制


## 原理


## GNSS 数据处理软件
### 科研软件
精度高 操作复杂
GAMIT  PANDA
### 商用
TGO LGO CHC 
精度低 操作简单

# Chapter 11: GNSS 网测设

## GNSS 网分类
框架基准网
精度 可靠性要求高
效率 费用低

## GPS 网形设计
观测时段数计算公式
C=n*m/N
 例：n=4,m=3 ,N=3
时段数 C=n\*m/N
总基线数 C\*N\*(N-1)??
必要基线数
独立基线数
多余基线数 

观测时段 
同步观测

布网方案 

设计（ignore)


