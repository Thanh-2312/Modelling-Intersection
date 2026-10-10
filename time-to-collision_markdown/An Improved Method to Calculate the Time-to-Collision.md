# An Improved Method to Calculate the Time-to-Collision of Two Vehicles 

Felipe Jiménez • José Eugenio Naranjo • Fernando García

Published online: 28 November 2012
© Springer Science+Business Media New York 2012


#### Abstract

In order to improve vehicle safety, a interaction phase between primary and secondary safety systems has been defined. These systems use information provided by the primary safety systems to achieve both the primary and the secondary systems' objectives. It is essential to discriminate whether a collision is avoidable or not and to calculate the time available before the crash happens. This paper shows a method that improves on other simplified methods to calculate the time-to-collision (TTC) to provide a more accurate result that could be used in a collision avoidance system.


Keywords Time-to-collision • Time-to-avoidance • Pre-crash • Laser

## 1 Introduction

Traffic accident data have shown a clear reduction during recent years. This reduction is being achieved by the introduction of measures that affect all areas of road

[^0]transport: infrastructure, vehicle and driver [1]. Perhaps, where these advances are most evident is in the vehiclerelated area where numerous safety systems have been introduced. It is estimated that 90 \% of accidents are caused by human error, mainly due to distractions, misjudgement or lack of knowledge of the situation [2]. Thus, systems are being introduced to help to improve drivers' perception of the environment, and systems that process information and alert the driver to potential hazards and even act if necessary.

We can distinguish primary safety systems which are designed to avoid accidents, and secondary safety systems that attempt to reduce the consequences of such accidents. Primary safety systems provide the vehicle with intelligent systems able to predict and prevent accidents that the driver alone could not control. Different studies show that the potential offered by primary systems is much higher than that of secondary systems, while part of the margin for improvement of these secondary systems is prepared to use the information captured by specific sensors of the primary safety systems. The incorporation of advanced technologies in vehicles has improved the protection afforded to vehicle occupants and pedestrians and reduced road accidents in the last decade despite the huge increase in the vehicle fleet and in mobility. In order to improve integrated safety models of road vehicles, a phase of interaction between primary and secondary safety systems has been defined (Fig. 1) [3]. Therefore, there is also a group of safety systems, that is, pre-collision systems, overlapping the previous ones, as they reuse the information provided by the primary systems to achieve both the primary and secondary safety systems' objectives. These systems use information captured by the sensors so that they can act on the control and protection systems in order to reduce the probability and consequences of the accident. They allow taking measures some seconds in advance, allowing new measures and/or

Fig. 1 Integrated safety model [3]
![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-2.jpg?height=792&width=1279&top_left_y=182&top_left_x=618)

increasing their effectiveness. Some of the actions are automatic braking, automatic action on the steering system to improve the angle of impact, pre-tensioner activation, preparation of airbags and measures to improve the compatibility between vehicles such as extendable bumpers, suspension height control, etc., or the deployment of measures to minimize the effects of pedestrian accidents.

Several projects have been developed that have tested pre-collision systems. Specifically, for example, the PRE-VENT Integrated Project [4] can be mentioned within the Sixth Framework Program, which includes several subprojects in which data fusion is considered to represent the environment so that action can be taken before the collision or preparations made for it. Intensive review work has been carried out in the WG19 of the EEVC (European Enhanced Vehicle-safety Committee) [5].

The evaluation of the effectiveness and possible limitations of pre-collision systems has been studied in several projects such as the European project, ASSESS [6]. This project aims to develop evaluation procedures. These procedures will be performed to evaluate the driver, the behaviour of the pre-collision system, and the socio-economic assessment. The main objectives are to develop standardized assessment procedures aimed at the frontal pre-crash systems. These systems detect hazardous situations and trigger primary and secondary safety systems before an unavoidable accident happens. Assessment tools provide recommendations to facilitate the implementation of the most important technologies and identify barriers that introduce integrated safety systems. With early action, the effectiveness of secondary safety systems can be increased by 10 \% [7] and, moreover, it is estimated that nowadays only 50 \% of the potential of primary safety systems has been utilized. It should be kept in mind that, if about half a second more is available, 60 \% of accidents could be avoided and if you have 1 s, this figure would reach 90 \%. According to this, and bearing in mind that in 2 thirds of the accidents there is a longer time between the triggering event and the impact, it is clearly possible to take action. In [8], the authors examined the effects of pre-collision systems in 50 accident scenarios. Actions to be considered are: audible, visual and haptic warnings that apply tension to the seatbelts and pressure to the brakes automatically in the event of the system detecting a collision. Various studies show that the system could have prevented 38 \% of accidents, with a reduction of 44 \% in the probability of having fatal results. Another study by Daimler Chrysler and Mercedes [9] suggests reductions of 30-50 \% in head injuries and 20-40 \% in neck injuries.

The pre-collision systems seek benefits such as reducing the number of accidents and their severity, responding to risk situations and adapting safety measures to the vehicle's occupants and characteristics of the collision. However, it is necessary to develop sensors and algorithms for detecting an imminent collision [10], estimating the time until it happens, and finally deciding when it becomes unavoidable. The advance warning allows us to adopt measures that otherwise would not be possible or would not be so effective. One key aspect in these systems is the decision whether a collision is unavoidable or not, as it conditions the type of action the vehicle should take automatically (reversible or irreversible steps). To this end, from real-time analysis of the situation, the system should calculate the TTC (Time-To-Collision) and compare with the TTA (Time-To-Avoidance). Other information of interest is the relative velocity of impact, the probability of it, its location, characteristics of mass and stiffness of the obstacle and its identification [5]. These requirements determine the specifications of the sensors and often involve data fusion to obtain robust and reliable
results. This work is within the field of calculating the time remaining before the collision and improving the algorithms proposed in previous works.

## 2 Simplified Calculation of TTC

In [11], a procedure to calculate the time-to-collision between two vehicles is presented. Data that are considered are the initial positions of the vehicles, their speeds and directions, together with the assumption that the vehicles are two ideal points (Fig. 2). Then, the data calculate the intersection of the two vehicles, given by the following expressions:

$$
x_{+}=\frac{\left(y_{2}-y_{1}\right)-\left(x_{2} \cdot \tan \theta_{2}-x_{1} \cdot \tan \theta_{1}\right)}{\tan \theta_{1}-\tan \theta_{2}}
$$

$$
y_{+}=\frac{\left(x_{2}-x_{1}\right)-\left(y_{2} \cdot \cot \theta_{2}-y_{1} \cdot \cot \theta_{1}\right)}{\cot \theta_{1}-\cot \theta_{2}}
$$

Once the intersection point has been found, a procedure is established to calculate the collision time, which consists in calculating the time it takes each of the two vehicles to reach the intersection. When these two times coincide, that is the time-to-collision (TTC). In order to take into account a safety margin that compensates the simplifications made, a

![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-3.jpg?height=970&width=833&top_left_y=1455&top_left_x=174)
Fig. 2 Simplified diagram for the calculation of the intersection point

factor $\delta$ is considered, setting the following relationship to consider collision:

$$
|T X 1-T X 2|<\delta
$$

where the terms TX1 and TX2 are the times vehicles 1 and 2 take to reach the intersection point. The $\delta$ factor is the safety parameter. Therefore, for considering that a collision has occurred TX1=TX2 is not required, but a less strict compliance with the previous relationship. The higher the $\delta$ value is, the more conservative the algorithm becomes.

## 3 Improved Calculation of TTC

The above procedure is simple but the results may become very dependent on the $\delta$ parameter. Thus, using the previous methodology, this paper presents the calculation, but by assuming the vehicle geometry to be rectangular, which, although not accurate, is a much greater approximation to reality.

When two vehicles crash, it can be seen that the corner of one of them is the first area that comes into contact. This fact leads to what we call normal collision configurations. This always happens unless the collision is perfectly parallel or perfectly perpendicular (Fig. 3). In this case, both the corner and the rest of the side contacts with the other vehicle at the same time, but we can assume that a corner always strikes first for the calculation of collision times. Another special case arises when both vehicles hit each other on a corner, but this does not need to be dealt with specifically.

In the general case, there are 32 possible situations, as each corner of each vehicle (4 corners) can impact on any of the 4 sides of the other vehicle and this calculation must be repeated with both vehicles. However, only 10 accident configurations are possible. Two possible initial configurations can be distinguished taking into account the angle $\alpha$

![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-3.jpg?height=590&width=835&top_left_y=1833&top_left_x=1060)
Fig. 3 Collision configurations

between the motion vectors of both vehicles: $\alpha<90^{\circ}$ and $\alpha>90^{\circ}$ (Fig. 4).

### 3.1 Accident Configurations When $\alpha<90^{\circ}$

In this situation, 6 possible configurations are identified. Table 1 illustrates them, including the time conditions that should be satisfied in each one and which configuration could take place if those time conditions are not satisfied. It should be noted that in 3 of the configurations vehicle 2 hits vehicle 1 and, in the other 3, vehicle 1 is the one that hits the other. Figure 5 shows the evolution of the crash point.

### 3.2 Accident Configurations When $\alpha>90^{\circ}$

In this situation, 4 possible configurations are identified. Table 2 illustrates them. It should be noted that in one of the configurations vehicle 2 hits vehicle 1 and, in another, vehicle 1 hits the other. In the other two configurations both vehicles crash but it is not possible to say which one hits the other. Figure 6 shows the evolution of the crash point.

### 3.3 Justification of Time Conditions and TTC Calculation

### 3.3.1 Case 1: The Corner of a Vehicle Hits the Side of Another Vehicle

When a corner of a vehicle hits the side of the other vehicle (cases A, D, G and J), the crash point is located on one of the intersections of the prolongation lines of the sides of the vehicles. For example, in configuration A), the corner of vehicle 2, defined by point A2 hits the side C1D1 of vehicle 1. If the collision happens between the corner of vehicle 2 and the side of vehicle 1, the intersection point should be Q1. Two conditions must be met:

a) The corner A2 should reach Q1 (TA21) later than D1 (TD11).
b) The time A2 takes to reach the intersection Q1 (TA21) must be less than or equal to what C1 takes to get to Q1 (TC11) because, if C1 arrives before, vehicle 1 has passed by the intersection point and therefore there is no impact on A2.

So, if $\mathrm{TTC} 1 \geq \mathrm{TTA} 2 \geq \mathrm{TTD} 1$, a collision occurs and TTC is given by the time the corner takes to reach the intersection point, that is, TTC=TA21.

### 3.3.2 Case 2: The Corner of a Vehicle Hits the Front or the Rear Part of the Other Vehicle

When a corner hits the front or the rear part of the other vehicle, the crash point location is a priori unknown. For example, to illustrate this situation, we can consider configuration I). The collision takes place somewhere on the line between Q1 and Q2. For such a collision to occur, two conditions must be met:

a) Point A2 must reach Q1 (TA21) before point D1 (TD11). If D1 arrives before, the collision would not occur on the front of vehicle 1.
b) Point A2 must reach Q2 (TA22) later than A1 (TA12).

The calculation of TTC is more complicated than in the previous case because the collision point is not known. We call s the position along the line where the collision will take place (Q1-Q2, for example) and its length is denoted by D. It should be analyzed how the corner moves along that segment and how the other vehicle is entering that segment (more specifically, how the last point of the area of the other vehicle where the crash occurs evolves). In this respect, two situations can be distinguished:

a) When $\alpha<90^{\circ}$, both the corner and the last point of the other vehicle that enters the segment moves in the same direction. Furthermore, the order of the 4 time spots involved is unequivocally specified in the time conditions, as can be seen in Table 1 where the order T1>T2 >T3>T4 has been established..

Fig. 4 Initial configurations ( $\alpha<90^{\circ} ; \alpha>90^{\circ}$ )
![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-4.jpg?height=577&width=1286&top_left_y=1908&top_left_x=614)

Table 1 Accident configurations when $\alpha<90^{\circ}$
|  | Situation | Diagram | Time conditions (Situation in the event the condition is not satisfied) | TTC |
| :--- | :--- | :--- | :--- | :--- |
| A) | Corner Vehicle 2 hits side Vehicle 1 | A) | TC11 > TA21 > TD11 <br>  B  D  | TA21 |
| B) | Front part Vehicle 2 hits corner Vehicle 1 | в) | TC13 > TD23 > TA21 > TC11 <br>  C  *  A  | (TA21, TD23) |
| C) | Corner Vehicle 2 hits rear part Vehicle 1 | c) | TB14 > TD24 > TD23 > TC13 <br>  X  *  B  | (TD23, TD24) |
| D) | Corner Vehicle 1 hits side Vehicle 1 | D) | TB21 > TD11 > TA21 <br>  E  A  | TD11 |
| E) | Front part Vehicle 1 hits corner Vehicle 2 | E) | TB22 > TA12 > TD11 > TB21 <br>  F  *  D  | (TD11, TA12) |
| F) | Corner Vehicle 1 hits rear part Vehicle 2 |  | TC24 > TA14 > TA12 > TB22 <br>  X  *  E  | (TA12, TA14) |


*=Always occurs X=No accident

b) When $\alpha>90^{\circ}$, the points move in opposite directions. In this case, the order of the 4 time spots involved is not completely specified in the time conditions and it is not possible to know a priori the order (T1, T2, T3, T4), because some of the relationships depend on each particular case. For example, in configuration I), it is not possible to establish whether TA12 is lower or higher than TA21, and the same occurs with TA22 and TD11, and varies depending on the situation.

Figure 7 shows the situation of the first case. Taking configuration B) as an example, TTC can be calculated as the intersection between the 2 lines:

- Line 1: C1 comes into the section Q1-Q3 $(\mathrm{s}=0)$ at TC11 (T4) and leaves that section $(\mathrm{s}=\mathrm{D})$ at TC13 (T1).
- Line 2: The intersection between the front part of vehicle 2 and the line Q1-Q3 begins at $\mathrm{s}=0$ at TA21 (T3) and reaches s=D at TD23 (T2)

The time-to-collision, TTC, can be calculated by the following equation:

$$
T T C=\frac{T 1 T 3-T 2 T 4}{T 1+T 3-T 2-T 4}
$$

Figure 8 shows the situation of the second case. In configuration I), point A2 is evolving along the crash segment and the front of vehicle 1 from the other side. TTC can be calculated as the intersection between the following 2 lines:

- Line 1: A2 comes into the segment $(\mathrm{s}=0)$ at TA21, and comes out of the section (s=D) at TA22.

![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=625&width=839&top_left_y=187&top_left_x=172)
Fig. 5 Crash point location

- Line 2: The intersection between the front part of vehicle 1 and the line Q1-Q3 begins at $\mathrm{s}=\mathrm{D}$ at TA12 and reaches $\mathrm{s}=0$ at TD11.

Depending on the order between TA12 and TA21, and TA22 and TD11, the two cases shown in Fig. 8 can occur. The intersection that provides TTC is comprised between $\mathrm{T} 3=\max (\mathrm{TA} 21, \mathrm{TA} 12)$ and $\mathrm{T} 2=\min (\mathrm{TD} 11, \mathrm{TA} 22)$. In both cases, the time-to-collision, TTC, can be calculated by the following equation:

$$
T T C=\frac{T 1 T 2-T 3 T 4}{T 1+T 2-T 3-T 4}
$$

In the event of a vehicle not having a uniform motion, the lines in Figs. 7 and 8 become curves. Then, Eqs. (4) and (5) are not valid but the calculation method does not change and intersection of both curves should be found using analytical (when possible) or numerical solution methods. In case the trajectory changes, numerical methods should be used.

## 4 Collision Avoidance System

The algorithm is oriented to be implemented in a collision avoidance system. This system is composed of 4 main parts:

- Vehicle positioning (GPS receiver) and kinematical variables measurement (vehicle CAN bus)
- Obstacles detection subsystem that can be based on radar, laser-scanner or computer vision, among other technologies, or a combination of some of them using

Table 2 Accident configurations when $\alpha>90^{\circ}$
|  | Situation | Diagram | Time conditions (Situation in the event the condition is not satisfied) | TTC |
| :--- | :--- | :--- | :--- | :--- |
| G) | Corner Vehicle 2 hits side Vehicle 1 | ![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=176&width=271&top_left_y=1416&top_left_x=544) | ![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=77&width=556&top_left_y=1493&top_left_x=904) | TD23 |
|  | Corner Vehicle 1 hits front part Vehicle 2 | ![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=223&width=269&top_left_y=1692&top_left_x=548) | ![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=77&width=300&top_left_y=1649&top_left_x=846)![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=77&width=307&top_left_y=1649&top_left_x=1187)![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=77&width=302&top_left_y=1752&top_left_x=1028)![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=75&width=305&top_left_y=1856&top_left_x=1028) |  |
|  | Corner Vehicle 2 hits front part Vehicle 1 |  | ![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=27&width=27&top_left_y=1968&top_left_x=548)![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=80&width=184&top_left_y=1929&top_left_x=846)![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=78&width=303&top_left_y=2030&top_left_x=1028)![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=75&width=303&top_left_y=2133&top_left_x=1030) |  |
| J) | Corner Vehicle 1 hits side Vehicle 2 |  | ![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=26&width=29&top_left_y=2227&top_left_x=550)![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-6.jpg?height=77&width=554&top_left_y=2289&top_left_x=904) | TA12 |


[^1]![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-7.jpg?height=524&width=828&top_left_y=185&top_left_x=176)
Fig. 6 Crash point location

sensor fusion techniques [12-14]. This subsystem involves also obstacles detection and tracking algorithms [10].

- Decision module, in which movement of the vehicle and the obstacles are estimated, TTC is calculated and the system decides the most appropriate warning or manoeuvres. This decision is commonly based on artificial intelligence tools.
- Warning and autonomous action modules that perform the decisions of the previous module. This subsystem involves automation of gas and brake pedals and the steering wheel [15].

## 5 Practical Example

In order to show the improvements provided by the proposed method here is an example of a configuration of a simple scenario. It represents a possible collision between two vehicles in a crossing of perpendicular roads. Both vehicles are located 10 m apart from the central point of the crossing. Dimensions of vehicles are supposed to be $2 \times 5 \mathrm{~m}$. Vehicle 1 speed is 19 m/s and we consider two cases of initial speeds for vehicle 2: 20 m/s (scenario 1) and 25 m/s (scenario 2).

![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-7.jpg?height=543&width=841&top_left_y=1884&top_left_x=170)
Fig. 7 Scheme for the calculation of crash point and TTC ( $\alpha<90^{\circ}$ )

![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-7.jpg?height=537&width=839&top_left_y=187&top_left_x=1056)
Fig. 8 Scheme for the calculation of crash point and TTC ( $\alpha>90^{\circ}$ )

Following the method of [11], in both scenarios, the intersection should occur at the central point of the crossing if it really happens. Then, the time both vehicles take to reach that point is calculated.

In scenario $1, \mathrm{TX} 1=0.526 \mathrm{~s}$ and $\mathrm{TX} 2=0.5 \mathrm{~s}$ and, considering Eq. (3), the algorithm concludes that for $\delta$ values lower than $0.526-0.5=0.026 \mathrm{~s}$, it is assumed that there is no collision. However, the second method shows that a collision occurs because, if configuration A) is identified:

- $\mathrm{TC} 11=14 / 20=0.7 \mathrm{~s}$
- TA21 $=9 / 19=0.47 \mathrm{~s}$
- $\mathrm{TD} 11=9 / 20=0.45 \mathrm{~s}$

so the condition $\mathrm{TC} 11 \geq \mathrm{TA} 21 \geq \mathrm{TD} 11$ is met, and this fact means that a collision occurs. .

In the second scenario, it can be checked with proposed method that there is no collision because, when a vehicle arrives, the other has passed the interference area (the time it takes the point C1 to leave the intersection area TC11= 0.44 s is lower than it takes for the vehicle 2 to reach the intersection area $\mathrm{TA} 21=0.47 \mathrm{~s}$ ). However, in the simplified method, $\mathrm{TX} 1=0.526 \mathrm{~s}$ and $\mathrm{TX} 2=0.4 \mathrm{~s}$. Then, $\delta$ values greater than $0.526-0.4=0.126 \mathrm{~s}$ will make that the method considers that a collision occurs when in fact it does not happen.

As we can see, the simplified method is very sensitive to the tolerance value and this fact could lead to erroneous decision on whether a collision may occur or not. The proposed method overcomes this limitation and more reliable results are obtained.

## 6 Conclusions

This article has presented a more accurate calculation of the time-to-collision between two vehicles colliding at constant speed along a straight path without excessive computational cost. Moreover, the proposed method is easily generalized to
the case of curved paths (if the analytical expression is known) and it is not mandatory for the vehicle movement to be uniform and it is possible to estimate the braking motion that the system could even do automatically if it is deemed necessary to avoid collision. In general, the vehicles movement changes constantly. In this case, speed and acceleration of the vehicle with the collision avoidance system are measured and kinematical variables of the obstacles are estimated taking into account the object tracking process. Then, Time-to-collision is recalculated in real time at every moment assuming that these variables will remain constant and evolution of TTC is obtained. Continuous calculation considering uniform or uniformly accelerated motion should provide good results under normal driving conditions.

The results provided by this algorithm improve on the ones presented in [11] because they do not depend on the $\delta$ value, which could lead to false positives or false negatives, which are decrease driver confidence on the warning system and are not admissible when the system performs automatic actions to avoid collisions. .

Obviously, uncertainties in obstacles detection and estimation of their kinematical variables could make the proposed algorithm results inaccurate. This fact conditions the sensor used in the pre-crash system and the algorithms to identify obstacles because reliability of these data is essential for the correct estimation of the available time before the collision occurs and for the correct decision making of the most appropriate manoeuvre to avoid it or reduce its consequences.

Acknowledgments The work reported in this paper has been partly funded by the Spanish Ministry of Science and Innovation (SAMPLER project TRA2010-20225-C03-01 and TRA2010-20225-C03-03; and IVANET project TRA 2010-15645).

## References

1. Elvik, R., Vaa, T.: The handbook of road safety measures. Elsevier, UK (2004)
2. Hobbs, F.D.: Traffic planning and engineering. Pergamon Press, Oxford (1989)
3. Aparicio, F., Arenas, B., Gómez, A., Jiménez, F., López, J.M., Martínez, L., Páez, F.J.: Ingeniería del Transporte. Dossat, Madrid (2008). in Spanish
4. Project PREVENT http://www.prevent-ip.org/ (accessed on February 2011)
5. EEVC WG 19. Primary and secondary safety interaction. EEVC (2004)
6. Project ASSESS: http://www.assess-project.eu/ (accessed on February 2011)
7. Baumann, K.-H., Schöneburg, R., Justen, R. The vision of a comprehensive safety concept. 17th International Technical Conference on the Enhanced Safety of Vehicles. Amsterdam, 4-7 June 2001 (2001)
8. Sugimoto, Y., Sauer, C. Effectiveness estimation method for advanced driver assistance system and its application to collision mitigation brake system. Proceedings of the 19th International Technical Conference on the Enhanced Safety of Vehicles. Washington, DC. June 6-9, 2005 (2005)
9. Schoeneburg, R., Breitling, T. Enhancement of active and passive safety by future Pre-Safe systems. Proceedings - 19th International Technical Conference on the Enhanced Safety of Vehicles, Washington, D.C., June 6-9, 2005 (2005)
10. Jiménez, F., Naranjo, J.E.: Improving the obstacle detection and identification algorithms of a laserscanner-based collision avoidance system. Transp. Res. Part C: Emerg. Technol. 19(4), 658-672 (2011)
11. Miller, R., Huang, Q. An adaptive peer-to-peer collision warning system. IEEE Veh. Technol. Conf. (2002)
12. Caraffi, C., Cattani, S., Grisleri, P.: Off-road path and obstacle detection using decision networks and stereo vision. IEEE Trans. Intell. Transp. Syst. 8(4), 607-618 (2007)
13. Polychronopoulos, A., Tsogas, M., Amditis, A.J., Andreone, L.: Sensor fusion for predicting vehicles. Path for collision avoidance systems. IEEE Trans. Intell. Transp. Syst. 8(3), 549-562 (2007)
14. Guivant, J., Nebot, E., Baiker, S.: Autonomous navigation and map building using laser range sensors in outdoor applications. J. Robot. Syst. 17(10), 565-583 (2000)
15. Naranjo, J.E., Jiménez, F., Gómez, O., Zato, J.G.: Low level control layer definition for autonomous vehicles based on fuzzy logic. Intell. Autom. Soft Comput. 18(4), 333-348 (2012)

![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-8.jpg?height=479&width=391&top_left_y=1470&top_left_x=1060)
Felipe Jiménez obtained his Master's Degree in Industrial Engineering from the Technical University of Madrid (UPM), his Master's Degree in Physical Science from the UNED and his PhD in Mechanical Engineering from the UPM in 2001, 2005 and 2006, respectively. Currently, he is Associate Professor at the UPM and Head of the Intelligent Systems Unit of the University Institute for Automobile Research of the UPM.

He has been involved in several research projects and has developed engineering studies for relevant national firms. His fields of interest are the automotive industry, vehicle safety, mechanical design, driver assistance systems and intelligent transport systems. He is the author of several papers in relevant scientific journals and has participated in several national and international congresses.
![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-9.jpg?height=472&width=388&top_left_y=219&top_left_x=176)

José E. Naranjo was born in Orense, Spain in 1975. He received his BEng. and MEng. degree in Computer Science Engineering from the Technical University of Madrid (UPM) in 1998 and 2001 respectively. He was awarded a PhD in Computer Science from the UPM in 2005. He obtained a position as associate professor in the School of Computer Science of the UPM in 2007.

Fernando García is associated
![](https://cdn.mathpix.com/cropped/6e83ee87-a3eb-460f-ac11-316816e106ba-9.jpg?height=459&width=378&top_left_y=230&top_left_x=1060)
professor at Carlos III University of Madrid where he is also a PhD student. He received his Graduate degree in Telecommunication Engineering at this university in 2006 and his Master's Degree in Robotics and Automatics in 2009. He started his research activities in 2007 joining the Intelligent System Lab where he performs his research activities in the field of Intelligent Transport Systems, focusing on sensors and data fusion applications.


[^0]:    F. Jiménez ()
    INSIA, Technical University of Madrid, Campus Sur UPM. Carretera de Valencia km 7, 28031 Madrid, Spain
    e-mail: felipe.jimenez@upm.es
    J. E. Naranjo
    EUI, Technical University of Madrid, Campus Sur UPM. Carretera de Valencia km 7, 28031 Madrid, Spain
    e-mail: joseeugenio.naranjo@upm.es
    F. García
    University Carlos III of Madrid, Avda. de la Universidad 30, 28911 Leganés, Madrid, Spain
    e-mail: fegarcia@ing.uc3m.es

[^1]:    *=Always occurs X=No accident

