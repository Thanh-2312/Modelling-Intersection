# Collision-Free Cooperative Motion Planning and Decision-Making for Connected and Automated Vehicles at Unsignalized Intersections 

Xinle Gong ${ }^{\text {(1) }}$, Member, IEEE, Bowen Wang ${ }^{\text {(1) }}$, and Sheng Liang ${ }^{\text {(1) }}$


#### Abstract

This article proposes a novel cooperative motion planning and decision-making approach for connected and automated vehicles (CAVs) at unsignalized intersections, where a multivehicle collision-free trajectories generating problem is modeled as a constrained optimization problem. A learning-based iterative optimization (LBIO) algorithm is developed to solve the problem iteratively and obtain velocity-optimal trajectories using the historical vehicle states at previous iterations as data sets. To make the trained trajectories adapt to continuous and timevarying traffic flow, an online decision-making algorithm based on Monte Carlo tree search (MCTS) is presented to derive a timeoptimal vehicle passing sequence, where a tree structure is built to efficiently express all possible cluster-dividing modes between vehicles. In addition, we propose a trajectory planning algorithm to regulate velocities of vehicles in the cooperative control area surrounding the intersection. The proposed approach is validated on the SUMO under typical intersection scenarios. Results show that our approach enables potentially conflicting vehicles to go through the intersection simultaneously without queuing and significantly improves the overall traffic efficiency.


Index Terms-Connected and automated vehicles (CAVs), learning-based iterative optimization (LBIO), motion planning, unsignalized intersection.

## I. Introduction

A. Background and Motivation

THE RAPID urbanization and increasing commuting demand have brought great challenges to road transportation. As an important hub of the traffic network [1], intersections form the main source of congestion due to their high complexity for vehicle coordination. Consequently, the method to improve efficiency and safety at intersections has been extensively studied recently. In traditional intersection

[^0]scenarios, the vehicles usually are controlled by traffic signal lights and related research can be found in [2]. The main idea is to regulate vehicles by optimizing the signal control strategy.

Connected and automated vehicles (CAVs) attract more attention with the fast development of vehicle-to-infrastructure (V2I) communications [3]. As a result, some research focuses on developing cooperative driving methods based on the CAVs to ameliorate the intersection delays [4]. The intersection coordination generally can be categorized into decentralized and centralized architectures. The decentralized one requires low computational devices and deploy easily in practice [5]. However, the limited perceptible range makes it difficult to guarantee safety and global travel efficiency. The centralized approach compensates for vehicle perception deficiency with a central unit. For instance, Dresner and Stone [6] proposed a first come first serve (FCFS) policy based on a centralized scheme. The approach needs high-performance computing equipment. Meng et al. [7] concluded that the centralized architecture demonstrates a potential advantage when suffering high-density traffic flow. A comprehensive survey of both architectures can be seen in [8]. As the conflicting nature of vehicles at intersections, cooperative motion planning and decision-making approaches remain to be further developed.

## B. Related Works

Among the existing architecture, the optimization-based methods have been well-studied, such as mixed-integer programming (MIP) [9], [10] and nonlinear programming (NP) [11], [12]. The methods plan the optimal/suboptimal velocity profiles and time gaps of vehicles to avoid each group of vehicles simultaneously approaching cross-collision points using global information, mainly oriented to a centralized framework [13]. Lee and Park [14] proposed a centralized cooperative vehicle intersection control (CVIC) system to eliminate the potential overlaps of trajectories at intersections, and the optimal gap searching logic is converted to a nonlinear constrained optimization problem. Zhang et al. [15] designed a two-layer scheme to optimize path and speed profiles of the vehicles by using a centralized computing unit, which determines a feasible crossing channel based on the space-time block and a state trajectory at different layers.

With the number of vehicles increasing, the optimization problem is difficult to solve. To address this problem, Vaio et al. [16] proposed an optimization-based strategy in
a decentralized fashion, the method is testified via on-road experiments. Hult et al. [17] introduced a bilevel model predictive control (MPC) approach, where the coordination layer allocates occupation time period of vehicles in a decentralized manner and the vehicle layer calculates control command. To derive the global time-optimal vehicle passing decision. Xu et al. [18] suggested a hybrid architecture to decrease the computing burden based on the virtual platoon (VP) method, where the optimal control strategy can be calculated in a decentralized manner once the conflict-free decision sequence is determined by a centralized coordinator. Similarly, Zhou et al. [19] transferred the vehicles close to the intersection into coordinated independent VPs for efficient communication. To sum up, the existing optimizationbased method can generate proper cooperative trajectories. But the uncertainty risk of vehicle cooperative driving greatly increases for high dynamic intersection traffic flow. This article adopts an Monte Carlo tree search (MCTS)-based approach to derive the optimal vehicle passing sequence.

Learning-based methods, such as reinforcement learning (RL) [20] and deep RL (DRL) [21], are being attempted to apply for cooperative autonomous driving at complex intersections due to their self-learning ability. The methods learn a decision-making or control policy by training the historical/current data. Yan et al. [22] trained a policy considering the courteous behavior of automated vehicles by the DRL based on an IM unit, which allowed the automated vehicles yield to other vehicles to improve the traffic flow. Guan et al. [23] proposed a centralized intersection coordination scheme using RL. The optimal control policy is offline trained by a model accelerated proximal policy optimization algorithm for online application. Xu et al. [24] employed decentralized RL method to realize cooperative multi-intersection control.

Without a central coordinator at unsignalized intersection, vehicles have to understand surrounding vehicle intentions to make proper tactical planning for safe and efficient driving [25], [26]. To better account for environmental uncertainty, other machine learning methods like partially observable Markov decision process (POMDP) is commonly used to model the tactical planning task, which can derive the policy from past actions and states with high scalability and robustness [27]. For example, a continuous POMDP solver for tactical planning is proposed to obtain the driving strategy [28]. Hoel et al. [29] proposed a DRL-based approach for tactical decision-making, which can be employed in a variety of uncertain conditions. In addition, some researchers attempt to combine the optimization-based method, such as game theory (GT) [30] or MPC [31], with RL to derive optimal policy. Generally, the learning-based methods show their potential to address the safe and efficient driving problem at intersections for a single autonomous vehicle which makes it more compatible for decentralized architecture. However, there are still bottlenecks in transferring the learning-based methods from single vehicle-to-vehicle flow scenario due to limitations on training resources.

Last but not least, most of the existing methods do not analyze potential collision conflicts between vehicle trajectories

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-02.jpg?height=382&width=834&top_left_y=185&top_left_x=1104)
Fig. 1. Literature review summary for CAVs coordination.

in the conflict region from a spatial-temporal perspective in microscopic level, but achieve collision avoidance and multivehicle coordination by longitudinal speed planning based on a macroscopic level with a simplified point mass model and predefined straight, left or right turn paths. Although some studies have analyzed vehicle interactions in conflict areas considering the longitudinal and lateral characteristics [32], [33], only few vehicles are considered for the validation instead of time-varying traffic flow scenarios This article aims at the gap and leverages an iterative learning approach to generate cooperative motion trajectories. The literature review is summarized in Fig. 1.

## C. Contribution

The first contribution of this work is that an iterative learning-based trajectory optimization method is innovatively proposed to eliminate multivehicle conflicts at the unsignalized intersection. We first systematically analyze and summarize conflicting modes between vehicles. For each mode, multivehicle collision-free trajectory generating problem in space-time is modeled as a constrained optimization problem. the problem is solved off-line and iteratively where terminal constraint set and terminal cost function are rebuilt using closed-loop motion trajectories at previous iterations as data set. The relevance mechanism between vehicle trajectory and intersection time cost thereby is learned, and the optimal collision-free trajectories are obtained in only several iterations. As high flexibility of the generated trajectories, the proposed method allows conflicting vehicles to pass intersection simultaneously and avoid the time waste. Furthermore, the offline training process effectively reduces the computational load.

The MCTS-based decision-making algorithm is declared as the secondary contribution, which makes the offline trained collision-free trajectories adapt to high-dynamic and highdensity intersection traffic flow. The proposed algorithm engages a decision tree to express all possible cluster-dividing modes between vehicles for an arbitrary intersection traffic flow. Through the finite iterative calculation of the best child node, the cluster-dividing decision gradually converges to an optimal vehicle passing sequence. Since we systematically consider the influence of cluster-dividing decision of vehicles in front on that of rear vehicles with the tree structure, the overall efficiency for vehicles to pass the intersection is effectively improved. Furthermore, the algorithm has fast convergence speed and can search for the optimal decision-making

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-03.jpg?height=410&width=859&top_left_y=187&top_left_x=176)
Fig. 2. Intersection coordination decision-making and control framework.

sequence with fewer times, enabling it to be online applied in real-time based on roadside units.

A customized trajectory planning method to regulate vehicle velocity in a cooperative area is regarded as the third contribution. we develop a differential-based two accelerating/decelerating stages velocity planning algorithm to guarantee the vehicles reach the intersection at specified state. By updating the planning results at each moment, vehicle flow can be well coordinated in an orderly manner to follow the formation of the cluster-dividing sequence and the trained condition.

This article is organized as follows. Section II introduces the system model and crossing mode of typical unsignalized intersection. Sections III-V propose the cooperative motion planning and decision-making method. Section VI verifies the performance of the proposed approach based on SUMO. Conclusions are summarized in Section VII. The logical architecture of this article is illustrated in Fig. 2.

## II. Problem Statement and Formulation

## A. Intersection Scenario

A typical four-way one-lane unsignalized intersection scenario as shown in Fig. 3 is considered in this work. We divide the intersection into cooperative area $\Psi$ and noncooperative area $\hat{\Psi}$ by a circle with the radius of $R_{c}$. Assuming that the vehicles (only the CAVs) in the $\Psi$ can realize communication with a centralized coordinator. Vehicle state, i.e., position, velocity and turning intention, etc., can be uploaded to the coordinator for processing, and the planned results are returned to the vehicles for control execution.

For the sake of introducing of the proposed algorithm, we counterclockwise number all vehicles in the cooperative area according to the distances to the intersection. The color and turning actions of the vehicles are also listed (see Fig. 3).

## B. Traffic Crossing Mode

In the defined scenario, we represent lane directions of south, east, north, and west, respectively, by $\{S, N, E, W\}$. Three possible vehicle actions, i.e., straight ahead, left turn, and right turn are denoted by $\{L, T, R\}$. Fig. 4 shows common passing modes. Potential collisions may occur when vehicles arrive at intersection. We define $\{O\}$ as the case that there is no vehicle entering the intersection at the corresponding

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-03.jpg?height=793&width=821&top_left_y=187&top_left_x=1109)
Fig. 3. Typical intersection scenario.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-03.jpg?height=363&width=844&top_left_y=1087&top_left_x=1098)
Fig. 4. Common crossing mode.

lane. To uniformly describe the crossing modes of vehicles, we construct a set † as

$$
\dagger=\left\{\{\Pi\}_{S},\{\Pi\}_{E},\{\Pi\}_{N},\{\Pi\}_{W}\right\}
$$

where $\Pi \in\{L, T, R, O\}$. The simplification of the crossing model set † , e.g., LLTR, is used in the following section.

Based on the above definition, we systematically analyze and summarize 256 crossing modes, including 14 free-modes and 242 conflict modes in the four-way single-lane scenario.

## C. System Model

As vehicle speed is relatively low at the intersection, the kinematic model is used to describe the vehicle motion. For an arbitrary vehicle $i$ in the cooperative area, we employ $\xi_{i}=$ $\left[X_{i}, Y_{i}, \varphi_{i}, v_{i}\right]$ as the state vector and $u_{i}=\left[a_{i}, \delta_{i}\right]$ as the input vector. The differential expressions are given as

$$
\left\{\begin{array}{l}
\dot{v}_{i}=a_{i} \\
\dot{\varphi}_{i}=\frac{v_{i}}{\left(l_{f, i}+l_{r, i}\right)} \sin \delta_{i} \\
\dot{X}_{i}=v_{i} \cos \left(\varphi_{i}+\delta_{i}\right) \\
\dot{Y}_{i}=v_{i} \sin \left(\varphi_{i}+\delta_{i}\right)
\end{array}\right.
$$

where $X_{i}$ and $Y_{i}$ represent the position in cartesian coordinate system, $\varphi_{i}$ is the heading angle, $v_{i}$ denotes the vehicle speed,
$l_{f, i}$ and $l_{r, i}$ are the distances from front and rear axis to center of gravity (CoG). The control inputs $\delta_{i}$ and $a_{i}$ are steering angle and acceleration, respectively. For the control design, we rewrite the differential expression into discrete-time system as

$$
\xi_{i, t+1}=f_{i}\left(\xi_{i, t}, u_{i, t}\right) .
$$

At time $t$, in order to uniformly represent the state vector $\xi_{i}$ and the control vector $u_{i}$ of all vehicles in the cooperative area, we construct $\boldsymbol{\xi}_{t}$ and $\boldsymbol{u}_{t}$ as follows:

$$
\begin{aligned}
\boldsymbol{\xi}_{t} & =\left[\xi_{1, t}, \xi_{2, t}, \ldots, \xi_{M, t}\right]^{T} \in \mathbb{R}^{M} \\
\boldsymbol{u}_{t} & =\left[u_{1, t}, u_{2, t}, \ldots, u_{M, t}\right]^{T} \in \mathbb{R}^{M}
\end{aligned}
$$

where $M$ denotes the number of vehicles.

## III. Collision-Free Trajectories Learning

In this section, a learning-based iterative optimization (LBIO) method is introduced to realize the cooperative motion of multivehicle based on the intersection conflict mode. Our goal is to enable vehicles to safely cross the intersection with minimum time. The detail is given in the following.

## A. Terminal State Set

At each iteration, the terminal constraint set is modeled to provide feasible terminal states for the iterative optimization algorithm design using the historical vehicle motion states. For $m(m \leq 4)$ vehicles with the given conflict mode, we define the vectors $\boldsymbol{\xi}_{i}^{j}$ and $\boldsymbol{u}_{i}^{j}$, respectively, to collect the closed-loop states and inputs of the vehicle $i$ during the $j$ th iteration

$$
\begin{aligned}
\boldsymbol{\xi}_{i}^{j} & =\left[\xi_{i, 0}^{j}, \xi_{i, 1}^{j}, \ldots, \xi_{i, T_{i}^{j}}^{j}\right]^{T} \in \mathbb{R}^{T_{i}^{j}} \\
\boldsymbol{u}_{i}^{j} & =\left[u_{i, 0}^{j}, u_{i, 1}^{j}, \ldots, u_{i, T_{i}^{j}-1}^{j}\right]^{T} \in \mathbb{R}^{T_{i}^{j}-1}
\end{aligned}
$$

where $i \in\{1, \ldots, m\} . T_{i}^{j}$ denotes the time cost of the vehicle $i$ from the start to target position along the $j$ th iteration. To guarantee initial feasibility of the optimization algorithm, we need to provide an initial feasible collision-free trajectory. At each iteration, the vehicle is assigned the same initial and target position $\xi_{i, 0}$ and $\xi_{i, F}$, respectively

$$
\xi_{i, 1}^{j}=\xi_{i, 0}, \quad \xi_{i, T^{j}}^{j}=\xi_{i, F}, \quad \forall j \geq 0 .
$$

In addition, to describe integrally the historical close-loop states, inputs and time costs of all $m$ vehicles in iterations, we define the datasets $\mathcal{D}_{\xi}=\left\{\boldsymbol{\xi}^{0}, \ldots, \boldsymbol{\xi}^{j}, \ldots,\right\}, \mathcal{D}_{u}=$ $\left\{\boldsymbol{u}^{0}, \ldots, \boldsymbol{u}^{j}, \ldots,\right\}$, and $\mathcal{D}_{T}=\left\{\boldsymbol{T}^{0}, \ldots, \boldsymbol{T}^{j}, \ldots,\right\}$, where $\boldsymbol{\xi}^{j}=$ $\left[\xi_{1}^{j}, \ldots, \xi_{m}^{j}\right] \in \mathbb{R}^{m}, \boldsymbol{u}^{j}=\left[\boldsymbol{u}_{1}^{j}, \ldots, \boldsymbol{u}_{\boldsymbol{m}}^{j}\right] \in \mathbb{R}^{m}$, and $\boldsymbol{T}^{j}=$ $\left[T_{1}^{j}, \ldots, T_{m}^{j}\right] \in \mathbb{R}^{m}$.

For the construction of terminal state set, the minimal time cost and corresponding trajectories from the datasets $\mathcal{D}_{\xi}$ and $\mathcal{D}_{T}$, respectively, need to be first selected, which are given as

$$
\boldsymbol{T}^{q}=\min _{q \in\{0, \ldots, j-1\}} \boldsymbol{T}^{j-1} \in \mathcal{D}_{T}, \quad \boldsymbol{\xi}^{q} \in \mathcal{D}_{\xi} .
$$

Since the terminal constraint set is time-varying, a time base needs to be determined for all vehicles. We heuristically calculate time base using the maximum time cost in $T^{q}$ as

$$
T^{q}=\max \left\{T_{1}^{q}, \ldots, T_{i}^{q}, \ldots, T_{m}^{q}\right\} \in \boldsymbol{T}^{q} .
$$

Based on (7) and (8), at time $t$ of the $j$ th iteration there exists an input sequence $\boldsymbol{u}_{i, t+N: T^{q}}^{q}$ satisfying $f\left(\xi_{i, k}^{q}, u_{i, k}^{q}\right) \in \boldsymbol{\xi}_{i}^{q}$ where $k \in\left\{t+N: T^{q}\right\}$ and $N$ is prediction horizon, to guarantee the vehicle $\xi_{i, F}$ reaching the target state from the state $\xi_{i, t+N}^{q}$ in time cost $\left(T^{q}-t-N\right)$. Therefore, the trajectory points $\xi_{i, t+N+\Delta t}^{q}$ of the $j$ th iteration at from $t+N$ to $T^{q}$ are selected to build the terminal constraint set, that is given by

$$
\mathcal{T} \mathcal{S}_{i, t}^{j}=\left\{\begin{array}{l}
\left\{\xi_{i, t+N+\Delta t}^{q} \in \mathcal{D}_{\xi}\right\}, \quad t+N<T^{q} \\
\left\{\xi_{i, F}\right\}, \quad t+N \geq T^{q}
\end{array}\right.
$$

where $t+N+\Delta t \in\left\{t+N, \ldots, T^{q}\right\}$, and the terminal state $\xi_{i, F}$ is taken as the unique point in $\mathcal{T} \mathcal{S}_{i, t}^{j}$ when $t+N \geq T_{i}^{q}$.

At $t+1$, the terminal state set will be updated by injecting new information from the historical datasets $\mathcal{D}_{\xi}$ and $\mathcal{D}_{T}$.

## B. Collision-Free Constraint

A global collision-free constraint should be constructed to ensure the driving safety of the vehicles. Vehicle Collisionfree indicates that there exists a division plane capable of completely separating their trajectories in space and time. In this section, we apply support vector machine (SVM) to divide the hyperplane between historical trajectories of two vehicles, thereby obtaining the collision-free constraints.

At time $t$ of the $j$ th iteration, the position vector of the vehicles $i_{1}$ and $i_{2}$ can be denoted by $\eta_{i_{1}, t}^{j}=\left[X_{i_{1}, t}^{j}, Y_{i_{1}, t}^{j}\right]^{T}$ and $\eta_{i_{2}, t}^{j}=\left[X_{i_{2}, t}^{j}, Y_{i_{2}, t}^{j}\right]^{T}$, respectively. We define a data vector to collect vector segments of the historical trajectories $\boldsymbol{\xi}_{i_{1}}^{j}$ and $\boldsymbol{\xi}_{i_{2}}^{j}$ from $t$ to $t+l_{s}$, that is defined as

$$
\begin{aligned}
\boldsymbol{\eta}_{t}=\{ & \left(\eta_{i, t}^{j}, \lambda_{t}\right),\left(\eta_{i, t+1}^{j}, \lambda_{t+1}\right), \ldots, \\
& \left., \ldots,\left(\eta_{i, t+k}^{j}, \lambda_{t+k}\right),\left(\eta_{i, t+l_{s}}^{j}, \lambda_{t+l_{s}}\right)\right\} \in \mathbb{R}^{l_{s}}
\end{aligned}
$$

where $i \in\left\{i_{1}, i_{2}\right\}, l_{s}$ is the time length determined by the demand, and $\lambda_{t+k} \in\{-1,1\}$ represents the label for indexing of different data categories.

Based on (10), we build a problem for $k \in\left\{0, \ldots, l_{s}\right\}$ as

$$
\begin{aligned}
& \mathcal{V}\left(\eta_{i, t+k}^{j}\right)=\min \frac{1}{2}\left(W_{t}^{j}\right)^{T} W_{t}^{j} \\
& \text { s.t. } y_{t+k} \cdot\left[\left(W_{t}^{j}\right)^{T} \eta_{i, t+k}^{j}+b_{t}^{j}\right] \geq 1 \\
& \quad\left\|\eta_{i_{1}, t}-\eta_{i_{2}, t}\right\|_{2} \geq d_{r}
\end{aligned}
$$

where $d_{r}$ represents safe distance between two vehicles.
By solving the optimization problem (11), we obtain the optimal hyperplane parameters $W_{t}^{*, j}, b_{t}^{*, j}$ at time $t$. Then the collision-free constraints for the vehicle $i$ are built as

$$
\left(K_{i, t}^{j}\right)^{T} \eta_{i, t+k}^{j}+h_{i, t}^{j} \leq 0
$$

where $K_{i, t}^{j} \in\left\{-W_{t}^{*, j}, W_{t}^{*, j}\right\}$ and $h_{i, t}^{j} \in\left\{-b_{t}^{*, j}-1, b_{t}^{*, j}-1\right\}$
For more than two vehicles in the system, the collision-free constraints need to be solved in pairs of arbitrary two vehicles. Therefore, at time $t$ there exist $m-1$ groups of constraints for the vehicle $i$, that are given by

$$
\boldsymbol{K}_{i, t}^{j}=\left[K_{i, t}^{j, 1}, K_{i, t}^{j, 2}, \ldots, K_{i, t}^{j, m-1}\right]^{T} \in \mathbb{R}^{m-1}
$$

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-05.jpg?height=361&width=814&top_left_y=180&top_left_x=198)
Fig. 5. Time-varying piecewise safe driving corridor.

$$
\boldsymbol{h}_{i, t}^{j}=\left[h_{i, t}^{j, 1}, h_{i, t}^{j, 2}, \ldots, h_{i, t}^{j, m-1}\right]^{T} \in \mathbb{R}^{m-1} .
$$

Based on (15), the collision avoidance constraint at the $j$ th iteration can be transformed into a compact expression as

$$
g_{i, t}^{j}\left(\eta_{i, t}^{j}\right)=\left(\boldsymbol{K}_{i, t}^{j}\right)^{T} \eta_{i, t}^{j}+\boldsymbol{h}_{i, t}^{j} \preceq 0 .
$$

The global collision-free constraint will be recalculated by intercepting new segments at time $t+1$.

## C. Safe Driving Corridor

The vehicle should strictly satisfy the intersection rules and cannot cross into the reverse lane. Thus, at the trajectory generating stage, we need to constrain all vehicles in specified lane. In this section, the safe driving corridor is given by

$$
r_{i, t}^{j, L}\left(X_{i, t}^{j}\right) \leq \eta_{i, t}^{j} \leq r_{i, t}^{j, U}\left(X_{i, t}^{j}\right)
$$

where $r_{i, t}^{j, U}$ and $r_{i, t}^{j, L}$ denote the left and right bound.
Fig. 5 illustrates different types of constrained corridors. To maintain continuous feasibility of the optimization problem, the safe driving corridor with multiple segments will be divided into several convex sets.

## D. Time Cost

In this section, we model the time-optimal cost function to characterize the intersection traffic efficiency. At time $t$ of the $j$ th iteration, the time cost of driving the vehicle $i$ from the current state $\xi_{i, t}$ to the target state $\xi_{i, F}$ is denoted as

$$
H_{i, t \rightarrow T_{i}^{j}}^{j}\left(\xi_{i, t}^{j}, t\right)=\sum_{t=0}^{T_{i}^{j}} p\left(\xi_{i, t}^{j}, u_{i, t}^{j}\right)
$$

where $p(\cdot, \cdot)$ is the stage cost that is given by

$$
p\left(\xi_{i, t}, u_{i, t}\right)=\left\{\begin{array}{l}
0, \text { if } \xi_{i, t}=\xi_{i, F} \\
1, \text { otherwise }
\end{array}\right.
$$

The optimization problem with (16) is generally nontrivial. To reduce the computational burden, we approximate the function (16) with two parts, i.e., the $N$-step accumulative time cost and the terminal cost. The former is given by

$$
H_{i, t \rightarrow t+N}^{j}\left(\xi_{i, t}^{j}, t\right)=\sum_{t}^{t+N} p\left(\xi_{i, t}^{j}, u_{i, t}^{j}\right)
$$

where the terminal state $\xi_{i, t+N}^{j} \in \mathcal{T} \mathcal{S}_{i, t}^{j-1}$.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-05.jpg?height=339&width=814&top_left_y=185&top_left_x=1113)
Fig. 6. Iterative optimization process.

The terminal cost denotes the time consume from the terminal state $\xi_{i, t+N}^{j}$ to the state $\xi_{i, F}$, that can be approximately calculated using historical trajectories. In particular, we select the minimal time cost from the time $t+N$ to the target position in the historical datasets, i.e., the data of the $q$ th iteration, as the terminal cost

$$
\begin{aligned}
& R_{i, t+N+1 \rightarrow T_{i}^{j}}^{j}\left(\xi_{i, t}^{j}, t\right)= \\
& \begin{cases}\sum_{t+N+1}^{T_{i}^{j}} p\left(\xi_{i, t}^{j}, u_{i, t}^{j}\right)=T_{i}^{q}-(t+N), & \text { if } \xi_{i, t}^{j} \in \xi_{i, t+N: T_{i}^{q}}^{q} \\
+\infty, & \text { otherwise } .\end{cases}
\end{aligned}
$$

## E. Learning-Based Iterative Optimization

At time $t$ the $j$ th iteration, we formulate the constrained optimization control problem for the collision-free trajectory generation of the vehicle $i$ as

$$
\begin{aligned}
\min _{u_{i, 0: N-1 \mid t}^{*, j}} & H_{i, t \rightarrow t+N}^{j}\left(\xi_{i, t}^{j}, t\right)+R_{i, t+N+1 \rightarrow T_{i}^{j}}^{j}\left(\xi_{i, t}^{j}, t\right) \\
\text { s.t. } & \xi_{i, k+1 \mid t}^{j}=f_{i}\left(\xi_{i, k \mid t}^{j}, u_{i, k \mid t}^{j}\right) \\
& u_{i, \min } \leq u_{i, k \mid t} \leq u_{i, \max } \\
& \Delta u_{i, \min } \leq u_{i, k+1 \mid t}-u_{i, k \mid t} \leq \Delta u_{i, \max } \\
& g_{i, t+k}^{j-1}\left(\xi_{i, k \mid t}^{j}\right) \leq 0, r_{i, t+k}^{j}\left(\xi_{i, k \mid t}^{j}\right) \preceq 0 \\
& \xi_{i, N \mid t}^{j} \in \mathcal{T} \mathcal{S}_{i, t+N}^{j-1}, \xi_{i, 0 \mid t}^{j}=\xi_{i, t-1}^{j} \\
& \forall k \in\{0, \ldots, N-1\}
\end{aligned}
$$

where $k \mid t$ denotes the $k$ th step prediction at time $t$. Equation (20b) is the vehicle model. Equations (20c) and (20d) are boundary constraints of vehicle input and input rate, respectively. The collision avoidance and safe driving corridor are indicated by (20e). $\xi_{i, N \mid t}^{j}$ in (20f) is the terminal state, which is enforced into the set $\mathcal{T} \mathcal{S}_{i, t}^{j}$ derived by (10). The state $\xi_{i, t-1}^{j}$ is regarded as the initial condition at time $t$ in (20f).

Fig. 6 shows the iteration optimization process at time $t$ of $j^{\text {th }}$ iteration. To find the optimal iterative solution of (20), the first step is to select an arbitrary historical trajectory point in $\mathcal{T} \mathcal{S}_{i, t}^{j}$ as terminal state $\xi_{i, N \mid t}^{j}$, and solve (20) to obtain a control input vector $\boldsymbol{u}_{i, 0: N-1 \mid t}^{j}$ and an accumulative stage cost $C h_{i, t}^{j}$. The terminal cost then is calculated using (19), denoted as $C r_{i, t}^{j}$. The overall cost thus is represented by $C o_{i, t}^{j}=C h_{i, t}^{j}+C r_{i, t}^{j}$. For each historical trajectory point in $\mathcal{T} \mathcal{S}_{i, t}^{j}$, the above process is repeatedly performed and a feasible

```
Algorithm 1: Collision-Free Trajectories Generating
    Input: \(\boldsymbol{\xi}^{0}, \boldsymbol{u}^{0}, \boldsymbol{T}^{0}, Z_{l}, N, m\)
    \(\mathcal{D}_{\xi} \leftarrow\left\{\boldsymbol{\xi}^{0}\right\}, \mathcal{D}_{u} \leftarrow\left\{\boldsymbol{u}^{0}\right\}, \mathcal{D}_{T} \leftarrow\left\{\boldsymbol{T}^{0}\right\}\)
    \(\left\{g_{i, t}^{0}(\cdot) \preceq 0 \leftarrow \text { Solve } \mathcal{V}\left(\eta_{i, t+k}^{0}\right)\right\}_{i \in \Psi},\left\{\mathcal{T} \mathcal{S}_{i, t}^{0}\right\}_{i \in \Psi}\)
    for \(j \in\left\{1,2, \ldots, Z_{l}\right\}\) do
        \(\boldsymbol{\xi}^{j} \leftarrow \emptyset, \boldsymbol{u}^{j} \leftarrow \emptyset, \boldsymbol{T}^{j} \leftarrow \emptyset\)
        for vehicle \(i \in\{1, \ldots, m\}\) in parallel do
            \(t \leftarrow 0, \xi_{i, 0}^{j} \leftarrow \xi_{i, 0}, \boldsymbol{\xi}_{i}^{j} \leftarrow\left\{\xi_{i, 0}\right\}, \boldsymbol{u}_{i}^{j} \leftarrow \emptyset\)
            while \(\xi_{i, t}^{j} \neq \xi_{i, F}\) do
                \(\boldsymbol{U}_{i, t}^{j} \leftarrow \emptyset, \boldsymbol{C}_{i, t}^{j} \leftarrow \emptyset\)
                \(r_{i, t}^{j}(\cdot) \preceq 0 \leftarrow\) Update \(r_{i, t}^{j, L}\left(X_{i, t}^{j}\right), r_{i, t}^{j, U}\left(X_{i, t}^{j}\right)\)
                for \(\xi_{i, N \mid t} \in \mathcal{T} \mathcal{S}_{i, t}^{j}\) do
                    \(C r_{i, t}^{j}, C h_{i, t}^{j}, u_{i, t}^{j} \leftarrow\) Solve (22)
                    \(\boldsymbol{U}_{i, t}^{j} \leftarrow \boldsymbol{U}_{i, t}^{j} \cup\left\{u_{i, t}^{j}\right\}\)
                    \(\boldsymbol{C}_{i, t}^{j} \leftarrow \boldsymbol{C}_{i, t}^{j} \cup\left\{C h_{i, t}^{j}+C r_{i, t}^{j}\right\}\)
                end
                \(u_{i, t}^{*, j}, C o_{i, t}^{*, j} \leftarrow\) Search from \(\left\{\boldsymbol{U}_{i, t}^{j}, \boldsymbol{C}_{i, t}^{j}\right\}\)
                \(\xi_{i, t+1}^{*, j} \leftarrow\) Calculate \(f_{i}\left(\xi_{i, t}^{j}, u_{i, t}^{*, j}\right)\)
                \(\boldsymbol{\xi}_{i}^{j} \leftarrow \boldsymbol{\xi}_{i}^{j} \cup\left\{\xi_{i, t+1}^{*, j}\right\}, \boldsymbol{u}_{i}^{j} \leftarrow \boldsymbol{u}_{i}^{j} \cup\left\{u_{i, t}^{*, j}\right\}\)
                \(t \leftarrow t+1, T_{i}^{j} \leftarrow t\)
            end
            \(\boldsymbol{\xi}^{j} \leftarrow \boldsymbol{\xi}^{j} \cup\left\{\boldsymbol{\xi}_{i}^{j}\right\}, \boldsymbol{u}^{j} \leftarrow \boldsymbol{u}^{j} \cup\left\{\boldsymbol{u}_{i}^{j}\right\}, \boldsymbol{T}^{j} \leftarrow \boldsymbol{T}^{j} \cup\left\{T_{i}^{j}\right\}\)
        end
        \(\mathcal{D}_{\xi} \leftarrow \mathcal{D}_{\xi} \cup\left\{\boldsymbol{\xi}^{j}\right\}, \mathcal{D}_{u} \leftarrow \mathcal{D}_{u} \cup\left\{\boldsymbol{u}^{j}\right\}, \mathcal{D}_{T} \leftarrow \mathcal{D}_{T} \cup\left\{\boldsymbol{T}^{j}\right\}\)
        \(\left\{g_{i, t}^{j}(\cdot) \preceq 0 \leftarrow \text { Solve } \mathcal{V}\left(\eta_{i, t+k}^{j}\right)\right\}_{i \in \Psi},\left\{\mathcal{T} \mathcal{S}_{i, t}^{j}\right\}_{i \in \Psi}\)
    end
    \(\boldsymbol{\xi}_{\text {ref }, \dagger}^{\text {LBIO }} \leftarrow \boldsymbol{\xi}^{Z_{l}}, T_{\text {ref }, \dagger}^{\text {LBIO }} \leftarrow \max _{i \in\{1, \ldots, m\}}\left\{T_{1}^{Z_{l}}, \ldots, T_{m}^{Z_{l}}\right\}\)
    Output: \(\xi_{\text {ref }, \ddagger}^{\text {LBIO }}, T_{\text {ref }, \ddagger}^{\text {LBIO }}\)
```

solution dataset $\left\{\boldsymbol{U}_{i, t}^{j}, \boldsymbol{C}_{i, t}^{j}\right\}$ can be obtained, where the vectors of control inputs and overall costs is $\boldsymbol{U}_{i, t}^{j}=\left[\boldsymbol{u}_{i, 0: N-1 \mid t}^{j}, \ldots,\right]^{T}$ and $\boldsymbol{C}_{i, t}^{j}=\left[C o_{i, 0: N-1 \mid t}^{j}, \ldots,\right]^{T}$. The second step is to search the minimal cost $C o_{i, t}^{*, j}$ from the constructed dataset $\left\{\boldsymbol{U}_{i, t}^{j}, \boldsymbol{C}_{i, t}^{j}\right\}$, and the corresponding optimal control input vector $\boldsymbol{u}_{i, 0: N-1 \mid t}^{*, j}=$ $\left[u_{i, 0 \mid t}^{*, j}, \ldots, u_{i, N-1 \mid t}^{*, j}\right]^{T}$. At time $t$ of the $j$ th iteration, the first element of $\boldsymbol{u}_{i, 0: N-1 \mid t}^{*, j}$, i.e., $u_{i, t}^{*, j}=u_{i, 0 \mid t}^{*, j}$, is used as the optimal solution to apply for the vehicle $i$ and the actual vehicle state $\xi_{i, t+1}^{*, j}$ can be measured.

Similarly, the problem (20) for other vehicles in the system is solved in parallel until they reach their target positions. The terminal constraint set is updated at the next iteration.

## F. Collision-Free Trajectories Generation

A collision-free trajectory generation algorithm is designed to derive optimal trajectories for a given conflict mode. The detailed process is illustrated in Algorithm 1. Lines 1 to 2 in Algorithm 1 represent initialization of the datasets, collision-free constraints, and terminal set. The for-loop from lines 3-24 shows the iterative process of trajectory training for $m$ vehicles. The final vehicle trajectories and time cost

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-06.jpg?height=943&width=849&top_left_y=178&top_left_x=1094)
Fig. 7. Trajectories comparison between initial and final iteration. (a) LLTR mode. (b) OTLL mode. (c) LOLL mode. (d) OTLO mode.

is obtained in line 25. We train the optimal multivehicle motion trajectories and time costs for all conflict modes by Algorithm 1, and collect them by $\boldsymbol{\xi}_{\text {ref }}^{\mathrm{LBIO}}$ and $\boldsymbol{T}_{\text {ref }}^{\mathrm{LBIO}}$

$$
\begin{aligned}
& \xi_{\text {ref }}^{\mathrm{LBIO}}=\left\{\xi_{\text {ref,LLTR }}^{\mathrm{LBIO}}, \xi_{\text {ref,LLLL }}^{\mathrm{LBIO}}, \ldots, \xi_{\text {ref }, \dagger}^{\mathrm{LBIO}}\right\} \\
& \boldsymbol{T}_{\text {ref }}^{\mathrm{LBIO}}=\left\{T_{\text {ref,LLTR }}^{\mathrm{LBIO}}, T_{\text {ref,LLLL }, \ldots, T_{\text {ref }, \dagger}^{\mathrm{LBIO}}}^{\mathrm{LBIO}}\right\} .
\end{aligned}
$$

Due to the page limitation, we only illustrate the trained collision-free trajectories for the conflict modes LLTR, LOLL, OTLL, and OTLO. During the training process, the lane width is set to 5 m, the initial position of each vehicle is 9 m far from the center point of the intersection and the terminal position is determined according to vehicle maneuver.

Fig. 7 shows trajectory comparisons between the initial and final iterations where the time interval between points at each trajectory is the same. The denser the points, the slower the vehicle movement. We can see that the vehicles take a long time to go through the intersection without collisions at the 0th iteration. After near convergence, i.e., at the 15th iteration, distributions of vehicle trajectory points become sparse, indicating that the vehicles pass the intersection in shorter time. The results demonstrate that cooperative collision-free trajectories can be learned by the proposed algorithm.

Fig. 8 illustrates time costs of four conflict modes during the offline iterations, which provides a more intuitive view of the convergence process. The time costs of vehicles gradually decrease and finally converge to the stable value in only several iterations. By comparing the convergence speeds of four conflict modes, it can be seen that the trained trajectories are related to the complexity of the conflict mode. The proposed algorithm converges faster with fewer conflict vehicles and

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-07.jpg?height=924&width=849&top_left_y=180&top_left_x=183)
Fig. 8. Time costs of four common conflict modes. (a) LLTR mode. (b) OTLL mode. (c) LOLL mode. (d) OTLO mode.

TABLE I
Computational Time for Trajectory Generation
| Mode | Total time [s] | Initial iteration [s] | Final iteration [s] |
| :--- | :--- | :--- | :--- |
| LLLL | 2982.15 | 512.18 | 61.34 |
| LLTR | 2749.97 | 416.83 | 50.41 |
| LLOL | 1100.07 | 134.66 | 41.92 |
| OTLL | 964.12 | 113.71 | 34.31 |
| OTLO | 325.87 | 34.22 | 25.77 |


simpler conflict scenarios. It is consistent with the natural characteristics of the learning-based algorithm.

The offline computational time for collision-free trajectory generation with the typical crossing mode is summarized in Table I, where the time cost during initial and final iterations is recorded. With the iterative process running, the algorithm learns correlation mechanism between time cost and conflicting trajectories, thus the solution time is gradually reduced. The computational time for each mode is around 5-50 min.

## IV. Cluster-Dividing Decision-Making

To apply the trained trajectories at dynamic and continuous traffic flows, we need to divide vehicles in groups. In this work, each group is defined as a cluster with the same crossing mode. We denote the $n$th cluster with crossing mode † as

$$
\mathcal{C}_{\dagger}^{n}=\left\{\{i, \Pi\}_{S},\{i, \Pi\}_{E},\{i, \Pi\}_{N},\{i, \Pi\}_{W}\right\}
$$

where $i$ represents the vehicle index.

A simplified case of traffic scene is extracted from Fig. 3, including vehicles with indexes 1-10. According to vehicle queuing orders, the clusters can be generally indicated as

$$
\begin{aligned}
\mathcal{C}_{\ddagger}^{1} & =\left\{\{1, R\}_{S},\{2, L\}_{E},\{3, L\}_{N},\{4, L\}_{W}\right\} \\
\mathcal{C}_{\ddagger}^{2} & =\left\{\{5, T\}_{S},\{6, T\}_{E},\{7, L\}_{N},\{8, T\}_{W}\right\} \\
\mathcal{C}_{\ddagger}^{3} & =\left\{\{9, L\}_{S},\{10, L\}_{E},\{0, T\}_{N},\{0, R\}_{W}\right\}
\end{aligned}
$$

where 0 in the cluster $\mathcal{C}_{\dagger}^{3}$ represents no vehicle in this direction. Based on (23), the vehicle flow can be transformed compactly into a cluster-dividing result

$$
\boldsymbol{\Theta}=\left\{\mathcal{C}_{\dagger}^{1}, \mathcal{C}_{\dagger}^{2}, \ldots, \mathcal{C}_{\ddagger}^{n}, \ldots\right\} .
$$

Due to high random distribution of vehicles at intersections, cluster-dividing decisions will significantly affect the overall traffic efficiency. In this section, we propose an MCTS-based cluster-dividing decision-making algorithm to achieve efficient vehicle passing at intersections.

## A. Decision Tree

We first represent potential decisions of the vehicle $i$ in the cooperative area by

$$
\Omega_{i}=\left\{\begin{array}{lc}
\left\{\sigma_{m}, \sigma_{w}\right\}, & \text { if } \frac{d_{s, i}}{v_{e}} \geq T_{\text {ref }, \dagger}^{\mathrm{LBIO}} \\
\left\{\sigma_{m}\right\}, & \text { otherwise }
\end{array}\right.
$$

where $\sigma_{w}$ and $\sigma_{m}$, respectively, denote waiting and moving decisions. $v_{e}$ is desired velocity and $T_{\text {ref }, \dagger}^{\text {LBIO }}$ is the reference time cost of previous cluster. $d_{s, i}$ is the distance to the intersection, which is calculated by

$$
d_{s . i}=d_{m, i}-d_{e}-\frac{1}{2} w
$$

where $d_{m, i}$ is the Manhattan distance from the vehicle position $\left(X_{i}, Y_{i}\right)$ and the center point of the intersection, $d_{e}$ represents the distance from the start position to the center point of the intersection, and $w$ is the lane width.

A tree model is built to describe all possible clusterdividing decisions for a given traffic flow. The tree structure generally consists of $n$ levels. For $e \in\{1, \ldots, n\}$, the $e$ th level denotes all possible vehicle indexes of the $e$ th cluster for passing the intersection. A tree node in the $e$ th level can be written as

$$
s_{p_{1} \cdots p_{e}}^{e}=\left\{\Omega_{i}: i \in \mathcal{C}_{\dagger}^{e}\right\}, \quad \Omega_{i} \in\left\{\sigma_{m}, \sigma_{w}\right\}
$$

where $p_{1} \ldots p_{e}$ represents the decisions from the root node to the current mode. Based on (27), a decision sequence under the tree depth $n$ is indicated as

$$
S=\left\{s_{p_{1}}^{1}, s_{p_{1} p_{2}}^{2}, \ldots, s_{p_{1} \cdots p_{n}}^{n}\right\} .
$$

Fig. 9 shows the construction process of the tree structure where the root node $s_{1}^{1}$ is the initial node. Take the nodes $s_{11}^{2}$, $s_{12}^{2}$ and $s_{13}^{2}$ of the second level for example, the corresponding decisions of the blue vehicles can be written as

$$
\begin{aligned}
& s_{11}^{2}=\left\{\Omega_{5} \leftarrow \sigma_{m}, \Omega_{6} \leftarrow \sigma_{m}, \Omega_{7} \leftarrow \sigma_{m}, \Omega_{8} \leftarrow \sigma_{m}\right\} \\
& s_{12}^{2}=\left\{\Omega_{5} \leftarrow \sigma_{m}, \Omega_{6} \leftarrow \sigma_{m}, \Omega_{7} \leftarrow \sigma_{m}, \Omega_{8} \leftarrow \sigma_{w}\right\} \\
& s_{13}^{2}=\left\{\Omega_{5} \leftarrow \sigma_{m}, \Omega_{6} \leftarrow \sigma_{m}, \Omega_{7} \leftarrow \sigma_{w}, \Omega_{8} \leftarrow \sigma_{w}\right\} .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-08.jpg?height=629&width=801&top_left_y=185&top_left_x=204)
Fig. 9. Decision tree structure.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-08.jpg?height=320&width=797&top_left_y=922&top_left_x=208)
Fig. 10. Cluster-dividing decision-making process.

Similarly, the nodes $s_{111}^{3}, s_{121}^{3}$, and $s_{123}^{3}$ of the third level are one of the child nodes of $s_{11}^{2}, s_{121}^{2}$, and $s_{13}^{2}$, respectively, that indicate the vehicles in the cluster with the decision of $\sigma_{m}$.

Fig. 10 illustrates the transform from a decision sequence $S=\left\{s_{1}^{1}, s_{13}^{2}, s_{131}^{3}\right\}$ to a cluster-dividing result $\boldsymbol{\Theta}$. In particular, starting from the root node $s_{1}^{1}$, the decision action of vehicles \#7 and \#8 at node $s_{12}^{2}$ in the second layer is waiting, hence they are moved to the next node $s_{13}^{3}$ for further judgment. By analogy, the decision sequence composed of three nodes can divide the vehicle flow into clusters. With the increase of vehicles, all possible cluster-dividing decisions in the traffic scenario can be represented by a decision tree.

## B. Decision-Making Algorithm

Due to the dynamic nature of traffic flow, we adapt the MCTS algorithm with customized rules to search the optimal sequence in the defined decision tree. The MCTS algorithm mainly consists of four stages: 1) selection; 2) expansion; 3) simulation; and 4) backpropagation. In the following, we describe the search process in detail and simply depict the current tree node as $s$.

The selection step is to search for an optimal node among the explored nodes for iterations. The upper confidence bounds (UCBs) function is used to measure the average reward and exploration times of nodes to select the optimal child nodes, that can be expressed as

$$
U C B_{s}=\bar{V}_{s}+c \sqrt{\frac{2 \ln N_{m}}{N_{s}}}
$$

```
Algorithm 2: Cluster-Dividing Decision-Making
Input: \(\boldsymbol{\Theta}^{0},\left\{I_{*}\right\}_{* \in\{S, N, E, W\}}, \boldsymbol{\xi}_{t}, Z_{m}, \boldsymbol{T}_{\text {ref }}^{\text {LBIO }}\)
\(\Theta \leftarrow \Theta^{0}, S \leftarrow \emptyset, z \leftarrow 0, N_{s} \leftarrow 0\)
while \(z \in\left\{0,1,2, \ldots, Z_{m}\right\}\) do
    Set the current node \(s\) as root node, \(\Omega_{s} \leftarrow \emptyset\)
    if \(s\) is the leaf node then
        if \(N_{s}>0\) then
            Search index of node \(s\) in \(\left\{i_{*}\right\}_{* \in\{S, N, E, W\}}\)
            for \(i \in\left\{i_{*}\right\}_{* \in\{S, N, E, W\}}\) do
                \(d_{s, i} \leftarrow \operatorname{DisToIns}\left(X_{i}, Y_{i}, d_{e}, w\right), \Omega_{i} \leftarrow \sigma_{m}\)
                if \(d_{s, i} / v_{e} \geq T_{\text {ref }, \dagger}^{L B I O} \in \boldsymbol{T}_{\text {ref }}^{L B I O}\) then
                    \(\Omega_{i} \leftarrow \sigma_{w}, \sigma_{m}\)
                end
                \(\boldsymbol{\Omega}_{s} \leftarrow \boldsymbol{\Omega}_{s} \times\left\{\Omega_{i}\right\}\)
            end
            \(s \leftarrow\) Random \(\left(\boldsymbol{\Omega}_{s}\right)\)
        end
        \(z \leftarrow z+1, S \leftarrow \operatorname{Simulation}(s), \operatorname{Backprop}(S)\)
    else
        Select the best child node \(s_{o}\), and \(s \leftarrow s_{o}\)
    end
end
Transmit \(S\) into the form of \(\Theta\)
Output: \(\Theta\)
```

where $\bar{V}_{s}$ represents the average reward, $N_{m}$ is the searching times in the tree structure. The first term of (30) encourages to obtain higher average rewards, and the second term yields to the less visited choices of node $s$. The selection step is repeated until the current node is found to be a leaf node.

The expansion step of the MCTS begins with the leaf node. If the leaf node has already been searched, the expansion step will be performed (i.e., $N_{s}>0$ ), otherwise the simulation step is performed $\left(N_{s}=0\right)$. To exhaustively enumerate possible tree nodes, we list all potential decisions for the vehicle $i$ in the next cluster with the decision $\Omega_{i}$.

The simulation step is used to produce a random decision sequence from the current node and calculate the reward based on the given policy $V_{s}$, which is written as

$$
\left(V_{s}\right)^{-1}=T_{\mathrm{ref}, \dagger}^{\mathrm{LBIO}}+\frac{d_{s, i}}{v_{e}} .
$$

The simulation step will be performed on a new leaf node generated by the expansion step.

At the backpropagation process, the reward calculated by (30) is propagated to all nodes in the random decision sequence generated by the simulation step, and the searching times of the nodes are also updated.

An MCTS-based cluster-dividing decision-making algorithm for intersection coordination is proposed in Algorithm 2 where $\left\{I_{*}\right\}_{* \in\{S, N, E, W\}}$ is the index set of vehicle numbers and $Z_{m}$ is the interation number. The for-loop from lines 2 to 20 shows a single iteration of the MCTS where lines 5 to 15 is the expansion stage. Simulation() and Backprop() denote the steps of simulation and backpropagation, respectively. DisToIns() represents the expression of (26) and Random() is

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-09.jpg?height=350&width=808&top_left_y=183&top_left_x=202)
Fig. 11. Trajectory planning in cooperative area.

used to randomly select an element from the set $\boldsymbol{\Omega}_{s}$. After several iterations, the MCTS algorithm will gradually converge to the optimal decision sequence and is denoted as

$$
S=\left\{s_{o}^{0}, s_{o}^{1}, \ldots, s_{o}^{n}\right\} .
$$

Finally, we transform (32) into the cluster-dividing result $\boldsymbol{\Theta}=\left\{\mathcal{C}_{\ddagger}^{1}, \mathcal{C}_{\ddagger}^{2}, \ldots, \mathcal{C}_{\ddagger}^{n}, \ldots\right\}$ based on the process in Fig. 10.

Remark 1: In this article, the global vehicle information around the intersection is necessary to construct the optimal cluster-dividing decision sequence, so the vehicles still need to communicate with a centralized coordinator. However, the vehicles no longer need to communicate with the centralized coordinator but with their neighboring vehicles if the clusterdividing decision is determined using the rule-based method, e.g., the vehicle arriving at an intersection in a close proximity to each other can automatically be grouped into a cluster. Thereby, the proposed method have significant potential to be applied in a distributed manner.

## V. Cooperative Area Trajectory Planning

We divide the cooperative area $\Psi$ into three regions, including lane entrance $\Upsilon_{\text {in }}$, intersection $\mathcal{I}$ and lane exit $\Upsilon_{\text {out }}$. The illustration is given in Fig. 11. To apply the trained trajectories in the region $\mathcal{I}$, a trajectory planning method needs to be developed to regulate vehicles into the cooperative area to reach the intersection in an orderly manner with the decisionmaking result. Assuming the vehicles in the region $\Upsilon_{i n}$ can track lane centerline by an MPC controller and move with a free speed in the region $\Upsilon_{\text {out }}$. In the following, we focus on the velocity planning in the region $\Upsilon_{i n}$.

## A. Vehicles in Lane Entrance

At time $t$, let $\mathcal{C}_{\dagger}^{q, t}$ represent the vehicle cluster closest to the intersection, e.g., the red cluster in Fig. 11, $\mathcal{C}_{\dagger}^{e, t}$ the vehicle cluster in the region $\mathcal{I}$, e.g., the purple cluster, and $\mathcal{C}_{\dagger}^{n}$ the vehicle cluster of all leaders, e.g., the red and blue cluster. To coordinate the vehicles in the region $\Upsilon_{i n}$, we need to obtain an allowed minimum arrival time of the leaders to the intersection, which is expressed as

$$
T_{r, i}= \begin{cases}T_{\text {ref }, \dagger, e}^{\mathrm{LBIO}}+T_{\text {ref }, \dagger, q}^{\mathrm{LBIO}}-T_{\text {ins }}, & \text { if } i \notin \mathcal{C}_{\dagger}^{q, t} \\ T_{\text {ref }, \dagger, e}^{\mathrm{LBIO}}-T_{\text {ins }}, & \text { if } i \in \mathcal{C}_{\dagger}^{q, t} \\ 0, & \text { no vehicles in } \mathcal{I}\end{cases}
$$

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-09.jpg?height=266&width=778&top_left_y=180&top_left_x=1130)
Fig. 12. Velocity coordination of leader vehicles. The subparts of (a) and (b) represent the approximated arrival time of vehicles before and after the velocity regulation respectively.

where $T_{\text {ref }, \dagger, e}^{\mathrm{LBIO}}$ and $T_{\text {ref }, \dagger, q}^{\mathrm{LBIO}}$ is time costs of the cluster $\mathcal{C}_{\dagger}^{e, t}$ and $\mathcal{C}_{\dagger}^{q, t}$, respectively. $T_{\text {ins }}(t)$ records the occupancy time of the vehicles in the region $\mathcal{I}$, which is written as

$$
T_{i n s}(t)= \begin{cases}0, & \text { if } \mathcal{C}_{\dagger}^{e, \bar{t}} \neq \mathcal{C}_{\dagger}^{e, \bar{t}-1}, \forall t>0 \\ t-\bar{t}, & \text { otherwise }\end{cases}
$$

where $\bar{t}$ denotes the time point when cluster changes in $\mathcal{I}$.
To estimate the arrival time of leaders, we first let it move with a constant speed for a period $N_{p} \tau$, and then accelerate or decelerate to the intersection at desired velocity as shown in Fig. 12(a). Thus, the arrival time is approximated by

$$
T_{a, i}=\frac{2\left(d_{s, i}-v_{i} N_{p} \tau\right)}{\left(v_{i}+v_{e}\right)}
$$

where $N_{p}$ is a given predictive horizon and $\tau$ is the sampled time. $v_{e}$ is desired velocity at the intersection, which is determined according to the actual demand.

We aim at regulating the leaders to reach the intersection quickly with the minimum time constraint $T_{r, i}$. Based on (33) and (35), the desired arrival time $T_{c, i}$ can be determined by

$$
T_{c, i}=\max \left\{T_{r, i}, \min _{i \in \mathcal{C}_{\ddagger}^{n}}\left\{T_{a, i}\right\}\right\} .
$$

Two accelerating/decelerating stages maneuver is employed to guarantee the vehicles reach the intersection at time $T_{c, i}$, as shown in Fig. 12(b). In particular, at the first stage the vehicles move from $t$ to $t+N_{p} \tau$ with a constant acceleration $a_{\text {ref }, i}$ then the acceleration at the second stage from $t+N_{p} \tau$ to $T_{c, i}$ can be derived using known constraint conditions. Based on the idea of differential calculus, with an appropriate $N_{p}$, the desired acceleration $a_{\text {ref }, i}$ of the leader $i$ can be calculated by

$$
a_{\mathrm{ref}, i}=\frac{2 d_{i n s}^{i}-2 v_{i} N_{p} \tau-T_{c, i}\left(v_{e}+v_{i}\right)}{T_{c, i} N_{p} \tau+\left(N_{p} \tau\right)^{2}} .
$$

For followers behind the leaders, to keep the safe relative distances and velocities, the desired acceleration is given as

$$
a_{\mathrm{ref}, i}=k_{d}\left(d_{r}-d_{r}^{e}\right)+k_{v} v_{r}
$$

where $d_{r}=\left|d_{s, i}-d_{s, f}\right|$ and $v_{r}=\left(v_{i}-v_{f}\right)$ characterize relative distance and velocity to the front vehicle, respectively. $k_{d}$ and $k_{v}$ denote the weight factors. $d_{r}^{e}$ is the safe distance. $d_{s, f}$ and $v_{f}$ denote the distance to intersection and velocity of the front vehicle, respectively.

For each controlled vehicle, at time $t$ we apply the reference acceleration trajectory $a_{\text {ref }, i}$ to the vehicle model and obtain a $N_{p}$-step predictive state reference vector $\xi_{\text {ref }, i}$.

TABLE II
Initial Parameters
| Symbol | Description | Values [units] |
| :--- | :--- | :--- |
| $N$ | prediction horizon | 20 [-] |
| $Z_{m}$ | iteration times | 10000 [-] |
| $Z_{l}$ | iteration times | 15 [-] |
| $a_{i, \text { min }}, a_{i, \text { max }}$ | acceleration constraints | -5, $5[\mathrm{~m} / \mathrm{s} 2]$ |
| $\delta_{i, \min }, \delta_{i, \max }$ | steering angle constraints | -18, 18 [deg] |
| $\Delta a_{i, \text { min }}, \Delta a_{i, \text { max }}$ | acceleration rate bounds | -3, 1.5 [m/s3] |
| $\Delta \delta_{i, \min }, \Delta \delta_{i, \max }$ | steering angle rate bounds | -10, 10 [deg/s] |


![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-10.jpg?height=312&width=840&top_left_y=606&top_left_x=185)
Fig. 13. Snapshots based on the proposed method.

## B. Vehicles in Intersection

When the vehicles enter into the $\mathcal{I}$, the trained collisionfree trajectory $\xi_{\text {ref }, \dagger}^{\text {lppc }}$ will be used for the reference, and the occupancy time $T_{\text {ins }}$ of each vehicle in the $\mathcal{I}$ will be recorded.

## VI. Simulations and Results

To validate the effectiveness of the proposed multivehicle cooperative method, the SUMO platform is used to model the challenging intersection scenario and surrounding vehicles. An open-source NP package, i.e., IPOPT, is used to iteratively solve the optimization algorithm for multivehicle collisionfree trajectories. The simulation is tested on hardware platform with Core i5-6200U $2.40-\mathrm{GHz}$ CPU and $7.2-\mathrm{GB}$ RAM. For most of unsignalized intersection scenarios, the proposed cluster-dividing algorithm based on MCTS can be computed in 0.2 s with our software and hardware platform. Therefore, we set the maximum cluster-dividing searching time to 0.2 s in the following experiments. We build a typical four-way single lane intersection, and the vehicles are randomly set around the intersection with the speed range of 0-15 m/s. The initial parameters are listed in Table II.

In the following, we first use four vehicles to verify the performance of the collision-free trajectories generation and cooperative planning algorithm. Second, a continuous traffic flow scenario is designed to testify the cluster-dividing decision-making algorithm and the integrated approach. The FCFS-based control algorithm is adopted for comparison to demonstrate the advantages of the proposed method.

## A. Performance Analysis of Collision-Free Trajectories Generation and Cooperative Area Trajectory Planning

Four vehicles are randomly set in the $\Upsilon_{\text {in }}$ with the conflict mode LLTR to the trajectory learning and planning algorithm.

Fig. 13 highlights some key moments of the proposed algorithm by the snapshots. The vehicles are denoted by colored rectangular blocks and the indexing number in the upper

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-10.jpg?height=316&width=827&top_left_y=180&top_left_x=1104)
Fig. 14. Vehicle velocities based on the proposed method.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-10.jpg?height=309&width=838&top_left_y=602&top_left_x=1100)
Fig. 15. Snapshots based on the FCFS-based method.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-10.jpg?height=318&width=836&top_left_y=1016&top_left_x=1100)
Fig. 16. Vehicle velocities based on the FCFS-based method.

right corner. The vehicle motion trajectories are indicated by the dotted line. As shown in Fig. 13, applying the trained trajectories, four vehicles enter the intersection at the same time, and implement cooperative movements while effectively avoiding collisions without significant speed reduction (refer to Fig. 14). The vehicles leave the intersection safely and orderly according to the desired turning intention.

Fig. 14 illustrates the velocity variation of the vehicles where the light orange area represents the occupying time in the intersection. It is observed that the vehicles enter the cooperative control area with different velocities. The trajectory planning algorithm then begins to perform, regulating the vehicles to the desired speed. When nearly reaching the intersection, i.e., about 4 s, the velocities adjustment is completed. The total occupying time in the intersection is about 2.7 s, which is highly consistent with the theoretical time of the trained collision-free trajectories. Furthermore, during the overall traveling process, the vehicles quickly pass through the intersection without waiting.

Figs. 15 and 16 show the results using the FCFS-based algorithm. It can be seen from Fig. 15 four vehicles approach the intersection at about 5.0 s, similar to Fig. 13. However, after that the vehicle \#3 in the northbound passes the intersection first since it goes straight with higher priority. Vehicles \#1, \#2 and \#4 have to wait. At about 7.2 s, vehicle \#1 starts to turn left and the right-turning vehicle \#4 also enters the intersection. The last vehicle \#2 leaves out the intersection

TABLE III
Time Cost Comparison of Scenario A
|  | Proposed method | FCFS-based method | Improved rate |
| :--- | :--- | :--- | :--- |
| Times [s] | 8.0 | 13.0 | 38.5\% |


![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-11.jpg?height=932&width=846&top_left_y=455&top_left_x=178)
Fig. 17. Snapshots based on the proposed method.

at about 10.0 s. In Fig. 16, the vehicles pass through the intersection in order strictly according to priority strategy with obvious speed reduction and even stop for waiting.

Table III summarizes the total time cost of four vehicles through the intersection of two methods. The results show that the learned collision-free trajectories using the proposed method save 38.5\% of the time cost compared to the traditional FCFS-based control method.

## B. Performance Analysis of Cluster-Dividing <br> Decision-Making and Integrated System

In this section, we validate the MCTS-based online vehicle cluster-dividing decision algorithm and the integrated system. A continuous traffic flow with density up to eight cars per lane per 200 m is randomly set on the SUMO for testing.

Figs. 17-19 show the test results of the proposed method. The seven colored shaded parts in Figs. 18 and 19 represent different seven vehicle clusters divided by the MCTS decision algorithm. Fig. 17 highlights the key moments of seven vehicle clusters by the snapshots. The corresponding crossing mode are presented as follows: OTLL ( $t=7.4 \mathrm{~s}$ ), TLOO ( $t=10.0 \mathrm{~s}$ ), TLTR $(t=12.4 \mathrm{~s})$, RTLL $(t=16.4 \mathrm{~s})$, TTTR $(t=20.6 \mathrm{~s})$, LLTR ( $t=22.8 \mathrm{~s}$ ), LOLL ( $t=26.0 \mathrm{~s}$ ).

The proposed decision algorithm considers the waiting time and speeds of all vehicles in the cooperative area from a

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-11.jpg?height=324&width=829&top_left_y=183&top_left_x=1104)
Fig. 18. Distances to intersection based on the proposed method.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-11.jpg?height=314&width=825&top_left_y=623&top_left_x=1106)
Fig. 19. Vehicle velocities based on the proposed method.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-11.jpg?height=314&width=836&top_left_y=1053&top_left_x=1100)
Fig. 20. Snapshots based on the FCFS-based method.

global perspective. As shown in Fig. 17, vehicles \#2, \#3, and \#4 at different lanes are determined as the first cluster that enters the intersection with the crossing mode OTLL. The vehicle \#1 in the southbound lane is combined with vehicle \#6 as next cluster to pass through the intersection according to the TLOO pattern since it is too far away from the first cluster. Additionally, it can be seen from Fig. 19, the algorithm deduces that vehicles \#7 and \#8 farther away at the north and west directions can accelerate to the intersection in advance and form a new cluster with vehicles \#5 and \#10 at the south and east directions. Similarly, subsequent vehicles gradually form the respective cluster under the regulation of the proposed trajectory planning algorithm. They go through the intersection in order based on the modes determined by the decision algorithm. Finally, all vehicles take about 29.6 s to pass the intersection, and the traffic efficiency is improved.

Figs. 20-22 show the results of the FCFS-based approach. It is clear from Figs. 20 and 21 that the vehicles strictly follow the priority strategy. Specifically, the vehicles in east and westbound lanes arrive at the intersection at about 7.6 s and wait to enter into the intersection until all north and southbound vehicles have passed the intersection at about 37.4 s. All vehicles completely exit the intersection at about 53 s. Fig. 22 shows that most of the vehicles will have to stop which seriously affects traffic efficiency.

Table IV lists the time cost comparison of two methods. The results indicate that the proposed integrated system is able to

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-12.jpg?height=324&width=834&top_left_y=183&top_left_x=189)
Fig. 21. Distances to intersection based on the FCFS-based method.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-12.jpg?height=316&width=825&top_left_y=612&top_left_x=193)
Fig. 22. Vehicle velocities based on the FCFS-based method.

TABLE IV
Time Cost Comparison in Scenario B
|  | Proposed method | FCFS-based method | Improved rate |
| :--- | :--- | :--- | :--- |
| Times [s] | 29.6 | 53.8 | 45\% |


reduce the passage time by 45\% compared with the traditional FCFS-based control method in the scenario.

## VII. Conclusion

In this article, a collision-free cooperative motion planning and decision-making method for CAVs is proposed at unsignalized intersections, including intersection trajectory learning, vehicle cluster-dividing decision-making, cooperative area trajectory planning. The presented approach eliminates motion conflicts between vehicles and achieves efficient and safe cooperative control for dynamic traffic flow. Based on SUMO, we validate and compare the proposed approach with the FCFS-based method. The results show that the trained collision-free trajectories enable vehicles to simultaneously and quickly pass the intersection without waiting in single conflict mode scenario, saving 38.5\% of the travel time. Furthermore, the proposed decision algorithm can obtain the optimal cluster-dividing decision sequence and save 45\% of passing time by combining with the learning-based trajectory optimization and planning algorithm in continuous traffic scenario.

In future work, we will extend the proposed approach to adapt to more complex traffic scenarios, such as multilane intersections and ramps, etc. Moreover, random uncertainties, such as pedestrians and bicycles, will be further considered.

## References

[1] M. S. Shirazi and B. T. Morris, "Looking at intersections: A survey of intersection monitoring, behavior and safety analysis of recent studies," IEEE Trans. Intell. Transp. Syst., vol. 18, no. 1, pp. 4-24, Jan. 2017.
[2] F. Ahmad, S. A. Mahmud, and F. Z. Yousaf, "Shortest processing time scheduling to reduce traffic congestion in dense urban areas," IEEE Trans. Syst. Man Cybern., Syst., vol. 47, no. 5, pp. 838-855, May 2017.
[3] L.-W. Chen and C.-C. Chang "Cooperative traffic control with green wave coordination for multiple intersections based on the Internet of Vehicles," IEEE Trans. Syst. Man Cybern., Syst., vol. 47, no. 7, pp. 1321-1335, Jul. 2017.
[4] J. Zhang et al., "CAVSim: A microscopic traffic simulator for evaluation of connected and automated vehicles," IEEE Trans. Intell. Transp. Syst., vol. 24, no. 9, pp. 10038-10054, Sep. 2023.
[5] K. Wang, Y. Wang, L. Wang, H. Du, and K. Nam, "Distributed intersection conflict resolution for multiple vehicles considering longitudinal-lateral dynamics," IEEE Trans. Veh. Technol., vol. 70, no. 5, pp. 4166-4177, May 2021.
[6] K. Dresner and P. Stone, "A multiagent approach to autonomous intersection management," J. Artif. Intell. Res., vol. 31, pp. 591-656, Aug. 2008.
[7] Y. Meng, L. Li, F. -Y. Wang, K. Li, and Z. Li, "Analysis of cooperative driving strategies for nonsignalized intersections," IEEE Trans. Veh. Technol., vol. 67, no. 4, pp. 2900-2911, Apr. 2018.
[8] Y. Bian, S. E. Li, W. Ren, J. Wang, K. Li, and H. X. Liu, "Cooperation of multiple connected vehicles at Unsignalized intersections: Distributed observation, optimization, and control," IEEE Trans. Ind. Electron., vol. 67, no. 12, pp. 10744-10754, Dec. 2020.
[9] A. I. Morales Medina, F. Creemers, E. Lefeber, and N. Van De Wouw, "Optimal access management for cooperative intersection control," IEEE Trans. Intell. Transp. Syst., vol. 21, no. 5, pp. 2114-2127, May 2020.
[10] S. A. Fayazi and A. Vahidi, "Mixed-integer linear programming for optimal scheduling of autonomous vehicle intersection crossing," IEEE Trans. Intell. Veh., vol. 3, no. 3, pp. 287-299, Sep. 2018.
[11] ZZ. Yao, H. Jiang, Y. Cheng, Y. Jiang, and B. Ran, "Integrated schedule and trajectory optimization for connected automated vehicles in a conflict zone," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 3, pp. 1841-1851, Mar. 2022.
[12] M. A. S. Kamal, J.-I. Imura, T. Hayakawa, A. Ohata, and K. Aihara, "A vehicle-intersection coordination scheme for smooth flows of traffic without using traffic lights," IEEE Trans. Intell. Transp. Syst., vol. 16, no. 3, pp. 1136-1147, Jun. 2015.
[13] Z. Deng, K. Yang, W. Shen, and Y. Shi, "Cooperative platoon formation of connected and autonomous vehicles: Toward efficient merging coordination at unsignalized intersections," IEEE Trans. Intell. Transp. Syst., vol. 24, no. 5, pp. 5625-5639, May 2023.
[14] J. Lee and B. Park, "Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment," IEEE Trans. Intell. Transp. Syst., vol. 13, no. 1, pp. 81-90, Mar. 2012.
[15] Y. Zhang, R. Hao, T. Zhang, X. Chang, Z. Xie, and Q. Zhang, "A trajectory optimization-based intersection coordination framework for cooperative autonomous vehicles," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 9, pp. 14674-14688, Sep. 2022.
[16] M. D. Vaio, P. Falcone, R. Hult, A. Petrillo, A. Salvi, and S. Santini, "Design and experimental validation of a distributed interaction protocol for connected autonomous vehicles at a road intersection," IEEE Trans. Veh. Technol., vol. 68, no. 10, pp. 9451-9465, Oct. 2019.
[17] R. Hult, M. Zanon, S. Gros, and P. Falcone, "Optimal coordination of automated vehicles at intersections: Theory and experiments," IEEE Trans. Control Syst. Technol., vol. 27, no. 6, pp. 2510-2525, Nov. 2019.
[18] B. Xu et al., "Distributed conflict-free cooperation for multiple connected vehicles at unsignalized intersections," Transp. Res. Part C, Emerg. Technol., vol. 93, pp. 322-334, Aug. 2018.
[19] A. Zhou et al., "Cooperative signal-free intersection control using virtual platooning and traffic flow regulation," Transp. Res. Part C, Emerg. Technol., vol. 138, Art. no. 103610, May 2022.
[20] Y. Guan et al., "Integrated decision and control: Toward interpretable and computationally efficient driving intelligence," IEEE Trans. Cybern., vol. 53, no. 2, pp. 859-873, Feb. 2023.
[21] H. Shu, T. Liu, X. Mu, and D. Cao, "Driving tasks transfer using deep reinforcement learning for decision-making of autonomous vehicles in unsignalized intersection," IEEE Trans. Veh. Technol., vol. 71, no. 1, pp. 41-52, Jan. 2022.
[22] S. Yan, T. Welschehold, D. Büscher, and W. Burgard, "Courteous behavior of automated vehicles at unsignalized intersections via reinforcement learning," IEEE Robot. Autom. Lett., vol. 7, no. 1, pp. 191-198, Jan. 2022.

[23] Y. Guan, Y. Ren, S. E. Li, Q. Sun, L. Luo, and K. Li, "Centralized cooperation for connected and automated vehicles at intersections by proximal policy optimization," IEEE Trans. Veh. Technol., vol. 69, no. 11, pp. 12597-12608, Nov. 2020.
[24] Y. Xu, H. Zhou, T. Ma, J. Zhao, B. Qian, and X. Shen, "Leveraging Multiagent learning for automated vehicles scheduling at nonsignalized intersections," IEEE Internet Things J., vol. 8, no. 14, pp. 11427-11439, Jul. 2021.
[25] K. Esterle, P. Hart, J. Bernhard, and A. Knoll, "Spatiotemporal motion planning with combinatorial reasoning for autonomous driving," in Proc. 21st Int. Conf. Intell. Transp. Syst. (ITSC), 2018, pp. 1053-1060.
[26] P. F. Orzechowski, C. Burger, and M. Lauer, "Decision-making for automated vehicles using a hierarchical behavior-based arbitration scheme," in Proc. IEEE Intell. Veh. Symp. (IV), 2020, pp. 767-774.
[27] M. Sefati, J. Chandiramani, K. Kreiskoether, A. Kampker, and S. Baldi, "Towards tactical behaviour planning under uncertainties for automated vehicles in urban scenarios," in Proc. IEEE Int. Conf. Intell. Transp. Syst. (ITSC), 2017, pp. 1-7.
[28] S. Brechtel, T. Gindele, and R. Dillmann, "Probabilistic decision-making under uncertainty for autonomous driving using continuous POMDPs," in Proc. 17th IEEE Int. Conf. Intell. Transp. Syst. (ITSC), 2014, pp. 392-399.
[29] C.-J. Hoel, K. Driggs-Campbell, K. Wolff, L. Laine, and M. J. Kochenderfer, "Combining planning and deep reinforcement learning in tactical decision making for autonomous driving," IEEE Trans. Intell. Veh., vol. 5, no. 2, pp. 294-305, Jun. 2020.
[30] M. Yuan, J. Shan, and K. Mi, "Deep reinforcement learning based game-theoretic decision-making for autonomous vehicles," IEEE Robot. Autom. Lett., vol. 7, no. 2, pp. 818-825, Apr. 2022.
[31] R. Bautista-Montesano, R. Galluzzi, K. Ruan, Y. Fu, and X. Di, "Autonomous navigation at unsignalized intersections: A coupled reinforcement learning and model predictive control approach," Transp. Res. Part C, Emerg. Technol., vol. 139, Art. no. 103662, Jun. 2022.
[32] K. Wang, Y. Wang, H. Du, and K. Nam, "Game-theory-inspired hierarchical distributed control strategy for cooperative intersection considering priority negotiation," IEEE Trans. Veh. Technol., vol. 70, no. 7, pp. 6438-6449, Jul. 2021.
[33] S. Jing, F. Hui, X. Zhao, J. Rios-Torres, and A. J. Khattak, "Integrated longitudinal and lateral hierarchical control of cooperative merging of connected and automated vehicles at on-ramps," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 12, pp. 24248-24262, Dec. 2022.

![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-13.jpg?height=320&width=256&top_left_y=204&top_left_x=1081)

Xinle Gong (Member, IEEE) received the B.E. degree in mechanical engineering from the Wuhan Institute of Technology, Wuhan, China, in 2014, and the Ph.D. degree in mechanical engineering from the Beijing Institute of Technology, Beijing, China, in 2020.

He is currently a Postdoctoral Researcher of Mechanical Engineering with Tsinghua University, Beijing. Since 2017, he has been a visiting Ph.D. student with the Department of Mechanical Engineering, University of California at Berkeley, Berkeley, CA, USA. His research interests include nonlinear optimal control and model predictive control and with its application to automated and connected vehicles.
![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-13.jpg?height=318&width=258&top_left_y=761&top_left_x=1079)

Bowen Wang received the B.S. degree in vehicle engineering from the Wuhan University of Technology, Wuhan, China, in 2020, and the M.S. degree in mechanical engineering from the Beijing Institute of Technology, Beijing, China, in 2023. He is currently pursuing the Ph.D. degree in mechanical engineering with Shanghai Jiao Tong University, Shanghai, China.

His current research interests include autonomous vehicle motion planning and model predictive control theory.
![](https://cdn.mathpix.com/cropped/78eb56c5-bbda-42b1-b26f-7b93e84ccd4e-13.jpg?height=318&width=256&top_left_y=1220&top_left_x=1081)

Sheng Liang received the B.S. degree in vehicle engineering and the Ph.D. degree in mechanical engineering from the Beijing Institute of Technology, Beijing, China, in 2017 and 2022, respectively.

His research interests mainly include vehicle dynamics modelling, automotive control, fourwheel independent drive electric vehicles, and multiobjective optimization for electric vehicles


[^0]:    Manuscript received 14 December 2022; revised 8 June 2023 and 1 October 2023; accepted 18 December 2023. Date of publication 18 January 2024; date of current version 17 April 2024. This work was supported by the National Natural Science Foundation of China under Grant 52102438. This article was recommended by Associate Editor M. P. Fanti. (Corresponding author: Bowen Wang.)
    Xinle Gong is with the School of Vehicle and Mobility, Tsinghua University, Beijing 10084, China (e-mail: xinlegong@gmail.com).
    Bowen Wang is with the School of Mechanical Engineering, Shanghai Jiao Tong University, Shanghai 200240, China (e-mail: 98.wangbowen@sjtu.edu.cn).
    Sheng Liang is with the Department of Mechanical Engineering, Beijing Institute of Technology, Beijing 100081, China (e-mail: liangsheng@ bit.edu.cn).
    Color versions of one or more figures in this article are available at https://doi.org/10.1109/TSMC.2023.3346275.
    Digital Object Identifier 10.1109/TSMC.2023.3346275

