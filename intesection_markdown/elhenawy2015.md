# An Intersection Game-Theory-Based Traffic Control Algorithm in a Connected Vehicle Environment 

Mohammed Elhenawy ${ }^{1}$, Ahmed A. Elbery ${ }^{2}$, and Abdallah A. Hassan ${ }^{1}$<br>${ }^{1}$ Dept. of Electrical and Computer Engineering<br>${ }^{2}$ Dept. of Computer Science and Application<br>Virginia Tech

Blacksburg, VA 24061
mohame1@vt.edu, aelbery@vt.edu, abdallah@vt.edu

Hesham A. Rakha
Dept. of Civil and Environmental
Engineering
Virginia Tech Transportation Institute
Blacksburg, VA 24061
hrakha@vt.edu


#### Abstract

Urban traffic congestion is a growing problem that we experience every day. Intersections are one of the major bottlenecks that contribute to urban traffic congestion. Traditional traffic control methods, such as traffic signal and stop sign control are not optimal for all demand levels as demonstrated in the literature. Recently, numerous research efforts proposed Intelligent Transportation System (ITS) applications to enhance intersection capacity and hence reduce congestion. In this paper we propose a game-theory-based algorithm for controlling autonomous vehicle movements equipped with Cooperative Adaptive Cruise Control (CACC) systems at uncontrolled intersections. The goal of this research effort is to develop an algorithm capable of using the future autonomous/automated vehicle capabilities to replace the usual state-of-the-practice control systems at intersections (e.g. stop signs, traffic signals, etc.). The proposed algorithm is chicken-game inspired and is efficient for application in real-time. It assumes vehicles can communicate with a central agent at the intersection to provide their instantaneous speeds and locations. The proposed algorithm assumes that vehicles obey the Nash equilibrium solution of the game. The simulation results demonstrated reductions in vehicle travel time and delay relative to an all-way stop sign control in the range of 49 and 89 percent on average respectively.


Keywords-traffic management; uncontrolled intersections; ITS; connected vehicles; CACC

## I. INTRODUCTION

The state-of-practice control systems at road intersections are stop signs, yield signs or traffic signals. The main design goal of these control systems is to manage traffic as well as to improve safety at intersections. Recently, some issues were raised related to the efficiency and safety of intersections using these control systems. The intersection safety needs identification report published by the Federal Highway Administration (FHWA) in July 2009 showed that in 2007, 22\% of the total fatal crashes were intersection-related with an estimated cost of 27.8 US billion dollars. In addition, 44.8\% of the total injury crashes were also intersection-related with an estimated cost of 51.3 US billion dollars [1]. Texas Transportation Institute published the 2011 Urban Mobility Report [2], which showed that the average commuter experienced 34 hours of delay in 2010 with an estimated cost of \$100.9 US billion dollars. A later report in 2012 published by the same institute [3], showed how the problem is getting worse as the amount of delay experienced by the average commuter in 2011 increased to 38 hours with an estimated cost of $\$ 121.2$ US billion dollars.

The above problems need innovative solutions, especially, when we know that the number of operating vehicles in the world will, at least, double by 2050 [4]. The use of autonomous vehicles is one of the promising innovative solutions. This idea dates back to 1939 when General Motors (GM) presented its vision of driverless vehicles at the World's Fair in New York. Back then, even before the appearance of computers, the aim was to reach fully-automated vehicles controlled by mechanical systems and radio controls. The appearance of computers encouraged GM and the US Department of Transportation (USDOT) to introduce the fully-automated highway concept [5].

The Automated Highway Systems (AHS) program was established by USDOT to reduce delay and to improve safety of traffic networks using automated vehicle control [5]. At the time of establishment of the AHS program, the existing technology was not mature enough, so the program was not able to continue. Yet, the AHS project paved the way for many drive assistant systems that exist in today's market.

The advances in wireless technologies and positioning systems make it possible to establish communication links between vehicles, traffic environment, and the control system. Moreover, new opportunities are introduced such as cooperative driving for the lane changing and merging in platoon [6], collision free movements of vehicles through non-signalized intersections (blind crossing) [7], etc.

Recently, the concept of Cooperative Adaptive Cruise Control (CACC) systems became feasible. CACC is an improvement on the Adaptive Cruise Control (ACC) which uses forward ranging sensors to measure the distance and approaching rate to the leading vehicle. ACC requires heavily processing algorithms to filter the input signals of the sensors from noise and interference. This signal filtering introduces delays which limits the ability of the ACC to accurately follow other leading vehicles. CACC overcomes this limitation by obtaining additional information communicated over a wireless data link. CACC can obtain information through vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communication and fuses it with the sensed information to make better and quicker decisions and to be able to follow the
leading vehicle with higher accuracy. The decision taken by the CACC after fusing the information can either be to accelerate, to decelerate, or to maintain the current speed. The current generation of the CACC is not responsible for maneuverability.

This paper presents a new intersection management algorithm for autonomous vehicles. The algorithm is gametheory-based and inspired by chicken-game. The algorithm utilizes on two main capabilities in the vehicle. The first is its capability to communicate to a central management center in the intersection to report its speed, location and direction. The intersection management center these information from all vehicles approaching the intersection and decide the action for each vehicles that will avoid crashes and give the lowest delay for each vehicle. The second is the CACC capability of the vehicle which will use the action received from the management center to drive the vehicle.

The rest of this paper is organized as following; Section II briefly discusses some related work in literature and the two main classes of methods for scheduling vehicles at uncontrolled intersections. Section III provides an overview of the chicken game algorithm and Section IV describes the proposed algorithm. The results of the experimental work are shown in Section V. The conclusions of the paper and future work are discussed in Section VI.

## II. RELATED WORK

The main objective of the algorithms for uncontrolled intersections is to provide an efficient way for crossing vehicles to negotiate and to cooperate to receive information to access the conflict zones of uncontrolled intersections. A conflict zone in an intersection is defined as an area of the intersection where two different crossing vehicles access during the same time interval. The algorithms for uncontrolled intersection can be classified into two broad categories.

One category of methods use centralized control. Vehicles approaching the intersection communicate with a central controller at the intersection. The central controller responds with directions needed for every vehicle to safely cross the intersection. Dresner and Stone proposed a simple centralized framework based on First In First Out (FIFO) priorities [8]. They used a multi-agent time reservation system consisting of an intersection manager (controller) and vehicle agents. When a vehicle approaches the intersection it requests time-space slot to cross the intersection. Upon receiving the driver agent request, the controller simulates the vehicle crossing the intersection and based on the output trajectories, the controller makes decisions that avoid conflicts.

There are several research efforts that treated safe-crossing of vehicles at uncontrolled intersections as a scheduling problem. Colombo et al. solved this problem by finding the maximum controlled invariant set and checking membership in this set using an algorithm that approximated the solution [9]. This approximate solution was used to design the controller for collision avoidance. The above scheduling approach is limited because it requires a perfect state information and absence of any disturbances. Bruni et al. improved the design of the controller by removing the limitations above and designed a controller that can deal with imperfect state information and input uncertainties [10]. Both of the above controllers assumed all vehicles are equipped with driver assistance systems (controlled vehicles). Ahn et al. proposed an inserted idle-time (IIT) scheduling approach [11] to enable the design of controller in presence of multiple uncontrolled vehicles [12]. Arora et al. modeled the collision avoidance between two vehicles at intersection as a two-player zero-sum game problem [13]. In their algorithm, each vehicle was modeled using a state space model at the continuous level. The two players in this game were the control action of the first vehicle and the velocity disturbance in the second vehicle.

The other category of methods use distributed (decentralized) control. Vehicles approaching an intersection directly negotiate with each other and decide which vehicle gets the right-of-way at which time. Guangquan et al. defined a set of rules used to prioritize passing vehicles through an intersection [14]. Following these rules was shown to resolve conflict problems and help avoid collisions. Based on the rules, each approaching car exchanges information with other vehicles and then decides whether to preempt or to yield other cars. Makarem and Gillet proposed a decentralized algorithm using a navigation function [15]. Their algorithm prioritized vehicles based on several factors to optimize on-board energy. Van Middlesworth et al. proposed another decentralized algorithm which required peer-to-peer communication to replace stop signs and schedule the crossing vehicles in small intersections [16]. The drawback of that algorithm is the requirement that each vehicle communicates with all other vehicles at each time step. Hassan and Rakha proposed a fully distributed algorithm which is more scalable because it required communication only between neighboring vehicles [17]. A complete intersection utilization schedule is formed after the leading vehicles on all approach lanes share information with each other. The algorithm minimized the overall intersection delay by favoring vehicles coming from heavier lanes.

The algorithm introduced in this paper builds on the work done at the center of sustainable mobility at Virginia tech transportation institute (VTTI) [4, 18-21] which used centralized multi-agent modeling and proposed and tested many algorithms to solve conflicts between autonomous vehicles at intersections. In [18], a simulator (OSDI) was built in the central controlling agent. OSDI used a heuristic optimization algorithm to continuously adjust the vehicles trajectories such that the occupancy time in areas of conflict in the intersection.is minimized. The experimental result showed a significant reduction in the delay for a simplified scenario of four-vehicles passing through the intersection zone. A game theory framework is used in [4, 19, 20] to develop a heuristic algorithm for autonomous vehicles equipped with cooperative adaptive cruise control CACC. The algorithms based on the game theory achieved significant reduction in vehicle delay compared to traditional intersection control schemes such as the use of traffic lights or the use stop signs.

## III. CHICKEN GAME BACKGROUND

The game of chicken [22] is a non-zero game that models two conflicting drivers. Both drivers are approaching a single lane bridge from opposite directions. Drivers are competing for the right to access the bridge first. The driver, who decides to
swerve away and yield the bridge to the other opposing driver, loses the game and is called the chicken while the other wins the game. If both drivers decide to go straight, they would crash and both will lose. The payoff matrix for this game is shown in FIGURE 1. The payoffs are chosen to show the players' preferences. The higher the payoff, the higher the player's preference. The most preferred outcome is to win and the least preferred outcome is to crash.

## IV. THE PROPOSED GAME FOR ISOLATED INTERSECTIONS

In this section we will describe our algorithm (game) to resolve the conflict between crossing vehicles at intersections. Any game consists of three basic elements, players, player actions, and utilities (payoffs). The following subsections define these three elements and set up the game for an intersection consisting of four single-lane approaches.

![](https://cdn.mathpix.com/cropped/dea911f2-27da-45ee-93c9-6683adb81d0a-3.jpg?height=767&width=657&top_left_y=920&top_left_x=294)
FIGURE 1: CHICKEN GAME MATRIX (a) PAYOFF MATRIX (b) NUMERICAL PAYOFF MATRIX

## A. Players

This game has only two players. The first player decides the actions of vehicles 2 and 4 while the second player decides the actions of vehicles 1 and 3 as shown in FIGURE 2. Each player wants to control the vehicles in such a way to minimize their delay at the intersection and to guarantee they safely cross the intersection without colliding with any conflicting vehicles.

## B. Player Actions

Depending on the speed of a vehicle, each player has three possible actions at most: to accelerate, to decelerate, or to continue at its current speed. For example, if the speed of a vehicle is less than the maximum speed and greater than zero, the player can assign it one of the above three actions. When a vehicle runs at the maximum posted speed, the player has only two actions (decelerate and constant) because the player cannot violate the speed limit. Since each player has two vehicles and each vehicle has an action set, the player's actions are the cross product of the actions of the vehicles. For example, if the actions of car \#1 are \{accelerate, constant\} and the actions of car \#3 are \{accelerate, constant, decelerate\}, then player \#2 actions are \{accelerate, constant\} × \{accelerate, constant, decelerate $\}=\{($ accelerate, accelerate $),($ constant, accelerate $)$, (decelerate, accelerate), (accelerate, constant), (constant, constant), (decelerate, constant)\}.

![](https://cdn.mathpix.com/cropped/dea911f2-27da-45ee-93c9-6683adb81d0a-3.jpg?height=655&width=715&top_left_y=513&top_left_x=1113)
FIGURE 2: ILLUSTRATION of PLAYERS in PROPOSED GAME

## C. Payoffs

We set up the following utilities for each player's action as shown in TABLE 1. The payoff utilities are chosen such that the most preferred action of the player is the action which guarantees safe crossing and minimum delay.

## D. Playing a game to choose the best players' action

1- Whenever a vehicle gets close to the central controller agent (e.g. 200m from the center of the intersection), it sends its current speed and position to the controller.

2- The controller chooses the nearest vehicle in each approach to the stop line, and based on their speeds it finds the set of feasible actions for each vehicle as explained in the players actions subsection.

3- The controller gets each player's actions by cross multiplying its vehicle actions.

4- The controller sets up a game matrix for the current four vehicles.

5- The controller scans the matrix and for each action set of player \#1 and player \#2, it runs a simulation. Based on the simulation result (collision/no collision) and the game payoff values shown in TABLE 1, the payoffs are assigned to each player.

FIGURE 3 shows an example of a game matrix for two players, each having four actions only.

6- The controller solves the game matrix and reaches the Nash equilibrium $x^{*}$ which satisfies $\forall i, x_{i} \in S_{i}: f_{i}\left(x_{i}^{*}, x_{-i}^{*}\right) \geq$ $f_{i}\left(x_{i}, x_{-i}^{*}\right)$ where $S_{i}$ is the actions set for player $i, f_{i}\left(x_{i}, x_{-i}\right)$ is
payoff for player $i$ when he plays $x_{i} \in S_{i}$ and other player plays $x_{-i} \in S_{-i}$.

7- The controller sends back to each vehicle its optimum action.

TABLE 1: GAME PAYOFFS FOR ONE PLAYER
| Player's Action | Utility if no conflict | Utility if conflict |
| :--- | :--- | :--- |
| (accelerate, accelerate) | 4 | -100 |
| (constant, accelerate) | 3 | -100 |
| (decelerate, accelerate) | 2 | -100 |
| (accelerate, constant) | 3 | -100 |
| (constant, constant) | 2 | -100 |
| (decelerate, constant) | 1 | -100 |
| (accelerate, decelerate) | 2 | -100 |
| (constant, decelerate) | 1 | -100 |
| (decelerate, decelerate) | 0 | -100 |


Player \#2
|  |  | (accelerate accelerate) | (constant accelerate) | (accelerate constant) | (constant constant) |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  | (accelerate, accelerate) | 4,4 | -100, -100 | 4,3 | 4,2 |
|  | (constant, accelerate) | -100, -100 | -100, -100 | -100, -100 | 3,2 |
| Player \#1 <br> Player \#1 | (accelerate, constant) | -100, -100 | -100, -100 | -100, -100 | 3,2 |
|  | (constant, constant) | -100, -100 | -100, -100 | -100, -100 | -100, -100 |


FIGURE 3: PAYOFF MATRIX FOR THE GAME WHEN PLAYER \#1 HAS FOUR ACTIONS AND PLAYER \#2 HAS FOUR ACTIONS. EACH CELL IN THIS MATRIX SHOWS THE PAYOFF FOR EACH PLAYER IF THEIR ACTIONS DID NOT CAUSE A CONFLICT.

## V. SIMULATED EXPERIMENTS

To test the proposed algorithm, a simulated study is held assuming an intersection consisting of four single lane approaches, as shown in FIGURE 2. The speed limit for each approach is set to 40 km/h (25 mph). For each experiment, this study considers a single vehicle arriving at each approach. For each experiment, the proposed game-theory-based intersection manager is compared to an all-way stop sign controlled intersection. For both scenarios, the entrance time and the speed of each vehicle is randomly generated. The average travel time is computed for all four automated vehicles. This procedure is repeated 30,000 times using a Monte Carlo simulation and the average travel time and delay were recorded for each simulation. The travel time in each simulation is the time taken by a vehicle to travel from the entrance point (200m from the center of the intersection) until it passes the intersection. FIGURE 4 shows the percentage reduction in the average travel time when using the proposed game theory algorithm compared to the use of a conventional stop sign control scheme. Figure 5 shows the percentage reduction in the total delay when using the proposed game theory algorithm compared to the use of a conventional stop sign control scheme. The average reduction in delay is 89 percent which is better than the 70 percent delay reduction achieved in [21].

## VI. CONCLUSIONS AND FUTURE WORK

This paper proposes an algorithm for traffic control at uncontrolled intersections. The proposed algorithm is inspired by the famous chicken game. The proposed algorithm assumes perfect communication between vehicles and the controller and that vehicles are equipped with CACC. Our algorithm has small game matrix and is suitable for real intersection controllers. Moreover the algorithm finds the best strategy for each player each time we play the game. The results of the simulated experiments show that the proposed algorithm achieves 49\% reduction in average travel time delay on average and 89\% reduction in delay when compared to the all-way stop sign controlled intersection.

Currently work is performed on extending the proposed algorithm beyond the isolated intersection case. Our future version of this algorithm aims to resolve the conflict of crossing vehicles while taking into account the traffic status at the downstream intersections. Another future extension to the work introduced in this paper is playing another game on each approach such that vehicles are platooned to improve the average delay experience by each vehicle.

![](https://cdn.mathpix.com/cropped/dea911f2-27da-45ee-93c9-6683adb81d0a-4.jpg?height=513&width=804&top_left_y=1362&top_left_x=1126)
FIGURE 4: HISTOGRAM OF TRAVEL TIME REDUCTION ASSOCIATED WITH THE PROPOSED GAME THEORY ALGORITHM.

![](https://cdn.mathpix.com/cropped/dea911f2-27da-45ee-93c9-6683adb81d0a-5.jpg?height=529&width=829&top_left_y=249&top_left_x=198)
Figure 5: HISTOGRAM OF DELAY REDUCTION ASSOCIATED WITH THE PROPOSED GAME THEORY ALGORITHM.

## ACKNOWLEDGEMENTS

This research was funded by the Connected Vehicle Initiative University Transportation Center (CVI-UTC).

## REFERENCES

[1] Richard C. Coakley and E. R. Stollof, "Intersection Safety Needs Identification Report," 2009.
[2] D. Schrank, T. Lomax, and B. Eisele, "2011 urban mobility report," 2011.
[3] D. Schrank, B. Eisele, and T. Lomax, "TTI's 2012 urban mobility report," Texas A\&M Transportation Institute. The Texas A\&M University System, 2012.
[4] I. H. Zohdy and H. Rakha, "Game theory algorithm for intersection-based cooperative adaptive cruise control (CACC) systems," in Intelligent Transportation Systems (ITSC), 2012 15th International IEEE Conference on, 2012, pp. 1097-1102.
[5] S. Cheon, "An overview of automated highway systems (AHS) and the social and institutional challenges they face," University of California Transportation Center, 2003.
[6] S. Tsugawa, "Inter-vehicle communications and their applications to intelligent vehicles: an overview," in Intelligent Vehicle Symposium, 2002. IEEE, 2002, pp. 564-569 vol.2.
[7] L. Li and F.-Y. Wang, "Cooperative driving at blind crossings using intervehicle communication," Vehicular Technology, IEEE Transactions on, vol. 55, pp. 1712-1724, 2006.
[8] K. Dresner and P. Stone, "Traffic intersections of the future," 2006.
[9] A. Colombo and D. Del Vecchio, "Efficient algorithms for collision avoidance at intersections," in Proceedings of the 15th ACM international conference on Hybrid Systems: Computation and Control, 2012, pp. 145-154.
[10] L. Bruni, A. Colombo, and D. Del Vecchio, "Robust multiagent collision avoidance through scheduling."
[11] J. J. Kanet and V. Sridharan, "Scheduling with inserted idle time: problem taxonomy and literature review," Operations Research, vol. 48, pp. 99-110, 2000.
[12] H. Ahn, A. Colombo, and D. Del Vecchio, "Supervisory control for intersection collision avoidance in the presence of uncontrolled vehicles," in American Control Conference (ACC), 2014, 2014, pp. 867-873.
[13] S. Arora, A. K. Raina, and A. K. Mittal, "Collision avoidance among AGVs at junctions," in Intelligent VehiclesSymposium, 2000. IV 2000. Proceedings of the IEEE, 2000, pp. 585-589.
[14] L. Guangquan, L. Lumiao, W. Yunpeng, Z. Ran, B. Zewen, and C. Haichong, "A rule based control algorithm of connected vehicles in uncontrolled intersection," in Intelligent Transportation Systems (ITSC), 2014 IEEE 17th International Conference on, 2014, pp. 115-120.
[15] L. Makarem and D. Gillet, "Fluent coordination of autonomous vehicles at intersections," in Systems, Man, and Cybernetics (SMC), 2012 IEEE International Conference on, 2012, pp. 2557-2562.
[16] M. VanMiddlesworth, K. Dresner, and P. Stone, "Replacing the stop sign: Unmanaged intersection control for autonomous vehicles," in Proceedings of the 7th international joint conference on Autonomous agents and multiagent systems-Volume 3, 2008, pp. 1413-1416.
[17] A. A. Hassan and H. A. Rakha, "A Fully-Distributed Heuristic Algorithm for Control of Autonomous Vehicle Movements at Isolated Intersections," International Journal of Transportation Science and Technology, vol. 3, pp. 297-310, 2014.
[18] I. Zohdy and H. Rakha, "Optimizing driverless vehicles at intersections."
[19] I. H. Zohdy, R. K. Kamalanathsharma, and H. Rakha, "Intersection management for autonomous vehicles using icacc," in Intelligent Transportation Systems (ITSC), 2012 15th International IEEE Conference on, 2012, pp. 1109-1114.
[20] I. H. Zohdy and H. A. Rakha, "Intersection management via vehicle connectivity: The intersection cooperative adaptive cruise control system concept," Journal of Intelligent Transportation Systems, pp. 1-16, 2014.
[21] H. A. Rakha, I. H. Zohdy, and R. K. Kamalanathsharm, "Agent-Based Game Theory Modeling for Driverless Vehicles at Intersections," 2013.
[22] Z. Han, D. Niyato, W. Saad, and T. Başar, Game Theory in Wireless and Communication Networks: Theory, Models, and Applications Cambridge University Press, January 2012.
