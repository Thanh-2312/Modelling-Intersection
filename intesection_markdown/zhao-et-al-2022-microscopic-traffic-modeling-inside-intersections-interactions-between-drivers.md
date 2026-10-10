This article was downloaded by: [116.96.45.109] On: 13 August 2026, At: 02:10
Publisher: Institute for Operations Research and the Management Sciences (INFORMS)
INFORMS is located in Maryland, USA
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-01.jpg?height=674&width=505&top_left_y=258&top_left_x=72)

Transportation Science

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Microscopic Traffic Modeling Inside Intersections: Interactions Between Drivers 

Jing Zhao, Victor L. Knoop, Meng Wang

To cite this article:
Jing Zhao, Victor L. Knoop, Meng Wang (2023) Microscopic Traffic Modeling Inside Intersections: Interactions Between Drivers. Transportation Science 57(1):135-155. https://doi.org/10.1287/trsc.2022.1163

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy, distribute, transmit and adapt this work, but you must attribute this work as "Transportation Science. Copyright © 2022 The Author(s). https://doi.org/10.1287/trsc.2022.1163, used under a Creative Commons Attribution License: https://creativecommons.org/licenses/by/4.0/."

Copyright © 2022 The Author(s)

Please scroll down for article-it is on subsequent pages

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.
For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Microscopic Traffic Modeling Inside Intersections: Interactions Between Drivers 

Jing Zhao, ${ }^{\mathbf{a , b , *}}$ Victor L. Knoop, ${ }^{\mathbf{b}}$ Meng Wang ${ }^{\mathbf{b , c}}$<br>${ }^{\text {a }}$ Department of Traffic Engineering, University of Shanghai for Science and Technology, Shanghai 200093, China; ${ }^{\text {b }}$ Department of Transport \& Planning, Delft University of Technology, 2628 CN Delft, Netherlands; ${ }^{\text {c }}$ "Friedrich List" Faculty of Transport and Traffic Sciences, Technische Universität Dresden, 01069 Dresden, Germany<br>*Corresponding author<br>Contact: jing_zhao_traffic@163.com, (D https://orcid.org/0000-0003-0741-4911 (JZ); v.l.knoop@tudelft.nl, - https://orcid.org/0000-0001-7423-3841 (VLK); meng.wang@tu-dresden.de, (D) https://orcid.org/0000-0001-6555-5558 (MW)

Received: October 25, 2020
Revised: September 11, 2021; March 4, 2022
Accepted: June 30, 2022
Published Online in Articles in Advance:
July 27, 2022
https://doi.org/10.1287/trsc.2022.1163
Copyright: © 2022 The Author(s)


#### Abstract

Microscopic traffic flow models enable predictions of traffic operations, which allows traffic engineers to assess the efficiency and safety effects of roadway designs. Modeling vehicle trajectories inside intersections is challenging because there is an infinite number of possible paths in a two-dimensional space, and drivers can simultaneously adapt their speeds as well. To date, human driver models for simultaneous longitudinal and lateral vehicle control based on the infrastructure characteristics and interactions with other drivers inside an intersection are still lacking. The contribution of this paper is threefold. First, it proposes an integrated microscopic traffic flow model to describe human-driven vehicle maneuvers under interactions. Drivers plan their heading and acceleration in the predicted future to minimize costs representing undesirable situations. The model works with a joint optimization for an interaction cost term. The weights associated with the interaction cost reflect how selfish or altruistic drivers are. Second, the proposed model endogenously gives the order of vehicles in case of crossing paths. Third, the paper develops a clustered validation method for microscopic traffic flow models with interacting vehicles, which account for interdriver variations. Results show that the model can accurately describe vehicle passing orders of interacting maneuvers, paths, and speeds against empirical data. The model can be applied to assess various intersection designs.


Open Access Statement: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy, distribute, transmit and adapt this work, but you must attribute this work as "Transportation Science. Copyright © 2022 The Author(s). https://doi.org/10.1287/trsc.2022.1163, used under a Creative Commons Attribution License: https://creativecommons.org/licenses/by/4.0/." Funding: This work was supported by the National Natural Science Foundation of China [Grants 71971140 and 52122215] and the Natural Science Foundation of Shanghai [Grant 20ZR1439300].

Keywords: traffic flow model • driver interactions • intersections • vehicular trajectory • optimal control

## 1. Introduction

Intersections are the critical nodes of the urban traffic network, and their design has great implications for traffic safety and efficiency. Microscopic traffic flow models describing vehicular maneuvers and traffic patterns are widely used as a tool for optimal design and performance evaluation of traffic facilities. In the inner area of interactions, driver behavior is heavily influenced by the interactions with conflicting vehicles. Understanding and describing vehicle maneuvers in the inner area of interactions taking into account vehicle interactions is a challenging task for traffic flow modeling and deserves dedicated attention.

A significant volume of research exists on microscopic traffic flow modeling at intersections. They can be mainly divided into four categories: car-following combined with lane-changing models, cellular automata models, social force models, and optimal control models. The following paragraphs made a brief review of the existing studies in the aforementioned order.

Car-following and lane-changing models are the two fundamental driving behavior models. Carfollowing models describe the longitudinal behavior of the following vehicle under the influence of the preceding vehicle(s), and lane changing models describe drivers' decision to change from the current lane to an adjacent lane (Li, Jiang, and Jia 2011, Wang et al. 2020). At intersections, existing studies mainly include the effect of signal control and traffic management on driving behavior. Ahn, Cassidy, and Laval (2004) discussed the time-space trajectory of discharging vehicles by verifying Newell (2002)'s simplified carfollowing model. Sasaki and Nagatani (2003) explored the traffic flow under three signal control scenarios:
the simple synchronized, green wave, and random switching strategies. Tang et al. (2008) explored the traffic clustering, dissipating, and the propagation of stop and start waves caused by the signal control. The effects of the various signal control methods on the car-following behavior at intersections were discussed, such as the green signal countdown device (Yu and Shi 2015, Tang et al. 2017), the speed guidance system (Zhao and Li 2016, Tang, Zhang, and Liu 2017), and the automation and communication technology (Hoogendoorn, van Arerm, and Hoogendoom 2014). Human factors were also considered in modeling to achieve a more realistic representation of driving behavior in complex traffic conditions and to better understand the widely reported puzzling traffic flow phenomena (Saifuzzaman and Zheng 2014). Based on a series of car-following experiments on the open road (Jiang et al. 2015, 2018), Jiang et al. (2018) proposed that traffic instability is caused by the cumulative effect of stochastic factors. A two-dimensional intelligent driver model (2D-IDM) was proposed to describe the car-following behavior correspondingly, in which the desired time gap changes over time. It is found that the traffic state of the following vehicle could oscillate in the 2D region of the velocity-spacing plane, even if the leading vehicle moves with constant velocity. The 2D-IDM was further improved to eliminate overly high deceleration by restricting the changing rate of desired time gap (Xiong, Jiang, and Tian 2019). In general, car-following and lane-changing models have well-described vehicle behaviors on the approach lanes of intersections. However, existing car-following and lane-changing models are lane based, that is, vehicles have to travel along a given lane. Mullakkal-Babu et al. (2021) presented a method to integrate vehicle lateral dynamics and yaw motion into a submicroscopic traffic modeling framework so that 2D vehicle trajectories can be generated. However, it focused on lane-based highway driving, and tactical lane change decisions are needed. The mechanism behind these models is intrinsically different from the 2D driver behavior in the inner area of the intersection absent of lanes. Because the concept of traffic lanes is weakened in the inner area of intersections, existing car-following and lane-changing models cannot provide a realistic description of traffic operations.

Cellular automata (CA) models are another type of widely used model in describing the complex movements of vehicles at intersections. The conflicts between the vehicles at intersections were firstly analyzed (Ruskin and Wang 2002, Foulaadvand and Belbasi 2007, Li et al. 2009). Based on these CA models, the relationship between conflict occurrences and control strategies can be explored (Chai and Wong 2014). Chai and Wong (2015) proposed a fuzzy cellular automata model at signalized intersections by combining the cellular automata and fuzzy logic, which can replicate the decisionmaking processes of the driver. The CA model was also developed for the mixed traffic flow at intersections, for example, the interaction between vehicles and bicycles (Zhao, Gao, and Jia 2007, Vasic and Ruskin 2012). Recently, the driving behavior models of electric bicycles (Tang et al. 2018) and the connected vehicles (Zhu and Ukkusuri 2018) at the intersections were also proposed. However, because the lattice of cells in CA models has an equal size, the movement of vehicles is limited by the given tracks of cells in the CA model. Therefore, the descriptive power of the CA model is also limited in the inner area of the intersection.

Social force-based models can describe vehicle movements in the inner area of the intersection without lane division. In the literature, the social force-based model has been applied to describe the pedestrian flow (Helbing et al. 2005, Zeng et al. 2014), cyclist flow (Huang et al. 2016), and vehicular flow (Ma et al. 2017) at intersections and the interaction between them in shared spaces (Anvari et al. 2014, 2015; Yuan et al. 2017). Several types of forces were considered to obtain realistic trajectories, including the self-driven force, the repulsive force, the attractive force, and other forces for specific conditions. These models reproduce a broad set of collective phenomena successfully. For the vehicular movement, several social force-based vehicle movement models were established to simulate the vehicular traffic flow with the consideration of no lane division (Fellendorf, Schönauer, and Huang 2012, Huynh, Boltze, and Vu 2013, Yang et al. 2019). Aiming at describing the vehicular movement at intersections, Ma, Sun, and Wang (2017) proposed a three-layered "plan-decision-action" model to simulate the moving of turning vehicles at mixed-flow intersections. The social force model was further used to generate vehicle movements in the operation layer (Ma et al. 2017). However, one of the shortcomings of social force-based models is that the trajectory is obtained by the comprehensive result of several types of forces instead of being obtained from the driver's maneuvers. The interpretability of model results may be argued.

The optimal control model is another feasible method to describe vehicular movement at intersections. In the field of autonomous vehicle control, lots of cooperative vehicle control algorithms were established to enable autonomous vehicles to pass the intersection cooperatively without traffic signals (Yu et al. 2019) The vehicular trajectories are assumed to be along the predetermined traffic lanes in these models. For the 2D modeling, Hoogendoorn and colleagues planned the route of pedestrians (Hoogendoorn and Bovy 2004) and vessels (Shu et al. 2015). For vehicles, Bichiou and Rakha (2018) developed an algorithm to obtain an optimal trajectory for the automated vehicle. The
algorithm was further simplified to make it possible for real-time implementations (Bichiou and Rakha 2019). The model can well control autonomous vehicles. To describe the maneuvers of human drivers, a 2D vehicular movement model for one vehicle movement was proposed (Zhao, Knoop, and Wang 2020). The model can handle interactions with the roadway. However, only one vehicle movement was considered. The interactions between vehicles are not considered with the rigorous formulation and systematic calibration and validation.

Therefore, the purpose of this paper is to establish the 2D traffic flow model to describe vehicle maneuvers with the consideration of the interactions between human-driven vehicles inside interactions. The difficulty of modeling vehicle maneuvers in the inner area of interactions lies in (1) getting the order of vehicles correct, (2) getting the right path in 2D space because there is an infinite number of possible, and (3) getting the right speed of the drivers on that path.

The contributions of the paper are threefold. First, the model can describe 2D vehicle maneuvers of paths and speeds under interactions accurately. Second, the model endogenously gives the order of vehicles in case of crossing paths. Third, a "calibration-clustering-validation" method is proposed to validate the established model. Compared with the previous model (Zhao, Knoop, and Wang 2020), the current model can describe the interactions of vehicles with each other, whereas the previous model can only handle interactions between the vehicle and the roadway. Moreover, model validation is an issue for stochastic models because neither selecting a random set of parameters for each vehicle nor trying the best of all trajectories with calibrated parameters are desirable. A new three-step approach validation method is proposed, which is a generic methodology validating the traffic flow model with stochastic driver behavior. The application of the model lies in the evaluation of intersection design.

The remainder of the article is organized as follows. The optimization model formulation and implementation are introduced in Section 2. The properties of the proposed model, including the descriptive power and plausibility analysis, are explored in Section 3. Section 4 proposes a generic methodology for validating models with interacting vehicles. Then, Section 5 presents the tailored validation method for the proposed model and the validation procedure using empirical data. Section 6 presents the conclusions and discusses future research directions.

## 2. Optimization Model Formulation and Implementation

This section introduces the mathematical model. The conceptual idea of the new model is first introduced. Then, the vehicular movement model for one vehicle is briefly revisited. The specification of the vehicle interactions is described in Section 2.3, which considers the interaction between human-driven vehicles at intersections. Last, the solution of the proposed model is introduced in Section 2.4.

### 2.1. Conceptual Model and Assumptions

At intersections, vehicles move from an approach lane to an exit lane. In such continuous 2D space, an infinite number of trajectories from origin to destination is possible. In the process of passing intersections, vehicles have to interact with each other, such as crossing, merging, and car-following, as shown in Figure 1. Generally, human drivers control the longitudinal and lateral vehicle motion based on the infrastructure characteristics and interactions with other drivers. The model framework postulates human drivers are predictive utility maximizers: that is, they predict the change in the dynamic driving environment and control the steering angle and accelerations simultaneously to minimize a cost function. Costs/disutilities reflect undesirable situations such as deviation from the preferred path, desired speed, and increased risk of collision with static and moving objects (Zhao, Knoop, and Wang 2020).

In this paper, we focus on interactions with other human drivers. We do so by adding a safety cost term for being close to another driver, of which the magnitude depends on the proximity, speeds, and relative angles. We assume that drivers are rational and able to estimate the trajectories (a combination of location in space and speed profile) of interacting vehicles and minimize this safety cost while maximizing driving efficiency and ride comfort. Conflicts are handled by making tradeoffs between different costs.

Figure 1. (Color online) Problem Description
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-04.jpg?height=816&width=767&top_left_y=1740&top_left_x=1077)

Under the behavioral assumptions and the optimal control framework, the model can capture conflicts as crossing, merging, and car-following, as well as describe different strategies as slowing down to yield, making a detour to avoid the conflict, and speeding up to make a hard cut. Different drivers can have different driving styles that are reflected by the weights of the costs.

### 2.2. Revisit of the One Vehicle Movement Model

The 2D vehicular movement model for one vehicle was proposed in previous work (Zhao, Knoop, and Wang 2020). It incorporates steering and acceleration as two separate model inputs and chooses the travelled distance (s) as the main independent variable instead of time. The advantage of choosing the travelled distance as the main independent variable is that the longitudinal and lateral controls are decoupled. A particular steering function as a function of $s$ leads, independently of the acceleration function, to a particular path in space. The vehicle motion dynamics can be described by Equation (1); $\kappa_{i}$ and $\alpha_{i}$ constitute the control $\mathbf{U}_{i}$, as shown in Equation (2). The control variable $\kappa_{i}$ can be seen as the control of the steering wheel, whereas another control variable $\alpha_{i}$ can be seen as the control of the brake or throttle pedals. In this way, the full trajectory of a vehicle from the approach lane to the exit lane can be described as the control result of a human driver. The lane-free approach is used because there is no lane division inside the intersection in most cases. If there is strict lane discipline inside the interaction, the constraint of the allowed moving space can be added:

$$
\frac{\mathrm{d}}{\mathrm{~d} s} \mathbf{X}_{i}(s)=\frac{\mathrm{d}}{\mathrm{~d} s}\left[\begin{array}{c}
x_{i}(s) \\
y_{i}(s) \\
\theta_{i}(s) \\
p_{i}(s)
\end{array}\right]=\left[\begin{array}{c}
\cos \theta_{i}(s) \\
\sin \theta_{i}(s) \\
\kappa_{i}(s) \\
\alpha_{i}(s)
\end{array}\right] \text {, with } \mathbf{X}_{i}(0)=\mathbf{X}_{0 i}
$$

where $\mathbf{X}_{i}(s)$ is the state vector of vehicle $i$ at moving distance $s ; x_{i}(s)$ and $y_{i}(s)$ are the plane coordinate of vehicle $i$ at moving distance $s$, in meters; $\theta_{i}(s)$ is the heading angle of vehicle $i$ at moving distance $s$, in rad; $p_{i}(s)$ is the pace of vehicle $i$ (reciprocal of the speed of vehicle $i$ at moving distance $s$ ), in seconds per meter; $\kappa_{i}(s)$ is the curvature (reciprocal of the turning radius) of the trajectory of vehicle $i$ at moving distance $s$, in rad per meter; $\alpha_{i}(s)$ is the parameter indicating the acceleration of vehicle $i$ at moving distance $s$, in seconds per meter (a positive value indicates decelerating, a negative value indicates accelerating); $\mathbf{X}_{0 i}$ is the initial state of vehicle $i ; \mathbf{X}_{f i}$ is the terminal state of vehicle $i$; and $s_{f i}$ is the distance traveled from the initial state to the terminal state of vehicle $i$, in meters:

$$
\mathbf{U}_{i}(s)=\left[\begin{array}{c}
\kappa_{i}(s) \\
\alpha_{i}(s)
\end{array}\right],
$$

where $\mathbf{U}_{i}(s)$ is the control vector of vehicle $i$ at moving distance $s$.

The optimal full trajectory planning problem from the initial state $\mathbf{X}_{0 i}$ to the terminal state $\mathbf{X}_{f i}$ can be formulated as Equation (3). The initial state and terminal state are given, which reflects the geometric characteristics. The running cost $L_{i}$ reflects the different cost aspects considered by the drivers during driving. We model it as a sum of different elements, including the travel time of the trajectory (travel time cost), the vehicular lateral acceleration (turning cost), and longitudinal acceleration (acceleration cost), as shown in Equation (4):

$$
\min _{\mathbf{U}_{i}} C\left(\mathbf{X}_{i}, \mathbf{U}_{i}\right)=\min _{\mathbf{U}_{i}} \int_{0}^{s_{f i}} L_{i}\left(s, \mathbf{X}_{i}, \mathbf{U}_{i}\right) \mathrm{d} s,
$$

where $L_{i}$ is the running cost of vehicle $i$, which reflects the costs occurring during a trajectory:

$$
L_{i}=\sum_{j} \beta_{j i} L_{j i}=\beta_{1 i} p_{i}+\beta_{2 i} \frac{1}{2} a_{c i}^{2}+\beta_{3 i} \frac{1}{2} a_{l i}^{2},
$$

where, $L_{j i}$ is the running cost of term $j$ of vehicle $i ; \beta_{j i}$ is the relative weight of the running cost aspect $j$ of vehicle $i$, which is the intrinsic characteristic of drivers; $a_{c i}$ is the vehicular lateral acceleration, in meters per second ${ }^{2}$, which can be calculated by Equation (5); and $a_{l i}$ is the vehicular longitudinal acceleration, in meters per second ${ }^{2}$, which can be calculated by Equation (6):

$$
\begin{aligned}
a_{c i} & =\kappa_{i} p_{i}^{-2} \\
a_{l i} & =-\alpha_{i} p_{i}^{-3}
\end{aligned}
$$

For constraints, the running speed, curvature, and acceleration should be limited according to the traffic rule and the characteristic of a vehicle, as shown in Equations (7)-(9), respectively:

$$
\begin{aligned}
\frac{1}{v_{i \max }} & \leq p_{i} \leq \frac{1}{v_{i \min }}, \\
-\frac{1}{r_{i \min }} & \leq \kappa_{i} \leq \frac{1}{r_{i \min }}, \\
a_{i \min } & \leq a_{l i} \leq a_{i \max }
\end{aligned}
$$

where $v_{i \max }$ and $v_{i \min }$ are the speed limit of vehicle $i$, in meters per second; $r_{\text {imin }}$ is the minimum turning radius of vehicle $i$, in meters; and $a_{i \text { min }}$ and $a_{i \text { max }}$ are the minimum and maximum acceleration of vehicle $i$, in meters per second ${ }^{2}$.

### 2.3. Model with Vehicle Interactions

When there is more than one vehicle, human drivers want to keep safe and avoid collisions during driving.

However, various human drivers have various awareness of safety (Hamdar, Mahmassani, and Treiber 2015, Hamdar et al. 2020). We hope the proposed model can reflect the difference in the safety concept among human drivers and the tradeoff between the utilities of time, comfort, and safety during driving. Therefore, the vehicle interaction is treated by adding a new running cost term in the objective function of the model instead of adding a hard constraint on safety. In this way, the weights of the costs can be used to reflect the interdriver variations and the priority rules, for example, aggressive drivers care more about travel time, whereas conservative drivers care more about safety.

The new running cost term is shown in Equation (10). It is a function of the radial velocity and the distance, as shown in Figure 2(a). The radial velocity of an object with respect to a given point is the rate of change of the distance between the object and the point. That is, the radial velocity is the component of the object's velocity that points in the direction of the radius connecting the point and the object. Here, only the positive value is used, as shown in Equation (11). Additionally, according to the physical concept, kinetic energy is proportional to the square of the speed. Therefore, the square of the radial velocity is used. Moreover, enlarging the distance between the vehicles can increase safety. The distance has a more significant effect when the two vehicles are close to each other. Therefore, the negative exponential function of the distance is used. Then, the safety running cost $\left(L_{4 i}\right)$ increases with the increase of the radial velocity and with the decrease of the distance between the interacting vehicles. The combined effect is shown in Figure 2(b):

$$
L_{4 i}=v_{r i b}^{2} e^{-D_{i b}},
$$

where $v_{\text {rib }}$ is the radial velocity of the interacting vehicle $b$ with respect to the target vehicle $i$, in meters per second, which can be determined by Equation (11); and $D_{i b}$ is the distance between two vehicles, $D_{i b}=\sqrt{\left(x_{i}-x_{b}\right)^{2}+\left(y_{i}-y_{b}\right)^{2}}$, in meters:

$$
v_{r i b}=\left\{\begin{aligned}
v_{i} \cos \varphi_{i b}+v_{b} \cos \gamma_{i b}, & v_{i} \cos \varphi_{i b}+v_{b} \cos \gamma_{i b} \geq 0 \\
0, & v_{i} \cos \varphi_{i b}+v_{b} \cos \gamma_{i b}<0,
\end{aligned}\right.
$$

where $v_{i}=1 / p_{i}$ and $v_{b}=1 / p_{i}$ are the velocities of the target and interacting vehicles, respectively, in meters per second; $\varphi_{i b}$ is the angle between the direction from the target vehicle $i$ to the interacting vehicle $b$ and direction of the target vehicle's velocity, in rad; and $\gamma_{i b}$ is the angle between the direction from the interacting vehicle $b$ to the target vehicle $i$ and direction of the interacting vehicle's velocity, in rad. The safety cost will be active (larger than zero) when the radial velocity is larger than zero. For the oncoming vehicles, the radial velocity is always larger than zero because the directions of the interacting vehicles are opposing. For crossing and merging conflicts, the radial velocity is larger than zero before one vehicle passes the conflict point because the velocity components in the direction of connecting the two interaction vehicles are opposing. For other conditions such as following vehicles and diverging conflicts, it depends. For example, if the velocity of the following vehicle is lower than that of the vehicle in front, there is no risk of collision.

Therefore, the running cost of one vehicle can be determined by Equation (12). For multiple vehicles condition, the interacting vehicles deal with the conflict together to pass the intersection. One way to formulate this process is to incorporate the cost into the path planning of both interacting vehicles simultaneously.

Figure 2. (Color online) Safety Cost Under the Combined Effect of Radial Velocity and Distance
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-06.jpg?height=571&width=1436&top_left_y=1929&top_left_x=297)

Alternative formulations are that each driver planned his own cost in a game-theoretical framework (Talebpour, Mahmassani, and Hamdar 2015, Wang et al. 2015, Kang and Rakha 2018, Ali et al. 2019). Some models allow balancing between cooperation and selfishness (Kesting, Treiber, and Helbing 2007). The model that we propose chooses the cooperative modeling method, which assumes that drivers will consider the running cost of other vehicles. From the modeling perspective, there is an advantage to the cooperative way of modeling. In that case, a full trajectory of a vehicle from the approach lane to the exit lane can be planned at one time using the cooperative objective function of multiple vehicles. In the case of selfish game-theoretic modeling, the trajectory of a vehicle passing the intersection has to be generated by repeating trajectory planning because the running condition of conflicting vehicles will change over time. In real life, at the intersection, drivers have almost complete information about conflicting vehicles, so predicting the paths of others is not unreasonable to assume. Moreover, drivers are trained to drivers control their vehicles to avoid collisions. For the proposed model, the cooperative approach predicts the vehicle interactions well (see the validation results in Section 5); hence, this approach is followed in the paper.

The total running cost equals the sum of the running cost of each vehicle, as shown in Equation (13), and the full trajectories of multiple vehicles can be obtained simultaneously.

$$
\begin{aligned}
L_{i} & =\sum \beta_{j i} L_{j i} \\
& =\beta_{1 i} p_{i}+\beta_{2 i} \frac{1}{2} \kappa_{i}^{2} p_{i}^{-4}+\beta_{3 i} \frac{1}{2} \alpha_{i}^{2} p_{i}^{-6}+\beta_{4 i} v_{r i b}^{2} e^{-D_{i b}} \\
& L=\sum_{i} \frac{1}{\beta_{4 i}} L_{i}
\end{aligned}
$$

The reciprocal of $\beta_{4 i}$ is used as the weight for $L_{i}$, which indicates the dominant level of a vehicle among the interacting vehicles, as shown in Equation (13). The running cost of the vehicle with a lower safety concern (lower $\beta_{4 i}$ ) will have a relatively higher weight in the cooperative running cost of the interacting vehicles. Then, the model is inclined to keep the original trajectory without the consideration of the vehicle interaction. In the other extreme end, for the vehicle with higher safety concerns (higher $\beta_{4 i}$ ), its running cost will have a relatively lower weight in the total running cost of the interacting vehicles. Then, its trajectory will be largely affected by the conflicting vehicles. In the absence of interactions, the value $\beta_{4 i}$ has no effect, and the planned trajectory will be the same as the result of the one-vehicle movement model in previous work (Zhao, Knoop, and Wang 2020) because the weights are relative. The optimal objective function value will increase proportionally by multiplying a coefficient to the running cost, but the optimal solution will not change.

### 2.4. Solution of the Optimal Control Model

The proposed model can plan the full trajectories from the approach lanes to the exit lanes of multiple humandriven vehicles. The trajectories of interacting vehicles are jointly planned. The proposed 2D trajectory planning problem is a free terminal problem because the upper limit of integral in Equation (3), $s_{f i}$, is unspecified. To handle this problem, the traveled distance is rescaled to be $\zeta=s / s_{f i}$. Then, $\zeta \in[0,1]$, and the rescaled distance at the terminal equals to 1 . Correspondingly, the derivative $\mathrm{d} s$ should be replaced by $s_{f i} \mathrm{~d} \zeta . s_{f i}$ becomes an additional unknown that has to be determined by the optimization. Hence, the control vector $\left(\mathbf{U}_{i}\right)$ and the distance traveled from the initial state to the terminal state $\left(s_{f i}\right)$ of all interacting vehicles are planed together, as shown in Equation (14):

$$
\mathbf{U}=\left(\mathbf{U}_{1}^{T}, s_{f 1}, \ldots, \mathbf{U}_{n}^{T}, s_{f n}\right)^{T},
$$

where $\mathbf{U}$ is the set of control variables of all interacting vehicles; and $I=1,2 \ldots n$ is the set of interacting vehicles we considered.

In summary, the 2D trajectory planning problem can be reformulated as follows:

$$
\min _{\mathbf{U}}\left(\sum_{i} \int_{0}^{1} \frac{1}{\beta_{4 i}} L_{i} s_{f i} \mathrm{~d} \zeta, \forall i \in I\right)
$$

subject to

$$
\frac{\mathrm{d}}{\mathrm{~d} \zeta}\left[\begin{array}{c}
x_{i} \\
y_{i} \\
\theta_{i} \\
p_{i}
\end{array}\right]=s_{f i}\left[\begin{array}{c}
\cos \theta_{i} \\
\sin \theta_{i} \\
\kappa_{i} \\
\alpha_{i}
\end{array}\right], \quad \text { with } \quad \mathbf{X}_{i}(0)=\mathbf{X}_{0 i} \text { and } \mathbf{X}_{i}(1)=\mathbf{X}_{f i}
$$

$$
L_{i}=\sum \beta_{j i} L_{j i}=\beta_{1 i} p_{i}+\beta_{2 i} \frac{1}{2} \kappa_{i}^{2} p_{i}^{-4}+\beta_{3 i} \frac{1}{2} \alpha_{i}^{2} p_{i}^{-6}+\beta_{4 i} v_{r i b}^{2} e^{-D_{i b}},
$$

$$
\frac{1}{v_{i \max }} \leq p_{i} \leq \frac{1}{v_{i \min }},
$$

$$
-\frac{1}{r_{i \min }} \leq \kappa_{i} \leq \frac{1}{r_{i \min }} .
$$

$$
a_{i \min } \leq a_{l i} \leq a_{i \max }
$$

The optimizer then picks the appropriate traveled distance at the terminal $\left(s_{f i}\right)$ and the control vector $\left(\mathbf{U}_{i}\right)$, which contains the curvature $\kappa_{i}$ and acceleration $\alpha_{i}$ in each control step, for all interacting vehicles simultaneously.

To solve the proposed trajectory planning model (Equations (15)-(20)), the control variables are discretized with the consideration of control constraints. Then, the state variables in each control step and the
objective function can be derived from the initial state in succession by numerical integration. The discrete problem is solved as a constrained optimization problem. The numeric optimization toolbox CasADi is used (Andersson et al. 2019) to solve the proposed model, in which we opt for the IPOPT (interior-point optimizer) algorithm (Wächter and Biegler 2006). The computational time is around 150 seconds for each interacting pair with the precision of 50 control steps in the full trajectory on an Intel(R) Core(TM) i7 2.60-GHz processor with 16.0 GB of RAM, which is acceptable for this offline traffic flow model.

The states of the interacting vehicles should be at the same timestamp when calculating the safety cost. Because the state of a vehicle is described by using the moving distance as the dependent variable in the proposed model, the state of a conflicting vehicle should be converted to a state with the same timestamp. The time $\Delta t$ between the two successive control steps can be obtained from distance $s$ and the pace $p$, as shown in Equation (21). In a quite short distance, Equation (21) turns to Equation (22) by using the Euler forward difference. Normally, it will cause a stability issue. However, the terminal state is given as external input in this study. The vehicle is restricted to reach the terminal state even the discretization step is large. Therefore, the stability issue can be avoided. The Euler backward scheme is an alternative method to enhance stability, which is more complex as it requires iteration:

$$
\begin{gathered}
\Delta t_{i k}=\int_{\zeta_{i k}}^{\zeta_{i(k+1)}} p_{i} s_{f i} \mathrm{~d} \zeta \\
\Delta t_{i k}=p_{i k} s_{f i} \Delta \zeta_{i}+\frac{1}{2} \alpha_{i k} s_{f i} \Delta \zeta_{i}^{2}
\end{gathered}
$$

where $\Delta t_{i k}$ is the passed time between the two successive control steps $k$ and $k+1$ of vehicle $i$, in seconds; and $\Delta \zeta_{i}$ is the normalized control step length of vehicle $i$.

The reaction time and other time-related factors can be incorporated in the proposed model using the receding horizon concept. Reaction time can be modeled explicitly as delay in the state variables. One may argue that there are other human factors: human anticipation in space and time, which can effectively compensate for delays and hence justify the delay-free formulation as we did. In car-following, this has been shown by Treiber, Kesting, and Helbing (2006). Compensation delay in optimal control is very straightforward and leads to almost the same trajectory as the delay-free formulation if a delay is insignificant (Wang et al. 2018). Errors in estimation and prediction of surrounding vehicles trajectories can also be included. Receding horizon control is a feedback optimal control approach that allows replanning of trajectories, which can correct human errors in estimating and predicting other vehicles' trajectories in our case. However, our modeling principle is parsimonious. Incorporating more human factors will increase the model complexity, the number of parameters, and add additional challenges in model validation and calibration. This is a dedicated subject and can be left for future research.

The numerical implementation leads to numerical errors. For special cases, we can find analytical solutions to verify numerical solutions. The main idea in the analytical solution procedure is to construct the Hamiltonian and solve it with the Pontryagin principle (Hoogendoorn et al. 2012, Wang et al. 2012, Zhao, Knoop, and Wang 2020). We have analyzed 16 reallife inspired cases of movement of a single vehicle to check the effects of the numerical errors. As listed in Table 1, they contain U-turn (Scenarios A and B), left turns with various angles (Scenarios C to I), through movements with/without an offset (Scenarios J to L), and right turns with various angles (Scenarios M to P). The results of the numerical solution and the analytical one are illustrated in Figure 3. The Euclidean distance for the path and the absolute error of the pace at each calculated step is calculated. Then, the RMSE (root-mean-square error) in path (position state) and pace under each case can be obtained, as shown in Table 1. Overall, the differences between the numerical solution and the analytical one are minimal: a typical error in position in the order of millimeters and a typical error in speed in the order of 1E-5 m/s.

## 3. Model Properties

The properties of the proposed model are explored in this section according to the following two steps: (1) analyze the descriptive power of a solution to the model by simultaneously planning the trajectories of several vehicles (Section 3.1); and (2) analyze the plausibility of model behavior in the crossing, merging, and car-following maneuvers (Section 3.2).

### 3.1. Descriptive Power Analysis

The proposed method can plan the trajectories of several vehicles simultaneously. As an example, several vehicles with various initial and terminal states are listed in Table 2. The planned trajectories are illustrated in Figure 4, in which the color of the trajectory indicates the running time. One can find that because the conflict point between vehicles A and B is closer to the initial position of vehicle A, vehicle A crosses the conflict point first, whereas vehicle B slows down and makes a slight detour to avoid the conflict. Similarly, vehicles C crosses the conflict point with vehicle A first and then passes the conflict point following vehicle B. It shows that the proposed solution algorithm can

Table 1. Numerical Errors Analysis Under the Fastest Trajectory Condition
| Scenario | Movement | Initial state | Terminal state | RMSE |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  | Path $(x, y), \mathrm{m}$ | Pace $(p), \mathrm{s} / \mathrm{m}$ |
| A | U-turn | [0, 0, 0, 1/8] | $[0,10, \pi]$ | $2.230 \mathrm{E}-03$ | $3.969 \mathrm{E}-05$ |
| B | Left-turn |  | $[2,10,9 \pi / 10]$ | $2.247 \mathrm{E}-03$ | $3.385 \mathrm{E}-05$ |
| C | Left-turn |  | $[4,10,4 \pi / 5]$ | $2.154 \mathrm{E}-03$ | $3.168 \mathrm{E}-05$ |
| D | Left-turn |  | $[6,10,7 \pi / 10]$ | $1.989 \mathrm{E}-03$ | $3.228 \mathrm{E}-05$ |
| E | Left-turn |  | $[8,10,3 \pi / 5]$ | 1.764E-03 | $3.540 \mathrm{E}-05$ |
| F | Left-turn |  | $[10,10, \pi / 2]$ | $1.509 \mathrm{E}-03$ | $4.101 \mathrm{E}-05$ |
| G | Left-turn |  | $[10,8,3 \pi / 8]$ | $1.358 \mathrm{E}-03$ | $3.067 \mathrm{E}-05$ |
| H | Left-turn |  | $[10,6, \pi / 4]$ | $1.159 \mathrm{E}-03$ | 2.343E-05 |
| I | Left-turn |  | $[10,4, \pi / 8]$ | $1.097 \mathrm{E}-03$ | $1.858 \mathrm{E}-05$ |
| J | Through |  | [10, 2, 0] | $5.517 \mathrm{E}-04$ | $1.808 \mathrm{E}-05$ |
| K | Through |  | [10, 0, 0] | $7.347 \mathrm{E}-11$ | $1.489 \mathrm{E}-05$ |
| L | Through |  | [10, -2, 0] | $7.727 \mathrm{E}-04$ | $1.581 \mathrm{E}-05$ |
| M | Right-turn |  | $[10,-4,-\pi / 8]$ | $1.101 \mathrm{E}-03$ | $1.858 \mathrm{E}-05$ |
| N | Right-turn |  | $[10,-6,-\pi / 4]$ | $1.666 \mathrm{E}-03$ | $2.343 \mathrm{E}-05$ |
| O | Right-turn |  | $[8,-6,-3 \pi / 8]$ | $1.043 \mathrm{E}-03$ | $1.839 \mathrm{E}-05$ |
| P | Right-turn |  | $[6,-6,-\pi / 2]$ | $2.233 \mathrm{E}-03$ | $1.125 \mathrm{E}-05$ |
| Average |  |  |  | $1.430 \mathrm{E}-03$ | $2.544 \mathrm{E}-05$ |
| Maximum |  |  |  | $2.247 \mathrm{E}-03$ | $4.101 \mathrm{E}-05$ |
| Minimum |  |  |  | $7.347 \mathrm{E}-11$ | $1.125 \mathrm{E}-05$ |


plan trajectories with different numbers of vehicles. For simplicity, we use two vehicles in the sequel of the analysis.

### 3.2. Plausibility Analysis of Model Behavior

To explore the plausibility of model behavior, three common maneuvers shown in Figure 1 are tested. We illustrate the plausibility of the model behavior in the crossing, merging, and car-following maneuvers.
3.2.1. Crossing Maneuver. There are two interacting vehicles, as illustrated in Figure 5. Vehicle A drives

Figure 3. (Color online) Comparison Between Algorithm Results and Analytical Solutions
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-09.jpg?height=765&width=760&top_left_y=1789&top_left_x=191)

from $\left(x_{0 \mathrm{~A}}, y_{0 \mathrm{~A}}\right)=(0,0) \mathrm{m}$ to $\left(x_{f \mathrm{~A}}, y_{f \mathrm{~A}}\right)=(10,15) \mathrm{m}$. Its initial heading angle $\left(\theta_{0 \mathrm{~A}}\right)$ is 0 rad, initial velocity $\left(v_{0 \mathrm{~A}}\right)$ is 8 m/s, and terminal heading angle $\left(\theta_{f \mathrm{~A}}\right)$ is $\pi / 2$ rad. Vehicle B drives from $\left(x_{0 \mathrm{~B}}, y_{0 \mathrm{~B}}\right)=(5,15) \mathrm{m}$ to $\left(x_{f \mathrm{~B}}, y_{f \mathrm{~B}}\right)=(15,0) \mathrm{m}$. Its initial heading angle $\left(\theta_{0 \mathrm{~B}}\right)$ is $-\pi / 2 \mathrm{rad}$, initial velocity $\left(v_{0 \mathrm{~B}}\right)$ is 8 m/s, and terminal heading angle $\left(\theta_{f \mathrm{~B}}\right)$ is 0 rad. The weights of the travel time $\operatorname{cost}\left(\beta_{1 i}\right)$, turning cost $\left(\beta_{2 i}\right)$, and acceleration $\operatorname{cost}\left(\beta_{3 i}\right)$ are set to be $1,0.01 \mathrm{~s}^{5} / \mathrm{m}^{3}$, and $0.01 \mathrm{~s}^{5} / \mathrm{m}^{3}$, respectively, for both vehicles. Because this paper aims to analyze the behavior of vehicles under the interaction effect, we focus on the effect of the change of the safety cost $\left(\beta_{4 i}\right)$ on the trajectories. In the tested scenarios, the weight of the safety cost of vehicle B $\left(\beta_{4 \mathrm{~B}}\right)$ is changed in the range of $0.01 \mathrm{~s}^{2} / \mathrm{m}$ and 1.0 $\mathrm{s}^{2} / \mathrm{m}$, whereas the safety cost of vehicle $\mathrm{A}\left(\beta_{4 \mathrm{~A}}\right)$ is constant to be $0.01 \mathrm{~s}^{2} / \mathrm{m}$. The maximum speed is set to be 15 m/s. The acceleration is limited in the range of $[-5,5] \mathrm{m}^{2} / \mathrm{s}$. The minimum turning radius is 4 m.

The trajectory pairs (each pair using the same color) under various $\beta_{4 \mathrm{~B}}$ are shown in Figure 5. Overall, with the increase in the weight of the safety cost $\left(\beta_{4 \mathrm{~B}}\right)$, the vehicles make a long detour. As a result, they do more by changing the path and speed to avoid conflict, which is consistent with intuition. To avoid conflict, vehicles should make a tradeoff between changing the path and the velocity, which is a combinational result of different terms of the cost.

Furthermore, the order of vehicles crossing the conflict point is an important feature for the crossing maneuver. It depends on the initial states and the driving behaviors of the interacting vehicles. When the driving behaviors of the interacting vehicles are comparable, the one that can arrive at the conflict point first crosses first. The

Table 2. Input Parameters of Vehicles for Descriptive Power Validation
| Input parameters | Vehicle |  |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  | A | B | C | D |
| Initial position $\left(x_{0}, y_{0}\right), \mathrm{m}$ | $(0,0)$ | $(5,15)$ | $(15,10)$ | $(10,0)$ |
| Initial heading angle $\theta_{0}$, rad | 0 | $-\pi / 2$ | $\pi$ | $\pi / 2$ |
| Initial pace $p_{0}, \mathrm{~s} / \mathrm{m}$ | 1/8 | 1/8 | 1/8 | 1/8 |
| Terminal position $\left(x_{f}, y_{f}\right)$, m | $(10,15)$ | $(15,0)$ | $(0,10)$ | $(0,10)$ |
| Terminal heading angle $\theta_{f}$, rad | $\pi / 2$ | 0 | $\pi$ | $\pi$ |
| Weight of cost $\beta_{1}$ | 1 | 1 | 1 | 1 |
| $\beta_{2}, \mathrm{~s}^{5} / \mathrm{m}^{3}$ | 0.01 | 0.01 | 0.01 | 0.01 |
| $\beta_{3}, \mathrm{~s}^{5} / \mathrm{m}^{3}$ | 0.01 | 0.01 | 0.01 | 0.01 |
| $\beta_{3}, \mathrm{~s}^{2} / \mathrm{m}$ | 1 | 1 | 1 | 1 |
| Maximum speed $v_{\text {max }}, \mathrm{m} / \mathrm{s}$ | 15 | 15 | 15 | 15 |
| Boundary of acceleration $\left[a_{\text {min }}, a_{\text {max }}\right], \mathrm{m}^{2} / \mathrm{s}$ | [-5, 5] | [-5, 5] | [-5, 5] | [-5, 5] |
| Minimum turning radius $r_{\text {min }}$, m | 4 | 4 | 4 | 4 |


order of vehicles crossing the conflict point under various initial states of the vehicles is shown in Figure 6(a) under the condition that $\beta_{1 i^{\prime}}, \beta_{2 i}, \beta_{3 i}$, and $\beta_{4 i}$ are set to be $1,0.01 \mathrm{~s}^{5} / \mathrm{m}^{3}, 0.01 \mathrm{~s}^{5} / \mathrm{m}^{3}$, and $0.01 \mathrm{~s}^{2} / \mathrm{m}$, respectively, for both two vehicles. One can find that, although the conflict point is much closer to vehicle A, the order can be changed when vehicle B has a high initial speed.

The order of vehicles crossing the conflict point also switches under various $\beta_{4 \mathrm{i}}$ values, as shown in Figure 6(b). The initial velocity of vehicle $\mathrm{A}\left(v_{0 \mathrm{~A}}\right)$ and $\mathrm{B}\left(v_{0 \mathrm{~B}}\right)$ are 2.5 m/s and 8 m/s, respectively. In this case, the two vehicles arrive at the conflict point almost at the same time if neglecting the interaction between them. As we expected, the vehicle with the lower $\beta_{4 i}$ (concerning less on safety cost) crosses the conflict point first. Therefore, the $\beta_{4 i}$ can indicate the priority of the vehicle or the aggressiveness of the driver. The lower $\beta_{4 i^{\prime}}$ the more aggressive the driver is.
3.2.2. Merging Maneuver. A symmetric merging scenario is used. There are two vehicles A and B. Vehicle A drives from $\left(x_{0 \mathrm{~A}}, y_{0 \mathrm{~A}}\right)=(0,0) \mathrm{m}$ to $\left(x_{f \mathrm{~A}}, y_{f \mathrm{~A}}\right)=(10,15) \mathrm{m}$. Its initial heading angle $\left(\theta_{0 \mathrm{~A}}\right)$ is 0 rad, initial velocity $\left(v_{0 \mathrm{~A}}\right)$ is 8 m/s, and terminal heading angle $\left(\theta_{f \mathrm{~A}}\right)$ is $\pi / 2$ rad. Vehicle B drives from $\left(x_{0 \mathrm{~B}}, y_{0 \mathrm{~B}}\right)=(20,0) \mathrm{m}$ to $\left(x_{f \mathrm{~B}}\right.$, $\left.y_{f \mathrm{~B}}\right)=(10,15) \mathrm{m}$. Its initial heading angle $\left(\theta_{0 \mathrm{~B}}\right)$ is $\pi \mathrm{rad}$, initial velocity $\left(v_{0 \mathrm{~B}}\right)$ is 8 m/s, and terminal heading angle $\left(\theta_{f \mathrm{~B}}\right)$ is $\pi / 2 \mathrm{rad}$. The weights of the travel time cost $\left(\beta_{1}\right)$, turning cost $\left(\beta_{2}\right)$, and acceleration cost $\left(\beta_{3}\right)$ are set to be 1, $0.01 \mathrm{~s}^{5} / \mathrm{m}^{3}$, and $0.01 \mathrm{~s}^{5} / \mathrm{m}^{3}$, respectively, for both vehicles. The weights of the safety cost of two vehicles are changed from $0.01 \mathrm{~s}^{2} / \mathrm{m}$ to $10 \mathrm{~s}^{2} / \mathrm{m}$. The other parameters remain the same.

The path pairs (each pair using the same color) under various $\beta_{4}$ are shown in Figure 7(a). The solid lines are those with the constant weight of the safety cost of vehicle $\mathrm{B}\left(\beta_{4 \mathrm{~B}}=1 \mathrm{~s}^{2} / \mathrm{m}\right)$, whereas the dotted lines are those with the constant weight of the safety cost of vehicle A $\left(\beta_{4 \mathrm{~A}}=1 \mathrm{~s}^{2} / \mathrm{m}\right)$. In other words, the $\beta_{4}$ for vehicles A and B are switched between solid lines and dotted lines. One can find that the paths are symmetric when the weights of the safety cost are symmetric, for example, the solid line under $\beta_{4 \mathrm{~A}}=0.01 \mathrm{~s}^{2} / \mathrm{m}$ and $\beta_{4 \mathrm{~B}}=1 \mathrm{~s}^{2} / \mathrm{m}$ versus the dotted line under $\beta_{4 \mathrm{~A}}=$ $1 \mathrm{~s}^{2} / \mathrm{m}$ and $\beta_{4 \mathrm{~B}}=0.01 \mathrm{~s}^{2} / \mathrm{m}$. This symmetric phenomenon can be further confirmed by Figure 7(b). The velocity curves are overlapped with each other when the weights of the safety cost are symmetric.

Figure 4. (Color online) Trajectories with Various Number of Vehicles
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-10.jpg?height=478&width=1470&top_left_y=2022&top_left_x=280)

Figure 5. (Color online) Trajectory Analysis for Crossing Maneuver
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-11.jpg?height=565&width=1362&top_left_y=293&top_left_x=334)

Notes. (a) Path. (b) Velocity.

Moreover, the order of vehicles passing the conflict point switches under different initial states and driving behaviors of conflicting vehicles, as shown in Figure 8. The weights of the costs are constant in Figure 8(a), whereas the initial velocities are constant in Figure 8(b). As expected, the order of vehicles passing the conflict point is also symmetric.
3.2.3. Car-Following Maneuver. The two vehicles A and B are considered. Vehicle A drives from ( $x_{0 \mathrm{~A}}$, $\left.y_{0 \mathrm{~A}}\right)=(0,0) \mathrm{m}$ to $\left(x_{f \mathrm{~A}}, y_{f \mathrm{~A}}\right)=(15,15) \mathrm{m}$. Its initial heading angle $\left(\theta_{0 \mathrm{~A}}\right)$ is 0 rad, initial velocity $\left(v_{0 \mathrm{~A}}\right)$ is 8 m/s, and terminal heading angle $\left(\theta_{f \mathrm{~A}}\right)$ is $\pi / 2$ rad. Vehicle B drives from $\left(x_{0 \mathrm{~B}}, y_{0 \mathrm{~B}}\right)=(-5,0) \mathrm{m}$ to $\left(x_{f \mathrm{~B}}, y_{f \mathrm{~B}}\right)=(15$, 15) m. Its initial heading angle ( $\theta_{0 \mathrm{~B}}$ ) is 0 rad, initial velocity $\left(v_{0 \mathrm{~B}}\right)$ is 8 m/s, and terminal heading angle $\left(\theta_{f \mathrm{~B}}\right)$ is $\pi / 2 \mathrm{rad}$. The weight of the safety cost of vehicle $\mathrm{B}\left(\beta_{4 \mathrm{~B}}\right)$ is changed in the range of $0.01 \mathrm{~s}^{2} / \mathrm{m}$ and $10 \mathrm{~s}^{2} / \mathrm{m}$, whereas the safety cost of vehicle $\mathrm{A}\left(\beta_{4 \mathrm{~A}}\right)$ is constant to be $0.01 \mathrm{~s}^{2} / \mathrm{m}$. The other parameters remain the same. The path $(x, y)$ and the velocity $(v)$ are analyzed, as illustrated in Figure 9. Vehicle B adjusts its trajectory under various safety costs. However, the change is slighter than the change for the crossing maneuver. It can be understood because human drivers do not adjust their paths too much under the car-following scenario. They rely mainly on speed adjustment to maintain safety.

## 4. Validation Methodology

Apart from the model formulation, validation is essential to ensure the quality of the model. Up to now, a generic methodology to microscopically validate a model describing interactions between vehicles is lacking. Therefore, this paper develops so in this section. We first present existing methods for validation (Section 4.1) and then propose a generic methodology for validating models with interacting vehicles (Section 4.2). The tailored validation method for the current model and the results are presented in Section 5.

Figure 6. Crossing Order Analysis
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-11.jpg?height=593&width=1190&top_left_y=1912&top_left_x=421)

Figure 7. (Color online) Trajectory Analysis for Merging Maneuver
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-12.jpg?height=559&width=1360&top_left_y=293&top_left_x=336)

Notes. (a) Path. (b) Velocity.

### 4.1. Existing Validation Techniques

The traditional procedure to validate a traffic flow model contains two steps: first, the model parameters are calibrated using the collected field data (i.e., find the best fitting parameters), and then the quality of the model with these parameters is tested on another data set, which is the validation step (Treiber and Kesting 2012, Daamen, Buisson, and Hoogendoorn 2014, Spiliopoulou et al. 2014, Treiber and Kesting 2014, Punzo and Montanino 2016, Jin et al. 2018, Mariotte et al. 2020). In calibration and validation, the macroscopic performance indicators are commonly used to measure the overall performance of the system, such as the traffic flow (Xie, Nie, and Liu 2017, Tang et al. 2020), flow rate (Jiang et al. 2017, Yuan, Knoop, and Hoogendoorn 2017), speed (Chiu, Zhou, and Song 2010, Tian et al. 2017), density (Ma, Dong, and Zhang 2007, Sayegh, Connors, and Tate 2018), queue length (Zhang et al. 2020), travel times (Hollander and Liu 2008), and their combinations (Kim and Mahmassani 2011, Ni et al. 2016, Han et al. 2017, Kontorinaki et al. 2017, Spiliopoulou et al. 2017). One may notice that, although calibration of the model can involve finding individual vehicle parameters (Treiber and Kesting 2013), in validation often aggregate variables are used (Treiber and Kesting 2012).

In our earlier 2020 model (Zhao, Knoop, and Wang 2020), the traditional validation technique mentioned previously is used. In this study, the proposed model describing microscopic properties (trajectories) of vehicles is a stochastic model, in which the parameters representing the driving behavior are stochastic. The calibrated parameter set can be obtained by empirical data collection. However, the validation is an issue for stochastic models. Selecting a random set of parameters for each vehicle will hence most likely provide a wrong set of trajectories, but this is indeed not the goal of the model. Trying the best of all trajectories,

Figure 8. Merging Order Analysis
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-12.jpg?height=608&width=1187&top_left_y=1886&top_left_x=421)

Figure 9. (Color online) Trajectory Analysis for Car-Following Maneuver
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-13.jpg?height=565&width=1360&top_left_y=293&top_left_x=336)

Notes. (a) Path. (b) Velocity.
which is the method used in our previous study (Zhao, Knoop, and Wang 2020), involves a second calibration and will overestimate the quality of the model. Therefore, it is essential to propose a new generic validation method for models with interacting vehicles.

### 4.2 Clustered Validation Method

In this paper, we propose a three-step approach to validation that accounts for interdriver variations. The essential step in this is to cluster drivers into various distinct groups. The method basically entails creating representative drivers from the calibration and testing whether any of the representative drivers fit the observed validation data set. The process contains three steps: model calibration, parameter clustering, and model validation, which is as follows. Please note that this is a generic methodology for validating models. It is suitable for models with interacting vehicles, but also single-vehicle models.

The first step is to set the goal for the calibration. This should be a microscopic goal, for instance, the difference between the predicted and measured trajectory, or individual speeds. Then, the model should be calibrated for each individual vehicle or vehicle pair. This step will yield a set of optimized parameters for each driver/vehicle.

The second step is to cluster the parameters from the results of the calibration to create representative drivers. It is the key step in the proposed validation method. Different parameter values reflect the interdriver variations. Although various drivers have different driving behavior, they can be grouped into several styles, such as aggressive, moderate, and conservative (van Erp, Knoop, and Hoogendoorn 2017, Li, Wang, and Roetting 2018, Huang et al. 2019). The clustering techniques, such as the K-means clustering technique, can be used applied for this.

The third step is to validate the model by checking how well the model fits the observed validation data set using the parameters of one of these representative drivers. In this way, we can identify how well the model works when considering a limited number of driving styles instead of considering the driving behavior of each driver as an independent case. In an example of a case with five classes, the trajectory is simulated five times, and the best is chosen. The rationale is that the observed driver can be of any class, and we do not know which. However, once put into the class, the result should be accurate. If the model describes interacting vehicles, the number of possible cases increase. For instance, the model we have at hand describes the actions between two interacting vehicles. That means that we should have both drivers into the correct class, which means (in the case of five classes) trying out all 5 × 5 classes for combinations of types of drivers. Then, the best of these combinations is chosen. Again, the rationale is that we aim to check whether the predicted movement is correct once we know the class a driver belongs to.

This is a generic methodology for validating models with stochastic behavior. However, the limitations lie in that it is a data-dependent method. First, enough data should be collected for the calibration to ensure the parameters from the results of the calibration can reflect the overall distribution of driver behavior. Second, representative drivers should be rightly created in the clustering step to establish a good foundation for the validation. The K-means clustering technique we used has some known drawbacks, such as the determination of K and not performing well if the initial centroids of the groups are significantly different from the actual ones. It should be carefully checked in actual clustering. The elbow method and the visual check of the sample distribution can be used to relieve these issues (Thorndike 1953, Aldenderfer and Blashfield
1984). Although we propose using a K-means clustering technique in the study, alternative clustering techniques would also be suitable.

## 5. Model Performance on Real-World Data

The proposed model is validated using empirical data in this section. Section 5.1 first presents the tailored validation method for the proposed model. Then, the validation process is presented in this order: Section 5.2, empirical data; Section 5.3, parameter calibration; Section 5.4, the clustering; and Section 5.5, the validation results.

### 5.1. Validation and Calibration: Choices and Implementation

This section will explain how the validation method is applied to the model formulated in Section 4. The model has four parameters per vehicle/driver, which we will denote as $\boldsymbol{\beta}_{i}=\left\{\beta_{1 i^{\prime}}, \beta_{2 i^{\prime}}, \beta_{3 i^{\prime}}, \beta_{4 i}\right\}$. Because the cost can, in principle, be scaled up or down with an arbitrary factor, we can use this to reduce the degrees of freedom in the parameter calibration. In our approach, we choose to let $\beta_{4 i}$ a degree of freedom be calibrated. This allows fixing $\beta_{1 i}$. Alternatively, we could have fixed $\beta_{4 i}$ to one (i.e., it disappears) and let $\beta_{1 i}$ to $\beta_{3 i}$ vary. We choose to make $\beta_{4 i}$ a variable to explicitly show that drivers might have a different attitude toward each other, and give all drivers a fixed $\beta_{1 i}$ in line with our previous paper. For validation and calibration, the most accurate parameter calibration for multivehicle combination is to set only one parameter as one. Then, there are seven parameters to be calibrated for the combination of an interacting vehicle pair. However, it is meaningless to obtain the parameter combination of interacting vehicles because any vehicles with different driving behaviors may be combined in practice. It is more meaningful to calibrate the driving behavior parameters of each vehicle, which is conducive to the application of the model. Therefore, $\beta_{1 i}$ is set to one. The actual number of parameters to be calibrated for each vehicle is three. Hence, for each pair of interacting vehicles, we have six parameters to calibrate: $\mathbf{B}=\left\{\boldsymbol{\beta}_{\mathbf{A}}, \boldsymbol{\beta}_{\mathbf{B}}\right\}=\left\{\beta_{2 \mathbf{A}^{\prime}}, \beta_{3 \mathrm{~A}^{\prime}}\right.$ $\left.\beta_{4 \mathrm{~A}}, \beta_{2 \mathrm{~B}}, \beta_{3 \mathrm{~B}}, \beta_{4 \mathrm{~B}}\right\}$. Note that B indicates the combination of parameters of both drivers. The number of parameters, six, is a reasonable number for which an optimum can be found. Along the same line as the method proposed in Section 4.2, the specific validation method for the current model is shown as follows.

First, parameters in the proposed model $\left(\boldsymbol{\beta}_{\boldsymbol{i}}\right)$ are calibrated via an optimization program. The decision variables of the optimization model for calibration are the weights of costs of the two interacting vehicles $\left(\mathbf{B}=\left\{\boldsymbol{\beta}_{\mathrm{A}}, \boldsymbol{\beta}_{\mathrm{B}}\right\}\right)$. The objective of the optimization model for calibration is to minimize RMSE of the Euclidean distance between the planned trajectory and the real trajectory at all time steps, as shown in Equation (23). The Euclidean distance at each time step is the trajectory error between the planned trajectory and the real trajectory, as shown in Equation (24). The trajectory error is spatiotemporal. It includes the error in space and the error in speed because we compare the positions at the same timestamp pairwise:

$$
\mathbf{B}^{*}=\arg \min _{\mathbf{B}}\left(\mathrm{RMSE}_{d}\right)=\arg \min _{\mathbf{B}} \sqrt{\frac{\sum_{t=1}^{n} d_{t}^{2}}{n}},
$$

where $d$ denotes the Euclidean distance between the planned trajectory and the real trajectory, in meters; RMSE $_{d}$ denotes the root-mean-square error of $d$, in meters; $d_{t}$ denotes the Euclidean distance between the planned trajectory and the real trajectory at timestamp $t$, in meters; and $n$ is the total number of timestamps:

$$
d_{t}=\sqrt{\left(x_{t}^{p}-x_{t}^{r}\right)^{2}+\left(y_{t}^{p}-y_{t}^{r}\right)^{2}},
$$

where $\left(x_{t}^{p}, y_{t}^{p}\right)$ is the coordinates of the planned trajectory at timestamp $t$; and $\left(x_{t}^{r}, y_{t}^{r}\right)$ is the coordinates of the real trajectory at timestamp $t$.

Second, the calibrated $\boldsymbol{\beta}_{\boldsymbol{i}}$ for individual drivers are clustered into a discrete number of clusters. The K-means clustering algorithm is used (Han, Pei, and Kamber 2011). The estimation error (RMSE) of each vehicle pair can be calculated using the clustered $\boldsymbol{\beta}_{i}$. Please note there is a tradeoff between number of clusters and performance. Increasing the number of clusters (K) will decrease the estimation error but increase the computational cost in the following validation step. To find the optimal K, the change tendency (curve) of the mean RMSE of these vehicle pairs against K can be explored. The optimal K can be selected by searching for a kink in the curve.

Third, the planned trajectories using the clustered $\boldsymbol{\beta}_{i}$ are compared with the observed ones. Similar to calibration, we also use the RMSE of the Euclidean distance between the planned trajectory and the real trajectory as the comparison metrics. We can find the optimal combination with the lowest RMSE and check whether it fits well. Also, we will consider whether the model will correctly describe the order of crossing for the crossing vehicles.

### 5.2. Empirical Data

The data used in this section are collected at six intersections in Shanghai, China, by the unmanned aerial vehicle, as shown in Figure 10. The real vehicular trajectory can be obtained by extracting the position of each vehicle at each frame using a specially developed video recognition software. The geometric centre of the vehicle is collected to compute the distances/velocities/angles because all the videos are photographed from above.

Figure 10. (Color online) Surveyed Intersections
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-15.jpg?height=1604&width=1476&top_left_y=293&top_left_x=274)

Notes. Intersections in the calibration data set: (a) Zhangyang Road-Gushan Road and (b) Gaokezhong Road-ZhangDong Road. Intersections in the validation data set: (c) Yushan Road-Nanyangjing Road, (d) Yangtai Road-Zhentai Road, (e) Zuchongzhi Road-Gaosi Road, and (f) Youyi Road-Tieli Road.

The time resolution is 1/24 seconds. The average measurement error associated with the extraction process is 0.2 m.

The interacting vehicle pairs were selected for the hereafter analysis, for example, the through vehicle and the opposing left-turn vehicle pairs under the permitted left-turn phase. The data selection criterion are that the direct interaction vehicle pairs, that is, the two vehicles passing the conflict area successively, are selected to avoid the confusion of the choice of the interacting vehicles. The surveyed data were divided into two nonoverlapping sets. Thirty vehicle pairs collected from three intersections are used for model calibration (calibration data set), whereas 30 vehicle pairs collected from another three intersections are used for model validation (validation data set).

### 5.3. Calibration Results

For model calibration, 30 vehicle pairs are calibrated, including crossing, merging, and car-following maneuvers. The results of model calibration show that the mean, maximum, and minimum RMSE of trajectory

Figure 11. Cumulative Probability Curve of Parameters of the Calibrated Vehicles
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-16.jpg?height=414&width=1606&top_left_y=291&top_left_x=212)

are 1.049, 2.235, and 0.206 meters, respectively. It indicates the distance between the planned trajectory and the real trajectory at each timestamp is approximately 1 meter.

Moreover, the running orders of interacting vehicle pairs are also checked. They are all correctly estimated in all the crossing and merging cases. Therefore, the interaction between manual driving vehicles at intersections can be well represented by the proposed model. With the consideration of the computational time and to prevent the algorithm from falling into local minima with unreasonable values (Kim and Mahmassani 2011), the boundary of $\boldsymbol{\beta}_{i}$ is set to be [0.001,1] based on calibration results from our previous work (Zhao, Knoop, and Wang 2020). The distributions of the parameter values are shown in Figure 11. The parameters $\beta_{2}, \beta_{3}$, and $\beta_{4}$ obey the exponential distribution $\left(\mathrm{R}^{2}=0.876\right)$, exponential distribution $\left(\mathrm{R}^{2}=0.935\right)$, and uniform distribution $\left(\mathrm{R}^{2}=0.964\right)$, respectively. The Pearson correlation test is conducted to test the correlations between the three parameters. The results are shown in Table 3. The correlations of $\beta_{2}-\beta_{3}$ and $\beta_{2}-\beta_{4}$ are significant. It indicates that drivers concerned more about vehicular lateral acceleration are likely to be more concerned about longitudinal acceleration and traffic safety.

### 5.4. Clustering Results

For the parameter clustering, the calibrated $\boldsymbol{\beta}_{\boldsymbol{i}}$ is clustered into several classes. The K-means cluster analysis tool in SPSS is used. The maximum iterations number is set to be 20. The convergence criterion is set to be zero. We enumerate the cluster numbers from 2 to 10. The change tendency of the mean RMSE of trajectory as a function of the number of clusters (K) is

Table 3. Correlation Test
| Test statistics | $\beta_{2}-\beta_{3}$ | $\beta_{2}-\beta_{4}$ | $\beta_{3}-\beta_{4}$ |
| :--- | :--- | :--- | :--- |
| Correlation coefficient | $0.384{ }^{\text {a }}$ | $-0.320^{\mathrm{b}}$ | -0.186 |
| Significance | 0.002 | 0.013 | 0.154 |


[^0]shown in Figure 12. One can find that the curve flattens after the number of clusters, K, equals five. According to the elbow method, the calibrated $\boldsymbol{\beta}_{\boldsymbol{i}}$ is clustered into five classes, which can be regarded as five representative driver types. The standard parameter values for the vehicles per cluster are shown in Table 4. The cumulative probability curves of the parameters for the vehicles in each cluster are compared, as illustrated in Figure 13.

Let us consider the classification of the drivers in each of the classes, and the behavioral interpretation thereof. Figure 13 shows the distribution of parameter values for each of the classes. The parameters obey the uniform distribution $\left(\mathrm{R}^{2} \in[0.807,0.974]\right.$, average $\left.\mathrm{R}^{2}=0.908\right)$ within the same cluster. The drivers in cluster 1 have low values of $\beta_{2}$, low values of $\beta_{3}$, but high values of $\beta_{4}$. They care much more about safety than turning and acceleration costs. The drivers in cluster 2 have a high $\beta_{2}$, high $\beta_{3}$, and medium $\beta_{4}$. They care more about turning and acceleration comfort. The drivers in cluster 3 have a medium $\beta_{2}$, high $\beta_{3}$, and high $\beta_{4}$. They care more about safety and acceleration comfort comparing to turning comfort. The drivers in cluster 4 have a high $\beta_{2}$, low $\beta_{3}$, and low $\beta_{4}$. Opposite to cluster 3, they care more about turning comfort than safety and acceleration comfort.

Figure 12. Mean RMSE vs. Number of Clusters
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-16.jpg?height=497&width=765&top_left_y=2060&top_left_x=1075)

Table 4. Results of Parameter Clustering
| Clusters | Cluster center |  |  | Proportion |
| :--- | :--- | :--- | :--- | :--- |
|  | $\beta_{2}, \mathrm{~s}^{5} / \mathrm{m}^{3}$ | $\beta_{3}, \mathrm{~s}^{5} / \mathrm{m}^{3}$ | $\beta_{4}, \mathrm{~s}^{2} / \mathrm{m}$ |  |
| 1 | 0.085 | 0.093 | 0.790 | 35.00\% |
| 2 | 0.869 | 0.824 | 0.309 | 16.67\% |
| 3 | 0.437 | 0.751 | 0.689 | 11.67\% |
| 4 | 0.906 | 0.134 | 0.229 | 15.00\% |
| 5 | 0.103 | 0.294 | 0.094 | 21.66\% |


The drivers in cluster 5 have a low $\beta_{2}$, medium $\beta_{3}$, and low $\beta_{4}$. They mainly care about travel time.

Whether the cluster that a vehicle belongs to is the most suitable one is further checked. In the clustering method mentioned previously, the two vehicles in a vehicle pair have been assigned to a cluster, after which the values of the cluster have been determined. It could be identified whether this is indeed the best combination or there is a better one if we try all 25 possible combinations. For 49 of the 60 vehicles (82\%), there is no better cluster available.

We also check by much of the goodness of fit reduces due to the clustering. This information is useful when assessing the quality of the validation later. First, by clustering, the mean RMSE goes up from 1.049 to 1.735 meters, increasing by 0.686 meters. This can be reduced by freely choosing a cluster; in RMSE, it reduces by 1.735 to 1.585 meters by selecting the optimal cluster. The comparison of the performance (RMSE) of the calibration, clustered calibration, and best cluster are shown in Figure 14 (the first, second, and third bar, respectively). The figure splits the results for the various situations (crossing, merging, and car-following); they are similar. As expected, the performance of the planned trajectories is better if the values are fully free to be optimized. However, the performance loss by putting them into a cluster is limited, and the results are still very good for trajectory planning.

Figure 14. Comparison of RMSE of Calibration and Validation Data Sets
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-17.jpg?height=841&width=850&top_left_y=338&top_left_x=1037)

### 5.5. Validation Results

According to the five driver types created in Section 5.4, we can validate the proposed model using these representative drivers' parameters. Thirty vehicle pairs are used for model validation. The results of the model validation show a mean RMSE of 1.453 meters, using vehicle classes from the cluster (Table 4). As illustrated in Figure 14, the mean RMSE of the validation data set (the fourth bar) is comparable to the result of the calibration data set (the third bar). Also, a visual inspection of the trajectories (Figure 15) shows that trajectories in validation are almost as close as in calibration, and both are close to the real-world trajectory. It indicates the proposed model can describe the trajectories of interacting vehicles with the mean

Figure 13. (Color online) Cumulative Probability Curves of Parameters for Various Clusters
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-17.jpg?height=491&width=1600&top_left_y=2035&top_left_x=217)

Figure 15. (Color online) Examples of the Trajectories of the Vehicle Pairs
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-18.jpg?height=1553&width=1483&top_left_y=289&top_left_x=276)

trajectory error of 1.5 meters using the parameters of the five representative driver types.

We believe errors in the order of 1.5 meters is acceptable. The reasons are threefold. (1) The proposed model is a traffic flow model instead of a short time trajectory prediction model. The full trajectories of the interacting vehicles passing through the intersection are described by only giving the initial and terminal states. Considering drivers can choose among an infinite number of alternative travelling paths and speeds and the complex interacting effects between vehicles, the speed change will lead to a meter off easily at a specific time (about five seconds to pass an intersection). Because the positions at the same time are compared, a one-second delay at the same path will yield a 10-meter error under the speed of 10 m/s; 1.5 meters off is hence good. (2) Only four parameters and five representative driver types are used for each vehicle. It ensures that the proposed model is not too complex for the traffic flow analysis. (3) The running orders of interacting vehicle pairs are all correctly given in all the crossing and merging cases. It is important for the traffic flow analysis of conflicting vehicles. This means that overall, the proposed model performs very well in describing vehicle movements in the inner area of an intersection.

We also tried the modeling method that the vehicle only considers its own cost (i.e., noncooperative behavior). The objective function turns (Equation (15)) to be $\min _{\mathbf{U}}\left(\int_{0}^{1} L_{i} s_{f i} \mathrm{~d} \zeta\right)$. Other formulations remain the same. The full trajectories of conflicting vehicles can be generated by repeating trajectory planning
alternately considering the changing state of conflicting vehicles. The mean RMSE of the noncooperative model reaches 2.1 meters using the same 30 vehicle pairs, which is 40\% higher than that of the proposed cooperative model. This implies that drivers account for the cost of other drivers as well, and the weights associated with the interaction cost reflect how selfish or considerate drivers are.

To use the model in assessing a road design, the clustering method is not needed per se. First, numerous real vehicular trajectories can be collected to find the distribution of the parameters $\left(\boldsymbol{\beta}_{i}\right)$. Then, the model can be run where vehicles are generated based on the distributions of the parameters. Because this process is stochastic, the model should be run many times, each time with another parameter set $\boldsymbol{\beta}_{\boldsymbol{i}}$ for each of the vehicles.

### 5.6. Macroscopic Analysis Extension

Although the main function of the proposed model is to describe the microscopic trajectories of vehicles, the macroscopic traffic performance can be evaluated through simulation. Because the full trajectories of conflicting vehicles can be obtained according to the proposed model, we can get the travel times and delays of vehicles. Here, we perform a sensitivity analysis to explore the relationship between delay and traffic flow for the left turn and through conflict. The drivers' parameters of vehicles are randomly assigned using the five driver types and their proportion created in Section 5.4. The desired speeds of the left turn and through vehicles are set to be 20 and 30 km/h, respectively.

We first test the traffic flow scenario at the six surveyed intersections. The arrival times of vehicles are set to be the same as the empirical data. The delay of the left turn and through movement are calculated and compared with the empirical data, as shown in Table 5. Only the delay caused by the conflicting vehicles is included. One can find that the model results are in accord with the measured ones. The absolute error for each left turn and through conflict pair is no more than 4 s/vehicle. The result of the paired-samples $t$ test shows that there is no significant difference between the calculated and the measured results (significance $=0.649>0.05$ ).

Then, we performed a sensitivity analysis to explore the relationship between delay and traffic flow for the left turn and through conflict with various traffic volume and left-turn proportion conditions. Vehicle arrival adopts Poisson distribution. The total traffic volume changes from 100 to 2,000 vehicles/h, whereas the proportion of left-turn traffic volume changes from 10\% to 50\%. Figure 16 shows the results. In general, the growth rate of the vehicular delay increases with the increase of the volume and the left-turn (LT) proportion. When the volume is low (under 500 vehicles/h), the increase of the vehicular delay is flat, and the vehicular delay is not more than 5 s/vehicles. It is because the conflict of the left turn and through movement rarely happened and can almost be ignored. The vehicular delay reaches 30 s/vehicle when the volume reaches 1,450,1,150, and

Table 5. Comparison of Vehicular Delay
| Intersection | Conflicting pair | Traffic volume (vehicles/h) | Left-turn proportion | Measured delay (s/vehicle) | Model predicted delay (s/vehicle) | Absolute error (s/vehicle) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Zhangyang Road- | SBLT-NBTH | 176 | 44.83\% | 3.09 | 1.83 | 1.26 |
| Gushan Road | NBLT-SBTH | 103 | 31.03\% | 4.00 | 1.39 | 2.61 |
| Gaokezhong Road- | WBLT-EBTH | 407 | 34.43\% | 2.01 | 2.92 | 0.91 |
| ZhangDong Road | EBLT-WBTH | 760 | 23.68\% | 7.61 | 5.73 | 1.88 |
| Yushan Road- | SBLT-NBTH | 187 | 36.36\% | 3.43 | 1.76 | 1.67 |
| Nanyangjing | NBLT-SBTH | 263 | 19.35\% | 2.81 | 1.75 | 1.06 |
| Road | EBLT-WBTH | 391 | 15.22\% | 0.86 | 2.10 | 1.24 |
|  | WBLT-EBTH | 340 | 20.00\% | 2.30 | 2.05 | 0.26 |
| Yangtai Road- | EBLT-WBTH | 243 | 3.45\% | 0.47 | 1.41 | 0.95 |
| Zhentai Road | WBLT-EBTH | 243 | 48.28\% | 2.59 | 2.25 | 0.33 |
|  | NBLT-SBTH | 503 | 43.33\% | 1.06 | 4.25 | 3.19 |
|  | SBLT-NBTH | 461 | 45.45\% | 1.71 | 3.90 | 2.19 |
| Zuchongzhi Road- | NBLT-SBTH | 250 | 65.38\% | 0.62 | 2.65 | 2.03 |
| Gaosi Road | SBLT-NBTH | 337 | 22.86\% | 0.33 | 2.12 | 1.79 |
| Youyi Road-Tieli | NBLT-SBTH | 141 | 12.50\% | 0.53 | 1.32 | 0.79 |
| Road | SBLT-NBTH | 188 | 87.50\% | 3.41 | 2.52 | 0.90 |
| Average |  |  |  |  |  | 1.44 |
| Maximum |  |  |  |  |  | 3.19 |
| Minimum |  |  |  |  |  | 0.26 |


[^1]Figure 16. (Color online) Relationship Between Vehicular Delay and Traffic Flow
![](https://cdn.mathpix.com/cropped/906ce480-3e98-4ade-80a9-0a74233d5a31-20.jpg?height=580&width=845&top_left_y=334&top_left_x=153)

1,050 under the LT proportion of 10\%, 30\%, and 50\%, respectively.

## 6. Discussion and Conclusions

This study proposes a 2D traffic flow model to describe vehicle maneuvers of human-driven vehicles inside intersections. The travel time cost, turning cost, acceleration cost, and safety cost are considered in the proposed model. The activity of a driver is a tradeoff between the utilities of time, comfort, and safety. The model performs well in describing the observed vehicle trajectories in reality. Besides the accurate trajectories, it also predicts the order of crossing vehicles correctly. With the model, the traffic flow at intersections can be simulated more realistically, which is important for the geometric design, signal control, and traffic management at intersections.

The model prescribes costs for vehicles being close to each other. The model gives a good result (mean trajectory error is 1.5 meters) if the trajectories of interacting vehicles are jointly planned, that is, if one driver accounts for the cost of the other vehicle during its trajectory planning.

The model has a set of parameters for each driver/ vehicle combination. The paper presents a generic "calibration-clustering-validation" methodological for validating models with interacting vehicles. Its basis is to create classes of vehicles/drivers with the same behavior. The method can be used to classify behavior and is essential for the microscopic validation of models with stochastic behavior.

Regarding further research, the current paper identified five different vehicle/driver classes. It remains interesting to see whether similar groups of behavior can be identified in other driver models in future research. That can even be the case with a completely different model and different mathematical description, but the driver types might be similar. Moreover, to reflect the uncertainties of drivers' decisions, random parameters can be added when setting the cost weight parameters. Then, the probability distribution of the vehicle trajectories can be obtained through multiple trajectory planning. Another direction for future research is to represent/simulate the operational condition of the entire inner area of the intersection, in which the criteria of choice of interacting vehicles should be one of the critical factors.

## References

Ahn S, Cassidy MJ, Laval J (2004) Verification of a simplified carfollowing theory. Transportation Res. Part B: Methodological 38(5): 431-440.
Aldenderfer MS, Blashfield RK (1984) Cluster Analysis (SAGE Publications, Newbury Park, CA).
Ali Y, Zheng Z, Haque MM, Wang M (2019) A game theory-based approach for modeling mandatory lane-changing behavior in a connected environment. Transportation Res., Part C Emerging Tech. 106:220-242.
Andersson JA, Gillis J, Horn G, Rawlings JB, Diehl M (2019) Casadi: A software framework for nonlinear optimization and optimal control. Math. Programming Comput. 11(1):1-36.
Anvari B, Bell MG, Sivakumar A, Ochieng WY (2015) Modeling shared space users via rule-based social force model. Transportation Res., Part C Emerging Techn. 51:83-103.
Anvari B, Daamen W, Knoop VL, Hoogendoorn SP, Bell MG (2014) Shared space modeling based on social forces and distance potential field. Pedestrian Evacuation Dynamics 2012:907-916.
Bichiou Y, Rakha HA (2018) Developing an optimal intersection control system for automated connected vehicles. IEEE Trans. Intelligent Transportation Systems 20(5):1908-1916.
Bichiou Y, Rakha HA (2019) Real-time optimal intersection control system for automated/cooperative vehicles. Internat. J. Transportation Sci. Tech. 8(1):1-12.
Chai C, Wong Y (2014) Micro-simulation of vehicle conflicts involving right-turn vehicles at signalized intersections based on cellular automata. Accident Anal. Prevention 63:94-103.
Chai C, Wong YD (2015) Fuzzy cellular automata model for signalized intersections. Comput. Aided Civil Infrastructure Engrg. 30(12):951-964.
Chiu YC, Zhou L, Song H (2010) Development and calibration of the anisotropic mesoscopic simulation model for uninterrupted flow facilities. Transportation Res. Part B: Methodological 44(1):152-174.
Daamen W, Buisson C, Hoogendoorn SP (2014) Traffic Simulation and Data: Validation Methods and Applications (CRC Press, Boca Raton, FL).
Fellendorf M, Schönauer R, Huang W (2012) Social force-based vehicle model for two-dimensional spaces. Proc. Transportation Res. Board 91st Annual Meeting (Transportation Research Board, Washington, DC), 1-16. https://trid.trb.org/Results?txt Keywords=Social\%20force-based\%20vehicle\%20model\%20for \%20two-dimensional\%20spaces\&txtTitle=Social\%20forcebased\%20vehicle\%20model\%20for\%20two-dimensional\%20spaces \&txtSerial=\&ddlSubject=\&txtReportNum=\&ddITrisfile=\&txtIndex =\&specificTerms=\&txtAgency=\&sourceagency=\&txtAuthor=\& ddlResultType=\&chkFulltextOnly=0\&recordLanguage=\&subject Logic=and\&termsLogic=or\&dateStart=\&dateEnd=\&rangeType= publisheddate\&sortBy=\&sortOrder=DESC\&rpp=25\#/View/ 1129193.
Foulaadvand ME, Belbasi S (2007) Vehicular traffic flow at a nonsignalised intersection. J. Phys. A 40(29):8289-8297.
Hamdar SH, Mahmassani HS, Treiber M (2015) From behavioral psychology to acceleration modeling: Calibration, validation, and exploration of drivers' cognitive and safety parameters in a
risk-taking environment. Transportation Res. Part B: Methodological 78:32-53.
Hamdar SH, Dixit VV, Talebpour A, Treiber M (2020) A behavioral microeconomic foundation for car-following models. Transportation Res., Part C Emerging Tech. 113:228-244.
Han J, Pei J, Kamber M (2011) Data Mining: Concepts and Techniques (Elsevier, Waltham, MA).
Han Y, Hegyi A, Yuan Y, Hoogendoorn S (2017) Validation of an extended discrete first-order model with variable speed limits. Transportation Res., Part C Emerging Tech. 83:1-17.
Helbing D, Buzna L, Johansson A, Werner T (2005) Self-organized pedestrian crowd dynamics: Experiments, simulations, and design solutions. Transportation Sci. 39(1):1-24.
Hollander Y, Liu R (2008) Estimation of the distribution of travel times by repeated simulation. Transporation Res., Part C Emerging Tech. 16(2):212-231.
Hoogendoorn SP, Bovy PH (2004) Pedestrian route-choice and activity scheduling theory and models. Transportation Res. Part B: Methodological 38(2):169-190.
Hoogendoorn R, van Arerm B, Hoogendoom S (2014) Automated driving, traffic flow efficiency, and human factors: Literature review. Transportation Res. Record 2422(1):113-120.
Hoogendoorn S, Hoogendoorn R, Wang M, Daamen W (2012) Modeling driver, driver support, and cooperative systems with dynamic optimal control. Transportation Res. Record 2316(1):20-30.
Huang L, Wu J, You F, Lv Z, Song H (2016) Cyclist social force model at unsignalized intersections with heterogeneous traffic. IEEE Trans. Industrial Inform. 13(2):782-792.
Huang Y, Wang H, Khajepour A, Ding H, Yuan K, Qin Y (2019) A novel local motion planning framework for autonomous vehicles based on resistance network and model predictive control. IEEE Trans. Vehicular Tech. 69(1):55-66.
Huynh DN, Boltze M, Vu AT (2013) Modeling mixed traffic flow at signalized intersectionusing social force model. J. Eastern Asia Soc. Transportation Stud. 10:1734-1749.
Jiang R, Hu M, Wu Q, Song W (2017) Traffic dynamics of bicycle flow: Experiment and modeling. Transportation Sci. 51(3):998-1008.
Jiang R, Hu M, Zhang H, Gao Z, Jia B, Wu Q (2015) On some experimental features of car-following behavior and how to model them. Transportation Res. Part B: Methodological 80: 338-354.
Jiang R, Jin C, Zhang H, Huang Y, Tian J, Wang W, Hu M, Wang H, Jia B (2018) Experimental and empirical investigations of traffic flow instability. Transportation Res., Part C Emerging Tech. 94:83-98.
Jin C, Knoop VL, Jiang R, Wang W, Wang H (2018) Calibration and validation of cellular automaton traffic flow model with empirical and experimental data. IET Intelligent Transportation Systems 12(5):359-365.
Kang K, Rakha HA (2018) Modeling driver merging behavior: A repeated game theoretical approach. Transporation Res. Record 2672(20):144-153.
Kesting A, Treiber M, Helbing D (2007) General lane-changing model mobil for car-following models. Transporation Res. Record (1999):86-94.
Kim J, Mahmassani HS (2011) Correlated parameters in driving behavior models: Car-following example and implications for traffic microsimulation. Transporation Res. Record 2249(1):62-77.
Kontorinaki M, Spiliopoulou A, Roncoli C, Papageorgiou M (2017) First-order traffic flow models incorporating capacity drop: Overview and real-data validation. Transportation Res. Part B: Methodological 106:52-75.
Li L, Jiang R, Jia B (2011) Modern Traffic Flow Theory and Application (Tsinghua University Press, Beijing, China).
Li X, Gao Z, Jia B, Zhao X (2009) Cellular automata model for unsignalized t-shaped intersection. Internat. J. Modern Phys. C 20(4):501-512.
Li X, Wang W, Roetting M (2018) Estimating driver's lane-change intent considering driving style and contextual traffic. IEEE Trans. Intelligent Transportation Systems 20(9):3258-3271.
Ma J, Dong H, Zhang HM (1999) Calibration of microsimulation with heuristic optimization methods. Transporation Res. Record 1:208-217.
Ma Z, Sun J, Wang Y (2017) A two-dimensional simulation model for modeling turning vehicles at mixed-flow intersections. Transporation Res., Part C Emerging Tech. 75:103-119.
Ma Z, Xie J, Qi X, Xu Y, Sun J (2017) Two-dimensional simulation of turning behavior in potential conflict area of mixed-flow intersections. Comput. Aided Civil Infrastructure Engrg. 32(5):412-428.
Mariotte G, Leclercq L, Batista S, Krug J, Paipuri M (2020) Calibration and validation of multi-reservoir mfd models: A case study in lyon. Transportation Res. Part B: Methodological 136:62-86.
Mullakkal-Babu FA, Wang M, van Arem B, Shyrokau B, Happee R (2021) A hybrid submicroscopic-microscopic traffic flow simulation framework. IEEE Trans. Intelligent Transportation Systems 22(6):3430-3443.
Newell GF (2002) A simplified car-following theory: A lower order model. Transportation Res. Part B: Methodological 36(3):195-205.
Ni D, Leonard JD, Jia C, Wang J (2016) Vehicle longitudinal control and traffic stream modeling. Transportation Sci. 50(3):1016-1031.
Punzo V, Montanino M (2016) Speed or spacing? Cumulative variables, and convolution of model errors and time in traffic flow models validation and calibration. Transportation Res. Part B: Methodological 91:21-33.
Ruskin HJ, Wang R (2002) Modeling traffic flow at an urban unsignalized intersection. Proc. Internat. Conf. on Comput. Sci. (Springer, Berlin), 381-390.
Saifuzzaman M, Zheng Z (2014) Incorporating human-factors in car-following models: A review of recent developments and research needs. Transporation Res., Part C Emerging Tech. 48: 379-403.
Sasaki M, Nagatani T (2003) Transition and saturation of traffic flow controlled by traffic lights. Phys. A 325(3-4):531-546.
Sayegh AS, Connors RD, Tate JE (2018) Uncertainty propagation from the cell transmission traffic flow model to emission predictions: A data-driven approach. Transportation Sci. 52(6):1327-1346.
Shu Y, Daamen W, Ligteringen H, Hoogendoorn S (2015) Vessel route choice theory and modeling. Transportation Res. Record 2479(1):9-15.
Spiliopoulou A, Kontorinaki M, Papageorgiou M, Kopelias P (2014) Macroscopic traffic flow model validation at congested freeway off-ramp areas. Transporation Res., Part C Emerging Tech. 41: 18-29.
Spiliopoulou A, Papamichail I, Papageorgiou M, Tyrinopoulos Y, Chrysoulakis J (2017) Macroscopic traffic flow model calibration using different optimization algorithms. Oper. Res. 17(1):145-164.
Talebpour A, Mahmassani HS, Hamdar SH (2015) Modeling lanechanging behavior in a connected environment: A game theory approach. Transportation Res., Part C Emerging Tech. 59:216-232.
Tang K, Tan C, Cao Y, Yao J, Sun J (2020) A tensor decomposition method for cycle-based traffic volume estimation using sampled vehicle trajectories. Transporation Res., Part C Emerging Tech. 118:102739.
Tang T, Zhang J, Liu K (2017) A speed guidance model accounting for the driver's bounded rationality at a signalized intersection. Phys. A 473:45-52.
Tang T, Huang H, Gang X, Yu X (2008) A traffic flow model considering signal light influence and its numerical simulation. Wuli Xuebao 57(1):56-60.
Tang T, Luo X, Zhang J, Chen L (2018) Modeling electric bicycle's lane-changing and retrograde behaviors. Phys. A 490:1377-1386.
Tang T, Yi Z, Zhang J, Zheng N (2017) Modeling the driving behavior at a signalised intersection with the information of remaining green time. IET Intelligent Transportation Systems 11(9):596-603.

Thorndike RL (1953) Who belongs in the family? Psychometrika 18(4):267-276.
Tian J, Jia B, Ma S, Zhu C, Jiang R, Ding Y (2017) Cellular automaton model with dynamical 2d speed-gap relation. Transportation Sci. 51(3):807-822.
Treiber M, Kesting A (2012) Validation of traffic flow models with respect to the spatiotemporal evolution of congested traffic patterns. Transporation Res., Part C Emerging Tech. 21(1):31-41.
Treiber M, Kesting A (2013) Microscopic calibration and validation of car-following models-A systematic approach. Proc. 20th Internat. Sympos. on Transportation and Traffic Theory (Elsevier, New York), 922-939.
Treiber M, Kesting A (2014) Traffic flow dynamics: Data, models and simulation. Phys. Today 67(3):54.
Treiber M, Kesting A, Helbing D (2006) Delays, inaccuracies and anticipation in microscopic traffic models. Phys. A 360:71-88.
van Erp PB, Knoop VL, Hoogendoorn SP (2017) Macroscopic traffic state estimation: Understanding traffic sensing data-based estimation errors. J. Adv. Transportation 2017:5730648.
Vasic J, Ruskin HJ (2012) Cellular automata simulation of traffic including cars and bicycles. Phys. A 391(8):2720-2729.
Wächter A, Biegler LT (2006) On the implementation of an interiorpoint filter line-search algorithm for large-scale nonlinear programming. Math. Programming 106(1):25-57.
Wang M, Hoogendoorn SP, Daamen W, Hoogendoorn R, van Arem B (2012) Driver support and cooperative systems control design: Framework and preliminary results. Proc. Amer. Control Conf. (IEEE, New York), 5751-5756.
Wang M, Hoogendoorn SP, Daamen W, van Arem B, Happee R (2015) Game theoretic approach for predictive lane-changing and car-following control. Transporation Res., Part C Emerging Tech. 58:73-92.
Wang M, Hoogendoorn S, Daamen W, van Arem B, Shyrokau B, Happee R (2018) Delay-compensating strategy to enhance string stability of adaptive cruise controlled vehicles. Transportmetrica B Transport Dynamics 6:211-229.
Wang Y, Li X, Tian J, Jiang R (2020) Stability analysis of stochastic linear car-following models. Transportation Sci. 54(1):274-297.
Xie J, Nie YM, Liu X (2017) Testing the proportionality condition with taxi trajectory data. Transportation Res. Part B: Methodological 104:583-601.
Xiong B, Jiang R, Tian J (2019) Improving two-dimensional intelligent driver models to overcome overly high deceleration in car-following. Phys. A 534:122313.
Yang D, Zhou X, Su G, Liu S (2019) Model and simulation of the heterogeneous traffic flow of the urban signalized intersection with an island work zone. IEEE Trans. Intelligent Transportation Systems 20(5):1719-1727.
Yu C, Sun W, Liu HX, Yang X (2019) Managing connected and automated vehicles at isolated intersections: From reservationto optimization-based methods. Transportation Res. Part B: Methodological 122:416-435.
Yu S, Shi Z (2015) Analysis of car-following behaviors considering the green signal countdown device. Nonlinear Dynamics 82(1-2): 731-740.
Yuan K, Knoop VL, Hoogendoorn SP (2017) A microscopic investigation into the capacity drop: Impacts of longitudinal behavior on the queue discharge rate. Transportation Sci. 51(3):852-862.
Yuan Y, Goñi-Ros B, van Oijen TP, Daamen W, Hoogendoorn SP (2017) Social force model describing pedestrian and cyclist behavior in shared spaces. Proc. Internat. Conf. on Traffic and Granular Flow (Springer, Berlin), 477-486.
Zeng W, Chen P, Nakamura H, Iryo-Asano M (2014) Application of social force model to pedestrian behavior analysis at signalized crosswalk. Transporation Res., Part C Emerging Tech. 40:143-159.
Zhang H, Liu HX, Chen P, Yu G, Wang Y (2020) Cycle-based end of queue estimation at signalized intersections using low-penetration-rate vehicle trajectories. IEEE Trans. Intelligent Transportation Systems 21(8):3257-3272.
Zhao J, Knoop VL, Wang M (2020) Two-dimensional vehicular movement modeling at intersections based on optimal control. Transportation Res. Part B: Methodological 138:1-22.
Zhao J, Li P (2016) An extended car-following model with consideration of speed guidance at intersections. Phys. A 461:1-8.
Zhao X, Gao Z, Jia B (2007) The capacity drop caused by the combined effect of the intersection and the bus stop in a ca model. Phys. A 385(2):645-658.
Zhu F, Ukkusuri SV (2018) Modeling the proactive driving behavior of connected vehicles: A cell-based simulation approach. Comput. Aided Civil Infrastructure Engrg. 33(4):262-281.


[^0]:    ${ }^{\text {a }}$ Correlation is significant at the 0.01 level (two-tailed).
    ${ }^{\mathrm{b}}$ Correlation is significant at the 0.05 level (two-tailed).

[^1]:    Notes. SB, NB, EB, and WB indicate southbound, northbound, eastbound, and westbound, respectively. LT and TH indicate left turn and through movement, respectively.

