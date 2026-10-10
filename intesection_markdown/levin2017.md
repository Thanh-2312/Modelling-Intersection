# Conflict-point formulation of intersection control for autonomous vehicles 

Michael W. Levin ${ }^{\mathrm{a}, *}$, David Rey ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}} 140$ Civil Engineering Building, Department of Civil, Environmental, and Geo-Engineering, University of Minnesota, 500 Pillsbury Drive SE, Minneapolis, MN 55455, United States<br>${ }^{\mathrm{b}}$ School of Civil and Environmental Engineering, UNSW Sydney, NSW 2052, Australia

## ARTICLE INFO

Keywords:
Reservation-based
Intersection control
Autonomous vehicles
Conflict point
Collision avoidance


#### Abstract

Reservation-based intersection controls, in which vehicles reserve space-time paths through the intersection, have the potential to make greater use of intersection capacity than traffic signals. However, the efficiency of previous microsimulations of reservations has been severely limited by a protocol that requires vehicles to request reservations and the intersection manager to accept or reject them. We propose a new protocol, AIM*, in which the intersection manager assigns reservations to vehicles, to greatly increase the optimization possibilities. Then, we present a mixed integer linear program for optimally choosing vehicle reservations under AIM*. The formulation is similar to conflict resolution models for aviation, and ensures separation at all points that vehicles might intersect. We therefore present a rolling-horizon algorithm to extend the method to larger numbers of vehicles. Results show that the optimal reservation assignments from AIM* significantly reduce delays over previous protocols. Furthermore, the rolling horizon solutions have similar delays to a fixed horizon, thereby providing an efficient method of implementing AIM*.


## 1. Introduction

Several new technologies have been proposed for connected autonomous vehicles (AVs) to improve traffic flow (Chen and Englund, 2016). This paper focuses on optimizing reservation-based intersection control (Dresner and Stone, 2004, 2005), which has been well-studied in the literature. In previous work on reservations, vehicles reserve a space-time path through the intersection by communicating wirelessly with an intersection manager (IM) computer. The IM accepts or rejects reservations based on forward simulation of vehicle requests.

Most previous studies have focused on the first-come-first-serve (FCFS) policy, in which vehicle requests are prioritized by the order they are received. FCFS was shown to reduce delays beyond optimized signals for certain scenarios (Fajardo et al., 2011; Li et al., 2013). Indeed, since reservations can implement traffic signals, the optimal reservation policy performs at least as well as signals (Dresner and Stone, 2007). However, Levin et al. (2016) found several situations in which FCFS would have higher delays than traffic signals. Therefore, more optimal policies are necessary before reservations can be deployed effectively.

The purpose of this paper is to optimize reservations in real-time using a conflict point separation model. The conflict point model is similar to work on aircraft separation (Rey et al., 2012, 2015a,b), although aircraft require different separation constraints than road vehicles. This differs from previous work on optimizing reservations in that the conflict point formulation includes all collision

[^0]avoidance constraints and directly specifies vehicle departure times and speeds for reservations. Therefore, the solutions from this formulation may be directly used for safe vehicle movement. Unfortunately, the current reservation protocol, called autonomous intersection management (AIM), is quite limited in the reservation solutions it can use. AIM checks the feasibility of vehicle requests, but is dependent on vehicles to propose a reservation timing solution. To use the solutions from our formulation, this paper also presents a more general reservation protocol, AIM*.

The contributions of this paper are as follows: we develop a new communications protocol for reservations, AIM*, to facilitate optimal reservation policies. Using a conflict point approach to vehicle separation, we formulate a mixed integer linear program (MILP) to optimize vehicle intersection trajectories. Since MILPs scale poorly with the number of variables, we develop a rolling horizon approach and evaluate empirically problem sizes that may be efficiently solved. We perform several experiments that reach the following conclusions. First, AIM* performs much better than AIM (with FCFS policy) even on a single, symmetric intersection due to the potential to optimize vehicle trajectories. Second, the rolling horizon approach loses little optimality over the singlehorizon solution, and can therefore be used as an efficient algorithm for implementation.

The remainder of this paper is organized as follows. Section 2 describes previous work on optimizing reservations. Section 3 presents AIM*, which admits the conflict point MILP developed in Section 4. Section 5 develops a rolling horizon formulation, which is used for numerical results in Section 6. We discuss conclusions in Section 7.

## 2. Literature review

Connected and automated vehicle technologies can be used to improve intersection delays and throughput (Chen and Englund, 2016). These technologies range from incorporating vehicle-to-infrastructure communications into adaptive signal timing to protocols that entirely obviate traffic signals. We focus on the AIM protocol proposed by Dresner and Stone $(2004,2005)$ as an alternative to traffic signals for AVs. In AIM, vehicles communicate wirelessly to request a reservation from the intersection manager (IM). A reservation specifies the turning movement as well as the time at which the vehicle can enter the intersection. The IM simulates reservation requests on a spacetime grid of tiles (illustrated by Fajardo et al. (2011) in Fig. 1) and accepts requests if they do not conflict with other reservations. If two vehicles will occupy the same tile at the same time, a potential conflict exists and the request must be rejected.

### 2.1. Vehicle prioritization

The design of AIM lends itself to the FCFS policy: vehicles are prioritized by order of vehicle request. This is a simple policy to implement within the framework of AIM because it involves simulating vehicle requests in the order that they are received, and accepting or rejecting them based on tile occupancies of previous reservations. Consequently, FCFS has been studied in much of the literature on reservations. Fajardo et al. (2011) and Li et al. (2013) compared FCFS with optimized traffic signals, and found that FCFS reduced delays in certain scenarios. However, FCFS is only one of many potential policies for reservations. For instance, Dresner and Stone (2006) proposed a policy that prioritizes emergency vehicles. Schepperle and Böhm $(2007,2008)$ proposed to use intersection auctions to decide on vehicle priority. In addition to the reservation request, vehicles would also communicate a willingness to pay. The vehicle willing to pay the most would receive the highest priority (and pay a corresponding amount). Schepperle and Böhm $(2007,2008)$ found that auctions reduced delay weighted by vehicle value-of-time, and Vasirani and Ossowski (2012) found similar results for a network of intersections. Carlino et al. (2013) used system bids to further improve the efficiency of auctions. However, Levin and Boyles (2015) found that high value-of-time vehicles could become trapped behind low value-of-time vehicles, making it difficult to realize higher travel time savings for high-bidding vehicles.

AIM can easily implement traffic signals as a policy by rejecting requests to enter the intersection during red lights. Therefore, the optimal policy for AIM can perform at least as well as traffic signals. However, the widely-used FCFS policy is far from optimal. In fact, although FCFS can reduce delays beyond traffic signals for certain intersections (Fajardo et al., 2011; Li et al., 2013), Levin et al. (2016) found several instances for which FCFS reservations had higher delay than traffic signals. These occurred because FCFS does not account for capacity differences in roads or coordinate between intersections. Therefore, more work is needed on optimizing

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-02.jpg?height=467&width=905&top_left_y=1886&top_left_x=494)
Fig. 1. Tile-based reservation protocol (Fajardo et al., 2011).

reservations. Levin et al. (2017) proposed an integer program for reservations in dynamic traffic assignment, and proposed two heuristic policies to reduce intersection delay or energy consumption. Unfortunately, those policies cannot be implemented with AIM because they require that the IM be aware of all vehicles and able to assign arbitrary reservations.

### 2.2. Human-aware policies

One common criticism of reservations is lack of compatibility with non-autonomous vehicles. AIM can be used when not all vehicles are autonomous by periodically cycling a green light to allow conventional vehicles to move (Dresner and Stone, 2006, 2007). In addition, Qian et al. (2014) proposed to use car-following to avoid collisions with conventional vehicles, and Conde Bento et al. (2013) suggested that conventional vehicles could use AIM by reserving additional space to serve as a safety buffer. These strategies are compatible with the AIM* protocol that we propose. Therefore, we focus on the scenario for 100\% AVs. Although reservations can be implemented with conventional vehicles, they might not improve over signals until the AV market penetration is above 80\% (Levin and Boyles, 2016).

### 2.3. Networks of intersections

Because intersection control affects route choice (Smith, 1979), optimizing reservations requires consideration of network impacts. However, the AIM protocol is computationally intensive because it involves vehicle-to-intersection communications and microsimulation of reservation requests. As a result, most simulations of multiple intersections have been limited to small networks (Hausknecht et al., 2011) or required simplified tile models that also greatly reduced intersection efficiency (Carlino et al., 2012, 2013). Levin and Boyles (2015) proposed the conflict region model for dynamic traffic assignment that was shown to be tractable for city networks, and decentralized policies for the conflict region model (Levin et al., 2017; Levin and Boyles, 2017) were shown to reduced travel times across city networks.

To optimize throughput of traffic signals, several papers have proposed decentralized pressure-based policies based on the communications network research of Tassiulas and Ephremides (1992). These policies are typically decentralized but are proven to be throughput optimal for traffic networks. Varaiya (2013) developed a maximum-pressure control for signal phases, and proved that it maximizes network throughput. Wongpiromsarn et al. (2014) were able to show that their pressure-based policy maximized throughput for unbounded queues. However, practical limitations such as link length require careful choice of the pressure function to avoid queue spillback. Therefore, Xiao et al. (2014) proposed a pressure-releasing policy that accounts for finite queue capacities. Nonetheless, to more canonically apply the pressure-based routing they assumed that each turning movement has a separate queue, which is often not realistic. Le et al. (2015) proved stability for fixed turning proportions and unbounded queues, but also compared their signal control policy to other pressure-based policies. Several papers also studied pressure-based policies with respect to route choice (Zhang et al., 2012; Gregoire et al., 2014; Zaidi et al., 2015), which is important as Levin et al. (2016) showed that decentralized control of reservations could cause the Daganzo (1998) paradox.

With the exception of Levin and Boyles (2017), previous work on pressure-based intersection control has focused on adjusting traffic signal timings and phases. Previous studies on pressure-based policies used discretized-time queuing models, often through Markov decision process theory, because of the difficulties in proving throughput optimality. Although we only optimize a single intersection, our formulation differs from the models used in pressure-based policies in that we assume continuous time and include vehicle speeds as decision variables. Our objective function may be modified to implement decentralized pressure-based policies.

### 2.4. Trajectory optimization

Unlike pressure-based policies, our formulation optimizes vehicle intersection trajectories at a more microscopic level. We include continuous time and optimize vehicle speeds. Gregoire et al. (2013) developed a cooperative motion-planning algorithm using a pathvelocity decomposition to optimally coordinate vehicles while preventing collisions. De La Fortelle and Qian (2015) integrated a priority-based assignment into autonomous intersection simulation. Altché and De La Fortelle (2016) developed a MILP formulation to coordinate vehicles through intersections. However, unlike our formulation, they discretized time, and tracked vehicle movement in continuous space variables. We take the reverse approach: we choose discrete points in space at which vehicles might conflict, and optimize the time at which each vehicle passes through the discrete space points along their trajectory using continuous arrival time variables. Our approach might reduce the number of variables per vehicle, depending on the time discretization used by Altché and De La Fortelle (2016). Our space discretization considers only the points at which two vehicles might conflict, which reduces the number of spatial points along each trajectory. For our formulation, the number of variables does not increase with the time horizon (although of course it increases with the number of vehicles).

## 3. New reservation protocol

AIM is quite limited in its ability to optimize vehicle reservation timings. For instance, one of the proposed policies in the literature is based on queue lengths (Levin et al., 2017). When one incoming link has a much longer queue length, the policy gives priority to vehicles on that queue. However, in AIM vehicles cannot request a reservation until they know when they will reach the intersection. Vehicles in the middle of the queue may not request a reservation early enough for the IM to prioritize long queues. Unfortunately, the design of the AIM protocol limits its ability to implement potential reservation policies. In AIM, the IM can only
choose between the reservation requests that vehicles send it. For a more general protocol, the IM must be able to specify arbitrary reservations. Therefore, in this section we define a new protocol, AIM*. AIM* is a prerequisite to deploying the conflict point MILP we develop in Section 4.

A manager-centric communications protocol has been implicitly used by previous work on optimizing reservations, such as in Levin et al. (2017). In addition, de La Fortelle (2010) described a finite state machine approach to reserving intersection movements, and Zhang et al. (2013) developed a priority scheduling algorithm for reservations. However, neither these nor other studies on reservations have proposed a communications protocol for specifying intersection-optimized vehicle trajectories.

In AIM*, vehicles announce themselves and their positions to the IM, and the IM then specifies reservation assignments. Vehicles can "accept" or "reject" these assignments, but they are incentivized to accept reservations if possible because rejecting a reservation will typically result in additional delay. The AIM* protocol has several advantages over AIM:

- The IM is aware of all vehicles on each incoming link and their positions. Many policies could benefit from this information. For instance, the policy of prioritizing emergency vehicles (Dresner and Stone, 2006) is more effective if the IM is aware of emergency vehicles at the back of a queue.
- Reduced communications. In AIM, when a reservation request is rejected, the vehicle must make a new request at a later time. This incentivizes vehicles to send many reservation requests to receive an earlier reservation time.
- The computational effort of AIM* is determined by the IM rather than in reaction to vehicle reservation requests. In AIM, the IM must simulate each reservation request for feasibility. As discussed above, vehicles are incentivized to make many requests until one is accepted, which results in high, vehicle-driven computational requirements. In AIM*, the IM itself determines when to simulate and check feasibility of potential reservations.

By reducing the communications bandwidth and computational requirements, AIM* can reduce the operations costs for reservation-based control in addition to more efficient intersection control. The protocol implementation is defined in terms of vehicle and IM communications and actions.

### 3.1. Messages

The types of communications used in this protocol divided into vehicle to intersection messages (Section 3.1.1) and intersection to vehicle messages (Section 3.1.2). These messages are similar to those specified by Dresner and Stone (2005), except that the directions of the protocol communications are largely reversed. IMs communicate reservation parameters to vehicles, which accept or reject them.

We use the following notation to define the protocol. Let $G=(N, A)$ be the traffic network, with $N$ the set of nodes, i.e. intersection, and $A$ the set of links. For any node $n \in N$, let $\Gamma_{n}^{-} \subseteq A$ be the set of incoming links and $\Gamma_{n}^{+} \subseteq A$ be the set of outgoing links. We assume that each intersection $n$ is controlled by the IM $\mathscr{M}_{n}$. A movement $\left(n^{-}, n, n^{+}\right)$across intersection $n \in N$ consists of moving from link $\left(n^{-}, n\right) \in \Gamma_{n}^{-}$to link $\left(n, n^{+}\right) \in \Gamma_{n}^{+}$.

Throughout this protocol, we assume that messages have a unique and identifiable sender and recipient. Official specifications for vehicle-to-intersection communication technology have yet to be finalized. For instance, communications may involve broadcasting messages on specified frequencies. In addition to the information contained within each message, we assume that each message will contain vehicle and intersection identification information so that vehicles and IMs will ignore messages not sent to them. Furthermore, we assume that some type of error-checking (such as a checksum) is used to ensure that messages with errors in them are ignored.

### 3.1.1. Vehicle to intersection

Vehicle-position This message contains the vehicle position (via GPS), speed, and vehicle type. The vehicle type defines the physical length, speed, and acceleration constraints of the vehicle. We denote $\mathscr{V}$ the set of vehicles. After vehicle $i \in \mathscr{V}$ enters link $\left(n^{-}, n\right) \in A, i$ transmits a Vehicle-position message to $\mathscr{M}_{n}$. It becomes the responsibility of $\mathscr{M}_{n}$ to find a reservation for $i$ to move across the intersection. Repeated submissions of Vehicleposition messages can be used by the IM to update its information about the position and speed of $i$. However, unlike the reservation request messages in previous protocols (Dresner and Stone, 2005; Fajardo et al., 2011), the vehicle-position message does not require a response indicating acceptance or rejection. This avoids the computational burden of determining the response as well as reducing the communication requirements of the IM.
As reservation technology matures, reservation precision may improve to admit reduced safety margins and greater intersection capacity. This protocol is robust to such improvements in precision. The vehicle type parameter of the Vehicle-position message can be used by a vehicle $i$ to communicate the precision level that $i$ is capable of. The IM can account for the available precision in its reservation assignment.
Accept The Accept message indicates that the vehicle will comply with the assigned reservation. This message is used to acknowledge a reservation assignment so that the IM does not send duplicate Reservation messages.
Reject The Reject message indicates that a vehicle is unable to complete the assigned reservation. A vehicle that transmits a Reject message cannot enter the intersection until receiving another reservation assignment.

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-05.jpg?height=1312&width=1195&top_left_y=181&top_left_x=349)
Fig. 2. Vehicle and intersection manager actions and communications.

Therefore, when a vehicle rejects a reservation, the IM can use the space for other vehicles.
Reservation-complete After vehicle $i$ completes a movement across intersection $n \in N, i$ transmits a Reservation-complete message to $\mathscr{M}_{n}$. This message can be used by $\mathscr{M}_{n}$ as an indication to stop tracking $i$. This message is not necessary for safety, but reduces the computational requirements of $\mathscr{M}_{n}$.

### 3.1.2. Intersection to vehicle

Reservation The Reservation message specifies a reservation for a turning movement through the intersection. It includes the departure lane, arrival lane, intersection enter time, and speed and acceleration parameters. This contains all of the information necessary to ensure a sufficiently precise movement through the intersection.
By sending this message to a vehicle $i$, the IM guarantees that $i$ is permitted to make the specified turning movement. Therefore, the IM cannot send out two Reservation messages for two turning movement clearances that would result in a safety conflict.
Acknowledge This message is used to acknowledge receipt of a Vehicle-position, Reservation-complete, or Reject message. It contains the type of message being acknowledged. The receipt of Acknowledge messages by $i$ is not necessary for the safety of the protocol. However, it could reduce the number of messages sent. For instance, if $\mathscr{M}_{n}$ does not acknowledge that it has received the Vehicle-position message of $\mathscr{M}_{n}, i$ may resend it to ensure $\mathscr{M}_{n}$ is aware its position.

### 3.2. Protocol actions

The vehicles and the IM must obey certain rules and take certain actions for AIM* to work. Fig. 2 shows the typical flow of communications and actions.
3.2.1. Vehicle actions

Consider a vehicle $i$ with links $\left(n^{-}, n\right) \in \Gamma_{n}^{-}$and $\left(n, n^{+}\right) \in \Gamma_{n}^{+}$as part of its path. The communications and actions of $i$ are as follows:

1. After entering $\left(n^{-}, n\right), i$ sends a Vehicle-position message to $\mathscr{M}_{n}$. Vehicle $i$ continues to travel on $\left(n^{-}, n\right)$ while waiting for a response.
2. At some point (while traveling or while in the intersection queue), $i$ will receive a Reservation message from $\mathscr{M}_{n}$. If vehicle $i$ can make the specified reservation, $i$ will adjust its space-time trajectory to enter the intersection at the specified time and speed. Vehicle $i$ will also send an Accept message to $\mathscr{M}_{j}=n$ to indicate that $i$ will comply with the assigned reservation. If $i$ cannot make the reservation, or at a later time becomes aware that it cannot make the reservation, $i$ sends a Reject message to $\mathscr{M}_{n}$.
3. Once vehicle $i$ has an assigned reservation, it moves from $\left(n^{-}, n\right)$ to $\left(n, n^{+}\right)$.
4. Eventually, $i$ will enter link $\left(n, n^{+}\right)$. At that point, $i$ sends a Reservation-complete message to $\mathscr{M}_{n}$.

In addition, $i$ must follow these rules in AIM*:

- $i$ may not enter the intersection without a reservation. If $i$ receives a Reservation message, $i$ is considered to have a reservation. (Recall that all messages have specific and unique senders and receivers).
- If $i$ has a reservation, $i$ must follow the specified path to within the specified or assumed precision tolerances. If unable, $i$ cannot enter the intersection and must send a Reject message.
- $i$ may send a Vehicle-position message to $n \in N$ if and only if $i$ is on link $\left(n^{-}, n\right)$.
- $i$ must send a Reservation-complete message to $n \in N$ after entering a link $\left(n, n^{+}\right) \in \Gamma_{n}^{+}$.

3.2.2. Intersection actions

We now describe the actions of the IM $\mathscr{M}_{n} . \mathscr{M}_{n}$ maintains a list of all vehicles $V_{n}$ on the links $\Gamma_{n}^{-} . \mathscr{M}_{n}$ also maintains a list $W_{n} \subseteq V_{n}$ of vehicles without an assigned reservation. The communications and actions of $\mathscr{M}_{n}$ with $i$ are as follows:

1. Upon receiving a Vehicle-position message from $i, \mathscr{M}_{n}$ adds $i$ to $W_{n}$ and $V_{n}$, and sends a Acknowledge message to $i$.
2. $\mathscr{M}_{n}$ analyzes $W_{n}$ and assigns reservations to some subset $W_{n}^{\prime} \subseteq W_{n}$. In assigning the new reservations, $\mathscr{M}_{n}$ must also ensure that they do not conflict with reservations given to vehicles in $V_{n} \backslash W_{n} . \mathscr{M}_{n}$ sends a Reservation message to each vehicle $i \in W_{n}^{\prime}$ and sets $W_{n}$ to be $W_{n} \backslash W_{n}^{\prime}$.
3. If $\mathscr{M}_{n}$ receives a Reject message from $i, \mathscr{M}_{n}$ sends an Acknowledge message to $i$, adds $i$ to $W_{n}$ again, and returns to step 2.
4. After receiving a Reservation-complete message from $i, \mathscr{M}_{n}$ removes $i$ from $V_{n}$ and sends a Acknowledge message to $i$.

The IM has the following responsibilities in AIM*:

- Once $\mathscr{M}_{n}$ is aware of $i$, it is the responsibility of $\mathscr{M}_{n}$ to find a feasible reservation for $i$. If no reservation is given, $i$ cannot enter the intersection and will block traffic.
- $\mathscr{M}_{n}$ cannot issue two reservations that result in a safety conflict. Once $\mathscr{M}_{n}$ sends a Reservation message to $i, i$ is considered to have the specified reservation.

3.3. Contributions of AIM*

In terms of implementation, AIM and AIM* require similar types of communications. Instead of vehicles sending reservation requests to the IM, the IM sends reservation assignments to the vehicles. Compared with AIM (Dresner and Stone, 2005), the communication flow is largely reversed. The value in AIM* is that the IM is aware of all vehicles on incoming links. In AIM, the IM is only aware of vehicles that have submitted reservation requests. Since vehicles cannot request a specific time until they know when they will reach the intersection, the IM may not be aware of all vehicles in a platoon when the most efficient policy would be to move the entire platoon together. More generally, in Section 4 we will formulate a mixed integer linear program that allows the IM to choose the order of vehicle movements for arbitrary objective functions.
4. Conflict point formulation

Having defined the AIM* protocol which admits arbitrary vehicle reservation assignments specified by the IM, we now develop an MILP to determine the optimal reservations for a single intersection. As previously discussed, we focus on a single intersection because networks of intersections adds considerable complexity, which reduces tractability. This is not a limitation when using decentralized policies that have been shown to be effective for city networks (Levin et al., 2017; Levin and Boyles, 2017). Since the notation in the remainder of this paper focuses on the single intersection optimization, we will simplify the notation to remove network-level indices.

We replace the tiles in early work on reservations (Dresner and Stone, 2004, 2006) with conflict points, which are the intersections between different turning movement paths. Conflict points are an alternative method of ensuring collision avoidance that are more amenable to mathematical programming formulations. Appendix A derives the conflict points for a standard four-approach intersection. Two vehicles are separated if they do not occupy the same conflict point at the same time. This is similar to the separation requirement for tiles (Dresner and Stone, 2004, 2006), but conflict points are only placed where potential conflicts occur. Conflict
points have previously been used to model reservations by Zhu and Ukkusuri (2015), although their formulation was intended for use within dynamic traffic assignment rather than as a deployable solution to reservation-based intersection control. Conflict points have also been used for aircraft separation models (Rey et al., 2012, 2015a,b), but aircraft require different separation constraints. Appendix A gives the conflict points for a symmetric four approach, two lanes per approach intersection. Conflict points for other intersection configurations may be derived geometrically.

### 4.1. Notation

Consider a single intersection with set of vehicles $\mathscr{V}$. The intersection has sets of entry and exit lanes, $\Gamma^{-}$and $\Gamma^{+}$, respectively. Let $\mathscr{C}$ be the set of all conflict points. Each vehicle requests a turning movement traveling from an entry lane to an exit lane. We assume all specified turning movements are legal and physically feasible. Each vehicle requires a path $\rho_{i}$ through the intersection, which is an ordered set of conflict points. For each vehicle $i$, we must determine $t_{i}(c)$, which is the time that $i$ passes through point $c$, for all $c \in \rho_{i}$. The first point in $\rho_{i}$ is the entrance to the intersection, and the last point is the exit point for the intersection. Then $t_{i}\left(\gamma_{i}^{-}\right)$is the time at which $i$ enters the intersection.

We assume that vehicles travel at an uniform speed through the intersection, but that the speed is a decision variable. The reason for this assumption is that varying speeds can greatly complicate determining how long vehicles occupy conflict points because vehicles may occupy multiple conflict points simultaneously. Although the uniform speed assumption may be relaxed in future work, we use it here to focus on the exposition of the conflict avoidance formulation.

Let $\underline{U}_{i}$ and $\bar{U}_{i}$ be the minimum and maximum speed for which $i$ can travel through the intersection, respectively. We require a minimum speed to ensure that vehicles to do not spend arbitrarily long times in the intersection. For each vehicle $i$, and conflict point $c \in \rho_{i}, i$ takes some time $\tau_{i}(c)$ to completely pass through $c . \tau_{i}(c)$ is a function of the vehicle speed during the turning movement. Thus, when $i$ moves through the intersection, $c$ is unusable during the time interval $\left[t_{i}(c), t_{i}(c)+\tau_{i}(c)\right)$. An appropriate buffer may be added to $\tau_{i}(c)$ to ensure sufficient separation. $t_{i}\left(\gamma_{i}^{+}\right)+\tau_{i}\left(\gamma_{i}^{+}\right)$is the time at which $i$ exits the intersection.

### 4.2. Vehicle ordering

Assume that vehicles do not change lanes while under the control of the intersection manager. Therefore, FIFO holds on all lanes. Let $e_{i}$ denote the earliest time that $i$ could reach the intersection. Then

$$
t_{i}\left(\gamma_{i}^{-}\right) \geqslant e_{i} \quad \forall i \in \mathscr{V}
$$

Assume without loss of generality that $e_{i}<e_{j}$, so $i$ comes before $j$ in the lane queue. Then $t_{i}\left(\gamma_{i}^{-}\right)<t_{j}\left(\gamma_{j}^{-}\right)$must hold as well. Because $i$ occupies $\gamma_{i}^{-}$for $\tau_{i}\left(\gamma_{i}^{-}\right)$,

$$
t_{i}\left(\gamma_{i}^{-}\right)+\tau_{i}\left(\gamma_{i}^{-}\right) \leqslant t_{j}\left(\gamma_{i}^{-}\right) \quad \forall i, j \in \mathscr{V}: \gamma_{i}^{-}=\gamma_{j}^{-}, e_{i}<e_{j}
$$

### 4.3. Travel time between conflict points

For some vehicle $i$ and any two conflict points $c_{1}, c_{2} \in \rho_{i}$ with $c_{2}$ after $c_{1}$ in $\rho_{i}$, let $d_{i}\left(c_{1}, c_{2}\right)$ be the distance $i$ travels between $c_{1}$ and $c_{2}$. Note that $d_{i}\left(c_{1}, c_{2}\right)$ may not be the Euclidean distance between $c_{1}$ and $c_{2}$ because turning vehicles may travel along an elliptical path (e.g. for left turns). The minimum and maximum vehicle speeds place constraints on the travel time through the intersection:

$$
\frac{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}{\bar{U}_{i}} \leqslant t_{i}\left(\gamma_{i}^{+}\right)-t_{i}\left(\gamma_{i}^{-}\right) \leqslant \frac{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}{\underline{U}_{i}} \quad \forall i \in \mathscr{V}
$$

Furthermore, we require that vehicles maintain the same speed throughout the intersection. This is to ensure that vehicles move through conflict points properly. If several conflict points are close together, with distance smaller than vehicle length, speed changes could result in the vehicle blocking a conflict point but not triggering the corresponding constraint. Therefore:

$$
\frac{t_{i}(c)-t_{i}\left(\gamma_{i}^{-}\right)}{d_{i}\left(\gamma_{i}^{-}, c\right)}=\frac{t_{i}\left(\gamma_{i}^{+}\right)-t_{i}\left(\gamma_{i}^{-}\right)}{d\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)} \quad \forall i \in \mathscr{V}, \forall c \in \rho_{i}
$$

### 4.4. Time spent at conflict points

For each vehicle $i$ traversing the intersection, we can determine the time spent at each conflict point $c \in \rho_{i}, \tau_{i}(c)$. based on geometry of $i$ and turning movement shape (straight or circular). Specifically, let $D_{i}(c)$ be the spacing required by $i$ at $c$. This spacing should depend on the vehicle speed in case an emergency braking is required to avoid a collision for unforeseen circumstances (such as a vehicle stall or a pedestrian jaywalking). The spacing for a given speed may be derived from the speed-density relationship, and can be used to specify the desired flow-density relationship for reservation travel. Eq. (4) gives the speed of vehicle $i, u_{i}$, as

$$
u_{i}=\frac{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}{t_{i}\left(\gamma_{i}^{+}\right)-t_{i}\left(\gamma_{i}^{-}\right)}
$$

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-08.jpg?height=371&width=1296&top_left_y=181&top_left_x=298)
Fig. 3. Calculation of $L_{i}(c)$ along circular paths.

Using the inverse speed of the vehicle, the time vehicle $i$ spends at conflict point $c$ is

$$
\tau_{i}(c)=\frac{D_{i}(c)}{u_{i}} \quad \forall i \in \mathscr{V}, \forall c \in \rho_{i}
$$

For simplicity in the formulation, assume that the fundamental diagram is triangular (Newell, 1993; Yperman et al., 2005). The fundamental diagram is defined as

$$
q(k)=\min \left\{\overline{U_{i}} k, w(K-k)\right\}
$$

where $k$ is the density, $K$ is the jam density, $w$ is the congested wave speed, and $q(k)$ is the flow-density relationship. We assume that $K$ and $w$ are constants.

Speeds are constrained by spacing only in the congested region, and from Eq. (7) the speed satisfies

$$
u_{i}=\frac{w}{k}(K-k)
$$

Let $L_{i}(c)$ be the distance the vehicle travels around $c$. If the turning movement is a straight line, $L_{i}(c)=l_{i}$, where $l_{i}$ is the length of $i$. For left and right turns, the vehicle will travel for a greater distance while occupying $c$. For circular turns (e.g. left and right turns in a symmetric intersection), $L_{i}(c)=4 R \sin ^{-1}\left(\frac{l_{i}}{2 R}\right)$ where $R$ is the turn radius, as shown in Fig. 3.

Using the fact that spacing is the inverse of density, i.e. $D_{i}(c)=\frac{1}{k}$ and $K=\frac{1}{L_{i}(c)}$, Eq. (8) can be rewritten as

$$
D_{i}(c)=L_{i}(c) \frac{u_{i}+w}{w}
$$

From Eqs. (9), (6) can then be rewritten as

$$
\begin{aligned}
\tau_{i}(c) & =L_{i}(c) \frac{u_{i}+w}{u_{i} w} \\
& =\frac{L_{i}(c)}{w}+\frac{L_{i}(c)}{u_{i}} \\
& =\frac{L_{i}(c)}{w}+\frac{L_{i}(c)\left(t_{i}\left(\gamma_{i}^{+}\right)-t_{i}\left(\gamma_{i}^{-}\right)\right)}{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}
\end{aligned}
$$

which is linear in the decision variables of conflict point arrival times.

### 4.5 Separation at conflict points

For any two vehicles $i, j \in \mathscr{V}$, let $\delta_{i j}(c) \in\{0,1\}$ denote whether $i$ and $j$ overlap at $c . \delta_{i j}(c)$ is sensitive to the order of vehicles, so each pair of vehicles has two such $\delta$ variables per shared conflict point. $\delta_{i j}(c)=1$ if $j$ arrives at $c$ after $i$ has left. Thus, $\delta_{i j}(c)=1$ if $t_{j}(c) \geqslant t_{i}(c)+\tau_{i}(c)$. This is written as

$$
t_{i}(c)+\tau_{i}(c)-t_{j}(c) \leqslant\left(1-\delta_{i j}(c)\right) M_{i j} \quad \forall i, j \in V, \forall c \in \rho_{i} \cap \rho_{j}
$$

where $M_{i j}$ is a large positive constant. If $t_{j}(c) \geqslant t_{i}(c)+\tau_{i}(c)$ then $\delta_{i j}(c)=1$; otherwise $\delta_{i j}(c)=0$. Note that it suffices to have $M_{i j} \geqslant \max \left\{t_{i}(c)+\tau_{i}(c)-t_{j}(c)\right\}$ for this separation constraint to be valid.

Separation is guaranteed for any two pair of vehicles $i, j \in \mathscr{V}$ and any conflict point $c$ if $j$ enters $c$ after $i$ leaves, or if $i$ enters $c$ after $j$ leaves:

$$
\delta_{i j}(c)+\delta_{j i}(c)=1 \quad \forall i, j \in \mathscr{V}: i<j, \forall c \in \rho_{i} \cap \rho_{j}
$$

Constraint (12) does not depend on vehicle ordering, and therefore occurs once per pair of vehicles per shared conflict point.
Note that the number of binary $\delta_{i j}(c)$ variables may be reduced for vehicles with $\gamma_{i}^{-}=\gamma_{j}^{-}$. For such pairs vehicles, the ordering at the entry point determines the ordering at any conflict points that they share. Constraints (11) and (12) may therefore be replaced with

$$
t_{i}(c)+\tau_{i}(c) \leqslant t_{j}(c) \quad \forall i, j \in \mathscr{V}: \gamma_{i}^{-}=\gamma_{j}^{-}, e_{i}<e_{j}, \forall c \in \rho_{i} \cap \rho_{j}
$$

for pairs of vehicles $i, j \in \mathscr{V}$ with $\gamma_{i}^{-}=\gamma_{j}^{-}$.

### 4.6. Objective function

The objective function represents how the intersection manager aims to operate traffic. An intuitive objective consists in maximizing intersection throughput. While this approach may maximize social welfare, such an intersection control policy may also lead to imbalanced vehicle delays, thus potentially impacting acceptability. Alternatively, the intersection manager may seek to minimize the maximum delay experienced or maximize fairness. These alternative objective functions aim to incorporate some level of fairness in the allocation of reservation assignments at the vehicular scale. More elaborate fair objective functions can also be designed to balance reservation assignments across routes or traffic approaches (e.g. North, South, East, West).

Because the constraints guarantee complete separation of vehicles through the intersection, the objective function decides in which order vehicles should move. Denote by $f_{i}>0$ the weight of each vehicle, which indicates its priority for movement. The weights can model a variety of situations. For instance, $f_{i}=1$ for all vehicles is maximum throughput. $f_{i}=e_{i}$ weights vehicles by earliest arrival time, which is similar to a fairness based objective. Note that $f_{i}=e_{i}$ is not the same as the FCFS policy used in previous work on reservations, because FCFS results in absolute priority for the vehicle with the earliest arrival time. The objective $f_{i}=e_{i}$ may delay early-arriving vehicles to find the combination with the greatest fairness.

In this paper, we focus on two optimal intersection control formulations: flow-maximization with and without FCFS constraints. The proposed objective function values movements by the time vehicles exit the intersection, $t_{i}\left(\gamma_{i}^{+}\right)+\tau_{i}\left(\gamma_{i}^{+}\right)$:

$$
\min \sum_{i \in \mathscr{V}} f_{i}\left(t_{i}\left(\gamma_{i}^{+}\right)+\tau_{i}\left(\gamma_{i}^{+}\right)\right)
$$

Exit times are chosen because vehicle speeds are an implicit decision variable. Both vehicle delays and slower turn speeds will increase the objective value. Note that the objective function (14) will never be equal to 0 if $f_{i}>0$. To obtain a measure of delay for vehicle $i$, we can subtract the constant term $\frac{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}{U_{i}}+e_{i}$, which is the earliest time that vehicle $i$ could exit the intersection.

### 4.7. Mixed integer linear program

Combining the above constraints and objective function results in the MILP represented by (15)-(24), henceforth referred to as the Conflict-Point Intersection Control (CPIC) formulation.

$$
\begin{aligned}
& \min \sum_{i \in \mathscr{V}} f_{i}\left(t_{i}\left(\gamma_{i}^{+}\right)+\tau_{i}\left(\gamma_{i}^{+}\right)\right) \\
& \text {s.t.t. } t_{i}\left(\gamma_{i}^{-}\right) \geqslant e_{i} \quad \forall i \in \mathscr{V} \\
& t_{i}\left(\gamma_{i}^{-}\right)+\tau_{i}\left(\gamma_{i}^{-}\right) \leqslant t_{j}\left(\gamma_{j}^{-}\right) \quad \forall i, j \in \mathscr{V}: \gamma_{i}^{-}=\gamma_{j}^{-}, e_{i}<e_{j} \\
& \tau_{i}(c)=\frac{L_{i}}{w}+\frac{L_{i}\left(t_{i}\left(\gamma_{i}^{+}\right)-t_{i}\left(\gamma_{i}^{-}\right)\right)}{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)} \quad \forall i \in \mathscr{V}, \forall c \in \rho_{i} \\
& \frac{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}{\overline{U_{i}}} \leqslant t_{i}\left(\gamma_{i}^{+}\right)-t_{i}\left(\gamma_{i}^{-}\right) \leqslant \frac{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}{\underline{U}_{i}} \quad \forall i \in \mathscr{V} \\
& \frac{t_{i}(c)-t_{i}\left(\gamma_{i}^{-}\right)}{d_{i}\left(\gamma_{i}^{-}, c\right)}=\frac{t_{i}\left(\gamma_{i}^{+}\right)-t_{i}\left(\gamma_{i}^{-}\right)}{d\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)} \quad \forall i \in \mathscr{V}, \forall c \in \rho_{i} \\
& t_{i}(c)+\tau_{i}(c) \leqslant t_{j}(c) \quad \forall i, j \in \mathscr{V}: \gamma_{i}^{-}=\gamma_{j}^{-}, e_{i}<e_{j}, \forall c \in \rho_{i} \cap \rho_{j} \\
& t_{i}(c)+\tau_{i}(c)-t_{j}(c) \leqslant\left(1-\delta_{i j}(c)\right) M_{i j} \quad \forall i, j \in \mathscr{V}: \gamma_{i}^{-} \neq \gamma_{j}^{-}, \forall c \in \rho_{i} \cap \rho_{j} \\
& \delta_{i j}(c)+\delta_{j i}(c)=1 \quad \forall i, j \in \mathscr{V}: \gamma_{i}^{-} \neq \gamma_{j}^{-}, i<j, \forall c \in \rho_{i} \cap \rho_{j} \\
& \delta_{i j}(c) \in\{0,1\} \quad \forall i, j \in \mathscr{V}: \gamma_{i}^{-} \neq \gamma_{j}^{-}, \forall c \in \rho_{i} \cap \rho_{j}
\end{aligned}
$$

The decision variables are the arrival times at each conflict point for each vehicle $i, t_{i}(c)$, and vehicle ordering at conflict points, determined by $\delta_{i j}(c)$ variables. The times spent at conflict points, $\tau_{i}(c)$, is defined by the speed at which vehicle $i$ moves through the intersection, which is implicitly defined by vehicle-specific arrival times at conflict points. It is not known whether Model CPIC is NP-hard. However, similar collision avoidance models for aircraft (Chiang et al., 1997) can be generalized as a motion planning problem in the presence of obstacles, which is NP-hard in most cases (Reif and Sharir, 1994).

Model CPIC is always feasible because there is no upper bound on vehicle entry and exit times. If necessary, vehicles could be given arbitrarily long delays to ensure that collision avoidance constraints are satisfied. Proposition 1 constructs a trivial feasible solution.

Proposition 1. Model CPIC has at least one feasible solution.
Proof 1 . Consider the solution constructed as follows. Sort $\mathscr{V}$ by increasing $e_{i}$ for all $i \in \mathscr{V}$ and let index $i=0$ denote the first vehicle. Let $t_{0}\left(\gamma_{0}^{-}\right)=e_{0}$ and for each $i \in \mathscr{V} \backslash\{0\}$, let $t_{i}\left(\gamma_{i}^{-}\right)=\max \left\{e_{i}, t_{i-1}\left(\gamma_{i-1}^{+}\right)+\tau_{i-1}\left(\gamma_{i-1}^{+}\right)\right\}$. Set $t_{i}\left(\gamma_{i}^{+}\right)=t_{i}\left(\gamma_{i}^{-}\right)+\frac{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}{D_{i}}$, and choose $t_{i}(c)$ according to constraint (20) for all $c \in \rho_{i} /\left\{\gamma_{i}^{-}, \gamma_{i}^{+}\right\}$. Then, Constraints (16), (17), (19), and (20) are satisfied by definition. Constraints (18) and (22)-(24) are satisfied because only one vehicle is in the intersection at any time.

Vehicles' waiting time at the intersection entry points is unbounded, hence the values $M_{i j}$ may also be unbounded. Specifically, if $\delta_{i j}=0$, then Constraint (22) becomes $t_{i}(c)+\tau_{i}(c)-t_{j}(c) \leqslant M_{i j}$, which should hold for any values of the decision variables involved therein. Since $\max \left\{t_{i}(c)+\tau_{i}(c)-t_{j}(c)\right\} \rightarrow \infty$, the big-M values should be chosen carefully to maintain feasibility and avoid cutting out the optimal solution. The proof of Proposition 1 provides a method to construct a feasible solution to Model CPIC. We can use this solution to tighten the big-M values $M_{i j}$. Let $i=|\mathscr{V}|-1$ denote the last vehicle in the sorted set $\mathscr{V}$ and let $\bar{t}=t_{|\mathscr{V}|-1}\left(\gamma_{|\mathscr{K}|-1}^{+}\right)+\tau_{|\mathscr{V}|-1}\left(\gamma_{|\mathscr{Y}|-1}^{+}\right)$denote the latest instant reserved by the intersection. Then $M=\bar{t}-e_{0}$ is a valid big-M value for any pair of vehicles.
4.8. First-come-first-served policy

Previous work on AIM mostly used the first-come-first-served (FCFS) policy, in which vehicles are prioritized in the order their reservation requests are received. We create a FCFS policy here for the purposes of comparison, as FCFS is suboptimal in some common situations (Levin et al., 2016). Since AIM* does not include a reservation request time (as vehicles do not request reservations), we assume that the order of reservation requests is the same as the order of earliest arrival times. (Note that the Vehicleposition message is not the same as a reservation request because vehicles cannot request a reservation until they know their arrival time at the intersection, which depends on other vehicles.) Consequently, the resulting policy is the same as a first-in-first-out policy due to this assumption.

To prioritize vehicles by their earliest arrival time, we add the following constraints to Model CPIC:

$$
\begin{aligned}
& t_{i}\left(\gamma_{i}^{-}\right) \leqslant t_{j}\left(\gamma_{j}^{-}\right) \quad \forall i, j \in \mathscr{V}: e_{i}<e_{j} \\
& t_{i}\left(\gamma_{i}^{+}\right) \leqslant t_{j}\left(\gamma_{j}^{+}\right) \quad \forall i, j \in \mathscr{V}: e_{i}<e_{j}
\end{aligned}
$$

For brevity we abuse notation and henceforth refer to this formulation as FCFS. Model FCFS allows vehicles to move together as long as they do not conflict, but vehicles cannot enter or exit the intersection before earlier arriving vehicles. Constraint (25) follows from the definition of the FCFS policy. Constraint (26) is to prevent early arriving vehicles from being given low-speed reservations while later vehicles are given high-speed reservations that allow them to exit earlier. This is not an issue when vehicles request reservations because vehicles would be more likely to request maximum-speed movements, but is potentially an issue when the IM assigns reservations via the AIM* protocol. Model FCFS is also feasible because the solution constructed in Proposition 1 is also feasible for Model CPIC with the added constraints (25) and (26). However, the additional constraints imply that the solution of Model CPIC will always be at least as good as the solution with FCFS constraints.
4.9. Initial numerical results

We conducted a preliminary study to explore the computational performance of Model CPIC under a varying traffic demand. We used CPLEX to solve Model CPIC via its Java interface on an Intel i5-4590 CPU clocked at 3.30 GHz with 8 GB of memory. Because this collision avoidance problem was formulated as an MILP solved using CPLEX's branch-and-cut algorithm, computation times increased at a high rate with the number of vehicles. Fig. 4 shows computation times as a function of the number of vehicles using the benchmark intersection detailed in Appendix A. Reported computation times are the average of 100 Monte Carlo simulations. Vehicle earliest arrival times were based on a Poisson distribution with a demand of 800 vph per lane. Through movements were $80 \%$ of the total demand, and left and right turns each comprised 10\% of the total demand. The measured computation times show that Model CPIC can be solved in real-time for up to 30 vehicles, at fairly high traffic demand. To handle larger time horizons and number of vehicles, as well as to cope with the uncertainty in traffic demand we adopt a rolling horizon approach.
5. Rolling horizon framework

In this section, we introduce a rolling horizon framework to solve the proposed intersection control problem in real-time over large periods of time. As observed by the initial results presented in Section 4.9, the runtime required to solve Model CPIC increases with traffic demand. In order to remain suitable for real-time intersection control, computational runtime should be kept to a minimum. Further, future traffic demand may not be known perfectly. For instance, in the AIM* protocol, vehicles are only expected to communicate with the IM once they enter an incoming link to the intersection and no information on expected demand is assumed available. To address these operational challenges, we propose to use a finite look-ahead time window (horizon) and restrict the traffic demand for the MILP accordingly. We then iteratively slide the horizon with a predefined time step, update the traffic demand and solve Model CPIC periodically (for each time step).

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-11.jpg?height=629&width=1287&top_left_y=183&top_left_x=300)
Fig. 4. Average computation times for increasing numbers of vehicles.

### 5.1. Dynamic reservation policies

The rolling horizon framework is characterized by two parameters: the time horizon, $\Delta T$ determines which vehicles are considered by the IM; and the time step, $p$ determines the periodicity of the traffic demand update. For every time $T \in\{0, p, 2 p, 3 p, \ldots\}$, Model CPIC is solved for vehicles able to enter the intersection during the interval $[T, T+\Delta T)$.

To ensure that no vehicle is left out it is necessary that $\Delta T \geqslant p$. If $\Delta T=p$, the rolling horizon configuration is myopic with regards to future traffic demand and may potentially lead to unstable traffic flow management policies. Hence a configuration with $\Delta T>p$ is generally preferred. In this case, two consecutive time horizons overlap during $\Delta T-p$, which provides a more informed framework.

We propose two dynamic reservation policies to manage vehicle reservations over multiple iterations. The proposed policies differ in the way the reservations of the overlapping traffic demand are treated at the next iteration. The as soon as possible (ASAP) policy finalizes reservations as soon as vehicles send a Vehicle-position message to the IM. The as late as possible (ALAP) policy takes the opposite view, and delays assigning reservations until vehicles are about to enter the intersection. There are several potential advantages for early reservation finalizations. First, when vehicles know their reservation in advance, they can adjust their speed to reach the intersection at the appropriate time. This speed adjustment reduces fuel consumption and avoids start-up lost times. Also, AIM* requires two-way communications to verify a reservation, in the form of a Reservation message and Accept or Reject reply. Setting reservations earlier could improve the reliability of the communications in the AIM* protocol. On the other hand, ALAP offers more freedom in the optimization by delaying reservation assignments as much as possible in the hope to further improve the traffic flow across the intersection.

Formally, for every time $T \in\{0, p, 2 p, 3 p, \ldots\}$, under the ASAP policy, all vehicle trajectories optimized at $T$ will retain their reservation at $T+P$. In contrast, under the ALAP policy, only vehicles with an entry time $t_{i}\left(\gamma_{i}^{-}\right)<T+p$ will retain their reservation at iteration $T+p$ while the rest of them may be re-optimized in response to later traffic demand. (In terms of implementation with AIM*, vehicles with $t_{i}\left(\gamma_{i}^{-}\right) \geqslant T+p$ will not be assigned a reservation by the IM until later.) Consequently, the ASAP policy will result in MILP instances with less decision variables compared to the ALAP policy since the space-time trajectories of traffic demand from the previous iteration will be treated as fixed. Hence, it is expected that the ASAP policy outperforms the ALAP policy in terms of computational resources in exchange for degrees of freedom. From an operational perspective, both dynamic reservation policies have merits, but the ASAP policy may be easier to deploy for communication protocol and energy consumption reasons. We compare both policies in our numerical experiments.

### 5.2. Implementation

To implement policies ASAP and ALAP, we introduce two sets $\mathscr{V}_{T}$ and $\overline{\mathscr{V}_{T}}$ with the union representing all active vehicles at iteration $T$ of the rolling horizon. Active vehicles includes the set $\mathscr{V}_{T}$ of vehicles $i \in \mathscr{V}$ without a finalized reservation which earliest arrival time is such that $e_{i}<T+\Delta T$; and the set $\overline{y_{T}}$ of vehicles with a finalized reservation which will occupy the intersection for some time in the interval $[T, T+\Delta T)$. For each vehicle $i \in \mathscr{V}$ and $c \in \rho_{i}$, we denote $\bar{t}_{i}(c)$ and $\bar{\tau}_{i}(c)$ the finalized arrival time and occupancy values. If $\bar{t}_{i}\left(\gamma_{i}^{+}\right)<T$, then $i$ is inactive and can be omitted from $\overline{\gamma_{T}}$ without affecting the traffic for the interval $[T, T+\Delta T)$ since it will have exited the intersection by time $T$.

Let $r_{i}, \forall i \in \mathscr{V}$ be a binary indicator taking value 1 if $i$ has a finalized reservation and 0 otherwise, formally:

$$
\begin{aligned}
& \mathscr{V}_{T}=\left\{i \in \mathscr{V}: r_{i}=0, e_{i}<T+\Delta T\right\} \\
& \overline{\mathscr{V}_{T}}=\left\{i \in \mathscr{V}: r_{i}=1, \bar{t}_{i}\left(\gamma_{i}^{+}\right) \geqslant T\right\}
\end{aligned}
$$

From an optimization standpoint，at each iteration $T$ ，Model CPIC can be solved by replacing $\mathscr{V}$ with the set of active vehicles $\mathscr{V}_{T} \cup \overline{\mathscr{V}_{T}}$ ．In addition，for each vehicle $i \in \overline{\mathscr{V}_{T}}$ and each conflict point $c \in \rho_{i}$ ，the decision variables $t_{i}(c)$ and $\tau_{i}(c)$ are replaced by the finalized arrival time and occupancy time values $\bar{t}_{i}(c)$ and $\bar{\tau}_{i}(c)$ ．The reservations of vehicles in $\overline{r_{T}}$ are fixed and will not change based on ulterior optimizations but must be included in the formulation until these vehicles have exited the intersection as they may take up intersection space．Policies ASAP and ALAP differ in the way the set $\overline{y_{T}}$ is managed．

The proposed rolling horizon framework can be implemented using Algorithm 1：at time $T$ ，the MILP is solved for the interval $[T, T+\Delta T)$ ．Let $t_{i}^{\frac{1}{2}}(c)$ and $\tau_{i}^{\frac{1}{2}}(c)$ denote the optimal arrival times and occupancy times for vehicle $i \in \mathscr{V}_{T}$ at conflict point $c \in \rho_{i}$ ， respectively．For the ASAP policy，if $t_{i}^{\mathrm{A}}\left(\gamma_{i}^{-}\right) \in[T, T+\Delta T)$ ，then the reservation of $i$ is finalized and all the corresponding decision variables are fixed accordingly，i．e． $\bar{t}_{i}(c):=t_{i}^{\text {租 }}(c)$ and $\bar{\tau}_{i}(c):=\tau_{i}^{\text {辥 }}(c)$ ，for all $c \in \rho_{i}$ ．For the ALAP policy，the condition for reservation finalization is stricter：only if $t_{i}^{\text {★ }}\left(\gamma_{i}^{-}\right) \in[T, T+p)$ will the reservation of $i$ be finalized．Note that in line 5，it is not necessary that the entirety of $\mathscr{V}$ be known，only the subset of $\mathscr{V}$ that has an earliest arrival time between $T$ and $T+\Delta T$ ．We assume that once the IM decides to assign vehicle $i$ a reservation in line 20，the reservation is communicated to $i$ via the AIM＊protocol and the IM executes the reservation at $\bar{t}_{i}\left(\gamma_{i}^{-}\right)$．Handling vehicles that fail to follow the assigned reservation is outside the scope of this paper，and discussed further by Dresner and Stone（2008）．

Algorithm 1．Rolling horizon framework（policy）

```
for all \(i \in \mathscr{V}\) do
    \(r_{i}:=0\)
end for
for all \(T \in\{0, p, 2 p, 3 p, \ldots\}\) do
    \(\mathscr{V}_{T}:=\left\{i \in \mathscr{V}: r_{i}=0, e_{i}<T+\Delta T\right\}\)
    \(\overline{\mathscr{V}_{T}}:=\left\{i \in \mathscr{V}: r_{i}=1, \bar{t}_{i}\left(\gamma_{i}^{+}\right) \geqslant T\right\}\)
    Solve Model CPIC
    for all \(i \in \mathscr{V}_{T}\) do
        if policy = ALAP then
            \(F:=p\)
        else if policy = ASAP then
            \(F:=\Delta T\)
        end if
        if \(t_{i}^{\text {★ }}\left(\gamma_{i}^{-}\right) \in[T, T+F)\) then
            for all \(c \in \rho_{i}\) do
                \(\bar{t}_{i}(c):=t_{i}^{\frac{1}{4}}(c)\)
                \(\bar{\tau}_{i}(c):=\tau_{i}^{{ }^{\text {放 }}}(c)\)
                \(n_{i}:=1\)
            end for
            Assign \(i\) a reservation at \(\bar{t}_{i}\left(\gamma_{i}^{-}\right)\)
        end if
    end for
end for
```


## 6．Experimental results

We performed a variety of experiments with the rolling horizon and fixed－horizon methods on the four－approach，two lane intersection depicted in Fig． 9 with lane widths of 12 ft．Appendix A derives the conflict point geometry with an inter－lane distance $\lambda=0$ ，a right－turn radius $\mu_{R}=6 \mathrm{ft}$ ，a left－turn radius $\mu_{L}=30 \mathrm{ft}$ and an intersection width $\omega=48 \mathrm{ft}$ ．We evaluated solutions on the metrics of total delay and throughput，defined as follows．

Delay， $\mathscr{D}$ ，is the additional time vehicles spend in the intersection，relative to the minimum possible time：

$$
\mathscr{D}=\sum_{i \in \mathscr{V}}\left(t_{i}\left(\gamma_{i}^{+}\right)-e_{i}-\frac{d_{i}\left(\gamma_{i}^{-}, \gamma_{i}^{+}\right)}{\bar{U}_{i}}\right)
$$

The objective function（14）with $f_{i}=1$ minimizes Eq．（29）because $e_{i}$ is a constant for every vehicle $i$ ．
Throughput is the number of vehicles passing through the intersection per unit time．The average throughput， $\mathscr{D}$ ，is calculated as

$$
\mathscr{Q}=\frac{|\mathscr{V}|}{\sum_{i \in \mathscr{V}}\left(t_{i}\left(\gamma_{i}^{+}\right)+\tau\left(\gamma_{i}^{+}\right)-t_{i}\left(\gamma_{i}^{-}\right)\right)}
$$

Note that the denominator of Eq．（30）differs from the definition of $\mathscr{T} . \mathscr{T}$ includes time spent waiting to enter the intersection，

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-13.jpg?height=1155&width=1559&top_left_y=179&top_left_x=165)
Fig. 5. Average delay and intersection flows for increasing numbers of vehicles.

whereas Eq. (30) does not.
All reported results are the average of 100 Monte Carlo simulations, wherein the randomness is in the vehicle earliest arrival times $\left(e_{i}\right)$ and vehicle turning movements ( $\gamma_{i}^{-}$and $\gamma_{i}^{+}$). Each simulation was independently generated, and had a fixed number of vehicles. Scenarios were generated as follows: for each vehicle $i$, the incoming lane $\gamma_{i}^{-}$was randomly selected from $\Gamma^{-}$with equal probabilities for each incoming lane. The earliest arrival time spacing between $i$ and the last vehicle on $\gamma_{i}^{-}$was generated using a Poisson process. The outgoing lane had a 80\% chance of being a through movement, and a 20\% chance of being a left or a right turn, depending on the turning movement possible for the incoming lane. This resulted in $80 \%$ through movements, $10 \%$ right turns, and $10 \%$ left turns. Every MILP was solved to optimality (no time limit) with CPLEX's default settings.

### 6.1. Comparison of single-horizon and rolling-horizon

First, we compared the solutions from the single-horizon and the two rolling-horizon policies (ASAP and ALAP). Due to the computation times for the single-horizon solution method (Section 4.9), we limited the maximum number of vehicles to 40 . We also considered three density scenarios: traffic demands of 200, 500, or 800 vph per lane. These demand rates provided the mean for the Poisson distribution used to determine vehicle spacing per lane. We used the objective function (14) with $f_{i}=1$.

Fig. 5 shows the average delay per vehicle $\left(\frac{\mathscr{D}}{|\mathscr{V}|}\right)$ and the average intersection flow $(\mathscr{Q})$ for each solution method and for various numbers and densities of vehicles. For ASAP and ALAP policies, we used a time step of $p=10 \mathrm{~s}$ and a time horizon of $\Delta T=15 \mathrm{~s}$. For the highest number of vehicles included, 40 vehicles, at the density of 800 vph, vehicle earliest arrival times would have been distributed, on average, over 22.5 s. Therefore, solving several MILPs would have been necessary to assign reservations to all vehicles. The average delays increased with the number of vehicles, showing the intersection congestion. Furthermore, the rate of increase was higher for higher densities, which demonstrates that demand exceeded supply for these scenarios. Average delays were lower than might be experienced with traffic signals because vehicles do not need to wait for a signal phase change.

A comparison across various solution methods (single horizon, ASAP, and ALAP) in Fig. 5 shows very little differences between the average delays and intersection flows, even as the number of vehicles and the density of vehicles varies. These are encouraging results because they suggest that a rolling horizon method with horizons as low as 10-15 s could produce similar results to considering all vehicles in Model CPIC. Of course, the rolling horizon had much lower computation times due to considering fewer

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-14.jpg?height=1435&width=1350&top_left_y=179&top_left_x=270)
Fig. 6. Effects of changing the ratio $\frac{p}{\Delta T}$ on ASAP and ALAP. The time horizon was fixed at 8s. Error bars show the standard deviation.

number of vehicles. Therefore, for the remainder of the results we will focus solely on rolling horizon approaches.
Fig. 5 also shows intersection flows resulting from reservations. Flow peaks at around 1500 vph, but declines to around 1000 vph at the maximum demand scenario considered (40 vehicles with a density of 800 vph). These flow metrics could be compared with traffic signal flows. However, it is important to note that the objective function used was to minimize the TSTT. Maximizing flow might result in more platooning, and platooning would benefit from considering larger numbers of vehicles. In addition, the flow depends on the following headways, which might be reduced for CAVs.

### 6.2. Comparison of time horizons

Next, we explored how ASAP and ALAP were affected by different time horizons. We tested 15 min of demand, with average density of 500 vph per lane, for a total of 1000 vehicles. The purpose of these experiments are to study the tradeoff between computation time and optimality. Small periodicities and time horizons reduce the number of vehicles under consideration, thereby reducing the number of variables in each MILP and the computation required to solve it. However, larger periodicities include more vehicles in each MILP, and are therefore likely to be closer to the optimal single-horizon solution. Due to the exponential increases in computation time from additional vehicles, the greatest time horizon that admits computationally tractable MILPs is likely the best choice.

Fig. 6 shows a set of experiments in which the periodicity, $p$, varied from 2 to 8 s, whereas the time horizon, $\Delta T$, remained fixed at 8 s. This resulted in changing the ratio $\frac{p}{\Delta t}$. The error bars show the standard deviation for the ASAP policy. As $p$ approached $\Delta T$, the differences decreased, and in fact the ALAP and ASAP policies are equivalent when $p=\Delta T$. (The differences in the results at 8 s are

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-15.jpg?height=653&width=1344&top_left_y=181&top_left_x=272)
Fig. 7. Effects of greater periodicity on ASAP and ALAP. The time horizon was set to 150\% of the period. Error bars show the standard deviation.

due to stochasticity in the scenarios.) The total system travel time from ALAP increased with the period because the number of fixed vehicles increased, reducing the feasible region of the MILP. ALAP consistently had a lower average total system travel time (except where $p=\Delta T$ ). However, it is not clear these differences were significant. Even at $p=2 \mathrm{~s}$, the difference barely exceeded one standard deviation. Still, it is possible that many more Monte Carlo simulations would show a statistically significant difference between ALAP and ASAP.

We also studied a set of experiments in which the ratio $\frac{p}{\Delta T}$ was held constant. Fig. 7 shows average travel times per vehicle as periodicity varies from 5 to 10 s. The time horizon, $\Delta T$, was set at $\Delta T=1.5 p$. This resulted in an average of 17-33 vehicles arriving within each horizon, although the number of vehicles under consideration in the MILP could differ depending on the solution to previous periods. As expected, both ASAP and ALAP exhibited a downward trend, although variance was high. The downward trend resulted from considering a larger time horizon, and thus more vehicles, in each MILP. ALAP did not show significant improvements over ASAP; the differences between ASAP and ALAP were within one standard deviation for all periodicities. However, ALAP again appeared to have lower average travel times at all periodicities. Overall, the benefits of ALAP (if statistically significant) appear fairly small (less than 0.2s per vehicle), although greater benefits might be observed in more congested or non-symmetric scenarios. These results are encouraging for efficient use of Model CPIC in practice as ASAP is both more reliable and requires less computation time.

Fig. 6 also shows the average computation times for each policy. Computation times were higher for ALAP, especially at low ratios of $\frac{p}{\Delta t}$. The reason ALAP required more time is because the MILP was solved using a non-polynomial algorithm, and therefore computation times increased exponentially with the number of vehicles. ALAP, by definition, considers more vehicles in each period because fewer vehicles are fixed. Recall that since ALAP delays vehicle reservations as much as possible, the number of decision variables within the corresponding MILP problems is likely to increase compared to the ASAP policy and computation time is expected to increase with the number of vehicles. Computation times for both ASAP and ALAP for the experiment in Fig. 6 were sufficiently low to be solved in real-time, as vehicles were distributed over 15 min on average. Besides improving computation times, ASAP has the further benefit of locking in reservations sooner, which may improve the reliability of AIM*. Given the comparison of ALAP and ASAP, we use ASAP for our objective function comparisons in Section 6.3.

### 6.3. Comparison of CPIC and FCFS

Finally, we studied how this protocol compares to the FCFS policy used by previous work (Fajardo et al., 2011; Li et al., 2013). To model FCFS within the AIM* protocol and MILP, we added the constraints discussed in Section 4.8. We compared scenarios with 5 min of demand at different densities with and without the FCFS constraints. Fig. 8 shows how the average (from 100 Monte Carlo simulations) delay and flow vary with density. Note that the delay shown is the total delay, not the delay per vehicle. At the highest density of 450 vph, the average delay per vehicle is less than 4s. Still, these differences illustrate the potential delay penalties imposed by using AIM with FCFS. Furthermore, these FCFS constraints are likely an optimistic estimation of the solution resulting from AIM with the FCFS protocol, because the MILP was used to minimize objective (14) while satisfying the FCFS constraints. Because AIM relies on vehicles to request reservations and propose a solution, it is unlikely to achieve a solution as good as the one found by AIM* with FCFS constraints. Since AIM with FCFS was shown to improve over optimized traffic signals on single, symmetric intersections (Fajardo et al., 2011), these results show that AIM* is likely to improve over optimized traffic signals on this intersection as well. We conducted two-sample unpaired T-tests on each difference, and found that all differences were statistically significant. All $p$-values were less than $1 \times 10^{-24}$.

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-16.jpg?height=639&width=1336&top_left_y=183&top_left_x=276)
Fig. 8. Effects of FCFS on delay for 5 min of demand. Error bars show the standard deviation.

## 7. Conclusions

This paper developed a method for optimizing reservation-based intersection controls to address known issues with existing policies (Levin et al., 2016). Due to the limited ability of the AIM communications protocol to admit arbitrary vehicle trajectories, we developed a new protocol, AIM*, in which the intersection manager specifies reservations for each vehicle. To determine these reservations, we adopted a conflict point approach to vehicle separation. Vehicles must be sufficiently spaced at each conflict point, which is the intersection between vehicle spatial trajectories. These spacings include the following headways used in a typical speeddensity relationship in case of unforeseen circumstances. The conflict point model was used to formulate a MILP, which can be solved using off-the-shelf optimization software. In order to solve the problem in real-time over large periods of time, we developed a rolling horizon framework and empirically observed that the proposed formulation can be solved with up to 40 vehicles in a few seconds. We compared the as-soon-as-possible and as-late-as-possible variants of rolling horizon reservation policies through the rolling horizon, and found only small differences between these policies and a single time horizon. A comparison of the solutions obtained with Model CPIC to those from a FCFS policy showed that the AIM* protocol can significantly reduce delays over AIM, even on a symmetric intersection.

The communications protocol and reservation assignment methods developed in this paper might replace suboptimal protocols and policies for microsimulation and future implementation of reservations. Still, there are several open questions. More efficient solution algorithms or heuristics exploiting the unique structure of this problem could reduce the computational burden for large numbers of vehicles or longer time horizons. Trajectories with non-uniform speeds could also improve intersection throughput, and this method might be implemented in a microsimulator to study its effects on queuing and compare with traffic signals. Asymmetric intersections (with different numbers of incoming lanes per approach, capacities, and/or free flow speeds) might yield more interesting comparisons with the AIM protocol and traffic signals. Finally, decentralized reservation policies are known to create potential issues due to lack of coordination or user equilibrium route choice (Levin et al., 2016), so future work should optimize networks of intersections as well.

## Acknowledgements

The authors appreciate the support of the Data-Supported Transportation Operations \& Planning Center and the National Science Foundation, Grant No. 1254921. The authors are also grateful for the comments and suggestions from Dr. Stephen D. Boyles and Dr. Vinayak V. Dixit.

## Appendix A. Conflict points of a four-approach intersection

To illustrate the derivation of conflict points for collision avoidance, we calculate the conflict points for a symmetric fourapproach, two lane intersection. Conflict points for any intersection configuration may be calculated geometrically. Consider the four-approach intersection depicted in Fig. 9. Since the intersection is symmetric, we focus on the West approach. The set of Westincoming links contains two elements, i.e. $\Gamma^{-}=\left\{W_{L}, W_{R}\right\}$ (left and right lanes) and leads to a total of four vehicle paths $W S_{R}, W E_{R}, W E_{L}$ and $W N_{L}$. We assume that turning movements (paths $W S_{R}$ and $W N_{L}$ ) are circular. Let $\mu_{R}$ be the radius of the right turn trajectory, $\mu_{L}$ be the radius of the left trajectory and $\lambda$ be the inter-lane distance. The width of the intersection is denoted $\omega$.

To determine the travel time between conflict points, we consider each vehicle path independently. Fig. 10 provides a detailed illustration of the conflict points for each vehicle path for the West approach.

For $W S_{R}$, which represents a right turn, there are only two conflict points: the intersection enter and exit points denoted $\gamma_{W_{R}}^{-}$and $\gamma_{S_{R}}^{+}$

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-17.jpg?height=1195&width=1199&top_left_y=185&top_left_x=345)
Fig. 9. 4-approach, 2-lane intersection. Four vehicle paths are available $W S_{R}, W E_{R}, W E_{L}, W N_{L}$ for the West approach. All conflicts points on each trajectory are represented with a rhombus.

respectively. The distance between these conflicts points correspond a quarter-circle

$$
d\left(\gamma_{W_{R}}^{-}, \gamma_{S_{R}}^{+}\right)=\frac{2 \pi \mu_{R}}{4}=\mu_{R} \frac{\pi}{2}
$$

For all other trajectories, there is a total of six conflict points inside the intersection plus the exit point, hence a total of seven distances are required. The second trajectory, $W E_{R}$ corresponds to a straight movement on the right-hand side lane. The distance from the entry point to all other conflict points on this trajectory are determined using basic geometry.

$$
\begin{aligned}
& d\left(\gamma_{W_{R}}^{-}, c_{W E_{R}}^{1}\right)=\mu_{R} \\
& d\left(\gamma_{W_{R}}^{-}, c_{W E_{R}}^{2}\right)=\mu_{R}+\lambda \\
& d\left(\gamma_{W_{R}}^{-}, c_{W E_{R}}^{3}\right)=\omega-\sqrt{\mu_{L}^{2}-\mu_{R}^{2}} \\
& d\left(\gamma_{W_{R}}^{-}, c_{W E_{R}}^{4}\right)=\sqrt{\mu_{L}^{2}-\mu_{R}^{2}} \\
& d\left(\gamma_{W_{R}}^{-}, c_{W E_{R}}^{5}\right)=\mu_{L} \\
& d\left(\gamma_{W_{R}}^{-}, c_{W E_{R}}^{6}\right)=\mu_{L}+\lambda \\
& d\left(\gamma_{W_{R}}^{-}, \gamma_{E_{R}}^{+}\right)=\omega
\end{aligned}
$$

Similar computations yield the distance for trajectory $W E_{L}$ which corresponds to a straight movement on the left-hand side lane (note that only the distance to the 3rd and 4th conflicts points differ from $W E_{R}$ ).

$$
d\left(\gamma_{W_{L}}^{-}, c_{W E_{L}}^{1}\right)=\mu_{R}
$$

![](https://cdn.mathpix.com/cropped/411aa35f-5e32-4e85-96b3-e142cdd13008-18.jpg?height=1684&width=1562&top_left_y=179&top_left_x=163)
Fig. 10. Conflict points on each vehicle path for the West approach: $W S_{R}, W E_{R}, W E_{L}, W N_{L}$ ). All conflicts points on each trajectory are represented with a rhombus.

$$
\begin{aligned}
& d\left(\gamma_{W_{L}}^{-}, c_{W E_{L}}^{2}\right)=\mu_{R}+\lambda \\
& d\left(\gamma_{W_{L}}^{-}, c_{W E_{L}}^{3}\right)=\sqrt{\mu_{L}^{2}-\left(\mu_{R}+\lambda\right)^{2}} \\
& d\left(\gamma_{W_{L}}^{-}, c_{W E_{L}}^{4}\right)=\omega-\sqrt{\mu_{L}^{2}-\left(\mu_{R}+\lambda\right)^{2}} \\
& d\left(\gamma_{W_{L}}^{-}, c_{W E_{L}}^{5}\right)=\mu_{L} \\
& d\left(\gamma_{W_{L}}^{-}, c_{W E_{L}}^{6}\right)=\mu_{L}+\lambda \\
& d\left(\gamma_{W_{L}}^{-}, \gamma_{E_{L}}^{+}\right)=\omega
\end{aligned}
$$

Finally, $W N_{L}$ corresponds to a left turn and the distance to the conflict points therein represent vehicle movement on an arc.

$$
\begin{aligned}
& d\left(\gamma_{W_{L}}^{-}, c_{W N_{L}}^{1}\right)=\mu_{L} \arcsin \left(\frac{\mu_{R}}{\mu_{L}}\right) \\
& d\left(\gamma_{W_{L}}^{-}, c_{W N_{L}}^{2}\right)=\mu_{L} \arccos \left(\frac{\omega}{2 \mu_{L}}\right) \\
& d\left(\gamma_{W_{L}}^{-}, c_{W N_{L}}^{3}\right)=\mu_{L} \arcsin \left(\frac{\mu_{R}+\lambda}{\mu_{L}}\right) \\
& d\left(\gamma_{W_{L}}^{-}, c_{W N_{L}}^{4}\right)=\mu_{L} \arccos \left(\frac{\mu_{R}+\lambda}{\mu_{L}}\right) \\
& d\left(\gamma_{W_{L}}^{-}, c_{W N_{L}}^{5}\right)=\mu_{L} \arcsin \left(\frac{\omega}{2 \mu_{L}}\right) \\
& d\left(\gamma_{W_{L}}^{-}, c_{W N_{L}}^{6}\right)=\mu_{L} \arccos \left(\frac{\mu_{R}}{\mu_{L}}\right) \\
& d\left(\gamma_{W_{L}}^{-}, \gamma_{N_{L}}^{+}\right)=\mu_{L} \frac{\pi}{2}
\end{aligned}
$$

## References

Altché, F., De La Fortelle, A., 2016. Analysis of optimal solutions to robot coordination problems to improve autonomous intersection management policies. In: 2016 IEEE Intelligent Vehicles Symposium (IV). IEEE, pp. 86-91.
Carlino, D., Boyles, S.D., Stone, P., 2013. Auction-based autonomous intersection management. In: 2013 16th International IEEE Conference on Intelligent Transportation Systems-(ITSC). IEEE, pp. 529-534.
Carlino, D., Depinet, M., Khandelwal, P., Stone, P., 2012. Approximately orchestrated routing and transportation analyzer: Large-scale traffic simulation for autonomous vehicles. In: 2012 15th International IEEE Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 334-339.
Chen, L., Englund, C., 2016. Cooperative intersection management: a survey. IEEE Trans. Intell. Transport. Syst. 17 (2), 570-586.
Chiang, Y.-J., Klosowski, J.T., Lee, C., Mitchell, J.S., 1997. Geometric algorithms for conflict detection/resolution in air traffic management. In: Proceedings of the 36th IEEE Conference on Decision and Control, 1997, vol. 2. IEEE, pp. 1835-1840.
Conde Bento, L., Parafita, R., Santos, S., Nunes, U., 2013. Intelligent traffic management at intersections: Legacy mode for vehicles not equipped with v2v and v2i communications. In: 2013 16th International IEEE Conference on Intelligent Transportation Systems-(ITSC). IEEE, pp. 726-731.
Daganzo, C.F., 1998. Queue spillovers in transportation networks with a route choice. Transport. Sci. 32 (1), 3-11.
de La Fortelle, A., 2010. Analysis of reservation algorithms for cooperative planning at intersections. In: 2010 13th International IEEE Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 445-449.
De La Fortelle, A., Qian, X., 2015. Autonomous driving at intersections: combining theoretical analysis with practical considerations. In: ITS World Congress 2015. Dresner, K., Stone, P., 2004. Multiagent traffic management: a reservation-based intersection control mechanism. In: Proceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems, vol. 2. IEEE Computer Society, pp. 530-537.
Dresner, K., Stone, P., 2005. Multiagent traffic management: An improved intersection control mechanism. In: Proceedings of the Fourth International Joint Conference on Autonomous Agents and Multiagent Systems. ACM, pp. 471-477.
Dresner, K., Stone, P., 2006. Human-usable and emergency vehicle-aware control policies for autonomous intersection management. In: Fourth International Workshop on Agents in Traffic and Transportation (ATT), Hakodate, Japan.
Dresner, K., Stone, P., 2006. Traffic intersections of the future. In: Proceedings of the National Conference on Artificial Intelligence (2006), vol. 21, Menlo Park, CA; Cambridge, MA; London; AAAI Press; MIT Press; 2006, p. 1593.
Dresner, K., Stone, P., 2008. Mitigating catastrophic failure at intersections of autonomous vehicles. In: Proceedings of the 7th international joint conference on Autonomous agents and multiagent systems-Vol. 3, International Foundation for Autonomous Agents and Multiagent Systems, pp. 1393-1396.
Dresner, K.M., Stone, P., 2007. Sharing the road: autonomous vehicles meet human drivers. In: IJCAI, vol. 7, pp. 1263-1268.
Fajardo, D., Au, T.-C., Waller, S., Stone, P., Yang, D., 2011. Automated intersection control: performance of future innovation versus current traffic signal control. Transport. Res. Rec.: J. Transport. Res. Board 2259, 223-232.
Gregoire, J., Bonnabel, S., de La Fortelle, A., 2013. Optimal cooperative motion planning for vehicles at intersections. Also available at: arXiv preprint arXiv:1310. 7729.
Gregoire, J., Frazzoli, E., de La Fortelle, A., Wongpiromsarn, T., 2014. Back-pressure traffic signal control with unknown routing rates. IFAC Proc. Volumes 47 (3), 11332-11337.
Hausknecht, M., Au, T.-C., Stone, P., 2011. Autonomous intersection management: multi-intersection optimization. In: 2011 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS). IEEE, pp. 4581-4586.
Le, T., Kovács, P., Walton, N., Vu, H.L., Andrew, L.L., Hoogendoorn, S.S., 2015. Decentralized signal control for urban road networks. Transport. Res. Part C: Emerg. Technol. 58, 431-450.
Levin, M.W., Boyles, S.D., 2015. Intersection auctions and reservation-based control in dynamic traffic assignment. Transport. Res. Rec.: J. Transport. Res. Board 2497, 35-44.
Levin, M.W., Boyles, S.D., 2016. A multiclass cell transmission model for shared human and autonomous vehicle roads. Transport. Res. Part C: Emerg. Technol. 62, 103-116.
Levin, M.W., Boyles, S.D., 2017. Pressure-based policies for reservation-based intersection control. In: Transportation Research Board 96th Annual Meeting.
Levin, M.W., Boyles, S.D., Patel, R., 2016. Paradoxes of reservation-based intersection controls in traffic networks. Transport. Res. Part A: Policy Pract. 90, 14-25.
Levin, M.W., Fritz, H., Boyles, S.D., 2017. On optimizing reservation-based intersection controls. IEEE Trans. Intell. Transport. Syst. 18 (3), 505-515.
Li, Z., Chitturi, M., Zheng, D., Bill, A., Noyce, D., 2013. Modeling reservation-based autonomous intersection control in Vissim. Transport. Res. Rec.: J. Transport. Res. Board 2381, 81-90.

Newell, G.F., 1993. A simplified theory of kinematic waves in highway traffic, part i: General theory. Transport. Res. Part B: Methodol. 27 (4), 281-287.
Qian, X., Gregoire, J., Moutarde, F., De La Fortelle, A., 2014. Priority-based coordination of autonomous and legacy vehicles at intersection. In: 2014 IEEE 17th International Conference on Intelligent Transportation Systems (ITSC). IEEE, pp. 1166-1171.
Reif, J., Sharir, M., 1994. Motion planning in the presence of moving obstacles. J. ACM (JACM) 41 (4), 764-790.
Rey, D., Rapine, C., Dixit, V.V., Waller, S.T., 2015a. Equity-oriented aircraft collision avoidance model. IEEE Trans. Intell. Transport. Syst. 16 (1), 172-183.
Rey, D., Rapine, C., Fondacci, R., El Faouzi, N.-E., 2012. Minimization of potential air conflicts through speed regulation. Transport. Res. Rec.: J. Transport. Res. Board 2300, 59-67.
Rey, D., Rapine, C., Fondacci, R., El Faouzi, N.-E., 2015b. Subliminal speed control in air traffic management: optimization and simulation. Transport. Sci. 50 (1), 240-262.
Schepperle, H., Böhm, K., 2007. Agent-based traffic control using auctions. In: Cooperative Information Agents XI. Springer, pp. 119-133.
Schepperle, H., Bohm, K., 2008. Auction-based traffic management: towards effective concurrent utilization of road intersections. In: 2008 10th IEEE Conference on E-Commerce Technology and the Fifth IEEE Conference on Enterprise Computing, E-Commerce and E-Services. IEEE, pp. 105-112.
Schepperle, H., Böhm, K., Forster, S., 2008. Traffic management based on negotiations between vehicles-a feasibility demonstration using agents. In: Agent-Mediated Electronic Commerce and Trading Agent Design and Analysis. Springer, pp. 90-104.
Smith, M., 1979. Traffic control and route-choice; a simple example. Transport. Res. Part B: Methodol. 13 (4), 289-294.
Tassiulas, L., Ephremides, A., 1992. Stability properties of constrained queueing systems and scheduling policies for maximum throughput in multihop radio networks. IEEE Trans. Autom. Control 37 (12), 1936-1948.
Varaiya, P., 2013. Max pressure control of a network of signalized intersections. Transport. Res. Part C: Emerg. Technol. 36, 177-195.
Vasirani, M., Ossowski, S., 2012. A market-inspired approach for intersection management in urban road traffic networks. J. Artif. Intell. Res. 621-659.
Wongpiromsarn, T., Uthaicharoenpong, T., Frazzoli, E., Wang, Y., Wang, D., 2014. Throughput optimal distributed traffic signal control. Also available at: arXiv preprint arXiv:1407.1164.
Xiao, N., Frazzoli, E., Li, Y., Wang, Y., Wang, D., 2014. Pressure releasing policy in traffic signal control with finite queue capacities. In: 2014 IEEE 53rd Annual Conference on Decision and Control (CDC). IEEE, pp. 6492-6497.
Yperman, I., Logghe, S., Immers, B., 2005. The link transmission model: an efficient implementation of the kinematic wave theory in traffic networks. In: Proceedings of the 10th EWGT Meeting, Poznan, Poland.
Zaidi, Ali A., Kulcsár, Balázs, Wymeersch, Henk, 2016. Back-pressure traffic signal control with fixed and adaptive routing for urban vehicular networks. IEEE Trans. Transport. Syst. 17 (8), 2134-2143.
Zhang, K., De La Fortelle, A., Zhang, D., Wu, X., 2013. Analysis and modeled design of one state-driven autonomous passing-through algorithm for driverless vehicles at intersections. In: 2013 IEEE 16th International Conference on Computational Science and Engineering (CSE). IEEE, pp. 751-757.
Zhang, R., Li, Z., Feng, C., Jiang, S., 2012. Traffic routing guidance algorithm based on backpressure with a trade-off between user satisfaction and traffic load. In: 2012 IEEE Vehicular Technology Conference (VTC Fall). IEEE, pp. 1-5.
Zhu, F., Ukkusuri, S.V., 2015. A linear programming formulation for autonomous intersection control within a dynamic traffic assignment and connected vehicle environment. Transport. Res. Part C: Emerg. Technol. 55, 363-378.


[^0]:    * Corresponding author.
    E-mail addresses: mlevin@umn.edu (M.W. Levin), d.rey@unsw.edu.au (D. Rey).

