# Real-time Cooperative Vehicle Coordination at Unsignalized Road Intersections 

Jiping Luo, Tingting Zhang, Member, IEEE, Rui Hao, Donglin Li, Chunsheng Chen, Zhenyu Na, Member, IEEE, and Qinyu Zhang, Senior Menber, IEEE


#### Abstract

Cooperative coordination at unsignalized road intersections, which aims to improve the driving safety and traffic throughput for connected and automated vehicles, has attracted increasing interests in recent years. However, most existing investigations either suffer from computational complexity or cannot harness the full potential of the road infrastructure. To this end, we first present a dedicated intersection coordination framework, where the involved vehicles hand over their control authorities and follow instructions from a centralized coordinator. Then a unified cooperative trajectory optimization problem will be formulated to maximize the traffic throughput while ensuring the driving safety and long-term stability of the coordination system. To address the key computational challenges in the real-world deployment, we reformulate this non-convex sequential decision problem into a model-free Markov Decision Process (MDP) and tackle it by devising a Twin Delayed Deep Deterministic Policy Gradient (TD3)-based strategy in the deep reinforcement learning (DRL) framework. Simulation and practical experiments show that the proposed strategy could achieve near-optimal performance in sub-static coordination scenarios and significantly improve the traffic throughput in the realistic continuous traffic flow. The most remarkable advantage is that our strategy could reduce the time complexity of computation to milliseconds, and is shown scalable when the road lanes increase.


Index Terms-connected and automated vehicles, intersection coordination, deep reinforcement learning

## I. INTRODUCTION

WITH the proliferation of traffic demand and vehicle ownership, the current transportation systems are now facing some serious social problems: traffic congestion, accidents, fuel consumption, air pollution, etc [1]-[5]. Road intersections where multiple roads cross and merge are the main bottlenecks for urban traffic. As reported in [6], [7], congestion and accidents in these areas cause substantial economic loss and tremendous safety hazards to society, and excessive travel time for drivers. Therefore, it is critical to develop dedicated intersection management systems, to allow vehicles to cross the intersection safely and efficiently.

Traditional traffic signal control (TSC) systems, where the traffic signal timing is predetermined according to historical traffic data, is widely used in current intersection coordination systems. However, this solution may not accommodate realtime traffic flow and bursty traffic demands [8]. Benefiting from the artificial intelligence, especially reinforcement learning (RL), the adaptive TSC which could adjust traffic signal timing according to real-time traffic demand, has been shown effectiveness in reducing traffic congestion [8]-[13]. However, this paradigm is still far from satisfactory with respect to both driving safety and traffic efficiency as over 90 percent of crashes are tied to improper human behaviors [7]. Moreover, the inconveniences of frequent stops and idling at intersections not only waste both fuel and time but also degrade the comfort of drivers and passengers [14]-[16].

In recent years, centralized coordination at unsignalized intersections has been widely studied to improve the performance of intersection control, especially when interoperations are required among vehicles. In this paradigm, there usually exists a coordination node that is fulfilled at the road side unit (RSU) to collect state information such as position, velocity, acceleration, heading angle, and intention of all involved vehicles via vehicle-to-infrastructure (V2I) communication links. After proper coordination algorithms, the maneuver instructions could be generated and forwarded to vehicles. Recent investigations show that centralized coordinators are advantageous in traffic throughput, collision-free, deadlockfree, passenger comfort, fuel efficiency, etc [14]-[18], making them suitable for real-world deployments. However, the design of centralized coordination algorithms confronts challenges due to the collision-free constraints and the complexity of the required maneuvers.

Lee an Park [19] proposed a cooperative vehicle intersection control strategy for connected and automated vehicles to reduce stop delay, total passing time, air pollution and fuel consumption. They adopted the following two strict assumptions: (1) Any two vehicles with overlapped paths should not exist at the intersection area at the same time, thereby eliminating the potential collisions coming from all conflicting approaches. (2) The acceleration of each vehicle is fixed from its initial position to the end of the intersection. Though this algorithm significantly improves the coordination performance compared with traditional TSC, it is apparent that the above two assumptions would impose limitations on the maximum coordination capacities of the intersection. Moreover, the formulated nonlinear constrained programming (NCP) problem was solved by employing search-based algorithms such as the Active Set Method (ASM), Interior Point Method (IPM) and genetic algorithm (GA) that could produce undesirable solutions and computation time.

The authors in [20]-[25] adopted similar rules that the whole intersection area was reserved for conflicting vehicles one after another, namely collision set (or critical set) strategy. The most notable difference is that the acceleration is treated as a continuous variable rather than a fixed value for the subsequent time slots, which could further improve the coordination efficiency and passenger comfort. However, due to the non-convexity of the formulated problems, some relaxations
such as the mixed integer programming (MIP) solutions are required, which inevitably increase computational complexity. In [23], [24], the stability of the coordination system was also considered as a metric to trade off long-term against shortterm performances. Aiming at the computational complexity, appropriate task offloading from the centralized coordinator was shown to be an option [26].

To address the underutilization issue of the intersection spatial resources, Kamal et al. [27] defined the cross-collision points (CCPs) inside the intersection area where the paths of any two conflicting vehicles intersect. The circle (with a certain radius) centering the CCP shows an approximate area where two vehicles are not allowed to enter at the same time. In addition, smooth traffic flows were achieved by solving an NCP problem at each time step over a finite horizon in the model predictive control (MPC) framework. However, as stated in this paper, MPC is usually computationally demanding and the average computation time is about 1.76 seconds per iteration, which is impractical in real-world deployments. Similarly, the intersection area can also be divided into multiple rectangular sub-zones (each could be reserved for one vehicle at a time) according to the combination of each pair of orthogonal lanes [14], [28], [29]. However, this reservation rule depends heavily on the road structure and spares no room to ensure system robustness.

More recently, the authors in [30] and [31] brought totally different insights that the cooperative trajectories can be optimized in the three-dimensional space with X, Y and T domains to harness the full potential of the intersection. In [31], a space-time resource searching (STRS) algorithm was proposed to search for compact and disjoint trajectories in the XYT domains, which allows multiple vehicles to share the intersection simultaneously and safely without any reservation rules, thereby providing tremendous coordination efficiency advantages over the aforementioned rule-based strategies. However, the STRS strategy shows obvious disadvantages in real-time processing performance due to the high dimensional searching space and the combination of dynamic programming (DP) and quadratic programming (QP).

In this paper, comprehensively considering the key issues, i.e., traffic throughput, driving safety, long-term coordination stability, computational complexity, system robustness and passenger comfort, at unsignalized intersections, a Twin Delayed Deep Deterministic Policy Gradient (TD3)-based centralized coordination strategy is designed in the deep reinforcement learning (DRL) framework. The contributions of this paper can be summarized as follows.

- Leveraging Rate Stability Theorem and Lyapunov Optimization Theorem, a unified cooperative trajectory optimization problem is formulated to maximize traffic throughput while ensuring driving safety and long-term stability of the coordination system. To harness the full coordination potential of the road intersections, we adopt the paradigm that all controlled vehicles could occupy the intersection simultaneously without any reservation rules. Safety redundancy is also considered to remedy the imperfections in communication, localization andcontrol, thus enhancing the robustness of the coordination algorithms.
- To rapidly solve the formulated non-convex sequential decision problem and obtain optimal disjoint trajectories in XYT domains, we transform this problem into a model-free Markov Decision Process (MDP) and elucidate the design of the state space, action space and reward function in detail. Then a TD3-based centralized coordinator is trained offline and can be deployed online to meet the stringent real-time coordination requirements. Moreover, a speed profile smoother is designed to smooth the original trajectories generated by the TD3 agent thereby improving passenger comfort.
- Simulation results and laboratorial experiments demonstrate that our TD3-based strategy could achieve nearoptimal performance in static coordination scenarios and significantly improve traffic throughput in continuous traffic flow. The most impressive advantage is that our strategy has millisecond computational latency, which outperforms most existing strategies by which the computational complexity increases exponentially with the increase of vehicles and lanes. Moreover, our strategy shows good scalability with respect to the number of road lanes. Only minor changes on the coordination model are required for intersections with different road structures without introducing additional mathematical analysis and assumptions.

The rest of this paper is organized as follows. First, the system model is presented in Section II, including the centralized coordination framework, vehicle kinematic model, collision detection, long-term coordination stability, formulation of optimal coordination problem, and benchmark solutions for comparison. In Section III, the formulated optimization problem is transformed and solved by devising a TD3-based strategy. Section IV presents extensive simulation results and experiments to illustrate the performance of the proposed strategy. Finally, the conclusion and future work are presented in Section V.

## II. System Model

## A. Intersection Coordination Framework

We consider a typical unsignalized intersection which consists of $R$ roads (usually we set $R=4$ ), each with $K$ lanes, as shown in Fig. 1. The area within the circle is called the Centralized Control Zone (CCZ) where a centralized coordinator is deployed at the road side unit (RSU) to collect the state information of the vehicles and make coordination decisions. The blue area is called the Conflict Area (CA) where a potential collision may occur.

In the CCZ, all vehicles will go through three different phases, i.e., waiting vehicle (WV), controlled vehicle (CV), and safe vehicle (SV). Once a vehicle enters the CCZ, it will travel at a low speed $v_{\text {low }}$ and wait for coordination, namely WV. The WVs need to keep a safe distance from the vehicles ahead and cannot enter the CA without permission. CVs represent the vehicles that update their state information to the centralized coordinator and need to leave the CCZ under

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-03.jpg?height=692&width=700&top_left_y=193&top_left_x=254)
Fig. 1. Graphic model of the intersection coordination system.

instructions. SVs are the CVs that have passed the CA without collision. If all the CVs turn green, the coordinator can focus on the next batch of CVs, and all SVs can leave the CCZ at a specified speed along their respective paths.

In the decision-making issue of unsignalized intersections, the large number of vehicles, high collision probability, and the inherent need for real-time processing make the centralized coordination system difficult to implement. For ease of analysis, we adopt the following assumptions:

1) The vehicles in the leftmost/rightmost lane of each road can turn left/right or go straight, and the rest can only go straight. Changing lane maneuvers is prohibited in the CCZ to ensure driving safety.
2) Each vehicle shares its driving states (position, velocity, etc.) and intentions (i.e., go straight, turn left and turn right) with the centralized coordinator via vehicle-toinfrastructure (V2I) communication links. Based on the collected information, the coordinator could broadcast the computed instructions (acceleration, steering angle, etc.) to the CVs without any error or packet drops.
3) Without loss of generality, each vehicle travels along its reference path which is predefined and fixed.
5) The coordinator adopts a batch optimization approach, where each batch contains up to $N R K$ CVs (i.e., each lane has up to $N$ CVs). The rationality of this approach will be demonstrated in Section II-D and II-E.

Notations $\mathcal{R}=\{1,2, \ldots, R\}, \mathcal{K}_{r}=\{1,2, \ldots, K\}$ and $\mathcal{N}_{r, k}=\{1,2, \ldots, N\}$ represent the set of roads, the set of lanes of road $r$ and the set of CVs in the $k$-th lane of road $r$, respectively. Denote $\mathcal{I}_{r, k} / I_{r, k}$ as the set/number of vehicles in the $k$-th lane of road $r$. We use tuple ( $r, k$ ) and ( $r, k, n$ ) to indicate the $k$-th lane of road $r$ and the $n$-th CV in the $k$-th lane of road $r$, respectively. $\left(r_{1}, k_{1}, n_{1}\right) \neq\left(r_{2}, k_{2}, n_{2}\right)$ means two different CVs.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-03.jpg?height=312&width=492&top_left_y=200&top_left_x=1278)
Fig. 2. Schematics on the kinematic model of a front steering vehicle.

## B. Vehicle Kinematic Model

Since vehicles usually pass the intersection at middle or even low speeds and in order to reduce the computational complexity of the coordination algorithm, the popular kinematic bicycle model [32] is adopted to control the vehicles in this paper, as shown in Fig. 2. The state vector of the CV $(r, k, n)$ can be expressed as $\mathbf{z}_{r, k}^{n}=\left[x_{r, k}^{n}, y_{r, k}^{n}, v_{r, k}^{n}, \psi_{r, k}^{n}\right]^{\mathrm{T}}$, where $\left(x_{r, k}^{n}, y_{r, k}^{n}\right), v_{r, k}^{n}$ and $\psi_{r, k}^{n}$ are the position, longitudinal velocity and heading angle, respectively. The control input vector is defined as $\left[a_{r, k}^{n}, \delta_{r, k}^{n}\right]^{\mathrm{T}}$, where $a_{r, k}^{n}$ is the longitudinal acceleration and $\delta_{r, k}^{n}$ is the steering angle. The vehicle dynamics are given as follows:

$$
\left[\begin{array}{c}
\dot{x}_{r, k}^{n}(t) \\
\dot{y}_{r, k}^{n}(t) \\
\dot{v}_{r, k}^{n}(t) \\
\dot{\psi}_{r, k}^{n}(t)
\end{array}\right]=\left[\begin{array}{c}
v_{r, k}^{n}(t) \cos \left(\psi_{r, k}^{n}(t)\right) \\
v_{r, k}^{n}(t) \sin \left(\psi_{r, k}^{n}(t)\right) \\
a_{r, k}^{n}(t) \\
v_{r, k}^{n}(t) \tan \left(\delta_{r, k}^{n}(t)\right) / L_{\mathrm{w}}
\end{array}\right]
$$

where $r \in \mathcal{R}, k \in \mathcal{K}_{r}, n \in \mathcal{N}_{r, k},(\bullet):=\frac{\partial}{\partial t}(\bullet), L_{\mathrm{w}}$ is the distance between the front and rear wheel axles. Considering the practical constraints in the vehicle model, we do have

$$
\begin{aligned}
-a_{\max } & \leq a_{r, k}^{n}(t) \leq a_{\max } \\
0 & \leq v_{r, k}^{n}(t) \leq v_{\max } \\
-\delta_{\max } & \leq \delta_{r, k}^{n}(t) \leq \delta_{\max }
\end{aligned}
$$

In the three-dimensional Cartesian coordinates XYT, the trajectory function can be described as:

$$
\begin{cases}\text { Path: } & \left\{\begin{array}{l}
x_{r, k}^{n}=f_{r, k}^{n}\left(s_{r, k}^{n}\right) \\
y_{r, k}^{n}=g_{r, k}^{n}\left(s_{r, k}^{n}\right)
\end{array}\right. \\
\text { Speed Profile: } & s_{r, k}^{n}=u_{r, k}^{n}(t)\end{cases}
$$

where $s$ is the arc length along the path, and $u$ is a function of velocity and acceleration. Given a reference path function $(f, g)$, e.g., line \& circle curves, polynomial curves, Bézier curves, and splines, the trajectory could be determined by optimizing the speed profile.

## C. Collision Detection

In practice, there exist some imperfections in the coordination system. First, the noise in localization and control could result in the vehicle deviating from the planned trajectory. Moreover, the communication delay of the V2I links is inevitable, which may reduce the freshness of the coordination instructions. These imperfections need to be fully considered, especially in the CA where a small error could lead to a
collision. To this end, we provide safety redundancy for each vehicle to ensure the safety and robustness of the coordination system, as depicted in Fig. 3. The road region occupied by the vehicle is defined by a two-dimensional convex polygon $\mathcal{P}, L_{\text {car }}$ and $W_{\text {car }}$ are the length and width of the vehicle, $d_{\text {lon }}$ and $d_{\text {lat }}$ are the longitudinal and lateral safe distances.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-04.jpg?height=281&width=471&top_left_y=488&top_left_x=374)
Fig. 3. The occupied road region is modeled as a rectangle with safety redundancy.

The convex set $\mathcal{P}$ for a state vector $\mathbf{z}=[x, y, v, \psi]$ can be mathematically defined as [33]:

$$
\begin{aligned}
\mathcal{P}(\mathbf{z}) & =\left\{\mathbf{p} \in \mathbb{R}^{2} \mid \mathbf{A}(\mathbf{z}) \mathbf{p} \leq \mathbf{b}(\mathbf{z})\right\} \\
\mathbf{A}(\mathbf{z}) & =\left[\mathbf{M}(\psi)^{\mathrm{T}},-\mathbf{M}(\psi)^{\mathrm{T}}\right]^{\mathrm{T}} \\
\mathbf{b}(\mathbf{z}) & =[L / 2, W / 2, L / 2, W / 2]^{\mathrm{T}}+\mathbf{A}(\mathbf{z})\left[x_{\mathrm{c}}, y_{\mathrm{c}}\right]^{\mathrm{T}}
\end{aligned}
$$

where $\mathbf{M}(\psi)=\left[\begin{array}{cc}\cos (\psi) & -\sin (\psi) \\ \sin (\psi) & \cos (\psi)\end{array}\right]$ is the rotation matrix, $L=L_{\text {car }}+d_{\text {lon }}$ and $W=W_{\text {car }}+d_{\text {lat }}$ are the length and width of the occupied road region, $x_{\mathrm{c}}=x+L_{\mathrm{w}} \cos (\psi) / 2$ and $y_{\mathrm{c}}=y+L_{\mathrm{w}} \sin (\psi) / 2$ are the coordinates of the center of the occupied road region. Collisions among the CVs can be avoided if the following constraints are satisfied throughout the coordination,

$$
\mathcal{P}\left(z_{r_{1}, k_{1}}^{n_{1}}(t)\right) \cap \mathcal{P}\left(z_{r_{2}, k_{2}}^{n_{2}}(t)\right)=\varnothing, \forall\left(r_{1}, k_{1}, n_{1}\right) \neq\left(r_{2}, k_{2}, n_{2}\right)
$$

In this paper, collision detection is performed by leveraging Separating Axis Theorem (SAT) [34], which is known as an efficient algorithm for checking the overlapping between polygons.

## D. Coordination Stability

For intersection coordination system, the queue length of each lane, i.e., $I_{r, k}(t)$, is time-varying due to the dynamic arrival of vehicles. Thus, it is critical to ensure that all queues in the coordination system are stable, i.e.,

$$
\lim _{T \rightarrow \infty} \sup \frac{1}{T} \sum_{t=1}^{T} \mathbb{E}\left\{I_{r, k}(t)\right\}<\infty, r \in \mathcal{R}, k \in \mathcal{K}_{r}
$$

where sup means the upper bound. Future queue states can be driven by stochastic arrival $a_{r, k}(t)$ and coordination rate $b_{r, k}(t)$ according to the following dynamic equation:

$$
I_{r, k}(t+1)=\max \left[I_{r, k}(t)+a_{r, k}(t)-b_{r, k}(t), 0\right]
$$

The real-time coordination rate is defined as:

$$
b_{r, k}(t)=\frac{N_{r, k}(t)}{T_{r, k}}
$$

where $T_{r, k}$ is the coordination time (the time elapsed from turning red to turning green) of the CVs in lane ( $r, k$ ), $0 \leq$ $N_{r, k}(t) \leq N$ is the number of CVs in lane ( $r, k$ ) of current batch.

Based on the Lyapunov Optimization Theorem [35], the objective of (10) can be achieved by minimizing the drift of a Lyapunov function. Let $\mathbf{I}(t)=\left[I_{1,1}(t), I_{1,2}(t), \ldots, I_{R, K}(t)\right]^{\mathrm{T}}$ be the vector of current queue backlogs, the Lyapunov function can be defined as:

$$
L(\mathbf{I}(t)) \triangleq \frac{1}{R K} \sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} I_{r, k}(t)
$$

To consistently push the Lyapunov function towards a low congestion region, we can minimize the bound on $\Delta(\mathbf{I}(t))$. Herein, $\Delta(\mathbf{I}(t))$ is the conditional Lyapunov drift and can be defined as:

$$
\Delta(\mathbf{I}(t)) \triangleq \mathbb{E}\{L(\mathbf{I}(t+1))-L(\mathbf{I}(t)) \mid \mathbf{I}(t)\}
$$

Substitute (11) and (13) into (14), the bound can be derived as:

$$
\begin{aligned}
\Delta(\mathbf{I}(t)) \leq & \frac{1}{R K} \mathbb{E}\left\{\sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} a_{r, k}(t)^{2}+b_{r, k}(t)^{2} \mid \mathbf{I}(t)\right\} \\
& +\frac{2}{R K} \sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} I_{r, k}(t) \lambda_{r, k} \\
& -\frac{2}{R K} \mathbb{E}\left\{\sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} I_{r, k}(t) b_{r, k}(t) \mid \mathbf{I}(t)\right\}
\end{aligned}
$$

where $\lambda_{r, k}=\mathbb{E}\left\{a_{r, k}(t) \mid \mathbf{I}(t)\right\}$ is the mean arrival rate. The first term on the right-hand-side of the above drift inequality can be upper bounded by a finite constant [35]. Therefore, minimize the bound on the drift is equivalent to maximize the following expression:

$$
\mathbb{E}\left\{\sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} I_{r, k}(t) b_{r, k}(t) \mid \mathbf{I}(t)\right\}
$$

## E. Problem Formulation

By using the concept of opportunistically maximizing an expectation [35], expression (16) is maximized by maximizing the weighted sum of the coordination rate, i.e., $\sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} I_{r, k}(t) b_{r, k}(t)$. It follows that the CVs in the lane with more vehicles have higher priority and need to be provided with more coordination rate. However, the intersection coordination capacity, defined as $C(t)=$ $\sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} b_{r, k}(t)$, is limited. CVs need to be controlled under the premise of satisfying the kinematic constraints (1)-(4) and collision-free constraints (9), rather than driving at will. How to efficiently coordinate the CVs according to queue states to support higher coordination rate is important to the intersection coordination system. To achieve this goal, the optimization problem can be formulated as follows,

$$
\begin{aligned}
\mathscr{P}: & \max _{\mathbf{u}_{r, k}^{n}} \sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} I_{r, k}(t) b_{r, k}(t) \\
& \text { s.t. }(1)-(5),(9),(12)
\end{aligned}
$$

where $\mathbf{u}_{r, k}^{n}=\left[u_{r, k}^{n}(0), u_{r, k}^{n}(1), \ldots, u_{r, k}^{n}\left(T_{r, k}\right)\right]^{\mathrm{T}}$ is the speed profile of CV $(r, k, n)$. For a given initial configuration, a multitude of solutions might exist (i.e., when and in what control sequence each CV cross the intersection), and the optimal trajectories can only be found by a structured exploration of the different alternatives [22]. Thus, the problem $\mathscr{P}$ is NPhard in general.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-05.jpg?height=451&width=892&top_left_y=537&top_left_x=157)
Fig. 4. An illustration of two benchmark strategies.

## F. Benchmark Solutions

In this subsection, we briefly introduce two state-of-the-art centralized intersection coordination solutions as benchmarks.

1) Collision Set: In the collision set (CS) strategy [23], the area where collisions may occur is defined as the collision set, where multiple vehicles cannot enter one collision set simultaneously. For a typical single-lane scenario, as shown in Fig. 4(a), any two left-turning vehicles may collide. Therefore, the vehicles could only cross the intersection one after another. As a result, the collision-free constraints could be ignored and thus significantly reduce the complexity of solving the aforementioned problem $\mathscr{P}$. Though the CS strategy shows superiority in terms of low-complexity implementation and long-term stability, it could not harness the full coordination potential of the intersection, especially for multi-lane scenarios.
2) Space-Time Resource Searching: The space-time resource searching (STRS) strategy [31] adopts the aggressive idea that all CVs simultaneously share the intersection to improve traffic throughput. Specifically, the space and time resources in the intersection can be regarded as threedimensional coordinates with X, Y, and T domains, as shown in Fig. 4(b). The proposition of optimizing speed profiles to make CVs travel safely on the overlapped paths in the XY domain is equivalent to searching for disjoint trajectories in XYT domains. Compared with the CS strategy, the STRS strategy shows obvious throughput advantages. By traversing space-time resources, the STRS strategy could obtain optimal passing order and trajectories, however, at the expense of realtime processing capabilities. In practical implementations, the coordinator requires tremendous computational resources and power supply to deal with high computational complexity. Excessive problem-solving time could also lead to safety issues, especially in the CA. Moreover, the computational complexity grows exponentially with the number of vehicles and lanes, which will hinder this strategy for multi-lane scenarios.

## III. DRL-based Centralized Coordinator

It is critical to rapidly obtain optimal trajectories for given initial configurations in the considered intersection coordination scenario. However, searching for the optimal trajectories in 3D space XYT, or optimizing the controls on given overlapped 2D paths, takes overlong problem-solving time. Moreover, the computational complexity of the centralized coordination strategy grows exponentially with the number of lanes and the number of CVs. Thus, it is challenging to adopt the pure optimization approach-based schemes to solve the optimal coordination problem in real-time.

To address the key computational challenges, an RL approach is leveraged in this paper. We first model the sequential decision-making problem $\mathscr{P}$ as a model-free MDP and then resort to DRL algorithms to tackle it. A speed profile smoother is also designed to improve passenger comfort.

## A. Problem Transformation

We first formulate the intersection coordination problem using the reinforcement learning (RL) framework. MDPs can be used to express the standard mathematical formalism of RL [36]. An MDP is a 5-tuple $(S, A, R, P, \gamma)$ that describes the interactions between the states of the environment and the actions of the RL agent. Specifically, at each time slot $t$, based on the observation $\mathbf{s}_{t} \in S$, an action $\mathbf{a}_{t} \in A$ sampled from a stochastic policy $\pi\left(\mathbf{a}_{t} \mid \mathbf{s}_{t}\right)$ or generated by a deterministic policy $\pi\left(\mathbf{s}_{t}\right)$ is executed by the RL agent and the environment transitions to next state $\mathbf{s}_{t+1} \in S$ with a transition probability $\operatorname{Pr}\left(\mathbf{s}_{t+1} \mid \mathbf{s}_{t}, \mathbf{a}_{t}\right) \in P$, receiving a reward $r_{t}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) \in R . \gamma \in[0,1)$ is the discount factor that trades off long-term against short-term rewards. According to whether the state transition probability and the expected return from any state-action pair are prior or not, RL algorithms can be classified into two categories: model-based and model-free. In the considered intersection coordination scenario, the agent has no idea how to make a proper decision for the subsequent time slot according to the current observed environment state. Hence, it can be regarded as a model-free one.

Deep RL (DRL), which combines RL with deep neural networks (DNNs), can be applied to deal with continuous control problems. By using DNNs as a non-linear function approximator over high-dimensional state spaces, only the network parameters need to be stored instead of a lookup table that records the values of all possible state-action pairs [37]. Moreover, DNNs can infer actions on unseen observations, enabling the algorithm to obtain expected performance without traversing all state-action pairs.

1) Observation and Action Spaces: Intuitively, the state of each CV should contain the position and velocity information. However, this information only portrays the current driving state and ignores the intention and association among CVs. For example, if the paths of the CVs do not overlap in the CA, they could leave the CCZ as quickly as possible. Otherwise, the CVs should collaboratively cross the CA to avoid collision in the subsequent time slots.

To capture the intentions of the CVs, a natural and straightforward scheme is to assign each vehicle a tag, i.e., 0-turn left,

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-06.jpg?height=520&width=698&top_left_y=198&top_left_x=260)
Fig. 5. Illustration of the network architecture used in this work.

1-go straight, and 2-turn right. However, DNNs have difficulty in identifying the meaning of these tags. To help the DNNs understand the tags, we could encode each of these tags as a three-element binary vector, e.g., [1, 0, 0] represents turning left. However, the required state dimensions to infer driving intentions increases linearly with the number of CVs, which is computationally inefficient for training the DRL agent. Finally, we use a $D_{r}$-element binary vector $\mathbf{d}_{r}$ to encode the joint intentions for CVs on the $r$-th road, where $D_{r}=3^{N}$ if $K=1$ else $D_{r}=4^{N}$. This joint encode scheme shows effectiveness in identifying CVs' intentions using much fewer state dimensions.

Moreover, to capture the dynamic feature of the traffic, the queue state vector $\mathbf{I}(t)$ is also considered. We normalize the queue states to reflect the priority of different lanes. The priority of lane ( $r, k$ ) can be defined as:

$$
p_{r, k}(t)=\frac{I_{r, k}(t)}{\sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} I_{r, k}(t)}
$$

Then, the environment state at time slot $t$ can be described as:

$$
\begin{array}{r}
\mathbf{s}_{t}=\left\{\mathbf{d}_{r}(t), p_{r, k}(t), x_{r, k}^{n}(t), y_{r, k}^{n}(t), v_{r, k}^{n}(t)\right. \\
\left.\mid r \in \mathcal{R}, k \in \mathcal{K}_{r}, n \in \mathcal{N}_{r, k}\right\}
\end{array}
$$

The DRL agent is trained to directly map the observation to CVs' control commands, i.e., acceleration, velocity, heading angle, and steering angle. For a given reference path, the velocity, heading angle, and steering angle can be determined by acceleration. Hence, the agent only needs to output acceleration commands, which could greatly reduce the training complexity, thus

$$
\mathbf{a}_{t}=\left\{a_{r, k}^{n}(t) \mid r \in \mathcal{R}, k \in \mathcal{K}_{r}, n \in \mathcal{N}_{r, k}\right\}
$$

Note that the output layer of the policy network is fixed, as shown in Fig. 5, so for the case where the number of CVs in lane ( $r, k$ ) is less than $N$, the controls for the non-existent vehicles will not be sent out.
2) Reward Functions: To some extent, the reward function determines how intelligent the RL agent would be. An unreasonable reward function may lead the agent to devise an ineffective or even unusable policy. Moreover, the reward function should be designed based on the objective of the original optimization problem $\mathscr{P}$. Intuitively, the total time spent on passing the intersection directly captures the main objective of the original problem, i.e.,

$$
r_{\mathrm{sa}}(t)=100001_{t} \cdot\left(\sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} \frac{p_{r, k}(t)}{T_{r, k}}\right)
$$

where $\mathbf{1}_{t}$ is an indicator variable that represents whether all CVs leave the CCZ or not at time slot $t$, i.e., $\mathbf{1}_{t}=1$ if all CVs leave CCZ and $\mathbf{1}_{t}=0$ otherwise. However, this reward can only be computed upon the completion of a full coordination, introducing sparsity that considerably increases the difficulty in evaluating the usefulness of individual actions. A popular approach to circumvent this problem is to use an immediate reward that roughly reflects the final goal while providing feedback to the agent at every time step [38]. Therefore, we use velocity information to represent the effectiveness of individual actions, i.e.,

$$
r_{\mathrm{v}}(t)=\sum_{r \in \mathcal{R}} \sum_{k \in \mathcal{K}_{r}} \sum_{n \in \mathcal{N}_{r, k}} v_{r, k}^{n}(t)
$$

Most importantly, to learn a safe policy, we define a large negative reward to discourage the CVs from colliding in the CA, which can be expressed as:

$$
r_{\mathrm{c}}(t)=\left\{\begin{array}{cl}
-r_{\mathrm{T}}, & \text { if collide } \\
0, & \text { otherwise }
\end{array}\right.
$$

where $r_{\mathrm{T}}$ is a hyperparameter that trades off between safety and efficiency. Specifically, a large penalty may hinder the agent from exploring better decisions and result in a more conservative and inefficient policy. In contrast, a small penalty may lead to aggressive actions that compromise safety. In this paper, $r_{\mathrm{T}}$ is set as 1000.

In addition, we define an intermediate reward to incentivize the vehicle to cross the intersection safely. It should be noted that this is an optional reward component designed to guide the agent to achieve our goal and improve the convergence speed and asymptotic performance of the DRL algorithm. The intermediate reward is defined as follows:

$$
r_{\mathrm{s}}(t)=1000 n_{t}
$$

where $n_{t}$ is the number of CVs that left the CCZ in time duration $[t, t+1)$. The final reward at each time slot $t$ could be defined as:

$$
r_{t}=r_{\mathrm{sa}}(t)+r_{\mathrm{v}}(t)+r_{\mathrm{c}}(t)+r_{\mathrm{s}}(t)
$$

## B. TD3-based Solution

The goal of the RL agent is to maximize the expected return by optimizing the policy over the environment dynamics [39], [40]. The expected return $V$ under a policy $\pi$ can be calculated as:

$$
V^{\pi}\left(\mathbf{s}_{t}\right)=\mathbb{E}_{\tau \sim \pi}\left[G_{t} \mid \mathbf{s}_{t}\right]
$$

where $G_{t}=\sum_{i=t}^{\infty} \gamma^{i-t} r_{i}$ is the discounted return, $\tau=$ $\left(\mathbf{s}_{t}, \mathbf{a}_{t}, \mathbf{s}_{t+1}, \mathbf{a}_{t+1}, \ldots\right)$ is the trajectory which the agent will follow from time step $t$, and $\tau \sim \pi$ means the agent acts according to the policy $\pi$. Value function (also called
critic or Q-function) can be established to estimate $V^{\pi}$ in a bootstrapping way. Under an arbitrary policy $\pi$, value function can be defined as:

$$
\begin{aligned}
Q^{\pi}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right) & =\mathbb{E}_{\tau \sim \pi}\left[G_{t} \mid \mathbf{s}_{t}, \mathbf{a}_{t}\right] \\
& =r_{t}+\gamma \cdot \mathbb{E}_{\tau \sim \pi}\left[Q^{\pi}\left(\mathbf{s}_{t+1}, \mathbf{a}_{t+1}\right)\right]
\end{aligned}
$$

Then the policy function (also called actor) can be obtained by maximizing value function, represented as:

$$
\pi^{*}=\arg \max _{\pi} \mathbb{E}_{\tau \sim \pi}\left[Q^{\pi}\left(\mathbf{s}_{t}, \mathbf{a}_{t}\right)\right]
$$

Equations (26) and (27) concrete the actor-critic RL framework. In practical implementations, we utilize neural networks as the differentiable function approximator to construct the actor and critic. Hence, the optimal policy can be obtained by optimizing the parameters of the policy network $\pi_{\theta}$ and value network $Q_{\phi}$.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-07.jpg?height=642&width=715&top_left_y=935&top_left_x=247)
Fig. 6. The architecture and training process of TD3 agent.

In this work, we train our agent using the TD3 algorithm [41], a state-of-the-art actor-critic method that is particularly popular in continuous control problems such as robotics and autonomous driving. As shown in Fig. 6, the TD3 agent consists of six neural networks of two types: the main networks and the target networks, and each type contains one policy network and two value networks. The target and main networks share the same structure but different parameters. At time step $t$, each CV shares its driving status with the agent, and based on the observation $\mathrm{s}_{t}$, the agent's main policy network $\pi_{\theta}$ outputs the control commands for the CVs, i.e.,

$$
\mathbf{a}_{t}=\operatorname{clip}\left(\pi_{\theta}\left(\mathbf{s}_{t}\right)+\epsilon,-a_{\max }, a_{\max }\right)
$$

where $\epsilon \sim \mathcal{N}(0, \sigma)$ is the exploration noise aiming to encourage the agent to take the risk of trying new actions which may lead to higher rewards, rather than exploiting its knowledge by selecting actions which are known to result in high rewards. By executing $\mathbf{a}_{t}$, the vehicles transition to the next state $\mathbf{s}_{t+1}$ according to the vehicle kinematic model (1) and receive a reward $r_{t}$ which evaluates the usefulness of the action. For more efficient use of previous experience and better convergence performance when training the TD3 agent, a replay buffer $\mathcal{D}$ is considered to save each experience ( $\mathbf{s}_{t}, \mathbf{a}_{t}, r_{t}, \mathbf{s}_{t+1}, d_{t}$ ), where $d_{t}$ indicates whether the state $\mathbf{s}_{t+1}$ is terminal (terminate on a collision or successful coordination).

During the training stage, a mini batch of experiences $\mathcal{B}=\left\{\left(\mathbf{s}, \mathbf{a}, r, \mathbf{s}^{\prime}, d\right)\right\}$ are randomly sampled from the replay buffer and then fed to the agent in parallel to update the neural networks. The value networks can be updated by minimizing the following critic loss function:

$$
\mathcal{L}^{Q}(\phi)=\frac{1}{|\mathcal{B}|} \sum_{\left(\mathbf{s}, \mathbf{a}, r, \mathbf{s}^{\prime}, d\right) \in \mathcal{B}}\left(Q_{\phi}(s, a)-y\left(r, s^{\prime}, d\right)\right)^{2}
$$

where $y\left(r, s^{\prime}, d\right)$ is called the temporal difference (TD)-target, which represents the latest prediction of the Q-function. In an actor-critic setting, the TD-target is usually formulated as $r+\gamma(1-d) Q_{\phi^{\prime}}\left(\mathbf{s}^{\prime}, \pi_{\theta^{\prime}}\left(\mathbf{s}^{\prime}\right)\right)$, where $Q_{\phi^{\prime}}$ and $\pi_{\theta^{\prime}}$ are the target value network and target policy network [42], respectively. In practice, however, using one target value network to update the estimate $Q_{\phi}(s, a)$ will lead to overestimation bias, which could result in suboptimal policy updates and divergent behavior. In TD3, a novel method, Clipped Double Q-learning, is designed to greatly reduce overestimation bias. The TD-target can be computed as:

$$
y\left(r, s^{\prime}, d\right)=r+\gamma(1-d) \min _{i=1,2} Q_{\phi_{i}^{\prime}}\left(s^{\prime}, \pi_{\theta^{\prime}}\left(s^{\prime}\right)+\tilde{\epsilon}\right)
$$

where $Q_{\phi_{1}^{\prime}}, Q_{\phi_{2}^{\prime}}$ are the two target value networks, $\tilde{\epsilon} \sim$ $\operatorname{clip}(\mathcal{N}(0, \tilde{\sigma}),-c, c)$ is the clipped policy noise, $c \in(0,1)$ is the clip ratio. The two value networks can be updated by gradient descent using

$$
\nabla_{\phi_{i}} \mathcal{L}^{Q}\left(\phi_{i}\right)=\nabla_{\phi_{i}} \frac{1}{|\mathcal{B}|} \sum_{\left(\mathbf{s}, \mathbf{a}, r, \mathbf{s}^{\prime}, d\right) \in \mathcal{B}}\left(Q_{\phi_{i}}(s, a)-y\left(r, s^{\prime}, d\right)\right)^{2}
$$

The policy network is updated by maximizing Q-function through deterministic policy gradient algorithm [43]:

$$
\begin{aligned}
\nabla_{\theta} \mathcal{L}^{\pi}(\theta) & =\nabla_{\theta} \frac{1}{|\mathcal{B}|} \sum_{\mathbf{s} \in \mathcal{B}} Q_{\phi_{1}}\left(s, \pi_{\theta}(s)\right) \\
& =\frac{1}{|\mathcal{B}|} \sum_{\mathbf{s} \in \mathcal{B}}\left(\left.\nabla_{a} Q_{\phi_{1}}(s, a)\right|_{a=\pi_{\theta}(s)} \nabla_{\theta} \pi_{\theta}(s)\right)
\end{aligned}
$$

Considering the overestimation bias caused by value networks, the policy network and target networks should be updated at a lower frequency than the value network. So we only update the policy and target networks after a fixed number of updates to the critic. The training stage of the TD3-based centralized coordinator can be found in Algorithm 1.

The policy network $\pi_{\theta}$ trained offline can be regarded as a real-time solver, which could instantly output current controls by inputting an observation of the environment. However, interacting with the environment at each time slot will waste tremendous communication resources, and the communication delay also causes jitter in control. In practical implementations, the coordinator can operate in predictive mode: all instructions for the subsequent time slots are sent to the CVs at once by simulating vehicle kinematics. It is reasonable when the noise in control, sensing and localization is relatively small. Otherwise, a re-planning operation will be necessary when the trajectory deviation is large enough.

```
Algorithm 1 Training Stage of The TD3-based Coordinator.
    Initialize policy parameters \(\theta\), value parameters \(\phi_{1}, \phi_{2}\).
    Empty replay buffer \(\mathcal{D}\). Set target parameters equal to
main parameters \(\theta^{\prime} \longleftarrow \theta, \phi_{1}^{\prime} \longleftarrow \phi_{1}, \phi_{2}^{\prime} \longleftarrow \phi_{2}\). The pa-
    rameters are updated after \(T_{\text {start }}\) steps, the policy network
    and target networks are updated after \(T_{\text {delay }}\) updates of the
critic. Initialize total time steps \(T_{\text {total }}=0\), total network
updates \(T_{\text {updates }}=0\).
    for episode \(=1\) to \(E\) do
        Randomly initialize the position of the CVs and the
        number of WVs, receive initial observation \(\mathbf{s}_{0}\). Set time
        step \(t=0\), done signal \(d_{0}=\) False.
        while not \(d_{t}\) do
            Observe current environment state \(\mathrm{s}_{t}\).
            if \(T_{\text {total }}<T_{\text {start }}\) then
                Randomly sample an action from action space.
            else
                Select action using policy \(\pi_{\theta}\) according to (28).
            end if
            The CVs execute control commands \(\mathbf{a}_{t}\) according to
            vehicle kinematic model (1).
            Check collision using SAT algorithm.
            if collide or complete then
                Set done signal \(d_{t}=\) True.
            end if
            Observe next state \(\mathbf{s}_{t+1}\), compute reward \(r_{t}\) according
            to (24), check done signal \(d_{t}\).
            Store experience \(\left(\mathbf{s}_{t}, \mathbf{a}_{t}, r_{t}, \mathbf{s}_{t+1}, d_{t}\right)\) in \(\mathcal{D}\).
            if \(T_{\text {total }}>T_{\text {start }}\) then
                \(T_{\text {updates }} \longleftarrow T_{\text {updates }}+1\)
                Randomly sample a mini-batch of transitions \(\mathcal{B}=\)
                \(\left\{\left(\mathbf{s}, \mathbf{a}, r, \mathbf{s}^{\prime}, d\right)\right\}\) from \(\mathcal{D}\).
                Compute TD-targets according to (30).
                Update \(\phi_{1}\) and \(\phi_{2}\) by gradient descent using (31).
                if \(T_{\text {updates }} \bmod T_{\text {delay }}=0\) then
                    Update \(\theta\) by gradient ascent using (32).
                    Update target networks using soft update:
                        \(\theta^{\prime} \longleftarrow \tau \theta+(1-\tau) \theta^{\prime}\)
                        \(\phi_{i}^{\prime} \longleftarrow \tau \phi_{i}+(1-\tau) \phi_{i}^{\prime}\), for \(i=1,2\)
                end if
            end if
            \(T_{\text {total }} \longleftarrow T_{\text {total }}+1\)
        end while
    end for
```


## C. Speed Profile Smoother

We observe that the original trajectories generated by the TD3 agent are significantly jittery before entering the CA due to the lack of passenger comfort metrics in the reward function. To this end, we further smooth the original trajectories in frénet coordinates [44]. In the frénet frame, the trajectory optimization problem can be decomposed into two simpler subproblems: lateral and longitudinal planning, responsible for reference path generation and speed profile optimization, respectively.

From the speed profile perspective, for a given start state $\left[s_{0}, v_{0}, a_{0}\right]$ at $t_{0}$ and a end state $\left[s_{1}, v_{1}, a_{1}\right]$ at some $t_{1}=t_{0}+T$ (here $s$ is the longitudinal distance along its path), we generate a smooth longitudinal trajectory using quintic polynomials,

$$
s(t)=\omega_{0}+\omega_{1} t+\omega_{2} t^{2}+\omega_{3} t^{3}+\omega_{4} t^{4}+\omega_{5} t^{5}
$$

Here, the coefficients can be calculated by solving the following linear function:

$$
\left[\begin{array}{c}
s_{0} \\
v_{0} \\
a_{0} \\
s_{1} \\
v_{1} \\
a_{1}
\end{array}\right]=\left[\begin{array}{cccccc}
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 2 & 0 & 0 & 0 \\
1 & T & T^{2} & T^{3} & T^{4} & T^{5} \\
0 & 1 & 2 T & 3 T^{2} & 4 T^{3} & 5 T^{4} \\
0 & 0 & 2 & 6 T & 12 T^{2} & 20 T^{3}
\end{array}\right] \cdot\left[\begin{array}{c}
\omega_{0} \\
\omega_{1} \\
\omega_{2} \\
\omega_{3} \\
\omega_{4} \\
\omega_{5}
\end{array}\right]
$$

```
Algorithm 2 The proposed dynamic coordination framework.
    The coordinator load pre-trained policy network \(\pi_{\theta}\).
    repeat
        Send Velocity Keeping and Safe-distance Maintaining
        commands to all WVs [44]. Current batch of CVs hand
        over their control authorities to the coordinator.
        Collect all state information including queue states,
        CV's driving states and intentions.
        Construct initial state vector according to (18).
    The coordinator operate in predictive mode and com-
        pute optimal trajectories for all CVs using policy \(\pi_{\theta}\).
    Smooth the original trajectories using (33) and (34).
        repeat
        Current batch of CVs cross the intersection according
        to maneuver instructions.
        if CV \((r, k, n)\) leave the CA then
            Turn green and keep a velocity \(v_{\text {max }}\).
        end if
        until All CVs leave the CA.
    Store all experiences in replay buffer \(\mathcal{D}\) for offline
        policy updating.
    Completion of current coordination. Transition to next
        batch of CVs.
    until The coordination process is finished.
```


## IV. Simulation Results and Experiments

## A. Simulation Settings

To demonstrate the performance of the proposed TD3-based coordination strategy, simulation results and experiments are presented in this section. To facilitate comparison with the strategies described in Section II-F, we consider a special case with $N=1$. The simulation procedure can be summarized in two stages, i.e., the training stage to optimize network parameters and the evaluation stage to test the trained agent.

In the training stage, we first train separate policies for single-lane and multi-lane scenarios, as shown in Fig. 7 and Fig. 1, respectively. Without loss of generality, the position, velocity and intention of the vehicles are randomly initialized,

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-09.jpg?height=507&width=507&top_left_y=191&top_left_x=352)
Fig. 7. An illustration of the single-lane scenario with different left-turning radii.

and the paths of the left/right-turning vehicles are line \& circle curves. The left/right-turning radius, denoted by $R_{1} / R_{\mathrm{r}}$, is set as $15(10) \mathrm{m} / 15 \mathrm{~m}$ for single-lane case and $40 \mathrm{~m} / 20 \mathrm{~m}$ for multilane case. Therefore, three separate policies are trained: (1) single-lane road intersection with $R_{1}=15 \mathrm{~m}$. (2) single-lane road intersection with with $R_{1}=10 \mathrm{~m}$. (3) multi-lane road intersection. The training process confronts challenges due to the high dimensionality of searching space, the complexity of required maneuvers, and the randomness of initial states. To this end, we adopt the parallel sampling scheme, which allows for increasing the number of agents to interact with different environments in parallel, resulting in a significant speed-up in data collection. Moreover, parallelization is an effective way to enrich the diversity of the collected experiences, which is beneficial to avoiding policy overfitting and increasing the probability of successful coordination. Detailed training parameters of the single-lane and multi-lane scenarios are listed in Table I.

In the evaluation stage, the CS and STRS strategies discussed in Section II-F are also performed for comparison. For ease of analysis, both static and dynamic coordination tasks are considered, where static coordination refers to the coordination of a single batch of CVs, while dynamic coordination refers to multiple batches of CVs over a period of time. There are three kinds of performance indices evaluated in the simulations:

- total passing time: it refers to the total time when a single batch of CVs within the control area have passed the CCZ. In fact, the total passing time can be used to measure the objective value of the proposed optimization problem $\mathscr{P}$.
- average computation time: it refers to the average computation time taken for coordinating a single batch of CVs, which is used to evaluate the computational efficiency of the strategies.
- traffic throughput: it refers to the total number of vehicles that have passed the CCZ in a specified period, or equivalently, the average passing time for a specified number of vehicles. This metric is utilized to evaluate traffic efficiency in continuous traffic flow.

TABLE I
Simulation Parameters
| Parameters | Value |  |
| :--- | :--- | :--- |
|  | Single-lane | Multi-lane |
| Number of lanes | 1 | 3 |
| Radius of CCZ | 50 m | 100 m |
| Size of CA | 20 m × 20 m | 48 m × 48 m |
| left/right-turning radius | 15(10) m / 15 m | 40 m / 20 m |
| Vehicle size $L_{\text {car }} / W_{\text {car }}$ | 4 m / 2 m | 4 m / 2 m |
| Safe redundancy $d_{\text {lon }} / d_{\text {lat }}$ | 4 m / 2 m | 4 m / 2 m |
| Maximum velocity $v_{\text {max }}$ | $15 \mathrm{~m} / \mathrm{s}$ | $15 \mathrm{~m} / \mathrm{s}$ |
| Maximum acceleration $a_{\text {max }}$ | $5 \mathrm{~m} / \mathrm{s}^{2}$ | $5 \mathrm{~m} / \mathrm{s}^{2}$ |
| Maximum steering angle $\delta_{\text {max }}$ | 0.78 rad | 0.78 rad |
| WV's velocity $v_{\text {low }}$ | 5 m/s | 5 m/s |
| Slot duration $\Delta T$ | 0.1 s | 0.1 s |
| Number of parallel agents | 6 | 12 |
| Network architecture | [28,256,256,4] | [64, 400, 300, 12] |
| Learning rate of actor/critic | 3e-4 / 3e-4 | 3e-4 / 3e-4 |
| Soft update rate $\tau$ | 5e-3 | 5e-3 |
| Exploration noise $\sigma$ | 0.1 | 0.1 |
| Policy noise $\tilde{\sigma} /$ clip ratio $c$ | 0.2 / 0.5 | 0.2 / 0.5 |
| Discount factor $\gamma$ | 0.99 | 0.99 |
| Mini-banch size $\|\mathcal{B}\|$ | 128 | 256 |
| Maximum episodes $E$ | 2000 | 20000 |
| Training delay $T_{\text {after }}$ | 25e3 | 50e3 |
| Policy delay $T_{\text {delay }}$ | 2 | 2 |


![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-09.jpg?height=479&width=657&top_left_y=1195&top_left_x=1156)
Fig. 8. Convergence performance of the proposed TD3-based strategy.

## B. Single-lane Scenario

1) Convergence Performance: Fig. 8 demonstrates the convergence performance of the proposed TD3-based coordination strategy for single-lane scenario. As we can see from the figure, the total rewards per episode fluctuates sharply in the first 1000 episodes. As illustrated in Algorithm 1, the parameters of the neural networks are randomly initialized and the agent executes random actions for better exploration in the first few episodes. Consequently, a majority of episodes terminate on a collision, resulting in unstable and undesirable rewards. However, with the parameters gradually being optimized after about 1250 episodes, the agent is intelligent enough to make proper decisions. It is obvious that the proposed TD3-based algorithm can improve the coordination efficiency significantly with a considerable convergence rate.
2) Trajectory Analysis: Fig. 9 and Fig. 10 present the outputs of the CS-based and TD3-based coordinator for a static coordination scenario, respectively. All the four left-turning

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-10.jpg?height=655&width=1805&top_left_y=226&top_left_x=168)
Fig. 9. The optimized outputs of the CS-based coordinator $\left(R_{1}=15 \mathrm{~m}\right)$.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-10.jpg?height=657&width=1805&top_left_y=997&top_left_x=168)
Fig. 10. The original and smoothed outputs of the TD3-based coordinator $\left(R_{\mathrm{l}}=15 \mathrm{~m}\right)$.

CVs are initialized at $p_{1}=p_{2}=p_{3}=p_{4}=20 \mathrm{~m}$ with velocity $v_{\text {low }}=5 \mathrm{~m} / \mathrm{s}$ and left-turning radius $R_{1}=15 \mathrm{~m}$. The output information of each vehicle is distinguished by different colors, the dotted and solid lines in Fig. 10 indicate the original and smoothed outputs, respectively. The red circles represent the entry points of the CA. It is obvious that the original acceleration and speed profile jitters dramatically before the time entering the CA. On the contrary, the smoothed profiles could provide better passenger comfort and adapt much better to the traffic flow. Fig. 10(c) shows the longitudinal distance versus coordination time (i.e., S-T figure), which implies that the CA can be occupied by two vehicles simultaneously. However, as shown in Fig. 9(c), all CVs should enter the CA one after another under the guidance of the CS strategy. Hence, the total passing time for the TD3-based strategy could be significantly reduced compared to the CS strategy.

Furthermore, we recognize that the left-turning radius has a significant influence on the coordination efficiency, as shown in Fig. 11. Fig. 11(a) indicates that all the four CVs guided by the TD3 agent could occupy the intersection simultane- ously. Fig. 11(b) and Fig. 11(c) show the 3D trajectories for $R_{1}=15 \mathrm{~m}$ and $R_{1}=10 \mathrm{~m}$, respectively. From Fig. 11(a) and Fig. 11(c), it can be seen that the vehicles with $R_{1}=10 \mathrm{~m}$ in the opposite directions can cross the intersection at the same speed. In contrast, as shown in Fig. 10(c) and Fig. 11(b), the vehicles with $R_{1}=15 \mathrm{~m}$ could only pass the intersection consecutively. A more detailed discussion is beyond the scope of this paper. How intersection geometry and different turning radii influence coordination efficiency will be investigated in our future work.
3) Total Passing Time: Fig. 12 demonstrates the total passing time of the four left-turning CVs versus the initial positions. For ease of analysis, all the CVs are initialized at $p_{1}=p_{2}=p_{3}=p_{4}=p_{\text {init }}$ and the left-turning radius is set as $R_{1}=15 \mathrm{~m}$. The total passing time of the CS strategy is much higher than that of the TD3 and STRS strategies. The STRS strategy iteratively searches the XYT resource blocks to obtain the optimal trajectories and passing order. Hence, the total passing time of the STRS strategy can be regarded as a lower bound. As can be seen from the figure, the total

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-11.jpg?height=657&width=1790&top_left_y=189&top_left_x=172)
Fig. 11. Comparison of coordination efficiency for different left-turning radii.

passage time of TD3-based strategy is almost the same as STRS strategy when $p_{\text {init }}>20 \mathrm{~m}$, and slightly larger when $p_{\text {init }} \leq 20 \mathrm{~m}$. A possible explanation for this might be that the collision probability increases when all CVs are close to the CA, resulting in the TD3 agent tending to make conservative decisions and failing to obtain the optimal passing order.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-11.jpg?height=537&width=700&top_left_y=1319&top_left_x=234)
Fig. 12. The total passing time of different strategies ( $R_{1}=15 \mathrm{~m}$ ).

4) Average Computation Time: An important observation in Fig. 13 is that our proposed TD3-based strategy significantly outperforms other strategies in terms of average computation time. Notably, we utilize GPUs to accelerate parallel computation in the training stage. However, in the evaluation stage, all strategies are compared on CPUs of the same platform for fairness. As the initial positions become farther, the average computation time of the STRS and CS strategies increases due to the increase of the searching space. In particular, the STRS strategy is not a wise choice in practical implementations because the computation time is in the order of minutes. The CS strategy has a computation time of about 1-10 seconds due to its low algorithm complexity, however, at the expense of coordination efficiency. Admittedly, with the advancement and deployment of mobile edge computing (MEC) tech-

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-11.jpg?height=539&width=718&top_left_y=1021&top_left_x=1130)
Fig. 13. The average computation time of different strategies ( $R_{\mathrm{l}}=15 \mathrm{~m}$ ).

nologies, the coordination node could get a great arithmetic power or offload computation tasks to the cloud to reduce the computational latency. However, this may not meet the stringent real-time coordination requirements and is a waste of computation resources and power supply. Remarkably, our TD3-based strategy shows obvious advantages in terms of computational performance as the average computation time is 2-3ms. From Fig. 12 and Fig. 13, we can conclude that the TD3-based strategy can provide near-optimal coordination performances in static coordination scenarios while ensuring real-time coordination capabilities.
5) Traffic Throughput: In Fig. 14, we compare the traffic throughput of the CS and TD3 strategies in continuous traffic flow and also present how the left-turning radius influences the traffic throughput. Fig. 14(a) illustrates the average passing time versus the number of vehicles obtained by different strategies. From the figure, the average passing time decreases with the number of vehicles and turns out to be a stable value $1 / b^{\text {av }}$, i.e., the inverse of the mean coordination rate, indicating the lower the value the higher the traffic throughput. It is observed that the mean coordination rate of our proposed

TD3-based strategy is much better than CS strategy. For $R_{1}=15 \mathrm{~m}$, the TD3-based strategy with 0.75 vehicle/s in mean is better than CS strategy with 0.51 vehicle/s, which means 47\% advantage in traffic throughput. Moreover, the mean coordination rates of CS and TD3 strategies for $R_{1}=10 \mathrm{~m}$ are 0.49 vehicle/s and 0.97 vehicle/s, respectively. Compared with $R_{1}=15 \mathrm{~m}$, there is a $4 \%$ reduction and a $29.3 \%$ increase in traffic throughput for the CS and TD3 strategies, respectively. This result may be explained by the fact that a small leftturning radius means more space-time resources for the TD3based strategy but longer 2D paths for the CS strategy. Fig. 14(b) shows the cumulative distribution function (CDF) of average passing time.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-12.jpg?height=1315&width=784&top_left_y=784&top_left_x=213)
Fig. 14. Throughput of different strategies with respect to the number of vehicles.

## C. Multi-lane Scenario

For the CS and STRS strategies, the computational complexity grows exponentially with the number of lanes and vehicles, which presents challenges to multi-lane intersection coordination systems. In contrast, our TD3-based strategy can be easily extended to multi-lane intersections by simply adapting the input and output dimensions of the neural networks. Fig. 15 is a capture of the multi-lane dynamic vehicle coordination animation. The line at the rear of each vehicle represents the last 4s historical path, which highlights that the 2D paths of the vehicles are overlapped. The simulation parameters for the considered multi-lane scenario can be found in Table I. Fig. 16 compares the traffic throughput of singlelane and multi-lane scenarios. In the considered multi-lane scenario, each road has three lanes and the size of the CA is set as 48m×48m. The mean coordination rate for the considered multi-lane intersection is 1.37 vechile/s, which means a 82.7\% and 41.2\% improvement compared to single-lane intersection with $R_{1}=15 \mathrm{~m}$ and $R_{1}=10 \mathrm{~m}$. As can be seen from the figure, the traffic throughput of the three-lane intersection is less than twice of the single-lane one. This is because the CA's size of the three-lane intersection is 5.76 times larger than that of the single-lane intersection, resulting in the increase in coordination time.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-12.jpg?height=722&width=730&top_left_y=924&top_left_x=1147)
Fig. 15. A capture of the multi-lane dynamic vehicle coordination animation.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-12.jpg?height=574&width=776&top_left_y=1865&top_left_x=1128)
Fig. 16. Traffic throughput of single-lane and multi-lane scenarios.

## D. Laboratorial Experiments

Finally, we conduct experiments with four autonomous mobile robots based on robot operating system (ROS) [45] to verify the feasibility and practicability of the proposed coordination strategy. As shown in Fig. 17, we use a laptop as the centralized coordinator and broadcast control sequences to the robots via Wi-Fi links. Each robot is equipped with a motion control unit for trajectory tracking and an Intel RealSense T265 tracking camera for self-localization. The experiment parameters are set as $v_{\text {max }}=0.3 \mathrm{~m} / \mathrm{s}, a_{\text {max }}=0.1 \mathrm{~m} / \mathrm{s}^{2}$, $R_{1}=1.8 \mathrm{~m}, \Delta T=0.5 \mathrm{~s}, L_{\text {car }}=0.45 \mathrm{~m}, W_{\text {car }}=0.38 \mathrm{~m}$, $d_{\text {lon }}=0.5 \mathrm{~m}, d_{\text {lat }}=0.4 \mathrm{~m}$.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-13.jpg?height=372&width=885&top_left_y=776&top_left_x=161)
Fig. 17. Devices used in the experiments.

Fig. 18 shows an image of the experimental coordination scenario. Our strategy enables the four left-turning robots to occupy the intersection area simultaneously, pushing the intersection coordination capacity to its limit. Fig. 19 further analyzes the deviation of the planned trajectory (solid line) and actual trajectory (dashed line). The figure shows that both the planned and actual trajectories are within the occupied road region, illustrating that the safety redundancy is well set to circumvent safety hazards caused by system imperfections. Videos of our simulations and experiments can be found at the supplementary materials, or online at https://www.youtube.com/watch?v=FEwa-YuFFAk.

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-13.jpg?height=434&width=868&top_left_y=1775&top_left_x=172)
Fig. 18. Laboratorial experiments based on ROS robots.

## E. Discussions

By utilizing the offline learning methodology and real-time online processing capability of the DRL framework, our TD3based strategy allows a batch of CVs to share the intersection area simultaneously, which significantly improves the capacity

![](https://cdn.mathpix.com/cropped/f7414f5d-a44f-419b-a99a-cbe4e0150857-13.jpg?height=546&width=552&top_left_y=202&top_left_x=1242)
Fig. 19. The planned and actual trajectories.

of road intersections. Although near-optimal static coordination performance can be achieved, the optimal coordination strategy for continuous traffic flow is still worth investigating. As demonstrated in Algorithm 2, the WVs need to wait for the current batch of CVs to leave the CA before being coordinated. Such a strategy could avoid potential collisions between adjacent batches of CVs, but it sacrifices coordination performances. One option to address this issue is to coordinate more vehicles at a time, i.e., increasing the value of $N$. As long as $N$ is large enough, all vehicles inside the CCZ could be coordinated at a time, which will greatly reduce the number of batches and thus the waiting time. In practice, however, we recognize that the training time grows significantly as $N$ increases. In addition, $N$ should be chosen according to the traffic demand because low-traffic intersections have a small number of vehicles in the CCZ. Hence, there exists a trade-off between online performance and offline training costs. Another option is to develop a multi-batch management system to determine when to coordinate the next batch of CVs. Therefore, an additional optimization problem needs to be proposed to avoid collisions between different batches of CVs and reduce waiting time.

## V. Conclusion

In this paper, we have investigated the cooperative vehicle coordination problem at unsignalized road intersections, where the key issues to be addressed were traffic throughput, driving safety, long-term coordination stability, computational complexity, passenger comfort and system robustness. A unified optimization problem has been formulated to maximize the coordination capacity of the intersection while ensuring safety and stability. As the original optimization problem is computationally intractable in real-time, we have exploited the DRL to transform and solve it and devised the TD3based strategy. Moreover, the safety redundancy and speed profile smoother have also been designed to remedy system imperfections and passenger discomfort. Extensive simulation results and practical experiments have shown that our proposed TD3-based strategy can significantly improve traffic throughput and achieve near-optimal performances in static
coordination scenarios. The most impressive advantage is that our strategy has millisecond computational latency, which makes it promising to be implemented in practice.

Future research directions involve an extension of the presented framework to include a re-planning operation for accommodating system imperfections and alleviating accumulated trajectory error. Further, we will take turning radius into consideration and provide reference path alternatives to improve traffic throughput. Moreover, optimal dynamic coordination strategies in continuous traffic flow are expected to be further explored. We will study the interplay between traffic demand and batch size. A multi-batch management system will also be investigated to reduce waiting time.

## References

[1] M. Alsabaan, W. Alasmary, A. Albasir, and K. Naik, "Vehicular networks for a greener environment: A survey," IEEE Communications Surveys \& Tutorials, vol. 15, no. 3, pp. 1372-1388, 2012.
[2] S. Dornbush and A. Joshi, "Streetsmart traffic: Discovering and disseminating automobile congestion using vanet's," in 2007 IEEE 65th Vehicular Technology Conference-VTC2007-Spring. IEEE, 2007, pp. 11-15.
[3] G. Marfia and M. Roccetti, "Vehicular congestion detection and shortterm forecasting: a new model with results," IEEE Transactions on Vehicular Technology, vol. 60, no. 7, pp. 2936-2948, 2011.
[4] K. Mandal, A. Sen, A. Chakraborty, S. Roy, S. Batabyal, and S. Bandyopadhyay, "Road traffic congestion monitoring and measurement using active rfid and gsm technology," in 2011 14th International IEEE Conference on Intelligent Transportation Systems (ITSC). IEEE, 2011, pp. 1375-1379.
[5] D. Zhao, Y. Dai, and Z. Zhang, "Computational intelligence in urban traffic signal control: A survey," IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews), vol. 42, no. 4, pp. 485-494, 2011.
[6] D. Schrank, B. Eisele, T. Lomax, and J. Bak, "Urban mobility scorecard," Texas A\&M Transportation Institute, vol. 39, p. 5, 2015.
[7] E. Bellis and J. Page, "National motor vehicle crash causation survey (nmvccs) sas analytical users manual," Tech. Rep., 2008.
[8] J. Gao, Y. Shen, J. Liu, M. Ito, and N. Shiratori, "Adaptive traffic signal control: Deep reinforcement learning algorithm with experience replay and target network," arXiv preprint arXiv:1705.02755, 2017.
[9] B. Abdulhai, R. Pringle, and G. J. Karakoulas, "Reinforcement learning for true adaptive traffic signal control," Journal of Transportation Engineering, vol. 129, no. 3, pp. 278-285, 2003.
[10] L. Li, Y. Lv, and F.-Y. Wang, "Traffic signal timing via deep reinforcement learning," IEEE/CAA Journal of Automatica Sinica, vol. 3, no. 3, pp. 247-254, 2016.
[11] H. Wei, G. Zheng, H. Yao, and Z. Li, "Intellilight: A reinforcement learning approach for intelligent traffic light control," in Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining, 2018, pp. 2496-2505.
[12] X. Liang, X. Du, G. Wang, and Z. Han, "A deep reinforcement learning network for traffic light cycle control," IEEE Transactions on Vehicular Technology, vol. 68, no. 2, pp. 1243-1253, 2019.
[13] A. Haydari and Y. Yilmaz, "Deep reinforcement learning for intelligent transportation systems: A survey," IEEE Transactions on Intelligent Transportation Systems, 2020.
[14] P. Dai, K. Liu, Q. Zhuge, E. H.-M. Sha, V. C. S. Lee, and S. H. Son, "Quality-of-experience-oriented autonomous intersection control in vehicular networks," IEEE Transactions on Intelligent Transportation Systems, vol. 17, no. 7, pp. 1956-1967, 2016.
[15] J. Rios-Torres and A. A. Malikopoulos, "A survey on the coordination of connected and automated vehicles at intersections and merging at highway on-ramps," IEEE Transactions on Intelligent Transportation Systems, vol. 18, no. 5, pp. 1066-1077, 2016.
[16] L. Chen and C. Englund, "Cooperative intersection management: A survey," IEEE Transactions on Intelligent Transportation Systems, vol. 17, no. 2, pp. 570-586, 2016.
[17] S. Li, K. Shu, C. Chen, and D. Cao, "Planning and decision-making for connected autonomous vehicles at road intersections: A review," Chinese Journal of Mechanical Engineering, vol. 34, no. 1, pp. 1-18, 2021.
[18] Z. Zhang, R. Han, and J. Pan, "An efficient centralized planner for multiple automated guided vehicles at the crossroad of polynomial curves," IEEE Robotics and Automation Letters, vol. 7, no. 1, pp. 398-405, 2021.
[19] J. Lee and B. Park, "Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment," IEEE transactions on intelligent transportation systems, vol. 13, no. 1, pp. 81-90, 2012.
[20] A. Colombo and D. Del Vecchio, "Efficient algorithms for collision avoidance at intersections," in Proceedings of the 15th ACM international conference on Hybrid Systems: Computation and Control, 2012, pp. 145-154.
[21] R. Hult, G. R. Campos, P. Falcone, and H. Wymeersch, "An approximate solution to the optimal coordination problem for autonomous vehicles at intersections," in 2015 American Control Conference (ACC). IEEE, 2015, pp. 763-768.
[22] R. Hult, G. R. Campos, E. Steinmetz, L. Hammarstrand, P. Falcone, and H. Wymeersch, "Coordination of cooperative autonomous vehicles: Toward safer and more efficient road transportation," IEEE Signal Processing Magazine, vol. 33, no. 6, pp. 74-84, 2016.
[23] M. Wang, T. Zhang, L. Gao, and Q. Zhang, "High throughput dynamic vehicle coordination for intersection ground traffic," in 2018 IEEE 88th Vehicular Technology Conference (VTC-Fall), 2018, pp. 1-6.
[24] C. Liu, Y. Zhang, T. Zhang, X. Wu, L. Gao, and Q. Zhang, "High throughput vehicle coordination strategies at road intersections," IEEE Transactions on Vehicular Technology, vol. 69, no. 12, pp. 14341-14354, 2020.
[25] Y. Mo, M. Wang, T. Zhang, and Q. Zhang, "Autonomous cooperative vehicle coordination at road intersections," Journal of Communications and Information Networks, vol. 4, no. 1, pp. 78-87, 2019.
[26] -, "Intelligent offloading strategies for high throughput traffic intersection coordination," in 2019 IEEE Wireless Communications and Networking Conference Workshop (WCNCW), 2019, pp. 1-6.
[27] M. A. S. Kamal, J.-i. Imura, T. Hayakawa, A. Ohata, and K. Aihara, "A vehicle-intersection coordination scheme for smooth flows of traffic without using traffic lights," IEEE Transactions on Intelligent Transportation Systems, vol. 16, no. 3, pp. 1136-1147, 2014.
[28] H. Xu, Y. Zhang, L. Li, and W. Li, "Cooperative driving at unsignalized intersections using tree search," IEEE Transactions on Intelligent Transportation Systems, vol. 21, no. 11, pp. 4563-4571, 2019.
[29] H. Xu, C. G. Cassandras, L. Li, and Y. Zhang, "Comparison of cooperative driving strategies for cavs at signal-free intersections," IEEE Transactions on Intelligent Transportation Systems, 2021.
[30] C. Mavrogiannis, J. A. DeCastro, and S. S. Srinivasa, "Implicit multiagent coordination at unsignalized intersections via multimodal inference enabled by topological braids," arXiv preprint arXiv:2004.05205, 2020.
[31] Y. Zhang, R. Hao, T. Zhang, X. Chang, Z. Xie, and Q. Zhang, "A trajectory optimization-based intersection coordination framework for cooperative autonomous vehicles," IEEE Transactions on Intelligent Transportation Systems, pp. 1-15, 2021.
[32] P. Hang, C. Huang, Z. Hu, and C. Lv, "Driving conflict resolution of autonomous vehicles at unsignalized intersections: A differential game approach," arXiv preprint arXiv:2201.01424, 2022.
[33] R. Firoozi, X. Zhang, and F. Borrelli, "Formation and reconfiguration of tight multi-lane platoons," Control Engineering Practice, vol. 108, p. 104714, 2021.
[34] C. Ericson, Real-time collision detection. Crc Press, 2004.
[35] M. J. Neely, "Stochastic network optimization with application to communication and queueing systems," Synthesis Lectures on Communication Networks, vol. 3, no. 1, pp. 1-211, 2010.
[36] D. Silver, "Lectures on reinforcement learning," url: https://www. davidsilver.uk/teaching/, 2015.
[37] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski et al., "Human-level control through deep reinforcement learning," nature, vol. 518, no. 7540, pp. 529-533, 2015.
[38] Y. Song, M. Steinweg, E. Kaufmann, and D. Scaramuzza, "Autonomous drone racing with deep reinforcement learning," in 2021 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, 2021, pp. 1205-1212.
[39] J. Achiam, "Spinning Up in Deep Reinforcement Learning," 2018.
[40] R. S. Sutton and A. G. Barto, Reinforcement learning: An introduction. MIT press, 2018.
[41] S. Fujimoto, H. Hoof, and D. Meger, "Addressing function approximation error in actor-critic methods," in International conference on machine learning. PMLR, 2018, pp. 1587-1596.

[42] T. P. Lillicrap, J. J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, D. Silver, and D. Wierstra, "Continuous control with deep reinforcement learning," arXiv preprint arXiv:1509.02971, 2015.
[43] D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, and M. Riedmiller, "Deterministic policy gradient algorithms," in International conference on machine learning. PMLR, 2014, pp. 387-395.
[44] M. Werling, J. Ziegler, S. Kammel, and S. Thrun, "Optimal trajectory generation for dynamic street scenarios in a frenet frame," in 2010 IEEE International Conference on Robotics and Automation. IEEE, 2010, pp. 987-993.
[45] M. Quigley, K. Conley, B. Gerkey, J. Faust, T. Foote, J. Leibs, R. Wheeler, A. Y. Ng et al., "Ros: an open-source robot operating system," in ICRA workshop on open source software, vol. 3, no. 3.2. Kobe, Japan, 2009, p. 5.
