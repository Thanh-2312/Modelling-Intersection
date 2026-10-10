# International Journal of Transportation Science and Technology 

Research Paper

# Adaptive look-ahead driving for enhancing traffic flow performance at urban signalized intersections 

Magzhan Atykhan ${ }^{\mathrm{a}}$, A.S.M. Bakibillah ${ }^{\mathrm{b}}$, Md Abdus Samad Kamal ${ }^{\mathrm{a}, *,}$ Kou Yamada ${ }^{\mathrm{a}}$<br>${ }^{\mathrm{a}}$ Graduate School of Science and Technology, Gunma University, Kiryu 376-8515, Japan<br>${ }^{\mathrm{b}}$ Department of Systems and Control Engineering, School of Engineering, Institute of Science Tokyo, Tokyo 152-8552, Japan

## ARTICLE INFO

Article history:
Received 13 February 2025
Received in revised form 11 May 2025
Accepted 4 December 2025
Available online xxxx

Keywords:
Adaptive look-ahead driving (ALD)
Extended adaptive cruise control (ACC)
Anticipatory driving decisions
Intersection capacity
Traffic safety


#### Abstract

Enhancing driving efficiency while ensuring high throughput at signalized intersections is challenging to achieve safe and sustainable urban mobility. This paper proposes a novel adaptive look-ahead driving (ALD) system that employs anticipatory driving decisions to improve traffic flow performance, intersection throughput, and vehicle fuel efficiency at signalized intersections for a given signal timing to address this issue. The proposed system combines a naturalistic human driving model with an adaptive cruise control (ACC) model by extending them with a look-ahead step to realize desired stopping and starting behavior at traffic signals through safe and precise following of a preceding vehicle. Considering the predictive or look-ahead states of the preceding vehicle and utilizing an adaptive desired speed in response to the red signal ahead allows the host vehicle to behave like a predictive, optimally controlled vehicle with minimal computational effort. The performance of the proposed system is analyzed through microscopic traffic simulations at signalized intersection traffic scenarios, focusing on maintaining safe time headway and optimizing intersection throughput. The comparative analysis demonstrates improvements in intersection clearance, human-like vehicle spacing, and overall traffic flow efficiency. The proposed system can be implemented as an advanced driver assistance system (ADAS) for safe and sustainable mobility at urban intersections.


© 2026 Tongji University and Tongji University Press. Publishing Services by Elsevier B.V. on behalf of KeAi Communications Co., Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

## 1 Introduction

Over the past few decades, the development of intelligent transportation systems (ITS) has shown promising improvements in vehicle automation and traffic control. A crucial aspect of this progress is to improve traffic management at signalized intersections (Ait Ouallane et al., 2022; Jayson et al., 2024). However, the increasing traffic demands on urban road networks result in higher traffic volumes, often exceeding the capacity of current intersections and causing severe traffic congestion (Yue et al., 2022). Additionally, dynamic and unpredictable traffic conditions during peak and off-peak hours, combined with emergencies and road accidents, result in delays and inefficiencies in existing traffic control systems. Furthermore, the frequent stopping and idling at signalized intersections considerably increase fuel consumption and greenhouse gas (GHG) emissions (Alshayeb et al., 2022). Field studies show that stop-and-go vehicles produce 14\% extra energy

[^0]consumption and GHG emissions than vehicles driven at constant speeds (Xia et al., 2012). Therefore, efficient intersection control remains a major concern in modern traffic management systems for achieving safe and sustainable urban mobility.

Numerous works have been proposed to improve traffic management at signalized intersections. Early research focused on developing dynamic and adaptive traffic signal controllers and control algorithms using vehicle queue length information (Mirchandani and Zou, 2007; Liu et al., 2009). However, upgrading traffic signal infrastructure is expensive. Some studies proposed speed advisory systems (SAS) employing advanced signal phase and timing (SPAT) information via vehicle-tovehicle (V2V) and infrastructure-to-vehicle (I2V) communications to improve traffic flow at signalized intersections (Asadi and Vahidi, 2011; Nie and Farzaneh, 2022). However, accurate SPAT information is difficult to obtain in practice due to timing drift in fixed-time traffic lights. Moreover, V2V and I2V communications are not widespread enough to facilitate cooperative control between vehicles and infrastructure to improve intersection traffic management. Some other works proposed learning-based models for improving traffic management and safety at signalized intersections (Bakibillah et al., 2019a; Haddad et al., 2022). However, the learning-based models require a large amount of data to train the model, and such data is not readily available.

On the other hand, traffic flow at intersections can be improved by modeling driving behavior with desired space and time gaps. The model-based approaches of adaptive cruise control (ACC) as a driver assistant technology relied on radar sensing and simple gap-keeping rules to adjust a vehicle's speed to maintain a safe following distance and had limited robustness under varying traffic dynamics (Shladover, 1995). Today, ACC is a practical technology that can maintain uniform inter-vehicle gaps by adapting to the preceding vehicle (PV)'s distance and speed in real-time using sensors (Ntousakis et al., 2015). Numerous studies investigated ACC schemes in highway driving scenarios for varied space and time gaps (Moon et al., 2009; Manolis et al., 2020). These ACC schemes showed effectiveness in highway driving, where traffic is comparatively homogeneous (Gunter et al., 2021). However, the presence of critical braking zones at signalized intersections has limited the practical application of ACC in urban traffic management. Specifically, the ACC system deactivates when the PV applies aggressive braking, which may cause string instabilities (Talebpour and Mahmassani, 2016; Lu et al., 2019). Furthermore, the ACC technology is impaired by dynamic vehicle behavior (e.g., stop-and-go events), and short space and time gaps at signals (Milanés and Shladover, 2014). Therefore, extending the concept of ACC to integrate dynamic urban scenarios attracted significant interest. By tuning the parameters of the intelligent driver model (IDM), an ACC scheme was proposed for driving in congested or low-speed urban ways to reduce the congestion effectively (Kesting et al., 2008). However, the key idea is to conditionally switch the IDM parameters, e.g., to reduce the time gap between vehicles and quickly accelerate from bottlenecks in the same human driving style. In a different way, IDM with the same parameters is extended with a look-ahead concept by incorporating a PV's predicted state and acceleration for better performance of ACC vehicles (Kamal et al., 2022). However, these approaches do not incorporate synchronization aspects or compactly follow a PV, as found in real ACC vehicles (Milanés and Shladover, 2014).

Consequently, numerous works developed cooperative adaptive cruise control (CACC) systems employing V2V communication that can drive vehicles safely with a small headway by forming platoons, thereby increasing the traffic-flow capacity of a highway lane (Zohdy and Rakha, 2016; Xiao et al., 2018). However, conventional CACCs operate multiple cars in a platoon without predicting their future state. Some works designed ACC systems using advanced control algorithms, e.g., model predictive control (MPC) that considers future vehicle states within a predefined prediction horizon, enabling dynamic decision-making (Kamal et al., 2018; Bakibillah et al., 2019b; Lin et al., 2021). MPC can dynamically adjust a control input, reducing unnecessary acceleration and deceleration, which allows ACC systems to adapt to changing traffic conditions more effectively, resulting in smoother and more efficient vehicle operation. However, MPC-based schemes have high computational costs and limited practical applications. Alternatively, traditional human-based driving models are less computationally intensive but cannot predict preceding traffic and are often delayed in responding to varying traffic conditions. Moreover, human-based schemes cannot avoid aggressive braking zones since they use current vehicle states to define control acceleration. Therefore, computationally efficient predictive vehicle control schemes, namely look-ahead mechanisms within the ACC framework, e.g., by extending IDM or other car-following models, can be a potential solution to the shortcomings of the above schemes. Research shows that look-ahead methods can improve the vehicle's ability to maintain smooth traffic flow and string stability, especially in complex and dynamic traffic environments (Zhai et al., 2018; Kamal et al., 2022, 2024). However, although the look-ahead method is comparable to an MPC method in a typical car-following scenario, it lacks long-predicted optimal behavior while approaching a red signal intersection or leaving an intersection after a signal change. Furthermore, the predictive aspect of ACC can be enhanced by incorporating the acceleration of PVs (Gao and Yan, 2016; Kamal et al., 2022). ACC approaches are often studied under high-speed conditions or using connected vehicle information to predict future traffic states and improve decision-making. However, their applicability in urban traffic conditions remains limited due to the high-speed requirements of ACC and the assumption of full connectivity. Therefore, we propose developing a practical and computationally efficient extension of commercial ACC systems that can partially produce the anticipatory behaviors of MPC-based schemes while remaining suitable for current urban traffic conditions.

In this paper, we develop a novel adaptive look-ahead driving (ALD) system comprising a naturalistic human driving model and an ACC model, which uses the context-adaptive target speed and the look-ahead or predicted states to make more prudent predictive vehicle control decisions in transient situations. With adaptive target speed, the ALD system enhances its predictive driving ability for longer ranges that are suitable for the energy-efficient behavior of a vehicle when approaching a red signal. Using an ACC model strengthens the ALD system for quick and better-consolidated behavior when leaving the intersection immediately after the end of a red signal. Being a parametric function, the ALD requires minimal computational
time compared to the rigorous computation-based systems. We comparatively evaluate the effectiveness of the proposed model with existing human driving models. The results demonstrate the potential benefits of the proposed ALD system in improving intersection throughput and overall traffic flow efficiency. The main contributions of this work are as follows.

- The proposed system realizes the desired stopping and starting behavior at traffic signals through safe and precise following of a PV.
- Unlike MPC-based systems, the proposed model uses real-time decision-making rather than continuous numerical optimization.
- The proposed system improves traffic flow performance and capacity at signalized intersections for a given signal timing by employing anticipatory driving decisions.
- The proposed system operates in a look-ahead horizon, continuously updating decisions in small intervals, enabling realtime adaptation to varying traffic conditions.

The rest of the paper is organized as follows. Section 2 describes the methodology, including the problem statement, the traditional car-following model, and the ALD model. Section 3 outlines the simulation results and key findings. Finally, Section 4 concludes the paper, summarizing the contributions and potential future directions.

## 2 Methodology

The longitudinal motion control of a vehicle at a signalized intersection depends on the state of the proximate PV on the same lane and the distance and signal status of the intersection ahead. In contrast, the lateral motion of a car is mostly determined by the path curvature of the road ahead of the intended route. In this paper, we only consider the longitudinal motion control of vehicles when approaching the intersection, assuming that the driver or automated driving system properly steers the vehicle along the path. For simplicity, we also consider a single-lane road with car-following behavior without lanechanging or overtaking maneuvers.

The state variables of a host vehicle (HV) are denoted by its position $x_{\mathrm{hv}}$ and velocity $v_{\mathrm{hv}}$, with the control input decided by the acceleration $a_{\mathrm{hv}}$. The primary objective is to determine the control input $a_{\mathrm{hv}}$ for the HV based on its state variables $x_{\mathrm{hv}}$ and $v_{\mathrm{hv}}$, together with the states of the PV, which include the position $x_{\mathrm{pv}}$ and velocity $v_{\mathrm{pv}}$. The next section briefly describes a naturalistic human car-following model for longitudinal motion control of an HV. Then, the proposed ALD system is formulated based on its extension.

### 2.1 Traditional car-following scheme

Initially, the typical human driving model exhibiting the car-following behavior is briefly explained to better comprehend the look-ahead driving system proposed in this paper. We consider the IDM, a widely used model for describing human carfollowing behavior. IDM ensures collision-free driving and mimics explainable car-following behavior to represent naturalistic human driving patterns. It balances behavioral fidelity and computational efficiency, making it particularly suitable for simulation-based traffic flow studies. The parameters of IDM, such as the desired time headway, minimum gap, and maximum acceleration, are easily comprehensible and can be adjusted to represent different driving styles. Moreover, IDM integrates with ACC functionalities, making it a practical choice for studying hybrid human-automation interactions. In IDM, the instantaneous acceleration $a_{\mathrm{hv}}(t)$ of an HV at time $t$ can be determined using the function $f_{\text {idm }}$, which is defined as

$$
a_{\mathrm{hv}}(t)=f_{\mathrm{idm}}\left(v_{\mathrm{hv}}(t), \Delta v_{\mathrm{r}}(t), \Delta x_{\mathrm{r}}(t), V_{\mathrm{d}}\right),
$$

where $V_{\mathrm{d}}(\mathrm{m} / \mathrm{s})$ is the desired speed of the IDM, $\Delta x_{\mathrm{r}}(t)(\mathrm{m})$ is the distance between two vehicles or vehicle and intersection position $X_{\mathrm{j} . \text { red }}$ ahead (i.e., $X_{\mathrm{j} . \text { red }}>x_{\mathrm{hv}}(t)$, during the red phase of a traffic light and can be expressed as

$$
\Delta x_{\mathrm{r}}(t)=\left\{\begin{array}{c}
X_{\mathrm{j} . \mathrm{red}}-x_{\mathrm{hv}}(t)-L, i f x_{\mathrm{pv}}(t)>X_{\mathrm{j} . \mathrm{red}} \\
x_{\mathrm{pv}}(t)-x_{\mathrm{hv}}(t)-L, \text { otherwise },
\end{array}\right.
$$

where $L(\mathrm{~m})$ is vehicle length, and $\Delta v_{\mathrm{r}}(t)$ is the relative speed given as

$$
\Delta v_{\mathrm{r}}(t)=\left\{\begin{array}{c}
v_{\mathrm{hv}}(t), \text { if } x_{\mathrm{pv}}(t)>X_{\mathrm{j} . \text { red }} \\
v_{\mathrm{hv}}(t)-v_{\mathrm{pv}}(t), \text { otherwise. }
\end{array}\right.
$$

Basically, vehicle acceleration can be calculated based on the fundamental formulation of the IDM presented in Treiber et al. (2000), thus, the function $f_{\text {idm }}$ can be written as

$$
f_{\mathrm{idm}}\left(v_{\mathrm{hv}}, \Delta v_{\mathrm{r}}, \Delta x_{\mathrm{r}}, V_{\mathrm{d}}\right)=a\left(1-\left(\frac{v_{\mathrm{hv}}}{V_{\mathrm{d}}}\right)^{4}-\left(\frac{D *\left(v_{\mathrm{hv}}, \Delta v_{\mathrm{r}}\right)}{\Delta x_{\mathrm{r}}}\right)^{2}\right),
$$

where the equation combines a free-road acceleration strategy $\dot{v}_{\text {free }}\left(v_{\text {hv }}\right)=a\left[1-\left(\frac{v_{\text {hv }}}{V_{\mathrm{d}}}\right)^{4}\right]$ and a braking strategy $\dot{v}_{\text {brake }}\left(\Delta x_{\mathrm{r}}, v_{\mathrm{hv}}, \Delta v_{\mathrm{r}}\right)=-a\left(\frac{D_{*}}{\Delta x_{\mathrm{r}}}\right)^{2}$, which becomes dominant when the vehicle approaches the desired minimum gap $D^{*}\left(v_{\mathrm{hv}}, \Delta v_{\mathrm{r}}\right)$ to the PV, which is defined as

$$
D *\left(v_{\mathrm{hv}}, \Delta v_{\mathrm{r}}\right)=s_{0}+v_{\mathrm{hv}} T+\frac{v_{\mathrm{hv}} \Delta v_{\mathrm{r}}}{2 \sqrt{a b}},
$$

where $s_{0}, T, a$, and $b$ are model parameters, respectively denoting the minimum distance, the safe time gap, the maximum acceleration, and the comfortable deceleration rates that differ among drivers. The safe time gap among human drivers typically varies as $T \in[1,2]$ s, which often characterizes a driver as safe/conservative or aggressive.

The IDM primarily ensures a safe inter-vehicle distance and facilitates collision avoidance by adjusting the acceleration based on the distance and relative speed between the host and PV in typical driving situations. However, despite the simplicity and advantages of traditional car-following models (e.g., IDM), their only focus on the current states of vehicles, rather than future states, frequently affects traffic flows in critical scenarios. Specifically, braking styles of traditional human carfollowing models at a red signal are inefficient in energy savings, and a lack of compactness with quick starting styles from idling at red-to-green signal changes affects maximum traffic flows under critical conditions.

### 2.2 ALD system

To overcome these traditional human driving (THD) issues, we develop an ALD system that integrates the IDM with an ACC model and incorporates a look-ahead step prediction of vehicles. The fundamental concept of the proposed ALD is shown in Fig. 1. The ALD utilizes the adaptive target speed concerning the red signal ahead and the look-ahead or predicted states of the PV to make anticipatory driving decisions that generate naturalistic driving behavior with human-like vehicle spacing and improve overall traffic flow and fuel efficiency. The control acceleration $a_{\mathrm{hv}}(t)$ using the ALD system at time $t$ is obtained as

$$
a_{\mathrm{hv}}(t)=f_{\mathrm{idm}}\left(v_{\mathrm{hv}}(t), \Delta v_{\mathrm{r}}(t), \Delta \bar{x}_{\mathrm{r}}(t), v_{\mathrm{d}}(t)\right)+\alpha f_{\mathrm{acc}}\left(v_{\mathrm{hv}}(t), \Delta v_{\mathrm{r}}(t), \Delta \bar{x}_{\mathrm{r}}(t)\right),
$$

where $v_{\mathrm{d}}(t)(\mathrm{m} / \mathrm{s})$ is the time-varying target desired speed, $\alpha$ is the adjustment or compensating coefficient, $f_{\text {acc }}(\cdot)$ represents the ACC acceleration function and $\Delta \bar{x}_{\mathrm{r}}(\mathrm{m})$ is the look-ahead distance from the PV.

The car-following behavior is given as a combination of traditional IDM and ACC models, where the ACC component influences better-synchronized behavior by balancing the parameters $\alpha$ with the gain parameter $a$ of IDM in Eq. (4) in the adaptive mode for a close PV. Note that, like the original ACC in (Milanés and Shladover, 2014), for a sufficiently far PV, the driving is switched into the cruising mode, which is realized here by IDM part with negligible $\alpha$ limited $f_{\text {acc }}(\cdot)$, i.e., without a need for switching. Moreover, using the anticipatory relative gap $\Delta \bar{x}_{\mathrm{r}}$ in both parts ensures a linear combination of the decisions. With a short look-ahead step $t_{\mathrm{ls}}$ the estimated or predicted distance $\Delta \bar{x}_{\mathrm{r}}$ is obtained as

$$
\Delta \bar{x}_{\mathrm{r}}(t)=x_{\mathrm{pv}}(t)-x_{\mathrm{hv}}(t)+t_{\mathrm{ls}}\left(v_{\mathrm{pv}}(t)-v_{\mathrm{hv}}(t)\right)
$$

![](https://cdn.mathpix.com/cropped/6694358c-77c8-4d43-891e-bd8f5ab3f6af-04.jpg?height=552&width=1084&top_left_y=1705&top_left_x=403)
Fig. 1 Proposed ALD scheme that estimates look-ahead (future) states of the vehicles and incorporates adaptive parameters depending on the driving context with THD combined with an ACC model.

The desired speed $v_{\mathrm{d}}(t)$ is considered adaptive to the driving context, which is tuned during the red phase when the vehicle is within a certain distance from the intersection and needs to stop. Specifically, the look-ahead projected desired speed $\bar{v}_{\mathrm{d}}$ by tuning the current speed of the HV is determined as

$$
\bar{v}_{\mathrm{d}}(t)=v_{\mathrm{hv}}(t)-\widehat{a}_{\mathrm{b}}(t) t_{\mathrm{ls}},
$$

where $\widehat{a}_{\mathrm{b}}(t)$ is the estimated deceleration rate required to completely stop with monotonically decreasing speed at the red signal in an unconstrained situation, which can be given as

$$
\widehat{a}_{\mathrm{b}}(t)=\frac{v_{\mathrm{hv}}^{2}(t)}{2\left(X_{\mathrm{j} . \mathrm{red}}-X_{\mathrm{hv}}(t)\right)} .
$$

Next, for a realistic driving decision, the target desired speed $v_{\mathrm{d}}(t)$ is chosen between the original desired speed $V_{\mathrm{d}}$ and the projected desired speed $\bar{v}_{\mathrm{d}}$ as

$$
v_{\mathrm{d}}(t)=\gamma V_{\mathrm{d}}+(1-\gamma) \bar{v}_{\mathrm{d}}(t)
$$

where $\gamma \in[0,1]$ is a conditional adaptation factor. Under normal traffic flow circumstances, $\gamma=1$, i.e., $v_{\mathrm{d}}(t)=V_{\mathrm{d}}$. Under critical stopping conditions at the intersection, $\gamma$ is tuned to a suitable value for smoothly changing the desired speed to a lower value. In Eq. (6), with a small gain $\alpha, f_{\text {acc }}(\cdot)$ is introduced to facilitate compactness or fast synchronization with PVs when vehicles speed up from a low speed. The function $f_{\text {acc }}$ was originally developed by Milanés and Shladover (2014) for highway driving and based on the experimental driving of real ACC-equipped vehicles and it can be expressed in a modified form with soft limit constraints using $\tanh (\cdot)$ as

$$
f_{\mathrm{acc}}\left(v_{\mathrm{hv}}(t), \Delta v_{\mathrm{r}}(t), \Delta \bar{x}_{\mathrm{r}}(t)\right)=\tanh \left(k_{1}\left(\Delta \bar{x}_{\mathrm{r}}-s_{0}+T v_{\mathrm{hv}}\right)+k_{2}\left(v_{\mathrm{pv}}-v_{\mathrm{hv}}\right)\right)
$$

where $k_{1}$ and $k_{2}$ are gain parameters to regulate time-gap error relative to the PV. Note that in the original ACC model, these gains are tuned based on high-speed driving conditions on highways, whereas in this paper, these gains are tuned based on the urban car-following behavior at the signalized intersection with lower speed and the output of $f_{\text {acc }}$ is restricted by $\tanh (\cdot)$ to act as a small additive or compensating term in the decision making using Eq. (6) and to prevent excessive accelerations or decelerations resulting PV with large speed or gap errors. In the absence of a close PV (i.e., in cruising mode), the tuning parameter $\alpha$ is set to zero. Our proposed look-ahead approach does not require the PV's future acceleration; hence, it differs from (Kamal et al., 2022), which uses the estimated future acceleration of the PV. Thus, the proposed ALD is easy to implement in real-world conditions.

### 2.3 Fuel consumption model

A vehicle's fuel consumption is influenced by different factors, such as vehicle type, weight, engine size, and powertrain systems. Besides, the instantaneous velocity and acceleration are crucial dynamic factors contributing to a vehicle's fuel consumption rate. In this paper, the fuel consumption rate $f_{\mathrm{v}}(\mathrm{mL} / \mathrm{s})$ is computed using its instantaneous velocity $v$ and acceleration $\bar{a}$ as (Kamal et al., 2011).

$$
f_{\mathrm{v}}(v, \bar{a})=f_{\text {cruise }}+f_{\text {dyn }}
$$

where $f_{\text {cruise }}(\mathrm{mL} / \mathrm{s})$ represents fuel consumption due to instant velocity $v$ and $f_{\text {dyn }}$ (mL/s) is the fuel consumption caused by instant acceleration $\bar{a}$ at speed $v$, and given by

$$
\begin{aligned}
& f_{\text {cruise }}=b_{0}+b_{1} v+b_{2} v^{2}+b_{3} v^{3} \\
& f_{\text {dyn }}=\bar{a}\left(c_{0}+c_{1} v+c_{2} v^{2}\right)
\end{aligned}
$$

where $b_{0}, b_{1}, b_{2}, b_{3}, c_{0}, c_{1}$, and $c_{2}$ are model parameters that are known for a specific vehicle. The consumption constants were derived from an engine torque-speed-efficiency map of a typical vehicle explained in Kamal et al. (2011). Here, $\bar{a}=a$ for $a>0$, otherwise $\bar{a}=0$. It is assumed that when a vehicle brakes at high speed, i.e., $a<0$ no fuel is consumed. However, when the vehicle reaches a certain low speed or idling, the fuel consumption resumes since the engine runs while idling.

## 3 Results and discussion

To implement the proposed ALD system in urban traffic scenarios with signalized intersections, we used a customized traffic simulator built in MATLAB that was originally designed and used in (Bakibillah et al., 2019a; Kamal et al., 2022, 2024). We analyzed the proposed ALD system in terms of traffic flow, intersection clearance efficiency, and fuel consumption in comparison with other traditional (human-based) car-following schemes, namely the capacity-enhanced THD model (THD I) and safety-enhanced THD model (THD II). The THD and the proposed ALD system parameters are given in Table 1.

Table 1
IDM and proposed ALD parameters used in simulation.
| Parameter | Value |
| :--- | :--- |
| Safe time gap (THD I)(T) | 1.2 s |
| Safe time gap (THD II) $(T)$ | 1.5 s |
| Vehicle length ( $L$ ) | 4 m |
| Maximum acceleration (a) | $1.5 \mathrm{~m} / \mathrm{s}^{2}$ |
| Comfortable deceleration ( $b$ ) | $2.5 \mathrm{~m} / \mathrm{s}^{2}$ |
| Minimum spacing $\left(s_{0}\right)$ | 2 m |
| Desired velocity $\left(V_{\mathrm{d}}\right)$ | 50 km/h |
| Simulation time-step ( $t$ ) | 0.5 s |
| Adjustment coefficient ( $\alpha$ ) | 0.2 |
| Desired velocity factor $(\gamma)$ | 0.12 |
| Look-ahead time-step ( $t_{\mathrm{ls}}$ ) | 1 s |
| Gain for velocity error ( $k_{1}$ ) | $0.01 \mathrm{~s}^{-2}$ |
| Gain for gap error ( $k_{2}$ ) | $0.8 \mathrm{~s}^{-1}$ |


The fuel consumption model parameters are obtained from (Kamal et al., 2011) as $b_{0}=0.1569, b_{1}=2.450 \times 10^{-2}, b_{2}=-$ $7.415 \times 10^{-4}, b_{3}=5.975 \times 10^{-5}, c_{0}=0.07224, c_{1}=9.681 \times 10^{-2}$, and $c_{2}=1.075 \times 10^{-3}$. The key parameter, look-ahead time-step $t_{\mathrm{ls}}=1 \mathrm{~s}$, is selected at a lower value than the preferred time gap based on some sensitivity analysis on vehicle performance, considering the PV (or traffic) behavior variation to avoid the oscillation in the control decision or string instability.

### 3.1 Evaluation of decision-making by the proposed system

Firstly, we assessed the decision-making process of the proposed system with a few vehicles at an isolated signalized intersection to better comprehend its principles and potential compared to THD I and THD II. Therefore, to account for driving behavior heterogeneity, we conducted simulations using different driver styles by varying the desired time gap parameter in the model, effectively representing a range of behavioral patterns from aggressive (THD I) to safe (THD II) driving. Specifically, we analyzed the braking and stopping behavior of four vehicles when approaching the signalized intersection located at 300 m . The first 15 s (including the last 3 s of yellow time) are considered effective green time, whereas the next 30 s are in the red phase. Fig. 2 illustrates each vehicle's trajectory (position and relative gaps), speed, and acceleration profiles over 45 s.

It is found that THD I and THD II methods perform similar aggressive braking behavior with abrupt speed reductions when approaching the signalized intersection, as shown in Fig. 2(a) and (b). Since THD I has a time gap of 1.2 s, the vehicles needed to brake slightly faster than THD II, which has a time gap of 1.5 s. On the other hand, the proposed ALD decelerates smoothly with gradual speed reduction when approaching the intersection, as shown in Fig. 2(c), and thus better utilizes the effective red time. Moreover, similar to advanced optimal driving systems, the proposed ALD utilizes the kinetic energy of vehicles by generating smooth acceleration and braking, which has the potential to improve fuel efficiency significantly. The proposed ALD also maintains passenger riding comfort with smooth acceleration and braking behavior.

### 3.2 Evaluation of the proposed system in dense traffic

Next, we evaluated the performance of the proposed system in dense traffic in realistic near-congested situations on the road with multiple signalized intersections. The study road is a single-lane with intersections located at 300 m and 900 m. To better comprehend the performance of the proposed system, over-saturated (highly dense) traffic inflow to the first intersection is applied, whereas the second intersection has a different traffic inflow (as it is regulated by the first intersection). Each traffic signal cycle persists for 60 s and is evenly divided into green (including the last 3 s of yellow time) and red phases. Initially, each scheme has the same traffic and signal settings for an equitable comparison, i.e., at 0 s, vehicles come at an approximate flow rate of 780 veh/hour with a speed limit of 50 km/h and a green signal at the first intersection. As the traffic light changes to red, vehicles decelerate and stop at the first intersection. For each method, the trajectories (position and relative gaps), speed, and acceleration profiles are collected over 300 s as depicted in Fig. 3. Then, particular driving behaviors are analyzed, including queue formations and departures at the corresponding intersections.

It is found that in the THD I method, 12 vehicles successfully pass through the intersection in each cycle, whilst the THD II method allows for 11 vehicles, as shown in Fig. 3(a) and (b), respectively. THD I demonstrates faster intersection clearance than THD II due to shorter time gaps between vehicles. In contrast, the proposed ALD allows for 13 vehicles per cycle, as shown in Fig. 3(c), which can considerably increase the intersection throughput. Importantly, in THD I and THD II, one or two vehicles fail to clear the intersection in each cycle, whereas all vehicles successfully pass through the intersection in the proposed ALD. Moreover, the THD I and THD II create longer queues at the intersection than the ALD, which results in spill-back congestion, leading to increased delays and fuel consumption. In contrast, the proposed ALD improves traffic

![](https://cdn.mathpix.com/cropped/6694358c-77c8-4d43-891e-bd8f5ab3f6af-07.jpg?height=993&width=1630&top_left_y=183&top_left_x=131)
Fig. 2 Comparison of driving behavior of (a) THD I, (b) THD II, and (c) ALD methods at an isolated intersection. The sub-figures show the vehicle's trajectories (top), speed (middle), and acceleration (bottom) profiles for traveling over 45 s.

![](https://cdn.mathpix.com/cropped/6694358c-77c8-4d43-891e-bd8f5ab3f6af-07.jpg?height=963&width=1354&top_left_y=1354&top_left_x=266)
Fig. 3 Driving along multiple signalized intersections over 300 s. The sub-figures show the vehicle's trajectories (top), speed (middle), and acceleration (bottom) profiles for (a) THD I, (b) THD II, and (c) ALD methods under dense traffic conditions.

flow efficiency by reducing the starting lost time or delay at the intersection. This reduced lost time increases effective green time, significantly improving the intersection throughput under dense traffic conditions.

From the velocity and acceleration profiles shown in Fig. 3, distinct driving behaviors at the intersection are observed. From velocity profiles, it is found that vehicles slow down fast at the red light and stop completely before passing the intersection in THD I and THD II. On the contrary, in ALD, vehicles slow down gradually when approaching the red signal, utilize the effective red time, and some vehicles manage to avoid a complete stop at the red signal due to speed adjustments in a predictive manner. During the green signal, the ALD allows vehicles to speed up faster than the THD I and THD II, and quickly traverse the intersection. This quick speeding up enables fast recovery of traffic congestion and increases intersection throughput. From acceleration profiles, it is found that vehicles using THD I and THD II decelerate aggressively at the red signal, whilst ALD vehicles decelerate slowly through anticipatory behavior, significantly reducing deceleration magnitude. During the green signal, the ALD vehicles maintain better acceleration than THD I and THD II vehicles. This anticipatory behavior by the proposed ALD can significantly enhance traffic flow efficiency by avoiding stop-and-go behavior and improving fuel consumption in dense traffic.

Fig. 4(a) illustrates the queue density within 150 m of the first intersection at the start of the green signal over 10 signal cycles for THD I, THD II, and ALD. The queue density, measured as the number of vehicles near the stopping condition ( $v_{\mathrm{hv}}<2 \mathrm{~m} / \mathrm{s}$ ), demonstrates a distinct pattern in every method. In particular, the THD II system typically has the highest queue density, beginning with 8 cars in the first cycle and gradually increasing to 20 cars by the tenth. Alternatively, THD I have a moderate queue density, ranging from 8 to 14 cars, and grows more slowly than THD II. The ALD maintains the lowest queue density over all cycles, ranging from 8 to 10 cars, showing improved traffic flow behavior and less congestion near the intersection. Fig. 4(b) depicts the average fuel economy rate for vehicles in the queue between 150 and 400 m, corresponding to the intersection transition region, where considerable variations in speed can be observed. In this study, the fuel consumption rate for gasoline-driven vehicles is considered, reflecting the current dominance of fossil fuel vehicles. However, the proposed ALD can be applied to both conventional and electric vehicles. The proposed ALD consistently has the highest fuel economy rate compared to THD I and THD II. These findings emphasize the effectiveness of the proposed ALD in reducing queue formation, which is crucial for improving intersection throughput, minimizing delays, and increasing fuel economy rate.

Table 2 gives the performance comparison of THD I, THD II, and the proposed ALD methods. This evaluation considers the segment 200 m before the first intersection and 100 m after the second intersection, where significant speed fluctuations are observed due to stop-and-go events. Despite the safety enhancements, THD II has the lowest fuel economy, with a rate of approximately 20.42 km/L, due to abrupt deceleration and increased queue formation, which result in higher fuel consumption. THD I shows a fuel economy rate of about 21.83 km/L with a moderate improvement of 6.90\%. The proposed ALD achieves the highest fuel economy, with a rate of about 24.36 km/L and a 19.29\% improvement compared to THD II. By allowing for gradual speed adjustments and smoother deceleration patterns, the ALD system minimizes excessive braking and acceleration, resulting in reduced fuel consumption compared to THD I and THD II. The ALD exhibits smoother driving behavior, with the lowest deceleration at $-1.46 \mathrm{~m} / \mathrm{s}^{2}$, compared to $-1.71 \mathrm{~m} / \mathrm{s}^{2}$ for THD I and $-1.60 \mathrm{~m} / \mathrm{s}^{2}$ for THD II. Although the ALD has a slightly higher mean maximum acceleration at $1.16 \mathrm{~m} / \mathrm{s}^{2}$, indicating effective intersection throughput.

### 3.3 Evaluation of the proposed system for different traffic flow rates

Finally, the overall performance of the proposed system is evaluated concerning average speed, average fuel economy, idling time, and intersection throughout, for different traffic flow rates as illustrated in Fig. 5. The results are depicted over a 10 -minute simulation period. It is found that the proposed ALD outperforms THD I and THD II in all evaluation metrics. Therefore, the proposed ALD has the potential to enhance traffic flow efficiency and fuel economy for different traffic flow

![](https://cdn.mathpix.com/cropped/6694358c-77c8-4d43-891e-bd8f5ab3f6af-08.jpg?height=520&width=1634&top_left_y=1829&top_left_x=127)
Fig. 4 Evaluation of (a) queue density and (b) average fuel economy rate of THD I, THD II, and ALD vehicles at the first intersection over 10 signal cycles.

Table 2
Performance comparison of THD I, THD II, and the proposed ALD methods.
| Performance | THD I | THD II | ALD |
| :--- | :--- | :--- | :--- |
| Average fuel economy rate/( $\left.\mathrm{km} \cdot \mathrm{L}^{-1}\right)$ | 21.83 | 20.42 | 24.36 |
| Improvement with respect to THD II | +6.90\% | - | +19.29\% |
| Mean maximum acceleration/ $\left(\mathrm{m} \cdot \mathrm{s}^{-2}\right)$ | 1.03 | 1.01 | 1.16 |
| Mean maximum deceleration/ $\left(\mathrm{m} \cdot \mathrm{s}^{-2}\right)$ | -1.71 | -1.60 | -1.46 |
| Observed throughput per cycle/vehicles | 12 | 11 | 13 |
| Throughput per hour/vehicles | 720 | 660 | 780 |


![](https://cdn.mathpix.com/cropped/6694358c-77c8-4d43-891e-bd8f5ab3f6af-09.jpg?height=1138&width=1636&top_left_y=562&top_left_x=125)
Fig. 5 Performance comparison of THD I, THD II, and ALD for (a) average speed, (b) average fuel economy rate, (c) total idling time, and (d) intersection throughput at varied traffic flow rates.

rates at the urban signalized intersections. Specifically, the ability of the proposed ALD to maintain better performance under high traffic flow rates emphasizes its effectiveness in handling real-world traffic scenarios. Additionally, the primary focus of our study is on traffic flow efficiency enhancement under fixed-time signal control. However, it is a well-established principle in traffic engineering that increasing the cycle length generally results in higher intersection capacity. Additionally, according to the U.S. Department of Transportation (National Academies of Sciences, Engineering, and Medicine, 2015), start-up and clearance lost time is approximately 2 s each. Therefore, our method is particularly effective in reducing this lost time and remains applicable for varied signal phase durations.

### 3.4 Discussion

The proposed ALD demonstrates the capability to maintain smooth speed transitions during stop-and-go events. By predicting traffic conditions in advance, the ALD effectively minimizes aggressive braking zones, resulting in significant improvements in fuel efficiency. In addition, the intersection throughput is increased by reducing the clearance time while maintaining a safe inter-vehicle gap. These improvements are achieved without sacrificing computational performance, as the proposed ALD maintains lower computational complexity than advanced control algorithms, making it suitable for
real-time applications. The scope of risk-taking tendency is mainly related to overtaking, merging, or lane-change situations. In single-lane driving, taking a limited risk of a short gap, aggressive braking, or acceleration does not significantly affect the performance of the proposed scheme. Therefore, the model should be enhanced by incorporating lane change, overtaking, and merging decision systems and evaluated in the broader road network in the future. We believe that our modeling and simulation results provide a strong basis for assessing the effectiveness of the proposed system. Also, we recognize that hardware-in-the-loop (HIL) tests can offer deeper insights into system implementation challenges and performance under real-world uncertainties; however, such facilities are not currently available. Therefore, as future work, we plan to extend the current study by incorporating HIL tests for a few vehicles to validate the practical applicability of the proposed system further.

Under the proposed strategy, when a vehicle approaches a red signal, it slowly decelerates from far away to improve fuel efficiency. Even if it arrives at the intersection taking extra time, it does not increase travel time, depending on the duration of the red signal. On the other hand, when starting from idle, the vehicle accelerates slightly faster, causing marginally higher consumption. However, it helps clear the intersection without leaving some vehicles waiting for the next cycle and thus eventually improves the overall fuel efficiency of all vehicles. In this sense of single-vehicle performance, the leading vehicle trade-off is its fuel efficiency for traveling faster. However, when traffic is much lower than the capacity, the leading vehicle can avoid much faster acceleration to improve its fuel consumption slightly by accepting a slightly longer time, which can be a future study to determine the traffic adaptive parameter settings of the proposed system.

## 4 Conclusions

In this paper, we have developed an ALD system to improve traffic flow performance and throughput at urban signalized intersections via anticipatory driving decisions. The proposed ALD integrates a naturalistic human driving model and an ACC model with context-adaptive target speed and look-ahead states to realize desired stopping and starting behavior at traffic signals through safe and precise following of a PV. The ALD system with adaptive target speed improves its predictive driving abilities for longer distances, which are suited for the energy-efficient behavior of a vehicle when approaching a red signal. Using an ACC model reinforces the ALD system for speedy and better-consolidated behavior when leaving the intersection immediately following the end of a red signal. The results demonstrated the effectiveness of the proposed system in improving traffic flow performance, intersection throughput, and fuel efficiency via safe driving. As a parametric function, the ALD requires less computational time than rigorous computation-based systems. Therefore, the proposed ALD can be deployed as an ADAS in real-world scenarios.

In the future, we will extend the proposed system for multi-lane and mixed-traffic conditions. We will extend the capabilities of the proposed algorithm by considering different factors and testing them in dynamic traffic conditions to enhance traffic performance, safety, and sustainability further.

## CRediT authorship contribution statement

Magzhan Atykhan: Methodology, Data curation, Writing - original draft, Investigation, Software, Formal analysis. A.S.M. Bakibillah: Writing - review \& editing, Investigation, Writing - original draft, Supervision. Md Abdus Samad Kamal: Project administration, Writing - review \& editing, Funding acquisition, Supervision, Conceptualization. Kou Yamada: Project administration, Writing - review \& editing, Supervision.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgment

This research is supported by the Japan Society for the Promotion of Science (JSPS) Grants-in-Aid for Scientific Research (C) 23K03898.

## References

Ait Ouallane, A., Bakali, A., Bahnasse, A., Broumi, S., Talea, M., 2022. Fusion of engineering insights and emerging trends: intelligent urban traffic management system. Inf. Fusion 88, 218-248. https://doi.org/10.1016/j.inffus.2022.07.020.
Alshayeb, S., Stevanovic, A., Effinger, J.R., 2022. Investigating impacts of various operational conditions on fuel consumption and stop penalty at signalized intersections. Int. J. Transp. Sci. Technol. 11 (4), 690-710. https://doi.org/10.1016/j.ijtst.2021.09.005.
Asadi, B., Vahidi, A., 2011. Predictive cruise control: utilizing upcoming traffic signal information for improving fuel economy and reducing trip time. IEEE Trans. Control Syst. Technol. 19 (3), 707-714. https://doi.org/10.1109/TCST.2010.2047860.
Bakibillah, A.S.M., Kamal, M.A.S., Tan, C.P., Hayakawa, T., Imura, J.I., 2019a. Event-driven stochastic eco-driving strategy at signalized intersections from self-driving data. IEEE Trans. Veh. Technol. 68 (9), 8557-8569. https://doi.org/10.1109/TVT.2019.2931519.
Bakibillah, A.S.M., Hasan, M., Rahman, M.M., Kamal, M.A.S., 2019b. Predictive car-following scheme for improving traffic flows on urban road networks. Control Theory Technol. 17 (4), 325-334. https://doi.org/10.1007/s11768-019-9144-z.

Gunter, G., Gloudemans, D., Stern, R.E., McQuade, S., Bhadani, R., Bunting, M., Delle Monache, M.L., Lysecky, R., Seibold, B., Sprinkle, J., Piccoli, B., Work, D.B., 2021. Are commercially implemented adaptive cruise control systems string stable? IEEE Trans. Intell. Transp. Syst. 22 (11), 6992-7003. https://doi.org/10.1109/TITS.2020.3000682.
Gao, Z., Yan, W., 2016. A headway control algorithm for ACC vehicles with the compensation of the preceding vehicle acceleration. Procedia Eng. 137, 669-679. https://doi.org/10.1016/j.proeng.2016.01.304.
Haddad, T.A., Hedjazi, D., Aouag, S., 2022. A deep reinforcement learning-based cooperative approach for multi-intersection traffic signal control. Eng. Appl. Artif. Intel. 114, 105019. https://doi.org/10.1016/j.engappai.2022.105019.
Jayson, T., Bakibillah, A.S.M., Tan, C.P., Kamal, M.A.S., Monn, V., Imura, J.I., 2024. Electric vehicle eco-driving strategy at signalized intersections based on optimal energy consumption. J. Environ. Manag. 368, 122245. https://doi.org/10.1016/j.jenvman.2024.122245.
Kesting, A., Treiber, M., Schönhof, M., Helbing, D., 2008. Adaptive cruise control design for active congestion avoidance. Transp. Res. Part C Emerg. Technol. 16 (6), 668-683. https://doi.org/10.1016/j.trc.2007.12.004.
Kamal, M.A.S., Hashikura, K., Hayakawa, T., Yamada, K., Imura, J.I., 2022. Look-ahead driving schemes for efficient control of automated vehicles on urban roads. IEEE Trans. Veh. Technol. 71 (2), 1280-1292. https://doi.org/10.1109/TVT.2021.3132936.
Kamal, M.A.S., Hayakawa, T., Imura, J.I., 2018. Road-speed profile for enhanced perception of traffic conditions in a partially connected vehicle environment. IEEE Trans. Veh. Technol. 67 (8), 6824-6837. https://doi.org/10.1109/TVT.2018.2826067.
Kamal, M.A.S., Bakibillah, A.S.M., Hayakawa, T., Yamada, K., Imura, J.I., 2024. Cooperative look-ahead lane change system for improving driving intelligence of automated vehicles in critical scenarios. IEEE Trans. Intell. Veh. 9 (9), 5876-5888. https://doi.org/10.1109/TIV.2024.3357983.
Kamal, M.A.S., Mukai, M., Murata, J., Kawabe, T., 2011. Ecological vehicle control on roads with up-down slopes. IEEE Trans. Intell. Transp. Syst. 12 (3), 783-794. https://doi.org/10.1109/TITS.2011.2112648.
Liu, H.X., Wu, X., Ma, W., Hu, H., 2009. Real-time queue length estimation for congested signalized intersections. Transp. Res. Part C Emerg. Technol. 17 (4), 412-427. https://doi.org/10.1016/j.trc.2009.02.003.
Lu, C., Dong, J., Hu, L., Liu, C., 2019. An ecological adaptive cruise control for mixed traffic and its stabilization effect. IEEE Access 7, 81246-81256. https://doi. org/10.1109/ACCESS.2019.2923741.
Lin, Y., McPhee, J., Azad, N.L., 2021. Comparison of deep reinforcement learning and model predictive control for adaptive cruise control. IEEE Trans. Intell. Veh. 6 (2), 221-231. https://doi.org/10.1109/TIV.2020.3012947.
Mirchandani, P.B., Zou, N., 2007. Queuing models for analysis of traffic adaptive signal control. IEEE Trans. Intell. Transp. Syst. 8 (1), 50-59. https://doi.org/10.1109/TITS.2006.888619.
Manolis, D., Spiliopoulou, A., Vandorou, F., Papageorgiou, M., 2020. Real time adaptive cruise control strategy for motorways. Transp. Res. Part C Emerg. Technol. 115, 102617. https://doi.org/10.1016/j.trc.2020.102617.
Milanés, V., Shladover, S.E., 2014. Modeling cooperative and autonomous adaptive cruise control dynamic responses using experimental data. Transp. Res. Part C Emerg. Technol. 48, 285-300. https://doi.org/10.1016/j.trc.2014.09.001.
Moon, S., Moon, I., Yi, K., 2009. Design, tuning, and evaluation of a full-range adaptive cruise control system with collision avoidance. Control Eng. Pract. 17 (4), 442-455. https://doi.org/10.1016/j.conengprac.2008.09.006.
Nie, Z., Farzaneh, H., 2022. Real-time dynamic predictive cruise control for enhancing eco-driving of electric vehicles, considering traffic constraints and signal phase and timing (SPaT) information, using artificial-neural-network-based energy consumption model. Energy 241, 122888. https://doi.org/10.1016/j.energy.2021.122888.
National Academies of Sciences, Engineering, and Medicine, 2015. Signal Timing Manual - Second Edition. Washington, DC: The National Academies Press. doi: 10.17226/22097.
Ntousakis, I.A., Nikolos, I.K., Papageorgiou, M., 2015. On microscopic modelling of adaptive cruise control systems. Transp. Res. Procedia 6, 111-127. https://doi.org/10.1016/j.trpro.2015.03.010.
Shladover, S.E., 1995. Review of the state of development of advanced vehicle control systems (AVCS). Veh. Syst. Dyn. 24 (6-7), 551-595. https://doi.org/10.1080/00423119508969108.
Talebpour, A., Mahmassani, H.S., 2016. Influence of connected and autonomous vehicles on traffic flow stability and throughput. Transp. Res. Part C Emerg. Technol. 71, 143-163. https://doi.org/10.1016/j.trc.2016.07.007.
Treiber, M., Hennecke, A., Helbing, D., 2000. Congested traffic states in empirical observations and microscopic simulations. Phys. Rev. E 62 (2), 1805-1824. https://doi.org/10.1103/physreve.62.1805.
Xia, H., Boriboonsomsin, K., Schweizer, F., Winckler, A., Zhou, K., Zhang, W.B., Barth, M., 2012. Field operational testing of ECO-approach technology at a fixed-time signalized intersection. In: 2012 15th International IEEE Conference on Intelligent Transportation Systems. IEEE, pp. 188-193. https://doi. org/10.1109/ITSC.2012.6338888.
Xiao, L., Wang, M., Schakel, W., van Arem, B., 2018. Unravelling effects of cooperative adaptive cruise control deactivation on traffic flow characteristics at merging bottlenecks. Transp. Res. Part C Emerg. Technol. 96, 380-397. https://doi.org/10.1016/j.trc.2018.10.008.
Yue, W., Li, C., Chen, Y., Duan, P., Mao, G., 2022. What is the root cause of congestion in urban traffic networks: road infrastructure or signal control? IEEE Trans. Intell. Transp. Syst. 23 (7), 8662-8679. https://doi.org/10.1109/TITS.2021.3085021.
Zhai, C., Luo, F., Liu, Y., 2018. Cooperative look-ahead control of vehicle platoon for maximizing fuel efficiency under system constraints. IEEE Access 6, 37700-37714. https://doi.org/10.1109/ACCESS.2018.2848480.
Zohdy, I.H., Rakha, H.A., 2016. Intersection management via vehicle connectivity: the intersection cooperative adaptive cruise control system concept. J. Intell. Transp. Syst. 20 (1), 17-32. https://doi.org/10.1080/15472450.2014.889918.


[^0]:    Peer review under the responsibility of Tongji University

    * Corresponding author.
    E-mail address: maskamal@gunma-u.ac.jp (M.A.S. Kamal).

