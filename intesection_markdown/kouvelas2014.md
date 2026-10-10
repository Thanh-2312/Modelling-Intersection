# Maximum Pressure Controller for Stabilizing Queues in Signalized Arterial Networks 

Anastasios Kouvelas, Jennie Lioris, S. Alireza Fayazi, and Pravin Varaiya

In this paper the problem of arterial signal control is considered. Urban intersections face serious congestion problems, but the installation and maintenance of centralized systems is deemed cumbersome. A decentralized approach that is relatively simple to implement is studied. The recently proposed maximum pressure controller, demonstrated to stabilize queues in arterial traffic systems, is tested in simulations. Modifications of the controller are analyzed and compared under the same demand scenarios. The mesoscopic model used for the simulation experiments is an extended version of the store-and-forward model and emulates the arterial traffic network as a queuing system. The results demonstrate the efficiency of the maximum pressure algorithm, which, under certain conditions, can stabilize all queues in the system.

Recent advancements in computing and communications have set the ground for the development and implementation of the next generation of traffic control strategies. An effort toward the design and deployment of efficient signal control systems is emerging, especially in arterial networks, as urban congestion continues to grow in most cities around the world. Even though measures such as road pricing have improved public transport operations and access restrictions of various kinds, driver information, and guidance also can alleviate congestion, improved signal control strategies remain a significant objective. Real-time signal control systems that respond automatically to prevailing traffic conditions are deemed to be potentially more efficient than clock-based fixed-time control settings. Various strategies have been developed over the past few decades, some of which have been implemented while others are still in the research stage. Good reviews are available elsewhere (1, 2).

SCOOT (3) and SCATS (4) were among the earliest efforts to develop adaptive traffic control systems for arterial networks. These well-known, widely used, traffic-responsive control systems are based on heuristic optimization algorithms. Other optimization methods for arterial traffic control that follow a centralized design

[^0]avenue include OPAC (5), PRODYN (6), and RHODES (7), which all are based on dynamic programming and the rolling-horizon optimization scheme. More recently, the TUC system, which applies a multivariable feedback regulator approach that derives from a linear-quadratic optimal control problem, was introduced (8). This system has been implemented successfully in several large networks in Europe and South America; Kosmatopoulos et al. report some recent field results (9).

All the aforementioned systems have a centralized nature; in other words, the control inputs are a function of all the measurements of the network. Therefore, to apply one of these systems, the information from all intersections must be collected and transmitted to a central location (i.e., a traffic management center). This communication and computing architecture imposes significant installation, operating, and maintenance costs that have inhibited widespread adoption of traffic-responsive and -adaptive controls. According to Lindley, traffic-responsive and -adaptive controls achieve large benefits, but fewer than 10\% of intersections in the United States use them because of the deployment costs of detection and communication and uncertainty about the benefits (10). In contrast, local controllers use only the measurements around a certain area of interest and are considered easier to implement and more cost-effective.

This paper presents the local feedback controller maximum pressure, which is applied intersection by intersection and uses only the adjacent queue length measurements. The method was originally proposed by Tassiulas and Ephremides, who considered the problem of routing and scheduling packet transmissions in a wireless network (11). In packet networks, the term backpressure policy has been adopted. The name maximum pressure may have been coined by Dai and Lin, and it seems to be the preferred term for scheduling and routing in flexible manufacturing networks (12). Much literature on maximum pressure or backpressure algorithms is available. Different variations on the method that potentially can be applied to arterial road networks in real time (depending on the available infrastructure and communication capabilities) are presented here and evaluated in a mesoscopic simulation environment.

For the purposes of simulation, an event-based queuing model was developed and validated to capture the dynamics of queues on arterial streets. For the validation procedure, real data collected under the next generation simulation (NGSIM) initiative from an arterial in the Los Angeles, California, area were used (13). Results of the simulation investigations demonstrate the ability of maximum pressure to stabilize the queues of the studied system, whereas other local controllers (including priority service and fully actuated control) are proven to not stabilize the queues of vehicles in arterial intersections. Details are available elsewhere (14).

## DECENTRALIZED FEEDBACK CONTROL

In this section, the maximum pressure controller for arterial networks is introduced. This decentralized controller does not require any knowledge of the mean current or future demands of the network (in contrast to other model predictive control frameworks). Maximum pressure stabilizes the network if the demand is within certain limits and thereby maximizes network throughput. However, it does require knowledge of mean turn ratios and saturation rates, even though an adaptive version of maximum pressure will have the same performance if turn movements and saturation rates can be measured. It requires only local information at each intersection and is proven to maximize throughput (14). Several variations on the basic method (depending on the available infrastructure) are presented that can be applied in real time.

## Notations

The arterial network is represented as a directed graph with links $z \in Z$ and nodes $n \in N$. The incoming link set $\left(I_{n}\right)$ and outgoing link set $\left(O_{n}\right)$ are defined for each signalized intersection $n$. It is assumed that the offsets and the cycle time of node $n\left(C_{n}\right)$ are fixed or calculated in real time by another algorithm. A common assumption to enable network offset coordination is that $C_{n}=C$ for all intersections $n \in N$, but it is not the case here because the coordination problem is not considered. The signal control plan of node $n$ (including fixed lost time $L_{n}$ ) is based on a fixed number of stages that belong to the set $\left(F_{n}\right)$, where $v_{j}$ denotes the set of links that receives right of way at stage $j \in F_{n}$. Finally, the saturation flow of link $z \in Z\left(S_{z}\right)$ and the turning movement rates ( $\beta_{i, w}$, where $i \in I_{n}$ and $w \in O_{n}$ ) are assumed to be known and can be constant or varied over time.

By definition, the constraint holds for every node $n$,

$$
\sum_{j \in F_{n}} g_{n, j}\left(k_{n}\right)+L_{n} \leq C_{n}
$$

where $k_{n}=0,1,2, \ldots$ is the control discrete-time index and $g_{n, j}$ is the green time of stage $j$. Inequality in this equation may be useful in cases of strong network congestion to allow for all-red stages (e.g., for strong gating). In addition,

$$
g_{n, j}\left(k_{n}\right) \geq g_{n, j, \min } \quad j \in F_{n}
$$

where $g_{n, j, \min }$ is the minimum permissible green time for stage $j$ in node $n$ and is introduced to guarantee a sufficient allocation of green time to pedestrian phases. The control variables of the problem are $g_{n, j}\left(k_{n}\right)$, which depict the effective green time of every stage $j \in F_{n}$ of every intersection $n \in N$.

## Maximum Pressure

The state of each link $\left[x_{z}\left(k_{n}\right)\right]$ is defined by the number of vehicles waiting in the queue to be served for each control index $\left(k_{n}\right)$, that is, at the beginning of time period $\left[k_{n} C_{n},\left(k_{n}+1\right) C_{n}\right]$. Given that realtime measurements or estimates of all the states are provided, the pressure that each link exerts on the corresponding stage of node $n$ at the beginning of cycle $k_{n}\left[p_{z}\left(k_{n}\right)\right]$ can be calculated as

$$
p_{z}\left(k_{n}\right)=\left[\frac{x_{z}\left(k_{n}\right)}{x_{z, \max }}-\sum_{w \in O_{n}} \frac{\beta_{i, w} x_{w}\left(k_{n}\right)}{x_{w, \max }} g_{n, j}\left(k_{n}\right)\right] S_{z} \quad z \in I_{n}
$$

where $x_{z \text {, max }}$ is the storage capacity of link $z$ (in vehicles). Storage capacity is used in the denominator to account for the link lengths so that the pressure of a short link with several vehicles waiting to be served is higher than the pressure of a longer link with the same number of vehicles. The measurements (or estimates) $x_{z}\left(k_{n}\right)$, $\forall z \in Z$, represent feedback from the network under control, based on which the new pressures are calculated via the equation in real time.

The pressure of link $z$ during the control cycle $k_{n}$ is the queue length of the link (first term in the brackets) minus the average queue length of all the output links (second term in the brackets). Regarding the second term as the (average) downstream queue length and the first as the upstream queue length, the definition of the pressure is simply the difference between the upstream and downstream queue lengths. In the case where all output links are exiting the network [exit links are assumed to have infinite capacity (i.e., they do not experience any downstream blockage)], the second term in the brackets becomes zero. Therefore, the pressure of the link is simply the queue length multiplied by its corresponding saturation rate.

If the last equation is applied with $\forall z \in I_{n}$, the pressures of all incoming links of node $n$ are calculated. The pressure of each stage $j$ of the intersection then can be computed as

$$
P_{n, j}\left(k_{n}\right)=\max \left\{0, \sum_{z \in v_{j}} p_{z}\left(k_{n}\right)\right\} \quad j \in F_{n}
$$

This metric can be used to calculate splits for the conflicting stages of the intersection.

## Variations on Maximum Pressure

This paper investigates different modifications of maximum pressure control and their ability to stabilize system queues via simulation experiments. A demand (i.e., time series of incoming flow in the network origins) is said to be able to be stabilized if an existing control plan can accommodate it (i.e., the time average of every mean queue length is bounded). The set of feasible (able to be stabilized) demands $D$ is convex and can be defined easily for an intersection by solving a collection of linear inequalities that involve only the mean values of the demands, turn ratios, and saturation rates. If a demand $D^{0}$ is in the interior of the convex set $D$, then a fixed-time control exists that stabilizes the queues. Under this control, the intersections may experience cycle failures, but no queue is going to grow continuously.

Given that the pressure of each stage was computed in the last equation of the previous section, the total effective green time that is available to be distributed in node $n\left(G_{n}\right)$ can be split to all stages in many ways.

$$
G_{n}=C_{n}-L_{n}-\sum_{j \in F_{n}} g_{n, j, \min } \quad n \in N
$$

One approach is to select the stage with the maximum pressure and activate it for the next control cycle $C_{n}$, which implies that all the available effective green time $G_{n}$ will be given to this stage. In the next cycle, system queues are updated, new pressures are calculated, and the stage with the maximum pressure is selected to be activated. This approach may not be optimal, because the control cycle may be large and queues can grow unexpectedly at links that are not activated. Alternatively, maximum pressure can be called several times in a cycle $C_{n}$. However, every time the stage with the maximum
pressure is activated, the frequency of the measurements and control increases. The frequency of maximum pressure application to an intersection depends on two main factors: (a) available infrastructure and communications (i.e., the appropriate measurements or estimates of queue lengths should be provided in real time) and (b) optimal frequency of maximum pressure application, which must be investigated and defined (and could depend on the special characteristics of each site).

Another approach is to call maximum pressure at the end of each cycle and split green time $G_{n}$ proportionally to the computed pressure of each stage. For each decision variable $\widetilde{g}_{n, j}\left(k_{n}\right)$, where $\widetilde{g}_{n, j}$ depicts the green time of stage $j$ on top of $g_{n, j, \min }$, an update rule is applied:

$$
\tilde{g}_{n, j}\left(k_{n}\right)=\frac{P_{n, j}\left(k_{n}\right)}{\sum_{i \in F_{n}} P_{n, i}\left(k_{n}\right)} G_{n} \quad j \in F_{n}
$$

Thus, the total amount of green time allocated for each control variable $g_{n j}\left(k_{n}\right)$ for cycle $k_{n}$ is

$$
g_{n, j}\left(k_{n}\right)=\tilde{g}_{n, j}\left(k_{n}\right)+g_{n, j, \min } \quad j \in F_{n}
$$

This procedure is repeated periodically (for every cycle) and requires minimum communication specifications because the local controller is called once per cycle.

## SIMULATION MODEL

A modeling avenue for networkwide simulation of the queue dynamics in arterial networks, especially for oversaturated traffic conditions, is based on the store-and-forward modeling paradigm first proposed by Gazis and Potts (15). According to this model, the equation that describes the evolution of the queue for arterial link $z$ is

$$
x_{z}(t+1)=x_{z}(t)+T_{t \rightarrow(t+1)}\left[q_{z}(t)-s_{z}(t)+d_{z}(t)-u_{z}(t)\right]
$$

where

$$
\begin{aligned}
x_{z}(t)= & \text { number of vehicles in link } z \text { at the end of the dis- } \\
& \text { crete time period } t \text { (for the sake of brevity, also } \\
& \text { called queue in this paper); } \\
T_{t \rightarrow(t+1)}= & \text { sample period [i.e., for the time period between } \\
& \text { the discrete time index } t \text { and }(t+1)] ; \\
q_{z}(t) \text { and } u_{z}(t)= & \text { inflow and outflow, respectively, in the sample } \\
& \text { period; and } \\
d_{z}(t) \text { and } s_{z}(t)= & \text { demand and flow, respectively, exiting the network } \\
& \text { in this link. }
\end{aligned}
$$

[Equation details are published elsewhere (16).] As mentioned earlier, the sample periods are triggered by different kinds of events (e.g., vehicle arrival, signal change, and so forth) in this event-based simulation model and therefore are not constant. The updated previous equation establishes the conservation of vehicles in link $z$. Consider that link $z$ connects two intersections $M_{u}$ and $M_{d}$ such that $z \in O_{M_{u}}$ and $z \in I_{M_{d}}$. The exit flow $\left[s_{z}(t)\right]$ is given by

$$
s_{z}(t)=\beta_{z, 0} q_{z}(t)
$$

where $\beta_{z, 0}$ are exit rates and assumed to be known. The inflow to link $z$ is given by

$$
q_{z}(t)=\sum_{i \in I_{M_{u}}} \beta_{i, z} q_{i}(t)
$$

where $\beta_{i, z}$ with $i \in I_{M_{u}}$ are the turning rates toward link $z$ from the links that enter junction $M_{u}$. Queues are subject to the constraints

$$
0 \leq x_{z}(t) \leq x_{z, \max } \quad z \in Z
$$

where $x_{z, \text { max }}$ is the maximum admissible queue length (in vehicles). Even though it is modeled in the simulator, the right part of the inequality is not used in the present investigation because the aim is to demonstrate the ability of maximum pressure to bound the queue length-thus, no constraint on the maximum length of the queues is applied to the experiments presented. For modeling the outflow $\left[u_{z}(t)\right]$, an approach is introduced that characterizes the modeling approach used and can be found in many places (17). According to this approach, outflow $u_{z}(t)$ of link $z$ is equal to saturation flow $S_{z}$ if the link has the right of way, 0 otherwise. Consequently,

$$
u_{z}(t)=\left\{\begin{array}{lc}
\min \left\{x_{z}(t), S_{z} T_{t \rightarrow(t+1)}\right\} & \text { if sample period } \\
& T_{t \rightarrow(t+1)} \in \text { green phase } \\
0 & \text { if sample period } \\
& T_{t \rightarrow(t+1)} \in \text { red phase }
\end{array}\right.
$$

Another challenge of designing the simulation model has been modeling the turning movements (i.e., when more than one incoming link simultaneously flows to the same outgoing link). According to the signal plans used in the United States (permitted right and left turns must consider gaps between opposite traffic), an arterial network can have multiple input links merging or diverging into output links simultaneously for every discretized time period $t$. This scenario has been modeled with different queues for each movement and gap acceptance criteria, but details are beyond the scope of this paper; the simulation model is discussed elsewhere (14).

## Model Validation

The mesoscopic simulation model was validated with arterial data obtained from NGSIM (13). A network with four signalized intersections in Los Angeles was studied (Figure 1). The model inputs are demand profiles in all network origins (i.e., time series of number of vehicles entering the network), time-varying profiles of split ratios in all nodes, and all the information about signals (i.e., duration of phases, cycles, and offsets). In reality, actuated control is applied to all the studied intersections, therefore, the signal plans can vary over time depending on the prevailing traffic conditions. In the area are two parking lots, the inflows and outflows of which interact with traffic on the main arterial. Detailed information about turn ratios toward the parking lots and outflows from the lots to the main arterial also were provided.

The simulated data set has a duration of 30 min (8:30 to 9:00 a.m.), and the evaluation metric is the comparison between the total simulated outflow (in vehicles) for all the signalized links (Link IDs 1 through 9 in Figure $1 b$ ). In both simulation and in reality, the outflow is measured at the stop line of each link. The results obtained from the validation procedure are presented in Table 1. More precisely, Table 1 presents the real measurements after the raw NGSIM data was processed, the outflows obtained by the simulation model, and a comparison of the two mentioned outflows (as the percentage difference of the simulated over the real values). The comparison is done for 5-min time intervals, and the sampled number of vehicles accumulates as time progresses. The simulated outflows of the signals are close to the

![](https://cdn.mathpix.com/cropped/59c3f810-4166-43c3-974e-d0344639bf76-4.jpg?height=1248&width=1641&top_left_y=118&top_left_x=241)
FIGURE 1 NGSIM arterial network in Los Angeles: ( $a$ ) satellite view of network and ( $b$ ) schematic representation of simulation model (links, nodes, and signals) ( $\mathrm{E}=$ east, $\mathrm{S}=$ south, $\mathrm{W}=$ west, $\mathrm{N}=$ north ).

TABLE 1 Comparison of Total Outflows for Validation Network for Eight Links
| Time (a.m.) | North-South |  |  |  | South-North |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | 1 | 2 | 3 | 4 | 6 | 7 | 8 | 9 |
| Number of Vehicles Measured in Real Data Set (NGSIM) |  |  |  |  |  |  |  |  |
| 8:30-8:35 | 180 | 170 | 158 | 110 | 43 | 99 | 90 | 90 |
| 8:35-8:40 | 355 | 340 | 320 | 221 | 99 | 215 | 192 | 186 |
| 8:40-8:45 | 539 | 513 | 484 | 337 | 139 | 337 | 301 | 291 |
| 8:45-8:50 | 755 | 714 | 667 | 457 | 195 | 454 | 406 | 395 |
| 8:50-8:55 | 973 | 924 | 875 | 601 | 247 | 601 | 541 | 525 |
| 8:55-9:00 | 1,156 | 1,093 | 1,059 | 716 | 302 | 733 | 661 | 642 |
| Simulated Number of Vehicles |  |  |  |  |  |  |  |  |
| 8:30-8:35 | 178 | 177 | 166 | 104 | 43 | 98 | 100 | 84 |
| 8:35-8:40 | 355 | 352 | 319 | 213 | 100 | 220 | 201 | 179 |
| 8:40-8:45 | 541 | 524 | 495 | 344 | 138 | 338 | 316 | 287 |
| 8:45-8:50 | 757 | 738 | 697 | 470 | 194 | 483 | 423 | 390 |
| 8:50-8:55 | 977 | 951 | 918 | 626 | 246 | 630 | 534 | 501 |
| 8:55-9:00 | 1,160 | 1,135 | 1,099 | 751 | 301 | 771 | 655 | 615 |
| Comparison of Assessment Metric (\% difference of number of vehicles) |  |  |  |  |  |  |  |  |
| 8:30-8:35 | -1.11 | 4.12 | 5.06 | -5.45 | 0.00 | -1.01 | 11.11 | -6.67 |
| 8:35-8:40 | 0.00 | 3.53 | -0.31 | -3.62 | 1.01 | 2.33 | 4.69 | -3.76 |
| 8:40-8:45 | 0.37 | 2.14 | 2.27 | 2.08 | -0.72 | 0.30 | 4.98 | -1.37 |
| 8:45-8:50 | 0.26 | 3.36 | 4.50 | 2.84 | -0.51 | 6.39 | 4.19 | -1.27 |
| 8:50-8:55 | 0.41 | 2.92 | 4.91 | 4.16 | -0.40 | 4.83 | -1.29 | -4.57 |
| 8:55-9:00 | 0.35 | 3.84 | 3.78 | 4.89 | -0.33 | 5.18 | -0.91 | -4.21 |


real outflows, indicating that the store-and-forward model accurately simulates real traffic conditions. For the corresponding data set, the network does not experience severe congestion. Finally, the only tuning parameters for the simulation are saturation flows $S_{z}$ for each signal approach, which are assumed to be constant over the whole simulation horizon.

## Closed-Loop Control and Evaluation Metrics

To investigate the efficiency and stabilizing property of the maximum pressure controller, extensive simulation experiments were carried out. The developed simulation model described in the previous section also tests the applicability of the method under real-world conditions because it comprises a replica of real traffic conditions (as validated with real data). The arterial network is modeled as a queuing network with queues of vehicles waiting to be served at conflicting approaches of signalized intersections.

In study experiments, the overall closed-loop scheme uses a properly structured application programming interface module to control the traffic lights of the network in real time. More specifically, at each cycle $k_{n}$, the simulation engine delivers queue lengths for all the incoming and outgoing links of node $n$, which then are used as inputs to the maximum pressure controller. The pressures of each stage of the intersection are calculated, and the signal settings are computed [splits for every stage $g_{n, j}\left(k_{n}\right) \in F_{n}$ ] according to the version of the controller used. Figure 2 illustrates how maximum pressure controller is used in a closed loop with the simulation engine. The blue box denotes computations done on the maximum pressure side. The algorithm gets the simulated queue lengths $x_{z}(t), \forall z \in Z$ and outputs the duration of all stages in real time.

![](https://cdn.mathpix.com/cropped/59c3f810-4166-43c3-974e-d0344639bf76-5.jpg?height=967&width=840&top_left_y=1439&top_left_x=185)
FIGURE 2 Closed-loop testing scheme of max pressure controller using macroscopic simulation engine (API = application programming interface, max = maximum).

Another output of the simulation engine that is used to evaluate the applied control policies is mean travel time. The model keeps track of every individual vehicle, the time stamp when it entered the network, and the time stamps when it enters and exits each consecutive traveled link on its path. The time that each individual vehicle joins a queue also is stamped; thus, the user has access to the complete state of any vehicle in the network (i.e., its location and whether it is moving) at any given time. At the end of the simulation, statistics about the time that each vehicle has spent on each link of the network (e.g., time traveling on free flow and stopping time) are available, and all travel times can be averaged (by approach, link, path, and so forth) to provide a performance metric for enforced signal plans.

## SELECTED SIMULATION RESULTS

Selected illustrative results are presented in this section. Because of the stochastic nature of the simulator (i.e., all vehicles arrivals follow a Poisson process, and turn ratios in intersections follow stochastic distributions with predefined mean values) many replications of the same experiments were run, and results shown here stem from scenarios that are close to the average for the respective case. Figure 3 is a diagram of the fictitious arterial network that was used in the simulations, which consists of four signalized intersections and 12 one-way links. For simplicity, each intersection has two green stages (i.e., no left turns are allowed), the duration of which can be controlled in real time; cycle times and offsets are kept constant for all simulation scenarios. For all experiments, $C_{n}=62, \forall n$, and $g_{n, j \text { min }}=5, \forall n, j$, are used, and the interval between successive green stages is 5 s. The simulation horizon is 1 hour.

Two demand scenarios ( $D^{1}$ and $D^{2}$; vehicle arrivals in all origins of the network over time) are generated, and two fixed-time controls that can stabilize each demand ( $L^{1}$ and $L^{2}$, respectively) are calculated by solving the system of linear inequalities that derive for this network and each demand scenario. The demand scenarios are created in such a way that no single fixed-time control can stabilize both demands. Each simulation is characterized by three attributes: demand, applied control (two variations of maximum pressure are presented here), and link capacity. The third attribute, link capacity, is based on the queue bound and whether the maximum queue inequality is applied.

![](https://cdn.mathpix.com/cropped/59c3f810-4166-43c3-974e-d0344639bf76-5.jpg?height=509&width=548&top_left_y=1798&top_left_x=1248)
FIGURE 3 Directed graph of fictitious arterial network used in simulations with $N=\{1,2,3,4\}$ nodes and $Z=\{1,2, \ldots, 12\}$ links; links exiting network are assumed not to experience any downstream blockage.

In the case that the inequality holds, the storage capacity of the links is assumed to be finite; when the inequality is not applied, the storage capacity of the links is assumed to be infinite. The simulations were run for both cases to investigate whether this constraint is important for the model.

Figure 4a presents the evolution of the total number of vehicles in all the queues of the network $\left[\sum_{z \in Z} x_{z}(t)\right]$ when the queue capacity is infinite, and Figure $4 g$ shows the same run when the capacities are finite. Figure 4c presents the trajectory of the number of queued vehicles when MP1 control is applied. In MP1, the maximum pressure controller is called twice per cycle, and the stage with the maximum current pressure is activated. Figure $4 e$ displays the same scenario with MP2 control, in which the total green duration is split proportionally to the pressures; however, it is done once every $C_{n}$ (i.e., at the beginning of each cycle, according to the current measurements). Figure $4 b$ depicts what happens if, after the end of the simulation presented in Figure $4 a$, demand $D^{2}$ continues with the same fixed-time control $L^{1}$. This demand obviously cannot be

![](https://cdn.mathpix.com/cropped/59c3f810-4166-43c3-974e-d0344639bf76-6.jpg?height=1732&width=1777&top_left_y=657&top_left_x=174)
FIGURE 4 Evolution of total number of vehicles in all network queues for simulations that start with demand $D^{1}$ and different scenarios: (a) $D^{1}$ and $L^{1}$ (infinite capacities), $(b) D^{2}$ after $D^{1}$ and $L^{1}$ (finite capacities), $(c) D^{1}$ and MP1 (infinite capacities), $(d) D^{2}$ after $D^{1}$ and MP1 (infinite capacities), $(e) D^{1}$ and MP2 (finite capacities), and ( $f$ ) $D^{2}$ after $D^{1}$ and MP2 (finite capacities).

(continued)

![](https://cdn.mathpix.com/cropped/59c3f810-4166-43c3-974e-d0344639bf76-7.jpg?height=556&width=1775&top_left_y=204&top_left_x=176)
FIGURE 4 (continued) Evolution of total number of vehicles in all network queues for simulations that start with demand $D^{1}$ and different scenarios: $(g) D^{1}$ and $L^{1}$ (finite capacities) and $(h) D^{2}$ after $D^{1}$ and MP1 (finite capacities).

stabilized by this control, and the sum of the queues grows continuously until the end of the simulation. In contrast, if either MP1 (Figure $4 d$ ) or MP2 (Figure $4 f$ ) is applied, the system is stabilized because the sum of the queues is clearly bounded. Figure 4, $h$ and $d$, are the same run, where the capacities of the queues are considered finite. The queues are assumed finite in Figure $4 f$ as well.

Similar runs have been conducted for demand $D^{2}$, and selective results are presented in Figure 5. The evolution of queues is shown for the fixed-time control $L^{2}$ (Figure $5 a$ ), for controller MP1 (Figure $5 c$ ), and for controller MP2 (Figure $5 e$ ). After the end of demand $D^{2}$ (3,600 s), the simulation continues for another hour using demand $D^{1}$ and the same controllers are applied; results are displayed in

![](https://cdn.mathpix.com/cropped/59c3f810-4166-43c3-974e-d0344639bf76-7.jpg?height=1124&width=1781&top_left_y=1263&top_left_x=174)
FIGURE 5 Evolution of total number of vehicles in all network queues for simulations that start with demand $D^{2}$ and different scenarios: (a) $D^{2}$ and $L^{2}$ (infinite capacities), $(b) D^{1}$ after $D^{2}$ and $L^{2}$ (finite capacities), $(c) D^{2}$ and MP1 (infinite capacities), and $(d) D^{1}$ after $D^{2}$ and MP1 (infinite capacities).

(continued on next page)

![](https://cdn.mathpix.com/cropped/59c3f810-4166-43c3-974e-d0344639bf76-8.jpg?height=552&width=1772&top_left_y=206&top_left_x=178)
FIGURE 5 (continued) Evolution of total number of vehicles in all network queues for simulations that start with demand $D^{2}$ and different scenarios: (e) $D^{2}$ and MP2 (infinite capacities) and ( $f$ ) $D^{1}$ after $D^{2}$ and MP2 (infinite capacities).

Figure $5, b, d$, and $f$, respectively. All experiments presented in Figure 5 were run with infinite link capacities except Figure $5 e$, in which finite capacities were applied for all network links. In Figures 4 and 5, the controller MP2 produces higher oscillations than MP1 does for all experiments, indicating that it is better to call maximum pressure twice per cycle rather than once per cycle, because the recently updated measurements help the controller track the changes in queue lengths and adjust its inputs.

## Evaluation of Simulation Results

The simulation results presented here are some representative runs and comprise only a subset of all the experiments conducted. Two main findings of the simulations are related to control: ( $a$ ) maximum pressure will stabilize the queues of arterial networks if demand is within the feasible area, and $(b)$ the frequency with which the controller is applied affects its performance. According to the figures presented here, the more frequently maximum pressure is applied, the narrower the bounds of the system. However, this statement is not obvious for any arbitrary network topology. For the simulation model, the link capacity (finite versus infinite) does not seem to play an important role, at for this kind of experiment, the objective of which is to validate the stability of the system. One approach is helpful to investigate whether some of the queues are growing continuously with the corresponding control, and the other is important because it allows for the consideration of spillback (or even gridlock) phenomena.

Table 2 displays total travel times (in vehicles × hours) for all the major routes of the arterial network in Figure 3 and for all the simulated scenarios reported in this study. As expected, the total number of vehicles in the queues explodes if the fixed-time control is not appropriate (something that can even happen with other local controllers), although maximum pressure manages to stabilize the state of the system if a feasible fixed-time controller that can stabilize the system exists. The total travel time metric is slightly higher for MP2 than for MP1 because of the different frequencies (once and twice per cycle, respectively).

## CONCLUSIONS

Two versions of the maximum pressure controller are presented here and tested in simulation experiments. The first activates the stage with maximum pressure every time the controller is called, and the second distributes green time proportionally to the respective pressures. The macroscopic simulation model that was used for the investigations was developed in Python language and is based on the storeand-forward model. This event-based simulator (i.e., the simulation step is not constant but defined by events triggered by an event planner module) represents arterial traffic as a queuing system. The results demonstrate the efficiency of the maximum pressure controller and validate the already published theoretical argument that it can stabilize networks of arbitrary topology. As shown, the frequency with which the controller is applied influences the bounds

TABLE 2 Total Travel Time Criterion Computed Under Two Simulation Scenarios
| Route (entry link)(exit link) | Total Travel Time (vehicles * hours) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Simulation Scenario (Figure 4) |  |  |  |  |  |  |  | Simulation Scenario (Figure 5) |  |  |  |  |  |
|  | 1(a) | 1(b) | 1(c) | 1(d) | 1(e) | 1(f) | 1(g) | 1(h) | 2(a) | 2(b) | 2(c) | 2(d) | 2(e) | 2(f) |
| (1)-(3) | 4.63 | 2.25 | 5.02 | 2.02 | 7.64 | 3.58 | 4.64 | 2.20 | 3.86 | 36.91 | 1.87 | 5.12 | 2.54 | 9.02 |
| (4)-(6) | 4.70 | 51.91 | 2.48 | 5.78 | 3.77 | 9.52 | 4.39 | 5.41 | 9.83 | 2.97 | 5.87 | 2.42 | 11.12 | 4.08 |
| (7)-(9) | 2.97 | 37.24 | 2.45 | 4.91 | 2.83 | 5.67 | 3.08 | 4.58 | 4.05 | 2.21 | 5.01 | 2.70 | 5.56 | 2.60 |
| (10)-(12) | 5.88 | 6.43 | 4.74 | 4.29 | 5.51 | 4.24 | 6.26 | 4.35 | 4.13 | 10.81 | 3.43 | 5.41 | 4.66 | 6.74 |
| Sum | 18.18 | 97.83 | 14.69 | 17.00 | 19.75 | 23.01 | 18.37 | 16.54 | 21.87 | 52.90 | 16.18 | 15.65 | 23.88 | 22.44 |


of the summation of the network queues. Additional experiments are needed to clarify the optimal frequency for different networks and demand scenarios.

## ACKNOWLEDGMENTS

This research was funded primarily by the California Department of Transportation under the Connected Corridors program. S. A. Fayazi was sponsored in part by the National Science Foundation during his visit to the University of California, Berkeley. The authors thank Gabriel Gomes and Alex Kurzhanskiy for constructive discussions and useful comments. The authors also are grateful to Dongyan Su for providing the processed NGSIM data.

## REFERENCES

1. Mirchandani, P., and L. Head. A Real-Time Traffic Signal Control System: Architecture, Algorithms, and Analysis. Transportation Research Part C, Vol. 9, No. 6, 2001, pp. 415-432.
2. Papageorgiou, M., C. Diakaki, V. Dinopoulou, A. Kotsialos, and Y. Wang. Review of Road Traffic Control Strategies. Proceedings of the IEEE, Vol. 91, No. 12, 2003, pp. 2043-2067.
3. Hunt, P., D. Robertson, R. Bretherton, and M. Royle. The SCOOT On-line Traffic Signal Optimization Technique. Traffic Engineering and Control, Vol. 23, 1982, pp. 190-192.
4. Lowrie, P. SCATS: The Sydney Co-ordinated Adaptive Traffic System: Principles, Methodology, Algorithms. Proc., IEEE International Conference on Road Traffic Signalling, London, 1982, pp. 67-70.
5. Gartner, N. H. OPAC: A Demand-Responsive Strategy for Traffic Signal Control. In Transportation Research Record 906, TRB, National Research Council, Washington, D.C., 1983, pp. 75-84.
6. Farges, J., J. Henry, and J. Tufal. The PRODYN Real-Time Traffic Algorithm. Proc., 4th IFAC Symposium on Transportation Systems, Baden, Germany, 1983, pp. 307-312.
7. Mirchandani, P., and L. Head. A Real-Time Traffic Signal Control System: Architecture, Algorithms, and Analysis. Proc., TRISTAN III, Vol. 2, San Juan, Puerto Rico, 1998.
8. Diakaki, C., M. Papageorgiou, and K. Aboudolas. A Multivariable Regulator Approach to Traffic-Responsive Network-Wide Signal Control. Control Engineering Practice, Vol. 10, 2002, pp. 183-195.
9. Kosmatopoulos, E., M. Papageorgiou, C. Bielefeldt, V. Dinopoulou, R. Morris, J. Mueck, A. Richards, and F. Weichenmeier. International Comparative Field Evaluation of a Traffic-Responsive Signal Control Strategy in Three Cities. Transportation Research Part A, Vol. 40, No. 5, 2006, pp. 399-413.
10. Lindley, J. Applying Systems Engineering to Implementation of Adaptive Signal Control Technology. Proc., 19th ITS World Congress, Vienna, Austria, 2012.
11. Tassiulas, L., and A. Ephremides. Stability Properties of Constrained Queuing Systems and Scheduling Policies for Maximum Throughput in Multihop Radio Networks. IEEE Transactions on Automatic Control, Vol. 37, No. 12, 1992, pp. 1936-1948.
12. Dai, J., and W. Lin. Maximum Pressure Policies in Stochastic Processing Networks. Operations Research, Vol. 53, No. 2, 2005, pp. 197-218.
13. NGSIM: The Next Generation SIMulation Community. FHWA, U.S. Department of Transportation, 2006. www.ngsim.fhwa.dot.gov.
14. Varaiya, P. The Max-Pressure Controller for Arbitrary Networks of Signalized Intersections. In Advances in Dynamic Network Modeling in Complex Transportation Systems (S. V. Ukkusuri and K. Ozbay, eds.). Springer, New York, 2013, pp. 27-66.
15. Gazis, D. C., and R. B. Potts. The Oversaturated Intersection. Proc., 2nd International Symposium on Traffic Theory, London, 1963, pp. 221-237.
16. Aboudolas, K., M. Papageorgiou, and E. Kosmatopoulos. Store-and-Forward Based Methods for the Signal Control Problem in Large-Scale Congested Urban Road Networks. Transportation Research Part C, Vol. 17, No. 2, 2009, pp. 163-174.
17. Aboudolas, K., M. Papageorgiou, A. Kouvelas, and E. Kosmatopoulos. A Rolling-Horizon Quadratic-Programming Approach to the Signal Control Problem in Large-Scale Congested Urban Road Networks. Transportation Research Part C, Vol. 18, No. 5, 2010, pp. 680-694.

The Traffic Flow Theory and Characteristics Committee peer-reviewed this paper.


[^0]:    A. Kouvelas and J. Lioris, Partners for Advanced Transportation Technology, 2105 Bancroft Way, Suite 300, and P. Varaiya, Department of Electrical Engineering and Computer Science, University of California, 271M Cory Hall, Berkeley, CA 94720-3830. S. A. Fayazi, Department of Mechanical Engineering, Clemson University, 138 Fluor Daniel Building, Clemson, SC 29634. Corresponding author: A. Kouvelas, kouvelas@berkeley.edu.

    Transportation Research Record: Journal of the Transportation Research Board, No. 2421, Transportation Research Board of the National Academies, Washington, D.C., 2014, pp. 133-141.
    DOI: 10.3141/2421-15

