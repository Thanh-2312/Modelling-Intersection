# Paradoxes of reservation-based intersection controls in traffic networks 

Michael W. Levin *, Stephen D. Boyles, Rahul Patel<br>Department of Civil, Architectural, and Environmental Engineering, The University of Texas at Austin, United States

ARTICLE INFO

Article history:
Received 22 July 2015
Received in revised form 28 December 2015
Accepted 5 May 2016

Keywords:
Autonomous vehicles
Reservation-based intersection control
Dynamic traffic assignment
Paradoxes


#### Abstract

Reservation-based intersection control is a revolutionary idea for using connected autonomous vehicle technologies to improve intersection controls. Vehicles individually request permission to follow precise paths through the intersection at specific times from an intersection manager agent. Previous studies have shown that reservations can reduce delays beyond optimized signals in many demand scenarios. The purpose of this paper is to demonstrate that signals can outperform reservations through theoretical and realistic examples. We present two examples that exploit the reservation protocol to prioritize vehicles on local roads over vehicles on arterials, increasing the total vehicle delay. A third theoretical example demonstrates that reservations can encourage selfish route choice leading to arbitrarily large queues. Next, we present two realistic networks taken from metropolitan planning organization data in which reservations perform worse than signals. We conclude with significantly positive results from comparing reservations and signals on the downtown Austin grid network using dynamic traffic assignment. Overall, these results indicate that network-based analyses are needed to detect adverse route choices before traffic signals can be replaced with reservation controls. In asymmetric intersections (e.g. local road-arterial intersections), reservation controls can cause several potential issues. However, in networks with more symmetric intersections such as a downtown grid, reservations have great potential to improve traffic.


© 2016 Elsevier Ltd. All rights reserved.

## 1. Introduction

Connected autonomous vehicles (CAVs), which are currently in testing on public roads, offer several new technologies that could revolutionize traffic operations. Cooperative adaptive cruise control (Van Arem et al., 2006), using short range communications between CAVs, can reduce following headways to increase capacity (Kesting et al., 2010; Shladover et al., 2012) and stability (Schakel et al., 2010). On the other hand, empty repositioning trips could greatly increase vehicular traffic demand, resulting in a net increase in congestion despite these capacity increases (Levin and Boyles, 2016). However, further optimizations have been proposed. Dynamic lane reversal (Hausknecht et al., 2011) could optimize lane configurations for dynamic traffic demand to maximize road usage. Reservation-based intersection control (Dresner and Stone, 2004, 2006), which is the focus of this paper, is a radical intersection control mechanism that takes advantage of the reduced safety margins necessary for CAVs to increase use of the intersection capacity. Comparisons of reservations against signals on a

[^0]single intersection using the first-come-first-serve (FCFS) policy have indicated that for some situations reservations may reduce delays for all vehicles beyond optimized signals (Fajardo et al., 2011; Li et al., 2013).

While these results are promising, they represent only a subset of potential scenarios. Braess (1968) and Daganzo (1998) paradoxes demonstrate that capacity improvements may increase travel times for all vehicles. Furthermore, policy goals such as the fairness of FCFS may be less efficient for the overall system. Thus far, no literature has presented negative comparisons of reservations with traffic signals. The primary purpose of this paper is to demonstrate that such situations exist to motivate the necessity for greater study before replacing signals with reservations. We present several paradoxical situations in which traffic signals outperform FCFS reservations. From a policy standpoint, it is important to recognize situations in which replacing signals with reservation-based controls may increase delays or congestion.

Although many previous studies have used FCFS for prioritizing vehicles, the reservation protocol is general enough to admit a large range of policies such as intersection auctions (Schepperle and Böhm, 2007). However, this range makes it impossible to generalize our studies to arbitrary policies. Indeed, as Dresner and Stone (2007) note, traffic signals may be viewed as a specific case of the general reservation protocol. Accordingly, there is always a reservation policy that performs identically to current signal technology. Therefore, the examples in this paper are based on the FCFS policy. It is the focus of most of the literature on reservation-based control (Dresner and Stone, 2004; Fajardo et al., 2011; Li et al., 2013), etc. Also, because of its inherent fairness, FCFS is a good candidate for a widely accepted control policy. We also discuss how the theoretical issues with FCFS reservations may extend to more general classes of reservation policies.

The contributions of this paper are to present and characterize several scenarios in which the use of FCFS-based reservations results in greater delays than signals. We present three theoretical examples, including a temporarily saturated arterial-local road intersection to a demonstration that replacing signals with reservations can result in infinite queuing. Finally, we solve dynamic traffic assignment (DTA) on a city network, and find that reservations significantly reduce travel time. Overall, these results demonstrate that while reservations perform better than traffic signals in certain situations, network-based analyses are necessary to detect adverse route choices before reservations can be used to replace signals entirely. In particular, asymmetric intersections (e.g. local road-arterial intersections) can cause several potential issues with reservation controls. However, based on the city network results, reservations have great potential for improving traffic.

The remainder of this paper is organized as follows. Section 2 describes previous work on reservation-based controls. Section 3 presents three theoretical examples in which signals outperform FCFS, and Section 4 contains results on realistic networks. We conclude in Section 5.

## 2. Reservation-based protocol

This section describes the tile-based reservation protocol introduced by Dresner and Stone (2004) and Dresner and Stone (2006) and the conflict region simplification proposed by Levin and Boyles (2016). The latter is tractable for large DTA networks and is also a more intuitive method of describing the behavior reservation protocol. Therefore, it is used in the theoretical examples and the DTA simulations. Finally, we discuss properties of the FCFS policy that is the focus of most literature on reservation-based control methods.

### 2.1. Tile-based reservations

The tile-based reservation protocol proposed by Dresner and Stone $(2004,2006)$ operates through an intersection manager agent communicating wirelessly with individual vehicles. The intersection manager divides the intersection into a grid

![](https://cdn.mathpix.com/cropped/c5a1da81-f4c9-4b6c-a9f4-ddca5a1078b6-02.jpg?height=586&width=1136&top_left_y=1761&top_left_x=367)
Fig. 1. Tile-based reservation protocol (Fajardo et al., 2011).

of space-time tiles, illustrated in Fig. 1. Vehicles request a reservation from the intersection manager, which simulates the vehicle's desired path through the grid. If no conflicts occur, the reservation may be accepted. Otherwise, the reservation of one or more of the conflicting vehicles must be rejected. Vehicles must know their arrival time at the intersection to request to enter the intersection at a specific time.

A major question for reservation controls is which vehicle's reservation should be accepted when requests conflict. Dresner and Stone (2004) suggested prioritizing on a first-come-first-serve (FCFS) basis for fairness. However, the question of vehicle priority admits a wide range of potential policies. Dresner and Stone (2006) suggested giving higher priority to emergency vehicles, and the use of intersection auctions to determine priority has been found to improve over FCFS by Schepperle and Böhm (2007), Vasirani and Ossowski (2010, 2012), and Carlino et al. (2013). Nevertheless, later studies comparing reservations with signals (Fajardo et al., 2011; Li et al., 2013) focused on FCFS and found that FCFS could reduce delays beyond optimized signals. However, as we will show in Section 3, in some situations signals will perform better than FCFSbased reservations.

Although the original reservation protocol was designed exclusively for CAVs, modified protocols may admit human drivers as well at the cost of some efficiency. Dresner and Stone $(2006,2007)$ suggested providing human drivers an occasional signal cycle, and Conde Bento et al. (2013) and Qian et al. (2014) studied methods to integrate human drivers into the reservation system itself without requiring direct communications with the intersection manager. These studies suggest that reservation-based protocols may be practical before all vehicles on public roads are CAVs. Nevertheless, for this paper we will focus on the scenario in which all vehicles are CAVs to avoid complicating the intersection control with human drivers.

### 2.2. Conflict region simplification

Because of the computational requirements of the tile-based reservation protocol, studies of reservations have been limited to small number of intersections (Hausknecht et al., 2011) or have made simplifications that greatly reduced its efficiency (Carlino et al., 2012). However, as we will demonstrate in Section 3.3, modeling reservation controls when solving DTA is necessary for determining whether it improves traffic. The conflict region simplification of the tile-based reservation protocol (Levin and Boyles, 2016) provides a computationally tractable method for simulating reservation-based intersections in DTA on a city network scale. Although the conflict region model loses some of the tile arrival time complexities, it is sufficient for the simple turning movements considered in the theoretical examples in this paper. It also provides a more intuitive method of analyzing the long-term behavior of the reservation protocol.

An example of such conflict regions is given in Fig. 2 (the dashed lines are lane markings). Every turning movement passes through a different set of conflict regions, with each conflict region limited by capacity. Conflicting turning movements are restricted by the capacity of the conflict region(s) in which they intersect. Each vehicle on turning movement $(i, j)$ passes through some set of conflict regions $C_{i j}$. To reserve the turning movement requires capacity of $\frac{Q_{c}}{Q_{i}}$ for all $c \in C_{i j}$, where $Q_{i}$ is the capacity of link $i$ and $Q_{c}=\max _{(i, j) \mid c \in C_{i} j} Q_{i}$. This capacity scaling models how, for example, a single vehicle on a local road crossing a major arterial could block multiple vehicles from moving along the arterial.

This model is more intuitive for understanding intersection capacity than either the tile-based or conflict-point reservation models, although the latter two are useful for practical implementation. It also results in a polynomial-time intersection flow algorithm tractable for solving DTA on city networks (Levin and Boyles, 2016). Therefore, we use the conflict region model for our theoretical examples and DTA results.

![](https://cdn.mathpix.com/cropped/c5a1da81-f4c9-4b6c-a9f4-ddca5a1078b6-03.jpg?height=598&width=598&top_left_y=1741&top_left_x=651)
Fig. 2. Conflict region representation of four-way intersection.

![](https://cdn.mathpix.com/cropped/c5a1da81-f4c9-4b6c-a9f4-ddca5a1078b6-04.jpg?height=234&width=220&top_left_y=185&top_left_x=820)
Fig. 3. Network for Section 3.1.

### 2.3. First-come-first-serve policy

FCFS is a fairness-based method for accepting reservations that has been used in most previous studies. When a vehicle requests a reservation, the intersection manager accepts it if it does not conflict with previously accepted reservations. Otherwise, it is rejected, and the intersection manager advises a later possible time (Fajardo et al., 2011). Equivalently, the vehicle is delayed until it can safely make its desired turning movement.

Although simple, the definition of FCFS results in some important properties that are exploited in the paradoxes of reservation-based control:

1. Vehicles are prioritized by when they first requested a reservation, independent of external costs imposed on other vehicles. Vehicles with lower priority that have fewer conflict separation limitations could move before vehicles with higher priority that are blocked due to conflicts. However, traffic signals often give higher priority to vehicles with fewer conflict separation limitations, such as vehicles making right turns or on major arterials. This is exploited in Section 3.1.
2. Reservation request time may not be the same as time spent queued or other intuitive measures. Vehicles cannot request a reservation unless they can execute it. Therefore, vehicles in a queue, or at the back of a platoon, may not request a reservation until they are able to enter the intersection. A road with more lanes may correspondingly obtain a greater share of the intersection capacity because the vehicle at the front of each lane can request a reservation. Also, vehicles on a long low-traffic road may be able to request a reservation long before reaching the intersection, because in free-flow conditions their arrival time at the intersection is known. This is exploited in Section 3.2.
3. If one vehicle's request is accepted, other requests that do not conflict may also be accepted. This may result in vehicles moving in an order that is different from the order of their reservation requests.
For instance, in the four-approach intersection in Fig. 2, suppose there are 3 vehicles, each at the front of their lane: vehicle 1 requests to move north-south through the intersection, vehicle 2 requests to move east-west, and vehicle 3 requests to move south-north (in that order). Vehicle 1's reservation is accepted due to priority. Vehicle 2's reservation is rejected due to conflict with vehicle 1. Vehicle 3's reservation is then accepted because it does not conflict with vehicle 1. Vehicles 1 and 3 move at the same time, and vehicle 2 moves after.

## 3. Theoretical examples

This section presents three examples in which FCFS reservations are less efficient than signals. First, we show that the fairness of FCFS can increase total vehicle delay for asymmetric intersections. Next, we discuss how reservations can disrupt platoon progression that is possible through optimally timing signals on a corridor. Finally, we demonstrate that replacing a signal with a reservation control can lead to arbitrarily large increases in queue size due to selfish route choice.

### 3.1. Greater total delay due to fairness

We first present a simple example of a temporarily oversaturated arterial-local road intersection. Clearly, some vehicles must be delayed due to crossing conflicts. We show that the fairness goal of FCFS results in greater total delay. Consider the intersection A shown in Fig. 3. As described in Table 1, links 1 and 2 form a three-lane arterial with total capacity of 3600 vph. Links 3 and 4 form a one-lane local road with capacity 1200 vph. Using a time step of 6 s, which is typical for the cell transmission model (Daganzo, 1994, 1995) used in simulation-based DTA, each time step six vehicles can move from link 1 to link 2, or two vehicles from link 3 to link 4, or any convex combination. Because the local road has lower capacity, moving one vehicle from link 3 to link 4 reserves a capacity equivalent to moving three vehicles from link 1 to link 2.

Table 1
Link parameters for Section 3.1.
| Link travel time (s) | Free flow | Capacity (vph) | Demand per timestep (first 2 time steps) |
| :--- | :--- | :--- | :--- |
| 1, 2 | 18 | 3600 | 6 vehicles |
| 3, 4 | 18 | 1200 | 2 vehicles |


The fairness property of FCFS can be exploited to cause greater delays. Suppose that for the first two time steps, demand for moving from link 1 to link 2 is six vehicles per time step, and demand for moving from link 3 to link 4 is two vehicles per time step. There is no demand after two time steps. Intersection A has greater demand than capacity in the first two time steps. Since the demand is finite, all demand will be served after four time steps, but some demand will be delayed. Which vehicles are delayed depends on the intersection control, and we show that the fairness of FCFS reservations is less efficient for the system.

For a traffic signal, the majority of green time may reasonably be given to the major approach - arterial links 1 and 2. Therefore, the typical pattern of vehicle movement with signals is as follows: during the first two time steps, six vehicles per time step move from link 1 to link 2. Those vehicles do not experience any delay. During the next two time steps, two vehicles per time step move from link 3 to link 4. Those vehicles are each delayed by two time steps, or 12 s. This results in a total vehicle delay of 48 s.

For FCFS reservations, vehicles are prioritized according to their waiting time. Therefore, the pattern of vehicle movement is to move three vehicles from link 1 to link 2 and one vehicle from link 3 to link 4 each time step. This is due to the fairness attribute of FCFS: the queues on links 1 and 3 alternate between having the longest waiting vehicle. The greater delay results from the fact that when one vehicle moves from link 1 to link 2, two other vehicles can move with it due to the greater capacity of the arterial. The vehicles moving in time steps 2 and 3 are each delayed by one time step, and the vehicles moving in time step 4 are delayed by two time steps. This results in a total vehicle delay of 96 s. Note that this delay does not include the additional time required for vehicles to start moving from a full stop. For signals, vehicles on the arterial need not stop at all, but for FCFS, most of the vehicles experience some delay and might slow down accordingly.

These results occur despite asymmetric lane configuration. As mentioned in the second property of FCFS (Section 2.3), vehicles at the front of their lane know with certainty their arrival time at the intersection, and can therefore make a reservation sooner than vehicles behind. Although the arterial has more lanes than the local road, vehicles on the local road are still able to block vehicles on the arterial.

Previous work by Fajardo et al. (2011) and Li et al. (2013), which found that FCFS reduced delays beyond optimized signals, only studied symmetric intersections in which each approach had the same capacities and number of lanes. This example demonstrates that for asymmetric intersections, FCFS increases total delay for some demand scenarios. The greater delay results from how signals are likely to delay vehicles on the local road longer to service vehicles on the arterial. On the other hand, FCFS seeks fairness in waiting time, which results in less delay for some vehicles on the local road but greater total delay. The fact that only a single simple intersection, with a small and common demand scenario, is sufficient to increase total delay suggests that this type of situation may be common when replacing signals with FCFS reservations. Of course, policies besides FCFS may address this issue, and we discuss these further in Section 4.

### 3.2. Disruption of platoon progression

This scenario extends the previous example to a two intersection network in which FCFS disrupts signal progression on an arterial, resulting in greater total delay. Consider the network shown in Fig. 4 with link parameters in Table 2. The network consists of an arterial (links 1, 2, and 3) intersected by two local roads (links 4 and 5 and links 6 and 7). Demand is as follows: at time 0 , six vehicles start traveling the path [1,2,3]. At time 6, two vehicles start traveling the path [6,7]. Assume that no other demand is present. Therefore, all vehicles will experience free flow until reaching intersection B, at which point some vehicles must be delayed due to the crossing conflict.

When signals are used at A and B, the signals may be timed to allow progression along the arterial. Thus the six vehicles on path [1,2,3] experience free flow whereas the vehicles on path [6,7] are delayed by 6 s, for a total vehicle delay of 12 s.

For reservation controls, vehicles may request a reservation at the next intersection as soon as they can know their arrival time there. It is reasonable to assume that vehicles will not request a reservation at an intersection until they enter an incoming link to that intersection, i.e. vehicles on link 1 traveling on path [1,2,3] will not request a reservation at B. There are several reasons why vehicles might do this. First, unforeseen circumstances at intersection A, such as jaywalking pedestrians, might delay vehicle movement across A. Second, vehicles using adaptive routing to respond to congestion may not want to commit themselves to a turning movement at B before getting closer to ascertain traffic conditions on outgoing links of B. Even without this assumption, it is trivial to add additional demand on link 2 that prevents the vehicles on path [1,2,3] from requesting a reservation at B until entering link 2. Under this condition, we find that reservations increase the total delay.

When reservations are used, the vehicles on path [6,7] can request a reservation at B at time 6, when they enter link 6, because the link is at free flow. However, the vehicles on path [1,2,3] cannot request a reservation until time 12, when they enter link 2. With a time step of delay between reservations, any reservation policy that does not account for future reservation requests - such as FCFS - will grant the requests of vehicles on path [6,7] because no conflicts are present at the time those requests are made. Therefore, none of the six vehicles on path [1,2,3] can cross B at time 24. This delays those vehicles by 1 time step, resulting in a total vehicle delay of 36 s.

Delaying acceptance of the reservation request until vehicles have moved closer to the intersection may not completely solve the issue. In practice, more complex reservation policies such as auctions must wait to collect all requests before making a decision. However, the difference of 6 s in submitting reservation requests in this example could easily be made greater

![](https://cdn.mathpix.com/cropped/c5a1da81-f4c9-4b6c-a9f4-ddca5a1078b6-06.jpg?height=280&width=435&top_left_y=185&top_left_x=721)
Fig. 4. Network for Section 3.2.

Table 2
Link parameters for Section 3.2.
| Link | Free flow travel time (s) | Capacity (vph) |
| :--- | :--- | :--- |
| 1, 2, 3 | 12 | 3600 |
| 4, 5, 6, 7 | 18 | 1200 |


by extending the length of the local road. Furthermore, vehicles may have to make late reservation requests due to traffic in front, which reduces the margins the intersection manager has for delaying acceptance.

If the reservation policy were to anticipate future reservation requests, it could avoid this situation. Traffic signals can "anticipate" these future requests by timing cycles to allow for progression. Therefore any reservation policy that operates only on existing reservations, such as FCFS or auctions, will grant vehicles on path [6,7] the reservation before vehicles on path [1,2,3] have even submitted their request. Another way to handle this type of situation is to retroactively deny a reservation. This adds complexity to the protocol: the vehicle with a previous reservation must confirm that it will not execute it. This could be useful to warn vehicles of impending hazards such as pedestrians or collisions. However, selfish vehicle programming might choose to ignore the retroactive denial message if used to shift reservation priorities to game the system. Retroactive denial would also introduce potential safety issues.

### 3.3. Arbitrarily large queues due to route choice

In the previous two examples, FCFS caused greater delays due to being less optimized for the network structure than traffic signals. This example combines that lack of optimization with selfish route choice to cause potentially infinite queuing. We make the typical assumption of DTA that vehicles choose routes to minimize their own travel time. This results in a dynamic user equilibrium: a route assignment in which no vehicle can improve travel time by changing routes. This Wardrop (1952) equilibrium has been shown to cause paradoxes in which network improvements increase travel time for all vehicles (Braess, 1968; Daganzo, 1998). This scenario is perhaps the most difficult to avoid because to do so requires some additional delay or toll on the local road, even when there is no conflicting demand from the arterial.

We present a network based on Daganzo's paradox (Daganzo, 1998) in which replacing a signal with a FCFS reservationbased control results in potentially infinite queuing. Consider the four link network shown in Fig. 5 with link parameters shown in Table 3. Vehicles can take arterial link 2 or local road 3 to travel between B and C. Assume that turning movements from links 2 and 3 to 4 conflict at C, i.e. 2400 vph may travel from 3 to 4, or 1200 vph from 2 to 4, or any convex combination. Also assume that the diverge at B has sufficient capacity to support any turning proportion split. Suppose that demand from A to D is 1800 vph. Since link 2 is an arterial, suppose intersection C is controlled by a signal with considerable delays for vehicle traveling from 3 to 4: the cycle is 60 s for movement from 2 to 4 then 10 s for movement from 3 to 4. Because of the average delay of nearly 30 s from the signal for vehicles traveling from 3 to 4, path [1,3,4] has an average travel time of around 170 s . In contrast, path [1,2,4] has an average travel time of around 140 s. Therefore, when all demand takes path [1,2,4], it is an equilibrium, and the network is nearly at free flow.

Now suppose that the signal at C is replaced with a reservation control using the FCFS policy. Because of the fairness attribute of FCFS, the expected delay for vehicles moving from 3 to 4 is small: they can expect to alternate with vehicles moving from 2 to 4. Because of this, all demand on path [1,2,4] is not an equilibrium, because path [1,3,4] has a travel time that is only slightly higher than 120 s - lower than the free flow time of path [1,2,4]. On the other hand, all demand on path [1,3,4] is an equilibrium. Vehicles reaching B are presented with the choice of taking link 2, with its free flow time of 80, or link 3, with its free flow time of 60, and link 3 is always better. However, the 1200 vph capacity of link 3 creates a queue on link 1. This queue can grow infinitely: if the demand of 1800 vph continues for an infinite time, all demand on path [1,3,4] will still be the equilibrium, which will result in the queue growing at the rate of 600 vph.

This scenario is similar to Daganzo's paradox (Daganzo, 1998) in that queuing before the diverge results in vehicles choosing the least efficient route for the system. In this example, once vehicles reach the diverge, they find free flow, or nearly free flow, conditions on both alternative paths. Since link 3 has a much lower free flow time than link 2, all vehicles choose the

![](https://cdn.mathpix.com/cropped/c5a1da81-f4c9-4b6c-a9f4-ddca5a1078b6-07.jpg?height=141&width=723&top_left_y=185&top_left_x=590)
Fig. 5. Network for Section 3.3.

Table 3
Link parameters for Section 3.3.
| Link | Free flow travel time (s) | Capacity (vph) |
| :--- | :--- | :--- |
| 1 | 30 | 2400 |
| 2 | 80 | 2400 |
| 3 | 60 | 1200 |
| 4 | 30 | 2400 |


shorter link. When signals were in place this choice was discouraged through an artificial delay placed on vehicles on link 3. With FCFS reservations, the delay is removed in the interests of fairness.

From this example, we make the following conclusions: first, replacing a signal with reservations can, in the worst case, result in arbitrarily long queues. Avoiding this type of scenario is difficult because the queuing results from the choice of control at C. In both scenarios, links 2, 3, and 4 are nearly at free flow. From the local perspective of intersection C, both signals and reservations at C are managing demand sufficiently. Identifying the congestion resulting from reservations at C requires a network perspective.

To stabilize this scenario, the control at C must impose some delay on movement from 3 to 4. If vehicles are given preference by time spent waiting (such as with FCFS) or even by some more system-related objectives such as maximum flow, the unstable situation results. Furthermore, it is necessary to delay vehicles moving from 3 to 4 even when no vehicles are waiting on link 2. This is contrary to the goal of most reservation policies to maximize utilization of intersection capacity. This delay could be in the form of waiting time or in a toll placed on movements from 3 to 4. Previous work on intersection auctions (Schepperle and Böhm, 2007) provides the technology necessary for tolling specific turning movements or microtolling every link.

## 4. Realistic networks

Having demonstrated the potential for signals to perform better than FCFS reservations through theoretical examples, we now investigate such situations in realistic networks. For these studies, we use the cell transmission model (Daganzo, 1994, 1995) for dynamic flow propagation with the conflict region algorithm (Levin and Boyles, 2016), which is consistent with the constraints on general intersection models of Tampère et al. (2011) for reservation-based control. Signals are modeled by calculating saturation flows for each turning movement proportional to green times. We study three subnetworks of the Austin regional network based on data from the Capital Area Metropolitan Planning Organization. To determine route choice, we used DTA to solve for dynamic user equilibrium.

First, we present an arterial subnetwork and a highway subnetwork in which signals or merges/diverges outperform reservations. For all networks, we considered several different levels of demand. (Link capacities and time horizon remained the same, so volume ratios decreased proportionally with demand.) Then, we compare FCFS reservations to signals on the downtown Austin subnetwork, which includes both signals and merges/diverges. The positive results for this large network demonstrates the potential benefits of reservations.

### 4.1. Arterial subnetwork

Lamar \& 38th Street is the intersection between two arterials in Austin, shown in Fig. 6. It contains 5 signalized intersections and 21 links. The intersections on Lamar (running southwest-northeast) do not have progression, but the two intersections on 38th Street are timed for it.

Table 4 shows total system travel time (TSTT) and travel time (TT) per vehicle at different demand scenarios. Traffic signals consistently outperformed reservations at all demand levels. Reservations appeared to scale somewhat worse with demand as well. The worst performing links for reservations at 100\% demand were along the Lamar arterial. The southwestern region in particular had high travel times with reservations. It is likely that FCFS reservations allowed vehicles entering from local roads to delay vehicles traveling along the arterial, as discussed in Section 3.1. The intersections there are close together, and reduced intersection capacities granted to the arterial by FCFS may have also resulted in queue spillback issues.

In addition, the progression on 38th Street was likely disrupted by the use of reservation-based controls. In particular, in the DTA model vehicles do not request a reservation from an intersection until after entering an incoming link. The gap between the intersections of Lamar \& 38th Street, and Medical Parkway and 38th Street, is smaller than the length of the

![](https://cdn.mathpix.com/cropped/c5a1da81-f4c9-4b6c-a9f4-ddca5a1078b6-08.jpg?height=973&width=1068&top_left_y=189&top_left_x=403)
Fig. 6. Lamar \& 38th St.

Table 4
Results on Lamar \& 38th St.
| Demand | Scenario | TSTT (h) | TT per vehicle (min) |
| :--- | :--- | :--- | :--- |
| 13,841 | Traffic signals | 4060.8 | 17.60 |
| (85\%) | FCFS reservations | 4560.4 | 19.77 |
| 14,655 | Traffic signals | 4937.0 | 20.21 |
| (90\%) | FCFS reservations | 5778.5 | 23.66 |
| 15,469 | Traffic signals | 6160.6 | 23.90 |
| (95\%) | FCFS reservations | 7189.4 | 27.89 |
| 16,284 | Traffic signals | 7159.5 | 26.38 |
| (100\%) | FCFS reservations | 8809.1 | 32.46 |


Medical Parkway link. This admits scenarios such as the one in Section 3.2 in which vehicles on Medical Parkway could place a reservation before vehicles on 38th Street.

At low demands, FCFS reservations performed better than traffic signals on this network because the intersections were uncongested, and traffic signals added some delay. However, at all demand levels shown in Table 4, signals performed better than reservations due to optimized timing.

### 4.2. Freeway subnetwork

Most literature has considered replacing traffic signals with reservation-based controls. However, the reservation protocol is general enough to be applied to any intersection. Previous studies such as Hall and Tsao (1997) have considered using autonomous vehicle technologies to improve highway on- and off-ramps. In addition, ramp metering to reduce freeway congestion has been well-studied in the literature (Papageorgiou and Kotsialos, 2000), and reservations with AVs would allow complete enforcement of ramp metering. Therefore, it is likely that researchers will consider using reservations to control freeway access. In this subsection we present an example on replacing conventional unsignalized merge/diverge behavior with FCFS reservation controls.

![](https://cdn.mathpix.com/cropped/c5a1da81-f4c9-4b6c-a9f4-ddca5a1078b6-09.jpg?height=981&width=540&top_left_y=187&top_left_x=673)
Fig. 7. I-35 corridor.

Table 5
Results on I-35 corridor.
| Demand | Scenario | TSTT (h) | TT per vehicle (min) |
| :--- | :--- | :--- | :--- |
| 64,025 | Merges/diverges | 4089.7 | 3.83 |
| (50\%) | FCFS reservations | 6023.4 | 5.64 |
| 76,830 | Merges/diverges | 5307.5 | 4.14 |
| (60\%) | FCFS reservations | 11912.9 | 9.30 |
| 89,635 | Merges/diverges | 8049.8 | 5.39 |
| (70\%) | FCFS reservations | 23248.8 | 15.56 |


In DTA, we model merging via constraints on the receiving flow. With normal merging behavior, the receiving flow is distributed among the upstream links by capacity, with leftover receiving flow given to saturated approaches. With FCFS reservations, receiving flow is distributed according to the vehicle order of request.

The I-35 corridor, shown in Fig. 7, is a freeway subnetwork with 220 links. (Many of the on- and off-ramps are difficult to see due to the length of the corridor.) All intersections are merges or diverges; none are traffic signals. Table 5 shows travel times at different levels of demand. Merges/diverges consistently outperformed reservations at all demand scenarios. At low demand, the differences were small, but as demand increased, FCFS scaled much worse than merges/diverges. An analysis of link travel times found that most of the delays occurred from vehicles entering the freeway. It is not clear why FCFS reservations made it more difficult for vehicles to enter the freeway. Possibly the greater number of lanes on the freeway allowed freeway vehicles to submit requests at a greater rate (vehicles could not submit requests unless they were not blocked from entering the intersection by vehicles in front). This could be indicative of an asymmetry issue where the three lane freeway intersects with one lane on- and off-ramps. Based on the long queues for vehicles entering the freeway, it appears that FCFS reservations in this case skew too much towards freeway traffic and do not provide enough capacity to the on-ramps.

### 4.3. Downtown Austin

Downtown Austin, shown in Fig. 8, contains the downtown grid, several major arterials, and part of I-35 on the east side. Overall, it has 171 zones, 546 intersections, 1247 links and 62,836 trips. Network and demand data was from the Capital Area Metropolitan Organization for the AM peak.

![](https://cdn.mathpix.com/cropped/c5a1da81-f4c9-4b6c-a9f4-ddca5a1078b6-10.jpg?height=897&width=733&top_left_y=187&top_left_x=568)
Fig. 8. Downtown Austin.

Table 6
Results on downtown Austin.
| Demand | Scenario | TSTT (h) | TT per vehicle (min) |
| :--- | :--- | :--- | :--- |
| 43,985 | Signals | 7367.01 | 10.05 |
| (70\%) | FCFS reservations | 3066.5 | 4.18 |
| 53,410 | Signals | 11113.52 | 12.48 |
| (85\%) | FCFS reservations | 4878.92 | 5.48 |
| 62,836 | Signals | 16194.33 | 15.46 |
| (100\%) | FCFS reservations | 7867.04 | 7.51 |


This is an useful test network because flow in the downtown grid is primarily restricted by intersections. Unlike the previous two subnetworks, downtown Austin contains different route options for vehicles. This admits congestion caused by selfish route choice and scenarios like that of Section 3.3. We considered two scenarios: first, using traditional intersections (traffic signals and merges/diverges), and second, replacing all intersection controls with FCFS reservations. To compare traditional intersections and reservations, we first solved DTA using the method of successive averages. Both scenarios were solved to a 2\% gap, with gap defined as

$$
\text { gap }=\frac{\text { TSTT }- \text { shortest path time }}{\text { TSTT }}
$$

Table 6 shows the results from solving DTA on downtown Austin. We tested three demand scenarios - 70\%, 85\%, and 100\% of predicted demand. Despite the increased travel time observed around the Lamar \& 38th St. intersection in the subnetwork, FCFS reservations decreased overall travel time by over 50\% on all scenarios.

Flow through the downtown grid is primarily limited by intersection conflicts. The travel time reductions due to FCFS were similar for each demand scenario, but exhibited a distinct decreasing trend. At 70\% demand, FCFS reservations reduced travel time by 58.4\%. At 85\% demand, the decrease was 56.1\%, and at 100\% demand, the decrease was 51.4\%. At lower demands, intersections are less saturated, and more of the intersection delay is due to vehicles waiting for a green phase at a undersaturated intersection. FCFS can perform better than signals in these undersaturated scenarios by allowing vehicles on conflicting turning movements (Fajardo et al., 2011). However, as the demand increases, intersection saturation also increases, and FCFS reservations has less room to improve over signals. As intersection saturation increases, FCFS reservations are also more likely to break progression (as in the example in Section 3.2) and/or cause queue spillback.

The examples in Sections 3.1 and 3.2 rely on temporary over-saturation on asymmetric intersections to induce greater delays. When undersaturated, FCFS reservations can allow all vehicles to move whereas signals could still delay vehicles
as they wait for a green phase. Also, the downtown grid has few asymmetric intersections. Furthermore, with many parallel links, user equilibrium route choice could encourage vehicles to avoid high delay intersections. FCFS reservations can break progression and/or cause queue spillback, as seen in Sections 3.2 and 4.1. However, when considering user equilibrium behavior in the downtown grid, vehicles will avoid congested routes due to their higher travel times, and seek less saturated intersections. Unless a paradox like that of Section 3.3 occurs, reservations are likely to outperform signals when the intersection is undersaturated, and route choice in grid networks distributes demand away from high delay intersections.

Overall, these city network results suggest that despite the potential issues described in Section 3, reservations can significantly reduce congestion due to intersections. Previous studies have compared signals with reservations on single intersections, or small groups of intersections, but not on a city network with user equilibrium behavior. Table 6 shows that even FCFS reservations have great potential to reduce city congestion, and optimized reservations are likely to further improve travel times.

## 5. Conclusions

To complement previous studies showing that reservations improve over traffic signals, this paper presented a variety of scenarios in which traffic signals and merges/diverges outperformed reservations. We studied three theoretical situations using the different attributes of FCFS reservations to increase delays:

1. The fairness of FCFS was found to increase total vehicle delay in an arterial-local road intersection. FCFS alternated priority between the arterial and the local road, resulting in greater delay to vehicles on the arterial. A signal timed to give more green time to the arterial would not have this issue. This could be avoided by a priority policy that is more systemefficient than FCFS.
2. We created a scenario in which reservations disrupted platoon progression that would occur with timed signals. Because vehicles on the local road requested a reservation before vehicles on the arterial submitted their requests, vehicles on the local road would have their reservation accepted. This might be avoided if the intersection manager attempted to anticipate future reservations or was able to deny a previously accepted reservation.
3. We presented a network similar to the Daganzo paradox (Daganzo, 1998) in which FCFS reservations decreased the expected delay for a local road. When signals were used, signal delay on the local road resulted in all demand using the arterial path - a free flow assignment. When the signals were replaced with a reservations, all demand preferred to take the lower capacity, but shorter, local road, leading to arbitrarily large queues. Avoiding this requires an artificial delay or toll on vehicles taking the local road, even if no conflicting demand exists.

Next, we presented two realistic networks from Capital Area Metropolitan Planning Organization data in which traffic signals or merges/diverges outperformed reservations. One was the intersection between two arterials, and the second was a highway corridor. These theoretical and realistic examples demonstrate that replacing traffic signals with reservations requires network-based analyses to detect adverse route choices. Nevertheless, a comparison of FCFS reservations with traffic signals on the downtown Austin city network resulted in 50\% less travel times. Sections 3.1 and 3.2 relied on asymmetric intersections (e.g. local road-arterial intersections) to increase delays. The downtown grid of Austin had a small proportion of asymmetric intersections and alternate routes to avoid them. Therefore, although reservations may increase congestion or vehicle delay in some situations, they have great potential to improve traffic. However, network-based analyses are necessary to detect adverse route choices before replacing traffic signals with reservation controls.

These results motivate the need for future study on reservations and reservation policies. Any traffic signal control is a feasible policy for reservations (Dresner and Stone, 2007). Therefore reservations can perform at least as well as traffic signals in all situations, and the greater control flexibility afforded by reservations should be able to improve over signals for many scenarios. Indeed, Fajardo et al. (2011) and Li et al. (2013) showed that even FCFS could improve over signals under the right conditions. These results should encourage work into system optimal reservation control policies.

A more analytical model of reservations under different control policies could be helpful for deriving conditions under which reservations are beneficial. The examples in Section 3.1 could be addressed by a new reservation policy that places greater emphasis on system efficiency. In light of Section 3.2, policies that include future predictions of demand to maximize expected system efficiency should be studied. For instance, policies could anticipate future demand to form platoons of vehicles. Finally, methods of identifying and solving induced route choice issues such as that of Section 3.3 could expedite widespread adoption of reservation-based controls.

## Acknowledgements

The authors gratefully acknowledge the support of the Data-Supported Transportation Operations \& Planning Center, the National Science Foundation under Grant No. 1254921, and the Texas Department of Transportation projects 0-6838 (Bringing Smart Transport to Texans: Ensuring the Benefits of a Connected and Autonomous Transport System in Texas) and 0-6847 (An Assessment of Autonomous Vehicles: Traffic Impacts and Infrastructure Needs).

## References

Braess, P.-D., 1968. Über ein paradoxon aus der verkehrsplanung. Unternehmensforschung 12 (1), 258-268.
Carlino, D., Depinet, M., Khandelwal, P., Stone, P., 2012. Approximately orchestrated routing and transportation analyzer: large-scale traffic simulation for autonomous vehicles. In: 2012 15th International IEEE Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 334-339.
Carlino, D., Boyles, S.D., Stone, P., 2013. Auction-based autonomous intersection management. In: 2013 16th International IEEE Conference on Intelligent Transportation Systems - (ITSC). IEEE, pp. 529-534.
Conde Bento, L., Parafita, R., Santos, S., Nunes, U., 2013. Intelligent traffic management at intersections: legacy mode for vehicles not equipped with v2v and v2i communications. In: 2013 16th International IEEE Conference on Intelligent Transportation Systems - (ITSC). IEEE, pp. 726-731.
Daganzo, C.F., 1994. The cell transmission model: a dynamic representation of highway traffic consistent with the hydrodynamic theory. Transport. Res. Part B: Methodol. 28 (4), 269-287.
Daganzo, C.F., 1995. The cell transmission model, Part ii: Network traffic. Transport. Res. Part B: Methodol. 29 (2), 79-93.
Daganzo, C.F., 1998. Queue spillovers in transportation networks with a route choice. Transport. Sci. 32 (1), 3-11.
Dresner, K., Stone, P., 2004. Multiagent traffic management: a reservation-based intersection control mechanism. Proceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems, vol. 2. IEEE Computer Society, pp. 530-537.
Dresner, K., Stone, P., 2006. Human-usable and emergency vehicle-aware control policies for autonomous intersection management. In: Fourth International Workshop on Agents in Traffic and Transportation (ATT), Hakodate, Japan.
Dresner, K., Stone, P., 2006. Traffic intersections of the future. Proceedings of the National Conference on Artificial Intelligence, vol. 21. AAAI Press; MIT Press, Menlo Park, CA; Cambridge, MA; London, p. 1593, 1999.
Dresner, K.M., Stone, P., 2007. Sharing the road: autonomous vehicles meet human drivers. IJCAI, vol. 7, pp. 1263-1268.
Fajardo, D., Au, T.-C., Waller, S., Stone, P., Yang, D., 2011. Automated intersection control: performance of future innovation versus current traffic signal control. Transport. Res. Rec.: J. Transport. Res. Board (2259), 223-232.
Hall, R.W., Tsao, H.J., 1997. Capacity of automated highway systems: merging efficiency. Proceedings of the 1997 American Control Conference, 1997, vol. 3. IEEE, pp. 2046-2050.
Hausknecht, M., Au, T.-C., Stone, P., 2011. Autonomous intersection management: multi-intersection optimization. In: 2011 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, pp. 4581-4586.
Hausknecht, M., Au, T.-C., Stone, P., Fajardo, D., Waller, T., 2011. Dynamic lane reversal in traffic management. In: 2011 14th International IEEE Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 1929-1934.
Kesting, A., Treiber, M., Helbing, D., 2010. Enhanced intelligent driver model to access the impact of driving strategies on traffic capacity. Philos. Trans. Roy. Soc. Lond. A: Math. Phys. Eng. Sci. 368 (1928), 4585-4605.
Levin, M.W., Boyles, S.D., 2016. Intersection auctions and reservation-based control in dynamic traffic assignment. Transport. Res. Rec.: J. Transport. Res. Board (2497), 35-44.
Li, Z., Chitturi, M., Zheng, D., Bill, A., Noyce, D., 2013. Modeling reservation-based autonomous intersection control in VISSIM. Transport. Res. Rec.: J. Transport. Res. Board (2381), 81-90.
Papageorgiou, M., Kotsialos, A., 2000. Freeway ramp metering: an overview. In: Intelligent Transportation Systems, 2000. Proceedings. 2000 IEEE. IEEE, pp. 228-239.
Qian, X., Gregoire, J., Moutarde, F., De La Fortelle, A., 2014. Priority-based coordination of autonomous and legacy vehicles at intersection. In: 2014 IEEE 17 th International Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 1166-1171.
Schakel, W.J., Van Arem, B., Netten, B.D., 2010. Effects of cooperative adaptive cruise control on traffic flow stability. In: 2010 13th International IEEE Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 759-764.
Schepperle, H., Böhm, K., 2007. Agent-based traffic control using auctions. In: Cooperative Information Agents XI. Springer, pp. 119-133.
Shladover, S., Su, D., Lu, X.-Y., 2012. Impacts of cooperative adaptive cruise control on freeway traffic flow. Transport. Res. Rec.: J. Transport. Res. Board (2324), 63-70.
Tampère, C.M., Corthout, R., Cattrysse, D., Immers, L.H., 2011. A generic class of first order node models for dynamic macroscopic simulation of traffic flows. Transport. Res. Part B: Methodol. 45 (1), 289-309.
Van Arem, B., Van Driel, C.J., Visser, R., 2006. The impact of cooperative adaptive cruise control on traffic-flow characteristics. IEEE Trans. Intell. Transport. Syst. 7 (4), 429-436.
Vasirani, M., Ossowski, S., 2010. A Market-Based Approach to Accommodate User Preferences in Reservation-Based Traffic Management. Tech. Rep., Technical Report ATT.
Vasirani, M., Ossowski, S., 2012. A market-inspired approach for intersection management in urban road traffic networks. J. Artif. Intell. Res., 621-659
Wardrop, J.G., 1952. Road paper. Some theoretical aspects of road traffic research. ICE Proceedings: Engineering Divisions, vol. 1. Thomas Telford, pp. 325-362.


[^0]:    * Corresponding author.
    E-mail address: michaellevin@utexas.edu (M.W. Levin).

