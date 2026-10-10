# Eco-driving at signalized intersections using V2I communication 

Hesham Rakha, Member, IEEE and Raj Kishore Kamalanathsharma


#### Abstract

The research presented in this paper develops a framework to enhance vehicle fuel consumption efficiency while approaching a signalized intersection through the provision of signal phase and timing information that may be available through vehicle-to-infrastructure communication. While past research uses simplified objective functions to optimize fuel consumption and/or emissions caused by signalized intersections, this research highlights the importance of retaining microscopic fuel consumption models in the optimization function. It presents an example which shows that simplified objective functions may result in erroneous conclusions.


## I. Introduction

The transportation sector is the second largest atmospheric carbon emitter in the United States [1]. Over two-thirds of this is contributed by non-freight vehicles [1]. Over 22 percent of the total petroleum consumption of the world is by the United States of which 71.4 percent is the transportation sector's share [2]. Since the 1960s, efforts to reduce atmospheric pollution caused by vehicles and to improve the efficiency of engines have grown significantly. Additionally, authorities world-wide have started to implement regulations to reduce global pollution and consumption of fossil fuels. But as the number of vehicles on the roads grow, traffic congestion has increased, annual miles traveled has increased and the net pollution has increased over the years [3].

Meanwhile, the U.S. Department of Transportation (FHWA) and other transportation agencies in developed nations have made significant advancements in various transportation technologies. In the mid 1990s, the FHWA's Intelligent Transportation Systems (ITS) Program emerged to increase the use of technology in the surface transportation sector [4]. Initial ITS applications were limited to Advanced Traffic Management Systems (ATMSs) and Advanced Traveler Information Systems (ATISs), but soon technology gained momentum in areas of communication and surveillance. In 2003, the Vehicle Infrastructure Integration (VII) Initiative was started by the

[^0]FHWA [5]. It aimed at bringing together the benefits of connecting vehicles and infrastructure to enhance roadway safety, reduce traffic congestion and mitigate the environmental impacts of transportation.

Simultaneously, research efforts focused on modeling driving decisions and other characteristics. Car-following, lane-changing, fuel-consumption and emissions models are examples for these. These research efforts helped in simulating and predicting driver behavior. Modeling efforts also aimed at predicting fuel consumption and emission levels of $\mathrm{NO}_{\mathrm{x}}, \mathrm{CO}_{2}, \mathrm{CO}$ and HC at a microscopic or macroscopic level. Some examples of state-of-the-art models include the Comprehensive Modal Emissions Model (CMEM), the VT-Micro Model, the VT Comprehensive Power-based Fuel Model (VT-CPFM) and the Vehicle Driveline model [6-9]. Also vehicle acceleration models can be used to predict a vehicle's trajectory [10]. These models collectively provide necessary tools to predict fuel consumption for various alternate trajectories and thereby, can help in developing an optimization system.

Research efforts attempting to reduce the carbon footprint and fuel consumption associated with driving have advanced significantly. On the mechanical side, nonpropulsion system improvements such as improved aerodynamics, rolling friction, weight reduction have enhanced average passenger vehicle gas mileage from 18.41/100 km in 1975 to 10.11/100 km in 2005. On the systems side, enhancement focused on reducing vehicular stops, travel time, smoothening the velocity curves and so forth [11].

This paper attempts to develop an eco-driving framework that utilizes vehicle-to-infrastructure (V2I) communication to receive signal phasing and timing (SPaT) information and compute the optimum course of action. The following sections, in order of presentation, deal with, literature review highlighting previous work on this front, development of the algorithm model, an example application and conclusions derived from this study.

## II. Literature Review

Past research has shown that braking is one of the biggest sources of power-loss in a vehicle primarily due to lost momentum the associated braking force [11]. Smoothing velocity trajectories, hence, was found to be an efficient fuel-saving method. Consequently, traffic safety advisors in the UK focused on development of Intelligent Speed Adaptation (ISA) devices that advised drivers on desired speed and speed limits on roadways [12]. Second generation ISA devices used built-in Global Positioning System (GPS)
units to advise the drivers of set-speed-limits on the roadway [13]. Third generation ISA devices used telematics to communicate real-time traffic information for speed advisories [14].

Even though ISA devices primarily aimed at safer driving, its users benefitted from reduced fuel consumption and emissions due to smoother speed variations [15]. From an energy/emissions stand-point, this laid the foundation for eco-driving, which refers to driving in an ecological and economical way. Maintaining a constant velocity and avoiding unnecessary acceleration and deceleration were the key principles behind eco-driving [6]. However, the dependency of speed variations on external factors such as neighboring vehicles, signal status and other infrastructural limitations rendered the use of eco-driving limited. A comparison study of eco-driving and ordinary driving showed no major difference in fuel-consumption when compact cars were considered [16]. Also, vehicles equipped with resistive devices to prevent sudden speed changes showed no major fuel efficiency enhancement [17].

However, use of real-time signal information to forecast the external factors to the vehicle and predict a fuel-optimal strategy was the focus of newer eco-driving research. Studies on freeway-based dynamic eco-driving systems showed fuel savings of the order of 10 to 20 percent when real-time signal information was used [18]. Potential savings in fuel were also identified in a separate research comparing Environment Adaptive Driving (EAD) when Inter-Vehicle Communication (IVC) was used and not used [19]. The Connected Vehicle Technology Initiative by the U.S. Department of Transportation aims at bringing vehicle-to-vehicle (V2V) communication and vehicle-toinfrastructure communication (V2I) together [20]. With this implementation, Signal Phase and Timing (SPaT) information will be made available to vehicles approaching an intersection which can be utilized to predict the speed trajectories in order to reduce fuel consumption at signalized intersections [21].

A few research efforts have been conducted aiming at developing algorithms that utilize traffic signal information to reduce fuel consumption and emissions. Barth et al. quantified the energy/emissions benefit of communicating Traffic Signal Status (TSS) to road users via Changeable Message Signs (CMS) or an in-vehicle Advanced Driving Alert System (ADAS) and found benefits of up to 40 percent under hypothetical conditions [22]. This system provided drivers with a Time to Red (TTR) advisory and did not use any Time to Green (TTG) information to compute the optimum velocity profile. Asadi and Vahidi developed a cruise control system which used constrained optimization to minimize the probability of reaching a stopline during a red phase by varying the speeds within an interval and showed up to 47 percent fuel savings [23]. This study, however, did not provide speed advisory to drivers, nor used any fuel consumption models to evaluate alternative velocity profiles.

Tielert et al. studied the factors affecting the fuel savings and reduction in emissions possible with Traffic Light to Vehicle Communication (TLVC) [24]. The VISSIM simulation tool was programmed at reducing the effective red time by speed adjustment. The Passenger car and Heavy duty Emissions Model (PHEM) was used in this study and showed savings of up to 22 percent. Malakorn and Park developed an IntelliDrive-based Cooperative Adaptive Cruise Control with the objective of minimizing the distance length of deceleration and acceleration as well as idling time when Traffic Signal Status (TSS) information is available [25]. This model neglected the maneuver downstream of the intersection and did not use any fuelconsumption model in the optimization function.

Mandava et al. developed an arterial velocity planning algorithm which provided velocity advisory to the drivers regarding the most fuel optimal path computed using the upcoming signal information [26]. The objective function did not use any fuel-consumption model and aimed at minimizing deceleration and acceleration rates. Benefits of 12 to 13 percent were shown. The TRAVOLUTION project partnered by Audi and GEVAS software aimed at providing a green wave to cars equipped with V2I communication modules. The system showed up to 21 percent reduction in fuel consumption levels [27]. No literature regarding the algorithm or model used is publicly available.

The aforementioned literature shows that there has been research in developing dynamic eco-driving logic using V2I communication. However, none of these approaches used an explicit optimization objective of reducing fuel consumption. The goal of reducing fuel consumption, in all these cases, is transformed to simpler functions of acceleration/deceleration rates, or duration of these events, or even the time of arrival at the intersection. In this research effort, the objective function of reducing fuel consumption will be maintained as it is and alternative analysis will be used to compare different velocity profiles that can be taken by a vehicle approaching an intersection.

## III. Algorithm Model

In this research, an eco-drive model is developed and evaluated using an example application. It assumes that SPaT information for the upcoming traffic signal is available to vehicles approaching it using V2I communication as envisioned by the Connected Vehicles Technology [20]. In order to avoid the effects due to human interaction, it assumes that the vehicle is in full control or that the driver follows the instructions precisely. In reality, this transforms to giving instantaneous speed advisory to drivers. Clearly the greater the accuracy of the driver in following these advisory recommendations, the closer it gets to the fuel optimum. The model uses the VT-Micro model to estimate fuel consumption for various alternative speed profiles and determines which is the optimum [6]. The vehicle trajectory is divided into the trajectory upstream and downstream of the traffic signal stop-line and a combined
optimum is calculated using mode-specific fuel consumption and emission levels for vehicle deceleration, cruising/idling, and acceleration modes. A vehicle dynamics model is used to compute the maximum instantaneous acceleration levels from the net force computation [10].

## A. VT Micro Model

The VT-Micro emissions model was developed as a statistical model consisting of linear, quadratic and cubic combinations of speed and acceleration levels using chassis dynamometer data collected at the Oak Ridge National Laboratory (ORNL) and the Environmental Protection Agency (EPA). The final regression models provided a good fit for all measures of effectiveness (MOEs) tested. The ORNL data consisted of 1300 to 1600 individual measurements for each vehicle-MOE combination and the final model is given in Equation 1.

![](https://cdn.mathpix.com/cropped/cee5aff5-9974-4647-bb76-ff10c3830ecb-3.jpg?height=1405&width=1656&top_left_y=563&top_left_x=234)
Figure 1: Proposed Eco-drive Model

$$
M O E_{e}= \begin{cases}\exp \left(\sum_{i=1}^{3} \sum_{j=1}^{3} L_{i, j}^{e} v^{i} a^{j}\right) & \text { for } a \geq 0 \\ \exp \left(\sum_{i=1}^{3} \sum_{j=1}^{3} M_{i, j}^{e} v^{i} a^{j}\right) & \text { for } a<0\end{cases}
$$

where, $M O E_{\mathrm{e}}$ is the instantaneous fuel consumption or emission rate (ml/s or mg/s); $L^{e}{ }_{i, j}$ are the model coefficients for $M O E_{e}$ at speed power $i$ and acceleration power $j$ for positive accelerations; $M^{e}{ }_{i, j}$ are the model coefficients for $M O E_{e}$ at speed power $i$ and acceleration power $j$ for negative accelerations; $v$ is the instantaneous speed (km/h); and $a$ is the instantaneous acceleration (km/h/s).

## B. Vehicle Dynamics Model

A vehicle dynamics model is used to model the acceleration maneuver. In doing so, the vehicle speed is computed from the resultant forces acting on the vehicle. These forces include the tractive force given by Equation 2 and various vehicle resistive forces given in Equation 3.

$$
\begin{aligned}
& F=\min \left(3600 f_{p} \beta \eta_{d} \frac{P}{v}, m_{t a} g \mu\right) \\
& R=\frac{\rho}{25.92} C_{d} C_{h} A_{f} v^{2}+m g \frac{c_{r 0}}{1000}\left(c_{r 1} v+c_{r 2}\right)+m g G
\end{aligned}
$$

where $f_{p}$ is the driver throttle input [0,1] (unitless) (field studies have shown that it is typically 0.60 ); $\beta$ is the gear reduction factor (unitless); $\eta_{d}$ is the driveline efficiency (unitless); $P$ is the vehicle power $(\mathrm{kW}) ; m_{t a}$ is the mass of the vehicle on the tractive axle (kg); $v$ is the vehicle speed $(\mathrm{km} / \mathrm{h}) ; g$ is the gravitational acceleration $\left(9.8067 \mathrm{~m} / \mathrm{s}^{2}\right) ; \mu$ is the coefficient of road adhesion or the coefficient of friction (unitless); $\rho$ is the air density at sea level and a temperature of $15^{\circ} \mathrm{C}\left(1.2256 \mathrm{~kg} / \mathrm{m}^{3}\right) ; C_{d}$ is the vehicle drag coefficient (unitless), typically $0.30 ; C_{h}$ is the altitude correction factor (unitless); $A_{f}$ is the vehicle frontal area ( $\mathrm{m}^{2}$ ); $c_{r 0}$ is rolling resistance constant (unitless); $c_{r 1}$ is the rolling resistance constant $(\mathrm{h} / \mathrm{km}) ; c_{r 2}$ is the rolling resistance constant (unitless); $m$ is the total vehicle mass (kg); and $G$ is the roadway grade at instant t (unitless).

The vehicle acceleration is calculated as a ratio of the difference between the tractive force and resistive forces and the vehicle mass (i.e., $a=(F-R) / m$ ). The vehicle speed at ( $t$ $+\Delta t)$ is then computed by solving the differential equation using a first-order Euler approximation as

$$
v(t+\Delta t)=v(t)+3.6 \frac{F(t)-R(t)}{m} \Delta t .
$$

## C. Eco-Drive Model

The eco-drive model predicts the fuel-optimum speed profile for vehicles approaching an intersection and provides instantaneous speed advisories. Such a model relies on Dedicated Short-Range Communication (DSRC) connectivity between vehicles and the infrastructure and communication of SPaT information to the vehicle. As a vehicle travels on a roadway and enters the DSRC range of a particular intersection, it receives information regarding future signal changes and information on the size of queues at the approach and/or leader vehicle(s). This is when the proposed eco-drive mode starts. This logic is demonstrated in Figure 1.

With respect to the future signal change a number cases can exist:

i. If the signal indication will be/remain green when the vehicle reaches the stop-line, then the advisory will be to proceed at the same speed.
ii. If the signal changes to yellow then the vehicle is advised to proceed as long as it does not run a red light.
iii. If the traffic light will change to red before the vehicle reaches the intersection, it may still be possible to pass freely if the vehicle accelerates to some allowed upper speed level.
iv. If the time gained by accelerating to the maximum set speed limit, is not sufficient to safely pass through the intersection then the vehicle decelerates and if needed stops. This delay is a function of the Time-to-Green (TTG) and number of vehicles queued ahead.

In the final case if the traffic signal indication is red, the model compares the fuel consumed for alternate speed profiles depending on the time to the start of the next green and clearing of queues. In order to incorporate the delay the vehicle should decelerate from its approach speed and once past the intersection, it can accelerate back. Therefore, the speed profiling for fuel optimization can be divided into two portions:

i. Upstream of the intersection to incorporate delay maintaining the Distance to Intersection (DTI), Time to Green (TTG) and if any, time to clear queues in front of the vehicle, and
ii. Downstream of the intersection where the vehicle accelerates back to its original speed.

Downstream of the intersection is considered because the fuel consumed in that portion depends on the speed of the vehicle at the intersection. The lower this speed, the larger is the fuel consumed to accelerate back.

## 1) Equations Governing Upstream Portion

Consider a vehicle approaching a traffic signal that is currently red and will turn green in $t$ seconds. Using V2I communication, the vehicle receives this information at a distance $x$ meters from the intersection. Assume that the vehicle is traveling at a speed of $v_{a} \mathrm{~m} / \mathrm{s}$. At this speed, it will reach the intersection before the green indication starts. Let $\Delta t$ seconds be the delay required so that the vehicle reaches the intersection once the signal turns green and queued vehicles are cleared and let $v_{s} \mathrm{~m} / \mathrm{s}$ (variable) be its speed at stop-bar.

The objective is to compute the speed profile of the vehicle that satisfies the input parameters. The speed profile is defined by two parameters, namely: the deceleration level $d$ and the speed the vehicle crosses the intersection stop line $v_{s}$. The solution to this problem is bounded by two solutions, as illustrated in Figure 2. The first bounding solution involves minimizing the time spent decelerating when the highest possible deceleration is applied. The second bounding solution involves minimizing the level of deceleration exerted by decelerating over the entire distance $x$. There are an infinite number of possible solutions between these two bounding solutions.

![](https://cdn.mathpix.com/cropped/cee5aff5-9974-4647-bb76-ff10c3830ecb-4.jpg?height=430&width=735&top_left_y=1835&top_left_x=1141)
Figure 2: Bounding Speed Profiles of Approaching Vehicle

The speed profile shown by the solid line in Figure 2 represents the speed profile of the vehicle if it travels at a constant minimum deceleration level in order to ensure that the vehicle traverses the distance $x$ in time $t$. Let this value of deceleration be labeled $d_{m i n}$. The speed profile shown by the dash-dotted line represents the vehicle speed profile if
the objective is to minimize the time spent decelerating. The vehicle decelerates at a maximum feasible rate of $d_{\text {max }} \mathrm{m} / \mathrm{s}^{2}$ to a velocity $v_{s} \mathrm{~m} / \mathrm{s}$ initially and then cruises at this velocity over a distance $x_{r}$ meters. In between these two solutions we have an infinite number of solutions for $d$ ranging between $d_{\text {min }}$ and $d_{\text {max }}$ (i.e. $d=\left[d_{\text {min }}, d_{\text {max }}\right]$ ).

In order to derive equations governing upstream speed profile of the vehicle, consider basic equations of motion. Since the value of $x$ is conserved in any case,

$$
x=\frac{v_{a}^{2}-v_{s}^{2}}{2 d}+x_{r}
$$

Also, the time to intersection, $t$ is conserved for all cases. Therefore,

$$
t=\frac{v_{a}-v_{s}}{d}+\frac{x_{r}}{v_{s}}
$$

Equation 5 can be re-written to:

$$
x_{r}=x-\frac{v_{a}^{2}-v_{s}^{2}}{2 d}
$$

Combining Equations 6 and 7:

$$
t=\frac{v_{a}-v_{s}}{d}+\frac{1}{v_{s}}\left(x-\frac{v_{a}^{2}-v_{s}^{2}}{2 d}\right)
$$

For a particular value of $d$, the only unknown in Equation 8 is the speed at intersection, $v_{s}$, which is the positive solution of the quadratic equation. This solution is given by:

$$
v_{s}=v_{a}-d t+\sqrt{d\left(d t^{2}-2 v_{a} t+2 x\right)}
$$

Once $v_{s}$ is computed, $x_{r}$ can be calculated using Equation 7.
These equations will be used to compute various speed profiles between the bounds specified earlier along with associated fuel consumption predicted using VT-Micro model. This is denoted by $F_{1}$ hereafter.

## 2) Equations Governing Downstream Portion

Vehicle maneuver downstream of the intersection is associated with accelerating back to $v_{a}$. A vehicle dynamics model will be used to compute the speed profiles for various throttle levels for a given $v_{s}-v_{a}$ pair. Vehicles are assumed to follow constant throttle to accelerate back and fuel consumed for the matrix of $v_{s}-v_{a}$ pair for throttle levels ranging from 30 to 100 percent at 10 percent increments is computed using VT-Micro model. This is denoted by $F_{2}$ hereafter.

## IV. Example Application

Consider a single vehicle approaching a signalized intersection with V2I communication capability with the current phase red. The vehicle approach speed is 20 m/s on a roadway with a zero percent grade (level road) at standard air temperature and pressure. At a distance of 200 m from the intersection stop-line, it receives information regarding the next green indication which will start in 14 seconds. If the vehicle continues at its current speed it will reach the stop line in 10 seconds suggesting that a delay of 4 seconds is needed in order to travel through the green indication. Using Equations 4 through 7, various speed profiles can be generated that satisfy the following input: $v_{a}=20 \mathrm{~m} / \mathrm{s}, x=$ $200 \mathrm{~m}, t=14 \mathrm{~s}$, and $\Delta t=4 \mathrm{~s}$. The minimum deceleration level $d_{\text {min }}$ is computed to be $0.816 \mathrm{~m} / \mathrm{s}^{2}$. The corresponding speed at the stop line $v_{s}$ is computed to be 8.571 m/s. Table 1 shows a few other possible scenarios where $d>d_{\text {min }}$ up to a deceleration level of 0.6g along with associated fuel consumed (assuming ORNL-composite vehicle characteristics) . Note that for any value of $d$ greater than $d_{\text {min }}$ there is an associated cruising phase.

Table 1: Fuel consumed during deceleration
| Case | d $\left(\mathrm{m} / \mathrm{s}^{2}\right)$ | $v_{s}(\mathrm{~m} / \mathrm{s})$ | $x_{r}(\mathrm{~m})$ | $t_{d}(\mathrm{~s})$ | $t_{c}(\mathrm{~s})$ | $F_{D}(\mathrm{ml})$ | $F_{C}(\mathrm{ml})$ | $F_{I}(\mathrm{ml})$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.82 | 8.57 | 0.0 | 14 | 0 | 7.15 | 0.00 | 7.15 |
| 2 | 0.83 | 9.99 | 19.8 | 12 | 2 | 6.26 | 2.26 | 8.52 |
| 3 | 0.89 | 11.11 | 44.5 | 10 | 4 | 5.29 | 4.00 | 9.29 |
| 4 | 1.00 | 12.00 | 72.0 | 8 | 6 | 4.26 | 5.86 | 10.12 |
| 5 | 1.21 | 12.72 | 101.6 | 6 | 8 | 3.22 | 7.80 | 11.03 |
| 6 | 2.13 | 13.60 | 149.5 | 3 | 11 | 1.81 | 10.84 | 12.65 |
| 7 | 5.90 | 14.07 | 182.9 | 1 | 13 | 0.92 | 12.92 | 13.84 |


The fuel consumed in each profile is computed using the VT-Micro model for an ORNL composite vehicle and summarized in Table 1. Table 1 shows that gradual deceleration to the stop-line, as denoted by Case 1, is the most fuel-efficient deceleration maneuver. It, however, results in a lower speed at the stop-line $\left(v_{s}\right)$ compared to the other cases and thus would require greater fuel, $F_{2}$, to accelerate back to $v_{a}$. The fuel consumption for the entire maneuver including decelerating, cruising, and accelerating is then computed as shown in Table 2. Vehicle dynamics model is used to compute the instantaneous speeds when accelerating back to the original speed for different throttles and the throttle level corresponding to minimum fuel was used to build cases.

Table 2: Fuel consumed during acceleration
| Case | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| u(m/s) | 8.6 | 10.0 | 11.1 | 12.0 | 12.7 | 13.6 | 14.1 |
| u(km/h) | 30.9 | 36.0 | 40.0 | 43.2 | 45.8 | 49.0 | 50.7 |
| v(km/h) | 72.0 | 72.0 | 72.0 | 72.0 | 72.0 | 72.0 | 72.0 |
| Throttle | 53.9 | 49.5 | 45.3 | 41.3 | 41.0 | 37.0 | 33.3 |
|  | 53.0 | 47.2 | 46.5 | 41.2 | 40.8 | 35.5 | 35.2 |
|  | 55.2 | 47.8 | 47.1 | 40.2 | 39.8 | 33.0 | 32.8 |
|  | 59.6 | 51.5 | 50.6 | 42.0 | 41.5 | 41.0 | 32.8 |
|  | 60.2 | 51.8 | 51.9 | 51.2 | 40.9 | 40.2 | 39.8 |
|  | 56.6 | 58.7 | 48.7 | 49.3 | 49.2 | 36.9 | 36.4 |
|  | 59.9 | 50.1 | 52.0 | 53.5 | 41.1 | 41.6 | 41.5 |
|  | 59.9 | 50.2 | 51.9 | 53.4 | 41.2 | 41.7 | 41.9 |
| $F_{2}(\mathrm{ml})$ | 53.0 | 47.2 | 45.3 | 40.2 | 39.8 | 33.0 | 32.8 |
| Throttle | 40\% | 40\% | 30\% | 50\% | 50\% | 50\% | 50\% |
| $F_{1}(\mathrm{ml})$ | 7.1 | 8.5 | 9.3 | 10.1 | 11.0 | 12.7 | 13.8 |
| Tot. Fuel (ml) | 60.1 | 55.7 | 54.6 | 50.4 | 50.8 | 45.7 | 46.6 |


Figure 3 shows a comparison of fuel consumed when these seven speed profile is followed and clearly, gradual deceleration resulted in a lower upstream fuel, however caused higher fuel on the downstream of intersection. Figure 4 shows the speed-time profile of the seven cases considered. Contrary to previous research efforts, the fueloptimal speed profile is neither the one with minimum
deceleration or acceleration, nor the one with minimum length of acceleration or deceleration. Case 6 is the most fuel optimal speed profile.

## V. Conclusions

There has been a handful of research on minimizing the fuel consumption of vehicles using traffic signal status information being available to drivers. However, most models previously developed use constrained optimization algorithms which use simpler objective functions such as minimizing the deceleration level, the time spent decelerating or idling or even maximizing the probability of encountering a green indication. None of the models have been identified to use an explicit objective function to minimize the total fuel consumed in passing an intersection safely. This research mainly focused on developing a strategy which yields the most fuel-optimal speed profile for a vehicle approaching a signalized intersection using V2I communication capabilities. It also showed that simplifying the objective function as well as not explicitly using the fuel consumption in the objective function can lead to erroneous results.

![](https://cdn.mathpix.com/cropped/cee5aff5-9974-4647-bb76-ff10c3830ecb-6.jpg?height=421&width=814&top_left_y=1121&top_left_x=191)
FIGURE 3 - Fuel consumed in ml for the entire maneuver in seven cases for an ORNL composite vehicle

![](https://cdn.mathpix.com/cropped/cee5aff5-9974-4647-bb76-ff10c3830ecb-6.jpg?height=479&width=849&top_left_y=1603&top_left_x=187)
Figure 4: Speed-time relation for all seven cases considered

## VI. References

1. EPA, 2010 U.S. Greenhouse Gas Inventory Report, 2010: Washington D.C.
2. Davis, S.C., S.W. Diegel, and R.G. Boundy, Transportation Energy Data Book, in US Department of Energy2010: Oak Ridge, TN. p. 385.
3. TTI, Annual Urban Mobility Report 2009, in Texas Transportation Institute, Texas A\&M University2009.
4. USDOT, Achieving the Vision: From VII to IntelliDrive. Research and Innovative Technology Administration, 2010.
5. USDOT, IntelliDrive(SM) Governance Needs Summary, in Research and Innovative Technology Administration2009: Washington D.C. p. 1-24.
6. Ahn, K., et al., Estimating vehicle fuel consumption and emissions based on instantaneous speed and acceleration levels. Journal of Transportation Engineering, 2002.
7. Rakha, H.A., et al. Simple Vehicle Driveline Model for Estimation of Vehicle Fuel Consumption Levels. in 90th Transportation Research Board Annual Meeting. 2011. Washington D.C.
8. Rakha, H., et al. Simple Comprehensive Fuel Consumption and CO2 Emission Model based on Instantaneous Vehicle Power. in 90th Transportation Research Board Annual Meeting. 2011. Washington D.C.
9. Barth, M., et al., Modal emissions modeling: a physical approach. Transportation Research Record: Journal of the Transportation Research Board, 1996. No. 1520: p. 81-88.
10. Rakha, H., M. Snare, and F. Dion, Vehicle dynamics model for estimating maximum light-duty vehicle acceleration levels. Transportation Research Record: Journal of the Transportation Research Board, 2004. 1883: p. 40-49.
11. Bandivadekar, A., et al., On the road in 2035: Reducing transportation's petroleum consumption and GHG emissions, 2008. p. 196.
12. Brookhuis, K. and D. Dewaard, Limiting speed, towards an intelligent speed adapter (ISA). Transportation Research Part F: Traffic Psychology and Behaviour, 1999. 2: p. 81-90.
13. Roozemond, D.A., Using intelligent agents for pro-active, real-time urban intersection control. European Journal of Operational Research, 2001. 131: p. 293-301.
14. Iglesias, I., et al. I2V Communication Driving Assistance System: On-Board Traffic Light Assistant. in Vehicular Technology Conference, 2008. VTC 2008-Fall. IEEE 68th. 2008. IEEE.
15. Boriboonsomsin, K., O. Servin, and M. Barth, Selection of control speeds in dynamic intelligent speed adaptation system: A preliminary analysis. EScholarship, 2008.
16. Johansson, H., P. Gustafsson, and M. Henke, Impact of EcoDriving on emissions. Transport and Air Pollution., 2003.
17. Ericsson, E., H. Larsson, and K. Brundellfreij, Optimizing route choice for lowest fuel consumption - Potential effects of a new driver support tool. Transportation Research Part C: Emerging Technologies, 2006. 14: p. 369-383.
18. Barth, M. and K. Boriboonsomsin, Energy and emissions impacts of a freeway-based dynamic eco-driving system. Transportation Research Part D: Transport and Environment, 2009. 14: p. 400-410.
19. Widodo, S., T. Hasegawa, and S. Tsugawa. Vehicle fuel consumption and emission estimation in environment-adaptive driving with or without inter-vehicle communications. in Proceedings of the IEEE Intelligent Vehicles Symposium 2000 (Cat. No.00TH8511). 2002. Ieee.
20. USDOT, Connected Vehicle, 2011.
21. Connected Vehicle Research, in Research and Innovative Technology Administration22010.
22. Wu, G., et al., Energy and Emission Benefit Comparison of Stationary and In-Vehicle Advanced Driving Alert Systems. Transportation Research Record: Journal of the Transportation Research Board, 2010. 2189: p. 98-106.
23. Asadi, B. and A. Vahidi, Predictive Cruise Control: Utilizing Upcoming Traffic Signal Information for Improving Fuel Economy and Reducing Trip Time. Control Systems Technology, IEEE Transactions, 2010: p. 1-9.
24. Tielert, T., et al. The impact of traffic-light-to-vehicle communication on fuel consumption and emissions. in Internet of Things (IOT), 2010. 2010. IEEE.
25. Malakorn, K.J. and B. Park. Assessment of mobility, energy, and environment impacts of IntelliDrive-based Cooperative Adaptive Cruise Control and Intelligent Traffic Signal control. in Sustainable Systems and Technology (ISSST), 2010 IEEE International Symposium. 2010. IEEE.
26. Mandava, S., K. Boriboonsomsin, and M. Barth. Arterial velocity planning based on traffic signal information under light traffic conditions. in Intelligent Transportation Systems, 2009. ITSC'09. 12th International IEEE Conference on Intelligent Transportation Systems. 2009. IEEE.
27. Green Wave Optimization with Genetic Algorithms and Car-to-Infrastructure Communication: Ingolstadt.

[^0]:    Manuscript received May 15, 2011 and updated on July 27, 2011. This work was done by the Center for Sustainable Mobility at Virginia Tech Transportation Institute and was funded by the Federal Highway Administration under contract DTFH61-10-P-00172.

    Hesham Rakha (corresponding author) is a Professor with the Charles E Via, Jr. Department of Civil and Environmental Engineering and the Director of the Center for Sustainable Mobility, Virginia Polytechnic Institute and State University, Blacksburg, Virginia, 24061 USA (Ph: 540-231-1505, email: hrakha@vtti.vt.edu).

    Raj Kishore Kamalanathsharma is a PhD Student in the Civil and Environmental Engineering Department, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061 USA (e-mail: rkishore@vt.edu).

