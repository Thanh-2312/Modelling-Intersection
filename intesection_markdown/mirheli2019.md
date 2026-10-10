Amir Mirheli ${ }^{\mathrm{a}}$, Mehrdad Tajalli ${ }^{\mathrm{b}}$, Leila Hajibabai ${ }^{\mathrm{a}, *}$, Ali Hajbabaie ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}}$ Department of Civil Engineering, State University of New York at Stony Brook, Stony Brook, NY 11794, USA<br>${ }^{\mathrm{b}}$ Department of Civil and Environmental Engineering, Washington State University, 405 Spokane St., Pullman, WA 99164, USA

A R T I C L E I N F O

Keywords:
Distributed algorithm
Coordination
Signal-free
Cooperative
Control logic
Connected and autonomous vehicles


#### Abstract

This paper develops a distributed cooperative control logic to determine conflict-free trajectories for connected and automated vehicles (CAVs) in signal-free intersections. The cooperative trajectory planning problem is formulated as vehicle-level mixed-integer non-linear programs (MINLPs) that aim to minimize travel time of each vehicle and their speed variations, while avoiding near-crash conditions. To push vehicle-level solutions towards global optimality, we develop a coordination scheme between CAVs on conflicting movements. The coordination scheme shares vehicle states (i.e., location) over a prediction horizon and incorporates such information in CAVs' respective MINLPs. Therefore, the CAVs will reach consensus through an iterative process and select conflict-free trajectories that minimize their travel time. The numerical experiments quantify the effects of the proposed methodology on traffic safety and performance measures in an intersection. The results show that the proposed distributed coordinated framework converges to near-optimal CAV trajectories with no conflicts in the intersection neighborhood. While the solutions are found in real-time, the comparison to a central intersection control logic for CAVs indicates a maximum marginal objective value of 2.30\%. Furthermore, the maximum marginal travel time, throughput, and average speed do not exceed $0.5 \%$, $0.1 \%$, and $0.5 \%$, respectively. The proposed control logic reduced travel time by 43.0-70.5\%, and increased throughput and average speed respectively by 0.8-115.6\% and $59.1-400.0 \%$ compared to an optimized actuated signal control, while eliminating all near-crash conditions.


## 1. Introduction

The Federal Highway Administration predicts that approximately 60\% of the total travel delay occurs on urban street networks, where bottlenecking caused by intersections is a major contributing factor. Literature has shown the effectiveness of signal timing optimization using connected vehicle technology through exchange of real-time location and speed information with signal controllers. Such information helps estimate connected and un-connected vehicles' arrival time, travel time, as well as the queue length at intersections (Beak et al., 2017; Feng et al., 2015; Ilgin Guler et al., 2014; Lee et al., 2013b; Priemer and Friedrich, 2009). Besides, CAVs have provided great opportunities to improve traffic operation (Perraki et al., 2018; Talebpour and Mahmassani, 2016; Ghiasi et al., 2017; Xiao et al., 2018), energy efficiency (Jiang et al., 2017; Vahidi and Sciarretta, 2018; Zhao et al., 2018), and traffic safety (Shabanpour et al., 2018; Van Brummelen et al., 2018) in transportation networks. Existing studies have also presented total delay

[^0]reductions using the CAV technology (e.g., see Lee et al. (2013) for a comparison to actuated control; He et al. (2012) for a multimodal traffic control in an arterial; or Goodall et al. (2013) for signal timing optimization in an arterial). Besides, Feng et al. (2018), Guo et al. (2019), Pourmehrab et al. (2018), and Yang et al. (2016) have shown the capability of intersection controllers to assign optimal trajectories to automated vehicles to enter and pass the intersections with lower number of stops and delay. In addition, Sun et al. (2018) have shown that CAVs' lateral control through optimal lane assignment helps improve traffic operations. Existing traffic control methods aim to reduce the number of crashes by preventing any vehicles with conflicting movements from simultaneously proceeding through an intersection. In other words, current strategies grant the right-of-way to one set of non-conflicting movements at a time, forcing all movements in conflict with the active movements to stop. As such, these systems are prone to high levels of bottlenecking, which increases the unwelcome consequences of travel delay.

An autonomous intersection management (AIM) offers the potential to significantly improve traffic operations at intersections while maintaining the maximum safety level, assuming that the technology is ready and fully tested. Literature presents a group of studies on the impact of AIM on the performance of signal-free intersection management. For example, a study by Dresner and Stone (2004) has developed a multi-agent reservation-based intersection control mechanism for traffic streams of fully autonomous vehicles. Their approach does not consider turning movements and assumes fixed vehicle speeds inside an intersection to simplify the problem. In a follow-up study, Dresner and Stone (2008) has included a first-come-first-serve algorithm in the method, where the intersection controller grants or rejects vehicle requests to proceed through the intersection at the moment they are received. As such, the decisions are made regardless of the requests that would be received in an immediate future, while including the potential future requests leads to more efficient operations and safety. In a related study, Shahidi (2010) has developed a delayed response policy to address this limitation and batched the received requests to make a more informed selection. Similar to prior related studies, this research is expert opinion-based and does not find optimal trajectories in intersections. Vasirani and Ossowski (2012) have extended the reservation-based intersection control proposed by Dresner and Stone (2004) through a market-inspired mechanism. They have modeled the supply-demand relationship at intersections that allows movements based on the volume-to-capacity ratio of the approach. A pricing policy is incorporated into the reservation-based intersection control system to reduce the delay. However, the winner determination algorithm is implemented for the current bids in each round, and the future bids are ignored and hence, the optimality of trajectories cannot be guaranteed over time. Au and Stone (2010) have developed a planning-based autonomous vehicle motion controller that interacts with AIM. In this study, the first-come-first-serve (FCFS) algorithm adopted in AIM is improved by better estimation of arrival time and speed of vehicles. However, the improved algorithm cannot guarantee the optimality of trajectories. Hausknecht et al. (2011) have expanded the AIM to a multiple-intersection network. In this study, vehicles send a notification to intersection managers, prior to their reservation requests, in order to update the traversal time of incoming vehicles. The intersection manager, in return, communicates a minimum traversal path with each vehicle using a time-based navigation policy; however, finding that path is not guaranteed. AIM has been solved in various studies following a central approach (e.g., Chouhan and Banda (2018), Fajardo et al. (2011), Levin and Boyles (2015), Ahmane et al. (2013), Carlino et al. (2013), and Belkhouche (2018)). As an extension to AIM, Levin and Rey (2017) have proposed AIM* to assign reservations to CAVs, where the intersection manager obtains the information of all CAVs on each approaching link. This study has formulated the conflict-point separation problem as a mixed-integer linear program to determine optimal conflict-free reservations in an isolated intersection.

Several studies have attempted to utilize exclusion policies and recovery modes in their control methods to address safety concerns. Wu et al. (2012) have proposed a centralized formulation to determine optimal solutions to the autonomous intersection management problem. Due to the large decision space, the study is not capable of solving the problem analytically; therefore, they have utilized an ant colony algorithm, which does not guarantee the optimality of their solutions. To promote safety, they have included a policy to allow vehicles to enter the intersection only after complete clearance of the conflicting movements. While this method achieves its objectives, it pushes the vehicle trajectories away from optimality. Similarly, Lee and Park (2012) have proposed a centralized cooperative intersection control that would minimize the total length of overlapped trajectories. Their proposed formulation is complex; hence, they have used genetic algorithms to solve the problem. Still, the solutions result in collisions since there are no explicit constraints to avoid them. Therefore, they have to include a recovery mode to prevent collisions by stopping vehicles on conflicting movements. The use of genetic algorithms and inclusion of the recovery mode does not allow this approach to find optimal collision-free trajectories. Dai et al. (2016) have extended Lee and Park's algorithm to vehicular cyber physical systems with the objective to enforce smooth movements to improve passengers' travel quality in a centralized formulation. They have linearized collision avoidance constraints and consequently converted the problem into a convex optimization problem. Their problem is still complex and hence, they have also included a recovery mode to find feasible solutions. Thus, their proposed methodology does not guarantee optimal collision-free trajectories.

Other studies have also attempted to use centralized models to develop an intersection control logic for connected vehicles. A study by Zohdy and Rakha (2014) has proposed a centralized cooperative adaptive cruise control model to identify conflicting movements. The controller defines vehicle trajectories using a rolling horizon approach based on data on speed, acceleration, and location of vehicles. Due to computational complexities involved in this approach, the length of the planning horizon has to be limited. Besides, Hassan and Rakha (2014) have developed a heuristic approach to provide communications between autonomous vehicles approaching an unsignalized intersection that prioritizes the approach with higher traffic volume to reduce delay. This approach can be solved in real-time, but it does not yield optimal trajectories. Wuthishuwong et al. (2015) have discretized the time and space at an intersection and used a centralized dynamic program to find each vehicle trajectory at every time step. The computational complexity of this problem grows exponentially when the number of vehicles increases, thus, the approach cannot find near-optimal solutions in real-time. Finally, Muller et al. (2016) have presented a centralized mixed-integer linear program to represent the intersection control, where location and speed of autonomous vehicles in each time step is gathered to provide the
shortest and longest travel times to reach an intersection. Then, the aggregated arrival time for all vehicles is minimized utilizing the travel times calculated in each time step. Then, the speed profiles are assigned to vehicles to approach the intersection. Average speeds are determined based on the feasible set of speed profiles. This method is also computationally complex and only addresses through movements.

The existing studies have provided invaluable information on AIM, its benefits, and the underlying logic. Nevertheless, they have limitations. They lack an analytical platform to determine optimal collision-free trajectories for the state space. Current formulations are riddled with complexities (e.g., including mixed-integer decision variables and non-linear terms in the objective functions and constraints) and can only be solved under simplified conditions. Besides, they often suffer from the "curses of dimensionality" resulting from huge state and action spaces (e.g., combinations of locations, speeds, and acceleration decisions over time) that impose significant problem intractability. Given the aforementioned complexities, current approaches have yet to define an analytical base to determine the optimal solutions. Instead, they either use heuristics, meta-heuristics, or expert opinion-based approaches to find vehicle trajectories. In the absence of an analytical platform, the existing approaches cannot find collision-free trajectories for all possible system states because they cannot enumerate all prevailing conditions and propose an efficient solution to each possible state. Instead, they must prevent collisions via a recovery mode. These recovery modes consider only a set of possible states with specific collision remedial actions, which leads to sub-optimal operations. Perhaps the most relevant study to this paper is the development of signal-head-free intersection control logic by Mirheli et al. (2018) that formulates a dynamic program to determine optimal acceleration rates over time through a stochastic look-ahead technique based on Monte Carlo tree search algorithm. Yet, the study utilizes a central intersection-level perspective rather than a cooperative vehicle-level structure as such, does not scale well if problem size grows significantly. The existing algorithms, even the agent-based methods, do not account for individual user behavior and assume that automated vehicles fully comply with system operator decisions. However, automated vehicles tend to optimize their own travel experiences. As such, a system-optimal central perspective does not accurately model the behavior of individual vehicles in an intersection. A distributed formulation can model CAV preferences more accurately and offers great potential to address the computational complexity of the problem.

Distributed optimization algorithms have been used in computer science and other domains (Boyd et al., 2011; Cao et al., 2013; Cortés and Bullo, 2005; Duchi et al., 2012; Fitzpatrick and Meertens, 2003; Gesbert et al., 2007; Inalhan et al., 2002; Kia et al., 2015; Rabbat and Nowak, 2004; Raffard et al., 2004; Wangermann and Stengel, 1999) to tackle the intractability of complex large-scale problems. The application of distributed coordinated methodologies in traffic operations has led to significant improvements in computational efficiency of transportation network problems; see distributed signal timing optimization problem (Islam and Hajbabaie, 2017; Mehrabipour and Hajbabaie, 2017; Timotheou et al., 2015), distributed traffic metering (Mohebifard and Hajbabaie, 2018), distributed speed harmonization (Tajalli and Hajbabaie, submitted for publication), and distributed cooperative highway driving (Liu et al., 2017). In another context, Chen et al. (2018) have used a distributed and coordinated model predictive control to solve the vessel train formation in a multi-vessel trajectory planning problem. The model aims to minimize the distance of vessels based on a set of pre-defined paths and maximize the distance between neighboring vessels. The methodology uses the alternating direction method of multipliers (ADMM) to iteratively design each vessel's trajectory sequentially, based on other vessels' trajectories, under collision avoidance constraints. Hence, the problem can be computationally expensive when the number of vessels increases (i.e., the distributed solutions are not real-time). Keviczky et al. (2008) have used a decentralized coordinated approach to find collision-free trajectories for autonomous air vehicles with no coupling constraints. Similarly, each vehicle's trajectory is optimized, and future trajectories of neighboring vehicles are predicted. This study uses a receding horizon approach to yield real-time solutions. Yet, fixed number of neighboring vehicles is assumed, while increasing the number can impose intractability to the problem. Another relevant study for aerial vehicles can be found in Kuwata and How (2011) with un-coupled constraints between trajectories, but a coupled objective function. Again, the sequential structure of the algorithm avoids finding solutions in real-time.

Other relevant distributed trajectory planning methodologies on the signal-free intersection management follow. Makarem and Gillet (2012) have developed a decentralized navigation function for coordination of autonomous vehicles at intersections considering a safety distance. Each vehicle receives information about the position, speed, and path of neighboring vehicles and minimizes its speed and energy consumption. In this study, heavier vehicles get higher priorities to reduce fuel consumption by avoiding un-necessary stops. The case study provides collision-free trajectories under very low traffic volume (i.e., only four vehicles). Campos et al. (2014) have decentralized the trajectory planning problem for autonomous vehicles, where each vehicle solves a finitetime local control problem under collision-avoidance constraints. A receding horizon approach is used to reduce the complexity of the problem. The proposed algorithm is tested by simulating three vehicles at an intersection. However, the performance of the algorithm has not been investigated for a higher number of vehicles. Zhang et al. (2016) have studied the CAVs' trajectory optimization problem that pass through two adjacent signal-free intersections. A vehicle-level decomposition scheme is applied through relaxing the coupling constraints and adding them to the objective function with Lagrangian multipliers. The proposed algorithm does not ensure feasible solutions due to infeasible initial state of vehicles. Xu et al. (2018) have developed a distributed cooperative method to find collision-free trajectory of multiple connected vehicles at unsignalized intersections. This study has projected different traffic movements into a virtual one-dimensional lane and provided a conflict-free topology (keeping a car-following distance to preceding vehicles) by solving a depth-first spanning tree search to find the order of vehicles entering the intersection. This study still requires a central controller to access the global information of all vehicles in the intersection neighborhood. On the other hand, Malikopoulos et al. (2018) have proposed a decentralized approach to minimize CAVs' energy consumption while maximizing intersection throughput. This study has developed a recursive equation to find the optimal arrival time of each CAV to the intersection, while maintaining the safety distance with neighboring CAVs.

This paper develops a distributed coordinated signal-free intersection control logic (DC-SICL) to prioritize conflicting movements

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-04.jpg?height=703&width=723&top_left_y=189&top_left_x=582)
Fig. 1. Consensus formation on movement priorities for conflicting trajectories.

in intersections when no traffic control devices exist (see Fig. 1).
The underlying concept is that CAVs negotiate with each other to determine collision-free trajectories for themselves that reduce their travel time. Therefore, the cooperative trajectory planning problem is formulated as vehicle-level mixed-integer non-linear programs (MINLPs) that aim to minimize travel time and avoid near-crash conditions for each vehicle. To ensure feasibility of the vehicle-level solutions and push them towards global optimality, we develop a coordination scheme between CAVs with conflicting trajectories. The proposed coordination scheme will share traffic state (i.e., vehicle location) over a prediction period among CAVs, and implement such information in their respective MINLPs. The numerical experiments quantify the effects of the proposed methodology on traffic safety and performance measures in an isolated intersection with two exclusive through and left-turn lanes in each approach.

The exposition of this paper follows. The next section presents the proposed methodology to formulate and solve the vehicle-level signal-free intersection control logic and design collision-free trajectories. The discussion is continued with presenting the numerical results and highlighting the concluding remarks and trends for further research.

## 2. Distributed optimization and coordination methodology

The majority of the existing studies on the signal-free trajectory optimization problem follow a centralized architecture and include large sets of decisions and state spaces that avoid finding optimal solutions in real-time. Hence, decentralized and distributed solution techniques have been proposed to tackle the imposed complexities of the central techniques. Yet, the solution quality and safety of trajectories obtained from such approaches need to be investigated, particularly in large-scale problems. This section presents the DC-SICL methodology. We first formulate a distributed optimization model to represent a collision-free trajectory for each CAV on each lane over time. Then, we develop a coordination scheme to push the distributed trajectory models towards global optimality while ensuring safe trajectories for all CAVs approaching to and passing through each intersection. We then present a benchmark central strategy, based on Mirheli et al. (2018), to further evaluate the performance of the proposed methodology.

### 2.1. Model formulation

This section formulates a distributed vehicle-level program to determine optimal non-conflicting trajectories for a CAV. We let $\Gamma$ denote the number of discrete time steps in the study period to capture the temporal dimension of CAV trajectories, where $t \in T=\{0,1, \cdots, \Gamma-1\}$ indicates the time steps for taking actions, i.e. acceleration/deceleration decisions. Let $I$ define the set of lanes approaching an intersection. We also define subset $I_{l}$ as the set of lanes with turning movements. We let $N^{t}$ be the set of all vehicles at time $t \in T$ and $C_{i}$ denote the set of lanes with conflicting movements with lane $i \in I$. Besides, we define $P_{i j}$ as the set of all vehicles predecessor to vehicle $j \in N^{t}$ on lane $i \in I$ at time $t \in T$. We assume a certain detection range for each CAV (e.g., 650 ft). Fig. 2 depicts a four-leg isolated intersection with two exclusive lanes for (i) left-turns and (ii) through movements on each approach. Note that the detection range of each vehicle $j \in N^{t}$ at time $t$ (shown in colored disks) is significantly down-sized compared to the vehicle and intersection dimensions, due to representation purposes. Let $b_{i}^{h}$ denote the beginning point of lane $i$ on approach $h$ defined as a reference location; hence, $X_{i j}^{t}$ represents the relative location of vehicle $j \in N^{t}$ from $b_{i}^{h}$. We let $\mathscr{V}_{i j}^{t}$ and $a_{i j}^{t}$ respectively represent the speed and acceleration rate of vehicle $j \in N^{t}$ on lane $i \in I$ at time $t \in T$. The state of each vehicle $j$ on lane $i$ at time $t$ is defined by its location at the intersection neighborhood (i.e., $S_{i j}^{t}=\left\{X_{i j}^{t}\right\}, \forall i \in I, j \in N^{t}, t \in T$ ).

CAVs share their current state (specifically, predicted trajectories) with other CAVs through dedicated short-range communication

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-05.jpg?height=657&width=721&top_left_y=187&top_left_x=584)
Fig. 2. An isolated intersection layout including movement notations, conflict regions, and CAV detection range.

at time $t$. While maintaining the safety distance between CAVs, this study aims to minimize the distance of each CAV from its predefined destination $r_{i}^{h}$ (i.e., end of its path at the intersection neighborhood) that is equivalent to minimizing the travel time of each CAV. Note that after passing the pre-defined destination, each CAV enters the neighboring intersection vicinity and solves the trajectory optimization problem in the neighboring intersection.

Using a distributed model structure and capturing vehicles' states on lane $i$ at time $t$, the optimal collision-free CAV-level trajectories will be found by assigning acceleration $a_{i j}^{t}$ (i.e., the decision variable of the model formulation) to vehicle $j$ to approach and cross the signal-free intersection. The proposed CAV-level distributed problem formulation for vehicle $j \in N^{t}$ on lane $i \in I$ follows.

$$
\begin{aligned}
& f_{j}=\min _{a} \sum_{t \in T}\left\{r_{i}^{h}-X_{i j}^{t+1}\right\}+\gamma\left|\mathscr{V}_{i j}^{t+1}-\mathscr{V}_{i j}^{t}\right|, \quad \forall i \in I, j \in N^{t}, \\
& \text { s.t. } \quad X_{i j}^{t+1}=\frac{1}{2} a_{i j}^{t} t^{2}+\mathscr{V}_{i j}^{t} t+X_{i j}^{t}, \quad \forall i \in I, j \in N^{t}, t \in T \\
& \mathscr{V}_{i j}^{t+1}=a_{i j}^{t} t+\mathscr{V}_{i j}^{t}, \quad \forall i \in I, j \in N^{t}, t \in T \\
& \alpha \leq a_{i j}^{t} \leq \alpha^{\prime}, \quad \forall i \in I, j \in N^{t}, t \in T \\
& 0 \leq \mathscr{V}_{i j}^{t+1} \leq \varepsilon, \quad \forall i \in I, j \in N^{t}, t \in T \\
& \mathscr{V}_{i j}^{t+1} \leq\left\{\begin{array}{cc}
\varepsilon^{\prime}, & e_{i}^{h} \leq X_{i j}^{t+1} \leq r_{i}^{h} \\
\varepsilon, & \forall i \in I_{l}, j \in N^{t}, t \in T
\end{array}\right. \\
& \widehat{X}_{i m}^{t+1}-X_{i j}^{t+1} \geq L_{v}+D+R \mathscr{V}_{i j}^{t+1}, \quad \forall i \in I, j \in N^{t}, m \in P_{i j}, t \in T \\
& \left|X_{i j}^{t+1}-F_{i}\right|+\left|\widehat{X}_{l m}^{t+1}-F_{l}\right| \geq L_{v}+D, \quad \forall i \in I, l \in C_{i}, j, m \in N^{t}, t \in T
\end{aligned}
$$

The objective function (1a) aims to minimize the travel time and speed variations of each CAV. The first term in (1a) is a convex linear function that minimizes the distance between vehicle $j$ 's location at time $t$ and a pre-defined destination $r_{i}^{h}$ on lane $i$. This distance minimization is equivalent to travel time minimization for each vehicle. Besides, $\left|\mathscr{V}_{i j}^{t+1}-\mathscr{V}_{i j}^{t}\right|$ in the second term of (1a) is a convex function that defines the speed variation of vehicle $j$ on lane $i$ at time $t$. The speed variation is minimized to reduce the likelihood of disruptive and frequent changes in vehicles speeds over time. Parameter $\gamma$ represents the speed-location conversion factor. Constraints (1b) and (1c) update the location $X_{i j}^{t+1}$ and speed $\mathscr{V}_{i j}^{t+1}$ of each CAV at time $t+1$ based on the acceleration decisions $a_{i j}^{t}$ and CAV's state $S_{i j}^{t}$ at time $t$. Constraints (1d) ensure that vehicles apply functional acceleration rates based on their performance to update their speed considering a certain acceleration threshold (i.e., $\alpha$ and $\alpha^{\prime}$ ). Constraints ( 1 e) define the thresholds of the driving speed with $\varepsilon$ representing the free-flow speed. Constraints (1e) enforce vehicles on turning movements to cross the intersection at a lower speed limit $\varepsilon^{\prime}$, where $e_{i}^{h}$ represents the entering point to the intersection. Constraints (1g) guarantee safe movements for vehicle $j \in N^{t}$ on lane $i \in I$ and its predecessor vehicle $m \in P_{i j}$ at time $t \in T$. Similarly, constraints (1h) ensure that vehicle $j \in N^{t}$ on lane $i$ keeps a safe distance with conflicting vehicles $m$ on lane $l \in C_{i}$ at time $t \in T$. Constraints (1h) avoid simultaneous crossings of conflict regions, where parameters $F_{i}$ and $F_{l}$ define the center point of the conflict region of each two lanes, measured from the beginning of each lane. Conflict regions are defined by the vehicle length and a safety distance. Note that the trajectory information $\widehat{X}_{i m}^{t+1}$ of neighboring vehicle $m$ on lane $i$ is an input in constraints (1g)-(1h). Parameters $L_{v}, D$, and $R$ represent
the vehicle length, a safety distance between CAVs, and the CAV's reaction time. Note that problem (1a)-(1h), if solved centrally for the total number of vehicles over the entire study period, provides the theoretical optimal trajectories.

### 2.2. Solution technique

The proposed problem (1a)-(1h), due to its CAV-level distributed nature, can suffer from huge state space when the number of CAVs increases in the intersection neighborhood. The exchange of state information between CAVs, i.e., capturing the current and predicted trajectories of neighboring vehicles in constraints (1g)-(1h), can help tackle the complexity of the problem at the cost of yielding sub-optimal or infeasible solutions. Note that the infeasibility can occur due to unseen interactions between CAVs at con-flicting regions (i.e., the safety constraints are loosely enforced due originally to lack of sufficient coordination among CAVs). Thus, we design a coordination methodology to push the CAV-level solutions towards global optimality. The details of the proposed technique follow.

The most recent CAVs' decisions $a_{i j}^{t}$ will be used to update the trajectories of neighboring CAV $j$ on lane $i$ at time $t$, i.e., state $S_{i j}^{t}$ captured in constraints (1g)-(1h), to avoid infeasible solutions. Note that constraints (1h) are the source of non-convexity in this problem since they divide the feasible region into two separate regions to prevent crashes at the conflict regions. We let $\delta_{j m}^{t}$ denote a vector of slack variables, to penalize the violation of constraints (1g)-(1h), that defines the difference between a minimum safety distance and the actual distance of vehicle $j \in N^{t}$ from

(i) its neighboring vehicle $m$ in constraints (1g) or
(ii) its pre-defined destination $r_{i}^{h}$ in constraints (1h).

Hence, constraints (1g)-(1h) will be re-written as

$$
\begin{aligned}
& \widehat{X}_{i m}^{t+1}-X_{i j}^{t+1}+\delta_{j m}^{t} \geq L_{v}+D+R \mathscr{V}_{i j}^{t+1}, \quad \forall i \in I, j \in N^{t}, m \in P_{i j}, t \in T \\
& \left|X_{i j}^{t+1}-F_{i}\right|+\left|\widehat{X}_{l m}^{t+1}-F_{l}\right|+\delta_{j m}^{t} \geq L_{v}+D, \quad \forall i \in I, l \in C_{i}, j, m \in N^{t}, t \in T \\
& 0 \leq \delta_{j m}^{t} \leq \delta_{M a x}, \quad \forall j, m \in N^{t}, t \in T
\end{aligned}
$$

Note, that the maximum value of slack $\delta_{\text {Max }}$ in constraints (2c) ensures that relaxing the coupling constraints avoids conflicts as vehicles always keep the minimum safety distance $L_{v}+D-\delta_{M a x}$.

Constraints (2b) introduce non-linearity to the proposed problem. We add binary variables $\theta_{i j}^{t+1}$ for vehicle $j \in N^{t}$ located on lane $i \in I$ at time $t \in \mathrm{~T}$ to linearize them as follows.

$$
\begin{aligned}
& X_{i j}^{t+1}-F_{i}+\left|\hat{X}_{l m}^{t+1}-F_{l}\right|+\delta_{j m}^{t} \geq L_{v}+D-M\left(1-\theta_{i j}^{t+1}\right), \quad \forall i \in I, l \in C_{i}, j, m \in N^{t}, t \in T, \\
& -X_{i j}^{t+1}+F_{i}+\left|\hat{X}_{l m}^{t+1}-F_{l}\right|+\delta_{j m}^{t} \geq L_{v}+D-M \theta_{i j}^{t+1}, \quad \forall i \in I, l \in C_{i}, j, m \in N^{t}, t \in T, \\
& \theta_{i j}^{t+1} \in\{0,1\}, \quad \forall i \in I, j \in N^{t}, t \in T
\end{aligned}
$$

where $M$ is a large number. Similarly, constraints (1f) are linearized as follows.

$$
\begin{aligned}
& e_{i}^{h} \leq X_{i j}^{t+1}+M\left(1-\rho_{1 i j}^{t+1}\right), \quad \forall i \in I_{l}, j \in N^{t}, t \in T \\
& e_{i}^{h}>X_{i j}^{t+1}-M \rho_{1 i j}^{t+1}, \quad \forall i \in I_{l}, j \in N^{t}, t \in T \\
& X_{i j}^{t+1} \leq r_{i}^{h}+M\left(1-\rho_{2 i j}^{t+1}\right), \quad \forall i \in I_{l}, j \in N^{t}, t \in T \\
& X_{i j}^{t+1}>r_{i}^{h}-M \rho_{2 i j}^{t+1}, \quad \forall i \in I_{l}, j \in N^{t}, t \in T \\
& 0 \leq \rho_{1 i j}^{t+1}+\rho_{2 i j}^{t+1}-2 \rho_{3 i j}^{t+1} \leq 1, \quad \forall i \in I_{l}, j \in N^{t}, t \in T \\
& V_{i j}^{t+1}-\varepsilon^{\prime} \leq M\left(1-\rho_{3 i j}^{t+1}\right), \quad \forall i \in I_{l}, j \in N^{t}, t \in T, \\
& \rho_{1 i j}^{t+1}, \rho_{2 i j}^{t+1}, \rho_{3 i j}^{t+1} \in\{0,1\}, \quad \forall i \in I, j \in N^{t}, t \in T .
\end{aligned}
$$

To establish a higher degree of coordination among CAVs, we add $\delta_{j m}^{t}$ to objective function (1a) and re-define it as follows.

$$
g_{j}=\min _{\boldsymbol{a}} \sum_{t \in T}\left\{r_{i}^{h}-X_{i j}^{t+1}\right\}+\gamma\left|\mathscr{V}_{i j}^{t+1}-\mathscr{V}_{i j}^{t}\right|+\beta \sum_{t \in T} \delta_{j m}^{t}, \quad \forall i \in I, j \in N^{t}
$$

where slack variables $\delta_{j m}^{t}$ will be minimized in objective function (5). Coefficient $\beta$ is a sufficiently large value to avoid conflicting
trajectories and ensure feasible solutions.
We re-formulate the objective function (5), by defining non-negative auxiliary variables and constraints, to tackle the nonlinearity, as shown below.

$$
\begin{aligned}
& g_{j}=\min _{a} \sum_{t \in T}\left\{r_{i}^{h}-X_{i j}^{t+1}\right\}+\gamma\left(\psi_{i j}^{t+1}+\omega_{i j}^{t+1}\right)+\beta \sum_{t \in T} \delta_{j m}^{t}, \quad \forall i \in I, j \in N^{t} \\
& \psi_{i j}^{t+1}-\omega_{i j}^{t+1}=\mathscr{V}_{i j}^{t+1}-\mathscr{V}_{i j}^{t}, \quad \forall i \in I, j \in N^{t}, t \in T, \\
& \psi_{i j}^{t+1}, \omega_{i j}^{t+1} \geq 0, \quad \forall i \in I, j \in N^{t}, t \in T,
\end{aligned}
$$

Thus, our trajectory optimization problem will be represented by (1b)-(1e), (2a), (2c), (3a)-(3c), (4a)-(4g), (6), and (7a)-(7b). Note that $f_{j}^{*} \leq g_{j}^{*}$ since $\beta \sum_{t \in T} \delta_{j m}^{t} \geq 0$ and thus, $f_{j}^{*}$ is a lower bound to the proposed problem.

To further reduce the computational complexity of the model and account for the dynamic nature of the proposed trajectory planning problem, our proposed DC-SICL uses a model predictive control (MPC) strategy that solves the problem over a prediction horizon $\tau$. Note that $\tau$ is long enough to let a CAV exit the intersection neighborhood. We implement the MPC through three steps: (i) initialization, (ii) consensus, and (iii) implementation and update, as follow.

Step 1. We first initialize the problem at time step $t=0$ by defining an initial set of vehicles $N^{0}$ and vehicle states $S_{i j}^{0}$.
Step 2. We then follow an iterative procedure to ensure CAVs will form consensus on feasible trajectories over $\xi^{t}$ iterations. All variables at each iteration of the consensus procedure are indexed by $\eta \in\left\{1,2, \cdots, \xi^{t}\right\}$. The consensus procedure is described as follows.
2.0. set $\eta=1$ and $S_{i j}^{t, \eta} \leftarrow S_{i j}^{t}$.
2.1. collect $S_{i j}^{t, \eta}$ for all $i \in I, j \in N^{t}$ in prediction horizon $t \rightarrow t+\tau$.
2.2. optimize each CAV's trajectory.

Each CAV $j \in N^{t}$ optimizes its own trajectory, i.e., finds optimal $a_{i j}^{t, \eta}$ through solving problem $\mathscr{A}$ : (1b)-(1e), (2a), (2c), (3a)-(3c), (4a)-(4g), (6), and (7a)-(7b), acquiring predicted trajectories of other CAVs as inputs.
2.3. update trajectory predictions.

The new trajectories for CAV $j \in N^{t}$, found in step 2.2, and trajectories $S_{i j}^{t, \eta}$, from step 2.1, will be averaged using a method adopted from Powell (2007) to push solutions towards forming consensus after $\eta$ th iteration:

$$
\left.S_{i j}^{t, \eta+1}=\left(1-\frac{1}{\eta}\right) S_{i j}^{t, \eta}+\left(\frac{1}{\eta}\right) X_{i j}^{t} \right\rvert\, \mathscr{A}, \quad \forall i \in I, j \in N^{t}, t \in T,
$$

2.4. form consensus.

The consensus between trajectories is achieved when the trajectory remains unchanged for all CAVs over iterations $\eta$. If no consensus is formed, we set $\eta \leftarrow \eta+1$ and decrease the maximum value of slack $\delta_{\text {Max }}$ in constraints (2c) to push solutions toward feasibility. We then go back to step 2.1; otherwise, we continue to Step 3.

Step 3. We then set $S_{i j}^{t+1} \leftarrow S_{i j}^{t, \eta+1}$ and calculate speed $\mathscr{V}_{i j}^{t}$ based on the final averaged trajectory decisions $S_{i j}^{t+1}$. The speed will be implemented at time $t$ for all CAVs only for the first time step (e.g., starting from $t=0$ ). The remaining averaged trajectories (i.e.,

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-07.jpg?height=566&width=1088&top_left_y=1777&top_left_x=403)
Fig. 3. Implementation of updated trajectories.

$t \rightarrow t+\tau$ ) will be considered as predicted trajectories for near future and shared with corresponding CAVs (see Fig. 3). Therefore, at the next time step (e.g., $t=1$ ), CAV $j$ obtains all recently updated trajectories of other CAVs as inputs and follows the proposed procedure from Step 2. We then update the set $N^{t+1}$, roll one time step, and set $t \leftarrow t+1$.

Steps 2 and 3 continue until CAVs' trajectories are implemented at $\Gamma-1+\tau$ that is defined as the end of the study period. Fig. 4 shows the general framework for the DC-SICL.

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-08.jpg?height=860&width=719&top_left_y=425&top_left_x=582)
Fig. 4. DC-SICL general framework.

### 2.3. Benchmark

This section introduces two benchmark intersection control methodologies used to further evaluate the performance of the proposed DC-SICL:
(i) signal-head-free intersection control logic (SICL) developed by Mirheli et al. (2018) and
(ii) optimized fully-actuated signal control in VISTRO (PTV group, 2014).

The first benchmark methodology formulates a central intersection-level CAV trajectory optimization that determines near-optimal solutions through the exchange of information between CAVs and a central control unit located at intersections. The model is similar to (1a)-(1h); however, it reflects an intersection-level scheme; see Mirheli et al. (2018) for more details. The control unit receives CAVs' states and optimizes the trajectories including CAV priorities to pass through and cross the intersection. The problem is then represented by a dynamic programming formulation and solved by applying a stochastic look-ahead model based on Monte Carlo tree search (MCTS) technique. The central intersection-level trajectory design model is solved at each time step $t$ based on current CAVs' states and an estimation of the value function for future. The MCTS technique is designed to avoid exponential expansion of the tree search and estimate the value function more accurately under a minimal computational burden. The proposed methodology provides non-real-time near-optimal solutions for the SICL framework. The second benchmark methodology is a fullyactuated signal control system with centrally optimized timing plans developed in VISTRO (PTV Group, 2015).

## 3. Numerical experiments

The proposed DC-SICL is coded in JAVA and run on a desktop computer with a quad-core 3.6 GHz CPU and 24 GB memory. We have implemented the proposed methodology in VISSIM microscopic traffic simulator (PTV Group, 2015), generated CAV arrivals in the intersection neighborhood, and measured the mobility performance measures (i.e., total travel time, number of completed trips, and average speed). We have used VISSIM Component Object Model (COM) interface to exchange CAVs' states between VISSIM and our JAVA-coded DC-SICL.

### 3.1. Case study

We apply the DC-SICL to an isolated four-leg intersection (see Fig. 2) with two exclusive lanes for (i) left-turns and (ii) through movements at each approach. We assume that CAVs choose their lanes prior to their arrival in the intersection neighborhood. We have also considered a detection range of 650ft, which is significantly less than the typical 1000 ft detection range. Besides, it is assumed that each CAV's state is exchanged with other CAVs within the presumed 650 ft range. To accurately update collision-free CAV trajectories, sufficiently short time steps of 0.2 sec are selected in this case study. Besides, the length $L_{v}$ of each CAV is assumed to be 13 ft and the safety distance $D$ to be 20ft. In this study, CAVs will accelerate up to $13.12 \mathrm{ft} / \mathrm{sec}^{2}$ and decelerate down to - $11.15 \mathrm{ft} / \mathrm{sec}^{2}$, respectively. The maximum desired speed is $46 \mathrm{ft} / \mathrm{sec}$. Moreover, the maximum speed for turning movements at the intersection is defined as $22 \mathrm{ft} / \mathrm{sec}$.

Using VISSIM demand distribution, we design eight scenarios, to evaluate the performance of DC-SICL, based on traffic volumes (a) within [500, 1500]veh/h/ln for through movements and (b) within [100, 600]veh/h/ln for exclusive left-turn movements. Table 1 summarizes six symmetric and two asymmetric demand patterns.

The numerical results in 15 min analysis periods (after a $1-\mathrm{min}$ warm up) are compared to the proposed benchmark solutions, introduced in the previous section. Specifying different speeds for turning movements, as shown in constraints (4a)-(4g), introduces binary variables. Therefore, the benchmark SICL method cannot solve the problem at very high traffic volumes. To compare the performance of DC-SICL with the benchmarks at high volumes, we have defined two more scenarios without turning movements; see Table 2.

Table 1
Demand patterns in DC-SICL.
| Scenario | East and West bound |  | North and South bound |  |
| :--- | :--- | :--- | :--- | :--- |
|  | Through demand(veh/h/ln) | Left-turn demand(veh/h/ln) | Through demand (veh/h/ln) | Left-turn demand(veh/h/ln) |
|  | Symmetric demand |  |  |  |
| 1 | 500 | 100 | 500 | 100 |
| 2 | 600 | 120 | 600 | 120 |
| 3 | 750 | 150 | 750 | 150 |
| 4 | 900 | 170 | 900 | 170 |
| 5 | 1200 | 400 | 1200 | 400 |
| 6 | 1500 | 600 | 1500 | 600 |
| Asymmetric demand |  |  |  |  |
| 7 | 1200 | 400 | 900 | 150 |
| 8 | 1500 | 600 | 1100 | 150 |


Table 2
Demand patterns without left-turn movements in DC-SICL.
| Scenario | East and West bound |  | North and South bound |  |
| :--- | :--- | :--- | :--- | :--- |
|  | Through demand(veh/h/ln) | Left-turn demand(veh/h/ln) | Through demand (veh/h/ln) | Left-turn demand(veh/h/ln) |
| Symmetric demand |  |  |  |  |
| 9 | 1200 | 0 | 1200 | 0 |
| 10 | 1500 | 0 | 1500 | 0 |


### 3.2. Results

We first conduct a set of sensitivity analyses to understand the behavior of the proposed formulation based on the number of iterations $\xi^{t}$ to find the best $\xi^{t}$ for all computational experiments. Then, we analyze the performance of our DC-SICL in comparison with the benchmarks, in terms of objective values, mobility performance measures, and safety, based on the proposed demand patterns in Scenarios 1-10. Finally, the computational performance of the proposed DC-SICL will be compared to SICL.

### 3.2.1. Sensitivity analysis

Fig. 5 shows the summation of objective values (6) for all CAVs in the intersection for the demand pattern in Scenario 6. In this minimization problem, increasing the number of iterations $\xi^{t}$ decreases the objective value (6) and feasible solutions converge to the optimality. We observe considerable reductions in the objective value when the number of iterations $\xi^{t}$ increases from 1 to 5. The reductions become insignificant by adding more iterations. The same trend is observed in other demand scenarios as well. However, $\xi^{t}$ has a direct relationship with the computation time. Hence, we have selected $\xi^{t}=5$ in this study since no significant improvement is observed in the objective value afterwards; see Fig. 5.

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-10.jpg?height=393&width=723&top_left_y=187&top_left_x=582)
Fig. 5. The changes of objective value (6) $\left(\times 10^{7}\right)$ for 10 iterations.

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-10.jpg?height=617&width=1148&top_left_y=679&top_left_x=371)
Fig. 6. Changes in trajectory across different iterations.

Fig. 6 shows a left-turning vehicle's trajectory over different iterations. The vehicle enters the intersection neighborhood at time $85{ }^{\text {th }}$ second and proceeds towards the intersection at the free flow speed. The trajectory over iterations is virtually the same up to (approximately) time $97{ }^{\text {th }}$ second, when it starts to reduce its speed to observe the turning movement speed limit. As shown, the trajectories do not show fluctuation over iterations and seem to converge. Similar trends are observed for other vehicles as well.

Fig. 7 shows changes in trajectory of the same vehicle over time from one iteration to the next. It is apparent that the changes in trajectory from iteration 1 to 2 is large; however, the difference decreases over iterations. It can be observed that the difference converges to almost zero at iterations 9 and 10.

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-10.jpg?height=635&width=1146&top_left_y=1709&top_left_x=373)
Fig. 7. The difference of trajectories between two consecutive iterations.

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-11.jpg?height=437&width=1209&top_left_y=181&top_left_x=341)
Fig. 8. (a) Sum of travel time and speed variation term in the objective function $\left(\times 10^{7}\right)$ and (b) Sum of slack values in the objective function $\left(\times 10^{7}\right)$.

The objective function (5), without the slack $\delta_{j m}^{t}$, is equivalent to the original objective function (1a). To further analyze the impact of $\delta_{j m}^{t}$ on slack $\xi^{t}$, we have used the demand pattern in Scenario 6 in two studies:
(i) variations of objective function (1a) over iterations $\xi^{t}$, as shown in Fig. 8(a) and
(ii) variations of slack $\delta_{j m}^{t}$ over iterations $\xi^{t}$, as shown in Fig. 8(b).

The first study reveals that increasing the number of iterations $\xi^{t}$ decreases the original objective value (1a), which confirms that the solutions are pushed towards optimality. Besides, the second study shows that increasing the number of iterations $\xi^{t}$ decreases the slack $\delta_{j m}^{t}$, which confirms that the solutions are pushed toward feasibility (i.e., collision-free trajectories). Same trends are observed for other scenarios as well.

### 3.2.2. Benchmark comparisons

3.2.2.1. Marginal objective values. Fig. 9 shows the values of objective function (1a) compared to the SICL benchmark based on different demand patterns. Note that high traffic volume scenarios (i.e., 5-8) cannot be solved by SICL due to the complexity of the central mixed integer linear problem. As indicated, the objective value of SICL is always less than our proposed DC-SICL. However, the maximum gap between the two solutions is 2.30\%, which confirms that the solutions of the proposed distributed approach are very close to those of the centralized approach.

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-11.jpg?height=345&width=745&top_left_y=1394&top_left_x=572)
Fig. 9. The objective value ( $\times 10^{7}$ ) comparison between the DC-SICL and SICL.

3.2.2.2. Mobility performance. Table 3 compares mobility performance measures obtained from DC-SICL compared to SICL and the fully-actuated signal timing in different scenarios. As indicated, our proposed DC-SICL reduces the travel time up to 70.5\% and increases the throughput and average speeds up to 115.6\% and 400.0\%, respectively in comparison with the fully-actuated signal control. Therefore, our DC-SICL outperforms the fully-actuated signal control benchmark with respect to all mobility performance measures, particularly in higher traffic demands.

As shown in Table 3, throughput in all scenarios is almost the same in both DC-SICL and SICL. However, compared to the SICL, our DC-SICL yields slightly higher travel time values by at most $0.5 \%$. Besides, we can observe slightly lower average speeds in our DC-SICL compared to SICL, by at most 0.5\% for Scenarios 1-4, 9, and 10. Therefore, the distributed approach yields the same traffic operations as the centralized approach.

Fig. 10 shows the trajectories of CAVs approaching the intersection on lane 8 (see Fig. 2) in both distributed and central control logics (i.e., DC-SICL and SICL) based on the demand pattern in Scenario 4. The dashed line shows the intersection location from the beginning of lane 8 . We can observe that both approaches maintain the desired vehicle speeds until a potential conflict enforces them to decelerate.

As indicated, the number of stops is reduced to zero in both solutions; vehicles maintain safe trajectories by changing their speeds slightly and avoiding complete stops. A comparison between Fig. 10(a) and (b) show more frequent speed variations in DC-SICL due

Table 3
Mobility performance.
| Scenario | Mobility performance | DC-SICL (a) |  |  | SICL (b) | Fully-actuated control (c) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | Value | \% Diff (a) - (b) | \% Diff (a) - (c) |  |  |
| 1 | Travel time (sec) | 21,260.0 | 0.3 | -43.0 | 21,199.6 | 37,279.3 |
|  | Throughput | 642 | 0.0 | 6.3 | 642 | 604 |
|  | Average speed (ft/sec) | 42.0 | -0.2 | 59.1 | 42.1 | 26.4 |
| 2 | Travel time (sec) | 25,197.2 | 0.4 | -44.9 | 25,105.2 | 45,692.1 |
|  | Throughput | 757 | 0.0 | 4.8 | 757 | 722 |
|  | Average speed (ft/sec) | 41.9 | -0.5 | 62.4 | 42.1 | 25.8 |
| 3 | Travel time (sec) | 32,265.0 | 0.4 | -49.1 | 32,127.2 | 63,426.9 |
|  | Throughput | 956 | 0.0 | 7.2 | 956 | 892 |
|  | Average speed (ft/sec) | 41.8 | -0.5 | 81.0 | 42.0 | 23.1 |
| 4 | Travel time (sec) | 35,540.0 | 0.4 | -62.0 | 35,400.4 | 93,556.6 |
|  | Throughput | 1035 | 0.0 | 0.8 | 1035 | 1027 |
|  | Average speed (ft/sec) | 41.6 | -0.2 | 128.6 | 41.7 | 18.2 |
| 5 | Travel time (sec) | 60,990.8 | NA ${ }^{\mathrm{a}}$ | -60.8 | NA | 155,411.5 |
|  | Throughput | 1624 | NA | 44.9 | NA | 1121 |
|  | Average speed (ft/sec) | 38.3 | NA | 219.2 | NA | 12.0 |
| 6 | Travel time (sec) | 71,784.4 | NA | -57.1 | NA | 16,7171.7 |
|  | Throughput | 1808 | NA | 57.6 | NA | 1147 |
|  | Average speed (ft/sec) | 36.5 | NA | 220.2 | NA | 11.4 |
| 7 | Travel time (sec) | 48,779.0 | NA | -63.6 | NA | 133,911.9 |
|  | Throughput | 1383 | NA | 25.0 | NA | 1106 |
|  | Average speed (ft/sec) | 40.3 | NA | 194.2 | NA | 13.7 |
| 8 | Travel time (sec) | 62,166.8 | NA | -58.8 | NA | 150,939.4 |
|  | Throughput | 1727 | NA | 52.0 | NA | 1136 |
|  | Average speed (ft/sec) | 39.4 | NA | 215.2 | NA | 12.5 |
| 9 | Travel time (sec) | 38,045.0 | 0.5 | -70.5 | 37,869.6 | 128,961.2 |
|  | Throughput | 1199 | -0.1 | 66.1 | 1200 | 722 |
|  | Average speed (ft/sec) | 45.6 | -0.4 | 385.1 | 45.8 | 9.4 |
| 10 | Travel time (sec) | 49,845.8 | 0.4 | -62.7 | 49,644.4 | 133,493.9 |
|  | Throughput | 1561 | -0.1 | 115.6 | 1562 | 724 |
|  | Average speed (ft/sec) | 45.5 | -0.4 | 400.0 | 45.7 | 9.1 |


${ }^{\mathrm{a}}$ Not Available (NA): SICL cannot find trajectories for the associated scenario.
to the lack of central communications among CAVs. Yet, vehicles maintain their desired speeds during short periods of time.
3.2.2.3. Safety performance. We have also analyzed surrogate safety measures for the CAV trajectories to ensure that constraints (2a), (2c), and (3a)-(3c) are not violated, i.e., safe trajectories are found by DC-SICL for all CAVs. The average time to collision (TTC) and the number of near-crash conditions in different demand scenarios are examined using the surrogate safety assessment model (SSAM) software (Gettman and Head, 2003; Pu and Joshi, 2008). TTC for each pair of vehicles is compared with a pre-defined threshold in SSAM and a near-crash condition is reported when TTC is less than the threshold.

Table 4 summarizes the analysis performed in SSAM under 1.5 sec TTC threshold for different traffic conditions. The average TTC in DC-SICL is higher than 1.5 sec in all demand scenarios. The numerical analysis shows zero near-crash conditions since CAVs update their trajectories in DC-SICL every 0.2 sec, where potential conflicts can be detected effectively (i.e., constraints (2a), (2c), and (3a)-(3c) are satisfied and the proposed coordination scheme pushes the solutions towards global optimality). Then vehicles adjust their maneuvers corresponding to their optimal trajectories to avoid accidents. As shown in Table 4, the average TTC is decreased in the VISSIM-simulated fully-actuated signal control that causes a significant number of near-crash conditions.

Since the likelihood of rear-end collision (rather than crossing conflicts) increases in signalized intersections, Table 4 also identifies the types of conflicts at the intersection. The results show that the proposed signal-free intersection control logic significantly reduces the likelihood of rear-end crashes.
3.2.2.4. Computational performance. Fig. 11 compares the computational performance of DC-SICL to SICL based on the demand pattern in Scenario 4. The DC-SICL runtime is defined as the average time that takes a CAV to find its near-optimal trajectory in a planning horizon. As indicated, our proposed methodology solves the problem in less CPU time compared to the benchmark approach since all CAVs simultaneously find their trajectories. Besides, DC-SICL optimizes the vehicle trajectories in real-time since the implementation period is 0.2sec. Note that the computation time of DC-SICL is reported for $\xi^{t}=5$ iterations. Reducing the number of iterations yields a faster performance.

Finally, Table 5 shows the total computation times for DC-SICL compared to SICL for all scenarios. The results indicate that the DC-SICL requires considerably less CPU time to yield near-optimal vehicle trajectories compared to the benchmark approach. Furthermore, the DC-SICL runtime does not increase with the number of vehicles since it follows a distributed architecture. This is not the case in the SICL.

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-13.jpg?height=1171&width=1211&top_left_y=179&top_left_x=336)
Fig. 10. Trajectories of vehicles on lane 8 in Scenario 4: (a) DC-SICL and (b) SICL.

Table 4
SSAM results for average TTC and number of accidents in traffic condition, 1.5 sec assigned threshold in SSAM.
| Scenario | DC-SICL |  | SICL |  | Fully-actuated signal control |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Ave. TTC(sec) | \# near-crash conditions | Ave. TTC(sec) | \# near-crash conditions | Rear End |  | Crossing |  |
|  |  |  |  |  | Ave. TTC(sec) | \# near-crash conditions | Ave. TTC(sec) | \# near-crash conditions |
| 1 | > 1.5 | 0 | > 1.5 | 0 | 1.15 | 35 | > 1.5 | 0 |
| 2 | > 1.5 | 0 | > 1.5 | 0 | 1.2 | 41 | > 1.5 | 0 |
| 3 | > 1.5 | 0 | > 1.5 | 0 | 1.14 | 55 | > 1.5 | 0 |
| 4 | > 1.5 | 0 | > 1.5 | 0 | 1.16 | 60 | > 1.5 | 0 |
| 5 | > 1.5 | 0 | NA ${ }^{\mathrm{a}}$ | NA | 1.11 | 83 | > 1.5 | 0 |
| 6 | > 1.5 | 0 | NA | NA | 1.09 | 69 | > 1.5 | 0 |
| 7 | > 1.5 | 0 | NA | NA | 1.04 | 65 | > 1.5 | 0 |
| 8 | > 1.5 | 0 | NA | NA | 0.97 | 78 | > 1.5 | 0 |
| 9 | > 1.5 | 0 | > 1.5 | 0 | 1.28 | 67 | > 1.5 | 0 |
| 10 | > 1.5 | 0 | > 1.5 | 0 | 1.23 | 82 | > 1.5 | 0 |


[^1]
## 4. Conclusions

This study develops a distributed coordinated trajectory optimization problem for CAVs for signal-free intersections. The problem is formulated as vehicle-level MINLPs and a coordination scheme is proposed between CAVs, through vehicle to vehicle communications, to push the distributed vehicle-level solutions towards global optimality. An MPC is utilized to capture the dynamics of the problem and provide predictions on vehicle states and future trajectories. CAVs solve their trajectory planning problem and update their solutions until they reach consensus. The numerical experiments quantify the effects of the proposed methodology on traffic

![](https://cdn.mathpix.com/cropped/002cb0af-6ef4-46a5-b1a1-621d3cef9c87-14.jpg?height=405&width=723&top_left_y=189&top_left_x=582)
Fig. 11. Comparison of the computation times.

Table 5
Total computation times (sec).
| Scenario | DC-SICL | SICL |
| :--- | :--- | :--- |
| 1 | 414.1 | 1703.4 |
| 2 | 337.9 | 2479.2 |
| 3 | 405.8 | 3926.5 |
| 4 | 424.0 | 5003.7 |
| 5 | 581.6 | NA ${ }^{\mathrm{a}}$ |
| 6 | 676.6 | NA |
| 7 | 497.3 | NA |
| 8 | 586.7 | NA |
| 9 | 286.3 | 9176.7 |
| 10 | 341.8 | 17,145.1 |


${ }^{\mathrm{a}}$ Not Available (NA): SICL cannot find trajectories for the associated scenario.
safety and performance measures in an isolated intersection under various traffic demand scenarios. The results obtained from the proposed distributed methodology are compared to a set of benchmark strategies to evaluate the performance of the proposed DC-SICL in terms of solution quality, mobility and safety performance measures, and computational efficiency. As indicated in the numerical results, the proposed DC-SICL finds near-optimal solutions with a $2.30 \%$ maximum marginal objective value in comparison with the central SICL. Furthermore, the mobility measures, compared to SICL, are at most $0.5 \%, 0.1 \%$, and $0.5 \%$ different for travel time, throughput, and average speed, respectively. Besides, SSAM reports zero near-crash conditions in the proposed DC-SICL. This is not the case for an optimized fully-actuated signal control. Finally, computation time analyses show that the proposed methodology requires less CPU time to yield near-optimal CAV trajectories compared to the benchmark approach in all demand scenarios. The DC-SICL runtime does not increase with traffic volume and remains real-time. It will be interesting to evaluate the mobility and safety performance measures of DC-SICL in an urban-street network in comparison with other alternative benchmarks. Besides, the proposed methodology can be applied to a wide range of large-scale problems to assess its solution quality and computational efficiency. Although the proposed methodology provides near-optimal CAV trajectories in signal-free intersections in real-time, it does not include uncertainties in the problem formulation. It will be worthwhile in the future to analyze the effect of stochsticities on the performance of the proposed methodology.

## References

Ahmane, M., Abbas-Turki, A., Perronnet, F., Wu, J., El Moudni, A., Buisson, J., Zeo, R., 2013. Modeling and controlling an isolated urban intersection based on cooperative vehicles. Transp. Res. Part C Emerg. Technol. 28, 44-62. https://doi.org/10.1016/j.trc.2012.11.004.
Au, T.-C., Stone, P., 2010. Motion Planning Algorithms for Autonomous Intersection Management. AAAI 2010 Work. Bridg. Gap Between Task Motion Plan.
Beak, B., Head, K.L., Feng, Y., 2017. Adaptive coordination based on connected vehicle technology. Transp. Res. Rec. J. Transp. Res. Board 1-12.
Belkhouche, F., 2018. Collaboration and optimal conflict resolution at an unsignalized intersection. IEEE Trans. Intell. Transp. Syst. PP, 1-12. https://doi.org/10. 1109/TITS.2018.2867256.
Boyd, S., Parikh, N., Chu, E., Peleato, B., Eckstein, J., 2011. Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers, 3, 1-122. https://doi.org/10.1561/2200000016.
Campos, G.R., Falcone, P., Wymeersch, H., Hult, R., Sjöberg, J., 2014. Cooperative receding horizon conflict resolution at traffic intersections. In: Decision and Control (CDC), 2014 IEEE 53rd Annual Conference On. pp. 2932-2937.
Cao, Y., Yu, W., Ren, W., Chen, G., 2013. An overview of recent progress in the study of distributed multi-agent coordination. IEEE Trans. Ind. Inform. 9, 427-438.
Carlino, D., Boyles, S.D., Stone, P., 2013. Auction-based autonomous intersection management. In: IEEE Conf. Intell. Transp. Syst. Proceedings, ITSC, pp. 529-534. https://doi.org/10.1109/ITSC.2013.6728285.
Chen, L., Hopman, H., Negenborn, R.R., 2018. Distributed model predictive control for vessel train formations of cooperative multi-vessel systems. Transp. Res. Part C Emerg. Technol. 92, 101-118.
Chouhan, A.P., Banda, G., 2018. Autonomous intersection management: a heuristic approach. IEEE Access 6, 53287-53295. https://doi.org/10.1109/ACCESS.2018. 2871337.
Cortés, J., Bullo, F., 2005. Coordination and geometric optimization via distributed dynamical systems. SIAM J. Control. Optim. 44, 1543-1574.

Dai, P., Liu, K., Zhuge, Q., Sha, E.H., Chung, V., Lee, S., Son, S.H., 2016. A convex optimization based autonomous intersection control strategy in vehicular cyberphysical systems. In: Ubiquitous Intelligence ↓ Computing, Advanced and Trusted Computing, Scalable Computing and Communications, Cloud and Big Data Computing, Internet of People, and Smart World Congress (UIC/ATC/ScalCom/CBDCom/IoP/SmartWorld), 2016 Intl IEEE Conferences, pp. 203-210. https://doi. org/https://doi.org/10.1109/UIC-ATC-ScalCom-CBDCom-IoP-SmartWorld.2016.0050.
Dresner, K., Stone, P., 2008. A multiagent approach to autonomous intersection management. J. Artif. Intell. Res. 31, 591-656.
Dresner, K., Stone, P., 2004. Multiagent traffic management: a reservation-based intersection control mechanism. In: Proc. Third Int. Jt. Conf. Auton. Agents Multiagent Syst, 2004. AAMAS 2004, pp. 530-537. https://doi.org/10.1109/AAMAS.2004.242421.
Duchi, J.C., Agarwal, A., Wainwright, M.J., 2012. Dual averaging for distributed optimization: convergence analysis and network scaling. IEEE Trans. Automat. Contr. 57, 592-606.
Fajardo, D., Au, T.-C., Waller, S., Stone, P., Yang, D., 2011. Automated intersection control. Transp. Res. Rec. J. Transp. Res. Board 2259, 223-232. https://doi.org/10. 3141/2259-21.
Feng, Y., Head, K.L., Khoshmagham, S., Zamanipour, M., 2015. A real-time adaptive signal control in a connected vehicle environment. Transp. Res. Part C Emerg. Technol. 55, 460-473.
Feng, Y., Yu, C., Liu, H.X., 2018. Spatiotemporal intersection control in a connected and automated vehicle environment. Transp. Res. Part C Emerg. Technol. 89, 364-383.
Fitzpatrick, S., Meertens, L., 2003. Distributed coordination through anarchic optimization. Distrib. Sens. Networks 257-295.
Gesbert, D., Kiani, S.G., Gjendemsjo, A., Oien, G.E., 2007. Adaptation, coordination, and distributed resource allocation in interference-limited wireless networks. Proc. IEEE 95, 2393-2409.
Gettman, D., Head, L., 2003. Surrogate safety measures from traffic simulation models. Transp. Res. Rec. J. Transp. Res. Board 104-115.
Ghiasi, A., Hussain, O., Qian, Z.S., Li, X., 2017. A mixed traffic capacity analysis and lane management model for connected automated vehicles: a Markov chain method. Transp. Res. Part B Methodol. 106, 266-292.
Goodall, N., Smith, B., Park, B., 2013. Traffic signal control with connected vehicles. Transp. Res. Rec. J. Transp. Res. Board 65-72.
Guo, Y., Ma, J., Xiong, C., Li, X., Zhou, F., Hao, W., 2019. Joint optimization of vehicle trajectories and intersection controllers with connected automated vehicles: combined dynamic programming and shooting heuristic approach. Transp. Res. Part C Emerg. Technol. 98, 54-72.
Hassan, A.A., Rakha, H.A., 2014. A fully-distributed heuristic algorithm for control of autonomous vehicle movements at isolated intersections. Int. J. Transp. Sci. Technol. 3, 297-309.
Hausknecht, M., Au, T.C., Stone, P., 2011. Autonomous intersection management: multi-intersection optimization. IEEE Int. Conf. Intell. Robot. Syst. 4581-4586. https://doi.org/10.1109/IROS.2011.6048565.
He, Q., Head, K.L., Ding, J., 2012. PAMSCOD: Platoon-based arterial multi-modal signal control with online data. Transp. Res. Part C Emerg. Technol. 20, 164-184. https://doi.org/10.1016/j.trc.2011.05.007.
Ilgin Guler, S., Menendez, M., Meier, L., 2014. Using connected vehicle technology to improve the efficiency of intersections. Transp. Res. Part C Emerg. Technol. 46, 121-131. https://doi.org/10.1016/j.trc.2014.05.008.
Inalhan, G., Stipanovic, D.M., Tomlin, C.J., 2002. Decentralized optimization, with application to multiple aircraft coordination. In: Decision and Control, 2002, Proceedings of the 41st IEEE Conference On, pp. 1147-1155.
Islam, S.M.A.B. Al, Hajbabaie, A., 2017. Distributed-coordinated signal timing optimization in connected transportation networks. Transp. Res. Part C Emerg. Technol. 80, 272-285. https://doi.org/10.1016/j.trc.2017.04.017.
Jiang, H., Hu, J., An, S., Wang, M., Park, B.B., 2017. Eco approaching at an isolated signalized intersection under partially connected and automated vehicles environment. Transp. Res. Part C Emerg. Technol. 79, 290-307.
Keviczky, T., Borrelli, F., Fregene, K., Godbole, D., Balas, G.J., 2008. Decentralized receding horizon control and coordination of autonomous vehicle formations. IEEE Trans. Control Syst. Technol. 16, 19-33.
Kia, S.S., Cortés, J., Martínez, S., 2015. Distributed convex optimization via continuous-time coordination algorithms with discrete-time communication. Automatica 55, 254-264.
Kuwata, Y., How, J.P., 2011. Cooperative distributed robust trajectory optimization using receding horizon MILP. IEEE Trans. Control Syst. Technol. 19, 423-431.
Lee, J., Brian, B., Malakorn, K., Jason, J., 2013a. Sustainability assessments of cooperative vehicle intersection control at an urban corridor. Transp. Res. Part C 32, 193-206. https://doi.org/10.1016/j.trc.2012.09.004.
Lee, J., Park, B., 2012. Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment. IEEE Trans. Intell. Transp. Syst. 13, 81-90. https://doi.org/10.1109/TITS.2011.2178836.
Lee, J., Park, B., Yun, I., 2013b. Cumulative travel-time responsive real-time intersection control algorithm in the connected vehicle environment. J. Transp. Eng. 139, 1020-1029.
Levin, M.W., Boyles, S.D., 2015. Intersection auctions and reservation-based control in dynamic traffic assignment. Transp. Res. Rec. J. Transp. Res. Board 2497, 35-44. https://doi.org/10.3141/2497-04.
Levin, M.W., Rey, D., 2017. Conflict-point formulation of intersection control for autonomous vehicles. Transp. Res. Part C Emerg. Technol. 85, 528-547. https://doi. org/10.1016/j.trc.2017.09.025.
Liu, P., Ozguner, U., Zhang, Y., 2017. Distributed MPC for cooperative highway driving and energy-economy validation via microscopic simulations. Transp. Res. Part C Emerg. Technol. 77, 80-95. https://doi.org/10.1016/j.trc.2016.12.016.
Makarem, L., Gillet, D., 2012. Fluent coordination of autonomous vehicles at intersections. In: Systems, Man, and Cybernetics (SMC), 2012 IEEE International Conference On, pp. 2557-2562.
Malikopoulos, A.A., Cassandras, C.G., Zhang, Y.J., 2018. A decentralized energy-optimal control framework for connected automated vehicles at signal-free intersections. Automatica 93, 244-256. https://doi.org/10.1016/j.automatica.2018.03.056.
Mehrabipour, M., Hajbabaie, A., 2017. A cell based distributed-coordinated approach for network level signal timing optimization. Comput. Aided Civ. Infrastruct. Eng. an Int. J. 32, 599-616.
Mirheli, A., Hajibabai, L., Hajbabaie, A., 2018. Development of a signal-head-free intersection control logic in a fully connected and autonomous vehicle environment. Transp. Res. Part C Emerg. Technol. 92, 412-425. https://doi.org/10.1016/j.trc.2018.04.026.
Mohebifard, R., Hajbabaie, A., 2018. Distributed optimization and coordination algorithms for real-time traffic metering in connected urban street networks. IEEE Trans. Intell. Transp. Syst. https://doi.org/10.1109/TITS.2018.2848246.
Muller, E.R., Carlson, R.C., Junior, W.K., 2016. Intersection control for automated vehicles with MILP. IFAC-PapersOnLine 49, 37-42. https://doi.org/10.1016/j. ifacol.2016.07.007.
Perraki, G., Roncoli, C., Papamichail, I., Papageorgiou, M., 2018. Evaluation of a model predictive control framework for motorway traffic involving conventional and automated vehicles. Transp. Res. Part C Emerg. Technol. 92, 456-471.
Pourmehrab, M., Elefteriadou, L., Ranka, S., 2018. Smart intersection control algorithms for automated vehicles. In: 2017 10th Int. Conf. Contemp. Comput. IC3 2017 2018-Janua, pp. 1-6. https://doi.org/10.1109/IC3.2017.8284361.
Powell, W.B., 2007. Approximate Dynamic Programming: Solving the curses of dimensionality.
Priemer, C., Friedrich, B., 2009. A decentralized adaptive traffic signal control using V2I communication data. In: 2009 12th International IEEE Conference on Intelligent Transportation Systems. IEEE, pp. 1-6. https://doi.org/10.1109/ITSC.2009.5309870.
PTV group, 2014. PTV VISTRO User Manual.
PTV Group, 2015. PTV Vissim 7 User Manual. PTV AG.
Pu, L., Joshi, R., 2008. Surrogate Safety Assessment Model (SSAM)- SOFTWARE USER MANUAL.
Rabbat, M., Nowak, R., 2004. Distributed optimization in sensor networks. In: Proceedings of the 3rd International Symposium on Information Processing in Sensor Networks, pp. 20-27.

Raffard, R.L., Tomlin, C.J., Boyd, S.P., 2004. Distributed optimization for cooperative agents: Application to formation flight. In: Decision and Control, 2004. CDC. 43rd IEEE Conference On, pp. 2453-2459.
Shabanpour, R., Golshani, N., Shamshiripour, A., Mohammadian, A. (Kouros), 2018. Eliciting preferences for adoption of fully automated vehicles using best-worst analysis. Transp. Res. Part C Emerg. Technol. 93, 463-478. https://doi.org/10.1016/j.trc.2018.06.014.
Shahidi, N., 2010. A Delayed Response Policy for Autonomous Intersection Management.
Sun, W., Zheng, J., Liu, H.X., 2018. A capacity maximization scheme for intersection management with automated vehicles. Transp. Res. Part C Emerg. Technol. 94, 19-31. https://doi.org/10.1016/j.trc.2017.12.006.
Tajalli, M., Hajbabaie, A., 2018. Distributed optimization and coordination algorithms for dynamic speed optimization of connected and autonomous vehicles in urban street networks. Transp. Res. Part C Emerg. Technol. 95, 497-515. https://doi.org/10.1016/j.trc.2018.07.012.
Talebpour, A., Mahmassani, H.S., 2016. Influence of connected and autonomous vehicles on traffic flow stability and throughput. Transp. Res. Part C Emerg. Technol. 71, 143-163.
Timotheou, S., Panayiotou, C.G., Polycarpou, M.M., 2015. Distributed Traffic Signal Control Using the Cell Transmission Model via the Alternating Direction Method of Multipliers, 16, pp. 919-933.
Vahidi, A., Sciarretta, A., 2018. Energy saving potentials of connected and automated vehicles. Transp. Res. Part C Emerg. Technol.
Van Brummelen, J., O'Brien, M., Gruyer, D., Najjaran, H., 2018. Autonomous vehicle perception: the technology of today and tomorrow. Transp. Res. part C Emerg. Technol.
Vasirani, M., Ossowski, S., 2012. A market-inspired approach for intersection management in urban road traffic networks. J. Artif. Intell. Res. 43, 621-659. https://doi. org/10.1613/jair.3560.
Wangermann, J.P., Stengel, R.F., 1999. Optimization and coordination of multiagent systems using principled negotiation. J. Guid. Control Dyn. 22, 43-50.
Wu, J., Abbas-Turki, A., El Moudni, A., 2012. Cooperative driving: an ant colony system for autonomous intersection management. Appl. Intell. 37, 207-222. https://doi.org/10.1007/s10489-011-0322-z.
Wuthishuwong, C., Traechtler, A., Bruns, T., 2015. Safe Trajectory Planning for Autonomous Intersection Management by Using Vehicle to Infrastructure Communication - Springer. https://doi.org/10.1186/s13638-015-0243-3.
Xiao, L., Wang, M., Schakel, W., van Arem, B., 2018. Unravelling effects of cooperative adaptive cruise control deactivation on traffic flow characteristics at merging bottlenecks. Transp. Res. Part C Emerg. Technol. 96, 380-397.
Xu, B., Li, S.E., Bian, Y., Li, S., Ban, X.J., Wang, J., Li, K., 2018. Distributed conflict-free cooperation for multiple connected vehicles at unsignalized intersections. Transp. Res. Part C Emerg. Technol. 93, 322-334. https://doi.org/10.1016/j.trc.2018.06.004.
Yang, K., Guler, S.I., Menendez, M., 2016. Isolated intersection control for various levels of vehicle technology: Conventional, connected, and automated vehicles. Transp. Res. Part C Emerg. Technol. 72, 109-129.
Zhang, Y.J., Malikopoulos, A.A. and Cassandras, C.G., 2016. Optimal control and coordination of connected and automated vehicles at urban traffic intersections. In: 2016 American Control Conference (ACC) (pp. 6227-6232). IEEE.
Zhao, W., Ngoduy, D., Shepherd, S., Liu, R., Papageorgiou, M., 2018. A platoon based cooperative eco-driving model for mixed automated and human-driven vehicles at a signalised intersection. Transp. Res. Part C Emerg. Technol. 95, 802-821.
Zohdy, I.A., Rakha, H.A., 2014. Intersection management via vehicle connectivity: the intersection cooperative adaptive cruise control system concept. J. Intell. Transp. Syst. 00, 1-16. https://doi.org/10.1080/15472450.2014.889918.


[^0]:    *Corresponding author.
    E-mail address: leila.hajibabaidizaji@stonybrook.edu (L. Hajibabai).

[^1]:    ${ }^{\mathrm{a}}$ Not Available (NA): SICL cannot find trajectories for the associated scenario.

