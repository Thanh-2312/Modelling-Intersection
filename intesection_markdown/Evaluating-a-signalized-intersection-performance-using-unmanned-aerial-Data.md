# Evaluating a signalized intersection performance using unmanned aerial Data 

Mujahid I. Ashqer ${ }^{\text {a** }}$, Huthaifa I. Ashqar ${ }^{\text {b,c }}$, Mohammed Elhenawy ${ }^{\text {d }}$, Mohammed Almannaa (D) ${ }^{\text {e }}$, Mohammad A. Aljamal ${ }^{\text {f }}$, Hesham A. Rakha ${ }^{\mathrm{g}}$ and Marwan Bikdash ${ }^{\mathrm{a}}$<br>${ }^{\mathrm{a}}$ Department of Computational Data Science and Engineering at North Carolina AT State University, Greensboro, North Carloina, USA; ${ }^{\mathrm{b}}$ Precision Systems, Inc, Washington DC, USA; ${ }^{\mathrm{c}}$ Department of Civil Engineering, Arab American University, Jenin, Palestine; ${ }^{\mathrm{d}}$ Research Fellow at CARRS-Q, Queensland University of Technology, Brisbane, Australia; ${ }^{\mathrm{e}}$ Civil Engineering Department, King Saud University, Riyadh, Saudi Arabia; ${ }^{\mathrm{f}}$ Managing Consultant at Guidehouse, Washington DC, USA; ${ }^{9}$ Civil and Environmental Engineering and the Bradley Department of Electrical and Computer Engineering (courtesy), Director of the Center of Sustainable Mobility, VTTI, Virginia, USA


#### Abstract

This paper presents a novel method to compute various measures of effectiveness (MOEs) at a signalized intersection using vehicle trajectory data collected by flying drones. Specifically, this study investigates the use of drone raw data at a busy three-way signalized intersection in Athens, Greece, and builds on the open data initiative of the pNEUMA experiment. Using a microscopic approach and shockwave analysis on data extracted from real-time videos, we estimated the maximum queue length, whether, when, and where a spillback occurred, vehicle stops, vehicle travel time and delay, crash rates, and fuel consumption. The results of the various MOEs were found to be promising. We also demonstrated that estimating MOEs in real-time is achievable using drone data. Such models can track individual vehicle movements within street networks and thus allow the modeler to consider any traffic conditions, ranging from highly under-saturated to highly over-saturated conditions.


## ARTICLE HISTORY

Received 3 October 2022
Accepted 14 April 2023

## KEYWORDS

-Measures of effectiveness
(MOEs); Signalized
intersection; Unmanned
Aerial Vehicles (UAVs);
Drones; Traffic data

## Introduction

Signalized intersections are major elements in causing abrupt changes in traffic patterns that lead to high traffic delays, fuel consumption, and emissions. Roadways often experience operational restrictions when they have signalized intersections. As a result, the control systems put in place to manage the right of way should consider both the specific location's requirements and the network's overall standards. For each approach at the intersection to be effective, several requirements must hold true, and the duration of the traffic signal should be optimized based on interconnected variables. Vehicle acceleration and speed change dramatically during the operation of signalized intersections. It depends on each driver's behavior how they decelerate, stop, and move through the intersection's queue before accelerating to clear an intersection. When it is noticed that there is no right of way at the signal, some drivers may accelerate more strongly, while others may decide to begin decelerating very early. Aggressive drivers, for example, may accelerate during the amber phase to get through the intersection more quickly, while drivers who are more cautious may decide to slow down or even break suddenly to avoid passing the stop sign once the red phase begins. However, traffic signals are crucial in increasing traffic safety along the intersection by avoiding conflicts of various movements. Traffic engineers carefully design traffic signal controllers to efficiently operate traffic movements with the aim of minimizing traffic queues, delays, fuel consumption, and emissions. Traffic demand data is used by traffic signal controllers to determine how traffic should move through the intersection. This information can be fed from different detection techniques, such as the traditional inductive loop detectors and camera systems. Recently, researchers have developed traffic signal controllers using advanced detection techniques such as probe vehicles (vehicles with GPS/Bluetooth devices and connected vehicles) (Aljamal, Abdelghaffar, and Rakha 2020). These advanced techniques allow traffic signal controllers to use real-time information that assists in improving traffic stream efficiency.

Using vehicles' trajectory extracted from Unmanned Aerial Vehicles (UAVs) (i.e. drones) at a busy signalized intersection in Athens, Greece, this study investigates the use of UAVs data to determine measures of effectiveness (MOEs) for signalized intersections including the maximum queue length, whether, when, and where a spillback occurred, vehicle stops, vehicle travel time, delay, crash rates, and fuel consumption. The UAVs technology has shown a promising future in a wide range of applications such as transportation, security, monitoring, survey, environmental mapping, and so on. Furthermore, UAVs technology is easy to deploy, introduces minimum interruptions to the studied area's traffic stream, and is relatively low-cost to maintain.

Traffic delays and queues are principal measures for determining the capacity and the traffic quality of service of signalized intersections. Calculating the number of vehicles and the queue length helps estimate the performance measures of an intersection. Many studies have used several methods to estimate the elements of MOEs, including using the Kalman Filtering technique to estimate the number of vehicles traveling along signalized approaches using real-time probe vehicle data (Aljamal, Abdelghaffar, and Rakha 2020, 2019) and applying Lighthill - Whitham-Richards (LWR) shockwave theory (Liu et al. 2009). Liu et al. used LWR shockwave theory to identify traffic state changes that distinguish queue discharge flow from upstream arrival traffic. Moreover, Ban et al. proposed methods to estimate real-time queue lengths at signalized intersections using sample travel times from mobile traffic sensors.

![](https://cdn.mathpix.com/cropped/169b2e28-c67c-440b-8c36-80f7905a9107-2.jpg?height=560&width=825&top_left_y=181&top_left_x=179)
Figure 1. Study area (Map data © 2021 Google).

The estimation was based on the observation that critical pattern changes of intersection travel times or delays. The model and algorithm were tested using field experiments and simulation data (Ban, Hao, and Sun 2011).

Traffic delays and queues are key parameters in determining the quality of service of signalized intersections. In this study, we used a microscopic approach and shockwave analysis on data extracted from a real-time video, which were collected using a drone, to characterize the various MOEs on a signalized approach for a three-way signalized intersection in Athens, Greece. Specifically, for the specified area in green shown in Figure 1, we used Unmanned Aerial Data to estimate the measures of effectiveness, including the maximum queue length, whether, when, and where a spillback occurred, vehicle stops, vehicle travel time, and delay, crash rates, and fuel consumption.

## Related work

Numerous studies were conducted on UAV video data to analyze and improve transportation networks. Recent research efforts utilized UAV datasets to detect queue and estimate its length on freeways and intersections (Cao et al. 2015; Heshami and Kattan 2021), identify and track heavy vehicles (Khan et al. 2018), investigate crash risk (Gu et al. 2018), detect hazard obstacles and accidents (Congress et al. 2020; Yahia et al. 2018), and better monitor traffic violations (Khan et al. 2020). In the area of estimating queue lengths using UAV data, there are limited efforts conducted at signalized intersections. Freeman et al. employed UAV to capture the traffic formulation at two signalized intersections in Kuwait (Freeman et al. 2019). They first utilized two drones to capture the entire area around the intersection while it was fully congested. Two periods with different traffic volumes were used. The authors were able to estimate the stationary stacking headway for individual vehicles, and types of vehicles were estimated. However, this study only used static UAV video and measured the stacking gab graphically at a stationary status.

Khan et al. has used UAV video data to develop an analytical methodology at four-way intersections in Sint-Truiden, Belgium (Khan et al. 2018). The authors extracted the individual trajectories of vehicles and drew the flow fundamental diagrams, dividing them into three states. Afterward, they conducted a shockwave analysis macroscopically and calculated the queue length for each direction based on the flow fundamental diagrams and shockwave analysis. Yet, the authors did not investigate and consider the microscopic level to calculate the queue length and other MOEs. Ke et al. adopted Machine Learning (ML) techniques such as K-means and Kanadelucas-Tomasi algorithms to estimate both macroscopic and microscopic traffic parameters (Ke et al. 2016). Although they have achieved a high accuracy, the computational time remains an obstacle for ML algorithms, especially when it comes to estimating the real-time queue length. In a different research effort, Ke et al. proposed a framework to estimate seven traffic flow fundamental parameters for both macroscopic and microscopic levels, yet queue length and other MOEs were not investigated (Ke et al. 2020).

Unlike the previous related works, this study proposes a microscopic methodology to estimate the MOEs of an approach in a signalized intersection using UAV data. Specifically, our approach can be used dynamically for real-time estimation of MOEs using UAV data, which could be used for traffic management applications. Our approach uses a microscopic method based on shockwave analysis, which considers the mobility and interaction of individual vehicles and is deemed to be more accurate than macroscopic methods. While our approach is believed to achieve high accuracy in estimating MOEs, it effectively accomplishes that with a relatively less computational complexity and time.

## Dataset

This study used a 14 -min video, which was recorded by a UAV at a three-way signalized intersection in Athens, Greece, as shown in Figures 1 and 2. The video was filmed in sunny weather by a drone hanging over a sufficiently high point at the center of the intersection to cover three approaches as follows: 1) Leof. Alexandras Road, with direction toward the west to 28is Oktovriou Road (Red polygon with 300 m length), 2) 28is Oktovriou Road, with direction toward north to Leof. Alexandras Road (Yellow polygon with 100 m length), and 3) 28is Oktovriou Road, with direction toward south to 28is Oktovriou Road (Green polygon with 100 m length). The geometric design of the intersection consists of five lanes (including a left-turn pocket) for the green polygon, three lanes for the red one, and two lanes for the orange one. The red polygon contains two additional traffic signals, and the speed limit for the three polygons is 55 km/h (34 mph).

The video was then converted to second-by-second trajectories for all types of vehicles, including cars, taxis, powered twoWheeler's, buses, and medium and heavy vehicles as shown in Figure 3. Each trajectory has a unique tracking ID with vehicle type in addition to initial traveled distance and average speed (once they enter the polygon). Each point in the trajectory has a timestamp (in seconds), instantaneous latitude and longitude,

![](https://cdn.mathpix.com/cropped/169b2e28-c67c-440b-8c36-80f7905a9107-2.jpg?height=659&width=814&top_left_y=1899&top_left_x=1117)
Figure 2. Intersection layout.

![](https://cdn.mathpix.com/cropped/169b2e28-c67c-440b-8c36-80f7905a9107-3.jpg?height=463&width=827&top_left_y=183&top_left_x=179)
Figure 3. Illustration of extracted trajectories.

instantaneous vehicle speed, instantaneous latitude, and longitude acceleration/deceleration. These features were utilized to identify the starting of each point of the trajectory and determine the lane allocations for each vehicle. More information on the methodology will be provided in the following two sections.

The first step in using the UAV data entailed utilizing Google Earth to divide each polygon into smaller subpolygons representing the lanes in the green area shown in Figures 1 and 2. We used a Keyhole Markup Language (KML) file, which is an international standard maintained by the Open Geospatial Consortium, Inc. (OGC), to display the geographic data from Google Earth. KML files were created by pinpointing the resulted locations of adding an image overlay of the study area. This geographic data was used in identifying the lane (i.e. sub-polygon) that the vehicles were on during their trip within the green-defined area. Keeping in mind that many vehicles may change their lane multiple times during their trip, the instantaneous longitude and latitude of each vehicle. That said, in order to validate the lane allocations at the upstream edge of the defined area and after leaving the downstream, the origin-destination of each trajectory was identified, and the mismatched values were corrected. Subsequently, a lane-specific timespace diagram was created using vehicle trajectories that were associated with the determined sub-polygon (i.e. lane). The third step entailed applying shockwave analysis on the microscopic level to determine the backward formation and backward recovery waves for each lane-specific queue. This was used to mainly identify the queues and the spillbacks past the upstream edge of the polygon, which is considered the zero reference of our study. The results of this process and other information were used in estimating the other MOEs for the defined area on the signalized intersection, as will be described in Section IV. It is worth mentioning here that we assumed that a vehicle traveling at a speed less than or equal to the typical pedestrian speed of 4.5 km/h (1.2 m/s) is stopped.

## Problem formulation and estimation approaches

## Problem formulation

The new era of sharing information and 'big data' has raised expectations to make mobility more predictable and controllable through a better utilization of data and existing resources. The realization of these opportunities requires going beyond the existing traditional ways of collecting traffic data that are based either on fixed-location sensors or GPS devices with low spatial coverage or penetration rates and significant measurement errors, especially in congested urban areas (Barmpounakis and Geroliminis 2020). pNEUMA is a first-of-its-kind experiment aiming to create the most complete urban dataset to study congestion. A swarm of 10 drones hovering over the central business district of Athens, Greece, over multiple days to record traffic streams in a congested area of a $1.3 \mathrm{~km}^{2}$ area with more than 100 km-lanes of road network, around 100 busy intersections (signalized or not), many bus stops and close to half a million trajectories. The aim of the experiment is to record traffic streams in a multi-modal congested environment over an urban setting using UAVs that can allow the deep investigation of critical traffic phenomena. The $p N E U M A$ experiment develops a prototype system that offers immense opportunities for researchers. This open science initiative creates a unique observatory of traffic congestion, a scale and order-of-magnitude higher than what was available till now, that researchers from different disciplines around the globe can use to develop and test their own models (Barmpounakis and Geroliminis 2020).

This study is built on the open data initiative of $p N E U M A$, which is a unique dataset that was acquired during a first-of-its-kind experiment using a swarm of drones over a dense city center of Athens. This dataset consists of more than half a million detailed trajectories of almost every vehicle that was present in the study area. The dataset includes trajectories that were monitored by one single drone covering a wide area over the central district of Athens, Greece. Both major and minor roads, bus stops, and signalized intersections are included in the study area. The dataset includes trajectories from cars, taxis, powered two-wheelers, buses, medium and heavy vehicles (Barmpounakis and Geroliminis 2020). In this study, we used part of $p N E U M A$ dataset to estimate the measures of effectiveness including the maximum queue length, whether, when and where a spillback occurred, vehicle stops, vehicle travel time and delay, crash rates, and fuel consumption.

As mentioned in Section III, the first phase of our proposed approach was dividing each polygon into mini polygons, representing the lanes into each polygon using Google Earth. We visually determined the mini polygons (i.e. lanes) for each direction. The second phase was identifying which lane the vehicles were on. Using the instantaneous longitude and latitude, we were able to track each vehicle from upstream to downstream of the specified area. Then, we created time-space diagrams (vehicle trajectories) and then linked this to the associated lane for each polygon. Figure 4 depicts a spacetime diagram resulted from this process. The third phase was using shockwave analysis to determine when the queue starts spilling back at the onset of the yellow/red signal traffic indication. This information along with instantaneous vehicle counts helped us characterize the signal phase timing for the traffic light at the intersection. For verification purposes, we matched between the vehicle counts per lane with the OD matrix (calculated from the trajectories). This process is summarized in Figure 5.

![](https://cdn.mathpix.com/cropped/169b2e28-c67c-440b-8c36-80f7905a9107-3.jpg?height=467&width=812&top_left_y=2093&top_left_x=1120)
Figure 4. Time-space diagram.

![](https://cdn.mathpix.com/cropped/169b2e28-c67c-440b-8c36-80f7905a9107-4.jpg?height=523&width=825&top_left_y=183&top_left_x=181)
Figure 5. Summary of proposed approach.

## Shockwave Analysis

According to the Lighthill-Whitham-Richards (LWR) traffic flow model, the flow at every point along the road is a function of density (Liu et al. 2009). The mobility of an abrupt shift in concentration is referred to as a shockwave. Traffic shockwave theory is generated from the LWR model and is used to analytically solve the partial differential equation (PDE) in the model (Liu et al. 2009). Multiple shock waves are produced at signalized intersection as a result of the stop-and-go traffic caused by signal changes. It is safe to presume that during the green phase, where the queue is completely discharged, vehicles are forced to halt during the next red interval, which alters the flow and density of both arriving and stopped traffic. Such a halt in traffic creates a shockwave of queued vehicles that moves upstream of the intersection (Cao et al. 2015; Khan et al. 2018).

We built an automatic simplified model that receives the extracted vehicle trajectories as input. This allows the model to be used in real-time applications. To make it easier to see how traffic flow changes at a signalized crossing, the raw trajectory data is represented in Figure 4. We identified the critical points (Liu et al. 2009; Ban, Hao, and Sun 2011) for the purpose of checking every vehicle in the stream at the approach of interest and find the queues and spills back. The critical point is defined as that point in a vehicle trajectory after which the motion of vehicle changes significantly. Based on this methodology, the important spots on the vehicle trajectories that reflect the significant or irreversible changes in the motion of the cars along the route are determined.

After shockwave analysis and to assess the performance of the signalized intersections under investigation, a number of performance indicators can also be retrieved based on microscopic models. Understanding the specifics of the traffic flow at the intersection at vehicle level requires the use of both shockwave analysis and microscopic models. The results of shockwave analysis can be useful for studying signal cycle lengths, as well as figuring out how quickly shockwaves are generated and dissipated. Additionally, a thorough examination of the queue at an intersection or in any other situation where there is a halted flow can be done using microscopic models. In the next sections, each of these factors and performance indicators has been estimated and presented in detail.

## Computation of queue information

We assumed that a vehicle is queued when its speed is less than or equal to the typical pedestrian speed of 1.2 m/s. In this approach, we constructed the time-space diagram for each lane. For each vehicle in the stream, we moved along its trajectory from the furthest upstream record within the defined area to its defined area exit record (see the green area shown in Figures 1 and 2). We then identified the time stamps and locations (relative to the defined area upstream point) of the points at which the vehicles enter (backward forming shockwave) and exit (backward recovery shockwave) a queuing state. The furthest upstream record that the trajectory enters a queuing state was located. The spatial extent of a queue is computed relative to the downstream end of the defined area, which equals to the area length minus the distance relative to the furthest upstream area boundary. Spillbacks were identified in the area when entry into queuing was immediately prior to the upstream edge of the area.

## Estimation of travel time

The model we developed determines the travel time for any given vehicle by providing that vehicle with a timecard upon its entry to any of the identified links. Subsequently, this timecard is retrieved when the vehicle leaves the link. The difference between these entries and exit times provides a direct measure of the link travel time experienced by each vehicle as Equation (1) and Equation (2) show.

$$
\begin{gathered}
N(t)=N(t-\Delta t)+u(t) \\
T T(t)=H(t) \times N(t)
\end{gathered}
$$

where $N(t)$ is the number of vehicles traversing the link at time $t, N$ $(t-\Delta t)$ is the number of vehicles traversing the link in the previous time interval, and $u(t)$ is the system inputs, as described in Equation (1). Equation (2) represents the system output by measuring the average travel time for the CVs. $H(t)$ is a transition vector that converts the vehicle counts to travel times, as shown in Equation (2).

## Estimation of vehicles stops

Each time a vehicle decelerates, the drop in speed is recorded as a partial stop, as demonstrated in Equation (3) (Rakha, Kang, and Dion 2001). The sum of these partial stops is also recorded. This sum, in turn, provides a very accurate explicit estimate of the total number of stops that were encountered along that particular link. This means that this method will often report that a vehicle has experienced more than one complete stop along a link. Multiple stops arise from the fact that a vehicle may have to stop several times before ultimately clearing the link stop line. This finding, while seldom recorded by or even permitted within macroscopic models, is a common observation within actual field data for links on which considerable over-saturation queues exist.

$$
S\left(t_{i}\right)=\frac{u\left(t_{i}\right)-u\left(t_{i-1}\right)}{u_{f}}
$$

where:
$S\left(t_{i}\right)$ : Instantaneous partial stop estimates at time $t_{i}, u\left(t_{i}\right)$ : Speed at instant $t_{i}, u\left(t_{i-1}\right)$ : Speed at instant $t_{i-1}$, and $u_{f}$. Roadway free-flow speed.

## Estimation of vehicle delay

The model estimates vehicle delays every Deci-second as the difference in travel time between travel at the vehicle's instantaneous
speed and travel at free-speed, as indicated in Equation (4) (Rakha, Van Aerde, and Wang 1993). This model has been validated against analytical time-dependent queuing models, shockwave analysis, and the Canadian Capacity Guide, Highway Capacity

Manual, and Australian Capacity Guide procedures (Rakha, Van Aerde, and Wang 1993; Rakha et al. 2000).

$$
d\left(t_{i}\right)=\Delta t\left(1-\frac{u\left(t_{i}\right)}{u_{f}}\right)
$$

where:
$\Delta t$ : The data processing time step (0.1 s in our case).

## Estimation of crash rates

The safety model that was used here is based on US national crash statistics. The model computes the crash risk for 14 different crash types as a function of the facility speed limit and a time-dependent measure of exposure. The use of a timedependent measure of exposure allows the model to capture differences in the crash risk that result from differences in the network efficiency. The model also computes the vehicle damage and level of injury to the passengers involved in the crash based on the vehicle's instantaneous speed. The use of the instantaneous speed means that the crash damage and injury level is responsive to the level of congestion. Consequently, the model can capture the safety impacts of operational-level alternatives including Intelligent Transportation Systems. By multiplying the distance-based crash rate by the facility free-speed, it was possible to estimate a time-based crash rate. The advantage of a timebased crash rate is that the rate level of exposure increases with higher levels of congestion even though vehicles might not necessarily travel longer distances. More information can be found here (Avgoustis, Rakha, and Van Aerde 2004).

$$
\text { CrashRate }_{i}=e^{a_{1}{ }^{i} * u_{f}+a_{2}{ }^{i}} \forall 1: 15
$$

where:
$a_{1}$ : Regression Coefficient $a_{1} . a_{2}$ : Regression Coefficient $a_{2}$. $u_{f}$. Freeflow Speed

## Fuel consumption

To find Fuel consumption, we used the Virginia Tech Comprehensive Power-Based Fuel Consumption Model (VTCPFM). VT-CPFM is a microscopic fuel consumption model based on instantaneous power; the detailed VT-CPFM model is described in the original paper by Rakha et al., which also includes a MATLAB script to run the model (Rakha et al. 2011).

Other models either require calibration of specific parameters from laboratory or field testing or produce a bang-bang control. VT-CPFM avoids both of these problems: because data collection is not always feasible, VT-CPFM uses only publicly available data. Additionally, because the function for fuel consumption is a second-degree polynomial with respect to vehicle-specific power (VSP), the partial derivative with respect to torque is a function of torque and the bang-bang control is not produced (Rakha et al. 2011). The model can also be used for different vehicle classes including light-duty vehicles (Rakha et al. 2011), heavy-duty vehicles (Wang and Rakha 2017), and buses (Edwardes and Rakha 2014).
First, power is calculated using Equation (6), as follows:

$$
P\left(t_{i}\right)=\left(\frac{R\left(t_{i}\right)+1.04 m a\left(t_{i}\right)}{3,600 \eta_{d}}\right) * v\left(t_{i}\right)
$$

where:
$P\left(t_{i}\right)=$ power at time step $t_{i}(\mathrm{~kW}), m=$ vehicle mass $(\mathrm{kg}), a\left(t_{i}\right)=$ vehicle acceleration at time step $t_{i}\left(\mathrm{~m} / \mathrm{s}^{2}\right), v\left(t_{i}\right)=$ vehicle speed at time step $t_{i}(\mathrm{~km} / \mathrm{h}), \eta_{d}=$ driveline efficiency, and $R\left(t_{i}\right)=$ resistance force at time step $t_{i}(\mathrm{~N})$.
The resistance force is calculated with Equation (7), as follows:

$$
\begin{aligned}
R\left(t_{i}\right)= & \frac{\rho}{25.92} C_{D} C_{h} A_{f} v\left(t_{i}\right)^{2}+9.8066 m \frac{C_{r}}{1,000}\left(C_{1} v\left(t_{i}\right)+C_{2}\right) \\
& +9.8066 m G\left(t_{i}\right)
\end{aligned}
$$

where:
$\rho=$ density of air $\left(1.2256 \mathrm{~kg} / \mathrm{m}^{3}\right.$ at sea level and 15°C), $C_{d}=$ vehicle drag coefficient (unitless),
$C_{h}=$ correction factor for elevation [which equals $10.085 H$ where $H$ is elevation (km)], $A_{f}=$ vehicle frontal area ( $\mathrm{m}^{2}$ ),
$G\left(t_{i}\right)=$ roadway grade at time step $t_{i}$, and $c_{r}, c_{1}$, and $c_{2}=$ rolling resistance parameters (unitless) (Rakha et al. 2011).

Then, fuel consumption, $F C(L / s)$, is calculated by using Equation (8). The alpha values are calculated using time, power, and fuel consumed from the EPA city and highway test cycles. A detailed list of the required variables and potential sources for the VT-CPFM can be found in (Rakha et al. 2011).

$$
F C\left(t_{i}\right)= \begin{cases}a_{0}+a_{1} P\left(t_{i}\right)+a_{2} P\left(t_{i}\right)^{2} & \forall P\left(t_{i}\right) \geq 0 \\ a_{0} & \forall P\left(t_{i}\right)<0\end{cases}
$$

where:
$\alpha_{0}, \alpha_{1}$ and $\alpha_{2}$ are vehicle-specific model constants that are calibrated for each vehicle.

## Results and discussion

Using a microscopic approach and based on shockwave analysis that considers the mobility and interaction of individual vehicles, we estimated the MOEs of an approach to a signalized intersection using UAV data. We constructed the time-space diagrams for each lane on the studied approach, as shown in Figures 1 and 2. The green polygon consists of five lanes (four lanes plus a left turn pocket lane). We labeled the pocket lane as follows: the leftmost lane as Lane 1 and increased the counter until the rightmost lane, which is labeled Lane 5. The total number of vehicles in the area is 750 during the monitoring period. We also identified the distribution of vehicle types in each lane as shown in Table 1. In the table, a vehicle may be counted multiple times as we were able to capture the vehicles that make lane-change movement from one lane to another during the monitoring period (see Table 2). However, a vehicle is counted one time in each lane at the end. We also investigated the $95{ }^{\text {th }}$ percentile and found it to be about 42 km/hr as shown in Figure 6.

## Queue Information

Using the information extracted from the time-space diagram of each lane, we were able to identify the length of each queue that was formed in each lane during the monitoring period, as shown in Table 3. The table shows the queue length that occurred on each lane, when, and where it occurred (i.e. the latitude (lat) and longitude (long) of the beginning of the queue and the end). The table demonstrates that the maximum queue length in the green polygon occurred in Lane 2 (the leftmost upstream of the left-turn pocket lane) at a length of 102.7 m (between the coordinates of (37.99225, 23.73141) and (37.99280, 23.73154)), which happened at a time of 350.2 s after the beginning of the monitoring period. Moreover, we used the time-space diagram to identify spillbacks on each lane

Table 1. Total number of vehicles for each Vehicle types per lane.
| Vehicle Type | Lane 1 | Lane 2 | Lane 3 | Lane 4 | Lane 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Light- \& medium-duty | 124 | 210 | 277 | 195 | 69 |
| Motorcycle | 24 | 53 | 124 | 160 | 66 |
| Heavy-duty | 1 | 3 | 4 | 4 | 3 |
| Bus | 0 | 1 | 1 | 9 | 11 |
| Total | 149 | 267 | 406 | 368 | 149 |


Table 2. Lane changes of each Vehicle type.
| Vehicle Type | Number of Vehicles | Number of Lane Changes |
| :--- | :--- | :--- |
| Light- \& medium-duty | 491 | 384 |
| Motorcycles | 237 | 190 |
| Heavy-duty | 8 | 7 |
| Bus | 14 | 8 |
| Total | 750 | 589 |


![](https://cdn.mathpix.com/cropped/169b2e28-c67c-440b-8c36-80f7905a9107-6.jpg?height=650&width=797&top_left_y=848&top_left_x=192)
Figure 6. Vehicle speed distribution.

during the monitoring period. Table 4 summarizes the results for the various spillbacks. It shows that there were two spillbacks as follows: one in Lane 2 (middle-left lane), which is also recorded as the maximum queue length; and the other one in Lane 3 (middle lane)-both occurred at time 350.2 s after the beginning of the monitoring period.

## Travel time

Our model to determine the travel time on each lane is a microscopic one based on Equation (1) and Equation (2). The model determines the link travel time for any given vehicle by providing that vehicle with a timecard upon its entry and exit from any link. The results of estimating the travel time on each lane per vehicle type are shown in Table 5 and per the traffic movement of each vehicle type is shown in Table 6. The tables show that the maximum travel time occurred by a heavy-duty

Table 4. The spillbacks information.
| Lane | Timestamp (s) |
| :--- | :--- |
| Lane 2 | 350.20 |
| Lane 3 | 350.20 |


vehicle on Lane 3 (i.e. part of the through traffic movement) and is equal to about 32 s. They also show that Lane 5 has the highest average travel time for all vehicles traveling through the study area. This could be as it is the closest lane to the parking lane and to the curbside, which pedestrians usually use. The second highest average travel time was for Lane 2, which is part of the left-turn traffic movement.

## Vehicle stops

To calculate vehicle stops, we used a microscopic model that computes instantaneous partial and full stops for undersaturated and oversaturated conditions in signalized intersection by using second-by-second speed measurements as described in Equation (4) (Rakha, Van Aerde, and Wang 1993). This model has shown that there is a significant impact of vehicle stops on fuel consumption and emissions (Rakha and Ding 2003). The model indicates that the vehicle fuel consumption rate is more sensitive to cruise-speed levels than to vehicle stops (Rakha and Ding 2003). Table 7 shows the number of vehicle stops on each lane per the number of vehicle types. It shows that vehicles on Lane 2 experienced the highest number of stops, followed by Lane 3. It also shows that heavy-duty vehicles experienced the highest number of stops, which occurred in Lane 3, followed by light- and medium-duty vehicles experience in Lane 2. Moreover, Table 8 shows that the total number of vehicles turning left experienced stops more than vehicles going through the intersection.

Table 3. The queue information on each lane.
| Lane | Queue length (m) | Timestamp (s) | Start lat | Start long | End Lat | End long |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Lane 1 | 25.0 | 565.04 | 37.99190 | 23.73136 | 37.99211 | 23.73140 |
| Lane 2 | 102.7 | 350.20 | 37.99225 | 23.73141 | 37.99280 | 23.73154 |
| Lane 3 | 102.2 | 346.00 | 37.99229 | 23.73139 | 37.99280 | 23.73150 |
| Lane 4 | 97.6 | 529.56 | 37.99275 | 23.73148 | 37.99275 | 23.73148 |
| Lane 5 | 98.6 | 783.12 | 37.99200 | 23.73121 | 37.99277 | 23.73142 |


Table 5. Travel time on each lane per the number of vehicle types (s).
| Vehicle Type | Lane 1 | Lane 2 | Lane 3 | Lane 4 | Lane 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Light- \& medium-duty | 20.29 | 23.27 | 19.48 | 13.58 | 13.14 |
| Motorcycles | 9.02 | 9.70 | 10.53 | 9.93 | 30.20 |
| Heavy-duty | 2.08 | 4.80 | 31.99 | 22.74 | 9.28 |
| Bus | - | 1.40 | 5.36 | 9.45 | 16.09 |
| Total | 18.35 | 20.29 | 16.84 | 11.99 | 20.84 |


Table 6. Travel time per movement for each vehicle type(s).
| Vehicle Type | Left Turn (Lane 1 \& 2) | Through (Lane 3, 4, \& 5) |
| :--- | :--- | :--- |
| Light- \& medium-duty | 22.17 | 16.55 |
| Motorcycles | 9.49 | 13.97 |
| Heavy-duty | 4.12 | 22.43 |
| Bus | 1.40 | 12.73 |
| Total | 19.60 | 15.55 |


Table 7. Vehicles stops on each lane per the number of vehicle types.
| Vehicle Types | Lane 1 | Lane 2 | Lane 3 | Lane 4 | Lane 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Light- \& medium-duty | 0.12 | 0.40 | 0.28 | 0.23 | 0.19 |
| Motorcycle | 0.11 | 0.21 | 0.24 | 0.21 | 0.24 |
| Heavy-duty vehicle | 0.09 | 0.11 | 0.68 | 0.26 | 0.04 |
| Bus | - | 0.01 | 0.07 | 0.10 | 0.13 |
| Total | 0.12 | 0.36 | 0.27 | 0.20 | 0.20 |


Table 8. Vehicle stops per movement for each vehicle type.
| Vehicle Type | Left Turn (Lane 1 \& 2) | Through (Lane 3, 4, \& 5) |
| :--- | :--- | :--- |
| Light- \& medium-duty | 0.30 | 0.24 |
| Motorcycle | 0.18 | 0.22 |
| Heavy-duty vehicle | 0.10 | 0.35 |
| Bus | 0.01 | 0.11 |
| Total | 0.27 | 0.23 |


## Vehicle delay

Delay at signalized intersections is considered a significant factor in determining the level of service at the intersection approaches as well as a parameter that is used in the optimization of traffic signal timings. In this study, we used a microscopic approach to obtain delay estimates in the study area. Within the model, delay is estimated for each individual vehicle by calculating, for each traveled link, the difference between the vehicle's recorded travel time and the travel time that the vehicle would have experienced on the link at free speed, as shown in Equation (4) (Rakha, Van Aerde, and Wang 1993). Table 9 shows the results of travel delay on each lane of the study area divided by the number of each vehicle type. When all vehicle types are considered, Lane 2 has the highest delay of all lanes, followed by Lane 5 and Lane 1. This depicts that the vehicles turning to left are more likely to experience higher delay than vehicles traveling through the intersection, which is clearly shown in Table 10. Moreover, the highest delay recorded was for heavy-duty vehicles traveling through Lane 3 and is equal to 20.63s. Table 10 also shows that light- \& medium-duty vehicles and motorcycles have higher travel delay when turning to the left. However, heavy-duty vehicles and buses have higher travel delays when traveling through the intersection.

Table 9. Global average delay on each lane per vehicle type(s).
| Vehicle Type | Lane 1 | Lane 2 | Lane 3 | Lane 4 | Lane 5 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Light- \& medium-duty | 11.63 | 15.77 | 10.30 | 7.51 | 8.98 |
| Motorcycle | 8.55 | 7.40 | 5.57 | 4.01 | 16.68 |
| Heavy-duty vehicle | 1.18 | 1.87 | 20.63 | 13.89 | 1.53 |
| Bus | - | 0.71 | 2.75 | 3.88 | 8.12 |
| Total | 11.06 | 13.90 | 8.94 | 5.97 | 12.18 |


Table 10. Travel delay per movement for each vehicle type(s).
| Vehicle Type | Left Turn (Lane 1 \& 2) | Through (Lane 3, 4 \& 5) |
| :--- | :--- | :--- |
| Light- \& medium-duty | 14.23 | 9.12 |
| Motorcycles | 7.76 | 6.95 |
| Heavy-duty | 1.70 | 12.97 |
| Bus | 0.71 | 6.05 |
| Total | 12.88 | 8.28 |


Table 11. Crash rates for 14 crash types (crashes/VMT).
| Crash Type | Crash Rate |
| :--- | :--- |
| Single Driver - Right Roadside Departure | 0.00296 |
| Single Driver - Left Roadside Departure | 0.00243 |
| Single Driver - Forward Impact | 0.00544 |
| Same Traffic Way and Same Direction - Rear-End | 0.00597 |
| Same Traffic Way and Same Direction - Forward Impact | 0.00023 |
| Same Traffic Way and Same Direction - Sideswipe/Angle | 0.00179 |
| Same Traffic Way and Opposite Direction - Head-On | 0.00041 |
| Same Traffic Way and Opposite Direction - Forward Impact | 0.00090 |
| Same Traffic Way and Opposite Direction - Sideswipe/Angle | 0.00244 |
| Change Traffic Way and Vehicle Turning - Turn Across Path | 0.00366 |
| Change Traffic Way and Vehicle Turning - Turn Input Path | 0.00434 |
| Intersecting Paths - Perpendicular Crash | 0.00267 |
| Backing Vehicle | 0.00043 |
| Other or Unknown | 0.00367 |
| Total Crash Rate | 0.03760 |


## Crash rates

We used a safety model that is based on US national crash statistics as described in (Avgoustis, Rakha, and Van Aerde 2004). The model computes the crash risk for 14 different crash types as a function of the facility speed limit and a time-dependent exposure measure as shown in Equation 5. The model can capture the safety impacts of operational-level alternatives including Intelligent Transportation Systems (ITS). Table 11 shows the crash rates for the 14 crash types included in the model. Results show that the rear-end crashes in the same traffic way and same direction has the highest crash rate in the intersection, followed by the forward impact of a single driver. The total crash rate was found to be about 0.038 crashes for every vehicle mile traveled (VMT).

## Fuel consumption

Using traffic data from drones, we investigated the use of Virginia Tech Comprehensive Power-Based Fuel Consumption Model (VT-CPFM). We investigated the applicability of VT-CPFM as a microscopic fuel consumption model based on instantaneous power (Rakha et al. 2011). VT-CPFM function for fuel consumption is a second-degree polynomial with respect to vehicle-specific power (VSP) using Equation (6) (Rakha et al. 2011). We used VT-CPFM in this study for the different vehicle classes including lightduty vehicles (Rakha et al. 2011), heavy-duty vehicles (Wang and Rakha 2017), and buses (Edwardes and Rakha 2014) that passed through the study area. We found that the total fuel consumption resulted from all 750 vehicles passing through the approach is about 207 L during the 14 -min study period; about 0.28 L per vehicle; or 0.25 L/s.

## Conclusion

Traffic delays, fuel consumption, stopping, spillbacks, and queues are key parameters in determining the quality of service at signalized intersections. This study investigates the use of drone raw data at a busy signalized intersection in Athens, Greece, to find the corresponding MOEs. Collecting traffic data using flying drones is an emerged technology that has shown a promising future in a wide range of applications because drones are easy to deploy and introduce minimum interruptions to the traffic stream of the studied area.

This study builds on the open data initiative of the $p N E U M A$ experiment that used a swarm of drones over a dense city center of Athens. Using a microscopic approach and shockwave analysis on the data extracted from real-time video, we determined the various MOEs of the signalized approach on a busy three-way signalized intersection in Athens, Greece. Specifically, we estimated the measures of effectiveness including the maximum queue length, whether, when and where a spillback occurred, vehicle stops, vehicle travel time and delay, crash rates, and vehicle fuel consumption. One challenge in this study was the duration of the data. Given that the proposed method of this study is intended to be used in real-time applications and there are some restrictions on storing big data in each controller's intersection; it was suggested to use a 14-min video data to evaluate the performance of signalized intersections. Results of the various MOEs were found to be promising, which confirms that the use of traffic data collected by drones has many advantages.

In this study, we found that understanding the specifics of the traffic flow on the microscopic level at intersections requires the use of a combination of methods - shockwave analysis and other microscopic models in our case. This combination can be useful for studying performance at intersections as well as figuring out how quickly shockwaves are generated and dissipated. Additionally, a thorough analysis of the queue at an intersection or in any other situation where there is an interrupted flow can be done using the extracted parameters and shockwave speeds.

We also found that the use of microscopic approaches to computing the MOEs at signalized intersections in real-time is achievable and desirable. Such models have the ability to track individual vehicle movements within street networks and thus capture traffic conditions on various MOEs, ranging from highly under-saturated to highly oversaturated conditions. The results of these models have higher accuracy than other aggregate models given that the approach captures vehicle transient behavior. Specifically, at the delay level, microscopic models can determine the delay incurred by an individual vehicle while traveling without the need for macroscopic formulas. This allows them to evaluate uniform and overflow delay, or delays in undersaturated and over-saturated traffic conditions, allowing for the evaluation of complex traffic situations. In addition, the ability to record vehicle speed and position on a second-by-second basis further allows the recording of speed profiles and the direct estimation of deceleration, stopped and acceleration delays, crash risk, and vehicle fuel consumption levels, as demonstrated in this study.

## Acknowledgments

The authors would like to thank the pNEUMA project for providing the dataset that was used in this study.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## ORCID

Huthaifa I. Ashqar (D) http://orcid.org/0000-0002-6835-8338
Mohammed Almannaa (D) http://orcid.org/0000-0002-5893-3052

## References

Aljamal, M. A., H. M. Abdelghaffar, and H. A. Rakha. 2019. "Developing a Neural-Kalman Filtering Approach for Estimating Traffic Stream Density Using Probe Vehicle Data." Sensors 19 (19): 4325. doi:10.3390/s19194325.
Aljamal, M. A., H. M. Abdelghaffar, and H. A. Rakha. 2020. "Real-Time Estimation of Vehicle Counts on Signalized Intersection Approaches Using Probe Vehicle Data." IEEE Transactions on Intelligent Transportation Systems 22 (5): 2719-2729. doi:10.1109/TITS.2020.2973954.
Avgoustis, A., H. Rakha, and M. Van Aerde. 2004. "Framework for Estimating Network-Wide Safety Impacts of Intelligent Transportation Systems," in Intelligent transportation systems safety and security conference, Vol. 2. Miami, FL.
Ban, X. J., P. Hao, and Z. Sun. 2011. "Real Time Queue Length Estimation for Signalized Intersections Using Travel Times from Mobile Sensors." Transportation Research Part C: Emerging Technologies 19 (6): 1133-1156. doi:10.1016/j.trc.2011.01.002.
Barmpounakis, E., and N. Geroliminis. 2020. "On the New Era of Urban Traffic Monitoring with Massive Drone Data: The Pneuma Large-Scale Field Experiment." Transportation Research Part C: Emerging Technologies 111: 50-71. doi:10.1016/j.trc.2019.11.023.
Cao, J., M. Hadiuzzaman, T. Z. Qiu, and D. Hu. 2015. "Real-time Queue Estimation Model Development for Uninterrupted Freeway Flow Based on Shockwave Analysis." Canadian Journal of Civil Engineering 42 (3): 153-163. doi:10.1139/cjce-2014-0218.
Congress, S. S. C., A. J. Puppala, A. Banerjee, and U. D. Patil. 2020. "Identifying Hazardous Obstructions Within an Intersection Using Unmanned Aerial Data Analysis." International Journal of Transportation Science and Technology 10 (1): 34-48, [Online]. Available. doi:10.1016/j.ijtst.2020.05.004.
Edwardes, W., and H. Rakha. 2014. "Virginia Tech Comprehensive Power-Based Fuel Consumption Model: Modeling Diesel and Hybrid Buses." Transportation Research Record 2428 (1): 1-9. doi:10.3141/2428-01.
Freeman, B. S., J. A. Al Matawah, M. Al Najjar, B. Gharabaghi, and J. The. 2019. "Vehicle Stacking estimation' at Signalized Intersections with Unmanned Aerial Systems." International Journal of Transportation Science and Technology 8 (2): 231-249. doi:10.1016/j.ijtst.2018.12.002.
Gu, X., M. Abdel-Aty, Q. Xiang, Q. Cai, and J. Yuan. 2018. "Utilizing UAV Video Data for In-Depth Analysis of drivers' Crash Risk at Interchange Merging Areas." Accident Analysis and Prevention 123 (November): 159-169. [Online]. Available. doi:10.1016/j.aap.2018.11.010.
Heshami, S., and L. Kattan. 2021. "A Queue Length Estimation and Prediction Model for Long Freeway Offramps." Journal of Intelligent Transportation Systems: Technology, Planning, and Operations 25 (1): 122-134. [Online]. Available. doi:10.1080/15472450.2020.1846125.
Ke, R., S. Feng, Z. Cui, and Y. Wang. 2020. "Advanced Framework for Microscopic and Lane-Level Macroscopic Traffic Parameters Estimation from Uav Video." IET Intelligent Transport Systems 14 (7): 724-734. doi:10. 1049/iet-its.2019.0463.
Ke, R., Z. Li, S. Kim, J. Ash, Z. Cui, and Y. Wang. 2016. "Real-Time Bidirectional Traffic Flow Parameter Estimation from Aerial Videos." IEEE Transactions on Intelligent Transportation Systems 18 (4): 890-901.
Khan, M. A., W. Ectors, T. Bellemans, D. Janssens, and G. Wets. 2018. "Unmanned Aerial Vehicle-Based Traffic Analysis: A Case Study for Shockwave Identification and Flow Parameters Estimation at Signalized Intersections." Remote Sensing 10 (3). doi:10.3390/rs10030458.
Khan, N. A., N. Z. Jhanjhi, S. N. Brohi, R. S. A. Usmani, and A. Nayyar. 2020. "Smart Traffic Monitoring System Using Unmanned Aerial Vehicles (UAVs)." Computer Communications 157 (January): 434-443. [Online]. Available. doi:10.1016/j.comcom.2020.04.049https://doi.org/10.1016/j.com com.2020.04.049.
Liu, H. X., X. Wu, W. Ma, and H. Hu. 2009. "Real-Time Queue Length Estimation for Congested Signalized Intersections." Transportation Research Part C: Emerging Technologies 17 (4): 412-427. doi:10.1016/j.trc. 2009.02.003.
Rakha, H. A., K. Ahn, K. Moran, B. Saerens, and E. Van den Bulck. 2011. "Virginia Tech Comprehensive Power-based Fuel Consumption Model: Model Development and Testing." Transportation Research Part D: Transport and Environment 16 (7): 492-503. doi:10.1016/j.trd.2011.05.008.
Rakha, H., and Y. Ding. 2003. "Impact of Stops on Vehicle Fuel Consumption and Emissions." Journal of Transportation Engineering 129 (1): 23-32. doi:10. 1061/(ASCE)0733-947X(2003)129:1(23).
Rakha, H., Y. -S. Kang, and F. Dion. 2001. "Estimating Vehicle Stops at Undersaturated and Oversaturated Fixed-time Signalized Intersections." Transportation Research Record 1776 (1): 128-137. doi:10.3141/1776-17.
Rakha, H., M. Van Aerde, K. Ahn, and A. Trani. 2000. "Requirements for Evaluation of Environmental Impacts of Intelligent Transportation Systems Using Speed and Acceleration Data." Transportation Research Record 1738 (1): 56-67. doi:10.3141/1738-07.
Rakha, H., M. Van Aerde, and J. Wang. 1993. "A Comparison of Two Alternative Traffic Simulation Models: Transyt Vs INTEGRATION." Proceeding of the Canadian Institute of Civil Engineers, Edmonton, Alberta.
Wang, J., and H. A. Rakha. 2017. "Fuel Consumption Model for Heavy Duty Diesel Trucks: Model Development and Testing." Transportation Research Part D: Transport and Environment 55: 127-141. doi:10.1016/j.trd.2017.06. 011.
Yahia, C. N., S. E. Scott, S. D. Boyles, and C. G. Claudel. 2018. "Unmanned Aerial Vehicle Path Planning for Traffic Estimation and Detection of Non-Recurrent Congestion." Transportation Letters 14 (8): 849-862.

