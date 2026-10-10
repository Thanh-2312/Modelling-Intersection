# A Rule Based Control Algorithm of Connected Vehicles in Uncontrolled Intersection 

Guangquan Lu, Lumiao Li, Yunpeng Wang, Ran Zhang, Zewen Bao, Haichong Chen


#### Abstract

Aiming to address the safety issue for the uncontrolled intersection, the existing schemes including design optimization of the intersection structure and additional traffic signal layout will waste lots of resources. With the rapid development of intelligent transportation, the technology of vehicle-vehicle communication provides a new way for this problem. The paper proposed a set of rules to clarify the sequence of vehicles to pass through uncontrolled intersection. The rules are planned based on the law of road traffic safety. According to the rules, each approaching car makes decision for preempting or yielding other cars based on the information from vehicle-vehicle communication. If the approaching car needs to yield other cars, we propose an algorithm to find a proper deceleration value to do yielding. The car brakes automatically using this deceleration value to avoid collision with other cars. After all, the tests were done to verify the effectiveness of the algorithm and demonstrate the function among the connected vehicles in intersection. The rule based collision avoidance algorithm can provide real-time collision detection and make safe deceleration for the cars crossing the uncontrolled intersection.


## I. Introduction

Traffic conflict is a phenomenon that can be observed. It mainly refers to two or more road users having potential

[^0]conflict when they are approaching each other. If they don't change their motion timely, collision will happen. Within the traffic conflict, vehicle-vehicle conflict is the common problem that plays an importance role in traffic safety, especially for intersection safety. With the development of wireless communication technology and intelligent vehicle technology, vehicle-to-vehicle communication (V2V) safety applications have been concerned by many researchers[1-7]. Zohdy and Rakha proposed a heuristic optimization algorithm for Intersection-based Cooperative Adaptive Cruise Control (CACC) Systems. In this system, vehicles communicate with other vehicles through V2V and vehicle-to-infrastructure (V2I) communication. Alexander and Haley applied V2V to prevent avoidable collisions by warning the driver (or even taking the automatic intervention) when vehicles had identified unsafe conditions.

V2V is an important part of Cooperative Vehicle Infrastructure System(CVIS) . As the key subsystem of CVIS control, V2V Control puts emphasis on conflict resolution, vehicle control and safety warning based on information collected through the on-board sensors and information interaction. With V2V, vehicles communicating with each other can be used in different applications and services that involved in traffic safety, such as cooperative driver assistance [8]. So V2V can be utilized in the following safety applications: (1) Traffic jam avoidance; (2) Vehicle collision avoidance in intersection; (3) Car-following by information interaction; (4) Lane-changing based onV2V; (5) Vehicle launch information based onV2V; (6) Abnormal road occupation warning; (7) Emergency braking of electronic brake warning lamp.

Due to its advances, Japan, USA, and Europe are all pioneers in V2V techniques, tools and applications[9]. Japan has made use of V2V broadcasting driving information (steering and speed) to each follower vehicle[10]. In this way, the front vehicles can send information to the behind vehicles and affect the behind vehicle's motion. United States has carried out the national projects[11, 12], such as Cooperative Vehicle-Highway Automation Systems(CVHAS) and IntelliDrive. These projects put emphasis on inter-vehicle communications and vehicle active safety and provide drivers with control assistance based on information that we can obtain by V2V. In European, it uses advanced sensors and vehicle positioning technology for collecting vehicle information and the surrounding traffic environment information through V2V. The main applications include the safe speed and following distance, horizontal assistance and intersection collision avoidance and etc. To sum up, they all put V2V control as their important research content and realize function of active collision avoidance.

Intersection Collision Avoidance System(ICAS) is one of the important researches of V2V and the key technologies of solving vehicle-vehicle conflict in uncontrolled intersections. ICAS can predict positions of the two (or more) vehicles, and both the current and future positions can be broadcast to surrounding vehicles using V2V. The popular avoidance system involved with intersection safety include Intersection Movement Assist (IMA) [13, 14] which is also known as intersection collision warning and Cooperative Vehicle Intersection Control (CVIC). IMA provides warnings of the potential side impact when drivers enter an intersection. The typical scenario is that the vehicle entering the intersection has low speed(or wait to enter) and the second vehicle is traveling at the speed limit. CVIC assumes that vehicles and an intersection controller could cooperatively work together to improve traffic operations at an intersection when all vehicles are fully automated [15]. And the inter-vehicle communication network will use tags to label the groups/vehicles encountered. So with a CVIC environment, an intersection controller would provide each vehicle with an adequate maneuver so that vehicles can safely pass through an intersection. And thus, traffic operations at intersections could be controlled without stop-and-go-style traffic lights.

In order to apply ICAS in uncontrolled intersections, scholars carried out a lot of researches which were about control algorithm and put forward the practical methods which can be divided into two categories. One category is the centralized control method based on the vehicle-infrastructure communication (V2I)[16]. This method needs to place a central controller with communication unit at the intersection and the central controller timely responses vehicles to requirement of crossing intersections, which effectively control the traffic at the same time. The other category is the distributed control method. This method mainly aims at the vehicle motion research and includes the acceptable gap model[17], the control method based on dynamic game theory[18], the conflict collision avoidance decision model based on preemptive level[19] and the lock resources algorithm based on conflict table[20].

In this paper, we equipped vehicles with sensors which obtain information of its own states, including dynamic position, speed, acceleration, and a communication module that broadcasts its own state information to other vehicles and receives data from other vehicles. We proposed a set of rules to clarify the sequence of vehicles passing through uncontrolled intersection. According to the rules, each approaching car makes decision for preempting or yielding other cars based on the information from V2V. If the approaching car needs to yield other cars, we propose an algorithm to find a proper deceleration value to do yielding. The car brakes automatically using this deceleration value to avoid collision with other cars. Finally, we carried out the tests to verify the effectiveness of the algorithm and demonstrate the function among the connected vehicles in intersection.

## II. RULES

According to China's Road Traffic Safety Law and relative implemented regulations, vehicle through intersections without traffic signal and police command should obey the following rules:
1)vehicles having entered the intersection have higher priority compared with vehicles preparing to enter intersection;
2)vehicles drive beside the left side of the road center point when turning on;
3)vehicles have higher priority under traffic sign and marking control;
4)vehicles going straight have higher priority compared with vehicles turning around;
5)left-turn vehicles have higher priority compared with right-turn vehicles in the opposite directions.

Taking Fig. 1 as a research instance, the vehicle in entrance1, as survey vehicle (SV), has three possible driving paths with left-turn1A, going-straight1B and right-turn1C. The POV includes twelve paths, which maybe any one of path iA, iB and iC (i=1,2,3,4). So the relative motion relationships include four kinds of collisions involved thirty-six types of conflict situations. The types of collisions include no collision, confluence point of conflict(represented with H), merging point of conflict(represented with F)and crossing point of conflict(represented with J).Table1 summarizes the rule of priority in uncontrolled intersections with traffic conflict.

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-2.jpg?height=593&width=696&top_left_y=1452&top_left_x=1171)
Figure 1. conflict of typical two-way single intersection

TABLE I. RULE OF PRIORITY AT UNSIGNALIZED INTERSECTION WITH TRAFFIC CONFLICT
| matching | Conflict describe | category | priority | go-first |
| :--- | :--- | :--- | :--- | :--- |
| (1A,1B) | left-turn, straight in same direction | F | uncertain | front |
| (1A,1C) | left-turn, right-turn in same direction | F | uncertain | front |
| (1A,2A) | left-turn, left-turn in right side | J | $2 \mathrm{~A}>1 \mathrm{~A}$ | 2A |
| (1A,2B) | left-turn, straight in right side | H | $2 \mathrm{~B}>1 \mathrm{~A}$ | 2B |
| (1A,3B) | left-turn, straight in opposite direction | J | $3 \mathrm{~B}>1 \mathrm{~A}$ | 3B |
| (1A,3C) | left-turn, right-turn in opposite direction | H | 1A>3C | 1A |
| (1A,4A) | left-turn, left-turn in left side | J | 1A>4A | 1A |
| (1A,4B) | left-turn, straight in left side | J | $4 \mathrm{~B}>1 \mathrm{~A}$ | 4B |
| (1B,1A) | Straight, left-turn in same direction | F | uncertain | front |
| (1B,1C) | Straight, right-turn in same direction | F | uncertain | front |
| (1B,2A) | Straight, left-turn in right side | J | 1B>2A | 1B |
| (1B,2B) | Straight, straight in right side | J | $2 \mathrm{~B}>1 \mathrm{~B}$ | 2B |
| (1B,2C) | Straight, right-turn in right side | H | 1B>2C | 1B |
| (1B,3A) | Straight, left-turn in opposite direction | J | 1B>3A | 1B |
| (1B,4A) | Straight, left-turn in left side | H | $1 \mathrm{~B}>4 \mathrm{~A}$ | 1B |
| (1B,4B) | Straight, straight in left side | J | $1 \mathrm{~B}>4 \mathrm{~B}$ | 1B |
| (1C,1A) | right-turn, left-turn in same direction | F | uncertain | front |
| (1C,1B) | right-turn, straight in same direction | F | uncertain | front |
| (1C,3A) | right-turn, left-turn in opposite direction | H | 3A>1C | 3A |
| (1C,4B) | right-turn, straight in left turn | H | $4 \mathrm{~B}>1 \mathrm{C}$ | 4B |


## III. Collision Avoidance Algorithm

The study makes the following hypothesis to reflect the regulation of collision: (a) two-lane road of intersection; (b) just taking vehicles collision into consideration without influence of bicycles and pedestrians; (c) all vehicles been equipped with on-board sensors to detect dynamic position, speed, acceleration; (d) normal communication from beginning of operation to end of operation.
A. Collision Avoidance Algorithm Between Two Vehicles without Road Information

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-3.jpg?height=357&width=617&top_left_y=1987&top_left_x=247)
Figure 2. collision avoidance principle between two vehicles without road information

In this situation, vehicles with low priority put off time
arriving to the collision area without stopping until vehicles with higher priority driving away the collision area. Fig. 2 shows the collision avoidance principle between two vehicles without road information.

As shown in Fig.2, vehicle's real traveling distance in process of giving way as follows:

$$
S=D T C
$$

where DTC is the curve distance between the location of vehicle to the conflict point.

Taking time of Braking System to eliminate brake clearance into consideration, vehicle's traveling distance is formulated as follows:

$$
S_{\text {clearence }}=V \tau
$$

Then the relationship of variables is defined as follows:

$$
S-S_{\text {clearence }}=V(T T L-\tau)+\frac{1}{2} a(T T L-\tau)^{2}
$$

where TTL is the time vehicle B driving away the collision area and TTL=TTC+M, TTC is the time vehicle arriving the collision area, M is a set value.

That is,

$$
\mathrm{a}=\frac{2(D T C-(T T L-\tau)-V \tau)}{(T T L-\tau)^{2}}
$$

Vehicle SV driving with acceleration of the above value will just arrive area of collision when vehicles POV leave this area.

The paper adapts the simplified algorithm of taking curve into straight line to calculate trajectory. In order to ensure vehicles safety, we adapt the minimum distance, that is L* $\sin \Psi$, from vehicle SV to vehicle POV instead of the distance from vehicle to trajectory point. So the target acceleration of vehicle safely crossing intersection is formulated as follows:

$$
\mathrm{a}=\frac{2(\mathrm{~L} * \sin \Psi-(T T L-\tau)-V \tau)}{(T T L-\tau)^{2}}
$$

The algorithm adopts the kinematics formula to carry out the collision avoidance strategy, which is based on the rule of priority in uncontrolled intersections. And it's the significant difference compared to the previous algorithms.

## B. Collision Avoidance Algorithm among Vehicles

Aiming to solve the conflict among vehicles in uncontrolled intersection, the first thing is to determine the order of passing through intersection, which is based on the rules described in Table1, and then carry out the speed control strategy.Fig.3(a)shows the scenario of conflict among four vehicles.

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-4.jpg?height=511&width=715&top_left_y=1364&top_left_x=262)
Figure 3. (a) conflict among four vehicles

Vehicle R and vehicle P can directly cross intersection without adjusting speed. Vehicle N should yield and adjust appropriate speed to avoid conflict with vehicle R and vehicle P. Under this circumstance, the necessary deceleration of vehicle N to avoid collision is $a_{N R}$ (with vehicle R) and $a_{N P}$ (with vehicle P). Obviously, vehicle N selects the larger deceleration as its target value to eliminate both conflicts with vehicle R and vehicle P. The same method is applied to vehicle Q, with selecting the larger deceleration from $a_{Q_{N}}$ and $a_{Q_{P}}$ that calculated with vehicle N and vehicle P, and finally to solve both collisions. Through the above analysis, collision avoidance strategy among vehicles can be displayed as Fig. 3 (b).

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-4.jpg?height=483&width=694&top_left_y=189&top_left_x=1201)
Figure3. (b) flow of collision avoidance

## IV. Test and Evaluation

The paper carried on the real vehicle tests to verify correct of conflict detection and collision avoidance strategy in uncontrolled intersection at Langfang, Hebei Province of China.

## A. Vehicles with V2V Function

Vehicle has made the necessary modification based on demand of data collection by installing GPS, gyroscope, WIFI, Industrial Personal Computer (IPC) and Human Machine Interface (HMI). Double antenna GPS is responsible for collection of vehicle position information and Angle. Gyroscope collects vehicle acceleration and yawing angular information. WIFI sends vehicle state information to other vehicles and receives other cars information. IPC controls information related to cars. Horns and display screen are human-computer interaction devices, with horns used for voice alarm and screen monitoring risk grade warning through graphical interface.

## B. Test without Road Information

We select two typical scenarios for test. In the first scenario, two vehicles went straight from the vertical directions. Fig.4(a) and Fig.4(b) respectively describe the actual trajectories of vehicle SV and POV and X, Y coordinates of vehicles with time.

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-4.jpg?height=473&width=696&top_left_y=1888&top_left_x=1195)
Figure 4. (a) the actual trajectories of vehicle SV and POV

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-5.jpg?height=526&width=694&top_left_y=180&top_left_x=286)
Figure4. (b) X, Y coordinates of vehicles SV and POV with time

In the test, both vehicles started at 150 meters far-away from the intersection with conflict. POV had higher priority than SV to cross the collision area when both vehicles had the same X coordinates and Y coordinates of vehicle POV was greater than vehicle SV's. Under this situation, the function of collision avoidance can be realized in this scenario if trajectories satisfy the conditions. Y coordinate of vehicle SV was smaller than that of vehicle POV when X coordinates of two vehicles were intersected. It can be seen that lower priority vehicle can realize the function of collision avoidance in this scenario.

At the time of the same X coordinate values of both vehicles, the difference of Y coordinate values was 9.95 meters, with length of vehicle 4.5 meters and the wide 1.8 meters. So the distance of the nearest point of the two vehicles was about 6.8 meters. It shows that when the right straight vehicle crossed the conflict point, the distance from the straight vehicle to the conflict point is 6.8 meters.

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-5.jpg?height=520&width=685&top_left_y=1543&top_left_x=264)
Figure4. (c) the change of acceleration and speed of vehicle SV

Fig.4(c) recorded the change of acceleration and speed of vehicle SV. Vehicle had the obvious deceleration process and just adopted the deceleration strategy without stop.

In the second scenario, one vehicle turned left and the other went straight in opposite direction. Fig.5(a) and Fig.5(b) respectively describe the actual trajectories of vehicle SV and POV and X, Y coordinates of vehicles.

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-5.jpg?height=354&width=703&top_left_y=185&top_left_x=1192)
Figure 5. (a) the actual trajectories of vehicle SV and POV

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-5.jpg?height=481&width=696&top_left_y=638&top_left_x=1190)
Figure5. (b) X, Y coordinates of vehicles SV and POV with time

![](https://cdn.mathpix.com/cropped/d97f958a-f47d-4d93-8a1e-a315ce27d83a-5.jpg?height=503&width=688&top_left_y=1186&top_left_x=1190)
Figure5. (c) the change of acceleration and speed of vehicle SV

POV had higher priority than SV to cross the collision area when both vehicles had the same X coordinates and Y coordinates of vehicle POV was greater than vehicle SV's. Under this situation, the function of collision avoidance can be realized in this scenario if trajectories satisfy the conditions. Y coordinate of vehicle SV was smaller than that of vehicle POV when X coordinates of two vehicles were intersected. It can be seen that lower priority vehicle can realize the function of collision avoidance in this scenario.

Fig.5(c) recorded the change of acceleration and speed of vehicle SV. Vehicle had the obvious deceleration process and just adopted the deceleration strategy without stop.

The same test and evaluation was adapted to other scenarios that listed in Table1.

## V. Discussion and Conclusion

In this paper, a set of priority rules is made to resolve conflict problems in intersection and the collision avoidance
algorithm provides the real-time collision detection and the safe deceleration for crossing the uncontrolled intersection. From the field test at Hebei Province of China, it was indicated that the collision avoidance algorithm met the practical situation and effectively realized the function of collision avoidance in uncontrolled intersection. This study could be significant for the following reasons. First, it was a special traffic rule which providing the standard traffic order for the uncontrolled intersection. Second, the collision avoidance algorithm based on the rules eliminated the conflicts of vehicles and improved the safety level of the uncontrolled intersection.

However, future works are still needed to study many vehicles conflicts in real vehicle test and to make vehicles automatically get road information by loading the electronic map.

## VI. Acknowledgment

This study is supported by the National Basic Research Program of China (2012CB725404) and also supported by the Fundamental Research Funds Program of Beihang University (YWF-14-JTXY-011).

## References

[1] I. Sen and D. W. Matolak, "Vehicle-Vehicle Channel Models for the 5-GHz Band," Intelligent Transportation Systems, vol. 9, pp. 235-245, 2008.
[2] A. Paier, J. Karedal, N. Czink, C. Dumard, T. Zemen, F. Tufvesson, et al., "Characterization of Vehicle-to-Vehicle Radio Channels from Measurements at 5.2 GHz," Wireless Personal Communications, vol. 50, pp. 19-32, 2008.
[3] Olivier Renaudin, Veli-Matti Kolmonen, Pertti Vainikainen, and C. Oestges, "Non-Stationary Narrowband MIMO Inter-Vehicle Channel Characterization in the 5-GHz Band," Vehicular Technology, vol. 59, pp. 2007-2015, 2010.
[4] Michael R. Hafner, Drew Cunningham, Lorenzo Caminiti, and D. D. Vecchio, "Cooperative Collision Avoidance at Intersections:Algorithms and Experiments," TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, vol. 14, pp. 1162-1175, 2013.
[5] Abbas Taimoor, Johan Karedal, and F. Tufvesson, "Measurement-based analysis: The effect of complementary antennas and diversity on vehicle-to-vehicle communication," 2013.
[6] Li Li, Ding Wen, and D. Yao, "A survey of traffic control aided by vehicular communication," IEEE Transactions on Intelligent Transportation Systems, vol. 15, pp. 425-432, 2014.
[7] Li Li and F. Y. Wang, "Cooperative driving at blind crossings using intervehicle communication," IEEE Transactions on Vehicular Technology, vol. 55, pp. 1712-1724, 2006.
[8] I. Jawhar, N. Mohamed, and L. Zhang, "Inter-vehicular Communication Systems, Protocols and Middleware," pp. 282-287, 2010.
[9] G. Karagiannis, O. Altintas, E. Ekici, G. Heijenk, B. Jarupan, K. Lin, et al., "Vehicular networking A survey and tutorial on and tutorial on requirements, architectures, challenges, standards and solutions," Communications Surveys \& Tutorials, IEEE, vol. 13, pp. 584-616, Fourth Quarter 2011.
[10] G. F. Dafflon B, Contet J M, et al. (2011) Intelligent crossroads for vehicle platoons reconguration. Adaptive and Intelligent Systems. 203-214.
[11] J. A. Misener, and Steven E. Shladover, "PATH Investigations in Vehicle-Roadside Cooperation and Safety: A Foundation for Safety and Vehicle-Infrastructure Integration Research," Intelligent Transportation Systems Conference, pp. 9-16, 2006.
[12] C. Desjardins and B. Chaib-draa, "Cooperative Adaptive Cruise Control: A Reinforcement Learning Approach," IEEE Transactions on Intelligent Transportation Systems, vol. 12, pp. 1248-1260, 2011.
[13] P. Alexander, David Haley, and Alex Grant, "Cooperative intelligent Transport Systems:5.9-GHz Field Trials " Proceedings of the IEEE, vol. 99, pp. 1213-1235, 2011.
[14] F. Yan, M. Dridi, and A. E. Moudni, "A scheduling approach for autonomous vehicle sequencing problem at multi-intersections," International Journal of Operations Research, vol. 9, pp. 57-68, 2011.
[15] J. Lee, and Byungkyu Park, "Development and Evaluation of a Cooperative Vehicle Intersection Control Algorithm Under the Connected Vehicles Environment," Intelligent Transportation Systems, IEEE Transactions, vol. 13, pp. 81-90, 2012.
[16] J. Görmer, J. F. Ehmke, M. Fiosins, D. Schmidt, H. Schumacher, and H. Tchouankem, "Decision Support for Dynamic City Traffic Management using Vehicular Communication," in SIMULTECH, 2011, pp. 327-332.
[17] I. H. Zohdy and H. A. Rakha, "Intersection Management via Vehicle Connectivity: The Intersection Cooperative Adaptive Cruise Control System Concept," Journal of Intelligent Transportation Systems, p. 140221073756009, 2014.
[18] I. H. Zohdy and H. Rakha, "Game Theory Algorithm for Intersection-based Cooperative Adaptive Cruise Control (CACC) Systems," Intelligent Transportation Systems (ITSC), 2012 15th International IEEE Conference pp. 1097-1102, 2012.
[19] Binga, G. W. Y. M. W., and W. Chunxiangb, "Game theory based cooperative driving algorithm for intersection," Journal of Huazhong University of Science and Technology (Natural Science Edition), 2011.
[20] S. R. Azimi, G. Bhatia, R. Rajkumar, and P. Mudalige, "Vehicular Networks for Collision Avoidance at Intersections," in SAE 2011 world congress and exhibition, 2011.

[^0]:    * Resrach supported by the National Basic Research Program of China (2012CB725404).
    Guangquan Lu, is with 1.School of Transportation Science and Engineering, Beihang University, Beijing 100191, China;2.Jiangsu Province Collaborative Innovation Center of Modern Urban Traffic Technologies SiPaiLou \#2, Nanjing,210096,China(Corresponding Author. Phone+86-10-82316330;fax+86-10-82316330;
    e-mail:lugq@buaa.edu.cn).
    Lumiao Li, is with 1.School of Transportation Science and Engineering, Beihang University, Beijing 100191, China;2.Jiangsu Province Collaborative Innovation Center of Modern Urban Traffic Technologies SiPaiLou \#2, Nanjing,210096,China(e-mail:ailsa.miao@163.com).
    Yunpeng Wang, is with 1.School of Transportation Science and Engineering, Beihang University, Beijing 100191, China;2.Jiangsu Province Collaborative Innovation Center of Modern Urban Traffic Technologies SiPaiLou \#2, Nanjing, 210096, China (e-mail:ypwang@buaa.edu.cn).
    Ran Zhang, is with 1.School of Transportation Science and Engineering, Beihang University, Beijing 100191, China;2.Jiangsu Province Collaborative Innovation Center of Modern Urban Traffic Technologies SiPaiLou \#2, Nanjing,210096,China(e-mail: zhangran371303@126.com)
    Zewen Bao, is with 1.School of Transportation Science and Engineering, Beihang University, Beijing 100191, China;2.Jiangsu Province Collaborative Innovation Center of Modern Urban Traffic Technologies SiPaiLou \#2, Nanjing,210096,China(bobpaul@126.com)
    Haichong Chen, is with 1.School of Transportation Science and Engineering, Beihang University, Beijing 100191, China;2.Jiangsu Province Collaborative Innovation Center of Modern Urban Traffic Technologies SiPaiLou \#2, Nanjing,210096,China(e-mail: chenhc570@gmail.com)

