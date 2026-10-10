# Traffic Responsive Intersection Control Algorithm Using GPS Data 

Craig B. Rafter*, Bani Anvari, and Simon Box


#### Abstract

This paper reports on the performance of signalised intersection control using vehicle GPS information compared to fixed-time and inductive loop based control. Traffic congestion forecasts estimate an increase of about $\mathbf{6 0} \boldsymbol{\%}$ in 2030. At present, poor choice of signal timings by isolated intersection controllers cause traffic delays that have enormous negative impacts on the economy and environment. Signal timings can be improved by using vehicles' GPS information to overcome the control action deficit at isolated intersections. This new signal control algorithm is beneficial for traffic engineers and governmental agencies, as traffic flow can be optimised and, hence, fuel consumption and emissions decreased.

Under the open European Telecommunication Standards Institute (ETSI) Cooperative Awareness Message (CAM) framework, a traffic responsive GPS based vehicle actuation algorithm (GPS-VA) is proposed. GPS-VA uses position and heading data from vehicle status broadcasts, and inferred velocity information to determine vehicle queue lengths and detect vehicles passing through the intersection. The gathered information is then used to actuate intersection signal timings. Microscopic simulations comparing GPS-VA to fixed-time control and inductive loop based vehicle actuation (Loop-VA) on four urban road networks were performed to see how the proposed GPS-VA algorithm performs compared to existing control strategies. The results show that GPS-VA is an effective alternative to traditional intersection control strategies, offering delay reductions of up to 50\% for connected vehicle fleet penetrations above 30\%.


## I. Introduction

Traffic delays are a significant problem in developed vehicle markets, costing the global economy billions of dollars in lost time and wasted energy [1]. Responsive control of traffic signals is one way in which traffic delays can be reduced. From simple control schemes such as fixed-time (e.g. TRAN-SYT [2]), or vehicle actuation, to more sophisticated adaptive control schemes such as SCOOT [3] and MOVA [4], the choice of intersection control strategy is important in managing the network demand [5].

Intelligent Transport Systems (ITS) are the integration and application of communication systems, data driven control strategies, and large-scale information processing to transport systems. Many of the hypothesised traffic control schemes for ITS assume ideal communication between vehicles and infrastructure, or require the dominant presence of autonomous or connected vehicles in the network [6], [7], [8].

Connected and Autonomous Vehicles (CAVs) are predicted to be introduced from 2020 onward and it will take time for the vehicle fleet to turnover [9]. Therefore, there is a need for strategies that can modify existing infrastructure and support the transport network as it becomes increasingly automated.

[^0]CAV centric control schemes will be needed eventually. Since vehicles are incrementally modernised, it is important that traffic control strategies adapt according to the vehicle fleet composition.

In this paper, connected vehicles (CVs) are those which transmit and receive information from vehicles and infrastructure equipped with communication systems. Having multiple classes of vehicles has been shown to have negative effects on the resulting traffic flow [10], [11], and is taken into account.

This paper contributes the GPS-VA algorithm which uses position and heading data from vehicle status broadcasts, and inferred velocity information to actuate signal timings. The signal timings are adjusted by predicting vehicle queue lengths in stopped lanes, and detecting vehicles passing through the junction on lanes in their green cycle. The data are transferred from the vehicles to the intersections using the IEEE 802.11p communication protocol [12], and the ETSI Cooperative Awareness Message (CAM) framework [13] in order to ensure interoperability among connected vehicle implementations. The proposed GPS-VA scheme is tested and compared in simulations to fixed-time control and Loop-VA on four common urban road networks (A T-junction, twin T-junction, corridor, and Manhattan grid).

This paper is organised as follows: Section II discusses the background literature surrounding the technologies and standards necessary to achieve GPS-VA, as well as existing intersection control strategies. In Section III fixed-time, Loop-VA, and GPS-VA intersection control algorithms are defined. The simulation procedure used to compare the algorithm to existing methods is outlined in Section IV, and the simulation results are presented and discussed in Section V. Finally, conclusions are drawn in Section VI and avenues for further research are discussed.

## II. Background

In order to facilitate an algorithm such as GPS-VA several technologies are required: The IEEE 802.11p communication protocol as discussed in Section II-A, the Global Positioning System (GPS) as outlined in Section II-B, and the ETSI Cooperative Awareness Message (CAM) is reviewed in Section II-C. Finally, previous work on communication based intersection management is summarised and the areas where GPS-VA extends the current literature are highlighted in Section II-D.

## A. Wireless Communications

IEEE 802.11p [12] amends IEEE 802.11 [14], and describes the architecture for Dedicated Short-Range Communication (DSRC) [15] systems in Wireless Access in Vehicular Environments (WAVE)[16]. The DSRC specification allocates the

75 MHz frequency band centred around 5.9 GHz (5.850 - 5.925 GHz) for intelligent transport applications.

IEEE 802.11p wireless networks are defined for three channel widths (20, 10, and 5 MHz); however, IEEE 802.11p DSRC networks will commonly utilise a 10 MHz channel width [17]. IEEE 802.11p has effective bit rates in the range $3-27 \mathrm{Mbps}$ as a result of using the lower 10 MHz channel width, and the implementation of forward error correction to increase the chance of successful decoding.

Research on IEEE 802.11p networks shows that signal strength within a 250 m range is high enough that messages can be received correctly [18], [19], and that packet latencies of approximately 50 ms are achievable at vehicles speeds up to 90 km/h [18].

## B. Global Positioning System

The Global Positioning System (GPS) is a network of satellites operated by the U.S. Department of Defence. The satellites operate at two carrier frequencies in the UHF band [20]. The UHF band is used to penetrate the ionosphere and light cover (such as foliage) facilitating line-of-sight operation. 2-Dimension operation (longitude and latitude) requires line-ofof sight at least 3 satellites, and a minimum of 4 satellites for 3-Dimension operation (longitude, latitude, and elevation).

GPS receivers gather position and time information from orbiting satellites and use the difference in time between its internal clock and the received times determine the device's location through trilateration. GPS resolution is typically around 5m or finer depending the number of overhead satellites and what correction techniques are implemented in the receiver [21]. A map-matched position can be used to provide a more accurate position than raw GPS coordinates if spatial road network data is available to the receiver [22]. Refresh rates of 1 Hz is typical of commercial GPS receivers, although 5 Hz and 10 Hz receivers are available for applications such as vehicle control, where more frequent updates are required [23].

## C. Cooperative Awareness Messages

CAMs [13] provide periodic status and position information to other agents within an ITS. The ETSI CAM standard specifies ITS agents engaging in V2X (Vehicle-to-Everything) communications must be able to transmit and receive CAMs. CAMs are transmitted periodically at rates between of 1 Hz and 10 Hz and are generated if any of the following conditions are met:

- A change in vehicle heading greater than $4^{\circ}$ occurs.
- The vehicle's position changes by more than 5 m..
- The vehicle is travelling at a velocity greater than 1 m/s.

CAM messages provide information to ITS agents, informing them of the positions and status of the other agents in the network, by relaying data such as longitude, latitude (degrees), and heading. The status of the ITS can be determined from information about its mobility, privacy, and physical relevancy (i.e. its state of presence on the road) from the CAM.

## D. Existing Intersection Control Strategies

A key area of concern for communications based control strategies is the number of CAVs present. Control strategies considering only CAVs are less complex to develop than those that consider mixed vehicle fleets. Much of the existing work focuses primarily on CAV control, providing information to vehicles to control their movements for example [7], [8]. An unbiased strategy that reduces delay for all users, rather than a select few CAV users, is preferable.

Work has also been done that uses GPS data for signalised intersection control. Box and Waterson [24] proposed an auction based algorithm, where a bid value for each lane based on the position and velocity of each vehicle on the road is used to control signal timings. The work of Goodall [6] focused on using the IntelliDrive System [25] (derived from the SAE J2735 standard [26]). Goodall's work focused on inferring vehicle positions and queue lengths via ITS message exchange. The proposed GPS-VA algorithm adapts and extends Goodall's work by using the more accessible open access ETSI CAM standard rather than the closed access SAE J2735 standard. Additionally, instead of only using queuing information, GPS-VA incorporates dynamic vehicle tracking to better actuate the stage timings.

## III. Intersection Control Strategies

In this section, the developed intersection control schemes are described. First, some terminology is introduced and the algorithms for the fixed-time and vehicle actuation benchmark intersection controllers are presented. An algorithm which uses GPS data to perform vehicle actuation is then proposed.

Traffic stages are defined as the traffic lights configuration at an intersection. Table I defines the possible phases a traffic light can have and their meanings. Here, a stage comprises the set of traffic phases that give priority green to a single side of intersection. The side of the junction showing priority green will be referred to as the 'active side', the others are considered 'inactive'. Inactive lanes display permissive green on routes that are not in conflict any priority green streams, and red on streams that conflict with priority stream(s). Pedestrians are not considered so stages only account for vehicle presence.

TABLE I: Traffic light phase definitions.
| Phase | Description |
| :--- | :--- |
| Red | Vehicles must stop |
| Yellow | Vehicles stop if it is safe to do so |
| Permissive Green | Vehicles proceed if the road is unoccupied by vehicles in a priority green stream |
| Priority Green | Vehicles proceed if it is safe to do so |


## A. Existing Algorithms

1) Fixed-time Control: Fixed-time control is the most basic form of automated signal control. Each side of the intersection is set active for a predetermined amount of time, and the controller cycles through the stages sequentially. Algorithm 1
is the pseudocode description of the fixed-time control process. Fixed-time control is relatively simple to implement but is not inherently adaptive or responsive, and cannot be optimised beyond calibrating the timings using historic traffic flow data.
```
Algorithm 1: Fixed-Time Control Algorithm Pseudocode
    begin Fixed-time control
        if elapsedTime < stageDuration then
            elapsedTime ← elapsedTime + timeStep
        else
            DO: change to next traffic stage
            elapsedTime ← 0
```

2) Loop Based Vehicle Actuation: Loop-VA uses inductive loops [27] to detect traffic and responsively adjust stage durations according to the traffic demand detected at the intersection.

In this paper, a fully-actuated intersection control strategy is implemented under Federal Highways Administration Signal Timing Manual (STM) [28] guidelines for Loop-VA. LoopVA systems can skip stages if they do not detect vehicles in the lane(s) corresponding to those stages; however, in order to make the Loop-VA scheme comparable to the GPS-VA scheme presented in Section III-B, a minimum green time is defined. The STM specifies that the minimum green time of between 7 and 16 s for major arterial roads, and between 4 and 10 s for minor arterial roads satisfies driver expectancy and queue clearance criteria for speed limits up to 50km/h. As the models used contain both minor and major arterial roads, the driver expectancy and queue clearing criteria for both road types is satisfied by a minimum green time of 10 s.

Maximum green times of 40 to 60 s for major arterials, and 30 to 50 s for minor arterials, are recommended on roads with speed limits up to 50km/h. As major arterials take precedence, a 60 s maximum green time satisfies the condition for major arterials, and does not greatly exceed the maximum green time upper limit for minor arterials.

The stage green time is extended in response to vehicle flows greater than 80\% of the lane's saturation flow in any priority green lane. The measured saturation flow for all lanes is $S=2160 \mathrm{veh} / h$. Therefore, vehicle flows above 80\% of the saturation flow can be detected if the last detection time between the detectors is less than $2 \mathrm{~s}(0.8 S / 3600=$ 0.48 veh $/ \mathrm{s} \mapsto \sim 2 \mathrm{~s} /$ veh ) and the green time can be extended if the maximum green time is not exceeded. An extend time between 0.1 and 2 s is suggested by the STM based on the work of Bonneson and McCoy [29], so an extend time of 1 s is used.

Algorithm 2 describes the Loop-VA implementation. In practice, adaptive algorithms such as SCOOT [3] and MOVA [4] are widely used to provide isolated and connected control to signalised intersections.

```
Algorithm 2: Loop-VA Algorithm Pseudocode
    begin Vehicle Actuation
        DO: get flow data from inductive loops
        flow ← activeLaneFlow
        if flow > flowThreshold then
            stageExtendTime ← defaultExtendTime
        else
            stageExtendTime ← 0
        stageDuration ←
            max(stageDuration, minGreenTime)
            + stageExtendTime
        stageDuration ←
            min(stageDuration, maxGreenTime)
        if elapsedTime < stageDuration then
                elapsedTime ← elapsedTime + timeStep
        else
                DO: change to next traffic stage
                elapsedTime ← 0
                stageDuration ← 0
```


## B. GPS Based Vehicle Actuation Algorithm

GPS-VA proposes the utilisation of GPS data extracted from CAMs broadcast by CVs to actuate signal timings. Inductive loop flow data are deliberately ignored so that the algorithm's performance relies solely on the information collected from CAMs (cf. Section II-C) communicated over a DSRC channel (cf. Section II-A).

Algorithm 3, which describes the GPS-VA implementation, can be understood in two parts, vehicle data acquisition, and intersection control:

1) Vehicle data acquisition: Vehicle data acquisition determines which CAMs originate from vehicles in the junction's control region, determining the queue length on routes that are not inactive, and the locations and velocities of the vehicles on the active lane.

The junction control region is defined as the 250 m radius surrounding the junction (area of reliable communication, cf. Section II-A). If another junction exists inside the control region, the boundary is cropped to 10 m less than the conflicting junction's location. The boundary reduction ensures as large a control region as possible while allowing data from vehicles associated with other junctions to be ignored.

The junction controller receives CAMs from all vehicles inside its control region, ignoring those that are not. The CAMs are broadcast by vehicles at a rate of 10 Hz over a DSRC network (cf. Section II-C). For these experiments, it is assumed that the junction controller receives an accurate snapshot of the network at a delay of 0.2 s. Further work may integrate a network simulation layer, such as ns-3 [30], to more accurately gauge the effects of the communication system on the algorithm's performance. The GPS position provided by the CAM updates at a rate of 10 Hz. In future, one may implement a system that considers multiple time-scales (e.g., 1 Hz, 5 Hz, and 10 Hz GPS).

The junction controller stores data regarding the vehicle positions and headings. The vehicles' velocities can be inferred from CAM data from previous time steps, and their lanes and approaches can be inferred from their headings. The junction controller has knowledge of its own layout/map and is able to determine the headings that correspond to an approach on each of its lanes. Vehicles in range of the junction and travelling with headings matching one of the known approaches (± a certain tolerance to allow for GPS positioning error) are considered to be approaching the junction.
2) Intersection Control: Inactive lane queue lengths are determined as the distance of the furthest queuing vehicle from the intersection. A vehicle is queuing if it is travelling at less than 5\% of the road speed limit (inferring that vehicles travelling so slowly are at or approaching the end of the queue). In this experiment, all vehicles are 5 m long and maintain a minimum gap of 2.5 m, therefore their effective vehicle length is $l_{\text {eff }}=7.5 \mathrm{~m}$. In the minimum green cycle of 10 s, the vehicle flow is estimated to be 1080 veh/h corresponding to $0.3 \mathrm{veh} / \mathrm{s}$, therefore the time to clear 1 vehicle is $3 . \dot{3} \mathrm{~s} /$ veh . As the effective vehicle length is known, the time for a vehicle to clear 1 m is $3 . \dot{3} / 7.5 \approx 0.45 \mathrm{~s}$. The vehicle clearance time per meter is calculated over the minimum green cycle. Therefore, the time loss due to stopand-go wave effects [31] resulting from finite driver reaction times is incorporated, and thus provides a slightly larger than required value. The vehicle clearance time per meter can be multiplied by the distance between the intersection and the last vehicle in the queue to get the queue clearance time.

If oncoming vehicles in the active lane are within 25 m of the intersection, the time it will take the vehicle to reach the intersection (centre point) is added to the stage duration if it will take longer than the remaining stage time to clear the intersection (up to the maximum green time). The time for a vehicle to reach the intersection is calculated as its distance from the intersection divided by its velocity if known. Otherwise, it is calculated based on its distance from the intersection times the clearance time per meter.

## IV. Simulation

Here, microsimulation is used to test whether intersection management can be improved using information from standardised ITS data streams. The GPS-VA strategy is compared to the cases where intersections are managed by fixed-time and Loop-VA controllers. The simulations are performed using the SUMO microsimulation environment [32]. The simulation is controlled using a Python API [33], [34], [35] that interfaces with SUMO and contains four intersection models (see Figure 1). All roads in the models operate at a 50 km/h speed limit, and the intersections contain inductive loops at 6 m and 18 m from each stop-line per UK Highways Agency standard MCE 0108 [36].

## A. Car-following Parameters

The Krauss [37] microscopic car-following model was chosen as it produces stable collision-free traffic flow, and is

```
Algorithm 3: GPS-VA Algorithm Pseudocode
begin GPS-VA
    DO: get CAM data
    for laneID \(\in\) approachLaneIDs do
        if lane is active then
            if nearestVehicleSpeed \(\neq\) NULL then
                queueClearTime ← nearestVehicleDistance
                    / nearestVehicleSpeed
            else
                queueClearTime ← nearestVehicleDistance
                    × clearTimePerMeter
            stageDuration[laneID] ←
                max(queueClearTime, remainingTime)
            stageDuration[laneID] ←
                min (stageDuration[laneID], maxGreenTime)
        else
            if lastVehicleDistance \(\neq\) NULL then
                queueClearTime ← lastVehicleDistance ×
                    clearTimePerMeter
                stageDuration[laneID] ←
                    max(queueClearTime, minGreenTime)
                stageDuration[laneID] ←
                    min(stageDuration[laneID],
                    maxGreenTime)
            else
                stageDuration[laneID] ← minGreenTime
    if elapsedTime < stageDuration[activeLaneID] then
        elapsedTime ← elapsedTime + timeStep
    else
        DO: change to next traffic stage
        elapsedTime ← 0
        stageDuration ← 0
```

well validated. As GPS-VA depends on information from CVs, the performance of the control strategies will depend on the penetration of CVs in the fleet. In order to model increasing CV penetration, two vehicle types are defined: Unconnected vehicles which do not support ITS functionality, and CVs capable of communicating CAMs. It is assumed that CVs do not have any driving advantages over unconnected vehicles. Therefore, both vehicle types have identical car-following parameters as described in Table II. The only difference between the vehicle types is that CVs can broadcast ITS CAMs. The parameters in Table II are typical of a passenger car.

## B. Traffic Generation

Vehicle routes are randomly generated for each simulation run based on the probability of a vehicle travelling along a given route at rates of ~ $1500 \mathrm{veh} / \mathrm{h}$ for approximately 3 hours. The vehicles are randomly assigned a type (unconnected or CV) based on a CV penetration ratio from 0 to 1. The CV presence in the network is incremented from 0\% to 100\% in steps of 10\%. As the proportion of CVs and the routes are

![](https://cdn.mathpix.com/cropped/ee5111b5-ba3a-448b-8ed8-3cdf546395cb-5.jpg?height=571&width=855&top_left_y=172&top_left_x=185)
Fig. 1: The four road topologies used in the simulations. (a) Simple T-Junction, (b) Twin T-Junction, (c) Corridor, (d) Manhattan grid.

TABLE II: The Krauss car-following model parameter values for both unconnected vehicles and CVs.
| Parameter | Value |
| :--- | :--- |
| Acceleration ( $\mathrm{m} / \mathrm{s}^{2}$ ) | 0.8 |
| Deceleration ( $\mathrm{m} / \mathrm{s}^{2}$ ) | 4.5 |
| Driver Imperfection - $\sigma$ | 0.5 |
| Reaction Time - $\tau(\mathrm{s})$ | 1.0 |
| Length (m) | 5.0 |
| Min. Gap (m) | 2.5 |
| Max. Speed (m/s) | 25 |


defined at random, the experiments are repeated 10 time for each CV penetration to achieve a reliable mean delay and confidence intervals.

## C. Free-flow Travel Times

The free-flow travel time is the base on which the delay calculations in Section V are made. Free-flow travel time is established by setting all intersection lights to green and passing 50 cars along each route in all the models. The average free-flow travel time for each route is then established. The vehicle departures are spaced in time so that the vehicles do not interact. Additional time is added between the calculation of a subsequent route's free-flow time to allow vehicles from the previous test to clear the network.

## V. Results and Discussion

The proposed GPS-VA algorithm is tested against the fixedtime and Loop-VA control algorithms on four road network models at increasing levels of CV penetration. Here, CV penetration is the percentage of connected vehicles in the network. Figure 2 shows a comparison of the delay times for each intersection control strategy on each road model.

Travel-time delay characterises the excess time a vehicle takes to complete its journey compared to the free-flow travel time for the same journey. The simulation time $T_{\text {sim }}$ is:

$$
T_{\mathrm{sim}}=T_{\mathrm{out}}-T_{\mathrm{add}}
$$

where $T_{\text {add }}$ is the time the vehicle is added to the simulation, and $T_{\text {out }}$ is the time the vehicle exits the simulation. Time delay $T_{\text {Delay }}$ can therefore be given by

$$
T_{\text {Delay }}=T_{\text {sim }}-T_{\text {freeflow }}
$$

where $T_{\text {freeflow }}$ is the time it takes the vehicle to make its journey on an unobstructed route. The free-flow travel times $T_{\text {freeflow }}$ are as calculated in Section IV-C. Delay time indicates the amount of time actually saved compared to the complete journey time, and highlights the performance limitations of each method.

Figure 2 shows a comparison of the delay times for each intersection control strategy on each road model. It can be seen that in all cases, the traffic responsive actuated control strategies reduce delays better than the fixed-time algorithm. GPS-VA degenerates to fixed-time with minimum green time cycles and performs poorly at low CV penetrations due to a control action deficit. However, at CV penetration rates exceeding 30\%, GPS-VA reduces delay comparably to or better than the implemented Loop-VA strategy for different traffic levels. GPS-VA's poor performance at low CV penetrations suggest that future work should investigate a system that uses both inductive loop and CAM information cooperatively. The Loop-VA and fixed-time strategies do not show as large a delay difference in the corridor model as in the other three. This is due to the short road segments connecting each junction inhibiting traffic flow. A coordinated strategy is more appropriate than isolated control in this case.

The reduction in delay with increasing CV penetration for GPS-VA is similar for road networks (a), (c), and (d), but much steeper for network (b). The alternative trend in the delay line on network (b) could be attributed to the proximity of the junctions, or more likely is due to the traffic demand levels applied to the network being too low to stress the junction adequately.

## VI. Conclusions and Future Work

This paper explores how traffic responsive GPS based vehicle actuation can be achieved under the ETSI CAM framework. The algorithm uses position and heading data received from CV status broadcasts to actuate intersection signal timings by determining vehicle queue lengths and detecting vehicles passing through the intersection.

Microscopic simulations were performed to see how the proposed GPS-VA algorithm performs compared to fixed-time and Loop-VA control strategies on four common urban road topologies. The results show that GPS-VA is a compelling alternative to traditional intersection control strategies, showing delay reductions of 10\% - 50\% over traditional Loop-VA for CV penetrations exceeding 30\%.

Algorithms that incorporate data from CVs and that consider low CV fleet penetrations are still an underdeveloped research area. Further work needs to be done on the algorithm to incorporate both GPS data and inductive loop information to increase the robustness of the algorithm at low CV penetrations. Work also needs to be done to establish the effects

![](https://cdn.mathpix.com/cropped/ee5111b5-ba3a-448b-8ed8-3cdf546395cb-6.jpg?height=468&width=1796&top_left_y=185&top_left_x=159)
Fig. 2: Travel-time delay for the three intersection control strategies on each of the four road networks. The solid lines denote the mean delay over all the simulation runs. The dashed lines denote the 5th and 95th percentiles of the data as an indicator of travel time variability.

of errors on the GPS-VA algorithm. Communication packet loss, GPS measurement noise, and disparate GPS measurement rates all must be considered if the algorithm is to be robust in real road networks and reliably provide reduced travel times to drivers.

## Acknowledgements

The authors would like to acknowledge support from the EPSRC and the Transport Research Laboratory (TRL) under Centre for Doctoral Training grant EP/L015382/1.

## References

[1] CEBR, "The future economic and environmental costs of gridlock in 2030," tech. rep., London, 2014.
[2] D. I. Robertson, "TRANSYT: a traffic network study tool," Ministry of Transport Road Research Laboratory Report, vol. LR 253, 1969.
[3] P. Hunt, D. Robertson, R. Bretherton, and R. Winton, SCOOT: A Traffic Responsive Method of Coordinating Signals. TRRL, 1981.
[4] G. R. Vincent and J. R. Peirce, "MOVA: Traffic responsive, selfoptimising signal control for isolated intersections," TRRL Research Report, vol. RR170, 1988.
[5] M. Papageorgiou, C. Diakaki, V. Dinopoulou, A. Kotsialos, and Y. Wang, "Review of road traffic control strategies," Proceedings of the IEEE, vol. 91, no. 12, pp. 2043-2067, 2003.
[6] N. Goodall, B. Smith, and B. Park, "Traffic Signal Control with Connected Vehicles," Transportation Research Record, vol. 2381, 2013.
[7] T. C. Au, S. Zhang, and P. Stone, "Autonomous Intersection Management for Semi-Autonomous Vehicles," Handbook of Transportation, 2015.
[8] B. HomChaudhuri, R. Lin, and P. Pisu, "Hierarchical control strategies for energy management of connected hybrid electric vehicles in urban roads," Transportation Research Part C, vol. 62, 2016.
[9] T. Litman, "Autonomous Vehicle Implementation Predictions," Victoria Transport Policy Institute, vol. 28, 2016.
[10] D. Ngoduy, "Effect of driver behaviours on the formation and dissipation of traffic flow instabilities," Nonlinear Dynamics, vol. 69, no. 3, 2012.
[11] D. Ngoduy, "Effect of the car-following combinations on the instability of heterogeneous traffic flow," Transportmetrica B: Transport Dynamics, vol. 0566, no. February 2015, 2014.
[12] IEEE, "IEEE Standard for Information technology - Local and metropolitan area networks - Specific requirements - Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications Amendment 6: Wireless Access in Vehicular Environments," IEEE Std 802.11p-2010, 2010.
[13] ETSI, "TS 102 637-2 Vehicular Communications Part 2: Specification of Cooperative Awareness Basic Service," 2011.
[14] IEEE, "IEEE Standard for Information technology-Telecommunications and information exchange between systems Local and metropolitan area networks-Specific requirements Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications," IEEE Std 802.11-2012 (Revision of IEEE Std 802.11-2007), pp. 1-2793, 2012.
[15] FCC, "Dedicated Short Range Communications Report and Order," tech. rep., U.S. FCC, R\&O FCC 03-324, 2003.
[16] IEEE, "IEEE Guide for Wireless Access in Vehicular Environments (WAVE) - Architecture," IEEE Std 1609.0-2013, pp. 1-78, 2014.
[17] J. B. Kenney, "Dedicated Short-Range Communications (DSRC) Standards in the United States," Proc. IEEE, vol. 99, no. 7, 2011.
[18] I. C. Msadaa, P. Cataldi, and F. Filali, "A Comparative Study between 802.11p and Mobile WiMAX-based V2I Communication Networks," in Conf. Next Generation Mobile Applications, Services and Technologies, IEEE, 2010.
[19] Z. Hameed Mir and F. Filali, "LTE and IEEE 802.11p for vehicular networking: a performance evaluation," EURASIP Journal on Wireless Communications and Networking, vol. 2014, no. 1, 2014.
[20] B. Hofmann-Wellenhof, H. Lichtenegger, and J. Collins, Global positioning system: theory and practice. Springer Science, 2012.
[21] M. S. Grewal, L. R. Weill, and A. P. Andrews, Global Positioning Systems, Inertial Navigation and Integration. John Wiley \& Sons, 2001.
[22] M. A. Quddus, W. Y. Ochieng, and R. B. Noland, "Current mapmatching algorithms for transport applications: State-of-the art and future research directions," Transportation Research Part C, 2007.
[23] H. S. Bae, J. Ryu, and J. C. Gerdes, "Road grade and vehicle parameter estimation for longitudinal control using GPS," in Proceedings of the IEEE Conference on Intelligent Transportation Systems, 2001.
[24] S. Box and B. J. Waterson, "Signal control using vehicle localization probe data," in 42nd UTSG Conference, 2010.
[25] B. L. Smith, R. Venkatanarayana, H. Park, N. Goodall, J. Datesh, and C. Skerrit, "IntelliDrive SM Traffic Signal Control Algorithms Final Report IntelliDrive SM Pooled Fund Study," tech. rep., 2011.
[26] SAE, "Dedicated Short Range Communications (DSRC) Message Set Dictionary, SAE Std. J2735," tech. rep., SAE Int., 2016.
[27] P. J. Yauch, Traffic Signal Control Equipment: State of the Art, vol. 166. Transportation Research Board, 1990.
[28] P. Koonce, L. Rodegerdts, K. Lee, and S. Quayle, "Traffic signal timing manual," p. 273, 2008.
[29] J. A. Bonneson and P. T. McCoy, Manual of Traffic Detector Design. Texas Transportation Institute, Texas A \& M University System, 2005.
[30] G. F. Riley and T. R. Henderson, "The ns-3 Network Simulator," in Modeling and Tools for Network Simulation, pp. 15-34, Berlin Heidelberg: Springer, 2010.
[31] R. E. Wilson, "Mechanisms for spatio-temporal pattern formation in highway traffic models.," Philosophical Trans. Series A, vol. 366, 2008.
[32] D. Krajzewicz, M. Bonert, and P. Wagner, "The Open Source Traffic Simulation Package \{SUMO\}," RoboCup 2006, 2006.
[33] G. Rossum, "Python Reference Manual," tech. rep., Amsterdam, The Netherlands, 1995.
[34] A. Wegener, M. Piórkowski Michałand Raya, H. Hellbrück, S. Fischer, and J.-P. Hubaux, "TraCI: An Interface for Coupling Road Traffic and Network Simulators," in Proc. 11th Comm. and Net. Sim. Symp., 2008.
[35] S. Box, "Traffic Control Test Set," 2013.
[36] Highways Agency, "Siting of Inductive Loops for Vehicle Detecting Equipments at Permanent Road Traffic Signal Installations," Tech. Rep. C, Highways Agency, 2002.
[37] S. Krauß, "Microscopic modeling of traffic flow: Investigation of collision free vehicle dynamics," $D L R$ - Forschungsberichte, no. 8, 1998.

[^0]:    *Corresponding author
    All authors are with: Transportation Research Group, Faculty of Engineering and the Environment University of Southampton, SO16 7QF, United Kingdom
    Email: \{c.b.rafter, b.anvari, s.box\}@soton.ac.uk

