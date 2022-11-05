---
layout: post
title: "GNSS-Chapter 7 Observation Equations and Algorithm"
categories: gnss
date:   2022-10-13 00:09:43 +0800
---



# Chapter 7 Observation Equations and Algorithm

## Questions 
1. What is the geometric principle of SPP?

SPP的几何原理？
$$ \left \{ \begin{matrix}
r_1=\sqrt{(x_s^1-x_R)^2+(y_s^1-y_R)^2+(z_s^1-z_R)^2} \\
r_2=\sqrt{(x_s^2-x_R)^2+(y_s^2-y_R)^2+(z_s^2-z_R)^2}\\
r_3=\sqrt{(x_s^3-x_R)^2+(y_s^3-y_R)^2+(z_s^3-z_R)^2}\\
r_4=6371km
\end{matrix}\right. $$

two spheres intersect-one ring.
three spheres intersect-two points
four spheres intersect-one point



2. What is the observation equation of SPP?

SPP的观测方程是什么

General expression of obs. Equ. of SPP:
$$ \tilde { \rho _i}= \sqrt{(x_S^i-x_R)^2+(y_S^i-y_R)^2+(z_S^i-z_R)^2}-c \cdot t_R + c \cdot t_S^i - dtrop_i - dion_i $$  
$\tilde{\rho_i}$：Obs. Dis.  
$\sqrt{(x_S^i-x_R)^2+(y_S^i-y_R)^2+(z_S^i-z_R)^2}$：Thoretic Dis. $\rho_i$  
$c \cdot t_R + c \cdot t_S^i - dtrop_i -dion_i$：Equivalent Dis. of Err.  


3. What is the mathematic model of SPP?

SPP的数学模型是什么


4. How to resolve the equation of SPP?

如何解SPP的方程

Parameter Estimation 参数估计

5. How to evaluate the precision of SPP?

如何评价标准单点定位的精度




## SPP 标准单点定位

标准单点定位实时以测码伪距作为观测值的一种绝对定位方式；
精密单点定位则是以载波相位作为观测者，并采用IGS等机构提供的精密星历和精密钟差计算卫星位置和卫星钟差来进行高精度绝对定位的一种定位方式。

单点（绝对）定位的优点是只需要一台接收机，数据处理简单。但绝对定位的大多数误差需要采用模型来改正。定位精度通常低于相对定位的精度。传统上，绝对定位都是利用单频接收机采用测码伪距观测值进行定位，用户在观测计划指定方面无需太多布置，仪器设备较为低廉。虽然收到各种误差（卫星钟差、轨道误差）的影响较大，但是绝对定位实时解算和价格低廉的特点仍然使其具有广阔的市场。例如车辆开导航就是这一技术很大部分的一种应用，只要几米的精度就可满足要求。

---

# Chapter 7 基线向量解算

## 主要内容
1. 周跳
2. 差分观测值
3. 基线解算双差数学模型
4. 整周模糊度固定


### 相对定位

相对定位是采用多台GPS接收机，定位结果是各**同步**观测站之间的**基线向量**（坐标差）。

因此，在相对定位中需要给出多个观测站中至少一个观测站的坐标值作为基准，来推求其他各站点的坐标值。

优点：
定位精度高，两个或多个测站，同步观测同一组卫星，可构成差分观测值，从而大大削弱有关误差的影响。因此，GPS相对定位是目前GPS定位中精度最好的一种方法。

缺点：
设备投入大，数据处理复杂。


### 基本概念

**基线向量** 是指利用接收机同步观测采集的观测数据形成的差分观测值，通过参数估计方法计算出的接收机间的三维坐标差，简称**基线** 。基线向量是相对定位的结果，在建立GNSS控制网的过程中，他是网平差时的观测量。