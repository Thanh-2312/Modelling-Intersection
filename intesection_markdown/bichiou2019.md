# Developing an Optimal Intersection Control System for Automated Connected Vehicles 

Youssef Bichiou and Hesham A. Rakha ${ }^{\text {(iD) }}$, Member, IEEE


#### Abstract

In recent years, automated vehicles (AVs) are emerging as a realistic and viable option. Consequently, substantial research efforts are being dedicated to the development of systems and technologies for the field implementation of AVs. One of the challenges researchers need to address is how to optimize the movement of AVs through roadway intersections. In this paper, an attempt to address this need is introduced. The developed model is an optimization problem subjected to dynamical constraints (i.e., ordinary differential equations governing the motion of a vehicle) and static constraints (i.e., maximum achievable velocities). By virtue of Pontryagin's minimum principle, the solution that minimizes the trip time is obtained. Given the problem parameters, the solution to the formulated problem is expected to be the true optimum and delivers the lowest possible delay that satisfies the previously mentioned constraints. This logic is simulated and compared with the operation of a roundabout, a stop sign, and a traffic signal-controlled intersection. The results demonstrate that an $80 \%$ reduction in delay is achievable compared with the best of these three intersection control strategies, on average. An interesting byproduct of this new logic is a reduction in vehicular fuel consumption and $\mathbf{C O}_{\mathbf{2}}$ emissions by $\mathbf{4 2 . 5 \%}$ and $\mathbf{4 0 \%}$, respectively.


Index Terms-Automated/cooperative vehicles, optimal control, roadway intersection, mobility, vehicular delay, $\mathbf{C O}_{\mathbf{2}}$ emissions.

## I. Introduction

SINCE the introduction of control theory and its introduction to real-time applications, numerous systems, previously requiring human intervention, have and are becoming more automated. Examples of these systems include roadway vehicles. In recent years, computers became integral components of vehicles with various tasks being handled automatically. Substantial research efforts are being dedicated to the enhancement of this technology [1]-[6]. The ultimate goal behind this trend is to make vehicles automated. The principal motivation behind this effort is the expected safety, economic and mobility advantages associated with the introduction of automated vehicles. At this stage various prototypes do exist.

[^0]However, the technology implemented is still not mature enough for mass field implementation. Considerable development in algorithms is required so that the vehicle performs as expected when facing any predicted or unpredicted situations. Substantial field testing on closed and open roads is needed to validate these newly developed algorithms. The legislative side of the matter is also a challenge. For example, who would be accountable in case of incidents and to whom or what a driver license should be given?

One of the most challenging scenarios that researchers need to address is how an automated vehicle should behave in an intersection and cross it optimally so that the delay is minimized and the system mobility is enhanced. Numerous solutions for this problem were and are still being developed. One of these solutions is the Cooperative Adaptive Cruise Control (CACC) system and particularly its intersection version (iCACC) [7]. The main objective of this system is to optimize vehicle trajectories while at the same time reduce delay. The optimality characteristic of this method for this particular situation is not proven. Medina et al. [8] tried to address this issue for a T-intersection. A mathematical model was developed and linearized. Collision avoidance was implemented but no dynamic constraints were used: acceleration constraints and velocity constraints. The authors were successful in solving this problem for six vehicles only. Gratner and Stefan [9] simulated a T-Intersection where only two vehicles were present. The study did not consider the effects of other vehicles on the road (i.e., there is no car-following model). The aim was to develop a collision prediction system. The computational burden of the system prevents it from being real-time and thus responsive in a dynamic environment. The developed model features static constraints on accelerations and nonlinear equations of motion. Zhu et al. [10] developed a methodology for making vehicles cross an intersection cooperatively by computing the required speed. Their paper focuses on scheduling and no developed dynamic model was provided. Li et al. [11] developed a reservation-based autonomous intersection control in VISSIM. The tool uses purely kinematic equations, and the vehicles communicate only with a centralized intersection controller. This controller determines the passing sequence of the approaching vehicles on a first-come, first-served basis. Dresner and Stone [12] presented a multi-agent approach to autonomous intersection management. They developed a simulation environment to show the benefits of their system. The principal limitation of their work is the lack of physical models surrounding the behavior of real vehicles. For instance, there was no car-following logic, the turn rate of the vehicles is not capped by specific constraints, there is no dynamic model
implemented that limits the acceleration and deceleration rates of the vehicles, and there is no optimization of the vehicle movement. In fact only kinematic equations were used. There was also a lot of emphasis on communication, message loss and/or corruption. A communication protocol was developed.

In this paper, a comprehensive and extended car model is proposed. The present work is the first to consider a fully comprehensive and nonlinear vehicle dynamics model. The behavior of a vehicle is modeled using nonlinear equations of motion. Nonlinear kinematic and dynamic constraints are accounted for. For example, bounds on vehicle velocity and accelerations are included [7]. The interaction with the road and other vehicles on the road is also accounted for. The car-following and collision avoidance model are also included [7], [13]. The roadway surface and vehicle tire conditions are also accounted for [14]. The $\mathrm{CO}_{2}$ and fuel consumption levels are also computed as part of the results. The change of the vehicle state as its evolution from initial conditions to desired and/or unknown future conditions is computed using optimal control theory, which guarantees the computation of a true optimal and best solution, given the problem parameters. This process is done with the help of a scheduler placed at the intersection. This scheduler allocates time slots for each vehicle to cross conflict zones in the intersection. Perfect communication between the vehicles themselves and between the scheduler and vehicles is assumed. The past, current and expected future velocity, position and acceleration as a function of time is shared between the different entities located and approaching the intersection. This information is also provided to the scheduler. Simulations are performed for an intersection that has one major and one minor roadway. The developed model was tested under various traffic conditions. The traffic inflows range from 500 veh/h to a maximum of 1200 veh/h for a roadway saturation flow rate $q_{c}$ of 1700 veh/h. The traffic inflows for the minor roadway range from 250 veh/h to 600 veh/h. Detailed vehicle information is captured during the simulation: velocity, acceleration, delay, $\mathrm{CO}_{2}$ emissions, fuel consumption, etc.

In summary, in this paper, we introduce a new comprehensive system that has optimality built in from the start, considers the system's kinematics and dynamics and is expected to deliver the best solution for vehicles crossing an intersection, given the problem formulation (i.e. constraints).

## A. Study Objective and Paper Layout

In this paper, a novel algorithm is developed to compute an optimal solution for each possible scenario a vehicle may encounter while traversing a roadway intersection. In this paper only single lane intersections are considered. This algorithm uses optimal control theory that guarantees the true optimality of the solution. The features of these systems include:

1) A dynamical system describing the motion of the vehicle: use of vehicle characteristics such as engine power, mass, fuel consumption model, physical acceleration and deceleration constraints that account for roadway surface and vehicle tire conditions;
2) Accounting for weather conditions (i.e. change in the road adhesion parameters);

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-2.jpg?height=574&width=756&top_left_y=202&top_left_x=1139)
Fig. 1. Schematics of a typical intersection.

3) Solving the trajectories for the four immediate vehicles at the intersection (i.e. one cycle);
4) Accounting for singular cases where the vehicle has to stop at the intersection and defer it to the next computational cycle.

In Section 2, we present the developed model for a vehicle traversing an intersection with all its dynamic and kinematic constraints. In Section 3, the obtained results in terms of vehicle delay, stops, fuel consumption levels and emissions are presented. In Section 4, the concluding remarks and a discussion of further research directions is presented.

## II. Model Description

In this paper, we consider the intersection given in Figure 1. Each vehicle represented in this Figure has three possible routes: through, left or right. These routes proceed through "conflict zones". A number of vehicles will share these zones and thus the solution to the proposed problem will feature an occupancy time slot allocation for each of these zones. For a given vehicle, the general dynamics can be easily depicted from Figure 3. The corresponding equations of motion are

$$
\begin{aligned}
\dot{x}(t) & =v(t) \cos \theta(t) \\
\dot{y}(t) & =v(t) \sin \theta(t) \\
\dot{v}(t) & =\alpha_{1}(t) \\
\dot{\theta}(t) & =\frac{\alpha_{2}(t)}{v(t)}
\end{aligned}
$$

where $\alpha_{1}$ and $\alpha_{2}$ are control inputs that govern the rate of change of the vehicle velocity $v$ and its vector orientation $\theta$ with respect to the horizontal axis (Figure 3). To simplify the notation, we use the state vector $X=(x y v \theta)^{T}$ and the control vector $\boldsymbol{\alpha}=\left(\alpha_{1} \alpha_{2}\right)^{T}$ and re-write the equations of motion as

$$
\dot{X}=f(X, \boldsymbol{\alpha})
$$

In this effort, we attempt to find the control vector $\boldsymbol{\alpha}(t)=\left(\alpha_{1}(t) \alpha_{2}(t)\right)^{T}$ such that, given the initial conditions $X\left(t_{i}\right)=X^{0}$, the car dynamics evolve according to equation 2 and arrive at the final state $X\left(t_{f}\right)=X^{1}$ while minimizing the cost function shown in Equation 3.

$$
P[\boldsymbol{\alpha}()]=\int_{t_{i}}^{t_{f}} d t=t_{f}-t_{i}
$$

where $t_{i}$ and $t_{f}$ are the initial and the final time of the trip and thus $t_{f}-t_{i}$ is the journey time. This problem is referred to as the time optimal control problem. In this paper, we will focus only on minimizing the travel time and travel time combined with the control effort. Nevertheless, other objective functions could be used.

For a typical vehicle there are a number of physical and kinematic constraints due, in part, to the presence of other vehicles sharing the road. In this paper, these constraints are (1) acceleration constraints, (2) a car-following model including collision avoidance constraints and (3) time constraints.

## A. Acceleration Constraints

For a typical vehicle, the maximum vehicle acceleration is computed as

$$
\alpha_{1_{\max }}=\frac{F-R}{m}
$$

where $F$ is the traction force, $R=R_{a}+R_{r}+R_{g}$ is the resistive force sum of the aerodynamic resistance $R_{a}$, the rolling resistance $R_{r}$ and the grade resistance $R_{g}$ and $m$ is the vehicle mass.

The traction force is defined in equation 5.

$$
F=\min \left(767 \eta_{d} f_{p} \frac{P}{v}, m_{t a} g \mu\right)
$$

where $\eta_{d}$ is the drive-line efficiency, $f_{p}$ is the driver throttle input (i.e. a value between 0 and 1 ), $P$ is the vehicle power, $v$ is the vehicle velocity, $m_{t a}$ is the vehicle mass on the tractive axle, $\mu$ is the coefficient of road adhesion (set at 1.0 for dry conditions, 0.8 for a wet roads and 0.6 for snowy conditions [14]) and $g$ is the gravitational acceleration.

The aerodynamic resistance force is defined by equation 6

$$
R_{a}=\frac{1}{2} \rho C_{d} C_{h} A_{f} v^{2}
$$

where $\rho$ is the fluid density, $C_{d}$ is the car drag coefficient, $C_{h}$ is the altitude correction factor and $A_{f}$ is the frontal area of the vehicle subjected to the air flow.

The rolling resistance force is defined by equation 7

$$
R_{r}=m g \frac{c_{r_{0}}}{1000}\left(c_{r_{1}} v+c_{r_{2}}\right)
$$

where $c_{r_{0}}, c_{r_{1}}$ and $c_{r_{2}}$ are the rolling resistance constants.
The grade resistance force is defined by equation 8

$$
R_{g}=m g G
$$

where $G$ is the roadway grade. In this work, we neglect the grade resistance force by assuming $G=0$.

The maximum deceleration that can be experienced by a vehicle in this paper is assumed to be $5 m . s^{-2}$. Consequently, the constraint associated with the longitudinal acceleration is given by equation 9 (Figure 2).

$$
-5 \leq \alpha_{1}(t) \leq \frac{F-R}{m}
$$

When the vehicle is making a turn, the minimum radius of curvature $R d$ is given by equation 10 [15]

$$
R d=\frac{v^{2}}{g\left(e+f_{s}\right)}
$$

TABLE I
Vehicle Physical Model Numerical Parameters
| Symbol | Value | Unit | Symbol | Value | Unit |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\eta_{d}$ | 0.92 | - | G | 0 | degrees |
| P | 177 | $h p$ | $d_{\text {max }}$ | 5 | $m . s^{-2}$ |
| $m_{t a}$ | 785 | kg | $v_{f}$ | 60 | $\frac{k m}{h}$ |
| g | 9.8067 | $N . k g^{-1}$ | $v_{c}$ | 38 | $\frac{k m}{h}$ |
| $\mu$ | 1, 0.8, 0.6 | - | $k_{j}$ | 150 | $\frac{v e h}{k m}$ |
| $\rho$ | 1.225 | $\mathrm{kg} . \mathrm{m}^{-3}$ | $q_{c}$ | 1700 | $\frac{v e h}{h}$ |
| $C_{d}$ | 0.3 | - | $e$ | 0 | - |
| $C_{h}$ | 1.0 | - | $f_{s}$ | 0.18 | - |
| $A_{f}$ | 2.32 | $m^{2}$ | $\alpha_{0}$ | $4.89 \times 10^{-4}$ | - |
| $c_{r_{0}}$ | 1.75 | - | $\alpha_{1}$ | $4.29 \times 10^{-4}$ | - |
| $c_{r_{1}}$ | 0.0328 | - | $\alpha_{2}$ | $10^{-6}$ | - |
| $c_{r_{2}}$ | 4.575 | - | $f_{p}$ | 0.4-1.0 | - |


![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-3.jpg?height=346&width=589&top_left_y=776&top_left_x=1222)
Fig. 2. Feasible acceleration values.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-3.jpg?height=486&width=561&top_left_y=1207&top_left_x=1238)
Fig. 3. Schematic of vehicle in motion along a path.

where $e$ is the super elevation and $f_{s}$ is the coefficient of side friction.

The velocity $v$ needs to satisfy the constraint given by equation 11.

$$
0 \leq v \leq \sqrt{R d g\left(e+f_{s}\right)}
$$

or alternatively,

$$
0 \leq \alpha_{2}(t) \leq g\left(e+f_{s}\right)
$$

## B. Car-Following Model [7], [13]

In order to model the behavior of a vehicle with respect to its peers on a lane, we use the Rakha-Pasumarthy-Adjerid (RPA) car-following model [13]. This model is general and can model the car-following behavior of AVs by calibrating AV-specific parameters. The model combines the Van Aerde steady-state car-following model [16], [17] with collision avoidance and acceleration constraints for non-steady state conditions. The RPA model predicts the velocity of a vehicle in order to remain within a safe distance with respect
to the vehicle ahead of it. It also ensures that the vehicle does not violate its physical capabilities (braking and acceleration behavior).

Given two vehicles indexed by $(.)_{n}$ and $(.)_{n-1}$, the expected velocity of vehicle ( n ) at time $t+\Delta t$ is given by equation 13 [7], [13].

$$
\begin{aligned}
& v_{n}(t+\Delta t) \\
& =\min \left\{\begin{array}{l}
v_{n}(t)+\frac{F_{n}(t)-R_{n}(t)}{m} \Delta t \\
\frac{-c_{1}+c_{3} v_{f}+s_{n}(t+\Delta t)-\sqrt{A}}{2 c_{3}} \\
\sqrt{v_{n-1}(t+\Delta t)^{2}+2 d_{\max }\left(s_{n}(t+\Delta t)-\frac{1}{k_{j}}\right)}
\end{array}\right.
\end{aligned}
$$

where $v_{f}$ is the free-flow speed, $v_{c}$ is the speed-at-capacity, $k_{j}$ is the jam density, $q_{c}$ is the lane saturation flow rate, $s_{n}(t+\Delta t)=s_{n}(t)+\left(v_{n-1}(t)-v_{n}(t)\right) \Delta t+\frac{1}{2} a_{n-1}(t) \Delta t^{2}$ is the vehicle spacing, $A=\left[c_{1}+c_{3} u_{f}-s_{n}(t+\Delta t)\right]^{2}-$ $4 c_{3}\left[s_{n}(t+\Delta t) v_{f}-c_{1} v_{f}-c_{2}\right], d_{\text {max }}$ is the maximum deceleration that could be experienced by the vehicle and $c_{1}=$ $\frac{v_{f}}{k_{j} v_{c}^{2}}\left(2 v_{c}-v_{f}\right), c_{2}=\frac{v_{f}}{k_{j} v_{c}^{2}}\left(v_{f}-v_{c}\right)^{2}$ and $c_{3}=\left(\frac{1}{q_{c}}-\frac{v_{f}}{k_{j} v_{c}^{2}}\right)$ are the steady-state car-following model parameters.

Equation 13 can be also cast as a constraint on the spacing between two consecutive vehicles, $d$

$$
d \geq \bar{d}=\min \left\{\begin{array}{l}
\max \left\{\begin{array}{l}
c_{1}+\frac{c_{2}}{v_{f}-v}+c_{3} v \\
\frac{v^{2}-\bar{v}^{2}}{2 d_{\max }}+c_{1}+\frac{c_{2}}{v_{f}}
\end{array} \text { if } v>\bar{v}\right. \\
c_{1}+\frac{c_{2}}{v_{f}-\frac{1}{2}\left(v_{c}+v_{f}\right)}+\frac{1}{2} c_{3}\left(v_{c}+v_{f}\right)
\end{array}\right.
$$

where, $v$ is the velocity of the vehicle under consideration and $\bar{v}$ is the velocity of the vehicle directly ahead of it in the same lane.

## C. Time Constraint

Since the vehicles cross a shared intersection with other vehicles (Figure 1), it is imperative that specific time slots be assigned to each vehicle. In this paper, we consider only the time after which a zone $\left(z_{i}\right)$ is free (i.e. $t_{z_{i}}$ ) and therefore a vehicle must arrive at the zone $z_{i}$ at a time $t_{\text {zone entry }}$ and satisfy equation 15 .

$$
t_{\text {zone entry }} \geq t_{z_{i}}
$$

Given the constraints defined in section (II-A), (II-B) and (II-C), the time optimal control problem that is solved in this paper for each vehicle is

$$
\begin{gathered}
\operatorname{minimize} P[\alpha(.)]=\int_{t_{i}}^{t_{f}} d t=t_{f}-t_{i} \\
\text { subjected to } \dot{X}=f(X, \alpha) \\
t_{z_{i}} \leq t_{z \text { one entry }} \leq \infty \\
-5 \leq \alpha_{1} \leq \frac{F-R}{m} \\
0 \leq v \leq \sqrt{R d g\left(e+f_{s}\right)} \\
\bar{d} \leq d \leq \infty
\end{gathered}
$$

The problem formulation presented in 16 means for each vehicle, a minimum trip time is sought subject to kinematic, dynamic and other conditions. The motion of the vehicle is governed by equation 1 and 2. The vehicle has to arrive at the intersection when it is free, namely at a time $t_{\text {zone entry }}$ satisfying equation 15. At all times the acceleration of the vehicle needs to be within the feasible range defined in Equation 9 and presented in Figure 2. At the intersection when the vehicle has to turn, its velocity needs to satisfy equation 11 in order not to slide and loose grip on the road. Finally, the vehicle needs to maintain a safe distance from the vehicle in front of it (equation 14).

When the system of equations 16 is solved using ICLOCS [18] and a solution is obtained, we can compute the fuel consumed along the vehicle trajectory using the VT-Micro model using Equation 17 [19], [20]. ICLOCS uses the IPOPT optimization software to find the solution. The possibility to obtain a non-global optimum is not the scope of this paper.

$$
F C(t)= \begin{cases}e^{\sum_{i=0}^{3} \sum_{j=0}^{3} L_{i j}^{e} v^{i} a^{j}} & \text { for } a \geq 0 \\ e^{\sum_{i=0}^{3} \sum_{j=0}^{3} M_{i j}^{e} v^{i} a^{j}} & \text { for } a<0\end{cases}
$$

where $L_{i j}^{e}$ are the model coefficients at speed power $i$ and acceleration power $j$ for positive accelerations, $M_{i j}^{e}$ are the model coefficients at speed power $i$ and acceleration power $j$ for negative accelerations, $v$ is the instantaneous speed and $a$ is the instantaneous acceleration. In this study the Oak Ridge National Lab (ORNL) composite vehicle parameters were used.

## III. Results and Discussion

Having described the model, we perform various simulations for an intersection considering various levels of congestion. The intersection has a major roadway and a minor roadway, where the arrival rates on the minor roadway are always half the flow of the major arterial. The flows along the major arterial range from 500 to 1200 veh/h, 10 \% of that turns left and 20 \% turns right at the intersection. The base saturation flow rate of the roadway is 1700 veh/h/lane. Given that the capacity of a signalized approach is much less than the saturation flow rate, the intersection experiences over-saturation delay in a number of scenarios. This paper presents two versions of the introduced logic. The first version Optimal Control Time (OCT) attempts to obtain a solution that reduces the delay regardless of the control effort (i.e. aggressive acceleration levels). The cost function will be

$$
P[\alpha()]=\int_{t_{i}}^{t_{f}} d t=t_{f}-t_{0}
$$

The second version, Optimal Control Effort (OCE) aims at obtaining the same results but while minimizing the control effort (i.e. avoid aggressive acceleration levels). In this case the cost function will be

$$
P[\alpha()]=\int_{t_{i}}^{t_{f}} 1+\alpha_{1}^{2}(t)+\alpha_{2}^{2}(t) d t
$$

The results of the introduced logic are compared to the results obtained when the intersection is controlled by a

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-5.jpg?height=380&width=720&top_left_y=196&top_left_x=247)
Fig. 4. (a) Two-phase plan and (b) Four-phase plan for the considered intersection.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-5.jpg?height=520&width=670&top_left_y=670&top_left_x=269)
Fig. 5. Delay obtained from an intersection equipped with traffic light having two and four phases.

roundabout (R), a stop sign (SS) and a traffic signal (TL). It is noted that a two-phase plan is implemented, since it presents better results compared to a four-phase plan. Figure 5 compares the delay obtained using an intersection equipped with a two-phase plan (Figure 4 (a)) and an intersection equipped with a four-phase plan with a separate phase for each approach (Figure 4 (b)). The results suggest that a two-phase plan performs better in terms of delay for this type of single lane intersection. This is particularly relevant since the percentage of vehicles turning left is only 10 \% and thus an additional phase is not warranted. For high percentage of left turn flows, a four-phase plan would be warranted. Consequently, in the rest of the paper, a two-phase plan is used. This plan is also optimized in real-time to maximize the intersection delay. This optimization is performed within INTEGRATION. The results of the (R), (SS) and (TL) approaches are obtained using the INTEGRATION software using the same and identical input. The same input is used to model vehicles crossing the intersection using the optimal control strategy. It should be noted that the INTEGRATION software also uses the RPA car-following and acceleration model that are embedded in the proposed algorithm.

Figure 6, 9, 10 and 11 present the mean delay, stops (using Equation 18), fuel consumption, and $\mathrm{CO}_{2}$ emissions for the entire intersection. The results suggest a general improvement in the mentioned quantities for both versions of the control system (i.e. (OCT) and (OCE)).

$$
\begin{aligned}
& s=\sum_{i=1}^{N} \frac{v(i \Delta t)-v((i+1) \Delta t)}{v_{f}} \\
& \quad \forall v(i \Delta t)>v((i+1) \Delta t)
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-5.jpg?height=417&width=535&top_left_y=200&top_left_x=1250)
Fig. 6. Mean delay in seconds for an intersection equipped with various control mechanisms and various flow rates.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-5.jpg?height=535&width=640&top_left_y=730&top_left_x=1197)
Fig. 7. Effects of random inputs on the delay in seconds generated for the newly introduced logic.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-5.jpg?height=423&width=533&top_left_y=1386&top_left_x=1253)
Fig. 8. Percentage reduction in delay of (OCT) and (OCE) in comparison to an intersection equipped with a roundabout.

Figure 6 presents the computed delay. It is noted that the (OCT) results in lower delays, drastically lower than the delay associated with a roundabout, the best among the other intersection control strategies. The (OCE) comes in after the (OCT) and performs also better than the roundabout. The benefits of the proposed approach is demonstrated and a true optimality is obtained. Specifically, the delay of approximately 2 (s) for (OCT) and 6 (s) for (OCE) are significantly lower than the delay of 76 (s) for the roundabout controlled intersection. Figure 8 illustrates the percentage reduction in vehicle delay compared to a roundabout controlled intersection for both versions of the proposed algorithm. We note that on average the delay is reduced by more than 80 \% for (OCT) and 55 \% for (OCE).

The effects of random input (i.e. random seed) is demonstrated in Figure 7. It is noted that three different seeds

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-6.jpg?height=425&width=535&top_left_y=198&top_left_x=337)
Fig. 9. Mean fuel consumption in liters for an intersection equipped with various control mechanisms and various flow rates.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-6.jpg?height=423&width=533&top_left_y=771&top_left_x=339)
Fig. 10. Mean stop for an intersection equipped with various control mechanisms and various flow rates.

were used. the results show that the newly introduced logic (OCT) is almost insensitive and always produces the best optimal solution. The figure also shows the results for an intersection equipped with a roundabout (R), a stop sign (SS) and a traffic light (TL). It should be noted that three random seeds were used and of the four control scenarios were run with the same three seeds.

Figure 9 illustrates the mean fuel consumption computed for all vehicles traversing the intersection. We note that an all-way stop controlled intersection produces the highest fuel consumption levels. The consumption generated by the proposed algorithm is insensitive to the demand level (approximately 0.117 L for (OCT) and 0.133 L for (OCE)). The intersection equipped with a (TL) produces a fuel consumption of 0.280 L and the (R) produces a fuel consumption level of 0.226 L. The optimality of the new approach leads to lower fuel consumption values.

Figure 10 presents the mean computed stops according to equation 18. We notice that the computed stops for the proposed algorithm remains fairly constant (i.e approximately 0.4 stops for (OCT)) in comparison with the roundabout that increases from 0.30 to 0.95 stops as the traffic demand increases. For the (OCE) the value of the number of vehicle stops remains constant at 0.55 stops/vehicle. It is noted that the value of the stops for an intersection equipped with a (SS) are slightly below 1.0, because the high demand levels result in the queue spilling back to the entrance point and thus vehicles enter the control zone at lower velocities. This means that the initial reduction in speed is not accounted for in computing the number of stops and thus is misleading [21].

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-6.jpg?height=417&width=535&top_left_y=198&top_left_x=1250)
Fig. 11. Mean $\mathrm{CO}_{2}$ emissions in grams for an intersection equipped with various control mechanisms and various flow rates.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-6.jpg?height=421&width=531&top_left_y=739&top_left_x=1253)
Fig. 12. Percentage reduction in stop of (OCT) and (OCE) in comparison to an intersection equipped with a roundabout.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-6.jpg?height=421&width=533&top_left_y=1293&top_left_x=1250)
Fig. 13. Percentage reduction in fuel consumption of (OCT) and (OCE) in comparison to an intersection equipped with a roundabout.

Figure 11 present the computed mean $\mathrm{CO}_{2}$ vehicle emissions for the different intersection control strategies. It is noted that the proposed algorithm results in lower $\mathrm{CO}_{2}$ emissions (i.e. 265 g for (OCT) and 286 g for (OCE)) when compared to other control algorithms. The roundabout produces the minimum $\mathrm{CO}_{2}$ emissions compared to the other control strategies (i.e. 446g). The proposed CAV intersection control approach produces more reductions in $\mathrm{CO}_{2}$ emissions.

Figure 8, 12, 13 and 14 present the percentage gained or lost in terms of vehicle delay, stops, fuel consumption and $\mathrm{CO}_{2}$ emissions for the proposed algorithm compared to the roundabout control. From the previous results and Figures 8, 12, 13 and 14, we note that (OCT) is better than (OCE) in terms of delay values. On average (OCT) results in 35 \% lower delay than the (OCE). This reduction is accompanied with higher fuel consumption (i.e. + 13 \%) and $\mathrm{CO}_{2}$ emissions (i.e. + 9 \%). These results demonstrate that there is a trad-off between delay and fuel consumption levels.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-7.jpg?height=425&width=563&top_left_y=198&top_left_x=322)
Fig. 14. Percentage reduction in $\mathrm{CO}_{2}$ of (OCT) and (OCE) in comparison to an intersection equipped with a roundabout.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-7.jpg?height=1433&width=776&top_left_y=733&top_left_x=217)
Fig. 15. Box plot for the delay experienced by the vehicles crossing the four-way intersection equipped with the new logic, the roundabout, the stop sign and the traffic signal and for different major axis flow rates.

Figure 15 present the box diagram for the delay for different flow rates and different approaches. These plots are obtained by considering all the data for each vehicle: the data of an individual vehicle is considered as a realization. It is noted that, the realizations for the proposed algorithm lie within a narrow region demonstrating that not only the mean travel time is low but also the variability in the travel times is also low.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-7.jpg?height=1452&width=778&top_left_y=202&top_left_x=1130)
Fig. 16. Box plot for the stop experienced by the vehicles crossing the four-way intersection equipped with the new logic, the roundabout, the stop sign and the traffic signal and for different major axis flow rates.

Figure 17 present the box plot for the fuel consumption for all the vehicles crossing the intersection. It is noted that the proposed algorithm produces low fuel consumption (i.e. 0.140 L as median for (OCT) and 0.109 L for (OCE)) in comparison to the roundabout for example (0.266 L as median). We note also that the realizations of these simulations for the proposed algorithm are confined to a lower value region: the $25^{\text {th }}$ percentile is 0.117 (L) and the $75^{\text {th }}$ percentile is 0.153 (L) for (OCT), the $25^{\text {th }}$ percentile is 0.102 (L) and the $75^{\text {th }}$ percentile is 0.137 (L) for (OCE) in comparison to the roundabout where the $25^{\text {th }}$ percentile is 0.205 (L) and the $75^{\text {th }}$ percentile is 0.246 (L). These values are generated for the mainline flow of 1200 veh/h.

The proposed algorithm has, however one main disadvantage, namely the high computational cost associated with the nonlinear optimization. Specifically, a set of four vehicles approaching the intersection takes somewhere between 2 to 5 minutes to solve. This drawback makes the algorithm unsuitable for real-time applications. Other simplified versions,

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-8.jpg?height=1431&width=776&top_left_y=198&top_left_x=217)
Fig. 17. Box plot for the fuel consumption levels for vehicles crossing the four-way intersection equipped with the proposed logic, the roundabout, the stop sign and the traffic signal for different demand levels.

however, were recently developed and were compared to the presented algorithm [22], which serves as the global optimum solution for comparison and evaluation purposes.

## IV. Conclusions

A novel intersection management algorithm that is derived from optimal control theory was developed for the control of connected automated vehicles. The developed algorithm was tested and compared to other intersection control strategies, including: a roundabout, a stop sign and a traffic signal controlled intersection. The results demonstrate that the proposed algorithm outperforms the other intersection control strategies producing lower delays and $\mathrm{CO}_{2}$ emissions with reductions of up to 80 \% and 40 \%, respectively, relative to the best intersection control strategy (in this case the roundabout).

One of the major disadvantages of the proposed algorithm is the high computational cost associated with finding the optimum solution, which makes the algorithm impractical for real-time implementations. Consequently additional research is needed to develop faster heuristic algorithms that are more suitable for real-time applications. It should be noted, however, that the proposed algorithm can be used to evaluate the accuracy of these heuristic algorithms given that the solutions generated using this algorithm represent the best that can be achieved.

## References

[1] A. de La Fortelle, "Coordination of automated vehicles at intersections: Decision, efficiency and control," in Proc. IEEE 18th Int. Conf. Intell. Transp. Syst., Sep. 2015, pp. 1708-1712.
[2] I. H. Zohdy and H. Rakha, "Game theory algorithm for intersectionbased cooperative adaptive cruise control (CACC) systems," in Proc. 15th Int. IEEE Conf. Intell. Transp. Syst., Sep. 2012, pp. 1097-1102.
[3] L. Li and F.-Y. Wang, "Cooperative driving at blind crossings using intervehicle communication," IEEE Trans. Veh. Technol., vol. 55, no. 6, pp. 1712-1724, Nov. 2006.
[4] S. Azimi, G. Bhatia, R. Rajkumar, and P. Mudalige, "Reliable intersection protocols using vehicular networks," in Proc. Int. Conf. Cyber-Phys. Syst., 2013, pp. 1-10.
[5] H. Rakha and R. K. Kamalanathsharma, "Eco-driving at signalized intersections using V2I communication," in Proc. 14th Int. IEEE Annu. Conf. Intell. Transp. Syst., Oct. 2011, pp. 341-346.
[6] J. Lee and B. Park, "Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment," IEEE Trans. Intell. Transp. Syst., vol. 13, no. 1, pp. 81-90, Mar. 2012.
[7] I. H. Zohdy and H. A. Rakha, "Intersection management via vehicle connectivity: The intersection cooperative adaptive cruise control system concept," J. Intell. Transp. Syst., Technol. Planning Oper., vol. 20, no. 1, pp. 17-32, 2014.
[8] A. I. M. Medina, N. van de Wouw, and H. Nijmeijer, "Automation of a T-intersection using virtual platoons of cooperative autonomous vehicles," in Proc. IEEE 18th Int. Conf. Intell. Transp. Syst., Sep. 2015, pp. 1696-1701.
[9] A. Gratner and S. Annell, "Probabilistic collision estimation system for autonomous vehicles," Ph.D. dissertation, School Ind. Eng. Manage., KTH Roy. Inst. Technol., Stockholm, Sweden, 2016.
[10] M. Zhu, X. Li, H. Huang, L. Kong, M. Li, and M.-Y. Wu, "LICP: A lookahead intersection control policy with intelligent vehicles," in Proc. IEEE 6th Int. Conf. Mobile Adhoc Sensor Syst., Oct. 2009, pp. 633-638.
[11] Z. Li, M. Chitturi, D. Zheng, A. Bill, and D. Noyce, "Modeling reservation-based autonomous intersection control in vissim," Transp. Res. Board, vol. 2381, pp. 81-90, Dec. 2013.
[12] K. Dresner and P. Stone, "A multiagent approach to autonomous intersection management," Artif. Intell. Res., vol. 31, pp. 591-656, Mar. 2008.
[13] H. Rakha, P. Pasumarthy, and S. Adjerid, "A simplified behavioral vehicle longitudinal motion model," Transp. Lett., vol. 1, no. 2, pp. 95-110, 2009.
[14] H. Rakha, I. Lucic, S. H. Demarchi, J. R. Setti, and M. V. Aerde, "Vehicle dynamics model for predicting maximum truck acceleration levels," J. Transp. Eng., vol. 127, no. 5, pp. 418-425, 2001.
[15] N. J. Garber and L. A. Hoel, Traffic and Highway Engineering, 5th ed. Boston, MA, USA: Cengage Learning, 2014.
[16] H. Rakha and B. Crowther, "Comparison of greenshields, pipes, and van aerde car-following and traffic stream models," Transp. Res. Rec., Transp. Res. Board, vol. 1802, pp. 248-262, Jan. 2002.
[17] H. Rakha, "Validation of van Aerde's simplified steadystate carfollowing and traffic stream model," Transp. Lett., vol. 1, no. 3, pp. 227-244, 2013.
[18] E. J. Van Wyk, P. Falugi, and E. C. Kerrigan. (2010). ICLOCS. [Online]. Available: http://www.ee.ic.ac.uk/ICLOCS
[19] K. Ahn, H. Rakha, A. Trani, and M. Van Aerde, "Estimating vehicle fuel consumption and emissions based on instantaneous speed and acceleration levels," ASCE J. Transp. Eng., vol. 128, no. 2, pp. 182-190, 2001.
[20] H. Rakha, K. Ahn, and A. Trani, "Development of VT-Micro model for estimating hot stabilized light duty vehicle and truck emissions," Transp. Res. D, Environ., vol. 9, no. 1, pp. 49-74, 2004.
[21] H. Rakha, Y.-S. Kang, and F. Dion, "Estimating vehicle stops at undersaturated and oversaturated fixed-time signalized intersections," Transp. Res. Board, vol. 1776, pp. 128-137, Jan. 2001.

[22] Y. Bichiou and H. A. Rakha, "Real-time optimal intersection control system for automated/cooperative vehicles," Int. J. Transp. Sci. Technol., to be published. [Online]. Available: http://www.sciencedirect.com/ science/article/pii/S2046043018300315, doi: 10.1016/j.ijtst.2018.04.003.
![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-9.jpg?height=318&width=254&top_left_y=464&top_left_x=168)

Youssef Bichiou received the M.Sc. degree in the field of fluid structure interaction from the Department of Mechanical Engineering, Tunisia Polytechnic School, La Marsa, Tunisia, and the Ph.D. degree in engineering mechanics from the Virginia Polytechnic Institute and State University (Virginia Tech). He is currently a Post-Doctoral Associate with the Virginia Tech Transportation Institute, Blacksburg, VA, USA. His research interests include fluid-structure interaction, nonlinear dynamics, optimal control, and traffic flow.

![](https://cdn.mathpix.com/cropped/6c85a086-e8b0-4504-aae5-f66756444653-9.jpg?height=318&width=254&top_left_y=215&top_left_x=1083)

Hesham A. Rakha (M'04) received the B.Sc. degree (Hons.) in civil engineering from Cairo University, Cairo, Egypt, in 1987, and the M.Sc. and Ph.D. degrees in civil and environmental engineering from Queen's University, Kingston, ON, Canada, in 1990 and 1993, respectively. He is currently the Samuel Reynolds Pritchard Professor of engineering with The Charles E. Via, Jr. Department of Civil and Environmental Engineering, and also a Courtesy Professor with the Bradley Department of Electrical and Computer Engineering, Virginia Tech, Blacksburg, VA, USA. He is also the Director of the Center for Sustainable Mobility, Virginia Tech Transportation Institute. He has authored and co-authored four books and over 330 refereed publications in the areas of traffic flow theory, traffic modeling and simulation, traveler and driver behavior modeling, artificial intelligence, dynamic traffic assignment, traffic control, energy and environmental modeling, and safety modeling. He is a member of the ITE, the ASCE, and the Transportation Research Board. He is a Professional Engineer in Ontario Province, Canada.


[^0]:    Manuscript received March 8, 2016; revised December 22, 2017 and May 28, 2018; accepted June 20, 2018. This work was supported by the Connected Vehicle Initiative University Transportation Center (CVI-UTC). The Associate Editor for this paper was M. Barth. (Corresponding author: Hesham A. Rakha.)
    Y. Bichiou is with the Center for Sustainable Mobility, Virginia Tech Transportation Institute, Blacksburg, VA 24061 USA.
    H. A. Rakha is with the Charles E. Via, Jr. Department of Civil and Environmental Engineering, Virginia Tech, Blacksburg, VA 24061 USA, also with the Bradley Department of Electrical and Computer Engineering, Virginia Tech, Blacksburg, VA 24061 USA, and also with the Center for Sustainable Mobility, Virginia Tech Transportation Institute, Blacksburg, VA 24061 USA (e-mail: hrakha@vt.edu).
    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
    Digital Object Identifier 10.1109/TITS.2018.2850335

