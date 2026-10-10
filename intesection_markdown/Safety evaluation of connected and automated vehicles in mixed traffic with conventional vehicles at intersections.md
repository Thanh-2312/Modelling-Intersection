# Safety evaluation of connected and automated vehicles in mixed traffic with conventional vehicles at intersections 

Ramin Arvin , Asad J. Khattak , Mohsen Kamrani \& Jackeline Rio-Torres<br>To cite this article: Ramin Arvin , Asad J. Khattak , Mohsen Kamrani \& Jackeline Rio-Torres (2020): Safety evaluation of connected and automated vehicles in mixed traffic with conventional vehicles at intersections, Journal of Intelligent Transportation Systems, DOI: 10.1080/15472450.2020.1834392

To link to this article: https://doi.org/10.1080/15472450.2020.1834392

Published online: 28 Oct 2020.

Submit your article to this journal

View related articles

View Crossmark data

# Safety evaluation of connected and automated vehicles in mixed traffic with conventional vehicles at intersections 

Ramin Arvin ${ }^{\mathrm{a}}$ (D), Asad J. Khattak ${ }^{\mathrm{a}}$ (D), Mohsen Kamrani ${ }^{\mathrm{a}}$ (D), and Jackeline Rio-Torres ${ }^{\mathrm{b}}$ (D)<br>${ }^{\mathrm{a}}$ Department of Civil and Environmental Engineering, The University of Tennessee, Knoxville, TN, USA; ${ }^{\mathrm{b}}$ Energy \& Transportation Science Division, Oak Ridge National Laboratory, Oak Ridge, TN, USA


#### Abstract

Connected and Automated Vehicles (CAVs) can potentially improve the performance of the transportation system by reducing human errors. This paper investigates the safety impact of CAVs in a mixed traffic with conventional vehicles at intersections. Analyzing real-world AV crashes in California revealed that rear-end crashes at intersections are the dominant crash type. Therefore, to enhance our understanding of the future interactions between human-driven vehicles with CAVs at intersections, a simulation framework was developed to model the mixed traffic environment of Automated Vehicles (AV), cooperative AVs, and conventional human-driven vehicles. In order to model AVs driving behavior, Adaptive Cruise Control (ACC) and cooperative ACC (CACC) models are utilized. Particularly, this study explores system improvements due to automation and connectivity across varying CAV market penetration scenarios. ACC and CACC car following models are used to mimic the behavior of AVs and cooperative AVs. Real-world connected vehicle data are utilized to modify and tune the acceleration/deceleration regimes of the Wiedemann model. Next, the driving volatility concept capturing variability in vehicle speeds was utilized to calibrate the simulation to represent the safety performance of a real-world environment. Two surrogate safety measures are used to evaluate the safety performance of a representative intersection under different market penetration rate of CAVs: the number of longitudinal conflicts and driving volatility. At low levels of ACC market penetration, the safety improvements were found to be marginal, but safety improved substantially with more than 40\% ACC penetration. Additional safety improvements can be achieved more quickly through the addition of cooperation and connectivity through CACC. Furthermore, ACC/CACC vehicles were found to improve mobility performance in terms of average speed and travel time at intersections.


ARTICLE HISTORY
Received 24 September 2019
Revised 9 July 2020
Accepted 24 August 2020

## KEYWORDS

Adaptive cruise control; connected and automated vehicles; cooperative adaptive cruise control; driving volatility; intersection safety; mobility; simulation; time to collision

## Introduction

According to the National Highway Traffic Safety Administration, there were more than 7.27 million vehicle crashes across the United States that caused 2.17 million injuries and 37,914 fatalities in 2016 (Anon, 2018). Given that human error is contributing to more than 90 percent of crashes (Singh, 2015), Automated Vehicles (AV) aim to improve the current state of transportation through eliminating human drivers from the driving task. A system of AVs offers significant potential to reduce crashes and related losses as well as reduce traffic congestion. The development and deployment of AVs creates a world of possibilities and questions. As prototype AVs are already commuting in the transportation network, widespread use of AVs is anticipated in the near future. The interaction between AVs and nonautomated vehicles raises many concerns as the driving styles and driving responses to the environment vary from driver to driver, and that can cause a disturbance in the traffic network. Referring to the AVs, Adaptive Cruise Control (ACC) is introduced as one of the driving assistant systems performing longitudinal control of AVs by automatically controlling vehicle movements and responding to the preceding vehicle. On the other hand, Connected and Automated Vehicles (CAVs) integrate connectivity and automation using Cooperative ACC (CACC), which is extending ACC by utilizing vehicle-to-vehicle (V2V) communication which allows cooperation among AVs. While the impact of AVs on transportation safety remains unknown due to lack of real-world data, microsimulation study can be the most costeffective approach for evaluation of potential benefits/
drawbacks of mass market adoption of AVs. This study presents a simulation framework to assess the impact of varying levels of AVs market penetration in a mixed traffic with conventional vehicles which can provide initial safety impact understanding on the implementation of AVs. While a few studies have explored the safety impact of AVs, the main goal of this paper is to explore the safety implications of AVs interacting with conventional vehicles at a signalized intersection.

This study analyzes the real-world AV-involved crashes in California in order to understand the current crash mechanism. Next, the interaction of AVs with conventional human-driven vehicles at a signalized intersection is simulated. The ACC and CACC models are utilized to simulate longitudinal control of AVs with and without cooperation. Furthermore, real-world Connected Vehicle (CV) data are used to revise the acceleration/deceleration regimes of the Wiedemann car-following model to accurately represent longitudinal vehicle control and following behavior of human drivers. Furthermore, the CV data was harnessed to calibrate the simulation to truly represent the actual traffic in the baseline scenario. Finally, using a developed behavioral framework, multiple scenarios are defined and simulated to study the mixed traffic of conventional vehicles, ACC, and CACC vehicles.

## Literature review

An analysis of traffic crashes in the United States revealed that the main contributing factor in 93 percent of crashes is human error (Anon, 2008). In an attempt to minimize human errors, new technologies and advanced driving assistant systems (ADAS) are being developed to minimize such errors by providing additional, crucial information to drivers. AV systems offering driver assistance functions can transfer the driving tasks from the human to the Automated Driving System (ADS) to minimize human error. The future of AVs has been studied from various viewpoints, such as policy, society, public opinion, adoption, ethical issues, planning, and so forth (Loeb et al., 2018; Ebnali et al., 2019; Nodjomian \& Kockelman, 2019; Motamedi et al., 2020). Milakis et al. (2017) reviewed AV-related studies and classified them into a three-fold order. The first order of impacts focuses on issues related to travel time, travel cost, travel choices, and road capacity. The second order of impacts focuses on vehicle ownership, vehicle sharing, infrastructure, and land use. Finally, the third order of impacts is concerned with safety, energy and fuel efficiency, public health, etc. Literature suggests that AVs would reduce vehicle ownership (Fagnant \& Kockelman, 2014), travel time (Kesting et al., 2008; Li et al., 2013), parking lots (Fagnant \& Kockelman, 2014), and emissions (Choi \& Bae, 2013; Fagnant \& Kockelman, 2014). It is also suggested that AVs would increase road capacity (Mahdavian et al., 2019; Shladover et al., 2012; Van Arem et al., 2006), traffic flow stability (Parsa et al., 2020; Talebpour \& Mahmassani, 2016), vehicle miles traveled (De Almeida Correia \& Van Arem, 2016; Fagnant \& Kockelman, 2014), fuel efficiency (Asadi \& Vahidi, 2011; Liu et al., 2020; Rios-Torres \& Malikopoulos, 2017b, 2017a), and safety (Arvin et al., 2018; Virdi et al., 2019). However, these benefits are unachievable unless AV penetration reaches a certain threshold. Moreover, this study concludes that the impact of AVs on some aspects such as value of time, long-term energy consumption and air pollution, equity, economy, and public health are still unclear. Furthermore, various factors are contributing to the pace of adoption, such as public opinion, willingness to pay, cybersecurity and safety, and policy barriers.

A few studies have attempted to quantify potential safety impacts of AVs on the transportation system. Microscopic simulation can help researchers evaluate the impact of varying levels of AVs market penetration in a mixed traffic with conventional vehicles. Tibljaš et al. (Deluka Tibljaš et al., 2018) attempted to quantify safety effects of CAVs at roundabouts using VISSIM microsimulation and changing the Wiedemann 99 car-following model parameters to emulate the following behavior of CAVs. Their analysis revealed that there might be a slight increase in conflicts with introduction of CAVs. It is worth noting that the Wiedemann model that they used for simulating CAV longitudinal control does not truly represent real-life CAV behavior. Similarly, Stanek et al. (2018) simulated CAV behavior by adopting Wiedemann 99 model parameters from the literature and studied potential impacts. In another study, Rahman and Abdel-Aty (2018) studied the impact of platooning AVs on expressways using VISSIM software. Surrogate safety measures are used to quantify crash risk, and the results reveal that forming platoons can reduce time to collision between $19 \%$ and $28 \%$. Papadoulis et al. (2019) also studied the safety impact of CAVs on motorways by analyzing time to collision using their developed algorithm, however, the model is not calibrated using real-world CAV data. Li et al. (2017) studied the impact of CACC vehicles on rearend collision risk with different market penetrations
at freeways. By reviewing the literature, it can be inferred that the limitation of the aforementioned studies is that they are focusing on roadway segments, while the interaction of CAVs in a mixed traffic environment at intersections remains unknown.

In the literature, different car-following models are developed to simulate the longitudinal and lateral movements of AVs. The ACC car-following model is one of the most well-known models used in the literature to emulate longitudinal following behavior of AVs. The ACC vehicles are able to perform longitudinal control of the vehicle by maintaining the desired speed and gap without any input from the human driver. By combining automated driving (ACC system) and wireless communication, CACC models further enhance AV's performance by simultaneously responding to the speed and acceleration changes of the leader (Mahdinia et al., 2020; Shladover et al., 2015). Literature has introduced several ACC and CACC frameworks to model AVs behavior (Amoozadeh et al., 2015; Milanés \& Shladover, 2014; Shladover et al., 2012; Xiao et al., 2017), and their widely explored potential benefits in the mixed traffic of conventional vehicles on the mobility in terms of capacity (Olia et al., 2018; Shladover et al., 2012), traffic flow stability (Milanés \& Shladover, 2014; Talebpour \& Mahmassani, 2016), and desired headway (Nowakowski et al., 2011). Furthermore, additional potential mobility impacts of CAVs via platooning (Amoozadeh et al., 2015; Gong et al., 2019), merging areas (Liu et al., 2018b; Rios-Torres \& Malikopoulos, 2017a), and intersections and traffic signals (Ala et al., 2016; Sun et al., 2017; Almannaa et al., 2019; Liu et al., 2019) are discussed in the literature.

While the potential mobility benefits of AVs are widely investigated in the literature, the safety impacts of AVs in the mixed traffic of conventional vehicles remain unknown, specifically at intersections. This study attempts to develop an understanding of the interaction of AVs and conventional vehicles in a mixed traffic environment at intersections, with and without communication between AVs. Notably, the ACC and CACC models developed by (Liu et al., 2018a; Milanés \& Shladover, 2014, 2016; Xiao et al., 2017) are utilized to simulate driving behavior of AVs. It worth noting that the model is validated in a real-world testbed and can truly represent the driving behavior of AVs in the simulation. The main goal of this study is to build the behavioral framework to simulate the interaction of conventional, ACC, and CACC vehicles, and to explore the impact of AVs on the safety performance at intersections by defining and simulating multiple scenarios. In this study, new and unique CV data obtained from the Safety Pilot Model Development (SPMD) collected in Ann Arbor, MI, is used and integrated into the simulation to accurately simulate conventional vehicles driving behavior. The safety performance of an intersection is analyzed using different safety metrics considering various penetration rates of AVs in mixed traffic.

## Methodology

Traffic micro-simulation models are widely used to assess the impacts of new technologies on traffic flow, road system, and society in general (Abdulsattar et al., 2020; Esfahani \& Song, 2019; Sheng et al., 2019; Wu et al., 2020). This study investigates the safety impact of automated vehicles in a mixed traffic environment involving conventional vehicles. In order to include a better representation of the driver behavior of conventional vehicles, the real-world connected vehicle data from the SPMD in Ann Arbor, MI, was used to modify the Wiedemann car-following model and calibrate the simulation. In order to calibrate the simulation with conventional vehicles, the cautiousness and situational awareness coefficients are tuned to reflect the observed driving volatilities at the intersection in the real-world condition. To model the AVs, the ACC and CACC models developed by Milanés and Shladover (2014, 2016); Xiao et al. (2017); and Liu et al. (2018a) were used. Next, to evaluate the safety performance of the intersection under mixed traffic, different scenarios were defined in the simulation considering different market penetrations of AVs. Two surrogate safety measures are used to evaluate the safety performance of a representative intersection under different market penetration rate of CAVs: the number of longitudinal conflicts and driving volatility. Furthermore, mobility impact of AVs in a mixed traffic is explored.

## Evidence in AV crashes

In September of 2014, California state allowed permitholding companies to test their AVs on the public roadways, including freeways, highways, and local streets. As of May 2020, more than 60 permit-holders are testing their automated vehicles in public roads of California within a mixed traffic environment containing human-driven vehicles (Boggs et al., 2020). Although AVs are currently in the prototype stage, analyzing the mechanism of the crashes will provide

Table 1. Summary of California State crash reports from September 2014 to May 2020.
| Variable | Category | Freq. | Percent |
| :--- | :--- | :--- | :--- |
| Location | Intersection | 177 | 72.8\% |
|  | Other | 66 | 27.1\% |
| Crash type | Rear-end | 155 | 63.8\% |
|  | Angle | 19 | 7.8\% |
|  | Sideswipe | 51 | 21.0\% |
|  | Other | 18 | 7.4\% |
| Severity | Property-damage-only | 199 | 81.9\% |
|  | Minor injuries | 44 | 18.1\% |
| Number of involved vehicles | 1 | 18 | 7.4\% |
|  | 2 | 221 | 90.9\% |
|  | 3 | 4 | 1.6\% |
| Time of day | Day | 175 | 72.0\% |
|  | Night | 60 | 24.7\% |
|  | Unknown | 8 | 3.3\% |


insight to the potential issues of AVs in a mixed traffic environment. According to the California Vehicle Code Section 38750, manufacturers are required to report all AV crashes to the California Department of Motor Vehicles (DMV, 2017). From September 2014 to May 2020, there were 243 crash reports involving an AV, and these are used as a database for analysis in this section. It is worth noting that significant effort was taken to manually extract this information from crash report files and narratives. Descriptive statistics for the crash reports are illustrated in Table 1. Among these 243 crashes, 72.8 percent (177 crashes) occurred at the intersections, and 27.1 percent at other locations (66 crashes). It can be inferred that intersections are the most dangerous location due to interrupted traffic flow, and AVs have higher chance of being involved in a crash at intersections. Referring to the type of crashes, 63.8 percent (155 crashes) were rearend, 7.8 percent (19 crashes) were angle crashes, 21.0 percent (51 crashes) were sideswipe, and 7.4 percent (18 crashes) are other types of crashes. It is worth noting that rear-end crashes are the dominant crash type in AV-involved crashes. Further details can be found in Table 1. While the results show that longitudinal conflicts at intersections are the dominant type of conflicts between AVs and conventional vehicles, it should be noted that these AVs are prototypes and their behavior is timid. Further evaluation is required in the future when ADS has matured, and the AVs are fully commercialized.

## Car-following model

## Automated vehicles

In this paper, ACC and CACC models are utilized to simulate the following behavior of AVs. In the following, details of each model are provided.

## ACC Car-following model

The currently available ACC systems enable vehicles to follow a front vehicle by transferring the control task of throttle and brake to the ADS. Specifically, range sensors (i.e. radar, camera, and lidar) enable the ACC vehicle to measure the relative distance and rate of change of the distance of a front vehicle. The ACC system enables the vehicle to adjust its speed to the preceding vehicle considering the desired headway. It should be noted that in the absence of leader, the ACC system will follow a desired speed that is specified by the user.

This study utilizes the ACC car-following model developed and validated with real-world AV data (Liu et al., 2018a; Milanés \& Shladover, 2014, 2016; Xiao et al., 2017). The developed control algorithm in this model relies on four modes depending on the motion purposes: 1- speed control; 2- gap control; 3- gapclosing control; and 4- collision avoidance mode. The latter model is developed by the Transition Areas for Infrastructure-Assisted Driving (TransAID) team (Mintsis, 2018), which tries to avoid rear-end collisions between vehicles. Details on each control mode are discussed.

Speed control: This mode is activated when there is not a leader in front of the subject vehicle, or when the leading vehicle is outside of the detection range of the radar, which is considered 120 m (Xiao et al., 2017; Liu et al., 2018a). This mode maintains the vehicle's speed close to the desired speed. The speed control mode recommends acceleration of vehicle $i$ at time $k+1$ :

$$
a_{i, k+1}=k_{1}\left(v_{d}-v_{i, k}\right)
$$

where $v_{d}$ is the desired speed, $v_{i, k}$ is the current speed of the vehicle $i$ at time $k$; and $k_{1}$ is the control gain, which determines the rate of speed deviation for acceleration. This value is suggested to be $0.3-0.4 s^{-1}$ by (Xiao et al., 2017). In this study, a value of $0.4 s^{-1}$ is selected.

Gap control: The goal of the gap control mode is to keep the desired gap between the ACC and front vehicle (Shladover et al., 2012). When this mode is activated, the acceleration at time $k+1$ can be written as a second-order function based on the speed and gap error with the leading vehicle:

$$
a_{i, k+1}=k_{2} e_{i, k}+k_{3}\left(v_{i-1, k}-v_{i, k}\right)
$$

where $e_{i, k}$ is the gap error at time $k ; k_{2}$ and $k_{3}$ are the control gain parameters for positioning and speed deviations. According to Xiao et al. (Xiao et al., 2017), the proposed values for these parameters can be: $k_{2}=$ $0.23 s^{-2}$ and $k_{3}=0.07 s^{-1}$. Furthermore, according
to Milanés and Shladover (Milanés \& Shladover, 2014, 2016), the gap error can be written as:

$$
e_{i, k}=x_{i-1, k}-x_{i, k}-t_{d} v_{i, k}
$$

where $x_{i-1, k}$ and $x_{i, k}$ denote the position of the following and leader vehicles at the current time $k$, and $t_{d}$ is the desired time gap for the ACC system.

Gap-closing control: The study by Milanes and Shladover (Milanés \& Shladover, 2016) developed the gap-closing mode to model the following behavior of AVs when distance with the front vehicle is lower than 100 m. However, this mode was not fully modeled in this study and Xiao et al (Xiao et al., 2017) tuned the gap-closing control mode by setting parameters of equation (2) as $k_{2}=0.04 s^{-2}$ and $k_{3}=$ $0.8 s^{-1}$. It is worth noting that if the gap between the vehicles lies between 100 m and 120 m, the control mode returns to the previous strategy to guarantee a smooth transition between two control modes.

Collision avoidance control: This control mode is introduced by the TransAID team and added to the ACC car-following model to avoid rear-end collisions. The nature of the collision avoidance control is similar to the gap controller, but is activated when the gap error with the leader is negative and the speed deviation is smaller than $0.1 \mathrm{~m} / \mathrm{s}$. In this manner, values of $k_{2}=0.8 s^{-2}$ and $k_{3}=0.23 s^{-1}$ are suggested to guarantee a hard break for safe operation of ACC vehicles in simulation even in critical events (Mintsis, 2018).

## CACC Car-following model

CACC systems extend the functionality of ACC systems by exploiting information generated by surrounding vehicles via V2V communication. Therefore, it is expected that such an enhanced system further improves transportation performance in terms of safety and mobility. In this study, the CACC model is based on the algorithm that is verified in a real-world condition (Milanés \& Shladover, 2014, 2016; Xiao et al., 2017; Liu et al., 2018a). Similar to the ACC model, it has four control phases including: 1- speed control; 2- gap control; 3- gap-closing control; and 4collision avoidance mode.

The speed control is similar to the ACC model, as the control aims to match the vehicle's speed to the desired speed. It should be noted that transmitted information does not affect the vehicle's cruising mode. The acceleration in the speed control mode can be obtained as:

$$
a_{i, k+1}=k_{4}\left(v_{d}-v_{i, k}\right)
$$

where $k_{4}$ is the speed control gain and is equal to 0.4 $s^{-1}$ (Milanés \& Shladover, 2014).

The gap control of the CACC model is a first-order transfer function, which can be written as:

$$
v_{i, k+1}=v_{i, k}+k_{5} e_{i, k}+k_{6} \dot{e}_{i, k}
$$

where $e_{i, k}$ is the gap error and $\dot{e}_{i, k}$ is the first derivative of the gap error. The values of $k_{5}$ and $k_{6}$ are suggested as $0.45 \mathrm{~s}^{-2}$ and $0.0125 \mathrm{~s}^{-1}$, respectively (Liu et al., 2018a). Furthermore, the derivative of the gap error can be defined as:

$$
\dot{e}_{i, k}=v_{i-1, k}-v_{i, k}-t_{d} \alpha_{i, k}
$$

where $\alpha_{i, k}$ is the acceleration at time $k$, and $t_{d}$ is the CACC controller defined desired time gap.

The collision avoidance mode of the CACC system is designed to avoid rear-end collisions in the simulation. The controller's logic is similar to the gap control mode, and the difference is the gain values which are $k_{5}=0.45 s^{-2}$ and $k_{6}=0.05 s^{-1}$ (Mintsis, 2018).

## Human-driven vehicles

The Wiedemann car-following model was used to model human driving behavior for conventional vehicles. This psychophysical model introduced by Rainer Wiedemann in 1974 has been widely used by researchers to model car-following (Wiedemann, 1974). To model the driving behavior of the following vehicle, Wiedemann considered four regimes of driving:

1. Free-driving regime: This regime illustrates the condition in which the behavior of the vehicle is not affected by the lead vehicle since the clearance gap with it is more than 150 meters. In this regime, the driver just reaches and maintains the desired speed.
2. Closing-in regime: In this regime, the distance with the leader vehicle is less than 150 meters and the driver perceives that he/she is approaching the leader due to higher speed and attempts to adjust it to maintain a safety gap.
3. Following regime: In this regime, the subject vehicle attempts to maintain a desired headway with the front vehicle by adjusting the acceleration/deceleration.
4. Emergency regime: In this regime, the clearance gap between the leader and following vehicle is smaller than the desired distance gap and the following vehicle decelerates with his/her maximum capability to avoid crash with the leading vehicle.

Figure 1 illustrates the regimes and thresholds of the Wiedemann model, which are defined and utilized according to the relative speed and distance between

![](https://cdn.mathpix.com/cropped/365d0b84-6b99-43a6-b9d3-084c8fc944da-07.jpg?height=978&width=1255&top_left_y=183&top_left_x=372)
Figure 1. Thresholds and driving regimes in the Wiedemann model.

the following and leading vehicle (Wiedemann, 1974). The thresholds can be defined as:
> $S D V$ : The threshold at which the driver realizes speed difference, CLDV: The threshold where the driver realizes positive speed differences where the gap is decreasing, OPDV: The threshold at which the driver realizes negative speed differences where the gap is increasing, AX: The desired distance gap between stationary vehicles, $A B X$ : The desired minimum following distance at low relative speeds, and SDX: The maximum following distance.

Various formulations of the Wiedemann model are presented by researchers. In this paper, we used the formulation suggested by Werner (Werner, 2010), which defines the thresholds as:

$$
\begin{gathered}
A X=L+1+2 * \alpha \\
A B X=A X+(1+7 * \alpha) \sqrt{v} \\
S D V=\left(\frac{\Delta x-A X}{C X}\right)^{2} \text { where } C X=25 *(1+\alpha+\beta)
\end{gathered}
$$

(9)
$S D X=A X+E X(A B X-A X)$ where $E X=2-\beta$
$C L D V=S D V * E X^{2}$
$O P D V=C L D V *(-1-2 *$ rand $)$
where $A X$ : desired minimum distance between two stationary vehicles, $A B X$ : desired minimum following distance, $S D X$ : maximum desired following distance, SDV: perception threshold, CLDV: threshold at which the driver starts to react, $O P D V$ : threshold at which the driver perceives speed difference, $L$ : vehicle length, $\alpha$ : Driver's cautiousness, $\beta$ : Driver's situational awareness, and rand: random number with mean 0.5 and standard deviation 0.15.

## Safety surrogate performance measures

In the microsimulation, the environment is collision free because the vehicles follow a pre-defined behavior set known as a car-following model. However, it is still possible to obtain insightful safety information regarding the relative changes in the system, especially when trying to predict future states. Therefore, in this paper, the safety impact of AVs is evaluated utilizing the concepts of number of conflicts and driving volatility, which has been shown to be highly correlated with the crash frequency at intersections (Kamrani et al., 2018b; Arvin et al., 2019b).

## Number of conflicts

A common measure to predict collisions is the number of observed conflicts. Amundsen and Hydén (1977) stated that crashes can be considered as a subset of conflicts. They have shown that the number of conflicts is highly correlated with crash frequency at

![](https://cdn.mathpix.com/cropped/365d0b84-6b99-43a6-b9d3-084c8fc944da-08.jpg?height=722&width=1697&top_left_y=176&top_left_x=215)
Figure 2. Intersection of Washtenaw Ave. and Huron Parkway in Ann Arbor, MI. Study area shown by yellow boundaries.

intersections (Dijkstra et al., 2010). In the literature, one of the most common approaches for quantifying the number of conflicts is time to collision (TTC), which can be written as (Saccomanno et al., 2008):

$$
T T C_{i, t}=\frac{\left(x_{i-1, t}-x_{i, t}\right)-L_{i-1, t}}{v_{i, t}-v_{i-1, t}}
$$

where $x_{i-1}$, and $v_{i-1}$ are the positions and speed of the leader, $x_{i}$ and $v_{i}$ are the speed and speed of the following vehicles, $L_{i-1}$ is the vehicle length, and $t$ refers to the time. In this study, a TTC lower than 0.5 seconds was considered as a serious conflict.

## Driving volatility

Recently, the concept of location-based driving volatility was introduced and utilized to quantify instantaneous variations in driving behavior in a particular geographic area (Kamrani et al., 2018b; Arvin et al., 2019b), or an event (Kamrani et al., 2018a; Wali et al., 2019; Wali \& Khattak, 2020). Various measures of volatility have previously been introduced (Kamrani et al., 2018b) and it was found that speed volatility is highly associated with the crash frequency at intersections (Arvin et al., 2019b; Kamrani et al., 2018b). In this paper, we used this measure as a surrogate safety index. This study utilized the speed volatility which intends to identify the times that the drivers showed volatile driving behavior in speed by defining a threshold and counting the number of outliers. Therefore, we can write:

$$
\text { Speed volatility }=\frac{k>\text { Threshold }}{n} * 100
$$

where $k$ is the number of times that observed speeds that lie beyond the defined threshold, and $n$ is the total number of observations. The threshold is defined as

$$
\text { Threshold }=\bar{v} \pm 2 * S_{d e v}
$$

where $\bar{v}$ is the average speed of the vehicles passing the intersection, and $S_{\text {dev }}$ is the standard deviation of the observed speeds (Hoseinzadeh et al., 2020; Kamrani et al., 2018b). Notably, the simulated speed samples during the times that vehicles stopped at the intersection (zero speeds) are removed for the volatility calculation. Further details can be found in a related study (Kamrani et al., 2018b).

## Simulation setup and calibration

This study utilized SUMO (Simulation of Urban Mobility) open-source microsimulation software (Behrisch et al., 2011). In order to evaluate the predefined scenarios involving multiple degrees of automation, the intersection of Huron parkway and Washtenaw Avenue in Ann Arbor, Michigan was selected (Figure 2, right). We have simulated 600 ft in each direction of the intersection, and intersection territory is defined as 250 ft from the intersection center (Figure 2, left), which is recommended by the Highway Safety Manual for the intersection safety analysis (HSM, 2010). Since intersection characteristics are highly correlated with the safety outcome (Kamrani et al., 2018b; Wali et al., 2018; Arvin et al., 2019b), this information is retrieved from the Metropolitan Planning Organization Website (http:// semcog.org/). In particular, the speed limit, average annual daily traffic (AADT), and number of lanes were used in the simulation.

Model calibration
In order to calibrate the micro-simulation to generate reasonable approximation of real-world traffic conditions at the selected intersection, the following steps were taken:

1. The Wiedemann car-following model was modified to generate more realistic acceleration and speed patterns.
2. The simulation is calibrated by incorporating safety measures for the conventional vehicles (base scenario).

In the following, the details for each step will be discussed.

Modifying the Wiedemann car-following model
Realistic acceleration limits were extracted from a plot of real-world acceleration versus speed to obtain accurate behavior trends in the simulation. The emergence of big data from connected vehicles provides enriched data which enabled us to compare the real-world data with simulation data. The data for this study was retrieved from the Intelligent Transportation System DataHub website (https://www. its.dot.gov/data/), collected in Ann Arbor, Michigan, utilizing more than 2800 connected vehicles operating under the real-world condition. The vehicles transmitted instantaneous vehicle information including their speed, acceleration, and coordinates at the frequency of 10 Hz via Basic Safety Messages (BSM). Using the coordinates of the intersection, along with the vehicle speed and acceleration, observations from more than 2300 vehicles passing through the intersection were extracted ( $\mathrm{n}=6,911,987 \mathrm{BSMs}$ ). It should be mentioned that the extracted data is also used for the model calibration (see following subsection).

Figure 3 (top) provides the plot of acceleration versus speed for the real-world CV data passing the selected intersection. As discussed in the literature (Arvin et al., 2018; Kamrani et al., 2018b), it can be observed that with an increase in the vehicle speed, the acceleration and deceleration capability of the vehicles decline. We compared this result with the simulation output of SUMO for the conventional vehicles following the default Wiedemann model in the software and the results are provided in Figure 3 (bottom, left). Comparing the results, it can be observed that the plot of speed versus acceleration for the default Wiedemann model does not represent the real-world behavior. The acceleration regime of vehicles showing a constant value and the deceleration regime does not reflect the real-world trend. This is due to the coding of the acceleration regime of the Wiedemann car-following model in SUMO that does not consider the fact that vehicles at high speeds are not able to accelerate and decelerate at their maximum capability. In order to overcome this issue, the acceleration/deceleration regimes of the Wiedemann model are modified by revising the boundaries of maximum acceleration/deceleration of the vehicles. Two polynomials were fitted to the real-world data and implemented in the software (as shown in Figure 3). The fitted equations are formulated as:

Acceleration regime : maximum acceleration

$$
\begin{aligned}
= & 1.609+1.583 v-0.4206 v^{2} \\
& +0.04904 v^{3}-0.002949 v^{4} \\
& +0.00008801 v^{5} \\
& -0.000001031 v^{6}
\end{aligned}
$$

Deceleration regime : maximum deceleration

$$
\begin{aligned}
= & -2.485-0.5957 v+0.117 v^{2} \\
& -0.008575 v^{3}+0.0002959 v^{4} \\
& -0.000003879 v^{5}
\end{aligned}
$$

The preceding two equations were used in the Wiedemann model in SUMO and after running a baseline simulation, the speed versus acceleration plot was generated again (Figure 3, bottom right). Comparing the new results with the real-world data, it can be observed that the modified Wiedemann model significantly improved the representation of the speed versus acceleration pattern. In order to compare the following behavior of vehicles before and after modification, a sample driving profile for three following vehicles is provided in Figure 4. The top two figures illustrate the speed and acceleration trajectories of vehicles following default model, and the two bottom figures are the revised model. The acceleration/deceleration rates of vehicles are unrealistically high in the original Wiedemann model, it can be inferred that the original model does not truly simulate real-life behavior. The modified model is a better representation of real-world following behavior.

To ensure the generated speeds from the simulation accurately represent real-world data, the speed density of the simulation results with the modified Wiedemann and the real-data are plotted and shown in Figure 5. It should be mentioned that due to the difference in signal timing of real-data and simulation, the zero speeds are removed from our analysis. In

![](https://cdn.mathpix.com/cropped/365d0b84-6b99-43a6-b9d3-084c8fc944da-10.jpg?height=1644&width=1712&top_left_y=174&top_left_x=206)
Figure 3. Vehicle speed vs. Acceleration plot of real-world connected vehicle observations (top, $\mathrm{N}=6,911,987$ ); default Wiedemann car-following model used in SUMO (bottom, left), and modified Wiedemann car-following model (bottom, right). Note: Blue, green, and red vehicles represent trajectories of three preceding vehicles passing through the study area

addition, the descriptive statistics of the simulation output and real-data is provided in Table 2. Comparison of the density plots and the descriptive statistics show that the speed generated by the simulation is representative of the real-world traffic condition.

## Calibrating the simulation for the conventional vehicles (base case study)

In the previous steps, the model was modified and verified based on the speed and acceleration output of the simulation, in this step, the simulation was calibrated using the driving volatility as the surrogate safety performance of the intersection. As discussed before, there are two parameters in the Wiedemann model which need to be calibrated in SUMO (their default value is 0.5 ). The $\alpha$ and $\beta$ parameters were calibrated based on the aforementioned driving volatility measures at the intersection. The calibration process leads to $\alpha$ value of 0.08 and $\beta$ value of 0.4 . The speed volatility measure for the connected vehicles passing the study area is 7.11, and simulated vehicles at the intersection shows volatility of 6.88, which shows $3.23 \%$ difference and it is acceptable.

Previous studies (Ahmed, 1999; Kamrani et al., 2014) presented an equation to estimate the minimum number of simulation runs required to ensure that simulation

![](https://cdn.mathpix.com/cropped/365d0b84-6b99-43a6-b9d3-084c8fc944da-11.jpg?height=1164&width=1693&top_left_y=172&top_left_x=155)
Figure 4. Speed and acceleration profiles of vehicles passing through the default and modified Wiedemann models in SUMO.

![](https://cdn.mathpix.com/cropped/365d0b84-6b99-43a6-b9d3-084c8fc944da-11.jpg?height=763&width=1687&top_left_y=1429&top_left_x=157)
Figure 5. Comparison of density plot of the speed for the SUMO simulation and real-world CV data.

results meet the desired confidence interval:

$$
N_{m}=\left(\frac{S_{m} * t_{m-1,1-\frac{\alpha}{2}}}{\bar{x}(m) \alpha}\right)^{2}
$$

where $N_{m}$ is the number of simulation runs, $S_{m}$ is the standard deviation of the simulation output,
$t_{m-1,1-\frac{\alpha}{2}}$ is the $t$ value with $m-1$ degree of freedom and $1-\frac{\alpha}{2}$ two-tail confidence interval, $\bar{x}(m)$ is the mean of the simulation output, and $\alpha$ is the percentage error. In this study, a 95 percent confidence interval is accepted. The calibration procedure leads to the value of $\alpha$ to equal 0.08, and the value of $\beta$ equal to 0.4.

Table 2. Descriptive statistics of vehicle speeds passing through intersections for real CV data and in SUMO simulation.
|  | Number of observations | Mean | Standard deviation | Min* | Max |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Real-Life CV data | 6,911,987 | 7.68 | 4.7 | 0.1 | 35.2 |
| Simulation (SUMO) | 2,700,491 | 7.50 | 4.2 | 0.1 | 24.6 |
| Difference | - | -2.34\% | 10.6\% | - | 29.8\% |


*Note: Since the signal timing for connected vehicle real-world data and the SUMO simulation data are different, speeds lower than 0.1 m/s are removed from the analysis.

Based on the equation (18), $N_{m}$ is lower than the number of required simulation runs, indicating that with 95 percent confidence interval, the generated volatilities in the SUMO simulation is similar to the realworld connected vehicle conditions.

## Results

## Definition of scenarios

In order to explore the safety impact of AVs in mixed traffic with conventional vehicles, this study considered two set of scenarios. The first set of scenarios focuses on different market penetration rates of AVs with no coordination, following ACC car-following model. The penetration rate of ACC vehicles ranges from zero to 100\% in 10\% increments. The second scenario considers coordination of AVs assuming that there is a V2V communication between AVs and the vehicles are following CACC car-following model. If the front vehicle is conventional vehicle or the distance is higher than 120 m, the CACC model downgrades to the ACC mode. It should be noted that the vehicle platooning is not considered in this study due to a limited study area that does not allow for the creation of vehicle platoons.

Prior to running the simulations, the intersection was empty and a one-hour warm up is considered. The simulation was run for the length of one hour, with a step-length of 0.1 second. We considered homogeneous traffic, i.e., all vehicles are assumed to have the same physical characteristics. To model the lane-changing behavior of all vehicle types, we used the default model in SUMO (Erdmann, 2015). For each scenario, the simulation was run 20 times, and the safety performance of scenarios in terms of driving volatility and number of conflicts was assessed.

## Simulation results

## Safety performance measures

Number of conflicts. This section discusses the number of conflicts in the study area to quantify the safety performance of the system under different penetration rates of AVs, with and without cooperation of AVs. For each simulation, 20 runs with random seeds were performed, and each conflict is considered the time that the TTC of two vehicles reaches a 0.5 second threshold. It should be noticed that a conflict is measured as a unique incident in which TTC between two vehicles was below 0.5 seconds, regardless of its duration. In other words, we are counting unique conflicts between consecutive vehicles. The simulation results for 10\% increments in AVs market penetration are provided in Figure 6. Referring to the figure, it can be observed at current state with zero penetration of AVs, number of potential conflicts is 9.94 for one hour of simulation.

In scenario 1, where AVs have no coordination with each other, a slight increase in number of conflicts is observed at 10\% market penetration compared to the baseline. However, with the higher increase in AVs' penetration rate, this reduction is more substantial and significant. Finally, at 100\% penetration of AVs, the number of conflicts reached zero. It can be inferred that a uniform AV response can reduce the relative speed of following vehicles, which leads to an increase in TTC, which then decreases the number of conflicts. Furthermore, by decreasing the penetration rate of conventional vehicles, the frequency of interaction between conventional vehicles will be reduced, which will naturally decrease the likelihood of longitudinal conflicts between human-driven vehicles.

On the other hand, by adding coordination to AVs (i.e. CACC vehicles), AVs are capable of adjusting their behavior in terms of speed with the front vehicle by receiving trajectory information via V2V communication. Based on the results, this coordination capability can further improve safety by decreasing the number of conflicts at the study area. By comparing the ACC and CACC at each penetration rate, it can be observed that there is a substantial reduction in number of conflicts for CACC compared to ACC, which indicates the importance of cooperation for additional improvement in safety performance.

Overall, the results indicate that holding the traffic demand constant, the increase in the market penetration of AVs will decrease the number of conflicts. However, this reduction is not linear and is not

![](https://cdn.mathpix.com/cropped/365d0b84-6b99-43a6-b9d3-084c8fc944da-13.jpg?height=1048&width=1263&top_left_y=178&top_left_x=367)
Figure 6. Number of conflicts observed at simulated intersection and confidence intervals in the study area, in 10\% increments of AV market penetration.

substantial. The results revealed that at lower market penetration, the improvements are not as significant as reductions in high penetration of AVs (i.e. +20 percent). The results are consistent with the findings of Virdi et. al (Virdi et al., 2019) which has shown that the number of CAV conflicts at intersections might not be substantial at low penetrations of CAVs, while an increase in CAV market penetration, will cause more improvements in term of conflicts.
Driving volatility. Previous studies have shown that driving volatility is highly associated with risk and severity of crashes (Arvin et al., 2019a; Kamrani et al., 2019). As discussed in the calibration section, the baseline scenario (zero market penetration of AVs) is calibrated for the driving volatility in order to truly represent safety performance of the vehicles in the simulation. Figure 7 provides the driving volatility for the different penetration rates of ACC and CACC vehicles ranging from zero to 100\%. The red line illustrates the ACC, and the blue line indicates CACC vehicles. Based on the results, with 100\% penetration of ACC and CACC, a significant drop in driving volatility can be observed, and for the mixed traffic scenarios, this reduction is nonlinear and different for ACC and CACC vehicles.

An increase in the market penetration (up to 40\%) for ACC vehicles in mixed traffic is associated with a slight increase in speed volatility. This increase in volatility could be associated with the instability of the ACC model when multiple ACC vehicles are driving consecutively (Milanés et al., 2014; Seiler et al., 2004). Increasing the penetration rate of ACC from 40\% to $60 \%$ is associated with a substantial decrease in speed volatility. However, moving from $60 \%$ to $80 \%$ market penetration contributes to a slight increase in speed volatility. Finally, there is a significant reduction in volatility with more than 80\% ACC penetration, and the speed volatility reaches zero when all vehicles follow the ACC model. Referring to the CACC vehicles, it can be observed that by adding communication to AVs, the speed volatility drops substantially relative to the baseline, and this reduction is much higher compared to the ACC vehicles. The speed volatility nonlinearly dropped with the increase in market penetration of CACC vehicles. By comparing the speed volatility and number of conflicts for the ACC and CACC vehicles, it can be inferred that speed volatility is showing a similar pattern.

Overall, the safety performance measures indicate that the safety performance of the intersection could substantially improve with a high market penetration of AVs that excludes human drivers from the driving task. Both the number of conflicts and the driving

![](https://cdn.mathpix.com/cropped/365d0b84-6b99-43a6-b9d3-084c8fc944da-14.jpg?height=1048&width=1263&top_left_y=178&top_left_x=430)
Figure 7. Speed volatility at simulated intersection for ACC vehicles and CACC vehicles.

volatility substantially decreased, which might be due to uniform AV response which can reduce the relative speed of the lead and following vehicles that could improve safety by decreasing abrupt vehicular movements. Furthermore, conventional vehicle human drivers would change their driving behavior with the passage of time and increase in AVs penetration by learning the AVs response. An analysis of AV involved crashes in California revealed that in almost all of the crashes, AVs were hit by conventional vehicles, since the human driver did not expect the AV behavior (Arvin et al., 2018). This learning process by humans could lead to further improvement in the safety outcome of intersections by reducing the conflicts frequency and driving volatility. However, it is also possible that drivers will game the limitations of AVs and behave more aggressively in their vicinity, which might reduce the improvements.

Mobility analysis. In order to evaluate AV performance in terms of mobility, average travel time and speed of vehicles passing the intersection are considered. The average travel time of vehicles passing the study area is calculated as:

$$
\overline{T T}=\frac{1}{n} \sum_{i=1}^{n}\left(t t_{i}\right)
$$

where $\overline{T T}$ is the average travel time, $n$ is the number of vehicles, and $t t_{i}$ is the travel time of vehicle $i$ passing the study area. The average traveling speed of vehicles is obtained by averaging the mean travel speed of vehicles passing the study area:

$$
\bar{V}=\frac{1}{n} \sum_{i=1}^{n}\left(\overline{v_{i}}\right)
$$

where $\bar{V}$ is the average traveling speed of vehicles passing the intersection, and $\overline{v_{i}}$ is the average speed of vehicle $i$ passing the intersection influence area. It is worth noting that for the mobility analysis, all the simulation time intervals during which the vehicles were passing the intersection was considered, including stoppage times at the intersection.

The results for the scenarios are summarized in Table 3. The results indicate that the increase in the penetration rate of ACC and CACC vehicles significantly improved the mobility in terms of travel time and average speed. The travel time decreased by 24.1\% and 39\% with ACC market penetration of 50\% and $100 \%$, respectively. The cooperation between AVs can further enhance the mobility performance. Compared to the baseline, the average travel time of passing vehicles decreased by 27.1\% and 43.4\% for market penetration rates of CACC vehicles 50\% and $100 \%$, respectively.

Table 3. Average travel time and traveling speed of ACC and CACC vehicles in different market penetration scenarios at simulated intersection.
| Pen. Rate | Travel time (sec) |  |  | Traveling speed (m/s) |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | ACC | CACC | Diff of CACC \& ACC (\%)*** | ACC | CACC | Diff of CACC \& ACC (\%) |
| 0 | Base* | Base | - | Base | Base | - |
| 10 | 88.56 (37.36)** | 88.32 (38.94) | 0.22 | 5.03 (2.79) | 5.13 (2.98) | 1.99 |
| 20 | 83.73 (35.07) | 81.84 (32.81) | 3.65 | 5.71 (2.96) | 5.91 (2.98) | 3.50 |
| 30 | 79.45 (32.02) | 77.51 (31.77) | 2.39 | 5.92 (3.06) | 6.17 (3.11) | 2.53 |
| 40 | 75.2 (31.54) | 73.02 (30.92) | 3.28 | 6.18 (3.35) | 6.46 (3.52) | 4.53 |
| 50 | 72.31 (30.93) | 69.41 (30.88) | 2.75 | 6.66 (3.52) | 6.97 (2.94) | 4.65 |
| 60 | 69.94 (30.46) | 67.27 (30.34) | 2.85 | 7.04 (3.79) | 7.34 (4.02) | 4.26 |
| 70 | 67.23 (30.50) | 64.36 (30.65) | 4.14 | 7.31 (4.03) | 7.78 (4.21) | 4.96 |
| 80 | 64.37 (30.18) | 61.27 (30.34) | 4.99 | 7.52 (4.15) | 7.92 (4.46) | 6.27 |
| 90 | 62.1 (29.91) | 58.36 (30.18) | 5.31 | 7.6 (4.37) | 8.12 (4.57) | 4.70 |
| 100 | 58.11 (38.48) | 53.9 (29.9) | 6.16 | 7.71 (4.48) | 8.21 (4.74) | 5.82 |


Note:.
*At zero percent market penetration, the mean travel time and traveling speed for conventional vehicles is $95.28(\mathrm{SD}=42.07)$ and $4.49(\mathrm{SD}=2.91)$, respectively.
**Numbers in parentheses show the standard deviations.
***Percentage of improvements in travel time and speed gained by CACC vehicles compared to ACC vehicles.

Referring to the traveling speed, it can be inferred that the average speed of vehicles passing through the intersection significantly increased relative to the baseline. With no cooperation between AVs, 50\% and 100\% penetration rate of ACC vehicles can increase average speed by 48.3\% and 71.7\%, respectively. Enabling communication between AVs improved the average speed of passing vehicles by 55.2\% and 82.8\% with 50\% and 100\% market penetration of CACC vehicles compared to the baseline.

## Limitations

This study investigates the safety impact of automated vehicles in mixed traffic, through development of a simulation framework and integration of real-world connected vehicle data. Though efforts have been made to integrate realistic measures and accurate calibration procedures, the study still has some limitations. As discussed, this study considers identical ACC and CACC models for all AVs, while real-life scenarios will contain multiple algorithms developed and implemented by different manufacturers, and this variability is not considered in this paper. In addition, the presented results are based on simulations which have well-known limitations, given their hypothetical nature. The results are limited to the selected intersection and might not be generalizable widely to other intersections with varying geometries and different traffic conditions.

## Conclusions

The study aims to predict the future impact of connected and automated vehicles in mixed traffic with conventional vehicles at an intersection, by integrating real-world connected vehicle data into simulation. In order to simulate the longitudinal control of AVs, ACC model is utilized, and cooperation and connectivity between AVs is considered using CACC model to represent CAV vehicles. A modified Wiedemann car-following model was used to model the driving behavior of conventional vehicles. Connected Vehicle (CV) data was obtained to calibrate the simulation from a real-world testbed in Ann Arbor, Michigan. First, to reflect the speedacceleration relationship of real-world CV data, the Wiedemann car-following model was modified. Then, the simulation was calibrated using driving volatility, as a proxy for the safety performance of the intersection, and speed profile of vehicles passing the intersection. The safety outcome of the simulation is quantified using two performance measures: 1- number of longitudinal conflicts, 2- driving volatility. Numerous studies have used the number of conflicts to describe the safety outcome. On the other hand, recent studies have revealed that driving volatility at intersections is highly correlated with the number of crashes, which can be used as a surrogate safety performance measure. In terms of mobility performance, average travel time and speed are utilized to study AV impacts under different market penetration scenarios.

The interaction of conventional vehicles with ACC and CACC vehicles was studied by investigating several scenarios considering different market penetration of AVs. The simulation results revealed that at early stages of ACC vehicle adoption, the safety improvement might not be substantial, while improvements are significant with +40 percent ACC vehicle market penetration. The results indicate a nonlinear safety improvement, where at low market penetration, there is not a substantial safety improvement, while with
higher penetration rates of ACC vehicles the number of conflicts and driving volatility drop substantially. On the other hand, by adding cooperation between AVs, a significant safety improvement, in terms of reduction in number of conflicts and driving volatility, is observed. This improvement might be due to faster response of AVs and smoother driving behavior that could improve safety by decreasing abrupt vehicular movements. Based on the results, ACC/CACC vehicles can improve mobility statistics in terms of average speed and travel time at intersections.

On the other hand, AVs can respond to the leader vehicles faster due to vehicle automation, and the uniform driving behavior could decrease the number of longitudinal conflicts and driving volatility. In this study, it is assumed that the behavior of humandriven vehicles remains the same. However, it is possible that human drivers might alter their behavior with the passage of time and their exposure to the AVs. One possible scenario is with the familiarization of human drivers with Automated Driving Systems (ADS), conflicts will further reduce. However, it is also possible that human-drivers game the cautiousness and limitations of AVs and behave more aggressively in their vicinity. Therefore, a longitudinal study can incorporate the learning process and behavior adjustments of human drivers into the analysis. Furthermore, although different manufacturers will use different ACC and CACC systems in practice, it is assumed that all the AVs are following the same algorithm for longitudinal vehicle control and their performance is identical, similar to the state of the art (Jeong et al., 2017; Papadoulis et al., 2019; Rahman et al., 2019; Talebpour \& Mahmassani, 2016). Therefore, this variation in ADSs might increase the conflicts/volatility.

## Acknowledgement

Authors also benefited from discussions with Mr. Mani Amoozadeh and his input is greatly appreciated. The authors thank Ms. Kinzee Clark and Mr. Zachary Jerome for editing the manuscript.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Funding

This paper is based upon work supported by the Collaborative Sciences Center for Road Safety, a U.S. DOT funded National Transportation Center, under the Project R-27, the Tennessee Department of Transportation, and in part by the Laboratory Directed Research, Development Program of the Oak Ridge National Laboratory, Oak Ridge, TN 37831 USA, managed by UT-Battelle, LLC, for the DOE.

## ORCID

Ramin Arvin (ID http://orcid.org/0000-0001-7805-3362
Asad J. Khattak (D http://orcid.org/0000-0002-0790-7794
Mohsen Kamrani (D http://orcid.org/0000-0003-2073-8582
Jackeline Rio-Torres (D) http://orcid.org/0000-0001-
6750-9408

## References

Abdulsattar, H., Mostafizi, A., Siam, M. R., \& Wang, H. (2020). Measuring the impacts of connected vehicles on travel time reliability in a work zone environment: An agent-based approach. Journal of Intelligent Transportation Systems, 24 (5), 421-436. https://doi.org/ 10.1080/15472450.2019.1573351
Ahmed, K. I. (1999). Modeling drivers' acceleration and lane changing behavior [PhD thesis]. Massachusetts Institute of Technology.
Ala, M. V., Yang, H., \& Rakha, H. (2016). Modeling evaluation of eco-cooperative adaptive cruise control in vicinity of signalized intersections. Transportation Research Record: Journal of the Transportation Research Board, 2559(1), 108-119. https://doi.org/10.3141/2559-13
Almannaa, M. H., Chen, H., Rakha, H. A., Loulizi, A., \& El-Shawarby, I. (2019). Field implementation and testing of an automated eco-cooperative adaptive cruise control system in the vicinity of signalized intersections. Transportation Research Part D: transport and Environment, 67, 244-262. https://doi.org/10.1016/j.trd. 2018.11.019
Amoozadeh, M., Deng, H., Chuah, C.-N., Zhang, H. M., \& Ghosal, D. (2015). Platoon management with cooperative adaptive cruise control enabled by vanet. Vehicular Communications , 2 (2), 110-123. https://doi.org/10.1016/ j.vehcom.2015.03.004
Amundsen, F., Hydén, C. (1977). Proceedings of first workshop on traffic conflicts. Oslo: TTI.
Anon (2008). National highway traffic safety administration. National motor vehicle crash causation survey: Report to congress. National Highway Traffic Safety Administration Technical (Report DOT HS 811, 059).
Anon (2018)., Federal highway administration. Highway Statistics. (2016).
Arvin, R., Kamrani, M., \& Khattak, A. (2019a). The role of pre-crash driving instability in contributing to crash intensity using naturalistic driving data. Accident Analysis and Prevention , 132, 105226. https://doi.org/10. 1016/j.aap.2019.07.002
Arvin, R., Kamrani, M., \& Khattak, A. J. (2019b). How instantaneous driving behavior contributes to crashes at intersections: Extracting useful information from connected vehicle message data. Accident; Analysis and

Prevention, 127, 118-133. https://doi.org/10.1016/j.aap. 2019.01.014
Arvin, R., Kamrani, M., Khattak, A. J., \& Rios-Torres, J. (2018). Safety impacts of automated vehicles in mixed traffic [Paper presentation]. Transportation Research Board 97th Annual Meeting Washington, DC.
Asadi, B., \& Vahidi, A. (2011). Predictive cruise control: Utilizing upcoming traffic signal information for improving fuel economy and reducing trip time. IEEE Transactions on Control Systems Technology, 19 (3), 707-714. https://doi.org/10.1109/TCST.2010.2047860
Behrisch, M., Bieker, L., Erdmann, J., \& Krajzewicz, D. 2011. Sumo-simulation of urban mobility: An overview [Paper presentation]. Proceedings of the Proceedings of SIMUL 2011, the Third International Conference on Advances in System Simulation.
Boggs, A. M., Arvin, R., \& Khattak, A. J. (2020). Exploring the who, what, when, where, and why of automated vehicle disengagements. Accident; Analysis and Prevention, 136, 105406. https://doi.org/10.1016/j.aap. 2019.105406
Choi, J.-E., \& Bae, S.-H. (2013). Development of a methodology to demonstrate the environmental impact of connected vehicles under lane-changing conditions. SIMULATION, 89(8), 964-976. https://doi.org/10.1177/0037549713489603
De Almeida Correia, G. H., \& Van Arem, B. (2016). Solving the user optimum privately owned automated vehicles assignment problem (uo-poavap): A model to explore the impacts of self-driving vehicles on urban mobility. Transportation Research Part B: Methodological, 87, 64-88. https://doi.org/10.1016/j.trb.2016.03.002
Deluka Tibljaš, A., Giuffrè, T., Surdonja, S., \& Trubia, S. (2018). Introduction of autonomous vehicles: Roundabouts design and safety performance evaluation. Sustainability , 10(4), 1060. https://doi.org/10.3390/su10041060
Dijkstra, A., Marchesini, P., Bijleveld, F., Kars, V., Drolenga, H., \& Van Maarseveen, M. (2010). Do calculated conflicts in microsimulation model predict number of crashes? Transportation Research Record. Transportation Research Record: Journal of the Transportation Research Board, 2147(1), 105-112. https://doi.org/10.3141/2147-13
DMV (2017). Report of traffic accident involving an autonomous vehicle (ol 316). California DMV.
Ebnali, M., Hulme, K., Ebnali-Heidari, A., \& Mazloumi, A. (2019). How does training effect users' attitudes and skills needed for highly automated driving? Transportation Research Part F: traffic Psychology and Behaviour, 66, 184-195. https://doi.org/10.1016/j.trf.2019.09.001
Erdmann, J. (2015). Sumo's lane-changing model. Modeling mobility with open data (pp. 105-123). Springer.
Esfahani, H. N., \& Song, Z. (2019). A new method for microsimulation model calibration: A case study of i-710 [Paper presentation]. Civil and Environmental Engineering Faculty Publications.
Fagnant, D. J., \& Kockelman, K. M. (2014). The travel and environmental implications of shared autonomous vehicles, using agent-based model scenarios. Transportation Research Part C: Emerging Technologies, 40, 1-13. https://doi.org/10.1016/j.trc.2013.12.001
Gong, S., Zhou, A., \& Peeta, S. (2019). Cooperative adaptive cruise control for a platoon of connected and autonomous vehicles considering dynamic information flow topology. Transportation Research Record: Journal of the Transportation Research Board, 2673(10), 185-198. https://doi.org/10.1177/0361198119847473
Hoseinzadeh, N., Arvin, R., Khattak, A. J., \& Han, L. D. (2020). Integrating safety and mobility for pathfinding using big data generated by connected vehicles. Journal of Intelligent Transportation Systems, 24(4), 404-417. https://doi.org/10.1080/15472450.2019.1699077
HSM. (2010). Highway Safety Manual, AASHTO - American Association of State Highway and Transportation Officials. Retrieved October 22, 2020, from http://www.highwaysafetymanual.org/Pages/default. aspx
Jeong, E., Oh, C., \& Lee, S. (2017). Is vehicle automation enough to prevent crashes? Role of traffic operations in automated driving environments for traffic safety. Accident; Analysis and Prevention, 104, 115-124. https://doi.org/10.1016/j.aap.2017.05.002
Kamrani, M., Abadi, S. M. H. E., \& Golroudbary, S. R. (2014). Traffic simulation of two adjacent unsignalized tjunctions during rush hours using arena software. Simulation Modelling Practice and Theory, 49, 167-179. https://doi.org/10.1016/j.simpat.2014.09.006
Kamrani, M., Arvin, R., \& Khattak, A. J. (2018b). Extracting useful information from basic safety message data: An empirical study of driving volatility measures and crash frequency at intersections. Transportation Research Record: Journal of the Transportation Research Board, 2672 (38), 290-301. https://doi.org/10.1177/0361198118773869
Kamrani, M., Arvin, R., \& Khattak, A. J. (2019). The role of aggressive driving and speeding in road safety: Insights from shrp2 naturalistic driving study data [Paper presentation]. Transportation Research Board 98th Annual Meeting, Washington DC.
Kamrani, M., Arvin, R., Khattak, A. J. (2018a). Analyzing highly volatile driving trips taken by alternative fuel vehicles. Transportation Research Board 97th Annual Meeting, Washington, DC, USA.
Kesting, A., Treiber, M., Schönhof, M., \& Helbing, D. (2008). Adaptive cruise control design for active congestion avoidance. Transportation Research Part C: Emerging Technologies, 16 (6), 668-683. https://doi.org/10.1016/j. trc.2007.12.004
Li, Y., Wang, H., Wang, W., Xing, L., Liu, S., \& Wei, X. (2017). Evaluation of the impacts of cooperative adaptive cruise control on reducing rear-end collision risks on freeways. Accident; Analysis and Prevention, 98, 87-95. https://doi.org/10.1016/j.aap.2016.09.015
Li, Z., Chitturi, M., Zheng, D., Bill, A., \& Noyce, D. (2013). Modeling reservation-based autonomous intersection control in vissim. Transportation Research Record: Journal of the Transportation Research Board, 2381(1), 81-90. https://doi.org/10.3141/2381-10
Liu, H., Kan, D. K., Shladover, S., Lu, X.-Y., Wang, M., Schakel, W., \& Van Aren, B. (2018a). Using cooperative adaptive cruise control (CACC) to form high-performance vehicle streams California PATH Progam., Institute of Transportation Studies, University of California, Berkley.

Liu, H., Kan, X., Shladover, S. E., Lu, X.-Y., \& Ferlis, R. E. (2018b). Impact of cooperative adaptive cruise control on multilane freeway merge capacity. Journal of Intelligent Transportation Systems, 22 (3), 263-275. https://doi.org/10.1080/15472450.2018.1438275
Liu, H., Lu, X.-Y., \& Shladover, S. E. (2019). Traffic signal control by leveraging cooperative adaptive cruise control (cacc) vehicle platooning capabilities. Transportation Research Part C: emerging Technologies, 104, 390-407. https://doi.org/10.1016/j.trc.2019.05.027
Liu, H., Shladover, S. E., Lu, X.-Y., \& Kan, X. (2020). Freeway vehicle fuel efficiency improvement via cooperative adaptive cruise control. Journal of Intelligent Transportation Systems, 1-13.
Loeb, B., Kockelman, K. M., \& Liu, J. (2018). Shared autonomous electric vehicle (SAEV) operations across the austin, texas network with charging infrastructure decisions. Transportation Research Part C: Emerging Technologies, 89, 222-233. https://doi.org/10.1016/j.trc. 2018.01.019
Mahdavian, A., Shojaei, A., \& Oloufa, A. 2019. Assessing the long-and mid-term effects of connected and automated vehicles on highways' traffic flow and capacity [Paper presentation]. Proceedings of the International Conference on Sustainable Infrastructure 2019: Leading Resilient Communities through the 21st Century, pp. 263-273. https://doi.org/10.1061/9780784482650.027
Mahdinia, I., Arvin, R., Khattak, A. J., \& Ghiasi, A. (2020). Safety, energy, and emissions impacts of adaptive cruise control and cooperative adaptive cruise control. Transportation Research Record: Journal of the Transportation Research Board, 2674(6), 253-267. https://doi.org/10.1177/0361198120918572
Milakis, D., Van Arem, B., \& Van Wee, B. (2017). Policy and society related implications of automated driving: A review of literature and directions for future research. Journal of Intelligent Transportation Systems, 21(4), 324-325. https://doi.org/10.1080/15472450.2017.1291351
Milanés, V., \& Shladover, S. E. (2014). Modeling cooperative and autonomous adaptive cruise control dynamic responses using experimental data. Transportation Research Part C: Emerging Technologies, 48, 285-300. https://doi.org/10.1016/j.trc.2014.09.001
Milanés, V., \& Shladover, S. E. (2016). Handling cut-in vehicles in strings of cooperative adaptive cruise control vehicles. Journal of Intelligent Transportation Systems, 20 (2), 178-191. https://doi.org/10.1080/15472450.2015.1016023
Milanés, V., Shladover, S. E., Spring, J., Nowakowski, C., Kawazoe, H., \& Nakamura, M. (2014). Cooperative adaptive cruise control in real traffic situations. IEEE Transactions on Intelligent Transportation Systems, 15 (1), 296-305. https://doi.org/10.1109/TITS.2013.2278494
Mintsis, E. (2018). Modelling, simulation and assessment of vehicle automations and automated vehicles' driver behaviour in mixed traffic. TransAID Deliverable.
Motamedi, S., Wang, P., Zhang, T., \& Chan, C.-Y. (2020). Acceptance of full driving automation: Personally owned and shared-use concepts. Human Factors, 62 (2), 288-309. https://doi.org/10.1177/0018720819870658
Nodjomian, A. T., \& Kockelman, K. (2019). How does the built environment affect interest in the ownership and use of self-driving vehicles? Journal of Transport Geography, 78, 115-134. https://doi.org/10.1016/j.jtrangeo.2019.05.016
Nowakowski, C., Shladover, S. E., Cody, D., Bu, F., O'connell, J., Spring, J., Dickey, S., \& Nelson, D. (2011). Cooperative adaptive cruise control: Testing drivers' choices of following distances.
Olia, A., Razavi, S., Abdulhai, B., \& Abdelgawad, H. (2018). Traffic capacity implications of automated vehicles mixed with regular vehicles. Journal of Intelligent Transportation Systems, 22 (3), 244-262. https://doi.org/10.1080/ 15472450.2017.1404680
Papadoulis, A., Quddus, M., \& Imprialou, M. (2019). Evaluating the safety impact of connected and autonomous vehicles on motorways. Accident; Analysis and Prevention, 124, 12-22. https://doi.org/10.1016/j.aap.2018. 12.019
Parsa, A. B., Shabanpour, R., Mohammadian, A., Auld, J., \& Stephens, T. (2020). A data-driven approach to characterize the impact of connected and autonomous vehicles on traffic flow. Transportation Letters-The International Journal of Transportation Research. https://doi.org/10. 1080/19427867.2020.1776956
Rahman, M. S., \& Abdel-Aty, M. (2018). Longitudinal safety evaluation of connected vehicles' platooning on expressways. Accident; Analysis and Prevention, 117, 381-391. https://doi.org/10.1016/j.aap.2017.12.012
Rahman, M. S., Abdel-Aty, M., Lee, J., \& Rahman, M. H. (2019). Safety benefits of arterials' crash risk under connected and automated vehicles. Transportation Research Part C: Emerging Technologies, 100, 354-371. https://doi. org/10.1016/j.trc.2019.01.029
Rios-Torres, J., \& Malikopoulos, A. A. (2017a). Automated and cooperative vehicle merging at highway on-ramps. IEEE Transactions on Intelligent Transportation Systems, 18(4), 780-789. https://doi.org/10.1109/TITS.2016.2587582
Rios-Torres, J., \& Malikopoulos, A. A. (2017b). A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps. IEEE Transactions on Intelligent Transportation Systems, 18(5), 1066-1077. https://doi.org/10.1109/TITS.2016.2600504
Saccomanno, F., Cunto, F., Guido, G., \& Vitale, A. (2008). Comparing safety at signalized intersections and roundabouts using simulated rear-end conflicts. Transportation Research Record: Journal of the Transportation Research Board, 2078(1), 90-95. https://doi.org/10.3141/2078-12
Seiler, P., Pant, A., \& Hedrick, K. (2004). Disturbance propagation in vehicle strings. IEEE Transactions on Automatic Control, 49(10), 1835-1842. https://doi.org/10. 1109/TAC.2004.835586
Sheng, S., Pakdamanian, E., Han, K., Kim, B., Tiwari, P., Kim, I., \& Feng, L. 2019. A case study of trust on autonomous driving [Paper presentation]. Proceedings of the 2019 IEEE Intelligent Transportation Systems Conference (ITSC), pp. 4368-4373.
Shladover, S. E., Nowakowski, C., Lu, X.-Y., \& Ferlis, R. (2015). Cooperative adaptive cruise control: Definitions and operating concepts. Transportation Research Record: Journal of the Transportation Research Board, 2489(1), 145-152. https://doi.org/10.3141/2489-17
Shladover, S., Su, D., \& Lu, X.-Y. (2012). Impacts of cooperative adaptive cruise control on freeway traffic flow. Transportation Research Record: Journal of the

Transportation Research Board, 2324(1), 63-70. https://doi.org/10.3141/2324-08
Singh, S. (2015). Critical reasons for crashes investigated in the national motor vehicle crash causation survey. Traffic Safety Facts Crash Stats National Highway Traffic Safety Administration.
Stanek, D., Milam, R. T., Huang, E., \& Wang, Y. A. (2018). Measuring autonomous vehicle impacts on congested networks using simulation. Transportation Research Board 97th Annual Meeting, Washington DC.
Sun, W., Zheng, J., \& Liu, H. X. (2017). A capacity maximization scheme for intersection management with automated vehicles. Transportation Research Procedia, 23, 121-136. https://doi.org/10.1016/j.trpro.2017.05.008
Talebpour, A., \& Mahmassani, H. S. (2016). Influence of connected and autonomous vehicles on traffic flow stability and throughput. Transportation Research Part C: Emerging Technologies, 71, 143-163. https://doi.org/10. 1016/j.trc.2016.07.007
Van Arem, B., Van Driel, C. J., \& Visser, R. (2006). The impact of cooperative adaptive cruise control on trafficflow characteristics. IEEE Transactions on Intelligent Transportation Systems, 7 (4), 429-436. https://doi.org/10. 1109/TITS.2006.884615
Virdi, N., Grzybowska, H., Waller, S. T., \& Dixit, V. (2019). A safety assessment of mixed fleets with connected and autonomous vehicles using the surrogate safety assessment module. Accident; Analysis and Prevention, 131, 95-111. https://doi.org/10.1016/j.aap.2019.06.001
Wali, B., \& Khattak, A. J. (2020). Harnessing ambient sensing \& naturalistic driving systems to understand links between driving volatility and crash propensity in school zones-a generalized hierarchical mixed logit framework. Transportation Research Part C: Emerging Technologies, 114, 405-424. https://doi.org/10.1016/j.trc.2020.01.028
Wali, B., Khattak, A. J., \& Karnowski, T. (2019). Exploring microscopic driving volatility in naturalistic driving environment prior to involvement in safety critical events-Concept of event-based driving volatility . Accident; Analysis and Prevention, 132, 105277. https://doi.org/10.1016/j.aap.2019.105277
Wali, B., Khattak, A. J., Bozdogan, H., \& Kamrani, M. (2018). How is driving volatility related to intersection safety? A Bbayesian heterogeneity-based analysis of instrumented vehicles data. Transportation Research Part C: Emerging Technologies, 92, 504-524. https://doi.org/10. 1016/j.trc.2018.05.017
Werner, C. (2010). Integration von fahrzeugfolge-und fahrstreifenwechselmodellen in nachtfahrtsimulation luciddrive. [Master's thesis]. Universität der Informationsgesellschaft.
Wiedemann, R. (1974). Simulation des strassenverkehrsflusses. Schriftenreihe des Instituts für Verkehrswesen der Universität Karlsruhe., Band 8, Germany.
Wu, Y., Abdel-Aty, M., Wang, L., \& Rahman, M. S. (2020). Combined connected vehicles and variable speed limit strategies to reduce rear-end crash risk under fog conditions. Journal of Intelligent Transportation Systems, 24(5), 494-513. https://doi.org/10.1080/15472450.2019.1634560
Xiao, L., Wang, M., \& Van Arem, B. (2017). Realistic car-following models for microscopic simulation of adaptive and cooperative adaptive cruise control vehicles. Transportation Research Record: Journal of the Transportation Research Board, 2623(1), 1-9. https://doi.org/10.3141/2623-01

