Amir Mirheli ${ }^{\mathrm{a}}$, Leila Hajibabai ${ }^{\mathrm{a}, *}$, Ali Hajbabaie ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}}$ Department of Civil Engineering, State University of New York at Stony Brook, Stony Brook, NY 11794, USA<br>${ }^{\mathrm{b}}$ Department of Civil and Environmental Engineering, Washington State University, Pullman, WA 99164, USA

A R T I C L E I N F O

Keywords:
Control logic
Autonomous intersection control
Monte Carlo tree search
Look-ahead model
Connected and autonomous vehicles
Dynamic programming


#### Abstract

Establishment of effective cooperation between vehicles and transportation infrastructure improves travel reliability in urban transportation networks. Lack of collaboration, however, exacerbates congestion due mainly to frequent stops at signalized intersections. It is beneficial to develop a control logic that collects basic safety message from approaching connected and autonomous vehicles and guarantees efficient intersection operations with safe and incident free vehicle maneuvers. In this paper, a signal-head-free intersection control logic is formulated into a dynamic programming model that aims to maximize the intersection throughput. A stochastic look-ahead technique is proposed based on Monte Carlo tree search algorithm to determine the near-optimal actions (i.e., acceleration rates) over time to prevent movement conflicts. Our numerical results confirm that the proposed technique can solve the problem efficiently and addresses the consequences of existing traffic signals. The proposed approach, while completely avoids incidents at intersections, significantly reduces travel time (ranging between 59.4\% and 83.7\% when compared to fixed-time and fully-actuated control strategies) at intersections under various demand patterns.


## 1. Introduction

Congestion cost is an immediate consequence of population growth causing 6.9 billion hours of travel delay and extra 3.1 billion gallons of fuel waste in 2014. It has contributed to \$160 billion cost in the US in 2014 demonstrating 40\% rise compared to 2000 (Schrank et al., 2015). Besides, the increasing trend in vehicle ownership has contributed to traffic safety and reliability concerns. National highway traffic safety administration reports annual rates of severe traffic accidents between 2012 and 2014 that have resulted in 33,117 life losses (NHTSA, 2014). Vehicular movements on busy intersections are mainly controlled by traffic signals, where possible maneuvers for passing through an intersection are regulated. The controllers aim to prioritize traffic movements and coordinate with neighboring controllers while avoiding conflicting flows, where controlling the stop-and-go conditions is not often considered as the highest priority. Signal timing of intersections can be optimized to reduce the congestion delay; yet, there is more opportunity to further minimize the control delay through innovative use of advanced technologies that help avoid unnecessary stops and provide safe vehicle trajectories.

Recent advancements in communication technologies and the internet of things provide promising solutions to future-oriented transportation problems, e.g., reducing delay of traffic movements without compromising traffic safety. Moving towards such capabilities, the emerging connected vehicle technology is offering vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I)

[^0]communication that allow passing basic safety message (e.g., vehicle location, speed, and acceleration) between the entities. Besides, vehicle information can be transmitted to an intersection control unit over time that provides vehicles with their desired trajectory for next time intervals. Such technologies enable replacing the conventional traffic control systems by an effective communication scheme among vehicles and a local controller. This control strategy is much more effective in a connected and autonomous vehicle (CAV) environment, where (i) perception-reaction (P-R) times are reduced (i.e., less than 1.0-1.5 s measured for experienced drivers compared to 2-2.5 sec for typical human drivers (NAHSC, 1996)) and (ii) stochastic human-based errors are excluded from the system. Therefore, spacing between CAVs will be shorter and higher level of roadway capacity will be experienced (Wei et al., 2016). Finding optimal vehicle trajectories under safety constraints is often very challenging when the traffic volume is high. Adding vehicles to the optimization models increases the state space and enlarges the number of variables in each time period, which makes the problem even more complex such that existing commercial solvers will be unable to find their optimal solutions. Besides, introducing uncertainties to the problem (e.g., accidents, miscommunications among vehicles and controllers) will add more variables to handle the stochasticities. Literature has presented research efforts on the implementation of a rolling horizon approach in a deterministic environment with moderate traffic volumes. Most studies have used dynamic programming (DP) approaches by looking at stochastic look-ahead models that consider uncertainties over time (Bent and Van Hentenryck, 2004; Powell, Simao and Bouzaiene-Ayari, 2012). To facilitate decision making in each time interval, state and action spaces are discretized in these methods (Puterman, 2014). Similarly, on a different case study, Al-kanj et al. (2016) have formulated the vehicle routing problem in emergency storm response as a sequential stochastic optimization model and applied a Monte Carlo tree search (MCTS) algorithm in a stochastic look-ahead policy to handle unknown events in the next steps.

This paper first presents a formulation for signal-head-free intersection control logic (SICL) that obtains vehicular movement information, allocates the desired speed to CAVs approaching the intersection, and assigns acceleration/deceleration rates to vehicles with conflicting movements (see Fig. 1).

The problem includes both through and left-turn movements. The objective is to maximize the intersection throughput under a set of conflict avoidance constraints on the intersection approaches and inside the intersections. Previous studies minimize total length of overlapped trajectories only for crossing vehicles (e.g., Lee and Park (2012)). Expanding upon those studies, this paper applies the control logic to all approaching CAVs and adjusts each vehicle's trajectory before crossing the intersection. The problem is solved using a stochastic look-ahead technique based on the MCTS algorithm and applied to a set of case study scenarios to evaluate its performance. The proposed methodology is also compared to the conventional traffic control systems and a set of benchmark solutions at various demand rates. The proposed SICL methodology efficiently determines near-optimal CAV trajectories for high traffic volumes and various turning movements. The computation time of the proposed technique is sufficiently short that allows finding feasible solutions without the need to use a recovery mode. SICL can handle uncertainties (e.g., in traffic demand) and it can find the trajectories of all vehicles in the intersection neighborhood and re-optimize the trajectories if an unexpected event happens.

The remainder of this paper is organized as follows. Section 2 summarizes previous studies on different traffic control algorithms under deterministic and stochastic conditions. Section 3 presents the mathematical formulation for the proposed SICL and Section 4 details the solution technique. Section 5 presents the numerical experiments and evaluates the mobility impact of the proposed control logic under varying traffic demand. Finally, Section 6 concludes the paper and discusses future research directions.

![](https://cdn.mathpix.com/cropped/f7cbcf4d-7353-4369-a735-9add015efac1-02.jpg?height=717&width=737&top_left_y=1628&top_left_x=576)
Fig. 1. Cooperative traffic control in the intersection neighborhood.

## 2. Background

Advancements in information technology have provided reliable connectivity among entities of transportation systems that facilitates the development of autonomous urban traffic control systems. For instance, under traffic signal control strategies, Sun et al. (2017) have developed an intersection operation scheme to maximize intersection capacity via dynamic optimization of lane assignments and green times. Li et al. (2014) have developed an algorithm to jointly optimize intersection signal timing parameters and vehicle paths using communications between approaching vehicles and the controller captured via a rolling horizon technique. Recently, Islam and Hajbabaie (2017) have developed a real-time signal control strategy to find near-optimal signal timing parameters in a connected urban street network, which implements a distributed optimization and coordination algorithm presented in Mehrabipour and Hajbabaie (2017). Guler et al. (2014) have proposed an algorithm to optimize traffic operations at an intersection using individual vehicles' location and speed on one-way streets with predefined signal timing scenarios, CAV penetration rates, and total demand variations. Zhou et al. (2017) have developed a parsimonious shooting heuristic to determine vehicle trajectories on a signalized highway segment under vehicle arrival patterns, car-following safety, signal operations, and vehicle kinematic limits. In a follow-up study, Ma et al. (2017) have developed a numerical sub-gradient-based algorithm with embedded shooting heuristic to identify a stream of vehicle trajectories that yield optimal traffic performance measures. Despite its importance, intersection management using signal-head-free controllers has not been intensively studied in the literature, mainly due to the limitations of traditional communication technologies. This section summarizes the existing methodologies that aim to reduce travel delay and maintain a safe environment for crossing vehicles.

Dresner and Stone $(2004,2008)$ have developed a multi-agent reservation-based intersection control mechanism designed for traffic streams of fully autonomous vehicles. Their proposed approach does not consider turning movements and assumes fixed vehicle speeds inside an intersection. In a follow-up study, Dresner and Stone (2008) has included a first-come-first-serve algorithm in their method, where the intersection controller grants or rejects vehicle requests to proceed through the intersection once the requests are received. As such, the decisions are made regardless of potential vehicle arrivals at an immediate future that can cause operations and safety concerns. In a related study, Shahidi (2010) has developed a delayed response policy to address this limitation and batched the received requests to make a more informed selection. This study, similar to the previous ones, is expert opinion-based and does not find optimal stop-free trajectories in intersections. Vasirani and Ossowski (2012) have extended the reservation-based intersection control model (Dresner and Stone, 2004) utilizing a market-inspired mechanism. They have modeled the supply-demand relationship at intersections that allow movements based on the ratio of volume over the capacity of the approach. A pricing policy has been incorporated into the reservation-based intersection control system to reduce the delay. However, the winner determination algorithm has been implemented for the current bids in each round, and the future bids have been completely ignored, as such the trajectories would not be optimal over time. To address safety concerns, several studies have attempted to use exclusion policies and recovery modes in their control methods. Wu et al. (2012) have used a centralized formulation to solve the autonomous intersection management problem. The study does not solve the problem analytically due to the large decision space. Therefore, an ant colony algorithm is applied to address this issue, which does not guarantee the optimality of their solutions. To promote safety, they have included a policy to allow vehicles to enter the intersection only after conflicting movements have completely cleared the intersection. While this method achieves its aims, it also pushes the attained trajectories even farther away from optimality.

Similarly, Lee and Park (2012), Lee et al. (2013) have proposed a centralized cooperative intersection control that would minimize the total length of overlapped trajectories. Their proposed mathematical formulation is complex; hence, they have used genetic algorithms to solve the problem, where, still, their solutions result in collisions since there are no constraints to avoid them. Therefore, they have included a recovery mode to prevent collisions by stopping vehicles on conflicting movements. The use of genetic algorithms and inclusion of the recovery mode does not allow this approach to find optimal collision-free trajectories. Dai et al. (2016) have extended Lee and Park's algorithm to vehicular cyber physical systems with the objective to enforce smooth movements to improve passengers' travel quality in a centralized formulation. The intersection zone is divided into identical small areas and route conflicts are specified in collision zones. They have linearized collision avoidance constraints and consequently converted the problem into a convex optimization program. However, the problem is still complex, and their solution algorithm cannot always find a feasible solution. As such, they have included a recovery mode, meaning that the algorithm does not guarantee optimal collision-free trajectories.

On the other hand, a set of research efforts have attempted to use centralized programming to develop an intersection control logic for connected vehicles. The first study by Zohdy and Rakha (2014) have proposed a centralized, deterministic, intersection cooperative adaptive cruise control model to identify conflicting movements. The controller defines vehicle trajectories through a rolling horizon approach using data on speed, acceleration, and location of vehicles. Vehicle delay is defined based on the difference of arrival times to an intersection with and without conflict avoidance constraints; once potential accidents are identified, the actual time of reaching to conflict points is determined using an interior-point algorithm. In this methodology, the length of the planning horizon has to be limited in this approach due to computational complexities. Additionally, the approach is deterministic and does not address uncertainties. Wuthishuwong et al. (2015) have discretized the time and space at an intersection and used a centralized dynamic programming to find the trajectory of each vehicle at every discretized time. The computational complexity of this problem grows exponentially when the number of vehicles increases, thus, the approach cannot find near-optimal solutions in real-time. Finally, Muller et al. (2016) have presented a centralized mixed-integer linear programming (MILP) intersection control model, where location and speed of autonomous vehicles in each time step are gathered to provide the shortest and longest travel times to reach an intersection. Then, the aggregated arrival time for all vehicles is minimized utilizing the travel times calculated in each time step, and the speed profile is assigned to vehicles to approach the intersection. Average speed is determined based on the feasible set
of allowable speed profiles. This method is also computationally complex and only addresses through movements. Wei et al. (2016), on the other hand, have developed a simplified car following model and a DP algorithm to minimize vehicles' total travel cost and fuel consumption to assure minimal safety spacing between vehicles by discretizing the time into stages and space into a grid. The proposed algorithm is not capable of solving the network-level problem with a large set of vehicles due to the computational complexity of their DP algorithm.

A category of literature has focused on control algorithms that seek to coordinate autonomous vehicles using only V2V or infrastructure to infrastructure (I2I) communication schemes to guarantee safe maneuvers without optimizing trajectories for improving network performance, e.g., Faye et al. (2012), Azimi et al. (2013). Simulation results of implementing such control algorithms show improvements in terms of average travel time and number of completed trips. However, there is no guarantee that a better solution does not exist. One reason is that prioritizing the movements does not account for waiting time of vehicles stopped at the intersection as their conflicting movements are still passing the intersection. Vehicles without conflicts can be granted permits even if they have arrived later than vehicles with conflicts. Therefore, this solution may not lead to minimum travel time. Another school of research aims to incorporate analytical techniques to determine the optimal solution to safe intersection crossing trajectories. For instance, Raravi et al. (2007) have proposed a merging algorithm that finds the optimal trajectories for vehicles from two conflicting approaches with the objective of minimizing the travel time to reach the intersection region. In this algorithm, vehicles can cross the intersection only when the intersection is completely clear. Consequently, this approach will not find the shortest possible travel time.

All of the previous studies have shown that an autonomous intersection control logic improves traffic operations compared to optimally timed signals for autonomous vehicles. Nevertheless, the studies and efforts in the literature have limitations. None of these studies have been able to develop an analytical platform to obtain near-optimal collision-free trajectories under any possible system state. As such, while they can find reliable collision-free trajectories under certain defined conditions, they cannot do so under all prevailing conditions. The proposed study will fill this gap and offers an analytical platform to find collision-free trajectories under various system states.

## 3. Model formulation

This section introduces a dynamic programming framework to find near-optimal trajectories for CAVs approaching and crossing an intersection under safety constraints. Let $T$ be the number of discrete time periods in the planning horizon and $\Gamma=\{0,1, \ldots, T-1\}$ represent the times at which decisions are made. We let $I$ denote the set of lanes for approaching vehicles to the intersection. The width of each lane is 12 ft and a 650 ft range around the intersection is assumed to define the vehicle detection zone. Fig. 2 illustrates the layout of an isolated intersection with eight incoming approach lanes.

For each $t \in \Gamma, i \in I$, we let $\widehat{C}_{i}^{t}$ denote the set of vehicles on lane $i$ first detected in the intersection neighborhood at time $t$. Therefore, $\hat{C}^{t}=\bigcup_{i \in I} \widehat{C}_{i}^{t}$ presents the set of newly added vehicles to the intersection at time $t$. We also let $C_{i}^{t}$ be the set of previously detected vehicles on lane $i$ at time $t$ before new arrivals to the intersection and $C^{t}=\bigcup_{i \in I} C_{i}^{t}$ indicates the set of already existing vehicles in the system. Then, $C^{t^{+}}$presents the set of all vehicles in the intersection neighborhood at time $t$ that includes all existing as well as newly realized vehicles, i.e., $C^{t^{+}}=C^{t} \cup \widehat{C}^{t}$. Similarly, let $\widehat{X}_{i j}^{t}$ present the location of vehicle $j \in \widehat{C}_{i}^{t}$ first detected on lane $i$ at time $t$ and $\widehat{X}^{t}=\bigcup_{i \in I, j \in \hat{c}_{i}^{t}} \widehat{X}_{i j}^{t}$ describe the spatial distribution of all newly realized vehicles at the intersection at time $t$. We let $X_{i j}^{t}$ be

![](https://cdn.mathpix.com/cropped/f7cbcf4d-7353-4369-a735-9add015efac1-04.jpg?height=735&width=735&top_left_y=1608&top_left_x=578)
Fig. 2. An isolated intersection layout including movement notations, conflict regions, and CAV detection range.

the location of existing vehicle $j$ on lane $i$ at time $t$ before any new arrivals to the intersection neighborhood; similarly, $X^{t}=\bigcup_{i \in I, j \in C_{i}^{t}} X_{i j}^{t}$ represents the location of vehicles that are previously detected in the system at time $t$. Then, $X^{t^{+}}$indicates the location of all vehicles in the intersection neighborhood at time $t$, where $X^{t^{+}}=X^{t} \cup \widehat{X}^{t}$. Similarly, to keep track of vehicle speeds, $\widehat{\mathscr{V}}_{i j}^{t}$ is defined for each $t \in \Gamma, i \in I, j \in \widehat{C}_{i}^{t}$ and $\widehat{\mathscr{V}}^{t}=\bigcup_{i \in I, j \in \hat{C}_{i}^{t}} \widehat{\mathscr{V}}_{i j}^{t}$ presents all vehicle speeds, where vehicles are first detected at time $t$. Then, $\mathscr{V}_{i j}^{t}$ denotes the speed of vehicle $j$ already on lane $i$ at time $t$ and $\mathscr{V}^{t}=\bigcup_{i \in I, j \in C_{i}^{t}} \mathscr{V}_{i j}^{t}$ represents the set of speeds before the speed of new vehicles in $\widehat{\mathscr{V}}^{t}$ are included in the system. Again, $\mathscr{V}^{t^{+}}$presents the speed of all vehicles in the intersection neighborhood at time $t$, i.e., $\mathscr{V}^{t^{+}}=\mathscr{V}^{t} \cup \hat{\mathscr{V}}^{t}$. Similar to Hajibabai and Ouyang (2016), we let $W^{t}=\left(\hat{C}^{t}, \hat{X}^{t}, \hat{\mathscr{V}}^{t}\right)$ represent new information arriving at time $t$, where $\left(W^{t}\right)_{t=0}^{T}$ denotes our stochastic information process with realization $W^{t}(\omega)=\omega_{t}=\left(\widehat{C}^{t}(\omega), \widehat{X}^{t}(\omega), \widehat{\mathscr{V}}^{t}(\omega)\right)$. Sample realization $\omega$ depends on the policy selection, e.g., less traffic demand and lower speed reduces the risk of accidents that is defined as a new information. Therefore, we let $\Omega^{\pi}$ be the set of outcomes that depend on policy $\pi$ we use to permit vehicle movements. The state of our system is captured by the distribution of available vehicles, their location on each lane, and their speed at each intersection neighborhood, i.e., $S^{t}=\left\{C^{t}, X^{t}, \mathscr{V}^{t}\right\}$. This study eliminates traffic signals at intersections and instead, develops a SICL system; i.e., at each time $t$, basic safety message provides information on location and speed of each vehicle in an isolated intersection. Based upon traffic state at the intersection and downstream streets, the near-optimal vehicle maneuvers will be determined by assigning acceleration $a_{i j}^{t}$ to vehicle $j \in C_{i}^{t^{+}}$on lane $i \in I$ at time $t \in \Gamma$ to approach and cross the intersection without any conflicts. Thus, at each time $t$, SICL decisions impose vehicles to (i) keep their desired speed and pass the intersection or (ii) change their speed to avoid collisions and then recover their desired speed. Therefore, by maintaining an appropriate safety distance, vehicles pass the intersections at shorter headways that reduces their travel times and improves the intersection throughput that is the objective of this research. All decisions at time $t$ are captured by the acceleration vector $a^{t}=\bigcup_{i \in I, j \in C_{i}^{+}} a_{i j}^{t}$. Research shows that throughput maximization outperforms travel time and delay minimization under oversaturated flow conditions thus, this study aims to maximize intersection throughput (Hajbabaie and Benekohal, 2013, 2015). Let $\zeta^{t}\left(a^{t}\right)$ define the one-period reward function that is the intersection throughput based on the decisions made at time $t$. To maximize $\zeta^{t}\left(a^{t}\right)$, we alternatively define $\delta^{t}\left(a^{t}\right)$ that represents the distance between the location of vehicles at time $t$ and their pre-defined destination $X_{r_{i}}$ at each intersection lane $i$, where $\max \zeta^{t}\left(a^{t}\right) \equiv \min \delta^{t}\left(a^{t}\right)$. To ensure smooth speed variance on each lane, we define the one-period cost function $\delta_{v}^{t}\left(a^{t}\right)$ as

$$
\delta_{v}^{t}\left(a^{t}\right)=\sum_{i \in I} \sum_{j \in C_{i}^{t^{+}}}\left(X_{r_{i}}-X_{i j}^{t+1}\right)+\gamma\left|\mathscr{V}_{i j}^{t+1}-\mathscr{V}_{i j}^{t^{+}}\right|,
$$

where $\left|\mathscr{V}_{i j}^{t+1}-\mathscr{V}_{i j}^{t^{+}}\right|$represents the change in vehicle $j$ 's speed on lane $i$ over time $t$ and $\gamma$ is the speed-location conversion factor. The feasible region for a given outcome $\omega$ at time $t$ is subject to

$$
\begin{aligned}
& X_{i j}^{t+1}(\omega)=\frac{1}{2} a_{i j}^{t}(\omega) t^{2}+\mathscr{V}_{i j}^{t^{+}}(\omega) t+X_{i j}^{t^{+}}(\omega), \quad \forall i \in I, \forall j \in C_{i}^{t^{+}}, t \in \Gamma, \\
& \mathscr{V}_{i j}^{t+1}(\omega)=a_{i j}^{t}(\omega) t+\mathscr{V}_{i j}^{t^{+}}(\omega), \quad \forall i \in I, \forall j \in C_{i}^{t^{+}}, t \in \Gamma, \\
& \alpha \leqslant a_{i j}^{t}(\omega) \leqslant \alpha^{\prime}, \quad \forall i \in I, \forall j \in C_{i}^{t^{+}}, t \in \Gamma, \\
& 0 \leqslant \mathscr{V}_{i j}^{t+1} \leqslant \varepsilon^{\prime}, \forall i \in I, \forall j \in C_{i}^{t^{+}}, t \in \Gamma, \\
& \left|X_{i j}^{t+1}(\omega)-X_{i j+1}^{t+1}(\omega)\right| \geqslant\left(L_{v}+D\right)+R \mathscr{V}_{i j+1}^{t+1}(\omega), \forall i \in I, \quad \forall j \in C_{i}^{t^{+}}, t \in \Gamma, \\
& \left|X_{i j}^{t+1}(\omega)-F_{i}\right|+\left|X_{l m}^{t+1}(\omega)-F_{l}\right| \geqslant\left(L_{v}+D\right), \forall i, l \in I, i \neq l, \forall j, m \in C^{t^{+}}, j \neq m, \quad \forall t \in \Gamma .
\end{aligned}
$$

Constraints (1b) and (1c) define the location $X_{i j}^{t+1}$ and speed $\mathscr{V}_{i j}^{t+1}$ of each vehicle at time $t+1$ based on acceleration decisions for a given outcome $\omega$ at time $t$. Constraints (1d) enforce vehicles to apply functional acceleration rates depending on the vehicles' performance to change their speed within a certain acceleration threshold, i.e., $\alpha$ and $\alpha^{\prime}$. Similarly, constraints (1e) enforce the driving speed to fall between a minimum speed $\varepsilon$ and free-flow speed $\varepsilon^{\prime}$. Constraints (1f) and (1g) ensure safe movements for vehicles in one lane and crossing lanes, respectively, where $L_{v}$ denotes the length of vehicle, $D$ is considered as a safety distance between CAVs, and $R$ represents the CAV reaction time. $F_{i}$ and $F_{l}(\forall i, l \in I)$ are input parameters defined as center of the conflict regions of each two lanes shown in Fig. 2. The safety distance and vehicle length define the radius of the conflict regions. Constraints (1g) avoids simultaneous appearance of crossing vehicles in the conflict regions.

While constraints (1b) and (1c) capture the dynamics of the system over time, our objective function is defined to minimize the expected difference between the location of each vehicle and its destination over the planning horizon under smooth speed change, given an initial state $S^{0}$, as follows:

$$
\min _{a^{0}} \delta_{v}^{0}\left(a^{0}\right)+\mathbb{E}\left\{\sum_{\mathbf{t} \in \Gamma \backslash\{\boldsymbol{Q}\}} \min _{\mathbf{a}^{1}} \delta_{\mathbf{v}}^{\mathbf{t}}\left(\mathbf{a}^{\mathbf{t}}\right)\right\} .
$$

Thus, the overall optimization problem is represented by (1b)-(1g) and (2), where $\delta_{v}^{t}\left(a^{t}\right)$ is computed by (1a).

## 4. Solution technique

The objective function (2) is re-written as an equivalent Bellman's equation, i.e., $V^{t}\left(S^{t}\right)=\mathbb{E}\left\{\min _{\left(\mathbf{a}^{\mathbf{t}}\right)} \delta_{\mathbf{v}}^{\mathbf{t}}\left(\mathbf{a}^{\mathbf{t}}\right)+\mathbb{V}^{\mathbf{t}+\mathbf{1}}\left(\mathbb{S}^{\mathbf{t}+\mathbf{1}}\right) \mid \mathbb{S}^{\mathbf{t}}\right\}$. For a single sample realization $\omega$ at time $t \in \Gamma$, the corresponding problem will be presented by $V^{t}\left(S^{t}, \omega\right)=\min _{\left(a^{t}(\omega)\right)} \delta_{v}^{t}\left(a^{t}\right)+V^{t+1}\left(S^{t+1}\right)$. For notation simplicity, we focus on one generic sample realization and omit $\omega$ everywhere beginning from this section.

Problem (1b)-(1g) and (2) is a challenging non-linear program (NLP). We linearize constraints (1g) as follows.

$$
\begin{aligned}
& \left(X_{i j}^{t+1}-F_{i}\right)+\left(X_{l m}^{t+1}-F_{l}\right) \geqslant\left(L_{v}+D\right)-M\left(1-\theta_{1}\right), \quad \forall i, l \in I, i \neq l, \forall j, m \in C^{t}, j \neq m, \forall t \in \Gamma, \\
& \left(X_{i j}^{t+1}-F_{i}\right)-\left(X_{l m}^{t+1}-F_{l}\right) \geqslant\left(L_{v}+D\right)-M\left(1-\theta_{2}\right), \forall i, l \in I, i \neq l, \forall j, m \in C^{t}, j \neq m, \forall t \in \Gamma, \\
& -\left(X_{i j}^{t+1}-F_{i}\right)+\left(X_{l m}^{t+1}-F_{l}\right) \geqslant\left(L_{v}+D\right)-M\left(1-\theta_{3}\right), \quad \forall i, l \in I, i \neq l, \forall j, m \in C^{t}, j \neq m, \forall t \in \Gamma, \\
& -\left(X_{i j}^{t+1}-F_{i}\right)-\left(X_{l m}^{t+1}-F_{l}\right) \geqslant\left(L_{v}+D\right)-M\left(1-\theta_{4}\right), \quad \forall i, l \in I, i \neq l, \forall j, m \in C^{t}, j \neq m, \forall t \in \Gamma, \\
& \theta_{b} \in\{0,1\}, \quad \forall b \in\{1, \ldots, 4\}, \\
& \sum_{b=1}^{4} \theta_{b}=1 .
\end{aligned}
$$

where $M$ is a sufficiently large constant value. Thus, the original problem will be converted into a MILP represented by (1b)-(1f), (2), and (3a)-(3f). We use a stochastic look-ahead approach based on MCTS to solve the MILP problem in each time $t$ considering current states and the outcomes of previously selected actions.

This problem experiences a huge state space, i.e., too many combinations of available vehicles, their locations on each lane, and their speed at each intersection neighborhood over all times $t \in \Gamma$ on all lanes $i \in I$, which makes the problem computationally intractable. Hence, it is very helpful to use approximation methods to solve the problem over the whole planning horizon (e.g., excluding a state variable and substituting the value function with an estimated function of the remaining state variables in Godfrey and Powell. 2001; Hajibabai and Ouyang, 2016). Alternatively, value function can be provided for limited time periods so as to simplify the look-ahead model (Al-kanj et al., 2016). In both approaches, the states, actions, and time are discretized to tackle the computational intractability. In this paper, the set of available vehicles $C^{t}$ in the state space obtains fix values based on traffic demand distribution from a microscopic traffic simulation (e.g., VISSIM (PTV GROUP, 2014)) to partially reduce the state space and simplify the look-ahead model. The value function is then estimated by $\widetilde{V}^{t+1}\left(X^{t+1}, \mathscr{V}^{t+1}\right)$, which is only a function of vehicle locations and speeds. The decisions at each time $t$ is made based on:

$$
\mathscr{A}^{*^{t}}\left(S^{t}\right)=\operatorname{argmin}_{a^{t} \in \mathscr{A}^{t}\left(S^{t}\right)}\left(\delta_{v}^{t}\left(X^{t}, \mathscr{V}^{t}, a^{t}\right)+\widetilde{V}^{t+1}\left(X^{t+1}, \mathscr{V}^{t+1}\right)\right)
$$

subject to (1b)-(1g) and (3a)-(3f), where $\mathscr{A}^{t}$ denotes the vector of feasible actions and $\mathscr{A}^{*}$ represents the near-optimal actions at time $t$. Tree search scenarios can be applied to find the approximation of value function, i.e., $\widetilde{V}^{t+1}\left(X^{t+1}, \mathscr{V}^{t+1}\right)$. However, the combination of all feasible actions at time $t$ and new information arriving in the following time periods, makes the tree to grow exponentially. We, therefore, apply MCTS algorithm that is very helpful to solve non-deterministic decision-making problems (Browne et al., 2012; Munos, 2014) and enables the decision-makers to include uncertainties to the search by adding possible random realizations into the tree.

The MCTS algorithm generally consists of four steps (Browne et al., 2012; Munos, 2014): selection, expansion, simulation, and back-propagation. In the selection step, based on the existing actions and their values, an action is selected until an expandable state is reached, while the expansion step adds a state to the tree. In the simulation step, the value of added state is calculated to determine its worthiness to keep and finally, the back-propagation step updates the value functions of predecessor states based on the value of recently added states. In this paper, selection, expansion, and simulation steps are integrated. Extensive studies have used MCTS algorithm on deterministic problems (refer to Browne et al. (2012) for more details). To handle the uncertainty, stochastic information (available in each time $t$ ), is averaged or added to the tree search.

In this paper, we include the exogenous information obtained at the beginning of $t \in \Gamma$ in the tree search and observe its impacts. In the look-ahead model, the index $t^{\prime}$ represents the time steps within the tree. Then, the approximation of value function is divided into pre-decision value function $\widetilde{V}^{t, t^{\prime}}\left(\widetilde{S}^{t, t^{\prime}}\right)$ and post-decision value function $\widetilde{V}_{a}^{t, t^{\prime}}\left(\widetilde{S}_{a}^{t, t^{\prime}}\right)$ for $t^{\prime}=t, \ldots, t+H-1$ that includes the effects of adding exogenous information, where $\widetilde{S}^{t}=\left\{X^{t}, \mathscr{V}^{t}\right\}$ and $H$ represents a limited time horizon as a threshold for tree expansion (i.e., inner tree iterations). Besides, $\widetilde{\mathscr{A}}^{t, t^{\prime}}\left(\widetilde{S}^{t, t^{\prime}}\right)$ denotes the set of decisions, where the unexplored decisions are defined by $\widetilde{\mathscr{A}}_{u}^{t, t^{\prime}}\left(\widetilde{S}^{t, t^{\prime}}\right)$ and its complement set $\widetilde{\mathscr{A}}_{e}^{t, t^{\prime}}\left(\widetilde{S}^{t, t^{\prime}}\right)$ presents the set of explored decisions. Moreover, $\widetilde{\Omega}^{t, t^{\prime}+1}\left(\widetilde{S}_{a}^{t, t^{\prime}}\right)$ represents all possible outcomes depending on policy $\pi$ at time $t^{\prime}+1$ given state $\widetilde{S}_{a}^{t, t^{\prime}}$ and again, the explored and unexplored sets of possible outcomes are identified by subscripts $u$ and $e$, respectively.

In stochastic MCTS, the pre-decision states $\widetilde{S}^{t, t^{\prime}}$ are given and the post-decision states $\widetilde{S}_{a}^{t, t^{\prime}}$ are obtained by decisions $\widetilde{a}^{t, t^{\prime}}$. When the
acceleration rates are assigned to vehicles, a sample of possible outcomes $\widetilde{\omega} \in \widetilde{\Omega}^{t, t^{\prime}+1}\left(\widetilde{S}_{a}^{t, t^{\prime}}\right)$ is generated to introduce unpredicted states of the intersection at time $t$. Thus, the stochasticity is incorporated in MCTS following each decision. Our algorithm framework follows the stochastic MCTS with the computational budget of $N$ iterations: given a current state $S^{t}$, we create a state $\widetilde{S}^{t, t^{\prime}}$ as a root node of the tree, generate a MCTS algorithm, and build a look-ahead model at each time $t$ to estimate the value functions $\widetilde{V}^{t+1}$ and return the vector of near-optimal actions $\mathscr{A}^{*^{t}}$ in time period $t$.

In the selection step, there is a trade-off between exploiting and exploring of each generated node. When the number of elements in $\widetilde{\mathscr{A}}_{e}^{t, t^{\prime}}\left(\widetilde{S}^{t, t^{\prime}}\right)$ meets the threshold of having enough possible actions $d^{t h r}$, an action shall be selected. $d^{t h r}$ is the maximum number of actions in the set of possible actions. Following upper confidence-bounding for trees (UCT) ${ }^{1}$ (Browne et al., 2012), our decisions on acceleration rates $\widetilde{a}_{t, t^{\prime}}^{*}$ will be determined by

$$
\widetilde{a}^{t, t^{\prime}}=\operatorname{argmax}_{\widetilde{a} t, t^{\prime} \in \widetilde{\mathscr{A}}_{e}^{t, t^{\prime}}}\left(\widetilde{S}^{t, t^{\prime}}\right)\left(-\left(\widetilde{\delta}_{v}^{t}\left(\widetilde{S}^{t, t^{\prime}}, \widetilde{a}^{t, t^{\prime}}\right)+\widetilde{V}_{a}^{t, t^{\prime}}\left(\widetilde{S}_{a}^{t, t^{\prime}}\right)\right)+\beta \sqrt{\left.\frac{\ln N\left(\widetilde{S}^{t, t^{\prime}}\right)}{N\left(\widetilde{S}^{t, t^{\prime}}, \widetilde{a}^{t, t^{\prime}}\right)}\right)},\right.
$$

where $\beta$ is an adjustable parameter to balance exploration and exploitation, $N\left(\widetilde{S}^{t, t^{\prime}}\right)$ represents the number of visiting states $\widetilde{S}^{t, t^{\prime}}$, and $N\left(\widetilde{S}^{t, t^{\prime}}, \widetilde{a}^{t, t^{\prime}}\right)$ identifies the number of times a decision $\widetilde{a}^{t, t^{\prime}}$ is taken from state $\widetilde{S}^{t, t^{\prime}}$ during the tree search process. After making a decision $\widetilde{a}^{t, t^{\prime}}$, the state of an intersection neighborhood will be $\widetilde{S}_{a}^{t, t^{\prime}}$, where we add a sample realization of exogenous information to reach the next pre-decision state $\widetilde{S}^{t, t^{\prime}+1}=S^{M, a}\left(\widetilde{S}_{a}^{t, t^{\prime}}, \widetilde{W}^{t, t^{\prime}+1}\right)$.

The general algorithm framework follows. At each tree node, when the state $S^{t, t^{\prime}}$ is expandable (before reaching threshold, $H$ ), the optimization problem (1b)-(1f), (3a)-(3f), and (5) is solved for a limited time horizon over $t^{\prime}$ that returns the acceleration rates for one time period $t$. Feasible solutions (i.e., vehicle trajectories with no travel conflicts), if found, imply that additional actions are worth to be added to the tree, otherwise actions need to be modified. Therefore, the feasible actions and subsequent nodes that store updated information from applying the actions, will be added to tree. A tentative action to substitute an infeasible action is to assign higher deceleration (i.e., negative acceleration) rates from the set $\mathscr{A}_{F}$ (that includes fractions of maximum deceleration rate) to vehicles who tend to reduce their speed. We keep reducing the speed of vehicles until we get a feasible solution, otherwise (in a worst case) vehicles will get the maximum deceleration rate to stop completely after several time periods. Then, in the back-propagation step, the value function at the added nodes will be transmitted back to the predecessor nodes to update their values until reaching the root state. The number of visits of all states predecessor to a state $\widetilde{S}^{t, t^{\prime}}$ are increased by one and their values are updated based on the near-optimal value of descendant nodes. By assuming $\widetilde{S}^{t, t^{\prime}}=S^{M, a}\left(\widetilde{S}_{a}^{t, t^{*}}, \widetilde{W}^{t, t^{*}+1}\right)$, the value of $\Delta \leftarrow \widetilde{f}^{t}\left(\widetilde{S}^{t, t^{*}}, \widetilde{a}^{t, t^{*}}\right)+\widetilde{V}_{a}^{t, t^{*}}\left(\widetilde{S}_{a}^{t, t^{*}}\right)$ is the updated value for the ancestor post-decision state. Therefore, the value function of the ancestor pre-decision state shall be updated by the updated value of the post-decision state over updated number of visits, i.e., $\widetilde{V}^{t, t^{*}}\left(\widetilde{S}^{t, t^{*}}\right) \leftarrow \widetilde{V}^{t, t^{*}}\left(\widetilde{S}^{t, t^{*}}\right)+\frac{\Delta-\widetilde{V}^{t, t^{*}}\left(\widetilde{S}^{t, t^{*}}\right)}{N\left(\widetilde{S}^{t, t^{*}}\right)}$. The entire process is repeated until the end of the planning horizon. Fig. 3 presents the proposed look-ahead policy to find the near-optimal vehicle trajectories, while Fig. 4 illustrates the proposed MCTS algorithm. In the MCTS algorithm, the tree policy section explores the feasible actions to expand the tree and exploit each action where the back-propagation step updates the value function. When the tree search terminates, the near-optimal acceleration rates will be selected, which correspond to the best value from the root node.

## 5. Numerical experiments

The proposed solution algorithm is coded in JAVA and run on a desktop computer with quad core 3.6 GHz CPU and 16 GB of memory. VISSIM microscopic traffic simulator is used for generating vehicle arrivals at an intersection neighborhood and measure the mobility performance measures (i.e., calculating the number of completed trips, average travel time, and average delay). CAV information is passed between VISSIM and our look-ahead optimization model developed in JAVA through VISSIM's COM interface (PTV GROUP, 2014).

### 5.1. Dataset

Problem (1b)-(1f), (3a)-(3f), and (5) and the MCTS solution framework in Section 4 are applied to an isolated four-leg intersection (see Fig. 2) with an exclusive lane at each intersection approach for left-turn movements. It is assumed that vehicles have chosen their lanes before they are detected by the intersection. We have conservatively assumed a detection range of 650 ft, which is significantly less than the typical 1000 ft detection range. Besides, CAVs send their locations and speeds to the SICL system within 650 ft range and receive speed assignments to reach their destinations, i.e., $X_{r_{i}}$. To precisely update vehicle locations and avoid movement conflicts, the length of time periods is designed to be sufficiently short (i.e., 0.2 sec ). Besides, the CAV's length $L_{v}$ is assumed to be 20 ft and the safety distance between them is 5.2 ft. Besides, the CAV reaction time is assumed to be 0.5 sec. The time horizon threshold for the inner tree iterations is set to $H=10$, where the number of optimization iterations is set to 25 . Note that in

[^1]![](https://cdn.mathpix.com/cropped/f7cbcf4d-7353-4369-a735-9add015efac1-08.jpg?height=709&width=737&top_left_y=185&top_left_x=576)
Fig. 3. The look-ahead policy to find near-optimal vehicle trajectories.

![](https://cdn.mathpix.com/cropped/f7cbcf4d-7353-4369-a735-9add015efac1-08.jpg?height=1374&width=1533&top_left_y=985&top_left_x=179)
Fig. 4. The proposed MCTS algorithm framework.

Table 1
Model parameters.
| Parameter | Value |
| :--- | :--- |
| Desired speed | 46 ft/sec |
| Maximum Acceleration | $13.12 \mathrm{ft} / \mathrm{sec}^{2}$ |
| Maximum Deceleration | $-11.15 \mathrm{ft} / \mathrm{sec}^{2}$ |


![](https://cdn.mathpix.com/cropped/f7cbcf4d-7353-4369-a735-9add015efac1-09.jpg?height=699&width=1390&top_left_y=548&top_left_x=250)
Fig. 5. Trajectories of vehicles in lane 8 for case 7 traffic demand in the proposed algorithm.

our numerical results exogenous information is ignored to allow a fair comparison of the proposed approach with the existing intersection control methods. Table 1 presents values for the desired speed, maximum acceleration rate, and maximum deceleration rate in each lane.

To evaluate the performance of the proposed solution technique, nine different scenarios are considered based on traffic volumes in [500, 1200] veh/h/ln for through movements and [100, 400] veh/h/ln for exclusive left-turn movements using VISSIM demand distribution. In addition, the numerical results in 15 min analysis periods (after a 1-min warm up), are compared to those of fixed-time and fully-actuated control signal systems (with optimal timing plans) developed by VISTRO (PTV GROUP, 2014).

### 5.2. Results

Trajectories of vehicles in lane 8 (see Fig. 2) are shown in Fig. 5 for the analysis period, where the dashed line shows the intersection location. Vehicles travel at their desired speed and maintain safe headways until a possible conflict enforces them to decelerate.

After passing the conflict region or gaining enough headway, they accelerate until they reach to their desired speed again. Fig. 6(a) and (b) present vehicle trajectories for fully-actuated and fixed-time signal control. It is apparent that vehicles stop at the intersections before the red signal; however, under SICL, vehicles slightly reduce their speed to avoid the conflict and continue traveling through the intersection. As such, we expect the SICL methodology to yield significantly lower delay compared to the fixedtime and fully-actuated control signal settings.

Average travel time, average delay, and completed number of trips are summarized in Table 2 for each scenario. Delay for each vehicle is defined as the difference of travel time in the free flow conditions and actual travel time.

In Table 2, the intersection layout and demand pattern are identical for all approaches in each case. As shown in the table, for low demand levels (less than 600 veh/h/ln), all three approaches find comparable number of completed trips. However, the proposed algorithm finds average travel times and delays that are significantly lower than the fixed-time and fully-actuated control signal settings. By increasing the demand pattern to 750 veh $/ \mathrm{h} / \mathrm{ln}$ and beyond, the difference between the number of completed trips

![](https://cdn.mathpix.com/cropped/f7cbcf4d-7353-4369-a735-9add015efac1-10.jpg?height=1114&width=1394&top_left_y=183&top_left_x=250)
Fig. 6. Trajectories of vehicles before the intersection in lane 8 for case 7 traffic demand in (a) fully-actuated signal control and (b) fixed-time signal control.

Table 2
Summary of the mobility measures of proposed algorithm for symmetric demand.
| Case | Through demand (veh/h/ln) | Left-turn demand (veh/h/ln) | Proposed algorithm |  |  | Fully-actuated signal control |  |  | Fixed-time signal control |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | Ave. delay (sec/veh) | Ave. travel time (sec/veh) | \# completed trips | Ave. delay (sec/veh) | Ave. travel time (sec/veh) | \# completed trips | Ave. delay (sec/veh) | Ave. travel time (sec/veh) | \# completed trips |
| 1 | 500 | 100 | 0.108 | 29.36 | 676 | 29.22 | 70.57 | 557 | 31.00 | 72.33 | 557 |
| 2 | 600 | 120 | 0.12 | 29.37 | 793 | 37.25 | 80.44 | 658 | 41.45 | 84.23 | 640 |
| 3 | 750 | 150 | 0.131 | 29.39 | 946 | 56.34 | 104.63 | 761 | 64.33 | 110.35 | 784 |
| 4 | 900 | 170 | 0.137 | 29.4 | 1078 | 82.25 | 133.53 | 742 | 84.06 | 138.88 | 681 |
| 5 | 1000 | 200 | 0.14 | 29.4 | 1197 | 90.17 | 144.57 | 741 | 92.41 | 146.22 | 844 |
| 6 | 1100 | 300 | 0.15 | 29.42 | 1421 | 113.03 | 178.38 | 825 | 116.53 | 180.77 | 945 |
| 7 | 1200 | 400 | 0.17 | 29.45 | 1574 | 117.89 | 180.38 | 690 | 126.48 | 179.48 | 722 |


becomes large as well, indicating that our algorithm significantly increases intersection capacity.
To evaluate the performance of the intersection under asymmetric demand pattern, two additional cases are analyzed, i.e., case 8 and case 9 each at different traffic demands, as follows. The results are compared in Table 3.

Table 3
Summary of the mobility measures of proposed algorithm for asymmetric demand.
| Case | Proposed algorithm |  |  | Fully-actuated signal control |  |  | Fixed-time signal control |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Ave. delay (sec/veh) | Ave. travel time (sec/veh) | \# completed trips | Ave. delay (sec/veh) | Ave. travel time (sec/veh) | \# completed trips | Ave. delay (sec/veh) | Ave. travel time (sec/veh) | \# completed trips |
| 8 | 0.11 | 29.39 | 897 | 58.11 | 102.6 | 759 | 89.82 | 143.5 | 587 |
| 9 | 0.144 | 29.41 | 1279 | 104.28 | 168.32 | 808 | 106.62 | 170.16 | 925 |


i Case 8, traffic demand at:

- 920 and 200 veh/h/ln for through and left-turn movements in east and west bound, and
- 500 and 100 veh/h/ln for through and left-turn movements in north and south bound.

ii Case 9, traffic demand at:

- 1200 and 400 veh/h/lnfor through and left-turn movements in east and west bound, and
- 750 and 150 veh/h/ln for through and left-turn movements in north and south bound.

As expected, our proposed methodology eliminates complete stops at the intersection, which leads to significantly less travel delay. Besides, it results in higher intersection throughput compared to conventional control systems.

To ensure that the improvements in the traffic operations do not negatively affect traffic safety, we analyze two surrogate safety measures: (i) average time to collision (TTC) and (ii) the number of crashes under two TTC thresholds of 0.75 sec and 1.5 sec . The analyses are performed in SSAM software (Gettman and Head, 2003; Pu and Joshi, 2008) and summarized in Table 4 for different traffic conditions.

Table 4
SSAM results for average TTC and number of accidents in traffic conditions.
| Case | Proposed algorithm |  |  |  |  | Fully-actuated signal control |  |  | Fixed-time signal control |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Ave. TTC (sec) $D=5.2 \mathrm{ft}$ | Ave. TTC (sec) $D=23 f t$ | \# accidents $\left(T^{*}=0.75\right) D=5.2 \mathrm{ft}$ \& $D=23 \mathrm{ft}$ | \# accidents ( $T=1.5$ ) $D=5.2 \mathrm{ft}$ | \# accidents ( $T=1.5$ ) $D=23 \mathrm{ft}$ | Ave. TTC (sec) | \# accidents $(T=0.75)$ | \# accidents ( $\mathrm{T}=1.5$ ) | Ave. TTC (sec) | \# accidents ( $T=0.75$ ) | \# accidents ( $T=1.5$ ) |
| 1 | 1.3 | > 1.5 | 0 | 1 | 0 | 0.86 | 25 | 68 | 0.66 | 25 | 48 |
| 2 | > 1.5 | > 1.5 | 0 | 0 | 0 | 0.9 | 28 | 81 | 0.67 | 35 | 67 |
| 3 | > 1.5 | > 1.5 | 0 | 0 | 0 | 1.12 | 19 | 107 | 1.36 | 1 | 29 |
| 4 | 1 | > 1.5 | 0 | 1 | 0 | 1.12 | 20 | 105 | 0.83 | 17 | 45 |
| 5 | 1.5 | > 1.5 | 0 | 1 | 0 | 1.12 | 22 | 122 | 0.9 | 24 | 65 |
| 6 | 1.04 | > 1.5 | 0 | 2 | 0 | 1.25 | 11 | 101 | 0.76 | 38 | 83 |
| 7 | 1.2 | > 1.5 | 0 | 5 | 0 | 1.15 | 15 | 93 | 0.93 | 10 | 38 |
| 8 | > 1.5 | > 1.5 | 0 | 0 | 0 | 1.05 | 22 | 90 | 0.73 | 32 | 68 |
| 9 | 1.4 | > 1.5 | 0 | 2 | 0 | 1.2 | 12 | 106 | 0.74 | 32 | 70 |


*: assigned threshold for TTC in SSAM in sec.
Number of accidents ranges between 0 and 5 under SICL when safety distance and maximum TTC are, respectively, set to 5.2 ft and 1.5 sec. These values are significantly less than number of accidents under fixed-time and fully-actuated signal control strategies. Increasing the safety distance to 23 ft yields more than 1.5 sec of individual TTC values. As a result, average TTC values are more than 1.5 sec as well. As such, the proposed algorithm improves traffic safety in the intersection neighborhood.

When the safety distance is set to 5.2 ft, the proposed algorithm results in no crashes for TTC threshold of 0.75 sec under all demand levels. This is not the case for the fixed-time and fully-actuated signal control strategies. Similarly, the proposed algorithm results in significantly fewer crashes than fixed-time and fully-actuated signal control strategies when the TTC threshold is set to 1.5 sec . When the safety distance is set to 0.75 sec , the proposed algorithm finds zero crashes for both 0.75 sec and 1.5 sec TTC thresholds, while other signal control strategies result in substantial number of crashes. These observations indicate that the proposed algorithm significantly improves the safety of traffic operations at the intersection.

Fig. 7 shows sensitivity of two performance measures (i.e., average travel time and the number of completed trips) to the safety distance for case 7. The number of completed trips reduces with an increase in the value of the safety distance. In fact, increasing the

![](https://cdn.mathpix.com/cropped/f7cbcf4d-7353-4369-a735-9add015efac1-11.jpg?height=502&width=1187&top_left_y=1842&top_left_x=353)
Fig. 7. Sensitivity analysis on different safety distances for traffic demand under case 7.

![](https://cdn.mathpix.com/cropped/f7cbcf4d-7353-4369-a735-9add015efac1-12.jpg?height=693&width=1199&top_left_y=185&top_left_x=345)
Fig. 8. Comparison of variance and average speed for traffic demand under cases 1-7.

△ Average speed in fixed time traffic signal ○ Average speed in actuated traffic signal

| ○ Average speed in proposed algorithm | □ Speed variance in fixed time traffic signal |
| :--- | :--- |
| ◇ Speed variance in actuated traffic signal | □ Speed variance in proposed algorithm |

Fig. 8. Comparison of variance and average speed for traffic demand under cases 1-7.

safety distance from 5.2 to 23 ft has reduced the number of completed trips from 1574 to 1227 vehicles. On the other hand, safety distance has a minimal effect on the average travel time, as it only increases the value by at most 0.18 sec .

Fig. 8 shows the variance and average speed of vehicles passing through the intersection for demand patterns under cases 1-7. Under fixed-time and fully-actuated signal control strategies, average speed decreases with an increase in the demand level, as expected. On the other hand, the proposed algorithm maintains the average speed around 45 ft/sec for all demand levels, while keeping speed variance close to zero. These observations indicate that the proposed algorithm is capable of working under various demand levels and maintaining efficient intersection operations.

### 5.3. Benchmark

The near-optimal vehicle trajectories are derived in each time period using the SICL methodology. MCTS algorithm provides an accurate estimation of decisions in each time period to handle the computation complexity over the entire planning horizon. To examine the accuracy of the estimation, a theoretical lower-bound is defined by relaxing constraints (3a)-(3f) from the optimization problem (1b)-(1f), (3a)-(3f), and (5). This assumption, converts the MILP problem to a linear program (LP), where the CAV trajectories can be found across the entire planning horizon. Table 5 presents the objective function value found by the proposed algorithm and the LP, number of completed trips, average delay and computation time for the demand pattern in case 7.

The results indicate that the proposed methodology finds near-optimal solutions by avoiding all accidents. The average delay of vehicles drops from 0.17 sec to 0.06 sec in the LP because vehicles do not reduce their speed to avoid conflicting movements. However, the LP's runtime increases by around 9 times compared to our algorithm, as it needs to be solved centrally over all time periods. Expectedly, the number of completed trips is the same in both solutions and it turns out that our approach alters vehicles' speeds as little as possible to provide safe maneuvers. This can be done by changing the headway of vehicles without reducing the intersection throughput. As the LP does not enforce the conflict avoiding constraints, i.e., (3a)-(3f), it results in a very high number of accidents for any TTC threshold. In other words, vehicles travel at their maximum desired speed and do not avoid any conflict, which results in lower objective value compared to the proposed algorithm. On the other hand, the objective value of the proposed algorithm increases by increasing the safety distance $D$ as vehicles reduce their speed to avoid accidents, which is not the case in the LP. Thus, the gap between the objective values increases.

Table 5
Comparison with the benchmark solution obtained by the linear program.
|  | Computation time (sec) | \# completed trips | Ave. delay (sec/veh) | \# accidents | Objective value (ft) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Proposed algorithm | 5166 | 1574 | 0.17 | 0 | $1.79 \mathrm{E}+08$ |
| LP | 48,106 | 1457 | 0.06 | 525 | $1.57 \mathrm{E}+08$ |


[^2]Table 6
Comparison with the benchmark solution obtained by GAMS.
|  | Computation time (sec) | \# completed trips | Objective value (ft) |
| :--- | :--- | :--- | :--- |
| GAMS | 99,537.6 | 35 | $1.684 \mathrm{E}+09$ |
| Proposed approach | 1642.5 | 472 | $5.919 \mathrm{E}+07$ |


*Study period is 5 min.
The performance of the proposed algorithm is also evaluated through a comparison to the solutions found directly from coding the original non-linear formulation (1a)-(1g) in GAMS (Brook et al., 1988). GAMS has not been able to solve the problem when the study period was more than 5 min. Even with a five-minute study period, GAMS solutions (over a long computation time) are significantly worse than the solutions from the proposed algorithm. Table 6 presents the computation outcomes.

## 6. Conclusion

This paper presents a novel control logic that determines near-optimal trajectories for CAVs to cross intersections without any movement conflict. Once a vehicle approaches the intersection, basic safety messages will be captured by the proposed methodology through a reliable wireless connection. Then the maneuver for each CAV is designed by the proposed optimization framework under safety constraints. In other words, CAVs travel at their desired speed for a fixed time horizon until they receive recommendations from our system to change their trajectories by acceleration or deceleration to avoid collisions given the captured state of the system. The proposed SICL methodology is able to find the near-optimal CAV trajectories under uncertain demand, stochastic events, and high traffic volumes approaching the intersections.

The proposed algorithm is applied to an isolated intersection under various demand levels and compared to fixed-time and fullyactuated signal control strategies, and two benchmark solutions. Computational results show that the proposed algorithm can solve the problem efficiently, significantly improve all traffic operations performance measures in both under-saturated and over-saturated traffic conditions, and maintain safe intersection operations. Travel time is reduced by 59.4\%-83.7\% compared to fixed-time and fully-actuated intersection control strategies under various demand patterns. In addition, the number of stops drops to zero in all cases by adjusting vehicles' speeds in the intersection neighborhood. The speed variance is also decreased, which helps reduce fuel consumption with a positive impact on environmental sustainability. It will be interesting in the future to expand the methodology to include multiple intersections in an urban street network using a distributed optimization and coordination schemes.

## References

Al-kanj, L., Powell, W.B., Bouzaiene-ayari, B., 2016. The Information-Collecting Vehicle Routing Problem : Stochastic Optimization for Emergency Storm Response. arXiv preprint arXiv:1605.05711, pp. 1-32.
America, P., 2014. PTV VISTRO User Manual.
Azimi, S.R., Bhatia, G., Rajkumar, R.R., Mudalige, P. 2013. Reliable intersection protocols using vehicular networks. In: Proceedings of the ACM/IEEE 4th International Conference on Cyber-Physical Systems, ACM, pp. 1-10.
Bent, R.W., Van Hentenryck, P., 2004. Scenario-based planning for partially dynamic vehicle routing with stochastic customers. Oper. Res. 52(6), 977-987.
Brook, A., Kendrick, D., Meeraus, A., 1988. GAMS, a user's guide. ACM Signum Newsletter. ACM 23 (3-4), 10-11.
Browne, C.B., Powley, E., Whitehouse, D., Lucas, S.M., Cowling, P.I., Rohlfshagen, P., Tavener, S., Perez, D., Samothrakis, S., Colton, S., 2012. A survey of monte carlo tree search methods. IEEE Trans. Comput. Intell. AI Games 4 (1), 1-43.
Dai, P. et al., 2016. A Convex Optimization Based Autonomous Intersection Control Strategy in Vehicular Cyber-Physical Systems. In: Ubiquitous Intelligence \& Computing, Advanced and Trusted Computing, Scalable Computing and Communications, Cloud and Big Data Computing, Internet of People, and Smart World Congress (UIC/ATC/ScalCom/CBDCom/IoP/SmartWorld), 2016 Intl IEEE Conferences, pp. 203-210. https://doi.org/10.1109/UIC-ATC-ScalCom-CBDCom-IoP-SmartWorld.2016.0050.
Dresner, K., Stone, P., 2004. Multiagent traffic management: a reservation-based intersection control mechanism. In: Proceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems, 2004. AAMAS 2004., (July), pp. 530-537. doi: 10.1109/AAMAS.2004.242421.
Dresner, K., Stone, P., 2008. A multiagent approach to autonomous intersection management. J. Artificial Intell. Res. 31, 591-656.
Faye, S., Chaudet, C., Demeure, I., 2012. A distributed algorithm for adaptive traffic lights control. In: 2012 15th International IEEE Conference on Intelligent Transportation Systems, pp. 1572-1577. doi: 10.1109/ITSC.2012.6338671.
Gettman, D., Head, L., 2003. 'Surrogate safety measures from traffic simulation models. Transport. Res. Record: J. Transport. Res. Board Transport. Res. Board National Acad. 1840, 104-115.
Godfrey, G.A., Powell, W.B., 2001. An adaptive, distribution-free algorithm for the newsvendor problem with censored demands, with applications to inventory and distribution. Manage. Sci. 47 (8), 1101-1112. http://dx.doi.org/10.1287/mnsc.47.8.1101.10231.
Guler, S.I., Menendez, M., Meier, L., 2014. Using connected vehicle technology to improve the efficiency of intersections. Transport. Res. Part C: Emerg. Technol.Elsevier 46, 121-131.
Hajbabaie, A., Benekohal, R.F., 2015. A program for simultaneous network signal timing optimization and traffic assignment. IEEE Trans. Intell. Transport. Syst. 16 (5), 2573-2586. http://dx.doi.org/10.1109/TITS.2015.2413360.
Hajbabaie, A., Benekohal, R.F., (Ray), 2013. Traffic signal timing optimization. Transport. Res. Record: J. Transport. Res. Board 2355 (1), 10-19. http://dx.doi.org/10. 3141/2355-02.
Hajibabai, L., Ouyang, Y., 2016. Dynamic snow plow fleet management under uncertain demand and service disruption. IEEE Trans. Intell. Transport. Syst. 17 (9), 2574-2582. http://dx.doi.org/10.1109/TITS.2016.2520918.
Islam, S.M.A., Hajbabaie, A., 2017. Distributed coordinated signal timing optimization in connected transportation networks'. Transport. Res. Part C: Emerg. Technol.Elsevier 80, 272-285. http://dx.doi.org/10.1016/j.trc.2017.04.017.
Lee, J., Park, B.B., Malakorn, K., So, J.J., 2013. Sustainability assessments of cooperative vehicle intersection control at an urban corridor. Transport. Res. Part C:Emerg. Technol. Elsevier 32, 193-206.
Lee, J., Park, B., 2012. Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment. IEEE Trans.

Intell. Transport. Syst. 13 (1), 81-90. http://dx.doi.org/10.1109/TITS.2011.2178836.
Li, Z., Elefteriadou, L., Ranka, S., 2014. Signal control optimization for automated vehicles at isolated signalized intersections. Transport. Res. Part C: Emerg. Technol. Elsevier 49, 1-18.
Ma, J., Li, X., Zhou, F., Hu, J., Park, B.B., 2017. Parsimonious shooting heuristic for trajectory design of connected automated traffic part II: computational issues and optimization. Transport. Res. Part B: Methodol. Elsevier 95, 421-441.
Mehrabipour, M., Hajbabaie, A., 2017. A cell-based distributed-coordinated approach for network-level signal timing optimization. Comput.-Aided Civil Infrastruct. Eng. 32 (7), 599-616. http://dx.doi.org/10.1111/mice.12272.
Muller, E.R., Carlson, R.C., Junior, W.K., 2016. Intersection control for automated vehicles with MILP. IFAC-PapersOnLine. Elsevier B.V., 49(3), pp. 37-42. doi: 10. 1016/j.ifacol.2016.07.007.
Munos, R., 2014. From bandits to Monte-Carlo tree search: The optimistic principle applied to optimization and planning. Found. Trends Mach. Learn. 7 (1), 1-129.
National Automated Highway System Consortium, 1996. Milestone 2 Reporter.
NHTSA, 2014. Traffic Safety Facts 2014. National Highwat Traffic Safety Admin, pp. 1-6.
Powell, W.B., Simao, H.P., Bouzaiene-Ayari, B., 2012. Approximate dynamic programming in transportation and logistics: a unified framework. EURO J. Transport. Logist. 1 (3), 237-284. http://dx.doi.org/10.1007/s13676-012-0015-8.
Pu, L., Joshi, R., 2008. Surrogate Safety Assessment Model (SSAM)- SOFTWARE USER MANUAL.
Puterman, M.L., 2014. Markov decision processes: discrete stochastic dynamic programming.
Raravi, G., Shingde, V., Ramamritham, K., Bharadia, J. 2007. Merge algorithms for intelligent vehicles. In: Next Generation Design and Verification Methodologies for Distributed Embedded Control Systems, Springer, Dordrecht, pp. 51-65.
Schrank, D., Eisele, B., Lomax, T., Bak, J. 2015. 2015 Urban Mobility Scorecard. Texas A\&M Transportation Institute.
Shahidi, N., 2010. A Delayed Response Policy for Autonomous Intersection Management.
Sun, W., Zheng, J., Liu, H.X., 2017. A capacity maximization scheme for intersection management with automated vehicles. Transport. Res. Procedia Elsevier 23, 121-136.
Vasirani S., Ossowski, M.V. 2012. A market-inspired approach for intersection management in urban road traffic networks'. J. Artificial Intell. Res., 43, pp. 621-659 doi: 10.1613/jair.3560.
Wei, Y., Liu, J., Li, P., Zhou, X. 2016. Longitude trajectory optimization for autonomous vehicles: An approach based on simplified car-following model. In: Transportation Research Board 95th Annual Meeting 2016 (No. 16-6895).
Wu, J., Abbas-Turki, A., El Moudni, A., 2012. Cooperative driving: An ant colony system for autonomous intersection management. Appl. Intell. 37 (2), 207-222. http://dx.doi.org/10.1007/s10489-011-0322-z.
Wuthishuwong, C., Traechtler, A. and Bruns, T., 2015. Safe trajectory planning for autonomous intersection management by using vehicle to infrastructure communication - Springer. doi: 10.1186/s13638-015-0243-3.
Zhou, F., Li, X., Ma, J., 2017. Parsimonious shooting heuristic for trajectory design of connected automated traffic part I: theoretical analysis with generalized time geography. Transport. Res. Part B: Methodol. Elsevier 95, 394-420.
Zohdy, I.A., Rakha, H.A., 2014. Intersection Management via Vehicle Connectivity: The Intersection Cooperative Adaptive Cruise Control System Concept. J. Intell. Transport. Syst., 0(JUNE 2014), pp. 1-16. doi: 10.1080/15472450.2014.889918.


[^0]:    * Corresponding author.
    E-mail address: leila.hajibabaidizaji@stonybrook.edu (L. Hajibabai).

[^1]:    ${ }^{1}$ UCT is widely used in computer science literature and established for solving maximization problems (Browne et al., 2012).

[^2]:    *Study period is 15 min.

