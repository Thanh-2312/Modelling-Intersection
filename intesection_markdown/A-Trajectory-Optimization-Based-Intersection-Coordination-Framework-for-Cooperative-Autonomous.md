# A Trajectory Optimization-Based Intersection Coordination Framework for Cooperative Autonomous Vehicles 

Yixiao Zhang ${ }^{\text {(b) }}$, Rui Hao, Tingting Zhang ${ }^{\text {(iD) }}$, Member, IEEE, Xiaohan Chang, Zepeng Xie, and Qinyu Zhang ${ }^{\text {(iD) }}$, Senior Member, IEEE


#### Abstract

Since vehicles from multiple roads frequently merge at intersections, it formulates a typical traffic bottleneck of modern transportation systems. Proper vehicle coordination and motion plan at road intersections are of importance to guarantee safety as well as improving the traffic throughput, fuel efficiency and so on. In this paper, we try to present a general dedicated intersection coordination framework for autonomous vehicles, where both high- and low-level planners are appropriately designed and integrated. In the high-level planner, two different strategies are formulated to coordinate the autonomous vehicles to generate reference trajectories and feasible "tunnels", respectively. Especially, a novel space-time-block based resource allocation scheme is presented to describe the feasible tunnels. Furthermore, to avoid collisions with unexpected obstacles such as pedestrians, bicycles or other vehicles with human drivers, a low-level planner is designed to generate practical trajectories based on the solutions from the high-level planner, according to their local on-board observations. Simulations and practical experiments are carried out, to show that our proposed coordination framework can achieve obvious performance advantages in various traffic metrics, including the throughput, fairness in driving maneuvers and driving comfort, etc. We also find that the high-level planner is effective in eliminating possible deadlocks among autonomous vehicles, which is rarely discussed in existing investigations.


Index Terms-Road transportation, multi-agent systems, autonomous vehicles, motion planning, trajectory optimization.

Manuscript received 20 May 2021; revised 14 September 2021; accepted 17 November 2021. Date of publication 15 December 2021; date of current version 12 September 2022. This work was supported in part by the National Scientific Foundation of China (NSFC) under Grant 62171160, Grant 61771159, and Grant 91638204; and in part by the Shenzhen Fundamental Research Project under Grant JCYJ20190806143212658. The work of Qinyu Zhang was supported in part by the National Natural Sciences Foundation of China under Grant 61831008 and Grant 62027802 and in part by the Guangdong Science and Technology Planning Project under Grant 2018B030322004. An earlier version of this paper was presented in part at the 2021 IEEE International Conference on Autonomous Systems (ICAS) [1] [DOI: 10.1109/ICAS49788.2021.9551179]. The Associate Editor for this article was C. F. Mecklenbräuker. (Corresponding author: Tingting Zhang.)
Yixiao Zhang is with the School of Electrical Engineering and Computer Science, KTH Royal Institute of Technology (KTH), Stockholm 11428, Sweden.

Rui Hao and Zepeng Xie are with the School of Electronics and Information Engineering, Harbin Institute of Technology (Shenzhen), Shenzhen 518055, China.

Tingting Zhang and Qinyu Zhang are with the School of Electronics and Information Engineering, Harbin Institute of Technology (Shenzhen), Shenzhen 518055, China, and also with the Peng Cheng Laboratory (PCL), Shenzhen 518066, China (e-mail: zhangtt@hit.edu.cn).

Xiaohan Chang is with the School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences, Beijing 101408, China.

This article has supplementary downloadable material available at https://doi.org/10.1109/TITS.2021.3131570, provided by the authors.

Digital Object Identifier 10.1109/TITS.2021.3131570

## I. Introduction

A. Background and Motivation

AS O NE of the comersonas of the madern seciety, the tratifional read trafic system is now Weings tremendous presare and challenge, wiln the capid utratamizion and industratiatiston [21-31.7. There are so many venides those arc expeced to eneret the transportions system, that hey are posting the read infrafanceuter to, or even beyond it limits. At roas intercescitons where mutupipe reaus cross or megge,
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-01.jpg?height=37&width=877&top_left_y=1059&top_left_x=1083) intercescions occupy a perty small part of the centre read system. Aceording to recent repors from Europe and he United States, rodintersections account for a significan part of the bottence of the traffic systems. More than 40\% of
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-01.jpg?height=37&width=877&top_left_y=1268&top_left_x=1083) tions [2], [16. Therefora, un we intersection nammagement is one of die most presing and challeging problems in moder traffic systems
Traditinal intersection cocordination solumos include traffoc lights, roundabous and sop signs, etc. which minity
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-01.jpg?height=37&width=879&top_left_y=1517&top_left_x=1083) information and communiciston crechologies, such as verticle-
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-01.jpg?height=39&width=877&top_left_y=1598&top_left_x=1083) eanbled new won signivied de checks. by y haring enviromench${ }^{\text {tal information and planing results anong vehiles through }}$ vericultra an hoc neworis (VANETS) [3]. Accortingly. the modoins of verheles could be earcuily planced viva a cocortanation center an verifeics themselves.
Mos existing investagiations on verhice metion planing focus on the cgo vehicl [7]. Honevers, at intencectons where multiple radas merges, rupere coopertion amongs vehicles will be helpful (4). [S]. Furthemore, in compliciacd driving
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-01.jpg?height=39&width=877&top_left_y=2013&top_left_x=1083) and ober main-difien vencirces arc in icluded. The auconomous veñice stould be able to maice decisions accoring to its
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-01.jpg?height=37&width=877&top_left_y=2138&top_left_x=1083) etc. Therefore, it is natural to formulatia an integracted covardantion francework, in which the copercioning anong vehiles. as well as the ego polaner, should bont be considered.

## B. Retared Works

Depending on the working sylles current intersection cororinination inescietientions could be categericated into
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-01.jpg?height=39&width=877&top_left_y=2490&top_left_x=1083)
respectively. In infrastructure-based planners, a centralized coordinator, which could be integrated in the road side unit (RSU), will receive the requests from vehicles and then coordinate the maneuver and trajectory for each vehicle [4]. Though these strategies have the potential to improve the safety, fuel efficiency and traffic throughput [8], they mostly focus on the coordination among vehicles and lack of flexibility when dealing with other random obstacles, such as pedestrians, bicycles and parked cars. In vehicle-based planners, vehicles use their own sensors such as cameras, radars and communication modules, for environment awareness, and then plan trajectories accordingly at their on-board computing units [9]. Though these strategies account for most the possible obstacles, and improve passenger comfort via trajectory smoothness, it becomes less efficient and even lead to possible deadlocks [10] when the number of vehicles increases.

One major category is using the infrastructure-based centralized node to allocate the space and time resources of the intersection for vehicles [4]. In the resource allocation, different metrics can be adopted for the coordination, among which the safety and efficiency are mostly concerned [11]. To guarantee the safety issue, the area where the collisions may occur is defined as the collision set. Multiple vehicles cannot enter one collision set simultaneously. These original coordination problems can be usually reformulated as mixed integer programming (MIP) problems [12]. In order to improve the efficiency, some researches tried to extend the single collision set model to multiple-set one, for better use of space resources. But the multiple-collision-set coordination depends heavily on the road structure and interactions between the pre-specified paths from different lanes [13]-[16].

Authors in [17], [18] considered the dynamic arrival of vehicles. A coordination framework based on the rate stability theorem is used to improve the queue stability of the intersection. However, most investigations are based on simplified linear trajectories, which cannot be applied in practical real-time vehicle control. In [18], [19], the coordination was formulated along with the kinematic vehicle model, to improve the feasibility and trajectory smoothness. Furthermore, another challenge lies in the fact that the computation complexity on the coordination agent may be severe when the vehicle number is large. In [20], an efficient computation offloading method was used to reduce the computation time of the system.

There also exist several investigations on vehicle-based strategies. Unlike the infrastructure-based coordination, the decision is performed by the individual vehicle, or a local group of vehicles [7]. For optimization-based strategies, traditional model predictive control (MPC) is a highly popular solution, which can find a predictive motion solution over a longer horizon time at each sampling time [21], [22]. Though the main advantages of traditional MPC are its logicality and predictive horizon, it is still rather limited for non-convex and high complexity problems. Therefore, a progressive MPC can be given by combining with some function optimization strategies [23]. Parametric curves those subject to vehicle kinematic constraints can be used to describe trajectory functions, e.g., line \& circle curves [24], polynomial curves [25], Bézier curves [26], [27] and splines [28], [29]. Accordingly, after modeling the vehicle and environment constraints in a mathematical form, a suitable solver of motion planning can help to find the optimal trajectory function. In [30], a trajectory optimization method of path and speed profile generation separately was proposed, which can reduce the complexity of the three-dimensional optimization. Meanwhile, the quadratic programming (QP) is a useful tool to search iteratively for an optimal/sub-optimal solution [31], [32]. However, when obstacles such as pedestrians are involved, the trajectory planning problems become non-convex. Baidu Apollo EM planner thus combined dynamic programming (DP) with QP, to give feasible solutions [33]. There also exist another major category on learning-based approaches, such as reinforcement learning [34]-[36], end-to-end learning [37], etc., which mainly requires high computing resources and training time [38].

To the best of the authors' knowledge, there are rather limited investigations on considering both efficiency and flexibility in multi-obstacle and multi-vehicle intersections, which is also one of main motivations of this paper.

## C. Main Contributions

In this paper, we try to smartly integrate the infrastructure and vehicle-based planners together, to provide safe, efficient and comfortable vehicle maneuvers. According to the analysis, our proposed coordination framework is shown to be able to obviously improve the coordination performance (traffic throughput, fairness, queueing stability). Meanwhile, it also remains the flexibility for avoiding collisions with unexpected obstacles. Theoretical analysis and practical experiments are provided. Main contributions can be concluded as follows.

- We propose a double-level coordination framework based on vehicle trajectory optimization. A high-level planner (infrastructure-based) is used to provide reference trajectories and feasible tunnels for all autonomous vehicles, which can avoid collisions and potential deadlocks, as well as improving the traffic throughput. Within the feasible tunnel, a low-level planner (vehicle-based) at each ego vehicle could further adjust its practical trajectory, to avoid potential obstacles.
- To further improve the traffic throughput, we propose a novel space-time resource allocation strategy in high-level planner, by using resource blocks to describe the space and time usage at different vehicles in the intersection. Comparing to the existing collision-set based strategies, this new method shows obvious throughput advantages. Furthermore, we put forward a new performance criterion, resource occupation rate, to guarantee the coordination fairness among different driving maneuvers.
- All planning problems in the proposed coordination framework can be formulated as standard optimization problems, which can be effectively solved by DP and spline-based QP. The proposed coordination problems are validated and evaluated by both simulations and practical experiments, to see obvious performance advantages.

The paper is organized as follows: The intersection model, vehicle kinematic model and structure of the planning

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-03.jpg?height=758&width=771&top_left_y=200&top_left_x=219)
Fig. 1. Graphic model of the intersection coordination system.

framework are presented in Section II. In Section III and Section IV, two strategies, the traditional collision-set strategy and the novel space-time resource allocation strategy, are introduced for the high-level planner. The replanning strategy for the low-level planner is explained in Section V. The simulations and laboratorial experiments are carried out in Section VI and Section VII respectively, for the validation of the proposed framework.

## II. System Model

A. Intersection Model

We consider a typical road intersection which consists of $R$ roads with lane width $\mathcal{W}_{\text {lane }}$ (usually we set $R=4$ ), as shown in Fig. 1. The intersection area can be spatially divided into three main sections. Arrival Area (AA) is where vehicles arrive at the intersection dynamically. In Buffer Area (BA), each arrived vehicle queues up and waits for the coordination. Conflict Area (CA) represents the intersection area where a potential collision may occur.

There also exist three levels of computing units in the intersection. Each vehicle has an ego computing unit for self-planning. In the middle of the intersection, a centralized coordinator (CC) is to receive vehicle information and make coordination decisions. At the side of each road, an edge node (EN) can help reduce the task overload in the CC and provide a low response delay. Multi-access edge computing (MEC) servers have been implemented in all the ENs and CC.

We use queue length $I_{r}$ to indicate the number of vehicles waiting in BA at road $r$. Notations $\mathcal{R}=\{1,2, \ldots, R\}$ and $\mathcal{I}_{r}=\left\{1, \ldots, I_{r}\right\}$ represent the sets of roads and vehicles on the $r$-th road, respectively. Without loss of generality, there are four possible maneuvers when a vehicle passes an intersection, i.e., go straight, turn left, right and U turn.
B. Vehicle Kinematic Model

We adopt the popular kinematic bicycle model [39] for vehicles in this paper. The state parameters of the $i$-th vehicle on road $r$ can be described by $\left[x_{i, r}, y_{i, r}, \theta_{i, r}, v_{i, r}\right]^{\mathrm{T}}$, where $\left(x_{i, r}, y_{i, r}\right), \theta_{i, r}$ and $v_{i, r}$ are position (in Cartesian Coordinates), heading and velocity, respectively. The control inputs are curvature and acceleration $\left[\kappa_{i, r}, a_{i, r}\right]^{\mathrm{T}}$, where $\kappa_{i, r}$ is related to the steering angle $\omega$ by $\kappa \propto \tan (\omega)$ and $a_{i, r}$ is related to the throttle and brake of the vehicle. Therefore, the vehicle kinematic state can be uniquely determined by the control inputs and its initial state, i.e.,

$$
\left[\begin{array}{c}
\dot{x}_{i, r} \\
\dot{y}_{i, r} \\
\dot{\theta}_{i, r} \\
\dot{v}_{i, r}
\end{array}\right]=v_{i, r} \cdot\left[\begin{array}{c}
\cos \left(\theta_{i, r}\right) \\
\sin \left(\theta_{i, r}\right) \\
\kappa_{i, r} \\
0
\end{array}\right]+a_{i, r} \cdot\left[\begin{array}{l}
0 \\
0 \\
0 \\
1
\end{array}\right] r \in \mathcal{R}, \quad i \in \mathcal{I}_{r}
$$

with $(\bullet):=\frac{\partial}{\partial t}(\bullet)$. Two different coordinates including the Cartesian coordinates and Frenét Frame are adopted for trajectory optimization, which can be described as follows.

1) Trajectory in Cartesian Coordinates: In the Cartesian coordinate system, we use three-dimensional Cartesian coordinates $X Y T$ to describe the searching space, where $X Y$ means space domain and $T$ means time domain. Thus, trajectory functions can be expressed as

$$
\left\{\begin{array}{l}
\text { Path: }\left\{\begin{array}{l}
x_{i, r}=f_{i, r}\left(s_{i, r}\right) \\
y_{i, r}=g_{i, r}\left(s_{i, r}\right)
\end{array}\right. \\
\text { Speed Profile: } s_{i, r}=u_{i, r}(t)
\end{array}\right.
$$

with $s$ the arc length of the vehicle along the path. The vehicle controls can be uniquely mapped into the trajectory as follows.

$$
\begin{array}{r}
{\left[f, g, \arctan \left(\frac{g^{\prime}(s)}{f^{\prime}(s)}\right), \frac{\left|f^{\prime}(s) g^{\prime \prime}(s)-f^{\prime \prime}(s) g^{\prime}(s)\right|}{f^{\prime 2}(s)+g^{\prime 2}(s)}, u^{\prime}(t), u^{\prime \prime}(t)\right]^{\mathrm{T}}} \\
=[x, y, \theta, \kappa, v, a]^{\mathrm{T}}
\end{array}
$$

2) Trajectory in Frenét Frame: In the Frenét Frame [40], a reference path is applied to reduce the number of functions that describe vehicle path, by setting $s$ and $l$ domains as the longitudinal and lateral distances a vehicle travels along the reference path, respectively. As a consequence, in the new SLT space, trajectory functions can be expressed as

$$
\begin{cases}\text { Path: } & l_{i, r}=p_{i, r}\left(s_{i, r}\right) \\ \text { Speed Profile: } & s_{i, r}=q_{i, r}(t)\end{cases}
$$

From [40], we know that there are transformations

$$
\left[p(s), q(t), p^{\prime}(s), p^{\prime \prime}(s), q^{\prime}(t), q^{\prime \prime}(t)\right] \mapsto[x, y, \theta, \kappa, v, a]
$$

Therefore, given smooth trajectory functions (2) or (4) for all the vehicles, we can control them via (1), (3) and (5).
C. Structure of the Planning Framework

The planning process could be expressed as follows.

- High-Level Planner (Infrastructure-Based): The ENs receive driving maneuvers and initial states of all the vehicles in BA by V2I communications. Then ENs and CC will generate the reference trajectories and feasible tunnels for vehicles in Cartesian Coordinates.

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-04.jpg?height=387&width=866&top_left_y=204&top_left_x=174)
Fig. 2. Structure of the planning framework.

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-04.jpg?height=404&width=868&top_left_y=713&top_left_x=172)
Fig. 3. Feasible tunnel at each time point.

- Low-Level Planner (Vehicle-Based): Each vehicle first can get its reference trajectory and feasible tunnel from ENs. Within the feasible tunnel, each vehicle will build its practical trajectory based on the reference trajectory, using its on-board sensor observations, to avoid unexpected obstacles.

Definition 1 (Feasible Tunnel): Considering the flexibility requirement of the low-level planner to avoid potential unexpected obstacles such as pedestrians, the high-level planner should leave some extra redundancies for the low-level planner, namely feasible tunnel. As shown in Fig. 3, we can define the boundaries of feasible tunnel at each time point with the longitudinal redundancy $s_{\text {red }}$ and lateral redundancy $l_{\text {red }}$, i.e.

$$
\begin{aligned}
s_{\mathrm{red}} & \geq \mathcal{L}_{\mathrm{car}}+d_{\mathrm{min}}^{\mathrm{s}} \\
l_{\mathrm{red}} & \geq \mathcal{W}_{\mathrm{car}}+d_{\mathrm{min}}^{1}
\end{aligned}
$$

where $\mathcal{L}_{\text {car }}$ and $\mathcal{W}_{\text {car }}$ are the length and width of the vehicle, $d_{\text {min }}^{\mathrm{s}}$ and $d_{\text {min }}^{1}$ are the longitudinal and lateral safe distances [41]. The values of $s_{\text {red }}$ and $l_{\text {red }}$ depends on the obstacle density (e.g. energy map [42]) of statistics in the intersection.

A special case of feasible tunnel is the vehicle platooning, where we only need to focus on the trajectory optimization for the head vehicle of the group in the planning framework. Based on the number of vehicles in the group $n_{\text {platoon }}$, the longitudinal redundancy $s_{\text {red }}$ can be extended as

$$
s_{\text {red }} \geq n_{\text {platoon }} \cdot \mathcal{L}_{\text {car }}+n_{\text {platoon }} \cdot d_{\text {min }}^{\mathrm{s}}
$$

III. High-Level Planner I: Collision-Set Strategy
A. Problem Formulation

In the high-level planner, we only consider vehicles rather than other obstacles in the intersection. The collision-set based strategies of the high-level planner is to give reference trajectories (2) and feasible tunnels $\mathbb{F}_{i, r}^{\text {XYT }}$ for all vehicles in BA from all $R$ roads. There are two main parts in this strategy. Reference path generator aims to give vehicles feasible paths $f_{i, r}(s), g_{i, r}(s)$ for all possible driving maneuvers, while reference speed profile generator coordinates speed profiles $u_{i, r}(t)$ of vehicles to give passing order and improve traffic performance as well.

1) Reference Path Generator: First, we should generate a reference path for each vehicle. One popular reference path is the simplified line \& circle path [24]. However, for practical turning maneuvers (turn left, right and U turn), the line \& circle paths are too ideal to be realized in the kinematic bicycle model (1). Therefore, we need to use smooth optimization to search for a smooth feasible reference path $f(s)$ and $g(s)^{1}$ based on the line \& circle path.

We use cost function $C_{\mathrm{s}, \text { ref }}^{\mathrm{P}}$ to make $\kappa_{i, r}$ continuous and improve the smoothness of the path according to (3), which can be described as

$$
C_{\mathrm{s}, \text { ref }}^{\mathrm{P}}(f, g)=\sum_{z=2}^{3} w_{\mathrm{s}, z}^{\mathrm{P}}\left[\int\left(f^{(z)}\right)^{2}(s) \mathrm{d} s+\int\left(g^{(z)}\right)^{2}(s) \mathrm{d} s\right]
$$

For keeping the behavior of each vehicle not to change heavily, we need to limit the search space of the optimization near the line \& circle path. Thus, we segment the total distance of the line \& circle path at interval $\Delta s_{\mathrm{a}}$, for getting $n_{\mathrm{a}}+1$ anchor points $\left\{\left(x_{\mathrm{a}, j}, y_{\mathrm{a}, j}, s_{\mathrm{a}, j}\right) \mid j=0,1, \ldots, n_{\mathrm{a}}\right\}$. We let

$$
\begin{aligned}
\left|f\left(s_{\mathrm{a}, j}\right)-x_{\mathrm{a}, j}\right| & \leq \varepsilon \\
\left|g\left(s_{\mathrm{a}, j}\right)-y_{\mathrm{a}, j}\right| & \leq \varepsilon
\end{aligned}
$$

where $\varepsilon$ is the maximum allowable offset in both $X$ and $Y$ domains.

Otherwise, the path of each vehicle should match the initial state at the start and point, i.e.,

$$
\begin{aligned}
f^{(\gamma)}\left(s_{0}\right)=x_{0}^{(\gamma)}, & g^{(\gamma)}\left(s_{0}\right)=y_{0}^{(\gamma)}, \quad \gamma=0,1,2 \\
f^{(\gamma)}\left(s_{\text {end }}\right)=x_{\text {end }}^{(\gamma)}, & g^{(\gamma)}\left(s_{\text {end }}\right)=y_{\text {end }}^{(\gamma)}, \quad \gamma=0,1,2
\end{aligned}
$$

Therefore, the smooth optimization in the reference path generator is shown as follows

$$
\begin{aligned}
\mathscr{P}_{1}: & \min _{f, g} . \\
& C_{\mathrm{s}, \text { ref }}^{\mathrm{P}}(f, g) \\
\text { s.t. } & (10)-(13)
\end{aligned}
$$

which can be solved by spline-based QP in Appendix A.
2) Reference Speed Profile Generator: After the path of each vehicle is predefined, the reference speed profile generator is to coordinate and find feasible speed profile functions $u_{i, r}(t)$ for all vehicles in BA.

For avoiding collisions between vehicles, the area of CA can be regarded as a collision set and we should ensure that only one vehicle can occupy CA simultaneously. Based on the reference path $f_{i, r}\left(s_{i, r}\right), g_{i, r}\left(s_{i, r}\right)$, the distances when each vehicle entering and leaving CA can be obtained and defined

[^0]as $s_{i, r}^{\mathrm{L}}$ and $s_{i, r}^{\mathrm{H}}$. Therefore, any two vehicles' occupation times in CA should not be overlapped, which can be expressed as
$$
\begin{aligned}
& {\left[u_{i_{1}, r_{1}}^{-1}\left(s_{i_{1}, r_{1}}^{\mathrm{L}}-\frac{s_{\text {red }}}{2}\right) u_{i_{1}, r_{1}}^{-1}\left(s_{i_{1}, r_{1}}^{\mathrm{H}}+\frac{s_{\text {red }}}{2}\right)\right]} \\
& \cap\left[u_{i_{2}, r_{2}}^{-1}\left(s_{i_{2}, r_{2}}^{\mathrm{L}}-\frac{s_{\text {red }}}{2}\right) u_{i_{2}, r_{2}}^{-1}\left(s_{i_{2}, r_{2}}^{\mathrm{H}}+\frac{s_{\text {red }}}{2}\right)\right]=\varnothing
\end{aligned}
$$
with $r_{1}, r_{2} \in \mathcal{R}, i_{1} \in \mathcal{I}_{r_{1}}$ and $i_{2} \in \mathcal{I}_{r_{2}}$.
Furthermore, the queue length of each road is time-varying due to the dynamic arrival of vehicles. We should ensure that all the queues in the intersection are stable [43], i.e.,
$$
\lim _{T \rightarrow \infty} \sup \frac{1}{T} \sum_{t=1}^{T} E\left[I_{r}(t)\right]<\infty, \quad r \in \mathcal{R}
$$
where sup means the upper bound, $I_{r}(t)$ is the queue length on road $r$.

Other constraints for coordination are represented as

$$
\begin{aligned}
0 & \leq u_{i, r}^{\prime}(t) \leq v_{i, r \text { max }} \\
a_{i, r \text { min }} & \leq u_{i, r}^{\prime \prime}(t) \leq a_{i, r \text { max }} \\
u_{i, r}^{(\gamma)}\left(t_{0}\right) & =s_{0}^{(\gamma)}, \quad \gamma=0,1,2
\end{aligned}
$$

Constraints (16) - (17) are limitations for velocity and acceleration. Otherwise, backing maneuvers is forbad based on (16) by keeping the monotonicity of the speed profile. (18) is a constraint based on the initial state.

The cost function of reference speed profile generator includes two parts. The first part $C_{\mathrm{p}, \text { ref }}^{\mathrm{S}}$ is for the coordination performance, by comparing the vehicle velocity $u_{i, r}^{\prime}(t)$ with $v_{\text {eff }}$, since each vehicle has a velocity $v_{\text {eff }}$ for providing the optimal fuel consumption [4] or the optimal passing throughput [18], which can achieve high efficiency. The second part $C_{\text {s,ref }}^{\mathrm{S}}$ is for keeping $a_{i, r}$ continuous and improving the smoothness of the speed profile, which is for vehicle comfort.

$$
\begin{aligned}
& C_{\mathrm{p}, \text { ref }}^{\mathrm{S}}\left(u_{i, r}\right)=w_{\mathrm{p}}^{\mathrm{S}} \int\left(u_{i, r}^{\prime}(t)-v_{\text {eff }}\right)^{2} \mathrm{~d} t \\
& C_{\mathrm{s}, \text { ref }}^{\mathrm{S}}\left(u_{i, r}\right)=\sum_{z=2}^{3}\left[w_{\mathrm{s}, z}^{\mathrm{S}} \int\left(u_{i, r}^{(z)}\right)^{2}(t) \mathrm{d} t\right]
\end{aligned}
$$

In some scenarios, to further improve the passenger comfort, we can also add a Yaw Rate cost in the optimization, which can avoid rapid changes of direction. See in Appendix B.

Therefore, the coordination in the reference speed profile generator can be described as

$$
\mathscr{P}_{2}: \min _{u_{i, r}} . \sum_{r=1}^{R} \sum_{i=1}^{I_{r}}\left[C_{\mathrm{p}, \text { ref }}^{\mathrm{S}}\left(u_{i, r}\right)+C_{\mathrm{s}, \text { ref }}^{\mathrm{S}}\left(u_{i, r}\right)\right]
$$

Since constraint (14) is essentially NP-hard for considering all the vehicles in the intersection, and constraint (15) is nonconvex, solving $\mathscr{P}_{2}$ is challenging.
3) Feasible Tunnel: After the reference path and speed profile generators, we can obtain the reference trajectories $f_{i, r}(s), g_{i, r}(s), u_{i, r}(t), r \in \mathcal{R}, i \in \mathcal{I}_{r}$ from $\mathscr{P}_{1}$ and $\mathscr{P}_{2}$.

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-05.jpg?height=359&width=870&top_left_y=200&top_left_x=1085)
Fig. 4. Round-based decision (round $k$ ).

Therefore, the feasible tunnel for each vehicle is describe as $\mathbb{F}_{i, r}^{\mathrm{XYT}}$

$$
=\left\{(x, y, t) \left\lvert\, \begin{array}{c}
\sqrt{\left[x-f_{i, r}\left(s_{\perp}\right)\right]^{2}+\left[y-g_{i, r}\left(s_{\perp}\right)\right]^{2}}<\frac{l_{\mathrm{red}}}{2} \\
u_{i, r}(t)-\frac{s_{\mathrm{red}}}{2} \leq s_{\perp} \leq u_{i, r}(t)+\frac{s_{\mathrm{red}}}{2}
\end{array}\right.\right\}
$$

where $\left[f\left(s_{\perp}\right), g\left(s_{\perp}\right)\right]$ is the perpendicular projection point of $(x, y)$ onto the reference path.

## B. Problem Decomposition

Because the dynamic problem $\mathscr{P}_{2}$ is non-convex and computation-intensive, we divide the dynamic optimization problem into a series of sub-static problems with round based decisions. As shown in Fig. 4, in each round, (i) we determine the reference trajectory and feasible tunnel for the first vehicle in each road, and then (ii) we decide the optimal road to occupy the intersection. $k$ denotes the number of rounds.

1) Single-Road Planning: On each road, the vehicles will be served using first input first output (FIFO) strategy, which means we always focus on getting the reference trajectory $f_{1, r}(s), g_{1, r}(s), u_{1, r}(t)$ for the first vehicle on the road. Otherwise, this part can be offloaded into EN at the side of each road, which can improve computational efficiency.

First, we need to solve $\mathscr{P}_{1}$ to get the reference path $f_{1, r}(s), g_{1, r}(s)$ of the vehicle. Then, in reference speed profile generator, constraint (14) can be easily rewritten as an affine one, i.e.,

$$
t_{k-1}^{\mathrm{H}} \leq u_{1, r}^{-1}\left(s_{1, r}^{\mathrm{L}}-\frac{s_{\mathrm{red}}}{2}\right)
$$

where $t_{k-1}^{\mathrm{H}}$ denotes the leaving time from the previous round coordination (round $k-1$ ). Therefore, $\mathscr{P}_{2}$ on each road can be simplified as

$$
\begin{aligned}
\mathscr{P}_{3}: & \min _{u_{1, r}} . \quad C_{\mathrm{p}, \text { ref }}^{\mathrm{S}}\left(u_{1, r}\right)+C_{\mathrm{s}, \text { ref }}^{\mathrm{S}}\left(u_{1, r}\right) \\
& \text { s.t. } \quad(16)-(18),(22)
\end{aligned}
$$

which can be solved by spline-based QP in Appendix A.
2) Multiple-Road Decision: After solving the single road planning on all $R$ roads, CC needs to decide the optimal road to occupy the intersection. We have two performance criteria for the decision, i.e.,

$$
\begin{aligned}
P_{\mathrm{th}} & =w_{\mathrm{th}} \cdot \frac{u_{1, r}^{-1}\left(s_{1, r}^{\mathrm{end}}+\frac{s_{\mathrm{red}}}{2}\right)}{n_{\mathrm{car}}+1} \\
P_{\mathrm{sta}} & =-w_{\mathrm{sta}} \cdot I_{r}(t) a_{r}^{\mathrm{av}}
\end{aligned}
$$

where $n_{\text {car }}$ refers to the number of previous passing car, $a_{r}^{\text {av }}$ is the average coordinate rate. The first part $P_{\mathrm{th}}$ is for improving the traffic throughput, by minimizing the average passing time of the vehicles. The second part $P_{\text {sta }}$ is for the queue stability based on constraint (15), by using Rate Stability Theorem and Lyapunov Theorem for simplification [18].

Therefore, we can select the optimal road $\hat{r}$ to pass the intersection, based on

$$
\hat{r}=\arg \min \left\{P_{\text {th }}+P_{\text {sta }}\right\}
$$

The process and details of high-level planner I are given in Algorithm 1.

```
Algorithm 1 High-Level Planner I
    Initialization. Set initial vehicles \(\forall r \in \mathcal{R}, \forall i \in \mathcal{I}_{r}\) and the
    vehicle arrival rate, set \(k=1, t_{k-1}^{\mathrm{H}}=0\).
    repeat
        ENs get the initial states \(x_{0}^{(\gamma)}, y_{0}^{(\gamma)}, s_{0}^{(\gamma)}\) and driving
        maneuvers of vehicles in BA
        for each \(r \in[1, R]\) do
            Solve the single-road planning problem \(\mathscr{P}_{1}\) and \(\mathscr{P}_{3}\)
            for the first vehicle on the road.
            Output: Reference trajectory \(f_{1, r}(s), g_{1, r}(s), u_{1, r}(t)\)
            and feasible tunnel \(\mathbb{F}_{1, r}^{\mathrm{XYT}}\).
        end for
        According to (25), CC select the optimal road \(\hat{r}\).
        The first vehicle on road \(\hat{r}\) gets instructions \(f_{1, \hat{r}}(s)\),
        \(g_{1, \hat{r}}(s), u_{1, \hat{r}}(t), \mathbb{F}_{1, \hat{r}}^{\mathrm{XYT}}\), and passes the intersection using
        its low-level planner.
        The second vehicle on road \(\hat{r}\) replaces the first vehicle
        \(i=i-1, i \in \mathcal{I}_{\hat{r}}\).
        Update the leaving time from the previous round coor-
        dination
            \(t_{k-1}^{\mathrm{H}}=u_{1, \hat{r}}^{-1}\left(s_{1, \hat{r}}^{\mathrm{H}}+\frac{s_{\text {red }}}{2}\right)\)
        \(k=k+1\).
    until the coordination process is finished.
```


## IV. High-Level Planner II: Space-Time Resource Allocation Strategy

## A. Problem Formulation

In Section III, the collision-set strategy only allows one vehicle to occupy the entire intersection simultaneously, so the collision set is as large as the intersection, which will waste some resources in spatial domain. One solution to further improve the traffic throughput is increasing the number of collision sets in the intersection [18]. However, this multicollision-set based solution is based on pre-specified paths and leaves no space for feasible tunnels, which is not suitable for the proposed double-level coordination framework.

In this section, we propose a novel space-time resource allocation strategy to improve traffic efficiency in high-level planner. In the strategy, the space and time resources in the intersection can be regarded as a three dimensional coordinates with $X, Y$ and $T$ domains. As shown in Fig. 5, to describe

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-06.jpg?height=365&width=857&top_left_y=202&top_left_x=1087)
Fig. 5. XYT coordinates and resource blocks in the intersection.

the feasible resources, we divide the coordinates into multiple small resource blocks with $d x$ in length, $d y$ in width and $d t$ in height. Each resource block can be represented as

$$
\mathbb{B}_{j_{x}, j_{y}, j_{t}}^{\mathrm{XYT}}=\left\{\begin{array}{l|l}
\left(j_{x}-1\right) \cdot d x \leq x<j_{x} \cdot d x \\
\left(j_{y}-1\right) \cdot d y \leq y<j_{y} \cdot d y \\
\left(j_{t}-1\right) \cdot d t \leq t<j_{t} \cdot d t
\end{array}\right\}
$$

where $\left(j_{x}, j_{y}, j_{t}\right)$ is the index of the resource block. The coordination strategy is not only to generate reference trajectories but also to allocate resource blocks to different vehicles.

The allocated area for each vehicle can be represented as a collection of resource blocks, i.e.,

$$
\mathbb{A}_{i, r}^{\mathrm{XYT}}=\bigcup_{\left(j_{x}, j_{y}, j_{t}\right) \in \mathcal{A}_{i, r}^{\mathrm{XYT}}} \mathbb{B}_{j_{x}, j_{y}, j_{t}}^{\mathrm{XYT}}
$$

where $\mathcal{A}_{i, r}^{\mathrm{XYT}}$ is the set of resource block indexes. Therefore, for avoiding collisions between vehicles, we should ensure that each resource block can only be allocated to one vehicle. That means, any two vehicles' allocated areas should not be overlapped, i.e.,

$$
\mathbb{A}_{i_{1}, r_{1}}^{\mathrm{XYT}} \cap \mathbb{A}_{i_{2}, r_{2}}^{\mathrm{XYT}}=\varnothing
$$

with $r_{1}, r_{2} \in \mathcal{R}, i_{1} \in \mathcal{I}_{r_{1}}$ and $i_{2} \in \mathcal{I}_{r_{2}}$. Similarly, constraint (29) is NP-hard and we also need to decompose the optimization problem $\mathscr{P}_{2}$ with (29) into round-based planning and decision.

## B. Single-Road Planning (at ENs)

At round $k$, EN in each road first need to get the resource indexes $\mathcal{A}_{\text {pre }}^{\text {XYT }}$ which have been occupied in previous $1 \sim(k-$ 1) rounds. Thus, the previous occupied area at the intersection can be described as

$$
\mathbb{A}_{\text {pre }}^{\text {XYT }}=\bigcup_{\left(j_{x}, j_{y}, j_{t}\right) \in \mathcal{A}_{\text {pre }}^{\text {XYT }}} \mathbb{B}_{j_{x}, j_{y}, j_{t}}^{\text {XYT }}
$$

Then, we focus on planning the optimal reference trajectory and allocating the space-time resources for the first vehicle on the road. By solving $\mathscr{P}_{1}$, we can get the reference path function $f_{1, r}(s)$ and $g_{1, r}(s)$. After that, we can obtain the feasible tunnel in XY version for the vehicle, which can be described as

$$
\mathbb{F}_{1, r}^{\mathrm{XY}}=\left\{(x, y) \left\lvert\, \sqrt{\left[x-f_{1, r}\left(s_{\perp}\right)\right]^{2}+\left[y-g_{1, r}\left(s_{\perp}\right)\right]^{2}}<\frac{l_{\mathrm{red}}}{2}\right.\right\}
$$

where $\left[f\left(s_{\perp}\right), g\left(s_{\perp}\right)\right]$ is the perpendicular projection point of $(x, y)$ onto the reference path. Therefore, we should only focus on the previous occupied resource blocks within $\mathbb{F}_{1, r}^{\mathrm{XY}}$, which can be represented as a new index matrix $\mathcal{A}_{\text {pre }}^{\mathrm{XYT}^{\prime}}$

$$
\mathcal{A}_{\mathrm{pre}}^{\mathrm{XYT}}{ }^{\prime}=\left\{\begin{array}{l|l}
\left(j_{x}, j_{y}, j_{t}\right) & \begin{array}{c}
\left(j_{x}, j_{y}, j_{t}\right) \in \mathcal{A}_{\mathrm{pre}}^{\mathrm{XYT}} \\
\mathbb{B}_{j_{x}, j_{y}, j_{t}}^{\mathrm{XYT}} \cap \mathbb{F}_{1, r}^{\mathrm{XY}} \neq \varnothing
\end{array}
\end{array}\right\}
$$

Considering the planning task for reference speed profile $u_{1, r}(t)$, the previous occupied area should be mapped into ST coordinates. We use interval $d s$ to sample on the reference path, so the occupied area in ST coordinates is described as

$$
\mathbb{A}_{\text {pre }}^{\mathrm{ST}}=\bigcup_{\left(j_{s}, j_{t}\right) \in \mathcal{A}_{\text {pre }}^{\mathrm{ST}}} \mathbb{B}_{j_{s}, j_{t}}^{\mathrm{ST}}
$$

with

$$
\begin{aligned}
\mathbb{B}_{j_{s}, j_{t}}^{\mathrm{ST}} & =\left\{\begin{array}{l|l}
(s, t) & \begin{array}{l}
\left(j_{s}-1\right) \cdot d s \leq s \leq j_{s} \cdot d s \\
\left(j_{t}-1\right) \cdot d t \leq t \leq j_{t} \cdot d t
\end{array}
\end{array}\right\} \\
\mathcal{A}_{\mathrm{pre}}^{\mathrm{ST}} & =\left\{\begin{array}{l|l}
\left(j_{s}, j_{t}\right) & \begin{array}{c}
\left(j_{x}, j_{y}, j_{t}\right) \in \mathcal{A}_{\mathrm{pre}}^{\mathrm{XYT}} \\
\left(j_{s}-1\right) \cdot d s \leq s_{\perp}^{\prime} \leq j_{s} \cdot d s
\end{array}
\end{array}\right\}
\end{aligned}
$$

where $\left[\left(j_{x} \cdot d x-\frac{d x}{2}\right),\left(j_{y} \cdot d y-\frac{d y}{2}\right),\left(j_{t} \cdot d t-\frac{d t}{2}\right)\right]$ is the central point of the resource block, $\left[f\left(s_{\perp}^{\prime}\right), g\left(s_{\perp}^{\prime}\right)\right]$ is the perpendicular projection point of $\left[\left(j_{x} \cdot d x-\frac{d x}{2}\right),\left(j_{y} \cdot d y-\frac{d y}{2}\right)\right]$ onto the reference path.

Constraint (29) can be translated into a new cost function $C_{\mathrm{c}, \text { ref }}^{\mathrm{S}}$ to avoid double allocation of each resource block, by comparing the distance between previous occupied resource blocks in ST version and the reference speed profile, i.e.,

$$
\begin{aligned}
& C_{\mathrm{c}, \text { ref }}^{\mathrm{S}}\left(u_{1, r}\right) \\
& \quad=\sum_{\left(j_{s}, j_{t}\right) \in \mathcal{A}_{\text {pre }}^{\mathrm{ST}}}\left\{\begin{array}{l}
\operatorname{Inf}\left\{\begin{array}{l}
\left(j_{t}-1\right) \cdot d t \leq t \leq j_{t} \cdot d t \\
\text { and } \\
\left|u_{1, r}(t)-\left(j_{s} \cdot d s-\frac{d s}{2}\right)\right|-\frac{d s}{2} \leq \frac{s_{\text {red }}}{2}
\end{array}\right. \\
0 \text { else }
\end{array}\right.
\end{aligned}
$$

Therefore, the optimization for reference speed profile can be represented as

$$
\begin{aligned}
\mathscr{P}_{4}: & \min _{u_{1, r}} . C_{\mathrm{p}, \text { ref }}^{\mathrm{S}}\left(u_{1, r}\right)+C_{\mathrm{s}, \text { ref }}^{\mathrm{S}}\left(u_{1, r}\right)+C_{\mathrm{c}, \text { ref }}^{\mathrm{S}}\left(u_{1, r}\right) \\
& \text { s.t. }(16)-(18)
\end{aligned}
$$

Since $C_{\mathrm{c}, \text { ref }}^{\mathrm{S}}$ is not a convex cost function, we need to use both DP and spline-based QP to solve $\mathscr{P}_{4}$. Details of the proposed solver can also be found in Appendix A.

After getting the reference trajectory, we can obtain the feasible tunnel in XYT version $\mathbb{F}_{1, r}^{\text {XYT }}$ for the vehicle, based on (21). Then the allocated area $\mathbb{A}_{1, r}^{\mathrm{XYT}}$ for vehicle can also be expressed based on (28) and block indexes $\mathcal{A}_{1, r}^{\mathrm{XYT}}$

$$
\mathcal{A}_{1, r}^{\mathrm{XYT}}=\left\{\left(j_{x}, j_{y}, j_{t}\right) \mid \mathbb{B}_{j_{x}, j_{y}, j_{t}}^{\mathrm{XYT}} \bigcap \mathbb{F}_{1, r}^{\mathrm{XYT}} \neq \varnothing\right\}
$$

## C. Multiple-Road Decision (at CC)

In the space-time resource allocation strategy, the multiple-road decision in CC also focuses on traffic throughput $P_{\text {th }}$ and queue stability $P_{\text {sta }}$ (24). Based on the allocated resource blocks, $P_{\mathrm{th}}$ can be rewritten as

$$
P_{\mathrm{th}}=w_{\mathrm{th}} \cdot \frac{\max \left\{j_{t} \mid j_{t} \in\left(\mathcal{A}_{1, r}^{\mathrm{XYT}} \cup \mathcal{A}_{\mathrm{pre}}^{\mathrm{XYT}}\right)\right\} \cdot d t}{n_{\mathrm{car}}+1}
$$

However, $P_{\mathrm{th}}$ and $P_{\text {sta }}$ are not enough for the multi-vehicle scenario. There exists a special situation, as shown in Fig. 8(a). Because the travel distances of 4 driving maneuvers are different (turn right < U turn < go straight < turn left), the maneuver with shorter travel distances is more likely to win the competition in this decision approach, that may lead to unexpected unfairness. If a road has a large number of vehicles with long-distance maneuver requests, resources in this road will not be allocated for a long time.

To guarantee the fairness between different driving maneuvers, we propose a novel performance criterion, resource occupation rate $P_{\mathrm{occ}}$, which refers to the ratio of occupied resource blocks to total available resource blocks, i.e.

$$
\begin{aligned}
P_{\mathrm{occ}}= & w_{\mathrm{occ}} \cdot \frac{N_{\text {occupy }}}{N_{\text {available }}} \\
= & w_{\mathrm{occ}} \\
& \cdot \frac{\operatorname{card}\left(\mathcal{A}_{\mathrm{pre}}^{\mathrm{XYT}}\right)+\operatorname{card}\left(\mathcal{A}_{1, r}^{\mathrm{XYT}}\right)}{\frac{x_{\max }}{d x} \cdot \frac{y_{\max }}{d x} \cdot \max \left\{j_{t} \mid j_{t} \in\left(\mathcal{A}_{1, r}^{\mathrm{XYT}} \cup \mathcal{A}_{\mathrm{pre}}^{\mathrm{XYT}}\right)\right\}-N_{\mathrm{un}}}
\end{aligned}
$$

where $\operatorname{card}(\cdot)$ means the number of set elements, $N_{\text {un }}$ is the unavailable area based on the road boundaries. Improving the resource occupation rate can help to enhance the fit between vehicle occupancy and previous occupancy of resource blocks. It can avoid situations where a resource area in the intersection remains unused for a long period of time.

We can select the optimal road $\hat{r}$ to pass the intersection, based on

$$
\hat{r}=\arg \min \left\{P_{\mathrm{th}}+P_{\mathrm{sta}}-P_{\mathrm{occ}}\right\}
$$

The process and details of high-level planner II are given in Algorithm 2.

## V. Low-Level Planner: Ego Planning Strategy

In real intersections, in addition to autonomous vehicles, there may exist various random obstacles such as pedestrians, bicycles and human-driving cars, which cannot be accurately tracked or predicted in time by road infrastructures. Therefore, vehicles need to use their on-board sensors to further observe the environment and use low-level planner to replan for their practical trajectory, based on the results from high-level planner in Section III or IV. Significantly, due to the limited perception range of most vehicle-mounted sensors, we assume a circular perception field for each vehicle. Thus, the ego planning strategy in the low-level planner should be done iteratively with a replanning interval $\Delta t$, to handle the oncoming obstacles to the perception field.

TABLE I
Cost Functions for Low-Level Planner
| Impact | Path Planning | Speed Profile Planning |
| :--- | :--- | :--- |
| smoothness | $C_{\mathrm{s}}^{\mathrm{P}}(p)=\sum_{z=2}^{3}\left[w_{\mathrm{s}, z}^{\mathrm{P}} \int\left(p^{(z)}\right)^{2}(s) \mathrm{d} s\right]$ | $C_{\mathrm{s}}^{\mathrm{S}}(q)=\sum_{z=2}^{3}\left[w_{\mathrm{s}, z}^{\mathrm{S}} \int\left(q^{(z)}\right)^{2}(t) \mathrm{d} t\right]$ |
| vehicle behavior | $C_{\mathrm{b}}^{\mathrm{P}}(p)=w_{\mathrm{b}}^{\mathrm{P}} \int p^{2}(s) \mathrm{d} s$ | $C_{\mathrm{b}}^{\mathrm{S}}(q)=w_{\mathrm{b}}^{\mathrm{S}} \int(q(t)-u(t))^{2} \mathrm{~d} t$ |
| collision avoidance | $C_{\mathrm{c}}^{\mathrm{P}}(p)=\sum_{j=1}^{N_{\mathrm{ob}}} \begin{cases}\operatorname{Inf} & d_{j}^{\mathrm{s}}<d_{\text {min }}^{\mathrm{s}} \& d_{j}^{\mathrm{l}}<d_{\text {min }}^{\mathrm{l}} \\ 0 & \text { else }\end{cases}$ | $C_{\mathrm{c}}^{\mathrm{s}}(q)=\sum_{j=1}^{N_{\mathrm{ob}}} \begin{cases}\operatorname{Inf} & d_{j}^{\mathrm{s}}<d_{\min }^{\mathrm{s}} \\ 0 & \text { else }\end{cases}$ |


```
Algorithm 2 High-Level Planner II
    Initialization. Set initial vehicles \(\forall r \in \mathcal{R}, \forall i \in \mathcal{I}_{r}\) and the
    vehicle arrival rate, set \(k=1, \mathcal{A}_{\text {pre }}^{\mathrm{XYT}}=0\).
    repeat
        ENs get the initial states \(x_{0}^{(\gamma)}, y_{0}^{(\gamma)}, s_{0}^{(\gamma)}\) and driving
        maneuvers of vehicles in BA
        for each \(r \in[1, R]\) do
            Solve the single-road reference path planning \(\mathscr{P}_{1}\) for
            the first vehicle on the road.
            Output: Reference path \(f_{1, r}(s), g_{1, r}(s)\) and feasible
            tunnel in XY version \(\mathbb{F}_{1, r}^{\mathrm{XY}}\).
            Based on \(\mathcal{A}_{\text {pre }}^{\text {XYT }}\), find a new index matrix \(\mathcal{A}_{\text {pre }}^{\text {XYT' }}\) of
            previous occupied blocks within \(\mathbb{F}_{1, r}^{\mathrm{XY}}\).
            Map the \(\mathcal{A}_{\text {pre }}^{\mathrm{XYT}^{\prime}}\) into ST coordinates, for getting \(\mathcal{A}_{\text {pre }}^{\mathrm{ST}}\)
            Solve the single-road reference speed profile planning
            \(\mathscr{P}_{4}\) for the first vehicle on the road.
            Output: Reference speed profile \(u_{1, r}(t)\), feasible
            tunnel in XYT version \(\mathbb{F}_{1, r}^{\text {XYT }}\) and allocated resource
            block indexes \(\mathcal{A}_{1, r}^{\mathrm{XYT}}\) for the vehicle.
        end for
        According to (40), CC select the optimal road \(\hat{r}\).
        The first vehicle on road \(\hat{r}\) gets instructions \(f_{1, \hat{r}}(s)\),
        \(g_{1, \hat{r}}(s), u_{1, \hat{r}}(t), \mathbb{F}_{1, \hat{r}}^{\mathrm{XYT}}\), and passes the intersection using
        its low-level planner.
        The second vehicle on road \(\hat{r}\) replaces the first vehicle
        \(i=i-1, i \in \mathcal{I}_{\hat{r}}\).
        Update the previous occupied resource blocks
                \(\mathcal{A}_{\text {pre,new }}^{\mathrm{XYT}}=\mathcal{A}_{\text {pre }}^{\mathrm{XYT}} \cup \mathcal{A}_{1, \hat{r}}^{\mathrm{XYT}}\)
        \(k=k+1\).
    until the coordination process is finished.
```

- For static obstacles, the positions will be projected directly based on Cartesian-Frenét transformation.
- For dynamic obstacles, we need to translate the dynamic collision regions into static expected collision regions. Specifically, the estimated positions of dynamic obstacles and ego vehicle at each time point can be evaluated based on the predictive obstacle moving trajectory and previous cycle planning trajectory, respectively. Then, the overlaps of dynamic obstacles and vehicle at each time point will be regarded as the expected collision regions and mapped into SL coordinates.

The cost functions are given in Table I. $C_{\mathrm{s}}$ refers to the smoothness of the trajectory for improving the passenger comfort. $C_{\mathrm{b}}$ is the difference between trajectory and reference trajectory for keeping the vehicle behavior. $C_{\mathrm{c}}$ compares the distances $d^{\mathrm{s}}, d^{\mathrm{l}}$ and the safe distances $d_{\text {min }}^{\mathrm{s}}, d_{\text {min }}^{\mathrm{l}}$ between vehicle and $N_{\mathrm{ob}}$ obstacles from both longitudinal and lateral directions, for collision avoidance.

Therefore, the path planning problem can be described as

$$
\begin{array}{ll}
\mathscr{P}_{5}: \min _{p} . & C_{\mathrm{s}}^{\mathrm{P}}(p)+C_{\mathrm{b}}^{\mathrm{P}}(p)+C_{\mathrm{c}}^{\mathrm{P}}(p) \\
\text { s.t. } & p(s)+\delta p^{\prime}(s) \geq-\left(\frac{l_{\text {red }}}{2}-\frac{\mathcal{W}_{\text {car }}}{2}-\frac{d_{\text {min }}^{1}}{2}\right) \\
& p(s)+\delta p^{\prime}(s) \leq \frac{l_{\text {red }}}{2}-\frac{\mathcal{W}_{\text {car }}}{2}-\frac{d_{\text {min }}^{1}}{2} \\
& p^{(\gamma)}\left(s_{0}\right)=l_{0}^{(\gamma)}, \quad p^{(\gamma)}\left(s_{\text {end }}\right)=l_{\text {end }}^{(\gamma)}
\end{array}
$$

with $\gamma=0,1,2$. Constraints (42) and (43) are to keep the path within the feasible tunnel, and $\delta p^{\prime}(s)$ is the offset considering vehicle heading under kinematic bicycle model [33]. The path optimization $\mathscr{P}_{5}$ can be solved by DP and spline-based QP in Appendix A to get the optimal path function $p(s)$.

Based on the generated path profile, obstacles can be evaluated on ST coordinates, by finding the overlap regions between the planned path and predictive obstacle trajectories. Thus, the speed profile planning problem can be given by

$$
\begin{aligned}
\mathscr{P}_{6}: \min _{q} . & C_{\mathrm{s}}^{\mathrm{S}}(q)+C_{\mathrm{b}}^{\mathrm{S}}(q)+C_{\mathrm{c}}^{\mathrm{S}}(q) \\
\text { s.t. } & q(t) \geq u(t)-\left(\frac{S_{\mathrm{red}}}{2}-\frac{\mathcal{L}_{\mathrm{car}}}{2}-\frac{d_{\mathrm{min}}^{\mathrm{s}}}{2}\right) \\
& q(t) \leq u(t)+\left(\frac{S_{\mathrm{red}}}{2}-\frac{\mathcal{L}_{\mathrm{car}}}{2}-\frac{d_{\mathrm{min}}^{\mathrm{s}}}{2}\right) \\
& (16)-(18)
\end{aligned}
$$

where $u_{i, r}$ is replaced with $q$ in (16) - (18). Constraints (45) and (46) is to keep the speed profile within the feasible tunnel. The speed profile optimization $\mathscr{P}_{6}$ can also be solved by DP and spline-based QP in Appendix A to get the optimal speed profile function $q(t)$.

The details of low-level planner are given in Algorithm 3.
Considering a rare case in low-level planner, if both $\mathscr{P}_{5}$ and $\mathscr{P}_{6}$ cannot find a solution within the feasible tunnel, constraints (45) - (46) in $\mathscr{P}_{6}$ should be removed on this vehicle. The new $\mathscr{P}_{6}$ will give a solution of safe stop outside the feasible tunnel. From then on, this vehicle will no longer follow the high-level instructions, and it becomes a self-driven vehicle operated totally by the low-level planner. For other vehicles in the intersection, they will regard this self-driven vehicle as a dynamic "passive" obstacle and avoid it using their own observations in low-level planners [44].

```
Algorithm 3 Low-Level Planner on Each Vehicle
    Initialization. Set initial state \(l_{0}^{(\gamma)}, s_{0}^{(\gamma)}\) and driving maneu-
    ver of the vehicle.
    Get reference trajectory \(f(s), g(s), u(t)\) and feasible tunnel
    \(\mathbb{F}^{\mathrm{XYT}}\) from high-level planner.
    Build Frenét Frame based on reference path \(f(s), g(s)\).
    for \(t_{0}=0: \Delta t: T_{\text {max }}\) do
        Observe and track all \(N_{\mathrm{ob}}\) obstacles in the perception
        field, and predict trajectories for the dynamic ones.
        Map \(N_{\mathrm{ob}}\) obstacles on the SL coordinates.
        Solve the path planning problem \(\mathscr{P}_{5}\).
        Output: Practical path function \(p(s)\).
        Map \(N_{\mathrm{ob}}\) obstacles on the ST coordinates, according to
        the new planned path \(p(s)\).
        Solve the speed profile planning problem \(\mathscr{P}_{6}\).
        Output: Practical speed profile function \(q(t)\).
        Control the vehicle during \(\Delta t\) period, through (3) based
        on \(p(s), q(t)\).
        Update the initial state of the vehicle.
            \(s_{0}^{(\gamma)}=q^{(\gamma)}\left(t_{0}+\Delta t\right), \quad l_{0}^{(\gamma)}=p^{(\gamma)}\left(q\left(t_{0}+\Delta t\right)\right)\)
    end for
```


## VI. Simulations Results

In this part, four roads are considered in a typical traffic intersection and we use Road $r,(r=1,2,3,4)$ to describe different roads, the same as Fig. 1. The settings of planning parameters are shown in Table II.

## A. High-Level Planner

1) High-Level Planner I: For the collision-set strategy, Fig. 6(a) shows the reference paths for all 4 driving maneuvers in Road 1, which are also the same in Road 2, 3, 4. Comparing to simplified line \& circle paths, the smooth optimization improves the feasibility and smoothness of the reference paths. In Fig. 6(b), we show the coordination of the vehicle reference speed profiles. All 4 vehicles from different roads are allowed to pass the intersection consecutively. At any time, only one

TABLE II
Calibration of Main Parameters
| Parameters | Value | Parameters | Value |
| :--- | :--- | :--- | :--- |
| $v_{\text {min }}, v_{\text {max }}$ | $-20 \mathrm{~m} / \mathrm{s}, 20 \mathrm{~m} / \mathrm{s}$ | $\mathcal{W}_{\text {car }}, \mathcal{L}_{\text {car }}$ | $4 \mathrm{~m}, 2 \mathrm{~m}$ |
| $a_{\text {min }}, a_{\text {max }}$ | $-5 \mathrm{~m} / \mathrm{s}^{2}, 5 \mathrm{~m} / \mathrm{s}^{2}$ | $d_{\text {min }}^{\mathrm{s}}, d_{\text {min }}^{\mathrm{l}}$ | 2m, 1m |
| $v_{\text {eff }}$ | $10 \mathrm{~m} / \mathrm{s}$ | $s_{\text {red }}, l_{\text {red }}$ | 12m, 4m |
| $\Delta s_{\mathrm{a}}, \varepsilon$ | 0.1m, 0.5m | $d x, d y$ | 0.2m, 0.2m |
| Perception Radius | 15 m | $d t, d s$ | $0.2 \mathrm{~s}, 0.2 \mathrm{~m}$ |
| $w_{\mathrm{s}, 2}^{\mathrm{P}}, w_{\mathrm{s}, 3}^{\mathrm{P}}, w_{\mathrm{b}}^{\mathrm{P}}$ | $10^{3}, 10^{4}, 1$ | $\Delta t$ | 0.2 s |
| $w_{\mathrm{s}, 2}^{\mathrm{s}}, w_{\mathrm{s}, 3}^{\mathrm{s}}, w_{\mathrm{p}}^{\mathrm{s}}, w_{\mathrm{b}}^{\mathrm{s}}$ | $10^{3}, 10^{4}, 10,1$ |  |  |


![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-09.jpg?height=438&width=879&top_left_y=718&top_left_x=1079)
Fig. 6. Results in high-level planner I.

vehicle occupies CA (grey area) and no collision occurs during the coordination. The longitudinal redundancy $s_{\text {red }}$ of feasible tunnel (yellow area) is also under consideration in the collision avoidance constraint.
2) High-Level Planner II: For the space-time resource allocation strategy, Fig. 7 shows single-vehicle planning results. Based on the generated reference path and speed profile (blue line), we can obtain the feasible tunnel (yellow area) and allocated resource blocks (purple area) for each vehicle in both XY and ST versions, via longitudinal and lateral redundancies $s_{\text {red }}, l_{\text {red }}$. As shown in Fig. 7(b), the allocated resource blocks have no intersection with the previous occupied blocks (green area), which can avoid resource conflicts between vehicles.

Fig. 8 shows the allocation of resource blocks in multi-vehicle scenario. Furthermore, we also analyze the necessity of choosing resource occupation rate as one of the performance criteria. In Fig. 8(a), we set a special case. All the vehicles in Road 1 and Road 3 are required to turn left and all the vehicles in Road 2 and Road 4 are required to go straight. We can see that, because of the advantage in shorter travel distance, the roads for going straight are more likely to occupy the intersection than those for turning left, which lead to unfairness and long-time resource waste in Road 1 and Road 3. As shown in Fig. 8(b), we add resource occupation rate into performance criteria of the coordination, which can better achieve the fairness for vehicles in different driving maneuvers and different roads.
3) Comparison on Different High-Level Planners: We compare the two high-level planners in terms of traffic throughput and resource occupation rate. In Fig. 9(a), we can easily see that, when the number of vehicles in the intersection increases, high-level planner II has a lower passing time than high-level

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-10.jpg?height=421&width=877&top_left_y=198&top_left_x=168)
Fig. 7. Single-vehicle results in high-level planner II (vehicle 4 in Fig. 8(b)).

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-10.jpg?height=1070&width=679&top_left_y=696&top_left_x=269)
Fig. 8. Allocated resource blocks for vehicles in high-level planner II.

planner I, that can lead to higher throughput. Fig. 9(b) shows the CDF of average passing time. High-level planner II with 2.02s in mean is 0.53s faster than high-level planner I with 2.55s, which means 20.78\% advantage in traffic throughput.

In Fig. 10(a), we can easily see that, when the number of vehicles in the intersection increases, high-level planner II has a higher resource occupation rate than high-level planner I. Fig. 10(b) shows the CDF of resource occupation rate. High-level planner II with 0.41 in mean is 2.3 times as much as high-level planner I with 0.18, which shows a great improvement in fairness when allocating resource blocks. Otherwise, a higher resource occupation rate also means that high-level planner II is able to more fully utilize the space and time resources in the intersection.

## B. Low-Level Planner

Fig. 11(a) and Fig. 11(b) show the path and speed profile planning of low-level planner. First, we can get the optimal

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-10.jpg?height=400&width=877&top_left_y=200&top_left_x=1083)
Fig. 9. Comparison on traffic throughput.

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-10.jpg?height=393&width=877&top_left_y=715&top_left_x=1081)
Fig. 10. Comparison on resource occupation rate.

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-10.jpg?height=808&width=883&top_left_y=1229&top_left_x=1079)
Fig. 11. Results in low-level planner.

linear line (purple line) and convex hull (grey area) through DP. Then spline-based QP is used to obtain the smooth practical path and speed profile (green line). We can see that the vehicle can avoid collisions with static and dynamic obstacles by nudging and decelerating. In addition, the practical trajectory is within the feasible tunnel (yellow area), which satisfy the result in high-level planner.

As mentioned before, combining with the high-level planner, our planning framework can avoid deadlock situations. Using only the low-level planner in each vehicle, as shown in Fig. 12(b), 4 vehicles always make the same decision to

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-11.jpg?height=436&width=877&top_left_y=196&top_left_x=168)
Fig. 12. Deadlock for only using low-level planner.

TABLE III
Mean Value Comparison of Smooth Costs
|  | Proposed Solver | Compared Solver [45] |
| :--- | :--- | :--- |
| Path $\left(C_{\mathrm{s}}^{\mathrm{P}}\right)$ | 3.60 | 7.50 |
| Speed ( $C_{\mathrm{s}}^{\mathrm{S}}$ ) | 3.80 | 8.84 |


avoid collisions. Firstly, they all decelerate, and then they all plan to accelerate after perceiving the trends of each other. Therefore, 4 vehicles are locked in CA. By contrast, our proposed framework first determines the crossing order and disjoint feasible tunnels for vehicles through the high-level planner, which shows better performance in multi-vehicle environments.

Table III shows the comparison of trajectory smoothness for different solvers in the low-level planner. Comparing with the highly used solver which imposes waypoints and curve interpolation in planning [45], our proposed solver, using DP and spline-based QP, can strongly decrease the mean value of smooth costs in both path and speed planning. In other words, our proposed solver can improve 52.00\% path comfort and 57.01\% speed comfort.

## VII. Laboratorial Experiments

In order to further verify the feasibility and practicability of the proposed planning framework, we conduct laboratory experiments with three low-speed ROS robots. For each robot, the range of velocity is -1.8m/s ~ 1.8m/s, and we set the $v_{\text {eff }} 0.9 \mathrm{~m} / \mathrm{s}$. The control frequency of robots is 50Hz. Lidars and cameras are used to perceive the environment and localize the position on each robot. Furthermore, for real-time communications, we also develop a wireless communication network between robots and a centralized computing unit based on Wi-Fi. In the experiments, the high-level planners are implemented on a centralized laptop with Core i5-1135G7 2.40-GHz CPU and 16-GB RAM, and the low-level planner is conducted on the computing unit of each robot, with Cortex-A57 MPCore 1.43-GHz CPU and 4-GB RAM.

Fig. 13 shows the map of experiments with $8.4 \mathrm{~m} \times 8.4 \mathrm{~m}$ in size, and the lane width is 1.2m at each road. The lines in the map with different colors show the driving maneuvers of robots on different roads. Three robots aim to efficiently reach the end points without collisions and deadlocks. As shown in the Fig. 15(a), high-level planner I was used in the experiments. At $t=7 \mathrm{~s}$ and 11s, we can see that when the front

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-11.jpg?height=565&width=705&top_left_y=198&top_left_x=1167)
Fig. 13. Experiment map and vehicle maneuvers.

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-11.jpg?height=1100&width=877&top_left_y=898&top_left_x=1083)
Fig. 14. Laboratorial experiment results based on ROS robots.

robot leaves the collision set (red bounding box), the next robot just enters, which remains only one robot in the collision set simultaneously. For high-level planner II, as shown in Fig. 15(b), we can see that three robots successfully passed the intersection, without any interaction on their feasible tunnels (red bounding boxes) at each time point. Therefore, both strategies can achieve vehicle safety in the experiments.

Fig. 13 compares the passing times of different strategies in the experiments. The average passing time of high-level planner II is 13.97s, which is 25.70\% more efficient than high-level planner I with 18.80s. The experimental results verify the advantage of the novel space-time

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-12.jpg?height=397&width=881&top_left_y=196&top_left_x=165)
Fig. 15. Comparison on passing times in experiments.

resource allocation strategy in improving traffic throughput, comparing to the traditional collision-set one. Furthermore, these results also validate the effectiveness and applicability of our proposed double-level framework. More details of our simulations and experiments can be found in the video of the supplementary material, or online: https://www.youtube.com/watch?v=SCrXHVa2Q4Y.

## VIII. Conclusion

In this paper, we mainly deal with the coordination problem at road intersections. Our main contributions include (i) formulate a double-level coordination framework, considering both efficiency and flexibility. (ii) In infrastructure-based high-level planner, for achieving better traffic performance (throughput, fairness, stability) than the traditional collision-set strategy, we propose a novel space-time resource allocation strategy to efficiently use the intersection resource. (iii) In vehicle-based low-level planner, an ego planning strategy is used to avoid obstacles and improve trajectory smoothness. Both simulations and practical experiments are carried out. Numerical results show that (i) the proposed framework is feasible for the realization of vehicle safety by avoiding collisions and deadlocks. (ii) The traffic throughput and resource occupation rate can be significantly improved by the high-level resource allocation strategy. Meanwhile, the flexibility is also guaranteed based on feasible tunnel. (iii) The solver used in low-level planner (DP and spline-based QP) can help to improve the passenger comfort by trajectory smoothness. The presented methods along with algorithms are of value to the development of future intelligent transportation systems. In addition, by regarding human-driven vehicles as dynamic obstacles, proposed framework shows the potential to deal with both autonomous and traditional human-driven vehicles simultaneously, which provides meaningful insights for related investigations.

## Appendix A <br> Solver: Dynamic Programming and Spline-Based Quadratic Programming

## A. Problem Description

Both path and speed optimizers in Section III, IV and V can use the same solver to deal with, based on dynamic programming (DP) and spline-based quadratic programming (QP). We define $\beta=h(\alpha)$ as one of the trajectory functions, and the optimization problem can be formed with an objective

TABLE IV
Correspondences of $\beta=h(\alpha)$
| Optimization | Function | Constraint Types | Solver |
| :--- | :--- | :--- | :--- |
| $\mathscr{P}_{1}$ | $f(s), g(s)$ | $C_{s, z}, C_{b}$ | QP |
| $\mathscr{P}_{3}$ | $u_{1, r}(t)$ | $C_{s, z}, C_{b}$ | QP |
| $\mathscr{P}_{4}$ | $u_{1, r}(t)$ | $C_{s, z}, C_{b}, C_{c}$ | DP + QP |
| $\mathscr{P}_{5}$ | $p(s)$ | $C_{s, z}, C_{b}, C_{c}$ | DP + QP |
| $\mathscr{P}_{6}$ | $q(t)$ | $C_{s, z}, C_{b}, C_{c}$ | $\mathrm{DP}+\mathrm{QP}$ |


function and multiple constraints. The objective function of $h$ can be described as

$$
\arg \min _{h} C(h)=\sum_{z} w_{\mathrm{s}, z} \cdot C_{\mathrm{s}, z}(h)+w_{\mathrm{b}} \cdot C_{\mathrm{b}}(h)+w_{\mathrm{c}} \cdot C_{\mathrm{c}}(h)
$$

with

$$
\begin{aligned}
C_{\mathrm{s}, z} & =\int\left(h^{(z)}\right)^{2}(\alpha) \mathrm{d} \alpha \\
C_{\mathrm{b}} & =\int(h(\alpha)-\tilde{h}(\alpha))^{2} \mathrm{~d} \alpha \\
C_{\mathrm{c}} & =\sum \begin{cases}\text { Inf } & \text { constrains on } h(\alpha) \\
0 & \text { else }\end{cases}
\end{aligned}
$$

where $\tilde{h}(x)$ is a pre-specified reference function. Furthermore, the constraints of the optimization include following types

$$
\begin{aligned}
L & \leq h^{(\gamma)}(\alpha) \leq H, \quad \gamma=0,1,2 \\
h^{(\gamma)}\left(\alpha_{0}\right) & =\beta_{0}^{(\gamma)}, \quad \gamma=0,1,2 \\
h^{\prime}(\alpha) & \geq 0
\end{aligned}
$$

where (52) is the boundary constraints of $h$ and its different derivatives, (53) is limitations for initial state, (54) is a specifical monotonicity constraint for speed optimizer. The correspondences can be shown in Table IV.

## B. Searching: Dynamic Programming (DP)

In the optimizers, the searching space is usually non-convex because of the cost function $C_{\mathrm{c}}$. Therefore, when $w_{\mathrm{c}} \neq 0$, we need to use DP to search and generate a convex domain for the next step optimization. Specifically, first we build lattice on the two-dimensional search space with longer sampling intervals $(d \alpha \cdot d \beta)$. Then DP is used to calculate the minimum cost and store the optimal path/speed profile on each sampling point. As shown in Fig. 16, the state transition equation of DP can be described as

Path Optimizer:

$$
P_{i, j}=\min \left\{P_{i-1, \mu}+C_{(i-1, \mu) \rightarrow(i, j)} \mid \mu=0,1, \ldots, M\right\}
$$

Speed Optimizer:

$$
P_{i, j}=\min \left\{P_{i-1, \mu}+C_{(i-1, \mu) \rightarrow(i, j)} \mid \mu=0,1, \ldots, j\right\}
$$

where $P_{i, j}$ is the state value of the sampling point $(i, j)$ in the $j$-th row and $i$-th column of the lattice, $i \in\{0,1, \ldots, N\}$,

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-13.jpg?height=425&width=808&top_left_y=202&top_left_x=202)
Fig. 16. Structure for DP path/speed profile searching.

$j \in\{0,1, \ldots, M\} . C_{\left(i_{1}, j_{1}\right) \rightarrow\left(i_{2}, j_{2}\right)}$ means the value of the objective function (48) from sampling point $\left(i_{1}, j_{1}\right)$ to $\left(i_{2}, j_{2}\right)$. After getting the optimal selection $\mu_{\text {opt }}$ of (55) or (56), the optimal profile to reach sampling point $(i, j)$ will be stored, i.e.

$$
\mathbb{S}_{i, j}=\left\{\mathbb{S}_{i-1, \mu_{\mathrm{opt}}},(i \cdot d \alpha, j \cdot d \beta)\right\}
$$

After DP, from the end point $\left(i_{\text {end }}, j_{\text {end }}\right)$, we can get the optimal sampling point set $\mathbb{S}_{i_{\text {end }}, j_{\text {end }}}$, which can be reformulated to $\left\{\left(\alpha_{m}, \beta_{m}\right) \mid m=0,1, \ldots, N\right\}$. Based on it, the convex domain $\left[\varepsilon_{\text {low }}(\alpha), \varepsilon_{\text {high }}(\alpha)\right]$ can be obtained. Therefore, non-convex cost function $C_{\mathrm{c}}$ can be converted to a convex searching space constraint

$$
\varepsilon_{\text {low }}(\alpha) \leq h(\alpha) \leq \varepsilon_{\text {high }}(\alpha)
$$

The time complexity of DP step is $\mathrm{O}\left(M^{2} \times N\right)$. Parallel computation can be used in the solver to further reduce the computation time.
C. Optimization: Spline-Based Quadratic Programming (QP)

1) Parameterization: Setting the optimal sampling points $\left\{\left(\alpha_{m}, \beta_{m}\right) \mid m=0,1, \ldots, N\right\}$ as knots, the trajectory function $h(\alpha)$ can be parameterized as spline with quintic polynomials

$$
h(\alpha)=\left\{\begin{array}{cc}
h_{0}\left(\alpha-\alpha_{0}\right) & \alpha \in\left[\alpha_{0}, \alpha_{1}\right) \\
h_{1}\left(\alpha-\alpha_{1}\right) & \alpha \in\left[\alpha_{1}, \alpha_{2}\right) \\
\ldots & \ldots \\
h_{N-1}\left(\alpha-\alpha_{N-1}\right) & \alpha \in\left[\alpha_{N-1}, \alpha_{N}\right]
\end{array}\right.
$$

with

$$
h_{m}(\alpha)=k_{m 0}+k_{m 1} \alpha+\ldots+k_{m 5} \alpha^{5}
$$

with $m=0,1, \ldots, N-1$. Therefore the optimization problem is transformed into a search for optimal coefficients $\mathbf{K}_{\text {coe }}$

$$
\begin{aligned}
\mathbf{K}_{\mathrm{coe}} & =\left[\begin{array}{ll}
\mathbf{K}_{0}^{\mathrm{T}} & \mathbf{K}_{1}^{\mathrm{T}} \cdots \mathbf{K}_{N-1}^{\mathrm{T}}
\end{array}\right]^{\mathrm{T}} \\
\mathbf{K}_{m} & =\left[\begin{array}{ll}
k_{m 0} & k_{m 1} \cdots k_{m 5}
\end{array}\right]^{\mathrm{T}}
\end{aligned}
$$

2) Optimization: Based on the convex searching space, we can search for a smooth feasible path/speed profile through the following optimization.

$$
\begin{aligned}
\mathscr{P}_{7}: \min _{h} & \Rightarrow \sum_{z} w_{\mathrm{s}, z} \cdot C_{\mathrm{s}, z}(h)+w_{\mathrm{b}} \cdot C_{\mathrm{b}}(h) \\
\text { s.t. } & h_{m}^{(\gamma)}\left(\alpha_{m+1}-\alpha_{m}\right)=h_{m+1}^{(\gamma)}(0) \\
& (52),(53),(58) \quad: \text { Path Optimizer } \\
& (52),(53),(54),(58) \quad: \text { Speed Optimizer }
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-13.jpg?height=503&width=621&top_left_y=200&top_left_x=1207)
Fig. 17. Reference speed profile with yaw rate cost on turning maneuvers.

with $m=0,1, \ldots, N-2$ and $\gamma=0,1,2,3$. Constraint (63) ensures that the piecewise polynomials are joint at spline knots, by matching the $\gamma$-th-order derivative.

The optimization problem $\mathscr{P}_{7}$ can be converted to a standard QP problem as follows.

$$
\begin{aligned}
\mathscr{P}_{8}: & \min . \quad \mathbf{K}_{\mathrm{coe}}{ }^{\mathbf{T}} \mathbf{H} \mathbf{K}_{\mathrm{coe}}+\mathbf{b}^{\mathrm{T}} \mathbf{K}_{\mathrm{coe}} \\
& \text { s.t. } \quad \mathbf{C}_{\text {ineq }} \mathbf{K}_{\mathrm{coe}} \leq \mathbf{D}_{\text {ineq }} \\
& \mathbf{C}_{\mathrm{eq}} \mathbf{K}_{\mathrm{coe}}=\mathbf{D}_{\mathrm{eq}}
\end{aligned}
$$

with constant matrixes $\mathbf{H}, \mathbf{b}, \mathbf{C}_{\text {ineq }}, \mathbf{C}_{\text {eq }}, \mathbf{D}_{\text {ineq }}$ and $\mathbf{D}_{\text {eq }}$. The optimization problem $\mathscr{P}_{8}$ can be solved by many offthe-shelf solvers, such as OSQP, GUROBI, etc. With the optimal coefficients $\mathbf{K}_{\text {coe }}$, we can get the smooth feasible path / speed profile via (59) and (60).

## Appendix B <br> Yaw Rate in Reference Speed Profile Generator

In some specific scenarios where vehicle maneuvers require large turning angles, we can also consider the relationship between the path curvature and the vehicle velocity in addition to trajectory smoothness, to further improve the vehicle comfort. The idea yaw rate $\dot{\theta}(t)$ of the vehicle can be used to describe the changing pace of direction when driving at turning maneuvers [31], i.e.,

$$
\begin{aligned}
\dot{\theta} & =\kappa(t) \cdot v \\
& =\frac{[f(u(t))]^{\prime}[g(u(t))]^{\prime \prime}-[f(u(t))]^{\prime \prime}[g(u(t))]^{\prime}}{\left\{[f(u(t))]^{\prime 2}+[g(u(t))]^{\prime 2}\right\}^{3 / 2}} \cdot u^{\prime}(t)
\end{aligned}
$$

where $x=f(s), y=g(s)$ are the path functions predefined by $\mathscr{P}_{1}, s=u(t)$ is the speed profile of the vehicle, $(\bullet):=\frac{\partial}{\partial t}(\bullet)$.

To further improve the comfort, we need to attenuate high yaw rates in vehicle trajectory. Therefore, in the reference speed profile generator $\mathscr{P}_{2}, \mathscr{P}_{3}, \mathscr{P}_{4}$, we can add a yaw rate cost, which can be represented as

$$
C_{\mathrm{y}, \text { ref }}^{\mathrm{S}}\left(u_{i, r}\right)=w_{\mathrm{y}}^{\mathrm{S}} \int \dot{\theta}^{2}(t) \mathrm{d} t
$$

Similarly, the new speed profile generator with yaw rate cost can be solved by DP and spline-based QP, which is shown in Fig. 17. We can see that with the yaw rate cost $C_{\mathrm{y}, \mathrm{ref}}^{\mathrm{S}}$, the vehicle will decelerate to attenuate high yaw rates when
changing the heading, which will provide a more comfortable trajectory in turning maneuvers.

## References

[1] Y. Zhang, G. Chen, and T. Zhang, "Intelligent intersection coordination and trajectory optimization for autonomous vehicles," in Proc. IEEE Int. Conf. Auto. Syst. (ICAS), Aug. 2021, pp. 1-6.
[2] E. H. Choi, Crash Factors in Intersection-Related Crashes: An On-Scene Perspective. Washington, DC, USA: National Highway Traffic Safety Administration, 2010.
[3] L. Chen and C. Englund, "Cooperative intersection management: A survey," IEEE Trans. Intell. Transp. Syst., vol. 17, no. 2, pp. 570-586, Feb. 2016.
[4] R. Hult, G. R. Campos, E. Steinmetz, L. Hammarstrand, P. Falcone, and H. Wymeersch, "Coordination of cooperative autonomous vehicles: Toward safer and more efficient road transportation," IEEE Signal Process. Mag., vol. 33, no. 6, pp. 74-84, Nov. 2016.
[5] S. Krishnan, R. G. Aadithya, R. Ramakrishnan, V. Arvindh, and K. Sivanathan, "A look at motion planning for AVs at an intersection," in Proc. 21st Int. Conf. Intell. Transp. Syst. (ITSC), Nov. 2018, pp. 333-340.
[6] 2010 Motor Vehicle Crashes: Overview. Accessed: Feb. 2012. [Online]. Available: https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/ 811552
[7] L. Claussmann, M. Revilloud, D. Gruyer, and S. Glaser, "A review of motion planning for highway autonomous driving," IEEE Trans. Intell. Transp. Syst., vol. 21, no. 5, pp. 1826-1848, May 2019.
[8] Y. Feng, D. He, and Y. Guan, "Composite platoon trajectory planning strategy for intersection throughput maximization," IEEE Trans. Veh. Technol., vol. 68, no. 7, pp. 6305-6319, Jul. 2019.
[9] D. González, J. Pérez, V. Milanés, and F. Nashashibi, "A review of motion planning techniques for automated vehicles," IEEE Trans. Intell. Transp. Syst., vol. 17, no. 4, pp. 1135-1145, Apr. 2016.
[10] F. Perronnet, J. Buisson, A. Lombard, A. Abbas-Turki, M. Ahmane, and A. El Moudni, "Deadlock prevention of self-driving vehicles in a network of intersections," IEEE Trans. Intell. Transp. Syst., vol. 20, no. 11, pp. 4219-4233, Nov. 2019.
[11] E. Namazi, J. Li, and C. Lu, "Intelligent intersection management systems considering autonomous vehicles: A systematic literature review," IEEE Access, vol. 7, pp. 91946-91965, 2019.
[12] R. Hult, G. R. Campos, P. Falcone, and H. Wymeersch, "An approximate solution to the optimal coordination problem for autonomous vehicles at intersections," in Proc. Amer. Control Conf. (ACC), Jul. 2015, pp. 763-768.
[13] Y. Mo, M. Wang, T. Zhang, and Q. Zhang, "Autonomous cooperative vehicle coordination at road intersections," J. Commun. Inf. Netw., vol. 4, no. 1, pp. 78-87, 2019.
[14] C. Liu, Y. Mo, B. Gao, and T. Zhang, "Low complexity coordination strategies at multi-lane intersections," in Proc. IEEE Globecom Workshops (GC Wkshps), Dec. 2019, pp. 1-6.
[15] Y. Xu, H. Zhou, B. Qian, H. Wu, Z. Zhang, and X. S. Shen, "When automated vehicles meet non-signalized intersections: A collision-free scheduling solution," in Proc. IEEE/CIC Int. Conf. Commun. China (ICCC), Aug. 2018, pp. 709-713.
[16] B. Qian, H. Zhou, F. Lyu, J. Li, T. Ma, and F. Hou, "Toward collisionfree and efficient coordination for automated vehicles at unsignalized intersection," IEEE Internet Things J., vol. 6, no. 6, pp. 10408-10420, Dec. 2019.
[17] M. Wang, T. Zhang, L. Gao, and Q. Zhang, "High throughput dynamic vehicle coordination for intersection ground traffic," in Proc. IEEE 88th Veh. Technol. Conf. (VTC-Fall), Aug. 2018, pp. 1-6.
[18] C. Liu, Y. Zhang, T. Zhang, X. Wu, L. Gao, and Q. Zhang, "High throughput vehicle coordination strategies at road intersections," IEEE Trans. Veh. Technol., vol. 69, no. 12, pp. 14341-14354, Dec. 2020.
[19] B. Li, Y. Zhang, Y. Zhang, N. Jia, and Y. Ge, "Near-optimal online motion planning of connected and automated vehicles at a signal-free and lane-free intersection," in Proc. IEEE Intell. Vehicles Symp. (IV), Jun. 2018, pp. 1432-1437.
[20] Y. Mo, M. Wang, T. Zhang, and Q. Zhang, "Intelligent offloading strategies for high throughput traffic intersection coordination," in Proc. IEEE Wireless Commun. Netw. Conf. Workshop (WCNCW), Apr. 2019, pp. 1-6.
[21] K.-D. Kim and P. R. Kumar, "An MPC-based approach to provable system-wide safety and liveness of autonomous ground traffic," IEEE Trans. Autom. Control, vol. 59, no. 12, pp. 3341-3356, Dec. 2014.
[22] C. Liu, S. Lee, S. Varnhagen, and H. E. Tseng, "Path planning for autonomous vehicles using model predictive control," in Proc. IEEE Intell. Vehicles Symp. (IV), Jun. 2017, pp. 174-179.
[23] Z. Zuo et al., "MPC-based cooperative control strategy of path planning and trajectory tracking for intelligent vehicles," IEEE Trans. Intell. Vehicles, vol. 6, no. 3, pp. 513-522, Sep. 2021.
[24] J. Horst and A. Barbera, "Trajectory generation for an on-road autonomous vehicle," in Unmanned Systems Technology VIII, vol. 6230, G. R. Gerhart, C. M. Shoemaker, and D. W. Gage, Eds. Bellingham, WA, USA: SPIE, 2006, pp. 866-877, doi: 10.1117/12.663643.
[25] H. Tehrani, Q. H. Do, M. Egawa, K. Muto, K. Yoneda, and S. Mita, "General behavior and motion model for automated lane change," in Proc. IEEE Intell. Vehicles Symp. (IV), Jun. 2015, pp. 1154-1159.
[26] D. González, J. Pérez, R. Lattarulo, V. Milanés, and F. Nashashibi, "Continuous curvature planning with obstacle avoidance capabilities in urban scenarios," in Proc. 17th Int. IEEE Conf. Intell. Transp. Syst. (ITSC), Oct. 2014, pp. 1430-1435.
[27] F. Garrido, D. González, V. Milanés, J. Pérez, and F. Nashashibi, "Real-time planning for adjacent consecutive intersections," in Proc. IEEE 19th Int. Conf. Intell. Transp. Syst. (ITSC), Nov. 2016, pp. 1108-1113.
[28] G. Liu and S. Wu, "A novel optimized trajectory planning method via spline function theorems," in Proc. IEEE 4th Inf. Technol. Mechatronics Eng. Conf. (ITOEC), Dec. 2018, pp. 745-749.
[29] J. Ziegler and C. Stiller, "Spatiotemporal state lattices for fast trajectory planning in dynamic on-road driving scenarios," in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst., Oct. 2009, pp. 1879-1884.
[30] W. Xu, J. Wei, J. M. Dolan, H. Zhao, and H. Zha, "A real-time motion planner with trajectory optimization for autonomous vehicles," in Proc. IEEE Int. Conf. Robot. Autom., May 2012, pp. 2061-2067.
[31] J. Ziegler, P. Bender, T. Dang, and C. Stiller, "Trajectory planning for Bertha-A local, continuous method," in Proc. IEEE Intell. Vehicles Symp., Jun. 2014, pp. 450-457.
[32] Y. Meng, Y. Wu, Q. Gu, and L. Liu, "A decoupled trajectory planning framework based on the integration of lattice searching and convex optimization," IEEE Access, vol. 7, pp. 130530-130551, 2019.
[33] H. Fan et al., "Baidu Apollo EM motion planner," 2018, arXiv:1807.08048.
[34] N. Li, D. W. Oyler, M. Zhang, Y. Yildiz, I. Kolmanovsky, and A. R. Girard, "Game theoretic modeling of driver and vehicle interactions for verification and validation of autonomous vehicle control systems," IEEE Trans. Control Syst. Technol., vol. 26, no. 5, pp. 1782-1797, Sep. 2018.
[35] P. Wang, C.-Y. Chan, and A. de La Fortelle, "A reinforcement learning based approach for automated lane change maneuvers," in Proc. IEEE Intell. Vehicles Symp. (IV), Jun. 2018, pp. 1379-1384.
[36] M. Zhang, T. Zhang, L. Yang, H. Xu, and Q. Zhang, "An autonomous overtaking maneuver based on relative position information," J. Commun. Inf. Netw., vol. 4, no. 2, pp. 101-110, 2019.
[37] L. Yang, X. Liang, T. Wang, and E. Xing, "Real-to-virtual domain unification for end-to-end autonomous driving," in Proc. Eur. Conf. Comput. Vis. (ECCV), Sep. 2018, pp. 530-545.
[38] G. Sartoretti et al., "PRIMAL: Pathfinding via reinforcement and imitation multi-agent learning," IEEE Robot. Autom. Lett., vol. 4, no. 3, pp. 2378-2385, Jul. 2019.
[39] J. Kong, M. Pfeiffer, G. Schildbach, and F. Borrelli, "Kinematic and dynamic vehicle models for autonomous driving control design," in Proc. IEEE Intell. Vehicles Symp. (IV), Jun. 2015, pp. 1094-1099.
[40] M. Werling, J. Ziegler, S. Kammel, and S. Thrun, "Optimal trajectory generation for dynamic street scenarios in a Frenét frame," in Proc. IEEE Int. Conf. Robot. Autom., May 2010, pp. 987-993.
[41] S. Shalev-Shwartz, S. Shammah, and A. Shashua, "On a formal model of safe and scalable self-driving cars," 2017, arXiv:1708.06374.
[42] S. Yi, H. Li, and X. Wang, "Understanding pedestrian behaviors from stationary crowd groups," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2015, pp. 3488-3496.
[43] M. J. Neely, "Stochastic network optimization with application to communication and queueing systems," Synth. Lect. Commun. Netw., vol. 3, no. 1, p. 211, 2010.
[44] Y. Zhang, R. Hao, B. Gao, Z. Xie, M. Liu, and T. Zhang, "A collisionfree coordination framework for mixed-vehicle intersections," in Proc. IEEE Veh. Technol. Conf. (VTC), Sep. 2021, pp. 1-6.
[45] D. Zhou, Z. Ma, and J. Sun, "Autonomous vehicles' turning motion planning for conflict areas at mixed-flow intersections," IEEE Trans. Intell. Vehicles, vol. 5, no. 2, pp. 204-216, Jun. 2020.
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-15.jpg?height=320&width=256&top_left_y=215&top_left_x=168)

Yixiao Zhang received the B.Eng. degree in communication engineering from the Harbin Institute of Technology (HIT), China, in 2020. He is currently pursuing the M.S. degree in machine learning with the School of Electrical Engineering and Computer Science, KTH Royal Institute of Technology (KTH), Stockholm, Sweden. He worked as a Research Assistant with the School of Electronics and Information Engineering, HIT (Shenzhen), Shenzhen, from 2020 to 2021. His main research interests include motion planning, resource optimization, multi-agent systems, machine learning, and autonomous vehicle navigation and control.
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-15.jpg?height=318&width=256&top_left_y=898&top_left_x=168)

Rui Hao received the B.S. degree in electronics and information engineering from Dalian Maritime University, Dalian, China, in 2020. He is currently pursuing the M.S. degree in communication and information systems with the School of Electrical and Information Engineering, Harbin Institute of Technology (Shenzhen), Shenzhen, China. His research interests include vehicle path planning, vehicle wireless communication and control, and indoor positioning.
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-15.jpg?height=320&width=254&top_left_y=1495&top_left_x=168)

Tingting Zhang (Member, IEEE) received the B.S. (Hons.), M.S., and Ph.D. degrees in electronic engineering from the Harbin Institute of Technology (HIT), Harbin, China, in 2003, 2005, and 2009, respectively. He is currently a Professor with the HIT (Shenzhen), Shenzhen. His main research interests include wireless localization, integration of sensing and communication, and autonomous vehicle navigation and control. He serves as an Organizer and a TPC Member for several international conferences, such as ICC, GLOBECOM, ICCC, and VTC. He received the Outstanding Post-Doctoral Award of HIT, Shenzhen Graduate School, in 2011. He also received the Shenzhen High Level Talent Program Award in 2012. He serves as an Associate Editor for Frontiers in Communications and Networks and a Guest Editor for IEEE Communications Magazine.
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-15.jpg?height=320&width=251&top_left_y=215&top_left_x=1083)

Xiaohan Chang received the B.Eng. degree in communication engineering from the Harbin Institute of Technology (HIT), China, in 2020. He is currently pursuing the M.S.E. degree in signal and information processing with the School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences (UCAS), China. His research interests include resource optimization, autonomous vehicle navigation and control, cross-technology communication, and physiological signal processing.
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-15.jpg?height=320&width=256&top_left_y=681&top_left_x=1081)

Zepeng Xie received the B.Eng. degree in electronics and information engineering from the Harbin Institute of Technology (HIT) in 2021. He is currently a postgraduate student with the School of Electronics and Information Engineering (EIE), HIT (Shenzhen), Shenzhen. His main research interests include wireless localization, trajectory optimization, and autonomous driving and control.
![](https://cdn.mathpix.com/cropped/1e7fd7c9-8c7f-41aa-b92c-69dc4c32f9a4-15.jpg?height=318&width=254&top_left_y=1126&top_left_x=1083)

Qinyu Zhang (Senior Member, IEEE) received the bachelor's degree in communication engineering from the Harbin Institute of Technology (HIT) in 1994 and the Ph.D. degree in biomedical and electrical engineering from the University of Tokushima, Japan, in 2003.

From 1999 to 2003, he was an Assistant Professor with the University of Tokushima. From 2003 to 2005, he was an Associate Professor with the HIT Shenzhen Graduate School, and was the Founding Director of the Communication Engineering Research Center, School of Electronics and Information Engineering (EIE). Since 2005, he has been a Full Professor, and serves as the Dean for the EIE School. His research interests include aerospace communications and networks, wireless communications and networks, cognitive radios, signal processing, and biomedical engineering.
Dr. Zhang has been a TPC Member of INFOCOM, ICC, GLOBECOM, WCNC, and other flagship conferences in communications. He is on the editorial board of some academic journals, such as Journal of Communications, KSII Transactions on Internet and Information Systems, and Science China: Information Sciences. He has been awarded the National Science Fund for Distinguished Young Scholars, the Young and Middle-Aged Leading Scientist of China, the Chinese New Century Excellent Talents in University, and obtained three scientific and technological awards from governments. He was the TPC Co-Chair of IEEE/CIC ICCC'15, the Symposium Co-Chair of IEEE VTC'16 Spring, the Associate Chair of Finance of ICMMT'12, and the Symposium Co-Chair of CHINACOM'11. He was the Founding Chair of the IEEE Communications Society Shenzhen Chapter.


[^0]:    ${ }^{1}$ Here the indexes $i$ and $r$ are omitted.

