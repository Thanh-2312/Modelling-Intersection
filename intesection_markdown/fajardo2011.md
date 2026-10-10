# Automated Intersection Control Performance of Future Innovation Versus Current Traffic Signal Control 

David Fajardo, Tsz-Chiu Au, S. Travis Waller, Peter Stone, and David Yang

Congestion is one of the biggest challenges faced by the transportation community; congestion accounted for an estimated $\mathbf{\$ 8 7 . 2}$ billion in losses in 2007 alone. Transportation professionals need to go beyond capacity expansion projects and explore novel strategies to mitigate traffic congestion. Automated intersection management is a novel strategy that has the potential to greatly reduce intersection delay and improve safety. Although the implementation of such a system is contingent on the development of automated vehicles, competitions such as the Grand Challenge and Urban Challenge of the Defense Advanced Research Projects Agency have shown that this technology is feasible and will be available. Therefore, the development of the infrastructure and associated control methods required to exploit fully the benefits of such technology at the system level is critical. This research explores one such innovative strategy, an automated intersection control protocol based on a first-come, first-served (FCFS) reservation system. The FCFS reservation system was shown to reduce intersection delay significantly by exploiting the features of autonomous vehicles. Microscopic simulation experimental results showed that the FCFS reservation system significantly outperformed a traditional traffic signal in reducing delay.

Because the ability of the transportation system to handle increased levels of demand has not matched population growth, congestion has become one of the most challenging engineering issues today. The roadway system is a source of mobility not only to drivers, but also to goods and services, and as such the ability for this system to handle vehicle demand is paramount to the economic development of the country. Traffic congestion accounted for an estimated $\$ 87.2$ billion in 2007 (1), and as the ability to build excess capacity has decreased, transportation professionals have been forced to look beyond capacity expansion-based approaches to address the issue of congestion.

FHWA's Exploratory Advanced Research program was established by the Safe, Accountable, Flexible, Efficient Transportation Equity Act-A Legacy for Users. The program focuses on longterm, high-risk research "with the potential for transformational improvements to plan, build, renew, and operate safe, congestion free, and environmentally sound transportation systems." This FHWA

[^0]program (www.fhwa.dot.gov/advancedresearch) addresses underlying gaps faced by applied highway research programs, anticipates emerging issues with national implications, and reflects broad transportation industry goals and objectives.

One Exploratory Advanced Research project being conducted is an examination of the feasibility of autonomous vehicles and intersections for the future. Research in the field of artificial intelligence and robotics in recent years has made the use of automated vehicles much more likely than in the past. Although the technology may not be at a stage warranting mass deployment of such vehicles now, it is clear that this technology will become the standard sooner rather than later. As such, it becomes important to begin to examine the consequences of what could be a major overhaul of traditional operational systems as the component of automation is introduced. Because congestion mitigation is an important societal problem, the operational efficiency derived from implementations aimed at exploiting the technological advantages of these automated vehicles warrants serious consideration.

Human error accounts for most vehicle crashes, and prevention of these crashes through automated driving is achievable but requires new systems to coordinate the movement of autonomous vehicles in complex traffic situations (2). This paper evaluates an automated intersection control mechanism called the first-come, firstserved (FCFS) protocol developed by Dresner and Stone (3). FCFS promises to process traffic much more efficiently than traffic signals, without compromising safety. Its development is guided by a set of criteria that includes the use of sensor technologies, the adoption of a standardized communication protocol, and the ability to deploy incrementally, allowing expansion to other intersections and adaptation to increasing numbers of autonomous vehicles. Absolute collision prevention, even under conditions of communications failure, is the primary goal for the system.

Although that previous work introduced the FCFS protocol and demonstrated its promise as a future intersection control mechanism, all of the testing was done against ad hoc signal timing and phasing plans. In addition to describing some refinements to the simulator and protocol, the main contribution of this paper is to validate the protocol against traffic signals that were optimized with the software package Synchro, which is generally accepted by the transportation community. Results further confirm the promise of the FCFS protocol.

## BACKGROUND

This section provides an overview of information relevant to this research: autonomous vehicles and their technological feasibility and the current state of technology, current practices in traditional
traffic signal design and optimization, automated intersection control and its potential benefits as an operational strategy, and microscopic simulation software and its role in numerical testing of operational strategies.

## Autonomous Vehicles

The engineering challenges concerning reliable computerized control of vehicles are well understood and solved mostly for perceptually simple situations. Vehicles can already be equipped with features of autonomy such as adaptive cruise control, Global Positioning System-based route planning (4, 5), and autonomous steering (6, 7). Since the late 1990s, adaptive cruise control systems have become standard optional equipment on luxury production vehicles of most of the major car manufacturers. Early adaptive cruise control systems can only slow down the vehicle when it is too close to the vehicle in front of it. But the capacity of adaptive cruise control systems has greatly improved since then. For instance, the adaptive cruise control systems on Mercedes-Benz S-Class and GM's Cadillac SLR can automatically maintain a safe following distance. Automatic parking is another autonomous feature that has already been commercialized. Today's automatic parking systems such as those in Toyota Prius and BMW can perform autonomous parallel parking with little or no human intervention. Some car manufacturers have already included other innovative autonomous features in their vehicles such as traffic sign recognition and lane departure warning systems. In 2008, GM was experimenting with a nearly autonomous vehicle under its European Opel brand (8). This prototype, the Opel Vectra, used a video camera, lasers, and substantial processing power to identify traffic signs, curves in the street, lane markings, and other vehicles. Early this year GM demonstrated a concept vehicle, EN-V, that has the ability to operate autonomously (9).

Meanwhile, the recent success of the Grand Challenge and Urban Challenge of the Defense Advanced Research Projects Agency (http://www.darpa.mil/grandchallenge/index.asp) suggests that fully autonomous vehicles are also on the horizon-in 2007, six autonomous vehicles completed the 60-mi course of suburban-type roadways with light traffic (10). In doing so, they demonstrated that it is currently possible to encode and act on traffic laws and precisely control an autonomous vehicle.

The use of autonomous vehicles has the potential to improve safety and mobility, reduce driving-related stress, increase freeway capacity, reduce emissions, and improve fuel efficiency. Furthermore, higher expected compliance levels with traffic instructions could improve system performance. Thus, once they are technologically feasible, there are many reasons for consumers to start using autonomous vehicles.

## Traditional Traffic Signals

Signal optimization methods aim to choose signal timing and phasing plans that achieve optimal values for specific intersection performance metrics, such as delay, throughput, and queue length. Intersection delay, defined as the amount of time the vehicle added to its travel time due to the presence of the intersection, is the most commonly used metric for evaluating the performance of intersections.

The operations of an intersection amount to a very complex system. As such, predicting intersection delay exactly is often infeasible. As a result, intersection delay is usually seen as a random variable. Traditional methods for estimating delay have relied on the use of ana- lytical equations that provide point estimates of delay, such as the expected value or specific percentiles. Once these analytical expressions have been determined, numerical methods can be used to obtain the optimal signal timing, phasing plan, or both. Although these mathematical programs are difficult to solve through exact methods because of their mathematical properties (nonlinearity, nondifferentiability), metaheuristics have been successfully implemented to determine good solutions.

Although signal optimization implementations have resulted in substantial operational improvements, there are fundamental limitations to the operational performance of a traditional intersection that stem from the need to address the safety issues arising from driving behavior, namely, the limited ability of drivers to process information and make subsequent decisions during the driving activity.

As such, intersections and their associated control devices have been limited to have a simple design and to minimize the number of simultaneous conflicting movements. The rules for navigating an intersection consist of a few elements of information, with many standard conventions limiting the number of decisions the driver has to make. For example, drivers are allowed to make only left or right turns from designated lanes and are never allowed to interfere with a lane containing through traffic. Another example is the use of protected left turns, which removes the need for drivers to evaluate whether gaps in oncoming traffic are appropriate for making a left turn.

Although some measures, such as turning lane conventions, do not significantly affect intersection performance, others, such as protected left turns, do significantly reduce the fraction of available intersection capacity that is actually used. As in many other transportation design problems, a balance must be reached between safety and operational efficiency.

## Autonomous Intersection Management

In parallel with independent, autonomous cars, infrastructure that is able to interact with these autonomous vehicles should be considered. The infrastructure will provide (a) a substitute for perception of the local environment, which is both computationally and monetarily expensive, and $(b)$ a tool for improving the overall system efficiency.

The central hypothesis of the present research is that the proposed form of intersection control can dramatically increase vehicle throughput on roads. The intersection control protocol presented in this research will be a major step toward the fully autonomous traffic infrastructure that will revolutionize the transportation of people and goods.

The introduction of autonomous drivers into a system allows for a greater degree of efficiency by removing the need for some of the safety-oriented features of traditional intersections. The operational efficiency that can be gained will be strongly influenced by the ability of the autonomous vehicle's driving mechanism to process information and navigate the vehicle. As technology continues to develop, one can expect that eventually autonomous vehicles will be vastly superior to human drivers in their ability to perform driving operations.

Another aspect that influences the design of intersections is the uncertain nature of driver behavior. Although individual drivers know what the trajectory of their vehicles will be, other drivers do not possess that information. As such, drivers must not only account for what they expect other drivers to do, they must also make decisions that are robust across all potential decisions other drivers may make. For example, a driver attempting to make a nonprotected left turn will decide whether a gap in oncoming traffic is acceptable on
the basis of the oncoming vehicles' current speed and also on how the gap will change if the vehicles begin to suddenly accelerate or decelerate.

Alternatively, a system in which driver decisions can be communicated directly to other vehicles, or to intersection-based infrastructure, allows for less conservative driving behavior as each vehicle can more accurately predict the trajectory of other vehicles in the intersection and can in turn better predict the viability of specific movements, thus improving intersection efficiency.

Automobiles in modern urban settings spend a great deal of time idling at intersections because of traffic congestion caused by inefficiency of traffic light systems and stop signs, generating harmful emissions and causing an increase in fuel use for no significant purpose.

According to a 2006 NHTSA report on traffic safety facts, intersection crashes account for about 40\% of the total crashes in the United States (11). In 2008, out of 37,261 fatalities on U.S. roadways, 7,772 occurred in an intersection or were intersection related (12). As intersections make up a very small portion of the roadway, this is a wildly disproportionate amount. Furthermore, collisions at intersections include a significant number of side-impact crashes, thus they frequently result in great injury and damage.

## Microscopic Simulation

To test the performance of automated intersection control protocols such as the one developed by the research team, the use of microscopic simulation models becomes indispensible. Because the technology for autonomous vehicles is currently not at the level needed for real-world testing of intersections with any meaningful amount of traffic flow, microscopic simulation software is necessary to obtain any estimate of the performance of the systems of such vehicles.

Microscopic simulation software packages are commonly used in the transportation field to evaluate operational strategies at a very high level of resolution. Software packages such as VISSIM (13), CORSIM (14), and SimTraffic (15) can realistically simulate the vehicle-to-vehicle interactions in a roadway system and allow transportation planners to generate estimates of performance metrics such as delay, throughput, and travel time.

Despite the great value that such software packages provide, the options offered in the programs are usually limited to existing transportation road elements and strategies. Furthermore, although some of these software packages do provide the user with some level of access to the internal data structures used for the simulation, this access is not enough to give the user the ability to incorporate the intersection control system presented in this paper. For these reasons, a microsimulator was coded from scratch so as to allow the research team to model the intersection control system developed and evaluate its performance.

## FCFS Intersection Control Protocol

Current intersection control mechanisms stem from the fact that they were designed to work with human-driven vehicles. When vehicles are driven by computers, there are opportunities to alleviate or resolve these issues by taking advantage of the capabilities of autonomous vehicles, wireless communication, and smart intersection management protocols. As laid out in detail in Dresner and Stone, an ideal autonomous intersection management protocol must satisfy seven desiderata: (a) allowance for fully distributed and autonomous control by the vehicles, (b) low communication complexity, (c) use of nonexpensive vehicle sensors found in production, ( $d$ ) use of a standardized communication protocol, ( $e$ ) incremental deployability, (f) safety, and (g) efficiency (3). Modern-day traffic signals completely satisfy all but the last one of these properties. Traffic signals are very inefficient-not only do vehicles traversing intersections equipped with these mechanisms experience large delays, but the intersections themselves can manage only a limited traffic capacity- much less efficient than the roads that feed into them. Therefore, we have investigated a solution that exceeds the efficiency of traffic signals without sacrificing any of the other properties.

## Reservation Idea

The aforementioned desiderata led to the development of an efficient intersection management system developed by Dresner and Stone that is a radical departure from existing traffic signal optimization schemes (3). The solution is based on a reservation paradigm, in which vehicles "call ahead" to reserve space-time in the intersection. In the approach, computer programs denoted as driver agents control the vehicles, and an arbiter agent called an intersection manager is assigned to each intersection. The role of the intersection manager is to grant or reject driver agent requests to reserve blocks of space-time in the intersection. In brief, the paradigm proceeds as follows (3):

- An approaching vehicle announces its impending arrival to the intersection manager. The vehicle indicates its size, predicted arrival time, velocity, acceleration, and arrival and departure lanes.
- The intersection manager simulates the vehicle's path through the intersection, checking for conflicts with the paths of any previously processed vehicles.
- If there are no conflicts, the intersection manager issues a reservation. It becomes the vehicle's responsibility to arrive at, and travel through, the intersection as specified (within a range of error tolerance).
- In the case of a conflict, the intersection manager suggests an alternate later reservation.
- The car may enter the intersection only when it has successfully obtained a reservation.
- On leaving the intersection, the car informs the intersection manager that its passage through the intersection was successful.

A key feature of this paradigm is that it relies only on vehicle-toinfrastructure communication. In particular, the vehicles need not know anything about each other beyond what is needed for local autonomous control (e.g., to avoid running into the car in front). The paradigm is also completely robust to communication disruptions: if a message is dropped, either by the intersection manager or by the vehicle, delays may increase, but safety is not compromised. Safety can also be guaranteed in mixed mode scenarios when autonomous and manual vehicles operate at intersections. The intersection efficiency will increase with the ratio of autonomous vehicles to manual vehicles in such scenarios.

## Intersection Control Policy

The present prototype intersection control policy divides the intersection into a grid of reservation tiles, as shown in Figure 1. (This notation can be generalized for rectangular and irregularly shaped

![](https://cdn.mathpix.com/cropped/9e5dd4e7-4597-423c-a9f1-ce1a4007408c-04.jpg?height=458&width=849&top_left_y=213&top_left_x=180)
FIGURE 1 Intersection divided into grid of reservation tiles: (a) successful (vehicle's space-time request has no conflicts at time $t$ ) and ( $b$ ) rejected (black vehicle's request is rejected because at time $t$ of its simulated trajectory, the vehicle requires a tile already reserved by another vehicle) (3).

intersections.) When a vehicle approaches the intersection, the intersection manager uses the data in the reservation request concerning the time and velocity of arrival, vehicle size, and so on to simulate the intended journey across the intersection. At each simulated time step, the policy determines which reservation tiles will be occupied by the vehicle.

If at any time during the trajectory simulation the requesting vehicle occupies a reservation tile that is already reserved by another vehicle, the policy rejects the driver's reservation request, and the intersection manager communicates this to the driver agent. Otherwise, the policy accepts the reservation and reserves the appropriate tiles. The intersection manager then sends a confirmation to the driver. If the reservation is denied, it is the vehicle's responsibility to maintain a speed such that it can stop before the intersection. Meanwhile, it can request a different reservation.

The issue of incremental deployability has been explored, but this variation of the FCFS system falls outside the scope of this paper. More information on the topic is found in Dresner and Stone (3).

## NUMERICAL TESTING: THE AIM4 SIMULATOR

Many traffic simulators are available for traffic purposes. Some of these simulators are designed to model vehicle kinematics with extremely high fidelity, including tire friction, engine power output, and even aerodynamics. Others deal with very large networks of roads or freeways, or model traffic flow instead of individual vehicles (16, 17). Many simulators are designed to model true human behavior, rather than testing custom agent algorithms (18). When this research began, however, none gave the ability to easily replace the mechanism by which intersections are governed. Because that is the main focus of this work, a custom simulator was required.

This section focuses on the features of the AIM4 simulator, with a concentration on its ability to model autonomous vehicles and automated intersections.

## Vehicle Representation

Each vehicle, although represented visually in the simulator as a rectangle with a fixed length and width, also possesses a vector of fixed properties and a vector of state variables.

At a bare minimum, vehicles in the simulator have the following fixed properties: vehicle identification number, length, width, front axle displacement, rear axle displacement, maximum velocity, maximum acceleration, minimum acceleration, maximum steering angle, maximum steering rate, sensor range, and transmission range. The front and back axle displacement, which represent the distance from the front of the vehicle to the front and back axle, respectively, and the maximum steering rate allow for more realistic limitations placed on the simulated vehicles during turning maneuvers.

Each vehicle also has the following state variables: position, velocity, heading, acceleration, steering angle. Position is represented in a Cartesian coordinate, in which the positive $x$-axis represents the east, and the positive $y$-axis represents the north. The heading, the direction a vehicle is facing, is represented as an angle, where zero radians would represent a vehicle driving east, and a vehicle with a positive steering angle $0<\psi<\pi / 2$ would be turning to the left.

## Vehicle Sensor Data

In real life an automated vehicle would be equipped with gauges designed to provide information from simulated sensors that the vehicle could have. Although an actual autonomous vehicle would have a multitude of outward-facing sensors, including laser range finders, short-wave radar, lidar, and video cameras, many of these technologies are either very difficult to simulate or do not make sense in the simulated environment. To operate safely in the simulated environment, it has been determined that a vehicle really needs to sense only one thing: how far away the next vehicle in front of it is. Which vehicle is the next vehicle in front may not be well defined, and so two sensors were created that try to answer that question: a simplified simulated laser range finder that can be used in any situation and an interval sensor that is much cheaper to use computationally, but can be used only when the vehicle is traveling within a lane.

## Simulated Laser Range Finder

To be able to simulate the complex workings of a full laser-range finder is not only computationally expensive, but also more detailed than necessary for microsimulation purposes. To address this issue, the laser range finder is implemented in the simulator by using a method introduced by Dresner and Stone (3). Although a single sensor aimed in the direction that the vehicle is moving can provide sufficient information when the vehicle is driving in a straight line, it is not enough to gather sufficient information during a turning movement. To address this problem, a flexible sensor is implemented in the simulator: when the vehicle is turning, the sensor's range increases in the direction of the turn, while it decreases from the opposite side. This treatment of sensors allows vehicles to avoid many collisions even in the absence of intersection control measures (3). The main drawback of this approach is that, unamortized, it requires $O\left(n^{2}\right)$ distance calculations just to determine which vehicles are in range of the sensor.

## Interval Sensor

Although the simulated laser finder is necessary in some complex driving scenarios, most of the time vehicles need only know the distance of the next vehicle in front of them. This determination can

![](https://cdn.mathpix.com/cropped/9e5dd4e7-4597-423c-a9f1-ce1a4007408c-05.jpg?height=838&width=838&top_left_y=217&top_left_x=185)
FIGURE 2 Screenshot of simulator in action (white vehicles are those with confirmed reservations; yellow vehicles are those without; blue vehicles are waiting for a confirmation or reject message from the intersection manager).

Task 2. Provide sensor input. For each vehicle, that vehicle's velocity, acceleration, heading, and position are recorded on the speedometer, accelerometer, compass, and position gauges, respectively. In addition, the interval gauge and simplified laser range finder are simulated, and the results are recorded on the corresponding gauges in the vehicle.

Task 3. Control vehicles. Vehicle controllers and intersection managers are given a chance to act after the vehicles' sensing inputs are updated.

Task 4. Deliver messages. Any messages in the vehicles' and the intersections' outgoing message queues are delivered to their destinations.

Task 5. Move vehicles. The positions, direction, and velocities of all vehicles are updated according to the simulator's physical model.

Task 6. Clean up. Any vehicle that has traveled outside the simulated area or has arrived at its intended destination is removed from the simulation.

Figure 2 shows a screenshot of the simulator's graphical display. The graphical interface shows not only the current state of the simulation but also the statistics of the simulation up to the current time step.

## DESCRIPTION OF TESTING PROCEDURE

The objective of this paper is to compare the performance of the FCFS intersection protocol with the performance of an optimized signal timing plan as generated by a standard signal optimization software package. Although several signal optimization software packages exist in the market, Synchro was chosen because of its common use by state agencies and private consulting agencies alike (22).

The hypothesis is that, by significantly decreasing the amount of lost time in the intersection, the intersection protocol presented in this paper will allow for much more efficient use of the time-space capacity of an intersection. The focus will be on the performance of an optimized signal plan and the automated intersection manager on a single three-lane, four-approach intersection. A more varied set of scenarios is desirable, but a validation of the model is impossible for 100\% of scenarios.

As such, the aim is to establish, at least for a common intersection configuration, whether or not the intersection manager outperforms a traditional intersection. A further aim is to identify the factors that affect the potential for improvement. In particular, the way performance varies with changes in the total volume per approach will be examined.

Two general sets of scenarios will be considered:

1. Two-phase intersection. Three levels of flow for the through movement at each of the four approaches of the intersection are considered: low [200 vehicles/hour (v/h)], medium (600 v/h), and high (1,000 v/h). The objective of this set of testing scenarios is to determine the effect that different combinations of overall level of congestion have on the performance of the intersection. Left-turn volume is kept at 100 v/h, and right-turn volume is kept at 200 v/h.
2. Three-phase intersection with single protected left turn. Five levels of flow for a single approach's left-turning volume (200, 400, 600, 800, 1,000 v/h) and four levels of flow for the opposing approach's through movement level of flow (400, 600, 800, 1,000 v/h) are considered. All other approaches are kept at 500 v/h for the through movement and 100 v/h for right- and left-turn movements. The objective of this set of testing scenarios is to determine how the conditions of the left-turning movement affect the performance of the intersection.

For each set of testing scenarios, four different intersection control strategies will be tested:

1. Traditional traffic signal optimized by using Synchro;
2. FCFS manager with 0.25-m static buffer, 0.1-s internal time buffer, and 0.25-s edge time buffer;
3. FCFS manager with 0.50-m static buffer, 0.2-s internal time buffer, and 0.50-s edge time buffer; and
4. FCFS manager with 0.75-m static buffer, 0.3-s internal time buffer, and 0.75-s edge time buffer.

## DISCUSSION OF RESULTS

The FCFS protocol significantly outperformed traditional signals in both sets of experiments conducted, regardless of the traffic pattern or selected set of safety buffers for the autonomous vehicles. Table 1 shows the results for the two-phase intersection experiment, and Table 2 shows results for the three-phase intersection experiment. In each case the null hypothesis that the average from the traditional signal $(Y)$ was less than or equal to the delays of the FCFS control $(X)$ was rejected, which allows one to conclude with great confidence that the FCFS reservation system significantly outperforms a traditional traffic signal in minimizing delay.

## Two-Phase Experiment

Although the FCFS protocol outperformed traditional signals in every scenario and for every set of buffers, the improvement in intersection
be made in the simulator by generating a list of vehicles and the distance from the start of the lane. Although it is possible for a vehicle to be in more than one lane, for example, during a lane-changing procedure, this situation can be accommodated in this system. Once the list of vehicles is sorted, the distances between the successive vehicles are calculated and recorded in the vehicles' interval sensor gauges. Instead of requiring $n^{2}$ time to complete, as with the laser range finder, this process takes only $O(n \log n)$ time. Instead of being able to simulate only tens of vehicles in real time, hundreds can be simulated.

## Safety Buffers

The AIM4 simulator makes use of three types of buffers to protect vehicles from moving too close to each other: ( $a$ ) a static buffer represents a constant size space around the vehicle (e.g., 0.5 m from each side of the vehicle) in which no other vehicle should be present at any time during the traversal of the intersection; (b) the internal time buffer adds additional space in the direction of travel that extends for $t$ seconds of driving distance, thus allowing the vehicle to arrive $t$ seconds early or late at the intersection; and (c) the edge time buffer creates a time gap of $t$ seconds at the edge of the intersection such that exiting vehicles have at least $t$ seconds of driving distance between them, thus preventing the vehicles from exiting too close to the previous vehicle.

## Communication

Each agent that can communicate has two queues of messages: an inbox and an outbox. Whenever an agent wants to send a message, it places it in the outbox. Synchronously, the simulator examines all agents' outboxes, takes any messages in them, and then conditionally delivers them to their destinations' inboxes. The next time the destination agents are able to act, they can examine their inboxes and take actions based on the messages present. Whether or not an individual message is delivered is a function of two factors: the transmission strength of the sending agent and the distance between the sending agent and the receiving agent. The location of an intersection, for these purposes, is the centroid of the intersection's area. For all experiments, a very simple function was used: the message is delivered if and only if the message strength is greater than or equal to the distance between the agents, although a stochastic model could easily be implemented.

One nice result of explicitly modeling communication (instead of using simple function calls, as in previous versions of the simulator) is that it allows one to do a mixed simulation. In a mixed simulation, one or more of the vehicles in the simulator is an actual physical vehicle. Each real vehicle corresponds to a proxy vehicle in the simulator whose state-position, velocity, and so forth-is continuously updated by using data from the real vehicle. The real vehicle's sensors are fed information from the simulator to make it appear to the real vehicle that the simulated vehicles are real. This enables one to run experiments involving real vehicles without risking expensive damage to the real vehicles should something go awry (19).

## Vehicle Controller

In every time step in a simulation, the AIM4 simulator updates the position, the direction, and the speed of every vehicle according to an approximate law of physics, as follows. On the basis of some simplifying assumptions, such as only planar motion is allowed and vehicles do not skid on a road, the state of a vehicle is updated by using the following differential equations for nonholonomic motion:

$$
\begin{aligned}
& \frac{\partial x}{\partial t}=v \cdot \cos (\phi) \\
& \frac{\partial y}{\partial t}=v \cdot \sin (\phi) \\
& \frac{\partial \phi}{\partial t}=v \cdot \frac{\tan \psi}{L}
\end{aligned}
$$

where

$$
\begin{aligned}
x, y, \text { and } \phi= & \text { coordinates and the direction of the vehicle, } \\
v= & \text { vehicle's velocity, } \\
\psi= & \text { steering angle, and } \\
L= & \text { vehicle's wheelbase (i.e., the length between the } \\
& \text { front wheels and the rear wheels). }
\end{aligned}
$$

Given $x, y, \phi, v$, and $\psi$ in the previous time step, the AIM4 simulator solves these equations and computes $x, y$, and $\phi$ in the next time step, assuming that $\psi$ remains constant in the time step and $v$ changes according to the acceleration $a$, which remains constant in the time step.

The vehicles' controllers control the motion of the vehicles by setting the acceleration $a$ and the steering angle $\psi$ at every time step, in the same way drivers in the real world control vehicles by gas pedal, brake, and steering wheel. In the previous version of the simulator, a vehicle controller computes the acceleration and the steering angle in every time step without planning ahead the entire course of actions for the traversal. This can cause some difficulties in meeting the arrival time and the arrival velocity requirement of the FCFS protocol (20, 21). In AIM4, vehicle controllers can optionally be given an acceleration schedule, track, or both to aid the control. An acceleration schedule is a time series of accelerations: $\left\langle\left(a_{1}, t_{1}\right)\right.$, $\left.\left(a_{1}, t_{2}\right), \ldots,\left(a_{n}, t_{n}\right)\right)$, which means that the controller should set the acceleration to $a_{i}$ at time $t_{i}$, for $1 \leq i \leq n$. In AIM4, when a vehicle sends a request to the intersection manager to make a reservation, the vehicle controller computes an acceleration schedule such that if it is followed correctly, the vehicle can arrive at the intersection at the arrival time and the arrival velocity stated in the request message. The use of an acceleration schedule can prevent vehicles from making reservations that are impossible to keep (20, 21). Likewise, a vehicle controller can control the steering angle by a given track, which is usually the middle of a lane or a precomputed trajectory in the intersection. The controller would then set the steering angle so as to stay as close to the track as possible.

## Simulation

The input of the simulator consists of a map, a detailed layout of the roads and intersections, and a specification of the vehicle generation at the vehicle spawn points. The simulation proceeds with a sequence of time steps; each of them represents a fixed amount of time $t$ (usually 0.02 s) in the simulation. At the beginning of each time step, the simulator performs a sequence of tasks as follows:

Task 1. Spawn vehicles. Vehicles are spawned according to an approximate Poisson process, except when there is no room in the lane.

TABLE 1 Delay for Two-Phase Experiment
| Flow by Approach (v/h) |  |  |  | Traffic Signals ( $Y$ ) |  | FCFS (0.25, 0.1, 0.25) ( $X_{25}$ ) |  |  | FCFS (0.50, 0.2, 0.50) $\left(X_{50}\right)$ |  |  | FCFS (0.75, 0.3, 0.75) $\left(X_{75}\right)$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  | Average <br> Delay (s) Delay (s) | SD (s) <br> SD (s) |  | SD (s) <br> SD (s) |  |  |  |  | Average <br> Delay (s) Delay (s) | SD (s) <br> SD (s) |  |
| EB | NB | SB | WB |  |  | Average <br> Delay (s) Delay (s) |  | $H_{0}: Y-X_{25} \leq 0 H_{A}: Y-X_{25}>0$ <br> $H_{A}: Y-X_{25}>0$ | Average <br> Delay (s) Delay (s) | SD (s) <br> SD (s) | $H_{0}: Y-X_{50} \leq 0 H_{A}: Y-X_{50}>0$ <br> $H_{A}: Y-X_{50}>0$ |  |  | $H_{0}: Y-X_{75} \leq 0 H_{A}: Y-X_{75}>0$ <br> $H_{A}: Y-X_{75}>0$ |
| 200 | 200 | 200 | 200 | 3.98 | 0.12 | 0.12 | 0.01 | Reject $H_{0}$ | 0.23 | 0.02 | Reject $H_{0}$ | 0.37 | 0.03 | Reject $H_{0}$ |
| 200 | 200 | 200 | 600 | 4.89 | 0.17 | 0.13 | 0.01 | Reject $H_{0}$ | 0.28 | 0.02 | Reject $H_{0}$ | 0.46 | 0.04 | Reject $H_{0}$ |
| 200 | 200 | 600 | 600 | 4.18 | 0.11 | 0.16 | 0.01 | Reject $H_{0}$ | 0.30 | 0.02 | Reject $H_{0}$ | 0.57 | 0.03 | Reject $H_{0}$ |
| 200 | 200 | 600 | 1,000 | 5.86 | 0.18 | 0.29 | 0.02 | Reject $H_{0}$ | 0.59 | 0.03 | Reject $H_{0}$ | 1.24 | 0.12 | Reject $H_{0}$ |
| 200 | 200 | 1,000 | 600 | 5.83 | 0.17 | 0.25 | 0.02 | Reject $H_{0}$ | 0.52 | 0.04 | Reject $H_{0}$ | 1.03 | 0.07 | Reject $H_{0}$ |
| 200 | 200 | 1,000 | 1,000 | 7.33 | 0.25 | 0.40 | 0.03 | Reject $H_{0}$ | 0.89 | 0.07 | Reject $H_{0}$ | 2.03 | 0.20 | Reject $H_{0}$ |
| 200 | 600 | 200 | 1,000 | 5.72 | 0.17 | 0.25 | 0.02 | Reject $H_{0}$ | 0.53 | 0.04 | Reject $H_{0}$ | 1.05 | 0.08 | Reject $H_{0}$ |
| 200 | 600 | 600 | 200 | 4.66 | 0.20 | 0.15 | 0.01 | Reject $H_{0}$ | 0.30 | 0.02 | Reject $H_{0}$ | 0.53 | 0.04 | Reject $H_{0}$ |
| 200 | 600 | 600 | 600 | 4.24 | 0.09 | 0.17 | 0.02 | Reject $H_{0}$ | 0.35 | 0.02 | Reject $H_{0}$ | 0.66 | 0.05 | Reject $H_{0}$ |
| 200 | 600 | 600 | 1,000 | 5.80 | 0.16 | 0.30 | 0.02 | Reject $H_{0}$ | 0.66 | 0.05 | Reject $H_{0}$ | 1.35 | 0.10 | Reject $H_{0}$ |
| 200 | 600 | 1,000 | 200 | 6.15 | 0.18 | 0.23 | 0.02 | Reject $H_{0}$ | 0.47 | 0.04 | Reject $H_{0}$ | 0.91 | 0.07 | Reject $H_{0}$ |
| 200 | 600 | 1,000 | 600 | 5.70 | 0.11 | 0.25 | 0.01 | Reject $H_{0}$ | 0.54 | 0.03 | Reject $H_{0}$ | 1.07 | 0.11 | Reject $H_{0}$ |
| 200 | 600 | 1,000 | 1,000 | 7.64 | 0.15 | 0.39 | 0.02 | Reject $H_{0}$ | 0.94 | 0.05 | Reject $H_{0}$ | 2.20 | 0.29 | Reject $H_{0}$ |
| 200 | 1,000 | 200 | 200 | 6.59 | 0.22 | 0.24 | 0.02 | Reject $H_{0}$ | 0.46 | 0.04 | Reject $H_{0}$ | 0.88 | 0.08 | Reject $H_{0}$ |
| 200 | 1,000 | 200 | 600 | 5.80 | 0.17 | 0.29 | 0.02 | Reject $H_{0}$ | 0.61 | 0.05 | Reject $H_{0}$ | 1.26 | 0.11 | Reject $H_{0}$ |
| 200 | 1,000 | 600 | 200 | 6.06 | 0.14 | 0.23 | 0.02 | Reject $H_{0}$ | 0.48 | 0.03 | Reject $H_{0}$ | 0.88 | 0.07 | Reject $H_{0}$ |
| 200 | 1,000 | 600 | 600 | 5.77 | 0.17 | 0.29 | 0.02 | Reject $H_{0}$ | 0.61 | 0.04 | Reject $H_{0}$ | 1.22 | 0.08 | Reject $H_{0}$ |
| 200 | 1,000 | 600 | 1,000 | 7.60 | 0.21 | 0.42 | 0.02 | Reject $H_{0}$ | 1.04 | 0.07 | Reject $H_{0}$ | 2.52 | 0.30 | Reject $H_{0}$ |
| 200 | 1,000 | 1,000 | 200 | 6.55 | 0.17 | 0.30 | 0.01 | Reject $H_{0}$ | 0.61 | 0.03 | Reject $H_{0}$ | 1.23 | 0.10 | Reject $H_{0}$ |
| 200 | 1,000 | 1,000 | 600 | 6.60 | 0.15 | 0.34 | 0.01 | Reject $H_{0}$ | 0.78 | 0.05 | Reject $H_{0}$ | 1.59 | 0.14 | Reject $H_{0}$ |
| 200 | 1,000 | 1,000 | 1,000 | 8.56 | 0.19 | 0.50 | 0.03 | Reject $H_{0}$ | 1.23 | 0.08 | Reject $H_{0}$ | 3.06 | 0.31 | Reject $H_{0}$ |
| 600 | 600 | 600 | 600 | 4.30 | 0.10 | 0.18 | 0.01 | Reject $H_{0}$ | 0.39 | 0.03 | Reject $H_{0}$ | 0.76 | 0.05 | Reject $H_{0}$ |
| 600 | 600 | 1,000 | 1,000 | 6.85 | 0.15 | 0.42 | 0.02 | Reject $H_{0}$ | 1.04 | 0.08 | Reject $H_{0}$ | 2.53 | 0.20 | Reject $H_{0}$ |
| 600 | 1,000 | 600 | 600 | 5.80 | 0.14 | 0.30 | 0.02 | Reject $H_{0}$ | 0.71 | 0.04 | Reject $H_{0}$ | 1.40 | 0.11 | Reject $H_{0}$ |
| 600 | 1,000 | 1,000 | 600 | 6.63 | 0.13 | 0.40 | 0.02 | Reject $H_{0}$ | 0.93 | 0.05 | Reject $H_{0}$ | 2.03 | 0.15 | Reject $H_{0}$ |
| 600 | 1,000 | 1,000 | 1,000 | 8.39 | 0.19 | 0.55 | 0.02 | Reject $H_{0}$ | 1.39 | 0.10 | Reject $H_{0}$ | 3.32 | 0.33 | Reject $H_{0}$ |
| 1,000 | 1,000 | 1,000 | 1,000 | 9.11 | 0.21 | 0.67 | 0.04 | Reject $H_{0}$ | 1.84 | 0.14 | Reject $H_{0}$ | 4.51 | 0.37 | Reject $H_{0}$ |


Note: $\mathrm{EB}=$ eastbound; $\mathrm{NB}=$ northbound; $\mathrm{SB}=$ southbound; $\mathrm{WB}=$ westbound; $\mathrm{SD}=$ standard deviation.

TABLE 2 Three-Phase, Protected Left-Turn Experiment
| Traffic Pattern |  | Traffic Signals ( $Y$ ) |  | FCFS (0.25, 0.1, 0.25) $\left(X_{25}\right)$ |  |  | FCFS ( $0.50,0.2,0.50$ ) ( $X_{50}$ ) |  |  | FCFS (0.75, 0.3, 0.75) $\left(X_{75}\right)$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Left Turn Volume | Opposite Approach Volume | Average Delay (s) | SD | Average Delay (s) | SD | $H_{0}: Y-X_{25} \leq 0 H_{A}: Y-X_{25}>0$ | Average Delay (s) | SD | $H_{0}: Y-X_{50} \leq 0 H_{A}: Y-X_{50}>0$ | Average Delay (s) | SD | $H_{0}: Y-X_{75} \leq 0 H_{A}: Y-X_{5}>0$ |
| 200 | 400 | 6.59 | 0.15 | 0.28 | 0.02 | Reject $H_{0}$ | 0.53 | 0.03 | Reject $H_{0}$ | 0.92 | 0.06 | Reject $H_{0}$ |
| 200 | 600 | 7.45 | 0.26 | 0.32 | 0.03 | Reject $H_{0}$ | 0.63 | 0.03 | Reject $H_{0}$ | 1.11 | 0.07 | Reject $H_{0}$ |
| 200 | 800 | 8.84 | 0.23 | 0.37 | 0.02 | Reject $H_{0}$ | 0.74 | 0.04 | Reject $H_{0}$ | 1.42 | 0.07 | Reject $H_{0}$ |
| 200 | 1,000 | 10.60 | 0.22 | 0.41 | 0.03 | Reject $H_{0}$ | 0.90 | 0.05 | Reject $H_{0}$ | 1.77 | 1.10 | Reject $H_{0}$ |
| 400 | 400 | 6.75 | 0.20 | 0.33 | 0.02 | Reject $H_{0}$ | 0.61 | 0.04 | Reject $H_{0}$ | 0.10 | 0.10 | Reject $H_{0}$ |
| 400 | 600 | 7.62 | 0.21 | 0.36 | 0.02 | Reject $H_{0}$ | 0.71 | 0.04 | Reject $H_{0}$ | 1.35 | 0.07 | Reject $H_{0}$ |
| 400 | 800 | 9.00 | 0.27 | 0.42 | 0.02 | Reject $H_{0}$ | 0.90 | 0.06 | Reject $H_{0}$ | 1.63 | 0.09 | Reject $H_{0}$ |
| 400 | 1,000 | 10.07 | 0.23 | 0.48 | 0.03 | Reject $H_{0}$ | 1.05 | 0.06 | Reject $H_{0}$ | 2.10 | 0.17 | Reject $H_{0}$ |
| 600 | 400 | 7.60 | 0.34 | 0.37 | 0.03 | Reject $H_{0}$ | 0.73 | 0.03 | Reject $H_{0}$ | 1.44 | 0.15 | Reject $H_{0}$ |
| 600 | 600 | 8.68 | 0.24 | 0.42 | 0.02 | Reject $H_{0}$ | 0.85 | 0.05 | Reject $H_{0}$ | 1.63 | 0.16 | Reject $H_{0}$ |
| 600 | 800 | 10.14 | 0.45 | 0.47 | 0.03 | Reject $H_{0}$ | 1.04 | 0.06 | Reject $H_{0}$ | 2.02 | 0.13 | Reject $H_{0}$ |
| 600 | 1,000 | 11.00 | 0.46 | 0.54 | 0.03 | Reject $H_{0}$ | 1.23 | 0.09 | Reject $H_{0}$ | 2.59 | 0.14 | Reject $H_{0}$ |
| 800 | 400 | 9.73 | 1.29 | 0.41 | 0.03 | Reject $H_{0}$ | 0.87 | 0.06 | Reject $H_{0}$ | 2.00 | 0.28 | Reject $H_{0}$ |
| 800 | 600 | 9.88 | 0.31 | 0.46 | 0.03 | Reject $H_{0}$ | 1.02 | 0.08 | Reject $H_{0}$ | 2.51 | 0.60 | Reject $H_{0}$ |
| 800 | 800 | 12.53 | 1.23 | 0.55 | 0.04 | Reject $H_{0}$ | 1.26 | 0.10 | Reject $H_{0}$ | 3.06 | 0.46 | Reject $H_{0}$ |
| 800 | 1,000 | 12.96 | 0.56 | 0.63 | 0.04 | Reject $H_{0}$ | 1.50 | 0.13 | Reject $H_{0}$ | 4.20 | 0.99 | Reject $H_{0}$ |
| 1,000 | 400 | 13.42 | 2.54 | 0.45 | 0.03 | Reject $H_{0}$ | 1.14 | 0.10 | Reject $H_{0}$ | 5.44 | 2.21 | Reject $H_{0}$ |
| 1,000 | 600 | 12.08 | 1.08 | 0.53 | 0.03 | Reject $H_{0}$ | 1.40 | 0.14 | Reject $H_{0}$ | 6.61 | 2.03 | Reject $H_{0}$ |
| 1,000 | 800 | 14.62 | 1.14 | 0.61 | 0.03 | Reject $H_{0}$ | 1.63 | 0.17 | Reject $H_{0}$ | 8.86 | 1.60 | Reject $H_{0}$ |
| 1,000 | 1,000 | 16.06 | 0.73 | 0.69 | 0.04 | Reject $H_{0}$ | 1.93 | 0.19 | Reject $H_{0}$ | 9.50 | 1.95 | Reject $H_{0}$ |


performance was affected by the set of buffers used, especially as levels of congestion increased. For the scenario with the lowest level of congestion, the FCFS protocol outperformed the traffic signal by an order of magnitude, with the average delays for the FCFS being under 0.4 s for all three sets of buffers. In the scenario with the highest level of congestion, the FCFS implementation with the least conservative buffers outperformed the traffic signal by an order of magnitude (0.67 s versus 9.11 s), yet the more conservative set of buffers was able to reduce delay only to an average of 4.51 s per vehicle. Although this improvement in performance is still significant compared with the traditional traffic signal, clearly the performance improvement is affected by the ability of the automated vehicle to sense information and accurately perform driving actions on the basis of the information. The results further show that determining the appropriate set of buffers is pivotal in the proper implementation of the FCFS protocol.

## Three-Phase Experiment

The FCFS implementations again outperform the traffic signal for all scenarios, but it is once again seen that the improvements from the FCFS implementation with more conservative buffers deteriorate much quicker with increasing flow than with less conservative buffers. Another interesting observation is that the variation between simulations for the same scenario increased much more significantly in the presence of increasing left-hand turns for the most conservative set of buffers, resulting in a standard deviation of 1.95 s, compared with a standard deviation of 0.37 s for the most congested case in the two-phase experiment.

Because left-turn movements increase the number of conflicts between opposing streams of traffic, it is expected that varying levels of left-turn flows would significantly affect the performance of traditional signals. As such, it is not surprising to see that left-turn volumes are also a significant factor for the performance of other intersection control systems such as FCFS.

An interesting corollary from the results of the three-phase experiment is that the network flow distribution in the form of route choice can have a significant effect on the performance of the system simply by affecting the distribution of left-turning movements per intersection: it may be beneficial to encourage vehicles to distribute left-turning vehicles among several intersections when possible.

## CONCLUSIONS AND FUTURE RESEARCH

A reservation-based intersection control protocol was tested against an optimized traditional traffic signal. Results show that the FCFS protocol performs significantly better than a traditional traffic signal, reducing average vehicle delay by an order of magnitude in all cases. It was observed, however, that varying levels of flow affected the observed levels of improvement for different implementations of FCFS, especially as the safety buffers used by the intersection manager became more conservative. It was further observed that the volume of left-turning vehicles would significantly affect the performance of traditional signals and FCFS.

The results are encouraging and show that further research must be conducted to enable deployment of such systems, as well as any other intelligent intersection control system, to exploit the benefits of automated vehicles. If the levels of performance observed in the numerical testing are achievable, the congestion mitigation effects an intersection management system such as FCFS could have would be enormous. Even the improvements seen from the most conservative set of buffers tested could more than halve the current estimated delay at intersections.

These results are promising, but they provide only a starting point for what should be a thriving research field. The following research directions will be taken, not only to validate further the FCFS intersection control strategy but also to develop more efficient intersection control systems:

- Although there is confidence that similar results will be observed regardless of the intersection configuration, a more thorough set of testing scenarios not only would provide validation, but also would allow for accurate prediction of expected delay reduction that could be achieved by replacing a traditional set of traffic signals with an automated intersection.
- It is important to be able to estimate average vehicle delays at the intersection level, but the network-level effects of such vehicle reductions are much more significant. Improved performance at a single intersection could potentially have a negative overall effect on the network if adjacent intersections are not prepared for the changes in traffic flow patterns, in traffic flow, or in both.
- The microsimulator used for testing procedures was custom developed for the testing of automated intersection management techniques. It can be confidently said that the simulator is realistic, but further validation of the simulator results would be desirable with the use of standard commercial packages. Because of the limitations of commercial microsimulation software, the process of validating the AIM4 simulator is a complex one, and to the authors' knowledge, there is no trivial validation process.


## ACKNOWLEDGMENTS

The authors acknowledge FHWA's Exploratory Advanced Research Program for funding this research. A portion of this work was conducted in the Learning Agents Research Group (LARG) of the Artificial Intelligence Laboratory, University of Texas at Austin. LARG research is supported in part by grants from the National Science Foundation, Office of Naval Research, Defense Advanced Research Projects Agency, and FHWA.

## REFERENCES

1. Schrank, D., and T. Lomax. Urban Mobility Report. Texas Transportation Institute. Texas A\&M University System, College Station. 2009. http://mobility.tamu.edu. Accessed July 30, 2010.
2. Wierwille, W. W., R. J. Hanowski, J. M. Hankey, C. A. Kieliszewski, S. E. Lee, A. Medina, A. S. Keisler, and T. A. Dingus. Identification and Evaluation of Driver Errors: Overview and Recommendations. Technical Report FHWA-RD-02-003. Virginia Polytechnic Institute and State University, Blacksburg, 2002.
3. Dresner, K., and P. Stone. A Multiagent Approach to Autonomous Intersection Management. Journal of Artificial Intelligence Research, Vol. 31, March 2008, pp. 591-656.
4. Rogers, S., C. N. Flechter, and P. Langley. An Adaptive Interactive Agent for Route Advice. Proc., 3rd International Conference on Autonomous Agents (Agents'99) (O. Etzioni, J. P. Muller, and J. M. Bradshaw, eds.), Seattle, Wash., Association for Computing Machinery, New York, 1999, pp. 198-205.
5. Schonberg, T., M. Ojala, J. Suomela, A. Torpo, and A. Halme. Positioning an Autonomous Off-Road Vehicle by Using Fused DGPS and Inertial Navigation. Proc., 2nd IFAC Conference on Intelligent Autonomous Vehicles, Espoo, Finland, Pergamon Press, Oxford, United Kingdom, 1995, pp. 226-231.

6. Pomerleau, D. A. Neural Network Perception for Mobile Robot Guidance. Kluwer Academic Publishers, Norwell, Mass., 1993.
7. Reynolds, C. W. Steering Behaviors for Autonomous Characters. Proc., Game Developers Conference, San Jose, Calif., Miller Freeman Game Group, San Francisco, Calif., 1999, pp. 763-782.
8. Squatriglia, C. GM Says Driverless Cars Could Be on the Road by 2010. Wired Magazine. 2008. http://www.wired.com/autopia/2008/01/gm-saysdriverl.
9. General Motors. GM Unveils EN-V Concept: A Vision for Future Urban Mobility. 2010. http://www.gizmag.com/gm-en-v-concept-vehicle/ 14617/.
10. Buehler, M., K. Iagnemma, and S. Singh. Editorial. Journal of Field Robotics, Vol. 25, No. 8, Special Issue on the 2007 DARPA Urban Challenge, Part I, Aug. 2008, pp. 423-424.
11. NHTSA. Traffic Safety Facts 2006: A Compilation of Motor Vehicle Crash Data from the Fatality Analysis Reporting System and the General Estimates System. National Center for Statistics and Analysis, National Highway Traffic Safety Administration, U.S. Department of Transportation, 2006.
12. Federal Highway Administration Safety Program, FHWA, U.S. Department of Transportation, Intersection Safety. http://safety.fhwa.dot.gov/ intersection/.
13. VISSIM User Manual-V.3.70. PTV, Karlsruhe, Germany, 2003.
14. CORSIM User's Guide, Version 1.03. KAMAN Science Corporation, Alexandria, Va., 1997.
15. Husch, D. SimTraffic User's Guide. Trafficware, Berkeley, Calif., 1998
16. Sukthankar, R., D. Pomerleau, and C. Thorpe. SHIVA: Simulated Highways for Intelligent Vehicle Algorithms. Proc., 1995 IEEE Intelligent Vehicles Symposium, IEEE, Piscataway, N.J., 1995.
17. Helbing, D., A. Hennecke, V. Shvetsov, and M. Treiber. MASTER: Macroscopic Traffic Simulation Based on a Gas-Kinetic, Nonlocal Traffic Model. Transportation Research Part B, Vol. 35, No. 2, 2001, pp. 183-211.
18. Caliper Corporation. Transmodeler. 2009. http://www.caliper.com/ transmodeler/Simulation.htm.
19. Nimmagadda, T. Building an Autonomous Ground Traffic System. Technical Report HR-09-09. University of Texas at Austin, 2009.
20. Quinlan, M., T.-C. Au, J. Zhu, N. Stiurca, and P. Stone. Bringing Simulation to Life: A Mixed Reality Autonomous Intersection. Proc., IROS 2010-IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2010), Taipei, Taiwan, IEEE, Piscataway, N.J., 2010.
21. Au, T.-C., and P. Stone. Motion Planning Algorithms for Autonomous Intersection Management. Proc., AAAI 2010 Workshop on Bridging the Gap Between Task and Motion Planning (BTAMP), Atlanta, Ga., Association for the Advancement of Artificial Intelligence, Menlo Park, Calif., 2010.
22. Husch, D., and J. Albeck. Trafficware Synchro 6 User Guide. Trafficware, Albany, Calif., 2004.

The Traffic Signal Systems Committee peer-reviewed this paper.


[^0]:    D. Fajardo, 6.202 ECJ Hall, and S. T. Waller, 6.204 ECJ Hall, Department of Civil Engineering, University of Texas, Austin, TX 78712. T.-C. Au, and P. Stone, Department of Computer Science, University of Texas, 1616 Guadalupe, Suite 2.408, Austin, TX 78701. D. Yang, Office of Operations Research and Development, Turner-Fairbank Highway Research Center, FHWA, U.S. Department of Transportation, 6300 Georgetown Pike, McLean, VA 22101. Corresponding author: D. Fajardo, davidf@mail.utexas.edu.

