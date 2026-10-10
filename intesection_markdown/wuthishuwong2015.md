# Safe trajectory planning for autonomous intersection management by using vehicle to infrastructure communication 

Chairit Wuthishuwong ${ }^{1^{*}}$, Ansgar Traechtler ${ }^{1}$ and Torsten Bruns ${ }^{2}$


#### Abstract

The development of autonomous vehicle or self-driving car integrates with the wireless communication technology which would be a forward step for road transportation in the near future. The autonomous crossing of an intersection with an autonomous vehicle will play a crucial role in the future of intelligent transportation system (ITS). The fundamental objectives of this work are to manage autonomous vehicles crossing an intersection with no collisions, maintaining that a vehicle drives continuously, and to decrease the waiting time at an intersection. In this paper, a discrete model of the one-way single intersection is designed. The vehicle-to-infrastructure (V21) communication is implemented to exchange information between a vehicle and an intersection manager which is the roadside infrastructure. The safe trajectory of autonomous vehicles for the autonomous intersection management is determined and presented by using discrete mathematics.


Keywords: Autonomous vehicle; Self-driving car; Intelligent transportation system (ITS); Vehicle-to-infrastructure communication (V21); Autonomous intersection management (AIM); Discrete mathematics

## 1 Introduction

The vehicle technology has grown rapidly in the past decade. Several systems have been installed into commercial vehicles to assist the driver to provide a more comfortable drive, including improving of the safety of the driver, passenger, and the pedestrian or cyclist. Recently, there has been a highly increased activity in the development of the autonomous vehicle research, which was initiated in 2005 by the first competition of autonomous vehicles. The Defense Advanced Research Projects Agency (DARPA) Grand Challenge was organized. In 2007, the DARPA Urban Challenge showed the progression of the autonomous vehicle. Several teams successfully developed a vehicle that has the ability to drive itself and achieve the assigned task. As a result, the self-driving car or autonomous vehicle is now successfully developed by many research groups either in universities or more recently by private companies [1-3]. They proved the performance of driving in a real-

[^0]traffic environment, autonomously with the capability of safety. It showed that the use of this technology is possible in the near future. Already, some cities in the USA currently allow the autonomous vehicle to drive on the same street as other vehicles, legally. Furthermore, the increased use of wireless communication technology is making a huge contribution to applications with the cooperation of multiple robots. Many multiple robots and cooperation researches were focusing on the mobile robot application, e.g., robot soccer, task allocation, area exploration, robot formation, and swarm robotics [4-7]. With the existing technology of wireless communication, the application of autonomous intersection management (AIM) (Additional file 1) is possible. The safety of driving is the first priority of road transportation. An intersection, especially, is considered one of the high-risk places for accidents to occur. In addition, traffic congestion is also very important and serves as the second objective of the traffic management.

There are two different approaches from previous research studies that developed the collision avoidance at an intersection: with and without communication. Without communication, the stand-alone autonomous vehicle is equipped with several sensors to measure its state, e.g., GPS, position, orientation, and velocity, which is now in general use. Also used, an environment sensor to measure the vehicle's surrounding, e.g., the laser range finder, radar, and camera, were used to locate the static and dynamic obstacles around a vehicle and then plan a collision free path by using the stop and go technique [8,9]. With communication, [10] presented the latest wireless communication standard for vehicle communication. The IEEE 802.11p with the spectrum of 5.9-GHz band, dedicated short-range communications (DSRC) is the standard that was developed for use only with vehicle communication. The time scheduling method by means of intelligent agents was introduced in [11]. It determined the arrival time of a vehicle and the time that a vehicle would stay at an intersection by sharing the state information and then passing it back to the following vehicle by using mobile ad hoc networks. Hafner et al. [12] presented the automated collision avoidance at an intersection between two vehicles, using vehicle-to-vehicle communication (V2V). It used V2V to share the state information of two vehicles to find the potential collision area and then control the longitudinal velocities of both vehicles to prevent them from reaching the collision area at the same time. Similarly, [13] proposed the method of sharing the state of vehicle inertia to create the navigation function that creates a safe and smooth path without fully stopping at the intersection. Sheng et al. [14] propose the method of intersection collision groups: each vehicle broadcasts its collision situation based on the path selection. When a vehicle reaches the communication range, the collision free path was determined by comparing the initial member of collision group and of another incoming vehicle. The driving speed was cooperatively calculated for the safe crossing of the intersection. The proposed concept in [15] consists of intersection geometry, to map the collision region by using the first-come first-serve (FCFS) principle to manage a vehicle crossing an intersection. Another method is using vehicle-to-infrastructure communication (V2I). Bruns and Trächtler [16] and Bruns [17] used the concept of network flow to model the intersection. The intersection was separated into small equal connected sections. The incoming vehicle has to reserve nodes based on the selected route, and the safe trajectory is determined by using dynamic programming. This resulted in the centralized control principle. Moreover, the extended study in [18] was considering optimization of multiple objectives to improve driving efficiency. The fuel consumption and duration of a journey were minimized by using the technique of dynamic programming.
Autonomous intersection management with the 'call ahead' concept was presented by [19-21]. Every car must send a reservation message to the intersection manager, and it will check the availability of the requested space. If the requested message is not in conflict with the intersection policy, a car is allowed to pass through the intersection. Otherwise, the car has to generate and send new request messages until it gets the permission from the intersection manager or, in the worst case, stop before entering the intersection. From the sample research works, the common parameter information that is shared is mostly the state of the car. Then, the possible collision event is computed and the velocity is controlled, speeding up or slowing down, to avoid the collision scenario.
In this paper, the authors propose the methodology of planning the safe trajectory for crossing an intersection, including improving the capacity of the intersection. Aforementioned works proposed the methodology of autonomous intersection management with the main focus of using artificial intelligent, supervised rulebased or machine-learning technique. On the other hand, we presented the different concept for managing vehicles crossing an intersection. The discrete time event was implemented in order to determine the safe trajectory so that the trajectory of each vehicle can be computed deterministically, the position of a vehicle can be controlled exactly to a particular time. The discrete model of a single intersection was presented. In addition, the idea of green wave, where a vehicle is able to continuously drive through an intersection, was investigated in the area of adaptive traffic light research. We have applied this concept for our autonomous intersection management. However, the traditional traffic light will be replaced by the intersection manager. Our approach relies on the exchange of information between an incoming car and the intersection manager. To coordinate a car to the intersection manager, the following message protocol has been designed: a vehicle sends a message to the intersection manager to request the state of intersection. The intersection manager will check its state and whether it is occupied by a previous vehicle. Then, it will update the time index and reserve it for the incoming vehicle. It will then return the message of the time index back to the incoming vehicle. The management mechanism is able to express the information as a personal, virtual traffic signal. Each vehicle will get an individual identity time index in which to occupy the intersection in order to then plan the safe trajectory to reach each node within the given time. The simulation of autonomous intersection
management for a single intersection is developed. The results show the improvement in velocity capacity and the traffic flow rate of an intersection compared to the traffic flow model.

## 2 Intersection model

In this work, the symmetrical four-way intersection with a single lane for each incoming and outgoing street is represented. The physical shape of this intersection is composed of four connected streets. Every street shares the common characteristic of driving direction. There are three possible choices of driving routes for each street that are composed of left, straight, and right directions. The model of the street and intersection is illustrated in Figure 1:

$$
r_{x}=\left\{r_{1}, r_{2}, r_{3} \mid 1,2,3 \in x, \quad x \in \mathbb{R}^{+}\right\}
$$

where $r_{x}$ is the number of possible routes of the fourway intersection, $x$ is the driving direction, $r_{1}$ is left direction, $r_{2}$ is straight direction, and $r_{3}$ is right direction.

The assumption is that every vehicle on each of the four connected streets is able to select the route independently. For this reason, there are 12 combination patterns in total. The total combinations of route choices of this intersection model can be expressed by the product of route choices and the total number of streets:

$$
\begin{aligned}
& s_{m}=\left\{s_{1}, s_{2}, s_{3}, s_{4} \mid 1,2,3,4 \in m, \quad m \in \mathbb{R}^{+}\right\} \\
& n_{f}=\left\{12 \mid s_{m} \cdot r_{x}\right\} \\
& n_{f}=\left\{n_{1}, n_{2}, \ldots, n_{f} \mid f \in m \cdot x\right\}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-03.jpg?height=782&width=814&top_left_y=1705&top_left_x=194)
Figure 1 Four-way intersection model.

where $s_{m}$ is the total number of street of an intersection, $m$ is street members of an intersection (North, East, West, South), and $n_{f}$ is the total number of possible routes.
For the simulation purpose, the vehicle's dynamics are configured based on the geometry of the intersection. The maximum allowance of driving velocity of a vehicle is limited at 120 km/h, and the presumed average velocity is at 80 km/h and the minimum is set at 0. The maximum acceleration is set at $2 \mathrm{~m} / \mathrm{s}^{2}$. It assumed based on the changing velocity from average to maximum in 5-s time interval. For deceleration, in the same way, the decreasing of velocity from average to 0 is able to set the value of deceleration at $4 \mathrm{~m} / \mathrm{s}^{2}$. In addition, the flow input to the intersection from each side of the street is limited at the maximum of 2,000 vehicles/h, according to the traffic flow model in [22,23].

## 3 Autonomous intersection management

The traditional traffic light system works on the principle of centralized control, i.e., a vehicle must stop when the light is red and it can go ahead when the light is green. Drivers will plan trajectory based on their visual data. On the other hand, autonomous intersection management is a fully autonomous system. Technically, autonomous intersection management relies on the communication between vehicles and the intersection manager. It will replace the traffic light with the intersection manager as well as replacing the typical vehicle with the autonomous vehicle. The intersection manager has the ability to communicate wirelessly with every incoming vehicle. Likewise, the vehicle also has the same feature, in order to transmit and receive information to intersection manager. The responsibility of the intersection manager is that it will prioritize the timing index, corresponding to the occupied space and tell a vehicle when it can pass through the intersection, based on the incoming, requested message from vehicles. In the same way, an autonomous vehicle will follow the policy from the intersection manager strictly and accurately. The trajectory will be planned based on the returned, available timing index from the intersection manager. The management mechanism is similar to the personal, virtual traffic signal. Every vehicle will get the personal timing index from the intersection manager and drive according to the received policy. The V2I communication is the tool in which the requested message from vehicle to the intersection manager is delivered and vice versa. The message protocol is defined in the section below.

### 3.1 Crossing intersection problem

In order to cross an intersection, the nature of the problem is the resource sharing. In this case, the resource is
concerned as a space and how vehicles use the limited space together. Therefore, the problem will be dealing with space and time. In practice, a vehicle is allowed to drive over the intersection area following the traffic signal. That is, the method to manage several vehicles to use the intersection area at different points of time. For the sample scenario, there are two vehicles on the different streets. The red vehicle (no. 1.) drives on the West Street and plans to go to the North Street. On the other side, the green vehicle (no. 2.) drives on the East street and the destination is the West street. The trajectory of both vehicles is clearly crossed over. Therefore, the collision can occur while vehicle no. 1. is turning left and vehicle no. 2. goes straight and both vehicles arrive at the confliction point at the same time. The general scenario of crossing an intersection is illustrated in Figure 2a:

$$
P^{*}=\left\{x^{*}, y^{*} \mid x_{1}, x_{2} \in x^{*} \Delta y_{1}, y_{2} \in y^{*}\right\}
$$

where $P^{*}$ is the coordinate of the confliction point, $x^{*}$ is the position in x direction, $y^{*}$ is the position in y direction, $x_{1}$ and $x_{2}$ are the x positions of vehicles no. 1 and no. 2, respectively, and $y_{1}$ and $y_{2}$ are the positions of vehicles no. 1 and no. 2, respectively.

### 3.2 Vehicle-to-infrastructure communication protocol

There are several works in vehicle inter-communication by using wireless communication. In this work, we implemented wireless communication between a vehicle and an infrastructure by using the normal standard of wireless local area network (WLAN, IEEE 802.11) for computer communication. User datagram protocol (UDP) together with a broadcasting technique is used to communicate between a vehicle and the intersection manager. In order to limit the number of vehicles communicating with the intersection manager, a vehicle will start sending a message when it reaches the designated range of communication. The communication region is set at the radius of 100 m away from the center of the intersection as illustrated in Figure 2b. The intersection manager will be polling the message and updating its state every 0.1 s or with in10-Hz frequency. Then, it returns the computed timing index, with the maximum and minimum acceleration allowance back to the requested vehicle. The requested message package from a vehicle contains the following six information:

- Vehicle identification code (vehicle ID): it is used to identify that a vehicle is present and to prevent the wrong determining vehicle, the Internet protocol (IP) address or the media access control (MAC) address can be used to represent a vehicle.
- Location: the position information integrates with the digital map of the local street containing the current street where a vehicle is located. It is used to determine the approaching vector of a vehicle to an intersection.
- Destination: the information containing the expected street where a vehicle will drive to. The direction of travel can be computed through corresponding the current location.

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-04.jpg?height=866&width=1684&top_left_y=1684&top_left_x=194)

- Distance to intersection: it is the distance between the current position of a vehicle and an intersection.
- Vehicle size: the length of a vehicle is usually taken into account for determining the leaving time of intersection. Different sizes of vehicles spend different times to cross an intersection.
- Velocity: the current longitudinal velocity of a vehicle

The intersection manager extracts the message information into the proposed parameters. The arrival time to the intersection and the leaving time are determined based on the provided information of the successor vehicle and the predecessor vehicle. The intersection will be updated and the new time slot will be transmitted to the requested vehicle. The V2I communication mechanism is illustrated in Figure 3.

### 3.3 Discretizing intersection

Following the crossing-an-intersection problem, a way to manage vehicles crossing intersection without using traffic light control is to manage the time interval of using an intersection space for incoming vehicles. This problem is expressed with the discrete time event, where the space and time can be solved deterministically. The reason is that the space of an intersection is constant, and the required output is time of possession corresponding to the specific reservation space. The exact position of a vehicle can be calculated deterministically at every time step by the given, inputted velocity. Then, it is able to guarantee that the intersection space will be reserved by only one vehicle at a time.

As mentioned earlier, the nature of crossing an intersection is generally to manage multiple vehicles not driving over the same area at the same moment of time. If we can then calculate the exact time that a vehicle can drive through the conflict area and a vehicle is able to follow that policy, the collision will not occur. Then, the problem of crossing an intersection can be modeled as a discrete problem. With the proposed intersection model, there are two processes of discretization, composed of distance discretization and time discretization.

Distance discretization: the intersection is firstly discretized into a section of distance. And every section is represented by each node of a discretized distance. It contains position coordinates of each discretized distance. In addition, each node is connected with an edge that is a discretized distance and the whole travelling distance is equal to the summation of the total discretized distances:

$$
\begin{aligned}
& s_{i, 0}<s_{i, 1}<s_{i, 2}<\ldots s_{i, k} ; 0<s_{i, k}<S_{i, f} \\
& \sum_{k=0}^{f} s_{k}=S_{i, f} \\
& P_{i, k}=\left\{x_{i}\left(s_{i, k}\right), y_{i}\left(s_{i, k}\right)\right\} ; P_{i, k} \subseteq P_{i, f}
\end{aligned}
$$

where $i$ is the index of a vehicle, $k$ is the discretized step, and $f$ is the final step of the discretization. $s_{i, k}$ is the discretized distance of step $k$ of the trajectory of a vehicle. $S_{i, f}$ is the total travelling distance of a vehicle. $P_{i, k}$ is the discrete position of a vehicle, and with respect to the Cartesian coordinate, it is the function of each discretized distance.

The desired trajectory of both vehicles in the proposed scenario is able to discretize into a set of connected
![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-05.jpg?height=790&width=1679&top_left_y=1759&top_left_x=196)
nodes. The problem of the space reservation will transfer the location to the network of nodes. The illustration of the intersection distance discretization is shown in the Figure 4.

Concerning time discretization, if there were a timing problem, an accident is able to occur if, and only if, the vehicles meet each other at a specific point of the intersection at the same time. To prevent that situation, time is discretized. The discretizing time step is constant. Time will be discretized into small steps, and the summation of the total discretized time will equal to total travelling time. Time discretization criteria can be written as the following equations:

$$
\begin{aligned}
& \ldots<t_{k-1}<t_{k}<t_{k+1}<\ldots ; t_{k} \leq T_{f} \\
& t_{k+1}-t_{k}=\Delta k \\
& \sum_{k=0}^{f} t_{k}=T_{f}
\end{aligned}
$$

where $t_{k}$ is the time step, $T_{f}$ is the total travelling time, and $\Delta k$ is the discretizing time.

The time discretizing model corresponding with the distance discretizing model for crossing an intersection of both vehicles is illustrated in the Figure 5.
The trajectory of each vehicle is planned by the vehicle itself based on the returned timing index from the intersection manager. The possession time of each node is calculated and accumulated from one discretized section to the next discretized section. The process is so that when a vehicle is reaching the designated communication region of the target intersection, it has to send a requested message to the intersection manager by wireless communication. From the V2I message protocol, the proposed information is extracted. This information, along with the current state of intersection, is then used to generate the trajectory of a vehicle. In Figure 6, the discrete trajectory of two vehicles is shown while they are crossing an intersection. The vehicle's trajectory was plotted together with the lateral and longitudinal distance and time discretization.
![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-06.jpg?height=480&width=820&top_left_y=2069&top_left_x=194)

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-06.jpg?height=633&width=767&top_left_y=327&top_left_x=1079)
Figure 5 The illustration of intersection distance and time discretization.

The process of reservation is made through iteratively calculating the nodes parameters, coordinate data of distance, and time of the incoming vehicle. The illustration of the node reservation is shown in Figure 7. The horizontal axis is the discretized distance. The vertical axis is the discretized time. The occupied nodes are shown by red, cross circles, and the blue circles represent the free nodes. In this case, there is no reservation of the current node from the predecessor, it means that the state of intersection is free to reserve for that period of time. The successor has the right to occupy the required nodes by setting the time of possession to the nodes based on its desired velocity.
![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-06.jpg?height=749&width=818&top_left_y=1800&top_left_x=1057)

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-07.jpg?height=650&width=760&top_left_y=332&top_left_x=222)
Figure 7 The illustration of node reservation.

The distance discretization process will divide the total travelling distance $\left(s_{f}\right)$ into small connected sections ( $s_{k}$, $s_{k+1}, \ldots, s_{k+i} \mid \forall s_{k} \in s_{f}$ ), and the required set of nodes will be determined based on the received information from a requesting vehicle. The reservation nodes are obtained with the information of time and distance ( $N\left[s_{i}\right.$, $\left.{ }_{k}, t_{i, k}\right]$ ). Integrating with the information of the current velocity of a vehicle, the average travelling time $\left(t_{f}\right)$ to the destination can be determined by the relationship of the linear motion principle. In addition, the discretization of time into equally small timing steps $(\Delta k)$ is applied to assign the timing index of each node to the corresponding discrete distance. The size of a vehicle is taken into account, when computing the number of nodes to be used and reserved.

On the other hand, the incoming vehicle is not allowed to reserve a node which has already been reserved for the previous vehicle. In order to make a successful reservation, the timing index for the specific node for the successor is shifted. The time is increased with respect to the predecessor timing index by the discretized time step, until the node is free to reserve. The cost of node is defined as the function of the accumulated time given by a specific node and the relative time between successor and predecessor. Generally speaking, the cost of node indicates the absolute value of time until the node will be released or it means until a vehicle has already left the intersection.
The time of possession of the successor is dependant on the situation of the predecessor. In the same way, the system determines the successor state based on the predecessor state. Then, it is able to consider the system as the first order system. According to the first order system property, the forward Euler method is used to update the timing index of the successor node. The term of the prior time is defined by the progression of the possession time which depends on the velocity of the predecessor itself. The time of possession of the predecessor is counting down along the increasing of accumulated distance until it is vanished when a vehicle has already passed the occupied node and the state of the node will be changed from an occupied node to a free node. Comparing to the predecessor state, the relative time between the predecessor and the successor is determined at the same reference distance after the message of the successor was received. Therefore, the absolute possession time of each node is iteratively updated until the predecessor vehicle has left the intersection. The time update can be written as the following equations:

$$
\begin{aligned}
& t_{k}^{-}(j)=t_{k}(i)+\Delta k_{i} \\
& \Delta k_{i}=\sum_{k-1}^{k} \frac{s_{k}(i)}{v(i)} \\
& T_{d}(j)=t_{s=0}(j)-t_{s=0}(i) \\
& t_{k}(j)=t_{k}^{-}(j)-T_{d}(j)
\end{aligned}
$$

where $i$ is the predecessor node, $j$ is the successor node, $t_{k}^{-}$is the prior timing index of the successor, $t_{k}$ is the posterior timing index of the successor, $\Delta k_{i}$ is the accumulative time step of the predecessor node, $s_{k}$ is the discretized distance, $v$ is the average velocity, and $T_{d}$ is relative time between the predecessor and the successor determined from a reference distance.
The recursive determination is required to find a solution of this discrete problem. The tool that we used to implement for the node reservation is dynamic programming (DP). Dynamic programming is frequently used for solving complex problems by breaking them down into several sub problems. It then solves each sub problem, part by part, and combines those solutions. Similarly, dynamic programming can deliver the optimal solution. It looks into all possible solutions of the problem and will select the best solution, e.g., finding the shortest path between two points is the most popular application of DP.
Therefore, dynamic programming is appropriate for solving the proposed discrete problem. It is used to find the trajectory of a vehicle at every discretized time step. Shown in the presented scenario, is the classic problem of crossing an intersection. The node reservation method is able to provide the safe trajectory of vehicles while crossing an intersection. The pseudo algorithm of node reservation for intersection management is calculated by using dynamic programming which is provided in the Algorithm 3.1.

```
Algorithm 3.1: Node reservation
\(/ / \boldsymbol{N}[\boldsymbol{i}]\) state of the predecessor node;
\(/ / N[j]\) state of the successor node;
\(/ / \boldsymbol{T}_{\boldsymbol{d}}(\boldsymbol{j})\) relative time at referent distance \(\boldsymbol{s}_{\boldsymbol{k}=\mathbf{0}}\);
\(/ / \boldsymbol{c}(\boldsymbol{i}, \boldsymbol{j})\) cost of node;
\(\mathrm{k}=0\);
While \(\left(\boldsymbol{s}_{\boldsymbol{k}}<\boldsymbol{s}_{\boldsymbol{f}}\right)\)
    For (Distance discretizing, \(\boldsymbol{s}_{\boldsymbol{k}} \subseteq \boldsymbol{s}_{\boldsymbol{f}}\) )
        \(s_{k+1}=s_{k}+\Delta k_{;}\)
        For (Time discretizing, \(\boldsymbol{t}_{\boldsymbol{i}} \subseteq \boldsymbol{t}_{\boldsymbol{k}}\) )
            \(T_{d}(j)=t_{s=0}(j)-t_{s=0}(i) ;\)
            \(c(i, j)=f\left(s_{k}(i), T_{d}(j)\right)\)
            If (Check all node \(\in \boldsymbol{S}_{\boldsymbol{f}}\) )
                If \((\boldsymbol{N}[\boldsymbol{i}]+\boldsymbol{c}(\boldsymbol{i}, \boldsymbol{j})<N[\boldsymbol{j}])\)
                    \(N[j]=N[j] ;\)
                Else
                    \(N[j]=N[i]+c(i, j) ;\)
            Update state \(\boldsymbol{N}[\boldsymbol{i}]=\boldsymbol{N}[\boldsymbol{j}]\)
    k++
Return
```

The management mechanism relies on the communication between vehicles and the intersection manager. To prevent the message crashing, the principle of FCFS is implemented for ordering the message queue. The intersection manager will make a service based on the sequence of the received message from vehicle.

The discretization of distance and time combined with the node reservation allows the possession time of required nodes to be calculated and then reserved. The state of an intersection is updated and waits for the next iteration from the next vehicle's request. The intersection state was reserved by the predecessor vehicle, and the time of possession was registered. The following vehicle is allowed to reserve the node after the possession time of the predecessor vehicle has expired. For this reason, both vehicles are at different places or nodes at the same time. The result of the vehicle's trajectories while crossing an intersection which are computed by using DP is illustrated in Figure 8. It is a time-distance plot. The horizontal axis indicates the discretized distance, and the vertical axis indicates the discretized time. The node reservation of a vehicle is illustrated. The trajectory of the first vehicle is showed in red and the following vehicle is showed in green. Gray represents the predecessor vehicle that has already left the intersection.

## 4 Simulation results

According to the focus of this work, the cooperative trajectory planning algorithm, the simulation is implemented based on the proposed method, regardless the technique of communication. Since the communication mediums are considered as tools to exchange the information between vehicle and infrastructure, any communication standard, which provides the fit qualification, can be applied to autonomous intersection management. In this work, the Internet protocol has been used for communicating between vehicle and infrastructure. The wireless local area network with UDP protocol is implemented. In general, a computer is set as the vehicle server in order to generate the requested messages and send to the intersection manager over the WiFi, IP address. Meanwhile, another computer is the intersection

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-08.jpg?height=650&width=999&top_left_y=1834&top_left_x=534)
Figure 8 Projection of vehicle's trajectory between distance and time.

manager for simulating the autonomous crossing. However, the option of the local host IP address 127.0.0.1 with different broadcast communication ports is used for communication in this simulation to run a simulation on a stand-alone computer, four communication ports for vehicles from each single street and another port for the intersection manager. The communication will be updated every $0.1-\mathrm{s}$ time interval or in $10-\mathrm{Hz}$ frequency.

The four-way intersection with a single lane of incoming and outgoing traffic is used as the reference model in the simulation scenario. The traffic flow rate is able to configure from the minimum 1 vehicle/h up to the maximum 3,000 vehicles/h. The maximum velocity is allowed at 100 km/h, and the minimum is set at 0 km/h. The range of communication is set at 100 m, radius from the center of the intersection. The parameters in this simulation are set through the following configuration. The traffic flow rate in this simulation is assumed to be homogeneous. The balance of the traffic flow is presumed by setting the same amount of flow rate to every incoming street. The inputted flow rate from each incoming street is configured at 1,500 vehicles/h. Therefore, the estimated gross flow rate, number of vehicles that will cross an intersection, will be equal to 6,000 vehicles/h. However, there is no fixed configuration of the route plan. Every vehicle on each street is able to select its own route randomly. The intersection manager only determines the priority of crossing an intersection without forcing to change the original route plan from the vehicles.

On the assumption that the communication between vehicles and intersection manager is performed by using host IP address, for this reason, the communication time between them is considered very small and it can be neglected. In addition, assuming that there is no incomplete data in transmitting and receiving, thus, the package loss throughout the communication is not investigated. In this simulation, the safe trajectory of vehicles while crossing an intersection is the main interest. The resulted trajectories are collected from vehicles on each street drive throughout an intersection. The communication radius is the initial distance of the vehicle trajectory. The intersection border is represented by the red line. The plot shows that the safe trajectory is guaranteed, even though vehicles are entering the intersection at the different times. The resulted plot of trajectories, of vehicles, while crossing an intersection is shown in Figure 9.
The second observed parameter is the average driving velocity of vehicles. The data was collected from a total of 40 vehicles that crossed intersection. Ten vehicles from each street were sampled, and their velocity data was collected. The average velocity is determined by arithmetic mean of the whole data from start to the end of travelling. From the data, the average velocity of vehicles on the North street is 82.9 km/h, on East street is 82.3 km/h, on West street is 76.4 km/h, and on the South street is 85.6 km/h. Then, the average velocity for crossing the intersection with four incoming streets is equal to average of the average velocity of each street, which is 81.8 km/h.

From the result, vehicles on each street can drive with nearly the same level of average velocity. On the other hand, it can be interpreted in the terms of total travelling time. When the total travelling distance is equal and vehicle drive is close to the average velocity, the average total travelling time will be nearly the same. The average velocity of vehicles on four streets, North, East, West, and South, are plotted in Figure 10.

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-09.jpg?height=629&width=999&top_left_y=1858&top_left_x=534)
Figure 9 Trajectory of vehicles while crossing an intersection.

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-10.jpg?height=627&width=1001&top_left_y=329&top_left_x=532)
Figure 10 The average velocity of vehicles on each street.

The third observed parameter is the crossing intersection time. The crossing time is defined as the time the vehicle took to drive from the initial distance until finished crossing an intersection. The data was collected by the intersection manager. From the data, the maximum crossing time is 6.76 s, minimum is 5.26 s, and the average crossing time is 6 s. The result showed that vehicles spent almost the same time in crossing the intersection. The number of stops at the intersection was not found. All vehicles crossed the intersection continuously without stop at the configured level of traffic flow. The average crossing time at the intersection is shown in Figure 11.

The relationship between traffic flow rate and average velocity is shown in Figure 12. The data was plotted between flow rate in horizontal axis and average velocity in vertical axis. The flow rate was determined based on the traffic flow theory using traffic density data that was collected by counting the number of incoming messages of the requested vehicles. According to the traffic flow model [22,23], the average velocity will decrease when the flow rate is increasing before the density will reach the critical value. In general, after the flow rate of 3,000 vehicles/h, average velocity will gradually decrease. However, the result showed that all vehicles still can maintain the higher velocity in the higher flow rate zone. In short, it can be expressed that the throughput of the system is increased because vehicles can use the higher velocity compared to the traffic flow model.

## 5 Conclusions

The fully autonomous intersection management system is not widely implemented due to several factors. The

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-10.jpg?height=635&width=1001&top_left_y=1852&top_left_x=532)
Figure 11 The average crossing time at the intersection.

![](https://cdn.mathpix.com/cropped/dbdfb96c-ad5f-4b39-b5f7-93aa6b8ef5f5-11.jpg?height=644&width=1001&top_left_y=327&top_left_x=532)
Figure 12 Flow and average velocity plot.

first obvious factor is that the autonomous vehicle itself is not ready for operation on real roads. However, the development of autonomous vehicles is progressing very well and it has recently been approved for use on public roads. In addition, the wireless communication for vehicles is not currently installed in the commercial vehicle. Most of the research in traffic management has been working on intelligent traffic signal control because the traffic light infrastructure system already exists. It focuses on increasing the performance of the traffic light system by adapting the timing of light signal. The period of red and green light timing is adapted based on the current traffic. Another approach has been working on the improvement for traffic safety, collision avoidance system, for example.
On the other hand, in this work, we try to develop a completely autonomous system for the concept of future, intelligent transportation. The primary objective of this work is to build a system that guarantees the collision-free crossing of an intersection and, as a secondary purpose, alleviates the traffic congestion. The standard of wireless communication for a vehicle has been recently introduced [8]. We implemented the methodology for an autonomous intersection management through the use of V2I communication. The communication protocol is designed, and the node reservation algorithm is implemented. The concept of virtual personal traffic signal is introduced. Each vehicle will get an individual, given time from the intersection manager. The discrete mathematics is applied to model the crossing intersection problem, and dynamic programming is used to calculate the trajectory of a vehicle. The simulation program for a single intersection is developed based on the proposed methodology. The result shows the successful cross of an intersection, without a collision. Furthermore, all vehicles are driven continuously. It can be expressed that the waiting time at an intersection is decreased compared to the traditional traffic light. The limitation of this work is that the simulation is able to simulate only a single intersection. We will extend this work to multiple intersections in the future work.

### 5.1 Future work

In the real environment of the road traffic, there is not only a single intersection. A lot of connected intersections cause the road networks to be very complex. The traffic management for multiple intersections is necessary for studying the traffic behavior at the microscopic level. To manage the traffic flow of multiple intersections, the coordination between neighborhood intersections, infrastructure-to-infrastructure communication (I2I) will be implemented in future work. Furthermore, the traffic flow theory will be investigated to observe the macroscopic traffic behavior.

## 6 Additional file

Additional file 1: Autonomous intersection management.

Competing interests
The authors declare that they have no competing interests.

Acknowledgements
This research is funded by the Ministry of Innovation, Science, Research, and Technology of the Federal State North-Rhine-Westphalia, Germany, through the International Graduate School of Dynamic Intelligent System. This work carried on the previous work of Torsten Bruns who initiated the Autonomous Intersection Management project under the supervision of Prof. Ansgar Traechtler of the Heinz Nixdorf Institute, Control Engineering and Mechatronics Department, University of Paderborn. The fundamental technique was developed based on the knowledge of his work.

Author details
${ }^{1}$ Heinz Nixdorf Institute, Control Engineering and Mechatronics Department, University Paderborn, Fürstenallee 11, Paderborn 33102, Germany.
${ }^{2}$ Projektgruppe Entwerfstechnik Mechatronik, Fraunhofer IPT, Zukunftsmeile 1, 33102 Paderborn, Germany.

Received: 31 January 2014 Accepted: 5 January 2015
Published online: 19 February 2015

References

1. S Thrun, M Montemerlo, H Dahlkamp, D Stavens, A Aron, J Diebel, P Fong, J Gale, M Halpenny, G Hoffman, K Lau, C Oakley, M Palatucci, V Pratt, P Stang, S Strihband, C Dupont, LE Jendrossek, C Koelen, C Markey, C Rummel, JV Niekerk, E Jensen, P Alessandrini, G Bradski, B Davies, S Ettinger, A Kaehler, A Nefian, P Mahoney, Stanley: the robot that won the DARPA Grand Challenge. J. Field. Robot. 23, 661-696 (2006). doi:10.1002/rob. 20147
2. ME Randall, A Lien, Autonomous vehicle development. IEEE Women Eng. Mag. 2(1), 34-37 (2008). doi:10.1109/MWIE.2008.925802
3. C Wuthishuwong, C Silawatchananai, M Panichkun, Navigation and control of an intelligent vehicle by using stand-alone GPS, compass and laser range finder (Paper presented at the IEEE international conference on Robotics and Biomimetics, Bangkok, 2008)
4. Y Cao, AS Fukunaka, AB Kahng, F Meng, Cooperative mobile robotics: antecedents and direction (Paper presented at the IEEE international conference on Intelligennt Robotics and Systems (IROS), IEEE, Pittsburgh, PA, 1995), pp. 144-149
5. R Madhavan, K Fregene, L Parker, Distributed cooperative outdoor multirobot localization and mapping. Auton. Robot. 17, 23-29 (2004). doi:10.1023/B:AURO.0000032936.24187.41
6. F Ducatelle, GA Di Caro, C Pinciroli, LM Gambardella, Self-organized cooperation between robotics swarms. Swarm Intell. 5, 73-96 (2011). doi:10.1007/s11721-011-0053-0
7. J Spletzer, AK Das, R Fierro, CJ Taylor, V Kumar, JP Ostrowski, Cooperative localization and control for multi-robot manipulation (Paper presented at the IEEE international conference on Intelligent Robots and Systems (IROS), IEEE, San Francisco, USA, 2011)
8. L Bouraoui, S Petti, A Laouiti, T Fraichard, M Parent, Cybercar cooperation for safe intersections (Paper presented at the IEEE Intelligent Transportation Systems (ITS), IEEE, Toronto, 2006)
9. Y-W Seo, C Urmson, A perception mechanism for supporting autonomous intersection handling in urban driving (Paper presented at the IEEE/RSJ international conference on Intelligent Robots and Systems, Nice, France, 2008)
10. JB Kenney, Dedicated short-range communications (DSRC) standards in the United States. IEEE SAE Stand. Wirel. Access Veh. Environ. (WAVE) 99, 1162-1182 (2011). doi:10.1109/JPROC.2011.2132790
11. X Zou, D Levinson, Vehicle-based intersection management with intelligent agents. ITS America Annual Meeting Proceedings, 2003
12. MR Hafner, D Cunningham, L Caminiti, D Del Vecchio, Autonomated vehicle-to-vehicle collision avoidance at intersections (Proceedings 18th ITS World Congress, Orlando, USA, 2011). Transport Research Board of the national academies (TRB). ISBN 978-1-61839-433-0
13. L Makarem, D Gillet, Information sharing among autonomous vehicles crossing an intersection (Paper presented at the IEEE international conference on Systems, Man, and Cybernatics (SMC), IEEE, Seoul, 2012)
14. W Sheng, Q Yang, Y Guo, Cooperative driving based on inter-vehicle communication: experimental platform and algorithm (Paper presented at the Proceeding of IEEE/RSJ international conference on Intelligent Robots and Systems (IROS), IEEE, Beijing, China, 2006)
15. R Naumann, R Rasche, J Tacken, Managing autonomous vehicles at intersections. IEEE Intell. Syst. 13, 82-86 (1998). doi:10.1109/5254.683216
16. T Bruns, A Trächtler, Kreuzungmanagement: trajektorienplanung mittels dynamischer programmierung (Oldenbourg Wissenchaftverlag, Automatisierungtechnik, 2009), pp. 253-261 (in German)
17. T Bruns, Trajektorienplanung mittels Diskretisierung und kombinatorischer Optimierung am Beispiel des autonomen Kreuzungsmanagements für Kraftfahrzeuge (Heinz Nixdorf Institute, University Paderborn, Dissertation, 2011) (in German)
18. S Gausemeier, K-P Jäker, A Trächtler, Multi-objective optimization of a vehicle velocity profile by means of dynamic programming (Paper presented at the 6th IFAC symposium on advances in automotive control (AAC), IFAC, Munich, Germany, 2010), pp. 366-371. doi:10.3182/20100712-3-DE-2013.00167
19. K Dresner, P Stone, A multiagent approach to autonomous intersection management. J. Artif. Intell. Res. 31, 591-656 (2008)
20. K Dresner, P Stone, Multiagent traffic manage: a reservation-based intersection control mechanism (The Third Joint Conference on Autonomous Agents and Multiagent Systems, New York, USA, 2004), pp. 530-537
21. T-C Au, P Stone, Motion Planning Algorithms for Autonomous Intersection Management, in AAAI Workshop on Bridging the Gap Between Task and Motion Planning (BTAMP) (Association for the Advanced Artificial Intelligence (AAAI), Atlanta, USA, 2010). ISBN 978-1-57735-492-5
22. AA Trani, Traffic flow models, lecture notes on introduction to transportation engineering (Virginia Polytechnic Institute and State University, Blackburg, Virginia, USA, Fall, 2009)
23. LH Immers, S Logghe, Traffic flow theory, lecture notes of the course basics of traffic engineering (Katholieke Universiteit Leuven, Belguim, 2002)

## Submit your manuscript to a SpringerOpen ${ }^{\text {® }}$ journal and benefit from:

- Convenient online submission
- Rigorous peer review
- Immediate publication on acceptance
- Open access: articles freely available online
- High visibility within the field
- Retaining the copyright to your article

Submit your next manuscript at » springeropen.com


[^0]:    * Correspondence: Chairit.wuthishuwong@hni.upb.de
    ${ }^{1}$ Heinz Nixdorf Institute, Control Engineering and Mechatronics Department, University Paderborn, Fürstenallee 11, Paderborn 33102, Germany Full list of author information is available at the end of the article

