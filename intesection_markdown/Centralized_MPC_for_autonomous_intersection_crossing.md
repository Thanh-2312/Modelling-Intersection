# Centralized MPC for Autonomous Intersection Crossing 

Lea Riegger, Markus Carlander, Niklas Lidander, Nikolce Murgovski, Jonas Sjöberg


#### Abstract

This paper develops a method for a safe and autonomous intersection crossing. A centralized system controls autonomous vehicles within a certain surrounding of the intersection and generates optimized trajectories for all vehicles in the area. A recently proposed design approach, [10], where this problem is expressed as a convex optimization problem using space sampling instead of time sampling, is formulated as a MPC problem solved by a QP algorithms so that it can be executed in real time. The MPC controller is then integrated in CarMaker using Matlab/Simulink so that the controller can be validated against the advanced vehicle models and sensor models available in CarMaker. Preliminary results of this validation are presented. Also, a method is designed to obtain time gaps between the vehicles to prevent the optimization problem to become infeasible when sensors give noisy measurements.


## I. Introduction

Around the world, traffic accidents that are related to intersections occur all too often. Compiled statistic from several European Countries shows that 43\% of all road injury accidents can be related to intersections [1]. Statistic conducted in the USA indicates similar numbers [2]. The actual number of related traffic accidents in Sweden is slightly less in total. Of all reported accidents in the year 2014 in Sweden, 24 \% are intersection related. Of those, 91 \% led to severe person injuries [3]. As the statistics show, intersections lead to high risk for accidents. Even though the most dangerous intersections are regulated by traffic lights, signs and road-markings, accidents occur still very frequently. On the contrary, improving the safety at intersection crossing by, e.g., installing traffic lights, may also come at a price in today's society since it limits the traffic flow. This causes bottlenecks in the traffic rhythm which not only wastes a lot of time for travelers but also leads to environment pollution caused by unnecessary accelerations/decelerations and engine idling operation.

Today's vehicles are trending to become more and more autonomous. Exclusive benefits as adaptive cruise control, automatic lane change maneuvers, parking assistance are available on the market today. Statistics from USA show that about 96\% of all intersection related accidents are attributed to drivers [2]. If intersections would be controlled by an autonomous cooperative intersection algorithm that can optimize the crossing sequence for all nearby vehicles,

[^0]the intersection should be made more safe since no human factor would cause accidents. The intersection should also be more efficient in both terms, time and energy consumption, since the algorithm would decide the crossing order and vehicles' speed for maximum efficiency. Aspects as minimizing deceleration, respectively acceleration, as well as reducing the total time for the intersection crossing could be taken into account for computing the optimal crossing sequence. It would also be possible to set different priority orders for different types of vehicles, for example according to their fuel consumption and performance. Emergency vehicles could be given precedence to enter the intersection on callout.

In this paper, a Model Predictive Controller (MPC) is designed for a centralized system which takes control over autonomous vehicles within a certain surrounding of the intersection. The vehicles are assumed to drive fully autonomously. Among other recent work some have already exploited the idea of using different MPC implementations [4], [5], [6], [7], [8], [9], [10]. In [6] for example, the solution is approximated by a centralized, finite time optimal control problem. In [7], a decentralized approach based on suboptimal decision-making heuristics is used.

The general optimization algorithm for intersection crossing in this paper is based on the modeling approach of [10] where the problem is formulated in space coordinates and the inverse of speed is used as a state variable. For a given crossing sequence, the approach allows the problem to be formulated as a convex program that optimizes vehicles' speed and prevents collision in a smooth way.

This paper has three main contributions. First, an MPC, based on a point mass model, is designed rested on the convex modeling proposed by [10]. The MPC, expressed as an quadratic program, (QP), generates optimized trajectories for all vehicles in the controlled area, such that a cost function is minimized and the constraints are satisfied. The vehicles may differ in speed, acceleration and braking capabilities. Second, to validate the controller based on the point mass model, the MPC is implemented in Matlab/Simulink and the simulation tool CarMaker, which provides advanced vehicle models and sensor models. Preliminary results with this simulation environment are presented where also the computational aspects of the algorithm are illustrated. Third, when the control is based on noisy sensor signals, it may happen that the trajectory optimization, which is repeated each sampling instant, becomes infeasible. This is solved by introducing a penalized time gap in the optimization criterion.

The paper is organized as follows: Section II gives an
overview of the convex problem formulation in space coordinates. In Section III, an MPC is designed. Section IV provides an MPC simulation in CarMaker running under Matlab/Simulink. Section V shows a case study and investigates the controller efficiency in the simulation environment. Section VI closes the paper with final conclusions.

## II. Problem Formulation

This section presents the modeling approach proposed by [10] and formulates the autonomous intersection crossing as a convex optimization problem.

## A. Assumptions

Considering $N_{v}$ autonomous vehicles in a surrounding of an intersection, each with a predefined path to follow, it is assumed that for each vehicle $i=1, \ldots N_{v}$, the acceleration along its path can be varied. The vehicle dynamics in the control model are simplified to a point mass model.

The presented intersection crossing scenario is limited to one vehicle per lane which means that the scenario where vehicles are following each other on the same lane is not studied here. Nevertheless, the controller is designed in such a way that an adaptation to enable this is possible.

## B. Problem statement

For a safe intersection crossing, autonomous vehicles within a certain surrounding of the intersection shall be controlled by a centralized system. An illustration of an intersection is shown in Fig. 1. The red color indicates the critical set, where more than one vehicle should never reside, due to safety reasons. The yellow color shows the enlarged set, which will be discussed later, in Section III-B. The light blue color indicates the start and end of the control region. The centralized system controls only vehicles in this region. The position, where vehicle $k$ enters respectively exits the critical set, is called $L_{k}$ respectively $H_{k}$. The order in which the vehicles cross the intersection is called crossing sequence and the matrix which contains all the possible crossing sequences is called permutation matrix $\Omega$.

The requirement to allow only one car in the critical set is unnecessary conservative. For example, two vehicles traveling in opposite directions could obviously pass the crossing at the same time. However, this algorithm does not permit it, a relaxation would be needed to allow this, but this is not done in this contribution.

## C. Convex problem statement

To formulate the optimization problem in a convex form, the problem is formulated in space coordinates, rather than time, according to [10]. With the spatial coordinate $p$, the linear state space model

$$
\kappa_{i}^{\prime}(p)=\underbrace{\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right)}_{A} \kappa_{i}(p)+\underbrace{\binom{0}{1}}_{B} u_{i}(p)
$$

is used to model each vehicle $i$, where $\kappa_{i}=\left(t_{i}(p) \quad z_{i}(p)\right)^{T}$ is the state vector and $\kappa_{i}^{\prime}=d \kappa / d p$ is the derivative with

![](https://cdn.mathpix.com/cropped/bd8a577c-c49e-4c6b-99e5-41b9bc294294-2.jpg?height=819&width=771&top_left_y=185&top_left_x=1126)
Fig. 1. Illustration of an intersection showing the critical set (red), the enlarged set (yellow) and the control region (light blue).

respect to the spatial distance $p$. The slowness of the system is indicated by the lethargy $z_{i}(p)=1 / v_{i}(p)$, where $v_{i}(p)$ is the vehicle velocity. The time needed to reach position $p$ is $t_{i}(p)$. Input $u_{i}(p)=z_{i}^{\prime}(p)$ is the spatial derivative of $z_{i}(p)$.

1) Cost function: The cumulative cost function is the sum of cost functions for each vehicle $i$

$$
\min _{u_{i}(p)} \sum_{i=1}^{N_{v}} J_{i}\left(\kappa_{i}(p), u_{i}(p), u_{i}^{\prime}(p), \kappa_{i}\left(p_{i f}\right)\right),
$$

where $p_{i f}$ is the final position after leaving the intersection. The cost function for each vehicle $i$

$$
J_{i}=J_{i 1}+J_{i 2}+J_{i 3}
$$

consists of three quadratic convex functions. The first term

$$
J_{i 1}=w_{i 1} \bar{v}_{i r}^{3} \int_{0}^{p_{i f}}\left(z_{i}(p)-\frac{1}{v_{i r}(p)}\right)^{2} d p
$$

penalizes the deviation from the reference velocity, where $w_{i j}[j=1$ in (4a)] are weighting factors. The mean of the reference velocity $v_{i r}(p)$ for each car $i$ is $\bar{v}_{i r}$. The terms $J_{i 2}, J_{i 3}$ with

$$
\begin{aligned}
& J_{i 2}=w_{i 2} \bar{v}_{i r}^{5} \int_{0}^{p_{i f}} u_{i}^{2}(p) d p \\
& J_{i 3}=w_{i 3} \bar{v}_{i r}^{7} \int_{0}^{p_{i f}} u_{i}^{\prime 2}(p) d p
\end{aligned}
$$

penalize high longitudinal acceleration and jerk to guarantee a comfortable drive and limited actuator usage. The unconventionally appearance of $J_{i 2}$ and $J_{i 3}$ with powers of the mean velocity is due to that the problem is described in space coordinates. In [10], it is shown how these are obtained by direct translation of quadratic penalties from time to space domain.
2) Constraints: In addition to the equality constraint (1), the problem includes inequality constraints on the states $\kappa_{i}$ and the input $u_{i}$ as well as initial and final state constraints

$$
\begin{aligned}
\kappa_{i}^{\prime}(p) & =A \kappa_{i}(p)+B u_{i}(p) \\
\kappa_{i}(p) & \in\left[\kappa_{i \min }(p), \kappa_{i \max }(p)\right] \\
u_{i}(p) & \in\left[u_{i \min }\left(p, z_{i}(p)\right), u_{i \max }\left(p, z_{i}(p)\right)\right] \\
\kappa_{i}(0) & =\kappa_{i 0}=\left(\begin{array}{ll}
0 & 1 / v_{i 0}
\end{array}\right)^{T} \\
\kappa_{i}\left(p_{i f}\right) & =\kappa_{i f}=\left(\begin{array}{ll}
\text { free } & 1 / v_{i f}
\end{array}\right)^{T},
\end{aligned}
$$

where the limits (5c) are linear functions of $z_{i}$ and represent a linearized inner approximation of corresponding constant acceleration limits in the time domain formulation [10]. To avoid collisions, a final constraint is needed, which guarantees that a vehicle can enter a certain critical set at the center of the intersection, only when the previous vehicle has left the critical set, i.e.

$$
\begin{aligned}
t_{k}\left(H_{k}\right) \leq t_{l}\left(L_{l}\right), \quad k & =\Omega_{m, n}, l=\Omega_{m, n+1} \\
n & =1, \ldots, N_{v}-1
\end{aligned}
$$

where $k$ and $l$ are indices of consecutive vehicles in a given crossing sequence $m$ of the permutation matrix $\Omega$, which contains all possible crossing sequences. Position $H_{k}$ is the point where vehicle $k$ exits the critical set and $L_{l}$ is the entry point for vehicle $l$. For a given crossing sequence, the optimization problem is a convex quadratic program (QP).

More detailed explanations about the convex modeling of the problem can be found in [10].

## III. MPC Design

This section presents the optimization problem in a discrete space coordinate, proposes and extended cost function and rewrites the problem as a standard QP suitable for MPC implementation.

## A. Discrete state space model

In order to implement the controller in Matlab, a discrete version of the model (1) with a sampling interval $d_{s}$ is derived with Forward Euler approximation. The result is the following discrete state space representation

$$
\kappa_{i}(p+1)=A_{d} \kappa_{i}(p)+B_{d} u_{i}(p),
$$

with the discrete matrices expressed as

$$
\begin{aligned}
& A_{d}=I_{2}+d_{s} A=\left(\begin{array}{cc}
1 & d_{s} \\
0 & 1
\end{array}\right) \\
& B_{d}=d_{s} B=\binom{0}{d_{s}}
\end{aligned}
$$

In order to guarantee stability of the discretized state space representation, the discretization step must fulfill the criterion $\left|I_{2}+d_{s} A\right| \leq 1$. Since the eigenvalues of the discrete state space representation $\lambda_{1,2}=1$ are mapped on the border of the unit circle, stability is guaranteed.

## B. Extended cost function to impose time gap

The constraint (5f) prevents the vehicles to collide, but it also allows several vehicles to be on the borders, or very close to the borders of the opposite ends of the critical set [when constraint (5f) is active]. This can lead to an infeasible solution in the next MPC update, in the case when noise and model uncertainty initialize the problem with a slight violation of (5f). Hence, constraint (5f) is modified so that there is some margin between the vehicles. This is done by introducing a slack variable $s_{j}$ for each consecutive vehicle pair inside the control region. The variable $s_{j}$ expresses the time difference between the first vehicle leaving the intersection and the second vehicle entering the intersection. By defining $\Delta t$ as the desired time difference, the cost function (2) can be extended to

$$
\min _{u_{i}, s_{j}} \sum_{i=1}^{N_{v}} J_{i}(\cdot)+\sum_{j=1}^{N_{v}-1} w_{j} \max \left(0, \Delta t-s_{j}\right)^{2}
$$

and the constraint (5f) can be replaced by

$$
s_{j}=t_{l}\left(L_{l}\right)-t_{k}\left(H_{k}\right), \quad s_{j} \geq 0 .
$$

The maximization in (8a) is a convex function of $s_{j}$ and $\Delta t$, where $t_{l}\left(L_{l}\right)-t_{k}\left(H_{k}\right)<\Delta t$. Vehicle pairs in which the vehicles are far apart are not forced to have a predefined time difference in the crossing. The extended cost function (8a) together with constraint (8b) effectively introduces an additional enlarged region, which is illustrated in Fig. 1. In comparison to the critical set, multiple vehicles may reside within the enlarged region, as long as they are outside the critical set.

Further, the min/max function in (8a) can be written without the max term as

$$
\begin{aligned}
& \min _{s_{j}} \sum_{j=1} w_{j} q_{j}^{2} \\
\text { subject to: } & q_{j} \geq \Delta t-s_{j}, \quad q_{j} \geq 0,
\end{aligned}
$$

where $q_{j}$ are additional optimization variables.

## C. Transformation to a standard QP

In this section, the problem is transformed into the standard QP form

$$
\begin{aligned}
\min _{x} & \frac{1}{2} x^{T} H x+f^{T} x \\
\text { subject to: } & A_{e q} x=b_{e q} \\
& A_{i n} x \leq b_{i n}
\end{aligned}
$$

where $x$ is the vector of optimization variables, $H$ the Hessian matrix and $f$ the remaining linear terms in the objective. The constraints are also transformed to fit the formulation in (10b)-(10c).

1) Cost function: The cost function (3) is transformed into a quadratic form for the MPC by writing the vector $x=\left(\begin{array}{lll}x_{1} & \ldots & x_{N_{v}}\end{array}\right)^{T}$ in (10a) as

$$
x_{i}=\left(\begin{array}{lllll}
K_{i} & U_{i} & U_{i}^{\prime} & S_{j} & Q_{j}
\end{array}\right)^{T}
$$

where $K_{i}=\left[\kappa_{i}(1), \ldots, \kappa_{i}(N)\right]^{T}, U_{i}=\left[u_{i}(0), \ldots, u_{i}(N-\right.$ 1) $]^{T}, \quad U_{i}^{\prime}=\left[u_{i}^{\prime}(0), \ldots, u_{i}^{\prime}(N-1)\right]^{T}, \quad S_{j}=$ $\left[s_{j}(1), \ldots, s_{j}(N)\right]^{T}, \quad Q_{j}=\left[q_{j}(1), \ldots, q_{j}(N)\right]^{T}$ for each vehicle $i$ and vehicle pair $j$ in the control region. The vector $x_{i}$ involves the states, the control input, the derivative of the control input and the slack variable. The prediction and control horizon are both equal to N. The Hessian matrix $H_{i}$ for each vehicle $i$ results in

$$
H_{i}=2\left(\begin{array}{ccccc}
Q_{i 1} & 0 & 0 & 0 & 0 \\
0 & Q_{i 2} & 0 & 0 & 0 \\
0 & 0 & Q_{i 3} & 0 & 0 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & Q_{i 4}
\end{array}\right) .
$$

The matrices $Q_{i 1}, Q_{i 2}, Q_{i 3}$ and the scalar $Q_{i 4}$ are equal to

$$
\begin{aligned}
Q_{i 1} & =w_{i 1} \bar{v}_{i r}^{3} C^{T} C I_{N}, \\
Q_{i 2} & =w_{i 2} \bar{v}_{i r}^{5} I_{N}, \\
Q_{i 3} & =w_{i 3} \bar{v}_{i r}^{7} I_{N}, \\
Q_{i 4} & =w_{j},
\end{aligned}
$$

where $I_{N}$ is the identity matrix with $N$ rows and $C=\left[\begin{array}{ll}0 & 1\end{array}\right]$. The $f_{i}$ vector containing the remaining non-quadratic terms for each vehicle $i$ is

$$
f_{i}^{T}=-2 w_{i 1} \bar{v}_{i r}^{3} \frac{1}{v_{i r}(p)}\left(\begin{array}{llllll}
C & \ldots & C & 0 & \ldots & 0
\end{array}\right) .
$$

2) Constraints: The state constraint of the model described in (5a) has to be reformulated in a matrix form as shown in (10b) with the discrete model described in (7). Furthermore, the constraints (5b)-(5c) limiting the state variables and the acceleration as well as the collision avoidance constraint (5f) can be written into new inequality constraints (10c). The two constraints (5b)-(5c) have to be split up into two constraints in order to be implemented in a matrix form.

In order to control $N_{v}$ vehicles, the cost function (10a) needs to be extended. The new vector $x$ and Hessian matrix for $N_{v}$ cars are then according to (10a)

$$
\begin{aligned}
x & =\left(x_{1: N_{v}}^{T}\right)^{T} \\
H & =\operatorname{diag}\left(H_{1: N_{v}}\right)
\end{aligned}
$$

and the vector $f$ is changed to

$$
f^{T}=\left(f_{1: N_{v}}^{T}\right) .
$$

Analogously, the constraints also change in the same manner. Using the vector $x$ (15), the equality and inequality constraints for all $N_{v}$ vehicles can be written as

$$
\begin{aligned}
A_{e q}^{T} & =\left(A_{e q, 1: N_{v}}^{T}\right), \\
b_{e q}^{T} & =\left(b_{e q, 1: N_{v}}^{T}\right), \\
A_{i n}^{T} & =\left(A_{i n, 1: N_{v}}^{T}\right), \\
b_{i n}^{T} & =\left(b_{i n, 1: N_{v}}^{T}\right) .
\end{aligned}
$$

## D. Control area and optimization horizon

Whether a vehicle is included in the MPC computation depends on its distance to the intersection. The control area of the centralized controller is defined for a certain surrounding of the intersection. The vehicle speed at the moment of entering the control area is chosen as a reference. The control area is re-scanned in every time step searching for new arriving or leaving cars. The controller re-optimizes in every time step and takes into account only the vehicles in the control area.

Since there is no point in controlling the vehicles after they have passed the control area, the optimization horizon $N_{i}$ for each vehicle $i=1, \ldots, N_{v}$, is not moving along the vehicles as they advance. Instead the horizon is shrinking as the cars are progressing through the control area. Thus, the computation load of the MPC algorithm is decreasing as controlled vehicles are approaching the end of the intersection and it is increasing as new vehicles enter the intersection.

## IV. Simulation

In this section the MPC is applied to an advanced vehicle model, with the focus on connecting the MPC developed in Matlab/Simulink to a traffic model and an advanced vehicle model developed in CarMaker.

The MPC is implemented in Simulink as a Matlab Function block, see Fig. 2. The simulation tool IPG CarMaker provides a detailed vehicle model and serves as a simulation environment to design a traffic model, containing an intersection and traffic flow. Furthermore, CarMaker provides a video animation by the plug in program IPG Movie for visualizing the simulation results. This is used as an additional tool for validation of collision avoidance and representation of the simulation results.

## A. Restrictions of CarMaker 5.0.2

In CarMaker 5.0.2, only one host car can be simulated as an advanced car model. For other cars, only their position can be controlled. This means that the validation is only done with respect to one (the simulated) car, the others can be placed exactly where the MPC controller commands them to be. Nevertheless, these cars have the same dynamics as the point mass model used for the controller design.

## B. Simulation environment design

A CarMaker road is constructed from start to stop by a list of road segments, each one only connected with the previous and following segment [11]. In this paper, for simplicity, the intersection is constructed by making a turn and letting the road cross itself (see Fig. 3). This causes a limitation to the movements of the vehicles because the motion of the traffic objects is connected to the definition of the road. Thus, the traffic objects have to pass straight through the intersection. A turn in such intersection is not possible.

After the creation of the intersection, traffic is added to the model. For each vehicle, the host car as well as the traffic objects, the vehicle type, the reference starting point and reference speed are preset. The host car starts with a zero

![](https://cdn.mathpix.com/cropped/bd8a577c-c49e-4c6b-99e5-41b9bc294294-5.jpg?height=718&width=1530&top_left_y=198&top_left_x=305)
Fig. 2. Implementation of the MPC in Simulink combined with CarMaker's Simulink environment. Green color indicates CarMaker's environment and orange color indicates signals taken from CarMaker. The MPC is added in between the two green boxes, where signals, e.g brake and gas are 'hijacked' from CarMaker and used in the MPC algorithm. The output of the MPC with the manipulated signals are afterward reconnected to CarMaker.

velocity and the road model is designed to allow the host vehicle reach its desired speed before entering the controlled intersection area.

## C. Including the MPC into CarMaker

The CarMaker simulation model in Simulink consists of a chain of individual subsystem blocks. These blocks cannot be removed, but their functionality can be changed by overwriting their input or output signals.

The MPC is included by replacing the driver model in CarMaker so that it gives the gas and brake signals in the Vehicle Control block in Simulink as seen in Fig. 2, where the preset desired speed is overwritten by the calculated values from the MPC algorithm. The gas and brake signals from the driver model are only used for the vehicle with dynamics. For the other vehicles the calculated control signals overwrite directly the acceleration signal without a conversion to gas and brake signals.

## V. Simulation evaluation with three vehicles

In the selected case study, the presented MPC is tested for three cars approaching an intersection as shown in Fig. 3. Car 1 is simulated using the advanced model in CarMaker, the other two are simulated with the same point mass model as in the MPC. In Table I, the parameters for the cars $i=1,2,3$ can be found. The speed and acceleration limits as well as the weights for the cost function are selected identically for all three vehicles. The desired crossing sequence is chosen to 1,2,3. This means, for space reasons, that the search over possible crossing sequences, one of the motivations to formulate the problem as an efficient QP, is skipped. The vehicles start with different initial speed and distances from the intersection. Without a controller, car 1 and 2 would

![](https://cdn.mathpix.com/cropped/bd8a577c-c49e-4c6b-99e5-41b9bc294294-5.jpg?height=438&width=771&top_left_y=1130&top_left_x=1128)
Fig. 3. Created intersection crossing in CarMaker environment where the three cars are approaching the intersection.

TABLE I
Problem data of the case study.
| Parameter | Values |
| :--- | :--- |
| $\left(\begin{array}{lll}v_{1 r} & v_{2 r} & v_{3 r}\end{array}\right)$ | ( 47 km/h 48 km/h 50 km/h) |
|  | $(30 \mathrm{~km} / \mathrm{h} 90 \mathrm{~km} / \mathrm{h})$ |
| $\left(\begin{array}{ll}v_{i m i n} & v_{i m a x} \\ a_{i m i n} & a_{i m a x}\end{array}\right)$ | $\left(-3 \mathrm{~m} / \mathrm{s}^{2} \quad 3 \mathrm{~m} / \mathrm{s}^{2}\right)$ |
| $\left(w_{i 1} \quad w_{i 2} \quad w_{i 3} \quad w_{i 4}\right)$ | $\left(\begin{array}{llll}1 & 1100 & 23 & 10000\end{array}\right)$ |
| $\Delta t$ | 0.6 s |
| $d_{s}$ | 4 m |


collide in the intersection ${ }^{1}$. The MPC takes control over a vehicle when it has entered the control distance of the intersection, which is 60 m. The critical set, where no collisions are allowed, is the $15 \cdot 15 \mathrm{~m}^{2}$ intersection crossing area. The vehicles do not turn left or right in the intersection, instead they only drive straight forward. The initial optimization

[^1]horizon for every car entering the control area is $\mathrm{N}=135$ steps, with a sampling interval of 1 m.

Data gathered from the CarMaker vehicle sensors are shown in the top three plots of Fig. 4. When vehicle 1 comes closer to the intersection it can be observed that it starts to accelerate and vehicle 2 starts to decelerate in order to avoid a collision. The third vehicle slows down to avoid a collision between the second and third vehicle. Furthermore, by looking at the last plot, it is evident that the MPC controller efficiently prohibits collisions between the vehicles ${ }^{2}$. An upward-pointing triangle depicts the time where the vehicle is entering the intersection and a downward-pointing triangle shows the time when it is leaving. Since there is no vertical alignment among the triangles, there are no collisions.

![](https://cdn.mathpix.com/cropped/bd8a577c-c49e-4c6b-99e5-41b9bc294294-6.jpg?height=1044&width=831&top_left_y=896&top_left_x=200)
Fig. 4. Trajectories from the MPC controller. The upper three subplots show velocity, acceleration and position for each vehicle. The very last plot shows the computation time of the quadratic programming solver.

Compared to the solution presented in [10], the computation time for the convex problem is decreased by using a QP solver instead of the generalized second order cone program (SOCP) solver. It can be seen in the bottom plot of Fig. 4 that in the worst case scenario, the problem can

[^2]be solved in less than 0.05 seconds ${ }^{3}$. The figure also shows that the computation time has an increasing trend, up to the MPC update at about the 18th second, when all cars have entered the control area. After this, the computation time has a decreasing trend, since the prediction horizon is shrinking for all the vehicles.

## VI. Conclusions

This paper provides a centralized MPC for optimal control of autonomous vehicles in the control area of an intersection. The problem is formulated as a convex quadratic program that can be solved efficiently. The controller is tested for an advanced vehicle model using the simulation tool CarMaker. The simulation results show that the test environment works as intended, and the algorithm successfully avoids collisions in the test example.

Hence, the test environment is ready to be used for more advanced validation of the MPC algorithm. Sensor noise can be included, and the parameters of the test situation can be explored. Also, the simulation environment can be extended for further validation tests, the road construction can be improved to allow cars turning in the crossing, robustness can be explored adding noise to the not simulated cars etc. These, and further tasks are left for future studies.

## References

[1] M. A. Martinez. Accident causation and pre-accidental driving situations. [Online]. Available: https://dspace.lboro.ac.uk/2134/8434, 2008
[2] National Highway Traffic Safety Administration. Crash factors in intersection-related crashes: An on-scene perspective. [Online]. Available: http://www-nrd.nhtsa.dot.gov/Pubs/811366.pdf,2010
[3] Sveriges Officiella Statestik Trafik Analys. Vägtrafikskador 2014. road traffic injuries 2014. [Online]. Available: http://www-nrd.nhtsa. dot.gov/Pubs/811366.pdf
[4] K.-D. Kim, "Collision free autonomous ground traffic: A model predictive control approach," in ACM/IEEE International Conference on Cyber-Physical Systems (ICCPS), 2013, pp. 51-60.
[5] K.-D. Kim and P. Kumar, "An MPC-based approach to provable system-wide safety and liveness of autonomous ground traffic," IEEE Transactions on Automatic Control, vol. 59, no. 12, pp. 3341-3356, 2014.
[6] R. Hult, G. R. de Campos, P. Falcone, and H. Wymeersch, "An approximate solution to the optimal coordination problem for autonomous vehicles at intersections," in Proceedings of the American Control Conference, 2015, pp. 763-768.
[7] G. R. de Campos, P. Falcone, and J. Sjöberg, "Autonomous cooperative driving: A velocity-based negotiation approach for intersection crossing," in 16th International IEEE Conference on Intelligent Transportation Systems (ITSC), Oct 2013, pp. 1456-1461.
[8] G. R. de Campos, P. Falcone, H. Wymeersch, R. Hult, and J. Sjöberg, "Cooperative receding horizon conflict resolution at traffic intersections," in IEEE 53rd Annual Conference on Decision and Control (CDC), Dec 2014, pp. 2932-2937.
[9] L. Makarem and D. Gillet, "Model predictive coordination of autonomous vehicles crossing intersections," in 16th International IEEE Conference on Intelligent Transportation Systems (ITSC 2013), Oct 2013, pp. 1799-1804.
[10] N. Murgovski, G. R. de Campos, and J. Sjöberg, "Convex modeling of conflict resolution at traffic intersections," in Conference on Decision and Control, Osaka, Japan, 2015.
[11] IPG CarMaker, User's guide version 5.0.2. IPG Automotive, Karlsruhe, 2015.
[^3]
[^0]:    This work was supported by the European Commission Seventh Framework Program under the project AdaptIVe, grant agreement number 610428.

    This work has been performed by the first three authors as a student project supervised by the last two authors, Nikolce Murgovski and Jonas Sjöberg who are with the Department of Signals and Systems, Chalmers University of Technology, Sweden. \{nikolce.murgovski, jonas.sjoberg\}@chalmers.se.

[^1]:    ${ }^{1}$ A video animation showing that vehicles would collide if not controlled, is provided at https://youtu.be/LKcXflY6Mtw.

[^2]:    ${ }^{2}$ A video animation showing that the controller has prevented collision can be found on https://youtu.be/VV36-eJ0tEw. In the video, it can be observed that the cars drive in a smooth way following the given crossing sequence and there is never more than one car in the intersection.

[^3]:    ${ }^{3}$ The Simulation was preformed on a computer with (Intel(R) Core(TM) i7-3520M) processor and 8 GB RAM.

