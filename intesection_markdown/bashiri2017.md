# A Platoon-Based Intersection Management System for Autonomous Vehicles 

Masoud Bashiri ${ }^{1}$ and Cody H. Fleming ${ }^{2}$


#### Abstract

Recent advancements in Intelligent Transportation Systems suggest that the roads will gradually be filled with autonomous vehicles that are able to drive themselves while communicating with each other and the infrastructure. Autonomous intersection management is among the more challenging traffic scenarios, which involves coordinating the movement of autonomous vehicles through a conflict zone. Intersection management is also potentially one of the more beneficial traffic scenarios in terms of mobility and environmental impact.

In this paper we propose a platoon-based approach for the cooperative intersection management problem. We assert that leveraging the platooning capability of autonomous vehicles could improve the efficiency of any policy at an intersection, in terms of average delay time per vehicle and can reduce the communication overhead in the vicinity of intersections by a factor of up to the average platoon size.

We also develop a new autonomous intersection management method that guarantees the safety of traffic by allowing one platoon in the conflict zone at any time. We examine the effects of platooning on a simple stop sign at a single 4-way intersection in a simulated environment and report the results in terms of average delay per vehicle and communication overhead. Moreover, we evaluate the performance of the proposed method in a simulated environment and compare the results in terms of average wait time per vehicle and variance in delay with that of a stop sign.


## I. INTRODUCTION

Intersections are bottlenecks of traffic flow and a major cause of traffic accidents. According to National Highway Traffic Safety Administration (NHTSA), [1] about 40 percent of the estimated 5,811,000 crashes that occurred in the United States in 2008 were intersection-related crashes. Moreover, Traffic efficiency is reported to be closely correlated with traffic safety on intersections [3], i.e. traffic accidents tend to occur more frequently on congested intersections. Congestion is also among the most important influences on $C O_{2}$ emissions [21] which is the largest constituent of transport's greenhouse gas (GHG) emissions. Vehicle stop times at intersections also contribute to carbon monoxide $(C O)$ emissions. According to [20], when vehicles idle at an intersection they emit about 5-7 times as much $C O$ as vehicles traveling between $5-10 m p h$.

Traffic Lights and stop signs are major traffic control devices that are currently being used at intersections. Traffic lights have helped improve traffic flow at intersections, yet they still considered inefficient and a source for traffic congestion and accidents; a majority of intersection-related acci-

[^0]dents occur in the presence of traffic lights. Many traffic light control algorithms have been proposed through the years to improve the performance. Fuzzy logic [2], mathematical models such as Mixed-Integer Linear Programming [4] and machine learning approaches including neural networks[5] and Reinforcement Learning [6] are among the more significant works that have been done.

Recent advancements of Information Technology and the emergence of Vehicular Adhoc Networks (VANETs) that support Vehicle to Vehicle (V2V), Vehicle to Infrastructure (V2I) and Vehicle to Pedestrian (V2P) communications has brought forth opportunities for further advancements of intersection management infrastructure and new nonsignalized approaches for the intersection management problem commonly known as Cooperative Intersection Management (CIM) where road users, i.e. vehicles communicate with the intersection control units to cooperatively coordinate the traffic flow. In 2014, the Institute of Electrical and Electronics Engineers (IEEE) published the Wireless Access for Vehicle Environments (WAVE) [7] specification. The standards define architectures based on Dedicated Short Range Communications (DSRC) for which the Society of Automotive Engineers (SAE) has specified message types and data elements through various standards.

Several methods have been proposed to leverage autonomous and connected vehicles for the intersection management. The new methodologies for CIM can be categorized into two classes of Centralized and Distributed methods. In centralized methods, a central intersection manager unit receives real-time information and requests from road users and decides how to coordinate the traffic flow, e.g. instruct vehicles how, when and if to pass the intersection. Distributed methods, on the other hand, do not rely on a central control unit. Instead, all vehicles communicate with each other and the infrastructure to coordinate the conflict zone. Vehicles locally decide what to do and negotiate right of way.

In [8], Dresner et al. propose a centralized resource reservation algorithm based on First Come First Serve (FCFS) policy. The control unit receives requests from all vehicles approaching the intersection, simulates the most recent and confirms the request if there is no conflict with previously accepted trajectories, otherwise the request would be rejected and the vehicle has to request at a later time. The authors assume constant speed at the intersection and perform simulations comparing results with a traffic light and an overpass. It was shown that the proposed method outperformed traffic light in terms of average vehicle delay. The authors further developed their work in [9] to add several methods to
improve the performance and overcome major disadvantages of the previous work. Moreover, they improved the work in [10], [11] and [12] by adding support for human drivers, considering emergency vehicles that generally have higher priority, and communication schemes for vehicles with different levels of autonomy.

In [13] a controller model has been proposed along with different v2v-based intersection management protocols to enhance traffic throughput and safety. Each vehicle runs a collision avoidance algorithm that takes in all safety messages that are being broadcast by surrounding vehicles and detects possible collision, and the estimations are then used to generate alternative trajectories to avoid collisions. The results have been compared with that of traffic light and stop signs, showing significant decrease in average trip delay. However, the proposed protocols rely on position accuracy and assume fast and reliable communication between vehicles.

The existing approaches are limited with respect to at least one of the following factors: (1) unrealistic or infeasible bandwidth requirements on communication, (2) no performance guarantees, i.e. no guarantee that the intersection will behave better than signalized intersections, (3) no guarantees of safety as vehicles traverse the intersection, or (4) inability to scale to realistic traffic volumes or roadway geometries. To address these issues we propose a platoon-based approach where vehicles request a pass as a platoon. The intersection manager agent utilizes an optimization policy to allocate slots in time and space for any platoon approaching the intersection. This approach minimizes the communication burden to realistic levels and also takes advantage of recent advances in platooning and connected vehicle control.
[14] studies the problem of scheduling vehicle platoons through unregulated intersections. The authors model an intersection as a k-way merge and the scheduling task as a minimization problem where the target is minimizing the maximum delay suffered by any platoon in a given schedule. They provide proof of computational complexity for different scenarios. This approach is similar to the method proposed in this paper, however we introduce two different solutions to the scheduling problem that guarantee safety and significantly reduce computational complexity. Moreover we design and implement a simulation environment in Matlab and leverage the capabilities of software to evaluate the proposed method.

The rest of this paper is organized as follows. In section 2, the effects of platooning on a stop sign policy at a 4-way intersection is studied through simulations and efficiency is reported in terms of average delay per vehicle and communication overhead. Section 3 provides a description of the proposed method for autonomous intersection management. In section 4, results from the proposed method are compared to that of stop signs through simulations conducted in our simulator. Conclusions and future works are presented in section 5.

## II. Effects of Platooning on Intersection Efficiency

The vehicle platoon control problem [18] has been widely studied in the literature and several solutions have been proposed [15], [16], [17]. We propose that platooning in the vicinity of intersections could help improve the efficiency of any scheduling policy. Moreover, it can reduce communication overhead by allowing platoon leaders to negotiate with the infrastructure on behalf of the entire platoon. To examine this idea, we design a simulation experiment involving a 4- way intersection, and a stop sign policy installed. That is, the intersection manager behaves like a classic stop sign in that every approaching platoon comes to a stop and is not granted clearance until the intersection is free. It is first come, first serve and in the event of simultaneous arrival, the platoon in the counterclockwise direction is given clearance first.

We examine the efficiency and communication overhead of stop signs given maximum platoon sizes of 1 to 8 vehicles. All lanes have the same traffic levels that are changed from 500 vehicle/hour up to 2000 vehicle/hour. The simulator samples new platoons according to the traffic level from a distribution that matches current traffic level. To make the comparisons more dependable, we set identical seeds to the random number generator for each traffic level. Results are shown in Fig. 1 for different traffic levels. We conduct six independent 10 minute simulation runs for each experiment and average results to account for randomization inside the simulation. Figs. 1a and 1b show the average travel wait time per vehicle and average number of packets exchanged between leaders and the infrastructure. Results show that leveraging platoons could potentially reduce average wait time by up to 55\% and communication overhead by 50\%.

Communication Protocol: Below is the structure of request messages broadcast by platoon leaders.

- Platoon ID, a unique number identifying the platoon
- State, a string in the set: ['move-and-wait', 'stop-andwait', 'crossing', 'emergency', 'done']
- Platoon Length, length of the platoon in meters
- Platoon Size, number of vehicles in the platoon
- Waiting Time, platoon's current total waiting time
- Location, the leader's position
- Velocity, current velocity of platoon in $\mathrm{m} / \mathrm{s}$
- Acceleration, current acceleration of platoon in $\mathrm{m} / \mathrm{s}^{2}$
- Expected Arrival Time, estimated time of arrival

Each platoon has one platoon leader that is the first vehicle in the queue. The leader is in charge of communicating with the infrastructure to request to cross and broadcasts a message, with the above structure and content, ten times a second. This message is received by the intersection infrastructure and used by the intersection manager to calculate a crossing time for the platoon. The intersection manager sends the reserved crossing time to the leader. The other simulations in this work also adopt the same structure as above. There are two other message types provisioned for this framework-one is a confirmation message sent from the intersection manager to platoon leaders which contains

![](https://cdn.mathpix.com/cropped/8edc201d-19ec-4059-8d6d-0b229cfdbeef-3.jpg?height=1568&width=864&top_left_y=163&top_left_x=180)
Fig. 1: Effects of Platooning on the Performance of a Stop Sign Policy

the platoon's unique identifier and a crossing time, and the other is a response message from the platoon leaders to the manager that contains the platoon's identifier and a state variable that would be set to emergency if the platoon cannot cross the intersection in time, in which case the manager generates new crossing time for the platoons in the queue and re-sends the appropriate confirmation messages.

Assumptions: To simplify the scheduling problem we assume constant velocity of $10 m / s$ for each vehicle. Moreover, the platoon control algorithm is assumed to be perfect, i.e. vehicles can identify and generate the same real time velocity, acceleration and steering as that of the vehicle in front. Future work will include more realistic dynamics. Broadcast messages are received by the intersection manager at a frequency of 10hz.

## III. Platoon-Based Intersection Scheduling Algorithm

Consider the scenario in Fig. 2 where four platoons arrive at a 4-way intersection with conflicting trajectories. Assuming identical vehicles with constant velocity and a square shaped conflict zone, the clearance time of any given platoon can be formulated as Eq. 1, where $\operatorname{size}(*)$ is a function that returns the length of a platoon, $\alpha$ is the time needed for a vehicle, i.e. the leader, to enter the intersection and completely clear the conflict zone and $\beta$ is the follower coefficient that determines the time needed for each follower vehicle to leave the conflict zone. Since the headway distance between vehicles in platoon is always shorter than the distance between any two ends of the conflict zone, once the leading vehicle has passed the conflict zone, the subsequent vehicle is already in the conflict zone and will take less time to clear the conflict zone, i.e. $\beta<\alpha$.

In this work we use $\alpha=10$ and $\beta=2$. A simple stop sign policy will yield the schedule $\left(P_{1}, P_{2}, P_{3}, P_{4}\right)$. Considering all 4! possible schedules, one can note that there could be two other major approaches to solving the problem. First is to minimize the average delay per vehicle, and the second is to minimize the final clearance time, that is, the final time at which the intersection clears for the next batch of platoons to cross. The results for each of these approaches can be found in Table I.

$$
C_{i}=\alpha+\beta *\left(\operatorname{size}\left(p_{i}\right)-1\right)
$$

We implement and examine these two approaches and com-

![](https://cdn.mathpix.com/cropped/8edc201d-19ec-4059-8d6d-0b229cfdbeef-3.jpg?height=849&width=855&top_left_y=1431&top_left_x=1087)
Fig. 2: A simple scenario at a 4 way intersection

pare with stop signs. The proposed method works as follows. At each iteration, the manager takes in the information of a set of platoons that are selected based on the following criteria:

TABLE I: Results of different schedulers for a 4-way intersection
|  | Schedule | Average Delay Per Vehicle | Clearance Time | Max_Delay |
| :--- | :--- | :--- | :--- | :--- |
| Stop Signs | ( $P_{1}, P_{2}, P_{3}, P_{4}$ ) | 20.7 | 60 | 32 |
| Minimize_Average_Delay | ( $P_{2}, P_{1}, P_{4}, P_{3}$ ) | 17.7 | 61 | 42 |
| Minimize_Clearance_Time | ( $P_{1}, P_{2}, P_{4}, P_{3}$ ) | 18.7 | 60 | 41 |


- It must be leading its lane
- Its state should be either 'move - and - wait' or 'stop-and-wait', i.e. if the platoon has already started crossing the intersection it would not be stopped
- Its expected arrival time should be sooner than current clear time of the intersection, i.e. there is a conflict if it keeps traveling. If not, it should not be considered in the decision.

In this work, the intersection scheduling problem is defined as in equation 2 , where $\delta(*)$ is the cost function and $S$ is the set of all $K$ ! possible schedules given $K$ platoons arriving at the intersection.

$$
\underset{s}{\arg \min } \delta(s):=\left\{s \mid s \in S \wedge \forall s^{\prime} \in S: \delta(s) \leq \delta\left(s^{\prime}\right)\right\}
$$

where $S=\left\{\left(p_{1}, \ldots, p_{k-1}, p_{k}\right), \ldots,\left(p_{k}, p_{k-1}, \ldots, p_{1}\right)\right\}$

The intersection manager computes a schedule using a simple greedy algorithm that optimizes over one of the following cost functions. The algorithm runs every time the selection pool is updated.

$$
\begin{gathered}
\delta_{1}(s)=\sum_{n=1}^{k} \operatorname{wait}\left(p_{n}\right) * \operatorname{size}\left(p_{n}\right) \\
\delta_{2}(s)=\sum_{n=1}^{k} n * \operatorname{wait}\left(p_{n}\right) * \operatorname{size}\left(p_{n}\right)
\end{gathered}
$$

Algorithm 1 shows a pseudocode for the proposed autonomous manager. According to the selection criteria above, a platoon that has already been given a crossing pass would still be eligible to enter the scheduling pool if it has not yet started crossing the conflict area. This will help further improve the efficiency of the scheduler.

In the above equations $\operatorname{wait}(*)$ is a function that estimates the expected waiting time of a platoon given its turn in the schedule, plus the platoon's current total waiting time. The $\operatorname{size}(*)$ is a function that returns the length of a platoon, i.e. number of vehicles in the platoon. This function could be extended to return the total number of passengers in a platoon for other applications or cost functions. In equation 4, variable $n$ represents a platoon's turn in the schedule. To guarantee the safety of vehicles, the proposed method is based on stop sign policy, meaning only one platoon is crossing the conflict zone at any time.

```
Algorithm 1 Autonomous Intersection Manager
    function IntersectionManager \((s)^{a}\)
        while True do
            \(P=\) getRequests ()\(^{b}\)
            \(\operatorname{sort}(P)^{c}\)
            pool = selectCandidates \((P)\)
            if !pool.isUpdated() then
                continue \({ }^{d}\)
            end if
            if \(s=1\) then
                [platoons, schedule] =
    PDM (pool)
            else if \(s=2\) then
                [platoons, schedule] =
    PV M (pool)
            end if
            \(i=1\)
            for platoon in platoons do
                update(platoon, schedule \({ }_{i}\) )
                \(i++\)
            end for
        end while
    end function
```

${ }^{a}$ Where s is an integer in \{1,2\}
${ }^{b}$ Where P is a map of platoons paired with their respective request information
${ }^{c}$ Sort the platoon list based on their arrival time to make the candidate selection run faster
${ }^{d}$ Skip this iteration if the selection pool has not changed

The cost function given in equation 3 which we will refer to as Platoon-based Delay Minimization (PDM), helps the scheduler pick a schedule that minimizes the overall wait time, but one might note that it could potentially increase the variance of wait time per platoon/vehicle. In the simulations, we noticed that this policy ends up favoring some lanes over others, producing smooth traffic on the favored lanes and high congestion on the others. This is due to the fact that the cost function is designed to minimize average wait time rather than to minimize the maximum wait time, i.e. there is no term in the function $\delta_{1}(s)$ to penalize maximum wait time per vehicle. The high variability of wait time affects the reliability of expected travel time, which is among the major factors that drivers care about when choosing between alternative routes [19].

To address this issue, we propose another cost function, $\delta_{2}(s)$ in equation 4 called Platoon-based Variance Minimization (PVM), that makes a trade-off between minimizing average and minimizing the maximum wait time. This tradeoff is implied by variable $n$ that helps penalize schedules that move the larger platoons with long wait times to the end of the schedule. Due to this penalty on long weight times, we expect this strategy to significantly reduce the variance in wait time compared to that of the first strategy.

We compare the efficiency of the two proposed policies against that of a stop sign policy in terms of average delay per vehicle and variance in delay per vehicle. To examine the effectiveness of the proposed method in different levels of incoming traffic, we conduct independent experiments applying different traffic levels ranging from 500 veh/hour to 2000veh/hour. The spawning of a new platoon is seeded with a random number that matches the traffic level and the randomly selected size of the platoon. The results are averaged from six independent runs of 10 minutes of simulated time. Maximum vehicle per platoon is set to 4 for all experiments.

Figs. 3a and 3b demonstrate the comparisons in terms of average delay per vehicle and variance in delay per vehicle, respectively. It is interesting to note that PVM outperforms PDM for average delay in lower levels of traffic. This is due to the fairness nature of the PVM method that on average tries to assign equal number of passes to the incoming lanes. Putting it together with the simulation assumption of equal traffic levels on all lanes, the results for Traffic levels of 500veh/hour and 600veh/hour make sense. The intuition behind a potential increase in variance is as follows. The optimizer using $\delta_{1}$ will assign a platoon, say $p_{e}$, to the back of the queue during any arbitrary iteration. Once the first platoon in the pool clears the conflict zone, then the pool will be updated. Depending on the arrival time of the next platoon, it is likely that the same platoon that was assigned to the back of the queue during the previous iteration, i.e. $p_{e}$, will be penalized again. With sufficiently low traffic volumes, it is possible to minimize average delay while also minimizing the worst-case travel time because the above phenomenon occurs much less frequently.

However, as the traffic levels rise, delay minimization effects start to show up. After traffic level of 700veh/hour, the PVM algorithm is outperformed in terms of average delay per vehicle. The greedy nature of PDM presents itself in terms of significantly higher variance of delay per vehicle. The PDM cost function prefers minimizing delay over letting platoons that already have a high wait time to pass. The PVM policy on the other hand, makes the opposite decision, hence decreasing the variance in delay time even compared to stop sign that is considered a reliable device at intersections in terms of expected travel times.

Fig. 3b demonstrates the variance of wait time per vehicle. One can note the significant increase of variance in wait time generated by the PDM compared to that of the PVM and stop signs policies. On average, the PDM policy increases the variance by a factor of 5 and decreases average wait time by 30\% compared to stop sign policy. The PVM policy decreases the variance by 50\% and the average wait time per vehicle by 20\%. The comparisons are averaged from simulations with traffic levels ranging from 500 to 2000veh/hour/lane with an interval value of 100.

![](https://cdn.mathpix.com/cropped/8edc201d-19ec-4059-8d6d-0b229cfdbeef-5.jpg?height=1555&width=862&top_left_y=168&top_left_x=1083)
Fig. 3: Comparison of the proposed methods against stop signs

## V. CONCLUSIONS AND FUTURE WORK

This paper examines the effects of platooning on a simple stop sign at a single 4-way intersection in a simulated environment and reports the results in terms of average delay per vehicle and communication overhead. Moreover, we evaluate the performance of the proposed method in a simulated environment and compare the results in terms of average wait time per vehicle and variance in delay with that of a stop sign.

The simulation results suggest that the PDM method can reduce average delay per vehicle by up to 50\%, but will increase the variance in delay times which is an important reliability factor in transportation. There could also be implications with larger variance when multiple intersections are connected together, and the variance could potentially
cascade. Such effects will be studied in future work. The PVM method however, can reduce average delay by up to 40\% while reducing variance by 50\% compared to stop sign policy.

The intersection management policy presented in this paper is currently being further extended into a more efficient one that significantly improves upon the constant velocity and identical vehicle model assumptions of this work and will be more realistic.

Moreover, we intend to extend the low level controllers on the platoons to optimize the trajectories from current position to the stop point at the intersection. One of the main objectives of such optimization will be to minimize the $C O_{2}$ emissions from fuel combustion. The second objective would be to minimize the stop time of the platoon given the clearance time of the intersection.

## References

[1] Choi, Eun-Ha. Crash factors in intersection-related crashes: An onscene perspective. No. HS-811 366. 2010.
[2] Niittymäki, Jarkko, and Matti Pursula. "Signal control using fuzzy logic." Fuzzy sets and systems 116.1 (2000): 11-22.
[3] Chang, Gang-Len, and Hua Xiang. The Relationship between Congestion Levels and Accidents. No. MD-03-SP 208B46,. 2003.
[4] Lin, Wei-Hua, and Chenghong Wang. "An enhanced 0-1 mixedinteger LP formulation for traffic signal control." IEEE Transactions on Intelligent transportation systems 5.4 (2004): 238-245.
[5] Spall, James C., and Daniel C. Chin. "Traffic-responsive signal timing for system-wide traffic control." Transportation Research Part C: Emerging Technologies 5.3 (1997): 153-163.
[6] Abdulhai, Baher, Rob Pringle, and Grigoris J. Karakoulas. "Reinforcement learning for true adaptive traffic signal control." Journal of Transportation Engineering 129.3 (2003): 278-285.
[7] IEEE Guide for Wireless Access in Vehicular Environments (WAVE) - Architecture, IEEE Std 1609.0-2013, Mar. 2014.
[8] Dresner, Kurt, and Peter Stone. "Multiagent traffic management: A reservation-based intersection control mechanism." Proceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems-Volume 2. IEEE Computer Society, 2004.
[9] Dresner, Kurt, and Peter Stone. "Multiagent traffic management: An improved intersection control mechanism." Proceedings of the fourth international joint conference on Autonomous agents and multiagent systems. ACM, 2005.
[10] Dresner, Kurt, and Peter Stone. "Human-usable and emergency vehicle-aware control policies for autonomous intersection management." Fourth International Workshop on Agents in Traffic and Transportation (ATT), Hakodate, Japan. 2006.
[11] Dresner, Kurt, and Peter Stone. "A multiagent approach to autonomous intersection management." Journal of artificial intelligence research 31 (2008): 591-656.
[12] Au, Tsz-Chiu, Shun Zhang, and Peter Stone. "Autonomous intersection management for semi-autonomous vehicles." Handbook of Transportation. Routledge, Taylor \& Francis Group (2015).
[13] Azimi, Reza, et al. Intersection management using vehicular networks. No. 2012-01-0292. SAE Technical Paper, 2012.
[14] Vial, Juan José Besa, et al. "Scheduling Autonomous Vehicle Platoons Through an Unregulated Intersection." arXiv preprint arXiv:1609.04512 (2016).
[15] Iihoshi, Akira, Sachio Kobayashi, and Yoshimi Furukawa. "Vehicle platoon control system." U.S. Patent No. 6,032,097. 29 Feb. 2000.
[16] Hedrick, J. K., et al. "Longitudinal vehicle controller design for IVHS systems." American Control Conference, 1991. IEEE, 1991.
[17] Kato, Shin, et al. "Vehicle control algorithms for cooperative driving with automated vehicles and intervehicle communications." IEEE Transactions on Intelligent Transportation Systems 3.3 (2002): 155-161.
[18] Varaiya, Pravin. "Smart cars on smart roads: problems of control." IEEE Transactions on automatic control 38.2 (1993): 195-207.
[19] Kockelman, Kara, T. Donna Chen, and Brice Nichols. "The economics of transportation systems: A Reference for Practitioners." Center for Transportation Research (2013).
[20] Van der Hoeven, M. "CO2 emissions from fuel combustion: highlights. Paris: Organisation for Economic Co-operation and Development." International Energy Agency (OECD/IEA) (2012).
[21] Grote, Matt, et al. "Including congestion effects in urban road traffic CO 2 emissions modelling: Do Local Government Authorities have the right options?." Transportation Research Part D: Transport and Environment 43 (2016): 95-106.

[^0]:    ${ }^{1}$ Masoud Bashiri is with the Department of Systems and Information Engineering, University of Virginia mb4bw@virginia.edu
    ${ }^{2}$ Cody H. Fleming is with the faculty of Systems and Information Engineering, University of Virginia cf5eg@virginia.edu

