# Cooperative Intersection Control Based on Virtual Platooning 

Alejandro Ivan Morales Medina, Nathan van de Wouw, and Henk Nijmeijer, Fellow, IEEE


#### Abstract

This paper proposes a cooperative intersection control strategy, which aims to decrease the number of accidents and to increase the traffic flow at intersections. Existing high-level automation methodologies mainly focus on the determination of a safe crossing sequence of the involved vehicles, typically ignoring realistic vehicle dynamics aspects. The solution proposed in this paper, referred to as cooperative intersection control (CIC), takes into account the dynamics of the vehicles and is based on the novel concept of virtual platooning. Virtual platooning allows to form platoons of vehicles that are in different lanes of the intersection and have different directional intentions. Herewith, both safe passage of the vehicles through the intersection and a high intersection throughput (due to close "virtual" vehicle following) can be achieved. The performance of the proposed strategy is assessed, and a comparison between the CIC and an intersection controlled with traffic lights is presented.


Index Terms-Cooperative systems, virtual platoons, cooperative autonomous vehicles, and intersection management.

## I. Introduction

ROAD intersections are prone to traffic accidents since they are the places in which individual vehicle trajectories cross. In 2016, accidents in road intersections accounted for 20\% of all the traffic accidents in the European Union [1], which is a relatively high percentage for such small part of the road system. Traffic lights, roundabouts and stop signs are existing preventive measures that were devised to ensure safety of intersections. Still, a high percentage of accidents at intersections regulated by traffic lights are caused by human error. The recent development of automated vehicles aims to achieve a better performance of the driving task using sensing and behavioral protocols. The addition of Vehicle-to-vehicle (V2V) communication to such automated vehicles, has allowed to develop behavioral protocols that include cooperation between vehicles (distributed protocols), and between vehicles and

[^0]infrastructure (centralized protocols). Both approaches aim to determine a safe and efficient crossing sequence of vehicles through an intersection. Centralized approaches [2], [3], allow to optimize certain measures, such as average delay or the overall flow of vehicles, while distributed approaches [4], [5], rely on road priority to assign a suitable crossing sequence.

The existing solutions to manage an automated intersection can be categorized as Cooperative Resource Reservation approaches and Trajectory Planning approaches (as categorized in [6]). Cooperative Resource Reservation approaches [7], [8], focus on scheduling space tiles and time slots requested by vehicles intending to cross the intersection, and the Trajectory Planning approaches [9], [10], focus on the relative motion between vehicles to determine a safe crossing sequence.

In Cooperative Resource Reservation approaches, the intersection space is discretized into space tiles. When a vehicle requests to cross the intersection, a prediction of its motion is performed based on its dynamics. This prediction determines on which space tiles the vehicle would drive, and at which time, if it is granted access to the intersection. If the space tiles and time slots are free, meaning that there is no other vehicle that conflicts in time and space, then the reservation is granted. A new request has to be made if the reservation is rejected. In centralized solutions, presented in [11] and [12], the predictions and reservations are managed by an intersection agent, that receives the vehicles requests and determines the crossing sequence by solving an optimization problem. In distributed solutions, presented in [13] and [14], the space and time reservation is made by means of tokens, which are assigned to each conflict point. A vehicle that intends to cross the intersection communicates with surrounding vehicles to determine if a token is taken or not, if the token is free then the vehicle crosses the intersection, if not, the vehicle waits until the token is released.

The Trajectory Planning approaches focus on the calculation of the exact point of intersection between trajectories to define projections of vehicles driving on other lanes, or virtual vehicles, and to design time based velocity or acceleration profiles. The projection and profiles are used to generate a safe relative motion between vehicles. In the centralized solution presented in [15], an intersection agent uses the vehicle information to predict the trajectories through the intersection, the prediction is used to calculate the optimal crossing sequence. Once the sequence is defined, certain vehicles are commanded to decelerate to achieve safe crossing. In decentralized solutions, presented in [4] and [16], the road
priorities are used to determine the crossing sequence which is executed by maintaining a safe relative motion between vehicles. The work in [17] focuses on determining optimal control policies, for a fixed crossing order, by decomposing the intersection problem into an upper level time-slot allocation problem and multiple vehicle-level optimal control problems. In [18], a hybrid solution is presented, where a leader vehicle is selected to optimize the crossing sequence and communicate it to the other vehicles.

All the aforementioned works focus on the determination of the crossing sequence and pay little to no attention, to the execution of the crossing sequence on a vehicle level. The vehicles are expected to execute the predicted trajectories that are calculated considering a free road, which is not always possible because other vehicles may be waiting in the same lane to cross the intersection. The desired vehicle dynamics are just implied and no formal control laws are presented. To account for the gap between the determination and the execution of the crossing sequence we have developed the Cooperative Intersection Control (CIC) methodology. Note that the development of this methodology was part of the Grand Cooperative Driving Challenge [19]. In fact, safe passage of the vehicles through the intersection is not (only) achieved by scheduling, but mainly by direct dynamic cooperation between vehicles. Such dynamic cooperation is achieved by the introduction of the virtual platooning concept, in which platoons of vehicles (in different lanes and with different directional intentions) are formed. Doing so, a robust (to the actual dynamic behavior of the vehicles) way of providing both safe passage through the intersection and a high intersection throughput (due to close 'virtual' vehicle following) is obtained. One of the outcomes of this dynamic cooperation is that the vehicles are not required to standstill which reduces the fuel consumption since the vehicles do not idle while waiting to cross the intersection. The CIC methodology differs from the Trajectory Planning approaches (as in [5], [9], and [15]) in that it focuses on the coordination of the relative motions between vehicles disregarding time. This allows for a simplification of the two-dimensional intersection problem into a one-dimensional (virtual) platooning problem. In this context, the determination of the crossing sequence is transformed into the determination of a platoon index. When the platoon index is assigned the proper (safe) spacing is realized by the vehicle controllers. Therefore, the determination of crossing sequence does not rely on the prediction of the trajectories of the vehicles, and the subsequent scheduling of time-space tiles, as in the Cooperative Resource Reservation approaches in [8], [11], and [13]. A preliminary version of CIC was presented in [20].

In comparison with the work in [20], this paper presents, firstly, a generalization of CIC to generic intersection geometries, secondly, stability proofs for the proposed control laws, thirdly, the analysis of the performance of the proposed strategy, and, finally, a simulation comparison between the proposed CIC strategy and an intersection controlled with traffic lights.

The proposed CIC methodology (which assumes that all vehicles have both wireless communication capabilities and

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-02.jpg?height=849&width=864&top_left_y=196&top_left_x=1083)
Fig. 1. Intersection with four $(K=4)$ lanes, and several possible trajectories.

an accurate on-board GPS) comprises two hierarchical control levels: an execution level which deals with the control of the vehicle dynamics and a supervisory level that manages the access to the intersection (i.e., it determines the crossing sequence of the vehicles entering the intersection). The selected control strategies, used in the execution level, allow the decoupling of the control of the lateral and longitudinal dynamics of the vehicle, which is instrumental for the formation of the virtual platoons. The subsystems that constitute the supervisory level allow for a distributed assignment of the crossing sequence.

The rest of the paper is organized as follows; Section II presents the problem statement and the proposed solution. The details on the low-level execution part of the control strategy, i.e. the longitudinal and lateral vehicular motion controllers, are presented in Section III. The highlevel part of the control strategy, i.e. the determination of the crossing sequence and the cancellation of the virtual platooning, is described in IV. A simulation study is presented in Section V. And finally, the paper is concluded in Section VI.

## II. Problem Statement and Proposed Solution

In this section, first the problem of cooperative intersection control will be described and preliminary notational conventions will be introduced in Section II-A. Moreover, in Section II-B the main idea behind the proposed control solution is described concisely.

## A. Problem Statement

We define a generic intersection, with $K \in \mathbb{N}$ lanes and radius $r$, as the set $\mathcal{I}_{K, r}=\left\{F^{0}, \mathcal{L}\right\}$, where $F^{0}$ is referred to as the Intersection Reference Frame (IRF), and $\mathcal{L}=\left\{\mathcal{L}_{k} \mid k \in \mathcal{K}\right\}$ (where $\mathcal{K}=\{1,2, \ldots, K\}$ ) is the set of all lanes, Figure 1 depicts an intersection with $K=4$ lanes.

The IRF is defined as $F^{0}=\left\{\mathcal{Q}, \underline{\vec{e}}^{0}\right\}$, where $\mathcal{Q}$ is the center of the intersection and the center of the circle of radius $r$ that encloses the intersection-this circle is hereafter referred to as the Cooperation Zone (CZ)-and $\underline{\vec{e}}^{0}=\left[\begin{array}{ll}\vec{e}_{1}^{0} & \vec{e}_{2}^{0}\end{array}\right]^{T}$ is the orthonormal basis of the IRF, where $\vec{e}_{1}^{0}$ and $\vec{e}_{2}^{0}$ are unit vectors spanning the frame $\underline{\vec{e}}^{0}$. Note that the vector $\vec{e}_{3}^{0}=\vec{e}_{1}^{0} \times \vec{e}_{2}^{0}$ points out of the page, and that $\vec{e}_{1}^{0}$ is parallel to the middle line of lane $\mathcal{L}_{1}$. A lane is defined as $\mathcal{L}_{k}=$ $\left\{w_{k}, \psi_{k}, I^{k}, O^{k}, F^{k}\right\}$ where $w_{k}$ is the width of the lane, $\psi_{k}$ is the angle between the middle line of $\mathcal{L}_{1}$ and $\mathcal{L}_{k}, I^{k}$ is the entry point, $O^{k}$ is the exit point, and $F^{k}=\left\{I^{k}, \underline{\vec{e}}^{k}\right\}$ is the Lane Frame (LF). The orthonormal basis of the LF is given by

$$
\underline{\vec{e}}^{k}=\underline{A}^{k 0}\left(\Psi_{k}\right) \underline{\vec{e}}^{0}
$$

where $\Psi_{k}=\pi+\psi_{k}$, and

$$
\underline{A}^{k 0}\left(\Psi_{k}\right)=\left[\begin{array}{cc}
\cos \Psi_{k} & \sin \Psi_{k} \\
-\sin \Psi_{k} & \cos \Psi_{k}
\end{array}\right]
$$

is the direction cosine matrix associated with a rotation about $\vec{e}_{3}^{0}$. The position of the entry point of each lane with respect to the IRF is given by the vector $\vec{r}_{I^{k}}=\underline{r}_{I^{k}}^{0^{T}} \underline{\vec{e}}^{0}$, the coordinates of which are given by

$$
\underline{r}_{I^{k}}^{0^{T}}=\left[\begin{array}{ll}
r & \frac{1}{4} w_{k}
\end{array}\right] \underline{A}^{k 0}\left(\psi_{k}\right) .
$$

Similarly, the position of the exit point of each lane with respect to the IRF is given by the vector $\vec{r}_{O^{k}}=\underline{r}_{O^{k}}^{0^{T}} \vec{e}^{0}$ which coordinates are given by

$$
\underline{r}_{O^{k}}^{0^{T}}=\left[\begin{array}{ll}
r & -\frac{1}{4} w_{k}
\end{array}\right] \underline{A}^{k 0}\left(\psi_{k}\right) .
$$

A vehicle that intends to cross the intersection entering on lane $\mathcal{L}_{\eta}$ and exiting on lane $\mathcal{L}_{\omega}(\eta, \omega \in \mathcal{K})$, will drive the trajectory $\mathcal{C}_{\eta, \omega}$. The trajectories of two vehicles driving through the intersection can be either non-crossing or crossing trajectories. Figure 1 shows an example of non-crossing trajectories ( $\mathcal{C}_{4,2}$ and $\mathcal{C}_{3,4}$ ) and crossing trajectories ( $\mathcal{C}_{4,2}$ and $\mathcal{C}_{1,3}$ ). If two vehicles have non-crossing trajectories, then these can cross the intersection at the same time in a safe manner. A coordination problem arises when two vehicles have crossing trajectories making a collision possible.

The Intersection Vehicle Counter (IVC) is a label that identifies every vehicle that enters the CZ and is defined as $i \in[\underline{i}, \bar{i}]$, where $\underline{i} \in \mathbb{N}_{0}$ and $\bar{i} \in \mathbb{N}_{0}$ are the minimum and maximum value of the IVC of the vehicles inside the CZ, respectively. Note that $\bar{i}$ increases by one every time a vehicle enters the CZ (if there are no vehicles inside the CZ then $\underline{i}=\bar{i}=0$ ). Therefore, the vehicle $V_{i}$ will follow the trajectory $\mathcal{T}_{i} \equiv \mathcal{C}_{\eta_{i}, \omega_{i}}$.

Consider two vehicles that intend to cross the intersection; the vehicle $V_{m}$, where $m=\bar{i}$, which is the last vehicle to enter the CZ, and a vehicle $V_{n}$, where $n \in[\underline{i}, \bar{i})$, which is already inside the CZ. For instance, in Figure 1; $V_{m}$ will drive along $\mathcal{T}_{m} \equiv \mathcal{C}_{4,2}$ with an associated curvilinear path coordinate defined as $s_{m}$, and $V_{n}$ will drive along $\mathcal{T}_{n} \equiv \mathcal{C}_{1,3}$ with an associated curvilinear path coordinate defined as $s_{n}$.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-03.jpg?height=449&width=481&top_left_y=200&top_left_x=1276)
Fig. 2. Collision point and region of two crossing trajectories.

These trajectories intersect in the collision point $\mathcal{X}_{m, n}$ (note that the point $\mathcal{X}_{m, n}$ is undefined if the trajectories are non-crossing). Since the vehicles are not considered as particles, but rather vehicles with certain dimension, there is a collision region $\mathcal{W}_{m, n}$ around the collision point $\mathcal{X}_{m, n}$ which is determined by the geometry of the vehicles. Figure 2 shows the collision region as a function of the path coordinates $s_{m}$ and $s_{n}$ (note that the path coordinates refer to the back bumper of the vehicles). For the sake of simplicity, the collision region $\mathcal{W}_{m, n}$ is represented as a square with the collision point $\mathcal{X}_{m, n}$ as one of its vertices. Note that this representation can be applied to any pair of trajectories even if they are curved.

Figure 2, which is inspired by the work in [21], shows three instances of relative motions of the vehicles. The relative motion $\mathcal{R}_{m=n}$ depicts an unsafe scenario in which the two vehicles would collide; this is true for any relative motion that crosses $\mathcal{W}_{m, n}$. The relative motion $\mathcal{R}_{m>n}$ exemplifies a safe crossing in which vehicle $V_{n}$ crosses the intersection before $V_{m}$. Similarly, the relative motion $\mathcal{R}_{m<n}$ exemplifies a safe crossing in which vehicle $V_{m}$ crosses the intersection before $V_{n}$.

Therefore, the problem to be solved is to design a control strategy such that, for any pair of trajectories $\mathcal{T}_{m}$ and $\mathcal{T}_{n}$ for which the collision point $\mathcal{X}_{m, n}$ is defined, the relative motion between the host vehicle $V_{m}$ and the target vehicle $V_{n}$ is of the class $\mathcal{R}_{m>n}$. Moreover, the relative motion has to be such that it is as close as possible to the collision region (which is achieved by virtual platooning) for the throughput to be increased.

## B. Proposed Solution

The proposed solution is referred to as Cooperative Intersection Control (CIC) that relies on Vehicle to Vehicle (V2V) communication to achieve an efficient, smooth and safe crossing of vehicles through an intersection. The three key control concepts underlying CIC are, firstly, virtual platooning for longitudinal control, path following for lateral control, and a First-Come-First-Serve (FCFS) crossing sequence governing the access of vehicles to the intersection.

The architecture of the CIC methodology is depicted in Figure 3. The execution level, as described in Section III, takes care of the lateral and longitudinal control of the vehicle.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-04.jpg?height=597&width=685&top_left_y=211&top_left_x=256)
Fig. 3. System architecture.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-04.jpg?height=404&width=537&top_left_y=950&top_left_x=339)
Fig. 4. Representation of the car-like configuration.

The lateral path following control ensures that the vehicle follows a predefined path, while the longitudinal control (based on virtual platooning) modifies the velocity of the vehicles to ensure safe passage of the vehicles through the intersection. The supervision level, as described in detail in Section IV, governs the access of vehicles to the intersection (based on the FCFS protocol) and assigns a safe crossing sequence for the vehicles. The supervision level of control also contains a Target Vehicle Assignment (TVA) protocol and a Control Reconfiguration protocol. The TVA system checks whether, for a vehicle gaining access to the intersection, a vehicle with crossing trajectory is present in the intersection and, if so, assigns it as the target vehicle that should be followed by the longitudinal (virtual platooning) controller. The Control Reconfiguration system realizes a smooth transition between control modes when the suitable control mode to achieve a specific control objective is determined, see Section IV for more details.

## III. Execution Control Level

In Section III-A, the lateral path-following controller will be designed, in Section III-B, the concept of virtual platooning will be introduced as a basis for longitudinal control, and in Section III-C the relation between the lateral and longitudinal controllers is described.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-04.jpg?height=322&width=726&top_left_y=198&top_left_x=1156)
Fig. 5. Coordinate representation in a Frénet frame.

## A. Path-Following Control

1) Model for Lateral Vehicle Dynamics: Consider the carlike kinematic model, defined in [22] and depicted in Figure 4, given by

$$
\left\{\begin{aligned}
\dot{x} & =v \cos \theta \\
\dot{y} & =v \sin \theta \\
\dot{\theta} & =\frac{v}{L} \tan \phi \\
\dot{\phi} & =\sigma\left(u_{y}-\phi\right)
\end{aligned}\right.
$$

where $[x, y]^{T}$ are the coordinates of the point $\mathcal{P}$ with respect to the frame $F=\{I, \underline{\vec{e}}\}, \theta$ is the orientation of the vehicle with respect to the frame $\underline{\vec{e}}, L$ is the length between the rear and front axles, $\phi$ is the steering angle, $\sigma$ is a time constant related to the actuation of the steering wheel, and $u_{y}$ is the reference steering angle. Moreover, note that, due to a no side slip condition on the tyres, $\theta$ is also the orientation of the forward velocity vector, of magnitude $v$, of point $\mathcal{P}$.

Now, consider a path $\mathcal{C}$ in space as shown in Figure 5. By projecting orthogonally the point $\mathcal{P}$, see Figure 5 for its meaning, on the curve $\mathcal{C}$ we obtain three variables, namely the path coordinate $s$, the distance $d$, and the orientation error $\theta_{e}=\theta-\theta_{s}$, which is the difference between the orientation of the velocity vector and the orientation of the tangent to the curve $\mathcal{C}$ at point $s$. We can define the Frénet frame $T=\left\{\mathcal{P}_{s}, \underline{\vec{b}}\right\}$ such that $\underline{\vec{b}}=\underline{A}^{b e}\left(\theta_{s}\right) \underline{\vec{e}}$, note that $\underline{A}^{b e}\left(\theta_{s}\right)$ has the same structure as (2).

The position vector of $\mathcal{P}$ is given by $\vec{r}_{\mathcal{P}}=\left[\begin{array}{ll}x & y\end{array}\right] \underline{\vec{e}}$ and its time derivative, according to (5) and $\underline{\vec{e}}=\underline{A}^{b e^{T}}\left(\theta_{S}\right) \underline{\vec{b}}$, is given by

$$
\begin{aligned}
\dot{\vec{r}}_{\mathcal{P}} & =\left[\begin{array}{ll}
v \cos \theta & v \sin \theta
\end{array}\right] \underline{\vec{e}} \\
& =\left[\begin{array}{ll}
v \cos \theta_{e} & v \sin \theta_{e}
\end{array}\right] \underline{\vec{b}} .
\end{aligned}
$$

The position vector of $\mathcal{P}$ can also be written as $\vec{r}_{\mathcal{P}}=$ $\vec{r}_{\mathcal{P}_{s}}+\vec{r}_{\mathcal{P} / \mathcal{P}_{s}}$ where $\vec{r}_{\mathcal{P} / \mathcal{P}_{s}}=\left[\begin{array}{ll}0 & d\end{array}\right] \underline{\vec{b}}$; hence, its time derivative satisfies

$$
\begin{aligned}
\dot{\vec{r}}_{\mathcal{P}} & =\dot{\vec{r}}_{\mathcal{P}_{s}}+\dot{\vec{r}}_{\mathcal{P}} / \mathcal{P}_{s} \\
& =\left[\begin{array}{ll}
\dot{s} & 0
\end{array}\right] \underline{\vec{b}}+\left[\begin{array}{ll}
0 & \dot{d}
\end{array}\right] \underline{\vec{b}}+\left[\begin{array}{ll}
0 & d
\end{array}\right] \underline{\vec{b}} \\
& =\left[\begin{array}{ll}
\dot{s} & \dot{d}
\end{array}\right] \underline{\vec{b}}+\left[\begin{array}{ll}
0 & d \dot{\theta}_{s}
\end{array}\right]\left[\begin{array}{cc}
-\sin \theta_{s} & \cos \theta_{s} \\
-\cos \theta_{s} & -\sin \theta_{s}
\end{array}\right] \underline{\vec{e}} \\
& =\left[\begin{array}{ll}
\dot{s} & \dot{d}
\end{array}\right] \overrightarrow{\vec{b}}+\left[-d \dot{\theta}_{s}\right. \\
& =\left[\begin{array}{ll}
\dot{s}-d \dot{\theta}_{s} & \dot{d}
\end{array}\right] \underline{\vec{b}}
\end{aligned}
$$

where $\dot{\theta}_{s}$ can be rewritten as $\dot{\theta}_{s}=\frac{\partial \theta_{s}}{\partial s} \dot{s}$ or $\dot{\theta}_{s}=\kappa(s) \dot{s}$, where $\kappa(s)$ is referred to as the curvature of $\mathcal{C}$ at $s$.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-05.jpg?height=679&width=685&top_left_y=213&top_left_x=264)
Fig. 6. Possible trajectories for a vehicle in lane $\mathcal{L}_{\eta}$.

By comparing (6) with (7) and considering the car-like model in (5) we obtain the kinematic model in terms of the path coordinates given by

$$
\left\{\begin{array}{l}
\dot{s}=\frac{v \cos \theta_{e}}{1-d \kappa(s)} \\
\dot{d}=v \sin \theta_{e} \\
\dot{\theta}_{e}=\frac{v}{L} \tan \phi-\kappa(s) \dot{s} \\
\dot{\phi}=\sigma\left(u_{y}-\phi\right) .
\end{array}\right.
$$

2) Trajectory Description: To define the path-following coordinates in the context of the intersection consider a vehicle entering in an arbitrary input lane $\mathcal{L}_{\eta}$ and exiting through the lane $\mathcal{L}_{\omega}$, with $\eta, \omega \in \mathcal{K}$. Figure 6 shows the possible trajectories (in a four lane intersection). Note that it is straight-forward to generalize to more complex intersection geometries.

Consider the intention function

$$
\imath(\eta, \omega)= \begin{cases}0, & \text { if }\left|\xi\left(\psi_{\omega}-\psi_{\eta}\right)\right|=\pi \\ 1, & \text { if } 0>\xi\left(\psi_{\omega}-\psi_{\eta}\right)>-\pi \\ -1, & \text { if } 0<\xi\left(\psi_{\omega}-\psi_{\eta}\right)<\pi\end{cases}
$$

where $\xi(\psi)=\psi-2 \pi\left\lfloor\frac{\psi+\pi}{2 \pi}\right\rfloor$, which differentiates between a left turn trajectory $\left(\iota\left(\eta, \omega_{1}\right)=1\right)$, a right turn trajectory $\left(\imath\left(\eta, \omega_{2}\right)=-1\right)$, and a straight trajectory $\left(\imath\left(\eta, \omega_{3}\right)=0\right)$, see also the lane numbering as introduced in Figure 1. Both leftand right-turn trajectories consist of three segments: a straight line at the entry lane, a circular arc that connects the entry lane with the exit lane and a straight line at the exit lane. If the entry and exit lanes are parallel the arc segment disappears and a straight trajectory results. Therefore, we can define three regions: $\mathcal{Z}_{1}$ for the entry line, $\mathcal{Z}_{2}$ for the $\operatorname{arc}$, and $\mathcal{Z}_{3}$ for the exit line; note that in the case of the straight trajectory the region $\mathcal{Z}_{1}$ extends from the entry lane to the exit lane.

To define these regions consider the position vector of a point $\mathcal{P}$ given by

$$
\vec{r}_{\mathcal{P} / I^{\eta}}=\left[\begin{array}{ll}
x_{\eta} & y_{\eta}
\end{array}\right] \underline{\vec{e}}^{\eta},
$$

where $I^{\eta} \in \mathcal{L}_{\eta}$ is the entry point, $\left\{x_{\eta}, y_{\eta}\right\}$ are the coordinates and $\underline{\vec{e}}^{\eta} \in F^{\eta}$ is the orthonormal basis of the entry lane frame. Moreover, consider the position vector of the center of the circular arc $Q^{\omega}$ (see Figure 6) given by

$$
\vec{r}_{Q^{\omega} / I^{\eta}}=\left[x_{R}(\eta, \omega) y_{R}(\eta, \omega)\right] \underline{e}^{\eta}
$$

where

$$
x_{R}(\eta, \omega)=r-R+\frac{1}{4} l(\eta, \omega) w_{\omega} \quad \text { and, } y_{R}(\eta, \omega)=\imath(\eta, \omega) R,
$$

where $r$ is the radius of the intersection, $R$ is the radius of the circular arc, and $w_{\omega} \in \mathcal{L}_{\omega}$ is the width of the exit lane. Note that the value of $R$ is calculated using the maximum desired lateral acceleration $a_{y}$ such that $R=v_{R}^{2} / a_{y}$ (note that a uniform circular motion is considered to calculate the radius), where $v_{R}$ is the maximum longitudinal velocity during the turn.

Using (9), (10), and (11) we can define the regions as

$$
\begin{aligned}
& \mathcal{Z}_{1} \equiv \begin{cases}\left(x_{\eta} \leq x_{R}\right), & \text { if } \imath \neq 0 \\
\left(0 \leq x_{\eta} \leq 2 r \wedge\left|y_{\eta}\right| \leq r\right), & \text { if } \imath=0\end{cases} \\
& \mathcal{Z}_{2} \equiv\left(x_{\eta}>x_{R} \wedge l y_{\eta} \leq l y_{R}\right), \quad \text { if } \imath \neq 0 \\
& \mathcal{Z}_{3} \equiv\left(\imath y_{\eta}>l y_{R}\right), \quad \text { if } \imath \neq 0 .
\end{aligned}
$$

To define the path-following coordinates, it is necessary to calculate the smallest distance from a point to a curve, the proximal point of the involved projection, and the curvature at that proximal point. This is straightforward for the straight lines in the regions $\mathcal{Z}_{1}$ and $\mathcal{Z}_{3}$. For the circular arc in zone $\mathcal{Z}_{2}$, consider the equation parametrizing the line segment that connects $\mathcal{P}$ and $Q^{\omega}$ given by

$$
x=x_{R}+\Delta x_{\eta, R} v \quad \text { and, } y=y_{R}+\Delta y_{\eta, R} v,
$$

where $\nu>0, \Delta x_{\eta, R}=x_{\eta}-x_{R}$ and $\Delta y_{\eta, R}=y_{\eta}-y_{R}$, and consider the equation of a circle

$$
\left(x-x_{R}\right)^{2}+\left(y-y_{R}\right)^{2}=R^{2} .
$$

By substituting (14) in (15), solving for $v$ and, subsequently, substituting the result in (14), we obtain that the coordinates of the proximal point are given by

$$
x_{C}=x_{R}+\frac{\Delta x_{\eta, R} R}{\bar{d}_{\eta, R}} \quad \text { and, } y_{C}=y_{R}+\frac{\Delta y_{\eta, R} R}{\bar{d}_{\eta, R}},
$$

where

$$
\bar{d}_{\eta, R}=\sqrt{\Delta x_{\eta, R}^{2}+\Delta y_{\eta, R}^{2}} .
$$

With this point we can calculate the angle

$$
\gamma=\arccos \left(\frac{\imath\left(y_{R}-y_{C}\right)}{R}\right)
$$

depicted in Figure 6, which is used to calculate the arc length from the entry point to the calculated proximal point in the region $\mathcal{Z}_{2}$.

Finally, we can define the path following coordinates for all possible trajectories through the intersection as

$$
\begin{aligned}
& s= \begin{cases}x_{\eta}, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{1} \\
x_{R}+\gamma R, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{2} \\
x_{R}+\frac{\pi}{2} R+\imath y_{\eta}-R, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{3}\end{cases} \\
& d= \begin{cases}y_{\eta}, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{1} \\
l\left(R-\bar{d}_{\eta, R}\right), & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{2} \\
\frac{1}{4} w_{\omega}+\imath\left(r-x_{\eta}\right), & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{3}\end{cases} \\
& \theta_{e}= \begin{cases}\theta_{\eta}, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{1} \\
\theta_{\eta}-\imath \gamma, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{2} \\
\theta_{\eta}-\imath \frac{\pi}{2}, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{3}\end{cases} \\
& \kappa= \begin{cases}0, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{1} \\
l / R, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{2} \\
0, & \text { for }\left(x_{\eta}, y_{\eta}\right) \in \mathcal{Z}_{3} .\end{cases}
\end{aligned}
$$

3) Lateral Controller Design: Next, we design a pathfollowing control law with the following objective:

$$
\lim _{t \rightarrow \infty}\left\{d, \theta_{e}\right\}=\{0,0\} .
$$

Hereto, we apply the coordinate transformation

$$
\left(s, d, \theta_{e}, \phi, v, u_{y}\right) \mapsto\left(z_{1}, z_{2}, z_{3}, z_{4}, v_{1}, v_{2}\right)
$$

to (8) to transform the dynamics into the chain form system defined as

$$
\begin{aligned}
& \dot{z}_{1}=v_{1} \\
& \dot{z}_{2}=v_{1} z_{3} \\
& \dot{z}_{3}=v_{1} z_{4} \\
& \dot{z}_{4}=v_{2} .
\end{aligned}
$$

The transformation, as presented in [22], is as follows:

$$
\begin{aligned}
z_{1} & =s \\
z_{2} & =d \\
z_{3} & =(1-d \kappa) \tan \theta_{e} \\
z_{4} & =\frac{1}{L}(1-d \kappa)^{2} \sec ^{3} \theta_{e} \tan \phi-\kappa(1-d \kappa)\left(1+2 \tan ^{2} \theta_{e}\right) \\
v_{1} & =\dot{z}_{1} \\
v_{2} & =\dot{z}_{4}
\end{aligned}
$$

where $\kappa$ is piece-wise constant.
If we consider the term $v_{1}$ in (22) as a time-varying parameter, then (22) can be rewritten as

$$
\begin{aligned}
\dot{\tilde{z}}_{1} & =0 \\
{\left[\begin{array}{c}
\dot{z}_{2} \\
\dot{z}_{3} \\
\dot{z}_{4}
\end{array}\right] } & =\left[\begin{array}{ccc}
0 & v_{1}(t) & 0 \\
0 & 0 & v_{1}(t) \\
0 & 0 & 0
\end{array}\right]\left[\begin{array}{l}
z_{2} \\
z_{3} \\
z_{4}
\end{array}\right]+\left[\begin{array}{l}
0 \\
0 \\
1
\end{array}\right] v_{2}
\end{aligned}
$$

with

$$
\tilde{z}_{1}=z_{1}-\int_{0}^{t} v_{1}(\tau) d \tau
$$

If $v_{1}(t)$ is considered to be continuous, bounded and strictly positive, i.e., $0<\hat{v}_{1} \leq v_{1}(t)$, then $z_{1}$ will vary monotonically with time with

$$
\lim _{t \rightarrow \infty} z_{1}(t)=\infty .
$$

Thus $z_{1}$ can be taken as a new transformed time variable. This change of variable, presented in [23], is referred to as the $v_{1}$-time-scaling procedure.

Therefore, we can rewrite the second part of (24) as

$$
\left[\begin{array}{l}
z_{2}^{[1]} \\
z_{3}^{[1]} \\
z_{4}^{[1]}
\end{array}\right]=\left[\begin{array}{lll}
0 & 1 & 0 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{array}\right]\left[\begin{array}{l}
z_{2} \\
z_{3} \\
z_{4}
\end{array}\right]+\left[\begin{array}{l}
0 \\
0 \\
1
\end{array}\right] w_{2},
$$

where $z_{i}^{[1]} \equiv \partial z_{i} / \partial z_{1} \forall i=2,3,4$, and $w_{2} \equiv v_{2} / v_{1}(t)$. This system is linear and $v_{1}$-invariant and can be stabilized with a static feedback control law. To include integral action to the control law, with the purpose of rejecting steady-state errors, define the control state $z_{0}$ as

$$
\dot{z}_{0}=v_{1} z_{2} \quad \text { or } \quad z_{0}=\int_{0}^{t} v_{1}(\tau) z_{2} d \tau
$$

Including the $z_{0}$ dynamics in (27) we obtain

$$
Z^{[1]}=\left[\begin{array}{llll}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right] Z+\left[\begin{array}{l}
0 \\
0 \\
0 \\
1
\end{array}\right] w_{2}
$$

where $Z=\left[\begin{array}{llll}z_{0} & z_{2} & z_{3} & z_{4}\end{array}\right]^{T}$.
We design the linear feedback for $w_{2}$ in (29) given by

$$
w_{2}=-\left[\begin{array}{llll}
k_{0} & k_{2} & k_{3} & k_{4}
\end{array}\right] Z .
$$

Note that the mapping $w_{2} \mapsto u_{y}$ is given by

$$
u_{y}=\frac{\left(v_{1}(t) w_{2}+\zeta_{4}-\zeta_{5}\right) L \cos \phi}{\sigma \zeta_{1}^{2} \zeta_{2}^{3}}+\phi
$$

where

$$
\begin{aligned}
& \zeta_{1}=1-d \kappa ; \quad \dot{\zeta}_{1}=-\kappa \dot{d} \\
& \zeta_{2}=\sec \theta_{e} ; \quad \dot{\zeta}_{2}=\dot{\theta}_{e} \sec \theta_{e} \tan \theta_{e} \\
& \zeta_{3}=\tan \theta_{e} ; \quad \dot{\zeta}_{3}=\dot{\theta}_{e} \sec ^{2} \theta_{e} \\
& \zeta_{4}=\kappa\left(\dot{\zeta}_{1}\left(1+2 \zeta_{3}^{2}\right)+4 \zeta_{1} \zeta_{3} \dot{\zeta}_{3}\right) \\
& \zeta_{5}=L^{-1} \zeta_{1}\left(2 \dot{\zeta}_{1} \zeta_{2}^{3}+3 \zeta_{1} \zeta_{2} \dot{\zeta}_{2}\right) \tan \phi
\end{aligned}
$$

with $\dot{d}$, and $\dot{\theta}_{e}$ as in (8).
Applying the control law in (30) to (29) gives the closedloop dynamics

$$
Z^{[1]}=\Xi Z
$$

where

$$
\Xi=\left[\begin{array}{rrrr}
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
-k_{0} & -k_{2} & -k_{3} & -k_{4}
\end{array}\right] .
$$

Given the fact that the system in (29) is controllable, we can perform pole-placement using the feedback law in (30) to ensure that the poles $\lambda_{i}, \forall i=\{1,2,3,4\}$, of (33)
satisfy $\Re\left(\lambda_{i}\right)<0 \forall i=\{1,2,3,4\}$. As a consequence, we have that

$$
\lim _{z_{1} \rightarrow \infty} Z\left(z_{1}\right)=0,
$$

which together with (26) implies that

$$
\lim _{t \rightarrow \infty} Z(t)=0
$$

which, in turn, implies that the objective in (20) is met since $z_{2}=d$, and $z_{3}=(1-d \kappa) \tan \theta_{e}$ converge to zero.

We can conclude that we can achieve the stabilization of the time-varying system in (24) with the time-varying control law given by

$$
\begin{aligned}
v_{2} & =v_{1}(t) w_{2} \\
& =-v_{1}(t)\left[\begin{array}{llll}
k_{0} & k_{2} & k_{3} & k_{4}
\end{array}\right] Z .
\end{aligned}
$$

Therefore, the result of substituting (37) in (31) will ensure the path-following of the system in (8).

## B. Virtual Platooning for Longitudinal Control

Before defining the virtual platooning concept, we introduce the longitudinal vehicle dynamics model, and different longitudinal control modes, such as CC which is a velocity control, CACC which is an inter-vehicle distance control, and VCACC which expands the CACC functionality to two dimensions. Additionally, we assume that the vehicles are on their desired paths (i.e. the lateral controllers, designed in the previous section, are functioning properly).

We employ the linearized longitudinal vehicle dynamics model, presented in [24], given by

$$
\left\{\begin{array}{l}
\dot{\delta}=v_{t}-v \\
\dot{v}=a \\
\dot{a}=-\frac{1}{\tau} a+\frac{1}{\tau} u_{x}
\end{array}\right.
$$

where $\delta$ is the inter-vehicle distance, $v_{t}$ is the velocity of the target vehicle, $v$ is the velocity of the host vehicle, $a$ is the acceleration, $\tau$ is a time constant related to the drive line of the vehicle, and $u_{x}$ is the reference acceleration input.

1) Cruise Control (CC): The objective of this control mode is to realize a reference velocity $v_{\text {ref }}$. Consider the error state $e=v-v_{\text {ref }}$ with time derivative $\dot{e}=a-a_{\text {ref }}$, where $a_{\text {ref }}=\dot{v}_{\text {ref }}$. Define $e_{1}=e$ and $e_{2}=\dot{e}$ such that $\dot{e}_{1}=e_{2}$ and $\dot{e}_{2}=\ddot{e}=\dot{a}$ (note that we consider $\dot{a}_{\text {ref }}=0$ ). Using (38), we obtain

$$
\dot{e}_{2}=\frac{1}{\tau}\left(-a+u_{x}\right)=\frac{1}{\tau}\left(-e_{2}-a_{r e f}+u_{x}\right) .
$$

Consider the control law given by

$$
u_{x}=-k_{c c} e_{1}+a_{r e f}
$$

which yields the following closed-loop error dynamics:

$$
\left[\begin{array}{l}
\dot{e}_{1} \\
\dot{e}_{2}
\end{array}\right]=\left[\begin{array}{cc}
0 & 1 \\
-\frac{k_{c c}}{\tau} & -\frac{1}{\tau}
\end{array}\right]\left[\begin{array}{l}
e_{1} \\
e_{2}
\end{array}\right]
$$

which is exponentially stable for $k_{c c}, \tau>0$. Therefore, the CC control input $u_{x, 1}$ given by

$$
u_{x, 1}=-k_{c c}\left(v-v_{r e f}\right)+a_{r e f}
$$

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-07.jpg?height=623&width=780&top_left_y=202&top_left_x=1134)
Fig. 7. Platooning and virtual platooning.

exponentially stabilizes the dynamics in (38) at a reference velocity $v_{\text {ref }}$, with time derivative $a_{\text {ref }}$, for $k_{c c}>0$.
2) Cooperative Adaptive Cruise Control (CACC): The objective of this control mode is to realize a reference intervehicle distance $\delta_{\text {ref }}=r+h v$ where $r$ is the stand-still distance, $h$ is the headway time, and $v$ is the velocity of the host vehicle. The inter-vehicle distance between the target vehicle, represented by $\mathcal{P}_{t}$ in Figure 7, and the host vehicle represented by $\mathcal{P}$ is defined as

$$
\delta=s_{t}-s-L,
$$

where $L$ is the length of the host vehicle, $s$ is the path coordinate of the host vehicle, and $s_{t}$ is the path coordinate of the target vehicle. Note that both $s$ and $s_{t}$ are referenced to the frame $F$.

Consider the CACC control input $u_{x, 2}$ given by

$$
\dot{u}_{x, 2}=\frac{1}{h}\left(u_{x, t}-u_{x, 2}+k_{p}(\delta-(r+h v))+k_{d}(\dot{\delta}-h a)\right)
$$

where $u_{x, t}$, which is the reference acceleration of the target vehicle, is obtained through V2V communication. This control law ensures that a vehicle, modeled by (38), exponentially stabilizes a reference inter-vehicle distance $\delta_{\text {ref }}$, for $h>0$, and $k_{d}>\tau k_{p}$; the reader is referred to [24], and [25] for the details of the stability analysis of the control law in (44).
3) Virtual CACC (VCACC): The objective of this control mode is to expand the CACC functionality into two dimensions using coordinate transformations. In other words, we aim to achieve virtual platooning of (two) vehicles driving two distinct (potentially curved) trajectories through the intersection. Consider the target vehicle, represented in Figure 7 by $\mathcal{P}_{t}$ with path coordinate $s_{t}$ referenced to the frame $F$, and the host vehicle represented by $\tilde{\mathcal{P}}$ with path coordinate $\tilde{s}$ referenced to the frame $\tilde{F}$. Note that now $\mathcal{P}_{t}$ and $\tilde{\mathcal{P}}$ are not necessarily following the same straight path, as in the case of CACC, but may follow distinct (possibly curved) paths associated with distinct routes through the intersection from different lanes. Still, we can define the so-called virtual inter-vehicle distance as

$$
\tilde{\delta}=s_{t}-\tilde{s}-L-S_{t}+\tilde{S},
$$

where $s_{t}$ is the path coordinate of the target vehicle along its path $\mathcal{T}_{n}, \tilde{s}$ is the path coordinate of the host vehicle along its path $\mathcal{T}_{m}, S_{t}$ is the traveled distance from $I$ to the collision point $\mathcal{X}_{m, n}$ (defined in Section II-A), and $\tilde{S}$ is the traveled distance from $\tilde{I}$ to $\mathcal{X}_{m, n}$. These traveled distances $S_{t}$ and $\tilde{S}$ are, hereafter, referred to as the distances to collision and are constants that represent the path lengths from the entry point, either $I$ or $\tilde{I}$ in this case, to the collision point $\mathcal{X}_{m, n}$. Note that the virtual inter-vehicle distance definition is useful to achieve a virtual inter-vehicle reference distance, given by $\tilde{\delta}_{\text {ref }}=\tilde{r}+\tilde{h} v$, for vehicles driving on different (curved) paths that have a collision point. In other words, the host vehicle will modify its velocity along its path to allow the target vehicle to cross the collision point first. Moreover, it is evident that CACC functionality is a special case of the VCACC in which both the host and target vehicles drive on the same (straight) path such that $S_{t}=\tilde{S}$ which yields the definition in (43).

Given this insight, we propose and extension of the CACC controller in (44) towards a VCACC controller with control input $u_{x, 3}$ as follows:

$$
\dot{u}_{x, 3}=\frac{1}{\tilde{h}}\left(u_{x, t}-u_{x, 3}+k_{p}(\tilde{\delta}-(\tilde{r}+\tilde{h} v))+k_{d}(\dot{\tilde{\delta}}-\tilde{h} a)\right),
$$

where $u_{x, t}$ is obtained through V2V communication. This VCACC control law ensures that a vehicle, modeled by (38), exponentially stabilizes a virtual reference inter-vehicle distance $\tilde{\delta}_{\text {ref }}$, for $\tilde{h}>0$, and $k_{d}>\tau k_{p}$.
4) Control Mixing: The three aforementioned control modes are mixed, as described in [26], to achieve the control signal

$$
u_{x}=\sum_{i=1}^{3} \beta_{i} u_{x, i},
$$

which is a convex combination of (42), (44), and (46), where the mixing signals are such that $\beta_{i}>0$ and $\sum_{i=1}^{3} \beta_{i}=1$. The control signal in (47) allows the model in (38) to have CC, CACC, and VCACC as control modes. Note that the mixing signals will be briefly described in Section IV-B.

To define the concept of a Virtual Platoon (VP) consider the three vehicles in Figure 7. In this figure, the vehicle represented by $\mathcal{P}_{t}$ drives with its CC mode, the vehicle represented by $\tilde{\mathcal{P}}$ follows $\mathcal{P}_{t}$ using its VCACC mode, and finally the vehicle represented by $\mathcal{P}$ follows $\tilde{\mathcal{P}}$ which uses its VCACC mode, see also Figure 8(a). Using VCACC such a VP will cross the collision point $\mathcal{X}_{m, n}$ in a safe manner. As a second example of a virtual platooning with three vehicles involving different control modes (Figure 8(b)), consider $\mathcal{P}_{t}$ as the leader of the VP, which drives in CC mode and is followed by $\mathcal{P}$ using its CACC mode. Finally, $\tilde{\mathcal{P}}$ follows $\mathcal{P}$ using its VCACC mode.

## C. Integration of Path Following Control and Virtual Platooning

In order to explain the integration of the proposed lateral and longitudinal control concepts, consider two vehicles obeying the kinematics described by (8) and following a specific path.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-08.jpg?height=415&width=758&top_left_y=211&top_left_x=1139)
Fig. 8. Examples of virtual platoons.

Additionally, assume that one of such vehicles is following the other using either CACC or VCACC. The inter-vehicle distance in (43) and the virtual inter-vehicle distance in (45) can be generalized as

$$
\delta=s_{t}-s-L-S_{t}+S
$$

where $s_{t}$ is the path coordinate of the target vehicle, $s$ is the path coordinate of the host vehicle, $L$ is the length of the host vehicle, $S_{t}$ and $S$ are the total traveled distances to the collision point for the target and host vehicle, respectively (note that $S_{t}-S=0$ in case of CACC). Its derivative is given by

$$
\begin{aligned}
\dot{\delta} & =\dot{s}_{t}-\dot{s} \\
& =\frac{v_{t} \cos \theta_{e, t}}{1-d_{t} \kappa_{t}}-\frac{v \cos \theta_{e}}{1-d \kappa},
\end{aligned}
$$

where $\theta_{e, t}, d_{t}$, and $\kappa_{t}$ are the path-following coordinates related to the target vehicle. We know that the lateral control law in (31) realizes the control objective in (20), i.e., the lateral control objective is achieved irrespective of the longitudinal dynamics. As a consequence,

$$
\lim _{t \rightarrow \infty} d(t)=\lim _{t \rightarrow \infty} d_{t}(t)=\lim _{t \rightarrow \infty} \theta_{e}(t)=\lim _{t \rightarrow \infty} \theta_{e, t}(t)=0
$$

and the limit of (49) as $t \rightarrow \infty$ equals

$$
\lim _{t \rightarrow \infty} \dot{\delta}=v_{t}-v
$$

which corresponds to the (isolated) longitudinal dynamics in (38).

We can conclude that, as long as the time scale of the closed-loop lateral dynamics is faster (i.e., sufficiently separated from) that of the closed-loop longitudinal dynamics, we can achieve a decoupled control of the longitudinal motion of a vehicle, as is described as in (38), and the lateral motion of a vehicle, as is described in (8) to cross an intersection in a safe manner using V2V communication.

## IV. Supervison Level

In Section III, we have described the execution level control strategies necessary to cross the intersection in a safe manner. In this section, we describe the strategies used to form the so-called Virtual Platoon and the control reconfiguration method used to switch between the different control modes. Section IV-A explains the Target Vehicle Assignment subsystem that is triggered when a vehicle enters the intersection and is responsible of the virtual platoon forming.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-09.jpg?height=571&width=571&top_left_y=211&top_left_x=320)
Fig. 9. All possible trajectories through the intersection and all collision points.

Section IV-B explains the Mixing strategy used to achieve a smooth switch between control modes, in particular for the cases when the vehicle enters the intersection and when the vehicle has crossed the intersection.

## A. Target Vehicle Assignment

Figure 9 shows all possible trajectories through the intersection and all the related collision points (circles). As mentioned in Section III-A, every trajectory consist of lines and circular arcs; therefore, we refer to that section for the calculation of the collision point between two given trajectories and focus here on the calculation of other variables relevant for the Target Vehicle Assignment.

Consider the vehicle $V_{m}$ with trajectory $\mathcal{T}_{m}$ and the vehicle $V_{n}$ with trajectory $\mathcal{T}_{n}$. The collision point $\mathcal{X}_{m, n}$ is defined if $\mathcal{T}_{m}$ crosses $\mathcal{T}_{n}$ and undefined if the trajectories do not cross. The position of $\mathcal{X}_{m, n}$ with respect to the IRF is given by the vector $\vec{r}_{\mathcal{X}_{m, n}}=\underline{r}_{\mathcal{X}_{m, n}}^{0^{T}} \vec{e}^{0}$ where

$$
\underline{r}_{\mathcal{X}_{m, n}^{0}}^{0^{T}}=\left[\begin{array}{ll}
X_{m, n}^{0} & Y_{m, n}^{0}
\end{array}\right] .
$$

The position of $\mathcal{X}_{m, n}$ with respect to the entry points $I^{\eta_{p}} \in$ $\mathcal{L}_{\eta_{p}} \forall p=\{m, n\}$ is given by $\vec{r}_{\mathcal{X}_{m, n} / I^{\eta p}}=\vec{r}_{\mathcal{X}_{m, n}}-\vec{r}_{I^{\eta p}}$ which can be rewritten, considering (1) and (3), as

$$
\vec{r}_{\mathcal{X}_{m, n} / I^{\eta_{p}}}=\left[\begin{array}{ll}
X_{m, n}^{\eta_{p}} & Y_{m, n}^{\eta_{p}}
\end{array}\right] \underline{e}^{\eta_{p}}
$$

with

$$
\left[\begin{array}{ll}
X_{m, n}^{\eta_{p}} & Y_{m, n}^{\eta_{p}}
\end{array}\right]=\left(\underline{r}_{\mathcal{X}_{m, n}}^{0^{T}}-\underline{r}_{I}^{0^{T} \eta_{p}}\right) \underline{A}^{0 \eta_{p}}\left(\Psi_{\eta_{p}}\right) .
$$

As described in Section II-A, vehicles in the intersection are defined as $V_{i}, \forall i \in\left[M_{\text {min }}, M_{\text {max }}\right]$, where $V_{m}$, with $m=$ $M_{\text {max }}$, is the last vehicle to enter the intersection. As $V_{m}$ enters the intersection it is assigned to a target vehicle $V_{n}$, with $n \in$ $\left[M_{\text {min }}, M_{\text {max }}\right)$, as a target vehicle. The value of $n$ (i.e., how to determine the target vehicle index) is determined as follows. First consider the index set, of vehicles exhibiting a crossing trajectory with the vehicle $V_{m}$, given by

$$
\mathcal{N}=\left\{q \mid \forall q \in\left[M_{\min }, M_{\max }\right):\left\langle\mathcal{X}_{m, q}\right\rangle=1\right\}
$$

where

$$
\left\langle\mathcal{X}_{m, q}\right\rangle= \begin{cases}1, & \text { if } \mathcal{X}_{m, q} \text { is defined } \\ 0, & \text { otherwise }\end{cases}
$$

Note that $\mathcal{N}=\varnothing$ if none of the trajectories of the vehicles in the intersection cross with the trajectory of vehicle $V_{m}$. The value of $n$ is then given by

$$
n= \begin{cases}\operatorname{argmin}_{q \in \mathcal{N}} \mathcal{S}(q), & \text { if } \mathcal{N} \neq \varnothing \\ 0, & \text { if } \mathcal{N}=\varnothing\end{cases}
$$

where

$$
\mathcal{S}(q)=s\left(X_{m, q}^{\eta_{q}}, Y_{m, q}^{\eta_{q}}, \eta_{q}, \omega_{q}\right)
$$

is the distance to collision calculated using the definition of the path coordinate in (19), which is represented by the function $s\left(x_{\eta}, y_{\eta}, \eta, \omega\right)$, and the coordinates of the collision point with respect to $F^{\eta_{q}} \in \mathcal{L}_{\eta_{q}}$. Note that $n=0$ represents the case in which the trajectory $\mathcal{T}_{m}$ does not cross any trajectory of the vehicles inside the intersection.

Therefore, the distance to collision for vehicle $V_{m}$ is given by

$$
S_{m}=s\left(X_{m, n}^{\eta_{m}}, Y_{m, n}^{\eta_{m}}, \eta_{m}, \omega_{m}\right),
$$

and, in the same fashion, the distance to collision for vehicle $V_{n}$ is given by

$$
S_{n}=s\left(X_{m, n}^{\eta_{n}}, Y_{m, n}^{\eta_{n}}, \eta_{n}, \omega_{n}\right) .
$$

## B. Control Reconfiguration With Mixing

As described in the previous sections, each vehicle has three control modes, namely CC, CACC and VCACC. In order to determine which control mode will be activated we define several variables. Consider that each vehicle is equipped with a radar with a certain range. This radar can be represented as a circular sector in front of the vehicle with certain radius and central angle. Let $\alpha$ represent whether a target vehicle is detected by the radar or, in other words, whether a vehicle is inside the circular sector. Thus,

$$
\alpha= \begin{cases}1, & \text { Target vehicle detected } \\ 0, & \text { Otherwise }\end{cases}
$$

Let $\gamma$ be the variable that indicates that the vehicle $V_{m}$, with the point $\mathcal{P}_{m}$ in the center of its rear bumper, is inside the CZ. Such that

$$
\gamma= \begin{cases}1, & \left\|\vec{r}_{\mathcal{P}_{m}}\right\| \leq\left\|\vec{r}_{I} \eta_{m}\right\| \\ 0, & \text { otherwise }\end{cases}
$$

where $\vec{r}_{I^{\eta_{m}}}$ is the position vector of the entry point $I^{\eta_{m}} \in \mathcal{L}_{\eta_{m}}$.
Now, we can define the control mode as

$$
\rho= \begin{cases}1, & \alpha=0 \wedge \neg \mathcal{G} \\ 2, & \alpha=1 \wedge \neg \mathcal{G} \\ 3, & \mathcal{G}\end{cases}
$$

where $\mathcal{G} \equiv(\gamma=1 \wedge n \neq 0 \wedge s \leq S)$ represents the case in which a vehicle is inside the intersection, has a defined target vehicle and it has not crossed the intersection point
(represented by $s \leq S$, where $s$ and $S$ are the path coordinate and the distance to collision of the host vehicle, respectively); note that $\neg \mathcal{G}$ represents the negation of $\mathcal{G}$. The control modes are defined as follows: $\rho=1$ represents CC mode, $\rho=2$ represents CACC mode, and $\rho=3$ represents VCACC mode. Note that $\rho$ is piecewise continuous. To avoid the undesired effect of an instantaneous change in the reference acceleration generated by the controller when $\rho$ is switched, a set of mixing signals is used (as described in [26]).

Consider the signal

$$
o(t)=\min \left\{\frac{t-t_{t}}{t_{m}}, 1\right\}, \quad t \geq t_{t},
$$

where $t_{m}$ is the so-called mixing time, which will be considered constant for this work, and $t_{t}$ is the time in which a control switch was commanded such that $\rho\left(t_{t}\right) \neq \rho\left(t_{t}-\epsilon\right)$ for all $0<\epsilon \ll 1$.

Consider two mixing signals, a descending one $\beta^{d}$ that descends from 1 to 0, and an ascending one $\beta^{a}$ from 0 to 1, such that

$$
\beta^{d}(o)=\frac{\xi(o)}{\xi(o)+\xi(o-1)}, \quad \text { and } \beta^{a}(o)=\frac{\xi(o-1)}{\xi(o)+\xi(o-1)},
$$

where

$$
\xi(x)= \begin{cases}\exp \left(-\frac{1}{1-x^{2}}\right), & |x|<1 \\ 0, & |x| \geq 1\end{cases}
$$

is the so-called bump function.
Therefore, the mixing signals vector $\underline{\beta}$ is defined as

$$
\underline{\beta}=\left\{\left.\left[\begin{array}{lll}
\beta_{1} & \beta_{2} & \beta_{3}
\end{array}\right] \right\rvert\, \beta_{\rho_{t}}=\beta^{a}, \beta_{\rho_{\epsilon}}=\beta^{d}, \beta_{i}=0 \forall i \in \mathcal{E}\right\},
$$

where $\rho_{t}=\rho\left(t_{t}\right), \rho_{\epsilon}=\rho\left(t_{t}-\epsilon\right)$, and $\mathcal{E}=\{1,2,3\}-\left\{\rho_{t}, \rho_{\epsilon}\right\}$, such that the longitudinal reference acceleration is given by

$$
u_{x}=\underline{\beta} u_{x}
$$

where $\underline{u_{x}}=\left[u_{x, 1} \quad u_{x, 2} \quad u_{x, 3}\right]^{T}$, which corresponds to (47).

## V. Simulation Results

This section presents the results of two simulation studies. Section V-A presents the results for a scenario in which only two vehicles cross the intersection. This scenario allows the assessment of the functionality of the lateral and longitudinal virtual platooning controllers. The results of the second simulation study, which are presented in Section V-B, focus on the comparison between an intersection automated with the CIC methodology and an intersection controlled by traffic lights to illustrate the benefits of CIC.

The values for the intersection variables are: $K=4$, $r \in\{40 \mathrm{~m}, 150 \mathrm{~m}\}, w_{k}=6 \mathrm{~m} \forall k \in \mathcal{K}, \psi_{k}=\pi(k-1) / 2 \forall k \in \mathcal{K}$. The values for the longitudinal model and controller are: $\tau=0.1 \mathrm{~s}^{-1}, r=\tilde{r}=3 \mathrm{~m}, h=\tilde{h}=0.3 \mathrm{~s}, k_{p}=0.2 \mathrm{~s}^{-2}$, $k_{d}=0.7 \mathrm{~s}^{-1}, a_{\text {ref }}=0$, and $v_{\text {ref }} \in\{3 \mathrm{~m} / \mathrm{s}, 8 \mathrm{~m} / \mathrm{s}\}$. Finally, the values for the control reconfiguration variables are: $t_{m}=1 \mathrm{~s}$.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-10.jpg?height=397&width=793&top_left_y=198&top_left_x=1121)
Fig. 10. Virtual inter-vehicle distance and inter-vehicle distance.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-10.jpg?height=395&width=754&top_left_y=675&top_left_x=1139)
Fig. 11. Velocity of the target and host vehicles.

## A. CIC for Two Vehicles

This section focuses on the behavior of the longitudinal and lateral controllers for an scenario with only two vehicles that enter the intersection, of radius $r=40 \mathrm{~m}$, at the same time with a reference velocity $v_{\text {ref }}=3 \mathrm{~m} / \mathrm{s}$. Consider a pair of vehicles such that the target vehicle $\mathcal{V}_{1}$ follows the trajectory $\mathcal{T}_{1} \equiv \mathcal{C}_{1,3}$ and the host vehicle $\mathcal{V}_{2}$ follows the trajectory $\mathcal{T}_{2} \equiv \mathcal{C}_{2,3}$ such that the point $\mathcal{X}_{2,1}$ is defined (which means that $\mathcal{T}_{1}$ crosses with $\mathcal{T}_{2}$ ). As a consequence, the distance to collision of the target vehicle is $S_{1}=44.8$ and of the host vehicle is $S_{2}=40.5$. Note that this trajectories are depicted in Figure 1.

The values for the lateral model and controller are: $L=2.7 \mathrm{~m}, \sigma=50.25, a_{y}=3 \mathrm{~m} / \mathrm{s}^{2}, R=3 \mathrm{~m}$, $k_{0}=48.63, k_{2}=73.96, k_{3}=42.07$, and $k_{4}=10.61$.

The control mode of $\mathcal{V}_{1}$ is CC for the whole simulation; on the other hand, the control mode of $\mathcal{V}_{2}$ changes from VCACC to CACC. Figure 10 shows both the virtual inter-vehicle distance $\tilde{\delta}$ and the inter-vehicle distance $\delta$ as measured by $\mathcal{V}_{2}$, the vertical dashed line represents the moment in which the change in control mode occurs. Note that $\tilde{\delta}=\delta$ when the control mode switch is commanded. Clearly the VCACC and CACC controllers ensure that the (virtual) intervehicle distance is regulated to the desired distance. We can observe the effects of the aforementioned control mode switch in the velocity (Figure 11) and acceleration (Figure 12) of $\mathcal{V}_{2}$. Figure 13 shows the reaction of the lateral controller of $\mathcal{V}_{2}$; note that the change in curvature $\kappa$ acts as a step input to the lateral controller. Finally, Figure 14 evidences the avoidance of the collision region $\mathcal{W}_{2,1}$. In other words, Figure 14 shows that the two vehicles indeed safely cross the intersection in a cooperative fashion as can be seen in Video 1. ${ }^{1}$

[^1]![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-11.jpg?height=395&width=786&top_left_y=200&top_left_x=213)
Fig. 12. Acceleration of the target and host vehicles.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-11.jpg?height=432&width=741&top_left_y=690&top_left_x=234)
Fig. 13. Path following coordinates, where the units are $d[\mathrm{~m}], \theta_{e}[\mathrm{rad}]$, and $\kappa\left[\mathrm{m}^{-1}\right]$.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-11.jpg?height=694&width=681&top_left_y=1248&top_left_x=264)
Fig. 14. Avoidance of the collision region.

## B. Comparison of CIC to a Traffic Lights Scenario

This section presents a comparison between the CIC methodology and an intersection controlled with Traffic Lights (TL); for a 4-way $(K=4)$ intersection with radius $r=150 \mathrm{~m}$. For this scenario, we define a constant in-flow of vehicles (in vehicles per second, or [veh/s]) per lane $f_{k} \forall k \in \mathcal{K}$, and consider only straight trajectories. We compare the capacity of the intersection (which measures the number of vehicles that cross the intersection as a function of time), the average delay of vehicles (which is the time spent inside the intersection) and the average velocity of vehicles.

In the case of the traffic lights intersection we use the Intelligent Driver Model, defined in [27], to simulate the

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-11.jpg?height=393&width=797&top_left_y=200&top_left_x=1119)
Fig. 15. Comparison of the capacity of the intersection for a constant flow.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-11.jpg?height=395&width=786&top_left_y=655&top_left_x=1124)
Fig. 16. Comparison of the average delay in the intersection for a constant flow.

behavior of a human driver. Such model is defined as

$$
\dot{v}=\hat{a}\left(1-\left(\frac{v}{v_{r e f}}\right)^{D}-\left(\frac{\delta^{*}(v, \dot{\delta})}{\delta}\right)^{2}\right)
$$

with

$$
\delta^{*}(v, \dot{\delta})=s_{0}+s_{1} \sqrt{\frac{v}{v_{\text {ref }}}}+v T+\frac{v \dot{\delta}}{2 \sqrt{\hat{a} \hat{b}}}
$$

where $v_{\text {ref }}=8 \mathrm{~m} / \mathrm{s}$ is the desired velocity, $T=1.6 \mathrm{~s}$ is the time headway, $\hat{a}=3 \mathrm{~m} / \mathrm{s}^{2}$ is the maximum acceleration, $\hat{b}=2 \mathrm{~m} / \mathrm{s}^{2}$ is the comfortable deceleration, $D=4$ is the acceleration exponent, $s_{0}=2 \mathrm{~m}$ is the linear jam distance, and $s_{1}=3 \mathrm{~m}$ is the non-linear jam distance. The traffic light schedule is as follows: ten seconds of green light for lanes $\mathcal{L}_{1}$ and $\mathcal{L}_{3}$ and of red light for lanes $\mathcal{L}_{2}$ and $\mathcal{L}_{4}$, one second of red light for all lanes, ten seconds of green light for lanes $\mathcal{L}_{2}$ and $\mathcal{L}_{4}$ and of red light for lanes $\mathcal{L}_{1}$ and $\mathcal{L}_{3}$, one second of red light for all lanes. This protocol is repeated periodically. Note that this traffic light schedule is designed for the simulation study and it intends to represent a realistic fixed time schedule.

1) Constant In-Flow: Consider an input flow $f_{k}=$ $1 / 10$ veh $/ \mathrm{s} \forall k \in \mathcal{K}$. Figure 15 shows the comparison between the capacity of the intersection for the CIC and the TL approaches. The slope of the red dashed line corresponds to the total in-flow $f=\sum_{k=1}^{4} f_{k}=4 / 10 \mathrm{veh} / \mathrm{s}$. Both approaches are able to service all vehicles since the out-flow for both approaches is equal to the in-flow (note that the three lines have the same slope). The main differences are in average delay, shown in Figure 16, and in average velocity, shown in Figure 17. The CIC approach maintains a higher average velocity and a lower average delay since the vehicles do not have to come to a full stop (as it is the case for the TL); instead, using CIC the vehicles regulate their velocity cooperatively

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-12.jpg?height=410&width=773&top_left_y=196&top_left_x=219)
Fig. 17. Comparison of the average velocity in the intersection for a constant flow.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-12.jpg?height=397&width=799&top_left_y=730&top_left_x=204)
Fig. 18. Comparison of the capacity of the intersection for a sudden change in flow.

to realize the desired virtual gap between vehicles and then continue to drive at their reference velocities.

Note that for CIC the average delay is smaller and the average velocity higher but the capacity is the same for both approaches. The main difference between both is that at every instant in time the TL intersection holds more vehicles inside (note that the curve for TL in Figure 15 is slightly lower than the one for CIC), since the queues at the traffic lights are never longer than the radius of the intersection then there is never input saturation, and the intersection out-flow equals the in-flow. Video $2^{2}$ shows the aforementioned results.
2) Sudden Change of the In-Flow: In this scenario, we consider an input flow $f_{k}=1 / 10$ veh $/ \mathrm{s} \forall k \in \mathcal{K}$ for the first ten minutes of simulation. After ten minutes, the flows switch to $f_{1}=1 / 4 \mathrm{veh} / \mathrm{s}, f_{2}=1 / 5 \mathrm{veh} / \mathrm{s}, f_{3}=1 / 6 \mathrm{veh} / \mathrm{s}$, and $f_{4}=1 / 7 \mathrm{veh} / \mathrm{s}$. Figure 18 shows the comparison between the capacity of the intersection for the CIC and the TL approaches. We observe the same behavior, as in the previous comparison, for the first ten minutes. When the in-flow changes we can see how the CIC approach reacts to the change and keeps serving all vehicles that enter the intersection. In contrast, we can see that the TL approach becomes saturated which generates queues longer than the intersection radius. This effect is represented by the lower slope of the out-flow compared to the slope of the in-flow. The effects of the saturation are also present in the average delay, Figure 19, and in the average velocity, Figure 20. On the other hand, the CIC approach reacts to the in-flow change and maintains its performance. Video $3^{3}$ shows the aforementioned results.

[^2]![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-12.jpg?height=406&width=804&top_left_y=198&top_left_x=1117)
Fig. 19. Comparison of the average delay in the intersection for a sudden change in flow.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-12.jpg?height=408&width=771&top_left_y=709&top_left_x=1132)
Fig. 20. Comparison of the average velocity in the intersection for a sudden change in flow.

These comparisons help to demonstrate that the CIC methodology is robust to the changes in traffic flow maintaining an almost constant average delay and average velocity through the intersection without using knowledge on the in-flow. The TL approach used here only considers a static scheduling; an adaptive TL schedule would require knowledge of the in-flow (or at least an estimate), or sensors on the road to react to the in-flow conditions. Note that the comparison results are based only on straight trajectories, including all possible trajectories would increase the average delay, in the TL case, since there are more conflicting trajectories. In comparison, the CIC approach can handle the situation in which every vehicle has a distinct trajectory without the need to modify the proposed algorithms as shown in Video 4. ${ }^{4}$

## VI. Conclusions

This work presents the Cooperative Intersection Control (CIC) methodology which is a decentralized solution to cooperatively automate a road intersection. The cooperative autonomous vehicles controlled by CIC follow their individual trajectories through the intersection while avoiding collisions. The safe and efficient passage of vehicles through the intersection is achieved using the concept of Virtual Platooning which is a two-dimensional generalization of conventional longitudinal platooning. Such virtual platooning allows vehicles to cross the intersection at a small (virtual) inter-vehicle distance without standing-still (as happens at traffic lights). This benefits not only the throughput capacity of the intersection, but is also beneficial for fuel consumption, as a smoother vehicle flow implies less acceleration/deceleration (which is related to fuel consumption).

[^3]The simulation study shows the execution and supervision level of the CIC which together accomplish a complex collective behavior based on relatively simple local control techniques. The methodology reacts to the variations of traffic flow without a need of optimization techniques or additional infrastructure. It is worth noting that there is a limit to the First Come First Serve approach, used in this work. There are conditions on which the CIC also experiences saturation of vehicles. Moreover, the presented intersection geometry reduces all directional intentions to just one lane (meaning that vehicles drive on the same lane regardless of intending to go left, right, or straight). A possible extension involves the design a multi-lane intersection layout (with multiple sub-lanes on every lane entering the intersection) which has specific lanes for each directional intention (using the same presented definitions) to study the effects on throughput. Note that the vehicles must be arranged on the specific lane that represents their directional intention. The lane changing process needed to achieve this arrangement is a different problem to be solved.

The CIC methodology is designed under the assumption that all vehicles have both wireless communication capabilities and an accurate on-board GPS. It is not straight-forward to consider mixed traffic scenarios, with autonomous and non-autonomous vehicles. In fact, to deal with such scenarios a different/adapted intersection management strategy must be devised.

The optimization of the scheduling protocol is part of the future work, together with exploring the chain form lateral controller applied to a single track model, which is a lateral vehicle dynamics model that takes into consideration the side slip effect on the tyres.

## References

[1] European Commission, "Traffic safety basic facts on seasonality," Eur. Commission, Directorate General Transp., Brussels, Belgium, Jun. 2016.
[2] S. Huang, A. W. Sadek, and Y. Zhao, "Assessing the mobility and environmental benefits of reservation-based intelligent intersections using an integrated simulator," IEEE Trans. Intell. Transp. Syst., vol. 13, no. 3, pp. 1201-1214, Sep. 2012.
[3] C. Wuthishuwong and A. Traechtler, "Coordination of multiple autonomous intersections by using local neighborhood information," in Proc. Int. Conf. Connected Vehicles Expo (ICCVE), Dec. 2013, pp. 48-53.
[4] A. Uno, T. Sakaguchi, and S. Tsugawa, "A merging control algorithm based on inter-vehicle communication," in Proc. IEEE/IEEJ/JSAI Int. Conf. Intell. Transp. Syst., Oct. 1999, pp. 783-787.
[5] X.-Y. Lu and K. J. Hedrick, "Longitudinal control algorithm for automated vehicle merging," in Proc. 39th IEEE Conf. Decision Control, Dec. 2000, pp. 450-455.
[6] L. Chen and C. Englund, "Cooperative intersection management: A survey," IEEE Trans. Intell. Transp. Syst., vol. 17, no. 2, pp. 570-586, Feb. 2016.
[7] K. Dresner and P. Stone, "Multiagent traffic management: A reservationbased intersection control mechanism," in Proc. 3rd Int. Joint Conf. Auto. Agents Multiagent Syst. (AAMAS), 2004, pp. 530-537.
[8] S. R. Azimi, G. Bhatia, R. Rajkumar, and P. Mudalige, "Reliable intersection protocols using vehicular networks," in Proc. ACM/IEEE Int. Conf. Cyber-Phys. Syst. (ICCPS), Apr. 2013, pp. 1-10.
[9] G. K. Schmidt and B. Posch, "A two-layer control scheme for merging of automated vehicles," in Proc. 22nd IEEE Conf. Decision Control, Dec. 1983, pp. 495-500.
[10] B. Ran, S. Leight, and B. Chang, "A microscopic simulation model for merging control on a dedicated-lane automated highway system," Transp. Res. C, Emerg. Technol., vol. 7, no. 6, pp. 369-388, 1999.
[11] K. Dresner and P. Stone, "A multiagent approach to autonomous intersection management," J. Artif. Intell. Res., vol. 31, pp. 591-656, Mar. 2008.
[12] R. Tachet et al., "Revisiting street intersections using slot-based systems," PLoS ONE, vol. 11, no. 3, p. e0149607, 2016.
[13] R. Naumann, R. Rasche, J. Tacken, and C. Tahedi, "Validation and simulation of a decentralized intersection collision avoidance algorithm," in Proc. IEEE Conf. Intell. Transp. Syst., Nov. 1997, pp. 818-823.
[14] M. VanMiddlesworth, K. Dresner, and P. Stone, "Replacing the stop sign: Unmanaged intersection control for autonomous vehicles," in Proc. AAMAS Workshop Agents Traffic Transp., 2008, pp. 94-101.
[15] J. Lee and B. Park, "Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment," IEEE Trans. Intell. Transp. Syst., vol. 13, no. 1, pp. 81-90, Mar. 2012.
[16] M. Tlig, O. Buffet, and O. Simonin, "Decentralized traffic management: A synchronization-based intersection control-Extended version," in Proc. Int. Conf. Adv. Logistics Transp. (ICALT), 2014, pp. 109-114.
[17] R. Hult, M. Zanon, S. Gros, and P. Falcone, "Primal decomposition of the optimal coordination of vehicles at traffic intersections," in Proc. IEEE 55th Conf. Decision Control (CDC), vol. 55. Dec. 2016, pp. 2567-2573.
[18] L. Li and F.-Y. Wang, "Cooperative driving at blind crossings using intervehicle communication," IEEE Trans. Veh. Technol., vol. 55, no. 6, pp. 1712-1724, Nov. 2006.
[19] C. Englund et al., "The grand cooperative driving challenge 2016: Boosting the introduction of cooperative automated vehicles," IEEE Wireless Commun., vol. 23, no. 4, pp. 146-152, Aug. 2016.
[20] A. I. M. Medina, N. van de Wouw, and H. Nijmeijer, "Automation of a T-intersection using virtual platoons of cooperative autonomous vehicles," in Proc. IEEE 18th Int. Conf. Intell. Transp. Syst. (ITSC), Sep. 2015, pp. 1696-1701.
[21] J. Gregoire, S. Bonnabel, and A. De La Fortelle, "Priority-based coordination of robots," CoRR, pp. 20, 2014. [Online]. Available: https://hal.archives-ouvertes.fr/hal-00828976v3
[22] B. Siciliano and O. Khatib, Eds., "Motion control of wheeled mobile robots," in Handbook of Robotics. Berlin, Germany: Springer-Verlag, 2008.
[23] C. Samson, "Control of chained systems application to path following and time-varying point-stabilization of mobile robots," IEEE Trans. Autom. Control, vol. 40, no. 1, pp. 64-77, Jan. 1995.
[24] J. Ploeg, B. T. M. Scheepers, E. van Nunen, N. van de Wouw, and H. Nijmeijer, "Design and experimental evaluation of cooperative adaptive cruise control," in Proc. 14th Int. IEEE Conf. Intell. Transp. Syst. (ITSC), Oct. 2011, pp. 260-265.
[25] J. Ploeg, N. van de Wouw, and H. Nijmeijer, "Lp string stability of cascaded systems: Application to vehicle platooning," IEEE Trans. Control Syst. Technol., vol. 22, no. 2, pp. 786-793, Mar. 2014.
[26] A. I. Morales Medina, "Control reconfiguration with mixing applied to a longitudinally-automated vehicle," Dept. Mech. Eng., Eindhoven Univ. Technol., Eindhoven, The Netherlands, Tech. Rep. DC 2013.059, 2013.
[27] M. Treiber, A. Hennecke, and D. Helbing, "Congested traffic states in empirical observations and microscopic simulations," Phys. Rev. E, Stat. Phys. Plasmas Fluids Relat. Interdiscip. Top., vol. 62, no. 2, pp. 1805-1824, 2000.

![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-13.jpg?height=316&width=256&top_left_y=2237&top_left_x=1081)

Alejandro Ivan Morales Medina was born in 1986. He received the B.Sc. degree in mechatronics from UPIITA-IPN, Mexico City, Mexico, in 2009, and the M.Sc. degree in automotive technology with a dynamics and control specialization from the Eindhoven University of Technology, Eindhoven, The Netherlands, in 2013, where he is currently pursuing the Ph.D. degree. His current research is on the cooperative motion of vehicles through road intersections, including the control strategies to control the longitudinal and lateral motion of the vehicles, and the optimization of the traffic flow.
![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-14.jpg?height=318&width=256&top_left_y=217&top_left_x=168)

Nathan van de Wouw was born in 1970. He received the M.Sc. degree (Hons.) and the Ph.D. degree in mechanical engineering from the Eindhoven University of Technology, Eindhoven, The Netherlands, in 1994 and 1999, respectively. In 2000, he was with Philips Applied Technologies, Eindhoven, and, in 2001, he was with the Netherlands Organisation for Applied Scientific Research (TNO), Delft, The Netherlands. He has held a visiting professor position with the University of California at Santa Barbara, USA, in 2006 and 2007, The University of Melbourne, Australia, in 2009 and 2010, and the University of Minnesota, USA, in 2012 and 2013. He currently holds a full professor position with the Mechanical Engineering Department, Eindhoven University of Technology. He also holds an adjunct full professor position with the University of Minnesota, USA, and a (part-time) full professor position with the Delft University of Technology, The Netherlands. He has published a large number of journal and conference papers and the books Uniform Output Regulation of Nonlinear Systems: A convergent Dynamics Approach with A. V. Pavlov and H. Nijmeijer (Birkhauser, 2005) and Stability and Convergence of Mechanical Systems with Unilateral Constraints with R. I. Leine (Springer-Verlag, 2008). His current research interests are the modeling analysis and control of nonlinear/hybrid systems, with applications to vehicular platooning, high-tech systems, resource exploration, smart energy systems, and networked control systems. In 2015, he received the IEEE Control Systems Technology Award For the development and application of variable-gain control techniques for high-performance motion systems. He currently is an Associate Editor of the journals Automatica and the IEEE Transactions on Control Systems Technology.
![](https://cdn.mathpix.com/cropped/e3802edf-1bfb-43c2-aefa-be8400c90bf3-14.jpg?height=316&width=251&top_left_y=219&top_left_x=1083)

Henk Nijmeijer (F'00) was born in 1955. Since 2015, he has been the Scientific Director of the Dutch Institute of Systems and Control. He is currently a Full Professor with the Eindhoven University of Technology, and chairs the Dynamics and Control Group. He has published a large number of journal and conference papers, and several books. Since 2011, he has been an IFAC Council Member. He is appointed as the Honorary Knight of the Golden Feedback Loop in 2011. He received the IEE Heaviside Premium in 1990. He was a recipient of the 2015 IEEE Control Systems Technology Award. He is a Program Leader of the Dutch Research Program Integrated Cooperative Automated Vehicles. He is or was at the editorial board of numerous journals. He is an Editor of Communications in Nonlinear Science and Numerical Simulations.


[^0]:    Manuscript received February 8, 2017; revised June 20, 2017; accepted July 30, 2017. This work was supported in part by the European Union Seventh Framework Programme [FP7-ICT-2013-10] under Grant 612035 and in part by Interoperable GCDC (Grand Cooperative Driving Challenge) AutoMation Experience (i-GAME). The Associate Editor for this paper was B. Fidan. (Corresponding author: Alejandro Ivan Morales Medina.)
    A. I. Morales Medina and H. Nijmeijer are with the Department Mechanical Engineering, Eindhoven University of Technology, 5612 AZ Eindhoven, The Netherlands (e-mail: a.i.morales.medina@tue.nl; h.nijmeijer@tue.nl).
    N. van de Wouw is with the Department of Mechanical Engineering, Eindhoven University of Technology, 5612 AZ Eindhoven, The Netherlands, also with the Civil, Environmental and Geo-Engineering Department, University of Minnesota, Minneapolis, MN 55455 USA, and also with the Delft Center for Systems and Control, Delft University of Technology, 2628 CD Delft, The Netherlands (e-mail: n.v.d.wouw@tue.nl).
    Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
    Digital Object Identifier 10.1109/TITS.2017.2735628

[^1]:    ${ }^{1}$ https://youtu.be/uUp3WgJ9UpA

[^2]:    ${ }^{2}$ https://youtu.be/K9S5fHs10cE
    ${ }^{3}$ https://youtu.be/oPzM8sUsN14

[^3]:    ${ }^{4}$ https://youtu.be/0hM_lwrnmyE

