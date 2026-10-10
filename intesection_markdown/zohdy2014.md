![](https://cdn.mathpix.com/cropped/c2946066-c94b-4d8f-94d3-d2a715d92ca8-01.jpg?height=561&width=434&top_left_y=362&top_left_x=70)

# Intersection Management via Vehicle Connectivity: The Intersection Cooperative Adaptive Cruise Control System Concept 

Ismail H. Zohdy ${ }^{\text {a }}$ \& Hesham A. Rakha ${ }^{\text {a }}$<br>${ }^{\mathrm{a}}$ Charles E. Via, Jr. Department of Civil and Environmental Engineering, Virginia Polytechnic Institute and State University, Blacksburg, Virginia, USA<br>Accepted author version posted online: 21 Feb 2014.Published online: 06 Dec 2014.

CrossMark
Click for updates

To cite this article: Ismail H. Zohdy \& Hesham A. Rakha (2014): Intersection Management via Vehicle Connectivity: The Intersection Cooperative Adaptive Cruise Control System Concept, J ournal of Intelligent Transportation Systems: Technology, Planning, and Operations, DOI: 10.1080/ 15472450.2014.889918

To link to this article: http://dx.doi.org/ 10.1080/ 15472450.2014.889918

PLEASE SCROLL DOWN FOR ARTICLE
Taylor \& Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor \& Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor \& Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms \& Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

# Intersection Management via Vehicle Connectivity: The Intersection Cooperative Adaptive Cruise Control System Concept 

ISMAIL H. ZOHDY and HESHAM A. RAKHA<br>Charles E. Via, Jr. Department of Civil and Environmental Engineering, Virginia Polytechnic Institute and State University, Blacksburg, Virginia, USA


#### Abstract

Since the introduction of the vehicle infrastructure integration (VII) and connected vehicle (CV) initiatives in the United States, numerous in-vehicle technologies based on wireless communications are currently being deployed. One of these technologies is cooperative adaptive cruise control (CACC) systems, which provide better connectivity, safety, and mobility by allowing vehicles to travel in denser platoons through vehicle-to-vehicle (V2V) communication. Accordingly, the research presented in this article develops a simulation/optimization tool that optimizes the movement of CACC-equipped vehicles as a replacement for traditional intersection control. This system, which is named iCACC, assumes that the intersection controller receives vehicle requests to travel through an intersection and advises each vehicle on the optimum course of action ensuring no crashes occur while at the same time minimizing the intersection delay. Four intersection control scenarios are compared, namely: a traffic signal, an all-way stop control (AWSC), a roundabout, and the iCACC controller. The results show that the proposed iCACC system significantly reduces the average intersection delay and fuel consumption level by 90 and 45\%, respectively. Additionally, the article investigates the impact of vehicle dynamics, weather conditions, and level of market penetration of equipped vehicles on the future of automated vehicle control.


Keywords Connected Vehicles; Cooperative Cruise Control; Intersection Management

## INTRODUCTION

The idea of an automated driving environment has been researched for decades in an attempt to enhance mobility and safety. Recently, some successful trials have been implemented, especially at the Defense Advanced Research Projects Agency (DARPA) Grand Challenge as one of the main field tests designed to accelerate research and development (R\&D) in autonomous ground vehicles. Examples include the Ohio State University (OSU) autonomous ground vehicles (Chen et al., 2004), the Stanley (Thrun et al., 2006), and also the Google

[^0]Driverless car (Markoff, 2011a). After successful tests of autonomous vehicles, Nevada passed a law to allow self-driving vehicles on the road as of March 1, 2012. The law asks the Department of Motor Vehicles (DMV) to create a driver's license endorsement for such vehicles (Markoff, 2011b).

Since the initialization of the connected vehicle (CV) research program, a number of vehicle technologies are being developed using wireless communication (RITA, 2012). With in-vehicle automation and vehicle connectivity gaining momentum, cooperative adaptive cruise control (CACC) systems are expected to enter the market as an application for in-vehicle speed adaptation. The CACC is considered the latest generation of the traditional cruise control systems and the next generation of the adaptive cruise control (ACC) system. In such a system, vehicles can communicate with other vehicles (V2V) and infrastructure (V2I) within a communication range using CV technologies. The CACC system was mainly introduced for use on highways to reduce the gaps between vehicles. Literature
available on CACC (i.e., speed adaptation) is limited to studies on development of this technology and driver compliance to use of this technology. The majority of studies use simulation to validate the system.

Assuming the technology matures and the connected vehicles hit the market, many of the running vehicles will be equipped with highly sophisticated sensors and communication hardware and certainly there will be a need for innovative algorithms for controlling these vehicles. Very limited research efforts have studied the impact of advanced cruise control and automated vehicle systems on intersection performance compared to the many highway studies. As a result, the main goal of the research effort presented in this article is to develop a system for intersection control that communicates with equipped vehicles to adjust their trajectories within what is termed the intersection zone (IZ).

Consequently, this article presents the state-of-the-art of a proposed optimization/simulation tool for CACC-equipped vehicles in the vicinity of intersections, entitled iCACC (intersection management using cooperative adaptive cruise control). The iCACC system optimizes vehicle trajectories to ensure that no collisions occur while at the same time minimizing the total intersection delay in real time. Optimizing vehicle trajectories may have an inherent advantage of reducing the fuel consumption. It is proposed that the intersection be equipped with a controller that receives requests from vehicles approaching the intersection zone (IZ), optimizes the vehicle movements, and sends the optimum movement strategies to the vehicles.

## LITERATURE REVIEW

Many of the technical challenges to highway automation Have been addressed in a significant number of research efforts. Most of the past work on ACC or CACC has been based on simulation models, and very few literature studies have applied direct experiments on the roadway, though a few papers investigate the use of ACC or CACC systems for the operation of intersections. These systems are discussed in this section.

Many of the studies directly related on CACC operations at intersections have focused on energy and environmental impacts of these systems. There has been little research on developing dynamic optimal speed advising algorithms on the vehicle side but studies instead have focused on the signal timing side (Nishuichi \& Yoshii, 2005; Stevanovic et al., 2009). The main purpose of the speed advice algorithm is to ensure the arrival of the vehicle at the green light while satisfying various constraints. For emission impacts, Rakha and Kamalanathsharma presented a framework to enhance fuel consumption efficiency "eco-driving" of vehicles while approaching a signalized intersection (Rakha \& Kamalanathsharma, 2011). The framework uses signal phase and timing (SPaT) information that is received via I2V communication to optimize the vehicle trajectory. This is consistent with the European research program GLOSA (Green Light Optimized Speed Advisory) where the speed of an approaching vehicle to the intersection changes to reduce the fuel consumption based on the signal timing (Katsaros et al., 2011).

Using CV technology, Malakorn and Park (2010) explored the difference between the intelligent traffic signal integrated with CACC systems and traditional intersection control. The results showed how the system is beneficial to the drivers and the environment (the reduction of the amount of $\mathrm{CO}_{2}$ and fuel consumption). In 2011, Park et al. (2011) examined an IntelliDrivebased cooperative vehicle-infrastructure control system as an alternative to current transportation infrastructure. The authors evaluated the system from an environmental perspective using life cycle assessment (LCA) and showed how it could improve both the mobility and the environmental performances of the urban corridor.

A few attempts have been made to create driving simulators (or simulation software) to model fully automated/autonomous vehicles. For example, the Ulysses system attempts to prevent automatic vehicles from crashing (Reece \& Shafer, 1991; Bazzan et al., 2012). The Ulysses. Moreover, Dresner and Stone in many publications (Dresner \& Stone, 2004a; Dresner \& Stone, 2004b; Dresner \& Stone, 2005) proposed an intersection control protocol called autonomous intersection management (AIM) and built their custom simulator using a multiagent approach. The AIM custom simulator is based on the reservation paradigm, in which vehicles "call ahead" to reserve space-time in the intersection under a first-in-first-out (FIFO) policy (Dresner \& Stone, 2004). The main concept is that each autonomous vehicle sends a request to the intersection manager and requests permission to pass through the intersection. Thereafter, the intersection manager decides whether to grant or reject the requested reservations. By expanding the previous work, Fajardo et al. (2011) compared the performance of a simulated intersection in two different scenarios: automated control (first come, first served [FCFS]), and signal control using Synchro software. The results showed that automated control could dramatically reduce the delay time compared to the traditional scenario.

In summary, the previous studies have several limitations and shortcomings:

1. All previous simulation tools manage the movement of automated vehicles without optimizing the global benefit (i.e., total intersection delay). Some algorithms only optimize conflicting vehicle trajectories but not the entire intersection operation and others simply apply the FIFO rule for managing the intersection.
2. All current algorithms do not account for weather condition impacts on roadway friction and how this impacts the system performance.
3. Most of the simulators/algorithms do not use vehicle physical characteristics (e.g., vehicle power, mass, and engine capacity) in the simulation of vehicle acceleration and deceleration behavior; instead, these are assumed to be constant.

4. None of the previous research efforts studied the impact of different vehicle classes/types on the intersection operation.
5. All previous studies ignored the level of penetration (automation), uncertainty and the percentage of error in developing their proposed algorithms. The algorithms have no moving horizon optimization.
6. In a number of studies, the functionality, architecture, or design of the CACC systems was not described.
7. Most of the literature modeled CACC on a case study consisting of a single-lane approach, which is quite similar to the FIFO concept given that overtaking is not possible. Very few references considered multilane approaches with different vehicle movements.

## STUDY OBJECTIVE AND ARTICLE LAYOUT

The objective of this article is to develop an optimization framework for controlling the movement of vehicles equipped with CACC systems at intersections. The research assumes that vehicles have some form of communication with the intersection controller to replace traditional traffic control systems at intersections (traffic signals, stop signs, yield signs, etc.).

To accomplish the research objective mentioned already, a simulation/optimization tool is required to support simulations at a microscopic level of detail. A new user-friendly tool is presented in order to develop an optimal control strategy entitled iCACC (intersection management for CACC equipped vehicles). The tool uses a moving horizon optimization framework to compute the optimal control strategy that ensures no collisions occur while at the same time minimizing the total intersection delay. In case of nonautomated vehicles, it is assumed that the intersection is equipped with roadside sensors or video detection technology to track the movement of these vehicles. Conflicts with these vehicles serve as constraints in the optimization logic. The logic uses lane striping to identify potential vehicle trajectory conflicts. Subsequently, the iCACC system simulates and optimizes the automated vehicle trajectories to ensure that no conflicts result. The system is thus able to deal with different levels of automation, that is, from legacy vehicles (e.g., classic cars with no automation) to fully autonomous vehicles at intersections, as explained later in this article.

In terms of the article layout, initially the iCACC architecture is presented where the different modules of the tool are described. Subsequently, the validation of the proposed system by comparing to traditional signal control system is presented. Thereafter, the sensitivity of the proposed tool to the weather condition and level of penetration is investigated. Finally, the conclusions of the article and the future research directions are presented.

## ICACC SYSTEM OVERVIEW

This research effort is a first attempt at not only addressing some of the issues neglected in state-of-the-art research efforts described earlier, but more importantly developing a real-time simulation/optimization intersection management tool that can operate in a mixed vehicle automation environment. In general, the tool computes and simulates the optimum trajectory of vehicles to ensure no conflicts occur while also minimizing the total intersection delay in real time. The tool enhances the intersection mobility by optimizing the arrival time of vehicles at the intersection box. The assumptions used in developing the tool are:

1. All equipped vehicles in the IZ are assumed to follow the iCACC instructions.
2. Wireless communication is secure and supports high speed and low latency communication.
3. The intersection is fully equipped with roadside sensors to track nonautomated vehicles.
4. All equipped vehicles report their destination, location, speed, and acceleration to the controller at each time step.

The intersection controller is assumed to have full control of the automated vehicles entering the intersection zone (IZ), which is determined by the communication range. Dedicated shortrange communication (DSRC) is assumed for V2I/I2V communication, as recommended in many literature sources (Chen, 2005; Neale et al., 2006; RITA, 2012). The DSRCs are the communications media of choice for safety systems research as they have low latency and are designed to be tolerant to multipath transmissions typical with roadway environments (RITA, 2012). For high efficiency, the suggested communication range in this research is assumed to be 200 m in each direction from the center of the intersection; consequently, this is considered the IZ for the controller. This distance is typical of DSRC systems.

To realize the optimum trajectory for vehicles, the tool consists of three main modules: an input module, an optimization/simulation module, and an output module, as explained in the following subsections. Figure 1 summarizes the different iCACC modules.

## The iCACC Input Module

The iCACC input module consists of five main entry categories: weather, intersection, vehicle, simulation/optimization input, and the built-in state-of-the-art models. Figure 2 shows the graphical user interface (GUI) used to input data to the iCACC tool.

The tool captures inclement weather impacts on both driver behavior and vehicle dynamics. The weather input for the current version of iCACC is divided into four weather categories from 1 to 4 for dry, rain, snow, and ice, respectively. With regard to the intersection input, the tool requires the intersection geometry, the number of lanes per approach, and the speed limit. To account for vehicle differences, the physical characteristics of each vehicle entering the IZ should also be provided. It should

![](https://cdn.mathpix.com/cropped/c2946066-c94b-4d8f-94d3-d2a715d92ca8-05.jpg?height=1603&width=1682&top_left_y=258&top_left_x=161)
Figure 1 The different modules of iCACC.

be mentioned that this option is the first of its kind compared to any similar automated vehicle traffic simulation tool. The fourth entry is limited to the simulation period, number of optimization iterations, and the time increment update for the optimization process $(\Delta t)$.

Last, the iCACC uses few state-of-the-art models for its optimization and comparison purposes, as described in the following subsections. The model uses the Rakha-Pasumarthy-Adjerid (RPA) car-following model that integrates vehicle dynamics and collision avoidance constraints with the Van Aerde steady-state car-following model (Rakha et al., 2009). In addition, the tool utilizes the Virginia Tech comprehensive power-based fuel consumption model (VT-CPFM) to estimate fuel consumption and $\mathrm{CO}_{2}$ emission levels. In addition, as part of modeling various levels of automation, the gap acceptance modeling is a vital part for the optimization process; especially for nonautomated vehicles.

## Van Aerde Steady-State Car-Following Model

The RPA car following model uses the Van Aerde steadystate car-following model (Rakha \& Crowther, 2002) together with vehicle dynamics and collision avoidance models. The RPA car-following model computes the vehicle speed as the minimum of the maximum allowed speed based on vehicle

![](https://cdn.mathpix.com/cropped/c2946066-c94b-4d8f-94d3-d2a715d92ca8-06.jpg?height=962&width=1637&top_left_y=266&top_left_x=275)
Figure 2 The input page of the iCACC tool.

dynamics, the steady-state car-following desired speed, and the collision avoidance speed, as:

$$
\begin{aligned}
& u_{n}(t+\Delta t) \\
& =\min \left\{\begin{array}{l}
u_{n}(t)+3.6 \cdot \frac{F_{n}(t)-R_{n}(t)}{m} \Delta t \\
\frac{-c_{1}+c_{3} u_{f}+\widetilde{s}_{n}(t+\Delta t)-\sqrt{A}}{2 c_{3}} \\
\sqrt{u_{n-1}(t+\Delta t)^{2}+25920 d_{\max }\left(\tilde{s}_{n}(t+\Delta t)-\frac{1}{k_{j}}\right)}
\end{array}\right\}
\end{aligned}
$$

$$
c_{1}=\frac{u_{f}}{k_{j} u_{c}^{2}}\left(2 u_{c}-u_{f}\right) ; \quad c_{2}=\frac{u_{f}}{k_{j} u_{c}^{2}}\left(u_{f}-u_{c}\right)^{2} ;
$$

$$
c_{3}=\left(\frac{1}{q_{c}}-\frac{u_{f}}{k_{j} u_{c}^{2}}\right)
$$

$$
A=\left[c_{1}-c_{3} u_{f}-\tilde{s}_{n}(t+\Delta t)\right]^{2}
$$

$$
-4 c_{3}\left[\tilde{s}_{n}(t+\Delta t) u_{f}-c_{1} u_{f}-c_{2}\right]
$$

$$
\tilde{s}_{n}(t+\Delta t)=s_{n}(t)+\left[u_{n-1}(t)-u_{n}(t)\right] \Delta t
$$

$$
+0.5 a_{n-1}(t) \Delta t^{2}
$$

where $u_{n}(t)$ is the speed of vehicle $n$ at time $t(\mathrm{~km} / \mathrm{h}) . ; c_{1}, c_{2}$, and $c_{3}$ are steady-state car-following model parameters; $u_{f}$ is the free-flow speed $(\mathrm{km} / \mathrm{h}) ; u_{c}$ is the speed-at-capacity $(\mathrm{km} / \mathrm{h}) ; s_{n}(t)$ is the spacing at time (t); $F_{n}(t)$ and $R_{n}(t)$ are the resultant forces acting on vehicle $n$ at time $t ; k_{j}$ is the jam density (veh/km/lane); $q_{c}$ is the capacity (veh/h/lane); $s_{n}(t)$ is vehicle spacing between the following vehicle $n$ and the lead vehicle $n-1(\mathrm{~km})$ at time $t$; $s_{n}(t+\Delta t)$ is the predicted spacing at time $t+\Delta t$ considering that vehicle $n$ continues at its current speed $(\mathrm{km}) ; a_{n}(t)$ is the acceleration of vehicle $n$ at time $t$; and $d_{\text {max }}$ is the maximum acceptable deceleration level the driver is willing to exert $\left(\mathrm{m} / \mathrm{s}^{2}\right)$.

Modeling Vehicle Dynamics
The vehicle dynamics model is used to capture vehicle acceleration constraints. In doing so, the vehicle speed is computed from the resultant forces acting on the vehicle. These forces include the tractive forces given by Eq. 5 and the resistive forces given in Eq. 6:

$$
\begin{aligned}
& F=\min \left(3600 \eta_{d} \frac{P}{v}, m_{t a} g \mu\right) . \\
& R=\frac{\rho}{25.92} C_{d} C_{h} A_{f} v^{2}+m g \frac{c_{r 0}}{1000}\left(c_{r 1} v+c_{r 2}\right)+\mathrm{mgG} .
\end{aligned}
$$

where $\eta_{d}$ is the driveline efficiency (unitless); $P$ is the vehicle power (kW); $m_{t a}$ is the mass of the vehicle on the tractive axle $(\mathrm{kg}) ; v$ is the vehicle speed $(\mathrm{km} / \mathrm{h}) ; g$ is the gravitational acceleration $\left(9.8067 \mathrm{~m} / \mathrm{s}^{2}\right) ; \mu$ is the coefficient of road adhesion (a function of the roadway surface condition) or the coefficient of friction (unitless); $\rho$ is the air density at sea level and a temperature of $15^{\circ} \mathrm{C}\left(1.2256 \mathrm{~kg} / \mathrm{m}^{3}\right) ; C_{d}$ is the vehicle drag coefficient
(unitless), typically $0.30 ; C_{h}$ is the altitude correction factor (unitless); $A_{f}$ is the vehicle frontal area $\left(\mathrm{m}^{2}\right) ; c_{r 0}$ is rolling resistance constant (unitless); $c_{r 1}$ is the rolling resistance constant (h/km); $c_{r 2}$ is the rolling resistance constant (unitless); $m$ is the total vehicle mass (kg); and $G$ is the roadway grade at instant $t$ (unitless).

The vehicle acceleration is calculated as the ratio of the difference in tractive and the resistive forces and the vehicle mass (i.e., $a=(F-R) / m$ ). The vehicle speed at ( $t+\Delta t$ ) is then computed by solving the differential equation using a first-order Euler approximation as:

$$
v(t+\Delta t)=v(t)+3.6 \frac{F(t)-R(t)}{m} \Delta t .
$$

Gap Acceptance Model
A gap is defined as the elapsed-time interval between arrivals of successive vehicles in the opposing flow at a specified reference point in the intersection area. The minimum gap that a driver is willing to accept is generally called the critical gap. The iCACC tool models the minimum acceptable gap for each driver as a stochastic value based on the vehicle capability, the crossing distance, and the weather condition (rain intensity). In an earlier study (Zohdy et al., 2010), it was demonstrated that by increasing the rain intensity, the critical gap (minimum acceptable gap) for the driver increases. The critical gap for different rain intensities can be computed using the following equation:

$$
t_{c}=-\frac{\beta_{0}}{\beta_{1}} \bar{\tau}_{t}-\frac{\beta_{2}}{\beta_{1}} w-\frac{\beta_{3} \bar{\tau}_{t}}{\beta_{1} \bar{r}} r
$$

where $t_{c}$ is the critical gap; $w$ is the waiting time to accept a gap $(\mathrm{s}) ; r$ is the rain intensity $(\mathrm{cm} / \mathrm{h}) ; \bar{r}$ is the average rain intensity at the site; $\bar{\tau}$ is the average travel time to a conflict point; and $\beta_{0}$, $\beta_{1}, \beta_{2}$, and $\beta_{3}$ were estimated to be equal to $-5.65,2.16,0.065$, and -0.11 , respectively. In the iCACC tool, the waiting time is set to be zero and the travel time is calculated using the vehicle dynamics model.

Fuel Consumption Model (VT-CPFM)
The iCACC tool uses the Virginia Tech comprehensive power-based fuel model (VT-CPFM Type 1) due to its simplicity, accuracy, and ease of calibration (Rakha \& Kamalanathsharma, 2011; Rakha, Ahn et al., 2011). The fuel consumption model utilizes instantaneous power as an input variable and can be calibrated using publicly available fuel economy data (i.e., U.S. Environmental Protection Agency [EPA] published city and highway fuel economy ratings). Thus, the calibration of model parameters does not require gathering any vehicle-specific data. The fuel consumption model is formulated in Eq. 9, where $\alpha_{0}$ is the fuel consumption rate (g/s or L/s) for idling conditions and $P(t)$ is the instantaneous total power in kilowatts (kW). Estimation of the model coefficients $\left(\alpha_{1}, \alpha_{2}\right)$ uses the fuel consumption rates of the standard fuel economy cycles (i.e., U.S. EPA published city and highway fuel economy ratings). Specific model relations for this computation can be found in the literature (Rakha, Ahn et al., 2011):

$$
\begin{array}{ll}
F C(t)=\alpha_{0}+\alpha_{1} P(t)+\alpha_{2} P(t)^{2} & \forall P(t) \geq 0 \\
\alpha_{0} & \forall P(t)<0
\end{array} .
$$

## The iCACC Simulation/Optimization Module

In this module, three zones are considered in the optimization logic. These zones include Zone I, Zone II, and the Intersection Box (IB), as shown in Figure 3a.

The ideal profile entails traveling the entire IZ at the speed limit. Zone I is used so that each vehicle can accelerate to the speed limit and maintain that speed for the remainder of the zone (assumed to be 50 m long in this article). As a result, the endpoint of Zone I is considered as the first fixed speed point in the iCACC-optimized profile. This fixed speed point is called the anchor point. In the absence of conflicting vehicles, a vehicle should be able to cross Zone II and the intersection box (IB) at the same maximum speed. For optimization purposes the speed may be reduced in Zone II in order to avoid conflicts with other vehicles. Zone II was assumed to be 150 meters long in this article. At the end of Zone II all vehicles travel at the movement-specific maximum possible speed while traversing the intersection, as illustrated in Figure 3a. This ensures that the speed of all vehicles equals the speed limit at the first anchor point and the maximum movement speed at the second anchor point. In other words, the speed at the second anchor point is based on the movement at the intersection; for example, the left turn movement is assumed to have a lower speed than the through movement. The second anchor point is assumed to be located at the intersection stop line.

The iCACC system adjusts the vehicle speed profile in Zone II so that all vehicles traverse the intersection box at their respective maximum movement speed without colliding with other vehicles. As an example, Figure 3b shows the 16 conflict points in a four-legged, three-lane approach intersection. Ideally, if the vehicle does not decelerate and/or stop in Zone II, it will arrive at the stop line at the shortest time possible (i.e., optimum time, $O T$ ). However, to avoid conflicts with other vehicles, each vehicle may need to decelerate and in some cases come to a complete stop, as is the case with traditional intersection control (traffic signal, stop sign, etc.). The vehicle arrives at the stop line at the actual time, $A T$. By minimizing the summation of the difference between $A T$ and $O T$ for all vehicles, the iCACC system minimizes the total intersection delay.

Consequently, the decision of arrival time for each vehicle is made using an optimization module. In optimizing the vehicle trajectories, the optimization module optimizes the time of arrival of each vehicle at the intersection stop line at each time step (i.e., optimization loop). The main objective of the optimization problem is to minimize the delay $(D)$ that is added to the $O T$, needed to avoid conflicts with crossing vehicles. This

![](https://cdn.mathpix.com/cropped/c2946066-c94b-4d8f-94d3-d2a715d92ca8-08.jpg?height=1751&width=1276&top_left_y=262&top_left_x=475)
Figure 3 (a) The different zones of the optimization process in the iCACC. (b) Vehicle trajectories inside the intersection zone.

optimization problem is formulated as:

$$
\left|\left(O T_{i}+D_{i}+\tau_{m n}\right)-\left(O T_{k}+D_{k}+\tau_{n m}\right)\right| \geq \Delta \tau\left(l_{i m} l_{k n} c_{m n}\right) ; i
$$

$$
\operatorname{Min}: \sum_{i=1}^{\Omega^{1}} D_{i}
$$

$$
\neq k, \forall i, k \in \Omega^{1}, \forall m, n \in \Psi
$$

subject to:

$$
\begin{aligned}
& \left(O T_{i}+D_{i}\right)-\left(O T_{j}+D_{j}\right) \geq H_{\min }\left(l_{i m} l_{j m}\right) ; i \\
& \quad \neq j, \forall i, j \in \Omega, \forall m \in \Psi
\end{aligned}
$$

$$
\begin{aligned}
& \left.\left(O T_{p}+D_{p}+\tau_{n m}\right)\right] ; \forall i \in \Omega^{1}, \forall f, p \in \Omega^{0}, \forall m, n \in \Psi \\
& D_{i} \geq 0 ; \forall i \in \Omega
\end{aligned}
$$

where (as illustrated in Figure 3) $i, j, f$, and $p$ are vehicle identification numbers; $D_{i}$ the time difference between the optimum time $(O T)$ and the actual time $(A T)$ for vehicle $i$ (for the ideal case $D_{i}$ is zero; no deceleration occurs in Zone II); and $O T_{i}$ the optimum arrival time of vehicle $i$ at the PIB (entrance point to the IB), such that $O T_{i}$ is estimated assuming that each vehicle accelerates to the maximum speed in Zone I and continues to travel at that maximum speed until PIB. The arrival time is calculated based on the mathematical equations presented in the following subsection). In addition, $\Omega^{0}$ is the set of vehicles that entered the IZ the last time step and are still in the IZ in the current time step; $\Omega^{1}$ the set of vehicles that enter the IZ in the current time step; $\Omega$ the set of vehicles in IZ in the current time step ( $\Omega=\Omega^{0}+\Omega^{1}$ ); $m$ and $n$ are lane identification numbers; $\Psi$ is the set of lanes at the intersection; $l_{i m}=1$ if vehicle $i$ enters the IB from lane $m$, and 0 otherwise, with $\sum_{m \in \Psi} l_{i m}=1 ; c_{m}=1$ if vehicle $i$ from lane $m$ has a conflict point with vehicles traveling on lane $n$, and 0 otherwise, with $\sum_{m, n \in \Psi} c_{m n}=1$; and $\tau_{m n}$ is travel time from the point PIB of lane $m$ entering into IB to the conflict point of lane $n$. Distance to each conflict point is based on the intersection geometry. It is assumed that all vehicles will be running at maximum speed in the IB, thus, $\tau_{m n}$ is fixed for all vehicles from the same lane $m$ to the same conflict point $m n$ (to facilitate the optimization process). It should be noted that the maximum speed may be different for different movements. Also, $\Delta \tau$ is the duration of time that a vehicle occupies the conflict point, in other words, the safety interval between two consecutive vehicles occupying the same conflict point. To simplify the model formulation and calculation, we assumed $\Delta \tau$ to be identical for all vehicles. This assumption can be relaxed for future testing. Finally, $H_{\text {min }}$ is the minimum headway between vehicles in the same lane.

The objective function (Eq. 10) is to minimize the total delay $\left(D_{i}\right)$ across all vehicles traversing the intersection. In order to achieve the proposed objective, four constraints are listed. Equation 11 ensures that the first in first out (FIFO) rule is maintained for all vehicles in the same lane. In other words, the arrival of each following vehicle should be after the arrival of the leading vehicle in the same lane by the minimum headway (minimum headway $H_{\text {min }}$ ). Equation 12 ensures that a vehicle does not conflict with another vehicle in the IB, by ensuring that the arrival times of two intersecting vehicles at the same conflict point is separated by a minimum safety interval $(\Delta \tau)$. For nonautomated vehicles, the minimum safety interval is considered the minimum acceptable gap (critical gap) value plus the minimum time needed to clear the conflict point.

At each time step (optimization loop), vehicles in the system are divided into two groups, namely, vehicles that entered in previous time steps and are still in the IZ ( $\Omega^{0}$ group) and vehicles that enter are in the current step ( $\Omega^{1}$ group). For the set of vehicles $\Omega^{0}$, the vehicle entry times to the IZ were optimized in previous time steps. Reoptimization of entry times can decrease the algorithm's computational efficiency and increase vehicle fuel consumption by changing vehicle decisions. Hence, only the set of vehicles $\Omega^{1}$ is optimized each time step. At each time step, the occupied time for each conflict point is stored as a new constraint for the following time step (optimization loop), as demonstrated in Eq. 13. The last constraint is the nonnegativity constraint for the additional time $\left(D_{i}\right)$; in other words, the additional time should be zero (no delay) or greater.

In summary, the iCACC tool uses an algorithm consisting of four main steps to solve the optimization problem. First, based on the entry speed and acceleration of each vehicle to the IZ, the arrival time of each vehicle to the IB is estimated. Second, assuming all vehicles will be running at maximum speed, the occupancy time for each conflict point is calculated. Third, the tool begins to search for unsafe conflict points-in other words, the points where the time difference between two crossing vehicles is less than the minimum safety interval $(\Delta \tau)$. Last, the tool modifies the arrival time of each vehicle (triggered as unsafe arrival time) to the IB and determines the optimum additional time needed $(D)$ using Eqs. 10 to 14. It could be stated that the idea of controlling the arrival time of each vehicle at the IB is quite similar to the concept of metered single-lane entrance ramps. In other words, the iCACC controls the flow of vehicles to the entry of the intersection to ensure that they can cross the intersection safely and smoothly with minimum delays.

This problem is a constrained nonlinear optimization program. The optimization module attempts to find the constrained minimum delay of a scalar function (Eq. 10), given an initial estimate of designated variables and subject to constraints 11 through 14. At the start of the optimization process, as an initial estimation, all vehicles are assumed to arrive at the IB at the optimum time $(O T)$, implying delay $\left(D_{i}\right)$ of zero. In solving the problem, the adopted algorithm for optimization is an "interior-point" algorithm. This algorithm-also referred to as a barrier algorithm-attempts to solve the problem as a sequence of approximate minimization problems where the bounds (constraints) are satisfied at all iterations. Consequently, the algorithm can handle large, sparse problems, as well as small, dense problems. The main idea behind the interior point method is fundamentally different from the simplex linear programming (LP) algorithm. Here, the optimal vertex is approached by moving through the interior of the feasible region whereas the simplex moves along the vertices of the feasible solution. This is done by creating a family of parameterized approximate solutions that asymptotically converge to the exact solution (Karmarkar, 1984).

## The iCACC Output Module

After the different input data are provided to the iCACC tool, the optimization process is run and displayed to the output module, as illustrated in Figure 4. The output include:

- The trajectory of each vehicle at $\Delta \tau$ increments (e.g., deciseconds).
- The average delay for every simulated vehicle (s).
- The average fuel consumption for every simulated vehicle (mL).

![](https://cdn.mathpix.com/cropped/c2946066-c94b-4d8f-94d3-d2a715d92ca8-10.jpg?height=1046&width=1753&top_left_y=264&top_left_x=241)
Figure 4 A screen shot for an output example for the iCACC tool.

The tool was built in the MATLAB environment; however, the tool can be compiled as a DLL (Dynamic Link Library) and integrated with any traffic microsimulation software (e.g., VIS-SIM, Paramics, AIMSUN, INTEGRATION, or TransModeler). This is something the researchers are currently investigating.

## CASE STUDY AND SYSTEM EVALUATION

In validating the proposed iCACC algorithm, four different scenarios for intersection control were tested, namely, traffic signal control, AWSC, roundabout, and iCACC control (as shown in Figure 5). The case study intersection consists of four approaches and each approach has two lanes with shared movements. Each lane is 3.5 m wide with a speed limit of 35 mph (approximately $16 \mathrm{~m} / \mathrm{s}$ ). The maximum desired travel speed and the speed at the anchor points are assumed to be the speed limit. In calibrating the vehicle dynamics and fuel consumption model parameters, the physical and mechanical characteristics of a 2010 Honda Accord was used. The vehicle has an engine power of 177 horsepower (Hp). The analysis assumes that the vehicle travels on a good flat asphalt surface (grade 0\%) and the current weather condition is dry.

Table 1 summarizes the specifications and the parameters used for testing the proposed connected vehicle application. The four intersection control scenarios were tested using different random number seeds for 16 different volume combinations, resulting in intersection volume-capacity ratios ranging from 0.15 to 0.9. The major street volume ranged between 500 and 2000 vehicles (veh)/h/approach and the minor street volume ranged between 250 and 1000 veh/h/approach. The direction split for each approach was 0.2:0.6:0.2 for left, through, and right turn movements. The microsimulation software INTE-GRATION was used for simulating the three conventional intersection control scenarios, namely, signal control, AWSC, and roundabout. The signal timing cycle length and phase splits were optimized using the Synchro 6 software and then modeled in the INTEGRATION software. The iCACC intersection control was simulated using the INTEGRATION state-of-theart car-following and vehicle-dynamics models. The entrance time of each vehicle to the intersection zone (IZ) and their initial speed and acceleration were picked using a random number generator.

The iCACC scenario was simulated in MATLAB using the "moving horizon optimization" concept at each time step (i.e., 30 s) to speed up the optimization process. In other words, at each time step, the new entering vehicles to the IZ are optimized with the expected entering vehicles in the following time step. Consequently, by using the moving horizon concept, the optimization process takes leass time, as the preliminary optimization results are used in the following time step as the initial input to the optimization process.

Two measures of effectiveness (MOEs) were computed, namely, the average vehicle delay and the average vehicle fuel

![](https://cdn.mathpix.com/cropped/c2946066-c94b-4d8f-94d3-d2a715d92ca8-11.jpg?height=1723&width=1702&top_left_y=249&top_left_x=155)
Figure 5 Different intersection scenarios: (a) signal, (b) AWSC, (c) roundabout, and (d) iCACC.

consumption level. Table 2 tabulates the different volume cases and the corresponding values of both MOEs for comparison purposes. Delay incurred to a vehicle was computed as the deviation in time to cover the distance under consideration, including the IZ at the speed limit versus its actual travel time. This value was averaged across all vehicles for the four scenarios for the 16 traffic demand cases, as illustrated in Figure 6a. Fuel consumption estimates were made using the VT-CPFM model calibrated for the test vehicle. Input for the model were instantaneous speed vectors for vehicles derived from the MATLAB simulation and trajectories extracted from the INTEGRATION software. The average fuel consumed for the vehicles to pass through the intersection was also computed the same way for all 16 scenarios as shown in Figure 6b.

Figure 6a and 6b compare the benefits of iCACC intersection control over conventional signalized intersection control in terms of delay and fuel consumed on a per-vehicle basis for the different traffic demand scenarios. The intersection and vehicles simulated in all cases were similar in all geometric and physical aspects. The AWSC produced the highest average delay per vehicle, followed by the signal control scenario. The roundabout and iCACC scenarios showed the least average

Table 1 The simulation inputs.
|  | Parameter | Value |
| :--- | :--- | :--- |
| Optimization inputs | Exchanged information rate | 0.1 s |
|  | Number of optimization iterations | 30 Iterations |
|  | Optimization horizon | 20 s |
| Physical parameters of the tested vehicle (2010 | Power of engine (P) | 177 Hp |
|  |  |  |
|  | Transmission efficiency $(\eta)$ | 1453 kg |
|  | Mass on tractive axle $\left(\mathrm{m}_{\mathrm{ta}}\right)$ | 785 kg |
|  | Air drag coefficient $\left(\mathrm{C}_{\mathrm{d}}\right)$ and altitude factor $\left(\mathrm{C}_{\mathrm{h}}\right)$ | 0.3 and 1 |
|  | Frontal area (A) | $2.32 \mathrm{~m}^{2}$ |
|  | Rolling coefficient | $\mathrm{Cr}_{0}=1.75$ |
|  |  | $\mathrm{Cr}_{1}=0.0328$ and $\mathrm{Cr}_{2}=$ 4.575 |
|  | U.S. EPA estimates | City/combined/highway 21/25/31 mpg |


delay per vehicle. The average delay value for the roundabout scenario was almost consistent with the iCACC scenario for each of the traffic demand scenarios. Consequently, it appears that by reducing the number of conflict points (i.e., roundabout), the impact on the average delay is nearly the same as managing/optimizing the movement of crossing vehicles considering a larger number of conflict points (i.e., iCACC). In the case of fuel consumption, the iCACC scenario showed higher savings over the conventional scenarios. The simulation results shows that fuel consumption for the iCACC scenario was, on average, 33\%, 45\%, and 11\% lower than the fuel consumption for the traffic signal control, AWSC, and roundabout scenarios, respectively.

In general, on a vehicle-by-vehicle basis, the iCACC algorithm reduces vehicle delay significantly when compared to conventional intersection control scenarios. In the case of highvolume intersections, the iCACC optimization algorithm would compromise the no-stop constraints and thus revert to the "firstin-first-out" concept. In other words, once the system could not find a feasible solution for the optimization process, it would manage the movement of vehicles based on the priority of entering to the intersection zone.

This study demonstrates the promising potential of iCACC intersection control when autonomous vehicles enter the market because it not only seeks crash avoidance but also reduces the total intersection delay and fuel consumption.

## INCLEMENT WEATHER ANALYSIS

Most of the literature on the effect of weather has focused on collision risk, traffic volume variations, signal control, travel pattern, and traffic flow parameters (Cools et al., 2008; Datla \& Sharma, 2008). In addition, there have been limited studies that directly address how adverse weather affects traffic flow variables, including speed, flow, density, capacity, and gap acceptance (Brilon \& Ponzlet, 1996; Rakha et al., 2008; Zohdy, Rakha et al., 2011). However, it is hard to find studies that characterize individual driver behavior for nonequipped vehicles under adverse weather conditions in conjunction with autonomous vehicles.

The iCACC system captures inclement weather impacts on both driver behavior and vehicle dynamics. The iCACC system has the ability to model the driver behavior in nonautonomous vehicles by adjusting the minimum acceptable gap based on the weather condition and the travel time needed to cross (using the vehicle dynamics model).

Table 2 Simulation results for average delay and fuel consumed for all scenarios.
| Case | Max v/c | Major volume (vph) | Minor volume (vph) | Traffic signal |  | AWSC intersection |  | Roundabout |  | iCACC |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  | Aver. veh delay (s) | Aver fuel use (mL) | Aver. veh delay (s) | Aver fuel use (mL) | Aver. veh delay (s) | Aver fuel use (mL) | Aver. veh delay (s) | Aver fuel use (mL) |
| 1 | 0.15 | 500 | 250 | 10.4 | 25.7 | 12.8 | 26.6 | 1.8 | 23.9 | 1.0 | 20.8 |
| 2 | 0.20 | 600 | 300 | 14.4 | 28.3 | 13.2 | 26.7 | 2.1 | 24.0 | 1.3 | 21.4 |
| 3 | 0.25 | 700 | 350 | 15.4 | 28.6 | 14.2 | 27.1 | 2.3 | 24.0 | 2.1 | 21.2 |
| 4 | 0.30 | 800 | 400 | 16.6 | 28.1 | 15.4 | 27.6 | 2.6 | 24.1 | 2.8 | 21.6 |
| 5 | 0.35 | 900 | 450 | 15.7 | 29.0 | 19.4 | 29.5 | 2.8 | 24.3 | 3.3 | 21.7 |
| 6 | 0.40 | 1000 | 500 | 15.2 | 28.3 | 21.1 | 30.3 | 3.0 | 24.4 | 4.5 | 22.3 |
| 7 | 0.45 | 1100 | 550 | 16.7 | 30.8 | 22.2 | 30.8 | 3.2 | 24.5 | 4.0 | 22.0 |
| 8 | 0.50 | 1200 | 600 | 22.0 | 29.9 | 40.3 | 39.3 | 3.6 | 24.7 | 4.2 | 22.7 |
| 9 | 0.55 | 1300 | 650 | 19.9 | 31.0 | 52.5 | 45.1 | 4.1 | 25.0 | 4.5 | 22.8 |
| 10 | 0.60 | 1400 | 700 | 18.4 | 30.3 | 55.2 | 46.3 | 3.9 | 24.8 | 4.6 | 22.3 |
| 11 | 0.65 | 1500 | 750 | 18.8 | 35.4 | 60.0 | 48.4 | 4.5 | 25.2 | 5.1 | 22.9 |
| 12 | 0.70 | 1600 | 800 | 19.7 | 36.9 | 68.1 | 52.2 | 4.8 | 25.3 | 5.2 | 22.8 |
| 13 | 0.75 | 1700 | 850 | 23.3 | 36.3 | 75.6 | 55.7 | 5.5 | 25.7 | 5.5 | 22.9 |
| 14 | 0.80 | 1800 | 900 | 31.7 | 39.7 | 72.3 | 54.1 | 6.0 | 25.9 | 5.6 | 22.7 |
| 15 | 0.85 | 1900 | 950 | 34.2 | 44.5 | 76.6 | 56.1 | 6.8 | 26.2 | 6.5 | 23.2 |
| 16 | 0.90 | 2000 | 1000 | 39.5 | 49.3 | 76.8 | 56.1 | 8.3 | 27.0 | 6.3 | 23.1 |


Note. Shaded cells indicate the lowest value for the specific case. Aver., average; veh, vehicles.

![](https://cdn.mathpix.com/cropped/c2946066-c94b-4d8f-94d3-d2a715d92ca8-13.jpg?height=2058&width=1480&top_left_y=346&top_left_x=264)
Figure 6 Comparison between different scenarios: (a) average delay comparison per vehicle (seconds) and (b) average fuel consumption per vehicle (milliliters).

Table 3 The weather adjustment factors.
| Classification | Weather adjustment factors |  |  |
| :--- | :--- | :--- | :--- |
|  | Dry | Rain | Snow |
| Free flow speed | 1 | 0.960 | 0.910 |
| Speed at capacity | 1 | 0.960 | 0.840 |
| Capacity | 1 | 0.890 | 0.880 |
| Minimum acceptable gap (tc) | 1 | 1.104 | 1.190 |


Table 4 The optimization simulation inputs.
|  | Parameter | Value |
| :--- | :--- | :--- |
| Car-following and gap acceptance parameters | Weather | Dry, rain, and snow |
|  | Approach free-flow speed $u_{f}$ | 38 mph (60 km/h) |
|  | Approach speed-at-capacity $u_{c}$ | 25 mph (38 km/h) |
|  | Approach jam density $k_{j}$ | 143 veh/km |
|  | Approach capacity $q_{c}$ | $1700 \mathrm{veh} / \mathrm{h}$ |
|  | Minimum acceptable gap (critical gap) for nonautomated vehicles (for dry conditions) | 4 s |
|  | Minimum acceptable gap for autonomous vehicles | Estimated travel time needed to reach and clear the conflict point |
|  | Roadway adhesion ( $\mu$ ) | Dry 1, wet 0.8, and snow 0.6 |


The objective of this section is to extend the previous analysis and investigate the impact of inclement weather on the intersection performance under different levels of market penetration and congestion. Specifically, this study investigates general approaches to construct simulation models accounting for the impact of rain and snow precipitation by means of calibrating car-following and gap-acceptance models. The adjustment factors corresponding to each weather condition are summarized in Table 3 (Rakha, Zohdy et al., 2011).

The evaluation of the iCACC system is made considering three different volume scenarios for a maximum volume-tocapacity (v/c) ratio of 0.2, 0.5 and 0.8. The simulated level of penetration ranges from 20 to 100\%. All input information for the optimization process is summarized in Table 4. A Monte Carlo simulation is adopted using random seeds to evaluate the different combinations of weather conditions, v/c ratios, and levels of market penetration. Two MOEs are calculated to evaluate the optimization/simulation performance: average vehicle delay and the average fuel consumed. These are computed using a decisecond interval for the vehicle trajectories derived from the MATLAB simulation. Table 5 summarizes the average vehicle delay and fuel consumed for different scenarios.

Given that it is not anticipated that the level of market penetration would be high in the near future, the research evaluates the performance of the intersection for various levels of market penetration. Obviously, by increasing the level of penetration (automation), the iCACC is able to reduce the delay and fuel consumption level by controlling the movements of the accessible autonomous vehicles. Consequently, at 100\% level of market penetration (LMP), the potential benefits are provided if full deployment of CACC is achieved.

The results demonstrate that in case of low volumes (v/c = 0.2), the impact of introducing the iCACC intersection controller is relatively small when compared to more congested conditions. For the high volume case (v/c = 0.8), the iCACC is able to significantly reduce the delay and fuel consumption level. On the other hand, for dry condition scenarios, as would be expected, the delay and fuel consumption levels are lower than the rainy and snowy condition scenarios. Both plots in Figure 7 illustrate the variation in the average delay and fuel consumption values, with the increase in the LMP corresponding to different weather conditions.

The impact of weather condition was captured in various models: vehicle dynamics (coefficient of friction and rolling resistance coefficients), car following (free-flow speed, speed-at-capacity, and capacity), and the gap acceptance models (critical gap and follow-up time). In other words, the weather condition directly affected the vehicle acceleration capabilities

Table 5 Average delay and fuel consumed for all scenarios.
| LMP | MOE | $\mathrm{V} / \mathrm{C}=0.2$ |  |  | $\mathrm{V} / \mathrm{C}=0.5$ |  |  | $\mathrm{V} / \mathrm{C}=0.8$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | Dry | Rain | Snow | Dry | Rain | Snow | Dry | Rain | Snow |
| 20\% | Delay (s) | 2.96 | 7.70 | 13.84 | 6.42 | 10.72 | 12.12 | 7.75 | 17.78 | 19.64 |
|  | Fuel (mL) | 22.46 | 24.24 | 26.98 | 23.13 | 25.45 | 26.05 | 24.16 | 27.91 | 27.98 |
| 40\% | Delay (s) | 2.81 | 6.56 | 14.06 | 5.93 | 12.90 | 13.97 | 6.61 | 17.15 | 15.19 |
|  | Fuel (mL) | 22.30 | 23.80 | 27.09 | 23.05 | 26.54 | 26.94 | 23.97 | 27.81 | 26.09 |
| 60\% | Delay (s) | 2.34 | 11.80 | 15.46 | 5.57 | 10.92 | 13.70 | 5.92 | 21.52 | 18.77 |
|  | Fuel (mL) | 22.03 | 26.19 | 27.70 | 22.97 | 25.66 | 26.98 | 23.59 | 29.76 | 28.16 |
| 80\% | Delay (s) | 2.09 | 8.13 | 13.19 | 5.29 | 4.06 | 18.11 | 6.25 | 10.72 | 12.12 |
|  | Fuel (mL) | 21.84 | 24.50 | 26.67 | 22.50 | 22.60 | 28.97 | 23.13 | 25.45 | 26.05 |
| 100\% | Delay (s) | 1.29 | 4.06 | 18.11 | 4.21 | 8.61 | 13.84 | 5.60 | 12.43 | 16.05 |
|  | Fuel (mL) | 21.40 | 22.60 | 28.97 | 22.4 | 24.57 | 26.90 | 22.7 | 26.15 | 27.10 |


![](https://cdn.mathpix.com/cropped/c2946066-c94b-4d8f-94d3-d2a715d92ca8-15.jpg?height=1925&width=1272&top_left_y=294&top_left_x=367)
Figure 7 The impact of level of penetration, v/c, and weather condition on (a) average delay per vehicle (seconds) and (b) average fuel consumption (milliliters) per vehicle.

and the decision of nonautonomous vehicles (gap acceptance/rejection) at the intersection zone (IZ).

In general, the weather causes various impacts on traffic management during and after weather events. However, the linkages between inclement weather conditions and advanced automated systems remain tenuous. The primary concern of the analyst is to understand how drivers make their decisions at intersections for various levels of market penetration of the system under
different weather conditions. Additionally, this section demonstrates how the impact of inclement weather and LMP of automated vehicles could impact the results.

## CONCLUSIONS AND FUTURE WORK

CACC systems can provide better connectivity, safety, and mobility by allowing vehicles to travel in denser platoons through vehicle-to-vehicle (V2V) communication. Accordingly, the research presented in this article developed a simulation/optimization tool that optimizes the movement of CACCequipped vehicles in the vicinity of intersections. This system, which is labeled iCACC, assumes that the intersection controller receives vehicle requests to travel through an intersection and advises each vehicle on the optimum course of action ensuring no crashes occur while at the same time minimizing the intersection delay. These recommendations are made in real time at each time step. The proposed system was tested and compared to different intersection control approaches using multiple traffic volume combinations. The results showed that the proposed iCACC system significantly reduced the average intersection delay and fuel consumption level by 90\% and 45\%, respectively. Additionally, the article demonstrated how the impact of inclement weather and LMP of automated vehicles could impact the results.

As with any research effort, additional work is needed to integrate the iCACC tool within state-of-the-art traffic simulation tools to conduct further testing of the system, extend the logic to deal with higher levels of congestion, and extend the system to consider multiple intersections. Finally, the results from this research warrant studies with regard to incorporating non-CACC vehicles into the system and studies pertaining to tackling unexpected system changes, pedestrian movements, and so on.

## FUNDING

The authors acknowledge the financial support provided by the Connected Vehicle University Transportation Center (UTC).

## REFERENCES

Bazzan, A., Amarante, M., \& Costa, F. (2012). Management of demand and routing in autonomous personal transportation. Journal of Intelligent Transportation Systems, 16(1), 1-11.
Brilon, W., \& Ponzlet, M. (1996). Variability of speed-flow relationships on German autobahns. Transportation Research Record, 1555, 91-98.
Chen, C. Y. (2005). California intersection decision support: A systems approach to achieve nationally interoperable solutions. California PATH Research Report. UCB-ITS-PRR-2005-11. Retrieved from http://safetrec.berkeley.edu/sites/default/files/UCB-ITS-PRR-2005-11.pdf
Chen, Q., Ozguner, U., \& Redmill, K. (2004). Ohio State University at the 2004 DARPA Grand Challenge: Developing a completely autonomous vehicle. IEEE, 9(5), 8-14.
Cools, M., Moons, E., \& Wets, G. (2008). Assessing the impact of weather on traffic intensity. Transportation Research Board Proceedings, paper 08-1903.
Datla, S., \& Sharma, S. (2008). Association of highway traffic volumes with cold, snow and their interactions. Transportation Research Board, paper 08-0843. Retrieved from http://trid.trb.org/ view.aspx?id=847702
Dresner, K., \& Stone, P. (2004a). Multiagent traffic management: A protocol for defining intersection control policies. Technical report UT-AI-TR-04-315. Austin, TX: University of Texas at Austin, Department of Computer Sciences, AI Laboratory.
Dresner, K., \& Stone, P. (2004b). Multiagent traffic management: A reservation-based intersection control mechanism. Presented at the Third International Joint Conference on Autonomous Agents and Multiagent Systems, New York, NY, 530-537.
Dresner, K., \& Stone, P. (2005). Multiagent traffic management: An improved intersection control mechanism. Presented at the Fourth International Joint Conference on Autonomous Agents and Multiagent Systems, Utrecht, The Netherlands, 471-477.
Fajardo, D., Au, T. C., Waller, S., Stone, P., \& Yang, D. (2011). Automated intersection control: Performance of future innovation versus current traffic signal control. Transportation Research Record: Journal of the Transportation Research Board, 2259. ISSN: 0361-1981.
Karmarkar, N. (1984). A new polynomial-time algorithm for linear programming. STOC'84 Proceedings of the Sixteenth Annual ACM Symposium on Theory of Computing, New York, NY, pp. 302-311.
Katsaros, K., Kernchen, R., Dianati, M., \& Rieck, D. (2011). Performance study of a green light optimized speed advisory (GLOSA) application using an integrated cooperative ITS simulation platform. Presented at International Wireless Communications and Mobile Computing Conference (IWCMC), July 4-8, Istanbul, Turkey.
Malakorn, K. J., \& Park, B. B. (2010). Assessment of mobility, energy, and environment impacts of IntelliDrive-based Cooperative adaptive cruise control and intelligent traffic signal control. Presented at IEEE International Symposium on Sustainable Systems and Technology, December 2010.
Markoff, J. (2011a). Google cars drive themselves, in traffic. The New York Times. Retrieved from http://www.nytimes.com/ 2010/10/10/science/10google.html
Markoff, J. (2011b). Google lobbies Nevada to allow self-driving cars. The New York Times. Retrieved from http://www.nytimes.com/ 2011/05/11/science/11drive.html?_r=2\&emc=eta1
Neale, V. L., Perez, M. A., Doerzph, Z., Lee, S., Stone, S., \& Dingus, T. (2006). Intersection decision support: Evaluation of a violation warning system to mitigate straight crossing path collisions. Virginia Tech Transportation Institute, final contract report number VTRC 06-CR10.
Nishuichi, H., \& Yoshii, T. (2005). A study of the signal control for the minimization of $\mathrm{CO}_{2}$ emission. Proceedings of the 12th World Congress on Intelligent Transport Systems, San Francisco, CA, November 6-10, pp. 20-28.
Park, B. B., Malakorn, K., \& Lee, J. (2011). Quantifying benefits of cooperative adaptive cruise control toward sustainable transportation system. Final report UVACTS-14-5-161. Retrieved from http://www.mautc.psu.edu/docs/UVA-2009-01.pdf

Rakha, H., \& Crowther, B. (2002). Comparison of greenshields, pipes, and Van Aerde car-following and traffic stream models. Transportation Research Record, 1802, 248-262.
Rakha, H., Farzaneh, M., Arafeh, M., \& Sterzin, E. (2008). Inclement weather impacts on freeway traffic stream behavior. Transportation Research Record: Journal of the Transportation Research Board, 2071, 8-18.
Rakha, H., \& Kamalanathsharma, R. (2011). Eco-driving at signalized intersections using V2I communication. Presented at 14th International IEEE Annual Conference on Intelligent Transportation Systems, Washington, DC, October 2011.
Rakha, H., Pasumarthy, P., \& Adjerid, S. (2009). A simplified behavioral vehicle longitudinal motion model. Transportation Letters: The International Journal of Transportation Research, 1(2), 95-110.
Rakha, H., Zohdy, I., Park, S., \& Krechmer, D. (2011). Microscopic analysis of traffic flow in inclement weather, Part 2. Report FHWA-JPO-11-020. Washington, DC.
Rakha, H. A., Ahn, K., Moran, K., \& Saerens, B. (2011). Virginia Tech comprehensive power-based fuel consumption model: Model development and testing. Transportation Research Part D-Transport and Environment, 16(7), 492-503.
Reece, D. A., \& Shafer, S. (1991). A computational model of driving for autonomous vehicles. Technical report CMU-CS-91-122. Pittsburgh, PA: Carnegie Mellon University.
RITA. (2012). Connected vehicle research program (Intel-liDrive). Retrieved from http://www.its.dot.gov/connected_vehicle/connected_vehicle.htm
Stevanovic, A., Stevanovic, J., Zhang, K., \& Batterman, S. (2009). Optimizing traffic control to reduce fuel consumption and vehicular emissions: An integrated approach of VISSIM, CMEM, and VIS-GAOST. Presented at the 88th Annual Meeting of the Transportation Research Board, Washington, DC, January 2010.
Thrun, S., Montemerio, M., Dahlkamp, H., Stavens, D., Aron, A., Diebel, ... Mahoney, P. (2006). Stanley: The robot that won the DARPA Grand Challenge. Journal of Field Robotics, 23(9), 661-692.
Zohdy, I., Rakha, H., Alfelor, R., Yang, D., \& Krechmer, D. (2011). Inclement weather impact on left-turn gap acceptance behavior of drivers. Transportation Research Record: Journal of the Transportation Research Board, 2257, 51-61.
Zohdy, I., Sadek, S., \& Rakha, H. (2010). Empirical analysis of wait time and rain intensity effects on driver left-turn gap acceptance behavior. Transportation Research Record: Journal of the Transportation Research Board, 2173, 1-10.


[^0]:    Address correspondence to Hesham A. Rakha, Charles E. Via, Jr. Department of Civil and Environmental Engineering, Center for Sustainable Mobility, Virginia Tech Transportation Institute, 3500 Transportation Research Plaza, Blacksburg, VA 24061, USA. E-mail: hrakha@vt.edu

    Color versions of one or more of the figures in the article can be found online at www.tandfonline.com/gits.

