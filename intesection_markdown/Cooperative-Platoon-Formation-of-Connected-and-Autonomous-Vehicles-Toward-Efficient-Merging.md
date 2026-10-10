# Cooperative Platoon Formation of Connected and Autonomous Vehicles: Toward Efficient Merging Coordination at Unsignalized Intersections 

Zhiyun Deng ${ }^{\text {(iD) }}$, Graduate Student Member, IEEE, Kaidi Yang ${ }^{\text {(iD) }}$, Weiming Shen ${ }^{\text {(iD) }}$, Fellow, IEEE, and Yanjun Shi


#### Abstract

This paper presents a Vehicle-Platoon-Aware Bi-Level Optimization Algorithm for Autonomous Intersection Management (VPA-AIM) to coordinate the merging of Connected and Automated Vehicles at unsignalized intersections. The constraint-coupled bi-level optimization is operated within a rolling horizon to balance traffic performance and computational efficiency. In each decision step, the platoon formation scheme is incorporated into an upper-level traffic scheduling model as decision variables to pursue an optimal schedule from a systemic view. Meanwhile, the passing sequence and timeslots of vehicles are jointly optimized with the platoon configuration scheme by virtue of real-time traffic states to improve operational efficiency and fairness. After that, a lower-level trajectory planning model will generate dynamically-feasible and energy-efficient trajectories according to the given schedule and coupling constraints with the objective of improving space utilization to prevent spillbacks. Moreover, the quantifiable connection between the makespan of traffic scheduling schemes and the occurrence of spillbacks is established, demonstrating that the cooperative platoon formation strategy is effective in avoiding and mitigating spillbacks in normal and saturated traffic states. Additionally, the proposed algorithm can be extended to mixed traffic scenarios. Numerical experiments are conducted on extensive scenarios with different arrival flows, where the Constraint Programming technique is employed to produce the optimal schedule. Experimental results indicate the superiority of the proposed approach in optimality and stability with reasonable sub-second computation time for real-life applications.


Index Terms-Cooperative driving, vehicle platooning, traffic scheduling, queue spillback, unsignalized intersections.

## I. Introduction

TRAFFIC intersections are the physical area where different transport flows meet and cross, resulting in natural

Manuscript received 15 September 2022; revised 31 December 2022; accepted 6 January 2023. Date of publication 18 January 2023; date of current version 8 May 2023. This work was supported in part by the National Key Research and Development Program of China under Grant 2018YFE0197700 and in part by the Fundamental Research Funds for the Central Universities of China under Grant 2021yjsCXCY048 and Grant 2021GCRC058. The work of Kaidi Yang was supported by the Singapore Ministry of Education under its Academic Research Fund Tier 1 under Grant A-8000404-01-00. The Associate Editor for this article was G. Guo. (Corresponding author: Weiming Shen.)
Zhiyun Deng and Weiming Shen are with the School of Mechanical Science and Engineering, Huazhong University of Science and Technology, Wuhan 430074, China (e-mail: dengzy@hust.edu.cn; shenwm@hust.edu.cn).

Kaidi Yang is with the Department of Civil and Environmental Engineering, National University of Singapore, Singapore 119077 (e-mail: kaidi.yang@nus.edu.sg).

Yanjun Shi is with the School of Mechanical Engineering, Dalian University of Technology, Dalian 116024, China (e-mail: syj@dlut.edu.cn).

Digital Object Identifier 10.1109/TITS.2023.3235774 bottlenecks in urban road networks. However, the present signalized intersection is far from perfect for the burgeoning number of vehicles [1]. It is observed that the switching of traffic signals constantly interrupts the traffic flow and gives rise to a frequently observed phenomenon called stop-andgo traffic [2]. Consequently, drivers may be tired, agitated, and even angry, leading to undesirable driving behaviors called road rage [3], which may further aggravate congestion. In addition, the signal-switching process is not instantaneous but requires a setup phase (i.e., the yellow light) lasting about five seconds [4], which reduces intersection throughput considerably. Furthermore, when adverse weather occurs (e.g., heavy rain, fog, snowstorms, and dust storms), it can be challenging for drivers or onboard infrared cameras to capture the signal light accurately [5].

Fortunately, Connected and Automated Vehicles (CAVs) that combine wireless communication and autonomous driving hold the potential to revolutionize intelligent transportation systems [6], [7], [8], offering advantages for accident avoidance [9], mobility improvement [10], and emission reduction [11]. The benefits of CAVs on intersection control are mainly two-fold. On the one hand, CAVs enable the joint optimization between passing sequences and motion trajectories at autonomous traffic intersections [12], [13], [14], [15]. In other words, vehicles will run with the pre-determined trajectories within assigned timeslots to improve traffic efficiency by avoiding unnecessary speed up/down operations and stops. Therefore, it is expected that physical traffic signals will no longer be necessary for future traffic management [16], since the Vehicle-to-Everything (V2X) technique enables virtual traffic lights [17] that reside at each vehicle to reduce the difficulty of signal detection. On the other hand, CAVs enable the application of vehicle platooning [18], [19], [20], [21], [22], which can further increase road storage by reducing inter-vehicular headway considerably [23], [24], [25], [26] and improve energy efficiency by mitigating aerodynamic drag and unnecessary speed fluctuations [27]. Hence, researchers try to facilitate the advantages of vehicle platooning to enhance traffic mobility at autonomous intersections, which raises a critical research question of how to determine the optimal platoon formation scheme for vehicles to optimize important objective indicators subject to relevant constraints.

Despite extensive existing works on jointly optimizing vehicle trajectories and passing sequence [12], [13], [14], [15],
the problem of platoon configuration has not been adequately addressed due to the complexity of the requirement for a global decision-maker. For example, most of the existing research assumes that platoons have been formed before vehicles enter the control zone [14], [28], [29], whereas other works group vehicles into platoons by virtue of empirical rules from the individual point of view [13], [30], [31], without cooperation with vehicles on other lanes. Hence, this paper aims to address these gaps in cooperative platoon formation to explore the potential of platoon-aware traffic management.

Compared to existing studies, the contributions of this paper are threefold. First, this work incorporates the platoon formation scheme as decision variables into the joint optimization of vehicle trajectories and intersection controllers, intending to pursue the global-optimal schedule, significantly improving operational efficiency and fairness compared with the state-of-the-art algorithms. In other words, the decision to merge vehicles into platoons is based on real-time traffic states to achieve one-dimensional cooperation on the same lane and two-dimensional cooperation with vehicles on another lane. Second, this work presents an effective traffic coordination algorithm to avoid/mitigate spillbacks in normal/saturated traffic states, where the quantifiable connection between the makespan of traffic scheduling schemes and the occurrence of spillbacks is established. Additionally, the proposed algorithm can be extended to mixed traffic scenarios with various penetration rates of CAVs based on the assumptions that Human Driven Vehicles (HDVs) have bounded tracking errors and CAVs serve as platoon leaders. Third, it is able to produce provable optimal traffic scheduling schemes with high computational efficiency and stability for real-life applications using the Constraint Programming (CP) technique, whose computation time remains at a sub-second level even for high-flow traffic states in most scenarios tested.

The remainder of this paper is organized as follows: Section II discusses related works on Autonomous Intersection Management (AIM). Section III presents definitions of the cooperative merging problem, followed by a detailed description of the proposed bi-level optimization method in Section IV. Numerical simulation experiments are conducted in Section V along with performance comparison with other existing methods. Section VI concludes this paper and discusses some open issues and future work.

## II. Related Work

Since Dresner and Stone presented the concept of AIM [32], numerous strategies have been proposed to improve traffic efficiency at autonomous intersections without signal controllers. It is clear that the overall performance of the system is susceptible to the underlying control strategy [33], [34], which can be categorized into three groups, i.e., the Priority-based AIM (PR-AIM), Optimization-based AIM (OP-AIM), and Heuristic-based AIM (HR-AIM). The FirstIn-First-Out (FIFO) policy [35] is a classical priority-based method, while the FIFO-based reservation system has been proved to outperform the signal controller in terms of delay under certain circumstances [36], [37]. In that case, the priority of $n$ vehicles will be determined by a centralized controller according to their arrival times, which effectively reduces the computational complexity from $\mathcal{O}(n!)$ to $\mathcal{O}(n)$. Hence, feasible solutions can be generated in real-time, while the performance of solutions cannot be guaranteed since it sets fairness as the fixed goal [38].

In order to obtain the optimal solution, a variety of OP-AIM methods are proposed by researchers, who translate the traffic scheduling problem into a mathematical programming problem and employ optimization-based methods to generate high-performance solutions in terms of delay [39], throughput [40], energy consumption [41], quality of experience [42], and communication overhead [28]. Besides, constraints regarding first-order dynamics limits and inter-vehicle separation distance are well-designed in [40] to ensure safety. Among OP-AIM methods, Mixed-Integer Linear Programming (MILP) models are widely adopted by existing literature to describe the discrete and continuous aspects of the system. For example, passing sequences of vehicles can be formulated by discrete variables, while their states (e.g., location, velocity, and acceleration) must be continuous. Besides, to generate dynamically feasible trajectories, Lu et al. [43] directly set instantaneous speeds of vehicles as time-varying decision variables, considering $n \times N$ variables in total, where $n$ and $M$ represent the number of vehicles and time steps, respectively. By contrast, several hierarchical frameworks are developed in [13], [14], [15], [44], [45], [46]. For example, Guo et al. [13] propose a framework of dynamic programming with shooting heuristic as a subroutine (DP-SH) to find the near-optimal solution for the integrated trajectory optimization and intersection control problem. Note that such two-step approaches have smaller search space than the former since they decoupled the optimization of vehicles' crossing timeslots and trajectories. Although these programming models can be solved with off-the-shelf software packages, obtaining solutions for large-scale problems is still time-consuming [29], which limits its application to dynamic traffic conditions.

Besides, HR-AIM methods use some heuristic rules to group vehicles into platoons, which accelerates the process of finding a satisfactory solution [23], [25]. Such a strategy can reduce model complexity since the centralized controller only needs to deal with platoon leaders, while the computation and communication load can be released [47]. For example, Miculescu et al. [48] proposed a polling-based method to schedule passing sequences of vehicles, where natural platooning behaviors emerge and help to save switching time. Besides, the authors compared different polling policies (i.e., exhaustive, gated, and k-limited policies) in the MATLAB-based simulations. Tallapragada et al. [49] adopted the k-means algorithm to form clusters based on vehicle positions, while the maximum number of clusters is pre-defined to reduce the computational burden. Ge et al. [50] developed a centralized coordination scheme based on MILP and used graph theory to decompose the original vehicle swarm into small batches after determining the relative priority and speed of vehicles. However, these platoon formation strategies are derived from previous experiences without being optimal, perfect,
or rational since they make decisions from the local point of view without considering the global traffic information.

Although different studies use different control strategies, most incorporate the rolling horizon procedure into their method. Therefore, the long-term optimization can be decomposed into a series of subproblems with a shorter planning horizon, which helps to reduce computational complexity. Admittedly, a longer horizon can enable these subproblems to better approximate the long-term optimization problem, thus improving the optimization performance. However, the prediction of dynamic traffic flow is only reliable over a limited horizon. Moreover, a long horizon may increase the scale of the subproblems, making it computationally challenging to solve them. Hence, the horizon length should be carefully selected to balance optimality and computation efficiency. Accordingly, Levin et al. [51] presented a rolling-horizon algorithm to extend the MILP model to larger numbers of vehicles, which takes 5-10 seconds to schedule up to 40 vehicles within a 15-second planning horizon. Mirheli et al. [52] established a mixed-integer non-linear programming model to determine optimal conflict-free reservations in an isolated intersection, which takes more than 10 seconds to schedule 70 vehicles within a 15 -second planning horizon. Yao et al. [45] proposed a 0-1 MILP model for vehicles entering scheduling, which takes less than one second to find the optimal scheduling scheme for up to 12 vehicles within a 10 -second planning horizon. Ge et al. [50] take about three seconds to schedule 40 vehicles within a 15 -second planning horizon. To the best of our knowledge, most existing research cannot solve large-scale AIM problems in real-time (e.g., at the sub-second resolution, which is crucial to reduce tracking errors and ensure vehicles follow the planned trajectories [53]). Hence, it motivates us to develop an efficient traffic scheduling method to pursue the optimal solution in a short time even for high-flow traffic states by integrating the advantages of OP-AIM and HR-AIM.

## III. Problem Definition

In this paper, we focus on the cooperative merging problem through a fully autonomous traffic intersection without signal controllers as shown in Fig. 1. It is assumed that all the vehicles are CAVs equipped with wireless communicators (e.g., Dedicated Short Range Communication (DSRC) and cellular devices) to support vehicular communications [54], [55], [56], while their kinematic states (e.g., position, speed, and acceleration) can be precisely estimated by Kalman filters through fusing GPS, camera, and IMU as illustrated in [57], [58], and [59]. This simple scenario consisting of two one-way traffic streams is defined as a standard test scenario by [12], [44], [45], [48], [60], and [61]. It is chosen to gain insights into the benefits of platoon-aware traffic scheduling for automated traffic operations, which serves as a building block for subsequent studies. Besides, we assume that Base Stations (BSs) and Road Side Units (RSUs) are responsible for providing cellular- and DSRC-based V2X networks outside and within the control region, respectively. Thus, the kinematic states of vehicles can be captured by the decision-maker via the cellular network before they enter the control zone [62], such that their

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-03.jpg?height=412&width=857&top_left_y=198&top_left_x=1094)
Fig. 1. Illustration of the cooperative merging problem at a fully autonomous traffic intersection without signal controllers.

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-03.jpg?height=249&width=862&top_left_y=724&top_left_x=1089)
Fig. 2. Illustration of time parameters within the intersection area.

arrival time can be predicted ahead of time. After that, the RSU, which serves as a centralized controller, can control the motion of vehicles via wireless communication.

Given the planning horizon $t \in\left[T_{0}, T_{0}+\Delta T\right]$, we assume that there are $n_{k}$ vehicles existing on the road $k \in \mathcal{K}=\{0,1\}$, which can be denoted by $V_{k, i}$ and indexed by $i \in \mathcal{I}=$ $\left\{1,2, \cdots, n_{k}\right\}$ according to their sequence of arrival. Besides, the overlapped region of two roads is called the merging zone and has a width of $W$, while the portion of the road segment within a distance of $L$ to the merging zone is called the control zone. It is assumed that vehicles are required to form $m_{k}$ platoons within the control zone $\left(m_{k} \leq n_{k}\right)$, which can be denoted by $P_{k, i}$ and indexed by $j \in \mathcal{J}=\left\{1,2, \cdots, m_{k}\right\}$. Without loss of generality, each vehicle is represented by a two-dimensional and rectangular rigid body with length $l$ and width $w$. Besides, suppose each vehicle is subject to second-order dynamics of the following form:

$$
\ddot{s}_{k, i}^{t}=a_{k, i}^{t}, \quad \forall k, i,
$$

where $s_{k, i}^{t}$ denotes the displacement of the vehicle's front bumper between the entrance of the control zone and current position, $\dot{s}_{k, i}^{t}$ the velocity, and $a_{k, i}^{t}$ the acceleration.

During the time when each vehicle passes through the control zone and merging zone, there are three special moments as shown in Fig. 2. In detail, (1) the arrival time $t_{k, i}^{+}$is the moment when its front bumper enters the control zone where $s_{k, i}^{t}=0$; (2) the start time $t_{k, i}^{*}$ is the moment when its front bumper enters the merging zone (i.e., crosses the stop line) where $s_{k, i}^{t}=L$; and (3) the departure time $t_{k, i}^{-}$ is the moment when its rear bumper leaves the merging zone where $s_{k, i}^{t}=L+W+l$. It is obvious that $t_{k, i}^{-}>t_{k, i}^{+}$for all vehicles. After that, we define the interval of these three moments as the (1) waiting time $t_{k, i}^{+, *}=t_{k, i}^{*}-t_{k, i}^{+}$, (2) operation time $t_{k, i}^{*,-}=t_{k, i}^{-}-t_{k, i}^{*}$, and (3) travel time $t_{k, i}^{+,-}=t_{k, i}^{-}-t_{k, i}^{+}$, respectively. With these notations in hand, we define safety as follows.

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-04.jpg?height=176&width=859&top_left_y=202&top_left_x=176)
Fig. 3. Illustration of the sequence-dependent switching time.

Definition 1 (Safety): The control zone is said to be safe at time $t$, if each vehicle maintains a sufficient separation with its preceding vehicle, i.e., $s_{k, i-1}^{t}-s_{k, i}^{t}>l$ for all $k \in \mathcal{K}=\{0,1\}$ when $i>1$. Besides, the merging zone is said to be safe, if there are no pairwise collisions among vehicles, i.e., $\left[t_{k, i}^{*}, t_{k, i}^{-}\right] \cap\left[t_{k, i-1}^{*}, t_{k, i-1}^{-}\right]=\varnothing$ and $\left[t_{k, i}^{*}, t_{k, i}^{-}\right] \cap\left[t_{1-k, i^{\prime}}^{*}, t_{1-k, i^{\prime}}^{-}\right]=\varnothing$ for all $k \in \mathcal{K}$ and $i, i^{\prime} \in$ $\mathcal{I}=\left\{1,2, \cdots, n_{k}\right\}$.

From a practical point of view, there should be an extra separation between vehicles when they enter the merging zone in case of communication latency and control error. Hence, we define the switching time on the occupation timeline of the merging zone as shown in Fig. 3, which should be greater than a minimum threshold value for security.

Definition 2 (Switching Time): In the merging zone, the switching time between vehicles coming from the same road is defined as $t_{k, i}^{*}-t_{k, i-1}^{*}$ for all $k \in\{0,1\}$ and $i>1$. The calculation of switching time is the same as the time-headway of vehicle $i$ and $i-1$ at the stop line when $s_{k, i}^{t}=s_{k, i-1}^{t}=L$. In addition, the switching time between vehicles coming from different directions can be calculated by $\left|t_{k, i}^{*}-t_{1-k, i^{\prime}}^{*}\right|$ for all $k \in\{0,1\}$ and $i, i^{\prime} \in\left\{1,2, \cdots, n_{k}\right\}$.

In this paper, we formulate the assumption of sequence-dependent switching time $t_{k, i}^{k^{\prime}, i^{\prime}}$ as follows since the vehicle platooning technique helps to reduce inter-vehicular distances considerably [25].

Assumption 1 (Sequence-Dependent Minimum Switching Time): We assume that the minimum switching time $t_{k, i}^{k^{\prime}, i^{\prime}}$ of vehicles in the merging zone is varied with each pair of individuals, which can be calculated by

$$
t_{k, i}^{k^{\prime}, i^{\prime}}=\left\{\begin{array}{ll}
\tau, & , \text { if } k^{\prime}=k \text { and same platoon, } \\
\sigma_{1} \tau, & k^{\prime}=k, \\
\sigma_{2} \tau, & \text { else if } k^{\prime} \neq k
\end{array} \quad \forall k, k^{\prime}, i, i^{\prime} .\right.
$$

where $\tau$ denotes the minimum time-headway of vehicles in the same platoon on the same road, $\sigma_{1}$ the factor of safety when vehicles are assigned into different platoons on the same road, and $\sigma_{2}$ the factor of safety when vehicles come from different roads $\left(\sigma_{2}>\sigma_{1}>1\right)$.

Given the departure velocity $v^{-}$, the delay of an individual vehicle can be calculated by the difference between its actual departure time $t_{k, i}^{-}$and virtual departure time, i.e., $\left(t_{k, i}^{+}+\right.$ $\left.\frac{L+W+l}{v^{-}}\right)$. In detail, the latter one is the time in ideal driving scenarios where the vehicle travels through the control and merging zone under free-flow ${ }^{1}$ conditions.

[^0]![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-04.jpg?height=249&width=866&top_left_y=200&top_left_x=1085)
Fig. 4. Illustration of the occurrence of spillbacks.

Definition 3 (Delay): The delay of vehicle is defined as

$$
t_{i, k}^{D}=\max \left\{0, t_{k, i}^{-}-\left(t_{k, i}^{+}+\frac{L+W+l}{v^{-}}\right)\right\} .
$$

Note that the maximum delay among vehicles reflects the fairness of the traffic scheduling scheme. In other words, the smaller the maximum delay, the smaller the variance of travel times, and the better the traffic scheduling scheme in terms of fairness.

Next, we define the makespan of a given traffic scheduling scheme as the departure time of the last vehicle within the current horizon. It is the period of time that the scheduling scheme took to let all the vehicles pass through the intersection area, reflecting the operational efficiency of the underlying control policy.

Definition 4 (Makespan): Given a set of vehicles denoted by $V_{k, i}$ where $k \in \mathcal{K}=\{0,1\}$ and $i \in\left\{1,2, \cdots, n_{k}\right\}$, the makespan of a traffic scheduling scheme is defined as

$$
C_{\max }=\max _{k \in \mathcal{K}} t_{k, n_{k}}^{-}=\max _{k \in \mathcal{K}}\left\{t_{k, n_{k}}^{*}+\frac{W+l}{v^{-}}\right\} .
$$

As illustrated in Fig. 4, the traffic spillback refers to the situation when the back of the queue propagates to the previous intersection, leading to extended blockages and queue overflowing buffers. It is evident that spillbacks occur because vehicles cannot pass through the merging zone on schedule, e.g., due to the sudden increase in traffic volume or inefficient traffic management methods.

In this paper, we show that the makespan is a helpful indicator to predict the time when spillbacks occur. To demonstrate this, we first establish a condition in Lemma 1 such that the violation of this condition will cause queue to constantly grow, and hence spillback will eventually happen. Based on this condition, we then calculate in Property 1 the estimated number of rolling horizon cycles without the occurrence of spillbacks.

Lemma 1: For a given planning horizon $t \in\left[T_{0}, T_{0}+\Delta T\right]$, let us assume that $T_{\text {min }}$ is the minimum time interval between a vehicle's arrival and start time in each horizon, the value of which is affected by the trajectory planning algorithm. Let $C_{\text {max }}$ be the makespan of the current traffic scheduling scheme. Then, the queue will not be carried over from the current horizon to the next one if

$$
C_{\max } \leq \Delta T+T_{\min } .
$$

Proof: Let us consider two adjacent planning horizons, i.e., $\left[T_{0}, T_{0}+\Delta T\right]$ and $\left[T_{0}+\Delta T, T_{0}+2 \Delta T\right]$. The ideal earliest moment when the front bumper of the first vehicle in the next horizon enters the merging zone can be denoted by $T_{0}+\Delta T+T_{\text {min }}$, the value of which is determined by the

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-05.jpg?height=247&width=868&top_left_y=202&top_left_x=172)
Fig. 5. Schematic diagram for calculating the number of rolling horizon cycles without the occurrence of spillbacks.

trajectory planning algorithm without considering the collision avoidance constraint. In addition, the moment when the rear bumper of the last vehicle in the previous horizon leaves the merging zone can be denoted by $T_{0}+C_{\text {max }}$. This is the actual earliest available time for vehicles in the next horizon to enter the merging zone that ensures safety.

It is obvious that if the actual earliest available moment (which is affected by vehicles in the previous horizon) is less than the ideal one, the queue will not be carried over from the previous horizon to the current one. Therefore, we have

$$
T_{0}+C_{\max } \leq T_{0}+\Delta T+T_{\min } .
$$

This completes the proof. $\square$

In this paper, we try to avoid spillbacks in normal traffic states where traffic can be effectively managed by minimizing the makespan of optimized traffic scheduling schemes and preventing delay propagation. Moreover, we try to mitigate spillbacks (i.e., postpone the occurrence of spillbacks) in saturated traffic states. To this end, we provide an upper bound for the number of rolling horizon cycles without the occurrence of spillbacks to calculate the maximum duration for which it can disperse traffic without causing a spillback.

Property 1 (Number of Rolling Horizon Cycles Without the Occurrence of Spillbacks): Suppose $L^{*}$ denotes the remaining road storage space, which is determined by the number of vehicles that arrived in advance but still exist on the road, i.e., $L^{*}=L-L^{\prime}$, where $L^{\prime}$ denotes the length of queue. Let $d$ be the minimum inter-vehicle distance and $h$ be vehicles' arrival intensity in seconds per vehicle (s/veh), which denotes the average headway. Then, in scenarios where the arrival flow is slowly changing, a spillback is expected to occur after $N$ cycles of rolling horizons, where

$$
N=\left[\frac{\frac{L^{*}}{l+d} \cdot h-T_{\min }}{C_{\max }-\Delta T-T_{\min }}\right] .
$$

Recall that $L$ and $l$ denote the length of the road and vehicles, $\Delta T$ the length of the planning horizon, $T_{\text {min }}$ the minimum travel time of vehicles, $C_{\text {max }}$ the makespan of the traffic scheduling scheme in the current horizon. According to Lemma 1, it is clear that the queue will not be carried over from the current horizon to the next one if $C_{\text {max }} \leq \Delta T+T_{\text {min }}$. On the contrary, the queue will be carried over to the next horizon if $C_{\text {max }}>\Delta T+T_{\text {min }}$ as shown in Fig. 5, which may cause delays propagating backward and accumulating, eventually leading to congestion and spillbacks. Note that spillbacks are expected to occur when the number of queued vehicles exceeds the maximum road storage (i.e., $\frac{L}{l+d}$ ). Then, the time when the road storage reaches its limit can be

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-05.jpg?height=576&width=812&top_left_y=200&top_left_x=1113)
Fig. 6. Framework of the proposed bi-bevel optimization model.

estimated by $\frac{L h}{l+d}$. Note that the derivation of Eq.(4) relies on a point queue model to calculate an upper bound for the duration for which it can disperse traffic without causing a spillback.

## IV. Vehicle-Platoon-Aware Bi-Level Optimization for Autonomous Intersection Management

## A. Method Framework

In this section, we propose a bilevel optimization algorithm, named VPA-AIM, which assigns vehicles to platoons to get through the unsignalized intersection cooperatively. Efficient coordination is achieved by solving two coupled optimization models. In detail, the upper-level task is referred to as platoon-aware traffic scheduling, which determines the optimal platoon formation scheme of vehicles during the control zone and allocates the sequence and timeslots of platoons passing through the merging zone. The lower-level task is referred to as multi-vehicle trajectory optimization, which designs referenced trajectories for multiple vehicles during the process of vehicles merging into platoons and passing through the control and merging zones. The two models are connected to each other via several coupling constraints, which ensures that the decisions generated by the upper-level traffic scheduling model are feasible for the lower-level trajectory planning model. The workflow of the VPA-AIM algorithm is presented in Fig. 6.

This paper proposes a rolling horizon procedure to deal with this online optimization problem since the prediction of dynamic traffic flows is reliable only over a limited horizon. This procedure decomposes the long-term optimization into a series of subproblems with a shorter time horizon, such that the computation time can be reduced. According to this method, a vehicle scheduling scheme is first determined up to a given point in time, ignoring everything that could happen afterward. After that, the planning interval is iteratively moved forward in time to generate the following schedule and so on.

In each decision step, the traffic scheduling scheme of vehicles (i.e., their departure time, which includes information about the platoon formation scheme) is optimized in the upper-level model to minimize the makespan and the maximum delay. Besides, referenced trajectories of vehicles are designed and optimized in the lower-level model according
to the pre-determined arrival and departure time to reduce the overall energy consumption of vehicles and improve space utilization to prevent spillbacks within the intersection area.

## B. Upper-Level Traffic Scheduling Model

1) Decision Variables: Recall that there are $n_{k}$ vehicles existing on the road $k \in \mathcal{K}=\{0,1\}$, which are indexed by $i \in$ $\mathcal{I}=\left\{1,2, \cdots, n_{k}\right\}$. These vehicles are required to be assigned into $m_{k}$ platoons indexed by $j \in\left\{1,2, \cdots, m_{k}\right\}\left(m_{k} \leq n_{k}\right)$. Therefore, we define the decision variables as the start time of vehicles, i.e., $\boldsymbol{t}^{*}=\left\{t_{k, i}^{*}\right\}_{k \in \mathcal{K}, i \in \mathcal{I}}$.

Besides, we characterize platoon formation using a dummy binary variable $x_{i}^{k}$ that represents whether vehicle $V_{k, i}$ is the leading vehicle of a platoon. In other words, we have

$$
x_{i}^{k}=\left\{\begin{array}{ll}
1, & \text { if } V_{k, i} \text { is a platoon leader, } \\
0, & \text { if } V_{k, i} \text { is a platoon follower. }
\end{array} \quad \forall k, i,\right.
$$

which can be expressed as a $n_{k}$-dimensional vector $\vec{x}^{k}$ for all $i \in \mathcal{I}$. For example, suppose there are five vehicles indexed by $\{1,2,3,4,5\}$ on the road $k$ and they are assigned into three groups, i.e., $\{1,2\},\{3\},\{4,5\}$. In this case, $V_{k, 1}, V_{k, 3}$, and $V_{k, 4}$ serve as platoon leaders, while $V_{k, 2}$ and $V_{k, 5}$ serve as platoon followers. Therefore, we have $\vec{x}^{k}=[1,0,1,1,0]$.

To describe the formation scheme directly, we take $y_{k}$ as an intermediate variable to denote the number of vehicles that have been assigned to each platoon on the road $k$, i.e.,

$$
\begin{aligned}
\vec{y}^{k} & =\left\{y_{j}^{k} \mid j=1,2, \cdots, m_{k}\right\} \\
\sum_{j=1}^{m_{k}} y_{j}^{k} & =n_{k}, \quad \forall k
\end{aligned}
$$

which can be inferred according to the value of $x_{i}^{k}$. For example, suppose there are five vehicles $\left(n_{k}=5\right)$ on the road $k$ indexed by $\{1,2,3,4,5\}$ and they are assigned into three groups $\left(m_{k}=3\right)$, i.e., $\{1,2\},\{3\},\{4,5\}$. In this case, $V_{k, 1}$ and $V_{k, 2}$ are assigned into the first platoon, $V_{k, 3}$ the second, $V_{k, 4}$ and $V_{k, 5}$ the third. In other words, there are two, one, and two vehicles in each platoon, respectively. Therefore, we have $\vec{y}^{k}=\{2,1,2\}$.

In addition, we take $z_{i, i^{\prime}}$ as another intermediate variable to denote the passing sequence of vehicles through the merging zone, i.e.,

$$
z_{i, i^{\prime}}=\left\{\begin{array}{ll}
0, & t_{k, i}^{*} \leq t_{1-k, i^{\prime}}^{*} \\
1, & t_{k, i}^{*}>t_{1-k, i^{\prime}}^{*},
\end{array} \quad \forall k, i, i^{\prime} .\right.
$$

For example, suppose the passing sequence of vehicles is $\left\{V_{1}^{1}, V_{1}^{0}, V_{2}^{1}\right\}$ and $t_{1,1}^{*}<t_{0,1}^{*}<t_{1,2}^{*}$, then it can be inferred that $z_{1,1}=1$ and $z_{1,2}=0$ since $t_{0,1}^{*}>t_{1,1}^{*}$ and $t_{0,1}^{*}<t_{1,2}^{*}$, respectively.
2) Constraints: Similar to [15], [33], [61], and [63], we assume overtaking is not allowed in the control zone. Hence, the passing sequence of vehicles through the merging zone on the same road should correspond to the order of arrival at the control zone. In addition, there should be an extra separation between vehicles when they enter the merging zone to avoid rear-end collisions, which is referred to as the switching time $t_{k, i}^{k^{\prime}, i^{\prime}}$ as described in Definition 2 and Assumption 1. Therefore, we have the following precedence constraints in the form of chains for vehicles on the same road:

$$
t_{k, i}^{*}-t_{k, i+1}^{*}-t_{k, i}^{k, i+1} \geq 0, \quad \forall k, i<n_{k} .
$$

To avoid side-impact collisions in the merging zone, the start time of two vehicles coming from different roads should also maintain a separation. Therefore, we have

$$
\begin{aligned}
z_{i, i^{\prime}} \times\left(t_{k, i}^{*}-t_{1-k, i^{\prime}}^{*}-t_{k, i}^{1-k, i^{\prime}}\right) & \geq 0, \quad \forall k=0, i, i^{\prime} \\
\left(1-z_{i, i^{\prime}}\right) \times\left(t_{1-k, i^{\prime}}^{*}-t_{k, i}^{*}-t_{k, i}^{1-k, i^{\prime}}\right) & \geq 0, \quad \forall k=0, i, i^{\prime}
\end{aligned}
$$

where $z_{i, i^{\prime}}$ describes the sequence of vehicles passing through the merging zone as stated in Eq. (8). It takes only the value of 1 or 0 to choose one of these two equations to activate. For example, suppose $t_{0,1}^{*}>t_{1,1}^{*}$ which suggests that $V_{0,1}$ pass through the intersection after $V_{1,1}$, then we have $z_{1,1}=1$. In that case, Eq. (10) will be activated and Eq. (11) will be disabled.

In addition, the ranges of decision variables and intermediate variables are restricted by the following coupling constraints explicitly dependent on the lower-level model:

$$
\begin{aligned}
t_{k, i}^{+}+T_{\min } \leq t_{k, i}^{*} & \leq t_{k, i}^{+}+T_{\max }, \quad \forall k, i, \\
1 \leq y_{j}^{k} & \leq M_{\max }, \quad \forall k, j,
\end{aligned}
$$

where $T_{\text {min }}$ and $T_{\text {max }}$ denote the minimum and maximum time interval between arrival time $t_{k, i}^{+}$and start time $t_{k, i}^{*}$; $M_{\text {max }}$ denotes the maximum number of vehicles in a platoon. Note that $T_{\text {max }}$ is used to prevent vehicles from stopping (i.e., to avoid the undesirable phenomenon of stop-and-go traffic), whose value is affected by the motion pattern defined in the lower-level trajectory planning model. Besides, the value of $T_{\text {min }}$ is also determined by the lower-level model since the maximum speed and acceleration of vehicles are bounded by traffic regulations and mechanical limitations, respectively. As suggested by [64], a larger maximum allowable platoon size helps to increase roadway capacity, but may introduce greater difficulties in maintaining string stability. Therefore, the maximum platoon size $M_{\text {max }}$ should be limited to a moderate value to trade off capacity and maneuverability.
3) Objective Functions: In the upper-level model, the passing sequence and timeslots of vehicles are jointly optimized with the platoon configuration scheme by virtue of real-time traffic states to improve operational efficiency (i.e., the makespan) and fairness (i.e., the maximum delay). Hence, we formulate a bi-criteria optimization problem that simultaneously considers the makespan of the traffic scheduling scheme and the maximum delay of all the vehicles under constraints (7) and (9-13). Moreover, we conduct the lexicographic optimization on these objectives, the preferences of which are imposed by ordering objective functions according to their importance, rather than by assigning weights. In other words, the makespan is considered the chief objective while the maximum delay is subordinated, since the former has a
direct influence on the occurrence of spillbacks, according to Eq. (3). Specifically, we have

$$
\begin{aligned}
\min _{\boldsymbol{t}^{*}} f_{1}\left(\boldsymbol{t}^{*}\right) & =\max _{k \in \mathcal{K}, i \in \mathcal{I}}\left\{t_{k, i}^{*}+\frac{W+l}{v^{-}}\right\} \\
\min _{\boldsymbol{t}^{*}} f_{2}\left(\boldsymbol{t}^{*}\right) & =\max _{k \in \mathcal{K}, i \in \mathcal{I}}\left\{t_{k, i}^{*}-t_{k, i}^{+}-\frac{L+W+l}{v^{-}}\right\}
\end{aligned}
$$

where $\boldsymbol{t}^{*}=\left\{t_{k, i}^{*}\right\}_{k \in \mathcal{K}, i \in \mathcal{I}}$ represents the decision variables, i.e., the start times of vehicles. Additionally, $f_{1}\left(\boldsymbol{t}^{*}\right)$ and $f_{2}\left(\boldsymbol{t}^{*}\right)$ denote the makespan and the maximum delay, respectively.
4) Solution Algorithm: It is challenging to solve the traffic scheduling model in real-time through classical mathematical programming methods (e.g., MILP) due to the complexity of the merging coordination problem.

Fortunately, the latest released commercial Constraint Programming (CP) solvers (e.g., IBM ILOG CPLEX CP Optimizer [65] and Google's OR-Tools) offer us an opportunity to employ out-of-the-box algorithms to solve combinatorial optimization problems. The main advantage of CP is it can deal with complex problems with much more decision variables within limited runtime budgets while ensuring optimality. Especially, the standard CP solver provided by IBM ILOG CPLEX has shown to provide excellent performance in various scheduling problems (e.g., vehicle routing [66], train scheduling [67], drone scheduling [68], and airline management [69] problems). However, to the best of our knowledge, CP has not been used to solve the intersection management problem yet. Hence, this paper wants to leverage the advantages of this technique and ventures to pursue the global-optimal solution within the tight runtime budget, contributing a novel application of CP to traffic scheduling problems.

The CP solver works by iteratively trying different combinations of values for variables in the problem, checking to see if they satisfy all the constraints, and backtracking if they do not. Additionally, the CP solver uses a search strategy that is designed to explore all the space of solutions in an efficient way, and to prune branches of the search tree that are not likely to contain solutions. This process continues until the optimal solution is found or it is determined that no solution exists. We refer readers to [65] for a detailed explanation of the underlying optimization principle.

## C. Revisit of the Lower-Level Trajectory Planning Model

In this section, we first revisit the trajectory planning method developed in our previous studies [70], [71], where a Hybrid Evolutionary Algorithm with Cooperative Coevolution (HEA-CC) is proposed and proved to be efficient to deal with the multi-vehicle trajectory optimization. Furthermore, we formulate a new objective function to fit the setting of this problem, which not only reduces the overall energy consumption of vehicles but also improves the usage of road space to avoid/mitigate spillbacks. This task is non-trivial since vehicles with non-uniform initial separation distance are required to merge into platoons while complex dynamics and safety-critical constraints must be satisfied all the time.

It is noteworthy that the arrival time $t_{k, i}^{+}$and departure time $t_{k, i}^{-}$of vehicles can be known if the optimal traffic scheduling

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-07.jpg?height=490&width=715&top_left_y=200&top_left_x=1162)
Fig. 7. Illustration of the lower-level multi-vehicle trajectory planning task.

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-07.jpg?height=367&width=866&top_left_y=784&top_left_x=1087)
Fig. 8. Illustration of the encoding scheme for vehicle trajectories.

scheme has been generated by the upper-level model. Hence, these two kinds of parameters are defined as the input of the lower-level trajectory planning algorithm. As shown in Fig. 7, we are required to design referenced trajectories for vehicles according to the given platoon formation scheme and the allocated passing sequence and timeslots. In this paper, we adopt the HEA-CC algorithm as a building block in the proposed bi-level optimization approach to solve the trajectory planning problem. Besides, it is assumed that all the vehicles have to adjust their speeds to an identical value before entering the control zone such that their separation distances are stable. This setting can be achieved by a speed harmonization operation in advance [72], [73]. In addition, we assume that the motions of vehicles can be controlled by the platoon leader who serves as a centralized decisionmaker, where the predecessor-leader-following communication topology [74] and model predictive control approach [75], [76] are used to maintain the desired inter-vehicle distance and velocity according to the referenced trajectories.

Unlike the well-known and widely-used shooting heuristic algorithm in the literature [77], [78], [79], our trajectory planning method requires less predetermined rules about the motion patterns while having a higher degree of freedom since the speed profiles of trajectories are configured by the optimization algorithm appropriately. To be specific, each trajectory is encoded by a set of via-points named knots as shown in Fig. 8, whose number varies automatically to balance the computational efficiency and sufficient degrees of freedom. Hence, the original trajectory planning problem can be converted to a constrained numerical optimization problem. The complete shape of trajectories can be easily constructed for performance evaluation by cubic spline interpolation.

After that, we formulate a new objective function for trajectory optimization, which not only reduces the energy consumption of vehicles but also improves the usage of road space to avoid/mitigate spillbacks with the consideration of dynamics and safety constraints. For a given planning horizon $t \in\left[T_{0}, T_{0}+\Delta T\right]$, we can discretize it into evenly-distributed time points by $\Delta t$ which denotes the interval of time for decision-making. Therefore, we have $t_{\xi}=T_{0}+\xi \Delta t$, where $t_{0}=T_{0}, t_{M}=T_{0}+\Delta T$, and $\xi=\{0,1, \cdots, M\}$.

$$
\begin{aligned}
\min _{s_{i}}= & f_{i}\left[t_{\xi}\right] \sum_{i=1}^{n_{k}} \sum_{\xi=0}^{M} P_{i}\left(t_{\xi}\right) \Delta t+\sum_{c=1}^{4}\left[\sigma_{c} \sum_{i=1}^{n_{k}} \sum_{\xi=0}^{M} g_{c}^{2}\left(s_{i}^{t_{\xi}}\right)\right] \\
& +\alpha \sum_{i=1}^{n_{k}}\left(L-s_{i}^{t_{\xi}}\right) \Delta t
\end{aligned}
$$

Here, $s_{i}^{t_{\xi}}$ denotes the displacement of the front bumper of vehicle $i \in\left[1, n_{k}\right]$ at time $t_{\xi}, P_{i}\left(t_{\xi}\right)$ denotes the instantaneous power, For the second term, $g_{c}\left(s_{i}^{t_{\xi}}\right)$ denotes the penalty function with the corresponding weight coefficient $\sigma_{c}$, where $g_{1}(\cdot)$ measures the violation of traffic regulations, $g_{2}(\cdot)$ the mechanical limitation, $g_{3}(\cdot)$ the comfort criteria, and $g_{4}(\cdot)$ the separation distance. We refer readers to read [70] for the calculation of these energy and penalty functions.

Additionally, the last term in Eq. (16) denotes the sum of the area above trajectory curves, where $L$ is the length of road and $\alpha$ is the coefficient used to trade-off between the objectives of eco-driving and spillback avoidance. It is clear that for given start times $t_{k, i}^{*}$, increasing the sum of the area under trajectory curves (i.e., the dark area shown in Fig. 8) can reserve more space for subsequent vehicles, leading to a smaller length of queue (i.e., $L^{\prime}$ ), which helps to mitigate the occurrence of spillbacks according to Property 1.

In the next step, the set of trajectories within the same platoon are calculated in parallel using a divide-and-conquer strategy until a near-optimal solution has been found, or a terminal condition is met. Note that the HEA-CC algorithm is able to generate feasible referenced trajectories with high energy efficiency in a sub-second computation time, which is at least two orders of magnitude lower than the planning period even for large-scale instances.

## D. Discussion of the Extension to Mixed Traffic

It is noteworthy that the proposed intersection coordination algorithm can be readily extended to mixed traffic scenarios with various penetration rates of CAVs. Next, we will briefly explain how to address two major challenges associated with the mixed traffic condition.

On the one hand, without the help of traffic signals, the centralized controller located on the roadside cannot force Human-Driven Vehicles (HDVs) to comply with the advised passing sequence, especially if the leading vehicles of both approaches are HDVs. Therefore, one solution is to modify the proposed algorithm to preclude such scenarios by requiring all platoon leaders to be CAVs, which, however, may not be feasible if the penetration rates of CAVs are not sufficiently high. Nevertheless, we notice that in current

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-08.jpg?height=445&width=634&top_left_y=200&top_left_x=1201)
Fig. 9. Illustration of vehicle trajectories within the mixed traffic.

practice, unsignalized intersections with pure HDV traffic are coordinated using the FIFO policy to provide right-of-way to the HDV that arrives earlier. Inspired by this, we can integrate the proposed algorithm with the classical FIFO policy to coordinate mixed traffic and deal with specific scenarios where HDVs are platooned.

On the other hand, it is difficult to predict and control the behaviors and motions of HDVs. To address this challenge, many previous works used the classic Optimal Velocity Model [80] and Intelligent Driver Model [81] to estimate the behaviors of HDVs. However, such deterministic car-following models impose many assumptions on vehicles' desired velocity and spacing time, which require elaborate tuning of parameters and may not be favorable under uncertain conditions. Some other researchers try to perform evaluations against HDVs uncertainties with the least-assumption-based approach [63] that fixes the velocity of HDVs as constants, which is however not the setting of this problem.

Fortunately, Advanced Driver-Assistance System (ADAS) enables the centralized controller to issue proper minimum and maximum speed recommendations to HDV drivers via Human Machine Interface (HMI) [82]. In that case, HDVs will be able to track the desired speed and trajectory such that they can pass through the merging zone in their pre-determined timeslots to avoid collisions. Hence, the proposed bi-level intersection coordination algorithm can be extended to mixed traffic conditions with the Assumption 2.

Assumption 2 (Tracking errors of HDV trajectories): This paper assumes that HDVs are able to track the speed profile provided by the proposed algorithm with bounded tracking errors, i.e.,

$$
\left|t^{*}-t^{\text {real }}\right| \leq t_{\max }^{\epsilon},
$$

where $t^{*}$ denotes the expected time-headway of a HDV with its preceding or succeeding vehicle, $t^{\text {real }}$ the actual time-headway, and $t_{\text {max }}^{\epsilon}$ the maximum tracking errors of HDVs. In that case, other vehicles should keep a sufficient inter-vehicle distance with the maximum tracking error boundaries of HDVs to ensure safety. Accordingly, the upper-level traffic scheduling model should also take tracking errors into consideration by reserving more space for HDVs to ensure safety when it assigns timeslots for vehicles.

An example of the generated trajectory planning scheme in the mixed traffic condition is presented in Fig. 9, where

TABLE I
Parameters Setting for Simulations
| Description | Notation and Value |
| :--- | :--- |
| Length of Optimization Time Horizon | $\Delta T=20 \mathrm{~s}$ |
| Size of Decision Time-Step | $\Delta t=0.1 \mathrm{~s}$ |
| Length and Width of Road Segment | $L=150 \mathrm{~m}, W=2 \mathrm{~m}$ |
| Length of Vehicle | $l=3 \mathrm{~m}$ |
| Minimum Inter-Vehicle Distance | $d=1 \mathrm{~m}$ |
| Minimum Time-Headway | $\tau=0.5 \mathrm{~s}$ |
| Factor of Safety for Time-Headway | $\sigma_{1}=2, \sigma_{2}=3$ |
| Maximum Tracking Errors of HDVs | $t_{\text {max }}^{\epsilon}=0.25 \mathrm{~s}$ |
| Arrival, Departure, and Maximum Speed | $16 \mathrm{~m} / \mathrm{s}$, $16 \mathrm{~m} / \mathrm{s}$, 22 m/s |
| Range of Acceleration and Jerk | $\pm 3 \mathrm{~m} / \mathrm{s}^{2}, \pm 0.9 \mathrm{~m} / \mathrm{s}^{3}$ |
| Range of Travel Time | $T_{\text {min }}=9 \mathrm{~s}, T_{\text {max }}=25 \mathrm{~s}$ |
| Maximum Number of Vehicles in a Platoon | $M_{\text {max }}=25$ |


the vehicle platoon consists of six CAVs marked in blue and one HDV marked in red. It can be seen that the trajectories of CAVs are deterministic, while the trajectory of HDV is uncertain since the driver behavior cannot be precisely controlled. However, the tracking errors of the HDV are bounded within certain limits (i.e., the area in red), which have been considered in advance in the trajectory planning phase to ensure safety. In other words, the other CAVs would leave enough space to prevent confusion due to the control errors of HDVs.

## V. Numerical Simulation Experiments

In this section, we formulate a micro-simulation platform in MATLAB 2021b to evaluate the proposed VPA-AIM algorithm. The simulation parameters are set as shown in Table I. The basic setting in simulations includes the platooning willingness of vehicles and their ability to communicate with others. The appropriate length of the control region depends on the practical needs of applications, but it cannot exceed the reliable communication range of the intersection manager located nearby the merging zone. In this paper, we set the length of the control zone as 150 meters, similar to existing studies [41], [48], [78]. Note that the minimum time-headway can be reduced if the latency of vehicular communication is stably maintained at a low level. Hence, we determine the two values according to [45], [83], [84], and [85]. The value of the maximum tracking errors of HDVs depends on a wide range of factors, including the skill of drivers, the type of vehicles, and the traffic conditions. In this paper, we set this value as one-quarter of a second according to the benchmark average human response time [86]. In addition, we set the arrival and departure speeds to 60 km/h according to the free flow speed used in [12] and limit the maximum speed to about 80 km/h to ensure platooning safety as suggested by [84]. The range of acceleration and jerk are limited within the comfort criteria recommended by [87]. The maximum platoon size $M_{\text {max }}$ is set to 25 that conforms with the platoon size configuration in previous studies [77], [88].

## A. Design of Test Scenarios

The vehicle arrival time $t_{k, i}^{+}$is modeled as a Matérn hardcore stochastic point process [48] on the non-negative real line. Additionally, the distance between points is lower bounded by a certain number (i.e., $t_{k+1, i}^{+}-t_{k, i}^{+} \geq t_{k, i}^{k^{\prime}, i^{\prime}}$ ), which denotes the sequence-dependent minimum switching time of vehicles in the same platoon. This setting guarantees that no two vehicles are in collision at the time of arrival. Define Matérn process with parameter $\lambda$ as the Matérn process obtained by thinning a Poisson process [89] in the line that has intensity $\lambda$. Suppose $t=l / V_{\text {max }}$, then the intensity of Matérn Type I point process can be defined as

$$
\lambda_{I}(\lambda)=\frac{1-\exp (-2 \lambda t)}{2 t} .
$$

In order to generate multiple scenarios with different arrival flows within a reasonable range, we define the road capacity as the maximum flow of vehicles on a road segment. Given the minimum headway $\tau$, the road capacity can be calculated by $1 / \tau$.

Next, we generate nine groups of test instances whose arrival flows vary from 720 to 3600 vph/lane using the Matérn hard-core stochastic point process in the scenario of balanced and uniform traffic flow. Meanwhile, each group of traffic scenarios is simulated five times with different random seeds to replicate stochasticity in transportation systems, where the arrival time of vehicles is different, but the arrival flow keeps the same. In other words, there are $9 \times 5=45$ scenarios tested in total.

## B. Computational Results

In this section, the proposed VPA-AIM method is tested in multiple scenarios with different arrival flows and compared with the FIFO-, polling-, and scheduling-based methods for AIM. The FIFO-based method is modified from [83], which determines the passing sequence of vehicles according to their arrival orders. The polling-based method is modified from [48], which switches the priority of vehicles coming from different directions using an exhaustive policy. The traditional scheduling-based method is modified from [45], which solves a linear programming model to determine the passing sequence of individual vehicles without considering grouping vehicles into platoons.

The computational results for different scenarios are reported in Table II. Note that the data shown in this table denotes the average value of five scenarios, while the average computation time for the upper-level traffic scheduling model is presented in the last column. To quantify the optimization performance of different algorithms, we define the Relative Percent Deviation (RPD) as below. Suppose $f_{i}$ and $f_{i}$ denote the indicator obtained by the proposed and comparison algorithms, then we have

$$
\mathrm{RPD}_{i \rightarrow j}=\frac{\left|f_{j}-f_{i}\right|}{f_{i}} \times 100 \% .
$$

It can be seen from Table II that the proposed method outperforms the other benchmark methods for minimizing both the makespan and maximum delay in all scenarios tested.

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-10.jpg?height=408&width=1768&top_left_y=196&top_left_x=178)
Fig. 10. Comparison of performance indicators in different traffic scenarios. The left, middle, and right plots are representative of makespan, maximum delay, and the number of rolling horizon cycles without the occurrence of spillbacks, respectively.

TABLE II
Computational Results of Different Methods
| Arrival Flow (vph/lane) | Makespan (s) |  |  |  | Maximum Delay ( $s$ ) |  |  |  | Runtime (s) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | FIFO | Pol. | Sche. | Ours | FIFO | Pol. | Sche. | Ours |  |
| 720 | 28.1 | 28.3 | 28.0 | 27.5 | 1.2 | 3.0 | 1.0 | 0.8 | 0.03 |
| 1080 | 28.7 | 29.1 | 28.4 | 27.9 | 1.7 | 2.5 | 1.6 | 1.2 | 0.03 |
| 1440 | 31.6 | 29.9 | 29.3 | 28.4 | 5.8 | 6.3 | 4.1 | 2.1 | 0.06 |
| 1800 | 34.6 | 33.4 | 31.8 | 28.9 | 6.4 | 8.4 | 5.9 | 2.5 | 0.03 |
| 2160 | 39.5 | 35.5 | 35.1 | 29.3 | 10.9 | 8.9 | 9.5 | 3.1 | 0.18 |
| 2520 | 45.9 | 40.6 | 38.7 | 30.8 | 17.2 | 13.1 | 11.6 | 4.2 | 0.31 |
| 2880 | 50.9 | 42.9 | 42.2 | 30.8 | 22.8 | 15.9 | 15.1 | 6.1 | 0.55 |
| 3240 | 56.2 | 46.7 | 45.7 | 32.3 | 27.1 | 18.8 | 18.9 | 5.7 | 0.87 |
| 3600 | 61.3 | 50.1 | 49.3 | 32.9 | 32.4 | 22.1 | 21.4 | 7.5 | 1.89 |
| Average ( $s$ ) | 41.0 | 36.6 | 35.7 | 29.2 | 13.4 | 10.6 | 9.5 | 3.5 | 0.44 |
| RPD (\%) | 24.2 | 17.8 | 15.8 | - | 34.6 | 32.0 | 26.5 | - | - |


${ }^{1}$ The problem is solved with the CP solver in the IBM ILOG CPLEX Optimization Studio 12.9.0 using an Intel i7-6700HQ chip.

The makespan and maximum delay can be reduced by up to 24.2\% and 34.6\%, respectively. Besides, the proposed method maintains the maximum delay among vehicles below 8 seconds for all scenarios, ensuring fairness in passing the intersection.

Furthermore, the performances of all these methods are affected by the arrival flow, as shown in Fig. 10. First, it can be seen that all these methods perform similarly when the arrival flow is low (e.g., from 720 to 1080 vph/lane) since vehicles are able to pass the intersection without additional intervention. In other words, there is little room for optimization in these cases. However, the makespan and the maximum delay of solutions obtained by the FIFO-, polling, and scheduling-based methods increase dramatically with the arrival flow (i.e., from 1440 to 1800 vph/lane). Second, it is observed that either the FIFO- or polling-based methods cannot trade off multiple objectives. For example, the FIFO-based method is inferior to the polling policy in terms of efficiency (i.e., makespan) but outperforms the latter in terms of fairness (i.e., maximum delay). Third, it can be seen that the scheduling-based method overmatches FIFOand polling-based methods in both objectives within low-flow traffic states. However, its performance has weakened to a level similar to the polling-based method in medium and high-flow traffic states, which suggests that the traditional scheduling method has limitations and cannot work stably in all traffic scenarios.

By contrast, the proposed VPA-AIM algorithm performs better than all the benchmark methods. Moreover, the proposed algorithm keeps the makespan of the traffic scheduling scheme below the threshold value when the arrival flow is not greater than 1800 vph/lane. As shown in Table II, when the arrival flow over 1440 vph/lane, the makespans of FIFO-, polling-, and scheduling-based methods exceed $\Delta T+T_{\text {min }}=20+9=$ $29 s$, which is the threshold value for ensuring that spillbacks will not occur as stated in Eq. (3). If the makespan of the current traffic scheduling scheme exceeds this threshold value, the queue will be carried over from the current horizon to the next one, which may cause delays to propagate backward and accumulate, eventually leading to congestion and spillbacks. Although the resulting makespan of our method may exceed the threshold value in over-saturated scenarios, it does not exceed that value too much and can remain stable for a longer period of time than those of benchmark methods, and thus our method is more efficient in avoiding spillbacks and mitigating congestion.

According to Property 1, the number of rolling horizon cycles without the occurrence of spillbacks is shown in Fig. 10. It can be seen that the proposed VPA-AIM algorithm can avoid spillbacks in normal traffic states (when the arrival flow is not greater than 2520 vph/lane). Moreover, the proposed method provides a mitigation mechanism to regulate spillbacks caused by extreme arrival flows (i.e, 2880-3600 vph/lane). Although the propagation of delay cannot be avoided in these situations, the number of rolling horizon cycles without the occurrence of spillbacks resulting from the proposed method is larger than the benchmark methods, which suggests that it can disperse traffic for a longer time.

## C. Traffic Scheduling and Trajectory Design Schemes

The differences in traffic scheduling schemes obtained by different methods in different arrival flows are demonstrated in Fig. 11 using the conflict-duration-graph developed in our previous study [37]. In short, the conflict-duration graph is used to denote the occupation state of the merging zone, where each block denotes the periods occupied by a vehicle. Besides, the left and right endpoints of each block correspond with the start time $t_{k, i}^{*}$ and departure time $t_{k, i}^{+}$of vehicles, respectively. Additionally, the interval between two blocks denotes the separation in time of two vehicles to ensure safety, whose minimum value is decided by the sequence-dependent

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-11.jpg?height=978&width=870&top_left_y=202&top_left_x=172)
Fig. 11. Comparison of traffic scheduling scheme in different traffic scenarios. The top, middle, and bottom plots are representative of light, medium, and heavy load traffic.

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-11.jpg?height=967&width=694&top_left_y=1332&top_left_x=258)
Fig. 12. Optimized vehicle trajectories under different arrival flows. The top, middle, and bottom plots are representative of light, medium, and heavy load traffic. The upper half of each plot depicts vehicle trajectories of lane 1, while the lower half depicts those of lane 0.

minimum switching time. Note that it is non-trivial and challenging to calculate the optimal platoon formation scheme and passing sequence and time, which cannot be obtained by heuristic rules since multiple constraints need to be satisfied simultaneously.

The optimized trajectories for vehicles obtained by the proposed method are shown in Fig. 12. The upper and lower half of each plot depicts the trajectories of lane 1 and lane 0, respectively, while the vertical axis describes the distance of vehicles from the merging zone. First, it can be seen that the platoon configuration is not always consistent, but vary in different situations. This happens because the platoon formation scheme is designed by the optimization model appropriately according to real-time traffic states. Hence, more vehicles are assigned to a platoon when the arrival flow increases. Second, the generated trajectories are smooth enough without illegal speed jumps, while there is enough space between trajectories to prevent collisions. Hence, vehicles can pass the intersection collaboratively without stopping with the support of well-designed traffic scheduling and trajectory planning schemes. Third, it can be observed that the number of vehicles assigned to a platoon increases with the arrival flow. In highflow traffic states, the right-of-way will be given to groups of vehicles in two lanes alternately with different lengths of time. This is similar to the phenomenon at signalized intersections with an adaptive signal controller [90], [91], [92]. Hence, when it comes to signalized intersections, the proposed algorithm can be extended and used to design signal timing plans that determine the optimal green time of each lane. Moreover, the proposed algorithm can generate smooth trajectories for vehicles and cluster them into platoons that can properly use the green light windows and pass the intersection at high speed to avoid stop-and-go movements.

It can be seen from Fig. 13 that the CP solver can find the optimal traffic scheduling scheme for up to 32 vehicles with a sub-second computation time using a 20 -second time horizon. However, the complexity and difficulty of problem-solving grow with the number of vehicles, leading to an exponentially increased computation time. For those scenarios with more than 36 vehicles to be controlled, a smaller planning horizon is suggested to reduce the number of decision variables such that the computation time can be maintained within the subsecond level. Otherwise, the CP solver may not be able to find the optimal solution within the limited runtime budget. From the practical point of view, the classical FIFO policy can be employed as an alternative for those scenarios without sufficient time to optimize or cannot find any feasible solutions. Additionally, recall that we incorporate a coupled constraint i,e, Eq.(12), derived from the lower-level trajectory planning algorithm into the upper-level scheduling model, which is used to prevent vehicles from stopping. This constraint can be relaxed (i.e., increase the value of $T_{\text {max }}$ ) if the solver cannot find a feasible solution since it is possible that vehicles have to stop and wait before the stop line of intersections at extremely high-flow traffic states.

## D. Mixed Traffic Scenarios With Diverse Autonomy Levels

In order to analyze the impact of different CAV penetration rates on the performance of the proposed method, we generate

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-12.jpg?height=417&width=653&top_left_y=211&top_left_x=277)
Fig. 13. Computation time of the upper-level traffic scheduling model.

$9 \times 9$ groups of test scenarios whose arrival flows vary from 720 to 3600 vph/lane and penetration rates vary from 100\% to 20\%. Meanwhile, each group of traffic scenarios is simulated five times with different random seeds. To quantify the robustness of the proposed method in different arrival flows and penetration rates, we define the Average Performance Degradation (APD) as below. Let $i$ index the penetration rate of CAVs and $j$ index the arrival flow, we can denote the performance indicator (i.e., the makespan and maximum delay) under arbitrary conditions and a specific condition with $100 \%$ penetration rate by $f_{i, j}$ and $f_{j}^{*}$, respectively. Then, we have

$$
\mathrm{APD}_{i, j}=\frac{f_{i, j}-f_{j}^{*}}{f_{j}^{*}} \times 100 \% .
$$

It can be seen from Fig. 14 that, compared with the pure autonomy scenarios, both performance indicators (i.e., the makespan and the maximum delay) experience degradation when the penetration rate decreases in all kinds of arrival flow. This happens because HDVs require much more space than CAVs to ensure safety, leading to heavier burdens for the limited road resource. Additionally, the requirement that platoon leaders be CAVs imposes additional constraints on the optimization problem, leading to performance degradation of the optimal solution. Apart from this, it is also observed that the performance degradation in terms of the makespan becomes more significant when the arrival flow increases, the maximum value of which reaches 60\% when the arrival flow and penetration rate becomes 3600 vph/lane and 20\%, respectively. By contrast, the performance degradation in terms of the maximum delay reaches 80\% when the arrival flow and penetration rate becomes 2160 vph/lane and 20\%, respectively.

An example of the traffic scheduling and trajectory planning scheme in the mixed traffic scenario with dynamic traffic demands is illustrated in Fig. 15. Recall that HDVs are able to track the desired speed profile with limited tracking errors according to the Assumption 2. It can be seen that the upper-level scheduling model tends to assign more space for HDVs than CAVs to pass through the merging zone while avoiding collisions. Meanwhile, the lower-level trajectory planner is able to estimate the maximum tracking error boundaries of HDVs. Further, the planner will adjust the trajectories of CAVs such that they can maintain a safe separation distance from those HDVs nearby to ensure safety. Simulation results indicate that the proposed algorithm is

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-12.jpg?height=425&width=864&top_left_y=202&top_left_x=1085)
Fig. 14. Average performance degradation of the proposed method under different penetration rates of CAVs. The value of performance degradation denotes the average percentage of increase in performance indicators compared with that in the 100\% CAV penetration rate condition.

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-12.jpg?height=393&width=842&top_left_y=806&top_left_x=1094)
Fig. 15. Mixed autonomy scenario with dynamic traffic demands.

sufficiently robust to handle mixed autonomy conditions involving CAVs and HDVs with dynamic traffic demands.

## VI. Conclusion

This paper proposes a bilevel optimization algorithm, named VPA-AIM, to coordinate the merging of CAVs at unsignalized intersections. In this work, the upper-level task is referred to as platoon-aware traffic scheduling, which determines the platoon formation scheme of vehicles during the control zone and allocates the passing sequence and timeslots of platoons through the merging zone, with the goal of reducing the makespan and maximum delay to enhance operational efficiency and fairness. The lower-level task is referred to as multi-vehicle trajectory planning, which is about designing referenced trajectories for vehicles during the process of passing through the control and merging zones, with the goal of reducing overall energy consumption and avoiding/mitigating spillbacks. The two levels are coupled by dynamics constraints and the arrival and departure times of vehicles. The bi-level optimization framework optimizes traffic operation within a rolling horizon to balance traffic performance and computational efficiency. At each decision step, the optimal scheduling scheme at the upper level can be solved by the CPLEX Constraint Programming solver with sub-second computation time, while the near-optimal trajectories in the lower level can be generated by the coevolutionary algorithm modified from our previous work [70], [71]. In addition, this paper establishes the quantifiable connection between the makespan of the traffic scheduling scheme and the occurrence of spillbacks, demonstrating that the optimization of the makespan helps to avoid/mitigate spillbacks in normal/saturated traffic states. It is
also noteworthy that the proposed algorithm can be extended to mixed traffic scenarios with various penetration rates of CAVs based on the assumptions that HDVs have bounded tracking errors and CAVs serve as platoon leaders.

The proposed VPA-AIM algorithm is tested in multiple scenarios with various arrival flows (i.e., 720-3600 vph/lane) and compared with FIFO-, polling-, and scheduling-based methods in MATLAB. Extensive numerical examples suggest that the proposed algorithm outperforms benchmark methods in terms of efficiency and fairness. For example, the makespan and maximum delay of traffic scheduling schemes can be reduced by up to 24.2\% and 34.6\%, respectively. Besides, the proposed algorithm remains stable in all scenarios tested, while the performance of benchmark methods degrades dramatically with the increase in the arrival flow. Moreover, it has the largest number of rolling horizon cycles without the occurrence of spillbacks among benchmark methods, which suggests that it can mitigate spillbacks even in saturated traffic states.

This study opens several directions for future work. First, we would like to further generalize the proposed algorithm to a complex intersection with multiple approaches, and conduct comprehensive experimental validation using laboratory-scale Arduino cars. Second, we will extend the algorithm to urban arterial intersections or networks and devise signal coordination strategies to enable green waves with consideration of spillbacks. Third, we will consider intersection control with multiple types of road users such as transit vehicles that require priority and pedestrians that could impose additional randomness on the system dynamics. Finally, we would like to leverage the interactive protocol proposed by [93] to establish a verifiable communication scheme between authorized intersection controllers and vehicles, which helps to ensure the authenticity, integrity, and confidentiality of the mobility data and control commands being transmitted, and thus reduces the risk of data privacy and cybersecurity issues.

## Acknowledgment

The authors would like to thank Prof. Xiangrui Zeng (Huazhong University of Science and Technology) for discussions on Section III.

## References

[1] Q. Guo, L. Li, and X. J. Ban, "Urban traffic signal control with connected and automated vehicles: A survey," Transp. Res. C, Emerg. Technol., vol. 101, pp. 313-334, Apr. 2019.
[2] X. Li, J. Cui, S. An, and M. Parsafard, "Stop-and-go traffic analysis: Theoretical properties, environmental impacts and oscillation mitigation," Transp. Res. B, Methodol., vol. 70, pp. 319-339, Dec. 2014.
[3] S. Love, L. Kannis-Dymand, J. Davey, and J. Freeman, "Metacognition, rumination and road rage: An examination of driver anger progression and expression in Australia," Transp. Res. F, Traffic Psychol. Behaviour, vol. 84, pp. 21-32, Jan. 2022.
[4] G. Lu, Y. Wang, X. Wu, and H. X. Liu, "Analysis of yellow-light running at signalized intersections using high-resolution traffic data," Transp. Res. A, Policy Pract., vol. 73, no. 1, pp. 39-52, 2015.
[5] M. B. Jensen, M. P. Philipsen, M. Trivedi, T. Møgelmose, and T. Moeslund, "Vision for looking at traffic lights: Issues, survey, and perspectives," IEEE Trans. Intell. Transp. Syst., vol. 17, no. 7, pp. 1800-1815, Jul. 2016.
[6] D. Cao et al., "Future directions of intelligent vehicles: Potentials, possibilities, and perspectives," IEEE Trans. Intell. Vehicles, vol. 7, no. 1, pp. 7-10, Mar. 2022.
[7] W. Liu, L. Xiong, X. Xia, and Z. Yu, "Intelligent vehicle sideslip angle estimation considering measurement signals delay," in Proc. IEEE Intell. Vehicles Symp. (IV), Jun. 2018, pp. 1584-1589.
[8] K. Yang and M. Menendez, "Queue estimation in a connected vehicle environment: A convex approach," IEEE Trans. Intell. Transp. Syst., vol. 20, no. 7, pp. 2480-2496, Jul. 2019.
[9] H. Pei, J. Zhang, Y. Zhang, X. Pei, S. Feng, and L. Li, "Fault-tolerant cooperative driving at signal-free intersections," IEEE Trans. Intell. Vehicles, early access, Mar. 15, 2022, doi: 10.1109/TIV.2022.3159088.
[10] Y. Guo and J. Ma, "Leveraging existing high-occupancy vehicle lanes for mixed-autonomy traffic management with emerging connected automated vehicle applications," Transportmetrica A, Transp. Sci., vol. 16, no. 3, pp. 1375-1399, Jan. 2020.
[11] J. Ma, J. Hu, E. Leslie, F. Zhou, P. Huang, and J. Bared, "An ecodrive experiment on rolling terrains for fuel consumption optimization with connected automated vehicles," Transp. Res. C, Emerg. Technol., vol. 100, pp. 125-141, Mar. 2019.
[12] K. Yang, S. I. Guler, and M. Menendez, "Isolated intersection control for various levels of vehicle technology: Conventional, connected, and automated vehicles," Transp. Res. C, Emerg. Techn., vol. 72, pp. 109-129, Nov. 2016.
[13] Y. Guo, C. Xiong, J. Ma, and X. Li, "Joint optimization of vehicle trajectories and intersection controllers with connected automated vehicles: Combined dynamic programming and shooting heuristic approach," Transp. Res. C, Emerg. Technol., vol. 98, pp. 54-72, Jan. 2019.
[14] R. Niroumand, M. Tajalli, L. Hajibabai, and A. Hajbabaie, "Joint optimization of vehicle-group trajectory and signal timing: Introducing the white phase for mixed-autonomy traffic stream," Transp. Res. C, Emerg. Technol., vol. 116, Jul. 2020, Art. no. 102659.
[15] B. Yin, M. Menendez, and K. Yang, "Joint optimization of intersection control and trajectory planning accounting for pedestrians in a connected and automated vehicle environment," Sustainability, vol. 13, no. 3, p. 1135, Jan. 2021.
[16] F.-Y. Wang, "Scanning the issue and beyond: The T-ITS awards and future transportation," IEEE Trans. Intell. Transp. Syst., vol. 15, no. 6, pp. 2353-2359, Dec. 2014.
[17] M. Ferreira and P. M. D'Orey, "On the impact of virtual traffic lights on carbon emissions mitigation," IEEE Trans. Intell. Transp. Syst., vol. 13, no. 1, pp. 284-295, Mar. 2012.
[18] Y. Guo, J. Ma, E. Leslie, and Z. Huang, "Evaluating the effectiveness of integrated connected automated vehicle applications applied to freeway managed lanes," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 1, pp. 522-536, Jan. 2022.
[19] G. Guo, Z. Zhao, and R. Zhang, "Distributed trajectory optimization and fixed-time tracking control of a group of connected vehicles," IEEE Trans. Veh. Technol., early access, Oct. 10, 2022, doi: 10.1109/TVT.2022.3212023.
[20] G. Guo, D. Yang, and R. Zhang, "Distributed trajectory optimization and platooning of vehicles to guarantee smooth traffic flow," IEEE Trans. Intell. Vehicles, early access, May 31, 2022, doi: 10.1109/TIV.2022.3179293.
[21] G. Guo and Q. Wang, "Fuel-efficient en route speed planning and tracking control of truck platoons," IEEE Trans. Intell. Transp. Syst., vol. 20, no. 8, pp. 3091-3103, Aug. 2018.
[22] X. Han et al., "Strategic and tactical decision-making for cooperative vehicle platooning with organized behavior on multi-lane highways," Transp. Res. C, Emerg. Technol., vol. 145, Dec. 2022, Art. no. 103952.
[23] Q. Jin, G. Wu, K. Boriboonsomsin, and M. Barth, "Platoon-based multiagent intersection management for connected vehicle," in Proc. 16th Int. IEEE Conf. Intell. Transp. Syst. (ITSC), Oct. 2013, pp. 1462-1467.
[24] R. Tachet et al., "Revisiting street intersections using slot-based systems," PLoS ONE, vol. 11, no. 3, Mar. 2016, Art. no. e0149607.
[25] J. Lioris, R. Pedarsani, F. Y. Tascikaraoglu, and P. Varaiya, "Platoons of connected vehicles can double throughput in urban roads," Transp. Res. C, Emerg. Technol., vol. 77, pp. 292-305, Apr. 2017.
[26] G. Tilg, K. Yang, and M. Menendez, "Evaluating the effects of automated vehicle technology on the capacity of freeway weaving sections," Transp. Res. C, Emerg. Technol., vol. 96, pp. 3-21, Nov. 2018.
[27] X. Han, R. Ma, and H. M. Zhang, "Energy-aware trajectory optimization of CAV platoons through a signalized intersection," Transp. Res. C, Emerg. Technol., vol. 118, Sep. 2020, Art. no. 102652.
[28] B. Qian, H. Zhou, F. Lyu, J. Li, T. Ma, and F. Hou, "Toward collisionfree and efficient coordination for automated vehicles at unsignalized intersection," IEEE Internet Things J., vol. 6, no. 6, pp. 10408-10420, Dec. 2019.

[29] C. Yu, W. Sun, H. X. Liu, and X. Yang, "Managing connected and automated vehicles at isolated intersections: From reservationto optimization-based methods," Transp. Res. B, Methodol., vol. 122, pp. 416-435, Apr. 2019.
[30] Z. Yang, Y. Feng, and H. X. Liu, "A cooperative driving framework for urban arterials in mixed traffic conditions," Transp. Res. C, Emerg. Technol., vol. 124, Mar. 2021, Art. no. 102918.
[31] X. Xiao, Y. Pan, L. Lv, and Y. Shi, "Scheduling multi-mode resourceconstrained tasks of automated guided vehicles with an improved particle swarm optimization algorithm," IET Collaborative Intell. Manuf., vol. 3, no. 2, pp. 93-104, Jun. 2021.
[32] K. Dresner and P. Stone, "A multiagent approach to autonomous intersection management," J. Artif. Intell. Res., vol. 31, pp. 591-656, Mar. 2008.
[33] Y. Meng, L. Li, F.-Y. Wang, K. Li, and Z. Li, "Analysis of cooperative driving strategies for nonsignalized intersections," IEEE Trans. Veh. Technol., vol. 67, no. 4, pp. 2900-2911, Apr. 2018.
[34] H. Xu, C. G. Cassandras, L. Li, and Y. Zhang, "Comparison of cooperative driving strategies for CAVs at signal-free intersections," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 7, pp. 7614-7627, Jul. 2022.
[35] Y. Bian, S. E. Li, W. Ren, J. Wang, K. Li, and H. X. Liu, "Cooperation of multiple connected vehicles at unsignalized intersections: Distributed observation, optimization, and control," IEEE Trans. Ind. Electron., vol. 67, no. 12, pp. 10744-10754, Dec. 2020.
[36] D. Fajardo, T.-C. Au, S. T. Waller, P. Stone, and D. Yang, "Automated intersection control: Performance of future innovation versus current traffic signal control," Transp. Res. Rec., J. Transp. Res. Board, vol. 2259, no. 1, pp. 223-232, 2011.
[37] Z. Deng, Y. Shi, Q. Han, L. Lv, and W. Shen, "A conflict duration graphbased coordination method for connected and automated vehicles at signal-free intersections," Appl. Sci., vol. 10, no. 18, p. 6223, Sep. 2020.
[38] M. W. Levin, S. D. Boyles, and R. Patel, "Paradoxes of reservationbased intersection controls in traffic networks," Transp. Res. A, Policy Pract., vol. 90, pp. 14-25, Aug. 2016.
[39] Z. Li et al., "Temporal-spatial dimension extension-based intersection control formulation for connected and autonomous vehicle systems," Transp. Res. C, Emerg. Technol., vol. 104, pp. 234-248, Jul. 2019.
[40] S. A. Fayazi and A. Vahidi, "Mixed-integer linear programming for optimal scheduling of autonomous vehicle intersection crossing," IEEE Trans. Intell. Veh., vol. 3, no. 3, pp. 287-299, Sep. 2018.
[41] Z. Wang, G. Wu, and M. J. Barth, "Cooperative eco-driving at signalized intersections in a partially connected and automated vehicle environment," IEEE Trans. Intell. Transp. Syst., vol. 21, no. 5, pp. 2029-2038, May 2020.
[42] P. Dai, K. Liu, Q. Zhuge, E. H.-M. Sha, V. C. S. Lee, and S. H. Son, "Quality-of-experience-oriented autonomous intersection control in vehicular networks," IEEE Trans. Intell. Transp. Syst., vol. 17, no. 7, pp. 1956-1967, Jul. 2016.
[43] Q. Lu and K.-D. Kim, "A mixed integer programming approach for autonomous and connected intersection crossing traffic control," in Proc. IEEE 88th Veh. Technol. Conf. (VTC-Fall), Aug. 2018, pp. 1-6.
[44] W. Zhao, R. Liu, and D. Ngoduy, "A bilevel programming model for autonomous intersection control and trajectory planning," Transportmetrica A, Transp. Sci., vol. 17, no. 1, pp. 34-58, 2021.
[45] Z. Yao, H. Jiang, Y. Cheng, Y. Jiang, and B. Ran, "Integrated schedule and trajectory optimization for connected automated vehicles in a conflict zone," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 3, pp. 1841-1851, Mar. 2022.
[46] C. Yu, Y. Feng, H. X. Liu, W. Ma, and X. Yang, "Integrated optimization of traffic signals and vehicle trajectories at isolated urban intersections," Transp. Res. B, Methodol., vol. 112, pp. 89-112, Jun. 2018.
[47] A. I. M. Medina, N. Van De Wouw, and H. Nijmeijer, "Cooperative intersection control based on virtual platooning," IEEE Trans. Intell. Transp. Syst., vol. 19, no. 6, pp. 1727-1740, Jun. 2017.
[48] D. Miculescu and S. Karaman, "Polling-Systems-Based autonomous vehicle coordination in traffic intersections with no traffic signals," IEEE Trans. Autom. Control, vol. 65, no. 2, pp. 680-694, Feb. 2020.
[49] P. Tallapragada and J. Cortés, "Hierarchical-distributed optimized coordination of intersection traffic," IEEE Trans. Intell. Transp. Syst., vol. 21, no. 5, pp. 2100-2113, May 2020.
[50] Q. Ge et al., "Real-time coordination of connected vehicles at intersections using graphical mixed integer optimization," IET Intell. Transp. Syst., vol. 15, no. 6, pp. 795-807, Jun. 2021.
[51] M. W. Levin and D. Rey, "Conflict-point formulation of intersection control for autonomous vehicles," Transp. Res. C, Emerg. Technol., vol. 85, pp. 528-547, Dec. 2017.
[52] A. Mirheli, M. Tajalli, L. Hajibabai, and A. Hajbabaie, "A consensusbased distributed trajectory control in a signal-free intersection," Transp. Res. C, Emerg. Technol., vol. 100, pp. 161-176, Mar. 2019.
[53] X. Li, A. Ghiasi, and Z. Xu, "A piecewise trajectory optimization model for connected automated vehicles: Exact optimization algorithm and queue propagation analysis," Transp. Res. B, Methodol., vol. 118, pp. 429-456, Dec. 2018.
[54] K. Abboud, H. A. Omar, and W. Zhuang, "Interworking of DSRC and cellular network technologies for V2X communications: A survey," IEEE Trans. Veh. Technol., vol. 65, no. 12, pp. 9457-9470, Dec. 2016.
[55] Y. Shi, Q. Han, W. Shen, and H. Zhang, "Potential applications of 5G communication technologies in collaborative intelligent manufacturing," IET Collaborative Intell. Manuf., vol. 1, no. 4, pp. 109-116, Dec. 2019.
[56] F. Hu, L. Lv, T. Zhang, and Y. Shi, "Vehicular task scheduling strategy with resource matching computing in cloud-edge collaboration," IET Collaborative Intell. Manuf., vol. 3, no. 4, pp. 334-344, Dec. 2021.
[57] W. Liu, L. Xiong, X. Xia, Y. Lu, L. Gao, and S. Song, "Vision-aided intelligent vehicle sideslip angle estimation based on a dynamic model," IET Intell. Transp. Syst., vol. 14, no. 10, pp. 1183-1189, Oct. 2020.
[58] L. Xiong et al., "IMU-based automated vehicle body sideslip angle and attitude estimation aided by GNSS using parallel adaptive Kalman filters," IEEE Trans. Veh. Technol., vol. 69, no. 10, pp. 10668-10680, Oct. 2020.
[59] W. Liu, X. Xia, L. Xiong, Y. Lu, L. Gao, and Z. Yu, "Automated vehicle sideslip angle estimation considering signal measurement characteristic," IEEE Sensors J., vol. 21, no. 19, pp. 21675-21687, Oct. 2021.
[60] S. I. Guler, M. Menendez, and L. Meier, "Using connected vehicle technology to improve the efficiency of intersections," Transp. Res. C, Emerg. Technol., vol. 46, pp. 121-131, Sep. 2014.
[61] H. Yao and X. Li, "Decentralized control of connected automated vehicle trajectories in mixed traffic at an isolated signalized intersection," Transp. Res. C, Emerg. Technol., vol. 121, Dec. 2020, Art. no. 102846.
[62] T. Li, X. Han, and J. Ma, "Cooperative perception for estimating and predicting microscopic traffic states to manage connected and automated traffic," IEEE Trans. Intell. Transp. Syst., vol. 23, no. 8, pp. 13694-13707, Aug. 2022.
[63] M. Faris, P. Falcone, and J. Sjöberg, "Optimization-based coordination of mixed traffic at unsignalized intersections based on platooning strategy," in Proc. IEEE Intell. Vehicles Symp. (IV), Jun. 2022, pp. 977-983.
[64] J. Zhou and F. Zhu, "Analytical analysis of the effect of maximum platoon size of connected and automated vehicles," Transp. Res. C, Emerg. Technol., vol. 122, Jan. 2021, Art. no. 102882.
[65] Ilog Cplex Optimization Studio. Accessed: Jul. 1, 2022. [Online]. Available: https://www.ibm.com/products/ilog-cplex-optimization-studio
[66] M. H. Hà, T. D. Nguyen, T. N. Duy, H. G. Pham, T. Do, and L.-M. Rousseau, "A new constraint programming model and a linear programming-based adaptive large neighborhood search for the vehicle routing problem with synchronization constraints," Comput. Oper. Res., vol. 124, Dec. 2020, Art. no. 105085.
[67] J. Rodriguez, "A constraint programming model for real-time train scheduling at junctions," Transp. Res. B, Methodol., vol. 41, no. 2, pp. 231-245, Feb. 2007.
[68] A. M. Ham, "Integrated scheduling of $m$-truck, $m$-drone, and $m$-depot constrained by time-window, drop-pickup, and $m$-visit using constraint programming," Transp. Res. C, Emerg. Technol., vol. 91, pp. 1-14, Jun. 2018.
[69] N. Schefers, J. J. R. González, P. Folch, and J. L. Munoz-Gamarra, "A constraint programming model with time uncertainty for cooperative flight departures," Transp. Res. C, Emerg. Technol., vol. 96, pp. 170-191, Nov. 2018.
[70] Z. Deng, J. Fan, Y. Shi, and W. Shen, "A coevolutionary algorithm for cooperative platoon formation of connected and automated vehicles," IEEE Trans. Veh. Technol., vol. 71, no. 12, pp. 12461-12474, Dec. 2022.
[71] Z. Deng, J. Fan, Y. Shi, and W. Shen, "Longitudinal trajectory optimization for connected and automated vehicles by evolving cubic splines with coevolution," in Proc. IEEE 25th Int. Conf. Comput. Supported Cooperat. Work Design (CSCWD), May 2022, pp. 641-646.
[72] J. Ma et al., "Freeway speed harmonization," IEEE Trans. Intell. Veh., vol. 1, no. 1, pp. 78-89, Mar. 2016.
[73] A. Ghiasi, X. Li, and J. Ma, "A mixed traffic speed harmonization model with connected autonomous vehicles," Transp. Res. C, Emerg. Technol., vol. 104, pp. 210-233, Jul. 2019.
[74] Z. Wang, Y. Bian, S. E. Shladover, G. Wu, S. E. Li, and M. J. Barth, "A survey on cooperative longitudinal motion control of multiple connected and automated vehicles," IEEE Intell. Transp. Syst. Mag., vol. 12, no. 1, pp. 4-24, Spring 2020.

[75] Y. Zhou, M. Wang, and S. Ahn, "Distributed model predictive control approach for cooperative car-following with guaranteed local and string stability," Transp. Res. B, Methodol., vol. 128, pp. 69-86, Jan. 2019.
[76] M. Gheisarnejad and M.-H. Khooban, "Supervised control strategy in trajectory tracking for a wheeled mobile robot," IET Collaborative Intell. Manuf., vol. 1, no. 1, pp. 3-9, 2019.
[77] J. Ma, X. Li, F. Zhou, J. Hu, and B. B. Park, "Parsimonious shooting heuristic for trajectory design of connected automated traffic part II: Computational issues and optimization," Transp. Res. B, Methodol., vol. 95, pp. 421-441, Jan. 2017.
[78] L. Li and X. Li, "Parsimonious trajectory design of connected automated traffic," Transp. Res. B, Methodol., vol. 119, pp. 1-21, Jan. 2019.
[79] Z. Xu et al., "Trajectory optimization for a connected automated traffic stream: Comparison between an exact model and fast heuristics," IEEE Trans. Intell. Transp. Syst., vol. 22, no. 5, pp. 2969-2978, May 2021.
[80] M. Bando, K. Hasebe, K. Nakanishi, and A. Nakayama, "Analysis of optimal velocity model with explicit delay," Phys. Rev. E, Stat. Phys. Plasmas Fluids Relat. Interdiscip. Top., vol. 58, no. 5, p. 5429, 1998.
[81] A. Kesting, M. Treiber, and D. Helbing, "Enhanced intelligent driver model to access the impact of driving strategies on traffic capacity," Philosoph. Trans. Roy. Soc. A, vol. 368, no. 1928, pp. 4585-4605, Oct. 2010.
[82] E. Adell, A. Varhelyi, M. Alonso, and J. Plaza, "Developing humanmachine interaction components for a driver assistance system for safe speed and safe distance," IET Intell. Transp. Syst., vol. 2, no. 1, pp. 1-14, 2008.
[83] Z. Wang, G. Wu, and M. Barth, "Distributed consensus-based cooperative highway on-ramp merging using V2X communications," SAE International, Detroit, MI, USA, SAE Tech. Paper 2018-01-1177, 2018.
[84] J. Thunberg, N. Lyamin, K. Sjöberg, and A. Vinel, "Vehicle-to-vehicle communications for platooning: Safety analysis," IEEE Netw. Lett., vol. 1, no. 4, pp. 168-172, Dec. 2019.
[85] Q. Chen, Y. Zhou, S. Ahn, J. Xia, S. Li, and S. Li, "Robustly string stable longitudinal control for vehicle platoons under communication failures: A generalized extended state observer-based control approach," IEEE Trans. Intell. Vehicles, early access, Feb. 25, 2022, doi: 10.1109/TIV.2022.3153472.
[86] C. D. Wickens, W. S. Helton, J. G. Hollands, and S. Banbury, Engineering Psychology and Human Performance. Evanston, IL, USA: Routledge, 2021.
[87] I. Bae, J. Moon, and J. Seo, "Toward a comfortable driving experience for a self-driving shuttle bus," Electronics, vol. 8, no. 9, p. 943, Aug. 2019.
[88] F. Zhou, X. Li, and J. Ma, "Parsimonious shooting heuristic for trajectory design of connected automated traffic part I: Theoretical analysis with generalized time geography," Transp. Res. B, Methodol., vol. 95, pp. 394-420, Jan. 2017.
[89] J. Zheng and H. X. Liu, "Estimating traffic volumes for signalized intersections using connected vehicle data," Transp. Res. C, Emerg. Technol., vol. 79, pp. 347-362, Jun. 2017.
[90] G. Guo and Y. Wang, "Eco-driving of freight vehicles with signal priority on congested arterial roads," IEEE Trans. Veh. Technol., vol. 70, no. 5, pp. 4225-4237, May 2021.
[91] K. Yang, M. Menendez, and S. I. Guler, "Implementing transit signal priority in a connected vehicle environment with and without bus stops," Transportmetrica B, Transp. Dyn., vol. 7, no. 1, pp. 423-445, Dec. 2019.
[92] G. Guo and Y. Wang, "An integrated MPC and deep reinforcement learning approach to trams-priority active signal control," Control Eng. Pract., vol. 110, May 2021, Art. no. 104758.
[93] M. Tsao, K. Yang, S. Zoepf, and M. Pavone, "Trust but verify: Cryptographic data privacy for mobility management," IEEE Trans. Control Netw. Syst., vol. 9, no. 1, pp. 50-61, Mar. 2022.

![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-15.jpg?height=320&width=256&top_left_y=215&top_left_x=1081)

Zhiyun Deng (Graduate Student Member, IEEE) recieved the B.E. degree from the School of Automotive Engineering, Wuhan University of Technology, Wuhan, China, in 2020, and the M.S. degree from the School of Mechanical Science and Engineering, Huazhong University of Science and Technology (HUST), Wuhan, in 2022. He is currently a Research Assistant with HUST. His current research interests include planning and scheduling algorithms for emerging mobility, and the automatic control of vehicular systems with deep reinforcement learning.
![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-15.jpg?height=320&width=238&top_left_y=685&top_left_x=1083)

Kaidi Yang received the B.Eng. and M.Sc. degrees from Tsinghua University and the Ph.D. degree from ETH Zurich. He is currently an Assistant Professor with the Department of Civil and Environmental Engineering, National University of Singapore. Prior to this, he was a Post-Doctoral Researcher with the Autonomous Systems Laboratory, Stanford University. His main research interests include the operation of future mobility systems enabled by connected and automated vehicles (CAVs) and shared mobility.
![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-15.jpg?height=320&width=254&top_left_y=1147&top_left_x=1083)

Weiming Shen (Fellow, IEEE) received the bachelor's and master's degrees from Northern Jiaotong University, Beijing, China, in 1983 and 1986, respectively, and the Ph.D. degree from the University of Technology of Compiegne, Compiègne, France, in 1996. He is currently a Professor with the Huazhong University of Science and Technology, Wuhan, China, and an Adjunct Professor with the University of Western Ontario, London, ON, Canada. His research interests include intelligent software agents, wireless-sensor networks, the IoT, big data, and their applications in industry. He is a fellow of the Canadian Academy of Engineering and the Engineering Institute of Canada.
![](https://cdn.mathpix.com/cropped/c2b5bbe9-7b9b-41f0-a30a-c307cb509c54-15.jpg?height=312&width=254&top_left_y=1684&top_left_x=1081)

Yanjun Shi received the B.S. degree in mechanical engineering from Dalian Ocean University, China, in 1996, the M.S. degree in mechatronic engineering from Beihang University, China, in 1999, and the Ph.D. degree in computer engineering from the Dalian University of Technology, China, in 2005. He is currently an Associate Professor with the School of Mechanical Engineering, Dalian University of Technology. He has authored or coauthored over 80 papers in scientific journals and international conferences. His research interests include collaborative planning and scheduling, multi-access edge computing, 5G applications, and autonomous vehicles. He is the Vice Chair of the IEEE SMC Dalian Chapter. He is an Associate Editor of the IET Collaborative Intelligent Manufacturing.


[^0]:    ${ }^{1}$ Note that the free-flow condition is only used to estimate the virtual departure time of vehicles, not the necessary condition of the proposed algorithm.

