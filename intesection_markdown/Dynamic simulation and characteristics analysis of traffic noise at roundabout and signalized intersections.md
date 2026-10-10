# Dynamic simulation and characteristics analysis of traffic noise at roundabout and signalized intersections 

Feng Li ${ }^{\mathrm{a}}$, Yushan Lin ${ }^{\mathrm{b}}$, Ming Cai ${ }^{\mathrm{b}, \mathrm{c}, *}$, Canyi Du ${ }^{\mathrm{a}}$<br>${ }^{\mathrm{a}}$ School of Automotive Engineering, GuangDong Polytechnic Normal University, Guangzhou 510665, China<br>${ }^{\mathrm{b}}$ Research Center of Intelligent Transport Systems, School of Engineering, Sun Yat-sen University, Guangzhou 510006, China<br>${ }^{\mathrm{c}}$ Key Laboratory of Intelligent Transportation System of Guangdong Province, Guangzhou 510006, China

ARTICLE INFO

Article history:
Received 25 September 2016
Received in revised form 18 January 2017
Accepted 19 January 2017
Available online 3 February 2017

Keywords:
Traffic noise
Dynamic simulation
Roundabout
Intersection


#### Abstract

Traffic noise prediction is an important topic for traffic environment planning in cities. The complex traffic flow at road intersections makes the prediction of traffic noise challenging. In this paper, a dynamic traffic noise simulation method based on microscopic traffic simulation is used to study the traffic noise near roundabout and signalized intersections. A vehicle noise emission model that considers the effect of acceleration is established using an experimental method. The accuracy of the model is verified by comparison with measured data. Traffic noise near roundabout and signalized intersections under different traffic volume levels is simulated, and the results are compared. Some significant relations between traffic noise and traffic volume are obtained, and the mechanisms are analyzed. The results show that traffic noise reaches an upper limit when traffic is saturated, and the noise energy contribution of the exit lane is far greater than that of the entrance lane.


© 2017 Elsevier Ltd. All rights reserved.

## 1. Introduction

The development of road traffic has produced serious noise pollution in cities. Long-term living and working in a high-noise environment leads to serious health problems [1,2]. Traffic noise prediction is a precondition of traffic noise control and an important task of environmental management. Many research works on traffic noise prediction have been performed, and various traffic noise prediction models have been established. The main traffic noise prediction models can be classified into two types: steadystate calculation models [3] and dynamic simulation models [4]. Steady-state calculation models can be applied to predict the average traffic noise over a period of time, such as the FHWA highway traffic noise prediction model in the United States [5], the CRTN model in the United Kingdom [6], the ASJ RTN-model in Japan [7], the CNOSSOS model in Europe [8,9], models for interrupted traffic [10,11], and models for intersections [12,13]. Dynamic simulation models that combine microscopic traffic simulations can be applied to predict not only the average traffic noise over a period of time but the second-by-second dynamic changes of the noise level

[^0][14-17]. Dynamic approaches have been used for traffic noise simulation on intersections and roundabouts.

Almost all steady-state models and dynamic models are based on a vehicle noise emission model, which is one of the key factors affecting the accuracy of the model. Most vehicle noise emission models are obtained by experimental measurements. Vehicle noise emission is usually expressed by a linear regression equation related to vehicle speed, and few models have considered the effect of vehicle acceleration. This approach may result in error, especially for road segments where vehicles are accelerating or decelerating. Although some studies have considered the effect of acceleration, acceleration was not incorporated into the linear regression equation [18,19].

Roundabouts and signalized intersections are two common forms of road junctions in urban road networks. The varying state of vehicle motion near an intersection makes traffic noise calculations challenging. The prediction of traffic noise near intersections has attracted wide attention, and many prediction models and methods have been proposed [20-24]. However, the influence of the degree of traffic saturation on the noise and the difference in noise emission between different types of lanes is not clear. In reality, traffic speed and volume cannot be infinitely increased, which means traffic noise also has a maximum value. Therefore, finding the relationship between traffic saturation and traffic noise is important to predict the maximum value of noise. Furthermore,
finding the difference on traffic noise emission between different types of lanes is helpful to analyze the main sources of noise and make the traffic noise control more targeted.

The purpose of this paper is to establish a vehicle noise emission model that considers the effect of vehicle acceleration based on an experimental method and to combine the emission model with a microscopic traffic simulation tool to simulate traffic noise near roundabout and signalized intersections. Additionally, the differences in traffic noise between the two types of intersection are explored, and the influences of the degree of traffic saturation and lane type on traffic noise are analyzed.

## 2. Dynamic traffic noise simulation method

To study the fluctuation of traffic noise, we use a dynamic traffic noise simulation method to simulate the dynamic noise change. The dynamic traffic noise simulation method is composed of three modules, a microscopic traffic simulation tool, a vehicle noise emission model and a sound propagation model (Fig. 1). The microscopic traffic simulation tool is applied to simulate the traffic flow on the road network and to obtain status data of the vehicles, including the type, position, speed and acceleration of each vehicle at each time-step of the simulation. The vehicle type, speed and acceleration data are input into the vehicle noise emission model to calculate the noise emission of each vehicle at a specific moment. The vehicle position and noise emission are input into the sound propagation model to calculate the individual contribution of each vehicle at the receiver. Thus, the instantaneous sound pressure level at the receiver can be obtained by summing the contribution of each vehicle at the corresponding time-step. A series of 1-s resolution sound pressure levels are obtained by running the simulation with a time-step of 1 s. Then, the time equivalent sound level $L_{\text {eq }}$, and the cumulative statistical sound levels $L_{10}, L_{50}$, and $L_{90}$, can be calculated.

In the traffic noise calculation, each vehicle on the road network is regarded as a point sound source. The sound pressure level of the $i$-th second at the receiving point that is emitted by the $j$-th car can be expressed as:

$$
L_{i, j}=L_{0}+L_{D(i, j)}+L_{\text {Other }(i, j)}
$$

where $L_{0}$ denotes the sound pressure level of a single vehicle measured at a standard distance and can be considered a vehicle noise emission model, $L_{D(i, j)}$ denotes the distance attenuation, and $L_{\text {Other }(i, j)}$ denotes the noise attenuation caused by other factors, such as air absorption, ground effect, and shielding by barriers. $L_{D(i, j)}$ and $L_{\text {Other }(i, j)}$ depend on the sound propagation model.

The distance attenuation can be expressed as:

$$
L_{D(i, j)}=10 \log _{10} \frac{d_{0}^{2}}{d_{i, j}^{2}}=10 \log _{10} \frac{d_{0}^{2}}{\left(x_{i, j}-x_{0}\right)^{2}+\left(y_{i, j}-y_{0}\right)^{2}}
$$

where $d_{0}$ denotes the reference distance when measuring the noise emission of a single vehicle, which is 7.5 m in the Chinese Standard "GB 1495-2002" [25], $d_{i, j}$ denotes the distance from the vehicle to the receiving point, $x_{i, j}$ and $y_{i, j}$ denote the coordinates of the vehicle, and $x_{0}$ and $y_{0}$ denote the coordinates of the receiving point.

By summing the sound energy of each vehicle at a time-step, we can obtain the instantaneous sound level:

$$
L_{i}=10 \log _{10}\left(\sum_{j=1}^{m_{i}} 10^{0.1 L_{i, j}}\right)
$$

where $m_{i}$ is the number of vehicles on the road at the $i$-th second.
In this work, we used Paramics 6.5 (a microscopic traffic simulation software) as to simulate the traffic on the road network. The software includes a vehicle generator that will generate some simulated vehicles randomly at any time-step based on the traffic OD of the road network. The generated vehicles will travel on the road network following the vehicle-following model, lane changing rules, signal control rules, and so on until they leave the road network. In the simulation process, there may be different numbers of vehicles running on the studied road network at different timestep. We developed a dynamic link library plug-in using C programming language to connect the Paramics software and collect the number of vehicles $m_{i}$ and their driving status data at each time-step. Then the traffic noise at each time-step during the traffic simulation is calculated based on these dynamic traffic data.

## 3. Experiment for the noise emission of a single vehicle

We used the experimental method to measure the noise emission of a single vehicle and to establish a vehicle noise emission model. The experimental scenario was set according to the Chinese standard GB 1495-2002 (Limits of external noise of an accelerating vehicle and relevant measurement methods) [25]. The experiments were performed on straight roads with low traffic and approximately 100 m without obvious reflectors. Three types of road segment (acceleration, deceleration and constant speed road segments) were chosen to measure the vehicle noise in different states of motion. The sound level meters were placed 1.2 m above the ground and 7.5 m from the traffic lane on each side of the road. The speed of each vehicle was recorded by radar speed indicators and video cameras. The acceleration of the vehicle was calculated based on the velocities when the vehicle passed two neighboring observation points.

The vehicles were classified into three types: light vehicles, with a length less than 6 m and a weight less than 2 tons; heavy vehicles, with a length greater than 10 m or a weight greater than 12 tons; and medium vehicles, i.e., anything other than a light vehicle or heavy vehicle. The noise emissions of 3372 vehicles (including 2451 light vehicles, 375 medium vehicles and 546 heavy vehicles) were measured as they passed a sound level meter. The noise emission data of 4 driving states were collected, including accelerating, decelerating, steady driving and idling. Linear regression was used to generate a vehicle noise emission model, as shown in Table 1. For steady driving noise, we established a relationship between noise emission and speed; for accelerating and decelerating noise, we established a relationship between noise emission and speed and acceleration; and for idling noise, we used a constant to represent the noise emission. The correlation coefficients were high, except the fitted formulas for medium vehicle acceleration and heavy vehicle acceleration and deceleration. To ensure the accuracy of the model, we conducted an F test and $t$ test for the fitting formulas. At the 0.05 significance level, all test values were greater than the critical value, which means the fitting formulas are credible.

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-02.jpg?height=202&width=1436&top_left_y=2366&top_left_x=332)
Fig. 1. Principle diagram of the dynamic traffic noise simulation method.

Table 1
Measurement results of single vehicle noise emission; $V$ is speed $(\mathrm{km} / \mathrm{h})$ and a is acceleration $\left(\mathrm{m} / \mathrm{s}^{2}\right)$.
| Vehicle type | Driving state | Sample size | Fitting formula (in dBA) | Correlation (r) |
| :--- | :--- | :--- | :--- | :--- |
| Light vehicle | Accelerating | 779 | $L_{O S}=35.56+19.4 \lg V+1.04 a$ | 0.669 |
|  | Decelerating | 550 | $L_{O S}=24.86+25.75 \lg V+0.33 a$ | 0.860 |
|  | Steady driving | 1058 | $L_{O S}=28.12+24.77 \lg V$ | 0.810 |
|  | Idling | 64 | $L_{0 S}=53.79$ |  |
| Medium vehicle | Accelerating | 92 | $L_{0 M}=60.13+7.76 \lg V+0.76 a$ | 0.360 |
|  | Decelerating | 96 | $L_{0 M}=44.99+16.62 \lg V-0.32 a$ | 0.614 |
|  | Steady driving | 167 | $L_{0 M}=16.8+36.32 \lg V$ | 0.802 |
|  | Idling | 20 | $L_{0 M}=58.49$ |  |
| Heavy vehicle | Accelerating | 202 | $L_{0 L}=68.92+6.44 \lg V+2.58 a$ | 0.464 |
|  | Decelerating | 165 | $L_{0 L}=61.9+10.21 \lg V+0.16 a$ | 0.442 |
|  | Steady driving | 119 | $L_{0 L}=33.35+28.56 \lg V$ | 0.746 |
|  | Idling | 60 | $L_{0 L}=63.32$ |  |


## 4. Model validation

The model was used to calculate the traffic noise of a roundabout and a signalized intersection, and the accuracy of the model was tested with the measured data. Field measurements for model validation were taken at the roundabout intersection of Shiliang Road and Xihuan Road and at the signalized intersection of Fude Road and Dexian Road in Guangzhou, China. Four noise monitoring points were used at each intersection, and the locations are shown in Figs. 2 and 3. These points were chosen in areas without buildings, so the influence of reflections is reduced. The monitoring time was from 15:00 to 18:00. The noise levels were recorded by sound level meters mounted 1.2 m above the ground. The traffic volume from the four directions of each intersection was recorded by video camera. Other parameters of the road, such as the number of lanes, the geometric dimensions, and signal time, were also measured. The hourly traffic volume of light, medium, and heavy vehicles was determined via video. The period from 15:00 to 16:00 was considered the mean traffic hour, and 17:00 to 18:00 was considered rush hour. Therefore, the traffic was increasing from 15:00 to 18:00, as shown in Table 2. The traffic distributions of each direction of the intersections were not uniform. The traffic on Shiliang Road was greater than that on Xihuan Road at the roundabout, and the traffic on Dexian Road was greater than that on Fude Road at the signalized intersection.

A simulated roundabout and a simulated signalized intersection were established based on the measured geometric dimension data, traffic volume data, and traffic control schemes in real intersections shown in Figs. 2 and 3. In the process of simulation, the simulated vehicles were generated by the vehicle generator based

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-03.jpg?height=1025&width=1449&top_left_y=1544&top_left_x=286)
Fig. 2. Aerial map of the roundabout at Shiliang Road and Xihuan Road.

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-04.jpg?height=1012&width=1449&top_left_y=230&top_left_x=321)
Fig. 3. Aerial map of the signalized intersection at Fude Road and Dexian Road.

Table 2
Measured traffic volume for the roundabout and the signalized intersections (veh).
| Direction | Roundabout at Shiliang Road and Xihuan Road |  |  | Intersection at Fude Road and Dexian Road |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | 15:00-16:00 | 16:00-17:00 | 17:00-18:00 | 15:00-16:00 | 16:00-17:00 | 17:00-18:00 |
| East-West | 193 | 272 | 325 | 116 | 154 | 197 |
| East-North | 90 | 121 | 152 | 65 | 88 | 92 |
| East-South | 127 | 158 | 195 | 33 | 54 | 68 |
| West-East | 226 | 289 | 354 | 135 | 166 | 254 |
| West-North | 114 | 157 | 163 | 48 | 59 | 93 |
| West-South | 73 | 91 | 139 | 142 | 153 | 208 |
| North-South | 96 | 129 | 147 | 312 | 395 | 542 |
| North-East | 42 | 51 | 68 | 96 | 167 | 188 |
| North-West | 56 | 72 | 75 | 189 | 243 | 307 |
| South-North | 62 | 86 | 98 | 143 | 221 | 268 |
| South-East | 65 | 101 | 124 | 76 | 109 | 138 |
| South-West | 30 | 41 | 66 | 158 | 178 | 284 |
| Total | 1174 | 1568 | 1906 | 1513 | 1987 | 2639 |


on the traffic OD of the road network, and then traveled following the fixed vehicle-following model, the lane changing rules, and the traffic control schemes. For the signalized intersection, the simulated vehicles accelerated through the intersection according to the signal control scheme. For the roundabout, the simulated vehicles would line up to wait for security clearance to enter the ring road, and then traveled steady without any disturbances, but would slow down and accelerated to ensure safety when disturbed by other vehicles. The accelerations of light, medium, and heavy vehicles were set to $2.5 \mathrm{~m} / \mathrm{s}^{2}, 1.8 \mathrm{~m} / \mathrm{s}^{2}$ and $1.2 \mathrm{~m} / \mathrm{s}^{2}$, and the decelerations were set to $4.5 \mathrm{~m} / \mathrm{s}^{2}, 4.0 \mathrm{~m} / \mathrm{s}^{2}$ and $3.5 \mathrm{~m} / \mathrm{s}^{2}$.

The traffic noise at the monitoring points were calculated. The time equivalent sound level $L_{\text {eq }}$, and the cumulative statistical sound levels $L_{10}, L_{50}$, and $L_{90}$, are taken statistics every 20 min . The comparison of the simulated noise levels and the measured noise levels is shown in Figs. 4 and 5. For both the roundabout and signalized intersections, the simulated values of $L_{\text {eq }}, L_{10}, L_{50}$, and $L_{90}$ are in good agreement with the measured values, with a mean absolute error less than 2 dBA. The simulated $L_{90}$ is slightly less than the measured value because there was some background noise in the measurement field, which is neglected in the calculation. Nevertheless, the accuracy of the model is acceptable. The results indicate that the model can be used to predict more complex evaluation parameters, such as the standard deviation of traffic noise $(\sigma)$ and the noise pollution level $\left(L_{\mathrm{NP}}\right)$, which is calculated by:

$$
L_{\mathrm{Np}}=L_{\mathrm{eq}}+2.56 \sigma
$$

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-05.jpg?height=1189&width=1490&top_left_y=226&top_left_x=267)
Fig. 4. Comparison of the simulated and measured $L_{\mathrm{eq}}, L_{10}, L_{50}$ and $L_{90}$ at the roundabout with a 20 -min simulation period for each traffic level.

## 5. Simulation and comparison of traffic noise near roundabout and signalized intersections

To compare the differences in traffic noise between roundabout and signalized intersections, we study two equal-scale intersections (one roundabout and one signalized intersection) and simulate the traffic noise. The entrances and exits of the two intersections are two-lane roads that are 7.4 m wide, and the speed limit of all the lanes is 60 km/h. The length of the road segment in each direction from the intersection is 300 m . The circle radius of the roundabout is 20 m. The coordinate origin is located at the center of the intersection, as shown in Figs. 6 and 7. The total traffic demand of the intersections is varied from 360 to 5400 PCU/h in 360 PCU/h steps. The traffic demand is evenly distributed in each direction, i.e., the traffic demand from each entrance to the other three directions is increased from 30 to 450 PCU/h in 30 PCU/h steps. For the signalized intersection, we use the F. Webster timing method to set a 4-phase traffic signal. The signal cycle is calculated by:

$$
C=\frac{1.5 L+5}{1-Y}
$$

where $L$ is the cycle lost time (the amber time is $3 \mathrm{~s}, 3 \times 4=12 \mathrm{~s}$ ), and $Y$ is the total flow rate. The green time for each phase is:

$$
g_{i}=\frac{(C-L) \cdot y_{i}}{Y}
$$

where $y_{i}$ is the flow rate of phase $i$. The saturation traffic volume of the intersection is set to 3600 PCU/h. The maximum signal period is limited to 150 s, with 37 s of green time for each phase when the traffic demand is greater than 3240 PCU/h. The specific signal timing is shown in Table 3. The traffic flow from only one of the entrances is allowed to go straight or turn left in one phase; beyond that, all vehicles are allowed to turn right at any time.

The results of the traffic flow simulation show that the traffic capacity of the signalized intersection is greater than that of the roundabout. The simulated saturation traffic volume of the signalized intersection is approximately 4000 PCU/h, and that of the roundabout is approximately 3500 PCU/h, as shown in Tables 3 and 4. When the traffic reaches the saturation volume, the simulated traffic volume cannot be increased further, regardless of how much the traffic demand increases. The vehicle density of the entrance and exit lanes increases with increasing traffic before reaching the saturation volume. When the traffic is saturated, the density of the entrance lane reaches a maximum of approximately 145 PCU/km, and the exit lane reaches a maximum of approximately 19 PCU/km for both the signalized intersection and the roundabout. The lane speeds also reflect this result. The average speed of the entrance lanes decreases with increasing traffic and eventually stabilizes at approximately 6 km/h, while the average speed of the exit lanes is maintained at approximately 50 km/h. The average speed of the ring lane of the roundabout also decreases with increasing traffic but eventually stabilizes at approximately 24 km/h.

Six pairs of corresponding observation points on the two intersections (the locations are shown in Figs. 6 and 7) are selected to calculate $L_{\text {eq }}$ and $L_{\text {NP }}$. The results are shown in Fig. 8 . Overall, $L_{\text {eq }}$ and $L_{\mathrm{NP}}$ are higher at the signalized intersection than at the round-

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-06.jpg?height=1156&width=1488&top_left_y=226&top_left_x=301)
Fig. 5. Comparison of the simulated and measured $L_{\mathrm{eq}}, L_{10}, L_{50}$ and $L_{90}$ at the signalized intersection with a 20-min simulation period for each traffic level.

about, especially at $\mathrm{P}_{2}$, because when a vehicle passes through the signalized intersection, there is an orderly, significant deceleration and acceleration process, resulting in a significant increase in noise and standard deviation. When a vehicle passes through the roundabout, the speed is slowed and the amplitude of acceleration and deceleration is smaller. When the traffic is non-saturated, $L_{\mathrm{eq}}$ increases with traffic OD. When the traffic is saturated, $L_{\mathrm{eq}}$ no longer increases but decreases with increasing traffic congestion. There is a maximum value of $L_{\mathrm{eq}}$ that occurs near the saturation point of the traffic volume. The maximum $L_{\text {eq }}$ occurs at 4000-4300 PCU/h for the signalized intersection and at 3600-4000 PCU/h for the roundabout. Because the standard deviation of the noise decreases with increasing traffic volume, $\mathrm{L}_{\mathrm{NP}}$ has undergoes minimal change with increasing traffic. Therefore, when traffic is low, $L_{\text {eq }}$ is small, but traffic noise pollution cannot be ignored.

The probability distribution statistics for the noise level values are calculated, and the results for $\mathrm{P}_{6}$ under different traffic conditions are compared in Fig. 9. We use $\mathrm{P}_{6}$ as because it is far from the center of the intersection, and the impact of some random factors can be excluded. The greater the traffic volume, the more concentrated the noise probability distribution, and the smaller the noise standard deviation. The noise probability distribution of the roundabout is more concentrated than that of the signalized intersection. The probability distribution curves of the signalized intersection are to the right of those of the roundabout, indicating that the traffic noise level at the signalized intersection is higher under the same traffic volume. The same trends exists for $L_{\mathrm{eq}}$ and $L_{\mathrm{NP}}$, as shown in Fig. 8.

Spatial distribution maps of the roundabout and signalized intersections with a 200 m by 200 m range and 1.5 m height are shown in Figs. 10 and 11. In this example, due to the large computation range, we consider the ground effect in addition to distance attenuation. According to international standard ISO 9613 [26], $L_{\text {Other }(i, j)}$ in Eq. (1) can be expressed as:

$$
L_{\text {Other }(i, j)}=A_{g r}=4.8-\left(2 h_{m} / d_{i, j}\right)\left[17+\left(300 / d_{i, j}\right)\right] \geqslant 0 \mathrm{~dB}
$$

where $A_{\mathrm{gr}}$ is the ground effect; $h_{m}$ is the mean height of the propagation path above the ground, in meters; and $d_{i, j}$ is the distance from source to receiver, in meters. Negative values for $A_{\mathrm{gr}}$ from Eq. (7) shall be replaced by zeros. The noise distribution over each road segment is asymmetric with respect to the center line of the road. The noise over the exit lane is greater than that over the corresponding entrance lane because the traffic in the exit lane is accelerating and produces greater noise emission according to the vehicle noise emission model. Due to the reduction of vehicle speed near the intersection, the noise near the intersection is lower than at the opposite end of the road segment. This point is particularly evident for the noise distribution on the roundabout.

## 6. Discussion

Traffic speed and volume are two key factors that affect traffic noise, and there is a complicated relationship between the two factors. Almost all traffic noise prediction models take traffic speed and volume as basic input parameters, but few models consider the relationship between traffic speed and volume [27,28]. The potential relationship between traffic speed and volume is

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-07.jpg?height=1120&width=1148&top_left_y=228&top_left_x=441)
Fig. 6. Map of the simulated roundabout and the locations of the noise receivers.

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-07.jpg?height=1145&width=1148&top_left_y=1425&top_left_x=441)
Fig. 7. Map of the simulated signalized intersection and the locations of the noise receivers.

Table 3
Results of the simulated traffic flow for the signalized intersection.
| Total OD (PCU/h) | Simulated traffic volume (PCU/h) | Green time (s) | Density of entrance lane (PCU/km) | Density of exit lane (PCU/km) | Speed of entrance lane (km/h) | Speed of exit lane (km/h) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 360 | 342 | 4 | 3 | 1 | 43.3 | 50.7 |
| 720 | 696 | 4 | 2 | 2 | 40.6 | 50.0 |
| 1080 | 1092 | 5 | 6 | 6 | 38.7 | 48.6 |
| 1440 | 1428 | 7 | 6 | 5 | 36.7 | 49.2 |
| 1800 | 1914 | 9 | 9 | 5 | 33.2 | 49.4 |
| 2160 | 2142 | 11 | 12 | 12 | 28.8 | 50.1 |
| 2520 | 2586 | 16 | 17 | 9 | 19.6 | 49.7 |
| 2880 | 3018 | 26 | 27 | 10 | 14.9 | 50.9 |
| 3240 | 3432 | 37 | 52 | 20 | 12.7 | 51.7 |
| 3600 | 3762 | 37 | 61 | 21 | 12.0 | 50.9 |
| 3960 | 3990 | 37 | 138 | 22 | 6.2 | 50.8 |
| 4320 | 4002 | 37 | 145 | 19 | 6.0 | 51.5 |
| 4680 | 4062 | 37 | 148 | 19 | 5.7 | 52.0 |
| 5040 | 4014 | 37 | 146 | 19 | 5.2 | 51.4 |
| 5400 | 4026 | 37 | 146 | 19 | 5.4 | 52.0 |


Table 4
Results of the simulated traffic flow for the roundabout.
| Total OD (PCU/h) | Simulated traffic volume (PCU/h) | Density of entrance lane (PCU/km) | Density of exit lane (PCU/km) | Speed of entrance lane (km/h) | Speed of exit lane (km/h) | Speed of ring lane (km/h) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 360 | 342 | 1 | 1 | 50.9 | 50.3 | 40.5 |
| 720 | 696 | 1 | 2 | 52.5 | 50.3 | 43.3 |
| 1080 | 1092 | 4 | 5 | 48.4 | 50.0 | 41.7 |
| 1440 | 1500 | 3 | 8 | 47.8 | 50.6 | 38.3 |
| 1800 | 1902 | 8 | 9 | 46.2 | 50.7 | 36.5 |
| 2160 | 2142 | 10 | 15 | 44.3 | 50.7 | 35.2 |
| 2520 | 2568 | 22 | 15 | 36.0 | 50.7 | 34.5 |
| 2880 | 2904 | 27 | 16 | 25.4 | 50.5 | 32.6 |
| 3240 | 3300 | 38 | 17 | 21.2 | 50.7 | 28.3 |
| 3600 | 3480 | 133 | 18 | 10.3 | 50.7 | 25.7 |
| 3960 | 3522 | 143 | 18 | 6.3 | 50.6 | 23.8 |
| 4320 | 3504 | 142 | 19 | 6.0 | 50.5 | 24.2 |
| 4680 | 3528 | 145 | 18 | 6.0 | 50.7 | 23.9 |
| 5040 | 3534 | 143 | 19 | 5.9 | 50.5 | 23.8 |
| 5400 | 3540 | 143 | 18 | 5.9 | 50.7 | 23.7 |


considered by the microscopic traffic simulation in this work. Traffic speed and volume cannot be infinitely increased, which means traffic noise also has a limit. From the results of the previous section, we know that when the traffic is saturated, the noise reaches a maximum. We define an evaluation parameter to investigate the mechanism: the level of the average sound power per meter per lane and per second, denoted by $L_{\text {wpl }}$, is used to evaluate the intensity of traffic noise in a lane. The sound power level of vehicles $\left(L_{\text {veh }}\right)$ can be calculated based on the vehicle noise emission model in Section 3:

$$
L_{v e h}=L_{0}+\log _{10}\left(2 \cdot \pi \cdot 7.5^{2}\right)=L_{0}+25.5
$$

where $L_{0}$ is the sound pressure level of a single vehicle measured at 7.5 m. The total sound power of a road in a period of time can be calculated by:

$$
\frac{W}{W_{o}}=\sum_{k=1}^{s} \sum_{j=1}^{n} \sum_{i=1}^{m_{j, k}} 10^{0.1 \cdot L_{v e h, i, j, k}}
$$

where $W_{o}=10^{-12}$ (Watts) - reference sound power; $s$ denotes the statistical time (in seconds); $n$ denotes the number of lanes; and $m_{j, k}$ denotes the number of vehicles in the lane at the $j$-th lane and the $k$-th second. Finally, $\mathrm{L}_{\mathrm{wpl}}$ can be calculated by:

$$
L_{w p l}=10 \log _{10}\left(\frac{W}{s \cdot n \cdot l \cdot W_{o}}\right)
$$

where $l$ denotes the length of the lane, in meters.

The $L_{\text {wpl }}$ of the entrance, exit and ring lane of the roundabout and the entrance and exit lane of the signalized intersection are calculated and compared, as shown in Fig. 12. The saturated traffic volume is about 3500 PCU/h at the roundabout and about 4000 PCU/h at the signalized intersection. When the traffic is saturated, the average speed of the exit lanes is kept at around 50 km/h, the speed of the entrance lane drops below 6 km/h, and the speed of the ring road is about 24 (see Tables 3 and 4). The $L_{\mathrm{wpl}}$ of the exit lane is greater than that of the entrance lane and ring lane, and the gap increases with traffic. This is related to the acceleration process and higher speed in the exit lane. The $L_{\text {wpl }}$ curves of the exit lane of the roundabout are in agreement with those of the signalized intersection, increasing with traffic and then maintaining a high level when the traffic is saturated. The $L_{\text {wpl }}$ curves of the entrance lanes and ring lane decrease to different extents when traffic is saturated. The largest reduction occurs in the ring lane of the roundabout, and the smallest reduction occurs in the entrance lane of the signalized intersection. The reason is that there is a continuous acceleration of traffic flow in the entrance lane of the signalized intersection when the light is green, which increases the noise emission. When the traffic is close to saturation, the gap in $\mathrm{L}_{\mathrm{wpl}}$ between the entrance lane and exit lane is approximately 4 dB, and the energy contribution of the entrance lane is less than 30\%. When the traffic is saturated on a roundabout, the gap expands to more than 10 dB, and the energy contribution of the entrance lane is less than $10 \%$.

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-09.jpg?height=1421&width=1753&top_left_y=224&top_left_x=138)
Fig. 8. Comparison of the simulated $L_{\mathrm{eq}}$ and $L_{\mathrm{NP}}$ at the roundabout and signalized intersections with a 1-h simulation period for each traffic level.

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-09.jpg?height=670&width=833&top_left_y=1766&top_left_x=133)
Fig. 9. Comparison of the probability distribution of the noise level of the roundabout and signalized intersections for different traffic levels.

The dynamic traffic noise simulation method introduced in this paper uses the microscopic traffic simulation software Paramics to simulate the traffic flow. The traffic simulation is based on the carfollowing model and lane-changing model. The simulated saturated traffic volume may be higher than the actual situation because the drivers in reality pay more attention to safe driving. Therefore, the limit of traffic noise in reality may be reached earlier. However, this does not affect the method used for researching traffic noise.

## 7. Conclusion

The presented vehicle noise emission model reflects the effects of acceleration and deceleration on vehicle noise emission. The dynamic traffic noise simulation method combining with a microscopic traffic simulation tool has considered the interplay between traffic speed and volume, and the accuracy of the model has been validated by experimental measurements, which indicate that the method is suitable for calculating traffic noise around intersections and other complicated road networks. Some relations between

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-10.jpg?height=967&width=1111&top_left_y=228&top_left_x=493)
Fig. 10. Noise distribution map of the roundabout with a traffic OD of 1800 PCU/h (in dBA).

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-10.jpg?height=971&width=1102&top_left_y=1378&top_left_x=495)
Fig. 11. Noise distribution map of the signalized intersection with a traffic OD of 1800 PCU/h (in dBA).

![](https://cdn.mathpix.com/cropped/4bd097b8-7315-4d79-a16c-f66d89c47f63-11.jpg?height=672&width=829&top_left_y=230&top_left_x=133)
Fig. 12. Comparison of the $L_{\text {wpl }}$ of different lanes for the roundabout and signalized intersections.

traffic noise and traffic volume on roundabout and signalized intersections have been obtained, and the mechanisms have been discussed. The difference in traffic noise generated by entrance lanes and exit lanes on roundabout and signalized intersections has been analyzed. The results of this paper are applicable to traffic noise management in cities.

## Acknowledgements

This work was supported by the National Natural Science Foundation of China (No. 11574407), the Science and Technology Planning Project of Guangdong Province, China (No. 2015B010110005), the Joint Foundation for Super-computing Science Applied Research of Guangdong, China (No. 2015_515), and the Excellent Young Teachers Program in Higher Education of Guangdong, China (No. Yq2014110). Comments and suggestions from the reviewers and editor are highly appreciated.

## References

[1] Babisch W, Wölke G, Heinrich J, Straff W. Road traffic noise and hypertension accounting for the location of rooms. Environ Res 2014;133:380-7.
[2] Tonne C, Halonen JI, Beevers SD, Dajnak D, Gulliver J, Kelly FJ, et al. Long-term traffic air and noise pollution in relation to mortality and hospital readmission among myocardial infarction survivors. Int J Hyg Environ Health 2016;219 (1):72-8.
[3] Garg N, Maji S. A critical review of principal traffic noise models: strategies and implications. Environ Impact Assess Rev 2014;46:68-81.
[4] Guarnaccia C. Advanced tools for traffic noise modelling and prediction. Wseas Trans Syst 2013;12(2):121-30.
[5] Rochat JL, Fleming GG. Validation of FHWA's Traffic Noise Model ${ }^{\text {® }}$ (TNM): phase 1. Washington (DC, US): Department of Transportation; 2002.
[6] Givargisa Sh, Mahmoodi M. Converting the UK calculation of road traffic noise (CORTN) to a model capable of calculating $\mathrm{L}_{\text {Aeq }}, 1 \mathrm{~h}$ for the Tehran's roads. Appl Acoust 2008;69(11):1108-13.
[7] Yamamoto K. Road traffic noise prediction model 'ASJ RTN-Model 2008': report of the research committee on road traffic noise. Acoust Sci Technol 2010;31:1-55.
[8] Kephalopoulos S, Paviotti M, Anfosso-Ledee F. Common noise assessment methods in Europe (CNOSSOS-EU) EUR 25379 EN. Luxembourg: Publications Office of the European Union; 2012.
[9] Kephalopoulos S, Paviotti M, Anfosso-Lédée F, van Maercke D, Shilton S, Jones N. Advances in the development of common noise assessment methods in Europe: the CNOSSOS-EU framework for strategic environmental noise mapping. Sci Total Environ 2014;31(2):482-3.
[10] Makarewicz R, Fujimoto M, Kokowski P. A model of interrupted road traffic noise. Appl Acoust 1999;57(2):129-37.
[11] Makarewicz R, Kokowski P. Prediction of noise changes due to traffic speed control. J Acoust Soc Am 2007;122(4):2074-81.
[12] Abo-Qudais S, Alhiary A. Statistical models for traffic noise at signalized intersections. Build Environ 2007;42(8):2939-48.
[13] To WM, Chan TM. The noise emitted from vehicles at roundabouts. J Acoust Soc Am 2000;107(5):2760-3.
[14] Luo WL, Cai M, Li F, Liu JK. Dynamic modeling of road traffic noise around building in an urban area. Noise Control Eng J 2012;60(4):353-62.
[15] Can A, Leclercq L, Lelong J, Botteldooren D. Traffic noise spectrum analysis: Dynamic modeling vs. experimental observations. Appl Acoust 2010;71:764-70.
[16] Can A, Chevallier E, Nadji M, Leclercq L. Dynamic traffic modeling for noise impact assessment of traffic strategies. Acta Acust United Acust 2010;96:482-93.
[17] Ramírez A, Domínguez E. Modeling urban traffic noise with stochastic and deterministic traffic models. Appl Acoust 2013;74:614-21.
[18] Li F, Cai M, Liu JK, Yu Z. Dynamic traffic noise simulation at a signalized intersection among buildings. Noise Control Eng J 2011;59(2):202-10.
[19] Cai M, Li F, Liu JK. Dynamic simulation and characteristics analysis of traffic noise at signal-controlled pedestrian crossing junction. Noise Control Eng J 2011;59(5):549-55.
[20] Covaciu D, Florea D, Timar J. Estimation of the noise level produced by road traffic in roundabouts. Appl Acoust 2015;98:34-51.
[21] Chevallier E, Can A, Nadji M, Leclercq L. Improving noise assessment at intersections by modeling traffic dynamics. Transport Res Part D Transport Environ 2009;14(2):100-10.
[22] Suzuki T, Tsukui K, Oshino Y, Tachibana H. Road traffic noise prediction model around signalized intersections. In: Proc Inter-noise. p. 1870-3.
[23] Chevallier E, Ledercq L, Lelong J, Chatagnon R. Dynamic noise modeling at roundabouts. Appl Acoust 2009;70:761-70.
[24] De Coensel B, Vanhove F, Logghe S, Wilmink I. Noise emission corrections at intersections based on microscopic traffic simulation. In: European conference on noise control. tampere.
[25] Limits and measurement methods for noise emitted by accelerating motor vehicles. Beijing: China Environmental Science Press; 2002.
[26] International standard ISO 9613. Acoustics - attenuation of sound during propagation outdoors - Part 2: General method of calculation. International Organization for Standardization; 1996.
[27] Makarewicz R, Galuszka M. Road traffic noise prediction based on speed-flow diagram. Appl Acoust 2011;72(4):190-5.
[28] Makarewicz R. The annual average sound level of road traffic noise estimated from the speed-flow diagram. Appl Acoust 2013;74(5):669-74.

[^0]:    * Corresponding author at: Research Center of Intelligent Transport Systems, School of Engineering, Sun Yat-sen University, Guangzhou, 510006, China.
    E-mail address: caiming@mail.sysu.edu.cn (M. Cai).

