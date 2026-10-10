# Game Theory Algorithm for Intersection-based Cooperative Adaptive Cruise Control (CACC) Systems 

Ismail H. Zohdy and Hesham Rakha, Member, IEEE


#### Abstract

The paper develops a heuristic optimization algorithm for automated vehicles (equipped with cooperative adaptive cruise control CACC systems) at uncontrolled intersections using a game theory framework. The proposed system models the automated vehicles as reactive agents interacting and collaborating with the intersection controller (manager agent) to minimize the total delay. The system is evaluated using a case study considering two different intersection control scenarios: a four-way stop control and the proposed intersection controller framework. In both scenarios, four automated vehicles (a single vehicle per approach) was simulated using a Monte Carlo simulation that was repeated 1000 times. The results show that the proposed system reduces the total delay relative to a traditional stop control by 35 seconds on average, which corresponds to an approximately 70 percent reduction in the total delay.


## I. Introduction

Every year in the United States, about six million traffic accidents occur on US roads where more than 90 percent of these accidents are a result of human distraction and/or misjudgment [1]. Consequently, the idea of an automated driving environment has been studied for decades to reduce the number of crashes and enhance the transportation system mobility.

In one of the early automation trials, the USDOT established the Automated Highway System (AHS) program for the purpose of increasing the efficiency (reducing delay and enhancing safety) of traffic networks using automated vehicle control [2]. Although the AHS program was not able to continue, it is considered the basis of many driver assistant systems in the market today.
After the development and deployment of the USDOT Connected Vehicle initiative [3], the enhancement of the

[^0]current driver assistance systems has become an expected step towards achieving better mobility and safety. Accordingly, the concept of Cooperative Adaptive Cruise Control (CACC) systems has been introduced as an advanced generation for the traditional cruise control. In the CACC system, vehicles have the ability to sense and communicate with other vehicles through vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communication. After fusing all data sources, vehicles make decisions with regards to acceleration, deceleration, or maintaining their current speed. The basic idea of the system is to assist the driver by controlling the speed of the vehicle; however it leaves the maneuver responsibility to the driver.

It is anticipated in the future that many (or most) of the vehicles will be fully automated; thus the movements of these vehicles should be optimized. The new CACC concept is introduced to highways, sometimes in dedicated lanes, to reduce the gaps between vehicles using communication technology. However, a few research efforts have considered the use of CACC at intersections in order to enhance vehicle movement, reduce delay, and reduce fuel consumption levels.

## II. Literature Review

Very limited research efforts have studied the impact of advanced cruise control systems on intersection operations in comparison to the wealth of literature dedicated to highway operations. Most of the studies directly related on CACC at intersections have focused on fuel consumption and emissions impacts (e.g. [4]). There are a few research efforts focused on the impact of optimal speed advisory for drivers comparing to the design of the signal timing of the traffic signals [5, 6].

Regarding research efforts directly related to CACC applications, Malakorn and Park (2010) evaluated the performance of intelligent traffic signal control systems integrated with CACC systems to traditional intersection control [7]. The goal of this system was to reduce the environmental impacts of vehicles in the vicinity of intersections by minimizing vehicle acceleration levels. The procedure estimates vehicle emissions using the VT-Micromodel [8]. Under the connected vehicles (CV) environment, Lee and Park [9] created a Cooperative Vehicle Intersection

Control (CVIC) system that enables cooperation between vehicles and infrastructure for effective intersection operations and management.

In general, the literature related to CACC is limited; especially the studies of CACC capabilities at intersections. The CACC controller can better foresee problems, enabling the vehicle to be safer and faster in response to various stimuli. However, extensively exploring the CACC impact on delay and how it could be used as a tool for optimizing the movements of vehicles at intersections is limited to only a few researchers. It could be stated that none of the previous approaches used an explicit optimization algorithm for reducing delay (minimizing travel time) and in some cases it was simply expressed as functions of acceleration/deceleration levels.

## III. STUDY OBJECTIVE AND PAPER LAYOUT

The purpose of this study is to develop a heuristic optimization algorithm for controlling vehicle movements of vehicles equipped with CACC systems at uncontrolled intersections using "Game Theory Decision" field theory. The vehicles are modeled as agents interacting with the intersection controller (manager agent) and obeying the optimum decision made by the intersection controller. In other words, the vehicles collaborate in a form of a "Cooperative Game" with the controller installed at the intersection. The main principle of this research is to employ the communication technologies with advanced vehicle capabilities to replace the usual state-of-the-practice control systems at intersections (e.g. stop sign, yield signs, etc.).

In terms of the paper layout, initially a description of the proposed multi-agent system is presented. Subsequently, the built-in simulation process using game theory is presented and the testing of the optimization algorithm is then discussed. Finally, the conclusions of the paper and future research directions are discussed.

## IV. proposed multi-agent modeling layout

The capabilities of an intelligent agent makes it possible to control various types of vehicles with different driving behavior. For the case of automated vehicles, agent-based modeling is considered the most appropriate approach as was suggested in several literature sources [10, 11]. Here we propose the use of agent-based modeling of CACC-equipped vehicles as the agents have two main features: (1) they are at least to some extent capable of autonomous actions or decisions and (2) they are capable of interacting with other agents through cooperation, coordination and negotiation [12].

The proposed multi-agent system (MAS) consists of two types of agents: reactive agents (vehicles equipped by CACC) and a manager agent (intersection controller). The main idea of the proposed system is that the manager agent communicates with the reactive agents in the intersection study zone (ISZ) and determines the optimum movements for each reactive agent based on a "Game Theory Decision Framework". The ISZ is the zone area around the intersection where the reactive agents begin to exchange information with the manager agent. The ISZ in this research 200 m upstream of the intersection to ensure that vehicles have sufficient time to receive and respond to the information received.

The proposed layout for the MAS assumes that all agents in the ISZ are interacting, communicating and exchanging information for the common benefit using some form of communication (e.g. Dedicated Short Range Communication (DSRC)). The global benefit is defined as reducing the total delay while ensuring no vehicle collisions occur. The reason for modeling the collaboration between agents is to overcome any selfish behavior by any vehicle or in other words to seek the global benefit for all vehicles in the ISZ. Therefore, the main task for the manager agent is to determine the optimum speed for each reactive agent at each time step by processing the input data through a real-time simulation. The MAS layout consists of three main components for controlling the movements of reactive agents in the ISZ: Input, Data processing and Output.
The input data for the manager agent consists of: intersection characteristics, weather station input and reactive agent input. The intersection characteristics contain the speed limit of the intersection and number of lanes of each approach. The weather station provides the instantaneous weather condition to take into account the roadway surface condition (dry or wet) in simulating the reactive agent movements. At each time step, all reactive agents in the ISZ report their physical characteristics, current speed, location and acceleration to the manager agent. All input information is received by the manager agent then processed and optimized using a game theory decision process. For the purpose of this research, a simulation tool was developed using Matlab. Figure 1 illustrates the layout of the proposed CACC multi-agent system.

![](https://cdn.mathpix.com/cropped/de4ea8e0-afa7-4ed7-93ff-bf438d97fbbd-3.jpg?height=496&width=1439&top_left_y=196&top_left_x=327)
Figure 1: The layout of the proposed MAS for equipped vehicles at uncontrolled intersections

## V. proposed Real-Time Simulation for CACC-Equipped Vehicles

This section describes the state-of-art simulation test bed that was developed to model the intersection controller. The research presented here is considered a first step in developing a fully automated intersection vehicle controller. In general, the simulation algorithm computes the optimum location, speed and acceleration of vehicles to ensure that no conflicts occur while at the same time minimizing the total intersection delay each time step (e.g. 0.5 sec). The total delay is defined by the summation of the delay experienced by each vehicle at each time step.

The proposed software is considered as a novel tool for optimizing the movement of automated vehicles at intersections; however, it has some limitations and assumptions. First, we assume a market penetration of 100\% of CACC-equipped vehicles. Second, all drivers/vehicles in the ISZ are assumed to follow the recommendations made by the intersection controller to achieve the global profit. Last, only one speed profile, i.e. one vehicle (the most critical one), is adjusted (optimized) each time step.

It should be mentioned that the vehicle dynamics (acceleration and deceleration) models are part of the simulation software. The dynamics models take into account the tractive and resistance forces (referred to the literature [13]) acting on vehicles at each time step. Consequently, the simulation process reflects the physical characteristics (power of engine, mass, etc.) and the weather condition (wet or dry) affecting the movements of vehicles.

At each time step of simulation, the existing vehicles in the ISZ are determined and thereafter the built-in simulation uses a heuristic optimization process divided into two main stages. The stages are: 1) calculate the Conflict Zone Occupancy Time (CZOT) for each conflict area, 2) conduct a Game Theory Optimization, as will be explained in more detail in the following sub-sections.
A. Calculate the Conflict Zone Occupancy Time in Conflict Areas

A conflict point in the intersection is a point that can be occupied by two different crossing vehicles during the same time interval. We introduce the term Conflict Zone Occupancy Time (CZOT) in the optimization process. The CZOT is the time interval where the two intersecting vehicles will be occupying the same conflict area. The simulation software uses the input information to simulate the trajectory of the vehicles; therefore estimates the time needed to enter and leave the conflict zone. The simulation software assumes that all vehicles will accelerate to the maximum speed (if their speed is less than the maximum) as an "initial decision" to reduce the total travel time for each vehicle. If the estimated CZOT value is positive (>0), it is an indication that by accepting the initial decision for both intersecting vehicles, a collision would occur. Alternatively, if CZOT is equal to zero (or less) that means the intersecting vehicles will not be conflicting with each other and it is safe to accept the initial decision.

For illustrating purposes, for a four-legged intersection we would have four conflict zones (assuming on through traffic on each approach), as shown in Figure 2 (a). Consequently, the CZOT value for each conflict area, CZOT1, CZOT2, CZOT3 and CZOT4 can be computed. Thereafter, the CZOT plot is drawn as shown in Figure 2 (b) where each rectangle illustrates the conflict occupancy time for each vehicle. In the example, we can observe that CZOT1, CZOT2 and CZOT4 have positive values (i.e. there is a common time interval between the two intersecting vehicles). Consequently, we need to adjust the vehicle trajectories in order to avoid a collision with the intersecting vehicles. On the other hand, the CZOT3 value is equal to zero as the two intersecting vehicles occupy the conflict zone at different time intervals.

As mentioned before, the built-in simulation selects only one vehicle to modify its trajectory each time step (i.e. 0.5 second). Therefore the next step is to select the appropriate vehicle to adjust its trajectory.

![](https://cdn.mathpix.com/cropped/de4ea8e0-afa7-4ed7-93ff-bf438d97fbbd-4.jpg?height=1467&width=761&top_left_y=238&top_left_x=234)
Figure 2: Conflict Zone Occupancy Time (CZOT) output example

## B. Game Theory Optimization Process

Various models that incorporate concepts from Game Theory are described in many transportation related literature [14-17]. Interaction and collaboration are essential aspects in the dynamic multi-agent systems (MASs); consequently, game theory provides powerful tools for analyzing those types of transport systems.

A game of strategy is defined as the game where each player is trying to choose the best strategy to maximize the total benefit [18]. In cooperative games (one of the types of the strategy games), the pay-off (benefit) for each potential group can be obtained by the coalitional of its members (or players). The challenge of the cooperative game is to allocate the pay-off (benefit) among the players in some fairway. Consequently, collaborating with all CACC-equipped vehicles together with the intersection controller, using communication technology, could be formulated in a cooperative game framework. Defining a game requires identification of the players, their choices (strategies) and their objectives as will be described in the following section.

## VI. Elements of the Game (Describing a Game)

Game theory provides a framework for modeling interactions between groups of decision-makers when individual actions jointly determine the outcome [18]. The proposed cooperative game framework in this research is entitled: CACC-CG (Cooperative Adaptive Cruise Control - Cooperative Game). The CACC-CG represents the decision process of the built-in simulation software to optimize the movement of automated vehicles at intersections. The proposed CACC-CG is considered a decision process that is repeated at each time step of the simulation. The CACC-CG cooperative game consists of the following elements: players $(s)$, actions $(A)$, information $(I)$, strategies $(S)$, pay-offs $(U)$, outcomes ( $O$ ) and equilibrium ( $\pi$ ).

Each player's goal is to choice the best action in order to maximize his/her utility. The players in the CACC-CG are the manager agent and all reactive agents at each time step. Actions are the choices that each player can make. For the manager agent, the action is to select one reactive agent for optimizing its movement each time step while other vehicles maintain their current state until the next time step. Reactive agents have three possible actions: decelerate, accelerate or maintain their current speed. It is assumed the information set is available for all players during the game decision process. In other words, the information is symmetric and certain for all players using communication technology (DSRC).
The player's strategy is simply the set of actions that could provide the maximum profit. In other words, the action set includes all actions that minimize the total delay and ensure safe maneuvers for all agents at the intersection.

Furthermore, Pay-off is the expected benefit or utility that the player will receive after all players took their decisions and the game has been played. In the CACC-CG, the pay-off is determined based on the actions of the players and it is proposed to be formulated as a Utility function. It is assumed in this framework that the optimum decision taken by the players would be the action set that lead to the minimum utility function (conflict zone and delay minimization). Consequently, the players follow the maximin principle. The value of utility function depends on the distance remaining to the intersection relatively to the needed stopping sight distance for each vehicle. Generally, the utility value is considered as the summation of the total CZOT values and the total delay due to the actions of manager agent $(i)$ and any selected reactive agent $(j)$. However, if the distance remaining for a vehicle to the intersection is less than minimum stopping sight distance, its utility value is set to be an infinity value. In other words, if a vehicle does not have the option other than decelerating
to complete stop, this vehicle will not be a part of the optimization process as presented in Equation (1).

$$
U_{i, j}=\left\{\begin{array}{ll}
\sum_{p=1}^{P} C Z O T_{i, j}+\sum_{i=1}^{N} D_{i, j} & ; \text { if } X_{j}>S S D_{j} \\
\infty & ; \text { if } X_{j}<S S D_{j}
\end{array}\right\}
$$

Where, $i$ is the action taken by the manager agent; $j$ is the action taken by the reactive agent; $U_{i, j}$ is the utility value corresponding to the action set $(i, j), P$ is the total number of conflict points; $C Z O T_{i, j}$ is the conflict zone occupancy time value (explained previously) corresponding to the action set $(i, j) ; X j$ is the current distance to the intersection for vehicle $j ; S S D j$ is the minimum stopping sight distance to the intersection for vehicle $j ; N$ is the total number of reactive agents (vehicles) existed in the current time step; and $D_{i, j}$ is the delay value for each reactive agent also corresponding to the action set $(i, j)$.

Outcome is a set of resulted elements after the game is played out. Consequently, the outcome of the proposed game is simply: vehicle trajectories (acceleration, deceleration or constant speed) for a chosen vehicle that would lead to the least utility function.

For the equilibrium, once the players have settled on strategies that satisfy all them, this condition is called the Nash equilibrium (named after John Forbes Nash) [18]. Some literature defines simply the equilibrium as the best decision by the player given that the other players already made their decision[18].

In the general case, the proposed game CACC-CG consists of a sequence of turns that need not be all the same; therefore it could be taken as the type of "Extensive Form" games. This kind of games is best represented by a game tree. A game tree is a connected graph which contains no circuit. The game tree form of the CACC-CG is presented in Figure 3(a). One way to solve an extensive game is to convert it to a normal-form game. The normal form is a matrix, each column is defined by a strategy for player 1 and each row of which is labeled with a strategy for player 2 as shown in Figure 3(b).
In summary, the game is simply to form a pay-off table -as Figure 3(b)- for the intersection controller (manager agent) and the vehicles (reactive agents)in the ISZ at each time step. The pay-off table shows the utility matrix of each action combination between the manager agent and each reactive agent. Consequently, by choosing the minimum utility value the best choice for all players would be decided: "the maximin principle". In other words, the equilibrium status could be achieved at each time step by selecting the best action combination between players in the proposed cooperative game CACC-CG. Consequently, the outcome of the optimization process that would be an optimum decision (accelerate, decelerate or constant speed) for a selected vehicle and accordingly the vehicle would follow the optimum decision. The process of the proposed optimization framework is heuristically repeated at each time step till the end of simulation.

![](https://cdn.mathpix.com/cropped/de4ea8e0-afa7-4ed7-93ff-bf438d97fbbd-5.jpg?height=1128&width=816&top_left_y=286&top_left_x=1109)
Figure 3: The extensive form (game tree \& normal-form) for the CACC-CG proposed game

## VII. system testing

In order to test the proposed system, two different intersection control scenarios for a case study intersection are considered. The first scenario uses a four-way stop control system while the second scenario applies the proposed game theory intersection manager. The case study intersection consists of four single lane approaches, as in Figure 2 (a). Standard lane widths of 3.5 meters are considered with approach speed limits of 35 mph. For illustration purposes, we modeled a Toyota Prius 2010 model with an engine power of 134 Horse Power (Hp). This vehicle is similar to the tested vehicle in the Google Driverless experiment [19]. The study considered a single vehicle arrival on each approach considering the proposed intersection manager and an all-way stop controlled intersection. For both scenarios, the entrance time, speed, and acceleration of each vehicle were randomly generated. The system was then modeled considering a time step ( $\Delta \mathrm{t}$ ) of 0.5 s. The total delay was computed for each run considering the two intersection control scenarios. The total delay was computed for all four automated vehicles. This procedure was repeated 1000 times using a Monte Carlo simulation and the total delay time was recorded for each
simulation. Figure 4 shows the total delay variation for the 1000 simulations for both intersection control strategies.

The results demonstrate that the proposed framework is giving less total delay time comparing to the stop sign control scenario. The average total delay time for the proposed scenario is approximately 19 seconds and for the stop sign control is 54 seconds. Thus, for the case of only four crossing vehicles, the proposed system reduces the total delay more than the traditional stop control by 35 seconds on average and obviously the total delay reduction would enlarge by having more vehicles crossing the intersection.

![](https://cdn.mathpix.com/cropped/de4ea8e0-afa7-4ed7-93ff-bf438d97fbbd-6.jpg?height=578&width=799&top_left_y=675&top_left_x=189)
Figure 4: Total Delay comparison between Stop Sign control and proposed optimization control using game theory

## VIII. Conclusions and future work

The research presented in this paper developed an innovative algorithm for optimizing the movement of vehicles at intersections within a CACC framework. The proposed framework uses game theory to ensure that no crashes occur while minimizing the intersection delay. The proposed framework assumes communication between vehicles and the intersection infrastructure to control the movements of the reactive agents approaching the intersection study zone (ISZ). A real-time simulation tool is developed that would be loaded onto an intersection controller to control the vehicle movements. The simulation determines the vehicles currently in the ISZ and then estimates their trajectories based on their current state. Thereafter, the optimization process begins by forming a pay-off table for what would be the output in case of any action taken by the controller or the vehicles. Consequently, the intersection controller would advice the vehicle (using communication) to the best action. This process is repeated heuristically at each time step for the duration of the simulation (i.e. all vehicles traverse the intersection). The proposed work serves as an initial step towards the development of agent-based CACC intersection control systems. The research results demonstrate the promising potential benefits of such a system over conventional stateof-the-practice intersection control systems. Further testing of the proposed system is recommended for typical intersection configurations under realistic traffic demand levels relative to alternative state-of-the-practice intersection control systems.

## References

1. NCSA, National Center for Statistics and Analysis, Traffic Safety Facts 2009, D.H. 811401, Editor. 2011: U.S. DOT, Washington, DC.
2. US Department of Transportation Website, http://www.fhwa.dot.gov, Accessed on November 10th 2011.
3. Connected Vehicle Research program (IntelliDrive), http://www.its.dot.gov/connected_vehicle/connected_vehicle.htm , Retrieved July 11th, 2012.
4. Rakha, H. and R.K. Kamalanathsharma, Eco-driving at Signalized Intersections using V2I Communication. 14th International IEEE Annual Conference on Intelligent Transportation Systems, 2011.
5. Stevanovic, A., et al., Optimizing traffic control to reduce fuel consumption and vehicular emissions: an integrated approach of VISSIM, CMEM, and VISGAOST, in The 88th Annual Meeting of the Transportation Research Board. 2009.
6. Nishuichi, H. and T. Yoshii, A study of the signal control for the minimization of CO2 emission, in Proceedings of the 12th World Congress on Intelligent Transport Systems. 2005: San Francisco, CA.
7. Malakorn, K.J. and B.B. Park, Assessment of Mobility, Energy, and Environment Impacts of IntelliDrive-based Cooperative Adaptive Cruise Control and Intelligent Traffic Signal Control. IEEE International Symposium on Sustainable Systems and Technology, 2010.
8. Rakha, H. and K. Ahn, Integration Modeling Framework for Estimating Mobile Source Emissions. Transportation Engineering ASCE, 2004: p. 183-193.
9. Lee, J. and B.B. Park, Development and Evaluation of a Cooperative Vehicle Intersection Control Algorithm under the Connected Vehicles Environment. IEEE Transactions on Intelligent Transportation Systems, 2011.
10. Dia, H., An agent-based approach to modelling driver route choice behaviour under the influence of real-time information. Transportation Research Part C 2002: p. 331-349.
11. Dresner, K. and P. Stone, Multiagent Traffic Management: Opportunities for Multiagent Learning, in K. Tuyls, et al, editors, LAMAS, Lecture Notes In Artificial Intelligence. 2005: Springer Verlag, Berlin.
12. Chen, B. and H.H. Cheng, A Review of the Applications of Agent Technology in Traffic and Transportation Systems. IEEE Transactions on Intelligent Transportation Systems, 2010. 11: p. 485-497.
13. Rakha, H. and I. Lucic, Variable power vehicle dynamics model for estimating maximum truck acceleration levels. Journal of Transportation Engineering, 2002. 128(5): p. 412-419.
14. Xinhai, X. and X. Lunhui, Traffic Signal Control Agent Interaction Model based on Game Theory and Reinforcement Learning, in International Forum on Computer Science-Technology and Applications. 2009.
15. Martın, J.C. and C. Roman, Hub location in the South-Atlantic airline market $A$ spatial competition game. Transportation Research Part A, 2003: p. 865-888.
16. Shyr, O. and M.-F. Hung, Intermodal Competition with High Speed Rail- a Game Theory Approach. Journal of Marine Science and Technology, 2010. 18(1): p. 32-40.
17. Laumonier, J., C. Desjardins, and B. Chaibdraa, Cooperative Adaptive Cruise Control: a Reinforcement Learning Approach, in Autonomous Agents and Multiagent Systems (AAMAS). 2006.
18. Rasmusen, E., Games and Information: An Introduction to Game Theory. 1990: Basil Blackwell, Inc.
19. The New York Times http://www.nytimes.com/2010/10/10/science/10google.html, Retrieved May15th, 2011.

[^0]:    Manuscript received March 15, 2012. This work was done by the Center for Sustainable Mobility at Virginia Tech Transportation Institute and was funded by the Mid-Atlantic University Transportation Center (MAUTC).

    Ismail H. Zohdy is a PhD Candidate in the Civil and Environmental Engineering Department, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061 USA (e-mail: izohdy@vt.edu).

    Hesham Rakha (corresponding author) is a Professor with the Charles E Via, Jr. Department of Civil and Environmental Engineering and the Director of the Center for Sustainable Mobility, Virginia Polytechnic Institute and State University, Blacksburg, Virginia, 24061 USA (Phone: 540-231-1505, email: hrakha@vtti.vt.edu).

