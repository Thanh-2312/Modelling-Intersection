# Evaluation of right-turn lanes at signalized intersection in non-lane-based heterogeneous traffic using microscopic simulation model 

A. Gowri ${ }^{* 1}$ and R. Sivanandan ${ }^{2}$

In developing countries like India, the traffic on urban roads is highly heterogeneous in nature, with vehicles of widely varying static and dynamic characteristics. This type of traffic is characterized by lack of queue and lane discipline (lane-less movement) based on availability of spaces near intersections. Moreover, at intersections, straight-through, left-, and right-turning vehicles seek to occupy the same physical space. In such situations, the through vehicles are susceptible to delays in the absence of turn lanes for the left-turning and right-turning vehicles and vice versa. Models suitable for analysis of such traffic flow hardly exist, and most of the available models are limited in scope. In the current study, a microscopic traffic simulation model for signalized intersection is developed specifically for heterogeneous traffic. This model covers different vehicle types and allows for some special behavior, such as seepage of two-wheelers to fronts of queues. Detailed study of queue formation and dissipation were done microscopically under non-lane-based traffic conditions near intersection area. The model was calibrated and tested with data from Chennai city, India, and its predictions were found to be in close agreement with the field data. In addition, the model makes a significant contribution to the study of right-turn lane (RTL) on delays to vehicles. In general, RTL is found to be advantageous for most cases of approach volumes and right-turn proportions. The optimal lengths of RTL are suggested for various approach volumes and right-turn proportions.

Keywords: Heterogeneous traffic, Signalized intersections, Microscopic simulation, Evaluation, Right-turn lanes

## Introduction

In India, the traffic on roads is heterogeneous in nature with wide variations in physical dimensions and other vehicular and traffic characteristics. In heterogeneous traffic, the vehicular composition include motorized twowheelers (MTW), cars (including jeeps and small vans), buses, auto-rickshaws (three-wheeled motorized vehicles), light commercial vehicles (LCV), trucks, and non-motorized vehicles such as bicycles. Here, vehicles move on the left side of the road. Vehicles do not respect the lane markings and tend to utilize every possible lateral or longitudinal gap. In particular, two-wheelers exhibit abnormal queuing behavior in which they do not wait at the end of queues but creep toward the front of queues, thereby dissipating faster at the intersection. Moreover, at

[^0]intersections, left, through, and right-turning vehicles seek to occupy the same physical space as close to the stop line as possible. These result in high levels of conflicts, delays, and blockage of through vehicles by turning vehicles and vice versa. In such situations, the through vehicles are faced with delays in the absence of turn lanes for the leftturning and right-turning vehicles. Intersection capacity also gets adversely affected in these situations. In order to prevent blockages and delays at signalized intersections, turn lanes can be provided to facilitate faster movement of turning vehicles. Turn lanes can improve safety, increase travel speed, reduce delay, and congestion. Considerable research has been carried out to determine maximum traffic flow, delays, queue length, driver and vehicular traffic characteristics, etc. for signalized intersections under homogeneous traffic flow characteristics (e.g., Kim and Benekohal, 2005; Sharma et al., 2007; Liu et al., 2009; Chang et al., 2013; Wu and Yang, 2013). Several simulation models have been developed for signalized intersections under homogeneous traffic conditions (Fang and Elefteriadou, 2005; Park and Qi, 2005; Chaudhry and Ranjitkar, 2009; Tan et al., 2012; Tohti et al., 2013; Chai

![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-02.jpg?height=1018&width=791&top_left_y=176&top_left_x=215)
1 Simulation model framework

and Wong, 2014). Several studies have been carried out to address the effect of control measures (shared and exclusive turn lanes) on signalized intersection operations; again, these are for homogeneous traffic conditions (e.g., Fitzpatrick et al., 2006; Tian and Wu, 2006; Potts et al., 2007; Yang, 2008; Kikuchi and Kronprasert, 2010; Qi et al., 2012; Chai and Wong, 2013).

A review of the literature shows that only limited studies have been carried out to understand the traffic flow characteristics at and near signalized intersections under heterogeneous traffic conditions. Maini and Khan (2000) studied the discharge characteristics of vehicles, entry time of vehicles, and vehicle characteristics at signalized intersections. Hossain (2001) estimated saturation flow at signalized intersections based on road width, turning proportion, and percentage of heavy and non-motorized vehicles using a micro-simulation modeling approach. Arasan and Kashani (2003) developed a simulation model to study the platoon dispersal pattern of heterogeneous traffic at a signalized intersection. Marwah et al. (2006) developed a simulation model for signalized intersection, considering the heterogeneous traffic on Indian roads using a strip strategy for road space allocation. Gowri et al. (2009) proposed an object-oriented model for simulating heterogeneous traffic with focus on mid-block and intersection flow modeling. Applicability of VISSIM model for heterogeneous traffic conditions was studied by Mathew and Radhakrishnan (2010). Sharma and Swami (2012) studied the effect of addition of turning lane at busy signalized at-grade intersection using VISSIM. Huynh et al. (2013) developed a social force model to study the mixed traffic flow characteristics at signalized intersections.

In most of the above mixed traffic studies, limited aspects of queue formation and dissipation at intersections have been addressed. Also, impact of traffic control and management measures have been studied in a limited way. For instance, they do not adequately consider the share of road space by straight-through, left-, and right-turning vehicles in the absence of lane discipline. The unique behavior such as seepage of two-wheelers to front of queues has received insufficient attention. Thus, the review of literature did not reveal comprehensive studies dealing with control measures under highly heterogeneous traffic conditions as prevailing in India. Hence, these aspects have been considered as the focus of this research work. The objectives of this research work were: (1) to study the queue formation and dissipation of vehicles at signalized intersections from microscopic data, (2) to develop simulation models incorporating heterogeneity that replicate field conditions (such as seepage of two-wheeler) as realistically as possible, and (3) to study the efficacy of right-turn lane (RTL) on measure of effectiveness (control delay), through simulation.

## Development of simulation model

Heterogeneous traffic is characterized by lack of queue and lane discipline (lane-less movement). The available simulation model developed by Gowri et al. (2009) was modified to facilitate simulation of traffic flow more realistically at a signalized intersection under heterogeneous traffic conditions. Logics of accumulation and dissipation of vehicles and seepage of two-wheelers to the front of queue are incorporated in the developed model. Further, the model was modified to facilitate simulating traffic flow with RTL (Gowri, 2011). For the purpose of simulation, the entire road space is considered as a single unit. The vehicles are represented as rectangular blocks on the road space, the length and breadth of the blocks representing, respectively, the overall length and the overall width of the vehicles. The model was developed in C++ language using object-oriented programming (OOP) concepts. The general flowchart of the simulation model is given in Fig. 1. The main parts of the traffic simulation model include data input and processing, generation of vehicles according to specified characteristics, placement and movement of vehicles (updating positions according to overtaking and car-following logics), accumulation and dissipation of vehicles, and processing of output for individual vehicles as well as for traffic stream. The logics are explained in the following subsections.

## Vehicle generation

At the beginning of a simulation run, the road space is assumed as empty. Then, the vehicles are generated at the starting point of the simulation road stretch using semiparametric distribution. Once a vehicle is generated, the type of the vehicle (two-wheeler, car, auto-rickshaw, LCV, bus, and truck) is identified based on the observed composition of traffic. The vehicular flows at intersections

![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-03.jpg?height=475&width=791&top_left_y=178&top_left_x=238)
2 Longitudinal and transverse spaces for vehicle placement

are of different types depending on the direction they take. The generated vehicle is assigned with the type of movement (left turning, straight through, or right turning) by generating a random number and comparing it with the cumulative composition of each type of movement.

The generated vehicle is also assigned a free speed. The speed of vehicles on simulation road stretch is based on two assumptions: (a) vehicle speeds will not be allowed to exceed their free speeds in the entire stretch, and (b) the vehicles are entering the simulation stretch with their free speeds. The free speeds of vehicles follow normal distribution. Hence, the standard normal deviates are generated using Box-Muller transformation method by using the equation

$$
Z=\sqrt{-2 \ln R_{1}} \times \cos \left(2 \pi R_{2}\right)
$$

where $Z$ is a standard normal deviate and $R_{1}, R_{2}$ are random numbers.

The free speed of each vehicle category can be obtained as

$$
u_{\mathrm{fi}}=\mu_{\mathrm{i}}+\sigma_{\mathrm{i}} Z
$$

where $u_{\mathrm{fi}}$ is the free speed of the vehicle category $i$ (car, bus, etc.), $\mu_{\mathrm{i}}$ is the mean speed of vehicle category $i$, and $\sigma_{\mathrm{i}}$ is the standard deviation of speed of vehicle category $i$.

## Vehicle placement

Vehicles are placed at the start of the roadway section in all periods of the simulation run. Vehicle placement at mid-block sections is based on availability of transverse and longitudinal spaces. Motorized vehicles can move more freely and faster nearer to the median. So, they are placed beginning from the right edge (median edge). Longitudinal and transverse spaces of vehicles are determined based on their current speeds. A motorized vehicle looks for longitudinal and transverse spaces in right most section of the road stretch. Figure 2 depicts the typical spaces that may be available at the simulation stretch for the placement of a motorized vehicle. A check is made to determine whether the available longitudinal and transverse spaces, with respect to the vehicle immediately ahead, on the right extreme side ( $L_{1}$ and $W_{1}$ in Fig. 2), are sufficient to place the entering vehicle as a follower to this vehicle. If the available transverse and longitudinal spaces are sufficient, the vehicle is placed on the rightmost location, leaving the specified clearance from the right edge. If either of them is inadequate, the available longitudinal and transverse spaces ( $L_{2}$ and $W_{2}$ in Fig. 2) with respect to the next-to-be-considered vehicle on the left side are compared with the respective values required for the entering vehicle to enable its placement behind it. Thus, all the longitudinal and transverse spaces are checked progressively along the width of the road toward the left end of the roadway, until the vehicle is placed in the simulation road stretch. Thus, the vehicles check the longitudinal and lateral spaces progressively from right edge to left edge of the road stretch. If such spaces are insufficient, the subject vehicle reduces its speed to that of its leader (car-following rule). Again, similar checks for spaces are made, beginning from the right most edge. If a vehicle is not able to find a suitable place, it will wait for the appropriate slot and will be loaded in the next scan interval.

## Vehicle movement

In this simulation model, a vehicle accelerates up to its free speed if there is no slow vehicle ahead of it. The position of vehicle is updated based on the following equations of motion

$$
\begin{aligned}
& S=u t+\frac{1}{2} a t^{2} \\
& v=u+a t
\end{aligned}
$$

where $S$ is the distance moved by the vehicle $(m), u$ is the initial speed of the vehicle ( $\mathrm{m} \mathrm{s}^{-1}$ ), $a$ is the acceleration of the vehicle $\left(\mathrm{m} \mathrm{s}^{-2}\right), t$ is the scan interval (s), and $v$ is the speed of the vehicle $\left(\mathrm{m} \mathrm{s}^{-1}\right)$ at the end of the scan interval.

If the initial speed of the vehicle is equal to its free speed, then the distance $S$ traveled by the vehicle in meters can be obtained using the following expression, since $a$ is 0 for a vehicle traveling at its free speed

$$
S=u_{\mathrm{f}} t
$$

where $u_{\mathrm{f}}$ is the free speed of the vehicle $\left(\mathrm{m} \mathrm{s}^{-1}\right)$ and $t$ is the scan interval (s).

When there is a slow moving vehicle in front of the subject vehicle, overtaking logic is invoked. During this stage, the subject vehicle (fast moving vehicle) checks for the free longitudinal and transverse spaces available on the right and left sides of the vehicle in front (slow moving vehicle). An overtaking maneuver is performed, if the spacing is found to be sufficient; in other words, it is at least equal to the sum of movable distance (MD) of the vehicle intending to overtake and the corresponding minimum longitudinal and lateral spaces. Left or right overtaking is performed based on the position of center line of overtaking vehicle. If the center line of the overtaking vehicle is on the right side of the center line of the overtaken vehicle, then the overtaking vehicle looks for availability of transverse and longitudinal spaces on the right side of the overtaken vehicle. If spaces are adequate on the right side, right overtaking is performed; if not, the overtaking vehicle looks for availability of such spaces on the left side, and if available, left overtaking is

![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-04.jpg?height=415&width=739&top_left_y=376&top_left_x=228)
(a)

![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-04.jpg?height=617&width=889&top_left_y=178&top_left_x=980)
(b)

## 3 Logics associated with vehicle movement process: a left and right overtaking maneuvers; b car following logic

performed. A similar overtaking process is applied for the vehicle whose center line is on the left side of the center line of the overtaken vehicle. In this overtaking process, the overtaking vehicle attempts lateral motion to come parallel to the overtaken vehicle. This process takes several scan intervals. The time taken for this lateral motion depends on the current vehicle speed, type of the vehicle, and its maximum acceleration rate. The left and right overtaking maneuvers are shown in Fig. 3a. The minimum required transverse spacing $\left(T_{\mathrm{s}}\right)$ for the overtaking vehicle is the sum of (a) width of the overtaking vehicle and (b) left side and right side clearances of the overtaking vehicle. Clearance is based on the premise that any vehicle should maintain adequate transverse clearances in the traffic stream on the left and right sides with respect to other vehicles/curb/median to avoid collision. The vehicle performs the overtaking (passing) maneuver only if the overall transverse space is at least equal to $T_{\mathrm{s}}$. If transverse space is inadequate on both sides, overtaking is not performed and car-following logic is invoked.

Figure 3b illustrates the car-following logic. In this case, the speed of the following vehicle is reduced to that of the lead vehicle, maintaining a safe spacing from it. The available distance (AD) in meters, is obtained as

$$
\mathrm{AD}=x_{\mathrm{n}}(t+1)-x_{\mathrm{n}+1}(t)
$$

where $x_{\mathrm{n}}(t+1)$ is the updated position of the lead vehicle (m) and $x_{\mathrm{n}+1}(t)$ is the position of the following vehicle before updation (m).

The MD of the following vehicle in meters is calculated during each scan interval by the following equation

$$
\mathrm{MD}=u_{\mathrm{F}} t+\frac{1}{2} a t^{2}
$$

where $u_{\mathrm{F}}$ is the speed of the following vehicle at the beginning of the scan interval $\left(\mathrm{m} \mathrm{s}^{-1}\right), a$ is the acceleration rate of the following vehicle $\left(\mathrm{m} \mathrm{s}^{-2}\right)$, and $t$ is the scan interval (s).

The following vehicle will move freely if AD is greater than or equal to distance (MD+safe space headway); otherwise, the following vehicle reduces its speed. In this case, the following vehicle trails the lead vehicle by decelerating to a speed equal to the speed of the lead vehicle ( $V_{\mathrm{n}+1}=V_{\mathrm{n}}$ ), and it maintains the minimum safe space headway. The minimum safe space headway $h$ is calculated as

$$
h=\left(c+L_{\mathrm{n}}\right)
$$

where $c$ is the clear longitudinal spacing between back of the lead vehicle and the front of the following vehicle (m) and $L_{\mathrm{n}}$ is the length of the lead vehicle (m). The $c$ value is calculated by multiplying the reaction time of driver by the reduced speed of the following vehicle.

## Vehicle accumulation

When the signal changes to red, the vehicles arriving near the intersection accumulate on the road based on the availability of spaces and type of turning movement. The logic used in the accumulation process is that vehicles try to occupy a position as close to the stop line as possible. The vehicles are placed on the road to occupy logical positions starting from the left side of the road, except the right-turning vehicles. After reaching near the intersection area, the vehicles' maneuvers are based on the direction and status of signal (red or amber or green). If two vehicles try to occupy the same gap, the one whose front position is closer to the stop line will take that gap. If the signal is amber, then those vehicles that have already entered the intersection accelerate and clear the intersection. The vehicles that are before the stop line will start to decelerate based on their deceleration rates. Then, the speeds of the vehicles are updated using the following equation

$$
v=u+a t
$$

When the status of the signal is red, the vehicles will decelerate and come to stop. All the vehicles form queues
behind the stop line based on their direction of movement. For example, the left-turn vehicles accumulate behind the queue on the left side of the road. Thus, all the vehicles accumulate on the intersection approach till the signal phase is red. The left and right clearances of vehicles are fixed based on field observed values.

## Vehicle dissipation

If the signal turns green, vehicles waiting at the intersection approach start dissipating after the reaction time. Initially, the current speed of all the accumulated vehicles is zero. The positions of all the vehicles are updated using equations of motion. Three maneuvers are possible for individual vehicles when the vehicles clear the intersection area:

1. The leading vehicle may be able to accelerate freely up to its desired speed when there are no vehicles in front. These vehicles are termed as free movers in the simulation model.
2. The vehicle may follow a slow moving vehicle, with relatively lesser speed and acceleration values. Then, the vehicle is allowed to overtake the slow vehicle in front, if space is available on the right side of the vehicle in front. If sufficient space is not available on the right side of the front vehicle, then, it will check for space on the left side of the vehicle in front to perform the overtaking maneuver. These vehicles are termed as overtakers.
3. Though the performance characteristics such as speed and acceleration of the subject vehicle may be higher than those of the vehicle in front, the vehicle may not be able to overtake because of insufficient free space; the vehicle will then simply follow the vehicles in front. Then, the subject vehicle is termed as follower.

## Vehicle movement on turn lanes

The model is also capable of simulating vehicular interactions on right-turn lanes. This logic forms part of the movement logic. Movement of vehicles on right-turn lanes involves the following:

- deceleration of vehicles approaching right-turn lanes, and
- lateral movement of vehicles to reach the right-turn lanes.

The information required for building a simulation model of the right-turn lane includes percentage of right-turning vehicles, total approach volume, and right-turn lane length. Right-turning vehicles check for possibility of occupying the right-turn lane. The key features of this logic are:

- When a right-turning vehicle approaches near the rightturn lane, a check is made to determine whether there is available space in RTL. The vehicles will decelerate and enter the turn lane if there is space.
- If space is not available, vehicle will continue to move in the same lane.
- It is ensured that other vehicular movements (left and straight) are not allowed on right-turn lanes.

## Model calibration

To test the concepts in this simulation work, a field study was conducted to determine the queue characteristics and traffic-dispersal patterns of heterogeneous traffic. Data required to build model parameters include the type of headway distribution, free speed characteristics of different types of vehicles, acceleration/deceleration characteristics of different types of vehicles, longitudinal spaces, and range of vehicle accumulation at stopped condition.

## Data collection and extraction

In order to study the vehicle behavior under heterogeneous conditions, video recordings of a signalized intersection in Ashok Nagar, Chennai city, India were conducted. This intersection has major approaches of 8.2 m road width and minor road approaches of 7.5 m width. In this intersection, a total of 9 h (2-h peak periods and 1-h off-peak periods on three consecutive weekdays) of video recording was carried out from vantage points.

To reduce errors because of parallax effect of cameras, virtual gridlines overlaid on the video images were used. The approach road width of 8.2 m was divided into eight grids of each 1 m except the left most grid, which is 1.2 m, and the length was divided into four blocks of each 5 m. Corresponding to these reference points on the ground, gridlines were overlaid on the video images using video editing and graphics software (Fig. 4). Knowing distances on the ground and corresponding coordinates on the screen, conversion factors (screen to real) were worked out. The variations in $x$ - and $y$-factors for different blocks are because of camera height and angle vis-a-vis the location of the block. These conversion factors reduce the parallax effect and are hence, useful in assessing the range of accumulations by vehicles when signal phase is red. Video image processing software was used to extract data from the video. It extracts video images into frames, where 1 s video data is converted into 25 frames. It was used to determine the screen coordinates of vehicle positions by manually viewing the individual frames. Each maneuver of vehicle was analyzed in detail to obtain the parameters for calibration and validation. The following subsections explain the data extraction procedure for calibrating the simulation model.

## Headways

The headway data were collected from an approach of a signalized intersection at the case study intersection. A video camera was mounted on the elevated point before the intersection, opposite to a lamp post (reference point) to continuously capture the moving traffic across the reference point. Traffic movements were captured using videography during peak and off-peak periods. The data contained 1442 headway observations corresponding to an hourly volume of 4000 vehicles. The data did not follow negative exponential, gamma, or lognormal distribution for a confidence level of 95\%. So, the headways of the vehicles were generated using semi-parametric distribution. Cumulative frequency of headway in the class interval of 0.6 s was obtained and given as input to the simulation model. The first random number was generated to find the vehicle in the headway range obtained. The second random number was used to calculate the headway within the selected range. Thus, the vehicles were generated. The number of vehicles observed in field and through the model was compared for 20 min traffic flow. They were found to be matching satisfactorily.
![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-06.jpg?height=879&width=1005&top_left_y=174&top_left_x=546)

## 4 Gridlines overlaid on the video

## Free speeds of vehicles

Free speed is defined as the speed adopted by the driver when not restricted by another vehicle in the stream under a set of given roadway and environmental conditions. Factors such as driver characteristics, vehicle, roadway, traffic, and environment influence free speeds. Average value of free speeds of each category of vehicles is termed as its mean free speed. To estimate the speeds of different categories of vehicles, time taken by vehicles to traverse a trap length of 100 m from stop line during green time was determined. The data collected at the case study intersection (during off-peak period of 6.30 am to 7.30 am) on two consecutive week days were used to estimate the free speeds of different types of vehicles.

## Deceleration rates of vehicles

The vehicles approaching the intersection area decelerate to come to stop if the signal is red. The deceleration rates of vehicles vary for different types of vehicles. For this purpose, data were collected from the case study intersection. Irfanview software was used for collection of deceleration rates of vehicles. Two stretches of 5 m length were selected, one before the stop line and the other before the first stretch. The speed of a vehicle in the first stretch was obtained by calculating the time taken by the vehicle to cross this stretch. Similarly, the speed on the second stretch was obtained. The deceleration rate was computed by using the speed difference of these two stretches and the time taken to cross these stretches. Highest deceleration rate was observed for two-wheelers ( $1.49 \mathrm{~m} \mathrm{~s}^{-2}$ ).

## Range of vehicle accumulation

When the signal changes to red, vehicles start accumulating at the intersection approach width. Since mixed traffic has no lane discipline, left-turning, straight-through, and right-turning vehicles accumulate at the approach haphazardly. The traffic simulation model requires range of accumulation by vehicles as necessary input. For this purpose, traffic data collected at the case study intersection were used. The traffic movements during each red phase for peak period (30 min) of three consecutive days were analyzed to extract vehicle accumulation data. The $x$ and $y$ coordinates of the left and right edge of a vehicle was found out from the frames of the video data. Type of vehicle, type of turning movement, left coordinate, right coordinate, block number, and grid number were noted down. Totally 700 data points were obtained from 90 min peak period. The data were analyzed using a MATLAB code. The conversion factors were applied to each data point to obtain the ground coordinates.

Figure 5 shows the values obtained by plotting the cumulative frequency distribution curves by analyzing the data points for each type of movement (straight-through, left-, and right-turning vehicles). The eighty-fifth percentile values from the cumulative frequency distribution curves are considered as the range of accumulation of each type of movement. Left-turning vehicles accumulate from 0 to 3.2 m, straight-through vehicles from 0 to 5.2 m, and right-turning vehicles from $4 \cdot 2$ to $8 \cdot 2$ m. These range of vehicle accumulation values are given as inputs to the traffic simulation model to simulate the vehicle behavior at stopped condition when the signal phase is red.

## Dissipation of vehicles

When the signal changes to green, vehicles start dissipating fro m the stopped condition after the reaction time. Acceleration during dissipation is different compared to acceleration of vehicles at the mid-block sections. The initial speed of a vehicle was taken as zero. A small stretch of 5 m at a distance of 5 m after the stop line was selected

![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-07.jpg?height=352&width=522&top_left_y=180&top_left_x=249)
(a)

![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-07.jpg?height=346&width=537&top_left_y=183&top_left_x=778)
(b)

![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-07.jpg?height=361&width=550&top_left_y=176&top_left_x=1343)
(c)

5 Cumulative frequency distribution curve for accumulation of vehicles at stopped condition: a left turning vehicles; b straight through vehicles; c right turning vehicles
to determine the final speed of the vehicle. The difference between the initial speed and final speed was calculated. The acceleration rate was then calculated by the difference in speed and time taken. Highest dissipation rates were observed for two-wheelers followed by cars.

## Longitudinal spacing of vehicles

Any vehicle moving in the traffic stream is to maintain sufficient longitudinal clearances in the front and back with respect to other vehicles to avoid collision. The vehicles that stop at the intersection approach maintain safe spaces with the front vehicles while they wait for the green signal to clear the intersection. The space between the back of the front vehicle (i.e., subject vehicle) and the front of the back vehicle at stopped condition is termed as longitudinal spacing of the subject vehicle. Owing to the mixed nature of the traffic, there are many combinations of front vehicle and back vehicles, and the spaces between them at stopped condition are necessary inputs for a simulation model. These spaces were observed in the field and used in the simulation model.

## Seepage of motorcycles to fronts of queues

At the case study intersection, two-wheelers were 71\% of the observed vehicles. They reduce the speed of other modes and make the traffic more congested because of their shapes and behavior. They are capable of zigzag maneuvers, creep up slowly to the front of the queue when the signal is red, and impede traffic flow by disturbing the start of other vehicles behind. On the basis of observations, the maximum creeping speed used in the model was $10 \mathrm{~km} \mathrm{~h}^{-1}$.

The input parameters for simulation model, such as traffic volume, vehicle composition, and proportion of turning movements were extracted from the video data. Total traffic volume at the intersection approach was 4000 veh $\mathrm{h}^{-1}$. Straight-through, right-turning, and leftturning vehicles comprise 75\%, 18\%, and 7\% of total vehicles, respectively.

## Model validation

Control delay is the portion of the total delay attributed to traffic signal operation for signalized intersections. This delay was observed for each vehicle type during peak period of traffic flow on three consecutive week days. It is expressed in terms of seconds. Since locating cameras at vantage points had some limitations and restrictions in this study as a result of site conditions, the following methodology was adopted to estimate the control delay. A trap length of 100 m was selected before the stop line on an approach. The entry and exit times of each vehicle on this trap length during green phase were noted down. The difference between these two timings was taken as the free flow travel time. The congested travel time was calculated if the vehicle enters the starting point of trap length during green or red phase and exits the trap length after experiencing delay at the intersection approach. The difference between the above congested travel time and free flow travel time was taken as the control delay in this study.

The traffic data collected at an approach of Ashok Nagar were used to validate the simulation model for intersection. Traffic movements were captured using videography during peak hours of traffic ( $8 \cdot 30-10 \cdot 30$ am) on three consecutive week days. Three video cameras were used to collect video data. One camera was placed at an elevated position, before 100 m from the stop line to collect data on headway, control delay, and free speeds. Second camera was placed at an elevated position before the stop line to collect data on control delays, free speeds, and vehicle accumulation. The third camera was placed on the ground to capture the signal timings to extract control delays and free speeds.

## Comparison of simulated and observed control delay

The ability of the model to predict the traffic behavior of vehicles on the link of the intersection was examined with the help of data on control delay. The control delay for each vehicle type was obtained from the field and simulation model. Table 1 shows the comparison of simulated and observed values of control delay for a volume level of 4000 veh $\mathrm{h}^{-1}$ on each major approach. Control delay of bus, LCV, and truck were combined to get control delay of heavy vehicles (HV). The percentage of error between observed and simulated delay was less than 15\% for all the vehicle types, which indicates that the model is replicating the field conditions reasonably. These values are acceptable and conform to the limits (15\%) as proposed by Dowling et al. (2004) and Mathew and Radhakrishnan (2010).
![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-08.jpg?height=395&width=778&top_left_y=180&top_left_x=221)

6 Schematic layout of the road stretch with the proposed right-turn lane (RTL)

## Model application

Right-turn lane is used to provide space for the deceleration and storage of right-turning vehicles and to separate the turning vehicles from the through movement. It is provided exclusively for right-turning vehicles to facilitate the right-turning movement to quickly dissipate from the intersection. The assumed layout of the road stretch with the proposed RTL is shown in Fig. 6. A number of factors influence the decision regarding whether RTL should be used at an urban intersection or not. In the absence of RTL, right-turning traffic increases congestion and delay, and reduces the safety and capacity of lanes. As a delay reduction and congestion mitigation measure, right-turn lanes can be used to provide space for the deceleration and storage of turning vehicles and to separate the turning vehicles from the through movement. However, the efficacy of such RTLs has not been studied so far under heterogeneous traffic conditions. The developed model was used to study this. A sensitivity analysis was carried out by varying the total approach volume, right-turn proportion and turn lane length to study the impacts of RTL on delays to vehicles. For this purpose, control delays for the two major approaches were obtained from the simulation model.

## Influencing parameters and the assumed values for sensitivity analysis

The case study intersection approach has a total volume of 4000 veh $\mathrm{h}^{-1}$ /major approach. The proportion of leftturning and right-turning vehicles were 7\% and 18\%, respectively, at the major approaches of the case study intersection. The width of case study intersection approach (major) is 8.2 m. The following parameters were assumed in the sensitivity analysis:

- Total approach volume on each of the major approaches was varied from 500 to 4000 veh $\mathrm{h}^{-1}$. The total volume on each of the minor approaches was taken as 500 veh $\mathrm{h}^{-1}$.
- The right-turn proportion was varied from 5\% to 40\%, in increments of 5\% on both the approaches.
- The length of turn lane on both approaches was varied from 10 to 70 m in increments of 10 m.
- The width of right-turn lane on the two major approaches was assumed as 3.5 m.
- Duration of red phase on both the approaches was taken as 55\% of total cycle time (field data).
- Total cycle time of the signal was taken as 134 s based on field data.

## Modeling traffic flow at signalized intersection with right-turn lanes

Provision of a RTL requires comprehensive study of the flow characteristics of traffic, and this can be done by using appropriate modeling technique. The available simulation model developed by Gowri et al. (2009) was modified to facilitate simulating traffic flow with RTL. The model in its current form can simulate only traffic flow at signalized intersection, modification of the available model (by making changes in program) was required to make the model suited for the present study (Gowri, 2011). Right-turn lane was added exclusively near the median ( $3 \cdot 5 \mathrm{~m}$ width), which was allotted for accumulation and dissipation of right-turning vehicles. The type of turning movements (straight through, left, and right turning) was identified by numbering them from 0 t o 2. If the type of turning movement was right, a decision was made to allot it to RTL. A snapshot of animation of traffic flow on RTL at a signalized intersection is shown in Fig. 7.

Each scenario was examined in two sets of simulation modeling runs: one with and one without a RTL. In each case, three simulation runs were carried out (using three seeds), and the average values of control delays were taken. Simulation runs were performed for 448 scenarios with RTL and 64 scenarios without it, for a total of 512 runs. Each scenario simulation run represented 1 h of traffic flow.

## Delay reduction because of provision of RTL

Figure 8 illustrates the trends in average control delays experienced by vehicles in the presence and absence of RTL for volume levels ranging from 500 to 4000 veh $\mathrm{h}^{-1}$ on the major approach by varying turn proportions and RTL lengths. It is seen that for total volume levels

Table 1 Comparison of observed and simulated control delay
| Vehicle type | Control delay (s veh ${ }^{-1}$ ) |  | \% of error |
| :--- | :--- | :--- | :--- |
|  | Field (average) | Model (average) |  |
| Motorized two-wheelers (MTW) | 46 | 52 | 11.5 |
| Car | 44 | 50 | 12 |
| Auto-rickshaw | 44 | 50 | 12 |
| Heavy vehicles (HV) | 45 | 52 | 13.5 |


![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-09.jpg?height=945&width=1255&top_left_y=172&top_left_x=447)
7 Screenshot of animation of traffic flow at a signalized intersection with right-turn lanes

of $500-2500$ veh $\mathrm{h}^{-1}$, RTL (as compared to no-RTL case) generally yields reduction in control delay for various right-turn proportions and RTL lengths, indicating the beneficial effects of RTL. This may be attributed to the fact that RTL facilitates smoother flow of right-turning vehicles, thereby reducing the overall vehicle delays. For these volume levels, RTL is useful in reducing the delay (up to $4 \mathrm{~s} \mathrm{veh}^{-1}$ ) for all right-turn proportions.

When the approach volume increases (3000-4000 veh $\mathrm{h}^{-1}$ ), RTL yields higher delays for higher turn proportions (40\% for $3000-3500$ veh $\mathrm{h}^{-1}$ in the case of shorter turn lane lengths and 35\% and 40\% for $4000 \mathrm{veh} \mathrm{h}^{-1}$ ). This can be explained as follows. It was observed in the field under heterogeneous traffic conditions as prevailing in India, that in the absence of RTL, straight-through and left-turning vehicles form queues (during red phase) more toward the left side of the road and right-turning vehicles to the right side. This behavior facilitates more efficient discharge of vehicles during the following green phase. However, when there is an exclusive right-turn lane (simulation model), straightthrough vehicles form queues in both the lanes, leaving only the right-turn lane space for the right-turning vehicles. In such a scenario, the straight-through vehicles and right-turning vehicles will get mingled in the queue behind the turn lane, which will cause extra delays to right-turn vehicles in entering the right-turn lane and to straight-through vehicles (by blocking right-turn vehicles) in getting discharged from the intersection. Hence, the overall average delay increases for few cases of higher volumes with higher right-turn proportions and lower turn lane lengths.

## Total delay reduction because of RTL

The trends in total delay reduction for various approach volumes because of the provision of RTL were studied to determine the optimal lengths of RTL. For volume level of 4000 veh $\mathrm{h}^{-1}$, highest delay reduction of 1281 veh$\min \mathrm{h}^{-1}$ is obtained for 5\% right-turn proportion and 40 m RTL. Such savings, when translated to several peak hours in a day can lead to significant benefits. The optimal lengths of turn lanes corresponding to highest reductions in delays are suggested. For various scenarios of approach volumes and right-turn proportions, optimal right-turn lane lengths are suggested (Table 2).

The above analysis has brought out valuable insights on judicial application of RTL for various combinations of affecting parameters for intersection traffic management.

## Conclusion

A microscopic traffic simulation model was developed for heterogeneous traffic conditions and implemented in C++ language using OOP for a signalized intersection. The model allows the simulation of various types of vehicles, which have widely varying performance capabilities and also considers some unique behavior, such as seepage to fronts of queues by two-wheeled vehicles. This model also incorporates microscopic details of queue formation and dissipation, range of vehicle accumulation and longitudinal spacing between vehicles under lane-less traffic conditions near intersection area.

For lower approach volumes ( $500-2500$ veh $\mathrm{h}^{-1}$ ) for the case study, RTL (as compared to no-RTL case) is generally advantageous for various right-turn proportions
![](https://cdn.mathpix.com/cropped/6db25fcc-2fb7-4232-9e8f-444782da9d79-10.jpg?height=2084&width=1656&top_left_y=163&top_left_x=219)

8 Control delays after provision of right-turn lane (RTL) for various approach volumes: a 500; b 1000; c 1500; d 2000; e 2500; f 3000; g 3500; h 4000 veh/h

Table 2 Optimal right-turn lane (RTL) lengths for various approach volumes and turn proportions
| Right-turn proportion (\%) | Volume (veh $\mathrm{h}^{\boldsymbol{-} \mathbf{1}}$ ) | RTL optimal length (m) | Volume (veh $\mathrm{h}^{\boldsymbol{-} \mathbf{1}}$ ) | RTL optimal length (m) |
| :--- | :--- | :--- | :--- | :--- |
| 5 | 500 | 10 | 2500 | 30 |
| 10 |  | 10 |  | 30 |
| 15 |  | 10 |  | 30 |
| 20 |  | 20 |  | 40 |
| 25 |  | 20 |  | 40 |
| 30 |  | 20 |  | 40 |
| 35 |  | 20 |  | 40 |
| 40 |  | 20 |  | 40 |
| 5 | 1000 | 20 | 3000 | 30 |
| 10 |  | 20 |  | 30 |
| 15 |  | 20 |  | 30 |
| 20 |  | 20 |  | 40 |
| 25 |  | 20 |  | 40 |
| 30 |  | 20 |  | 40 |
| 35 |  | 20 |  | 50 |
| 40 |  | 20 |  | 50 |
| 5 | 1500 | 20 | 3500 | 30 |
| 10 |  | 20 |  | 30 |
| 15 |  | 30 |  | 40 |
| 20 |  | 30 |  | 40 |
| 25 |  | 30 |  | 40 |
| 30 |  | 30 |  | 50 |
| 35 |  | 30 |  | 50 |
| 40 |  | 30 |  | 60 |
| 5 | 2000 | 30 | 4000 | 40 |
| 10 |  | 30 |  | 40 |
| 15 |  | 30 |  | 40 |
| 20 |  | 30 |  | 40 |
| 25 |  | 30 |  | 50 |
| 30 |  | 30 |  | 50 |
| 35 |  | 30 |  | 60 |
| 40 |  | 30 |  | 60 |


and RTL lengths, signifying the efficacy of RTL, which facilitates smoother flow of right-turning vehicles. When the approach volume increases ( $3000-4000$ veh $\mathrm{h}^{-1}$ ), RTL yields higher delays for higher turn proportions and lower turn lane lengths. Highest delay reduction (1281 veh$\min \mathrm{h}^{-1}$ ) is achieved at 5\% right-turn proportion and 40 m RTL for 4000 veh $\mathrm{h}^{-1}$. Optimal lengths of turn lanes corresponding to highest reductions in delays are recommended for various scenarios of approach volumes and right-turn proportions. These vary from 10 to 60 m for the case study.

The above findings demonstrate that right-turn lanes can be considered for application as an appropriate intersection lane control tool for enhancing the efficiency of flow in heterogeneous traffic conditions. The developed simulation model can be employed for scenario analysis and can be valuable to field traffic engineers in implementing right-turn lanes. Through this study, the developed model can be used for possible application in coordination of signals, corridor simulation, signal design, and capacity analysis.

## Acknowledgement

This research work was carried out when the first author was a PhD scholar at the Indian Institute of Technology Madras (IIT Madras). The work was partly supported by funds made available through the Centre of Excellence in Urban Transport at the Indian Institute of Technology Madras sponsored by the Ministry of Urban Transport, Government of India.

## References

Arasan, V. T. and Kashani, S. H. 2003. Modeling platoon dispersal pattern of heterogeneous road traffic, Transportation Research Record: Journal of the Transportation Research Board, No. 1852, Transportation Research Board of the National Academies, Washington, DC, 175-182.
Chai, C. and Wong, Y. D. 2013. Traffic performance of shared lanes at signalized intersections based on cellular automata modeling, J. Adv. Transp., 2013, Online publication.
Chai, C. and Wong, Y. D. 2014. Micro-simulation of vehicle conflicts involving right-turn vehicles at signalized intersections based on cellular automata, J. Accid. Anal. Prev., 63, 94-103.
Chang, J., Talas, M. and Muthuswamy, S. 2013. A simple methodology to estimate queue lengths at signalized intersections using detector data, Proc. 92nd 2013 TRB Annual Meeting, Washington, DC, USA.
Chaudhry, M. S. and Ranjitkar, P. 2009. Capacity analysis of signalised intersection using micro-simulation, Proc. 32nd Australian Transport Research Forum, Auckland, New Zealand.
Dowling, R., Skabardonis, A. and Alexiadis, V. 2004. Calibration of microsimulation models, Report HWA-HRT-04-040, Washington, DC.
Fang, C. F. and Elefteriadou, L. 2005. Some guidelines for selecting micro simulation models for interchange traffic operational analysis, $J$. Transp. Eng., ASCE, 31, 535-543.
Fitzpatrick, K., Schneider, W. H. and Park, E. S. 2006. Predicting speeds in an urban right-turn lane, J. Transp. Eng., ASCE, 132, (3), 199-204.

Gowri, A. 2011. Evaluation of turn lanes at signalized intersections under heterogeneous traffic conditions using microscopic simulation model, PhD thesis, Indian Institute of Technology Madras, Chennai, India.
Gowri, A., Venkatesan, K. and Sivanandan, R. 2009. Object-oriented methodology for intersection simulation model under heterogeneous traffic conditions, Adv. Eng. Software, 40, (10), 1000-1010.
Hossain, M. 2001. Estimation of saturation flow at signalized intersections of developing cities: a micro-simulation modeling approach, Transp. Res. Part A Policy Pract., 35, (2), 123-141.
Huynh, D. N., Boltze, M. and Vu, A. T. 2013. Modeling mixed traffic flow at signalized intersection using social force model, Journal of the Eastern Asia Society for Transportation Studies, 10, 1734-1749.
Kikuchi, S. and Kronprasert, N. 2010. Determining the lengths of the leftturn lanes at signalized intersections under different left-turn signal schemes, Transportation Research Record: Journal of the Transportation Research Board, No. 2195, Transportation Research Board of the National Academies, Washington, DC, 70-81.
Kim, S. O. and Benekohal, R. F. 2005. Comparison of control delays from CORSIM and the highway capacity manual for oversaturated signalized intersections, J. Transp. Eng., ASCE, 131, 917-923.
Liu, H. X., Wu, X., Ma, W. and Hu, H. 2009. Real-time queue length estimation for congested signalized intersections, Transp. Res. Part C, 7, 412-417.
Maini, P. and Khan, S. 2000. Discharge characteristics of heterogeneous traffic at signalized intersections, Proc. 4th Int. Symp. on Highway Capacity, Maui, Hawaii.
Marwah, B. R., Raman Parti and Dev Reddy, P. K. C. 2006. Modeling for simulation of heterogeneous traffic at a signalized intersection, Highw. Res. Bull. Indian Road Congr., 74, 81-89.
Mathew, T. V. and Radhakrishnan, P. 2010. Calibration of microsimulation models for non-lane based heterogeneous traffic at signalized intersections, J. Urban Plann. Dev., ASCE, 36, 59-66.
Park, B. and Qi, H. 2005. Development and evaluation of a procedure for the calibration of simulation models, Transportation Research Record: Journal of the Transportation Research Board, No. 1934, Transportation Research Board of the National Academies, Washington, DC, 208-217.
Potts, I. B., Harwood, D. B., Ringert, J. F. and Bauer, K. M. 2007. Operational and safety effects of right-turn deceleration lanes on urban and suburban arterials, Proc. Transportation Research Board 2007 Annual Meeting, Washington, DC.
Qi, Y. G., Guo, L., Yu, L. and Teng, H. 2012. Estimation of design lengths of left turn lanes, J. Transp. Eng., ASCE, 138, (3), 274-283.
Sharma, A., Bullock, D. M. and Bonneson, J. A. 2007. Input-output and hybrid techniques for real-time prediction of delay and maximum queue length at signalized intersections, Transportation Research Record: Journal of the Transportation Research Board, No. 2035, Transportation Research Board of the National Academies, Washington, DC, 69-80.
Sharma, H. K. and Swami, M. 2012. Effect of turning lane at busy signalized at grade intersection under mixed traffic in India, Eur. Transp., 52.
Tan, D. M., Alhajyaseen, W. K. M., Asano, M. and Nakamura, H. 2012. Development of microscopic traffic simulation model for safety assessment at signalized intersections, Transportation Research Record: Journal of the Transportation Research Board, No. 2316, Transportation Research Board of the National Academies, Washington, DC, 122-131.
Tian, Z. Z. and Wu, N. 2006. Probabilistic model for signalized intersection capacity with a short right turn lane, J. Transp. Eng., 132, (3), 205-212.
Tohti, G., Abdukeram, T., Geni, M., Cheng, Y. F., Tursun, M., Mahmut, D. and Wang, B. 2013. Traffic flow modeling and simulation of signalized intersections, Proc. 9th Int. Conf. on Fracture \& Strength of Solids, Jeju, Korea.
Wu, A. and Yang, X. 2013. Real-time queue length estimation of signalized intersections based on RFID data, Procedia Soc. Behav. Sci., 96, 1477-1484.
Yang, J. 2008. Risk-based volume warrants for free right-turn lanes on two-lane roadways, J. Transp. Eng., ASCE, 134, (4), 155-162.


[^0]:    ${ }^{1}$ Department of Civil Engineering, National Institute of Technology Karnataka, Surathkal, Mangalore 575025, India
    ${ }^{2}$ Department of Civil Engineering, Indian Institute of Technology Madras, Chennai 600036, India
    *Corresponding author, email gowri_iitm@yahoo.co.in

