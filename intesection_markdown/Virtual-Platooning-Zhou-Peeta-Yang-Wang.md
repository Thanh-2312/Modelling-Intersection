# Cooperative Signal-free Intersection Control using Virtual Platooning and Traffic Flow Regulation 

Anye Zhou<br>School of Civil and Environmental Engineering<br>Georgia Institute of Technology<br>790 Atlantic Drive<br>Atlanta, GA 30332<br>Email: azhou46@gatech.edu<br>Srinivas Peeta (Corresponding Author)<br>School of Civil and Environmental Engineering<br>H. Milton Stewart School of Industrial and Systems Engineering<br>Georgia Institute of Technology<br>790 Atlantic Drive<br>Atlanta, GA 30332<br>Tel: (404)894-2243<br>Email: peeta@gatech.edu<br>Menglin Yang<br>Jiangsu Key Laboratory of Urban ITS<br>School of Transportation<br>Southeast University<br>Si Pai Lou \#2<br>Nanjing, China, 210096<br>Email: mlyang @ seu.edu.cn<br>Jian Wang<br>School of Transportation<br>Southeast University<br>Nanjing, China, 210096<br>Email: jianw@seu.edu.cn


#### Abstract

The emerging technologies of connectivity and automation enable the potential for signal-free intersection control. In this context, virtual platooning is posited to be an innovative, decentralized control strategy that maps two-dimensional vehicle movements onto a one-dimension virtual platoon to enable intersection operations. However, the effectiveness of virtual platooning-based control can be limited or degraded by parametric inaccuracies and unparameterized disturbances in vehicle dynamics, heavy traffic congestion, and/or uncoordinated platoons in multi-lane intersections. To explicitly address these limitations, this study proposes a hybrid cooperative intersection control framework consisting of microscopic-level virtual platooning control and macroscopic-level traffic flow regulation for traffic environments with connected autonomous vehicles. In virtual platooning control, vehicles approaching an intersection are organized into coordinated independent virtual platoons to avoid potential conflicts triggered by platoon formation changes. Through coordination, vehicles in a platoon are grouped into compatible passing sets to maintain desired safe spacing when proceeding through the intersection. We propose a distributed adaptive sliding mode controller (DASMC) which uses the backstepping control method and model reference adaptive control method to address parametric inaccuracies, and the sliding mode control method to consistently suppress the negative effects of the unparameterized disturbances. Each vehicle approaching the intersection utilizes the kinematic information from neighboring vehicles to implement the DASMC in a distributed manner such that vehicles within the same virtual platoon can achieve consensus safely. However, virtual platooning control cannot preclude excessive traffic from approaching the intersection, which can cause undesired spillbacks and degrade intersection control performance. To address this issue, traffic flow regulation is integrated with the virtual platooning control using an iterative feedback loop mechanism. In each iteration of the iterative feedback loop, a constrained finite-time optimal control (CFTOC) problem is solved to determine the optimal input flow permitted to proceed through the intersection, and the virtual platooning control provides feedback on the queue status to the CFTOC to initiate the next iteration. The effectiveness of the proposed intersection control framework is evaluated through numerical experiments. The results indicate that the proposed virtual platooning DASMC controller can mitigate the effects of parametric inaccuracies and unparameterized disturbances to achieve consensus for approaching vehicles, as well as guarantee string stability. Further, the proposed framework can alleviate traffic spillbacks and travel delays effectively through traffic flow regulation.


Keywords: cooperative signal-free intersection control, connected and autonomous vehicle, virtual platooning control, adaptive sliding mode control, constrained optimal control.

## 1. Introduction

### 1.1. Background and motivation

As traffic intersections can involve multiple vehicle movement conflicts, intersection control significantly impacts safety, mobility, and energy consumption in congested urban networks. Currently, traffic signals are commonly used to regulate traffic flow at intersections, and traffic signal control strategies range from fixed-time signal control (Ceylan and Bell, 2004) to real-time adaptive signal control (Robertson and Bretherton, 1991; Cai et al., 2009; Feng et al., 2015; Genders and Razavi, 2019). However, human factors and behaviors associated with drivers cause start-up loss time, clearance loss time, and underutilization of space in the intersection. Consequently, current signal control strategies involving human-driven vehicles may have limits related to intersection performance effectiveness.

Through the advent of connected and autonomous technologies, connected autonomous vehicles (CAVs) can leverage connectivity and platooning capabilities. They can receive traffic-related information from the ambient traffic through vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communications. They can leverage this situational awareness of traffic conditions/events to react more efficiently, providing significant promise to enhance the performance of traffic operations (Horowitz and Varaiya, 2000; Talebpour and Mahmassani, 2016; McAuliffe et al., 2018). In a CAV traffic environment, signal-free
intersection control can be implemented in which the CAVs communicate with the intersection controller (that integrates roadside computing units and communication devices) and/or other approaching vehicles to determine their own movements at the intersection.

The literature on signal-free intersection control can be categorized into centralized and decentralized methods. In the centralized method, the intersection controller gathers information from all incoming vehicles to coordinate the passing sequence and organizes the spatiotemporal movements of vehicles. For example, Xu et al. (2019) propose a centralized cooperative intersection driving strategy using Monte Carlo Tree Search and some heuristic rules to obtain a nearly global-optimal passing order, which minimizes the total time delay, and further demonstrates the tradeoff between performance and computational flexibility. Dresner and Stone (2008) develop a multi-agent reservation-based intersection control method for autonomous vehicles, in which a centralized controller grants or rejects the requests from incoming vehicles to proceed through the intersection based on the first-come-first-serve (FCFS) policy. Similarly, Levin and Rey, (2017) introduce a time-path reservation method to separate the vehicles at conflict points, in which the intersection controller uses information from approaching vehicles to optimize the vehicle arrival time. Lee and Park (2012) propose a centralized cooperative intersection control method that minimizes the total length of overlapping trajectories of all approaching vehicles in the conflict region by using a genetic algorithm and an auxiliary recovery mode to search for collision-free solutions. While the centralized method can achieve the objectives of the intersection controller effectively due to its systems perspective, it entails powerful and efficient computational resources to calculate the trajectories of all approaching vehicles, which can be difficult in practice. Further, as the intersection controller communicates with all approaching vehicles, the substantial ongoing V2I communications can lead to reliability issues under heavy traffic conditions due to interference (Kim et al., 2017) and information congestion (Wang et al., 2018). Very importantly, substantial ongoing communications can trigger information packet losses and communication failures (Wang et al., 2018, 2020), which can drastically deteriorate the performance of the centralized control strategy. To significantly improve computational efficiency for intersection control, distributed optimization algorithms (Boyd and Sastry, 1986; Cao et al., 2013) that leverage distributed computing architectures have been applied to centralized control methods. However, they do not address the communication reliability issues as the centralized intersection controller still needs to consistently communicate with all vehicles to obtain the requisite information and deliver control decisions.

By contrast, decentralized methods use distributed control in which each vehicle operates using its own distributed controller to derive control decisions (which alleviates the computational burden) and only communicates with vehicles in its vicinity (which can appreciably reduce communication burden). Specifically, during the distributed intersection control process, each vehicle cooperatively regulates its trajectory based on kinematic information (i.e., position, speed, acceleration) from vehicles in its vicinity such that all vehicles can achieve consensus (i.e., traveling at a desired speed and maintaining desired safe spacings) and proceed through the intersection without collision. Distributed intersection control can be classified into trajectory planning-based and virtual platooning control methods. The trajectory planning-based method determines the trajectory of each vehicle (e.g., accelerations, speeds in future time steps) to enable safe traffic operations. For instance, Campos et al. (2014) propose a receding horizon-based distributed trajectory planning method, where vehicles solve local optimization problems to obtain collision-free trajectories. Mirheli et al. (2019) introduce a distributed trajectory planning method using mixed-integer nonlinear programming, in which vehicles utilize the kinematic information from neighboring vehicles and iteratively design a near-optimal conflict-free trajectory to minimize individual travel time. However, the trajectory planning-based method does not factor realistic vehicle dynamics to control vehicle movements, and solely relies on an extra low-level controller on each vehicle to track and realize the planned trajectory. Correspondingly, in real-world implementation, the performance of the trajectory planning method is significantly influenced by the performance of the low-level controller.

Virtual platooning control (Masi et al., 2018; Medina et al., 2015; Medina et al., 2018; Xu et al., 2018; Chen et al., 2021a) is a distributed intersection control method that leverages platoon control strategies. As these strategies are synergistic with CAV capabilities, this study uses virtual platooning control to enable vehicles to safely pass through the intersection cooperatively. The method addresses the aforementioned
drawbacks of the centralized methods related to computational burden and communication failures. In virtual platooning control, the two-dimensional vehicular movements at an intersection are mapped or projected onto a one-dimensional virtual platoon based on the spacing to the geometric center of the intersection and the passing sequence policy (e.g., FCFS). As illustrated in Fig. 1, all approaching vehicles are projected onto a one-dimensional platoon illustrated by the bold black line, where the position slots indicate the feasible slots to assemble non-conflicting vehicles (e.g., vehicles 1 and 2) so that they can converge to the same position and proceed through the intersection simultaneously. Vehicles with conflicting relationships (e.g., vehicles 6 and 7) are mapped to different position slots to enable carfollowing behavior to maintain a collision-free spacing. After projecting vehicles onto a one-dimensional platoon, virtual platooning control applies platoon control strategies to implement the distributed controllers for regulating the movement of approaching vehicles.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-04.jpg?height=733&width=1085&top_left_y=733&top_left_x=539)
Fig 1. Vehicle projection in the virtual platoon

Platoon control strategies can be categorized as: (i) graph theory-based strategies (Fax and Murray, 2004; Xu et al., 2018; Zheng et al., 2016), which utilize the topological matrix to analyze the closed-loop platoon dynamics; (ii) cascaded linear control-based strategies (Naus et al., 2010; Ploeg et al., 2014; Gong et al., 2019; Wang et al., 2020), which cascade a series of linear controllers using vehicle kinematic information; (iii) optimal control-based strategies (Gong et al., 2016; Zhou et al., 2017, 2019), which cooperatively optimize the control decisions based on the performance metrics of platoon control; and (iv) nonlinear control-based strategies (Kwon and Chwa, 2014; Wu et al., 2016, 2019; Xu et al., 2018), which apply nonlinear control techniques to reduce the effects of parametric inaccuracies and unparameterized disturbances in the vehicle dynamics model (i.e., the ordinary differential equations describing vehicle longitudinal motion), and control vehicles to reach consensus cooperatively. Note that here parametric inaccuracies refer to inaccurate vehicle parameters including the vehicle weight and powertrain lag factor used to describe vehicle longitudinal motion, and the rolling resistance and air drag coefficients used to compute physical resistance that vehicles encounter during operation. These vehicle parameters can be inaccurate because of imperfect identification of vehicle dynamics and varying operating conditions (e.g., number of onboard passengers, powertrain settings). The unparameterized disturbances here refer to the effects that are difficult to explicitly model (e.g., varying road grade, tire dynamics, vehicle transmission loss) in the vehicle dynamics model, and thus are typically accounted for using an unparameterized drift term in the model. Through carefully tuned distributed controllers, virtual platooning control can achieve the following desired properties: (i) harmonizing vehicle speeds to create uniform traffic flow, (ii) damping traffic oscillations to mitigate shockwave propagation upstream on the intersection approaches, and (iii) efficiently utilizing the space in the conflict zone (i.e., the red rectangle shown in Fig. 1, where vehicle
trajectories can intersect) to ensure safety and improve throughput.
Existing virtual platooning control methods (and other distributed intersection control methods) have gaps that limit their effectiveness in the real world. The first gap relates to the vehicle dynamics model. The existing methods depend on an explicitly identified vehicle dynamics model to accomplish the desired control performance, as vehicles need to accurately track planned trajectories or respond to control decisions. To the best of our knowledge, most studies use over-simplified second-order vehicle dynamics models (i.e., treat vehicles as unrealistic point masses) (Masi et al., 2018; Mirheli et al., 2019; Chen et al., 2021a), or idealized third-order vehicle dynamics models (i.e., describing internal powertrain delay) (Medina et al., 2018; Xu et al., 2018) with no consideration of parametric inaccuracies, unparameterized disturbances or physical resistance. These assumptions are restrictive as vehicles will inevitably encounter unparameterized disturbances and physical resistance in the real world, and the associated nonlinear effects will not be captured in the control process. Additionally, obtaining accurate vehicle parameters in the real world could be difficult. This is problematic because control decisions based on an erroneous vehicle dynamics model will be inaccurate, leading to safety issues. The second gap is that the existing literature on virtual platooning control considers only simple intersections or roundabouts with only one lane on each approach (Masi et al., 2018; Medina et al., 2015, 2018; Xu et al., 2018). However, multi-lane intersection approaches are common in urban traffic networks. Therefore, a control framework that can address more general scenarios, including complex intersections with multi-lane approaches, is essential for real-world implementation. The third gap is based on an inherent drawback of distributed control methods in that vehicles can only utilize instantaneous information from the neighboring vehicles. Thereby, platooning strategies based on limited information can lead to myopic scheduling issues, and the lack of global traffic information can cause platoon coordination solutions to deviate from the system optimal ones. In particular, the distributed control method suffers from performance degradation when the incoming traffic demand exceeds the intersection capacity (i.e., oversaturated traffic conditions) because approaching vehicles are not aware of potential traffic spillbacks as only kinematic information is provided through V2V communications. Then, persistent queues at the intersection approaches can significantly limit the effectiveness of the intersection control method (due to inefficient stop-and-go conditions).

### 1.2. Proposed framework and approach

To address the aforementioned three gaps, this study develops a hybrid cooperative signal-free intersection control framework for a multi-lane intersection in a CAV traffic environment, which accounts for parametric inaccuracies, unparameterized disturbances and physical resistance in the vehicle dynamics model, and incorporates traffic flow regulation to optimize system performance. Specifically, the proposed intersection control framework consists of two levels: (i) macroscopic-level traffic flow regulation which relies on the intersection controller to prevent excessive traffic from entering the intersection and to alleviate spillback, and (ii) microscopic-level virtual-platooning intersection control which depends on the distributed controller equipped in each individual vehicle to move vehicles through the intersection safely. It is implemented using an iterative feedback loop mechanism, as illustrated in Fig. 2. The iterative feedback loop starts from the traffic flow regulation, where the intersection controller determines the optimal input flows for each intersection approach to minimize the total queue length for the current operational time horizon (the time duration of each loop, in the order of a minute or a few minutes), based on the current traffic status (the exogenous traffic demand and queue length) and the capacities of exit lanes. Next, through V2I communications, the intersection controller will inform incoming vehicles whether they can proceed through the intersection, and organize them into virtual platoons with certain passing sequences. The virtual-platooning intersection control will then operate (based on the distributed controller of each vehicle and V2V communications) for that operational time horizon, and vehicles will provide information on their states (e.g., positions, speeds, and accelerations) to the intersection controller via V2I communications so that it can compute queue lengths and the capacities of exit lanes (i.e., the lanes that vehicles depart to, as labeled in Fig. 1). Then, the iteration counter is updated to initialize the next iteration, and the exogenous traffic demand is correspondingly measured for that iteration.

The proposed framework entails addressing three important challenges. The first challenge corresponds
to the first gap, which is to account for physical resistance, parametric inaccuracies, and unparameterized disturbances in the virtual platooning control. Ideally, if unparameterized disturbances do not exist and vehicle parameters are explicitly known, output feedback linearization and backstepping control methods (Khalil, 2002) can be used to fully negate the effects of physical resistance, and then cooperative control decisions can be applied to stabilize the vehicle platoon. However, due to the inevitable existence of parametric inaccuracies and unparameterized disturbances, it is difficult to fully circumvent the impacts of physical resistance. Hence, we use backstepping control (Khalil, 2002), model reference adaptive control (Parks, 1966), and sliding mode control (Young et al., 1999) methods here to develop a distributed adaptive sliding mode controller (DASMC) to proactively address the parametric inaccuracies and unparameterized disturbances. Specifically, the smooth projection-based parameter adaptation law in adaptive control can estimate the vehicle parameters effectively to ensure stability and convergence at the steady state, while the robust control decisions derived using the sliding mode control method (Young et al., 1999) can consistently suppress the negative effects (e.g., undesired overshoot and undershoot in the transient response) of unparameterized disturbances and physical resistance. Thereby, a combination of adaptive and robust control methods can improve the steady-state and transient responses (Yao and Tomizuka, 1997), which alleviates the overshoots/undershoots and ensures that vehicle states converge to specific values faster. Moreover, as the estimated vehicle parameters are not constant in the beginning stages of control, the variations of estimated vehicle parameters in the control decisions induce a time-varying closed-loop control system, precluding the use of the traditional Lyapunov function and LaSalle's invariant principle to analyze local stability. Hence, we apply Lyapunov function analysis with Barbalat's lemma (Khalil, 2002) to guarantee the local stability, implying vehicles can reach to platoon consensus safely. Further, we use the strict frequency-domain string stability criterion (Feng et al., 2019; Naus et al., 2010) for the sliding phase of the DASMC to derive a string-stable parametric restriction to prevent the spacing error (i.e., the difference between actual spacing and desired safe spacing) from being amplified upstream of the intersection approaches. Also, in this study, the control decision of virtual platooning control refers to the driving force of the vehicle (Kwon and Chwa, 2014; Wu et al., 2016).

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-06.jpg?height=645&width=1506&top_left_y=1439&top_left_x=314)
Fig 2. Iterative feedback loop mechanism

The second challenge corresponds to the second gap, which is to coordinate virtual platoons (i.e., organize vehicles into specific virtual platoons by determining desired safe spacings) for multi-lane intersections. In this study, the desired safe spacing refers to the spacing that will ensure that no collision occurs between two conflicting vehicles. As multi-lane intersections are characterized by multiple conflicting vehicle movements, the complexity in finding desired safe spacings to organize virtual platoons is significantly higher than for single-lane intersections. Moreover, as vehicles cooperatively pass through the intersection as a virtual platoon, vehicles continuously impact movements of neighboring vehicles. To
avoid situations where vehicles arriving later impact vehicles arriving earlier (discussed in Section 3.1), there is a need to group vehicles into independent virtual platoons. Two virtual platoons are independent if the vehicle at the tail of a virtual platoon (consisting of vehicles that arrive earlier) does not receive or use kinematic information from the first vehicle of the immediate successor virtual platoon (consisting of vehicles that arrive later) to devise control decisions. We first group the approaching vehicles into several independent virtual platoons based on their arrival times. Then, within a virtual platoon, non-conflicting vehicles are grouped into a compatible passing set. Next, the desired safe spacing between two compatible passing sets is determined using the Manhattan spacing (discussed in Section 3.3) with respect to the conflict points (i.e., the points located in the conflict zone where conflicting vehicles will collide) to guarantee that no collisions will occur. In addition, as the information flow topology (IFT) plays an important role in platoon control (Li et al., 2015; Wang et al., 2020; Zhou et al., 2020), we design the IFT among vehicles based on the property of structural controllability (Lin, 1974; Liu and Barabási, 2016) so that the virtual platoon can be fully controlled (i.e., all vehicles can their reach desired positions to maintain desired safe spacing).

The third challenge relates to addressing the myopic scheduling of virtual platooning control, which lies in integrating the macroscopic-level traffic flow regulation and the microscopic vehicle-level virtual platooning control to regulate the traffic entering the intersection. First, the capacity of each exit lane is needed to implement the traffic flow regulation at the intersection. However, the different combinations of vehicle directions, spacings and speed variations in the virtual platooning control process can lead to variability in the exit lane capacity, which is difficult to obtain analytically. Second, as the virtual platooning control coordinates the movement of individual vehicles (using distributed controllers) at the microscopic level, and the traffic flow regulation to control the input flow (i.e., the traffic volume entering the intersection) is performed macroscopically, the different formulations and control outputs lead to substantial difficulty in connecting these two levels using an explicit analytical approach. The proposed iterative feedback loop mechanism in Fig. 2 aims to circumvent these two difficulties to adjust the outputs of the traffic flow regulation (i.e., optimal input flows entering the intersection). Specifically, in each iteration of the iterative feedback loop, the capacities of exit lanes are updated and information on the queues generated from virtual platooning control is provided to the intersection controller. Through this mechanism, the traffic flow regulation adapts to the varying queue characteristics and traffic demand. The traffic flow regulation is formulated using the constrained finite-time optimal control (CFTOC) method and optimizes the intersection input flows over the operational time horizon.

The major contributions of this study are threefold. First, the proposed framework enables incoming vehicles to be grouped into independent virtual platoons to assure smooth and safe progress through the multi-lane intersection. In this context, the algorithms to search for compatible passing sets and desired safe spacings can efficiently organize vehicles with complex conflicting relationships in virtual platoons. Second, to factor physical resistance, unparameterized disturbances and parametric inaccuracies in the vehicle dynamics model, we integrate methods from backstepping control, model reference adaptive control (Parks, 1966) and sliding mode control to design the DASMC to proactively suppress their negative effects to improve both steady-state and transient responses. Further, through appropriate tuning of weighting coefficients, string stability is enabled in the virtual platooning control, which ensures that speed fluctuations will not be amplified upstream of each intersection approach. Third, the proposed framework bridges macroscopic flow regulation and microscopic vehicle-level control to enhance the distributed intersection control performance. The traffic flow regulation connects to the virtual platooning control through an iterative feedback loop to adaptively determine the optimal intersection input flows. Through the iterative feedback loop mechanism, traffic spillbacks and delays can be alleviated for saturated traffic conditions, unlike in the absence of traffic flow regulation. Importantly, the proposed framework addresses the intersection control problem in a holistic way. The virtual platooning control projects the 2-dimensional intersection operation into the 1-dimensional platoon control problem which considers vehicle movements in all directions simultaneously, and further cooperatively adjusts the vehicle movements to ensure smooth operations. Compared to traditional signalized intersection control methods that manage vehicle movements in various directions separately (which can cause more stop-and-go situations), virtual
platooning control can improve the traffic flow efficiency appreciably as illustrated by the numerical experiments. Further, traffic flow regulation also empowers the proposed control framework to be flexible and robust for increasing traffic demand.

The remainder of the paper is organized as follows. Section 2 describes the problem of interest for a multi-lane intersection. Section 3 describes the approach to coordinate the vehicles in the virtual platoons. Section 4 articulates the control design and stability analysis for the virtual platoon. Section 5 formulates the traffic flow regulation and links it to the virtual platooning control. Section 6 discusses numerical experiments and analyzes the results. Section 7 provides some concluding comments and future directions.

## 2. Problem description for multi-lane intersection

We consider a multi-lane intersection with four approaches to illustrate the proposed cooperative decentralized intersection control framework. As shown in Fig. 3, each entrance leg of the intersection has three lanes: one left-turn lane, one straight-through lane, and one straight-through/right-turn lane, while each exit leg contains two lanes. This intersection configuration is selected because it contains both protected and permitted turning movements that are common in urban networks. Based on the intersection configuration, we define a set of vehicle movements: $\mathrm{s}=\{1,2, \ldots, 16\}$ to describe the travel direction of each approaching vehicle (as labeled in Fig. 3). Correspondingly, we set up a conflict set $S_{\mathrm{s}_{i}}$ for each vehicle movement $\mathrm{s}_{i} \in \mathrm{~s}$ to store its conflicting directions for use in coordinating virtual platoons (Table A in Appendix A shows the conflict set). In this study, we constrain vehicles with turning movements to only enter the closest exit lane (e.g., exit lane 2 is for vehicles with movement 5 , exit lane 5 is for vehicles with movement 8). A vehicle with straight-through movement will enter the exit lane that is aligned with the entrance lane it travels from (e.g., exit lane 6 is for vehicles with movement 2 ). Note that the proposed framework can be generalized for other intersection configurations by modifying the conflict sets and desired safe spacings.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-08.jpg?height=711&width=808&top_left_y=1369&top_left_x=660)
Fig. 3. Intersection configuration

The intersection is conceptually divided into three zones as shown in Fig. 4: (i) the conflict zone (the central purple rectangle) where potential conflicting movements can occur, (ii) the cooperative zone (the inner blue ellipse) where vehicles execute virtual platooning control, and (iii) the buffer zone (the outer green loop) where vehicles are assigned to a specific virtual platoon and the IFT for each platoon is then constructed (by informing each vehicle on the other vehicles it should communicate with). Additionally, four virtual gates (red bars) are set up at the boundary of the buffer zone corresponding to the four approaches to hold excessive traffic and prevent it from proceeding to the buffer zone. The mechanism of
the virtual gate is similar to ramp metering (Kotsialos et al., 2001; Kotsialos and Papageorgiou, 2004) applied to the highway entrance, and traffic metering in urban street networks (Mohebifard and Hajbabaie, 2018). For implementation in the future pure CAV environment, the virtual gate is a location at the boundary of the buffer zone where the intersection controller informs approaching vehicles whether to proceed forward (through V2I communications). Related to infrastructure design, a virtual gate can be specified using traffic signage or lane markings analogous to ramp metering.

The tasks conducted by the approaching vehicles and the intersection controller in the different intersection zones are summarized as follows. As vehicles approach the virtual gate, they inform the intersection controller of their arrival time using V2I communications. Then, the intersection controller performs traffic flow regulation and counts the number of arriving vehicles, and informs each vehicle (using V2I communications) on whether it can proceed to the buffer zone. After crossing the boundary of the buffer zone, vehicles send information on their speeds, arrival times, and origin-destination (OD) information (i.e., from entrance lane to exit lane) to the intersection controller using V2I communications. Then, the intersection controller assigns each vehicle to a specific virtual platoon, constructs the IFT for each virtual platoon, and provides desired safe spacing between vehicles to enable virtual platooning control. In the cooperative and conflict zones, neighboring vehicles exchange kinematic information using V2V communications to implement virtual platooning control so that vehicles pass through the intersection safely. Note that in this study we assume that no communication failure or delay occurs, and all vehicles can track their trajectories accurately. Also, we assume that all lane-changing maneuvers have been completed before the initialization of virtual platooning control, and the ambient traffic information (i.e., queue lengths, traffic demand, turning ratios) can be accurately estimated or measured during the intersection control process.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-09.jpg?height=733&width=1285&top_left_y=1218&top_left_x=421)
Fig. 4. Intersection zones

## 3. Coordination of virtual platoon

This section discusses the set of steps to coordinate the organization of approaching vehicles into virtual platoons. A capability for V2I communications is essential for coordinating virtual platoons because each approaching vehicle needs to communicate with the intersection controller which further processes the vehicle status information to form virtual platoons. Virtual platoon coordination consists of three steps. The first step groups incoming vehicles into different virtual platoons such that vehicles approaching later will not impact those arriving earlier. In the second step, based on the conflict set $S_{\mathrm{s}_{i}}$ of vehicles in a virtual platoon, non-conflicting vehicles are grouped into one compatible passing set, and then the passing orders of compatible passing sets are organized to improve the throughput. In the third step, desired safe spacings
are set up for vehicles to enable virtual platooning control. Vehicles belonging to different compatible passing sets are assigned specific desired safe spacings to avoid collisions. Non-conflicting vehicles in the same compatible passing set are assigned the desired safe spacing of zero as they can converge to the same position slot and pass through the intersection simultaneously (as illustrated in Fig. 1).

### 3.1. Formation of virtual platoons

In virtual platooning control, to achieve consensus on the desired speed and spacings safely and efficiently, neighboring vehicles share kinematic information and cooperatively adjust their control decisions. Thereby, the movement of a vehicle will be influenced by both its immediate predecessor and successor vehicles. Adding a new vehicle sequentially to the tail of a virtual platoon with an achieved consensus will likely lead to vehicle states that deviate from the achieved consensus. This will then require vehicles in the updated virtual platoon to readjust their control decisions to form a new consensus, potentially triggering adverse impacts such as abrupt variations in vehicle speeds and safety concerns. To circumvent such impacts in the updated virtual platoon, we group vehicles into different independent virtual platoons. Then, the last vehicle (labeled as vehicle $\varkappa$ ) in an existing virtual platoon will not receive or use the kinematic information transmitted from the first vehicle in the immediate successor virtual platoon (containing vehicles arriving later); correspondingly, the control decision of vehicle $\varkappa$ will be independent of vehicles arriving later. Therefore, the updated virtual platoon will not be influenced by vehicles arriving later, which circumvents the need to form a new consensus.

The procedure for the formation of independent virtual platoons is as follows. When a vehicle $i$ crosses the boundary of the buffer zone, it notifies the intersection controller and communicates its speed $v_{i}$ to the intersection controller. The intersection controller then records its buffer zone arrival time $t_{i}^{b}$. Next, the intersection controller calculates the cooperative zone arrival time (i.e., the time when vehicle $i$ arrives at the boundary of the cooperative zone) of vehicle $i$ as: $t_{i}^{c}=t_{i}^{b}+\frac{L_{B}}{v_{i}}$, where $L_{B}$ is the length of the buffer zone. If $v_{i}=0$ due to oversaturated traffic conditions, vehicle $i$ will accelerate at a constant acceleration $a_{c}$ until it arrives to the cooperative zone; the cooperative zone arrival time is calculated as: $t_{i}^{c}=t_{i}^{b}+$ $\sqrt{\frac{2 L_{B}}{a_{c}}}$. Note that under unsaturated traffic conditions, a vehicle needs to maintain its initial speed $v_{i}$ when traveling in the buffer zone because the intersection controller is performing computations for intersection coordination and vehicles do not yet know which neighboring vehicles they will cooperate with. Hence, unnecessarily varying the speeds of vehicles could cause undesired fluctuations in spacings and speeds among vehicles in the virtual-platooning control process. For oversaturated traffic conditions, we set $a_{c}=$ $\frac{v_{\text {eq }}^{2}}{2 L_{B}}$ so that vehicles can achieve the desired operating speed $v_{\text {eq }}$ when arriving to the cooperative zone. In this way, the average speeds of approaching vehicles are increased and the speed fluctuations at the initial stage of virtual-platooning control are mitigated, which improves traffic efficiency for oversaturated traffic conditions.

Based on their arrival time to the cooperative zone, we label all approaching vehicles sequentially in terms of vehicle indices and form a dynamic vehicle set $\Upsilon_{s}=\{0,1,2, \ldots, N\}$ that is updated throughout a day, where a vehicle arriving earlier has a smaller index and $N$ is the total number of vehicles that approach the cooperative zone on that day. Then, we denote the cooperative zone arrival time of the first-arriving vehicle (the vehicle that arrives the earliest to the cooperative zone, labeled as V0 here) as $t_{0}$, and define a time window $\delta_{t}=L_{B} / v_{e q}$, where $v_{e q}$ is the intersection operating speed (i.e., the speed that vehicles need to maintain when passing through the intersection). On a given day, the first-arriving vehicle V0 will be assigned to a virtual platoon containing only itself, while vehicles whose cooperative zone arrival time is within the arrival time bound $t_{\text {bound }}=t_{0}+\delta_{t}$ will be included in a new virtual platoon sequentially behind the virtual platoon containing only V0. Then, we identify V0 as the lead vehicle for the immediate successor virtual platoon. Sequentially, the first vehicle excluded from the current virtual platoon (i.e., vehicle $\varrho$ with the earliest cooperative zone arrival time among the remaining vehicles not included in the current virtual platoon) becomes the first vehicle for the next virtual platoon, whose cooperative zone arrival time $t_{\varrho}$ will
be used to determine the arrival time bound $t_{\text {bound }}=t_{\varrho}+\delta_{t}$ for that platoon. The last vehicle included in the current virtual platoon (i.e., the vehicle with the latest cooperative zone arrival time in the current virtual platoon) becomes the lead vehicle for its successor virtual platoon. In situations where vehicles arriving to the cooperative zone are sufficiently far away from the current virtual platoon (i.e., the first vehicle of the current virtual platoon is already in the conflict zone), we repeat the procedure described for V0 and its successor virtual platoons, except that the vehicle index will be sequentially updated from that of the last vehicle in the current virtual platoon. The virtual platoon formation process is repeated until all vehicles have been assigned to a virtual platoon. The pseudo-code of the virtual platoon formation algorithm is:

```
input: the set of approaching vehicles: \(\Upsilon_{s} \leftarrow\{0,1,2, \ldots, N\}\), the cooperative zone arrival time: \(\mathfrak{T} \leftarrow\)
\(\left\{t_{0}, t_{1}, t_{2}, \ldots, t_{N}\right\}\)
output: the collection of independent virtual platoons \(\Upsilon_{p}\)
    initialize: set the length of the time window: \(\delta_{t}\), the collection of virtual platoons as empty: \(\Upsilon_{p} \leftarrow\)
{ }, the temporal set: Temp ← { }, the vehicle index: \(i \leftarrow 0\), the number of independent virtual platoons:
\(j \leftarrow 0\), the arrival time bound for current virtual platoon: \(t_{\text {bound }} \leftarrow t_{0}+\delta_{t}\).
    # Each element of \(\Upsilon_{p}\) is an independent virtual platoon \(\Upsilon_{\mathrm{vp}}\), entries in a \(\Upsilon_{\mathrm{vp}}\) are the vehicles in the
same independent virtual platoon
    while \(i \leq N\) do:
        if \(i\) is zero
            Update the number of independent virtual platoons: \(j \leftarrow j+1\)
            Append vehicle \(i\) as the first entry of the \(j\) th element in \(\Upsilon_{p}\)
            Update the arrival time bound: \(t_{\text {bound }} \leftarrow t_{i}+\delta_{t}\)
        end if
        if \(t_{i} \leq t_{\text {bound }}\) or the first vehicle of \(j\) th independent virtual platoon has not approached the
conflict zone
            Assign vehicle to the temporal set: Temp ← Temp \(\cup i\)
        else
            Append the temporal set Temp to the \(j\) th element in \(\Upsilon_{p}\)
            Update the arrival time bound: \(t_{\text {bound }} \leftarrow t_{i}+\delta_{t}\)
            Re-initialize the temporal set: Temp ← []
            Update the number of independent virtual platoons: \(j \leftarrow j+1\).
            Append vehicle \(i\) as the first entry of the \(j\) th element in \(\Upsilon_{p}\)
        end if
        Move to the next vehicle in \(\Upsilon_{s}: i \leftarrow i+1\)
    end while
```

Note that in this study, unlike in real (physical) platoons, the "lead" vehicle is not included in the virtual platoon it leads, as the lead vehicle only sends kinematic information to the next vehicle (the first vehicle in the virtual platoon) for tracking and does not cooperatively adjust its movements with the vehicles in that virtual platoon. The virtual platoon formation algorithm has a linear time complexity of $O(N)$, where $N$ is the number of approaching vehicles. Thereby, the virtual platoon formation algorithm is computationally efficient for real-world applications.

### 3.2. Compatible passing sets for non-conflicting vehicles

After grouping vehicles into independent virtual platoons, vehicles in the same virtual platoon are coordinated to improve the performance efficiency of the intersection. Correspondingly, we group the nonconflicting vehicles into a compatible passing set, and allocate them the same position slot in the virtual platoon so that they can proceed simultaneously. The method to construct a compatible passing set consists of three steps. First, select the first vehicle from a virtual platoon $V_{p}$, and identify all possible combinations of its non-conflicting vehicles. Second, select the combination with the largest cardinality to form the
compatible passing set $C_{n}$ (this can benefit the intersection throughput by allowing the set with more vehicles to proceed first). Third, remove the vehicles included in the compatible passing set $C_{n}$ from the virtual-platoon set $\Upsilon_{p}$. Repeat these three steps until the virtual platoon set $\Upsilon_{p}$ is empty. Note that the passing order of each compatible passing set is the index of it. The pseudo-code of the method to construct the compatible passing sets is:

```
input: the set of vehicles in an independent virtual platoon \(\Upsilon_{\mathrm{vp}} \leftarrow\left\{0,1,2, \ldots, N_{\mathrm{vp}}\right\}\)
output: the collection of compatible passing sets \(C\), the number of compatible passing sets \(N_{c}\)
    initialize: Set the number of compatible passing sets: \(N_{c} \leftarrow 0\), the collection of compatible passing
sets as empty: \(C \leftarrow\}\)
    while \(\Upsilon_{\mathrm{vp}}\) is not empty do:
        Update the number of compatible passing sets: \(N_{c} \leftarrow N_{c}+1\)
        Select vehicle \(i\) to be the first vehicle in the independent virtual platoon: \(i \leftarrow \Upsilon_{\mathrm{vp}}[0]\)
        Find and record all possible combinations of non-conflicting vehicles for vehicle \(i\) to form a series
of sets: \(C_{n}=\left\{C_{n}^{\mathrm{id}}\right\}_{\mathrm{id}=1}^{\mathrm{id}=m}\)
        Select \(C_{n}^{\mathrm{id}}\) with the largest cardinality: \(C_{n}^{\star}=\underset{C_{n}^{\mathrm{id}} \subseteq C_{n}}{\operatorname{argmax}}\left|C_{n}^{\mathrm{id}}\right|\), and append \(C_{n}^{\star}\) to \(C\)
        Remove vehicle \(i\) and vehicles in \(C_{n}^{\star}\) from the virtual platoon: \(\Upsilon_{\mathrm{vp}} \leftarrow \Upsilon_{\mathrm{vp}} \backslash\left\{i, \forall j \in C_{n}^{\star}\right\}\)
    end while
```

As the maximum number of non-conflicting vehicles for a vehicle is bounded by the maximum number of non-conflicting movements (which is six for the intersection used in this study), the time complexity of finding the combination of non-conflicting vehicles with the largest cardinality will not increase with the number of vehicles in an independent virtual platoon (i.e., $N_{\mathrm{vp}}$ ). Hence, the algorithm for forming compatible passing sets has a linearithmic time complexity of $O\left(N_{\mathrm{vp}} \log N_{\mathrm{vp}}\right)$, which is also computationally efficient for real-world applications.
3.3. Determination of desired safe spacings

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-12.jpg?height=649&width=1287&top_left_y=1507&top_left_x=305)
Fig. 5. Grid separation of conflict zone: (a) $5 \times 5$ grid layout; (b) grid label

This section describes the process of determining desired safe spacings between conflicting vehicles to avoid collisions. First, we divide the conflict zone into a 5×5 grid layout, where the center of each grid is the conflict point of vehicles from two conflicting directions (see Fig. 5). The length of a grid is the same as the lane width $w_{l}$. We denote the center of each grid as: $\mathfrak{C}_{i, j}, i, j \in\{1, \ldots, 5\}$. Then, we define the following spacing-related variables. The spacing between vehicle $i$ in compatible passing set $n$ and vehicle
$j$ in compatible passing set $n-1$ is denoted as $d_{i, j} . d_{i, j}$ is calculated using the difference in Manhattan spacings with respect to the corresponding conflict point $\mathfrak{C}_{m, n}: d_{i, j}=\left|x_{j}-\mathfrak{C}_{m, n}\right|_{1}-\left|x_{i}-\mathfrak{C}_{m, n}\right|_{1}$, where $x_{i}$ and $x_{j}$ are the positions of vehicles $i$ and $j$, respectively. The collision spacing $d_{i, j}^{c}=\left|x_{j}-\mathfrak{C}_{3,3}\right|_{1}-$ $\left|x_{i}-\mathfrak{C}_{3,3}\right|_{1}$ is defined as the spacing between vehicle $i$ and $j$, with respect to the geometric center $\mathfrak{C}_{3,3}$ (the center point based on which vehicles are projected onto virtual platoons). The collision spacing will trigger collision between vehicles $i$ and $j$ (i.e., $d_{i, j}=0$ ). $D_{n}$ is the desired safe spacing between a vehicle in compatible passing set $n$ and a vehicle in compatible passing set $n-1$ so as to avoid collision. It is used to calculate the spacing error of vehicles $i$ : $e_{i}=d_{i, j}-D_{n}, n \in\left\{2, \ldots N_{c}\right\}$ in section 4.2.

With the spacing-related variables defined above, we propose an algorithm to determine the desired safe spacing (i.e., to obtain $D_{n}, n \in\left\{2, \ldots N_{c}\right\}$ ). The algorithm is illustrated as follows. First, the conflicting vehicle pairs $(i, j)$ from two adjacent compatible passing sets $C_{n}$ and $C_{n+1}$ are enumerated, and the collision spacing $d_{i j}^{c}$ for each vehicle pair $(i, j)$ is determined and recorded. Then, the largest collision spacing among these vehicle pairs is selected and a safety cushion $\epsilon$ (a constant value of spacing, e.g., 8m) is added to determine the desired safe spacing between $C_{n}$ and $C_{n+1}$. Note that vehicles may deviate from the planned turning trajectories in the real-world operation, thereby requiring that the safety cushion be selected in a conservative manner. The collision spacing for each vehicle pair is shown in Table B in the Appendix A. The pseudo-code of the desired safe spacing determination algorithm is:

```
input: the collection of compatible passing sets \(C\), and number of compatible passing sets \(N_{c}\)
output: the array of desired safe spacings \(\mathrm{D} \in \mathbb{R}^{N_{c}}\)
1: initialize: Set the index of compatible passing sets: \(n \leftarrow 0\), the safety cushion: \(\epsilon>0\), and the array
of desired safe spacings as empty: \(\mathrm{D} \leftarrow[]\)
    while \(n<N_{c}-1\) do:
        For every vehicle pair \((i, j), i \in C_{n}, j \in C_{n+1}\), obtain and record the collision spacing \(d_{i j}^{c}\)
        Iterate through recorded \(d_{i j}^{c}\) to obtain the largest one, denoted it as \(d_{i j}^{c}{ }^{*}\)
        Obtain the desired safe spacing as: \(D_{n} \leftarrow d_{i j}^{c}{ }^{*}+\epsilon\)
        Append \(D_{n}\) to the desired safe spacing set D
        Update the index of compatible passing sets: \(n \leftarrow n+1\)
    end while
```

During the operation, the number of vehicles in a compatible passing set is bounded by the maximum number of vehicles that are not conflicting with each other (denoted as $N_{\max }$ ). $N_{\max }$ is equal to six for the intersection configuration used in this study. Thereby, lines 3 and 4 will have a fixed worst-case time complexity of $O\left(N_{\text {max }}^{2}\right)$. Correspondingly, the time complexity of the desired safe spacing determination algorithm has a linear time complexity of $O\left(N_{c}\right)$, where $N_{c}$ is the number of compatible passing sets. Thus, the algorithm to determine the safe spacing is also computationally efficient for real-world applications.

## 4. Virtual platooning control

This section describes the two-step control design of the virtual platooning strategy. The first step (section 4.1) is to construct an IFT with the property of structural controllability (Liu and Barabási, 2016) so that all vehicles in the virtual platoon $\Upsilon_{p}$ can be fully controlled to achieve consensus cooperatively:

$$
\begin{gathered}
\lim _{t \rightarrow \infty} a_{i}(t)=0, i \in \Upsilon_{p} \\
\lim _{t \rightarrow \infty}\left(v_{i}(t)-v_{e q}\right)=0, i \in \Upsilon_{p}
\end{gathered}
$$

$$
\left\{\begin{array}{c}
\lim _{t \rightarrow \infty}\left(\left|x_{i}(t)-\mathbb{C}_{m, n}\right|_{1}-\left|x_{j}(t)-\mathbb{C}_{m, n}\right|_{1}-D_{n}\right)=0, m, n \in\{1, \ldots, 5\}, i \in C_{n-1}, j \in C_{n}, n \in\left\{2, \ldots N_{c}\right\} \\
\lim _{t \rightarrow \infty}\left(\left|x_{i}(t)-\mathbb{C}_{m, n}\right|_{1}-\left|x_{j}(t)-\mathbb{C}_{m, n}\right|_{1}\right)=0, \quad m, n \in\{1, \ldots, 5\}, i, j \in C_{n}, n \in\left\{1, \ldots N_{c}\right\}
\end{array}\right.
$$

where $a_{i}(t), v_{i}(t)$, and $x_{i}(t)$ are the acceleration, speed, and position of vehicle $i$ at time $t$, respectively. Equation (1) states that vehicles should not accelerate. Equation (2) states that the speed tracking error $v_{i}(t)-v_{e q}$ needs to converge to zero, indicating that vehicles should drive at the intersection operating speed $v_{e q}$. Equation (3) states that vehicles in different compatible passing sets $n-1$ and $n$ should maintain a desired safe spacing $D_{n}$, while vehicles in the same compatible passing set should converge to the same position spot. A constant spacing policy is applied in virtual platooning control to maintain the desired safe spacing between vehicles. The reason for considering only the adjacent compatible passing sets in Equation (3) is to reduce the ongoing communication links during the intersection operation, which can improve the communication reliability in heavy traffic conditions by reducing communication interference. Note that we omit ( $t$ ) for all time-dependent variables from hereon to enhance readability.

The second step (section 4.2) is to devise the distributed controller based on the IFT construction. We combine the backstepping (Khalil, 2002), model reference adaptive (Parks, 1966), and sliding mode (Young et al., 1999) control methods to address the unparameterized disturbances and parametric inaccuracies in the vehicle dynamics model.

### 4.1. Information flow topology and structural controllability

The proposed IFT of a virtual platoon is expressed as a weighted graph $\mathbb{G}(v, e, w) . v$ is the vertex set representing vehicles in the virtual platoon, $e$ is the edge set which indicates the information flow direction, and $w$ is the set of weighting coefficients that will impact string stability (discussed in sections 4.2 and 4.3). To mitigate the potential communication-related issues, each vehicle $i \in \Upsilon_{p}$ can communicate with at most its two closest neighboring vehicles $i-1$ and $i+1$. More importantly, the proposed IFT ensures structural controllability (Liu and Barabási, 2016), implying that vehicles in the platoon can be moved to desired positions which can ensure safe operation of the platoon.

The construction of the proposed IFT is illustrated using Fig. 6 for two adjacent independent virtual platoons (blue- and red-dashed rectangular boxes), where the arrows represent the direction of information transmission. In the blue-dashed box, virtual platoon 1 has four compatible passing sets (containing 16 vehicles), while in the red-dashed box, virtual platoon 2 has two compatible passing sets (containing 7 vehicles). The first vehicle V0 (rectangular green box) functions as the lead vehicle for virtual platoon 1. As discussed in section 3.1, the last vehicle of a virtual platoon functions as the lead vehicle for the immediate successor virtual platoon (e.g., V16 leads virtual platoon 2). Each virtual platoon contains some compatible passing sets consisting of one pivot vehicle (in green circle) and some following vehicles. Within a compatible passing set, the pivot vehicle is defined as the vehicle with the smallest vehicle index. The lead vehicle provides the pivot vehicle in the adjacent compatible passing set (whose passing sequence is next to the lead vehicle) with position and speed information (e.g., V0 sends information to V1). A pivot vehicle communicates with the pivot vehicles in the adjacent compatible passing sets, and shares information on vehicle states to maintain desired safe spacings (e.g., V5 communicates with V3 and V11). A pivot vehicle also leads the corresponding compatible passing set and sends its position and speed information to its neighboring vehicle (e.g., V3 sends information to V8). Additionally, to reduce ongoing communications, all other following vehicles in the same compatible passing set only communicate with at most two neighboring vehicles to expand an undirected line-graph IFT (e.g., as shown in the compatible passing set $C_{1}$ which consists of V1, V2, V4, and V6), which will drive these vehicles to the same position slot.
Remark 1: Note that a pivot vehicle leads a compatible passing set. Let a vehicle with a smaller vehicle index arriving later to the cooperative zone be assigned as the pivot vehicle. It will induce other vehicles arriving earlier to decelerate to maintain the same pace with it, which can reduce the efficiency of virtual platooning control. Hence, the vehicle in a compatible passing set with the smallest vehicle index arriving
first to the cooperative zone is designated as the pivot vehicle.
Then, we introduce the following lemma to show that the proposed IFT enables structural controllability.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-15.jpg?height=618&width=1348&top_left_y=364&top_left_x=389)
Fig. 6. Example of IFT construction

Lemma 1: The proposed weighted graph $\operatorname{IFT} \mathbb{G}(v, e, w)$ guarantees the structural controllability of all compatible passing sets and all virtual platoons, implying that all vehicles in the virtual platoons can be moved to their desired positions to ensure the safe operation of the virtual platooning control.
Proof: We first prove the structural controllability of a compatible passing set, then of an independent virtual platoon, and finally of the concatenated virtual platoon formed by connecting multiple adjacent independent virtual platoons (e.g., the one formed by connecting V0, virtual platoon 1, and virtual platoon 2 in Fig. 6).

Based on the line-graph structure of the proposed IFT, the state dynamics of a $m$-vehicle compatible passing set shown in Fig.7(a) can be approximated as (Liu and Barabási, 2016):

$$
H=\left[\begin{array}{cccccc}
a_{11} & a_{12} & 0 & \cdots & 0 & 0 \\
a_{21} & a_{22} & a_{23} & \cdots & 0 & 0 \\
0 & a_{32} & a_{33} & \cdots & 0 & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & \cdots & a_{m, m-1} & a_{m, m}
\end{array}\right], G=\left[b_{1}, 0, \ldots, 0\right]^{T}
$$

where $\eta=\left[\eta_{1}, \eta_{2}, \eta_{3}, \ldots, \eta_{m}\right]^{T} \in \mathbb{R}^{m}$ is the state vector of the vehicles (vertices), $\dot{\eta}=$ $\left[\dot{\eta}_{1}, \dot{\eta}_{2}, \dot{\eta}_{3}, \ldots, \dot{\eta}_{m}\right]^{T} \in \mathbb{R}^{m}$ is the time derivative of vehicle state vector, $u$ is the scalar reference signal (i.e., desired speed of the pivot vehicle tracked by the other vehicles in the compatible passing set) provided to the compatible passing set. $H$ is the vehicular state-transition matrix whose non-zero entries $a_{i j}$ denote the correlations indicating the state variations in vehicle $i$ (i.e., $\dot{\eta}_{i}$ ) that will be induced by the state of vehicle $j$. $G$ is the control actuation matrix whose non-zero entry $b_{1}$ can be interpreted as the control gain of the pivot vehicle used for scaling the reference signal $u$. The control gain is incorporated to maintain the desired speed when lagging effects occur in terms of tracking it by the following vehicles. The values of $a_{i j}$ and $b_{1}$ are determined by the specific virtual platooning control method (DASMC in this study) and weighting coefficients in set $w$ of the proposed IFT.

The structural controllability of a compatible passing set described by Equation (4) can be guaranteed if the compatible passing set is controllable (Liu and Barabási, 2016). Correspondingly, the controllability of a compatible passing set (Equation (4) can be proved using the Kalman's rank condition (Åström and Murray, 2010): a dynamical system is controllable, and the system state (e.g., positions, speeds) can shift from the initial state $\eta(0)=\eta_{0}$ to the final state $\eta(T)=\eta_{T}$ in a finite time $T$, if and only if the controllability matrix:

$$
C \equiv\left[G, H G, H^{2} G, \ldots H^{m-1} G\right]
$$

has a full rank, i.e., $\operatorname{rank}(\mathrm{C})=m$. For the $m$-vehicle compatible passing set described in Equation (4), the controllability matrix C can be expressed as:

$$
\mathrm{C}=\left[\begin{array}{cccccc}
b_{1} & a_{11} b_{1} & a_{11}^{2} b_{1}+a_{12} a_{21} b_{1} & \beta_{1} & \ldots & o_{1, m} \\
0 & a_{21} b_{1} & a_{21} a_{11} b_{1}+a_{22} a_{21} b_{1} & \beta_{2} & \ldots & o_{2, m} \\
0 & 0 & a_{32} a_{21} b_{1} & \beta_{3} & \ldots & o_{3, m} \\
0 & 0 & 0 & a_{43} a_{32} a_{21} b_{1} & \ldots & o_{4, m} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & 0 & \ldots & a_{m, m-1} \cdots a_{21} b_{1}
\end{array}\right]
$$

where $\beta_{1}=b_{1}\left(a_{11}^{3}+a_{11} a_{12} a_{21}+a_{12} a_{21} a_{11}+a_{12} a_{22} a_{21}\right), \beta_{2}=b_{1}\left(a_{21} a_{11}^{2}+a_{12} a_{21}^{2}+a_{22} a_{21} a_{11}+\right.$ $\left.a_{22}^{2} a_{21}+a_{23} a_{32} a_{21}\right), \beta_{3}=b_{1}\left(a_{32} a_{21} a_{11}+a_{32} a_{22} a_{21}+a_{33} a_{32} a_{21}\right) . o_{i, m}, i \in\{1, \ldots, m-1\}$ are calculated using the correlations corresponding to the previous $m-1$ vehicles. $o_{i, m}$ is non-zero if $m$ is odd (even) and $i$ is odd (even). $o_{i, m}$ is zero if $m$ is odd (even) and $i$ is even (odd). As the controllability matrix C is strictly upper-triangular with non-zero diagonal entries, C is nonsingular and full-rank, indicating that the compatible passing set is controllable. Therefore, the proposed IFT assures that each compatible passing set in an independent virtual platoon is structurally controllable.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-16.jpg?height=396&width=1529&top_left_y=1011&top_left_x=303)
Fig. 7. Proposed IFT: (a) $m$-vehicle compatible passing set; (b) quotient graph of original IFT

In an independent virtual platoon, we can partition vehicles belonging to the same compatible passing set into a single vertex (as each compatible passing set is structurally controllable, and vehicles can converge to the same position slot), converting the original graph $\mathbb{G}$ (e.g., the IFT in Fig. 6) into the corresponding quotient graph $\mathbb{G}^{\prime}$ shown in Fig. 7(b). A quotient graph is a graph whose vertices are partition blocks containing a single vertex or multiple vertices (i.e., vehicles) of the original graph. In Fig. 7(b), the lead vehicle V0 and compatible passing sets become vertices of the quotient graph $\mathbb{G}^{\prime}$. As the proposed IFT also ensures each independent virtual platoon (e.g., virtual platoon 1) in the quotient graph $\mathbb{G}^{\prime}$ to be a line graph, we can use the approach used to prove the controllability of a compatible passing set to show that each independent virtual platoon is also structurally controllable.

The concatenated virtual platoon formed by connecting V0 and its adjacent independent virtual platoons (e.g., virtual platoon 1 and virtual platoon 2 in Fig. 7(b)) satisfies the properties of: (i) a cactus graph with no dilations (i.e., each independent virtual platoon has only one directed edge connecting to another independent virtual platoon); and (ii) no inaccessible vertices from the root vertex (i.e., V0 in Fig. 7(b)), which indicates that each independent virtual platoon has one edge path (i.e., a sequence of edges) originating from V0. Thus, the proposed IFT also ensures structural controllability of the concatenated virtual platoon (Liu and Barabási, 2016).

Hence, the proposed IFT can guarantee the structural controllability of all compatible passing sets, independent virtual platoons, and the concatenated virtual platoon, implying all the vehicles involved in the virtual platooning control can be moved to the desired positions for ensuring safe operation. This completes the proof of Lemma 1. ■
Remark 2: The linear system model in (4) can be interpreted as a linear approximation of the nonlinear
control system in the formulation of the DASMC that follows. Although a linear system cannot fully describe the evolution of vehicle states in the transient response, it can indicate the outcomes of the proposed DASMC based on the proposed IFT with line-graph structure. In the literature, linear system models are also widely used in CAV platoon control problems to approximate vehicle dynamics to articulate the impacts of IFTs and the string stability of certain platoon control strategies (Gong et al., 2016; Zheng et al., 2016; Zhou and Ahn, 2019).
4.2. Design of distributed adaptive sliding mode controller (DASMC)

The DASMC design is decomposed into two steps. The first step is to apply the backstepping control method (Khalil, 2002) to derive an explicit structure for the control decision of each vehicle to ensure that the third-order time derivative of vehicle state (as shown in Equation (9)) converges to zero. Based on that, the second step incorporates the model reference adaptive control (Parks, 1966) and sliding mode control (Young et al., 1999) methods to mitigate the effects of the parametric inaccuracies and unparameterized disturbances in the second-order time derivatives of vehicle states (as shown in Equation (8)), so that the spacing and speed tracking errors of all vehicles in a virtual platoon can converge to zeros asymptotically, implying the local stability of the virtual platoon. The local stability is proved using Lyapunov function analysis and Barbalat's lemma (Khalil, 2002), while string stability is guaranteed based on the strict frequency-domain string stability criterion (Feng et al., 2019; Naus et al., 2010). Note that in this study, stabilizing a variable means enabling the dynamics of the variable (i.e., time derivative) to converge to zero, so that the variable can converge to the desired value. Correspondingly, the convergence of a variable is in terms of time.
4.2.1. Vehicle dynamics model

The state dynamics of vehicle $i \in \Upsilon_{p}$ in a virtual platoon (vehicle $i$ can be a pivot vehicle or a following vehicle of a compatible passing set) are described using a third-order nonlinear dynamical model (Wu et al., 2016):

$$
\begin{gathered}
\dot{x}_{i}=v_{i} \\
\dot{v}_{i}=a_{i}=\frac{F_{i}-c_{i} \dot{x}_{i}^{2}-f_{i}}{M_{i}}+\delta_{i} \\
\dot{F}_{i}=\frac{u_{i}-F_{i}}{\tau_{i}}
\end{gathered}
$$

where $x_{i}$ is the vehicle position, $v_{i}$ is the vehicle speed, $a_{i}$ is the vehicle acceleration, $F_{i}$ is the actual driving force produced from vehicle actuator (i.e., engine, brakes), $u_{i}$ is the control decision (in this study, driving force decision sent to the vehicle actuator for execution), $M_{i}$ is the vehicle weight, $c_{i}$ is the air drag coefficient, $f_{i}$ is the rolling resistance, $\delta_{i}$ denotes the unparameterized disturbances, and $\tau_{i}$ is the inertial delay factor of the vehicle powertrain.
4.2.2. Stabilizing vehicle states: backstepping control method

Through backstepping control, an intermediate control decision $\alpha_{i}$ (formulated in section 4.2.3) is used to ensure vehicle states $x_{i}$ and $v_{i}$ can track desired values (i.e., the spacing and speed tracking errors of vehicle $i$ converge to zeros). This is achieved by reducing the error between the actual driving force and the intermediate control decision to zero through the use of an error variable:

$$
z_{i}=F_{i}-\alpha_{i}
$$

Then, taking the time derivative of the error variable, we have its dynamics:

$$
\dot{z}_{i}=\dot{F}_{i}-\dot{\alpha}_{i}=\frac{u_{i}-F_{i}}{\tau_{i}}-\dot{\alpha}_{i}
$$

As illustrated in Equation (11), the control decision $u_{i}$ is included in the error variable dynamics and is used to ensure that $z_{i}$ and the state dynamics (8) and (9) converge to zeros asymptotically. Lemma 2 discusses the design of the associated control decision structure.
Lemma 2: The control decision with a structure:

$$
u_{i}=F_{i}+\tau_{i}\left(\dot{\alpha}_{i}-k_{1} z_{i}\right)
$$

ensures that the error variable $z_{i}$ and state dynamics (8) and (9) converge to zero asymptotically, and also guarantees the local stability of the virtual platoon, if: (i) the intermediate control decision $\alpha_{i}$ can ensure that the spacing and speed tracking errors for each vehicle converge to zeros asymptotically, and (ii) the backstepping control gain satisfies $k_{1}>0$.
Proof: Define a Lyapunov function $V_{i}^{*}$ for vehicle $i$ :

$$
V_{i}^{*}=V_{i}+\frac{1}{2} z_{i}^{2}
$$

where $V_{i}$ is the Lyapunov function referring to the convergence of spacing and speed tracking errors, whose time derivative $\dot{V}_{i}$ will be negative-semidefinite if spacing and speed tracking errors both converge to zeros. Note that $V_{i}$ is positive-definite except at the origin where all errors are zeros, thus $V_{i}^{*}$ is also positivedefinite except at the origin where all errors and $z_{i}$ are zeros. Taking the time derivative of $V_{i}^{*}$, we have:

$$
\dot{V}_{i}^{*}=\dot{V}_{i}+z_{i} \dot{z}_{i}
$$

After substituting $u_{i}$ into $\dot{z}_{i}$, and then substituting $\dot{z}_{i}$ into $\dot{V}_{i}^{*}$, we can obtain:

$$
\dot{V}_{i}^{*}=\dot{V}_{i}-k_{1} z_{i}^{2}
$$

Thus, if an intermediate control law $\alpha_{i}$ is appropriately implemented to enforce the spacing and speed tracking errors both converge to zeros, then the time derivative of $V_{i}$ will be negative-semidefinite: $\dot{V}_{i} \leq 0$. Thereby, if $k_{1}>0, \dot{V}_{i}^{*}$ will be negative-definite: $\dot{V}_{i}^{*}<0$, except when all variables are equal to zeros. As $V_{i}^{*}$ is positive-definite (except at the origin where spacing and tracking errors, and $z_{i}$ are zeros) and radially unbounded with respect to spacing and speed errors and $z_{i}$, and $\dot{V}_{i}^{*}$ is negative-definite (except at the origin), we can conclude that given a properly designed $\alpha_{i}, u_{i}=F_{i}+\tau_{i}\left(\dot{\alpha}_{i}-k_{1} z_{i}\right)$ can ensure the error variable $z_{i}$ and the spacing and speed tracking errors of vehicle $i$ converge to zeros asymptotically.

Correspondingly, for $n$ pivot vehicles in a virtual platoon, or $n$ following vehicles in a compatible passing set, we aggregate the error variables of all vehicles into a vector: $Z=\left[z_{1}, \ldots, z_{n}\right]^{\dagger} \in \mathbb{R}^{n}$. Then, we define a Lyapunov function $V^{*}$ for $n$ vehicles as:

$$
V^{*}=\sum_{i=1}^{n} V_{i}^{*}=\sum_{i=1}^{n}\left(V_{i}+\frac{1}{2} z_{i}^{2}\right)
$$

Taking its time derivative, we obtain:

$$
\dot{V}^{*}=\sum_{i=1}^{n}\left(\dot{V}_{i}-k_{1} z_{i}^{2}\right)
$$

Thus, to ensure $\dot{V}^{*}$ is negative-definite (except at the origin), and enforce all error variables, and the spacing and speed tracking errors of all pivot vehicles in a virtual platoon, and all following vehicles in each compatible passing set converge to zeros asymptotically, we need to constrain $k_{1}>0$, and design the intermediate control decision $\alpha_{i}$ so as to ensure $\dot{V}_{i}$ is negative-definite (except at the origin) for each vehicle. Sequentially, enforcing the spacing and speed tracking errors of each vehicle converge to zeros asymptotically guarantees the local stability of the virtual platoon. This completes the proof of lemma 2. ■

The next step is to derive the intermediate control decision $\alpha_{i}$ to enforce the spacing and speed tracking errors both converge to zeros asymptotically, and drive all the vehicles in the virtual platoon to the consensus cooperatively.
4.2.3. Mitigating effects: model reference adaptive control and sliding mode control methods

To design the intermediate control decision $\alpha_{i}$, we first use the spacing error and speed tracking error to construct the sliding surface for each vehicle. Then, we use the sliding surfaces of neighboring vehicles to establish the cooperative sliding surface for each vehicle. Based on the cooperative sliding surface, the intermediate control decision $\alpha_{i}$ is determined by combining the model reference adaptive control method (Parks, 1966) with a smooth projection-based parameter adaptation law, and the sliding mode control method (Young et al., 1999).

The spacing error of vehicle $i$ is expressed as the difference between the actual spacing of two neighboring vehicles and the desired safe spacing:

$$
e_{i}=\left\{\begin{aligned}
x_{i-1}-x_{i}-D_{n}, & i-1 \in C_{n-1}, i \in C_{n} \\
x_{i-1}-x_{i}, & i-1 \in C_{n}, i \in C_{n}
\end{aligned}\right.
$$

Correspondingly, the speed tracking error is defined as the time derivative of spacing error:

$$
\dot{e}_{i}=v_{i-1}-v_{i}
$$

The sliding surface of vehicle $i$ is formulated as an ordinary differential equation (ODE) consisting of spacing error and speed tracking error:

$$
s_{i}=\dot{e}_{i}+\lambda e_{i}, \lambda>0
$$

The design of the sliding surface aims at ensuring that the spacing error $e_{i}$ and the speed tracking error $\dot{e}_{i}$ converge to zero. Next, we propose a cooperative sliding surface design that ensures that the sliding surface converges to zero: $s_{i}=0$; then, we can obtain a stable ODE of $\dot{e}_{i}$ :

$$
\dot{e}_{i}=-\lambda e_{i}
$$

which moves the spacing and speed tracking errors towards zero. The convergence of the spacing and speed tracking errors of each vehicle to zero indicates that all vehicle states have reached their desired values and the consensus (1)-(3) of the virtual platoon has been achieved. Then, all vehicles can proceed through the intersection safely.

We now describe the design of the cooperative sliding surface and intermediate control decision to ensure that the sliding surface of each vehicle converges to zero. We define a weighted Laplacian matrix $W$ as follows:

$$
[W]_{i j}=\left\{\begin{array}{c}
w_{i, 1}, \quad \text { if } i=j \\
w_{i, 2}, \quad \text { if } j=i+1 \\
0, \quad \text { otherwise }
\end{array}\right.
$$

where the entries $w_{i, j}$ are the weighting coefficients included in set $w$ (recall the weighted graph IFT in section 4.1) which will be further used in the string stability analysis in section 4.3. Then, to ensure that the sliding surfaces of all vehicles in the virtual platoon converge to zero, we construct the cooperative sliding surface of vehicle $i$ (denoted as $S_{i}$ ) using the weighted Laplacian matrix $W$ and sliding surfaces $s_{i}$ (Kwon and Chwa, 2014):

$$
S_{i}=\left\{\begin{aligned}
w_{i, 1} s_{i}+w_{i, 2} s_{i+1}, & i \in\{1, \ldots, n-1\} \\
w_{n, 1} s_{n}, & i=n
\end{aligned}\right.
$$

The cooperative sliding surface is based on the kinematic state information of immediate predecessor and successor vehicles, which leverages the line-graph IFT we set up in section 4.1. Next, lemma 3 states how the cooperative sliding surface ensures that the sliding surface of each vehicle converges to zero.
Lemma 3: The sliding surface $s_{i}$ will converge to zero if and only if the cooperative sliding surface $S_{i}$ converges to zero.
Proof: The cooperative sliding surfaces of $n$ pivot vehicles in a virtual platoon, or $n$ following vehicles of a compatible passing set, can be expressed as:

$$
S=\left[\begin{array}{c}
S_{1} \\
S_{2} \\
\vdots \\
S_{n-1} \\
S_{n}
\end{array}\right]=W s=\left[\begin{array}{ccccc}
w_{1,1} & w_{1,2} & \cdots & 0 & 0 \\
0 & w_{2,1} & w_{2,2} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & w_{n-1,1} & w_{n-1,2} \\
0 & 0 & \cdots & 0 & w_{n, 1}
\end{array}\right]\left[\begin{array}{c}
s_{1} \\
s_{2} \\
\vdots \\
s_{n-1} \\
s_{n}
\end{array}\right]
$$

The weighting Laplacian matrix $W$ is an upper-triangular matrix whose diagonal weighting coefficients are nonzero. Therefore, $W$ is nonsingular, implying that $s=0$ is valid if and only if $S=0$ (i.e., $s=0$ is equivalent to $S=0$ ). This completes the proof of Lemma 3. ■

From Lemma 3, we conclude that an intermediate control decision $\alpha_{i}$ that drives the cooperative sliding surface $S_{i}$ to zero is essential for spacing error $e_{i}$ and speed tracking error $\dot{e}_{i}$ to converge to zero.

Given $n$ pivot vehicles in a virtual platoon, or $n$ following vehicles of a compatible passing set, to ensure that the cooperative sliding surface of each vehicle $i, i \in\{1, \ldots, n-1\}$ converges to zero, we first take the time derivative of $S_{i}$ as follows:
-

$$
\begin{gathered}
\dot{S}_{i}=w_{i, 1} \dot{s}_{i}+w_{i, 2} \dot{S}_{i+1}=w_{i, 1}\left(\ddot{x}_{i-1}-\ddot{x}_{i}+\lambda \dot{e}_{i}\right)+w_{i, 2}\left(\ddot{x}_{i}-\ddot{x}_{i+1}+\lambda \dot{e}_{i+1}\right) \\
=\frac{w_{i, 2}-w_{i, 1}}{M_{i}}\left(\alpha_{i}-c_{i} v_{i}^{2}-f_{i}+\Delta_{i}\right)+A_{i}
\end{gathered}
$$

where $\Delta_{i}=M_{i} \delta_{i}$ are the lumped unparameterized disturbances, and $A_{i}=w_{i, 1} \ddot{x}_{i-1}-w_{i, 2} \ddot{x}_{i+1}+$ $\lambda\left(w_{i, 1} \dot{e}_{i}+w_{i, 2} \dot{e}_{i+1}\right)$ is the coupling term determined using speed tracking errors $\dot{e}_{i}$ and $\dot{e}_{i+1}$ and accelerations of vehicles $i-1$ and $i+1$.

As the last vehicle $n$ has no following vehicle, it uses only the kinematic information from itself and its predecessor vehicle $n-1$. From Equation (23), the corresponding time derivative of $S_{n}$ is then derived as:

$$
\dot{S}_{n}=w_{n, 1} \dot{S}_{n}=\frac{-w_{n, 1}}{M_{n}}\left(\alpha_{n}-c_{n} v_{n}^{2}-f_{n}+\Delta_{n}\right)+A_{n}
$$

where $A_{n}=\lambda w_{n, 1} \dot{e}_{n}+w_{n, 1} \ddot{x}_{n-1}$ is the coupling term derived using the speed tracking error $\dot{e}_{n}$ and the acceleration of vehicle $n-1$.

Then, we apply the model reference adaptive control (Parks, 1966) and sliding mode control (Young et al., 1999) methods to derive the intermediate control decision $\alpha_{i}$ as:

$$
\alpha_{i}=\left\{\begin{aligned}
\hat{c}_{i} v_{i}^{2}+\hat{f}_{i}-\frac{\hat{M}_{i}}{w_{i, 2}-w_{i, 1}} A_{i}-\frac{k_{2}}{w_{i, 2}-w_{i, 1}} S_{i}+\widehat{D}_{i} \operatorname{sgn}\left(S_{i}\right)-\frac{k_{3}}{w_{i, 2}-w_{i, 1}} \operatorname{sgn}\left(S_{i}\right), & i \in\{1, \ldots, n-1\} \\
\hat{c}_{n} v_{n}^{2}+\hat{f}_{n}+\frac{\widehat{M}_{n}}{w_{n, 1}} A_{n}+\frac{k_{2}}{w_{n, 1}} S_{n}+\widehat{D}_{n} \operatorname{sgn}\left(S_{n}\right)+\frac{k_{3}}{w_{n, 1}} \operatorname{sgn}\left(S_{n}\right), & i=n
\end{aligned}\right.
$$

where $\operatorname{sgn}(x)=\left\{\begin{aligned} 1, x>0 \\ 0, x=0 \\ -1, x<0\end{aligned}\right.$ is the sign function. $\hat{c}_{i}, \hat{f}_{i}, \widehat{D}_{i}$, and $\widehat{M}_{i}$ are the estimated values of vehicle parameters $c_{i}, f_{i}, \Delta_{i}$, and $M_{i}$, respectively; their estimation method is discussed in section 4.2.4. $k_{2}$ and $k_{3}$ are control gains to ensure that the cooperative sliding surface converges to zero. The first four terms in Equation (27) are derived based on the model reference adaptive control method (Parks, 1966) which aims to mitigate the effects of physical resistance and coupling terms $A_{i}$ in Equations (25) and (26), and to drive the cooperative sliding surface converge to zero. The last two terms in Equation (27) are derived using the sliding mode control method (Young et al., 1999) which mitigates the effects of unparameterized disturbances, imperfect negation of physical resistance, and unparameterized disturbances. Specifically, the effects of unparameterized disturbances and physical resistance cannot be perfectly negated because the parameter estimation error is inevitable in the early stages of the control process. This can lead to undesired large fluctuations in vehicle states and jeopardize convergence. To alleviate this, we include $\frac{k_{3}}{w_{i, 2}-w_{i, 1}} \operatorname{sgn}\left(S_{i}\right)\left(\frac{k_{3}}{w_{n, 1}} \operatorname{sgn}\left(S_{n}\right)\right.$ for the last vehicle) as the robust control decision to consistently suppress the effects of the imperfect negation of physical resistance and unparameterized disturbances in the control process. Correspondingly, the value of $k_{3}$ needs to be appropriately determined based on the upper and lower bounds of vehicle parameters and unparameterized disturbances, such that $\frac{k_{3}}{w_{i, 2}-w_{i, 1}} \operatorname{sgn}\left(S_{i}\right)$ and $\frac{k_{3}}{w_{n, 1}} \operatorname{sgn}\left(S_{n}\right)$ can dominate the negative effects of the imperfect negation throughout the control process.

Applying the lower and upper bounds of the parameters to Equations (25) and (26), the error triggered by the imperfect negation is bounded by:

$$
\Lambda=\left(\bar{c}_{i}-\underline{c}_{i}\right) v_{i}^{2}+\left(\bar{f}_{i}-\underline{f}_{i}\right)+\left(\bar{D}_{i}-\underline{D}_{i}\right)+\frac{\bar{M}_{i}-\underline{M}_{i}}{w_{i, 2}-w_{i, 1}}\left|A_{i}\right|, i \in\{1, \ldots, n\}
$$

Correspondingly, to ensure that the magnitude of robust control decision is larger than $\Lambda$, the value of $k_{3}$ should satisfy:

$$
k_{3} \geq\left(w_{i, 2}-w_{i, 1}\right)\left[\left(\bar{c}_{i}-\underline{c}_{i}\right) v_{i}^{2}+\left(\bar{f}_{i}-\underline{f_{i}}\right)+\left(\bar{D}_{i}-\underline{D}_{i}\right)\right]+\left(\bar{M}_{i}-\underline{M_{i}}\right)\left|A_{i}\right|+\varepsilon, i \in\{1, \ldots, n\}
$$

in which $\mathcal{E}$ is a positive robust margin (a positive real number used to ensure that the magnitude of the robust control decision is larger than $\Lambda$ ).
Remark 3: The inertial delay factor of vehicle powertrain $\tau_{i}$ is not estimated in the design process of $\alpha_{i}$,
because its impact is fully negated in the backstepping control method in Equation (11). Hence, $\tau_{i}$ serves as a regular coefficient in the vehicle dynamics model (9), and does not impact platoon local stability in the control process.

Next, we articulate the method to estimate the vehicle parameters.

### 4.2.4. Vehicle parameter estimation

As explicit knowledge of vehicle parameters is typically lacking, the vehicle parameters in Equation (27) are estimated through a gradient-type parameter estimation law (Kwon and Chwa, 2014):

$$
\begin{gathered}
\dot{\hat{c}}_{i}=\left\{\begin{array}{cc}
-\left(w_{i, 2}-w_{i, 1}\right) S_{i} v_{i}^{2}, & i \in\{1, \ldots, n-1\} \\
w_{n, 1} S_{n} v_{n}^{2}, & i=n
\end{array}\right. \\
\dot{\hat{f}}_{i}=\left\{\begin{aligned}
-\left(w_{i, 2}-w_{i, 1}\right) S_{i}, & i \in\{1, \ldots, n-1\} \\
w_{n, 1} S_{n}, & i=n
\end{aligned}\right. \\
\dot{\hat{D}}_{i}=\left\{\begin{aligned}
-\left(w_{i, 2}-w_{i, 1}\right)\left|S_{i}\right|, & i \in\{1, \ldots, n-1\} \\
w_{n, 1}\left|S_{n}\right|, & i=n
\end{aligned}\right. \\
\dot{\hat{M}}_{i}=\left\{\begin{array}{cc}
-A_{i} S_{i}, & i \in\{1, \ldots, n-1\} \\
A_{n} S_{n}, & i=n
\end{array}\right.
\end{gathered}
$$

In the control process, if the estimated vehicle parameters are not properly bounded, they can trigger excessive overshoot or undershoot. To alleviate the drawback of unbounded estimated vehicle parameters in the model reference adaptive control (Parks, 1966), we combine a complementary smooth projection function with the gradient-type parameter estimation law (30)-(33) to obtain the smooth projection-based parameter adaptation law as follows.

First, we define a vector of gradient-type parameter estimation law: $\zeta \in \mathbb{R}^{4 n}, \zeta_{i}=\left[\dot{\hat{c}}_{i}, \dot{\hat{f}}_{i}, \dot{\hat{D}}_{i}, \dot{\hat{M}}_{i}\right]^{\dagger}$, a positive-definite diagonal weighting matrix: $\mathcal{T}=I_{n} \otimes \operatorname{diag}\left(\left[\frac{1}{k_{c}^{i}}, \frac{1}{k_{f}^{i}}, \frac{1}{k_{D}^{i}}, \frac{1}{k_{M}^{i}}\right]\right) \in \mathbb{R}^{4 n \times 4 n}$, a vector of estimated vehicle parameters: $\hat{\theta} \in \mathbb{R}^{4 n}, \hat{\theta}_{i}=\left[\hat{c}_{i}, \hat{f}_{i}, \widehat{D}_{i}, \widehat{M}_{i}\right]^{\dagger}$, a vector of ground-truth vehicle parameters: $\theta \in \mathbb{R}^{4 n}, \theta_{i}=\left[c_{i}, f_{i}, D_{i}, M_{i}\right]^{\dagger}$, a vector of estimation errors: $\tilde{\theta}=\hat{\theta}-\theta, \tilde{\theta}_{i}=\left[\tilde{c}_{i}, \tilde{f}_{i}, \widetilde{D}_{i}, \widetilde{M}_{i}\right]^{\dagger}$, a vector of lower bounds of vehicle parameters: $\theta_{i, \min }=\left[\underline{c_{i}}, \underline{f_{i}}, \underline{D_{i}}, \underline{M_{i}}\right]^{\dagger}$, and a vector of upper bounds of vehicle parameters: $\theta_{i, \text { max }}=\left[\bar{c}_{i}, \bar{f}_{i}, \bar{D}_{i}, \bar{M}_{i}\right]^{\dagger}$. † denotes the transpose operation of a vector or matrix. Note that in this study we assume that the lower and upper bounds of vehicle parameters are known, such that the actual values of vehicle parameters are within specific range: $c_{i} \in\left[\underline{c}_{i}, \bar{c}_{i}\right], f_{i} \in\left[\underline{f_{i}}, \overline{f_{i}}\right], D_{i} \in\left[\underline{D_{i}}, \bar{D}_{i}\right], M_{i} \in$ $\left[\underline{M_{i}}, \bar{M}_{i}\right]$.

Then, we apply the following smooth projection function to bound the value of the estimated vehicle parameter $\widehat{\theta}_{i}$ :

$$
\operatorname{Proj}_{\hat{\theta}_{i}}\left(X_{i}\right)=\left\{\begin{array}{c}
0, \text { if } \hat{\theta}_{i}=\theta_{i, \max } \text { and } X_{i}>0 \\
0, \text { if } \hat{\theta}_{i}=\theta_{i, \min } \text { and } X_{i}<0, i \in\{1, \ldots, n\} \\
X_{i}, \text { otherwise }
\end{array}\right.
$$

where $X_{i}$ represents any variable applied to the smooth projection function $\operatorname{Proj}_{\hat{\theta}_{i}}(\cdot)$. Thus, the dynamics of estimated vehicle parameters can be correspondingly expressed via the smooth projection-based parameter adaptation law:

$$
\dot{\hat{\theta}}=\operatorname{Proj}_{\hat{\theta}}(\mathcal{T} \zeta)
$$

Correspondingly, two important properties of the smooth projection-based parameter adaptation law can be summarized as (Xu and Yao, 2001):

$$
\theta_{i, \min } \leq \hat{\theta}_{i} \leq \theta_{i, \max }, i \in\{1, \ldots, n\}
$$

- 

$$
\tilde{\theta}^{\dagger}\left(\mathcal{T}^{-1} \operatorname{Proj}_{\widehat{\theta}}(\mathcal{T} \zeta)-\zeta\right) \leq 0
$$

The first property (P1) implies that the estimated vehicle parameters are bounded within a proper range, which alleviates the undesired overshoot/undershoot. The second property (P2) states that the dynamics of estimation error is decaying, indicating that the estimated vehicle parameters will converge to certain values; it is used next in the proof of the local stability of a virtual platoon.

By combining Equations (27) and (35), the control decision $u_{i}$ of each vehicle in the virtual platoon mitigates the effects of physical resistance and unparameterized disturbances in the vehicle dynamics model, and then uses the cooperative sliding surface $S_{i}$ to ensure spacing and speed tracking errors converge to zeros, so that the consensus and local stability of the virtual platoon can be achieved safely. The local stability is then formally proved in section 4.3.
Remark 4: At the initial stage of virtual platooning control, we use the nominal values of vehicle parameters $c_{i}^{\text {nom }}, f_{i}^{\text {nom }}, \delta_{i}^{\text {nom }}, M_{i}^{\text {nom }}$, and $\tau_{i}^{\text {nom }}$ as prior knowledge to initialize the process of estimating vehicle parameters, and implementing the control decision. The nominal values are obtained from the manufacturer's vehicle specifications.
4.3. Local stability and string stability analysis

The properties of local stability and string stability can be achieved by setting up appropriate constraints for control gains $k_{1}, k_{2}, k_{3}$, and the weighting coefficients in weighted Laplacian matrix, as discussed hereafter.
Theorem 1: If the proposed control decision $u_{i}$ is applied to each vehicle in a virtual platoon, with $k_{1}, k_{2}>$ 0 , and $k_{3}$ satisfying Equation (29), then the cooperative sliding surfaces, spacing errors, and speed tracking errors converge to zero asymptotically, implying the local stability of the virtual platoon.
Proof: Please see Appendix B.
With the local stability ensured by the proposed control decision $u_{i}$, we can guarantee that the spacing and speed tracking errors of the virtual platoon decay to zero asymptotically. Next, we analyze the propagation and dissipation of the speed fluctuations and spacing errors upstream in the virtual platoon, and correspondingly tune the weighting coefficients to guarantee string stability.
Definition 1: Strong frequency-domain string stability (Feng et al., 2019; Naus et al., 2010). The equilibrium (equivalent to the consensus): $\left(e_{i}, \dot{e}_{i}, \ddot{e}_{i}\right)=(0,0,0), i \in\{0,1, \ldots, n\}$ of a vehicle $i$ in a $n$-vehicle virtual platoon described by $\dot{x}_{i}=f_{i}\left(x_{i}, x_{i-1}, \ldots, x_{i-n}\right)$ is strong frequency-domain string stable if the spacing error propagation transfer function $\mathfrak{G}_{i-1, i}(j \Omega)=\frac{\Xi_{i}(j \Omega)}{\Xi_{i-1}(j \Omega)}$ satisfies: $\left\|\mathfrak{G}_{i-1, i}(j \Omega)\right\|_{\infty} \leq 1$, where $j=\sqrt{-1}$ is the indicator for the complex number, and $\Omega$ is the angular frequency.
Theorem 2: If the weighting coefficients in the weighted Laplacian satisfy $\left|w_{i, 1}\right| \leq\left|w_{i, 2}\right|, \forall i \in \Upsilon_{p}$, then the strong frequency-domain string stability can be guaranteed at the equilibrium $\left(e_{i}, \dot{e}_{i}, \ddot{e}_{i}\right)=(0,0,0)$ for each vehicle in the virtual platoon.
Proof: As the control decision $u_{i}$ drives the cooperative sliding surface of vehicle $i$ to zero, we have:

$$
w_{i, 1} s_{i}+w_{i, 2} s_{i+1}=0, \forall i \in \Upsilon_{p}
$$

which then yields:

$$
w_{i, 1}\left(\dot{e}_{i}+\lambda e_{i}\right)=-w_{i, 2}\left(\dot{e}_{i+1}+\lambda e_{i+1}\right), \forall i \in \Upsilon_{p}
$$

Correspondingly, in the Laplace domain, Equation (39) can be expressed as:

$$
w_{i, 1} \Xi_{i}(s)(s+\lambda)=-w_{i, 2} \Xi_{i+1}(s)(s+\lambda), \forall i \in \Upsilon_{p}
$$

where $s=j \Omega$ is the Laplace operator, and $\Xi_{i}(s)$ is the spacing error $e_{i}$ in the Laplace domain. Applying the strong frequency-domain string stability condition introduced above, we require $\left|\frac{\Xi_{i+1}(s)}{\Xi_{i}(s)}\right|=\left|\frac{\Xi_{i+1}(j \Omega)}{\Xi_{i}(j \Omega)}\right|=$ $\left|\frac{w_{i, 1}}{w_{i, 2}}\right| \leq 1$ for string stability. Thus, $\left|w_{i, 1}\right| \leq\left|w_{i, 2}\right|$ is essential for preserving the string stability property of a virtual platoon. This completes the proof of Theorem 2. ■

Note that the case where $\mathfrak{G}_{i-1, i}(j \Omega)=1$ is referred to as the marginal string stability, which implies vehicles in the virtual platoon maintain the same fluctuations of spacing error and speed.

## 5. Traffic flow regulation

This section describes the modeling of the traffic flow regulation to alleviate spillbacks in oversaturated conditions. When excessive traffic enters the intersection, some vehicles will inevitably stop in the buffer zone (see Fig. 4) before they can proceed due to the limited capacity on exit lanes. Such a stop-and-go phenomenon significantly reduces the efficiency of virtual platooning control, as the controller needs to address vehicle states that deviate significantly from the consensus in Equations (1)-(3). As importantly, unregulated oversaturated traffic will cause queues which lead to travel delays. Traffic flow regulation alleviates this problem by determining the optimal input flow to the intersection, and holds back vehicles that cannot proceed beyond the virtual gate through V2I communication (see Fig. 4). The optimal input flow is determined by solving a constrained finite-time optimal control problem, which optimizes an objective function based on ambient traffic information (i.e., exogenous traffic demand from upstream roadways, queue status beyond the cooperative zone, turning ratios at the intersection, and the OD information of approaching vehicles).

### 5.1. Formulation of the CFTOC problem

We define the following variables to describe the traffic flow regulation. First, we define an entrance lane set: $I=\left\{1,2, \ldots, n_{I}\right\}$, where $n_{I}=12$; an exit lane set: $E=\left\{1,2, \ldots, n_{E}\right\}$, where $n_{E}=8$ (there are 8 exit lanes and 12 entrance lanes in Fig. 1). Then, an OD matrix $\mathcal{D} \in \mathbb{R}^{n_{I} \times n_{E}}$ is defined as: $[\mathcal{D}]_{i j}=$ $\left\{\begin{array}{ll}1, & \text { if OD }(i, j) \text { exists } \\ 0 & \text { otherwise }\end{array}\right.$ to describe which entrance lane $i \in I$ the traffic is coming from and which exit lane (0, otherwise $j \in E$ the traffic is heading to (detailed expression is shown in the Appendix A). Next, for a discrete time step $t$, we define a vector of queue lengths: $\omega(t)=\left[\omega_{1}(t), \ldots, \omega_{n_{I}}(t)\right]^{\dagger}$ at the virtual gates, and a vector of input flows $q(t)=\left[q_{1}(t), \ldots, q_{n_{I}}(t)\right]^{\dagger}$ passing through the virtual gate. The vector of exogenous traffic demand is $d(k)=\left[d_{1}(t), \ldots, d_{n_{I}}(t)\right]^{\dagger}$. The vector of input flow ratios (i.e., the ratio between input flow and exogenous traffic demand) is the decision variable obtained by solving the CFTOC problem: $\mu(t)=$ $\left[r_{1}(t), \ldots, r_{n_{I}}(t)\right]^{\dagger}$. The optimal input flow can then be calculated as: $q^{*}(t)=\mu(t)^{\dagger}\left(d(t)+\frac{\omega(t)}{\mathrm{dt}}\right)$. Correspondingly, the vector of traffic flows on exit lanes can be defined as: $q^{e}(t)=\mathcal{L}(t) q(t)=$ $\left[q_{1}^{e}(t), \ldots, q_{n_{E}}^{e}(t)\right]^{\dagger}=\left[\mathcal{L}_{1 .}(t) q(t), \ldots, \mathcal{L}_{n .}(t) q(t)\right]^{\dagger}$, where $\mathcal{L}(t) \in \mathbb{R}^{n_{I} \times n_{E}}$ is the flow distribution matrix mapping the input flow from entrance lane $i \in I$ to exit lane $j \in E . \mathcal{L}(t)$ is determined based on the turning ratio and OD matrix. Specifically, $[\mathcal{L}(t)]_{i j}$ indicates the proportion of input flow traveling from entrance lane $i$ to exit lane $j$ at time step $t$. The vector of the estimated capacities of exit lanes is denoted as: $Q=\left[Q_{1}, \ldots, Q_{n_{E}}\right]^{\dagger}$.

For a discretized operational time horizon (the duration of a cycle to perform the CFTOC) with $\iota=T / \mathrm{dt}$ time steps, where $T$ is the length of the operational time horizon and dt is the length of a time step, we formulate and solve a CFTOC problem to determine the optimal input flow that is permitted to enter the buffer zone at each time step $t \in\{0,1, . ., t\}$. During the implementation of iterative feedback loop (recall Fig. 2), the CFTOC is executed to enable traffic flow regulation, and then virtual platooning control is performed. This process repeats for $n_{l}$ iterations (i.e., $n_{l} \in\{1,2,3, \ldots\}$ ). The timeline of the iterative feedback loop is shown in Fig. 8(a). Specifically, after obtaining information on queue lengths $\omega\left(t_{n_{l}-1}\right)$, exogenous traffic demand $d\left(t_{n_{l}-1}\right)$, and estimated exit lane capacity $Q\left(t_{n_{l}-1}\right)$ from the final time step of previous operational time horizon $\llbracket t_{n_{l}-1}, t_{n_{l}} \rrbracket$, a new CFTOC problem is solved for the current operational time horizon $\llbracket t_{n_{l}}, t_{n_{l}+1} \rrbracket$ to obtain the optimal input flow vector $\{q(t)\}_{t=0}^{l}$, representing the traffic volumes permitted to proceed to the buffer zone at each entrance lane. Correspondingly, at each time step $t$ within an operational time horizon, the intersection controller executes traffic flow regulation based on $\mathrm{dt} q(t)$ (i.e., the number of vehicles permitted to proceed), and communicates with the approaching vehicles
through V2I communication on whether to proceed. The vehicles permitted to proceed will then execute the virtual platooning control during $\llbracket t_{n_{l}}, t_{n_{l}+1} \rrbracket$. In a deployment context, the queue lengths from the previous operational time horizon will be used to denote the initial condition for the CFTOC problem in current operational time horizon, while the estimated capacities of exit lanes and the exogenous traffic demand will be used as constant parameters throughout the current operational time horizon.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-24.jpg?height=1085&width=1270&top_left_y=492&top_left_x=428)
Fig. 8. Illustration of CFTOC: (a) timeline of iterative feedback loop; (b) variables at the virutal gates and exit lanes

Correspondingly, the CFTOC problem is formulated as follows:

$$
\begin{array}{ll}
\min _{\mu} J(\omega, \mu, t)=\sum_{t=0}^{l} \psi(\omega(t), \mu(t)) \\
\text { s.t. } & \omega(t+1)=f(\omega(t), \mu(t), d(t)) \\
& \omega(0)=\omega_{0} \\
& \mathcal{L}(t) q(t) \leq Q \\
& \omega_{\min } \leq \omega(t) \leq \omega_{\max } \\
& \mu_{\min } \leq \mu(t) \leq \mu_{\max }
\end{array}
$$

where $\psi(\omega(t), \mu(t))$ is the objective function from time step 0 to $\iota$, formulated as:

$$
\begin{gathered}
\psi(\omega(t), \mu(t))=\sum_{i \in I} b_{\omega, i}\left(\frac{\omega_{i}(t)}{\omega_{\max }}\right)^{2}+\mathrm{dt} \sum_{i \in I} b_{q, i}\left(\frac{\left(1-r_{i}(t)\right) q_{i}(t)}{r_{i}(t) Q_{j}}\right)^{2}+\sum_{i \in I} b_{f, i}\left[r_{i}(t)-\right. \\
\left.r_{i}(t-1)\right]^{2},[\mathcal{D}]_{i j}=1, i \in I, j \in E
\end{gathered}
$$

where $b_{\omega, i}$ is the scaling coefficient of traffic spillback in direction $i, b_{q, i}$ is the scaling coefficient of traffic prevented from entering the buffer zone in direction $i$, and $b_{f, i}$ is the scaling coefficient
corresponding to the difference between current and previous input flow ratio in direction $i$. The CFTOC (41) has three objectives: (i) penalizing traffic spillbacks to reduce travel delays, (ii) increasing the input inflow entering the buffer zone to improve the throughput (as it penalizes the traffic held back beyond the virtual gates), and (iii) alleviating inflow fluctuations to mitigate potential traffic oscillations. Each term in the objective function is also normalized within the range of $[0,1]$ to alleviate issues in tuning the scaling coefficients. Increasing the scaling coefficient of a specific objective in the objective function will increase the corresponding penalty value. Specifically, increasing $b_{\omega, i}$ will penalize the queue length more and emphasize the mitigation of traffic spillbacks more, but may be less effective in terms of the other two objectives. Increasing $b_{q, i}$ will increase the amount of vehicle permitted to proceed, which benefits the throughput, but may lead to longer transient queues. Increasing $b_{f, i}$ will encourage the intersection controller to generate a consistent $\mu(t)$ over the operational time horizon, which can improve the traffic smoothness, but may lead to longer queues when traffic demand suddenly increases.

In Equation (41), the first constraint describes the simplified discrete queueing dynamics (i.e., the time evolution of queue length $\omega(t)$ at the intersection entrance lanes):

$$
\omega_{i}(t+1)=f(\omega(t), \mu(t), d(t))=\omega_{i}(t)+\operatorname{dt}\left(d_{i}(t)-q_{i}(t)\right), i \in I
$$

where the input flow is determined by $q_{i}(t)=r_{i}(t)\left(d_{i}(t)+\frac{\omega_{i}(t)}{\mathrm{dt}}\right)$. As shown in Fig. 8 (b), the input flow is the traffic flow permitted to pass the virtual gate, while the exogenous traffic demand is the traffic flow arriving at the virtual gate. Thus, the difference in queue length between time steps $t$ and $t+1$ equals to the time step length (i.e., dt) times the difference between traffic demand and the input flow ( $d_{i}(t)-q_{i}(t)$ ). The reason for formulating the input flow in this way is to directly link the exogenous traffic demand and the current queuing status. Specifically, the $r_{i}(t)$ obtained by solving the CFTOC indicates that a specific portion of traffic flow (i.e., $d_{i}(t)+\frac{\omega_{i}(t)}{\mathrm{dt}}$ ) at the current time step can be permitted to enter the intersection buffer zone.
The second constraint indicates the initial queue length is $\omega_{0}$. The third constraint states that the traffic flow on a specific exit lane cannot exceed the lane capacity:

$$
\mathcal{L}_{i .}(t) q(t) \leq Q_{i}, i \in E
$$

where $\mathcal{L}_{i .}$ indicates the $i$ th row of matrix $\mathcal{L}$. The fourth constraint illustrates the lower and upper bounds of the queue length for each entrance lane:

$$
0 \leq \omega_{i}(t) \leq \omega_{\max }, i \in I
$$

where the minimum queue length is $\omega_{\min }=0$, the maximum queue length is given by $\omega_{\max }=$ $\max \left\{\bar{\omega}, \omega_{-1}+\mathrm{dt} d(t)\right\}$ to ensure the existence of the solution for the optimal input flow, $\bar{\omega}$ is a predetermined value for maximum queue length (obtained using empirical data), and $\omega_{-1}$ denotes the queue length obtained from the final step of the previous operational time horizon. The final constraint presents a feasible range for the input flow ratio:

$$
0 \leq \mu_{i}(t) \leq 1, i \in I
$$

where $\mu_{\min }=0, \mu_{\max }=1$. The estimated capacity of each exit lane $i \in E$ is obtained as:

$$
Q_{i}=\min \left\{Q_{m, i}, Q_{0, i}\right\}, i \in E
$$

where $Q_{0, i}$ is the maximum value of the traffic flow passing through an exit lane $i$ in the previous operational time horizons. $Q_{m, i}=\frac{v_{e q}}{\bar{d}_{m, i}}$ is the initial estimated capacity, where $v_{e q}$ is the intersection operating speed (recall the consensus in Equation (2)), and $\bar{d}_{m, i}$ is the car-following distance between vehicles traveling on the exit lane $i$ (e.g., 10 m). Note that $Q_{0, i}$ can also be obtained from historical data (i.e., maximum value of the traffic flow passing through an exit lane $i$ ) associated with previous operations (i.e., the recorded maximum traffic flow passing through an exit lane $i$ ).

### 5.2. Feasibility and solution of the CFTOC problem

In the CFTOC problem, the constraints associated with maximum queue length and exit lane capacity can create potential difficulties in obtaining the optimal solution. Specifically, to ensure that the feasible
region of CFTOC is not empty, the maximum queue length $\omega_{\text {max }}$ needs to be carefully selected at the beginning of each operational time horizon. A predetermined small default value of maximum queue length $\omega_{\max }=\bar{\omega}$ can lead to infeasibility when the exogenous traffic demand increases. By contrast, an excessively large $\omega_{\text {max }}$ can circumvent the issue of empty feasible region, but can degrade the control performance as a larger queue length is permitted in the control process. The following analysis is used to avoid an empty feasible region and alleviate the negative effect of traffic spillbacks.
Lemma 4: The lane capacity constraint (44) will not lead to an empty feasible region.
Proof: From constraint (43), we note that the exit lane capacity constraint (44) can be satisfied by appropriately adjusting the optimal input flow ratio $\mu^{*}(t)$ based on the following inequality:

$$
\mathcal{L}_{i .}(t) \mu^{*}(t)\left(d(t)+\frac{\omega(t)}{\mathrm{dt}}\right) \leq Q_{i}, i \in E
$$

Thus, the hard constraint on lane capacity will not lead to an empty feasible region, as we can always obtain a non-negative $\mu^{*}(t)$ to ensure Equation (48) is valid. This completes the proof of lemma 4. ■

Next, we discuss the maximum queue length in proposition 1.
Proposition 1: For an operational time horizon, by adaptively adjusting the maximum queue length as $\omega_{\text {max }}=\max \left\{\bar{\omega}, \omega_{-1}+\mathrm{dt} d(t)\right\}$ at the initialization, the feasible region of CFTOC
(41) has a non-empty interior.

Proof: We first substitute the input flow $q_{i}(t)$ into the dynamics of queue length in Equation (43) to obtain the following inequality:

$$
\omega_{i}(t)+\operatorname{dt}\left(d_{i}(t)-q_{i}(t)\right) \leq \omega_{i}(t)+\operatorname{dt} d_{i}(t), i \in E
$$

The right-hand side of Equation (49) provides an upper bound for the queue length at each time step $k$. Specifically, as the queue length in Equation (43) is stable (as the CFTOC keeps reducing the queue length), and the exogenous traffic demand is constant throughout the current operational time horizon, the queue length in each time step under traffic flow regulation will always be bounded by: $\omega(t+1) \leq \omega(t)+$ $\mathrm{dt} d(t), t \in \llbracket 0, \imath \rrbracket$. Thereby, incorporating the queue length $\omega_{-1}$ from the end of the previous operational time horizon, an upper bound for the maximum queue length for the current iteration can be derived as: $\omega_{-1}+\mathrm{dt} d(t)$, which circumvents the issue of empty feasible region triggered by large exogenous traffic demand. Correspondingly, the maximum queue length $\omega_{\text {max }}=\max \left\{\bar{\omega}, \omega_{-1}+\mathrm{dt} d(t)\right\}$ can guarantee that the feasible region of Equation (41) is non-empty even if the predetermined default upper bound $\bar{\omega}$ is too small (infeasible). This completes the proof of Proposition 1. ■

With the solution feasibility guaranteed, and as the objective function (42) and the queueing dynamics (43) are both smooth and continuously differentiable, the CFTOC problem can be efficiently solved using existing numerical algorithms. In this study, the CFTOC is programmed using YALMIP optimization package (Löfberg, 2004) in MATLAB, and then solved backwards in time (similar to the backward dynamic programming technique (Lewis et al., 2012)) using the built-in function "fmincon" with interior-point algorithm (Potra and Wright, 2000).
Remark 5: It is also worth noting that as traffic flow regulation adaptively captures the queue status generated from virtual platooning control to regulate the input flow at the intersection (through the iterative feedback loop), it can be further applied to coordinate virtual platooning control in multi-intersection scenarios. In the multi-intersection control problem, the traffic flows on exit lanes of an intersection will become the exogenous traffic demand for its adjacent intersections. Correspondingly, the intersection controllers can communicate with each other to exchange information on queue status on entrance lanes and traffic flow on exit lanes. Then, they can cooperatively adjust the input flow ratios based on a prespecified objective (e.g., maximizing the throughput or minimizing the total travel delay over all intersections) to enable the cooperative control of multiple intersections.

## 6. Numerical experiments

Three sets of numerical experiments are conducted to showcase the effectiveness of proposed intersection control framework. The first set of experiments focuses on analyzing the microscopic vehicle-
level performance of virtual platooning control (i.e., in terms of maintaining desired safe spacing and intersection operating speed), where we compare the virtual-platooning control with/without consideration of uncertain vehicle parameters, and investigate effect of not separating late-arriving vehicles into independent virtual platoons. The second set of experiments evaluates the intersection control by analyzing the macroscopic mobility performance of the iterative feedback loop in Fig. 2 (involving virtual platooning control and traffic flow regulation), in terms of mitigating traffic spillbacks and travel delays, under asymmetric and heterogeneous (time-varying) traffic demand scenarios. The third set of experiments compares the performance of the proposed intersection control framework to other existing signal-free and signalized intersection control methods, under different traffic demand levels and symmetric/asymmetric traffic demand scenarios. The experiments are conducted using MATLAB R2019b, PyTorch (Paszke et al., 2019) and SUMO (Lopez et al., 2018) on a personal laptop with Intel CORE i7 CPU.
6.1. Vehicle-level performance
6.1.1. Eight-vehicle virtual platoon

We first consider an experiment with an eight-vehicle homogeneous platoon (i.e., all vehicles have the same vehicle parameters) to verify the effectiveness of virtual platooning control at the vehicle level. Specifically, eight vehicles approach the intersection from the entrance lanes 1, 9, 5, 13, 14, 3, 4, and 11, respectively. Related to analyzing the local stability, the initial spacing errors and speed tracking errors of the platoon are assumed to follow normal distributions with zero means, and variances of 3 and 0.3, respectively. The initial accelerations are set to zero for all vehicles. After vehicles converge to the intersection operating speed of 15m/s for some time, the intersection operating speed is increased to 17m/s to simulate speed change and test the string stability performance. To obtain the vehicle position, speed and acceleration, we integrate the ODEs in the vehicle dynamics model (7)-(9) using ODE15's (Shampine and Reichelt, 1997) built-in solver. To mitigate the chattering phenomenon associated with the sliding mode control method (Young et al., 1999), and ensure the differentiability of the intermediate control decision, we replace the $\operatorname{sgn}(\cdot)$ function in the control decision with $\tanh (\cdot)$ function. The ground truth vehicle parameters are randomly sampled within the upper-bounds and lower-bounds shown in Table 1. The parameters of the vehicles, intersection, and controllers are also listed in Table 1.

Table 1. Numerical experiment parameters
| Intersection parameters | Notation | Value |
| :--- | :--- | :--- |
| Radius of cooperative zone | $R_{c}$ | 200 m |
| Length of buffer zone | $L_{B}$ | 100 m |
| Lane width | $w_{l}$ | 4 m |
| Safety cushion | $\epsilon$ | 4 m |
| Acceleration from stop | $a_{c}$ | $1.25 \mathrm{~m} / \mathrm{s}^{2}$ |
| Vehicle parameters | Notation | Value |
| Nominal vehicle weight | $M_{i}^{\text {nom }}$ | 1650 kg |
| Nominal air drag coefficient | $c_{i}^{\text {nom }}$ | 0.25 |
| Nominal rolling resistance | $f_{i}^{\text {nom }}$ | 405N |
| Nominal disturbance magnitude | $\delta_{i}^{\text {nom }}$ | 1650 N |
| Nominal inertial delay factor | $\tau_{i}^{\text {nom }}$ | 0.5 |
| Gravity | $g$ | $9.81 \mathrm{~m} / \mathrm{s}^{2}$ |
| Upper bound of air drag coefficient | $\bar{c}_{i}$ | 0.5 |
| Lower bound of air drag coefficient | $\underline{c}_{i}$ | 0.2 |


Upper bound of rolling resistance Lower bound of rolling resistance Upper bound of disturbance magnitude Lower bound of disturbance magnitude Upper bound of vehicle weight Lower bound of vehicle weight weight Notation Control gain of cooperative sliding surface Control gain of backstepping control decision Robust margin Weighting of air drag coefficient in parameter adaptation law Weighting of rolling resistance in parameter adaptation law Weighting of disturbance magnitude in parameter adaptation law Weighting of vehicle weight in parameter adaptation law Coefficient of ODE Diagonal weight of Laplacian matrix Off-diagonal weight of Laplacian matrix $w_{i, 2}$ $w_{i, 2}$ $w_{i, 2}$ 0.9

Given eight vehicles: $i=1,2, \ldots, 8$, approaching from entrance lanes $1,9,5,13,14,3,4$, and 11 , respectively, the virtual platoon is constructed using vehicle indices into four compatible passing sets: $\{\{1$, $2\},\{3,4\},\{5\},\{6,7,8\}\}$; they are labeled as compatible passing set $1,2,3$, and 4 , respectively.

Table 2 shows the time at which each vehicle passes the conflict zone (i.e., reaches the corresponding exit lane). We note that vehicles in the same compatible passing set (e.g., vehicles 1 and 2) proceed through the intersection simultaneously, while vehicles in different compatible passing sets (vehicles 4 and 5 ) have a time margin between them to avoid collisions. The results in terms of vehicle states are illustrated in Fig. 9. Fig. 9(a) illustrates that spacings between vehicles in the same compatible set (e.g., vehicles 1 and 2 in compatible passing set 1) converge to zero, indicating that they pass through the intersection simultaneously. Fig. 9(b) shows that the spacings between vehicles in different compatible passing sets (e.g., vehicle 2 in compatible passing set 1 and vehicle 3 in compatible passing set 2) converge to specific values, indicating that vehicles with conflicts maintain some desired safe spacing when passing through the intersection. Fig. 9(c) illustrates that vehicle speeds in the virtual platoon converge to the intersection operating speed with minor fluctuations, thereby achieving the desired speed tracking performance. The asymptotic convergence of spacings and speeds demonstrate the effectiveness of the proposed DASMC in terms of mitigating the effects of parametric inaccuracies and unparameterized disturbances in the vehicle dynamics model, and
driving vehicles to the consensus cooperatively and safely. In addition, when the intersection operating speed increases from 15m/s to 17m/s at 12 seconds, the speed profiles of vehicles upstream in the virtual platoon track that of the vehicle at the front, illustrating the marginal string stability property. This property can benefit intersection operations under the constant spacing policy, as spacing will not be altered (as shown in Figs. 9(a) and 9(b)) and the achieved consensus can be consistently preserved.

Table 2. Conflict zone passing time of vehicle
| Vehicle index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Passing time (sec) | 13.67 | 13.67 | 14.41 | 14.41 | 15.21 | 17.15 | 17.15 | 17.15 |


![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-29.jpg?height=1258&width=1466&top_left_y=769&top_left_x=353)
Fig. 9. Virtual platooning control performance: (a) spacings between non-conflicting vehicles; (b) spacings between conflicting vehicles; (c) vehicle speeds

Fig. 10 shows the results of vehicle parameter estimations. The estimated values of air drag coefficient, rolling resistance, and vehicle weight converge to specific values despite minor fluctuations. The estimated amplitude of the lumped unparameterized disturbances remains the same as the initial nominal value (see Fig. 10(c)), because the robust control decision dominates the lumped unparameterized disturbances throughout the control process. Hence, the error triggered by the lumped unparameterized disturbances are always close to zero. From Equation (32), we note that the gradient of the estimated lumped unparameterized disturbances is zero, implying they are unchanged. Additionally, all estimated vehicle parameters deviate from their actual values even after converging to the steady state. This phenomenon is
due to the persistence excitation (PE) condition (Boyd and Sastry, 1986) of the vehicle dynamics model. The desired safe spacing and intersection operating speed used in this experiment do not satisfy the PE condition of the vehicle dynamics model. Hence, the smooth projection-based parameter adaptation law cannot accurately estimate the vehicle parameters in the control process. However, even with inaccurately estimated (but converged) vehicle parameters, the DASMC stabilizes the virtual platoon because stability can be achieved not only through control decisions implemented with accurate vehicle parameters, but also through other control decisions with vehicle parameters estimated from the parameter adaptation law. This phenomenon is analogous to the underdetermined least-square estimation problem, where multiple combinations of parameters can lead to the same solution.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-30.jpg?height=1285&width=1633&top_left_y=643&top_left_x=240)
Fig. 10. Estimated vehicle parameters: (a) air drag coefficient; (b) rolling resistance; (c) disturbance magnitude; (d) vehicle weight

### 6.1.2. Eight-vehicle virtual platoon without DASMC

Fig. 11 shows the spacings of an eight-vehicle virtual platoon controlled under a distributed sliding mode controller (DSMC) (Wu et al., 2016) instead of the proposed DASMC. Vehicle parameters are randomly sampled within the bounds in Table 1, and deviate from the nominal values used in Wu et al., 2016. As the DSMC does not factor parametric uncertainties or unparameterized disturbances in the control design process, the spacings all diverge to undesired values compared to those in Fig. 9, indicating that DSMC fails to safely move the vehicles through the intersection. It also leads the failure of the ODE solver, resulting in the simulation lasting for less than 6 seconds. When juxtaposed with Fig. 9, the results further highlight the capabilities of the proposed DASMC in dealing with the parametric uncertainties and
unparameterized disturbances of vehicles, and enabling safe operation of signal-free intersection control in the real world.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-31.jpg?height=674&width=1577&top_left_y=337&top_left_x=251)
Fig. 11. Virtual platooning control with DSMC: (a) spacings between non-conflicting vehicles; (b) spacings between conflicting vehicles

### 6.1.3. Impacts of grouping new vehicles into independent virtual platoons

This experiment uses two scenarios to analyze the impacts of having new vehicles join an existing virtual platoon with consensus versus grouping them into an independent virtual platoon. In the first scenario, five vehicles are added near the tail of the existing virtual platoon in Fig. 9 that has reached consensus, implying a small spacing between the new vehicles and the existing platoon. The spacing between the first new vehicle and the tail of the existing virtual platoon is set to 15m, to simulate the situation where vehicles are relatively close to each other in heavy traffic conditions. If these vehicles join the existing virtual platoon and aim to achieve a new consensus with the current platoon vehicles, Figs. 12(a) and (b) show that the new vehicles induce fluctuations in speeds and spacings in the existing virtual platoon, which affects the smoothness and comfort of platoon operation. However, as vehicles are relatively close to each other, the perturbations are mitigated quickly and will not introduce safety concerns in the intersection control process. Hence, the impacts when spacings are small are not particularly severe. By contrast, as shown in Figs. 12(c) and (d), if new vehicles do not join the existing platoon and form a new independent virtual platoon, the fluctuations in vehicle speeds and spacings are even lower. This illustrates that grouping new vehicles into an independent virtual platoon is beneficial even when impacts are not severe due to the small spacings.

In the second scenario, vehicles in the existing virtual platoon are relatively further away from the newlyarriving vehicles; for example, the first vehicle of the existing virtual platoon may have arrived into the conflict zone, which can happen under lighter traffic conditions. In such a situation, if the new vehicles join the existing virtual platoon, they will cause vehicles near the tail of the existing virtual platoon to suddenly decelerate (see red curves in Fig. 13(a)) while accelerating themselves abruptly to catch up (see blue dashed line in Fig 13(a)) with the existing virtual platoon so as to achieve consensus. This phenomenon will increase the existing virtual platoon's travel time and significantly affect riding comfort. More importantly, Fig. 13(b) illustrates that spacings of vehicles in the existing virtual platoon are also perturbed and deviate from the desired values significantly. Then, vehicles need a long time to achieve a new consensus. If the new consensus is not achieved before vehicles arrive into the conflict zone, collisions will potentially occur. By contrast, as shown in Figs. 13(c) and (d), if the new vehicles are grouped as an independent virtual platoon, the fluctuations in vehicle speeds and spacings are significantly mitigated for the new vehicles, enabling them to achieve a new consensus more quickly (in Fig 13(c), the new vehicles reach a new
consensus in about 7 seconds). In addition, the speeds and spacings of vehicles in the existing virtual platoon will not change. Akin to the first scenario, the various impacts reinforce the value in grouping new vehicles into an independent virtual platoon for enhancing safety and smoothness.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-32.jpg?height=1294&width=1600&top_left_y=385&top_left_x=247)
Fig. 12. New vehicles are near the existing virtual platoon: (a) vehicle speeds when new vehicles join the existing virtual platoon; (b) spacings between non-conflicting vehicles in the existing virtual platoon when new vehicles join ithe existing virtual platoon; (c) vehicle speeds when new vehicles do not join the existing virtual platoon; (d) spacings between non-conflicting vehicles in the existing virtual platoon when new vehicles do not join the existing virtual platoon

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-33.jpg?height=1333&width=1624&top_left_y=251&top_left_x=244)
Fig. 13. New vehicles are further away from the existing virtual platoon: (a) vehicle speeds when new vehicles join the existing virtual platoon; (b) spacings between non-conflicting vehicles in the existing virtual platoon when new vehicles join the existing virtual platoon; (c) vehicle speeds when new vehicles do not join the existing virtual platoon; (d) spacings between non-conflicting vehicles in the existing virtual platoon when new vehicles do not join the existing virtual platoon

### 6.1.4. Forty-one vehicles in two virtual platoons

To further demonstrate the effectiveness of virtual platooning control in the real world, we generate 41 vehicles whose vehicle parameters are randomly selected from the parameter bounds in Table 1. The controller parameters and initial conditions (i.e., spacing errors, speed tracking errors, and accelerations) are identical to those of the experiment in section 6.1.1. The intersection operating speed is set to 15m/s. Note that here we include extra noise in the vehicle states, as real-world vehicle states can contain measurement noise. The measurement noises of position, speed, and acceleration are assumed to follow normal distributions with zero means, and standard deviations of 0.17, 0.13, and 0.1 (Zhou et al., 2020), respectively. Then, to mitigate the effect of measurement noise, we apply a low-pass filter $\frac{20}{s+20}$ to smoothen vehicle states used in the DASMC control decision. We include the following animation to provide a direct visualization of vehicle movements when they pass through the intersection conflict zone: https://drive.google.com/open?id=1qTEkkJzI5aenuHQD107yakwEf1fKSIdq. In it, the approaching vehicles are separated into two independent virtual platoons, with vehicles 1-16 belonging to the first virtual
platoon, and the remaining 25 vehicles belonging to the second one. All vehicles can maintain desired safe spacings with each other to pass the conflict zone sequentially, illustrating the effectiveness of the proposed virtual platooning control method in mitigating the effects of parametric inaccuracies and unparameterized disturbances to achieve consensus safely. Fig. 14 illustrates the vehicle speeds and accelerations, where vehicles in the same compatible passing set are grouped into the same subplot. The subplots indicate the convergence of vehicle states, and mild overshoots/undershoots of vehicle speeds and accelerations, implying the desired transient and steady-state response of the proposed DASMC.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-34.jpg?height=1238&width=1480&top_left_y=559&top_left_x=321)
Fig. 14. Vehicle speeds and accelerations for the two platoons

### 6.2. Evaluation of intersection control

This set of numerical experiments aims at evaluating the integration of virtual platooning control and traffic flow regulation to mitigate traffic spillbacks and travel delays. The vehicle parameters, controller parameters, and initial conditions are identical to those in section 6.1.2. The operational time horizon of the traffic flow regulation is set as $T=200 s$, and the length of time step is $\mathrm{dt}=20 s$. The total simulation time is 1200 seconds. Thus, each experiment has 60 time steps, where 6 iterations of the CFTOC problem are solved sequentially. The vehicle arrival time interval at the virtual intersection gate follows a Poisson distribution. The right-turning ratios are set as 0.25 for the right lane. The intersection operating speed has a constant value of 15m/s. In the CFTOC formulation, the default maximum queue length is set to $\bar{\omega}=7$, the scaling coefficient of traffic spillback is $b_{\omega}=1$, the scaling coefficient of throughput is $b_{q}=0.6$, and the scaling coefficient of inflow fluctuation is $b=0.2$. The scaling parameters are determined through the grid-search method. Specifically, we sample the scaling parameters from the [0,1] interval with 0.2 increments, to perform simulations for the traffic demand of 600veh/hr/lane. Then, we select the
combination of scaling parameters which yields the smallest average queue length. The first-order optimality measure (i.e., 2-norm of the gradient of the Lagrangian, which evaluates the optimality gap) is used as the indicator for the optimal solution (Vanderbei and Shanno, 1999). In the following numerical experiments, the first-order optimality measure always decays and is smaller than the optimality tolerance (i.e., 1e-6) after some iterations (smaller than the maximum number of iterations), indicating that the objective function has converged and the optimal solution of the CFTOC problem has been obtained.

In the first experiment, we consider a case with symmetric traffic demand, where the exogenous traffic demand on each lane is set as 600veh/hr/lane. As illustrated in Fig. 15, when traffic flow regulation is incorporated, the maximum queue length (as shown in the y-axis) and the queue time (indicated by green/red double-edge arrows) in each direction (i.e., each entrance lane) from the buffer zone are smaller than those without traffic flow regulation. This phenomenon is as expected under the proposed control framework, as the CFTOC actively regulates the number of vehicles permitted to proceed to the buffer zone. Thereby, once a queue starts to accumulate in any direction, the input flow in that direction is correspondingly reduced to alleviate the undesired stop-and-go movements and traffic spillbacks. Note that we show the queue status for only the first four directions in Figs. 15-17 for readability. The queue status for all directions is illustrated in Appendix D.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-35.jpg?height=522&width=1162&top_left_y=973&top_left_x=477)
Fig. 15. Queue status for directions 1-4 under symmetric traffic demand

Next, the case of asymmetric traffic demand is considered, where the exogenous traffic demand in the north and south bound directions (i.e., 1, 2, 3, 7, 8, and 9) is set as 1000veh/hr/lane, while the traffic demand in the east and south bound directions (i.e., 4, 5, 6, 10, 11, 12) is 600veh/hr/lane. Comparing Fig. 16 to Fig. 15, we can observe that with more traffic demand in the north and south bound directions, the queue lengths in directions 1, 2, 3, 7, 8, and 9 increase dramatically, especially for the case without traffic flow regulation. Specifically, the traffic flow regulation weighs the queue lengths in all directions equally, thereby preventing the queues in the north and south bound directions from increasing excessively compared to those in the east and west bound directions. The queue lengths in other directions (i.e., 4, 5, 6, 10, 11, 12) also increase due to the impact of increased traffic demand in the north and south bound directions. However, with traffic flow regulation, the growth of queue length is less severe than the case without traffic flow regulation. This is because the traffic flow regulation adaptively adjusts the input flow to mitigate the queue lengths in all directions. Thus, the virtual platooning control with traffic flow regulation can effectively deal with the asymmetric traffic demand and alleviate uneven traffic spillbacks.

The case of heterogeneous traffic demand (i.e., traffic demand in each direction is time-varying during the experiment) is then considered, where we compare three cyclic traffic demand patterns:

$$
\begin{aligned}
& d_{i}^{\text {pattern1 }}(t)=\left\{\begin{array}{c}
600 \text { veh } / \mathrm{hr} / \text { lane }, \text { if } t=2 \mathfrak{x}+1, \quad x=0,1,2, \ldots \\
400 \text { veh } / \mathrm{hr} / \text { lane }, \quad \text { otherwise }
\end{array}, i \in I,\right. \\
& d_{i}^{\text {pattern } 2}(t)=\left\{\begin{array}{r}
600 \mathrm{veh} / \mathrm{hr} / \text { lane }, \text { if } t=2 \mathfrak{x}+1, \quad \mathfrak{x}=0,1,2, \ldots \\
1200 \mathrm{veh} / \mathrm{hr} / \text { lane, } \text { otherwise }
\end{array}, i \in I,\right. \text { and } \\
& d_{i}^{\text {pattern } 3}(t)=\left\{\begin{array}{r}
1200 \mathrm{veh} / \mathrm{hr} / \text { lane, } \text { if } t=4 \mathfrak{x}, \mathfrak{x}=0,1,2, \ldots \\
600 \mathrm{veh} / \mathrm{hr} / \text { lane, } \text { otherwise }
\end{array}, i \in I .\right.
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-36.jpg?height=527&width=1206&top_left_y=247&top_left_x=459)
Fig. 16. Queue status for directions 1-4 under asymmetric traffic demand

Fig. 17 illustrates that the cyclic demand induces more fluctuations in queue lengths (compared to the homogeneous case with constant traffic demand over time in Fig. 15). In addition, a larger cyclic traffic demand pattern (pattern 2 in Fig. 17(b)) triggers longer queue dwelling time and greater queue length in every direction compared to those of a smaller cyclic traffic demand pattern (pattern 1 in Fig. 17(a)). Further, a shorter duration of large traffic demand (e.g., pattern 3 in Fig. 17(c)) will induce shorter queue dwelling time and smaller queue length. The proposed intersection control framework can effectively prevent the queue length from increasing indefinitely under heterogenous (cyclic) traffic demand. Also, a comparison of the cases with traffic flow regulation to those without traffic flow regulation illustrates appreciably smaller queue length and queue dwelling time, indicating the effectiveness of the proposed traffic flow regulation in dealing with heterogenous (cyclic) traffic demand.
![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-36.jpg?height=1081&width=1249&top_left_y=1310&top_left_x=439)

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-37.jpg?height=548&width=1263&top_left_y=241&top_left_x=432)
Fig. 17. Queue status for directions 1-4 under heterogeneous (time-varying) traffic demand: (a) pattern 1; (b) pattern 2; (c) pattern 3

The maximum computational time for virtual platoon formation, constructing compatible passing sets, and determining safe spacing is 0.076753 seconds throughout the experiment, which validates the computational efficiency of the proposed algorithms. Additionally, Fig. 18 shows the computational time in solving the CFTOC problem across the six iterations, for the five traffic demand scenarios. The computational time has a mean of 0.6475 seconds and a standard deviation of 0.1089 . Correspondingly, the computational time under the various traffic demand scenarios stay consistently below the length of the intersection control time step ( $\mathrm{dt}=20 \mathrm{sec}$ ), indicating that the optimal input flow can be obtained promptly without delay. Thus, the CFTOC problem can be implemented efficiently in real-time. Note that if the CFTOC problem is programmed using more efficient languages (e.g., C++, Julia) rather than solved in MATLAB, the computational speed can be much faster. This result also provides pointers for selecting an appropriate lower bound for the length of the time step (the sampling interval of intersection controller), which should be at least greater than the upper bound of the computational time. Otherwise, the CFTOC may not be sufficiently sensitive to the variations in the approaching traffic, and can potentially destabilize the intersection control process at times (i.e., leading to unbounded queue length).

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-37.jpg?height=694&width=1119&top_left_y=1521&top_left_x=503)
Fig. 18. CFTOC computational time

### 6.3. Comparison of different control methods under varying traffic demand

This section compares the performance of different control methods designed for signalized and signal-free intersections under different traffic demand scenarios (i.e., symmetric and asymmetric). In addition to the proposed intersection control framework with and without traffic flow regulation, an uncoordianted virtual-
platooning control with first-come-first-serve (FCFS) policy without traffic flow regulation is also included in the comparison. When the uncoordinated FCFS virtual-platooning control is applied, the intersection controller will not search for a compatible passing set with maximum cardinality to group vehicles. Instead, a vehicle will pass through the intersection to maintain desired safe spacings with its immediate predecessor and successor vehicles. In addition, we include a fixed-time signalized intersection control with a fixed time duration for each phase. The phase sequence is \{north-south green, north-south left-turn green, east-west green, east-west left-turn green\}; each phase is for 60 seconds. A deep Q-network (DQN)-based adaptive signalized intersection control method by Genders and Razavi (2019) is also considered. The intersection controller can obtain access to the upstream traffic demand through V2I communications. Each lane in the cooperative zone is separated into several cells of length of five meters. The state of the reinforcement learning environment at each time step is a tensor that includes the occupancy of each cell in the cooperative zone (i.e., 1 for occupied, 0 for empty), the average speed of vehicles in each cell, and the current signalized phase. The action is the signal phase. The reward function is the negative value of the total queue length over all directions. The DQN training is programmed using PyTorch (Paszke et al., 2019), and the simulation of signalized intersection control is conducted using SUMO (Lopez et al., 2018). The movement of CAVs in the signalized intersection control is modeled using the intelligent driver model (IDM) (Treiber et al., 2000) with parameters shown in Table 3.

Table 3. IDM parameters
| Parameters | Value | Parameters | Value |
| :--- | :--- | :--- | :--- |
| Desired time headway | 2s | Acceleration exponent | 4 |
| Maximum acceleration | $2 \mathrm{~m} / \mathrm{s}^{2}$ | Jam spacing | 2 m |
| Desired deceleration | $4 \mathrm{~m} / \mathrm{s}^{2}$ | Desired speed | 15 m/s |


To simulate the scenarios with symmetric traffic demand, we vary the traffic demand from 500veh/hr/lane to 2500veh/hr/lane with 500veh/hr/lane increments for all directions. Ten runs are conducted for each demand scenario. The average total queue length over all directions across all time steps is computed as: $\frac{1}{10} \sum_{\text {run }} \frac{1}{\mid \text { steps } \mid} \sum_{t \in \text { steps }} \sum_{i \in I}$ Queue $_{i}(t)$. The average total travel delay for all vehicles is computed as: $\frac{1}{10} \sum_{\text {run }} \sum_{i \in \Upsilon_{s}}$ Delay $_{i}$. The travel delay (i.e., Delay ${ }_{i}$ ) of vehicle $i$ is defined as the difference between its travel time when traveling at the intersection operating speed and its actual travel time recorded in the experiment. Note that the travel time in signal-free control methods is the time a vehicle spends to travel from its stopping location beyond the virtual gate to the entrance of the corresponding exit lane. For signalized control methods, the travel time is the time a vehicle travels from the buffer zone boundary to the entrance of the corresponding exit lane.

Figs. 19(a) and 19(b) illustrate the average total queue length and average total travel delay, respectively, of each intersection control method. As the traffic demand increases, both the queue length and the total travel delay increase monotonically for all methods. The two figures show that both the traffic flow regulation and the coordination of virtual platoons help to mitigate queues and delays. Further, the signalfree virtual platooning intersection control methods outperform the signalized intersection control methods as they regulate all vehicle movements simultaneously and coordinate vehicles' actions cooperatively. However, the difference between the DQN-based adaptive signalized control and uncoordinated FCFS virtual-platooning control without traffic flow regulation is not significant. This is because the DQN-based adaptive signalized control can adjust the number of vehicles passing the intersection using the queue status to improve the situational awareness and efficiency of intersection control. Table 4 illustrates the percentage reduction in average total queue length computed by the proposed control framework compared to the other four methods. It shows that the queue length reductions first increase and then decrease as traffic demand increases. This is because the use of virtual platooning control and traffic flow regulation under lower demand conditions provides more opportunities to enhance intersection efficiency, while the higher densities of traffic under oversaturated traffic conditions reduce the flexibility in coordinating virtual platoons and regulating traffic flow.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-39.jpg?height=654&width=1584&top_left_y=244&top_left_x=247)
Fig. 19. Comparison of intersection control methods with symmetric traffic demand: (a) average total queue length; (b) average total delay

Table 4. Percentage reduction in average total queue length under virtual platooning with regulation compared to the other control methods in the symmetric demand case
|  | Virtual platooning W/O regulation | FCFS virtual platooning W/O regulation | DQN adaptive signalized control | Fixed-time signalized control |
| :--- | :--- | :--- | :--- | :--- |
| 500veh/hr/lane | 39.62\% | 55.48\% | 64.27\% | 72.02\% |
| 1000veh/hr/lane | 44.10\% | 63.57\% | 68.28\% | 73.37\% |
| 1500veh/hr/lane | 42.37\% | 59.29\% | 62.95\% | 68.45\% |
| 2000veh/hr/lane | 40.68\% | 58.96\% | 62.41\% | 67.68\% |
| 2500veh/hr/lane | 28.79\% | 42.05\% | 46.81\% | 56.80\% |


In the asymmetric traffic demand scenario, the traffic demand in the east and west bound directions is varied from 500 veh $/ \mathrm{hr} /$ lane to 2500 veh $/ \mathrm{hr} /$ lane in 500 veh $/ \mathrm{hr} /$ lane increments and the traffic demand in the north and south bound directions is 1.5 times that in the east and west bound directions. Figs. 20(a)-(c) show the average total queue length in the north and south bound directions, the average total queue length in the east and west bound directions, and the average total travel delay, respectively. The queue lengths increase with the number of vehicles traveling in the north and south bound directions. A comparison of results shown in Figs. 20(a)-(c) and Table 5 illustrates trends similar to the symmetric traffic demand case. This indicates that the proposed control framework can also handle asymmetric traffic demand effectively. Fig. 20(d) shows the ratios of the total queue lengths in the north and south bound directions and the east and west bound directions. It illustrates that the fixed-time signalized control method yields the highest ratio as it is not responsive to the increased demand in the north and south bound directions. It also illustrates that the proposed control framework yields the lowest ratio as traffic flow regulation reduces the asymmetry in the queue lengths as it weighs the queue length in each direction equally, thereby allowing more input flows in the north and south bound directions to mitigate queue growth. The coordination of virtual platoons also helps to alleviate the asymmetry as it assigns more vehicles from the north and south bound directions to maximize the size of compatible passing sets. The DQN-based adaptive signalized control is aware of the traffic demand in each direction, and thereby adjusts the signal phase to mitigate the queue length asymmetry.

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-40.jpg?height=1281&width=1618&top_left_y=249&top_left_x=244)
Fig. 20. Comparison of intersection control methods with asymmetric traffic demand: (a) average total queue length in north and south bound directions; (b) average total queue length in east and west bound directions; (c) average total delay over all directions; (d) ratio of queue lengths in north and south directions and east and west bound directions

Table 5. Percentage reduction in average total queue length in the asymmetric demand case
|  | Virtual platooning W/O regulation | FCFS virtual platooning W/O regulation | DQN adaptive signalized control | Fixed-time signalized control |
| :--- | :--- | :--- | :--- | :--- |
| 500veh/hr/lane | 36.67\% | 53.59\% | 63.58\% | 79.08\% |
| 1000veh/hr/lane | 51.12\% | 69.72\% | 78.52\% | 84.61\% |
| 1500veh/hr/lane | 42.97\% | 57.68\% | 66.98\% | 74.79\% |
| 2000veh/hr/lane | 34.88\% | 56.93\% | 61.50\% | 70.21\% |
| 2500veh/hr/lane | 34.57\% | 54.20\% | 59.29\% | 68.62\% |


Next, we compare the previous five methods with two recent signal-free intersection methods. The first is a centralized signal-head-free intersection control logic (SICL) (Mirheli et al., 2018) in which vehicle trajectories are optimized in a centralized fashion to minimize the total travel time of approaching vehicles and ensure safety (i.e., collision avoidance). The second is a distributed coordinated signal-free intersection control logic (DC-SICL) (Mirheli et al., 2019). For consistency in comparing the performance of the signalfree methods with the previous five methods, we use the two-lane (left and through movements) intersection from Mirheli et al. (2018) and Mirheli et al. (2019) for this experiment. Additionally, we also define an intersection performance metric for the comparison, labeled the "out/in ratio" which is computed as the
throughput of the intersection divided by the total traffic demand arriving at the intersection. In this comparison, we incorporate two traffic demand patterns based on scenarios 4 and 8 from the numerical experiments of Mirheli et al. (2019). Traffic demand pattern 1 is a symmetric demand case, where the through demand is 900veh/hr/lane, and the left-turn demand is 600veh/hr/lane, for both the east and west bound directions and the north and south bound directions. Traffic demand pattern 2 is an asymmetric demand case, where the through and left-turn demands in the east and west bound directions are 1500veh/hr/lane and 600veh/hr/lane, respectively, and the through and left-turn demands in the north and south bound directions are 1100veh/hr/lane and 150veh/hr/lane, respectively.

Table 6 illustrates that the out/in ratio of the proposed control framework is the largest, while the virtual platooning control without traffic flow regulation has an out/in ratio similar to that of SICL and DC-SICL. The results indicate that virtual platooning control can lead to similar intersection efficiencies as other trajectory optimization-based methods. The benefit of traffic flow regulation in improving intersection efficiency is also illustrated. The results also suggest that distributed intersection control methods (i.e., virtual platooning control and DC-SICL) can achieve performance comparable to centralized ones (i.e., SICL). The uncoordinated FCFS virtual-platooning control (also, without traffic flow regulation) ranks fourth as platoons are not coordinated and thus less efficient during the operation. Additionally, akin to previous results, signalized control methods are outperformed by signal-free control methods, in that they cannot coordinate all vehicle movements simultaneously or cooperatively, leading to inefficiencies and non-smooth stop-and-go situations.

Table 6. Comparison of out/in ratios
| Traffic demand pattern 1 |  | Traffic demand pattern 2 |  |
| :--- | :--- | :--- | :--- |
| Control method | Out/in ratio | Control method | Out/in ratio |
| Virtual platooning control with traffic flow regulation | 0.2532 | Virtual platooning control with traffic flow regulation | 0.2706 |
| Virtual platooning control without traffic flow regulation | 0.2396 | Virtual platooning control without traffic flow regulation | 0.2588 |
| FCFS virtual platooning control without traffic flow regulation | 0.2253 | FCFS virtual platooning control without traffic flow regulation | 0.2407 |
| DC-SICL | 0.2418 | DC-SICL | 0.2578 |
| SICL | 0.2418 | SICL | N/A* |
| DQN-based adaptive signalized control | 0.1591 | DQN-based adaptive signalized control | 0.1673 |
| Fixed-time signalized control | 0.1182 | Fixed-time signalized control | 0.1194 |


* N/A means the SICL fails to generate vehicle trajectories.

In summary, insights from the results indicate the effectiveness of the proposed intersection control framework in alleviating traffic spillbacks and travel delays at intersections under both symmetric and asymmetric traffic demand.

## 7. Concluding comments

This study proposes a novel hybrid cooperative signal-free intersection control framework for CAVs to improve virtual platooning-based control. It combines the proposed DASMC-based microscopic virtual platooning control with the proposed CFTOC-based macroscopic traffic flow regulation, and is implemented as an iterative feedback loop. In the virtual platooning control, the approaching vehicles are grouped into independent virtual platoons to assure smooth operations. For vehicles within the same independent virtual platoon, algorithms are designed to group them into compatible passing sets and to obtain desired safe spacings between compatible passing sets. Correspondingly, an appropriate IFT is constructed to ensure the structural controllability of the virtual platoons so that all approaching vehicles
can be fully controlled to maintain desired safe spacings and the intersection operating speed. After setting up the IFT, the proposed DASMC effectively suppresses the negative effects of parametric inaccuracies and unparameterized disturbances in the vehicle dynamics model so as to enable the local stability and string stability of the virtual platoons. Furthermore, to enhance intersection control performance in heavy traffic scenarios, traffic flow regulation is proposed using the CFTOC method. The traffic flow regulation uses information on exogenous traffic demand, estimated exit lane capacity, and queue status generated from virtual platooning control, to iteratively optimize the number of vehicles permitted to proceed at each time step. Numerical experiments illustrate the effectiveness of the proposed intersection control framework in terms of maintaining safety and string stability, and improving traffic flow efficiency (i.e., alleviating queue lengths and travel delays).

The proposed intersection control framework provides opportunities for further improvements. Future research directions include: (i) incorporating graph search algorithms to organize optimal platoon size and passing sequence more efficiently (e.g., formulating a minimum clique problem (Chen et al., 2021a)); (ii) factoring imperfect communication issues (e.g., latency, faulty messages) in virtual platooning control design; and (iii) designing a cooperative control framework for a mixed-flow traffic environment involving connected vehicles, human-driven vehicles and CAVs (e.g., "1+n" mixed platoon control strategy for platoon controllability and traffic efficiency (Chen et al., 2021b)); and (iv) extending the proposed control framework to a multi-intersection scenario to balance optimality and computational efficiency (e.g., small-scale sub-problem decomposition method (Pei et al., 2021)).

## CRediT authorship contribution statement

Anye Zhou: Formal analysis; Investigation; Methodology; Software; Validation; Visualization; Roles/Writing - original draft; Roles/Writing - review \& editing. Srinivas Peeta: Conceptualization; Funding acquisition; Methodology; Supervision; Roles/Writing - review \& editing. Menglin Yang: Conceptualization; Roles/Writing - review \& editing. Jian Wang: Roles/Writing - review \& editing.

## Acknowledgements

This work is supported by Georgia Institute of Technology through funds provided to the corresponding author. Additional support is provided to the fourth author from the Natural Science Foundation of China (52002191), Natural Science Foundation of Zhejiang province (LQ20E080004), Natural Science Foundation of Ningbo, China (202003N4143). Any errors or omissions remain the sole responsibility of the authors.

## Appendix A. OD matrix, vehicle movement conflict sets and collision spacings

The OD matrix in section 5.1 is given by:

$$
\mathcal{D}=\left(\begin{array}{llllllll}
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 0 & 0 & 0 & 0 & 0
\end{array}\right)
$$

The vehicle movement conflict sets are illustrated in Table A, and collision spacings are shown in Table B.

Table A. Movement conflict sets
| $\mathcal{S}_{1}$ | 5 | 6 | 10 | 11 | 13 | 14 | 15 | 1 |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\mathcal{S}_{2}$ | 5 | 6 | 7 | 9 | 13 | 14 | 15 | 2 |  |
| $\mathcal{S}_{3}$ | 4 | 5 | 6 | 7 | 8 | 9 | 14 | 15 | 3 |
| $\mathcal{S}_{4}$ | 3 | 15 | 4 |  |  |  |  |  |  |
| $\mathcal{S}_{5}$ | 1 | 2 | 3 | 9 | 10 | 14 | 15 | 5 |  |
| $\mathcal{S}_{6}$ | 1 | 2 | 3 | 9 | 10 | 11 | 13 | 6 |  |
| $\mathcal{S}_{7}$ | 2 | 3 | 8 | 9 | 10 | 11 | 12 | 13 | 7 |
| $\mathcal{S}_{8}$ | 7 | 3 | 8 |  |  |  |  |  |  |
| $\mathcal{S}_{9}$ | 2 | 3 | 5 | 6 | 7 | 13 | 14 | 9 |  |
| $\mathcal{S}_{10}$ | 1 | 5 | 6 | 7 | 13 | 14 | 15 | 10 |  |
| $\mathcal{S}_{11}$ | 1 | 6 | 7 | 12 | 13 | 14 | 15 | 16 | 11 |
| $\mathcal{S}_{12}$ | 11 | 7 | 12 |  |  |  |  |  |  |
| $\mathcal{S}_{13}$ | 1 | 2 | 6 | 7 | 9 | 10 | 11 | 13 |  |
| $\mathcal{S}_{14}$ | 1 | 2 | 3 | 5 | 9 | 10 | 11 | 14 |  |
| $\mathcal{S}_{15}$ | 1 | 2 | 3 | 4 | 5 | 10 | 11 | 16 | 15 |
| $\mathcal{S}_{16}$ | 15 | 11 | 16 |  |  |  |  |  |  |


Table B. Collision spacing $d_{i j}^{c}$ of vehicle pairs $(i, j)$
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0 | N | N | N | 0 | $w_{l}$ | N | N | N | $3 w_{l}$ | $4 w_{l}$ | N | 0 | $-w_{l}$ | $-2 w_{l}$ | N |
| 2 | N | 0 | N | N | $w_{l}$ | $2 w_{l}$ | $3 w_{l}$ | N | $-3 w_{l}$ | N | N | N | $-w_{l}$ | $-2 w_{l}$ | $-3 w_{l}$ | N |
| 3 | N | N | 0 | 0 | $2 w_{l}$ | $3 w_{l}$ | $4 w_{l}$ | $4 w_{l}$ | $-4 w_{l}$ | N | N | N | N | $-3 w_{l}$ | $-4 w_{l}$ | N |
| 4 | N | N | 0 | 0 | N | N | N | N | N | N | N | N | N | N | $-4 w_{l}$ | N |
| 5 | 0 | $-w_{l}$ | $-2 w_{l}$ | N | 0 | N | N | N | 0 | $w_{l}$ | N | N | N | $3 w_{l}$ | $4 w_{l}$ | N |
| 6 | $-w_{l}$ | - | $-3 w_{l}$ | N | N | 0 | N | N | $w_{l}$ | $2 w_{l}$ | $3 w_{l}$ | N | $-3 w_{l}$ | N | N | N |
| 7 | N | - | $-4 w_{l}$ | N | N | N | 0 | 0 | $2 w_{l}$ | $3 w_{l}$ | $4 w_{l}$ | $4 w_{l}$ | $-4 w_{l}$ | N | N | N |
| 8 | N | N | $-4 w_{l}$ | N | N | N | 0 | 0 | N | N | N | N | N | N | N | N |
| 9 | N | $3 w_{l}$ | $4 w_{l}$ | N | 0 | $-w_{l}$ | $-2 w_{l}$ | N | 0 | N | N | N | 0 | $w_{l}$ | N | N |
| 10 | $-3 w_{l}$ | N | N | N | $-w_{l}$ | $-2 w_{l}$ | $-3 w_{l}$ | N | N | 0 | N | N | $w_{l}$ | $2 w_{l}$ | $3 w_{l}$ | N |
| 11 | $-4 w_{l}$ | N | N | N | N | $-3 w_{l}$ | $-4 w_{l}$ | N | N | N | 0 | 0 | $2 w_{l}$ | $3 w_{l}$ | $4 w_{l}$ | $4 w_{l}$ |
| 12 | N | N | N | N | N | N | $-4 w_{l}$ | N | N | N | 0 | 0 | N | N | N | N |
| 13 | 0 | $w_{l}$ | N | N | N | $3 w_{l}$ | $4 w_{l}$ | N | 0 | $-w_{l}$ | $-2 w_{l}$ | N | 0 | N | N | N |
| 14 | $w_{l}$ | $2 w_{l}$ | $3 w_{l}$ | N | $-3 w_{l}$ | N | N | N | $-w_{l}$ | - | $-3 w_{l}$ | N | N | 0 | N | N |
| 15 | $2 w_{l}$ | $3 w_{l}$ | $4 w_{l}$ | $4 w_{l}$ | $-4 w_{l}$ | N | N | N | N | - | $-4 w_{l}$ | N | N | N | 0 | 0 |
| 16 | N | N | N | N | N | N | N | N | N | N | $-4 w_{l}$ | N | N | N | 0 | 0 |


[^0]
## Appendix B. Proof of Theorem 1

Proof: We first consider the following Lyapunov function extended from Equations (13) and (16):

$$
V^{*}=V_{1}+\frac{1}{2} Z^{\dagger} Z=\frac{1}{2}\left(S^{\dagger} M S+\tilde{\theta}^{\dagger} \mathcal{T}^{-1} \tilde{\theta}\right)+\frac{1}{2} Z^{\dagger} Z
$$

where $M \in \mathbb{R}^{n \times n}$ is a diagonal matrix expressed as: $M=\operatorname{diag}\left\{M_{1}, M_{2}, \ldots, M_{n}\right\}$. Correspondingly, the $i$ th entry of $\frac{1}{2}\left(S^{\dagger} M S+\tilde{\theta}^{\dagger} \mathcal{T}^{-1} \tilde{\theta}\right)$ and $\frac{1}{2} Z^{\dagger} Z$ will be $V_{i}$ and $\frac{1}{2} z_{i}^{2}$ in Equation (16), respectively. $V^{*}$ is positivedefinite except at the origin where $S=0, \tilde{\theta}=0$, and $Z=0$. It is also radially unbounded with respect to $S, \tilde{\theta}$, and $Z$. Then, taking the time derivative of $V^{*}$ in the form of:

$$
\dot{V}^{*}=S^{\dagger} M \dot{S}+\tilde{\theta}^{\dagger} \mathcal{T}^{-1} \dot{\tilde{\theta}}-k_{3} Z^{\dagger} Z=S^{\dagger} M \dot{S}+\tilde{\theta}^{\dagger} \zeta+\left(\tilde{\theta}^{\dagger} \mathcal{T}^{-1} \operatorname{Proj}_{\widehat{\theta}}(\mathcal{T} \zeta)-\tilde{\theta}^{\dagger} \zeta\right)-k_{3} Z^{\dagger} Z
$$

$\dot{V}^{*}$ can then be separated into the summation of two components $\dot{V}=\dot{\bar{V}}_{1}+\dot{\bar{V}}_{2}$ :

$$
\dot{\bar{V}}_{1}=S^{\dagger} M \dot{S}+\tilde{\theta}^{\dagger} \zeta=\sum_{i=1}^{n} \dot{\bar{V}}_{1, i}
$$

and

$$
\dot{\bar{V}}_{2}=\left(\tilde{\theta}^{\dagger} \mathcal{T}^{-1} \operatorname{Proj}_{\widehat{\theta}}(\mathcal{T} \zeta)-\tilde{\theta}^{\dagger} \zeta\right)-k_{3} Z^{\dagger} Z
$$

Applying the second property (P2) from Equation (37), with $k_{3}>0$, we obtain:

$$
\dot{\bar{V}}_{2}=\left(\tilde{\theta}^{\dagger} \mathcal{T}^{-1} \operatorname{Proj}_{\widehat{\theta}}(\mathcal{T} \zeta)-\tilde{\theta}^{\dagger} \zeta\right)-k_{3} Z^{\dagger} Z \leq 0
$$

For vehicle $i, i \in\{1, \ldots, n\}$, to analyze $\dot{\bar{V}}_{1, i}$, we expand it into:

$$
\dot{\bar{V}}_{1, i}=M_{i} S_{i} \dot{S}_{i}+\tilde{c}_{i} \dot{\tilde{c}}_{i}+\tilde{f}_{i} \dot{\tilde{f}}_{i}+\widetilde{D}_{i} \dot{\widetilde{D}}_{i}+\widetilde{M}_{i} \dot{\widetilde{M}}_{i}
$$

Substituting in the intermediate control decision $\alpha_{i}$ from Equation (27) to $\dot{S}_{i}$ in (A6), we obtain:

$$
\begin{gathered}
\dot{\bar{V}}_{1, i}=M_{i} S_{i}\left[\frac{\left(w_{i, 2}-w_{i, 1}\right) \tilde{c}_{i} v_{i}^{2}}{M_{i}}+\frac{\left(w_{i, 2}-w_{i, 1}\right) \tilde{f}_{i}}{M_{i}}-\frac{\left(w_{i, 2}-w_{i, 1}\right)\left(\Delta_{i}+\widehat{D}_{i} \operatorname{sgn}\left(S_{i}\right)\right)}{M_{i}}+\frac{\widetilde{M}_{i}}{M_{i}} A_{i}-\frac{k_{2}}{M_{i}} S_{i}-\right. \\
\left.\frac{k_{3}}{M_{i}} \operatorname{sgn}\left(S_{i}\right)\right]+\tilde{c}_{i} \dot{\tilde{c}}_{i}+\tilde{f}_{i} \dot{\tilde{f}}_{i}+\widetilde{D}_{i} \dot{\widetilde{D}}_{i}+\widetilde{M}_{i} \dot{\widetilde{M}}_{i}, \forall i \in\{1, \ldots, n-1\} \\
\dot{\bar{V}}_{1, n}=M_{n} S_{n}\left[-\frac{w_{n, 1} \tilde{c}_{n} v_{n}^{2}}{M_{n}}-\frac{w_{n, 1} \tilde{f}_{n}}{M_{n}}+\frac{w_{n, 1}\left(\Delta_{n}+\widehat{D}_{n} \operatorname{sgn}\left(S_{n}\right)\right)}{M_{n}}+\frac{\widetilde{M}_{n}}{M_{n}} A_{n}-\frac{k_{2}}{M_{n}} S_{n}-\frac{k_{3}}{M_{n}} \operatorname{sgn}\left(S_{n}\right)\right]+ \\
\tilde{c}_{n} \dot{\tilde{c}}_{n}+\tilde{f}_{n} \dot{\tilde{f}}_{n}+\widetilde{D}_{n} \dot{\tilde{D}}_{n}+\widetilde{M}_{n} \dot{\tilde{M}}_{n}, i=n
\end{gathered}
$$

Then, after substituting Equations (30)-(33), and the following dynamics of estimation error: $\dot{\tilde{c}}_{i}=\dot{\hat{c}}_{i}, \dot{\tilde{f}}_{i}=$ $\dot{\hat{f}}_{i}, \dot{\widetilde{D}}_{i}=\dot{\widehat{D}}_{i}, \dot{\widetilde{M}}_{i}=\dot{\widehat{M}}_{i}$ into $\dot{\bar{V}}_{1, i}, \dot{\bar{V}}_{1, i}$ can be transformed into:

$$
\begin{gathered}
\dot{\bar{V}}_{1, i} \leq M_{i} S_{i}\left[\frac{\left(w_{i, 2}-w_{i, 1}\right) \tilde{c}_{i} v_{i}^{2}}{M_{i}}+\frac{\left(w_{i, 2}-w_{i, 1}\right) \tilde{f}_{i}}{M_{i}}-\frac{\left(w_{i, 2}-w_{i, 1}\right)\left(\Delta_{i}+\widehat{D}_{i} \operatorname{sgn}\left(S_{i}\right)\right)}{M_{i}}+\frac{\widetilde{M}_{i}}{M_{i}} A_{i}-\frac{k_{2}}{M_{i}} S_{i}-\right. \\
\left.\frac{k_{3}}{M_{i}} \operatorname{sgn}\left(S_{i}\right)\right]-\left(w_{i, 2}-w_{i, 1}\right) \tilde{c}_{i} v_{i}^{2} S_{i}-\left(w_{i, 2}-w_{i, 1}\right) \tilde{f}_{i} S_{i}+\left(w_{i, 2}-w_{i, 1}\right) \widetilde{D}_{i}\left|S_{i}\right|-\widetilde{M}_{i} A_{i} S_{i}-k_{1} z_{i}^{2} \\
\forall i \in\{1, \ldots, n-1\} . \\
\dot{\bar{V}}_{1, n} \leq M_{n} S_{n}\left[-\frac{w_{n, 1} \tilde{c}_{n} v_{n}^{2}}{M_{n}}-\frac{w_{n, 1} \tilde{f}_{n}}{M_{n}}+\frac{w_{n, 1}\left(\Delta_{n}+\widehat{D}_{n} \operatorname{sgn}\left(S_{n}\right)\right)}{M_{n}}+\frac{\widetilde{M}_{n}}{M_{n}} A_{n}-\frac{k_{2}}{M_{n}} S_{n}-\frac{k_{3}}{M_{n}} \operatorname{sgn}\left(S_{n}\right)\right]+ \\
w_{n, 1} \tilde{C}_{n} v_{n}^{2} S_{n}+w_{n, 1} \tilde{f}_{n} S_{n}-w_{n, 1} \widetilde{D}_{i}\left|S_{n}\right|-\widetilde{M}_{n} A_{n} S_{n}-k_{1} z_{n}^{2}, i=n
\end{gathered}
$$

Through arithmetic simplification of Equations (A9) and (A10), Equation (A6) can be written as:

$$
\dot{\bar{V}}_{1, i} \leq-k_{2} S_{i}^{2}-k_{3}\left|S_{i}\right|-k_{1} z_{i}^{2}, \forall i \in\{1, \ldots, n\}
$$

Thus, we have the following inequality for the time derivative of Lyapunov function in Equation (A1):

$$
\dot{V}^{*} \leq \sum_{i=1}^{n}\left(-k_{2} S_{i}^{2}-k_{3}\left|S_{i}\right|-k_{1} z_{i}^{2}\right)
$$

Note that as the estimation errors $\tilde{\theta}$ of vehicle parameters are not included in inequality (A12), we cannot infer the asymptotical convergence of all errors in the control process. To analyze the stability of the time-
varying dynamics of $S_{i}$ induced by vehicle parameter estimation, we use Barbalat's lemma ${ }^{1}$ (Khalil, 2002) to prove $S_{i} \rightarrow 0$ as $t \rightarrow \infty$ as follows.

Since we have $\dot{V}^{*}(S, \theta, t) \leq \sum_{i=1}^{n}\left(-k_{2} S_{i}^{2}-k_{3}\left|S_{i}\right|-k_{1} z_{i}^{2}\right)$ from Equation (A12), by integrating both sides of the inequality, we obtain:

$$
V^{*}(S, \theta, \mathfrak{T})-V^{*}\left(S, \theta, t_{0}\right) \leq-\int_{t_{0}}^{\mathfrak{T}} \sum_{i=1}^{n}\left(k_{2} S_{i}^{2}+k_{3}\left|S_{i}\right|+k_{1} z_{i}^{2}\right) \mathrm{dt}
$$

Then, as $V^{*}(S, \theta, \mathfrak{T}) \geq 0$, the following inequality is valid:

$$
\int_{t_{0}}^{\mathfrak{T}} \sum_{i=1}^{n}\left(k_{2} S_{i}^{2}+k_{3}\left|S_{i}\right|+k_{1} z_{i}^{2}\right) \mathrm{dt} \leq V^{*}\left(S, \theta, t_{0}\right)<\infty
$$

and we can guarantee that $\lim _{\mathfrak{T} \rightarrow \infty} \int_{t_{0}}^{\mathfrak{T}} \sum_{i=1}^{n}\left(k_{2} S_{i}^{2}+k_{3}\left|S_{i}\right|+k_{1} z_{i}^{2}\right) \mathrm{dt}$ is finite.
Additionally, as $k_{2} S_{i}^{2}+k_{3}\left|S_{i}\right|+k_{1} z_{i}^{2}$ is uniformly continuous with respect to $S_{i}$ and $z_{i}$, we conclude that $k_{2} S_{i}^{2}+k_{3}\left|S_{i}\right|+k_{1} z_{i}^{2} \rightarrow 0$ asymptotically, indicating $S_{i} \rightarrow 0$ and $z_{i} \rightarrow 0$ with time for each vehicle in the virtual platoon. Then, by applying Lemma 3, we can sequentially ensure $s_{i}, e_{i}$, and $\dot{e}_{i}$ will all converge to zero asymptotically for each vehicle in the virtual platoon. This completes the proof of the local stability in Theorem 1. $\square$

## Appendix C. Summary of Variables

Table C. Summary of variables
| Variable | Description | Variable | Description |
| :--- | :--- | :--- | :--- |
| $t_{i}^{b}$ | Buffer zone arrival time | $t_{i}^{c}$ | Cooperative zone arrival time |
| $L_{B}$ | Length of buffer zone | $a_{c}$ | Acceleration from virtual gate to cooperative zone in congestion |
| $\Upsilon_{s}$ | Set of approaching vehicles | $t_{\text {bound }}$ | Arrival time bound for separating virtual platoons |
| $\Upsilon_{s}$ | Set of virtual platoons | $C_{n}$ | Compatible passing set |
| $C$ | Collection of compatible passing sets | $N_{c}$ | Number of compatible passing sets |
| $d_{i, j}$ | Spacing between vehicles $i$ and $j$ | $d_{i j}^{c}$ | Collision spacing between vehicles $i$ and $j$ |
| $w_{l}$ | Lane width | $\epsilon$ | Safety cushion |
| $D_{n}$ | Safe spacing between compatible passing sets $n$ and $n+1$ | $x_{i}$ | Position of vehicle $i$ |
| $v_{i}$ | Speed of vehicle $i$ | $a_{i}$ | Acceleration of vehicle $i$ |
| $t$ | Time index for continuous timedependent variables | $\mathfrak{C}_{m, n}$ | Geometric center of conflict point |
| $c_{i}$ | Air drag coefficient of vehicle $i$ | $F_{i}$ | Actual vehicle driving force of vehicle $i$ |
| $f_{i}$ | Rolling resistance of vehicle $i$ | $M_{i}$ | Mass of vehicle $i$ |
| $\delta_{i}$ | Unparameterized disturbance of vehicle $i$ | $\tau_{i}$ | Inertial delay factor of vehicle $i$ |
| $u_{i}$ | Control decision of vehicle $i$ | $\alpha_{i}$ | Intermediate control decision of vehicle $i$ |
| $z_{i}$ | Error variable of vehicle $i$ | $k_{1}$ | Backstepping control gain |
| $e_{i}$ | Spacing error of vehicle $i$ | $\dot{e}_{i}$ | Speed tracking error of vehicle $i$ |
| $s_{i}$ | Sliding surface of vehicle $i$ | $S_{i}$ | Cooperative sliding surface of vehicle $i$ |
| W | Weighted Laplacian matrix | $\lambda$ | Coefficient in sliding surface |
| $k_{2}$ | Control gain of cooperative sliding surface | $k_{3}$ | Robust control gain |


[^1]| $k_{c}^{i}$ | Weighting of air drag coefficient in the parameter adaptation law of vehicle $i$ | $k_{f}^{i}$ | Weighting of rolling resistance in the parameter adaptation law of vehicle $i$ |
| :--- | :--- | :--- | :--- |
| $k_{D}^{i}$ | Weighting of disturbance magnitude in the parameter adaptation law of vehicle $i$ | $k_{M}^{i}$ | Weighting of vehicle mass in the parameter adaptation law of vehicle $i$ |
| $\mathcal{T}$ | Diagonal matrix of weightings | $\zeta_{i}$ | Parameter adaptation law of vehicle $i$ |
| $\theta$ | Vector of vehicle parameters in a virtual platoon | $\widehat{\theta}$ | Vector of estimated vehicle parameters in a virtual platoon |
| $\tilde{\theta}$ | Vector of estimation error of vehicle parameters in a virtual platoon | $\theta_{i, \text { min }}$ | Lower bound of estimated vehicle parameters of vehicle $i$ |
| $\theta_{i, \text { max }}$ | Upper bound of estimated vehicle parameters of vehicle $i$ | $\mathfrak{W}_{i-1, i}$ | Spacing error propagation transfer function between vehicle $i$ and $i-1$ |
| $E$ | Set of exit lanes | $I$ | Set of entrance lanes |
| $\mathcal{D}$ | OD matrix | $\omega$ | Vector of queue lengths |
| $q$ | Vector of input flows | $d$ | Vector of exogenous traffic demand |
| $\mu$ | Vector of input flow ratios | $q^{e}$ | Vector of traffic flow on exit lanes |
| $\mathcal{L}$ | Flow distribution matrix | $Q$ | Vector of estimated exit lane capacities |
| $T$ | Length of CFTOC operational time horizon | dt | Length of a time step |
| $\iota$ | Total time step within an operational time horizon | t | Discrete time index in CFTOC |
| $v_{e q}$ | Intersection operating speed | $\omega_{\text {max }}$ | Maximum queue length |
| $\omega_{\text {min }}$ | Minimum queue length | $\omega_{-1}$ | Queue length at the end of the previous operational time horizon |
| $b_{\omega, i}$ | Scaling coefficient of traffic spillback in direction $i$ | $b_{q, i}$ | Scaling coefficient of throughput in direction $i$ |
| $b_{f, i}$ | Scaling coefficient of traffic flow fluctuations in direction $i$ | $s$ | Laplace operator |

## Appendix D. Complimentary Results of Section 6.2

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-46.jpg?height=894&width=1638&top_left_y=1534&top_left_x=240)
Fig. A. Queue status for each direction under symmetric traffic demand. Corresponds to Fig. 15

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-47.jpg?height=894&width=1636&top_left_y=244&top_left_x=242)
Fig. B. Queue status for each direction under asymmetric traffic demand. Corresponds to Fig. 16

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-47.jpg?height=900&width=1643&top_left_y=1231&top_left_x=244)

![](https://cdn.mathpix.com/cropped/822078d7-36d9-4852-ae99-7df4c64749c6-48.jpg?height=1790&width=1647&top_left_y=242&top_left_x=244)
Fig. C. Queue status for each direction under heterogeneous (time-varying) traffic demand: (a) pattern 1; (b) pattern 2; (c) pattern 3. Corresponds to Fig. 17

## References

Boyd, S., Sastry, S.S., 1986. Necessary and sufficient conditions for parameter convergence in adaptive control. Automatica. 22 (6), 629-639.
Cai, C., Wong, C.K., Heydecker, B.G., 2009. Adaptive traffic signal control using approximate dynamic programming. Transp. Res. Part C Emerg. Technol. 17 (5), 456-474.
Campos, G.R., Falcone, P., Wymeersch, H., Hult, R., Sjoberg, J., 2014. Cooperative receding horizon conflict
resolution at traffic intersections. Proceedings of the IEEE Conference on Decision and Control. 2932-2937.
Cao, Y., Yu, W., Ren, W., Chen, G., 2013. An overview of recent progress in the study of distributed multi-agent coordination. IEEE Trans. Ind. Informatics. 9, 427-438.
Ceylan, H., Bell, M.G.H., 2004. Reserve capacity for a road network under optimized fixed time traffic signal control. J. Intell. Transp. Syst. Technol. Planning, Oper. 87-99.
Chen, C., Xu, Q., Cai, M., Wang, J., Wang, J., Xu, B., Li, K., 2021a. Conflict-free cooperation method for connected and automated vehicles at unsignalized intersections: graph-based modeling and optimality analysis. arXiv preprint arXiv:2107.07179.
Chen, C., Wang, J., Xu, Q., Wang, J., Li, K., 2021b. Mixed platoon control of automated and human-driven vehicles at a signalized intersection: dynamical analysis and optimal control. Transp. Res. Part C Emerg. Technol. 127, 103138. Dresner, K., Stone, P., 2008. A multiagent approach to autonomous intersection management. J. Artif. Intell. Res. 31, 591-656.
Fax, J.A., Murray, R.M., 2004. Information flow and cooperative control of vehicle formations. IEEE Trans. Automat. Contr. 49 (9), 1465-1476.
Feng, S., Zhang, Y., Li, S.E., Cao, Z., Liu, H.X., Li, L., 2019. String stability for vehicular platoon control: Definitions and analysis methods. Annu. Rev. Control. 47, 81-97.
Feng, Y., Head, K.L., Khoshmagham, S., Zamanipour, M., 2015. A real-time adaptive signal control in a connected vehicle environment. Transp. Res. Part C Emerg. Technol. 55, 460-473.
Genders, W., Razavi, S., 2019. Asynchronous n-step Q-learning adaptive traffic signal control. Journal of Intelligent Transportation Systems: Technology, Planning, and Operations. 23 (4), 319-331.
Gong, S., Shen, J., Du, L., 2016. Constrained optimization and distributed computation based car following control of a connected and autonomous vehicle platoon. Transp. Res. Part B Methodol. 96, 314-334.
Gong, S., Zhou, A., Peeta, S., 2019. Cooperative adaptive Cruise Control for a Platoon of Connected and Autonomous Vehicles considering Dynamic Information Flow Topology. Transp. Res. Rec. 2673 (10), 185-198.
Horowitz, R., Varaiya, P., 2000. Control design of an automated highway system. Proc. IEEE. 88 (7), 913-925.
Johan Åström, K., Murray, R.M., 2010. Feedback systems: an introduction for scientists and engineers. Princeton University Press.
Khalil, H.K., 2002. Nonlinear Systems. Upper Saddle River, NJ: Prentice Hall.
Kim, Y-H., Peeta, S., He, X., 2017. Modeling the information flow propagation wave under vehicle-to-vehicle communications. Transp. Res. Part C Emerg. Technol. 85, 377-395.
Kotsialos, A., Papageorgiou, M., 2004. Nonlinear optimal control applied to coordinated ramp metering. IEEE Trans. Control Syst. Technol. 12 (6), 920-933.
Kotsialos, A., Papageorgiou, M., Middelham, F., 2001. Optimal coordinated ramp metering with advanced motorway optimal control. Transportation Research Record. 1748 (1), 55-65.
Kwon, J.W., Chwa, D., 2014. Adaptive bidirectional platoon control using a coupled sliding mode control method. IEEE Trans. Intell. Transp. Syst. 15 (5), 2040-2048.
Lee, J., Park, B., 2012. Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment. IEEE Trans. Intell. Transp. Syst. 13 (1), 81-90.
Levin, M.W., Rey, D., 2017. Conflict-point formulation of intersection control for autonomous vehicles. Transp. Res. Part C Emerg. Technol. 85, 528-547.
Lewis, F., Vrabie, D., Syrmos, V.L., 2012. Optimal control. John Wiley \& Sons.
Li, S. E., Zheng, Y., Li, K., Wang, J., 2015. An overview of vehicular platoon control under the four-component framework. 2015 IEEE Intelligent Vehicles Symposium (IV), Seoul, South Korea, pp. 286-291.
Lin, C.T., 1974. Structural controllability. IEEE Trans. Automat. Contr. 19 (3), 201-208.
Liu, Y.Y., Barabási, A.L., 2016. Control principles of complex systems. Rev. Mod. Phys. 88 (3) 035006.
Löfberg, J., 2004. YALMIP: A toolbox for modeling and optimization in MATLAB. Proceedings of IEEE International Conference on Robotics and Automation. 284-289.
Lopez, P.A., Behrisch, M., Bieker-Walz, L., Erdmann, J., Flötteröd, Y.P., Hilbrich, R., Lücken, L., Rummel, J.,

Wagner, P. and Wießner, E., 2018. Microscopic traffic simulation using sumo. In 2018 21st International Conference on Intelligent Transportation Systems (ITSC). 2575-2582.
Masi, S., Xu, P., Bonnifait, P., 2018. Adapting the Virtual Platooning Concept to Roundabout Crossing. Proceedings of IEEE Intelligent Vehicles Symposium. 1366-1372.
McAuliffe, B., Lammert, M., Lu, X.Y., Shladover, S., Surcel, M.D., Kailas, A., 2018. Influences on energy savings of heavy trucks using cooperative adaptive cruise control. SAE Technical Papers. No. 2018-01-1181.
Medina, A.I.M., Wouw, N. Van De, Nijmeijer, H., 2015. Automation of a T-intersection using virtual platoons of cooperative autonomous vehicles. In: IEEE Conference on Intelligent Transportation Systems, Proceedings, ITSC. 1696-1701.
Medina, A.I.M., Van De Wouw, N., Nijmeijer, H., 2018. Cooperative intersection control based on virtual platooning. IEEE Trans. Intell. Transp. Syst. 19 (6), 1727-1740.
Mirheli, A., Hajibabai, L., Hajbabaie, A., 2018. Development of a signal-head-free control logic in a fully connected and autonomous vehicle environment. Transp. Res. Part C Emerg. Technol. 92, 412-425.
Mirheli, A., Tajalli, M., Hajibabai, L., Hajbabaie, A., 2019. A consensus-based distributed trajectory control in a signal-free intersection. Transp. Res. Part C Emerg. Technol. 100, 161-176.
Mohebifard, R., Hajbabaie, A., 2018. Dynamic traffic metering in urban street networks: formulation and solution algorithm. Transp. Res. Part C Emerg. Technol. 93, 161-178.
Naus, G.J.L., Vugts, R.P.A., Ploeg, J., van De Molengraft, M.J.G., Steinbuch, M., 2010. String-stable CACC design and experimental validation: a frequency-domain approach. IEEE Trans. Veh. Technol. 59 (9), 4268-4279.
Parks, P., 1966. Liapunov redesign of model reference adaptive control systems. IEEE Transactions on Automatic Control. 11(3), 362-367.
Paszke, A., Gross, S., Massa, F., Lerer, A., Bradbury, J., Chanan, G., Killeen, T., Lin, Z., Gimelshein, N., Antiga, L., Desmaison, A., 2019. Pytorch: an imperative style, high-performance deep learning library. Advances in Neural Information Processing Systems. 32, 8026-8037.
Pei, H., Zhang, Y., Tao, Q., Feng, S., Li, L., 2021. Distributed cooperative driving in multi-intersection road networks. IEEE Transactions on Vehicular Technology.
Ploeg, J., Shukla, D.P., Van De Wouw, N., Nijmeijer, H., 2014. Controller synthesis for string stability of vehicle platoons. IEEE Trans. Intell. Transp. Syst. 15(2), 854-865.
Potra, F. A., Wright, S. J., 2000. Interior-point methods. Journal of Computational and Applied Mathematics. 124(1-2), 281-302.
Robertson, D.I., Bretherton, R.D., 1991. Optimizing networks of traffic signals in real time-the SCOOT method. IEEE Trans. Veh. Technol. 40 (1), 11-15.
Shampine, L. F. and Reichelt, M. W., 1997. The MATLAB ODE suite. SIAM Journal on Scientific Computing, Vol. 18, 1-22.
Talebpour, A., Mahmassani, H.S., 2016. Influence of connected and autonomous vehicles on traffic flow stability and throughput. Transp. Res. Part C Emerg. Technol. 71, 143-163.
Treiber, M., Hennecke, A. and Helbing, D., 2000. Congested traffic states in empirical observations and microscopic simulations. Physical Review E. 62 (2), 1805.
Vanderbei, R.J., Shanno, D.F., 1999. An interior-point algorithm for nonconvex nonlinear programming. Computational Optimization and Applications. 13(1), 231-252.
Wang, C., Gong, S., Zhou, A., Li, T., Peeta, S., 2020. Cooperative adaptive cruise control for connected autonomous vehicles by factoring communication-related constraints. Transp. Res. Part C Emerg. Technol. 113, 124-145.
Wang, J., Kim, Y-H., He, X., Peeta, S., 2018. Analytical model for information flow propagation wave under an information relay control strategy in a congested vehicle-to-vehicle communication environment. Transp. Res. Part C Emerg. Technol. 94, 1-18.
Wu, Y., Li, S.E., Cortes, J., Poolla, K., 2019. Distributed sliding mode control for nonlinear heterogeneous platoon systems with positive definite topologies. IEEE Trans. Control Syst. Technol. 28 (4), 1272-1283.
Wu, Y., Li, S.E., Zheng, Y., Hedrick, J.K., 2016. Distributed sliding mode control for multi-vehicle systems with positive definite topologies, in: 2016 IEEE 55th Conference on Decision and Control, CDC. 5213-5219.

Xu, B., Li, S.E., Bian, Y., Li, S., Ban, X.J., Wang, J., Li, K., 2018. Distributed conflict-free cooperation for multiple connected vehicles at unsignalized intersections. Transp. Res. Part C Emerg. Technol. 93, 322-334.
Xu, H., Zhang, Y., Li, L., Li, W., 2019. Cooperative driving at unsignalized intersections using tree search. IEEE Trans. Intell. Transp. Syst. 21(11), 4563-4571.
Xu, L., Yao, B., 2001. Adaptive robust precision motion control of linear motors with negligible electrical dynamics: theory and experiments. IEEE/ASME Trans. Mechatronics. 6 (4), 444-452.
Xu, L., Zhuang, W., Yin, G., Bian, C., 2018. Stable longitudinal control of heterogeneous vehicular platoon with disturbances and information delays. IEEE Access. 6, 69794-69806.
Yao, B., Tomizuka, M., 1997. Adaptive robust control of siso nonlinear systems in a semi-strict feedback form. Automatica. 33 (5), 893-900.
Young, K. D., Utkin, V. I., Ozguner, U., 1999. A control engineer's guide to sliding mode control. IEEE Transactions on Control Systems Technology. 7(3), 328-342.
Zheng, Y., Li, S.E., Li, K., Wang, L.Y., 2016. Stability margin improvement of vehicular platoon considering undirected topology and asymmetric control. IEEE Trans. Control Syst. Technol. 24 (4), 1253-1265.
Zhou, A., Gong, S., Wang, C., Peeta, S. 2020. Smooth-Switching Control-Based Cooperative Adaptive Cruise Control by Considering Dynamic Information Flow Topology. Transportation Research Record. 2674(4), 444-458.
Zhou, Y., Ahn, S., Chitturi, M., Noyce, D.A., 2017. Rolling horizon stochastic optimal control strategy for ACC and CACC under uncertainty. Transp. Res. Part C Emerg. Technol. 83, 61-76.
Zhou, Y., Ahn, S., 2019. Robust local and string stability for a decentralized car following control strategy for connected automated vehicles. Transp. Res. Part B Methodol. 125, 175-196.
Zhou, Y., Wang, M., Ahn, S., 2019. Distributed model predictive control approach for cooperative car-following with guaranteed local and string stability. Transp. Res. Part B Methodol. 128, 69-86.


[^0]:    * N indicates that two vehicles do not have conflicts, and $w_{l}$ is the length of the grid

[^1]:    ${ }^{1}$ If $\lim _{t \rightarrow \infty} \int_{t_{0}}^{t} \phi(\tau) d \tau$ exits and is finite, and $\phi(\tau)$ is uniformly continuous, then $\phi(t) \rightarrow 0$ as $t \rightarrow \infty$.

