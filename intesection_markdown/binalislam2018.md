# Minimizing energy consumption from connected signalized intersections by reinforcement learning 

S.M.A. Bin Al Islam<br>Washington State University<br>Pullman, WA, United States<br>smabinal.islam@wsu.edu

H M Abdul Aziz (Corresponding Author)<br>Oak Ridge National Laboratory<br>Oak Ridge, TN, United States<br>aziz.husain.nexus@gmail.com, azizh@ornl.gov

Hong Wang<br>Pacific Northwest National Laboratory<br>Richland, WA, USA<br>hong.wang@pnnl.gov

Stanley E. Young<br>National Renewable Energy Laboratory<br>Golden, CO, USA<br>stanely.young@nrel.gov


#### Abstract

Explicit energy minimization objectives are often discouraged in signal optimization algorithms due to its negative impact on mobility performance. One potential direction to solve this problem is to provide a balanced objective function to achieve desired mobility with minimized energy consumption. This research developed a reinforcement learning (RL) based control with reward functions considering energy and mobility in a joint manner-a penalty function is introduced for number of stops. Further, we proposed a clustering-based technique to make the state-space finite which is critical for a tractable implementation of the RL algorithm. We implemented the algorithm in a calibrated NG-SIM network within a traffic micro-simulator-PTV VISSIM. With sole focus on energy, we report 47\% reduction in energy consumption when compared with existing signal control schemes, however causing a 65.6\% increase in system travel time. In contrast, the control strategy focusing on energy minimization with penalty for stops yields 6.7\% reduction in energy consumption with 27\% increase in system travel time. The developed RL algorithm with a flexible penalty function in the reward will achieve desired energy goals for a network of signalized intersections without compromising on the mobility performance.


Disclaimer: This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes. The Department of Energy will provide public access to these results of federally sponsored research in accordance with the DOE Public Access Plan(http://energy.gov/downloads/doe-public-access-plan

Index Terms-Reinforcement learning, fuel consumption, energy minimization, connected vehicles, traffic state observability.

## I. Motivation and Background

Suboptimal signal control at urban intersections can lead to significant energy consumption due to inefficient acceleration profile, idling, and frequent stop-go patterns. With a few exceptions [4], [13], [28], most signal control optimization algorithms focus on control delay, throughput, stops, and progression band when coordination is a priority. The energy aspects are often realized as benefits from optimizing signals rahter than a key objective. With advanced powertrains and electrification of the transportation networks, it is likely that energy consumption will get higher priority and will be needed to be an integral part of the signal control optimization. This research develops a machine learning based traffic control algorithm that explicitly accounts for energy consumption goal near signalized intersections. Further, a trade-off between mobility and energy performance is anticipated when we optimize energy consumption in an exclusive manner. To address, we have proposed multi-reward function integrating mobility and energy in the reinforcement learning (RL) algorithm. We leverage the data availability in a connected and automated transportation networks to develop a reinforcement learning based signal control algorithm.

Connected and automated environment provides an unprecedented environment for traffic state observability in realtime and the connectivity among vehicles and infrastructure components such as signal controllers allow the development of data-driven traffic flow control schemes. Accordingly, reinforcement learning (RL) based algorithms can be developed where the signal controllers learn to optimize over time through observing the transition of traffic states resulting from exploring and exploiting controller settings such as adjusting phase sequences and green durations. The stochastic nature of traffic flow in a transportation network makes it particularly suitable for RL-based approach where the solution technique does not need any prior information on the system. Compared to actuated and adaptive control schemes, the solutions from a RL-based technique can be theoretically proven to be optimal [7], [29]. Further, the RL approach is less computationally intensive and more resilient to traffic demand distribution compared with both exact optimization and adaptive control schemes. In addition, the controllers continue to learn as new traffic states are being realized in the system and keep improving the decision-making process [1], [3], [7]. However, RL-based techniques suffer from the curse of dimensionality as the number of traffic states grow exponentially in a real-world transportation network [1] and often restricts the analysis to a
limited sized network.
This research aims to develop and implement a reinforcement-learning based control with explicit energy consumption objectives with the following aspects in mind:

- The trade-off between mobility and energy objectiveshow to provide a balanced reward function within the context of an RL technique,
- Tractability of the state-space in a traffic environment,
- How can we levarge data in a connected-automated traffic environment to develop control schemes?

## II. Related Works

Acknowledging the vast literature on signal control optimization reearch we limit our scope to only energy focused control algorithms with RL-based approaches. Existing studies report several directions on minimizing energy consumption in signalized intersections through longitudinal control of approaching vehicles, and signal settings adjustments. With prior information on signal settings, the speed and acceleration profile of a vehicle can be optimized to cut down energy consumption [4], [8], [17]. Vehicles near the intersection and the signal controller can be jointly optimized through a unified framework to keep an energy-optimal speed profile [11], [30], [34]. Most studies have focused to find a smooth speed and acceleration rate to pass through intersections with minimal stops so that the energy benefits can be maximized without integrating an explicit energy consumption objective. A few exceptions include rule-based control with fuel consumption and emissions being integrated in a performance index function [12], [15], mathematical programs [13], simulation-based optimization model [20], [28], stochastic optimization [15]. For a comprehensive review, the readers are referred to [2], [23]-[25].

Numerous studies have applied RL-based techniques to solve signal control problems. [14], [16], [35] provide comprehensive review of the RL-based control studuies for urban signalized intersections. However, with fuel or energy consumption minimization goals, only a few studies [36], [38] applied RL-based algorithms and mostly used indirect reward functions such as number of stops and control delay to demonstrate energy benefits [3], [37].

With these gaps/limitations in the existing literature, our goals include:

1) To integrate an explicit energy-consumption based reward function (section III-C2),
2) To develop of a multi-reward function balancing energy and mobility (section III-C3),
3) To provide a tractable RL-algorithm with finite statespace in a connected vehicle (CV) environment(section III-A).

## III. Reinforcement learning-based Control: Methodology

Data rich environment with CVs provides an excellent avenue for executing machine learning based traffic control [5], [32]. RL-based techniques are well suited for dynamic environment like the road traffic networks. A major advantage can be gained in terms of computational complexity because no optimization is necessary in real-time. Traffic signal control as modeled as an Markov-Decision-Process (MDP) and solved by an RL technique in this research. The traffic network and controllers represent the environment and agents respectively. Each agent takes an action by activating a signal phase at each decision timestep. As such, the agent directly influences the transitions in traffic states. An RL algorithm will find the optimal policy that maximizes rewards for the system. RL algorithms can find solutions that can be proven optimal asymptotically [33], [37]. An RL-based algorithm requires essential components-state, action, and reward-to be defined specific to the problem at hand. This research proposes a decentralized architecture where each agent capable of controlling the traffic signal individually without any central supervising agent. Using vehicle to infrastructure (V2I) communication, an agent equipped with roadside unit (RSU) collects all the basic safety messages (BSM) from approaching equipped vehicles. Next, the agent collects information about the traffic states of neighboring intersections using infrastructure to infrastructure (I2I) communication. Finally, the agent determines state, action and rewards of the proposed RL algorithm. The next few subsections will define and describe these components in detail.

## A. State of the system

In a multi-agent system architecture, because of the decentralized control strategies, agents have a limited view of their surroundings. As a result, all the adjacent agents communicate back and forth to ensure the improvement in network-wide performance. At any step, the state of the system is represented by the queuing state of all the movements in an intersection plus the incoming and outgoing movements that send and receive vehicles to that intersection. For instance, as shown in figure 1, north-bound through (NBT) movement of intersection $n$ receives vehicles from east bound right (EBR), north-bound through (NBT) and west-bound left (WBL) movements of intersection $n-1$. Similarly, this movement sends vehicles to north-bound through (NBT) and west-bound right (WBR) movement of intersection $n+1$. States corresponding to left turn movements (i.e., north and south bound left) and source link movements (i.e., east and west bound through) of the intersection $n$ are adjusted by normalizing incoming vehicle flow to the saturated incoming flow.

1) Queuing state as Normalized-stopped-vehicles: At each decision period, the number of vehicles that stopped in an approaching movement was determined and further normalized by the length of the approach. We introduce the concept of Normalized-stopped-vehicle to make approaches with different length comparable. Traditional concept of queue stops does not account for the length of the movement. For instance, a 1000 ft movement with 30 queue stops is less congested than a 300 ft movement with same number of queue stops. Thus,

![](https://cdn.mathpix.com/cropped/a6702d18-1a47-4d40-b114-ca87fae3e04c-3.jpg?height=305&width=898&top_left_y=180&top_left_x=163)
Fig. 1. All the states corresponding in an intersection are presented with different colors. For instance, states corresponding to NBT and SBT are represented by red and black arrows respectively.

the Normalized-stopped-vehicle for a movement $i$ at time $t$ in an intersection $n, \psi_{i}^{t, n}$, can be written as:

$$
\psi_{i}^{t, n}=\frac{q_{i}^{t, n}}{L_{i}}
$$

Where $q_{i}^{t, n}$ : Number of vehicle stopped in a movement $i$ at time $t$ in an intersection $n$; and $L_{i}$ : Length of a movement $i$ such as the length of a left-turn pocket. It can be seen that $\psi_{i}^{t, n}$ is continuous in nature. The simplest way to solve a continuous state MDP is to discretize the states into finite space [7], [29]. We applied single dimensional $k$-means clustering algorithm to discretize continuous states. This method involves discretizing a state into predefined number of clusters to minimize withincluster sum of squares (WSS) from each element to its corresponding cluster mean [31]. The total WSS measures the compactness of the clustering; thus, the smallest value is preferable. The algorithm requires the number of clusters as an input. Finding the appropriate number of clusters for a given variable is generally a trial-and-error process [21]. We used WSS values to choose reasonable number of clusters with a preference to smaller WSS value.

## B. Action-selection

At each time, a signal controller agent takes an actioneither terminate or continue the existing phase till the next step. During training phase, an agent randomly selected a phase and calculated rewards. However, during the implementation, in the context of RL in traffic signal control, phase selection strategy involves an art of balancing the exploration and exploitation trade-off meaningfully. The selecting action by the signal controller can be either entirely greedy i.e. selecting the action with the maximal reward or exploratory by selecting random phases with pre-assigned probabilities. During exploration-exploitation suggested by [29], we used $\epsilon$-greedy method for selecting an action.

## C. Reward-functions

The reward function considered in this research have two components: a) control delay, and b) energy consumptions of all the vehicles in an intersection.

- Control delay: This delay is directly caused by the traffic controller and is approximately equal to time-in-queue delay plus the acceleration-deceleration delay component.

In this research, control delay was determined by summing up the difference between the time a vehicle spent and the expected travel time at free flow speed.

- Energy consumption: We follow Vehicle-Specific-Power(VSP) based approach that quantifies instantaneous power per unit mass of the vehicle as function of instantaneous speed, acceleration, aerodynamics, grade, and physics-based factors [6], [10], [26]. VSP can explain the power requirement from fundamental kinematics and also proven to be consistent with emissions and fuel consumptions measures from sensors in real-world scenarios. VSP parameters differ for vehicle classes: Light duty, heavy duty, hybrid, hybrid-electric, and so on. With standard parameters and coefficients in equation, the VSP for an LDV is computed as:
$$
V S P(L D V)=V[1.1 a+9.81 \Theta+0.132]+0.000302 V^{3}
$$
Where $m$ : Vehicle mass, $V$ : Vehicle speed, $a$ : Vehicle acceleration, and $\Theta$ : Road grade. The power requirement can be converted into fuel requirement with heat-content computation and brake-thermal, average drive train efficiency values [18], [27].
We have implemented three different reward functions to examine the trade-off between energy and mobility. Optimizing only energy may lead to higher delay which may become unacceptable. Therefore, we propose a reward function that focuses on energy minimization with a penalty for the delay so that we achieve a system state which would do better in terms of energy minimization compared to a delay minimization based control. At the same time, the delay will not be unacceptably high and the system operator can choose the trade-off through a selection of weights in the reward function.
1) Reward function: minimizing delay: The reward is calculated by the total control delay incurred between successive decision points by vehicles in the queues of all the approaches in an intersection. As such, the reward function for an intersection-level agent, $n$ can be written as:
$$
R_{D}=\tilde{D}_{n}^{t}=\sum_{i \in n} \tilde{D}_{i}^{t}=\sum_{i \in n} \sum_{j \in i} D_{j}^{t}
$$
$\tilde{D}_{n}^{t}$ : Control delay of intersection, $n$ at time $t, \tilde{D}_{i}^{t}$ : Control delay of movement, $i$ at time $t, D_{j}^{t}$ : Control delay of vehicle, $j$ at time $t$.
2) Reward function: minimizing energy : The reward was calculated by the total energy consumed by vehicles of all the approaches in an intersection. The energy consumed by a running vehicle was calculated from the vehicle specific power (VSP) from 2. In order to consider total energy consumption in an intersection, VSP and fuel consumption during idling phase were converted to gallons per unit time. The reward function for an intersection-agent $n$ at time $t$ is expressed as:
$$
R_{E}=E_{n}^{t}=\sum_{i \in n} E_{i}^{t}=\alpha \sum_{i \in n}\left\{\sum_{j \in i} \Phi\left(V S P_{j}^{t}\right)+\sum_{j \in i} \tilde{E}_{j}\right\}
$$

Where $E_{n}^{t}$ :Energy consumption of agent $n$ at time $t, E_{i}^{t}$ : Energy consumption of movement, $i$ at $t, \Phi\left(V S P_{j}^{t}\right)$ : Fuel consumption as a function of VSP for vehicle, $j$ in a movement, $i$ at $t, \alpha$ : Conversion factor from VSP to fuel consumption $\tilde{E}_{j}$ : Fuel consumed by a vehicle $j$, during idling phase.
3) Reward function: minimizing energy with penalty for stops: In this signal control strategy, queue stops penalized the Q-learning objective, shaping the reward function to reduce unnecessary vehicle stops. An exponential penalty function $\Gamma$, is added to 4. As a result, the Q-learning objective penalizes more for higher number of stops in an intersection.

$$
R_{B}=R_{E}-\Gamma(k)
$$

Where $R_{B}$ : Balanced reward function, $\Gamma(k)$ : An exponential penalty as a function of number of stops $k$ in a movement, $i$ at time $t$. For instance, such penalty function can have a form,

$$
\Gamma(k)=A \times \gamma \times \exp (B \times k)
$$

We have used $A=23.5$ and $B=0.0486$ for experimental purposes. $\gamma$ is the weight for the penalty associated with stops (Also see section VI-C1).

## D. Algorithm

The proposed RL based signal control algorithm has three phases: training, exploration-exploitation and implementation phase. During the training phase, an agent observed the system, took random action and updated the state-action value through interacting with the CV environment. Balancing exploration and exploitation in a learning phase is important for long-term performance of the proposed algorithm. At the exploration-exploitation phase the authors implemented $\epsilon$ - greedy method. During the implementation period, the algorithm emphasized on taking entirely greedy action. Details of the Q-learning algorithm step can be found in [3], [29].

## IV. Data for RL algorithm implementation in a CV ENVIRONMENT

CV environment facilitates communication platform between vehicles, vehicle to infrastructure and infrastructure components through vehicle-to-vehicle (V2V), V2I and I2I communication. Using V2I communications, vehicles continuously broadcast their status, such as speed, acceleration, position to an agent (intersection controller) through BSM data. Using the shared information from CVs, an agent determined the number of vehicles stopped in a queue based on their speed and acceleration. Similarly, an agent can detect the entrance of a vehicle based on the reported position in BSM of the vehicle and estimate the normalized entry flow for left turn and the movements that are connected to source link. When a vehicle is detected at the upstream of a movement, an expected leaving time of the vehicle from movement was assigned for each vehicle. Thus, controlled delay was determined based on the difference between current time and expected leaving time of a vehicle from a movement. Similarly, based on the reported speed and acceleration in BSMs, fuel consumptions of vehicle can easily be determined. Figure 2 presents the data flow in the CV environment.

![](https://cdn.mathpix.com/cropped/a6702d18-1a47-4d40-b114-ca87fae3e04c-4.jpg?height=430&width=881&top_left_y=174&top_left_x=1089)
Fig. 2. Data flow in a Connected-Vehicle environment for RL

## V. Implementation in a simulated environment

This paper developed and evaluated the signal control strategy of the study area in a microsimulation software, VISSIM [22], which based on a psycho-physical car following model for longitudinal vehicle movement. The network is calibrated using the Lankershim Boulevrad, CA data from NGSIM.

## A. Calibration and network preparation

This research follows the methodology proposed in [19] for the calibration process. A random sample considering all the controllable parameters in VISSIM was created based on Latin Hypercube sampling technique [9]. We selected trip travel time of three major origin-destination pairs that covers approximately 70\% of total trips in the study area. The signal control system based on RL was coded in Java inter-acting with VISSIM through the Component Object Model (COM) interface.

For simplicity, we assume internal combustion engines with gasoline vehicles for the demonstration purpose. Given all parameters, we can also simulate and estimate energy consumptions for a fleet of mixed vehicles using 2 and corresponding equations for advanced fuel vehicles. The energy consumptions are also converted into gallons of fuels using standard factors [18].

## B. Training and exploration-exploitation

At first, the calibrated Lankershim Boulevard arterial was trained for 450 times using different random seeds. The simulation period for each of these runs was 15 minutes. The rewards and other performance metrics were obtained directly from VISSIM. Finally, the Q-table was updated after the implementation of the random action. After initial training of the Q-table, the authors explored the network for additional 50 runs, each having 15 minutes simulation period. Finally, the Q-table was updated based on the rewards obtained from VISSIM.

## VI. Results and discussions

The authors conducted statistical tests to justify the findings using a sample of 33 VISSIM simulation instances each with a different random seed. Table I shows summary of performance metrics for the case study network. Percentage of changes

TABLE I
System performance: Change in percentage-Negative sign: Decrease, Positive sign : Increase-Relative to the base case
| Performance Metric |  | Control Strategies |  |
| :--- | :--- | :--- | :--- |
|  | Delay Minimize | Energy Minimize | Energy-Min with Penalty for Stops |
| Total queue time | -16.8\% | 166.9\% | 50.8\% |
| Average queue time | -16.7\% | 245.2\% | 51.1\% |
| System travel time | -2.0\% | 65.6\% | 27\% |
| Energy consumption | 10.5\% | -47.0\% | -6.7\% |


of the mean value of performance metrics for all proposed signal control strategies compared to the current signal control strategy in Lankershim Boulevard are reported.

## A. Control Strategy-Minimize Delay

We observe improvement in total and average queue time, system travel time, and total number of completed trips. However, the delay for all completed trips did not improve compared to the base case. Nevertheless, we found a improving trend with more training sets and accordingly, it is expected that average delay will be converged and show improvement in terms of delay for all vehicles in the network.

## B. Control Strategy: Minimize Energy

When the reward function solely focuses on energy consumption of a vehicle, the stopping phase yields less energy consumption compared to the cruising phase, and becomes the preferable state for signal controllers. Therefore, network-wide energy consumptions in the proposed strategy was the lowest among other control strategies. The energy consumption was reduced by 47\% compared with the base case. However, as shown in table I, this strategy yielded excessively higher delay and system travel time, and undesired traffic condition. For instance, the number of completed trips is reduced by 49\% and the average travel time is increased by 57.12\% compared with the base case.

## C. Control Strategy- Minimize Energy with Penalty for Stops

To achieve a balance between energy and mobility, we introduce a penalty function in energy minimization strategy (see III-C3). The penalty function was added to the energy consumption objective for stopped vehicles in an intersection. As a result, all the performance measures were improved except energy consumption compared to energy-minimize strategy (see III-C2). Compared to a 47\%, we obtained a 6.7\% reduction from the base case. The introduced penalty function ensured minimal stopped delay of the vehicle. As such, this strategy processed reasonable number of trips with reduced average delay compared to strategy focusing solely on energy.

1) Trade-off exploration: Finally, we compared total travel time and number of completed trips with total energy consumption in the network for different value of $\gamma$ in the penalty function 6. Fig. 3 shows that imposing higher penalty

![](https://cdn.mathpix.com/cropped/a6702d18-1a47-4d40-b114-ca87fae3e04c-5.jpg?height=260&width=786&top_left_y=178&top_left_x=1126)
Fig. 3. Trade-off between travel time and energy for different values of $\gamma$ in 6. Mean performance measures of 30 simulation runs and standard error bars are shown corresponding to $\gamma$

on number of stops will reduce total travel time. In contrast, total energy consumption in the network will increase as we increase the value of $\gamma$. Total travel time and number of completed trips improve significantly after $\gamma=0.2$. For instance, number of completed trips increased by 118\% and system travel time reduced by 43\% when the value of $\gamma$ increased from 0.2 to 0.3.

## VII. Conclusion and Future directions

The key contributions of this research are as follows: (a) A reinforcement learning algorithm to minimize energy consumption from signalized intersections leveraging data availability in a CV environment, (b) A clustering technique to produce a set of discretized states to make the state-space finite for tractable implementation, (c) A multi-reward learning approach to account for the trade-off between mobility and energy performances at signalized intersections

With the balanced reward function accounting for energy and mobility (see III-C3), it is possible to achieve desired traffic state with minimal energy and maximized mobility. The data-rich CV environment provides the suitable platform to implement learning-based algorithms that would be well suited for a stochastic traffic environment. The ability to learn from transitions in traffic states makes RL-based control more flexible and efficient compared to existing fixed, semiadaptive, and actuated control schemes.

## A. Key Findings

- The signal control strategy to minimize energy consumption yields the lowest amount of energy consumption compared to other strategies; however; negatively impacts other mobility performance measures. As such, only minimization of fuel consumption does not seem to be a reliable objective function in order to get reasonable performance from the network.
- Minimizing fuel consumption while penalizing for stopped delay yields better network-wide performance compared to the signal control strategy with energy minimization objective only. This is a reliable objective function while considering both mobility and energy for a network of signalized intersections.
- In order to get a better performance in delay and travel time, signal control system while considering control delay needs to be further trained.

## VIII. Acknowledgments

This research is funded by the Energy Efficient Mobility Systems (EEMS) program of the Vehicles Technologies Office of the Department of Energy, United States. The authors are grateful for the guidance and suggestions from the DOE program managers.

## References

[1] Baher Abdulhai, Rob Pringle, and Grigoris J. Karakoulas. Reinforcement learning for true adaptive traffic signal control. Journal of Transportation Engineering, 129(3):278-285, 2003.
[2] H M Abdul Aziz, Hong Wang, Stanley E. Young, Joshua Sperling, and John Beck. Synthesis study on transitions in signal infrastructure and control algorithms for connected and automated transportation. Technical report, Oak Ridge National Laboratory (ORNL), Oak Ridge, TN (United States), 2017.
[3] H M Abdul Aziz, Feng Zhu, and Satish V Ukkusuri. Learningbased traffic signal control algorithms with neighborhood information sharing: An application for sustainable mobility. Journal of Intelligent Transportation Systems, pages 1-13, 2017.
[4] Matthew Barth, Sindhura Mandava, Kanok Boriboonsomsin, and Haitao Xia. Dynamic ECO-driving for arterial corridors. In Integrated and Sustainable Transportation System (FISTS), 2011 IEEE Forum on, pages 182-188, 2011.
[5] Samah El-Tantawy, Baher Abdulhai, and Hossam Abdelgawad. Multiagent reinforcement learning for integrated network of adaptive traffic signal controllers (MARLIN-ATSC): methodology and large-scale application on downtown Toronto. IEEE Transactions on Intelligent Transportation Systems, 14(3):1140-1150, 2013.
[6] R Giannelli, Ek Nam, K Helmer, T Younglove, and G.Scora M.Barth. Heavy-duty diesel vehicle fuel consumption modeling based on road load and power train parameters. SAE World ... , page 13, 2005.
[7] Abhijit Gosavi. Simulation-Based Optimization: Parametric Optimization Techniques \& Reinforcement Learning. Springer, New York, 2015.
[8] Xiaozheng He, Henry X. Liu, and Xiaobo Liu. Optimal vehicle speed trajectory on a signalized arterial with consideration of queue. Transportation Research Part C: Emerging Technologies, 61:106-120, 2015.
[9] Ronald L Iman. Latin hypercube sampling. Encyclopedia of quantitative risk analysis and assessment, 2008.
[10] J. L. Jimenez-Palacios. Understanding and quantifying Motor vehicle emissions with vehicle specific power and TILDAS remote sensing. PhD thesis, MIT, Cambridge, MA., 1999.
[11] Hojin Jung, Saerona Choi, Byungkyu Brian Park, Haengju Lee, and Sang Hyuk Son. Bi-level optimization for eco-traffic signal system. In Connected Vehicles and Expo (ICCVE), 2016 International Conference on, pages 29-35, 2016.
[12] Xiugang Li, Guoqiang Li, Su Seng Pang, Xiaoguang Yang, and Jialin Tian. Signal timing of intersections using integrated optimization of traffic quality, emissions and fuel consumption: A note. Transportation Research Part D: Transport and Environment, 9(5):401-407, 2004.
[13] Tsai-Yun Liao. A fuel-based signal optimization model. Transportation Research Part D: Transport and Environment, 23:1-8, 2013.
[14] Zhiyong Liu. A survey of intelligence methods in urban traffic signal control. IJCSNS International Journal of Computer Science and Network Security, 7(7):105-112, 2007.
[15] Xiaoliang Ma, Junchen Jin, and Wei Lei. Multi-criteria analysis of optimal signal plans using microscopic traffic models. Transportation Research Part D: Transport and Environment, 32:1-14, 2014.
[16] Patrick Mannion, Jim Duggan, and Enda Howley. An experimental review of reinforcement learning algorithms for adaptive traffic signal control. In Autonomic Road Transport Support Systems, pages 47-66. Springer, 2016.
[17] Felicitas Mensing, Rochdi Trigui, and Eric Bideaux. Vehicle trajectory optimization for application in ECO-driving. In Vehicle Power and Propulsion Conference (VPPC), 2011 IEEE, pages 1-6, 2011.
[18] NAP Report. Assessment of Fuel Economy Technologies for Light-Duty Vehicles. Technical report, National Research Council of the National Academies, Washington, D.C., 2011.
[19] Byungkyu Park, Jongsun Won, Michael A Perfater, and Others. Microscopic simulation model calibration and validation handbook. Technical report, 2006.
[20] Byungkyu Park, Ilsoo Yun, and Kyoungho Ahn. Stochastic optimization for sustainable traffic signal control. International Journal of Sustainable Transportation, 3(4):263-284, 2009.
[21] Duc Truong Pham, Stefan S Dimov, and Chi D Nguyen. Selection of K in K-means clustering. Proceedings of the Institution of Mechanical Engineers, Part C: Journal of Mechanical Engineering Science, 219(1):103-119, 2005.
[22] Vision PTV America. 5.4 user manual. PTV Vision, 2012.
[23] Xuewei Qi, Matthew J Barth, Guoyuan Wu, Kanok Boriboonsomsin, and Peng Wang. Energy impact of connected eco-driving on electric vehicles. In Road Vehicle Automation 4, pages 97-111. Springer, 2018.
[24] Xuewei Qi, Peng Wang, Guoyuan Wu, Kanok Boriboonsomsin, and Matthew J Barth. Energy and mobility benefits from connected ecodriving for electric vehicles. In Intelligent Transportation Systems (ITSC), 2017 IEEE 20th International Conference on, pages 1-6. IEEE, 2017.
[25] Alexander Skabardonis, Steven Shladover, Wei-bin Zhang, and Others. Advanced Traffic Signal Control Algorithms. California PATH Program, UCB-ITS-PRR-2014-04, 2013.
[26] Guohua Song and Lei Yu. Characteristics of Low-Speed Vehicle-Specific Power Distributions on Urban Restricted-Access Roadways in Beijing. Transportation Research Record: Journal of the Transportation Research Board, 2233:90-98, 2011.
[27] Gino Sovran and Dwight Blaser. Quantifying the Potential Impacts of Regenerative Braking on a Vehicle ' s Tractive-Fuel Consumption for the U . S ., European , and Japanese Driving Schedules. SAE Technical Paper Series, 1(2006-01-0664), 2006.
[28] Aleksandar Stevanovic, Jelka Stevanovic, Kai Zhang, and Stuart Batterman. Optimizing traffic control to reduce fuel consumption and vehicular emissions: Integrated approach with VISSIM, CMEM, and VISGAOST. Transportation Research Record: Journal of the transportation research board, (2128):105-113, 2009.
[29] Richard S Sutton and Andrew G Barto. Reinforcement learning: An introduction (Second Edition). The MIT Press, Cambridge, Massachusetts, 2018.
[30] Tessa Tielert, Moritz Killat, Hannes Hartenstein, Raphael Luz, Stefan Hausberger, and Thomas Benz. The impact of traffic-light-to-vehicle communication on fuel consumption and emissions. In Internet of Things (IOT), 2010, pages 1-8, 2010.
[31] Haizhou Wang and Mingzhou Song. Ckmeans. 1d. dp: optimal k-means clustering in one dimension by dynamic programming. The $R$ journal, 3(2):29, 2011.
[32] M. Wiering, J. Vreeken, J. van Veenen, and A. Koopman. Simulation and optimization of traffic in a city. Intelligent Vehicles Symposium, 2004 IEEE, pages 453-458, 2004.
[33] M A Wiering. Multi-agent reinforcement learning for traffic light control. In Machine Learning: Proceedings of the Seventeenth International Conference (ICML'2000), pages 1151-1158, 2000.
[34] Chunhui Yu, Yiheng Feng, Henry X Liu, Wanjing Ma, and Xiaoguang Yang. Integrated optimization of traffic signals and vehicle trajectories at isolated urban intersections. Transportation Research Part B: Methodological, 112:89-112, jun 2018.
[35] Dongbin Zhao, Yujie Dai, and Zhen Zhang. Computational intelligence in urban traffic signal control: A survey. IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), 42(4):485-494, 2012.
[36] Pu Zhao, Yanzhi Wang, Naehyuck Chang, Qi Zhu, and Xue Lin. A deep reinforcement learning framework for optimizing fuel economy of hybrid electric vehicles. In Design Automation Conference (ASP-DAC), 2018 23rd Asia and South Pacific, pages 196-202. IEEE, 2018.
[37] Feng Zhu, H M Abdul Aziz, Xinwu Qian, and Satish V Ukkusuri. A junction-tree based learning algorithm to optimize network wide traffic control: A coordinated multi-agent framework. Transportation Research Part C: Emerging Technologies, 58:487-501, 2015.
[38] Yuan Zou, Teng Liu, Dexing Liu, and Fengchun Sun. Reinforcement learning-based real-time energy management for a hybrid tracked vehicle. Applied Energy, 171:372-382, 2016.
