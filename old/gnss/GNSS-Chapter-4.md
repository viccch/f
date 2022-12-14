---
layout: post
title: "GNSS-Chapter 4 GNSS Measurement and Linear Combination"
categories: gnss
date:   2022-10-13 00:06:43 +0800
---

# Chapter 4 GNSS Observables

## Code Pseudorange 
## Carrier Phases
## Doppler Measurements

# Key issues 


What is the basic principle of code measurements?

测距码测量的基本原理是什么？

What is the specific form of code observation equation?

测距码观测方程的具体形式？

What is the basic principle of carrier phase measurement?

载波相位测量的基本原理？

What is the specific form of carrier observation equation?

载波相位观测方程的具体形式？

What are the precisions of CA,P,L1 and L2 observables, respectively?

CA,P,L1,L2 观测的精度分别是？

What is the difference of ionospheric term between the carrier phase model and cod psuedorange model?

载波相位模型和测码伪距观测模型的电离层项有什么区别？

What is the basic principle of Doppler measurement?

多普勒观测的基本原理？

What is the specific form of Doppler observation equation?

多普勒观测方程的具体形式？

What are the chararters of the code psuedorange, carrier phase, and Doppler measurement, respectively?

测码伪距、载波相位、多普勒测量的特征分别是什么？


## 4.1 Code Pseudoranges

**测码伪距**

The pseudorange is a measure of the distance between the satellite and the receiver's antenna(天线).The distance is measured through measuring the GNSS signal transmitting(传输) time from the satellite to the GNSS receiver's antenna. Therefore, such a distance is referred to the distance between the satellite at the time of the GNSS signal emission(发射) and the GNSS antenna at the time of GNSS signal reception. The transmitting time is measured through maximum correlation analysis of the receiver code and the GNSS signal. The receiver code is derived(派生) from the clock used in the GNSS receiver. The GNSS signal is, of course generated by the click used int the GNSS satellite. The measured pseudorange is different from the geometric(几何) distance between the satellite and the receiver's antenna because of the errors of the both clocks and the influences of the signal transmitting mediums(介质). It is also notable(显著的) that the path of the signal transmission differs slightly(稍) from the geometric path. The transmitting medium not only delays the transmitting of the signal, but also bends(弯曲) the transmitting path of the signal.



伪距是卫星和接收机天线之间距离的量测。通过测量GNSS信号从卫星到接收机天线之间传输的时间来量测这段距离。因此，这个距离指的是卫星信号发射的时刻和GNSS天线接收到信号的时刻的距离。这个传输时间的测量是通过接收机伪码和GNSS信号之间最大相关性分析得到。接收机伪码是从GNSS接收机时钟派生的。GNSS信号是由GNSS卫星的时钟生成的。测码伪距区别于卫星和接收机天线之间的几何距离，因为有卫星和接收机两者的钟差、以及信号传输介质(空气，电离层、对流层等)造成的误差。显然，信号传输路径也和几何路径稍有区别。传输介质不仅造成信号延迟，还使信号传输路径弯曲。

Ths GNSS signal emission time of the satellite is denoted by $t_e$, and the GNSS signal reception time of the receiver is denoted by $t_r$. In case of vacuum medium and error-free situation, the measured pseudorange is equal to the geometric distance and can be presented by 
$$R_t^3(t_r,t_e)=(t_r-t_e)c \tag{4.1}$$
where $c$ denotes the speed of light, and subscript r and superscript s denote the receiver and satellite, respectively. On the left-hand side, $t_r$ denotes the epoch at which the pseudorange is measured.
$t_e$ and $t_r$ are considered true emission time and reception time of the GNSS signal. Taking both the satellite and receiver clock errors into account, the pseudorange can be represented as 
$$R_t^3(t_r,t_e)=(t_r-t_e)c-(\delta_r-\delta_s)c \tag{4.2}$$
where $\delta t_r$ and $\delta t_s$ denote the clock errors of the receiver and satellite, respectively. The GNSS satellite clock error term $\delta t_s$ is indeed known through GNSS satellite orbit determination. The clock errors are usually modelled by polynomials of time. The constant term represents the bias and the linear term the drift of the clocks.

GNSS信号发射时刻记为$t_e$，GNSS信号接收时刻记为$t_r$ ，在真空介质和无误差情况下，测量得到的伪距等于几何距离并且表示为 公式4.1。c表示光速，下标r上标s分别代表接收机和卫星。在等式左边，t_r代表伪距测量出的时间。 $t_e$ 和$t_r$ 是GNSS信号发射和被接收的时刻。考虑卫星和接收机两者的钟差，伪距表示为 公式4.2 delta 分别表示接收机和卫星的钟差。GNSS钟差项事实上可以从GNSS卫星轨道测定。钟差通常表示为时间的多项式模型。常数项表示偏移量。


The geometric distance of the first term on the right-hand side of Eq.4.2 is given by 
$$\rho_r^3(t_r,t_e)=\sqrt{(x_s-x_r)^2+(y_s-y_r)^2+(z_s-z_r)^2} \tag{4.3}$$
where the satellite coordinate vector $(x_s,y_s,z_s)$ is a vector function of the time $t_e$, and the receiver coordinate $(x_r,y_r,z_r)$ is a function of the time $t_r$. Therefore, the geometric distance is indeed a function of two time variables. Furthermore, the emission time $t_e$ is unknown in practice. Denoting the transmitting time as $\Delta t$,there is 
$$\Delta t = t_r-t_e \tag{4.4}$$
For illustrating the transmitting time computation, the geometric distance can be generally written as 
$$\rho_r^s(t_r,t_e)=\rho_r^s(t_r)+\frac{\delta\rho_r^s(t_r)}{dt}\Delta t \tag{4.5}$$
The transmitting time of the signal travelling from the GNSS satellite to the reveiver is about 0.07 sec. THe geometric distance function on the right-land side of Eq. 4.5 can be expanded into a Talor series at the reception time $t_r$ with respect to the transmitting time by 
$$ \rho_t^s(t_r,t_e)=\rho_r^e(t_r)+\frac{d\rho_r^s(t_r)}{dt}\Delta t \tag{4.6}$$
where $d\rho_r^s(t_r)/dt$ denotes the time derivation of the radial distance between satellite and receiver. The second term on the right-hand side of Eq.4.6 is called the transimtting time correction. It is notable that the coordinates of GNSS antennas are usually given in the ECFF coordinate system. During the signal transmission, the receiver rotates with the Earth, therefore by computing the distance of Eq.4.3, the so-called Earth rotation correction has to be considered.


公式4.2 右边的第一项几何距离根据公式4.3给出。 卫星坐标向量（x,y,z）是一个时间t_e的函数，接收机坐标是t_r的函数。因此，几个距离是这两个变量的函数。此外，发射时间t_e 在实践中是未知的。传输时间记为Delta t，有公式4.4 ， 为了说明传输时间的计算，几个距离通常写成 公式4.5 . 信号从GNSS卫星接收机的传输时间大约是0.07秒。几何距离函数 公式4.5右边，可以泰勒展开成一个 在接收时刻处关于传输时间的函数 公式 4.6. dp/dt 表示卫星和接收机之间径向距离的导数。第二项是传输时间矫正。显然GNSS天线坐标通常在ECEF坐标系下给出。在信号传输过程中，接收机随着地球旋转，因此通过计算公式4.3的距离，所谓的地球旋转矫正被纳入了考虑中。


Taking the ionospheric effects, tropospheric effects, Earth tide and loading tide effrcts, multipath and relativistic effects as well as remaining errors into account, the pseudorange model Eq.4.2 can be completed by
$$R_r^s(t_r,t_e)=\rho_r^s(t_r,t_e)-(\delta t_r-\delta t_e)c+\delta_{ion}+\delta_{tro}+\delta_{tide}+\delta_{mul}+\delta_{rel}+\epsilon \tag{4.7}$$
Where the measured pseudorange is on the left-hand side, it equals to the geometric distance between the satellite at the emission time and the antenna at the reception- time plus or minus several corrections. The clock error corrections are scaled by the velocity of light $c$ . $\delta_{ion}$ and $\delta_{tro}$ denote the ionospheric and tropospheric effects of the station r. $\delta_{tide}$ denotes the Earth tide and ocean loading tide effects, $\delta_{mul}$ denotes the multipath effects, and $\delta_{rel}$ denotes the relativistic effects. The remaining errors are denoted by $\epsilon$. For concenience, unit meter is used for all terms and instrumental biases are omitted here.

The height of the GNSS satellite is about 20200km; thus, the GNSS signal transmitting time is about 0.07 sec. The Earth rotates duringthe signal transition. The angular velocity of the Earth ratation is about $15 arcsec sec^{-1}$. The ralated Rarth rotation correctio is about 1 arcsec (cf., Goad 1996). The effects of such a correction depend on the latitude of the station. At the equator, 1 arcsec ratation is equivalent to about 31 meters position displacement. The clock errors could be very big. There are examples where the negative pseudoranges are observed in practice.  

The above-discussed pseudorange model is generally valid for both C/A code and P code. The precision of the pseudorange measurements depends on the electronic abilities. Generally speaking, it is no problem nowadays to measure with precision up to 1% of the chip length. Therefore, the C/A code has a precision of about 3 m, and the P code 30 cm. The mentioned corrections will be discussed later in detail.  


考虑到电离层影响、对流层影响、固体潮与海洋潮、多路径效应和相对论效应以及残差等，伪距模型完整表示为公式4.7. 左边是观测到的伪距，它等于卫星发射到天线接收时刻的几何距离 加上或者减去几个修正量。钟差修正量按找光速比例缩放，电离层和对流层误差相对于测站r。潮汐效应表示地球固体潮和海洋潮。多路径效应，相对论效应。epslion 表示残差。方便起见，所有项使用单位m。仪器误差忽略。

GNSS卫星高度为大约20200千米。因此GNSS信号传输时间是大约0.07秒。地球在信号传输的同时旋转。角速度是大约15 arcsec 每秒。相应的旋转改正量是大约1 arcsec。这个改正值的影响取决于测站的纬度。在赤道上，1arcsec旋转是等效于大约31m位移。钟差可能非常大。实践中观测出有负伪距的例子。

以上关于伪距模型的讨论对C/A码和P码都有效。伪距测量的精度取决于电子技术。通常来说，当前的精度高达1%芯片长度。因此，C/A码精度是3m，P码是30cm。上述改正随后将详细讨论。


## 4.2 Carrier Phases

The carrier phase is a measure of  the phase of the received satellite signal relative to the receiver-generated carrier phase at hte reception time. The measurement is made by shifting the receiver-generated phase to track the received phase. The number of full carrier waves between the reveiver ans the satellite cannot be accounted for at the initial signal acquisition. Therefore, measuring the carrier phase is to measure hte fractional phase and to keep track of changes in the cycles. The carrier phase observable is indeed an accumulated carrier phase observation, The fractional carrier phase can be measured by electronics with precision better than 1% of the wavelength, which corresponds to millimetre precision. This is also the reason why the phase measurement is more precise than that of the code. A full carrier ware is called a cycle. The abiguous integer number of cucles in the carrier phase measurement is called ambiguity, The initial measuring has correct fractional phase and an arbitrary integer counter setting at the start epoch. Such an arbitrary initial setting will be adjusted to the correct one by modelling with ambiguity parameters.  
In the case of a vacuum medium and an error-free situation, the measured phase can be presented by 
$$\phi_r^s(t_r)=\phi_r(t_r)-\phi^s(t_r)+N_r^s \tag{4.8}$$
where subscript r and superscript s denote the receiver and satellite, respectively. $t_r$ denotes GNSS signal reception time of the receiver. $\phi_r$ denotes the phase of receiver's oscilllator. $\phi^s$ denotes the received signal phase of the satellite. $N_r^s$ is the ambiguity related to receiver r and satellite s.  


载波相位是测量在接收信号时刻，接收到的卫星信号的相位相对于接收机生成的载波相位。测量通过shift 接收机生成的相位来跟踪接收到的相位。在刚开始接收信号的时候，卫星和接收机之间完整载波的数量不能被考虑到。因此，测量载波就是在测量相位小数和跟踪周数的变化。载波相位观测变量是累积的相位观测。载波相位分数可以通过电子学技术手段测量，并且精度高于1%波长，相当于毫米级精度。这也是为什么相位测量比伪距测量更精确。一个载波称为一个周期。载波相位测量中模糊的整数周期称为模糊度(ambiguity)。起初的观测有正确的小数相位和任意的整数计数器在历元的起始段。这个任意数起始设置会通过模糊度模型参数被调整成正确的。
假如真空介质和无误差情况，测量的载波表示为 公式（4.8）。 下标r和上标s分别表示接收机和卫星。$t_r$表示GNSS信号被接收机接收的时刻。$\phi_r$表示接收机振荡器的相位。 $\phi^s$  表示接收到的卫星信号相位。$N_r^s$ 是接收机r和卫星s的模糊度。



There is an interesting property of the signal phase transmission, i.e., the received phase of the satellite signal at the reception time is exactly the same as the phase of the emitted satellite signal at the emission time (Remondi 1984; Leick 1995), i.e.: 
$$\phi^s(t_r)=\phi_e^s(t_r-\Delta t) \tag{4.9}$$ 
where $\phi_e^s$ denotes the satellite emitted phase and $\Delta t$ is GNSS signal transmitting time. This can be represented by 
$$\Delta t=\frac{\rho_r^s(t_r,t_e)}{t_r} \tag{4.10}$$ 
where $\rho_r^s(t_r,t_e)$ is geometric distance between  the satellite at the emission time $t_e$ , and the GNSS antenna at the reception time $t_r$, c is the speed of light. The Eq. 4.8 can be written as: 
$$ \Phi_r^s(t_r)=\Phi_r(t_r)-\Phi_e^s(t_r-\Delta t)+N_r^s \tag{4.11}$$ 
Suppose the initial time is zero and the received satellite signal and the reference carrier of the receiver have the nominal frequency $f$. Then one has 
$$ \Phi_r(t_r)=ft_r\tag{4.12}$$ 
$$ \Phi_e^s(t_r-\Delta t)=f(t_r-\Delta t)\tag{4.13}$$ 
Substituting Eqs. 4.1o ,4.12 and 4.13 into Eq. 4.11 gives 
$$\Phi_r^s(t_r)=\frac{\rho_r^s(t_r,t_s)f}{c}+N_r^s \tag{4.14}$$ 
Taking both the satellite and receiver clock errors into account, the carrier phase can be represented as 
$$\Phi_r^s(t_r)=\frac{\rho_r^s(t_r,t_s)f}{c}-f(\delta t_r-\delta t_s)+N_r^s\tag{4.15}$$ 
where $\delta t_r$ and $\delta t_s$ denoet the clock errors of the receiver and satellite, respectively. The frequency $f$ and wavelength $\lambda$ have the relation of 
$$c=f\lambda \tag{4.16}$$ 
Taking the ionospheric effects, tropospheric effects, Earth tide and loading tide effects, multipath and relativestic effects as well as remaining errors into account, the arrier phase model Eq. 4.15 can be completed by 
$$\Phi _t^s(t_r)=\frac{\rho _r ^s(t_r,t_e)}{\lambda}-f(\delta t_r -\delta t_e)+ N_r^s \\-\frac{\delta _{ino}}{\lambda}+\frac{\delta _{tro}}{\lambda}+\frac{\delta _{tide}}{\lambda}+\frac{\delta _{mul}}{\lambda}+\frac{\delta _{rel}}{\lambda}+\frac{\epsilon}{\lambda}\tag{4.17}$$ 
or 
$$\lambda\Phi _t^s(t_r)=\rho _r ^s(t_r,t_e) -f(\delta t_r -\delta t_e)+ N_r^s \\-\delta _{ino} +\delta _{tro}+\delta _{tide} +\delta _{mul}+\delta _{rel} +\epsilon\tag{4.18}$$ 
where the measured phase on the left-hand side with a factor of $\lambda$ equals the geometric distance between the satellite at the emission time and the antenna at the reception time plus or minus several corrections. The clock error corrections are scaled by the speed of light $c$. $\delta_{ion}$ and $\delta_{tro}$ denote the ionospheric and tropospheric effects of the station r. $\delta_{tide}$ denotes the Earth tide and ocean loading tide effects. The multipath and relativistic effects as well as remaining  errors are denoted by $\delta_{mul}$,$\delta_{rel}$, $\epsilon$ respectively. Equation 4.18 is convenient to use, because all terms have units of length (meter). It is notable that the sign of the ionospheric term is negative, whereas in the pseudorange model it is positive (see Sect. 4.1). This will be discussed later in Sect. 5.1 in detail.   

During GNSS signal tracking, the phase and the integer account are continuously modelled and frequently measured. In this way, the changing oscillator frequency is accounted for. Every time the phase is measured, the coefficients in the tracking loop model are updated (Remondi 1984) to ensure sufficient precision of measurement. 


在GNSS信号跟踪时，两位和整周计数是在连续不断的建模和频繁采样的。这样，就要考虑振荡器频率的变化。每一次测量相位，循环追踪模型的系数被更新来保证足够的测量精度。



## 4.3 Doppler Measurements

The Doppler effect is a phenomenon of frequency shift of the electromangnetic signal caused by the relative motion of the emitter and receiver. Supposing the emitted signal has the nominal frequency $f$, the radial velocity of the satellite related to the receiver is 
$$V_\rho=\vec{V}\cdot \vec{U_\rho}=\lvert \vec{V} \rvert cos \alpha\tag{4.19}$$ 
where $\vec{V}$ is the velocity vector of the satellite related to the receiver, $V=\lvert\vec{V}\rvert$ , $\vec{U_\rho}$ is the identity vector in the direction from the receiver to the satellite, $\alpha$ is the projection angle of the vector $\vec{V}$ to $\vec{U_\rho}$ (see FIg. 4.1), index $\rho$ is the distance from the receiver to satellite. Then the received signal has a frequency of 
$$f_r=f(1+\frac{V_\rho}{c})^{-1}\approx f(1-\frac{V_\rho}{c}) \tag{4.20}$$ 
where $c$ is the speed of light.


多普勒效应是发射器和接收器之间的相对运动导致的电磁信号的频率移动。假设发出的信号有名为f的频率，卫星相对于接收机的径向速度是 公式（4.19）,V是卫星相对于接收机的速度向量。U是从接收机到卫星的方向向量，α是向量V到U的投影角，rho 是接收机和卫星间距离。接收到的信号频率为 公式（4.20），c是光速。


The Doppler frequency shift is then 
$$f_d=f-f_r\approx f\frac{V_\rho}{\lambda}=\frac{V_\rho}{\lambda}=\frac{d\rho}{\lambda dt} \tag{4.21}$$ 
where $\lambda = (f/c)$ is the wavelength.

The Doppler count (or integrated Doppler) D is the historical observable of the TRANSIT satellite and is the integration of the frequency shift over a time interval (ca. 1 minute). If the time interval is selected small enough, the Doppler count is the same as the instantaneous frequency shift, or 
$$ D=\frac{d\rho }{\lambda dt} \tag{4.22}$$ 
The appproximately predicted Doppler frequency shift is required to get the satellite signal acquired. Prediction of $D$ is a part of the GNSS signal tracking process. THe predicted $D$ is used to predict the phase change first, and then the phase change is compared with the measured value to get the precise value of the Doppler frequency shift. The accimulated integer account of cycles is obtained through a polynomial fitting of a series of predicted phase changes and measured values (Remondi 1984). Therefore, the Doppler frequency shift is a by-product of the carrier phase measurements. However, the Doppler frequency shift is an independent observable and a measure of the instantaneous range rate.  

Notice that in an error free environment, $d\rho/(\lambda dt)$ is the same as $d\Phi/dt$ and $\Phi$ is the phase measurement discussed in Sect. 4.2. Then the model of Eq. 4.22 can be obtained by defferentiating the Eq. 4.17 with respect to the time t:
$$D=\frac{d\rho_r^s(t_r,t_e)}{\lambda dt}- f\frac{d\beta}{dt}+\delta f +\epsilon  \tag{4.23}$$ 
where $\beta$ is the term of clock error $(\delta t_r-\delta t_s)$, $\delta _f$ is the frequency correction of the relativistic effects and $\epsilon$ is error. Effects with low frequency properties such as ionosphere, troposhere, tide, and multipath effects are cancelled out.
$$\Phi _t^s(t_r)=\frac{\rho _r ^s(t_r,t_e)}{\lambda}-f(\delta t_r -\delta t_e)+ N_r^s \\-\frac{\delta _{ino}}{\lambda}+\frac{\delta _{tro}}{\lambda}+\frac{\delta _{tide}}{\lambda}+\frac{\delta _{mul}}{\lambda}+\frac{\delta _{rel}}{\lambda}+\frac{\epsilon}{\lambda}\tag{4.17}$$

多普勒频率移动是 公式（4.21），lambda=f/c 是波长。
多普勒计数 D 是卫星TRANSIT 的历史观测量 并且是在一个时间间隔的频率移动的集成。如果时间间隔选择得组后小，多普勒计数和瞬时频率移动相同。公式（4.22）。多普勒频移的近似预测需要后天的（已获得的）卫星信号。D的预测是GNSS信号追踪过程的一部分。D 用来预测相位改变，以及将相变值与测量值进行比较，以获得多普勒频移的精确值。周期累积整数通过一系列预测的相变和测量值的多项式拟合获得。因此，多普勒频移是载波相位测量的副产品。然而，多普勒频移是一项独立的观测，量也是瞬时范围速率的量度。


### Homework

please design a method of integrated pseudorange, carrier phase, Doppler observables for a specific application ,where the advantages of three kings of observables are fully used.

For example, combing hte pseudorange and carrier phase of single frequency observables to eliminate ionospheric errors; using Doppler observables to detect cycle slips in the carrier phase observables.  



---


# Linear Combination of Measurements

## Questions
1. Why do we have linear Combination of Measurements?


2. Linear combination of measurements?

3. What are single difference, double difference and triple difference?


4. What are Linear combination of same type and different frequency measurements?


5. What are Linear combination of different type measurements?


## Linear combination of measurements

1. Linear combination of same type and same frequency measurements.

Eliminate satellite clock offset,receiver clock offset and ambiguity, etc.

2. Linear combination of same type ans different frequency measurements.

Eliminate he influence of ionosphere, helpful for ambiguity decomposition and data editing of medium-length baselines.

3. Linear combination of different type measurements.

Helpful for ambiguity decomposition in relative positioning, and weakens the influence of ionosphere in SPP.

## Linear cimbination of same type and same frequency measurements



## Homework

1. Please find out a new method or technology to improve the accuracy of pseudorange measurement.
2. How to integrate pseudorange, carrier phase and Doppler obs. for a special application?



---

# Quality Analysis of Measurements 

## Questions

1. Why do we have quality analysis of measurements?
2. What are the quality analysis softwares?
3. What are the quality analysis indicators?


---

# 载波相位测量

## 课程内容

- 载波相位的基本概念
- 载波重建的概念及方法
- 载波相位测量的原理（key）
- 课程小结与思考

## 1. 载波的基本概念
**载波（carrier)**
在无线电铜线中，为了更好的传送信息，并不直接发射这些信息，而是将其调制在高频载波上进行播发，可**运载调制信号的高频振荡波**称为载波。

在全球卫星导航系统中，测码伪距和导航电文就是通过调制到 L波段 进行播发。
## 载波的调制方式
二进制调相。
码状态和载波相乘。
载波相位局部发生偏转，载波信号不再连续。

## 利用载波相位测量的原因 
载波作为测距信号来使用。
载波相位测距精度：2~3mm，比伪距高2~3个数量级。

## 载波重建
### 基本概念
在进行载波相位测量之前，设法将调制在载波上的测距码和导航电文去掉（相位解调），将非连续的载波信号恢复成连续的载波信号。

### 码相关法


## 载波相位测量的原理
### 基本原理

### 实际观测值

整周计数：每当拍品信号的相位变化一周，计数器的计数加1，计数器记录的整波段数。

整周跳变：整周计数出现系统偏差而小数部分仍然保持正确的现象，简称周跳。

### 整周模糊度

载波相位观测值并非完整的卫星-接收机距离。表征完整的卫地距的载波相位观测值还包含一个整周未知数$N_0$

$$\phi _i=\phi _i +N_0=Int(\phi)_i+Fr(\phi)_i+N_0$$ 
整周模糊度：首观测值时，载波相位与基准相位差对应的整周未知数；只要不发生周跳，后续观测$N_0$将不变（常数）
### 观测方程

完整的载波（周）：
$$\tilde{\varphi _i}=\varphi _i + N_0 \tag{1}$$
完整的载波（米）：
$$\tilde{\rho}=\lambda \cdot \tilde{\varphi _i}=\lambda \cdot (\phi _i +N_0)\tag{2}$$
伪距观测方程（米）：
$$\tilde{\rho}=\rho - \delta _{t_R} \times c + \delta _{t^s} \times c - V_{ion}-V_{trop}\tag{3}$$
将（2）式代入（3）式：
$$\lambda \cdot \phi _i = \rho - \delta _{t_R} \cdot c + \delta _{t^S} \times c +V_{ion}-V_{trop} - \lambda \cdot N_0 \tag{4}$$
其中 
$\rho$：几何距离
$\delta_{t_R}$：接收机钟差
$\delta_{t^s}$：卫星钟差
$V_{ion}$：电离层延迟
$V_{trop}$：对流层延迟
$N_0$：整周未知数

## 解惑
是什么原因使得定位精度显著提高了？

测码伪距，测距精度低。
$$\rho=\tau \cdot c = \Delta t \cdot c$$

载波相位，测距精度高。

## 思考
结合本节课所讲载波观测方程内容，思考如下问题：
某一瞬间，接收机同时观察到4颗北斗卫星，若仅采用载波相位观测值，能否实现快速定位？

答：不能。
载波相位测量的 ***难点*** 在于**实时的、快速而准确的整周模糊度**

## 载波相位测量

[载波相位测量](https://baike.baidu.com/item/载波相位测量/8871041)





