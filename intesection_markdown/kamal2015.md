# A Vehicle-Intersection Coordination Scheme for Smooth Flows of Traffic Without Using Traffic Lights 

Md. Abdus Samad Kamal, Member, IEEE, Jun-ichi Imura, Member, IEEE, Tomohisa Hayakawa, Member, IEEE, Akira Ohata, and Kazuyuki Aihara


#### Abstract

This paper presents a coordination scheme of automated vehicles at an intersection without using any traffic lights. Using a two-way communication network, vehicles approaching the intersection from all sections are globally coordinated, by considering their states all together in a model predictive control framework, in order to achieve smooth traffic flows at the intersection. The optimal trajectories of the vehicles are computed based on avoidance of their cross-collision risks around the intersection under relevant constraints and preferences. The scheme efficiently utilizes the intersection area by preventing each pair of conflicting vehicles from approaching their cross-collision point at the same time, instead of reserving the whole intersection area for the conflicting vehicles one after another. The scheme also enables leftor right-turning movements of vehicles under constrained velocity without using any auxiliary lanes. The proposed vehicle-intersection coordination scheme is evaluated through numerical simulation in a typical test intersection consisting of both multilanes and single-lane approaches with turning movements of vehicles. Observations under different traffic flow conditions reveal that the proposed scheme significantly improves intersection performance compared with the traditional signalized intersection scheme.


Index Terms-Automated vehicles, connected vehicles, intelligent transportation systems, intersection coordination, model predictive control (MPC).

## I. Introduction

TRAFFIC congestion in urban road networks wastes a massive amount of time and fuel, and the overall cost due to traffic congestion is increasing every year [1]. Traffic congestion often occurs when traffic density becomes higher than the capacity of a road network. Efficient use of the existing road

[^0]networks by innovative intersection management and control is a remaining option for the cities where further construction and expansion of roads are difficult. In the traditional traffic control paradigm, traffic flows at intersections are regulated by traffic lights or signs that restrict the maximum traffic handling capacity of the intersections and increase inconveniences of frequent stops and idling. The intersections with light traffic are usually operated by yield-stop traffic signs or by forming a roundabout. A vehicle at a yield sign only has to stop if it is necessary to let a vehicle on another approach have the rightof-way first. In contrast, vehicles at a stop sign must come to a complete stop before crossing, even if no other vehicle is present. In a similar way but without any traffic sign, traffic entering the roundabout must yield to traffic already in the circle. At busy intersections, flows of vehicles on each approach are usually regulated by green and red lights that eventually increase the stop delay.

Among the various solutions to alleviate traffic congestion, traffic-light or signal control is commonly considered as the most effective method, and various strategies for urban traffic management have been developed [2]-[4]. These signal control strategies can only partially improve the traffic flow if all approaches to the intersection are not equally congested, and they cannot eliminate the stop delay of vehicles at intersections regardless of traffic volume. Considering increasing trends of vehicles and sustainability of the road transportation, a breakthrough in the intersection control paradigm, which may eliminate the necessity of stop and increase the capacity of intersections, is highly expected.

Semiautomated vehicles are already emerging in the market, and it is expected that fully automated vehicles will be widely used in the near future considering the advancement in sensor technology and adoption of communication technology. Connected vehicles environment provides a two-way wireless communication enabling vehicle-to-vehicle (V2V) and vehicleto-infrastructure communications [5]. Using V2V communication, cooperative adaptive cruise control (CACC) systems can safely drive vehicles with very short headway by forming platoons to improve traffic-flow capacity of a road [6], [7]. The concept of following a vehicle with a short gap in CACC can be extended to offer a new intersection control paradigm, in which nearly conflicting vehicles from different approaches can cross the intersection keeping marginal gaps without using any traffic signal. Such an intersection control paradigm would unleash the full potential of automated vehicles in mostly eliminating stop delay, reducing travel time, and increasing the capacity of an intersection.

A few studies on innovative intersection management have been found in the literature that attempt to control vehicles without using traffic signals. Raravi et al. [8] proposed an automatic merge control system for intelligent vehicles under a cooperative vehicle-infrastructure environment that ensures safe vehicle maneuvering at road intersections. By formulating an optimization problem with constraints to guarantee safety, the optimal maneuvers for merging vehicles were obtained by minimizing the maximum of driving time to intersection for every vehicle coming from two conflicting approaches. Uno et al. [9] also studied the merge control application based on V2V communication under the concept of virtual vehicles that is used to map vehicles on one lane onto the other lane for ensuring safe distance criteria. These merge control systems, however, are not suitable for intersections since complex movements of vehicles to and from various lanes are involved.

Dresner and Stone [10] presented an idea of autonomous intersection management (AIM) as an alternative to the traditional traffic signal control mechanism. In AIM, vehicles and intersections are treated as autonomous agents in a multiagent system. The intersection is divided into a number of cells, and an intersection manager program coordinates the reservation requests of temporal cell occupancies from every vehicle and offers right-of-way for each vehicle for ensuring safe crossing. However, this method does not coordinate the vehicles globally for their optimal flow and therefore stop delay cannot be avoided sometimes. Omae et al. [11] proposed a virtual platooning method for automatic vehicle control at an intersection for passing through without stopping. Vehicles on all lanes are considered on a virtual lane, and considering their interference at the intersection, they are independently controlled to safely follow the preceding vehicle in the platoon. The method is experimented at an intersection of one-way traffic using four electric vehicles equipped with automatic driving and V2V communication technologies.

Recently, a cooperative vehicle intersection control (CVIC) system has been proposed that enables cooperation between automated vehicles and infrastructure for effective intersection operations [12]. The CVIC algorithm is based on minimizing the overlaps of trajectories of conflicting vehicles at the intersection. More specifically, this system simply tries to avoid the presence of any pair of conflicting vehicles in the intersection area at the same time. The trajectory of each vehicle is generated by fixing an acceleration rate from its current position to the end of the intersection. Therefore, the natural dynamic behavior of a vehicle is ignored in the prediction horizon. Moreover, CVIC keeps the optimization problem simple without including any constraints for cross-collision avoidance, and minimization of the overlapping trajectories does not guarantee a feasible collision-free solution. Hence, an additional algorithm, in the form of priority rules for some lanes, is required to deal with the system failure resulting from infeasible solutions.

This paper proposes a vehicle-intersection coordination scheme (VICS) without using any traffic lights under a connected vehicles environment that overcomes the limitations of the existing methods. The conference paper [13] is a concise and preliminary version of this paper. The novelty of the proposed scheme is the global coordination, by considering the states of all vehicles together, based on avoidance of their crosscollision risks at the intersection. The scheme efficiently utilizes the intersection area by preventing each pair of conflicting vehicles from approaching their cross-collision point (CCP) at the same time, instead of reserving the whole intersection area for the conflicting vehicles successively. Moreover, the introduction of relevant constraints ensures the scheme free from any collisions and enables to manage turning movements of the vehicles under a safe velocity limit. Turning vehicles sometimes need special treatment so that multiple vehicles slowly and closely cross the intersection, which is realized in the VICS. An intersection coordination unit (ICU), which is assumed to be installed at the intersection, uses two-way communication to receive basic driving information from the approaching vehicles, e.g., current position, velocity, and destination at the next intersection and sends guidance to them after computing their control inputs.

In this scheme, a risk function is proposed that explicitly indicates only a portion of the intersection by quantifying the risk of a collision of a pair of vehicles around their CCP. More specifically, at any time, if two conflicting vehicles are very close to their CCP, the risk function returns a high value, and if at least one vehicle is far from the CCP, it returns a negligible value. Considering states of all vehicles, a constrained nonlinear optimization problem is solved in a model predictive control (MPC) framework in order to let the vehicles cross the intersection rapidly by minimizing the total quantified risks of all vehicle pairs. Minimization of risks helps generating safe trajectories of vehicles by reducing unused time and space in the intersection area and, consequently, enhances the traffic handling capacity of the intersection and improves traffic flows. Thus, the scheme integrates fully automated vehicles in a fully automated intersection to improve traffic operations. The proposed VICS has been evaluated through numerical simulation, and its performance is compared with the traditional signalized scheme. In various traffic-flow conditions, it is observed that the stop delay of vehicles at the intersection is almost eliminated, and flows of vehicles and the capacity of the intersection are significantly improved.

The rest of this paper is organized as follows. Section II describes the proposed VICS, including analysis of expected capacity improvement of an intersection, assumptions related to the intersection operation, state equations, risk functions, constraints, and formulation of a constrained nonlinear optimization problem in the MPC framework. Section III describes the details about numerical simulation, flowing behavior of individual vehicles, and overall performance of the proposed scheme, including comparison with the traditional signalized intersection scheme (SIS) observed in the Aimsun microscopic traffic simulator. Section IV discusses the proposed scheme and obtained results. Finally, Section V provides the conclusions.

## II. VICS

Traffic-flow patterns in an intersection depend on its geometry, area and allowable movements to and from its various lanes. Possible interference of vehicles in the intersection area needs to be analyzed for classifying their movements in some

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-03.jpg?height=954&width=864&top_left_y=241&top_left_x=133)
Fig. 1. Typical intersection used for developing and evaluating the proposed VICS, in which an ICU coordinates the vehicles. The straight and flat roads intersect at a right angle. The vehicles are allowed to turn as specified by the markers.

phases or groups and designing a control scheme. In this paper, a typical intersection shown in Fig. 1 is studied, in which the flat and straight roads cross at a right angle, and a coordination scheme is developed for the safe crossing of vehicles without using traffic lights. Specifically, it is assumed that traffic keeps to the left side on the roads, according to the convention in Japan. Two of the four approach sections and their extensions beyond the intersection have double lanes, and the other sections have single lanes. For simplicity, six approaching lanes to the intersection are numbered by letters A to F, and the white arrow marks on each lane indicate the allowable turning phases in the intersection. Specifically, vehicles are allowed to make a left or a right turn without using any auxiliary lanes from A and B, whereas the right turn is not allowed from C and E, and the left turn is not allowed from D and F. In the traditional control, the traffic flows of this intersection need to be grouped into at least two signal phases, and if the right-turning traffic is heavy then four signal phases are required.

In order to formulate the coordination scheme, some variables and parameters are defined as follows.

1) $l$ : lane identifier. Here, the lanes are numbered by letters A to F.
2) $d \in\{0,1,2\}$ : turning indication of vehicles at the intersection as straight, left, or right, respectively.
3) $\eta_{d}^{l} \in[0,1]$ : fraction of turning traffic coming over lane $l$ that turns into $d$ at the intersection.
4) $n$ : vehicle identifier within a lane.
5) $l_{v}$ : length of a vehicle in meters.
6) $b$ : width of a lane in meters. For simplicity, all lanes are assumed to have the same width. The inner area of the given intersection is $4 b \times 2 b$.
7) $a$ : minimum clearance from the intersection when it is occupied by other conflicting vehicles.
8) $V_{d}$ : desired velocity for crossing the intersection straightaway.
9) $V_{t}$ : maximum velocity of a turning vehicle inside the intersection.
10) $x_{n}^{l}$ : position of a vehicle $n$ on a lane $l$ that defines remaining distance from the center point of the vehicle to the beginning of the intersection. Note that on lane $l$, the vehicle $n$ is closer to the intersection than vehicle $n+1$, i.e., $x_{n}^{l}<x_{n+1}^{l}$ (see Fig. 1).
11) $v_{n}^{l}$ : velocity of a vehicle.
12) $u_{n}^{l}$ : control input of the vehicle in terms of acceleration. If its magnitude is negative, then it implies deceleration.
13) $t$ : time step counter.
14) $\tau$ : duration of the unit time step.

## A. Impact on the Intersection Capacity

This section studies the expected impact on the traffic-flow capacity or throughput of a coordinated intersection, in terms of vehicles per hour per lane. The traffic-flow capacity depends on many factors, and it is difficult to figure it out exactly in advance. In the case of traditional signalized intersections, the capacity depends on the saturation flow rate and the effective green time. Studies [14], [15] show that the saturation flow rates at signalized intersections vary widely but mostly lie in the range of 1700-1900 veh/h. Due to lost times associated with a change in signals at an intersection, the operating time, which is also known as the effective green time of a lane, is less than its actual green time. A typical value of lost time is about 4 s per change in signal [14]. For the given intersection, the flows from lanes can be divided into two groups considering the conflicting movements of vehicles, e.g., lanes A and B in Group 1, and lanes C to F in Group 2. Therefore, the actual capacity of a signalized intersection will be less than the half of its saturation flow rate (considering equally dense traffic on all lanes and 50\% green time for each signal phase). For example, in a 90-s cycle of traffic signal, the capacity can be in the range of 775-865 veh/h, considering the aforementioned saturation flow rates.

Here, the capacity of a coordinated intersection is investigated only for an indicative purpose in the case of equally dense traffic in all lanes. For simplicity, it is assumed that all vehicles have identical shape and they cross the intersection at the specified velocity in very ideal conditions.

Since all lanes are equally dense as assumed, vehicles from Group 1 and Group 2 need to cross the intersection alternatively by keeping a safe margin. For example, when vehicles from lanes A and B complete crossing the intersection, the vehicles from lanes C to F are allowed to enter into the intersection for crossing, and vice versa. It is assumed that the conflicts within a group due to right-turning vehicles can be overcome by adjusting their crossing velocities. Fig. 2 illustrates the paths that the vehicles need to follow for crossing the intersection area from both groups for different turning movements. For computational simplicity, it is assumed that each curved path has the same length with that shown by the dashed line. The parameters

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-04.jpg?height=724&width=595&top_left_y=238&top_left_x=286)
Fig. 2. Path of vehicles for various movements are shown by the thick gray curves, and the length of each path is approximated according to the dashed line.

$R_{0}, R_{1}$, and $R_{2}$ express the approximate lengths of the path that a vehicle from lane A has to pass over for crossing straightaway, turning left, and turning right, respectively. The corresponding paths from lane B are symmetric. Similarly, $R_{0}^{\prime}, R_{1}^{\prime}$, and $R_{2}^{\prime}$ express the same for the other lane group as illustrated. With the given width $b$ of the lanes, i.e., vehicle length $l_{v}$ and safe margin $a$, the lengths of these paths can be estimated as

$$
\begin{aligned}
& R_{0}=l_{v}+2 a+4 b \\
& R_{1}=l_{v}+2 a+1 / \sqrt{2} b \\
& R_{2}=l_{v}+2 a+3 / \sqrt{2} b \\
& R_{0}^{\prime}=l_{v}+2 a+2 b \\
& R_{1}^{\prime}=l_{v}+2 a+1 / \sqrt{2} b \\
& R_{2}^{\prime}=l_{v}+2 a+(1+\sqrt{5}) b
\end{aligned}
$$

It is assumed that the vehicles arrive at the intersection periodically in such a way that they cross straightaway at the specified velocity $V_{d}$, or turn left or right at a limited velocity $V_{t}$. The corresponding time to cross the intersection by a vehicle can be obtained as

$$
\begin{aligned}
& t_{0}=\frac{R_{0}}{V_{d}} \\
& t_{1}=\frac{R_{1}}{V_{t}} \\
& t_{2}=\frac{R_{2}}{V_{t}} \\
& t_{0}^{\prime}=\frac{R_{0}^{\prime}}{V_{d}} \\
& t_{1}^{\prime}=\frac{R_{1}^{\prime}}{V_{t}} \\
& t_{2}^{\prime}=\frac{R_{2}^{\prime}}{V_{t}} .
\end{aligned}
$$

Therefore, time required to completely clear the intersection depends on turning movements within the same group of lanes. For example, from lanes A and B, if both vehicles cross straightaway, it takes time $t_{0}$ to clear the intersection; if one turns left and the other moves straightaway, then it takes time $\max \left\{t_{0}, t_{1}\right\}$; if one turns right and the other turns left, then it takes time $\max \left\{t_{1}, t_{2}\right\}$. Similarly, the time required to clear the intersection for the other group can be obtained by the movements from lanes C to F. With reasonable values of $V_{d}$ and $V_{t}$, it is expected that $t_{0}<t_{1}<t_{2}$ and $t_{0}^{\prime}<t_{1}^{\prime}<t_{2}^{\prime}$. Based on these presumptions and the given rates $\eta_{d}^{l}$ of turning movements from all lanes, the average clearing times and their probabilities can be analytically obtained. Probabilities of the various movements and corresponding clearing time of the intersection by the group of vehicles from lanes A and B can be obtained as follows.

1) With probability $p_{0}=\eta_{0}^{\mathrm{A}} \eta_{0}^{\mathrm{B}}$, both vehicles from lanes A and B cross straightaway in clearing time $t_{0}$.
2) With probability $p_{1}=\eta_{1}^{\mathrm{A}} \eta_{0}^{\mathrm{B}}+\eta_{0}^{\mathrm{A}} \eta_{1}^{\mathrm{B}}+\eta_{1}^{\mathrm{A}} \eta_{1}^{\mathrm{B}}$, at least one vehicle turns left and the other does not turn right that requires clearing time of $t_{1}$.
3) With probability $p_{2}=\eta_{2}^{\mathrm{A}}\left(1-\eta_{2}^{\mathrm{B}}\right)+\left(1-\eta_{2}^{\mathrm{A}}\right) \eta_{2}^{\mathrm{B}}+$ $\eta_{2}^{\mathrm{A}} \eta_{2}^{\mathrm{B}}$, at least one vehicle turns right from either lane that requires a clearing time of $t_{2}$.

Note that $p_{0}+p_{1}+p_{2}=1$. Therefore, the average clearing time per crossing required by traffic from lanes A and B can be estimated as

$$
t_{c}=p_{0} t_{0}+p_{1} t_{1}+p_{2} t_{2} .
$$

Similarly, for the group of lanes C to F, probabilities can be obtained as follows.

1) With probability $p_{0}^{\prime}=\eta_{0}^{\mathrm{C}} \eta_{0}^{\mathrm{D}} \eta_{0}^{\mathrm{E}} \eta_{0}^{\mathrm{F}}$, all vehicles from lanes C to F cross straightaway in clearing time of $t_{0}^{\prime}$.
2) With probability $p_{1}^{\prime}=\eta_{0}^{\mathrm{D}} \eta_{0}^{\mathrm{F}}\left(\eta_{1}^{\mathrm{C}} \eta_{0}^{\mathrm{E}}+\eta_{0}^{\mathrm{C}} \eta_{1}^{\mathrm{E}}+\eta_{1}^{\mathrm{C}} \eta_{1}^{\mathrm{E}}\right)$, at least one vehicle turns left, whereas there is no rightturning vehicles, and they require a clearing time of $t_{1}^{\prime}$.
3) With probability $p_{2}^{\prime}=\eta_{2}^{\mathrm{D}}\left(1-\eta_{2}^{\mathrm{F}}\right)+\left(1-\eta_{2}^{\mathrm{D}}\right) \eta_{2}^{\mathrm{F}}+$ $\eta_{2}^{\mathrm{D}} \eta_{2}^{\mathrm{F}}$, at least one vehicle turns right from lane D and F and require clearing time of $t_{2}^{\prime}$.

Since $p_{0}^{\prime}+p_{1}^{\prime}+p_{2}^{\prime}=1$, the average clearing time per crossing required by traffic from lanes C to F can be estimated as

$$
t_{\mathrm{c}}^{\prime}=p_{0}^{\prime} t_{0}^{\prime}+p_{1}^{\prime} t_{1}^{\prime}+p_{2}^{\prime} t_{2} .
$$

In the case where vehicles from one group arrive exactly when the vehicles of the other group have crossed the intersection in a periodic way, the maximum capacity of the coordinated intersection in terms of vehicles per hour per lane can be estimated as

$$
c_{l}=\frac{3600}{\left(t_{c}+t_{c}^{\prime}\right)} .
$$

For a particular type of vehicles, the capacity depends on parameter $a$ that denotes the minimum safe gap as illustrated in Fig. 2. Considering typical values of the parameters $l_{v}=$ $5 \mathrm{~m}, b=3 \mathrm{~m}, a=2 \mathrm{~m}$, and $V_{d}=16.67 \mathrm{~m} / \mathrm{s}(60 \mathrm{~km} / \mathrm{h})$, the
straight crossing times can be obtained as $t_{c}=1.26 \mathrm{~s}$ and $t_{c}^{\prime}=0.9 \mathrm{~s}$. For the case where there is no turning vehicle, the lane capacity given by (5) is equal to 1667 veh/h, which is much higher than the capacity (e.g., 865 veh/h) achievable from a traditional signalized intersection. Similarly, capacity can be also estimated for mixed turning traffic if their rates $\eta_{d}^{l}$ is known. The aforementioned estimation is valid if vehicles arrive at the intersection exactly at the specified velocity and time successively from each group of lanes. However, in real traffic, sometimes vehicles from the conflicting lanes may approach the intersection almost at the same time, and consequently, they may require additional time for crossing the intersection, i.e., the actual capacity of the intersection can slightly differ from the estimated value. Nevertheless, such coordination of vehicle intersection has the potential of improving traffic flows significantly.

## B. Coordination Problem and Assumptions

It is assumed that all automated identical vehicles crossing the intersection can be manipulated by an ICU equipped at the intersection through two-way communication using the standard communication protocol as defined in Wireless Access in Vehicular Environments Short Range Communications standards [5], [16]. It is assumed that under such connected vehicles environment, every vehicle transmits its basic driving information, including current position, velocity and destination at the intersection, and the ICU transmits the corresponding guidance to each vehicle with negligible delay. Only the longitudinal motion of the vehicles is controlled, assuming the vehicles perfectly follow the lateral trajectories. The turning paths do not have very sharp bends so that a vehicle can move smoothly at a reasonably high velocity with sufficient lateral acceleration, instead of coming close to a complete stop and causing interruption in traffic flows at the intersection. Vehicles approach the intersection using their independent driving systems, and they are allowed to change their lane if there are sufficient space and necessity. Only a few leading vehicles on each lane need to be globally coordinated by optimizing the trajectories of the set of vehicles in question without considering lane changing option on the road as they are already close to the intersection. Once a vehicle crosses the intersection, its control is transferred to its independent driving system, and a new set of vehicles are coordinated for crossing the intersection in a successive approach.

It is assumed that a total of $N=6 M$ vehicles, taking $M$ vehicles from each lane, are coordinated at a time by the ICU. The vector $x=\left[x_{1}^{\mathrm{A}}, \ldots, x_{M}^{\mathrm{A}}, \ldots, x_{1}^{\mathrm{F}}, \ldots, x_{M}^{\mathrm{F}}\right]^{T} \in \mathbb{R}^{N}$ is defined to denote the position (distance from the intersection) of $N$ vehicles of lanes A to F. Similarly, vectors $v \in$ $\mathbb{R}^{N}$ and $u \in \mathbb{R}^{N}$ denote the velocity and acceleration of the same set of vehicles of lanes A to F. The discrete-time state equations describing the longitudinal motion of vehicle $i$ are given by

$$
\begin{aligned}
x_{i}(t+1) & =x_{i}(t)-v_{i}(t) \tau-\frac{1}{2} u_{i}(t) \tau^{2} \\
v_{i}(t+1) & =v_{i}(t)+u_{i}(t) \tau
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-05.jpg?height=655&width=821&top_left_y=238&top_left_x=1070)
Fig. 3. Illustration of the collision avoidance concept around a CCP: (a) safe situation and (b) unsafe situation.

The intersection crossing phase $\phi_{i}$ of each vehicle is defined by its lane number and its turning status, e.g., $\phi_{i}=\mathrm{A} 2$ implies vehicle $i$ is going to turn right from lane A.

## C. CCP and Risk Function

The concept of collision avoidance in the intersection area is illustrated in Fig. 3 using the positions and paths of two vehicles $i$ and $j$ from lanes A and E that cross the intersection straightaway, i.e., $\phi_{i}=\mathrm{A} 0$ and $\phi_{j}=\mathrm{E} 0$. Their paths intersect at a particular point in the intersection area at which they have a potential risk of collision, and this point is named as CCP in this paper. The distances of the point in the intersection area are $b / 2$ and $3 b / 2$ from the end of lanes A and E, respectively. The circle (or ellipse if the lengths of vehicles are not the same) centering the CCP shows an approximate area or zone where two vehicles are not allowed to enter at the same time for avoiding any collision. However, they can enter and leave this zone one after another. Fig. 3(a) shows that both vehicles are in the intersection area but they are safe, since the vehicle from lane A has already left the zone, whereas the vehicle from lane E approaches it. Fig. 3(b) shows the opposite case with a risk of collision, although both the vehicles (their center points) are just at the outside of the intersection. It is understood that the necessary condition for avoiding the collision of any pair of vehicles around their corresponding CCP is to prevent them from entering the zone at the same time. Considering the paths of vehicles from various lanes for various movements, crossing points or CCPs for all pairs of vehicles are not the same.

Collision can be also avoided if a pair of vehicles from conflicting sections can be prevented from entering the whole intersection area at the same time, e.g., vehicle $i$ is only allowed to enter the intersection when vehicle $j$ left the intersection completely, or vice versa. This way, the whole intersection area can be reserved for each group of vehicles successively as explained in the capacity estimation of the intersection in Section II-A. However, reserving the whole intersection area for a vehicle to avoid collision with the other would reduce the performance of the intersection significantly.

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-06.jpg?height=971&width=593&top_left_y=241&top_left_x=288)
Fig. 4. Specified path of vehicles for crossing the intersection and their possible CCPs in the intersection area. The curves marked by $d=0,1$ or 2 with the lane number denote the approximate path of vehicles for going straight, turning left, or turning right, respectively.

Based on the concept of CCPs, a risk indicator $\mathcal{R}_{i, j}(t)$ is proposed to quantitatively indicate whether the vehicle pair $i, j$ poses a potential risk of collision around their CCP at time $t$, which is given by

$$
\mathcal{R}_{i, j}(t)=e^{-\left(\alpha_{i}\left(x_{i}(t)+p_{\phi_{i} \phi_{j}}\right)^{2}+\alpha_{j}\left(x_{j}(t)+p_{\phi_{j} \phi_{i}}\right)^{2}\right)}
$$

where $\alpha_{i}$ and $\alpha_{j}$ are positive constants, and $p_{\phi_{i} \phi_{j}}$ and $p_{\phi_{j} \phi_{i}}$ are the distances of the CCP from the ends of lanes $l_{i}$ and $l_{j}$, respectively. For example, in the case shown in Fig. 3, $p_{\phi_{i} \phi_{j}}=$ $b / 2$ and $p_{\phi_{j} \phi_{i}}=3 b / 2$. The risk indicator is a 2-D Gaussian function, and $\alpha_{i}$ and $\alpha_{j}$ are related to its shape (or the area under high risk). By adjusting $\alpha_{i}$ and $\alpha_{j}$, area of risk for small to large vehicles can be tuned. Risk indicator $\mathcal{R}_{i, j}(t) \approx 1$ at $t$ implies a potential collision, if both vehicles $i$ and $j$ are at their CCP, and a negligible risk of collision, $\mathcal{R}_{i, j}(t) \approx 0$, if one or both of them are far from their CCP.

The aforementioned example of a risk indicator needs to be generalized for all possible pairs of vehicles at their respective CCPs. Since the paths of all possible pairs from $N$ vehicles do not cross in the intersection, it is necessary to map their CCPs considering their turning movements or phases. For the given intersection, the approximate paths of vehicles from all lanes are illustrated in Fig. 4. The CCPs are marked by the red circles in the figure. In the intersection, there are 12 CCPs for straight and turning movements of vehicles from various lanes. Conflicts at CCPs are shown by the paths of straight going and turning vehicles on them. A binary variable $\delta_{\phi_{i}, \phi_{j}}$ is introduced to state whether the vehicles $i$ and $j$ have a CCP, i.e., whether their paths cross in the intersection area. If they have a CCP, then $\delta_{\phi_{i}, \phi_{j}}=1$; otherwise, its value is set to 0 .

Using the risk indicator (7), a risk function $\mathcal{F}_{i, j}(t)$ is defined to quantitatively indicate whether any pair of vehicles $i$ and $j$ poses a potential risk of collision at their CCP at time $t$ given by

$$
\mathcal{F}_{i, j}(t)=H \delta_{\phi_{i}, \phi_{j}} e^{-\left(\alpha_{i}\left(x_{i}(t)+p_{\phi_{i} \phi_{j}}\right)^{2}+\alpha_{j}\left(x_{j}(t)+p_{\phi_{j} \phi_{i}}\right)^{2}\right)}
$$

where $H$ is a positive constant indicating the highest possible risk of collision. At any time, there can be a few active CCPs depending on the vehicle movements in the intersection area from all lanes. For their collision-free crossing, all trajectories should be adjusted in such a way that the sum of risks from all pairs of vehicles is negligible. The next section describes the formulation of an optimization problem using this risk function in an MPC framework for the proposed VICS.

## D. MPC

In the MPC framework, at each time step, a constrained nonlinear optimization problem is solved over a finite horizon to derive the optimal control sequences of the vehicles undertaken for coordination. For a safe flow of the vehicles both on the sections and intersections, several constraints are incorporated. Specifically, linear inequalities

$$
\begin{aligned}
& v_{i} \leq v_{\text {max }} \\
& v_{i} \geq v_{\text {min }} \\
& u_{i} \leq u_{\text {max }} \\
& u_{i} \geq u_{\text {min }}
\end{aligned}
$$

are defined that are related to the velocity and acceleration limits of the vehicles. Although the maximum possible acceleration depends on the current velocity of the vehicle, for simplicity in this study, constant magnitudes are considered as the limits. The minimum separation between two consecutive vehicles on the same lane, i.e., for $l_{i}=l_{i+1}$, is linearly constrained to avoid any rear ends collision, which is given by

$$
x_{i+1}-x_{i} \geq r_{\min }
$$

where $r_{\text {min }}$ is the sum of vehicle length and minimum allowable gap.

Some vehicles may turn left or right at the intersection, and it is essential that they can generate sufficient lateral acceleration to safely navigate the turning curve. The lateral acceleration required at a turning path depends on the friction between the vehicle's tires and the road, which can be also given by

$$
a_{c}=\frac{v^{2}}{R_{c}}
$$

where $R_{c}$ is the minimum radius of the curved path and $v_{c}$ is the velocity along the curve. If radii of turning curvatures are large, vehicles can turn at higher velocities and can more efficiently merge with the cross-street traffic [17], [18]. Considering the limiting factor in generating proper lateral acceleration, intersection design manual specifies the safe turning velocity versus the radius of curvature [18]. Based on the presumption that
the radius of the turning path is fixed and the corresponding safe maximum velocity is obtained from the intersection design manual, a nonlinear inequality constraint is introduced to ensure sufficient lateral acceleration of the turning vehicle $i$ with $d_{i} \neq 0$ as

$$
v_{i} \leq V_{a}\left(1-e^{-\beta\left(x_{i}+c_{l_{i}}\right)^{2}}\right)+V_{b}
$$

where $\beta$ is a constant, $\operatorname{and} c_{l_{i}}$ is the distance between the beginning and the center of the intersection. Positive constants $V_{a}$ and $V_{b}\left(\leq v_{c}\right)$ are set at some high values so that $V_{a}+V_{b}$ is much higher than the desired velocity of the vehicles. The nonlinear constraint (12) implies that at $x_{i}+c_{l_{i}}=0$ (at the center of the intersection), the constraint becomes $v_{i} \leq V_{b}$, and at $\left|x_{i}+c_{l_{i}}\right| \gg 0$ (the vehicle is very far from the intersection) the constraint becomes $v_{i} \leq V_{a}+V_{b}$. For ensuring no collision between a pair of vehicles with different crossing phases in the intersection, a nonlinear inequality constraint is defined as

$$
\left(x_{i}(t)+p_{\phi_{i} \phi_{j}}\right)^{2}+\left(x_{j}(t)+p_{\phi_{j} \phi_{i}}\right)^{2} \geq R_{\min }^{2}
$$

where $R_{\text {min }}$ is a constant that denotes minimum separation (distance between the centers of the two vehicles) to avoid any collision of the two vehicles at their CCP. Satisfying this constraint means that the optimal solution is found outside the unsafe or infeasible region, and collision-free operation of the intersection is thereby guaranteed.

Subject to the given current states of the vehicles, their state dynamics (6) and constraints (9)-(13), a performance index including the risk function (8) is defined as

$$
\begin{aligned}
J=\sum_{t=0}^{T-1} & \sum_{i=1}^{N} w_{v_{i}}\left(v_{i}(t+1)-v_{d}\right)^{2} \\
& \quad+\sum_{t=0}^{T-1} \sum_{i=1}^{N} w_{u}\left(u_{i}(t)\right)^{2}+\sum_{t=0}^{T-1} \sum_{i=1}^{N-1} \sum_{j=i+1}^{N} \mathcal{F}_{i, j}(t)
\end{aligned}
$$

where $T$ (steps) is the length of the prediction horizon, $v_{d}$ is the desired velocity, and $w_{v_{i}}$ and $w_{u}$ are weight coefficients. There are three cost terms in the aforementioned performance index. The first term denotes the cost related to velocity deviation from the desired value $v_{d}$. The second term denotes the cost of acceleration. Minimizing these two terms means comfortable and smooth flow of vehicles. The third term denotes the cost related to the risk of collisions as defined in the risk function (8), which sums up quantified risks at all CCPs for all possible pairs of vehicles considering their predicted trajectories in the horizon. This term enables the optimizer to push the solution faster toward the safest (least risk) point far from the infeasible region defined by constraint (13). Minimization of risks, which is based on the idea of reducing unused space in the intersection area, eventually increases the traffic handling capacity of the intersection. By setting $v_{d}$ at some high value, rapid intersection crossing of vehicles, by keeping marginal gaps as defined by the risk function, can be realized. In these ways, the traffic-flow capacity can be enhanced by minimizing the aforementioned performance index.

At each discrete time step $t$, the ICU receives information of current position, velocity, and destination of the vehicles and computes their control input $u$ for the entire horizon by solving the aforementioned nonlinear constraint optimization problem. However, only the control inputs $u_{l}^{n}(0)$ corresponding to the current time are applied to each vehicle. It is assumed that each vehicle has a local controller installed that perfectly generates and executes the actual engine torque considering the vehicleengine dynamics for realizing the desired acceleration received from the ICU. At the subsequent time step, the optimization procedure is repeated for newly measured initial conditions of the same or a new set of vehicles (if some vehicles have already crossed the intersection). Although optimal control inputs of a set of vehicles are calculated for the entire horizon of $T$-steps, the process needs to be repeated at every short interval by measuring new states of vehicles. This way, any unexpected change in the behavior of some vehicles due to any incidents in the intersection can be overcome.

## III. Numerical Simulation

The proposed VICS is numerically simulated for the test intersection shown in Fig. 1. The constrained nonlinear optimization problem in the proposed MPC framework is solved in MATLAB by the optimization toolbox fmincon using the solving algorithm interior point method [19]. Since the optimization problem is nonlinear, the solution of the optimization is not guaranteed to be the global optimum.

Two approaching vehicles $(M=2)$, which are the closest to the intersection from every lane, are coordinated at a time, i.e., trajectories of $12(N=6 M=12)$ vehicles are globally optimized by the ICU based on the states of the whole vehicles in question. The discrete time step is chosen as $\tau=0.5 \mathrm{~s}$, and the prediction horizon as $T=14$ steps. The parameters of the linear constraints are chosen as $v_{\text {max }}=23 \mathrm{~m} / \mathrm{s}, v_{\text {min }}=3$, $u_{\text {max }}=5 \mathrm{~m} / \mathrm{s}^{2}, u_{\text {min }}=-6 \mathrm{~m} / \mathrm{s}^{2}, r_{\text {min }}=7 \mathrm{~m}$, and $R_{\text {min }}=$ 7 m . The constraint related to the turning velocity (12) is set with $V_{a}=14, \beta=0.003$, and for left-turning vehicles $V_{b}=8$ and right-turning vehicles $V_{b}=10$. According to the intersection design manual [18], the minimum radius of the turning path should be higher than about 25 and 40 m for the left turning and the right turning, respectively. The parameters of the risk function (8) is chosen as $H=1000$ and $\alpha=0.005$ for all vehicles. The performance index is set with $v_{d}=16.67 \mathrm{~m} / \mathrm{s}$ $(60 \mathrm{~km} / \mathrm{h})$ and $w_{u}=5$. The weights $w_{v_{i}}$ are set at 2.0 and 1.0 for the first vehicle (denoted by the odd values of $i$ for $M=2$ ) and the second vehicle of each lane, respectively.

To comprehend the functionality of the proposed scheme, the optimal trajectories of vehicles generated at one step for an given initial state are observed (see Fig. 5). The results of optimization are shown in terms of the predicted trajectories, corresponding velocities, and control inputs of the vehicles. In this example, all the vehicles are set to cross the intersection straightaway except vehicle C2, which turns left under a constrained velocity at the intersection. Fig. 5(a) shows the remaining distance from the current vehicle position to the center of the intersection. Note that the length of the intersection in one side (in direction of lanes A and B) is double the

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-08.jpg?height=1551&width=769&top_left_y=232&top_left_x=200)
Fig. 5. Results of optimization for a test case: (a) distance from the center of the intersection, (b) velocity, and (c) acceleration of vehicles approaching the intersection from the four sections. The turning velocity of vehicle C2 is constrained, and the other vehicles move straight.

length of the other side as illustrated in Fig. 1. A comparatively difficult initial condition, in terms of position and velocity of the vehicles, is chosen to understand how their future trajectories are generated to avoid conflicts among vehicles over their CCPs in the intersection.

Since the conflicting vehicles are almost at the same distance from the intersection, some of them decelerate and others accelerate to make a quick gap for their safe crossing. Deceleration followed by acceleration of any vehicle is not desirable since it causes extra fuel consumption. However, once a few vehicles are coordinated successively, all vehicles on each lane will approach the intersection with a time difference by simply using their car-following algorithm, and such aggressive changes in velocity would not be necessary.

The actual coordination of vehicles is implemented in the MPC framework for continuous operation of the intersection.

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-08.jpg?height=604&width=771&top_left_y=236&top_left_x=1109)
Fig. 6. Maximum possible capacities of the intersection in terms of vehicles per hour per lane: the estimated and observed capacities by the proposed VICS and the capacity by the traditional SIS. Comparison is made for the three different traffic-flow patterns defined by Cases 1 to 3.

For its evaluation, a realistic traffic environment is created using the microscopic car-following model called intelligent driver model (IDM) [20]. Among the vehicles on every lane, two approaching vehicles closest to the intersection are manipulated by the ICU instead of driving them using their default system based on the IDM. In the MPC framework, at each step, the optimization problem is solved to obtain the inputs of all vehicles under consideration for the entire prediction horizon, as in the example shown in Fig. 5(c). However, only the control inputs corresponding to the current time is used to control the vehicles. In the next steps, the optimization process is repeated with newly measured vehicle states. If some vehicles complete crossing the intersection, in the next step, those are replaced by new approaching vehicles in the framework. In these ways all vehicles are successively coordinated using MPC.

Fig. 6 shows comparisons of the maximum capacities of the intersection by the proposed VICS and by the traditional SIS with full actuated signal control. Capacities of the intersection are observed from simulation for the following three trafficflow cases.

1) Case 1: There are no turning vehicles, i.e., all vehicles cross the intersection straightaway.
2) Case 2: There are 20\% left-turning vehicles from lanes A, B, C, and E, and the rest of vehicles cross the intersection straightaway.
3) Case 3: There are 20\% left-turning vehicles from lanes A, B, C, and E, and $10 \%$ right-turning vehicles from lanes A, B, D, and F, and the rest of vehicles cross the intersection straightaway.

In each case, the capacity observed from simulation of the proposed VICS is compared with the estimated value (VICS-Estimated) given by (2). In Case 1, a capacity of 1626 veh/h is observed by the VICS, which is very close to the estimated value of 1667 veh/h and much higher than the capacity of 840 veh/h of the SIS under full actuated signal control. The traditional SIS is simulated in the Aimsun microscopic traffic simulator, by setting the vehicles with the same parameters and preference as considered in simulation of the VICS,

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-09.jpg?height=874&width=1532&top_left_y=232&top_left_x=256)
Fig. 7. Distribution of velocity and acceleration of vehicles with respect to the distance from the intersection in two traffic flow cases: (a) 1210 veh/h and (b) 830 veh/h.

e.g., the same vehicle length, minimum desired gap, velocity preference, etc.

In the Aimsun simulator, vehicles are controlled according to their default microscopic flow, lane change, and other algorithms. For microscopic traffic flow, the Aimsun simulator uses the Gipps model instead of the IDM. For observing the maximum capacity of the SIS, input traffic into all the sections is set at an equally high rate to create a saturated condition at the intersection in such a way that both the green signals terminate at the maximum limits under the full actuated signal control. Due to constraints on turning velocity, some vehicles have to reduce the velocity at the intersection that also affects flows of the vehicles behind them. Specifically, right-turning vehicles need longer time to cross the intersection and face more conflict or higher number of CCPs. Therefore, in Cases 2 and 3, the maximum capacities of the VICS drop compared with the capacity in Case 1. However, this is also true for the traditional SIS; specifically at higher right-turning rates, the capacity severely drops. Regardless of the rate of turning, the maximum capacities remain significantly higher than that of the SIS.

Fig. 7 shows the distributions of velocity and acceleration of vehicles with respect to the distance from the intersection in two traffic flow cases, (a) 1210 veh/h and (b) 830 veh/h. In both cases, turning vehicles are not included. More than 1000 data points are taken from the vehicles under the VICS. The velocities and accelerations of vehicles vary, depending on the states of all vehicles under coordination at each time. At a higher traffic volume, velocities of vehicles are increased or aggressively decreased to create quick gaps for their safe crossing. In contrast, velocity variation and accelerations are not significant at a lower traffic volume. By taking a larger number of vehicles per lane in the MPC framework at a time, their velocity can be smoothly adjusted from a sufficiently far distance, and consequently, large deviation of velocities or aggressive accelerations can be avoided. When a vehicle is taken under the VICS for the first time, the vehicle accelerates or decelerates to quickly catch the optimal trajectories as found around 40-60 m and 80-100 m in Fig. 7(a) and (b), respectively. In most cases, the vehicles only accelerate to reach the desired crossing velocity, which is slightly higher than the velocity of the incoming traffic.

Capacity enhancement of the intersection is not the main purpose of the proposed VICS. It is more important to observe the performance of individual vehicles for crossing the intersection. Fig. 8 shows the comparison of the overall performance of the VICS with the SIS at various traffic flow conditions. The performance of each vehicle is observed for crossing the intersection. Here, crossing the intersection by a vehicle means traveling a distance of 100 m before leaving the intersection. In Fig. 8(a), the average time taken by the vehicles to cross the intersection is shown. The horizontal axis shows the average traffic flow per lane as observed. Each marker in the graphs shows the observed value, and the curves represent the respective trends. In the case of the traditional SIS, the crossing time (including the idling time) increases with the traffic flow. In contrast, the crossing time of vehicles under the VICS remains almost constant and much shorter than the SIS. Fig. 8(b) shows the average idling time of the vehicles at the intersection. In the case of traditional SIS, the idling time increases with the increase in traffic flow. When the incoming traffic is higher than its maximum capacity of 840 veh/h, some vehicles have to wait for more than one signal cycles (such cases is not included in the average values shown). Even when the traffic flow is very low, idling time cannot always be avoided since there are some vehicles that have to stop at the intersection due to the red signal in either group of lanes. On the other hand, the idling time of vehicles under the VICS is almost zero.

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-10.jpg?height=1500&width=750&top_left_y=232&top_left_x=206)
Fig. 8. Performance of the vehicles in the proposed VICS and comparison with that of SIS at different traffic flow conditions: (a) average time required to cross the intersection (a distance of 100 m before leaving the intersection), (b) the average idling time, and (c) the average fuel consumption.

Finally, the average fuel consumption of the vehicles for crossing the intersection is shown in Fig. 8(c). The fuel consumption is estimated using the fuel consumption model used in Aimsun [21], which was originally adopted from [22]. The same fuel consumption parameters of a Ford Fiesta car are considered here for all vehicles. In the case of traditional SIS under full actuated signal control, the fuel consumption during crossing the intersection (including consumption during idling) increases with the increase in the traffic flow. The vehicles in the proposed VICS require much less fuel than the vehicles in SIS. At a low traffic flow, fuel consumption is almost constant, and above 800 veh/h, fuel consumption has an increasing trend. At higher traffic flow, acceleration of vehicles considerably increases due to the increasing number of conflicting vehicles approaching at the same time that require rapid variation in their velocities. Therefore, the fuel consumption increases at higher traffic flow rate.

## IV. Discussion

The proposed VICS significantly increases the capacity of the intersection as found from both estimation and simulation. It allows vehicles with conflicting movements to cross the intersection with a very marginal gap at high velocity. Without high control precision such a small gap is not realistic, and it may also cause anxiety to the users. At high traffic flow, aggressive acceleration and braking are applied to some vehicles in order to avoid any risks of collision in the intersection area. Such aggressive acceleration and braking increase the fuel consumption of the vehicles. In addition to this extra consumption, such aggressive driving obviously increases discomfort of the users and is not studied in this paper. For the real implementation, the parameters of the VICS related to the driving preferences and intersection geometry must be chosen at some appropriate values considering the standard of driveability.

In this simulation, only two vehicles from each lane are coordinated at a time. Since in highly dense traffic, vehicles are coordinated by the ICU when they are already very close to the intersection, high acceleration is necessary to adjust the arrival and crossing time of vehicles. One option to alleviate such aggressive acceleration for a much smoother traffic flow is to coordinate more vehicles at a time in a zone close to the intersection so that they can reach the intersection at the appropriate time and velocity. The proposed VICS can easily be extended for coordinating more vehicles with additional computational cost. Another option is to operate the intersection at some level below its maximum possible capacity by regulating the incoming traffic to the intersection in some suitable way. Even if the VICS is operated at the same capacity of traditional intersection, it can still bring huge benefits by improving travel time, reducing fuel consumption and almost eliminating stop delay.

For computing the optimal solution, it is necessary to provide the initial values or guess of the solution. If both the initial values of the solution and initial states of vehicles satisfy the constraints, the optimizer always provides a feasible optimal solution. There can be various ways to provide an initial value analytically. The ICU coordinates only a few approaching vehicles close to the intersection, assuming other vehicles simply follow the standard car-following behavior before and after they are being coordinated. It is necessary to ensure that the vehicles that are not coordinated by the ICU keep a safe distance from its preceding vehicle. In other words, when the ICU attempts to coordinate a vehicle at the first time, its current states must satisfy the respective constraints, e.g., minimum velocity and minimum gap, otherwise a feasible solution may not be guaranteed. Again, if a lane after crossing the intersection cannot accommodate a vehicle further due to congestion, then the vehicles with such destination must be forcefully stopped early or changed the destination. The ICU can extend these types of coordination by simply providing the desired parameters of car-following models to the vehicles in the respective lanes. The lane change during intersection crossing is not considered under the proposed scheme. It could be an interesting extension of the scheme to coordinate lane changes of vehicles from a far distance by coordinating a large number of vehicles approaching the intersections.

In this paper, the comparison made with the traditional SIS with full actuated signal control is only for an indicative purpose to understand the degree at which the VICS outperforms in terms of the capacity, fuel consumption, and travel time. A detailed study of the technical aspects and performance of the VICS and other similar algorithms needs to be conducted in a more realistic road-traffic network in the future. In this paper, we kept our focus only on evaluating the performance of an isolated intersection by optimizing vehicle flows using MPC.

MPC is usually computationally demanding. In an Intel Core i5-2500, 3.3-GHz CPU, the average computation time is found to be about 1.76 s per iteration for an average traffic volume of about 1000 vehicles per hour per lane. The computation becomes very fast, e.g., a fraction of a second, when a good guess of the initial solution is given by extracting it from the optimal solution of the previous step for the same set of vehicles. However, when some vehicles completely cross the intersection, a new set of vehicles need to be optimized for the first time without using a very good guess of the initial solution. In such cases, the computation cost can be reduced further if a better initial guess of the optimal solution can be provided by mapping from the database of previously optimized solutions. The computational efficiency can be also improved by incorporating various signalized intersection scheme, e.g., parallel processing, generating C codes, and using an efficient optimizer, e.g., the continuation/GMRES method [23]. Such possibilities needs to be investigated in the future.

For fully automatic driving, it is also necessary to control the steering of a vehicle for following the given path perfectly, which we did not consider in this study. However, our proposed method can be implemented with partial automatic driving similar to an advanced adaptive cruise control system, in which steering is controlled by a driver and the velocity is adjusted automatically as directed by the VICS.

## V. Conclusion

A VICS for a traffic-lightless intersection has been proposed. Under a connected vehicles environment, automated vehicles approaching the intersection from all sections are globally coordinated by an ICU in order to allow them to cross the intersection safely and smoothly. The control inputs of the vehicles are optimized in an MPC framework by minimizing the risk of projected cross-collisions of the vehicles in the intersection area and considering relevant constraints for the safe crossing or turning. The proposed VICS has been evaluated through numerical simulation, and its performance is compared with a traditional SIS. It is observed that using the proposed scheme, the stop delay of vehicles at the intersection is almost eliminated, traffic flows and fuel consumption are improved, and consequently, the capacity of the intersection is significantly increased.

In future work, accommodation of both automatic and human-driven vehicles in the intersection coordination framework will be addressed to support gradual transition toward a fully automatic road transportation system.

## Acknowledgment

The authors would like to thank H. Nijmeijer from Eindhoven University of Technology for giving the inspiring idea of cooperative intersection management without using traffic lights.

## References

[1] D. Schrank, B. Eisele, and T. Lomax, "Urban mobility report," Texas Transp. Inst., College Station, TX, USA, 2012.
[2] M. Papageorgiou, C. Diakaki, V. Dinopoulou, A. Kotsialos, and Y. Wang, "Review of road traffic control strategies," IEEE Proc., vol. 91, no. 12, pp. 2043-2067, Dec. 2003.
[3] D. H. M. Treiber, A. Hennecke, and D. Helbing, "Congested traffic states in empirical observations and microscopic simulations," Phys. Rev. E, vol. 62, pp. 1805-1824, 2000.
[4] M. A. S. Kamal, J. Imura, A. Ohata, T. Hayakawa, and K. Aihara, "Control of traffic signals in a model predictive control framework," in Proc. IFAC Symp. Control Transp. Syst., 2012, pp. 38-43.
[5] Connected Vehicle Research. [Online]. Available: http://www.its.dot.gov/ connected_vehicle/connected_vehicle.htm
[6] B. Arem, J. Driel, and R. Visser, "The impact of cooperative adaptive cruise control on traffic-flow characteristics," IEEE Trans. Intell. Transp. Syst., vol. 7, no. 4, pp. 429-436, Dec. 2006.
[7] J. Ploeg, A. Serrarens, and G. J. Heijenk, "Connect \& drive: Design and evaluation of cooperative adaptive cruise control for congestion reduction," J. Modern Transp., vol. 19, no. 3, pp. 207-213, Sep. 2011.
[8] G. Raravi, V. Shingde, K. Ramamritham, and J. Bharadia, "Merge algorithms for intelligent vehicles," in Next Generation Design and Verification Methodologies for Distributed Embedded Control Systems, S. Ramesh and P. Sampath, Eds. Amsterdam, The Netherlands: Springer-Verlag, 2007, pp. 51-65.
[9] A. Uno, T. Sakaguchi, and S. Tsugawa, "A merging control algorithm based on intervehicle communication," in Proc. IEEE Int. Conf. ITS, 1999, pp. 783-787.
[10] K. Dresner and P. Stone, "A multiagent approach to autonomous intersection management," J. Artif. Intell. Res., vol. 31, no. 1, pp. 591-656, Jan. 2008.
[11] M. Omae, T. Ogitsu, N. Honma, and K. Usami, "Automatic driving control for passing through intersection without stopping," Int. J. Intell. Transp. Syst. Res., vol. 8, no. 3, pp. 201-210, Oct. 2010.
[12] J. Lee and B. Park, "Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment," IEEE Trans. Intell. Transp. Syst., vol. 13, no. 1, pp. 81-90, Mar. 2012.
[13] M. A. S. Kamal, J. Imura, A. Ohata, T. Hayakawa, and K. Aihara, "Coordination of automated vehicles at a traffic-lightless intersection," in Proc. IEEE Conf. Intell. Transp. Syst., 2013, pp. 922-927.
[14] Highway Capacity Manual (HCM2000), Transp. Res. Board (TRB), Washington, DC, USA, 2000. [Online]. Available: http://sjnavarro.files. wordpress.com/2008/08/highway_capacital_manual.pdf
[15] D. Husch and J. Albeck, Intersection Capacity Utilization: Evaluation Procedures for Intersections and Interchanges. Sugar Land, TX, USA: Trafficware, 2003. [Online]. Available: http://books.google.co.jp/books? id=jTLPPAAACAAJ
[16] K. Balke, P. Songchitruksa, and X. Zeng, "Potential connected vehicle applications to enhance mobility, safety, environmental security," College Station, TX, USA, SWUTC/12/161103-1, 2012. [Online]. Available: http://texashistory.unt.edu/ark:/67531/metapth281728/
[17] K. Fitzpatrick and W. Schneider, "Turn speeds and crashes within rightturn lanes," Austin, TX, USA, FHWA/TX-05/0-4365-4, 2004.
[18] DelDOT Road Design Manual: Chapter 7 Intersections, Delaware Department of Transportation, Dover, DE, USA, 2004.
[19] J. Nocedal and S. Wright, Numerical Optimization. New York, NY, USA: Springer-Verlag, 2000.
[20] D. Zhao, Y. Dai, and Z. Zhang, "Computational intelligence in urban traffic signal control: A survey," IEEE Trans. Syst., Man, Cybern. C, Appl. Rev., vol. 42, no. 4, pp. 485-494, Jul. 2012.
[21] AIMSUN User's Manual, Transp. Simul. Syst., Barcelona, Spain, 2013. [Online]. Available: http://www.aimsun.com/
[22] R. Akcelic, "Progress in fuel consumption modeling for urban traffic management," in Proc. ARR Board Res., 1982, vol. 124, p. 56.
[23] T. Ohtsuka, "A continuation/GMRES method for fast computation of nonlinear receding horizon control," Automatica, vol. 40, no. 4, pp. 563-574, Apr. 2004.

![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-12.jpg?height=318&width=254&top_left_y=247&top_left_x=146)
Md. Abdus Samad Kamal (S'01-M'07) received the B.Sc.Eng. degree from Khulna University of Engineering and Technology (KUET), Khulna, Bangladesh, in 1997 and the M.S. and Ph.D. degrees from Kyushu University, Fukuoka, Japan, in 2003 and 2006, respectively.

From 1997 to 2000 he was a Lecturer with KUET. In 2006 he was a Researcher with Kyushu University. From 2008 to 2011 he was an Assistant Professor with the Department of Mechatronics Engineering, International Islamic University Malaysia, Selangor, Malaysia. From 2006 to 2008 he was a Researcher with the Institute of Industrial Science, The University of Tokyo, Tokyo, Japan. From 2011 to 2014 he was also with the Japan Science and Technology Agency, Kawaguchi, Japan. Currently, he is a Visiting Researcher with Toyota Central Research and Development Laboratories, Inc., Japan. His research interests include intelligent transportation systems and the applications of model predictive control and reinforcement learning.

Dr. Kamal is a member of the Society of Instrument and Control Engineers.
![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-12.jpg?height=320&width=258&top_left_y=907&top_left_x=144)

Jun-ichi Imura (M'93) received the M.S. degree in applied systems science and the Ph.D. degree in mechanical engineering from Kyoto University, Kyoto, Japan, in 1990 and 1995, respectively.

From 1992 to 1996 he was a Research Associate with the Department of Mechanical Engineering and Science, Graduate School of Engineering, Kyoto University and, from 1996 to 2001, he was an Associate Professor with the Division of Machine Design Engineering, Faculty of Engineering, Hiroshima University, Hiroshima, Japan. From May 1998 to April 1999 he was a Visiting Researcher with Department of Applied Mathematics, University of Twente, Enschede, The Netherlands. Since 2001 he has been with the Department of Mechanical and Environmental Informatics, Graduate School of Information Science and Engineering, Tokyo Institute of Technology, Tokyo, Japan, where he is currently a Professor. His research interests include analysis and control synthesis of nonlinear systems, hybrid systems, and large-scale complex dynamical networks, with applications to biological systems and industrial process systems.

Dr. Imura is an Associate Editor of IEEE Transactions on Automatic Control, Automatica, and Nonlinear Analysis: Hybrid Systems.
![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-12.jpg?height=322&width=256&top_left_y=1629&top_left_x=146)

Tomohisa Hayakawa (S'00-M'04) received the B.Eng. degree in aeronautical engineering from Kyoto University, Kyoto, Japan, in 1997; the M.S. degree in aerospace engineering from The State University of New York, Buffalo, NY, USA, in 1999; and the M.S. degree in applied mathematics and the Ph.D. degree in aerospace engineering from Georgia Institute of Technology, Atlanta, GA, USA, in 2001 and 2003, respectively.

He was a Research Fellow with the Department of Aeronautics and Astronautics, Graduate School of Engineering, Kyoto University and with the Japan Science and Technology Agency in 2006, and then joined the Department of Mechanical and Environmental Informatics, Graduate School of Information Science and Engineering, Tokyo Institute of Technology, Tokyo, Japan, where he is currently an Associate Professor. His research interests include stability of nonlinear systems; nonnegative and compartmental systems; hybrid systems; nonlinear adaptive control; neural networks and intelligent control; stochastic dynamical systems; and applications to aerospace vehicles, formation control of multiagent systems, robotic systems, financial dynamics, and biological/biomedical systems.
![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-12.jpg?height=320&width=258&top_left_y=245&top_left_x=1057)

Akira Ohata received the B.E. degree from Tokyo Institute of Technology, Tokyo, Japan, in 1973.

After graduating, he directly joined Toyota Motor Corporation, where he was involved in exhaust gas emission controls; intake and exhaust system developments, including variable intake systems, hybrid vehicle control system, vehicle controls, and modelbased development; and the education of advanced control theory. He is currently a Senior General Manager with Toyota Motor Corporation, Shizuoka, Japan, and a Research Fellow with the Information Technology Promotion Agency, Tokyo, Japan, under the Ministry of Economy, Trade, and Industry. His research interests include modeling that includes model simplification and the integration of physical and empirical models.

Mr. Ohata is a Vice Chair of the International Federation of Automatic Control TC7.1 (automotive control) and the Chair of the Technical Committee on Plant Modeling of the Society of Instrument and Control Engineers. He oversees the standardization activity in Object Management Group, assuring the dependability of consumer devices. He received the Most Outstanding Paper Award in Convergence 2004 and the Technical Contribution Award from Japan Society of Automotive Engineers.
![](https://cdn.mathpix.com/cropped/c7931f8a-59c8-405d-93e9-f119772f03de-12.jpg?height=318&width=254&top_left_y=1126&top_left_x=1059)

Kazuyuki Aihara received the B.E. degree in electrical engineering and the Ph.D. degree in electronic engineering from The University of Tokyo, Tokyo, Japan, in 1977 and 1982, respectively.

He is a Professor with the Institute of Industrial Science and with the Graduate School of Information Science and Technology, The University of Tokyo. He is also the Director of the Collaborative Research Center for Innovative Mathematical Modelling, Institute of Industrial Science, The University of Tokyo. His research interests include the mathematical modeling of complex systems, parallel distributed processing with spatiotemporal chaos, and the time-series analysis of complex data.


[^0]:    Manuscript received October 23, 2013; revised February 11, 2014, May 20, 2014, and August 11, 2014; accepted August 19, 2014. This work was supported in part by the Aihara Innovative Mathematical Modeling Project of the Japan Society for the Promotion of Science through the Funding Program for World-Leading Innovative Research and Development on Science and Technology (FIRST Program), which was initiated by the Council for Science and Technology Policy, and in part by the JSPS Grant-in-Aid for Scientific Research (A) 26249062. The Associate Editor for this paper was M. Chowdhury.
    M. A. S. Kamal is with Toyota Central Research and Development Laboratories, Inc., Nagakute 480-1131, Japan (e-mail: maskamal@ieee.org).
    J. Imura and T. Hayakawa are with the Department of Mechanical and Environmental Informatics, Graduate School of Information Science and Engineering, Tokyo Institute of Technology, Tokyo 152-8552, Japan.
    A. Ohata is with Toyota Motor Corporation, Shizuoka 410-1193, Japan.
    K. Aihara is with the Collaborative Research Center for Innovative Mathematical Modelling, Institute of Industrial Science, The University of Tokyo, Tokyo 153-8505, Japan, and also with the Graduate School of Information Science and Technology, The University of Tokyo, Tokyo 113-8656, Japan.
    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
    Digital Object Identifier 10.1109/TITS.2014.2354380

