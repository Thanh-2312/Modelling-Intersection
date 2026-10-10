# Combined Alternate-Direction Lane Assignment and Reservationbased Intersection Control 

Aleksandar Stevanovic and Nikola Mitrovic

[1] The current method of organizing traffic flows in urban networks, uses directional Right-of-Way links to move traffic between urban intersections. Conflict resolution between vehicles is almost exclusively exercised at the intersections, which turns them into bottlenecks of our urban traffic systems. The recent conflict resolution concepts, that use a reservation-based scheduling approach, improve the efficiency but do not attack the core of the problem. This paper proposes a fundamentally different approach where directional driving paths are altered between neighboring lanes to align vehicles for conflict-less left and right turns at the intersections. Conflicts of the through vehicles are still handled by a reservation-based algorithm. The experiments are executed in FAUSIM - a new simulation tool specially developed to allow flexibility of driving behavior that cannot be found in other tools. The proposed scenario, (called CADLARIC -Combined Alternate-Direction Lane Assignment and Reservation-based Intersection Control) was compared to a conventional Fixed-Time (FT) signals and a novel Fully Reservation-Based Intersection Control (FR-BIC). The results of the experiments, executed on a small three-intersection corridor, show that CADLARIC significantly outperforms the other scenarios in terms of traffic efficiency (delays and stops) and generates a net reduction of conflicting situations when compared to the FR-BIC.

Keywords-traffic control, simulation, scheduling, conflict resolution, alternate directional driving

## I. Introduction

The current method of organizing traffic flows in urban networks, uses a directional Right of Way (ROW) to move traffic between urban intersections. Then, at such intersections, a conflict-resolution method is applied to safely and efficiently process traffic streams from the conflicting ROWs. A conflict-resolution method can be a set of traffic signs, signals, or road geometries combined with control rules (e.g. roundabouts, diverge-diamond, and other alternative geometry intersections); all of which prioritize movements of certain traffic units (vehicles, pedestrians, etc.). Even emerging concepts, such as intersection reservation systems [1], or where alternative geometry is combined with dynamic signal phasing and timing [2], do not step away from this traditional ROW concept.

[^0]However, driving rules do not have to be as restricted as they now are now. So far, our thinking has been focused on: 1. Road stretches, where traffic flows are handled as directional (compressible) fluids, and 2. Road intersections, as the major 'containers' of the conflicts between traffic streams. Our ability to leave behind this traditional ROW model has been limited due to: 1. Inability to fully control human behavior, and 2. Lack of technological resources to enable full communication and interaction among vehicles, and between vehicles and infrastructure. Recent technological advances with Connected and Automated Vehicles (CVs, AVs) have opened new opportunities to organize traffic within the existing road infrastructure. Our research efforts have resulted in the development of a system where every vehicle in the traffic stream can utilize, when not endangering the other road users, any part of the paved road surface regardless of the direction of its movement or its current speed or position [3]. This paradigm shift in the utilization of road infrastructure is motivated by the need to address the everlasting increase in travel demand, support sustainability, and preserve existing transport land use.

This novel framework proposes the organization of traffic flows without traditional directional restrictions. Entire available road surface can be utilized for conflict resolution and improvement of the traffic flows. For the sake of simplicity and field execution, lane discipline is preserved although some of the future scenarios can remove this type of driving discipline too. The proposed framework can be utilized for a number of various traffic control and management scenarios, which can allow, at the highest level, full spatial distribution of the conflicting points (between various traffic entities) in the road network.

The main objective of this paper is to present and evaluate one of the possible strategies that can be implemented by using this novel concept.. This strategy, called CADLARIC (Combined Alternate-Direction Lane Assignment and Reservation-based Intersection Control) assumes alternative directional use of lanes where each next lane is used by traffic going in the opposite direction. Under this strategy [3], the right- and left-turning vehicles use dedicated right and left lanes, respectively, between two intersections to completely avoid conflicts at the intersection. The paper compares this innovative concept with the Full Reservation-based Intersection Control (FR-BIC) system, similar to the one developed by others [1], and a base-case scenario with optimized Fixed-time (FT) signals.

## II. Literature Review

The existing research on the novel concepts of urban traffic control related to Reservation-Based Intersection Control (R-BIC) in CV and AV environment has started almost two decades ago. Some of the early studies on this subject include Kato et al. [5] research on automated vehicles to form flexible platoons through the means of using the dedicated short-range communication (DSRC). The first notable study on the R-BIC was done by Dresner and Stone [1, 6]. This seminal work has been followed up by a number of studies which address similar concepts of R-BIC, often also called automated intersection control or intersection management, etc. [7-12]. Each of this study is original on its own way (mostly by introducing a different technique to solve the scheduling problem) but most of them are similar in an attempt to integrate trajectory design into the signal control [7-9]. The other type of studies are those which address space-sharing coordination between moving units to enable their safe and efficient movement [10]. Some of the most recent studies combine this R-BIC with other concepts such as dynamic traffic assignments and discuss some of the paradoxes that are observed when the R-BIC is faced with network dynamics [11]. Although most of these studies bring very significant contributions to this emerging field of urban traffic operations, none of them yet addresses potential strategies that fully utilize road infrastructure; without strong directional constraints. A study or Levin and Boyles [12] probably comes closest to this idea but this study considers dynamic lane reversal where number of lanes for each direction can be changed dynamically, based on traffic conditions, but never fully separated in lane-directional traffic. The concept proposed in this paper goes a step further by splitting directional traffic into individual lanes, based on the movements at the downstream intersection, and combining this strategy with the R-BIC.

## III. Methodology

## A. FAUSIM Simulation Environment

In order to model flexible utilization of road infrastructure, it was necessary to develop a modeling environment which can provide for such flexibility, considering that most of the commercial tools (e.g. Vissim, Aimsun) and open-source platforms (e.g. SUMO) do not offer such flexibility. Thus, the researchers developed a new simulation environment which is called Flexible Arterial Utilization Simulation Modeling (FAUSIM). The FAUSIM was developed within NetLogo [4] modeling platform through a series of custom-made codes written in Scala, javacompatible, language [4]. While detailed descriptions of the algorithms within FAUSIM is too long for this manuscript, Fig. 1 below shows an overall scheme the platform with corresponding modules.

The Network Layer, shown in Fig. 1, is used to create elements of network geography where the movements of the vehicles are not restricted by links. The Travel Behavior Layer is used to define travel parameters for each car - e.g. where the vehicle enters, where it goes and similar. The Fleet Layer defines types of the vehicles in traffic stream, their individual kinematic characteristics and similar. This layer also contains a priority level for a vehicle, which is a very important parameter for any reservation-based control policy. The Driving Behavior Layer defines the driving actions of the cars when taken individually - e.g. how cars follow or overtake each other, change lanes and similar, when there is no centralized logic to provide rules.

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-2.jpg?height=690&width=844&top_left_y=468&top_left_x=1091)
Fig. 1. Basic architecture and layers of FAUSIM

The Control Policy (CP) Layer is used to impose any control policy on the utilization of time-space domain of the system. This module is used to implement any intersection control (signals, stop signs, etc.) but also to reserve timespace for conflictless movements of the vehicles. It is important to note here that the CP is not restricted only to intersection's geometry but can be used to reserve a timespace block anywhere within the entire domain (e.g. simulation time-network). It is this layer, and its unconstrained feature to reserve time-space blocks, that allows modeling of futuristic Automated Vehicle (AV) activities. Parameters and outputs of these various layers are merged within the Simulation Engine Layer which takes care of the simulation execution, every time step. The current time resolution of FAUSIM is 5Hz but this parameter is adjustable. Finally, simulation outputs are processed in the Evaluation Layer, which contains a number of subroutines necessary to compute traffic performance metrics (delays, stops, conflicts).

## B. Validation of the FAUSIM

Development of any new microsimulation model requires its proper validation before the model can be used to test various traffic scenarios. While FAUSIM can be utilized to create unconventional models, validation was restricted to a common-case scenario that can be replicated in other commercial tools. This common-case scenario, with FixedTime (FT) signals (of predefined signal timing lengths), was also later used as a base-case scenario in comparison with the other unconventional scenarios. Fig. 2 shows scatterplots and correlation between the delays generated, for FT scenario, in FAUSIM and Vissim (one of the leading commercial microsimulation platforms). Traffic demand (vehicular inputs) in both tools were identical, as well as the signal
timing logic (FT) and turning proportions. The results, which truly represent the similarity of the vehicle 'interaction' models (e.g. car-following, lane-changing, queuedischarging) in FAUSIM and Vissim, show very high similarity between the two simulations. The results are slightly better on the route (or OD) level than the node but this can be a consequence of many factors (see Fig. 2).

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-3.jpg?height=636&width=808&top_left_y=486&top_left_x=187)
Fig. 2. Correlation between FAUSIM and Vissim results for FT scenario

## C. Traffic Management/Control Scenarios

Three scenarios were developed to show the impact of flexible utilization of road infrastructure. The first scenario, CADLARIC, assumed unconventional road usage combined with a reservation-based control at the road intersections. The second scenario was modeled based on the conventional traffic movements between intersections and reservationbased control at the road intersections, similar to the research presented elsewhere [1,6]. The third was a base-case scenario with conventional traffic behavior between intersections and a fixed-time control at the intersections. The three scenarios were tested on a 3-intersection network shown in Fig. 3 below. Turning movement flows (in veh/hour) are given for each movement once extracted from the Origin-Destination (OD) flows. Origin and destination points are denoted with numbers in the circles next to each network entrance/exit. Lane assignments at the intersection, for conventional scenarios, are given with corresponding arrows. Each movement is also associated with a Level of Service (LOS) which represents a prevalent congestion level under the basecase scenario. The LOSs between D and F, as experienced by traffic on all of the movements, signify heavy traffic demand in the network.

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-3.jpg?height=243&width=846&top_left_y=2080&top_left_x=183)
Fig. 3. Schematic representation of the test network

## 1) CADLARIC Scenario

The CADLARIC scenario represents the core of this research. Its operational strategy lays at the extension of the R-BIC, presented in a number of other research papers [7-9]. Instead of using the reservation-based system to process all of the conflicts at the intersection, the authors propose that various turning flows are assigned to different lanes, in an alternate fashion as depicted in Fig. 4, to avoid a number of conflict points (and thus complexity of the R-BIC) at the intersection itself.

Essentially, FAUSIM is used to assign individual lanes (not groups of lanes) to specific movements and reserve those lanes for the movement traffic even at the intersection. In this way all of the left and right traffic movements go through an intersection without any conflicts and potential conflicts are reduced only to those between through vehicles. Then, an R-BIC system (similar to one presented in [1,6]) is used to handle conflict avoidance at the intersection itself. We call this concept Combined Alternate-Direction Lane Assignment and Reservation-based Intersection Control (CADLARIC) for self-explanatory reasons.

It should be noted here that FAUSIM can be used in many different ways to flexibly utilize road-infrastructure and CADLARIC is only one such utilization. Also, it should be noted that under these experiments CADLARIC was assumed to be surrounded by streets with the conventional traffic system. This means that all of the vehicles under CADLARIC scenario entered the network as if they would enter a regular network (in directional lane groups) and then changed the lanes to reassign themselves in the proper lanes for the next turn at the intersection.

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-3.jpg?height=539&width=840&top_left_y=1330&top_left_x=1100)
Fig .4. Lane-movement assignment in the CADLARIC scenario

While the exact logic of the CADLARIC's procedures is beyond the scope of this paper we present in Fig. 5 pseudocodes of the two most important subroutines, which handle cooperative lane-changing between intersections and reservation of time-space blocks at the intersections.

The reasoning for proposing this concept lays in the unused opportunity to stretch turning-conflict areas, which are in conventional scenarios almost exclusively located at the intersections, beyond intersection boundaries. By doing this a density of conflicts at the intersections can be reduced and thus both complexity of the reservation-based algorithms and workloads of their computers/systems can be reduced too. The proposed concept also increases a number of lanechanging conflicts between intersections, as the vehicles may need to realign themselves in the proper lanes for the next turn at an intersection. However, one should realize that
there is usually more space to efficiently handle such lanechanging conflicts between intersections than those within the intersection boundaries. To be on conservative side, a network with relatively short segments (200m) between intersections is used in the experiments for this paper (see Fig. 3).

```
procedure LANE CHANGING
    for each veh i do
        set \( 贝 \) as current lane of veh \( i \)
        set \( \math) des as desired lane of veh \( i; \) 不, des = f(movement of veh \( i at downstream int.)
```

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-4.jpg?height=26&width=138&top_left_y=574&top_left_x=273)

```
            get di,j as a distance between veh i and the nearest approaching veh j whose
```

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-4.jpg?height=28&width=241&top_left_y=640&top_left_x=387)

```
            set di, req = dsaf + 2 . k . ( ( t i + v j )
                where dsaf is safety distance and k is time required to move to the adjacent lane
            set di+1,i-1 as a gap between leading veh i+1 and following veh i-1
```

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-4.jpg?height=28&width=196&top_left_y=780&top_left_x=316)

```
            get di+1,i,i-1 as a minimum required gap between veh i+1 and i-1 that veh i needs
                to safely merge the flow
```

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-4.jpg?height=32&width=185&top_left_y=881&top_left_x=301)
![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-4.jpg?height=32&width=249&top_left_y=917&top_left_x=324)

```
                    Execute a lane-changing movement of the vehicle i
                else
```

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-4.jpg?height=30&width=589&top_left_y=1018&top_left_x=346)

```
                        reduce vi-1
                    end if
                end if
            else
```

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-4.jpg?height=30&width=559&top_left_y=1182&top_left_x=322)

```
                    do nothing
                else
                    reduce v
                end if
            end if
        end if
    end for
end procedure
```

A) A subroutine for lane-changing
procedure Time-space Reservation
for each veh $i$ do
if $d_{i, \text { nextInt }}<\mathrm{d}$ where d is a custom based threshold then
set $t_{i}^{\text {nextInt }}$ as estimated arrival time of veh $i$ at downstream intersection
set $v_{i}^{\text {nextInt }}$ as estimated speed of veh $i$ at downstream intersection
set the list of reservation block cells $C\left(C=\left\{c_{1}, c_{2}, \ldots c_{n}\right\}\right)$ for veh $i$
set $v_{\text {temp }}=v_{i}^{\text {nextInt }}$
while $v_{i}^{\text {nextInt }}>=v_{\text {min }}$ where $v_{\text {min }}$ is a custom based speed threshold
if $c_{j}\left(\forall c_{j} \in C\right)$ is available at $t_{j}$, where $t_{j}=t_{j-1}+\frac{c_{j-} c_{j-1}}{v_{i}^{\text {nextlnt }}}, t_{0}=t_{i}^{\text {nextInt }}$ then
reserve path for veh $i$
set the desired speed of veh i to $v_{i}^{\text {nextInt }}$
update the list of reservation block cells $C$
end procedure
else
$v_{i}^{\text {nextInt }} \leftarrow v_{i}^{\text {nextInt }}-v_{\text {step }}$
$t_{i}^{\text {nextInt }} \leftarrow d_{i, \text { nextInt }} / v_{i}^{\text {nextInt }}$
end if
end while
if $d_{i, \text { nextInt }} \geq s d_{i}$ where $\mathrm{sd}_{\mathrm{i}}$ is stopping distance of veh $i$ then
do nothing
else
$v_{i}=v_{\text {temp }}$
reduce $v_{i}$
end if
end if
end for
end procedure

B) A subroutine for time-space reservation

Fig. 5. Pseudocodes for lane-changing and time-space reservation

## 2) FR-BIC Scenario

Full Reservation-based Intersection Control (FR-BIC) scenario essentially represents a version of automated intersection control described in research of others [1,6]. This scenario is called "Full" because, as opposed to CADLARIC, it does not reserve time slots only for through vehicular movements but also for left-turn and right-turn movements. One should note, that the FR-BIC, as developed and used under these experiments may be a slightly more realistic version of the similar system from other studies as it takes in consideration some common traffic engineering parameters and knowledge ensuring that the time within intersection is efficiently utilized, turning-speeds are realistic and vehicular (saturation) headways correspond to some reasonable values.

## 3) Fixed-time Control

FT scenario was implemented in a fully protected way - no permissive left-turn phasing was allowed for left-turns and no right-turn-on-red operations for right-turns. These features made the FT scenario a conservative solution - less efficient but safer than what is sometimes observed in the field. It should be noted that phasing times of the FT scenario were taken as the results of VISTRO [13] optimization, which ensured near-optimal signal phases for each of the traffic movements.

## IV. Results

Simulations for each of the scenarios were performed for 5 random seeds for a duration of one full hour and 300 seconds of warm-up time. Performance measures that are investigated included conventional measures such as delays and stops, to represent the efficiency of various concepts; and conflicts between vehicles as surrogate measures of safety. Delays and stops are extracted for each O-D pair Regarding the conflicts - it should be noted that the definition of conflict in this research varies from what is usually used when similar microsimulation studies are done, where conflicts are found as 'near misses' between vehicles based on their trajectory data. In this study, a conflict means a 'conflicting request' for the same block of time-space, which was handled by respective reservation-based algorithms of the CADLARIC and FR-BIC scenarios. From that perspective, it is important to note that a higher number of conflicts does not necessarily mean unsafe operations as a 'conflicting request' can be handled in a very safe way.

## A. Delays

Fig. 6 shows the results of the delay comparisons. One can observe that both CADLARIC and FR-BIC significantly outperform the FT scenario. The CADLARIC is always the best in terms of the delay; often 50\% or more better than the FR-BIC and sometimes with virtually no delay except if a vehicle is slowed down by another vehicle in front of it, on the same path. Clearly, both reservation-based scenarios bring tremendous benefits in terms of efficiency of traffic streams.

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-5.jpg?height=591&width=816&top_left_y=191&top_left_x=193)
Fig. 6. Average delay per vehicle on an OD path

B. Stops

Stops in these experiments are defined, similarly to other research efforts, as events when the traveling speed of a vehicle drops below 5 km/h. If a vehicle stays under that speed for a number of seconds the entire time counts as a single stop. Fig. 7 shows the results of the comparison of an average number of stops in each scenario. The results are similar to those from delay considerations. The CADLARIC scenario is the best in every case.. Maybe the best evidence of CADLARIC's supremacy over FR-BIC is at these OD pairs (e.g., 15,25,51) that involve all three intersections. In these cases the CADLARIC causes 3 times fewer stops than FR-BIC, on average.This can be explained by the fact that through moving vehicles in the CADLARIC have to negotiate their reserved time-space blocks with a fewer number of conflicting vehicles than those under the FR-BIC scenario.

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-5.jpg?height=597&width=816&top_left_y=1555&top_left_x=213)
Fig. 7. Average number of stops on an OD path

C. Crossing Conflicts

By "Crossing Conflicts" the authors represent those conflicting requests that are mode for the time-space blocks within intersection boundaries. Considering that no permissive left-turn movements are allowed and no rightturns-on-red, the FT scenario does not have any crossing conflicts (all of the vehicular movements are fully protected by respective phases and no reservations are needed).

For the CADLARIC and FR-BIC scenarios, the situation is different. Fig 8. depicts how many conflicting requests are made for each cell within the intersection boundaries (a cell is a basic unit of space in FAUSIM's time-space domain, which is approximately $0.5 \mathrm{~m}^{2}$ ). The Fig. 8 shows clearly that the regarding the crossing conflicts within the intersections, the advantage is on the CADLARIC's side. One should note again that a conflict presented in Fig. 8 does not mean a 'near miss' between two vehicles but merely represents a fact that two vehicles made a claim for the same cell in the same time interval. Conflicting requests over multiple time intervals are grouped into a single conflict as long as they involve the same pair of vehicles. A conflict is always associated with a vehicle/ movement which requests a time-space block already reserved by another vehicle.

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-5.jpg?height=1474&width=797&top_left_y=814&top_left_x=1128)
Fig. 8. Crossing intersection conflicts for nonconventional scenarios

## D. Lane-changing Conflicts

Obviously, in order to avoid the conflicts at the intersections, the CADLARIC scenario displaces resolution of such conflicts in the areas between intersections, where vehicles need to change the lanes to align themselves in proper turning lanes. This is very visible in Fig. 9, where changelane conflicts are shown for the three scenarios. It should be noted that these conflicts are defined in a similar way to the crossing conflicts (it is a potential conflict that needs a resolution - not an actual near miss between vehicles). Fig. 9 shows that number of lane-changing conflicts is the highest with CADLARIC scenario, which is expected. It is also interesting to note that vehicles traveling on certain types of paths do not experience any lane-changing conflicts, under some scenarios This outcome is result of the fact that some vehicles turn immediately in their destination lane for the next intersection and there is no need to change lane. There is more lane-changing conflicts for FT scenario than FR-BIC scenario on certain OD paths). This can be attributed to the fact that vehicles in FT scenario roam more around in the search for the best traffic lane, whereas movements of the vehicles in FR-BIC scenarios are constrained by the need to save their reserved time-space blocks at the next intersection.

![](https://cdn.mathpix.com/cropped/536a1e63-5d1a-44e7-8f90-034bf03f637f-6.jpg?height=595&width=816&top_left_y=1113&top_left_x=213)
Fig. 9. Lane-cahnging conflicts for the three scenarios

Table 1 summarizes the cumulative results of the experiments for all three scenarios. The CADLARIC scenario is clearly more efficient (lower delays and stops) than the other two. FR-BIC also significantly outperforms the FT scenario in terms of delay and stops. When the conflicts are considered, the conservative FT scenario generates the fewest conflicts. The CADLARIC scenario generates the highest number of lane-changing conflicts but it reduces more the crossing conflicts at the intersections, and thus it has a lower net conflict contribution than the FR-BIC scenario.

Summary of the Performance Measures
| Scenario | Performance Measure |  |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  | Total Delay (h) | Stops | Conflicts LC | Conflicts Int. |
| CADLARIC | 8.0 | 820 | 832 | 4923 |
| FR-BIC | 17.5 | 2881 | 261 | 7107 |
| FT Scenario | 126.8 | 9137 | 351 | 0 |


For decades if not centuries, the conflicts between crossdirectional streams of traffic have been resolved at roads' intersections. With current advancements in technology and communications, and with future AVs and scheduling algorithms, there is no need to constrain the time-space reservation by intersection boundaries. This paper investigated how much we can gain, in efficiency of traffic streams and conflict resolution, if we consider that vehicles can flexibly utilize space between intersections and thus displace some of the vehicular conflicts to the mid-block areas where there may be more space for their efficient resolution. The results of the experiments, which are executed on FAUSIM - a specially designed simulation tool (whose basic operations have been validated), show that such a concept can bring significant benefits. The efficiency of the traffic streams is significantly improved and so is the conflict resolution process (the total number of conflicts is reduced). The authors believe that, under AV conditions of the future, this or similar concepts can significantly improve traffic efficiency of urban traffic streams. Further research is needed in several directions: further validation of the models, comparisons with the other common types of traffic control (e.g., actuated-coordinated), and dynamic lane reassignment to respond to changing travel demand.

## References

1. K. Dresner and P. Stone, "Multiagent traffic management: a reservationbased intersection control mechanism," $3^{\text {rd }}$ International Joint Conference on Autonomous Agents and Multiagent Systems, 2004, pp. 530-537.
2. W. Sun, J. Zheng, and H. X. Liu, "A capacity maximization scheme for intersection management with automated vehicles," Transp. Res. Procedia, vol. 23, pp. 121-136, 2017.
3. LATOM FAU. (2018, January 4). Flexible Infrastructure: "Comb" Scenario). Retrieved from https://youtu.be/RXSwJKqBQtM
4. Wilensky, U. 1999. NetLogo. http://ccl.northwestern.edu/netlogo/. Center for Connected Learning and Computer-Based Modeling, Northwestern University. Evanston, IL.
5. S. Kato, S. Tsugawa, K. Tokuda, T. Matsui, and H. Fujii, "Vehicle Control Algorithms for Cooperative Driving with Automated Vehicles and Intervehicle Communications," IEEE Trans. Intell. Transp. Syst., vol. 3, no. 3, pp. 155-160, 2002.
6. P. Stone, "A Multiagent Approach to Autonomous Intersection Management," J. Artif. Intell. Res., vol. 31, pp. 591-653, 2008.
7. J. Lee, B. B. Park, J. Lee, and B. Park, "Development and Evaluation of a Cooperative Vehicle Intersection Control Algorithm Under the Connected Vehicles Environment," IEEE Trans. Intell. Transp. Syst., vol. 13, no. January 2016, pp. 81-90,.
8. J. Wu, A. Abbas-Turki, and A. El Moudni, "Cooperative driving: An ant colony system for autonomous intersection management," Appl. Intell., vol. 37, no. 2, pp. 207-222, 2012.
9. P. Lin, J. Liu, P. J. Jin, and B. Ran, "Autonomous vehicle-intersection coordination method in a connected vehicle environment," IEEE Intell. Transp. Syst. Mag., vol. 9, no. 4, pp. 37-47, 2017.
10. M. Shahriari and M. Biglarbegian, "A prioritized collision avoidance methodology for autonomous driving," in IEEE Conference on Intelligent Transportation Systems, ITSC, 2016, pp. 1832-1837.
11. M. W. Levin and S. D. Boyles, "Intersection Auctions and ReservationBased Control in Dynamic Traffic Assignment," Transp. Res. Rec. J. Transp. Res. Board, vol. 2497, pp. 35-44, 2015.
12. M. W. Levin and S. D. Boyles, "A cell transmission model for dynamic lane reversal with autonomous vehicles," Transp. Res. Part C Emerg. Technol., vol. 68, pp. 126-143, Jul. 2016
13. Vistro 4.0 User Manual (2015). PTV Vision Group , Karlsruhe, Germany

[^0]:    Aleksandar Stevanovic and Nikola Mitrovic are with Department of Civil, Environmental and Geomatics Engineering (CEGE), Florida Atlantic University, Boca Raton, FL 33431 USA. (phone: 561-297-3743; e-mail: astevano@fau.edu).

