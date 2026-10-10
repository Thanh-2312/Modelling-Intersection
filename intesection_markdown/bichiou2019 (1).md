# International Journal of Transportation Science and Technology 

journal homepage: www.elsevier.com/locate/ijtst

# Real-time optimal intersection control system for automated/cooperative vehicles 

Youssef Bichiou ${ }^{\mathrm{a}}$, Hesham A. Rakha ${ }^{\mathrm{b}, \mathrm{c}, *}$<br>${ }^{\mathrm{a}}$ Center for Sustainable Mobility at the Virginia Tech Transportation Institute, 3500 Transportation Research Plaza, Virginia Tech, Blacksburg, VA 24061, United States<br>${ }^{\mathrm{b}}$ Center for Sustainable Mobility at the Virginia Tech Transportation Institute, United States<br>${ }^{\mathrm{c}}$ Samuel Reynolds Pritchard Professor of Engineering in the Charles E. Via, Jr. Department of Civil and Environmental Engineering, United States

ARTICLE INFO

Article history:
Received 28 February 2018
Received in revised form 13 April 2018
Accepted 18 April 2018
Available online xxxx

Keywords:
Real time
Autonomous/cooperative vehicles
Optimal control
Roadway intersection
Mobility
Delay
$\mathrm{CO}_{2}$ emissions


#### Abstract

Automated vehicles (AVs) are an emerging technology in the automotive industry. The numerous research efforts that are being dedicated to the development of these systems makes them achievable in the near future. The need to make this technology mature is justified by potential safety gains from the elimination of human error, the enhancement of mobility through the reduction of congestion, and the protection of the environment through the reduction in vehicle emissions. Algorithms are needed to deliver optimal and/or sub-optimal solutions for situations and/or scenarios that AVs would encounter in the field. In this paper, an attempt to optimize the movement of AVs through intersections is developed. The developed model is a real-time optimization problem subjected to dynamic constraints (i.e., ordinary differential equations governing the motion of a vehicle) and static constraints (i.e., maximum achievable velocities). By virtue of the Lagrangian formulation used in Pontryagin's minimum principle and convex optimization, the solution that minimizes the trip time is obtained. This logic is simulated and compared to the operation of a roundabout, an all-way stop sign, and a traffic-signal-controlled intersection. The results demonstrate that a 55\% reduction in delay is achievable compared to the best of these three intersection control strategies, on average. An interesting byproduct of this new logic is a 43\% reduction in fuel consumption (reduction from an average of 200 mL to 115 mL ) and $\mathrm{CO}_{2}$ emissions (a reduction from 445 g for the roundabout to 265 g). © 2018 Tongji University and Tongji University Press. Publishing Services by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/ licenses/by-nc-nd/4.0/).


1. Introduction

Since the introduction of automation, numerous systems that used to require human intervention are becoming automated. Examples of these systems include auto manufacturing systems, subway trains, and automated vehicles (AVs). In recent years, computers have become integral components of vehicles, handling various tasks automatically, from meeting the stoichiometric coefficient of the combustion reaction in the engine to cruise control. Substantial research efforts are being dedicated to the enhancement of these systems (Fortelle, 2015; Zohdy and Rakha, 2012; Li, 2006; Azimi et al., 2013; Rakha and Kamalanathsarma, 2011; Lee and Park, 2011; Le et al., 2013; Abdul Aziz et al., 2012; Ye et al., 2015;

[^0]Roozemond, 2001). The ultimate goal behind this trend is to make vehicles truly autonomous, and the principal motivation behind this effort is the expected safety, economic and mobility advantages associated with the introduction of automated/ autonomous vehicles. At this stage various prototypes exist. Yet, the technology implemented is still not mature enough for mass field implementation. Considerable development in algorithms is required so that the vehicle performs as expected when facing any predicted or unpredicted situations. The legislative side of the matter is also a challenge. For example, who would be accountable in the case of incidents, and to whom or what should a driver's license be given?

One of the challenging scenarios researchers need to address is how automated vehicles should optimally traverse an intersection that is not equipped with any control devices. Numerous solutions for this problem have been and are still being developed. One of these solutions is the Cooperative Adaptive Cruise Control (CACC) (Massera et al., 2016) system and particularly its intersection version (iCACC) (Zohdy and Rakha, 2014). The main objective of this system is to optimize vehicle trajectories while at the same time reducing vehicle delay. The optimality characteristic of this method for this particular situation is not proven. Medina et al. (2015) tried to address this issue for a T-intersection. A mathematical model was developed and linearized. Collision avoidance was implemented but no dynamic constraints were used. Examples of dynamic constraints include acceleration constraints and velocity constraints. The authors were successful in solving this problem for six vehicles. Gratner and Stefan (2016) simulated a T-Intersection where only two vehicles were present. The study did not consider the effects of other vehicles on the road (i.e., there is no car-following model). The aim was to develop a collision prediction system. The computational burden of the system prevents it from being real-time and thus responsive in a dynamic environment. The developed model features static constraints on accelerations and nonlinear equations of motion. Zhu et al. (2009) developed a methodology for making vehicles cross an intersection cooperatively by computing the required speed. Their paper focuses on scheduling and no developed dynamic model was provided. Li et al. (2013) developed a reservationbased autonomous intersection control in VISSIM. The tool uses purely kinematic equations, and the vehicles communicate only with a centralized intersection controller. This controller determines the passing sequence of the approaching vehicles on a first-come, first-served basis.

In this paper, a comprehensive and extended vehicle model is proposed. This model considers real traffic pattern (i.e. CarFollowing model, acceleration constraints obtained from real driver data, constraints on velocity based on the geometry of the road). The time series of the vehicle's position, velocity, and acceleration are computed. The vehicle delay, number of stops, fuel consumption and $\mathrm{CO}_{2}$ emissions are also computed as part of the results in a post-processing step.

### 1.1. Study objective and paper layout

In this paper, only single-lane intersections are considered. The problem of moving automated vehicles through an intersection is solved with the help of a scheduler placed at the intersection. Time slots for each vehicle to cross conflict zones within the intersection are allocated. Singular cases where a vehicle has to stop (at the intersection) are also accounted for. An enhanced algorithm is developed to compute an optimal solution for each possible scenario a vehicle may encounter while traversing a roadway intersection. The contribution of the paper is as follows. The present work is the first to consider a fully comprehensive and nonlinear vehicle dynamics model within the scheduler. This vehicle is also subject to nonlinear kinematic and dynamic constraints; for instance, bounds on vehicle velocity and acceleration/deceleration (Zohdy and Rakha, 2014). It also considers the interaction with other vehicles on the road, in this case the vehicles ahead. Carfollowing and collision avoidance models are also included Rakha et al. (2009), Zohdy and Rakha (2014). The conditions of the roadway surface (i.e., rain, snow, etc.) and vehicle tire conditions are also accounted for Rakha et al. (2001). Bichiou et al. (2016) developed a similar system for optimizing the movement of automated/autonomous vehicles crossing an intersection without traffic control devices. However, the full nonlinear model used in Bichiou et al. (2016) renders the developed tool unsuitable for field real-time implementations due the high computational cost associated with the scheduler. One of the key points of this present work is simplifying the models while retaining the relevant physics (i.e., obtaining results that are very close to those that are obtained from the complex and nonlinear model) while at the same time making it run in real-time. The developed algorithm therefore uses optimal control theory in order to formulate the complete dynamic model (i.e. the optimization model subject to dynamic constraints) and convex optimization in order to solve it. This provides optimality and/or sub-optimality with a guaranteed very low computational burden.

The simulations were performed for an intersection of a major and minor road. The traffic inflows ranged from $500 \mathrm{veh} / \mathrm{h}$ to a maximum of 1200 veh/h for a roadway saturation flow rate of $q_{c}=1700 \mathrm{veh} / \mathrm{h} /$ lane . The traffic inflows for the minor road ranged from 250 veh/h to 600 veh/h. Detailed vehicle information was captured during the simulation: position, velocity, and acceleration. In a post-processing step, the vehicle delay, stops, fuel consumption and $\mathrm{CO}_{2}$ emissions were evaluated and compared to the values obtained when the same vehicles crossed an intersection equipped with other types of controls.

In Section 2, we present the developed model for a vehicle traversing an intersection with all its dynamic and kinematic constraints. In Section 3, the obtained results in terms of vehicle delay, stops, fuel consumption levels, and emissions are presented. In Section 4, the concluding remarks and a discussion of further research directions are presented.

## 2. Model description

In this paper, we consider the intersection given in Fig. 1. Each vehicle represented in this figure has three possible routes: through, left, or right. These routes proceed through "conflict zones." A number of vehicles will share these zones, and thus

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-03.jpg?height=568&width=750&top_left_y=183&top_left_x=564)
Fig. 1. Schematic of a typical intersection.

the solution to the proposed problem will feature an occupancy time slot allocation for each zone. For this paper, we solve the problem based on the premise that 70\% of the incoming traffic goes through, 20\% turns right, and 10\% turns left. It should be noted that the proposed approach can deal with any movements, and this origin-destination matrix was selected for illustration purposes only. For a given vehicle, the general vehicle dynamics can be easily depicted from Fig. 2. The corresponding equations of motion are

$$
\begin{aligned}
& \dot{x}(t)=V(t) \cos \theta(t) \\
& \dot{y}(t)=V(t) \sin \theta(t) \\
& \dot{V}(t)=\alpha_{1}(t) \\
& \dot{\theta}(t)=\alpha_{2}(t)
\end{aligned}
$$

where $\alpha_{1}$ and $\alpha_{2}$ are scalar control inputs that govern the rate of change of the vehicle velocity $v$ and its orientation $\theta$ with respect to the horizontal axis (Fig. 2). These equations of motion can be linearized efficiently. This can be achieved by incorporating the geometry of the road in these equations. If the position of the vehicles is considered along the path and its velocity is assumed to be always tangent to this path then the Eqs. (1) can be simplified to the following linear form:

$$
\begin{aligned}
& \dot{S}(t)=V(t) \\
& \dot{V}(t)=\alpha_{1}(t)
\end{aligned}
$$

From this point on, we refer to $\alpha_{1}(t)$ as $\alpha(t)$ (i.e., $\alpha_{1}(t) \equiv \alpha(t)$ ), and we discard the control parameter $\alpha_{2}(t)$ since the vehicle will be following the road alignment at all times. Using the scalar quantities, $S(t)$ and $V(t)$, we introduce the state vector $X(t)=\binom{S(t)}{V(t)}$ to rewrite the equations of motion as

$$
\dot{X}(t)=\phi(X(t), \alpha(t))
$$

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-03.jpg?height=449&width=752&top_left_y=1882&top_left_x=562)
Fig. 2. Schematic of a vehicle in motion along a path and the change of coordinates.

where $\phi$ is a linear function.

$$
\dot{X}(t)=A X(t)+B \alpha(t)=\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)\binom{S(t)}{V(t)}+\binom{0}{1} \alpha(t)
$$

In this effort, we attempt to find the control parameter $\alpha(t)$ such that, given initial conditions $X\left(t_{i}\right)=X^{0}$, the car dynamics evolve according to Eq. (3) and arrive at the final state $X\left(t_{f}\right)=X^{1}$ while minimizing the cost function

$$
\zeta[\alpha(t)]=\int_{t_{i}}^{t_{f}}\left[1+\alpha(t)^{2}\right] d t
$$

where $t_{i}$ and $t_{f}$ are initial and final time and, therefore, $t_{f}-t_{i}$ is the journey time. The choice of this cost function is motivated by the results of Bichiou et al. (2016). This cost functional aims at finding the control sequence that minimizes the trip time while at the same time minimize the control energy. Minimizing the controls energy has direct consequence on the trip comfort. Passengers will not experience aggressive accelerations.

For a typical vehicle there are a number of physical and kinematic constraints due, in part, to the presence of other vehicles on the road. In this paper, these constraints are (1) acceleration constraints, (2) a car-following model including collision avoidance, and (3) time constraints.

### 2.1. Acceleration constraints

For a typical vehicle, the maximum vehicle acceleration is computed as

$$
\alpha_{\max }=\frac{F-R}{m}
$$

where $F$ is the traction force; $R=R_{a}+R_{r}+R_{g}$ is the resistive force sum of the aerodynamic resistance $R_{a}$, the rolling resistance $R_{r}$, and the grade resistance $R_{g}$; and $m$ is the vehicle mass.

The traction force is defined in Eq. (7) (Zohdy and Rakha, 2014).

$$
F=\min \left(746 \eta_{d} f_{p} \frac{P}{v}, m_{t a} g \mu\right)
$$

where the factor 746 is used to convert horsepower to watts, $\eta_{d}$ is the drive-line efficiency, $f_{p}$ is the driver throttle input (i.e., a value between 0 and 1 ), $P$ is the vehicle power, $v$ is the vehicle velocity, $m_{t a}$ is the vehicle mass on the tractive axle, $\mu$ is the coefficient of road adhesion (set at 1.0 for dry conditions, 0.8 for a wet roads, and 0.6 for snowy conditions Rakha et al. (2001)), and $g$ is the gravitational acceleration.

The aerodynamic resistance force is defined by Eq. (8) (Zohdy and Rakha, 2014):

$$
R_{a}=\frac{1}{2} \rho C_{d} C_{h} A_{f} v^{2}
$$

where $\rho$ is the fluid density, $C_{d}$ is the car drag coefficient, $C_{h}$ is the altitude correction factor, and $A_{f}$ is the frontal area of the vehicle subjected to the flow.

The rolling resistance force is defined by Eq. (9) (Zohdy and Rakha, 2014):

$$
R_{r}=m g \frac{c_{r_{0}}}{1000}\left(c_{r_{1}} v+c_{r_{2}}\right)
$$

where $c_{r_{0}}, c_{r_{1}}$, and $c_{r_{2}}$ are the rolling resistance constants.
The grade resistance force is defined by Eq. (10) (Zohdy and Rakha, 2014):

$$
R_{g}=m g G
$$

where $G$ is the roadway grade. In this work, we neglect the grade resistance force by assuming $G=0$.
The maximum deceleration that can be experienced by a vehicle in this paper is assumed to be $5 \mathrm{~m} \mathrm{~s}^{-2}$. This value is a user input and is motivated by the results of Fadhloun et al. (2017). Consequently, the constraint associated with the longitudinal acceleration is given by Eq. (12).

$$
-5 \leqslant \alpha(t) \leqslant \frac{F-R}{m}
$$

This nonlinear constraint is represented in Fig. 3(a) by the hashed region. In order to simplify the problem formulation, and thus enhance the computational efficiency, we convexify this constraint and assume that it is represented by the colored domain in Fig. 3(b), i. e.

$$
-5 \leqslant \alpha(t) \leqslant a V+b=-\frac{4}{65} V+4
$$

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-05.jpg?height=421&width=1263&top_left_y=183&top_left_x=284)
Fig. 3. Convexification of the acceleration domain and the car-following minimum required distance.

The authors acknowledge that other convexifications are possible, specifically simplifications that do not make unfeasible states feasible. However, we opted for the linear form provided above since it is closest to the boundary (Table 1).

This simplification violates slightly the initial acceleration constraint. However, this simplification does not violate the maximum power value but rather assumes a slightly lower roadway resistance.
2.2. Car-following model (Rakha et al., 2009; Zohdy and Rakha, 2014)

In order to model the behavior of a vehicle with respect to its peers in a lane, we use the Rakha-Pasumarthy-Adjerid (RPA) car-following model (Rakha et al., 2009). This model is general and can model the car-following behavior of AVs by calibrating the AV parameters. The model combines the Van Aerde steady-state car-following model (Rakha and Crowther, 2002; Rakha, 2009) with collision avoidance constraints for non-steady state conditions. The RPA model predicts the minimum distance between two consecutive vehicles.

The expected distance between two consecutive vehicles $d$ at time $t+\Delta t$ needs to be greater than $\bar{d}$ (Eq. (13)) (reference Zohdy and Rakha, 2014; Rakha et al., 2009).

$$
d \geqslant \bar{d}=\min \left\{\begin{array}{l}
\max \left\{\begin{array}{l}
c_{1}+\frac{c_{2}}{v_{f}-v}+c_{3} v \\
\frac{v^{2}-\bar{v}^{2}}{2 d_{\max }}+c_{1}+\frac{c_{2}}{v_{f}} \text { if } v>\bar{v} \\
c_{1}+\frac{c_{2}}{v_{f}-\frac{1}{2}\left(v_{c}+v_{f}\right)}+\frac{1}{2} c_{3}\left(v_{c}+v_{f}\right)
\end{array}\right.
\end{array}\right.
$$

where, $v$ is the velocity of the vehicle under consideration; $\bar{v}$ is the velocity of the vehicle directly ahead of it in the same lane; $v_{f}$ is the free-flow speed; $v_{c}$ is the speed-at-capacity; $c_{1}=\frac{v_{f}}{k_{j} v_{c}^{2}}\left(2 v_{c}-v_{f}\right), c_{2}=\frac{v_{f}}{k_{j} v_{c}^{2}}\left(v_{f}-v_{c}\right)^{2}$, and $c_{3}=\left(\frac{1}{q_{c}}-\frac{v_{f}}{k_{j} v_{c}^{2}}\right)$ are the steady-state car-following model parameters; $k_{j}$ is the jam density; and $q_{c}$ is the lane saturation flow rate.

Since this constraint is also nonlinear, we need to simplify it (i.e., convexify it) so that the optimization process is performed in real-time (i. e., Fig. 3(b)). We obtain $\bar{d}^{*}$

$$
\bar{d}^{*}=c_{1}+\frac{c_{2}}{u f}+c_{3} v+a x v^{2}
$$

where $a x=\frac{(u c-u f)\left(-2 q c u c+k j u c^{2}-3 q c u f\right)}{2 k j q c u c^{2} u f^{2}}, d=S_{n-1}(t)-S_{n}(t) \geqslant \bar{d}^{*}$

Table 1
Vehicle physical model numerical parameters.
| Symbol | Value | Unit | Symbol | Value | Unit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\eta_{d}$ | 0.92 | - | G | 0 | deg. |
| P | 177 | $h p$ | $d_{\text {max }}$ | 5 | $\mathrm{m} \mathrm{s}^{-2}$ |
| $m_{t a}$ | 785 | kg | $v_{f}$ | 60 | $\frac{\mathrm{km}}{\mathrm{h}}$ |
| g | 9.8067 | $\mathrm{N} \mathrm{kg}^{-1}$ | $v_{c}$ | 38 | $\frac{\mathrm{km}}{\mathrm{h}}$ |
| $\mu$ | 0.6-1 | - | $k_{j}$ | 150 | $\frac{\mathrm{veh}}{\mathrm{km}}$ |
| $\rho$ | 1.225 | $\mathrm{kg} \mathrm{m}^{-3}$ | $q_{c}$ | 1700 | veh |
| $C_{d}$ | 0.3 | - | $e$ | 0 | - |
| $C_{h}$ | 1.0 | - | $f_{s}$ | 0.18 | - |
| $A_{f}$ | 2.32 | $\mathrm{m}^{2}$ | $f_{p}$ | 0.4-1.0 | - |
| $c_{r_{0}}$ | 1.75 | - | - | - | - |
| $c_{r_{1}}$ | 0.0328 | - | - | - | - |
| $c_{r_{2}}$ | 4.575 | - | - | - | - |
| $c_{r_{2}}$ | 4.575 | - | - | - | - |


Please cite this article in press as: Bichiou, Y.-Q.id.t.t.s.f.p.(.t.a.'d.w.u.t.'.t.f.c.a.c.i.n."./.>., Rakha, H.A. Real-time optimal intersection control system for automated/cooperative vehicles. International Journal of Transportation Science and Technology (2018), https://doi.org/ 10.1016/j.ijtst.2018.04.003

Alternately,

$$
S_{n}(t) \leqslant S_{n-1}^{*}(t)-\left(c_{1}+\frac{c_{2}}{u f}+c_{3} v+a x v^{2}\right)
$$

where $S_{n-1}^{*}(t)$ is a convex form of the time series associated with the vehicle in front. Eq. 15 is therefore a convex form and a simplification of the car-following model.

### 2.3. Time constraint

Since the vehicles cross a shared intersection with other vehicles (Fig. 1), it is imperative that specific time slots be assigned to each vehicle. In this paper, we consider only the time after which a zone $\left(z_{i}\right)$ is free (i.e., $t_{z_{i}}$ ); therefore, a vehicle must arrive at the zone $z_{i}$ at a time $t_{\text {zone }}$ entry and satisfy Eq. (16).

$$
t_{\text {zone entry }} \geqslant t_{z_{i}}
$$

Given the constraints defined in Sections 2.1, 2.2, and 2.3, specifically, the equation of motion (2), the objective function (5), the acceleration constraint (12), the car-following constraint (15), and the time constraint (16), we use Pontryagin minimum principle to formulate the optimal control problem that is solved in this paper for each vehicle:

$$
\begin{array}{cl}
\text { minimize } & \zeta[\alpha()]=\int_{t_{i}}^{t_{f}}\left[1+\alpha(t)^{2}\right] d t=\int_{t_{i}}^{t_{f}} \mathcal{L}(X, \alpha, t) d t \\
\text { subjected to } & \dot{S}=V \\
& \dot{V}=\alpha \\
& S\left(t_{f}\right)=\bar{S} \\
t_{z_{i}} \leqslant t_{\text {zone entry }} & \leqslant \infty \\
-5 \leqslant & \alpha \quad \leqslant a V+b \\
-\infty \leqslant S_{n}(t) & \leqslant S_{n-1}^{*}(t)-\left(c_{1}+\frac{c_{2}}{u f}+c_{3} v+a x v^{2}\right)
\end{array}
$$

where, $\bar{S}$ is the coordinate at the intersection. If we define

$$
C(X(t), \alpha(t))=\left(\begin{array}{l}
\alpha(t)-a V(t)-b \\
-\alpha(t)-5 \\
S_{n}(t)-S_{n-1}^{*}(t)+ \\
\left(c_{1}+\frac{c_{2}}{u f}+c_{3} v(t)+a x v(t)^{2}\right)
\end{array}\right)
$$

The Hamiltonian associated with this problem is

$$
H(X, \alpha)=\mathcal{L}(X(t), \alpha(t), t)+\lambda^{T} \phi(X(t), \alpha(t))+\boldsymbol{\kappa} C(X(t), \alpha(t))
$$

where $\lambda$ and $\boldsymbol{\kappa}$ are vectors of Lagrange multipliers. The ith component of $\boldsymbol{\kappa}$ is defined as follows:

$$
\kappa_{i}= \begin{cases}>0 & \text { for } C=0 \\ =0 & \text { for } C<0\end{cases}
$$

The optimality condition in this case is

$$
\alpha^{*}=\arg \min _{\alpha} H(X, \alpha) \mathcal{L}_{\alpha}\left(X, \alpha^{*}, t\right)+\lambda^{T} \phi_{\alpha}\left(X(t), \alpha^{*}\right)+\boldsymbol{\kappa} C_{\alpha}\left(X(t), \alpha^{*}\right) \equiv 0
$$

The equations for the co-states are

$$
\dot{\lambda}=-\nabla_{X} H(X, \alpha)= \begin{cases}-\nabla_{X} L-\lambda^{T} \nabla_{X} \phi-\boldsymbol{\kappa} \nabla_{X} C & \text { if } C=0 \\ -\nabla_{X} L-\lambda^{T} \nabla_{X} \phi & \text { if } C<0\end{cases}
$$

Since $S\left(t_{f}\right)$ is known, we have

$$
\lambda_{1}\left(t_{f}\right)=1
$$

The problem can be solved in theory using the Pontryagin minimum principle. For that purpose we can use the previous Eqs. (((2), (18)-(21)). However, obtaining an analytical solution is a difficult task; therefore, we solve this problem numerically. For this purpose we use the Model Predictive Control numerical method (MPC) (Rawlings and Mayne, 2009).

The system presented in (17) is discretized by introducing the MPC into the system presented in Eq. (22). The time interval is divided into equal-valued segments (i.e., $\Delta t$ ). $t_{i}$ is known a priori and $S_{\text {intersection }}$ is the coordinate of the beginning of the intersection. For each vehicle, the value of $V_{\text {Max }}^{\text {desired }}$ is chosen with respect to the trajectory arc the vehicle follows when

[^1]crossing the intersection. It is important to note here that, due to the presence of other vehicles and curves in the path (i.e., the vehicle turns left or right at the intersection and decelerates if it approaches another vehicle), the acceleration $\alpha$ cannot be zero throughout the prediction horizon. Thus the trivial solution to this optimization problem cannot be considered.

This problem has three main inputs: (1) The time after which the conflict zones are free. This input is important since it will prevent collisions from occurring at the intersection (2) The time series for the vehicle in front, specifically, a convex form of $S_{n-1}(t), S_{n-1}^{*}(t)$. This input is also important since it will prevent the current vehicle (which the optimizer is solving for) from colliding with the vehicle in front of it before arriving at the intersection (3) Since the trip duration is not known a priori, $t_{f}$, an estimate of the control horizon, is needed. This unknown is cast into $N$, which is the number of temporal intervals. The equations of motion become algebraic equations. An estimate of $N$ is needed to achieve a feasible solution. Once the value of $N$ is estimated, a fast and convex optimization is performed. This optimization can be conducted in real-time to obtain a solution. Under this form, the optimal control problem becomes a simple convex optimization problem. The Pontryagin minimum principle is used to formulate the problem while a discrete and convex optimization solves the problem. The presented formulation (22) is solved numerically using CVXR (Grant and Boyd, 2014; Grant and Boyd, 2008):

$$
\begin{aligned}
\text { minimize } & \zeta[\alpha()]=\sum_{i=1}^{N}\left[1+\alpha(i)^{2}\right] \Delta t \\
\text { subjected to } & \left(\begin{array}{c}
\chi[1] \\
\cdot \\
\chi[N]
\end{array}\right)=\left(\begin{array}{c}
\bar{A} \\
\cdot \\
\cdot \\
\bar{A}^{N}
\end{array}\right) \chi[0]+\left(\begin{array}{cccc}
\bar{B} & 0 & 0 & 0 \\
\cdot & \cdot & 0 & 0 \\
\bar{A}^{N-2} \bar{B} & \cdot & \cdot & 0 \\
\bar{A}^{N-1} \bar{B} & \bar{A}^{N-2} \bar{B} & \cdot & \bar{B}
\end{array}\right) \cdot\left(\begin{array}{c}
\alpha[0] \\
\cdot \\
\cdot \\
\alpha[N-1]
\end{array}\right) \\
\chi[N]== & (\bar{S} \bar{V})^{T} \\
S_{\text {intersection }}= & \text { value } \\
V_{\text {arbitrary }} \leqslant & V_{\text {Max }}^{\text {desired }} \\
t_{z_{i}}-t_{0} \leqslant & N . \Delta t \\
-5 \leqslant & \alpha(i) \\
-\infty \leqslant & \leqslant a V(i)+b \\
& \leqslant S_{n-1}^{*}(i)- \\
& \left(c_{1}+\frac{c_{2}}{u f}+c_{3} v(i)+a x v(i)^{2}\right)
\end{aligned}
$$

where, $\bar{V}$ is an arbitrary velocity,

$$
\bar{A}=\left(\begin{array}{cc}
1 & \Delta t \\
0 & 1
\end{array}\right)
$$

and

$$
\bar{B}=\binom{\frac{1}{2} \Delta t^{2}}{\Delta t}
$$

After solving the previous convex optimization problem (22), we obtain the vehicle trajectory, velocity, and acceleration. We use this information to compute the fuel consumed by each vehicle using the VT-Micro model, utilizing Eq. (25) (Ahn et al., 2001, 2002; Rakha et al., 2004).

$$
F C(t)= \begin{cases}e^{\sum_{i=0}^{3} \sum_{j=0}^{3} L_{i j}^{e} v^{i} a^{j}} & \text { for } a \geqslant 0 \\ e^{\sum_{i=0}^{3} \sum_{j=0}^{3} M_{i j}^{e} v^{i} a^{j}} & \text { for } a<0\end{cases}
$$

where $L_{i j}^{e}$ are the model coefficients at speed power $i$ and acceleration power $j$ for positive accelerations, $M_{i j}^{e}$ are the model coefficients at speed power $i$ and acceleration power $j$ for negative accelerations, $v$ is the instantaneous speed, and $a$ is the instantaneous acceleration. In this study, the Oakridge National Lab (ORNL) composite vehicle parameters were used.

It is also important to note that the solution to the simplified problem (22) is expected to deliver a relevant approximation to the solution of the nonlinear problem (17). This implies that it can be an under or over-estimate of the true optimum.

## 3. Results and discussion

Before we perform the various simulations for an intersection considering various levels of congestion, it is important to determine and/or select the value for $\Delta t$. Fig. 4 presents the velocity time series for various $\Delta t$ values associated with a vehicle going forward through an intersection and where there is no vehicle in front of it. We expect in this case that the vehicle will reach the maximum allowed velocity. For this particular example this velocity is $10 \mathrm{~m} / \mathrm{s}$. It is noted that for $\Delta t$ values beyond 0.3 the velocity profile is distorted. For $\Delta t$ values of 0.3 and lower we notice that the time series start converging

[^2]to the actual velocity profile (i.e. associated with $\Delta t=0.005$ ). However, for $\Delta t=0.1 . .0 .3$ the initial condition associated with this example which is $V(t=0)=1 \mathrm{~m} / \mathrm{s}$ is not exactly captured. Nevertheless, we choose the value of $\Delta t=0.1(\mathrm{~s})$. This choice is motivated by the fact that (1) the associated precision is acceptable (2) most systems incorporated in vehicles function in deci-seconds, and (3) the size of the obtained system is moderate (i.e. for this particular example we have $N=331$ ).

In this paper, the intersection consisted of a major roadway and a minor roadway, where the arrival rates on the minor roadway were always half the flow of the major arterial. The flows along the major arterial ranged from 500 to 1200 veh/h, 10\% of which were modeled as turning left and 20\% of which were modeled turning right at the intersection. The base saturation flow rate of the roadway was 1700 veh/h. Given that the capacity was much less than the saturation flow rate, the intersection experienced over-saturation delay in a number of scenarios. This paper focuses on Optimal Control Effort - real time (OCRT), which attempts to obtain a solution that reduces the delay while at the same time minimizing the control effort (i.e., avoid aggressive acceleration levels to ensure that the ride is comfortable for the passengers).

The results of the introduced logic were compared to the results obtained when the optimal control was solved, including all nonlinear constraints (Bichiou et al., 2016) (i.e., Optimal Control Nonlinear (OCN)) and when the intersection was controlled by a roundabout (R), a stop sign (SS), and a traffic signal (TL). It should be noted that a two-phase plan was used to control the traffic signal, since it performed better than other plans. The results of the R, SS, and TL approaches were obtained using the INTEGRATION software and using identical input. The same input was used to model vehicles crossing the intersection using the introduced logic. It should be noted that the INTEGRATION software also uses the RPA carfollowing and acceleration models that are embedded in the proposed algorithm.

Fig. 5-8 present the mean delay, fuel consumption, stops (using Eq. (26)), and $\mathrm{CO}_{2}$ emissions for the entire intersection. The results suggest a general improvement in the mentioned quantities.

$$
s=\sum_{i=1}^{N} \frac{v(i \Delta t)-v((i+1) \Delta t)}{v_{f}} \quad \forall v(i \Delta t)>v((i+1) \Delta t)
$$

Fig. 5 presents the computed delay. It is noted that the OCRT results in lower delays, far better than the roundabout, and is the best among the other intersection control strategies. The benefits of the proposed approach are demonstrated and a true optimality is obtained. Specifically, the delay of approximately 6 s for OCRT is significantly lower than the delay of 76 s for the roundabout-controlled intersection. Fig. 9(a) illustrates the percentage reduction in vehicle delay compared to a roundabout-controlled intersection for both versions of the proposed algorithm. On average the delay is reduced by more than 55\% for OCRT.

Fig. 6 illustrates the mean fuel consumption computed for all vehicles traversing the intersection. An all-way stop controlled intersection produces the highest fuel consumption levels. The fuel consumption caused by the proposed algorithm is insensitive to the demand level (approximately 0.133 L for OCRT and OCN). The intersection equipped with a traffic signal produces a fuel consumption of 0.280 L, and a roundabout produces a fuel consumption level of 0.226 L. The optimality of the new approach leads to lower fuel consumption values.

Fig. 7 presents the mean number of vehicle stops computed using Eq. (26). The computed stops for the proposed algorithm remain fairly constant (i.e, approximately 0.3 stops for OCRT and OCN) in comparison with the roundabout, for which stops increase from 0.3 to 0.95 as the level of congestion increases. It is noted that the value of the stops for an intersection equipped with a stop sign are slightly below 1.0 for high demand levels. This is due to the fact that the queue spills back close to the entry point for high demand levels, and thus vehicles enter the control zone at speeds below the speed limit.

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-08.jpg?height=657&width=1501&top_left_y=1692&top_left_x=199)
Fig. 4. (a) Velocity profile for a vehicle going through an intersection and (b) window zoom for the same velocity profile.

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-09.jpg?height=590&width=739&top_left_y=193&top_left_x=566)
Fig. 5. Mean delay in seconds for an intersection equipped with various control mechanisms and various flow rates.

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-09.jpg?height=633&width=735&top_left_y=927&top_left_x=568)
Fig. 6. Mean fuel consumption in liters for an intersection equipped with various control mechanisms and various flow rates.

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-09.jpg?height=590&width=737&top_left_y=1701&top_left_x=568)
Fig. 7. Mean stop for an intersection equipped with various control mechanisms and various flow rates.

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-10.jpg?height=590&width=741&top_left_y=191&top_left_x=580)
Fig. 8. Mean $\mathrm{CO}_{2}$ emissions in grams for an intersection equipped with various control mechanisms and various flow rates.

![](https://cdn.mathpix.com/cropped/28a53d12-d6f1-4996-87eb-884980fb9d30-10.jpg?height=1439&width=1485&top_left_y=911&top_left_x=203)
Fig. 9. Percentage reduction in (a) delay, (b) stops, (c) fuel consumption, and (d) $\mathrm{CO}_{2}$ emissions for OCRT and OCN in comparison to a roundabout.

Fig. 8 presents the computed mean $\mathrm{CO}_{2}$ emissions for the vehicles and for the different intersections. It is noted that the proposed algorithm results in lower $\mathrm{CO}_{2}$ emissions (i.e., 286 g for OCRT) when compared to other control algorithms. The roundabout produces the minimum $\mathrm{CO}_{2}$ emissions compared to the other control strategies (i.e., 446 g).

Fig. 9(a), (b), and (c) present the percentage gained or lost in terms of delay, vehilce stops, fuel consumption, and $\mathrm{CO}_{2}$ emissions with the new proposed control system in comparison to the roundabout. From the previous results and Fig. 9, we note that OCRT is better than OCN in terms of delay values. On average, OCRT results in $35 \%$ less delay compared to OCN. This reduction is, however associated with the higher fuel consumption levels (i.e., +13\%) and $\mathrm{CO}_{2}$ emissions (i.e., +9\%). Consequently, the OCN may offer a better intersection controller.

The proposed algorithm has one main disadvantage that needs further improvement: namely, a proper estimate of the final time (i.e., the time when the vehicle is expected to reach the intersection). A proper estimate of $t_{f}$ or $N$ would enhance this logic further, and thus further work is planned in this regard.

Noteworthy is the fact that for a signalized intersection the approach capacity equals the saturation flow rate multiplied by the ratio of the effective green time to the cycle length. If we assume a phase split of $67: 33$ percent for the main and minor streets (given that the major street carries double the minor street flow), the capacity of the major approach would be $1062 \frac{\mathrm{veh}}{\mathrm{h}}$ and that for the minor street approach would be $531 \frac{\mathrm{veh}}{\mathrm{h}}$. For the newly introduced logic, we solve for a flow rate of up to $1200 \frac{\mathrm{veh}}{\mathrm{h}}$ along the main road and $600 \frac{\mathrm{veh}}{\mathrm{h}}$ along the minor road and thus demonstrate the algorithm is able to deal with what would be over-saturated conditions. The introduced logic, in this case, discharges more vehicles while having a substantial reduction in delay.

## 4. Conclusions

An enhancement of a novel intersection management algorithm that is derived from optimal control theory was developed for the control of automated and connected vehicles. The developed algorithm was tested and compared to other intersection control strategies, including a roundabout, an all-way stop sign, and a traffic-signal-controlled intersection. The results of this enhanced version were compared to the nonlinear optimization algorithm. It was deduced that the small reduction in precision justifies the reduction in computational cost. The results also show that the proposed algorithm outperforms the other intersection control strategies, producing lower delays and $\mathrm{CO}_{2}$ emissions with reductions of up to 55\% and $40 \%$, respectively, relative to the best intersection control strategy (in this case the roundabout). It was also noted that the chosen objective function to be minimized focuses only on reducing the trip time and the acceleration energy. This led to solutions having low delays and smooth accelerations. The reduction in vehicle fuel consumption and $\mathrm{CO}_{2}$ emissions is a byproduct of this optimization. This is justified by the elimination of aggressive acceleration maneuvers, which in turn will undeniably reduce the amount of fuel consumed by the vehicle. Other weighted objective functions are expected to lead to a trade-off between the different quantities (delay, stops, emissions, and fuel consumed). This will be implemented in future work.

This effort, however, has one drawback, namely that an estimate of the time the vehicle reaches the intersection is required in order to compute the solution. Once that is achieved, a real-time solution is obtained through convex optimization. Initial estimates of the arrival times can be used based on historical data.

## Acknowledgements

This effort was funded by the Connected Vehicle Initiative University Transportation Center (CVI-UTC) and the TranLIVE UTC.

## Appendix A. Supplementary data

Supplementary data associated with this article can be found, in the online version, at https://doi.org/10.1016/j.ijtst. 2018.04.003.

## References

Abdul Aziz, H.M., Ukkusuri, S.V., 2012. Unified framework for dynamic traffic assignment and signal control with cell transmission model. Transp. Res. Board (2311), 73-84.
Ahn, K., Rakha, H., Trani, A., Van Aerde, M., 2001. Estimating vehicle fuel consumption and emissions based on instantaneous speed and acceleration levels. ASCE J. Transp. Eng.
Ahn, K., Rakha, H., Trani, A., Van Aerde, M., 2002. Estimating vehicle fuel consumption and emissions based on instantaneous speed and acceleration levels. J. Transp. Eng. 128 (2), 182-190.
Azimi, R., Bhatia, G., Rajkumar, R., Mudalige, P., 2013. Reliable intersection protocols using vehicular networks. 2013 Cyber Physical Systems.
Bichiou, Y., Rakha, H.A., Roman, A., 2016. Developing an optimal intersection control system for automated connected vehicles. Submitted to IEEE Trans. Fadhloun, K., Rakha, H., Abdelkafi, A., Loulizi, A., 2017. An enhanced rakha-pasumarthy-adjerid car-following model accounting for human behavior. In: Transportation Research Board 96th Annual Meeting.
Fortelle, A., 2015. Coordination of automated vehicles at intersections: decision, efficiency and control. In: 2015 IEEE 18th International Conference on Intelligent Transportation Systems.

Grant, M., Boyd, S., 2008. Graph implementations for nonsmooth convex programs. In: Blondel, V., Boyd, S., Kimura, H. (Eds.), Recent Advances in Learning and Control. Lecture Notes in Control and Information Sciences. Springer-Verlag Limited, pp. 95-110. Url:http://stanford.edu/boyd/graphdcp.html.
Grant, M., Boyd, S., 2014. CVX: matlab software for disciplined convex programming, version 2.1. http://cvxr.com/cvx.
Gratner, A., Stefan, A., 2016. Probabilistic Collision Estimation System for Autonomous Vehicles (Ph.D. thesis). KTH Royal Institute of Technology, School of Industrial Engineering and Management, Stockholm, Sweden.
Le, T., Vu, H.L., Nazarathy, Y., Vo, B., Hoogendoorn, S., 2013. Linear-quadratic model predictive control for urban traffic networks. Social Behav. Sci. (80), 512-530
Lee, J., Park, B.B., 2011. Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment. In: 2011 IEEE Transactions on Intelligent Transportation Systems.
Li, L., 2006. Cooperative driving at blind crossings using intervehicle communication. In: 2006 IEEE Transaction on Vehicular Technology.
Li, Z., Chitturi, M., Zheng, D., Bill, A., Noyce, D., 2013. Modeling reservation-based autonomous intersection control in vissim. Transp. Res. Board (2381), 81-90.
Massera, C.M., Terra, M.H., Wolf, D.F., 2016. Safely optimizing highway traffic with robust model predictive control-based cooperative adaptive cruise control. IEEE Trans. Intell. Transp. Syst.
Medina, A.I.M., Wouw, N., Nijmeijer, H., 2015. Automation of a t-intersection using virtual platoons of cooperative autonomous vehicles. In: 2015 IEEE 18th International Conference on Intelligent Transportation Systems.
Rakha, H., 2009. Validation of van aerde's simplified steadystate car-following and traffic stream model. Transp. Lett. 1 (3), 227-244.
Rakha, H., Ahn, K., Trani, A., 2004. Development of vt-micro model for estimating hot stabilized light duty vehicle and truck emissions. Transp. Res. Part D: Transp. Environ. 9 (1), 49-74.
Rakha, H., Crowther, B., 2002. Comparison of Greenshields, Pipes, and Van Eerde Car-following and Traffic Stream Models. Transportation Research Record: Transportation Research Board, National Research Council, Washington, D.C..
Rakha, H., Kamalanathsarma, R.K., 2011. Eco-driving at signalized intersections using v2i communication. In: 2011 14th International IEEE Annual Conference on Intelligent Transportation Systems.
Rakha, H., Lucic, I., Demarchi, S.H., Setti, J.R., Aerde, M.V., 2001. Vehicle dynamics model for predicting maximum truck acceleration levels. J. Transp. Eng. 127 (5), 418-425.
Rakha, H., Pasumarthy, P., Adjerid, S., 2009. A simplified behavioral vehicle longitudinal motion model. Transp. Lett. 1 (2), 95-110.
Rawlings, J.B., Mayne, D.Q., 2009. Model Predictive Control: Theory and Design. Nob Hill.
Roozemond, D.A., 2001. Using intelligent agents for pro-active, real-time urban intersection control. Oper. Res. Int. J. 131, 293-301.
Ye, B.-L., Wu, W., Mao, W., 2015. Distributed model predictive control method for optimal coordination of signal splits in urban traffic networks. Asian J. Control 17, 775-790.
Zhu, M., Li, X., Huang, H., Kong, L., Li, M., Wu, M.-Y., 2009. Licp: A look-ahead intersection control policy with intelligent vehicles. In: IEEE 6th International Conference on Mobile Adhoc and Sensor Systems.
Zohdy, I.H., Rakha, H., 2012. Game theory algorithm for intersection-based cooperative adaptive cruise control (cacc) systems. In: 2012 15th International IEEE Conference on Intelligent Transportation Systems.
Zohdy, I.H., Rakha, H., 2014. Intersection management via vehicle connectivity: The intersection cooperative adaptive cruise control system concept. J. Intell. Transp. Syst.: Technol. Planning Oper.


[^0]:    * Corresponding author at: Center for Sustainable Mobility at the Virginia Tech Transportation Institute, 3500 Transportation Research Plaza, Virginia Tech, Blacksburg, VA 24061, United States.
    E-mail addresses: youssef1@vt.edu (Youssef Bichiou), hrakha@vt.edu (H.A. Rakha).

[^1]:    Please cite this article in press as: Bichiou, Y.-Q.id.t.t.s.f.p.(.t.a.'d.w.u.t.'.t.f.P.c.a.c.i.n.".|.>., Rakha, H.A. Real-time optimal intersection control system for automated/cooperative vehicles. International Journal of Transportation Science and Technology (2018), https://doi.org/ 10.1016/j.ijtst.2018.04.003

[^2]:    Please cite this article in press as: Bichiou, Y.-Q.id.t.t.s.f.p.(.t.a.'d.w.u.t.'.t.f.c.a.c.i.n."./.>., Rakha, H.A. Real-time optimal intersection control system for automated/cooperative vehicles. International Journal of Transportation Science and Technology (2018), https://doi.org/ 10.1016/j.ijtst.2018.04.003

