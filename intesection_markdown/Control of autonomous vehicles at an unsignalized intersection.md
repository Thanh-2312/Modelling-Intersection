# Control of autonomous vehicles at an unsignalized intersection 

F. Belkhouche


#### Abstract

Safety and optimal traffic flow are important priorities in intelligent transportation systems. This paper presents a collaborative method for collision avoidance between autonomous vehicles at an unsignalized intersection. The collision conditions are expressed in terms of the vehicles' speed ratios. The problem is then formulated and solved as an optimization problem with the safety constraints represented by the speed ratios. The cost function is defined in terms of the deviation from the current speeds. Both pairwise and three vehicle formulations are discussed. The proposed formulation allows to easily scale the solution to higher number of vehicles. The method is highly effective in resolving conflicts and achieving smooth flow. The results are formally proven and illustrated using simulation.


## I. Introduction

Improving safety and reducing road congestion are among the goals of intelligent transportation systems. Recent technology advances are helping to achieve effective solutions to improve safety and road capacity. While the idea of autonomous vehicles is not new, deployment in real world applications is recent. Autonomous parallel parking [1], [2], lane change [3], [4], and cruise control [3], [5], [6] have been for a long time among the most important topics discussed in the intelligent transportation community. Several practical solutions are currently available.

According to Maile et al., [7], more than one fifth of fatal accidents occur at intersections. The goal of this paper is to optimize the traffic flow at an unsignalized intersection while guaranteeing safety. A collaborative approach is proposed to address the problem. According to Kolodko and Vlacic [8], communication and collaboration are fundamental capabilities for the vehicles of the future. Smart intersections is a research topic of growing interest that includes the following aspects [9], [10]:

- Safety assessment and detection of potential collision at the intersection.
- Optimization of the traffic flow at the intersection.
- Communication and information sharing. This includes vehicle to infrastructure communication (V2I) and infrastructure to vehicle communication (I2V) as well as vehicle to vehicle communication (V2V).

A smart intersection has two characteristics: smart signalization and/or smart vehicles. A quick look at the recent publications shows that most published work on smart intersections deals with the development of intelligent signalization. Active safety procedures are becoming more common because of their effectiveness in reducing the number of accidents

[^0][11]. The development of collaborative vehicle collision avoidance systems is discussed by many authors including for example, Evdokimos et al. [12], Jian et al. [13], and Tan and Huang [14]. A cooperative vehicle intersection control system is developed in [15]. The algorithm uses a centralized controller; therefore it focuses on the cooperation between the vehicles and the infrastructure. Another algorithm that uses infrastructure communication is discussed in [16] where reliability is addressed to improve the collision avoidance system. The main drawback of centralized approaches is that the entire system suffers if the controller fails. Therefore, decentralized approaches offer better robustness in multi-agent systems. Another algorithm that combines both centralized and distributed solutions is addressed in [17]. Decentralized methods are also used in intersection crossing [18]. In [18], the authors used a centralized algorithm that uses state estimation to reduce the effect of uncertainty and delays. Scheduling methods that use a supervisor are also used [19], [20]. Collaborative behavior presents very important advantages, particularly in critical situations. This paper focuses on two aspects: the optimality of the solutions and the collaborative behavior to avoid collision between autonomous vehicles. The main contributions of this paper are summarized as follows:


- The collision conditions between the vehicles are expressed under a simple form consisting of speed ratios that can be easily transferred to the control space. Simplicity plays a crucial role when scaling the algorithm to more vehicles.
- The proposed algorithm is not restrictive and offers good flexibility by choosing the solutions based on their cost.
- The effect/benefit of collaboration is explored in terms of the cost to avoid collision. A comparison is carried out in terms of the action weights associated with the vehicles.


The problem statement as well as some definitions are introduced in the next section. Section III discusses pairwise collision detection as well as the optimal collaborative solutions. Section IV generalizes the results and discusses the three-vehicle formulation. Section V discusses scaling the solution to multiple agents. Finally, section VI shows the simulation results followed by a conclusion in section VII.

## II. Problem statement and background DEFINITIONS

We consider the problem of intelligent vehicles crossing an unsignalized traffic intersection as shown in figure 1. There is no traffic light or stop sign at the intersection. The
vehicles entering the intersection will collaborate to avoid conflict. The vehicles are denoted by $V_{i}$. The goal is to achieve optimal traffic flow at the intersection while at the same time guaranteeing safety by resolving the conflict in a timely manner. While communication between vehicles plays an important role, this paper focuses on the control aspects. Therefore, it is assumed that the vehicles can communicate and share their position, speed, and size in real time. The communication process is initiated when the vehicles are at a distance of $50 m$ from the intersection. The average speed of the vehicles is $10 m / s$. The maximum speed on the road is $v^{\max }=15 m / s$, and the maximum acceleration is $a^{m a x}=4 m / s^{2}$ for all vehicles. Let $v_{i}^{d e s}$ be the desired speed calculated by the control law for vehicle $V_{i}$, the tracking system response is characterized by a first order system as follows

$$
\dot{v}_{i}=-K_{i}\left(v_{i}-v_{i}^{d e s}\right)
$$

where $K_{i}$ is a positive constant related to the acceleration. It is characterized by the following condition on its maximum value

$$
K_{i}^{\max }<\frac{a^{\max }}{v_{i}-v_{i}^{\operatorname{des}}}
$$

The 98\% settling time is given by

$$
t_{s}=-\frac{1}{K} \ln \left(\left|\frac{-0.02 v_{i}^{d e s}}{v_{i}^{c}-v_{i}^{d e s}}\right|\right)
$$

where $v_{i}^{c}$ is the speed when the actions to resolve the conflict begin. The settling time plays an important role in the collision avoidance process. The cost to avoid a collision is defined in terms of the deviation between the current speed and the desired speed. We propose to use the following equation to calculate the cost associated with agent $V_{i}$ :

$$
\mathcal{C}_{i}=\left(v_{i}^{c}-v_{i}^{d e s}\right)^{2}
$$

Equation (4) provides an effective way to compare between the actions taken by the vehicles to avoid a collision. Since $v_{i}^{\text {des }}$ is the speed that resolves the conflict, $\mathcal{C}_{i}$ represents the cost to resolve a conflict associated with agent $V_{i}$. Before we discuss the collision conditions, the following geometric quantities are defined

- The distance between the reference points of $V_{1}$ and $V_{2}$ is denoted by $\rho_{12}$. The minimum acceptable distance between the closest points in $V_{1}$ and $V_{2}$ is denoted by $d_{12}^{m}$. In our formulation $d_{12}^{m}=1 m$ and is kept constant.
- The line of sight angle $\lambda_{12}$ is defined as shown in figure 2. The maximum and minimum line of sight angles are denoted by $\lambda_{12}^{b}$ and $\lambda_{12}^{a}$, respectively.

## III. Pairwise collision detection and avoidance

The virtual configuration space [21] is used to plan the path and avoid collision between the vehicles. We consider the case where two vehicles need to cooperate to traverse the intersection and optimize the traffic flow. Minkowski addition [22] is used to reduce one vehicle to a single point as shown in figure 2. It can be shown that the reference points of

![](https://cdn.mathpix.com/cropped/d3aad7ec-e2df-45f3-89fc-d9063011a3a2-2.jpg?height=584&width=898&top_left_y=172&top_left_x=1083)
Fig. 1. A representation of an unsignalized traffic intersection. There is no stop sign or traffic light

![](https://cdn.mathpix.com/cropped/d3aad7ec-e2df-45f3-89fc-d9063011a3a2-2.jpg?height=393&width=668&top_left_y=969&top_left_x=1203)
Fig. 2. Representation of the geometric variables after the Minkowski addition

vehicles $V_{1}$ and $V_{2}$ are in a collision course when [23]

$$
v_{1} \sin \left(\theta_{1}-\lambda_{12}\right)=v_{2} \sin \left(\theta_{2}-\lambda_{12}\right)
$$

This condition implies constant line of sight angles between the two vehicles [23]. In general, collision between the vehicles can be characterized by a single equation of the form

$$
\frac{v_{1}}{v_{2}}=m_{12}
$$

where $m_{12}$ is a function of $\theta_{1}, \theta_{2}$, and $\lambda_{12}$ as can be seen from equation (5), $m_{12}$ is called the speed ratio. We define the set of free speed ratios as the set of values of $m_{12}$ for which there is no collision between $V_{1}$ and $V_{2}$. The set of speed ratios forming the free space is denoted by $m_{12}^{f}$. Four values of the speed ratio are of particular interest. We first define $m_{12}^{a}, m_{12}^{b}$, which represent the speed ratios corresponding to $\lambda_{12}^{a}$ and $\lambda_{12}^{b}$, respectively. Any value of $m_{12}$ between $m_{12}^{a}$ and $m_{12}^{b}$ will result in collision. We also define speed ratios $m_{12}^{c}$ and $m_{12}^{d}$ which correspond to collision avoidance with a minimum distance equal to $d_{12}^{m}$. An illustration of the collision prediction process based on the speed ratio is shown in figure 3. The shaded area between $m_{12}^{a}$ and $m_{12}^{b}$ corresponds to collision between the

![](https://cdn.mathpix.com/cropped/d3aad7ec-e2df-45f3-89fc-d9063011a3a2-3.jpg?height=498&width=793&top_left_y=213&top_left_x=202)
Fig. 3. An illustration of the speed ratio and its relationship with the collision set and the safety margins (SM)

![](https://cdn.mathpix.com/cropped/d3aad7ec-e2df-45f3-89fc-d9063011a3a2-3.jpg?height=546&width=754&top_left_y=954&top_left_x=247)
Fig. 4. Time evolution of the speed ratios. Speed ratios $\left(m_{12}^{a}, m_{12}^{c}\right)$ and $\left(m_{12}^{b}, m_{12}^{d}\right)$ diverge with time even when both $v_{1}$ and $v_{2}$ are constant

vehicles. The current ratio $v_{1} / v_{2}$ is equal to one in this case and therefore is inside the shaded area. The areas between $m_{12}^{a}, m_{12}^{b}$ and $m_{12}^{c}, m_{12}^{d}$, respectively are called the safety margins (SM). For the particular example of figure 3, their numerical values are

$$
m_{12}^{c}=1.34 \quad \text { and } \quad m_{12}^{d}=0.75
$$

Avoiding collision by placing the speed ratio at $m_{12}^{c}$ yields a change of 0.34 while avoiding collision by moving the speed ratio to $m_{12}^{d}$ yields a change of 0.25 . Therefore, the cost is different even though the miss-distance is the same. The set of collision-free speed ratios is therefore given by

$$
m_{12}^{f}=\left\{m_{12} \mid m_{12} \geq m_{12}^{c} \text { or } m_{12} \leq m_{12}^{d}\right\}
$$

The goal is then to keep $m_{12} \in m_{12}^{f}$ for all values of $v_{1}$ and $v_{2}$.

Figure 4 shows the evolution of the speed ratios in the time interval $[0,4 s]$. Even though the vehicles speeds are constant, the speed ratios ( $m_{12}^{a}, m_{12}^{c}$ ) and ( $m_{12}^{b}, m_{12}^{d}$ ) diverge from each other and the colliding speed ratio set characterized by $\left|m_{12}^{a}-m_{12}^{b}\right|$ becomes larger with time.
A. Optimal solution

Optimization techniques can be used to resolve conflict and optimize the traffic flow and the control effort. It is possible to use several cost functions. In this paper, we define the following cost function

$$
\begin{array}{ll}
\operatorname{minimize} & J=w \mathcal{C}_{1}+(1-w) \mathcal{C}_{2} \\
\text { subject to } & m_{12} \in m_{12}^{f}
\end{array}
$$

where $w$ and $(1-w)$ are weights associated with the actions of the vehicles with $w \in[0,1]$. The cost function $J$ describes the distance from the current speed. Therefore, minimizing $J$ is equivalent to resolving the conflict with minimum deviation from the current speeds. The objective is to calculate the desired speeds $\left(v_{1}^{\text {des }}, v_{2}^{\text {des }}\right)$ that allow to resolve the conflict with the minimum acceptable distance between the vehicles. The cost function given by (4) captures two strategies to resolve a conflict:

- Unilateral action by $V_{1}$ or $V_{2}$ : When $w=0$ or $w=$ 1, the conflict is resolved by a single vehicle without any involvement from the other vehicle. Therefore, the speed of the non-contributing vehicle stays unchanged.
- Collaborative actions: Both weights are different from zero, in the particular case when $w=0.5$, the vehicles are equally responsible for resolving the conflict.

Proposition 3.1: The speeds of $V_{1}$ and $V_{2}$ corresponding to the upper speed ratio $m_{12}^{c}$ allowing to avoid collision while minimizing cost function (9) are given by

$$
\begin{array}{r}
v_{2}^{d e s}=\frac{w m_{12}^{c} v_{1}^{c}+(1-w) v_{2}^{c}}{(1-w)+w\left(m_{12}^{c}\right)^{2}} \\
v_{1}^{d e s}=m_{12}^{c} v_{2}^{d e s}
\end{array}
$$

Proof: A solution corresponding to the minimum clearance distance characterized by the upper speed ratio $m_{12}^{c}$ satisfies

$$
v_{1}=m_{12}^{c} v_{2}
$$

By substituting $v_{1}$ by its formula in (9), we obtain

$$
J^{c}=w\left(v_{1}^{c}-m_{12}^{c} v_{2}\right)^{2}+(1-w)\left(v_{2}^{c}-v_{2}\right)^{2}
$$

The optimal solution is obtained by setting $\partial J^{c} / \partial v_{2}=0$, which yields the solutions given by (10). $\square$

Proposition 3.2: The speeds of $V_{1}$ and $V_{2}$ corresponding to the lower speed ratio $m_{12}^{d}$ allowing to avoid collision while minimizing the cost function given by (9) are given by

$$
\begin{array}{r}
v_{2}^{d e s}=\frac{w m_{12}^{d} v_{1}^{c}+(1-w) v_{2}^{c}}{(1-w)+w\left(m_{12}^{d}\right)^{2}} \\
v_{1}^{d e s}=m_{12}^{d} v_{2}^{d e s}
\end{array}
$$

Proof: Similar to the previous case. The cost function to be minimized in this case is given by

$$
J^{d}=w\left(v_{1}^{c}-m_{12}^{d} v_{2}\right)^{2}+(1-w)\left(v_{2}^{c}-v_{2}\right)^{2}
$$ $\square$

The following example shows an illustration.

TABLE I
Comparison between different cases
|  | Vehicle | Desired speed | Cost |
| :--- | :--- | :--- | :--- |
| Case $1(w=0)$ | $V_{1}$ | 8.69 | 0.6 |
|  | $V_{2}$ | 11 | 0 |
| Case $2(w=0.5)$ | $V_{1}$ | 9.57 | 0.22 |
|  | $V_{2}$ | 12.12 | 0.14 |
| Case $3(w=0.6)$ | $V_{1}$ | 12.41 | 0.22 |
|  | $V_{2}$ | 9.8 | 0.16 |


B. Example

This example illustrates the collaboration process between two vehicles on a collision course. Three different approaches to avoid collision are considered and discussed below.

- Case 1: The speed ratio is moved to $m_{12}^{c}$ with $w=0$.
- Case 2: The speed ratio is moved to $m_{12}^{c}$ with $w=0.5$
- Case 3: The speed ratio is moved to $m_{12}^{d}$ with $w=0.6$

In case 1, $V_{2}$ does not participate in the conflict resolution process. In case 2, the weights associated with the agents are equal, which implies equal actions. Case 3 is similar to case 2 but with different speed ratio and weights. Table I shows a comparison between the cases in terms of the desired speeds and the costs to resolve the conflict. While the cost associated with $V_{2}$ is zero in case 1, the total cost is the highest. The lowest cost is obtained when the vehicles have the same weights. This example shows the importance of collaboration in conflict resolution.

## IV. Three-vehicle conflict resolution

Binary collision detection and avoidance is the most natural way to avoid collision at intersections. The methods described above for two vehicles can be easily generalized to multiple vehicles by expanding the cost function to include more terms. Another case of particular interest is the case of three-vehicle system. It is possible to formulate the threevehicle problem as two pairwise collaboration problems where two separate cost functions are defined as follows

$$
\begin{aligned}
& J_{12}=w \mathcal{C}_{1}+(1-w) \mathcal{C}_{2} \\
& J_{13}=w \mathcal{C}_{1}+(1-w) \mathcal{C}_{3}
\end{aligned}
$$

Under this formulation the coordination process includes pairs $\left(V_{1}, V_{2}\right)$ and $\left(V_{1}, V_{3}\right)$. Even thought $V_{2}$ and $V_{3}$ are not included in the same cost function, it is possible for them to coordinate through $V_{1}$. Two aspects arise when multiple vehicles are involved in collaboration.

- The first aspect is concerned with the optimal intersection crossing. Given the initial configuration at the time when the vehicles enter the intersection and assuming that at least two of them are on a collision course, what is the optimal order of passage that allows to resolve all conflicts?
- The second aspect is concerned with the vehicles speeds that allow to avoid collision for a given crossing order.

This is equivalent to finding optimal actions that minimize the cost function for each agent.

Let $m_{1}^{f}$ be the set of the collision-free speed ratios for $V_{1}$ defined as $m_{1}^{f}=m_{12}^{f} \bigcup m_{13}^{f}$. An expression of $m_{1}^{f}$ is

$$
\begin{aligned}
m_{1}^{f}=\left\{m_{12} \cup m_{13} \mid m_{12}\right. & \geq m_{12}^{c} \text { and } m_{13} \geq m_{13}^{c} \text { or } \\
m_{12} & \leq m_{12}^{d} \text { and } m_{13} \geq m_{13}^{c} \text { or } \\
m_{13} & \leq m_{13}^{d} \text { and } m_{12} \geq m_{12}^{c} \text { or } \\
m_{12} & \left.\leq m_{12}^{d} \text { and } m_{13} \leq m_{13}^{d}\right\}
\end{aligned}
$$

The expression of $m_{12}^{f}$ captures the following cases:

- $V_{1}$ enters the intersection first. The speed of $V_{1}$ satisfies $m_{12} \geq m_{12}^{c}$ and $m_{13} \geq m_{13}^{c}$.
- $V_{1}$ enters the intersection between $V_{2}$ and $V_{3}$ (or $V_{3}$ and $\left.V_{2}\right)$. The speed of $V_{1}$ to avoid collision is
$$
m_{13}^{c} v_{3} \leq v_{1} \leq m_{12}^{d} v_{2}
$$
or
$$
m_{12}^{c} v_{2} \leq v_{1} \leq m_{13}^{d} v_{3}
$$
When $m_{12}^{d} v_{2}=m_{13}^{c} v_{3}$ or $m_{12}^{c} v_{2}=m_{13}^{d} v_{3}$, there is one solution that allows for safe crossing.
- $V_{1}$ enters the intersection after $V_{2}$ and $V_{3}$. The speed of $V_{1}$ satisfies $m_{12} \leq m_{12}^{d}$ and $m_{13} \leq m_{13}^{d}$.

Inequalities (17) and (18) provide a platform for collaboration between $V_{2}$ and $V_{3}$ to create the safe crossing space for $V_{1}$. The options described above do not have the same cost. Assuming the current speeds of the vehicles are $v_{1}^{c}, v_{2}^{c}$ and $v_{3}^{c}$, we define the distance from the current speed ratios as follows

$$
\begin{array}{ll}
e_{1}=\left(m_{12}^{c}-v_{1}^{c} / v_{2}^{c}\right)^{2}, & e_{2}=\left(m_{12}^{d}-v_{1}^{c} / v_{2}^{c}\right)^{2} \\
e_{3}=\left(m_{13}^{c}-v_{1}^{c} / v_{3}^{c}\right)^{2}, & e_{4}=\left(m_{13}^{d}-v_{1}^{c} / v_{3}^{c}\right)^{2}
\end{array}
$$

These errors can be used to calculate the optimal crossing through the intersection. We define two speed ratios $n_{12}$ and $n_{13}$, where

- $n_{12}$ is the speed ratio that results in the minimum error between $e_{1}$ and $e_{2}$.
- $n_{13}$ is the speed ratio that results in the minimum error between $e_{3}$ and $e_{4}$.

We define the following cost function

$$
J=w_{1} \mathcal{C}_{1}+\alpha_{2} w_{2} \mathcal{C}_{2}+\alpha_{3} w_{3} \mathcal{C}_{3}
$$

where a weight $w_{i}$ is assigned to each vehicle with $w_{1}+$ $w_{2}+w_{3}=1$ and $\alpha_{2}, \alpha_{3}$ are chosen based on the presence or absence of conflict with $V_{2}$ or $V_{3}$, respectively. They are

$$
\begin{cases}\alpha_{j}=1, & \text { if } V_{j} \text { is on a collision course with } V_{1} \\ \alpha_{j}=0, & \text { if } V_{j} \text { is not on a collision course with } V_{1}\end{cases}
$$

The cost function given by (20) assumes that there is a collision risk with at least one vehicle, therefore, it is not possible to have both $\alpha_{2}$ and $\alpha_{3}$ equal to zeros.

Proposition 4.1: The solutions along speed ratios $n_{12}$ and

![](https://cdn.mathpix.com/cropped/d3aad7ec-e2df-45f3-89fc-d9063011a3a2-5.jpg?height=539&width=872&top_left_y=204&top_left_x=189)
Fig. 5. Cost associated with the vehicles to avoid collision. Left: threevehicle collaboration, and right pairwise formulation.

$n_{13}$ that minimize the cost function are given by

$$
v_{1}^{\text {des }}=\frac{n_{12} n_{13}\left[n_{12} n_{13} w_{1} v_{1}^{c}+\alpha_{2} n_{13} w_{2} v_{2}^{c}+\alpha_{3} n_{12} w_{3} v_{3}^{c}\right]}{n_{12}^{2} n_{13}^{2} w_{1}+\alpha_{2} n_{13}^{2} w_{2}+\alpha_{3} n_{12}^{2} w_{3}}
$$

and

$$
\begin{aligned}
& v_{2}^{\text {des }}= \begin{cases}\frac{v_{1}^{\text {des }}}{n_{12}} & \text { if } \alpha_{2}=1 \\
v_{2}^{c} & \text { if } \alpha_{2}=0\end{cases} \\
& v_{3}^{\text {des }}= \begin{cases}\frac{v_{1}^{\text {des }}}{n_{13}} & \text { if } \alpha_{3}=1 \\
v_{3}^{c} & \text { if } \alpha_{3}=0\end{cases}
\end{aligned}
$$

Assuming that $\alpha_{2}=1$ and $\alpha_{3}=0, V_{3}$ does not participate. It can be easily proven that equations (10) and (13) are recovered from system (21) with $n_{12}=m_{12}^{c}$ or $m_{12}^{d}$. This simply shows that the binary formulation is a particular case of the three-vehicle formulation.

Figure 5 shows the total cost and the cost associated with each vehicle as a function of the weights. All three vehicles participate in the collision avoidance process in figure 5-left with $w_{1}=w$ and $w_{2}=w_{3}=(1-w) / 2$. In figure 5-right, only $V_{1}$ and $V_{2}$ participate $\left(\alpha_{3}=0\right)$ with $w_{1}=w$ and $w_{2}=$ $1-w$. From figure 5-left, it is clear that when $w=0, V_{1}$ takes full responsibility to avoid collision. When $w=1$, priority is given to $V_{1}$ and the conflict is resolved by $V_{2}$ and $V_{3}$ only. The total cost which represents the cost of all collaborating vehicles has minimum point at $w=1 / 3$ which corresponds to equal contribution. In the pairwise formulation shown in figure 5-right, when $w=0$, the conflict is resolved by the actions of $V_{1}$ only. When $w=1$, the conflict is resolved by the actions of $V_{2}$ only. It is clear that the minimum cost is obtained when the two vehicles collaborate with $w=0.5$. This example shows the importance of collaboration and its effect on the total cost function. In both binary and threevehicle collaboration, the minimum value of the cost function is obtained when the vehicles' weights are equal.

![](https://cdn.mathpix.com/cropped/d3aad7ec-e2df-45f3-89fc-d9063011a3a2-5.jpg?height=522&width=763&top_left_y=206&top_left_x=1139)
Fig. 6. Speed ratios for optimal traffic control. The middle shaded area corresponds to collision. Left: Speed ratios corresponding to $\left(V_{1}, V_{2}\right)$, and Right: Speed ratios corresponding to $\left(V_{1}, V_{3}\right)$.

TABLE II
Speeds for safe intersection crossing for four different ACTIONS
|  | $v_{1}^{\text {des }}$ | $v_{2}^{\text {des }}$ | $v_{3}^{\text {des }}$ | $\frac{m_{12}^{c}}{m_{12}^{d}}$ | $\frac{m_{13}^{c}}{m_{13}^{d}}$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Action 1 | 8.94 | 6.98 | 13.06 | 1.28 | 0.68 |
| Action 2 | 10.85 | 8.47 | 9.41 | 1.28 | 1.15 |
| Action 3 | 8.21 | 10.52 | 11.99 | 0.78 | 0.68 |
| Action 4 | 9.44 | 12.10 | 8.19 | 0.78 | 1.15 |


## V. Conflict resolution with multiple vehicles AND ALGORITHM SCALABILITY

Several possibilities exist to scale the method to higher number of vehicles. A similar optimization approach to the cost function given by (20) can be used when multiple vehicles are present. This is achieved by including more vehicles in the expression of $J$. An advantage of using this strategy is that vehicles that are not on a collision course will be excluded by choosing the appropriate involvement weight $\left(\alpha_{i}\right)$. The cost function is therefore dynamic and includes only the vehicles that are involved, which corresponds to vehicles crossing the intersection at the same time.

## VI. Simulation

To illustrate the method we consider the case of three vehicles crossing the intersection. Initially all three vehicles have the same speed $(10 m / s)$. The speed ratio diagram is shown in figure 6, which shows that $V_{1}$ is on collision course with both $V_{2}$ and $V_{3}$. The desired speed ratios $m_{12}^{c}, m_{12}^{d}, m_{13}^{c}, m_{13}^{d}$ are 1.28, 0.78, 1.15, 0.68, respectively. Table III shows the cost associated with each action for each agent as well as the total cost. Based on the total cost, the optimal crossing is $V_{1} V_{3} V_{2}$. Simulation results near the intersection are shown in figure 7 for action 4 at different times.

## VII. Conclusion

This paper presents an optimal solution to the problem of conflict resolution at an unsignalized traffic intersection. The

![](https://cdn.mathpix.com/cropped/d3aad7ec-e2df-45f3-89fc-d9063011a3a2-6.jpg?height=339&width=1682&top_left_y=206&top_left_x=204)
Fig. 7. Illustration of action 4 at different times. The order of crossing is $V_{2} V_{1} V_{3}$

TABLE III
Cost to resolve the conflicts for different actions
|  | $\mathcal{C}_{1}$ | $\mathcal{C}_{2}$ | $\mathcal{C}_{2}$ | $\mathcal{C}_{1}+\mathcal{C}_{2}+\mathcal{C}_{3}$ |
| :--- | :--- | :--- | :--- | :--- |
| Action 1 | 1.1236 | 9.1204 | 9.3636 | 19.6076 |
| Action 2 | 0.7225 | 2.3409 | 0.3481 | 3.41156 |
| Action 3 | 3.2041 | 0.2704 | 3.9601 | 7.4346 |
| Action 4 | 0.3136 | 4.4100 | 3.2761 | 7.9997 |


problem is formulated as a collaboration problem where the first step is to determine the colliding speeds using a simple and fast algorithm. If a conflict is detected, the vehicles in conflict calculate their optimal actions based on a simple cost function. It is shown that the cost of resolving a conflict is minimized when the vehicles collaborate and have exactly the same responsibility for conflict resolution. The methods developed in this paper allow to calculate the optimal actions quickly and effectively. Simulation results demonstrate the effectiveness of the proposed approaches.

## References

[1] H. Vorobieva, S. Glaser, N. Minoiu-Enache, and S. Mammar, "Automatic parallel parking in tiny spots: Path planning and control," IEEE Transactions on Intelligent Transportation Systems, vol. 16, no. 1, pp. 396-410, 2015.
[2] T.-C. Lee, C.-Y. Tsai, and K.-T. Song, "Fast parking control of mobile robots: a motion planning approach with experimental validation," IEEE Transactions on Control Systems Technology, vol. 12, no. 5, pp. 661-676, 2004.
[3] J. Naranjo, C. Gonzalez, R. Garcia, and T. de Pedro, "Lane-change fuzzy control in autonomous vehicles for the overtaking maneuver," IEEE Transactions on Intelligent Transportation Systems, vol. 9, no. 3, pp. 438-450, 2008.
[4] C. Hatipoglu, U. Ozguner, and K. Redmill, "Automated lane change controller design," IEEE Transactions on Intelligent Transportation Systems, vol. 4, no. 1, pp. 13-22, 2003.
[5] L. Shengbo, K. Li, R. Rajamani, and J. Wang, "Model predictive multi-objective vehicular adaptive cruise control," IEEE Transactions on Control Systems Technology, vol. 19, no. 3, pp. 556-566, 2011.
[6] J. Naranjo, C. Gonzalez, J. Reviejo, and R. G. T. de Pedro, "Adaptive fuzzy control for inter-vehicle gap keeping," IEEE Transactions on Intelligent Transportation Systems, vol. 4, no. 3, pp. 132-142, 2003.
[7] M. Maile, F. Ahmed-Zaid, S. Bai, L. Caminiti, P. Mudalige, M. Peredo, and Z. Popovic, "Objective testing of a cooperative intersection collision avoidance system for traffic signal and stop sign violation," in Proc. IEEE Intelligent Vehicles Symposium, Baden-Baden, Jun. 2011, pp. 130-137.
[8] J. Kolodko and L. Vlavic, "Cooperative autonomous driving at the intelligent control systems laboratory," IEEE Intelligent Systems, vol. 18, no. 4, pp. 8-11, 2003.
[9] C.-Y. Chan and B. Bougler, "Evaluation of cooperative roadside and vehicle-based data collection for assessing intersection conflicts," in Proc. IEEE Intelligent Vehicles Symposium, Anchorage, AL, Sep. 2005, pp. 165-170.
[10] A. S. Farahmand and L. Mili, "Cooperative decentralized intersection collision avoidance using extended kalman filtering," in Proc. IEEE Intelligent Vehicles Symposium, Xian, Sep. 2009, pp. 977-982.
[11] U. Ozguner, C. Stiller, and K. Redmill, "Systems for safety and autonomous behavior in cars: The darpa grand challenge experience," Proceedings of the IEEE, vol. 95, no. 2, pp. 397-412, 2007.
[12] E. Konstantinidis, G. Patoulidis, I. Vandikas, C. Parisses, and N. Asimopoulos, "Development of a collaborative vehicle collision avoidance system," in Proc. IEEE Intelligent Vehicles Symposium, San Diego, CA, Jun. 2010, pp. 1066-1071.
[13] L. Jiang, C. Bai-Gen, W. Yun-Peng, and W. Jian, "Location-based cooperative vehicle collision avoidance for unsignalized intersections: A multi-sensor integration approach," in Proc. of International Conference on Conference on Connected Vehicles and Expo, Vienna,, Nov. 2014, pp. 246-251.
[14] H.-S. Tan and J. Huang, "DGPS-based vehicle-to-vehicle cooperative collision warning: Engineering feasibility viewpoints," IEEE Transactions on Intelligent Transportation Systems, vol. 7, no. 4, pp. 415-428, 2006.
[15] J. Lee and B. Park, "Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment," IEEE Transactions on Intelligent Transportation Systems, vol. 13, no. 1, pp. 81-90, 2012.
[16] F. Basma, Y. Tachwali, and H. Refai, "Intersection collision avoidance system using infrastructure communication," in Proc. of International Conference on Intelligent Transportation Systems, Washington DC, Oct. 2011, pp. 422-427.
[17] H. Kowshik, D. Caveney, and P. R. Kumar, "Provable systemwide safety in intelligent intersections," IEEE Transactions on Vehicular Technology, vol. 60, no. 3, pp. 804-817, 2011.
[18] M. R. Hafner, D. Cunningham, L. Caminiti, and D. D. Vecchio, "Cooperative collision avoidance at intersections: Algorithms and experiments," IEEE Transactions on Intelligent Transportation Systems, vol. 14, no. 3, pp. 1162-1175, 2013.
[19] H. Ahn and D. D. Vecchio, "Semi-autonomous intersection collision avoidance through job-shop scheduling," in Proc. of of the 19th International Conference on Hybrid Systems: Computation and Control.
[20] A. Colombo and D. D. Vecchio, "Least restrictive supervisors for intersection collision avoidance: A scheduling approach," IEEE Transactions on Automatic Control, vol. 60, no. 6, pp. 1515-1527, 2015.
[21] F. Belkhouche, "Reactive path planning in a dynamic environment," IEEE Transactions on Robotics, vol. 25, no. 4, pp. 902-911, 2009.
[22] D. Pallaschke and J. Rosenmuller, "Computing the Minkowski sum of prisms," Journal of Global Optimization, vol. 35, no. 2, pp. 321-341, 2006.
[23] F. Belkhouche and B. Bendjilali, "Dynamic collision risk modeling under uncertainty," Robotica, vol. 31, no. 4, pp. 525-537, 2012.

[^0]:    The author is with the department of Electrical and Electronic Engineering, CSU Sacramento. email: belkhouf@ecs.csus.edu.

