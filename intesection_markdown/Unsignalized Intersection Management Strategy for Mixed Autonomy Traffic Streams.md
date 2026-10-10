# Unsignalized Intersection Management Strategy for Mixed Autonomy Traffic Streams 

Junjie Zhou, Zhaokun Shen, Xiaofan Wang, and Lin Wang


#### Abstract

With the rapid development of connected and automated vehicles (CAVs) and intelligent transportation infrastructure, CAVs, connected human-driven vehicles (CHVs), and un-connected human-driven vehicles (HVs) will coexist on the roads in the future for a long time. This paper comprehensively considers the different traffic characteristics of CHVs, CAVs, and HVs, and systemically investigates the unsignalized intersection management strategy from the upper decision-making level to the lower execution level. The unsignalized intersection management strategy consists of two parts: the heuristic priority queues based right of way allocation (HPQ) algorithm and the vehicle planning and control algorithm. In the HPQ algorithm, a vehicle priority management model considering the difference between CAVs, CHVs, and HVs, is built to design the right of way management for different types of vehicles. In the lower level for vehicle planning and control algorithm, different control modes of CAVs are designed according to the upper-level decision made by the HPQ algorithm. Moreover, the vehicle control execution is realized by the model predictive controller combined with the geographical environment constraints and the unsignalized intersection management strategy. The proposed strategy is evaluated by simulations, which show that the proposed intersection management strategy can effectively reduce travel time and improve traffic efficiency. Results show that the proposed method can decrease the average travel time by 5\% to 65\% for different traffic flows compared with the comparative methods. The intersection management strategy captures the real-world balance between efficiency and safety for future intelligent traffic systems.


Index Terms-Mixed autonomy traffic streams, connected and automated vehicles (CAVs), unsignalized intersection, intelligent intersection, right of way allocation.

## I. INTRODUCTION

IN RECENT years, traffic congestion has become a critical social problem that troubles people's lives and hinders social development [1]. With the development of autonomous driving technology and the maturity of communication technology, connected and automated vehicles (CAVs) have gradually come into the public horizon. It is the primary direction

[^0]for researchers to improve intersection efficiency through vehicle coordination under safe conditions. Traffic signal control methods have good effects on intersections with relatively large traffic volumes and strong traffic capacity [2]. But for intersections with small traffic volumes and weak traffic capacity, signal control will cause unnecessary travel time loss.

Unsignalized intersections have been considered an effective solution to improve traffic efficiency in the past few years [3]. While unsignalized intersections provide effective tools to reduce energy consumption and traffic delays, it is also necessary to improve safety to reduce the number of accidents [4], [5]. As the penetration rate of connected vehicles is increasing rapidly, it is expected that such systems will become more practical in the near future. Besides, according to the study in [6], [7], governments worldwide are increasingly promoting the deployment of Vehicle-to-Everything (V2X) technologies. Considering the traffic environment of mixed connected human-driven vehicles (CHVs), un-connected human-driven vehicles (HVs), and CAVs will exist for an extended period of time in the future, efficient and reasonable intersection management strategies should be developed to ensure vehicle safety and improve the traffic efficiency for mixed autonomy traffic streams.

This paper focuses on the design of unsignalized intersections management strategy for mixed autonomy traffic streams based on the vehicle-to-infrastructure (V2I) architecture, which consists of the heuristic priority queues based right of way allocation (HPQ) algorithm and vehicle planning and control algorithm for the mixed traffic flow intersections. The HPQ algorithm is used to manage the right of way of vehicles at intersections to maximize the utilization efficiency of the conflict area. Through the geographic modeling of the intersection, the trajectories and conflict table of vehicles passing through the intersection are formulated, and the traffic condition constraints are used to ensure the safety of vehicles. According to the decision made by the HPQ algorithm at the intersection, the vehicle planning and control algorithm is designed based on four control modes, including car following mode, cruise mode, waiting mode, and conflict-solving mode.

Furthermore, the improved model predictive control is applied to realize the four control modes. The main contributions of this paper are as follows:

- We propose an integrated heuristic priority queues based intersection management strategy spanning from upper decision-making levels to lower execution levels. Distinguished from previous research, this paper proposes an enhanced HPQ algorithm tailored to address trajectory conflicts and prioritize management conditions for

CAVs, CHVs, and HVs. The overall time complexity of our algorithm is $O(n)$, ensuring real-time coordination and control of unsignalized intersections while reducing hardware computing device overhead.
- Four vehicle control modes are proposed based on the developed HPQ algorithm, with model predictive control facilitating smooth transitions between different control modes. Our robust scheduling and control strategy fully account for the characteristics of CAVs, CHVs, and HVs, with CAVs proactively avoiding trajectory conflicts with HVs to ensure safe and efficient traffic flow.
- To validate the safety and effectiveness of our proposed method, we conducted a hybrid simulation using SUMO and PreScan, evaluating both macroscopic and microscopic aspects. Our developed unsignalized intersection management strategy outperforms three existing state-ofthe-art methods in terms of travel time and the number of halts. Furthermore, our method is applicable to intersections of various sizes and types. To the best of our knowledge, this is the first time that an unsignalized intersection management method can efficiently coordinate mixed traffic flows, containing CAVs, CHVs, and HVs simultaneously.

The rest of the paper is organized as follows. Section II reviews the related works. Section III introduces the preliminary and system architecture of the proposed strategy. Section IV details the design of the HPQ algorithm, including the priority management model and right of way management model. Section V details the design of vehicle planning and control algorithm, including the path planning model, speed planning model and modified model predictive control for vehicle control modes. The simulation and performance comparison are presented in Section VI. While section VII concludes the paper.

## II. LITERATURE REVIEW

## A. Unsignalized Autonomous Intersection Management

As summarized in [33], there are two approaches to calculating the possible conflict between two vehicles at the intersection, including the expected vehicle trajectories and the spatiotemporal occupancy map. The system architecture of unsignalized intersections can be broadly classified into centralized system, decentralized system, and distributed system. The relevant works on the unsignalized intersection management methods are summarized in Table I.

At the centralized control intersection, vehicles obtain traffic schemes from the Intersection Control Unit (ICU) through V2I communications. The autonomous intersection management (AIM) of the centralized system follows the server-client scheme, which can be divided into reservation-based and priority-based intersection management. The conflict duration graph is proposed in [8] to resolve collisions and scheduling problems for CAVs at unsignalized intersections. Petri net and cycle removal algorithms are used in [9] to model intersecting scheduling problems. The tree search algorithm is utilized in [10], [11] for optimal passing order calculation. Besides, reinforcement learning algorithms are also widely used in [12]-[15] for centralized intersection management. Centralized methods are computationally intensive and time-consuming, especially for large intersections or high traffic volumes. Consequently, they place significant demands on computing resources and algorithmic complexity.

Decentralized intersection management methods aim to mitigate the computational burden of centralized controllers by distributing tasks across multiple shared computing nodes. In these methods, vehicles near the front of the queue often serve as decentralized hubs, forming queues and communicating with the intersection manager to request permission to enter the intersection [6], [22], [23]. Platoon formation is widely used in unsignalized autonomous intersection management. CAVs form platoons through V2V communication, and each platoon has a leading vehicle [34], [35]. The Vehicle-PlatoonAware Bi-Level Optimization Algorithm for Autonomous Intersection Management (VPA-AIM) algorithm is proposed in [22] to determine the platoon formation scheme of vehicles during the control zone and allocate the passing sequence and timeslots of platoons through the merging area. The VPA-AIM algorithm can be extended to mixed traffic scenarios. However, this method requires all platoon leaders to be CAVs. It is not feasible if the penetration rates of CAVs are not sufficiently high.

Distributed intersection management methods allocate computational nodes to individual vehicles, which then collaborate to determine the optimal passing order. The distributed robust differential game method is proposed in [31] to coordinate driving strategies of CAVs passing through unsignalized intersections. The depth-first spanning tree is utilized in [25] to calculate the right of way of vehicles at the intersection. Besides, the graph-based coordination method proposed in [26], [27] enables vehicles to pass through intersections efficiently. It is an effective method for coordinating unsignalized intersections. However, this approach necessitates that all vehicles within the intersection area be equipped with communication and computation devices to facilitate real-time information exchange and conflict resolution. As a result, distributed methods face challenges when applied to scenarios featuring mixed traffic streams comprising both connected vehicles and un-connected vehicles.

There are relatively few studies on unsignalized control methods for mixed traffic flows where CAVs, CHVs, and HVs coexist. The control of traditional HVs at intersections poses challenges due to the absence of advanced communication equipment, which renders them unable to respond to directives from intersection control units or receive messages from other vehicles. This limitation complicates multi-vehicle control scenarios at intersections without traffic lights. Certain studies simplify HV behaviors at intersections by assuming strict following to the preceding vehicle. While this simplification aids in the mathematical modeling of multi-vehicle control issues at intersections, it fails to capture real-world scenarios where HVs navigate intersections freely without leading vehicles. In this paper, we comprehensively consider the different traffic characteristics of CAVs, CHVs, and HVs, and propose a heuristic priority queues based intersection management strategy that can be used for mixed autonomy traffic streams.

TABLE I
SUMMARY OF UNSIGNALIZED INTERSECTION MANAGEMENT METHODS
| Category | Study | Method | Intersection Type | Control Policy | Mixed Traffic Flow |  |  | Validation Methods |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  | CAV | CHV | HV |  |
| Centralized System | [8] | Conflict Duration Graph | Signal-Free Intersection | Reservation Policy | * |  |  | MATLAB |
|  | [9] | Cycle Removal Algorithm | One-lane Intersection | Cycle Removal | * |  |  | Numerical Test |
|  | [10] | Reservation-based Scheduling | Unsignalized Intersection | Reservation Policy | * |  |  | Macro-simulation |
|  | [11] | Monte Carlo Tree Search | One-lane Unsignalized Intersection | Learning-based Iterative Optimization | * |  |  | SUMO |
|  | [12] | Transfer Deep Reinforcement Learning | One-lane Unsignalized Intersection | Priority Policy | * |  |  | OpenAI gym |
|  | [13] | Deep Reinforcement Learning | Three-way Intersection | Priority Policy | * |  | * | SUMO |
|  | [14] | Reinforcement Learning | One-lane Unsignalized Intersection | Coordination Policy | * |  |  | Numerical Simulation |
|  | [15] | Reinforcement Learning | One-lane Unsignalized Intersection | Priority Policy | * |  | * | Highway-env |
|  | [16] | Absolute Value Programming | Unsignalized Intersection | Priority Policy | * |  |  | SUMO |
|  | [17] | Reservation-prioritization-based Cooperative Control | Unsignalized Intersection | Reservation Policy | * |  | * | SUMO |
|  | [18] | Cooperative Maneuver Planning | Unsignalized Intersection | Reservation Policy | * | * |  | SUMO |
|  | [19] | Learning-based Iterative Optimization | Unsignalized Intersection | Cluster-based Motion Planning | * |  |  | SUMO |
|  | [20] | Conflict Graph Tree Search | Multi-lane Unsignalized Intersection | Priority Policy | * |  |  | Python |
| Decentralized System | [21] | Deep Reinforcement Learning | Double-lane Intersection | Platoon Control | * |  | * | SUMO Simulation |
|  | [6] | Fully-distributed Control Protocol | One-lane Unsignalized Intersection | Priority Policy | * | * |  | MiTraS |
|  | [22] | Vehicle-Platoon-Aware Bi-Level Optimization | One-lane <br> One-lane Unsignalized Intersection | Reservation Policy | * |  | * | MATLAB |
|  | [23] | Virtual Platooning | Signal-free Intersection | Adaptive Sliding Mode Controller | * |  |  | SUMO |
|  | [24] | Multiagent-based Deep Reinforcement Learning | Multiple Unsignalized Intersections | Priority Policy | * |  |  | Python |
| Distributed System | [25] | Vehicle Conflict Directed Graph | One-lane Unsignalized Intersection | Priority Policy | * |  |  | Numerical Test |
|  | [26] | Depth-First Spanning Tree | Unsignalized Intersection | Reservation Policy | * |  |  | SUMO Simulation |
|  | [27] | Depth-First Spanning Tree | Three-lane Unsignalized Intersection | Reservation Policy | * |  |  | SUMO Simulation |
|  | [28] | Interspersed Traffic Organization | Unsignalized Intersection | Priority Policy | * |  |  | VISSIM |
|  | [29] | Tree Generation Algorithm | One-lane Unsignalized Intersection One-lane Unsignalized Intersection | Priority Policy | * |  |  | Numerical Simulation |
|  | [30] | Task-area Partition | Unsignalized Intersection | Priority Policy | * |  |  | Numerical Simulation |
|  | [31] | Distributed Robust Differential Game | Small Unsignalized Intersection | Game Theory | * |  |  | Simulation |
|  | [32] | Iterative Grouping Algorithm | Multi-lane Unsignalized Intersection | Formation Control | * |  |  | SUMO |


## B. Mixed Autonomy Traffic Streams Management

According to the prediction, CAVs will not be fully popularized before 2045 [36]. For a long period of time in the future, the traffic environment of mixed CHVs, HVs, and CAVs will always exist. Therefore, it is necessary to study AIM in the mixed autonomy traffic streams. Stone et al. first proposed the AIM cooperative driving strategy for mixed traffic streams, which adopts the strategy called First Come First Served (FCFS) manner in the signalized intersection [37], [38]. HVs obey traffic signals, while CAVs adopt the requestbased method to request the right of way at the intersection. In [39], a Hybrid Autonomous Intersection Management (H-AIM) protocol was proposed to grant reservation for vehicles at intersections in FCFS order, which is demonstrated to be effective even in complex traffic scenarios.

Furthermore, to improve traffic throughput and reduce energy consumption, [40] established a connected vehicle center (CVC) to control the movement of all vehicles and detect the position and trajectory of HVs through sensors. When the HVs arrive near the stop line, the traffic lights are used to instruct the right of way for these HVs, while the CVC controls the AVs. To reduce the energy consumption of the vehicles at signalized intersections for mixed traffic streams, [41] proposed a dynamic platoon splitting and merging method to reduce the fuel consumption of the fleet. In addition, a distributed intersection protocol for mixed traffic streams is proposed in [42], where the AVs switch to the synchronous cooperation mode and pass through the intersection without stopping in the case of no HVs entering.

These existing methods focus on the AIM for mixed autonomy traffic streams at signalized intersections and put forward effective intersection management strategies to improve safety and efficiency. To the best of our knowledge, few studies have considered the difference between CAVs, CHVs, and HVs at unsignalized intersections. In this paper, we formally characterize the differences between CAVs, CHVs, and HVs in handling trajectory conflicts and priority management conditions, and design an improved HPQ algorithm to ensure the safety and travel efficiency of vehicles at unsignalized intersections, which derives a futuristic and practical unsignalized intersection management strategy.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-04.jpg?height=1588&width=834&top_left_y=206&top_left_x=193)
Fig. 1. Architecture of unsignalized intersection with mixed CAVs, CHVs, and HVs. The system architecture is mainly composed of two levels. The high level is the HPQ algorithm that assigns the right of way to vehicles at the intersection. The low level consists of vehicle planning and control algorithms for CAVs to safely and efficiently resolve potential trajectory conflicts with HVs.

## III. DESIGN OF SYSTEM ARCHITECTURE

In this section, a new type of unsignalized AIM system architecture is designed to enable vehicles to pass through the intersection more safely and efficiently. The Cooperative Vehicle Infrastructure System (CVIS) provides hardware and communication support for the intersection. All vehicles at the intersection are assumed to be equipped with an On-Board Unit (OBU) and can transmit the information of the ego vehicle to other vehicles and ICU at the intersection via V2V and V2I communications. Sensor equipment is installed

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-04.jpg?height=795&width=853&top_left_y=208&top_left_x=1091)
Fig. 2. Layout of the typical unsignalized intersection.

on the roadside to ensure that all messages, such as the speed and position of all vehicles, can be obtained at the intersection. At the same time, it ignores the delay, packet loss, and information attacks in the communication process. When CAVs and CHVs enter the intersection, they will send the estimated driving route to the ICU, and the drivers of CHVs will follow the driving route. A human-machine interface will be installed in the CHVs to display the traffic instructions of the ICU.

Fig. 1 depicts the architecture of unsignalized intersections with a mix of CAVs, CHVs, and HVs. The overall architecture is mainly composed of two levels. The high level is the HPQ algorithm, which is designed in detail in Section IV. It determines the priority management of vehicles and formulates corresponding right of way management methods for the two types of vehicles. The low level includes vehicle planning and control algorithms for CAVs, which are developed in detail in Section V.

Considering the feasibility and practicability of edging computing, the low-level vehicle planning and control algorithm uses the ICU to collect surrounding vehicle information, which can better ensure the safety of vehicles at the intersection and improve traffic efficiency. Since CAVs have high controllability and intelligence, four control modes, including car following mode, cruise mode, waiting mode, and conflict-solving mode, are designed for CAVs, according to the decision information from the high-level HPQ right of way allocation algorithm. Moreover, the model predictive controller is designed to realize the four control modes of the CAVs. In addition, through the geographic modeling of the intersection, the trajectories and conflict tables of vehicles passing through the intersection are provided in real time.

TABLE II
DEFINITION OF SETS, DATA STRUCTURE, VARIABLES AND PARAMETERS
| Sets: |  |
| :--- | :--- |
| $S$ | set of all vehicles at the intersection |
| $S_{1}$ | set of vehicles that have passed through the conflicting area |
| $S_{2}$ | set of vehicles that have not passed through the conflicting area but have been granted the right of way |
| $S_{3}$ | set of vehicles that have not obtained the right of way |
| $T_{r}(V)$ | set of trajectories of vehicle $V$ |
| Data structure: |  |
| $U$ | struct of the vehicle information containing the id, type, trajectory and other related information |
| $Q_{1}$ | a priority queue composed of vehicles entering the area at $A_{1}$ and belonging to the set $S_{3}$, sorted by priority from high to low |
| $Q_{2}$ | a priority queue composed of vehicles entering the area at $A_{2}$ and belonging to the set $S_{3}$, sorted by priority from high to low |
| $Q_{3}$ | a priority queue composed of vehicles entering the area at $A_{3}$ and belonging to the set $S_{3}$, sorted by priority from high to low |
| $Q_{4}$ | a priority queue composed of vehicles entering the area at $A_{4}$ and belonging to the set $S_{3}$, sorted by priority from high to low |
| $Q_{p}$ | a priority queue composed of $Q_{1}[0], Q_{2}[0], Q_{3}[0], Q_{4}[0]$ that are vehicles corresponding to the top elements of $Q_{1}, Q_{2}, Q_{3}, Q_{4}$ |
| Variables: |  |
| $I_{p}$ | the ID of the vehicle that obtains the right of way in the control cycle of the ICU |
| $I_{c}$ | the ID of the vehicle that has trajectory conflicts with vehicle $V$ |
| $V$ | the ego vehicle at the intersection |
| $\widetilde{V}$ | the vehicles other than $V$ at the intersection |
| Parameters: |  |
| $h$ | the minimum time headway |
| $T_{f}$ | the moment the preceding vehicle enters the intersection |
| $T_{b}$ | the moment the ego vehicle enters the intersection |
| $t_{f}$ | the travel time of the preceding vehicle from the stop line to the conflict point P |
| $t_{b}$ | the travel time of the ego vehicle from the stop line to the conflict point P |
| $s_{f}^{d}$ | the distance of the preceding vehicle from the stop line to the conflict point P |
| $s_{b}^{d}$ | the distance of the ego vehicle from the stop line to the conflict point P |
| $v_{f}$ | the speed of the preceding vehicle |
| $v_{b}$ | the speed of the ego vehicle |
| $N_{1}$ | the number of trajectory conflicts between the vehicle $V$ and other vehicles that have been granted the right of way |
| $N_{2}$ | the number of trajectory conflicts between the vehicle $V$ and other vehicles that have not obtained the right of way |


![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-05.jpg?height=657&width=696&top_left_y=217&top_left_x=1160)
Fig. 3. A typical conflict scenario.

## IV. HPQ RIGHT OF WAY ALLOCATION ALGORITHM

In this paper, we consider a typical four-way intersection, as illustrated in Fig. 2. This intersection has four directions, and each direction contains an entry lane and an exit lane. Let $M=$ $\left\{M_{j} \mid j=1,2,3,4\right\}$ be the set of all directions. In unsignalized intersections, the right of way allocation algorithm plays a vital role in ensuring safety. A typical conflict scenario is illustrated in Fig. 3, where $P$ is the point of conflict between the two vehicles. Let $T_{b}$ and $T_{f}$ be the moments when the ego vehicle and the preceding vehicle enter the intersection, respectively. The essential requirement to ensure the ego vehicle safely pass through the intersection is that:

$$
T_{b} \geq T_{f}+h+t_{f}-t_{b},
$$

where $t_{f}=\frac{s_{f}^{d}}{v_{f}}$ and $t_{b}=\frac{s_{b}^{d}}{v_{b}}$ are the travel time of the preceding vehicle and the ego vehicle from the stop line to the conflict point P, respectively; $s_{f}^{d}$ and $s_{b}^{d}$ are the distance of the preceding vehicle and the ego vehicle from the stop line to the conflict point P , respectively; $v_{f}$ and $v_{b}$ are the speed of the preceding vehicle and the ego vehicle, respectively; $h$ is the minimum time headway, as illustrated in Table II.

For CAVs, the vehicle priority, the location of the conflict point, and the position and speed of the preceding vehicle can be obtained through V2V and V2I communication, and the conflict with the preceding vehicle can be easily handled according to constraint (1). The typical conflict scenario is illustrated in Fig. 3.

## A. Priority Management Model

The priority of vehicles at intersections is designed based on the FCFS policy, and the vehicles entering the area of the intersection first will get a lower priority value $P(V)$. The smaller the priority value $P(V)$ obtained by the vehicle, the higher the priority of the vehicle. The priority value $P(V)$
of the vehicle entering the intersection area first is one, and the following vehicles are incremented by one according to the order in which they enter the intersection. When a vehicle obtains the right of way, the priority value $P(V)$ of all vehicles is reduced by one. When the vehicle enters the entry area, the moment of the current vehicle will be recorded by the ICU. When two vehicles have trajectory conflict, the right of way of the vehicles is determined by comparing the size of the time stamp.

The length of the entry area will influence the driving comfort. In order to guarantee the vehicle can slow down and stop in front of the stop line gracefully. Here, as illustrated in Fig. 2, the length of the entry area $A_{l}$ satisfies the constraint (2) as follow:

$$
A_{l} \geq\left|\frac{v_{l i m i t}^{2}}{2 a_{d}}\right| .
$$

where $v_{\text {limit }}$ is the speed limit for the road, and $a_{d}$ is the maximum acceleration without loss of comfort.

Usually, the priority is not allowed to be changed since changing the priority will easily cause deadlock at the intersection. The deadlock at an intersection means that multiple vehicles fall into a stalemate of cyclical waiting due to the fight for the right of way, and the vehicles can not pass normally at the intersection.

However, for abnormal situations such as breakdowns in conflict areas, the priority of the vehicle can be changed in the priority management model. If the abnormal vehicle keeps occupying the right of way, it will lead to the deadlock of the vehicles whose priority is lower than its and whose trajectory conflicts with it. In this instance, the ICU will kick the abnormal vehicle out of the priority sorting queue and adjust the priority of the vehicles in the same lane with the abnormal vehicle to the lowest to ensure the normal traffic of vehicles in other lanes. Here, a vehicle will be labeled as an abnormal vehicle if the passing time $t_{e}$ of the vehicle through the conflict point is larger than:

$$
t_{e}>\frac{A_{l}}{\frac{v_{l i m i t}}{2}}+\sigma,
$$

where $\sigma$ is the time constant of abnormal judgment.
Based on real-world human driving habits, at unsignalized intersections, HV behaviors can be categorized into two primary types: following the preceding vehicle and free-driving in the absence of preceding vehicles [43]. Based on the previous study [43], we developed rules for CAVs, CHVs, and HVs to pass through unsignalized intersections safely:

1) When there is a trajectory conflict between the CAVs or CHVs and the HVs while passing through an intersection, the CAVs and CHVs will give priority to the HVs to ensure safe passage through the intersection. The CAV is allowed to enter the intersection conflict zone with one HV at the same time by enabling the conflict resolution mode.
2) When two free HVs from conflicting directions reach the intersection simultaneously, they adhere to the right-hand rule to pass through the intersection.

The HV behavior model is modeled by referring to the previous study [44]. When there is a vehicle in front of the HV, the HV has to maintain a safe distance to avoid collision with the preceding vehicle, and thus, the HV needs to be maintained under a safe speed in real time:

$$
v_{\text {safe }}(t)=v_{f}(t)+\frac{g(t)-v_{f}(t) \tau}{\frac{v}{a_{d}}+\tau},
$$

where $v_{f}(t)$ is the speed of the preceding vehicle at time $t$, $g(t)$ is the distance between the two vehicles at time $t, \tau$ is the reaction time of the human driver, and $a_{d}$ is the maximum deceleration of the vehicle. In reality, the target speed of the vehicle should not only consider the above situation, but also consider the dynamic characteristics of the vehicle itself:

$$
v_{\text {des }}(t)=\min \left(v_{\text {safe }}(t), v(t-1)+a, v_{\text {max }}\right),
$$

where $v_{\text {max }}$ denotes the maximum speed limit when the vehicle passes through the intersection.

To model the uncertainty of human driving behavior more accurately, a random error $\epsilon$ is introduced here to portray the relative instability of human drivers' maneuvers:

$$
v(t)=\max \left(0, \operatorname{rand}\left(v_{d e s}(t)-\epsilon a, v_{d e s}(t)+\epsilon a\right)\right) .
$$

In the case of free-driving in the absence of preceding vehicles, the speed of the vehicle depends primarily on the speed limit $v_{\text {limit }}$, the speed of the yielding vehicle $v_{\text {yielding }}$, and the driver's target speed $v_{\text {target }}$.

## B. Right of Way Management Model

The most significant difference between an intersection with and without signal lamps is that the former allocates the right of way for each lane, while the latter allocates the right of way for each vehicle individually. Here, the factors that affect the right of way of each vehicle include vehicle priority, trajectory conflicts, and vehicle type. To save computing resources, the ICU divides all vehicles $S$ within the intersection into three groups. The first group $S_{1}$ is the set of vehicles that have passed through the conflict area, which does not need intersection management; the second group $S_{2}$ is the set of vehicles that have not passed through the conflict area but have obtained the right of way; the third group $S_{3}$ is the set of vehicles that have not obtained the right of way. The right of way management only needs to determine which vehicles in $S_{3}$ can get the right of way.

In the same lane, the vehicle in the front must have priority over the vehicle in the back. Therefore, the third group $S_{3}$ can be divided into four priority queues $\left(Q_{1}, Q_{2}, Q_{3}, Q_{4}\right)$ according to the four entry lanes, where $Q_{i}$ corresponds to the $i$-th lane and ranks the priority of vehicles in the $i$-th lane from small to large according to the time stamp of the vehicle entering the intersection. Every time when the right of way is allocated, the ICU only needs to consider the vehicles at the top of the four queues $Q_{1}[0], Q_{2}[0], Q_{3}[0], Q_{4}[0]$, which are classified as set $Q_{p}$. For the four vehicles at the top of the queue, sort them according to their priorities according to the FCFS policy and check whether the vehicles meet the following conditions for obtaining the right of way. The objective is to find one vehicle that meets the conditions to obtain the right of way. According to the differences between CAVs, CHVs, and HVs, the conditions are set respectively:

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-07.jpg?height=681&width=733&top_left_y=221&top_left_x=247)
Fig. 4. Vehicle trajectory conflict relationship diagram at intersections.

1) Conditions for CHVs to obtain the right of way: There is no trajectory conflict with the vehicles in the second set $S_{2}$, and there is no trajectory conflict with the vehicles with higher priority in the third set $S_{3}$.
2) Conditions for CAVs to obtain the right of way: There can be a trajectory conflict with at most one vehicle in the second set $S_{2}$, and there is no trajectory conflict with the vehicles with higher priority in the third set $S_{3}$.
3) Conditions for HVs to obtain the right of way: When there are preceding vehicles, HVs follow them through the intersection. When there are no preceding vehicles, HVs adhere to the right-hand rule to pass through the intersection.

For trajectory conflict in the typical unsignalized intersection as shown in Fig. 2, straight-through vehicles in entry area $A_{3}$ have crossing conflicts with straight-through vehicles and left-turn vehicles in entry area $A_{2}$, and have merging conflicts with right-turn vehicles in entry area $A_{2}$. Here, pairwise conflicting relationships are represented by an undirected conflict graph $\mathcal{G}=(\mathcal{V}, \mathcal{E})$, which will be used to sort vehicles without conflicts that can pass the intersection at the same time. Fig. 4 shows the vehicle trajectory conflict relationship diagram at the intersection. The number in the circle in Fig. 4 represents the trajectory number, where vehicle trajectory numbers 0, 3, 6, 9 represent right-turn movements; vehicle trajectory numbers 1, 4, 7, 10 represent through movements; vehicle trajectory numbers 2, 5, 8, 11 represent left-turn movements. And the circle with the same color represents the existence of merging conflicts. The trajectories in Fig. 4 can be regarded as a set of nodes $\mathcal{V}=\left\{v_{0}, v_{1}, v_{2}, \cdots, v_{n-1}\right\}$. And the crossing conflict between two trajectories can be represented by an edge, as indicated in Fig. 4. Here, $n=12$ for the four-way intersection, and the set of the edges is $\mathcal{E}=\left\{e_{0}, e_{1}, e_{2}, \cdots, e_{m-1}\right\}$, with $m=16$.

When a vehicle enters the intersection, it should send its own position, speed, acceleration, and other kinematics information to the ICU, including the type of vehicle $C(V)$ $(C(V)==1$ means CHV, and $C(V)==0$ means CAV), the time stamp of entering the intersection and the expected driving direction (going straight, turning right and turning left). After the ICU collects all the vehicles' information, it will execute the HPQ algorithm once in each control cycle to grant at most one vehicle the right of way. Once a vehicle obtains the right of way, the algorithm will update the status of all sets of vehicles and priority queues. Here, a control cycle means that the HPQ algorithm performs one cycle calculation on all vehicles in the priority queue $Q_{p}$ and outputs the result. The length of the control cycle will be changed according to the traffic flow at the intersection.

For the HPQ algorithm shown in Algorithm 1, the parameters $N_{1}$ and $N_{2}$ need to be initialized, where $N_{1}$ represents the number of trajectory conflicts between the vehicle $V$ in the priority queue $Q_{p}$ and other vehicles in the set $S_{2}$ that have been granted the right of way, and $N_{2}$ represents the number of trajectory conflicts between the vehicle $V$ in the priority queue $Q_{p}$ and the other vehicles in the set $S_{3}$ that have not obtained the right of way. Vehicle $V$ is the vehicle to be checked by the HPQ algorithm to determine whether it can be granted the right of way. The priority value $P(V)$ can be calculated by the priority management model.

The HPQ algorithm will find the vehicle that can be granted the right of way in the priority queue $Q_{p}$. First, for each candidate vehicle $V$ in $Q_{p}$, check the vehicle trajectory conflict and calculate the values of $N_{1}$ and $N_{2}$ according to the vehicle trajectory conflict relationship diagram in Fig. 4. If there is a trajectory conflict between the vehicle $V$ in the priority queue $Q_{p}$ and the other vehicles in $S_{2}$, the ID of the conflict vehicle will be recorded in the trajectory conflict variable $I_{c}$ and the value of $N_{1}$ will increase by 1 . Then find the vehicle $\widetilde{V}$ in the set $S_{3}$ whose priority value $P(\widetilde{V})$ is smaller than the priority value $P(V)$ of vehicle $V$ in the priority queue $Q_{p}$, where $S_{3}$ is the set of vehicles that have not obtained the right of way. If there is a trajectory conflict between the vehicle $V$ in the priority queue $Q_{p}$ and the other vehicle $\widetilde{V}$, the value of $N_{2}$ will increase by 1 . Finally, judge whether the vehicle $V$ in the priority queue $Q_{p}$ is a CHV or CAV. If the vehicle $V$ in the priority queue $Q_{p}$ is a CHV and satisfies the conditions for CHVs to obtain the right of way, that is, there is no trajectory conflict between the vehicle $V$ in the priority queue $Q_{p}$ and the other vehicles in the sets $S_{2}$ and $S_{3}$, the vehicle $V$ in the priority queue $Q_{p}$ is granted the right of way. If the vehicle $V$ in the priority queue $Q_{p}$ is a CAV and satisfies the conditions for CAVs to obtain the right of way, that is, the number of trajectories conflict between the vehicle $V$ in the priority queue $Q_{p}$ and the other vehicles in the set $S_{2}$ do not exceed one and there is no trajectory conflict between the vehicle $V$ in the priority queue $Q_{p}$ and the other vehicles in the set $S_{3}$, vehicle $V$ is granted the right of way. If the above conditions are not met, no vehicle is granted the right of way, and the next control cycle is performed.

When a vehicle is granted the right of way, the ICU will issue an instruction to allow the vehicle to pass. Finally, further conflict checks are carried out according to the realtime location of the vehicles at the intersection. If there is a trajectory conflict that requires to be dealt with, the ICU will also send the information of the trajectory conflict to the con-

```
Algorithm 1 HPQ Algorithm
Input: \(U\)
Output: \(I_{p}, I_{c}\)
    Initialize
    \(N_{1}=0, N_{2}=0,\left[I_{p}, I_{c}\right]=\left[{ }^{\prime},{ }^{\prime},{ }^{\prime}\right]\)
    for \(V\) in \(Q_{p}\) do
        for \(\widetilde{V}\) in \(S_{2}\) do
            if \(T_{r}(V) \cap T_{r}(\widetilde{V})!=\emptyset\) then
                \(N_{1}+=1\)
                \(I_{c}=\widetilde{V}\)
            end if
        end for
        for \(\widetilde{V}\) in \(S_{3}\) do
            if \(P(\widetilde{V}) \geq P(V)\) then
                continue
            end if
            if \(T_{r}(V) \cap T_{r}(\widetilde{V})!=\emptyset\) then
                \(N_{2}+=1\)
            end if
        end for
        if \(C(V)==1\) then
            if \(N_{1}+N_{2}==0\) then
                return \([V\), ' \(]\)
            end if
        else
            if \(N_{1} \leq 1\) and \(N_{2}=0\) then
                return \(\left[V, I_{c}\right]\)
            end if
        end if
    end for
    return [' ', ' ']
```

flict vehicles. In addition, CAVs can obtain information about other vehicles through V2V communication so as to improve the accuracy of low-level vehicle planning and control.

The time complexity of the right of way management algorithm is $O(n)$, where $n$ is the total number of vehicles at the intersection. In HPQ Algorithm 1, a vehicle information struct ( $U$ ), five priority queues ( $Q_{1}, Q_{2}, Q_{3}, Q_{4}, Q_{p}$ ), and four vehicle sets ( $S, S_{1}, S_{2}, S_{3}$ ) need to be updated in each control cycle. The priority queue is implemented by the heap. The time complexity of building a heap is $O(n)$, and the time complexity of heap insertion and deletion is $O(\log n)$. After that, to check whether a vehicle conflicts with another vehicle, it needs to query the adjacency matrix that represents the conflict relationship, and the time complexity of this operation is $O(1)$. Then, it needs to query all the corresponding sets $S_{2}$ and $S_{3}$, and the time complexity is $O(n)$. Because there are only four vehicles in $Q_{p}$ at most, the time complexity of querying all vehicles in $Q_{p}$ is $O(n)$. Therefore, the overall time complexity is $O(n)$, which guarantees the efficiency of real-time control for the right of way can be achieved.

According to the designed HPQ algorithm, vehicles with low priority may get the right of way earlier than vehicles with

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-08.jpg?height=812&width=782&top_left_y=208&top_left_x=1126)
Fig. 5. The whole procedure of vehicle planning and control. Based on the right of way allocation results calculated by the HPQ algorithm and the realtime traffic environment, the control modes of vehicles are calculated by the control modes switching algorithm. Then, motion planning is carried out, in which path planning and speed planning run in parallel to obtain the best lateral and longitudinal control scheme. All these control actions are finally output to the actuator for execution.

high priority. To take advantage of the intersection conflict area as efficiently as possible, vehicles with low priority can obtain the right of way as long as they do not affect the vehicles with high priority and vehicles that have already obtained the right of way. This means that vehicles from different entry areas of the intersection can pass the intersection simultaneously. For example, the vehicle with trajectory number 11 in Fig. 4 arrives at the intersection first and gets the highest priority, and then vehicles with trajectory numbers 0 and 5 also enter the intersection. Although the vehicle with trajectory number 11 has the highest priority, vehicles with trajectory numbers 0 and 5 can also obtain the right of way, and these three vehicles can pass the intersection simultaneously. Moreover, the CAVs are allowed to obtain the right of way in the case of conflicting with one vehicle that has been granted the right of way, since CAVs can solve the vehicle conflict through the designed low-level vehicle planning and control algorithm to ensure the safety of vehicles.

## V. VEHICLE PLANNING AND CONTROL ALGORITHM DESIGN

In the previous section, we developed the HPQ algorithm, which combines the differences between CAVs, CHVs, and HVs to arrange the corresponding right of way. In this section, we focus on vehicle planning and control for CAVs since the ICU has high computing power and can obtain the global information of the traffic participants near the intersection.

According to the driving situation of CAVs at the intersection, we introduce four possible decision making modes for

CAVs: the first mode is to follow the preceding vehicle; the second mode is autonomous cruise; the third mode is to stop before the stop line to wait for the right of way; and the last mode is to resolve the trajectory conflicts. In the following text, the corresponding planning and control methods for the four decision making modes of CAVs will be designed in detail. The motion planning problem is divided into two subproblems, including path planning and speed planning, where path planning is constrained by the layout of the road and the geographical model of the intersection, and speed planning enables passing through the intersection quickly, safely, and economically. By using model predictive control, CAVs can switch undisturbedly to the corresponding decision making mode according to the current traffic environment. The whole procedure of vehicle planning and control is illustrated in Fig. 5. Based on the right of way allocation results calculated by the HPQ algorithm and the real-time traffic environment, the control modes of vehicles are calculated by the control modes switching algorithm. Then, motion planning is carried out, in which path planning and speed planning run in parallel to obtain the best lateral and longitudinal control scheme. All these control actions are finally output to the actuator for execution.

## A. Path Planning Model

For a typical four-way unsignalized intersection, as shown in Fig. 6, the intersection trajectory is modeled, and the intersection coordinate system, lane coordinate system, and vehicle coordinate system are established to carry out vehicle path planning. The intersection coordinate system $\xi$ originates from the center point $O$ of the intersection, the Y-axis points north, and the X-axis points east. The lane coordinate system $\xi_{i}, i \in\{1,2,3,4\}$ takes the midpoint of the starting position of each lane in the entry area as the origin, where A-axis is along the center line of the lane, and B-axis is obtained by rotating A-axis 90 degrees counterclockwise. The vehicle coordinate system $\xi_{v}$ takes the vehicle centroid as the origin, where Maxis is the direction of vehicle heading, and N-axis is obtained by rotating M-axis 90 degrees counterclockwise.

The trajectory tracking of CAVs can be solved by vehicle lateral control [45]-[47]. For convenience, the Cartesian coordinate system is transformed into the coordinate system for vehicle path tracking, and the corresponding descriptions for left turn trajectory, straight trajectory, and right turn trajectory are formulated as follows. The coordinate of the CAVs in the lane coordinate system is denoted as $\left(\alpha_{p}, \beta_{p}\right)$. The distance traveled by the CAVs is denoted as $s$. The heading angle of the CAVs is denoted as $\theta$. The left turn trajectory is shown in Equations (7) and (8). The straight trajectory is shown in Equations (9) and (10). The right turn trajectory is shown in Equations (11) and (12).

$$
s= \begin{cases}\alpha_{p}, & \beta_{p}=0,0 \leq \alpha_{p} \leq l, \\ l+R \times \arctan \frac{\alpha_{p}-l}{R-\beta_{p}}, & l<\alpha_{p}<l+R, 0<\beta_{p}<R, \\ l+\frac{1}{2} \pi R+\beta_{p}-R, & \alpha_{p}=l+R, R \leq \beta_{p} \leq R+l .\end{cases}
$$

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-09.jpg?height=806&width=810&top_left_y=202&top_left_x=1104)
Fig. 6. Intersection coordinate system and trajectories of vehicles.

$$
\theta= \begin{cases}0, & \beta_{p}=0,0 \leq \alpha_{p} \leq l, \\ \arctan \frac{\alpha_{p}-l}{R-\beta_{p}}, & l<\alpha_{p}<l+R, 0<\beta_{p}<R, \\ 90, & \alpha_{p}=l+R, R \leq \beta_{p} \leq R+l .\end{cases}
$$

$$
s=\alpha_{p}, \quad 0 \leq \alpha_{p} \leq 2 L, \beta_{p}=0 .
$$

$$
\theta=0, \quad 0 \leq \alpha_{p} \leq 2 L, \beta_{p}=0 .
$$

$$
s= \begin{cases}\alpha_{p}, & \beta_{p}=0,0 \leq \alpha_{p} \leq l, \\ l+r \times \arctan \frac{\alpha_{p}-l}{r+\beta_{p}}, & l<\alpha_{p}<l+r,-r<\beta_{p}<0, \\ l+\frac{1}{2} \pi r-\beta_{p}-r, & \alpha_{p}=l+r,-l-r \leq \beta_{p} \leq-r .\end{cases}
$$

$$
\theta= \begin{cases}0, & \beta_{p}=0,0 \leq \alpha_{p} \leq l, \\ -\arctan \frac{\alpha_{p}-l}{r+\beta_{p}}, & l<\alpha_{p}<l+r,-r<\beta_{p}<0, \\ -90, & \alpha_{p}=l+r,-l-r \leq \beta_{p} \leq-r\end{cases}
$$

where $l$ is the length of the entry area; $l_{w}$ is the width of the lane; $L$ is the radius of the control range of the intersection area; $R$ and $r$ are the radius of turning left and turning right respectively, and meet the constrain $R+r=2 l_{w}$.

## B. Speed Planning Model

Since CAVs need to make corresponding decisions according to different environments, four control modes are designed to ensure the safety of vehicles and improve traffic efficiency. Each control mode includes a corresponding speed plan. The control modes of CAVs are listed as follows:

- Car following mode: Keep a safe distance from the preceding vehicle and follow it.
- Cruise mode: Keep the vehicle at a constant speed.
- Waiting mode: Slow down until the vehicle is stopped before the stop line.
- Conflict-solving mode: Resolve vehicle trajectory conflicts when passing through conflict areas.

To improve the conflict resolution ability of CAVs and ensure the safety of vehicles, the real-time switching of four vehicle control modes needs to be guaranteed. Define a bool type variable $B$ to denote whether the ego vehicle $V$ obtains the right of way at the intersection. $I_{c}$ represents the vehicle's ID with trajectory conflicts with the ego vehicle $V$, and $I_{f}$ represents the ID of the preceding vehicle of ego vehicle $V$. Define $S_{V}(E)$ and $S_{V}$ (stopline) to denote the position of vehicle $E$ and the position of the stop line in the vehicle coordinate system corresponding to the ego vehicle $V$, respectively. And $\epsilon$ is the distance constant.

We develop an undisturbed switching algorithm for the control modes by combining the real-time traffic environment around the ego vehicle $V$. First, judge whether each vehicle has obtained the right of way according to the high-level HPQ algorithm. For vehicles without obtaining the right of way: if there is a preceding vehicle, the control mode is switched to the car following mode; if there is no vehicle ahead and vehicle $V$ reaches near the stop line, the control mode is switched to the waiting mode; otherwise, the control mode is switched to cruise mode.

For vehicles with the right of way: if it can form a vehicle formation with the preceding vehicles to travel together without interference from other vehicles, the control mode is switched to the car following mode; if the vehicle formation may be interfered by other vehicles, the control mode is switched to conflict-solving mode; otherwise, the control mode is switched to cruise mode. Define $\operatorname{ind}\left(\min \left(d_{1}, d_{2}\right)\right)$ as an index when the minimum function gets the minimum value. The value of $\operatorname{ind}\left(\min \left(d_{1}, d_{2}\right)\right)$ is 0 when $d_{1} \leq d_{2}$, otherwise it is 1 . The principles of switching between the four control modes are shown in Algorithm 2.

Let $s$ and $v$ be the current position and velocity of vehicle $V$ in the corresponding lane coordinate system. For the four control modes of CAVs, different reference positions $s_{\text {ref }}$ and reference speeds $v_{\text {ref }}$ are designed respectively, as shown in Equations (13-16).

- Car following mode:
$$
\left\{\begin{array}{l}
s_{r e f}=s_{f}-d_{m i n}-l_{V}-h v, \\
v_{r e f}=v_{f},
\end{array}\right.
$$
where $s_{f}$ and $v_{f}$ are the position and speed of the preceding vehicle, respectively; $d_{\text {min }}$ is the minimum safety distance between the ego vehicle and the preceding vehicle; $h$ is the minimum travel time from the rear of the preceding vehicle to the front of the following vehicle; and $l_{V}$ is the length of vehicle $V$.
- Cruise mode:
$$
\left\{\begin{array}{l}
s_{r e f}=s \\
v_{r e f}=v_{t a r}
\end{array}\right.
$$
where $v_{\text {tar }}$ is target speed of vehicle $V$.
- Waiting mode:
$$
\left\{\begin{array}{l}
s_{r e f}=s_{\text {stopline }}-l_{\text {tar }} \\
v_{r e f}=0
\end{array}\right.
$$

where $s_{\text {stopline }}$ is the position of stop line and $l_{\text {tar }}$ is the target distance from vehicle centroid to the stop line.

- Conflict-solving mode:
```
Algorithm 2 Switching Algorithm for Control Modes
Input: \(B, I_{c}, I_{f}\)
Output: \(M(V)\)
    for \(V\) in \(S\) do
        if \(B==\) false then
            if \(I_{f}!=\) ' ' then
                \(M(V)=\) 'Car following'
            else if \(S_{V}\) (stopline) - \(S_{V}(V)<\epsilon\) then
                \(M(V)=\) 'Waiting'
            else
                \(M(V)=\) 'Cruise'
            end if
        else
            if \(I_{f}!={ }^{\prime}\) ' and \(\left(I_{c}=={ }^{\prime}\right.\) ' or \(I_{c}!={ }^{\prime}\) ' and
            \(\left.\operatorname{ind}\left(\min \left(S_{V}\left(I_{c}\right)-S_{V}(V), S_{V}\left(I_{f}\right)-S_{V}(V)\right)\right)\right)==1\)
            then
                \(M(V)=\) 'Car following'
            else if \(I_{c}!={ }^{\prime}\) ' and \(\left(I_{f}=={ }^{\prime}\right.\) ' or \(I_{f}!={ }^{\prime}\) ' and
            \(\left.\operatorname{ind}\left(\min \left(S_{V}\left(I_{c}\right)-S_{V}(V), S_{V}\left(I_{f}\right)-S_{V}(V)\right)\right)\right)==0\)
            then
                \(M(V)=\) 'Conflict-solving'
            else
                \(M(V)=\) 'Cruise'
            end if
    end if
    end for
```

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-10.jpg?height=537&width=812&top_left_y=1457&top_left_x=1117)
Fig. 7. Four control modes of CAVs.

$$
\left\{\begin{array}{l}
s_{r e f}=s_{p}-\widetilde{s_{p}}+\widetilde{s_{f}}-d_{m i n}-l_{V}-h v, \\
v_{r e f}=v_{f},
\end{array}\right.
$$

where $s_{p}$ is the position of the conflict point $P$ in the lane coordinate system corresponding to vehicle $V ; \widetilde{s_{p}}$ is the position of the conflict point $P$ in the lane coordinate system corresponding to the vehicle that conflicts with vehicle $V$, and $\widetilde{s_{f}}$ is the position of the vehicle $V$ in the lane coordinate system corresponding to the vehicle that conflicts with vehicle $V$.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-11.jpg?height=587&width=636&top_left_y=230&top_left_x=279)
Fig. 8. Schematic diagram of virtual formation method for collision avoidance.

The conflict-solving mode uses the idea of virtual formation [48] to solve the problem of vehicle conflict, as shown in Fig. 8. To make the preceding vehicle and the ego vehicle pass through the conflict point $P$ safely, we improve the speed planning model by introducing four control modes of undisturbed switching and virtual formation. Assuming that the distance between the ego vehicle and conflict point $P$ is $\Delta s_{b}$ and the distance between the preceding vehicle and conflict point $P$ is $\Delta s_{f}$. In order to make the time interval between the ego vehicle and the preceding vehicle reaching conflict point $P$ equal to $H$, which is greater than the minimum safety time headway, the virtual formation is used for position mapping to calculate the relative position between conflicting vehicles. The position of the preceding vehicle can be mapped from the original lane to the lane the ego vehicle is in, and the relative distance between the preceding vehicle and the conflict point $P$ remains unchanged, which meets $\Delta s_{f}^{\prime}=\Delta s_{f}$, as illustrated in Fig. 8. As long as the ego vehicle and the virtual preceding vehicle maintain time headway $H$, both the ego vehicle and the preceding vehicle can pass through the intersection safely and quickly. Different types of vehicles have different time headway $H$ to ensure the vehicle's safety to the greatest extent [49].

## C. Vehicle Control based on Model Predictive Control

- Lateral control:

The vehicle steering model uses the Stanley method [50], as shown in Fig. 9. To obtain the steering model, it is essential to determine the closest point from the center point of the front axle to the target trajectory. The blue curve in Fig. 9 is the target trajectory obtained by the path planning model; $\left(\alpha_{c}, \beta_{c}\right)$ is the closest point; $e_{s c}$ is the offset between the center point of the front axle and the closest point $\left(\alpha_{c}, \beta_{c}\right)$; and $\theta_{e}$ is the angle between the vehicle heading and the tangent to the trajectory of the closest point. The steering angle $\delta$ of the front wheel can be calculated as Equation (17).

$$
\delta=\theta_{V}-\theta_{P}+\arctan \left(\frac{k_{f} e_{s c}}{v}\right),
$$

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-11.jpg?height=595&width=636&top_left_y=213&top_left_x=1186)
Fig. 9. The Stanley method used for lateral control.

where $\theta_{V}$ is the heading angle of vehicle $V ; \theta_{P}$ is the tangent angle at point $\left(\alpha_{c}, \beta_{c}\right)$ relative to the target trajectory; $k_{f}$ is the proportional parameter; and $v$ is the speed of vehicle $V$.

- Longitudinal control:

For longitudinal control, the speed planning model is controlled by the model predictive controller designed in [51]. Define the longitudinal position error of vehicle $V$ as $e_{s f}=$ $s_{\text {ref }}-s$ and the speed error as $e_{v}=v_{\text {ref }}-v$. Error state equations of CAVs in continuous time domain are shown in Equations (18-19), which is utilized in [51] to establish the state space model of longitudinal dynamics of vehicles.

$$
\begin{gathered}
\dot{x}(t)=\widetilde{\Xi} x(t)+\widetilde{\Psi}_{1} \tau(t)+\widetilde{\Psi}_{2} \omega(t) \\
\widetilde{\Xi}=\left[\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right], \quad \widetilde{\Psi}_{1}=\left[\begin{array}{l}
-\widetilde{h} \\
-1
\end{array}\right], \quad \widetilde{\Psi}_{2}=\left[\begin{array}{l}
0 \\
1
\end{array}\right],
\end{gathered}
$$

where $x=\left[e_{s f}, e_{v}\right]^{T}, \tau=a, \omega=a_{t} . a$ is the acceleration of vehicle $V$, and $a_{t}$ is the acceleration of other vehicles, including the preceding vehicle or the vehicle that conflicts with vehicle $V . a_{t}=0$ means no preceding vehicle or vehicle conflicts with vehicle $V$. If the control mode of vehicle $V$ is car following mode or conflict-solving mode, $\widetilde{h}=h$. Otherwise, $\widetilde{h}=0$.

Since the update of the vehicle state quantity $x$ is discrete, the Equations (18-19) are transformed into discrete linear state equations as shown in Equations (20-21).

$$
x(\kappa+1)=\Xi x(\kappa)+\Psi_{1} \tau(\kappa)+\Psi_{2} \omega(\kappa),
$$

$$
\Xi=\left[\begin{array}{ll}
1 & \varphi \\
0 & 1
\end{array}\right], \quad \Psi_{1}=\left[\begin{array}{c}
-\widetilde{h} \varphi-\frac{1}{2} \varphi^{2} \\
-\varphi
\end{array}\right], \quad \Psi_{2}=\left[\begin{array}{c}
\frac{1}{2} \varphi^{2} \\
\varphi
\end{array}\right],
$$

where $\varphi$ is the control cycle. We use the idea of rolling optimization in model predictive control to realize the longitudinal control of the CAVs. The overall objective is to minimize the total deviation between the vehicle speed $v$ and the reference speed $v_{r e f}$ in a finite period of time in the future. To make the behaviors of the CAVs smoother and to improve the
driving comfort of the CAVs, we further introduce acceleration constraints [52]. The objective function and constraints of the proposed algorithm are as follows:

$$
\begin{aligned}
& \min _{\tau} \sum_{\eta=1}^{N_{p}}\|x(\kappa+\eta \mid \kappa)\|_{\Theta}^{2}+\sum_{\eta=0}^{N_{c}-1}\|\tau(\kappa+\eta \mid \kappa)\|_{\Phi}^{2} \\
& \text { s.t. } x_{\min } \leq x(\kappa+\eta \mid \kappa) \leq x_{\max } \\
& \tau_{\min } \leq \tau(\kappa+\eta \mid \kappa) \leq \tau_{\max } \\
& \Delta \tau_{\min } \leq \tau(\kappa+\eta \mid \kappa)-\tau(\kappa+\eta-1 \mid \kappa) \leq \Delta \tau_{\max } \\
& a_{d} \leq a(\kappa+\eta \mid \kappa) \leq a_{\operatorname{com}}
\end{aligned}
$$

where $N_{p}$ is the predictive step length; $N_{c}$ is the control step length; $\Theta$ is the state weight matrix; $\Phi$ is the input weight matrix; $x_{\text {min }}$ and $x_{\text {max }}$ are the lower limit of the state quantity and the upper limit of the state quantity respectively; $\tau_{\text {min }}$ and $\tau_{\text {max }}$ are the lower limit of the control quantity and the upper limit of the control quantity respectively; $\Delta \tau_{\text {min }}$ and $\Delta \tau_{\text {max }}$ are the lower limit of the increment of control quantity and the upper limit of the increment of control quantity respectively; $a_{d}$ is the maximum deceleration without loss of comfort, which is determined to be $-4 m / s^{2}$ by drawing on [52]. $a_{\text {com }}$ is the maximum acceleration without loss of comfort, which is determined to be $2 \mathrm{~m} / \mathrm{s}^{2}$ by drawing on [52].

## VI. SIMULATION RESULTS

To verify the efficiency of HPQ algorithm systematically and comprehensively, we conduct extensive simulations using SUMO [53] to generate mixed random traffic flow. We select scenarios with traffic flows of approximately 1000 passenger car units/hour $(\mathrm{pcu} / \mathrm{h}), 1300 \mathrm{pcu} / \mathrm{h}$ and $1600 \mathrm{pcu} / \mathrm{h}$ to simulate the algorithm and compare it with the hybrid AIM protocol proposed in [39], the delay-time actuated traffic lights algorithm proposed in [54] and the distributed conflict-free cooperation algorithm proposed in [25].

The hybrid AIM protocol [39] is a request-based right of way allocation algorithm for mixed traffic intersection management. Green trajectories and active green trajectories are defined to represent the right of way allocation of the intersection in real time. An active green trajectory is defined as a green trajectory with a HV present on it or on its incoming lane. If the trajectory of the CAV conflicts with the active green trajectory, the reservation of the CAV will be denied. Besides, the hybrid AIM protocol also investigates how to assign turning options for each lane and vehicle type and proposes turning assignment policy to improve traffic efficiency. The delay-time actuated traffic lights algorithm [54] proposes an approach to control signal lamps by capturing the delay time of vehicles and utilize them to regulate the traffic signal timing. Within the range of the minimum and maximum green time, once the accumulated delay on a lane is dissolved, the running green phase is terminated. The distributed conflictfree cooperation algorithm [25] is an iterative depth-first spanning tree algorithm. Each vehicle represents a vertice in the spanning tree. The depth of the vertices in the spanning tree is determined one by one according to the distance between the vehicle and the intersection center, and the conflict graph. According to the spanning tree, the right of way is granted to the corresponding vehicles. Further than these previous AIM algorithms, we comprehensively study the combination of the high-level HPQ algorithm and the low-level vehicle planning and control algorithm, and carry out detailed design for the vehicle control modes to improve traffic efficiency.

TABLE III
PARAMETER SETTINGS DURING THE CASE STUDY
| Parameter | Definition | Value |
| :--- | :--- | :--- |
| $\sigma$ | The time constant of abnormal judgment | 100s |
| $v_{\text {limit }}$ | The speed limit for the road | $13.8 m / s$ |
| $a_{d}$ | The maximum deceleration without loss of comfort | $-4 m / s^{2}$ [52] |
| $a_{\text {com }}$ | The maximum acceleration without loss of comfort | $2 m / s^{2}$ [52] |
| $l$ | The length of the entry area | $100 m$ |
| $l_{w}$ | The width of the lane | $3.5 m$ |
| $L$ | The radius of the control range of the intersection area | $103.5 m$ |
| $R$ | The radius of turning left | $5.25 m$ |
| $r$ | The radius of turning right | $1.75 m$ |
| $\epsilon$ | The distance constant | $20 m$ |
| $d_{\text {min }}$ | The minimum safety distance between the ego vehicle and the preceding vehicle | $1 m$ (CAVs) [22], $2.5 m$ (CHVs, HVs) |
| $h$ | The minimum travel time from the rear of the preceding vehicle to the front of the following vehicle | $0.5 s$ (CAVs) [22], $2 s$ (CHVs, HVs) |
| $l_{V}$ | The length of vehicle $V$ | $5.2 m$ (CAVs), $4.0 m$ (CHVs, HVs) |


Although SUMO can realize efficient mixed random traffic flow simulation in complex dynamic environment, it is arduous to integrate vehicle dynamics and verify the efficiency of the vehicle planning and control algorithms. Therefore, a joint simulation platform based on Matlab and PreScan [55] is built up to simulate the scenario of unsignalised intersections to verify the proposed vehicle planning and control algorithms. In the joint simulation platform based on Matlab and PreScan, Prescan can provide the realistic 3D modelling environment for traffic and physical models of sensor, and V2V and V2I communication simulation. Matlab can embed the vehicle planning and control algorithm to better realize algorithm simulation. The unsignalized intersection management strategy is validated by these simulation tools. The main fixed parameters used in the simulation are shown in Table III.

## A. Performance of HPQ Algorithm

We use SUMO to generate mixed random traffic flow to evaluate the performance of the proposed HPQ algorithm. To ensure the safety of vehicles at intersections, the speed limit is 13.8 m/s. The simulation scenario of the HPQ algorithm is a four-way intersection covering 200 m × 200 m, as shown in Fig. 2. We use the average number of halts, average travel time and average speed to evaluate the performance of algorithms.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-13.jpg?height=621&width=778&top_left_y=232&top_left_x=223)
Fig. 10. Comparison of the number of halts of vehicles between different algorithms at the intersection under different traffic flows (within 15min).

Vehicle stop state refers to the state when the vehicle speed is less than 1.4 m/s. In order to better evaluate the performance of the HPQ algorithm under mixed autonomy traffic streams, the simulation is carried out when the CAV penetration rates are 50\%. The simulation results within 15 minutes are used for comparison.

1) Traffic fluency: The average number of halts of vehicles under different traffic flows is calculated as shown in Fig. 10. It can be seen that both HPQ algorithm and the distributed conflict-free cooperation algorithm can greatly reduce the average number of halts of vehicles when the traffic flows are $1000 \mathrm{pcu} / \mathrm{h}$ and $1300 \mathrm{pcu} / \mathrm{h}$. However, when the traffic flow increases to 1600 pcu/h, the HPQ algorithm is significantly better than the distributed conflict-free cooperation algorithm for traffic fluency. And the HPQ algorithm is always better than the delay-time actuated traffic lights algorithm and Hybrid AIM protocol under different traffic flows. Therefore, the HPQ algorithm can effectively reduce the number of halts of vehicles and greatly improve the traffic fluency at intersections.
2) Travel time: The travel time of vehicles under different traffic flows is shown in Fig. 11. It can be seen that both HPQ algorithm and the distributed conflict-free cooperation algorithm can greatly reduce the average travel time of vehicles when the traffic flows are 1000 pcu/h and 1300 pcu/h. All vehicles can pass through the intersections efficiently in a limited time. Moreover, the HPQ algorithm reduces the average travel time by up to 34\% compared to the distributed conflictfree cooperation algorithm when the traffic flow is 1600 pcu/h. And the distributed conflict-free cooperation algorithm is more easily impacted by traffic densities. Compared with the delay-time actuated traffic lights algorithm and Hybrid AIM protocol, the HPQ algorithm can reduce the average travel time of vehicles at intersections by 22\% to 65\% under different traffic flows. The traffic light scheme seriously restrains traffic efficiency of intersections. In particular, the travel times of the HPQ algorithm at different periods and different traffic flows

TABLE IV PARAMETERS USED IN SIMULATION FOR COMPREHENSIVE SCENARIO
| Vehicle number | Vehicle type | Priority | Driving direction | Initial position | Initial speed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | CAV | 2 | Turn left | (-70 m, -1.75 m) | $9 \mathrm{~m} / \mathrm{s}$ |
| 2 | CAV | 6 | Straight | (-90 m, -1.75 m) | $9 \mathrm{~m} / \mathrm{s}$ |
| 3 | CAV | 3 | Straight | $(1.75 \mathrm{~m},-80 \mathrm{~m})$ | $9 \mathrm{~m} / \mathrm{s}$ |
| 4 | CAV | 5 | Straight | $(90 \mathrm{~m}, 1.75 \mathrm{~m})$ | $9 \mathrm{~m} / \mathrm{s}$ |
| 5 | CHV | 1 | Turn right | $(70 \mathrm{~m}, 1.75 \mathrm{~m})$ | $9 \mathrm{~m} / \mathrm{s}$ |
| 6 | CHV | 4 | Turn left | ( $-1.75 \mathrm{~m}, 85 \mathrm{~m}$ ) | $9 \mathrm{~m} / \mathrm{s}$ |


are very stable, comparing with the fluctuations of the other three algorithms. Therefore, the HPQ algorithm can effectively reduce the travel time of vehicles at intersections, so that vehicles can pass through the intersections more smoothly.
3) Average speed: To further investigate the effectiveness of the HPQ algorithm, we evaluate their performance using average vehicle speed, as shown in Fig. 12. It can be seen that vehicles under the control of the HPQ algorithm can pass through the intersection smoothly at a relatively high speed under different traffic flows. However, the speed of vehicles under the control of the other three algorithms fluctuates widely. This can be well explained since the vehicles under the control of the other three algorithms encounter a greater number of halts. The HPQ algorithm can reduce the number of halts and increase the speed of vehicles at intersections, therefore effectively improve the comfort and safety of occupants.

In general, the vehicles at the intersection under the control of the HPQ algorithm have a significant improvement in the traffic efficiency compared with the vehicles at the intersection under the control of the delay-time actuated traffic lights algorithm, the Hybrid AIM protocol and the distributed conflictfree cooperation algorithm. In addition, the performance of the HPQ algorithm is stable with different situations. Under low density traffic streams, vehicles almost do not need to slow down and stop at the intersection to avoid collision.

## B. Simulations of Vehicle Planning and Control Algorithm

Fig. 13 shows the comprehensive simulation scenario configuration. Table IV illustrates the parameters used in simulation for vehicle planning and control algorithm based on intersection coordinate system. According to the HPQ algorithm and the vehicle planning and control algorithm proposed in this paper, the control modes of all vehicles are as follows:

- Vehicle 1: Firstly, vehicle 1 obtains the right of way and switches to the conflict-solving mode to coordinate the merging conflict with vehicle 5. After vehicle 5 passed through the conflict area, vehicle 1 switches to car following mode to follow vehicle 5.
- Vehicle 2: Vehicle 2 follows vehicle 1 when entering the intersection control area. When vehicle 2 gets near the stop line, vehicle 2 switches to the waiting mode because vehicle 2 cannot get the right of way. It is not until vehicle 3 passed through the conflict area that vehicle 2 obtains the right of way and switches to the conflict-solving

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-14.jpg?height=503&width=1723&top_left_y=232&top_left_x=198)
Fig. 11. Comparison of average travel time between different algorithms at the intersection under different traffic flows. (a) Light traffic (Traffic flow = 1000 pcu/h). (b) Moderate traffic (Traffic flow = 1300 pcu/h). (c) Heavy traffic (Traffic flow = 1600 pcu/h).

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-14.jpg?height=503&width=1721&top_left_y=889&top_left_x=200)
Fig. 12. Comparison of average vehicle speed between different algorithms at the intersection under different traffic flows. (a) Light traffic (Traffic flow = 1000 pcu/h). (b) Moderate traffic (Traffic flow = 1300 pcu/h). (c) Heavy traffic (Traffic flow = 1600 pcu/h).

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-14.jpg?height=608&width=735&top_left_y=1553&top_left_x=232)
Fig. 13. Comprehensive simulation scenario configuration.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-14.jpg?height=565&width=769&top_left_y=1592&top_left_x=1134)
Fig. 14. Right of way allocation in comprehensive scenario.

mode to coordinate the merging conflict with vehicle 6. After vehicle 6 passed through the conflict area, vehicle 2 switches to car following mode to follow vehicle 6.

- Vehicle 3: When vehicle 3 enters the intersection control area, it first switches to cruise mode. When vehicle 3 is near the stop line, it will switch to the waiting mode

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-15.jpg?height=423&width=765&top_left_y=223&top_left_x=215)
Fig. 15. Control modes switching of CAVs in the comprehensive scenario.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-15.jpg?height=887&width=739&top_left_y=874&top_left_x=228)
Fig. 16. Speed profiles and acceleration profiles of CAVs and CHVs in the comprehensive scenario. (a) Speed profiles of CAVs and CHVs in the comprehensive scenario, where the blue line indicates the speed profile of the CAV and the cyan line indicates the speed profile of the CHV. (b) Acceleration profiles of CAVs and CHVs in the comprehensive scenario.

area, vehicle 3 switches to car following mode to follow vehicle 1.

- Vehicle 4: When vehicle 4 enters the intersection control area, it follows vehicle 5 first. when vehicle 4 approaches the stop line, it switches to waiting mode because it has not obtained the right of way. vehicle 4 will obtain the right of way and switch to the conflict-solving mode to coordinate the crossing conflict with vehicle 6 when vehicle 3 passed through the conflict area. After vehicle 6 passed through the conflict area, vehicle 4 switches to cruise mode.
- Vehicle 5: When vehicle 5 arrives at the intersection control area, it will obtain the right of way, and the driver will drive at a constant speed.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-15.jpg?height=889&width=735&top_left_y=236&top_left_x=1143)
Fig. 17. Relative distance and speed of vehicle 1 and vehicle 3. (a) Relative distances of vehicle 1 and vehicle 3 to the surrounding reference vehicles in different control modes. (b) Speed of vehicle 1 and vehicle 3 in different control modes.

- Vehicle 6: The driver first drives at a constant speed to the stop line and waits. Until vehicle 3 passes through the conflict area, vehicle 6 will obtain the right of way and continue to drive at a constant speed through the intersection.

During the whole simulation, the allocation of the right of way at the intersection is shown in Fig. 14. The blue bars represent the time when the vehicle is granted the right of way. We can see that vehicle 1 and vehicle 5 obtain the right of way first. The control modes switching of CAVs are shown in Fig. 15. Different colors represent different control modes of CAVs. When the color of the bar is blue, it means that the vehicle is in car following mode. We can see that vehicle 2 and vehicle 4 are in car following mode at the beginning of the simulation.

The speed profiles and acceleration profiles of CAVs and CHVs in the comprehensive simulation scenario are illustrated in Fig. 16. Fig. 16(a) depicts the speed profiles of CAVs and CHVs in the comprehensive scenario, where the blue line indicates the speed profile of the CAV and the cyan line indicates the speed profile of the CHV. Fig. 16(b) depicts the acceleration profiles of CAVs and CHVs in the comprehensive scenario. Vehicles 1-4 represent the CAVs, and vehicles 5-6 represent the CHVs. It can be seen that the speed profiles of the CAVs are smooth enough. In addition, the acceleration of the CAVs is basically kept between $-3 m / s^{2}$ and $2 m / s^{2}$, which not only ensures the safety of the vehicles, but also improves the comfort of the occupants. In contrast, the speed profile of the CHVs is slightly less smooth, and its maximum acceleration is greater than $4 m / s^{2}$. The main reason for

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-16.jpg?height=314&width=831&top_left_y=221&top_left_x=191)
Fig. 18. The scenario layout of the intersection. (a) The actual photo of the simulated intersection. (b) The simulation environment built in PreScan according to the real scene.

this is that all the CAVs near the intersection are controlled by the designed lower-level vehicle planning and control algorithm, which combines the upper-level HPQ algorithm to calculate the control modes for each CAV and uses model predictive control to control the vehicles safely, quickly and comfortably through the intersection. The car following model for the CHVs uses the classical Krauss model [56], under the assumption that humans can visually detect the distance to the vehicle ahead and drive safely to maintain a desired distance from it [6]. Thus the CAVs can achieve smooth motor behavior and improved driving comfort based on the idea of rolling optimization in model predictive control, whereas the behaviors of the CHVs are prone to more fluctuations influenced by the surrounding environment.

The relative distance and speed of vehicle 1 and vehicle 3 are shown in Fig. 17. Fig. 17(a) shows the relative distance of vehicle 1 and vehicle 3 to the surrounding reference vehicles, and Fig. 17(b) shows the speed of vehicle 1 and vehicle 3 in different control modes. It can be seen from the figure that vehicle 1 and vehicle 3 can quickly and accurately switch to the corresponding control mode designed under different traffic situations. And vehicle 1 and vehicle 3 can maintain a safe distance from surrounding vehicles at a relatively stable speed. Undisturbed switching of four control modes not only guarantees vehicle safety, but also improves the utilization rate of the conflict area of the intersection.

To better verify the effectiveness and robustness of the proposed unsignalized intersection management strategy, we conduct a larger-scale simulation considering the intersection at Shanghai Intelligent and Connected Vehicle Test Zone. The scenario layout of the intersection is shown in Fig. 18, where Fig. 18(a) is the actual photo of the simulated intersection, and Fig. 18(b) is the simulation environment built in PreScan according to the real scene in Fig. 18(a). The vehicles arrive at the intersection entrances randomly with the initial speed of 9 m/s. The right of way of the vehicles is calculated by the high-level HPQ algorithm. Then, the high-level calculation results are transmitted to the low-level vehicle terminal for vehicle planning and control. There are a total of 30 vehicles participated in the simulation.

Fig. 19 presents the arrival time of different types of vehicles approaching the intersection in different traffic movements. The circular contours indicate the different levels of arrival time, and their values are displayed in the color bar of the figure. Besides, the arrows indicate different vehicle move-

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-16.jpg?height=722&width=810&top_left_y=223&top_left_x=1117)
Fig. 19. Arrival time of approaching vehicles at three-way, one-lane irregular intersection simulations.

ments. It can be seen from Fig. 18 that there are three entry areas at the intersection, and each entry area is connected to two exit areas. The solid dots and hollow dots in Fig. 19 represent the time when the CAVs and the CHVs arrive at the intersection, respectively. The points on the same circle correspond to vehicles passing through the intersection at the same time. It can be seen from the figure that there is no conflict between vehicles passing through the intersection at the same time and all vehicles can pass through the intersection within 60 s, which proves that the unsignalized intersection management strategy can coordinate the vehicles passing the intersection safely and efficiently. In addition, the computation load required by the unsignalized intersection management strategy is small enough, so it is highly feasible to be applied to actual traffic control scenarios.

## C. Micro-simulation Validation of Mixed Autonomy Traffic Streams

To demonstrate the effectiveness of the proposed method in mixed autonomy traffic streams, we conducted microsimulations across a broader range of intersection configurations and traffic scenarios. Specifically, we constructed a digital twin simulation scenario in PreScan micro-simulation software based on the real-world four-way, three-lane intersection to demonstrate that the proposed method can be applied to many applications and problem sizes. The scenario layout of the intersection is illustrated in Fig. 20, where Fig. 20(a) is the actual photo of the case study at the intersection between Jianchuan Road and Dushi Road near Shanghai Jiao Tong University, and Fig. 20(b) is the simulation environment built in PreScan according to the real scene in Fig. 20(a). In the fourway, three-lane intersection, we conducted a comprehensive

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-17.jpg?height=404&width=840&top_left_y=223&top_left_x=187)
Fig. 20. One of the most congested intersections near Shanghai Jiao Tong University is depicted in 20(a), and the simulation environment built in PreScan, according to the real scene, is illustrated in 20(b).

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-17.jpg?height=713&width=780&top_left_y=799&top_left_x=221)
Fig. 21. Conflict relationship of traffic movements at the four-way, threelane intersection in the comprehensive simulation scenario under mixed traffic streams. Circles of the same color indicate merging conflicts between trajectories. Dashed outlines denote diversion conflicts between trajectories within the dashed box. Intersection points represent crossing conflicts between crossing trajectories.

simulation experiment of mixed traffic flow, including CAVs, CHVs, and HVs.

We use PreScan to validate the proposed unsignalized intersection management method for large-scale intersection scenarios under mixed traffic flows in microsimulation. The relationship diagram of vehicle motion conflicts in the simulation is shown in Fig. 21. From Fig. 21, it can be seen that there are three types of vehicle conflicts in this scenario: diversion conflict, crossing conflict, and merging conflict. The profile of the distance between the position of the vehicle and the center of the intersection is shown in Fig. 22. Different types of vehicles are represented by different line types. Vehicles 1-14 are CAVs. Vehicles 15-24 are CHVs. Vehicles 25-38 are HVs. The top dotted line indicates the stop line at the intersection boundary, and the bottom dotted line indicates the center of the intersection. It can be seen from Fig. 22 that most vehicles have a smooth trajectory and can safely pass through the

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-17.jpg?height=363&width=864&top_left_y=200&top_left_x=1091)
Fig. 22. Profile of the distance between the vehicle's position and the intersection's center. Different types of vehicles are represented by different line types. Vehicles 1-14 are CAVs. Vehicles 15-24 are CHVs. Vehicles 25-38 are HVs. The top dotted line indicates the stop line at the intersection boundary, and the bottom dotted line indicates the center of the intersection.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-17.jpg?height=365&width=866&top_left_y=868&top_left_x=1087)
Fig. 23. Vehicle velocity profiles in the complex intersection under mixed traffic flow. The speed profiles of CAVs exhibit smoother behavior in contrast to that of HVs, which aligns with real-world driving scenarios. Most of the vehicles pass through the intersection quickly at high speeds. Notably, CAVs proactively yield to the HVs in close proximity to the intersection to mitigate trajectory conflicts.

intersection in an orderly manner. Different types of vehicles can be effectively coordinated to pass through the intersection, and the CAVs reserve a certain safety distance for the HVs to ensure that the HVs can pass through the intersection safely. This demonstrates the robustness and effectiveness of the proposed method.

Vehicle velocity profiles in the complex intersection under mixed traffic flow are illustrated in Fig. 23. As can be seen in Fig. 23, the algorithm deduces that CAVs 1-8, which are farther away from the intersection, can accelerate to the intersection in advance switching to the car following mode or conflict-solving mode to pass through the intersection quickly. Similarly, subsequent vehicles arrive at the intersection in an orderly manner under the regulation of the proposed vehicle planning algorithm. They pass through the intersection sequentially by switching to different driving modes adaptively and without disturbance according to the vehicle planning and control algorithm.

Figs. 24-26 show the test results in the typical conflict scenario. Fig. 24 highlights the key moments of mixed traffic flow of CAVs, CHVs, and HVs by the snapshots. There is a typical conflict relationship between CAV 10, CHV 21, and HV 36. CAV 10 turns left through the intersection, and there is a merging conflict with HV 36, traveling straight

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-18.jpg?height=382&width=1736&top_left_y=208&top_left_x=185)
Fig. 24. Snapshots of the typical conflict scenario solved by the proposed unsignalized intersection management method under the mixed traffic streams of CAVs, CHVs, and HVs. Vehicles 1-14 are CAVs. Vehicles 15-24 are CHVs. Vehicles 25-38 are HVs. The red rectangles in the snapshot highlight critical moments in the mixed traffic flow of CAVs, CHVs, and HVs. There is a typical conflict relationship between CAV 10, CHV 21, and HV 36.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-18.jpg?height=361&width=866&top_left_y=812&top_left_x=176)
Fig. 25. Distance between the trajectories of the three types of vehicles to different conflict points. There are two conflict points between the three vehicles. The blue line indicates the change in distance from the vehicle to the conflict point between CAV 21 and HV 36. The cyan line indicates the change in distance from the vehicle to the conflict point between CHV 10 and HV 36.

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-18.jpg?height=363&width=866&top_left_y=1506&top_left_x=174)
Fig. 26. Profiles of velocity changes for three vehicles with conflicting spatiotemporal trajectories.

through the intersection. CHV 21 travels straight through the intersection, and there is a crossing conflict with HV 36, which is traveling straight through the intersection. As can be seen in the figure, both CAV 10 and CHV 21 made an excellent yield to prevent the trajectory conflict with HV 36. In addition, CAV 10 utilized a conflict resolution model to follow HV 36 through the intersection as quickly as possible while ensuring safe passage. Fig. 25 shows the distance between the trajectories of the three conflicting vehicles to different conflict points. There are two conflict points between the three vehicles. The blue line indicates the change in distance from the vehicle to the conflict point between CAV 21 and HV 36. The cyan line

![](https://cdn.mathpix.com/cropped/930a94ae-e21d-4506-8fb1-3ee7e92fa09a-18.jpg?height=670&width=812&top_left_y=825&top_left_x=1109)
Fig. 27. Arrival time of vehicles from different directions at the four-way, three-lane intersection in the comprehensive simulation scenario under mixed traffic streams. The circular contours indicate different levels of arrival time, and their values are shown in the figure's color bars. The solid dots, hollow dots, and plus signs with circles represent the arrival time of CAVs, CHVs, and HVs, respectively. The dots on the same circle correspond to the vehicles that pass through the intersection at the same time.

indicates the change in distance from the vehicle to the conflict point between CHV 10 and HV 36. All vehicles can pass through their respective conflict points in an orderly manner, maintaining a safe distance. Profiles of velocity changes for three vehicles with conflicting spatiotemporal trajectories are illustrated in Fig. 26. From the figure, it can be seen that all the conflicting vehicles can pass through the intersection smoothly at high speed, which proves the safety and efficiency of the proposed method in solving the conflict scenario with mixed traffic flow.

Fig. 27 shows the arrival time of different types of vehicles approaching the conflict zone of the intersection. The circular contours indicate different levels of arrival time, and their values are shown in the figure's color bars. The solid dots, hollow dots, and plus signs with circles in Fig. 27 represent the arrival time of CAVs, CHVs, and HVs, respectively. The dots on the same circle correspond to the vehicles that pass
through the intersection at the same time. From the figure, it can be seen that there is no spatiotemporal trajectory conflict between the vehicles crossing the intersection at the same time, and all the vehicles can cross the intersection within 46.9 s, and the traffic efficiency is improved. The videos of comprehensive simulation experiments under different scenarios are uploaded online. Please visit the website to view them (https://cnc.sjtu.edu.cn/HPQ/).

## VII. CONCLUSION

This paper proposes an intelligent intersection management system for mixed autonomy traffic streams, which comprehensively consists of algorithms for upper-level decision making and low-level vehicle planning and control. In the upperlevel right of way allocation, the HPQ algorithm is designed according to the difference between CAVs, CHVs, and HVs. Since CAVs can deal with intersection trajectory conflicts with the help of intelligent equipment, they are easier to obtain the right of way than CHVs. In the low-level vehicle planning and control for CAVs, four different control modes are designed, and the control execution is carried out through the model predictive controller. The application of the model predictive controller to the CAVs can realize the undisturbed switching of the control modes and satisfy the safety requirements of collision avoidance. Then SUMO is used to verify the efficiency and superiority of the proposed HPQ algorithm, which shows that the HPQ algorithm outperforms the delaytime actuated traffic lights algorithm and the Hybrid AIM protocol by decreasing the average travel time by 5\% to 65\% for different traffic flows. Moreover, the PreScan is used to conduct a microscopic simulation at the intersection, which verifies the safety and effectiveness of the proposed vehicle planning and control algorithm. Simulation results demonstrate that the proposed method can be effectively applied to large-scale traffic intersections with mixed traffic of CAVs, CHVs, and HVs, which effectively improves the intersection efficiency under the premise of ensuring traffic safety. The proposed unsignalized intersection management strategy is practical to be applied in the near future.

For future practical application deployment, challenges such as communication delay, packet loss, and pedestrian intervention need to be further considered. The problem will be more complicated when other traffic participants such as pedestrians are considered, because the interaction behaviors at the intersections are very diverse. We will further study the intelligent intersection management strategy in the presence of pedestrians and cyclists, so that the strategy can be applied to various types of public intersections.

## References

[1] H. Liu, K. Teng, L. Rai, and J. Xing, "Transit signal priority controlling method considering non-transit traffic benefits and coordinated phase states for multi-rings timing plan at isolated intersections," IEEE Trans. Intell. Transp. Syst., vol. 22, no. 2, pp. 913-936, 2021.
[2] D. Zhao, Y. Dai, and Z. Zhang, "Computational intelligence in urban traffic signal control: A survey," IEEE Trans. Syst. Man Cybern. Part C Appl. Rev., vol. 42, no. 4, pp. 485-494, 2012.
[3] P. Hang, C. Huang, Z. Hu, Y. Xing, and C. Lv, "Decision making of connected automated vehicles at an unsignalized roundabout considering personalized driving behaviours," IEEE Trans. Veh. Technol., vol. 70, no. 5, pp. 4051-4064, 2021.
[4] F. Belkhouche, "Collaboration and optimal conflict resolution at an unsignalized intersection," IEEE Trans. Intell. Transp. Syst., vol. 20, no. 6, pp. 2301-2312, 2019.
[5] R. Tian, N. Li, I. Kolmanovsky, Y. Yildiz, and A. R. Girard, "Gametheoretic modeling of traffic in unsignalized intersection network for autonomous vehicle control verification and validation," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 3, pp. 2211-2226, 2022.
[6] G. N. Bifulco, A. Coppola, A. Petrillo, and S. Santini, "Decentralized cooperative crossing at unsignalized intersections via vehicle-to-vehicle communication in mixed traffic flows," J. Intell. Transp. Syst., pp. 1-26, 2022.
[7] C. Ma, C. Yu, and X. Yang, "Trajectory planning for connected and automated vehicles at isolated signalized intersections under mixed traffic environment," Transp. Res. Part C Emerging Technol., vol. 130, p. 103309, 2021.
[8] Z. Deng, Y. Shi, Q. Han, L. Lv, and W. Shen, "A conflict duration graph-based coordination method for connected and automated vehicles at signal-free intersections," Appl. Sci., vol. 10, no. 18, p. 6223, 2020.
[9] Y.-T. Lin, H. Hsu, S.-C. Lin, C.-W. Lin, I. H.-R. Jiang, and C. Liu, "Graph-based modeling, scheduling, and verification for intersection management of intelligent vehicles," ACM Trans. Embedded Comput. Syst., vol. 18, no. 5s, pp. 1-21, 2019.
[10] M. Choi, A. Rubenecia, and H. H. Choi, "Reservation-based traffic management for autonomous intersection crossing," Int. J. Distrib. Sens. Netw., vol. 15, no. 12, p. 1550147719895956, 2019.
[11] X. Gong, B. Wang, and S. Liang, "Collision-free cooperative motion planning and decision-making for connected and automated vehicles at unsignalized intersections," IEEE Trans. Syst. Man Cybern.: Syst., pp. 1-13, 2024.
[12] H. Shu, T. Liu, X. Mu, and D. Cao, "Driving tasks transfer using deep reinforcement learning for decision-making of autonomous vehicles in unsignalized intersection," IEEE Trans. Veh. Technol., vol. 71, no. 1, pp. 41-52, 2022.
[13] S. Yan, T. Welschehold, D. Büscher, and W. Burgard, "Courteous behavior of automated vehicles at unsignalized intersections via reinforcement learning," IEEE Rob. Autom. Lett., vol. 7, no. 1, pp. 191-198, 2022.
[14] Y. Guan, Y. Ren, S. E. Li, Q. Sun, L. Luo, and K. Li, "Centralized cooperation for connected and automated vehicles at intersections by proximal policy optimization," IEEE Trans. Veh. Technol., vol. 69, no. 11, pp. 12597-12 608, 2020.
[15] M. Klimke, B. Völz, and M. Buchholz, "Automatic intersection management in mixed traffic using reinforcement learning and graph neural networks," in 2023 IEEE Intelligent Vehicles Symposium (IV), 2023, pp. 1-8.
[16] B. Qian, H. Zhou, F. Lyu, J. Li, T. Ma, and F. Hou, "Toward collisionfree and efficient coordination for automated vehicles at unsignalized intersection," IEEE Internet Things J., vol. 6, no. 6, pp. 10408-10420, 2019.
[17] W. Zhong, K. Li, J. Shi, J. Yu, and Y. Luo, "Reservation-prioritizationbased mixed-traffic cooperative control at unsignalized intersections," IEEE Trans. Intell. Veh., pp. 1-15, 2024.
[18] M. B. Mertens, J. Müller, and M. Buchholz, "Cooperative maneuver planning for mixed traffic at unsignalized intersections using probabilistic predictions," in 2022 IEEE Intelligent Vehicles Symposium (IV), 2022, pp. 1174-1180.
[19] B. Wang, X. Gong, Y. Wang, P. Lyu, and S. Liang, "Coordination for connected and autonomous vehicles at unsignalized intersections: An iterative learning-based collision-free motion planning method," IEEE Internet Things J., vol. 11, no. 3, pp. 5439-5454, 2024.
[20] Y. Li, M. Liu, Q. Yang, Z. Shen, and W. Wu, "Collision-free autonomous scheduling at unsignalized intersection using conflict graph tree search," IEEE Internet Things J., vol. 11, no. 8, pp. 14563-14578, 2024.
[21] B. Peng, M. F. Keskin, B. Kulcsár, and H. Wymeersch, "Connected autonomous vehicles for improving mixed traffic efficiency in unsignalized intersections with deep reinforcement learning," Commun. Transp. Res., vol. 1, p. 100017, 2021.
[22] Z. Deng, K. Yang, W. Shen, and Y. Shi, "Cooperative platoon formation of connected and autonomous vehicles: Toward efficient merging coordination at unsignalized intersections," IEEE Trans. Intell. Transp. Syst., pp. 1-15, 2023.
[23] A. Zhou, S. Peeta, M. Yang, and J. Wang, "Cooperative signal-free intersection control using virtual platooning and traffic flow regulation," Transp. Res. Part C Emerging Technol., vol. 138, p. 103610, 2022.

[24] Y. Xu, H. Zhou, T. Ma, J. Zhao, B. Qian, and X. Shen, "Leveraging multiagent learning for automated vehicles scheduling at nonsignalized intersections," IEEE Internet Things J., vol. 8, no. 14, pp. 11 427-11 439, 2021.
[25] B. Xu, S. E. Li, Y. Bian, S. Li, X. J. Ban, J. Wang, and K. Li, "Distributed conflict-free cooperation for multiple connected vehicles at unsignalized intersections," Transp. Res. Part C: Emerg. Technol., vol. 93, pp. 322-334, 2018.
[26] C. Chen, Q. Xu, M. Cai, J. Wang, J. Wang, and K. Li, "Conflict-free cooperation method for connected and automated vehicles at unsignalized intersections: Graph-based modeling and optimality analysis," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 11, pp. 21 897-21 914, 2022.
[27] C. Chen, Q. Xu, M. Cai, J. Wang, B. Xu, X. Wu, J. Wang, K. Li, and C. Qi, "A graph-based conflict-free cooperation method for intelligent electric vehicles at unsignalized intersections," in Proc. IEEE 24th Int. Conf. Intell. Transp. Syst., 2021, pp. 52-57.
[28] Q. Ma, S. Zhang, and Q. Zhou, "Development of a conflict-free unsignalized intersection organization method for multiple connected and autonomous vehicles," Plos one, vol. 16, no. 3, p. e0249170, 2021.
[29] L. Li and F. Wang, "Cooperative driving at blind crossings using intervehicle communication," IEEE Trans. Veh. Technol., vol. 55, no. 6, pp. 1712-1724, 2006.
[30] Y. Bian, S. E. Li, W. Ren, J. Wang, K. Li, and H. X. Liu, "Cooperation of multiple connected vehicles at unsignalized intersections: Distributed observation, optimization, and control," IEEE Trans. Ind. Electron., vol. 67, no. 12, pp. 10744-10754, 2020.
[31] J. Huang, Z. Wu, W. Xue, D. Lin, and Y. Chen, "Non-cooperative and cooperative driving strategies at unsignalized intersections: A robust differential game approach," IEEE Trans. Intell. Transp. Syst., pp. 1-15, 2024.
[32] M. Cai, Q. Xu, C. Chen, J. Wang, K. Li, J. Wang, and X. Wu, "Multilane unsignalized intersection cooperation with flexible lane direction based on multi-vehicle formation control," IEEE Trans. Veh. Technol., vol. 71, no. 6, pp. 5787-5798, 2022.
[33] M. Khayatian, M. Mehrabian, E. Andert, R. Dedinsky, S. Choudhary, Y. Lou, and A. Shirvastava, "A survey on intersection management of connected autonomous vehicles," ACM Trans. Cyber-Phys. Syst., vol. 4, no. 4, pp. 1-27, 2020.
[34] Q. Jin, G. Wu, K. Boriboonsomsin, and M. Barth, "Platoon-based multiagent intersection management for connected vehicle," in Proc. IEEE 16th Int. Conf. Intell. Transp. Syst., 2013, pp. 1462-1467.
[35] M. Bashiri, H. Jafarzadeh, and C. H. Fleming, "Paim: Platoon-based autonomous intersection management," in Proc. IEEE 21st Int. Conf. Intell. Transp. Syst., 2018, pp. 374-380.
[36] P. Bansal and K. M. Kockelman, "Forecasting americans' long-term adoption of connected and autonomous vehicle technologies," Transp. Res. Part A Policy Pract., vol. 95, pp. 49-63, 2017.
[37] K. Dresner and P. Stone, "A multiagent approach to autonomous intersection management," J. Artif. Intell. Res., vol. 31, pp. 591-656, 2008.
[38] K. M. Dresner and P. Stone, "Sharing the road: Autonomous vehicles meet human drivers," in Proc. 20th IJCAI, 2007, pp. 1263-1268.
[39] G. Sharon and P. Stone, "A protocol for mixed autonomous and humanoperated vehicles at intersections," in Proc. Int. Conf. Auton. Agents Multiagent Syst., 2017, pp. 151-167.
[40] P. Lin, J. Liu, P. J. Jin, and B. Ran, "Autonomous vehicle-intersection coordination method in a connected vehicle environment," IEEE Intell. Transp. Syst. Mag., vol. 9, no. 4, pp. 37-47, 2017.
[41] W. Zhao, D. Ngoduy, S. Shepherd, R. Liu, and M. Papageorgiou, "A platoon based cooperative eco-driving model for mixed automated and human-driven vehicles at a signalised intersection," Transp. Res. Part C: Emerg. Technol., vol. 95, pp. 802-821, 2018.
[42] S. Aoki and R. Rajkumar, "V2v-based synchronous intersection protocols for mixed traffic of human-driven and self-driving vehicles," in Proc. IEEE 25th Int. Conf. Embedded Real-Time Comput. Syst. Appl., 2019, pp. 1-11.
[43] H. Yu, R. Jiang, Z. He, Z. Zheng, L. Li, R. Liu, and X. Chen, "Automated vehicle-involved traffic flow studies: A survey of assumptions, models, speculations, and perspectives," Transp. Res. Part C Emerging Technol., vol. 127, p. 103101, 2021.
[44] V. Kanagaraj, G. Asaithambi, C. N. Kumar, K. K. Srinivasan, and R. Sivanandan, "Evaluation of different vehicle following models under mixed traffic conditions," Procedia-Social and Behavioral Sciences, vol. 104, pp. 390-401, 2013.
[45] W. Lim, S. Lee, M. Sunwoo, and K. Jo, "Hybrid trajectory planning for autonomous driving in on-road dynamic scenarios," IEEE Trans. Intell. Transp. Syst., vol. 22, no. 1, pp. 341-355, 2021.
[46] J. Nilsson, M. Brännström, J. Fredriksson, and E. Coelingh, "Longitudinal and lateral control for automated yielding maneuvers," IEEE Trans. Intell. Transp. Syst., vol. 17, no. 5, pp. 1404-1414, 2016.
[47] Z. Shen, A. Mahmood, Y. Wang, and L. Wang, "Coordination of connected autonomous and human-operated vehicles at the intersection," in Proc. IEEE/ASME Int. Conf. Adv. Intell. Mechatron., 2019, pp. 1391-1396.
[48] A. I. Morales Medina, N. van de Wouw, and H. Nijmeijer, "Cooperative intersection control based on virtual platooning," IEEE Trans. Intell. Transp. Syst., vol. 19, no. 6, pp. 1727-1740, 2018.
[49] M. Makridis, K. Mattas, and B. Ciuffo, "Response time and time headway of an adaptive cruise control. an empirical characterization and potential impacts on road capacity," IEEE Trans. Intell. Transp. Syst., vol. 21, no. 4, pp. 1677-1686, 2020.
[50] G. M. Hoffmann, C. J. Tomlin, M. Montemerlo, and S. Thrun, "Autonomous automobile trajectory tracking for off-road driving: Controller design, experimental validation and racing," in Proc. 26th Amer. Control Conf., 2007, pp. 2296-2301.
[51] Y. He, X. Tian, J. Shen, C. Yuan, and Y. Du, "Robust stabilization of longitudinal tracking for cooperative adaptive cruise control considering input saturation," Mod. Phys. Lett. B, vol. 34, no. 35, p. 2050409, 2020.
[52] N. Chen, B. van Arem, T. Alkim, and M. Wang, "A hierarchical model-based optimization control approach for cooperative merging by connected automated vehicles," IEEE Trans. Intell. Transp. Syst., vol. 22, no. 12, pp. 7712-7725, 2020.
[53] P. A. Lopez, M. Behrisch, L. Bieker-Walz, J. Erdmann, Y.-P. Flötteröd, R. Hilbrich, L. Lücken, J. Rummel, P. Wagner, and E. Wießner, "Microscopic traffic simulation using sumo," in Proc. IEEE 21st Int. Conf. Intell. Transp. Syst., 2018, pp. 2575-2582.
[54] R. Oertel and P. Wagner, "Delay-time actuated traffic signal control for an isolated intersection," in Proc. 90th Annu. Meeting Transp. Res. Board, 2011.
[55] M. Tideman, "Scenario-based simulation environment for assistance systems," ATZautotechnology, vol. 10, no. 1, pp. 28-32, 2010.
[56] S. Krauß, P. Wagner, and C. Gawron, "Metastable states in a microscopic model of traffic flow," Phys. Rev. E, vol. 55, no. 5, p. 5597, 1997.


[^0]:    This work was supported by the National Key R\&D Program of China with No. 2023YFB4706802, and the National Natural Science Foundation of China with No. 62373245 and 62336005, and in part by the "Dawn" Program of Shanghai Ed. (Corresponding author: Lin Wang.)

    Junjie Zhou, Zhaokun Shen and Lin Wang are with the Department of Automation, Shanghai Jiao Tong University, and Key Laboratory of System Control and Information Processing, Ministry of Education of China, Shanghai 200240, China (e-mail: junjie_zhou@sjtu.edu.cn; szk951124@sjtu.edu.cn; wanglin@sjtu.edu.cn).

    Xiaofan Wang is with the Department of Automation, Shanghai Jiao Tong University, the School of Mechatronic Engineering and Automation, Shanghai University, and the School of Electrical and Electronic Engineering, Shanghai Institute of Technology, Shanghai, 201418, China (e-mail: xfwang@sjtu.edu.cn).

