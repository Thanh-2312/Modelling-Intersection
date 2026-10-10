# A Differential Evolution Algorithm-Based Traffic Control Model for Signalized Intersections 

Ziya Cakici ${ }^{\mathbf{1}}$ and Yetis Sazi Murat ${ }^{\mathbf{2}}$<br>${ }^{1}$ Department of Civil Engineering, Faculty of Engineering, Bayburt University, Bayburt, P.O. Box 69000, Turkey<br>${ }^{2}$ Department of Civil Engineering, Faculty of Engineering, Pamukkale University, Denizli, P.O. Box 20160, Turkey<br>Correspondence should be addressed to Ziya Cakici; ziyacakici@bayburt.edu.tr

Received 28 June 2019; Revised 10 November 2019; Accepted 3 December 2019; Published 21 December 2019
Academic Editor: Zahid Hossain
Copyright © 2019 Ziya Cakici and Yetis Sazi Murat. This is an open access article distributed under the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

Sustainable management of traffic flows at signalized intersections is an important issue in terms of traffic engineering. The minimization of lost time, emission, fuel consumption, etc., can be achieved by optimization-based intersection management. In this study, a new traffic signal control model is developed for the management of three-leg signalized intersections. In the proposed model, signal timing and signal phasing are optimized simultaneously using Differential Evolution (DE) algorithm which is one of the population-based metaheuristic algorithms. The effectiveness of the model is tested on sample traffic scenarios with VISSIM simulation software considering average vehicle delay performance criteria. Results show that the proposed approach may reduce the average vehicle delay between the rates of $28 \%-42 \%$ and $3 \%-38 \%$ comparing to the optimum fixed-time signal control and vehicle-actuated signal control for tested scenarios, respectively.

## 1. Introduction

In recent years, mobility demands of people have increased considerably with economic and technological improvements in the world. However, travel demand has caused an increase in both car ownership and the number of vehicle per capita [1]. With this increment at the number of motorized vehicles, a significant part of existing road networks has been inadequate day by day, and traffic congestion problems have been overwhelmingly increased. Although some decision makers prefer to build a new road network as a solution, it may not be a reasonable choice for many cases. Thus, the efficient use of existing capacity may be preferred as a sustainable solution for the traffic congestion problem [2-4].

Capacity and safety problems generally appear at signalized intersections which are the critical zones of urban and rural road networks. Besides, fuel consumption, loss of time, exhaust emission, and noise pollution are at a high level in these areas [5]. Hence, the proper and sustainable management of traffic flows at signalized intersections requires experience and wide knowledge about traffic engineering. Insufficient analysis in the stages of phase plan selection and signal timing assignment causes excessive delays [6]. Determination of most proper cycle time, signal phase plan, and green splits for signalization systems is a quite important issue for efficient management of traffic flows at signalized intersections.

Signalized intersections can be managed in two different ways as isolated or coordinated. Isolated systems are not affected by other signalization systems that are located nearby. Types of management for isolated signalization systems can be classified into three different ways as fixedtime, vehicle-actuated, and adaptive management, respectively. For fixed-time management, assignment of signal timings and selection of phase plan are determined considering historical traffic data. The order of phases and green splits for each phase are fixed at all cycles. The order of phases and green splits are not changed according to fluctuations in traffic demand. In vehicle-actuated management, the system adapts to the fluctuations in traffic demands. Information related to traffic demand is obtained with
detectors. Green splits are extended or ended based on existing traffic demands using vehicle queuing information at intersection approaches [7, 8]. For adaptive management, signal timings (green splits and cycle time) are periodically optimized depending on the traffic demands at intersection approaches. Signal parameters are updated according to traffic demands and fluctuations. Traffic flows are continuously monitored, and as a result of this monitoring, signal timings are determined depending on the obtained data.

Adaptive management systems such as SCATS and SCOOT are used in many countries. Significant improvements for the performances of intersections can be achieved using these systems. The optimization process of adaptive management systems includes the assignment of signal timing plans based on real-time data and predictions that can be repeated in every 5 or 10 minutes. However, for the prediction process, if the period is more than 10 minutes, transition failure for new signal timings may occur [9]. Many studies in the literature also indicate that adaptive management systems are more successful and superior than other traffic management systems [10]. Some of them can be summarized as follows.

Mirchandani and Head [11] studied an adaptive management system which is named as RHODES. They revealed that average vehicle delays may be decreased by about 50\% for low traffic demand conditions and it may be decreased by about 30\% for high demand conditions comparing to semiactuated traffic management. Li and Prevedouros [12] developed an adaptive management approach which is called as TACOS for oversaturated intersections, as well as signal timings, phase sequences of the signalization system were also optimized in their model. They compared TACOS with the fixed-time and vehicle-actuated management systems. They concluded that remarkable improvements can be obtained with TACOS. Lee et al. [13] also focused on adaptive traffic signal control regarding the genetic algorithm in the optimization process. The algorithm was tested using microsimulation. As a result, they implicated that the real-time management system which is based on the genetic algorithm has higher performance than optimum fixed-time management. Shoufeng et al. [14] aimed to test the performance of the Q-Learning algorithm for adaptive traffic management. Obtained results by Q-Learning algorithm were compared with the results of fixed-time management. It was seen that average vehicle delays may be reduced using the Q-Learning algorithm especially when traffic fluctuations occur. Singh et al. [15] developed an adaptive traffic management system which is based on a genetic algorithm. They compared the adaptive system with the fixed-time traffic management system. Hence, the superiority of the adaptive traffic management system was proved once again. Zheng et al. [16] studied a real-time adaptive management model which aims to provide adaptive functionality of actuated systems. Thus, they improved the performance of the vehicle-actuated system. Obtained results showed that realtime adaptive management model is quite successful for improving the performance of intersection. Angulo et al. [17] presented an application of different computing techniques for adaptive traffic management. The model developed was compared with nonadaptive static and dynamic management. In the research, it was seen that total travel time can be significantly reduced with adaptive management. Samadi et al. [18] evaluated the SCATS adaptive traffic management system in Mashhad, Iran. In their study, the performance of the vehicle-actuated management system was compared with the performance of the SCATS adaptive traffic management system. As a result, it was pointed out that as well as average vehicle delays, air pollution and fuel consumption can also be reduced with the SCATS adaptive traffic management system. McKenney and White [19] developed an adaptive traffic management system which is based on traffic observation performed with traffic sensor devices and local interactions between traffic signals. Effectiveness of the developed system was tested using traffic data which are obtained from Ottawa, Canada. In this study, it was concluded that when compared with the fixed-time traffic management system, better network performance can be obtained with the adaptive traffic management system. Vilarinho and Tavares [20] proposed a new approach which includes both signal timing optimization and phase plan design. Fairly good results were obtained in unpredictable and unscheduled conditions with the proposed approach. Yulianto and Sutanto [21] designed an adaptive traffic management system considering fuzzy logic for coordinated intersections. The effectiveness of the system was investigated and tested using the VISSIM microsimulation program. Consequently, it was determined that especially when the traffic demand is high, the performance of intersections can be increased with this new system. Koltovska and Bombol [22] studied an adaptive traffic management system which is based on the Q-Learning algorithm for urban-isolated signalized intersections. The system was tested on a real intersection. Obtained results were compared with the results which were obtained from fixed-time and vehicle-actuated management systems. It was seen that best results for different performance measures such as average stop number, average vehicle delay, and total delay were obtained with the adaptive traffic management system. Aljaafreh and Al-Oudat [23] focused on an adaptive traffic management system which aims to optimize both traffic signal timing and phase sequences. On the scope of their study, the modified job scheduling algorithm was used for optimizing phase sequences. According to results, it was seen that the adaptive traffic management system outperforms than fixed-time traffic management. Khalighi [24] developed an adaptive traffic management system which optimizes traffic signal timings by minimizing total vehicle emissions for undersaturated conditions. The proposed management system was compared with the fixed-time management system. At the end of the study, it was concluded that more reduction of total vehicle emissions can be achieved with the adaptive traffic management system. Yu et al. [25] aimed to develop a new traffic signal management system which is based on a fuzzy logic approach. The performance of the proposed management system was compared with the performance of the fixed-time management system using the VISSIM microsimulation program. As a result, it was concluded that average vehicle
delays and stop ratios can be reduced significantly. Castro et al. [26] developed an adaptive (biological neural networkbased) system which can also change the phase control scheme as well as traffic signal timings. The proposed system was evaluated on a three-leg signalized intersection. In this study, it was seen that the capacity of intersection can be increased with an adaptive biological neural network system.

When the previous studies are investigated carefully, it can be seen that phase plan optimization is partially taken into account. But, the flexibility of the phase plan design is not studied and examined sufficiently in previous studies. In this study, different from the previous studies, the flexibility of phase plan design is taken into account. In the scope of the study, a signal timing and signal phasing optimization are aimed for the proper and sustainable management of threeleg signalized intersections using Differential Evolution algorithm. The effectiveness of the proposed model is tested considering different traffic scenarios using the VISSIM microsimulation program.

This paper consists of six parts. In the second part of the study, proposed optimization-based new approach is explained in detail. In the third part of the study, vehicleactuated traffic signal control is presented, and the flowchart for vehicle-actuated management is depicted. In the fourth part of the study, traffic scenarios created for testing the model are described, and the results obtained from the analyses are shown graphically. Results of the study are summarized in the fifth part of the study. Findings obtained from the analyses are evaluated and interpreted in the last part.

## 2. A Signal Timing and Phase Plan Optimization-Based Traffic Management Approach for Three-Leg Signalized Intersections: OPTiMA3

OPTiMA3 is an optimization-based traffic management approach which periodically updates signal timings and phase plan for three-leg signalized intersections. Because both signal timings and phase plan are optimized simultaneously with OPTiMA3, this approach differs from many previous studies in the literature. In this approach, lanebased traffic volumes for the signal timing optimization and conflicts of traffic flows (movements) for the phase plan optimization are considered as determinant factors.
2.1. Intersection Model and Possible Phase Plans. The aim of the phase plan optimization is to provide safe crossing the intersection without wasting the time of more vehicles at a current interval. Thus, it can be pointed out that the traffic flows (movements) at the intersection should be considered and evaluated as movement-based rather than phase-based [27]. Sample phase plan is presented in Figure 1(a). Besides, the movement-based cycle diagram is also described in Figure 1(b).

In the first step of signal timing and phase plan optimization process, a three-leg signalized intersection model (shown in Figure 2) is created. Determination of the most appropriate phase plans for a created model is aimed in the second step. Regarding the safety of vehicles and pedestrians, the interactions of traffic flow with each other are considered in this step. Designed possible phase plans, movements, and the total number of crossing and merging points related to these phase plans are presented in Table 1 in detail.

As can be seen from Figure 2, the movements are numbered ranging from 1 to 8. Here, the numbers 1 and 3 represent right-turning traffic movements. The numbers 2 and 8 represent left-turning traffic movements, and the numbers 4, 5, 6, and 7 represent through traffic movements. To obtain the lane-based traffic volumes, detectors are placed at 75 meters away from and just before the stop lines.

In Table 1, it can be seen that a total of 8 possible different phase plans are created for the three-leg signalized intersection model. The number of crossing for traffic flows is equal to 0 for each possible phase plan. Merging movements include less traffic accident risk than crossing movements. Thus, to determine the effect on average vehicle delay of merging movements, the phase plans that their number of merging movements equal to 1 is also regarded. In Table 1, while the number of merging movements is equal to 1 for 4 possible phase plans (2-3-7-8), the number of merging movements also is equal to 0 for other 4 possible phase plans (1-4-5-6). Movementbased cycle diagrams for created 8 different possible phase plans are presented in Figure 3. As can be seen from Figure 3, each traffic flow has right of way at least for one phase duration at each cycle. This situation is another important issue taken into account at the determination stage of possible phase plans.
2.2. Performance Criteria. Delay is one of the most important criteria used for determining performances and level of services of signalized intersections. Average vehicle delay is taken into account as the performance criteria in the proposed approach. The minimization of average vehicle delay by optimizing signal timing and phase plan is aimed. In the optimization process, delay equations such as Webster, Akcelik, and HCM are analyzed, and the most proper delay equation for OPTiMA3 is determined.

While delay equations of Webster and HCM target the phase-related evaluation of traffic flow, Akcelik's delay equation considers the movement-related evaluation [27]. Since the phase plan is optimized considering movements of traffic flows, in this study, Akcelik's delay equation is used as an objective function of signal timing and phase plan optimization problem. According to Akcelik method, the approximate value of total delay for a movement can be calculated by

$$
D=\frac{q C \times(1-u)^{2}}{2 \times(1-y)}+N_{O} x,
$$

where $D$ is the total delay; $q C$ is the average number of arrivals in vehicles per cycle ( $q=$ flow in per second, $C=$ cycle time in second); $u$ is the green time ratio $(=g / C) ; y$ is the flow ratio $(=q / s) ; s$ is the saturation flow in vehicles per second; $x$ is the degree of saturation; and $N_{O}$ is the average overflow queue in vehicles.

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-04.jpg?height=1610&width=1498&top_left_y=243&top_left_x=291)
Figure 1: (a) The intersection model. (b) Sample phase plan with movement-based cycle diagram.

Overflow queues grow continuously until the average arrival flow rate drops below the capacity, and the queues can be cleared during subsequent signal cycle for oversaturated conditions. According to Akcelik method, average overflow queues for both oversaturated and undersaturated conditions can be predicted by

$$
N_{O}=\left\{\begin{array}{cl}
\frac{Q T_{f}}{4}\left(z+\sqrt{Z^{2} \frac{12\left(x-x_{0}\right)}{Q T_{f}}}\right) & x \geq x_{0} \\
0 & x<x_{0}
\end{array}\right\},
$$

$$
x_{o}=0.67+\frac{s g}{600},
$$

where $N_{O}$ is the average overflow queue in vehicles; $Q$ is the capacity in vehicles in per hour; $T_{f}$ is the flow period; $Q T_{f}$ is the maximum number of vehicles which can be discharged during interval $T_{j} x$ is the degree of saturation $(=q / Q) ; z$ is $x-1$ (note that if $x<1$, it has a negative value); $x_{o}$ is the degree of saturation below which the average overflow queue is approximately zero; $s$ is the saturation flow in vehicles per second; and $g$ is the effective green time in seconds.

Average vehicle delay can be calculated by

$$
d=\frac{D}{q},
$$

where $D$ is the total delay and $q$ is the flow in vehicles per second.

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-05.jpg?height=1011&width=1493&top_left_y=247&top_left_x=295)
Figure 2: A three-leg signalized intersection model.

Table 1: Designed possible phase plans and related movements.
| Plan no. | Movements in Phase I | Movements in Phase II | Movements in Phase III | The number of crossing | The number of merging |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 6-7-8 | 3-4-5 | 1-2 | 0 | 0 |
| 2 | 3-6-7-8 | 3-4-5-6-7 | 1-2-3 | 0 | 1 |
| 3 | 3-6-7-8 | 3-4-5-6-7 | 1-2 | 0 | 1 |
| 4 | 6-7-8 | $3-4-5-6-7$ | 1-2 | 0 | 0 |
| 5 | 3-4-5-6-7 | 6-7-8 | 1-2 | 0 | 0 |
| 6 | 1-6-7-8 | 1-2-3 | 3-4-5 | 0 | 0 |
| 7 | 6-7-8 | 1-3-4-5-6-7 | 1-2-3 | 0 | 1 |
| 8 | 1-6-7-8 | 1-3-4-5-6-7 | 1-2-3 | 0 | 1 |


2.3. Optimization Model. In the development stages of the optimization model, the metaheuristic optimization algorithms are taken into consideration. Metaheuristic optimization algorithms are soft computing methods which are used for the purpose of decision making on the ones that are effective from various alternative movements to achieve any goal [28, 29]. Although exact solutions may not be achieved by using these types of algorithms, near-optimal solutions can be obtained. However, for about last 30 years, these types of algorithms are used as an effective tool for the solution of many engineering problems including civil engineering problems such as the assignment of traffic signal timing, transportation network design, steel construction design, ground-water management, the intensity-duration-frequency relationship determination, and so on [30-32]. Genetic Algorithm (GA), Harmony Search Algorithm (HS), Particle Swarm Optimization Algorithm (PSO), Ant Colony Optimization Algorithm (ACO), Artificial Bee Colony Algorithm (ABC), and Differential Evolution (DE) are some of the most used metaheuristic optimization methods for the solution of the problems. Previous studies in the literature showed that more effective solutions can be achieved by using the Differential Evolution algorithm rather than the other metaheuristic optimization algorithms [33-37]. Thus, it is preferred in this study.

Differential Evolution is a population-based algorithm which is developed by Storn and Price in 1995. When its function and operators are considered, DE is similar to GA. As a small difference, while the variables are represented by binary (0 or 1) values in GA, they are represented by their real values in DE. Besides, crossover and mutation-selection operators in GA are also used in DE [38].

In this study, phase signal timings for created 8 possible phase plans are optimized using DE. In the first step of the optimization process, objective function, decision variables, and the set of constraints relating to the problem are

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-06.jpg?height=1183&width=1198&top_left_y=250&top_left_x=443)
Figure 3: Movement-based cycle diagrams relating to created possible 8 phase plans.

determined. As it has been mentioned before, OPTiMA3 aims minimization of average delay at a three-leg intersection. Thus, minimization of average vehicle delay is considered as the objective function.

Minimization of average vehicle delay can be achieved by proper and reasonable assignment of signal timings. Random assignment of signal timings causes more waste of time. This situation adversely affects the performance of the intersection. Because signal timings are directly effective factors on the performance of a signalized intersection, green signal timings (green splits) for each phase are considered as decision variables. As can be seen from the previous studies, green signal timings for each phase should be within a certain range [39-41]. Average vehicle delays may significantly increase, otherwise. Thus, green signal timings (green splits) for each phase are constrained between 7 seconds and 45 seconds. In addition to this, the degree of saturation value for each lane is constrained with a maximum of 1.2 to investigate the oversaturated traffic conditions. Since the created three-leg signalized intersection model includes a total of 8 lanes, the total number of constraints relating to the degree of saturation is 8. The objective function, decision variables, and the set of constraints which are composed for the optimization problem are presented in Table 2 in detail.

In the second step of the optimization process, an algorithm which optimizes signal timings for created 8 possible phase plans is coded in MATLAB [42] considering objective function, decision variables, and set of constraints which are presented in Table 2. The selection steps of optimum signal timings and phase plan are given in Figure 4.

As can be seen from Figure 4, selection of optimum signal timings and phase plan are actualized in three steps. In the first step, lane-based traffic volumes and lane-based saturation flows which are used for optimization are provided. In the second step, these inputs are transferred to the optimization program which is coded in MATLAB. Then, optimum signal timings and average vehicle delay for each phase plan are obtained. In the last step, the phase plan which provides minimum average vehicle delay is selected, and optimum signal timings for this phase plan are determined. Finally, the selection of the most proper phase plan and signal timings is completed.

In OPTiMA3, phase plan and signal timings are changed periodically considering lane-based traffic volumes and lanebased saturation flows. The improvement of intersection performance is aimed in this way. The flowchart of OPTiMA3 is described in Figure 5.

In Figure 5, it can be seen that the value of $n$ (the intervention period) is not specified clearly. In the

Table 2：The objective function，decision variables，and the set of constraints for the optimization problem．
| Objective function（ $n=$ total number of lanes at intersection） |  | $f=\min \left(d=\sum_{i=1}^{n} D_{i} / \sum_{i=1}^{n} q_{i}\right)$ |
| :--- | :--- | :--- |
| Decision variables | $g_{1}$ | Green signal timing（green split）for Phase I（sec） |
|  | $g_{2}$ | Green signal timing（green split）for Phase II（sec） |
|  | $g_{3}$ | Green signal timing（green split）for Phase III（sec） |
| Set of constraints | $7 \leq g_{1} \leq 45$ <br> $7 \leq g_{2} \leq 45$ <br> $7 \leq g_{3} \leq 45$ <br> $7 \leq g_{3} \leq 45$ |  |
|  |  |  |
|  | $0 \leq\left(q_{1} \times C / g_{a} \times s_{1}\right) \leq 1.2$ | $0 \leq\left(q_{2} \times C / g_{b} \times s_{2}\right) \leq 1.2$ |
|  | $0 \leq\left(q_{3} \times C / g_{c} \times s_{3}\right) \leq 1.2$ | $0 \leq\left(q_{4} \times C / g_{d} \times s_{4}\right) \leq 1.2$ |
|  | $0 \leq\left(q_{5} \times C / g_{e} \times s_{5}\right) \leq 1.2$ | $0 \leq\left(q_{6} \times C / g_{f} \times s_{6}\right) \leq 1.2$ |
|  | $0 \leq\left(q_{7} \times C / g_{h} \times s_{7}\right) \leq 1.2$ | $0 \leq\left(q_{8} \times C / g_{j} \times s_{8}\right) \leq 1.2$ |
|  |  | As a sample：green signal timings（green splits）for one－numbered flow $\left(g_{a}\right)$ |
|  | For plan no．1：$g_{3}$ | For plan no．7：$g_{2}+g_{3}$ |
|  | For plan no．6：$g_{1}+g_{2}$ | For plan no．8：$g_{1}+g_{2}+g_{3}$ |


| Inputs | Optimization （MATLAB） | Plan no． | Optimum green signal timings for possible phase plans |  |  | Average vehicle delay |  | Selected phase plan | Optimum signal timings |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | Phase I | Phase II | Phase III |  |  |  |  |
| Lane－based traffic volumes <br> Lane－based saturation flows | optimum signal timings and average vehicle delay for <br> ![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-07.jpg?height=591&width=28&top_left_y=1208&top_left_x=683) <br> ![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-07.jpg?height=591&width=97&top_left_y=1208&top_left_x=614) |  | $t_{1}$ | $y_{1}$ | $z_{1}$ | $D_{1}$ |  |  |  |
|  |  |  |  |  |  |  |  |  | ![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-07.jpg?height=514&width=33&top_left_y=1251&top_left_x=1636) <br> ～A NAR單拜 <br> 單拜 ிão Ar ó ÄCA A．ABTODEDIDE BODO <br> ÀNADFRATEDTON A A A A En CO MEME A A A A En CO MEME <br> ![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-07.jpg?height=383&width=26&top_left_y=1382&top_left_x=1643) Andwrs．．． |
|  |  |  | $t_{3}$ | $y_{3}$ | $z_{3}$ | $D_{3}$ |  |  |  |
|  |  |  | $t_{4}$ | $y_{4}$ | $z_{4}$ | $D_{4}$ |  |  |  |
|  |  |  | $t_{5}$ | $y_{5}$ | $z_{5}$ | $D_{5}$ |  |  |  |
|  |  |  | $t_{6}$ | $y_{6}$ | $z_{6}$ | $D_{6}$ |  | AMANADED BETEDIANDECT Anding Andwth：dayan |  |
|  |  |  | $t_{7}$ | $y_{7}$ | $z_{7}$ | $D_{7}$ |  |  |  |
|  |  |  | $t_{8}$ | $y_{8}$ | $z_{8}$ | $D_{8}$ |  |  |  |

Figure 4：Selection steps of optimum signal timings and phase plan．

determination stage of this value，various analyses and statistical tests were executed．The values of $n=1,2, \ldots, 5$ were analyzed and evaluated，respectively．As a result，it is seen that the minimum average vehicle delay for overall intersection can be provided when $n$ is equal to 5．Thus，for the analyses which are in the fifth part of this study，the intervention period was considered as an $n=5$ cycle．

## 3．Vehicle－Actuated Management Model

In the vehicle－actuated control，traffic flows at an in－ tersection are managed using data and information from the detectors which are located at intersection approaches．This type of control can be classified in two ways as semiactuated and full－actuated．In the semiactuated traffic signal control， detectors are located at intersection approaches that hourly traffic volumes are quite low．Therefore，when the vehicle data and information are not detected from the detectors at side roads，right of way always belongs to traffic flows at mainstreams．Otherwise，right of way belongs to traffic flows at side roads．In the full－actuated traffic signal control， detectors are located at all approaches of the intersection．In this type of control，data and information relating to traffic flows are obtained from the detectors which are located in all approaches．Thus，the intersection is managed using ob－ tained data and information from all detectors．

In the vehicle－actuated control，the order of phases can be constant or variable．When the traffic demand is quite low or there is no demand for any phase，this phase is ignored and skipped to the next phase．In this type of control，

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-08.jpg?height=775&width=1539&top_left_y=250&top_left_x=271)
Figure 5: Flowchart of OPTiMA3.

effective management of an intersection is directly related to parameters such as minimum green times (minimum green splits), arrival headways of traffic flows, and maximum green times (maximum green splits). Therefore, the selection of appropriate and reasonable values for these parameters is quite important for the improvement of the performance of intersection [43].

In this study, since the test of applicability and effectiveness of OPTiMA3 are aimed, OPTiMA3 is compared with vehicle-actuated management (VAM). VISVAP module of VISSIM simulation software is used for vehicleactuated management [44-46]. The location of detectors at approaches of intersection which is modeled in the scope of the study is presented in Figure 6 in detail.

As can be seen from Figure 6, a total of 8 detectors are located at the modeled intersection. Detectors are used for both calculating minimum arrival headway and determining the occupancy. For vehicle-actuated management, one of the most important issues is also detector placements on the lanes. Precise information relating to the placement of presence detectors which are used for determining the queuing does not exist [5]. The location should be determined considering hourly traffic volumes at intersection approaches.

In this study, when the intersection approach-based traffic volumes for 14 different traffic scenarios were considered, the presence of three rows of vehicles for mainstreams (East and West approach) and the presence of two rows of vehicles for side road (North) were determined as critical situations considering vehicle queuing. Therefore, the detectors with the numbers 4 and 5 were placed 10 meters away from the approach stop line, and the detectors with the numbers 1-2-3-6-7 and 8 were also placed 15 meters away from the approach stop line.

In the scope of the study, for the vehicle-actuated management model, minimum green time is accepted as 5 seconds for a phase. Maximum green times for phases are determined as 60 seconds. Besides, minimum critical gap value is also considered as about 2 seconds.

In the vehicle-actuated management model, it is assumed that the intersection is operated with three phases. Right of way for each intersection approach is provided in separate phases. Right of ways for West, North, and East intersection approaches are provided in Phase I, Phase II, and Phase III, respectively. Based on the management model which is created in the VAP module, when excitation is not detected from the presence detectors which are at one of the intersection approaches, phase transitions (the order of phases can be changed) can be actualized. The flowchart of the vehicle-actuated management algorithm is presented in Figure 7.

## 4. Analyzes and Results

In this part of the study, the effectiveness of OPTiMA3 approach is analyzed using the VISSIM simulation program. In order to investigate the effects on the performance of different types of management, 14 traffic scenarios are created. For the created sample scenarios, while the traffic volumes at East and West approaches are constant, traffic volume at the North approach is varied.

Before starting the analysis, firstly, optimum signal timings and average vehicle delays for each scenario are computed with the signal timing optimization code, which is created in MATLAB. At this stage, it is assumed that the right of way for each intersection approach is provided in separate phases. For created traffic scenarios, traffic volumes, optimum signal timings, and average vehicle delays are presented in Table 3.

The average vehicle delay values which are obtained from the VISSIM simulation program for each scenario are compared with the results obtained from Akcelik average vehicle delay formula. Due to differences between the results, VISSIM is calibrated. In the calibration process, driving

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-09.jpg?height=1081&width=1491&top_left_y=247&top_left_x=295)
Figure 6: The location of detectors for vehicle-actuated management.

behaviors and safety factors in VISSIM software are revised considering the results which are obtained from Akcelik delay equation. At the end of the calibration studies, for the created traffic scenarios, it was seen that average vehicle delay results which were obtained from VISSIM were quite close to average vehicle delay results obtained by using Akcelik delay equation. Scenario-based comparisons of the average vehicle delay values are presented in Table 4 and Figure 8, respectively.

As can be seen from Table 4, the difference of average vehicle delays which are obtained from VISSIM and by using Akcelik's average delay equation is less than 5\% generally. The results show that calibrated VISSIM can provide similar average vehicle delay values with Akcelik delay equation and can be used for analysis studies.

After the calibration process, four different types of traffic management approaches are evaluated separately for created traffic scenarios. These types of management approaches which are taken into account for analyzes can be summarized as follows:

(1) Optimum Fixed-Time Management (OFTM). In optimum fixed-time management, three-phased management is applied. It is assumed that the right of way for each intersection approach is provided in separate phases. Movement-based traffic volumes and optimum signal timings are transferred to VISSIM. At the end of the analysis, average vehicle delay values for each scenario are obtained.
(2) Vehicle-Actuated Management (VAM). In vehicleactuated management, as can be seen from the fourth part of the study (in Figure 7), an intersection management control algorithm is created in VIS-VAP. Created 14 traffic scenarios are analyzed considering this control algorithm separately.
(3) A Signal Timing and Phase Plan Optimization-Based New Traffic Management Approach for Three-Leg Signalized Intersections/Merging = 0 (OPTiMA3/ $\mathrm{M}=0$ ). In this situation, intersection management approach which is explained in detail in the second part of this study is used. For the analysis studies, the phase plans which do not have any merging movements are considered.
(4) A Signal Timing and Phase Plan Optimization-Based New Traffic Management Approach for Three-Leg Signalized Intersections/Merging = 1 (OPTiMA3/ $\mathrm{M}=1$ ). As different from OPTiMA3/M=0, in this situation, the phase plans which have only one merging movement are considered for the analysis studies.

At the end of the analyzes which are made considering four different types of intersection management approaches, obtained average vehicle delays for the created traffic scenarios are presented in Figure 9 graphically.

When Figure 9 is examined carefully, it can be seen that average vehicle delays obtained by OPTiMA3 approaches are

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-10.jpg?height=2155&width=1454&top_left_y=251&top_left_x=315)
Figure 7: Flowchart of the vehicle-actuated management algorithm created with VAP logic.

Table 3: Traffic volumes, optimum signal timings, and average vehicle delays for created traffic scenarios.
| Scenario no. | Traffic demand (veh) | North | West | East | Green times (sec) | Cycle time (sec) | Av. vehicle delay (sec/veh) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | North | - | 25 | 25 | 7 |  |  |
| 1 | West | 400 | - | 1000 | 25 | 62 | 17.54 |
|  | East | 250 | 600 | - | 15 |  |  |
|  | North | - | 50 | 50 | 7 |  |  |
| 2 | West | 400 | - | 1000 | 25 | 62 | 17.71 |
|  | East | 250 | 600 | - | 15 |  |  |
|  | North | - | 75 | 75 | 7 |  |  |
| 3 | West | 400 | - | 1000 | 23 | 59 | 17.89 |
|  | East | 250 | 600 | - | 14 |  |  |
|  | North | - | 100 | 100 | 7 |  |  |
| 4 | West | 400 | - | 1000 | 23 | 59 | 18.04 |
|  | East | 250 | 600 | - | 14 |  |  |
|  | North | - | 125 | 125 | 7 |  |  |
| 5 | West | 400 | - | 1000 | 23 | 59 | 18.20 |
|  | East | 250 | 600 | - | 14 |  |  |
|  | North | - | 150 | 150 | 7 |  |  |
| 6 | West | 400 | - | 1000 | 21 | 56 | 18.48 |
|  | East | 250 | 600 | - | 13 |  |  |
|  | North | - | 175 | 175 | 8 |  |  |
| 7 | West | 400 | - | 1000 | 21 | 57 | 19.59 |
|  | East | 250 | 600 | - | 13 |  |  |
|  | North | - | 200 | 200 | 9 |  |  |
| 8 | West | 400 | - | 1000 | 21 | 58 | 20.82 |
|  | East | 250 | 600 | - | 13 |  |  |
|  | North | - | 225 | 225 | 10 |  |  |
| 9 | West | 400 | - | 1000 | 21 | 59 | 22.09 |
|  | East | 250 | 600 | - | 13 |  |  |
|  | North | - | 250 | 250 | 11 |  |  |
| 10 | West | 400 | - | 1000 | 21 | 60 | 23.42 |
|  | East | 250 | 600 | - | 13 |  |  |
|  | North | - | 275 | 275 | 13 |  |  |
| 11 | West | 400 | - | 1000 | 23 | 65 | 24.80 |
|  | East | 250 | 600 | - | 14 |  |  |
|  | North | - | 300 | 300 | 14 |  |  |
| 12 | West | 400 | - | 1000 | 23 | 66 | 26.20 |
|  | East | 250 | 600 | - | 14 |  |  |
|  | North | - | 325 | 325 | 15 |  |  |
| 13 | West | 400 | - | 1000 | 23 | 67 | 27.69 |
|  | East | 250 | 600 | - | 14 |  |  |
|  | North | - | 350 | 350 | 17 |  |  |
| 14 | West | 400 | - | 1000 | 24 | 71 | 29.21 |
|  | East | 250 | 600 | - | 15 |  |  |


Yellow time $=2+2 \mathrm{sec}$ (at the starting and finishing of each phase)/all red time $=1 \mathrm{sec}$ (at each phase transition).
lower than average vehicle delays that are provided by both OFTM and VAM approaches.

In order to evaluate the successes of the different intersection management approaches, the comparisons are made in this part of the study. For this purpose, reduction rates for average vehicle delays are calculated separately for created 14 scenarios. The comparisons for four different types of intersection management approaches are presented in Figure 10. These comparisons can be summarized as follows:

(i) In case of implementation of VAM instead of OFTM
(ii) In case of implementation of OPTiMA3/M=0 instead of OFTM
(iii) In case of implementation of OPTiMA3/M = 1 instead of OFTM
(iv) In case of implementation of OPTiMA3/M=0 instead of VAM
(v) In case of implementation of OPTiMA3/M = 1 instead of VAM
(vi) In case of implementation of OPTiMA3/M = 1 instead of OPTiMA3/M = 0

In Figure 10, the pairwise comparison of relative performances of different types of traffic management systems for the traffic scenarios is shown by bar charts. Besides, trends of delay reduction rates are depicted by red-dashed lines.

## 5. Evaluation of the Results

The results of the analyzes can be summarized as follows:

Table 4: Scenario-based comparison of average vehicle delay values.
| Scenario no. | Akcelik | VISSIM | Difference (\%) |
| :--- | :--- | :--- | :--- |
| 1 | 17.54 | 17.97 | -2.45 |
| 2 | 17.71 | 18.08 | -2.09 |
| 3 | 17.89 | 18.29 | -2.24 |
| 4 | 18.04 | 18.35 | -1.72 |
| 5 | 18.2 | 18.66 | -2.53 |
| 6 | 18.48 | 18.93 | -2.44 |
| 7 | 19.59 | 20.08 | -2.50 |
| 8 | 20.82 | 20.88 | -0.29 |
| 9 | 22.09 | 21.27 | 3.71 |
| 10 | 23.42 | 22.01 | 6.02 |
| 11 | 24.80 | 23.23 | 6.33 |
| 12 | 26.20 | 25.31 | 3.40 |
| 13 | 27.69 | 27.44 | 0.90 |
| 14 | 29.21 | 27.84 | 4.69 |


![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-12.jpg?height=543&width=799&top_left_y=972&top_left_x=195)
Figure 8: Comparison of average vehicle delays which were obtained from VISSIM and Akcelik average delay equation.

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-12.jpg?height=616&width=814&top_left_y=1667&top_left_x=187)
Figure 9: Comparison of the performances of different intersection management approaches.

(i) Comparisons of the performances of different intersection management approaches show thatthe results which were obtained with OPTiMA3 and VAM were close to each other for the traffic demand at North intersection approach was low. When the traffic demand in the North approach increased, the success of VAM was significantly reduced. Besides, significant increases or decreases were not seen for the success of OPTiMA3.
(ii) The lowest average vehicle delay values for the created scenarios were obtained with OPTiMA3/ $\mathrm{M}=1$. It can be seen that this approach may increase the performance of intersection significantly. On the contrary, it should be noted that this type of management approach is worse and weaker than the other types of management approaches in the context of a traffic safety issue.
(iii) As can be seen from Figure 10, for the scenarios, average vehicle delays can be reduced between 5\% and 35\% in case of implementation of VAM instead of OFTM. When the traffic demand at North intersection approach is low, the delay reduction rate is about $35 \%$. However, when the traffic demand at North intersection approach is increased, the delay reduction rate decreases up to about 5\%. Obtained results show that VAM operates more effectively in case of high differences in traffic demands at intersection approaches. These findings support the previous studies in the literature [41, 47].
(iv) In Figure 10, it may be inferred that average vehicle delays can be reduced between $28 \%$ and $37 \%$ in case of implementation of OPTiMA3/M=0 instead of OFTM. The results show that the level of success of OPTiMA3/M=0 is quite high for the management of intersection. Besides, average vehicle delays can be reduced between 37\% and $42 \%$ in case of implementation of OPTiMA3/M = 1 instead of OFTM. This situation shows that OP-TiMA3/M = 1 is more effective than OPTiMA3/ $\mathrm{M}=0$ for the reduction of average vehicle delay. In OPTiMA3/M=1, the signalized intersection is managed by allowing one merging movement at each signal cycle. Although this situation has an effective role in the reduction of average vehicle delay, it adversely affects traffic safety at the intersection.
(v) From the results, it can be seen that average vehicle delays can be significantly reduced in case of implementation of OPTiMA3/M=0 instead of VAM. When the traffic demand at North intersection approach is low, average vehicle delays which are obtained with OPTiMA3/M=0 and VAM are similar to each other. Thus, delay reduction rates are also quite low. When the traffic demand at North intersection approach increases, OPTiMA3/M = 0 becomes more advantageous than VAM due to the effect of phase plan optimization.

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-13.jpg?height=2023&width=1491&top_left_y=243&top_left_x=297)
Figure 10: The comparison of achievements for different intersection management approaches.

So, delay reduction rates show an increasing trend. For created scenarios, delay reduction rates range from 3\% to 27\% in case of implementation of OPTiMA3/M=0 instead of VAM.

(vi) As can be seen from Figure 9, average vehicle delays can be reduced in case of implementation of OPTiMA3/M=1 instead of VAM. For created scenarios, delay reduction rate trend resembles the

trend which is obtained in case of implementation of OPTiMA3/M = 0 instead of VAM. In addition to this, delay reduction rates range from 4\% to 38\% in case of implementation of OPTiMA3/M=1 instead of VAM.
(vii) When Figure 10 is examined carefully, it can be seen that the difference in performance between OPTiMA3/M=0 and OPTiMA3/M=1 is not considerable. Average vehicle delay reduction rates which are obtained in case of implementation of OPTiMA3/M = 1 instead of OPTiMA3/M = 0 show an increasing trend due to the effect of phase plan optimization and increase in traffic demand at North intersection approach. For created scenarios, delay reduction rates range from 1\% to 17\% in case of implementation of OPTiMA3/M=1 instead of OPTiMA3/M = 0.

## 6. Discussion and Conclusions

In this study, a new signal timing and signal phasing optimization-based control model is developed for the management of three-leg signalized intersections using the Differential Evolution algorithm. The effectiveness of the model is tested on traffic scenarios with VISSIM simulation software considering average vehicle delay performance criteria. The findings can be summarized as follows:

(i) Use of the Differential Evolution algorithm for signal timing and signal phasing optimization is analyzed in this research.
(ii) In the literature, many researchers focus on only the signal timing optimization problem generally. But in this study, as well as signal timing optimization, signal phasing optimization are also taken into account. Results show that signal phasing optimization is a quite important issue in traffic management, and if it is considered, it may help to reduce the average vehicle delays and to increase the performance of intersection.
(iii) It is concluded that the preference of movementrelated approach instead of phase-related approach can provide remarkable advantages for signal timing and signal phasing optimization studies (i.e., the flexibility of signal timing and signal phasing may increase by this way).
(iv) It has been understood that the optimization-based approaches can provide better results than trafficactuated and fixed-time management approaches in terms of average vehicle delay values.
(v) Especially in case of high differences in traffic demands at intersection approaches, the vehicleactuated management (VAM) approach provides significant improvements. However, in cases where there is no major change in traffic volume, the VAM may not provide enough advantage.
(vi) According to the results, it is understood that allowing the merging movements may reduce theaverage vehicle delays significantly. Although this situation has an effective role in the reduction of average vehicle delay, it adversely affects traffic safety at the intersection.
(vii) In this study, the effects of pedestrians are not considered in the development of all types of traffic signal control models. In the future studies, signal phasing for pedestrians can be taken into account, and the effects of pedestrians can be analyzed in detail. Besides, the effects of tram/rail lines and cyclists on the performance of signalized intersections can be investigated.
(viii) In this study, both of the traffic signal control models (OPTiMA3 and VAM) were developed for a three-leg signalized intersection model. In the future studies, different types of intersections can be considered. New signal timing and signal phasing optimization-based traffic signal control models can be developed considering these different types of intersection models. Thus, the applicability of the signal timing and signal phasing optimization-based traffic signal control models may be increased.

## Data Availability

The data used to support the findings of this study are included within the article.

## Conflicts of Interest

The authors declare no conflicts of interest.

## Acknowledgments

The authors of this article would like to thank PTV (Planung Transport Verkehr AG) for providing VISSIM simulation software.

## References

[1] Z. Cakici and Y. S. Murat, "The investigation of signalized roundabouts performances considering different traffic scenarios," in Proceedings of the 11th National Transportation Congress, pp. 105-116in Turkish, Istanbul, Turkey, 2015.
[2] I. Sahin, "The problem of transportation planning and transportation investments: istanbul sample," in Proceedings of the 11th National Transportation Congress, pp. 13-25in Turkish, Istanbul, Turkey, 2015.
[3] I. Gulgec, Ulasim Planlamasi, Ozsan Mat. San. Ltd. Sti., Ankara, Turkey, 1st edition, 1998, in Turkish.
[4] N. Yayla, Karayolu Muhendisligi, Birsen Yay. Ltd. Sti., Istanbul, Turkey, 3rd edition, 2008, in Turkish.
[5] National Research Council, Highway Capacity Manual-2010 (HCM-2010), National Research Council, Washington, DC, USA, 2010.
[6] Z. Cakici and Y. S. Murat, "A new calculation procedure for signalized roundabouts and performance analysis," Technical Journal of Turkish Chamber of Civil Engineers, vol. 27, no. 4, pp. 7569-7592, 2016.

[7] Y. S. Murat, Fuzzy logic traffic responsive signal cycle model for isolated signalized intersections, Ph.D. thesis, Istanbul Technical University, Institute of Natural and Applied Sciences, Turkey, 2001, in Turkish.
[8] E. Dogan, Isolated signalized intersection control by optimized fuzzy logic method, Ph.D. thesis, Kirikkale University, Institute of Natural and Applied Sciences,Kırıkkale, Turkey 2014, in Turkish.
[9] R. T. Van Katwijk, Multi-agent look-ahead traffic-adaptive control, Ph.D. thesis, Technische Universiteit Delft,Delft, Netherlands 2008.
[10] F. Gundogan, Simplified traffic responsive signal control method for developing large cities, Ph.D. thesis, Graz University of Technology, Graz, 2012.
[11] P. Mirchandani and L. Head, "A real-time traffic signal control system: architecture, algorithms, and analysis," Transportation Research Part C: Emerging Technologies, vol. 9, no. 6, pp. 415-432, 2001.
[12] H. Li and P. D. Prevedouros, "Traffic adaptive control for oversaturated isolated intersections: model development and simulation testing," Journal of Transportation Engineering, vol. 130, no. 5, pp. 594-601, 2004.
[13] J. Lee, B. Abdulhai, A. Shalaby, and E.-H. Chung, "Real-time optimization for adaptive traffic signal control using genetic algorithms," Journal of Intelligent Transportation Systems, vol. 9, no. 3, pp. 111-122, 2005.
[14] L. Shoufeng, L. Ximin, and D. Shiqiang, "Q-learning for adaptive traffic signal control based on delay minimization strategy," in Proceedings of the 2008 IEEE International Conference on Networking, Sensing and Control, pp. 687-691, Sanya-China, 2008.
[15] L. Singh, S. Tripathi, and H. Arora, "Time optimization for traffic signal control using genetic algorithm," International Journal of Recent Trends in Engineering, vol. 2, no. 2, pp. 4-6, 2009.
[16] X. Zheng, W. Recker, and L. Chu, "Optimization of control parameters for adaptive traffic-actuated signal control," Journal of Intelligent Transportation Systems, vol. 14, no. 2, pp. 95-108, 2010.
[17] E. Angulo, F. P. Romero, R. García, J. Serrano-Guerrero, and J. A. Olivas, "An adaptive approach to enhanced traffic signal optimization by using soft-computing techniques," Expert Systems with Applications, vol. 38, no. 3, pp. 2235-2247, 2011.
[18] S. Samadi, A. P. Rad, F. M. Kazemi, and H. Jafarian, "Performance evaluation of intelligent adaptive traffic control systems: a case study," Journal of Transportation Technologies, vol. 2, no. 3, pp. 248-259, 2012.
[19] D. McKenny and T. White, "Distributed and adaptive traffic signal control within a realistic traffic simulation," Engineering Applications of Artificial Intelligence, vol. 26, pp. 574-583, 2012.
[20] C. Vilarinho and J. P. Tavares, "Real-time traffic signal settings at an isolated signal control intersection," in Proceedings of the 17th Meeting of the Euro Working Group on Transportation, pp. 1021-1030, Seville, Spain, July 2014.
[21] B. Yulianto and B. Sutanto, "Adaptive traffic signal control for mixed traffic conditions," in Proceedings of the 1st International Conference on Engineering Technology and Industrial Application, pp. 111-116, Surakarta, Indonesia, November 2014.
[22] D. Koltovska and K. Bombol, "Intelligent agent based traffic signal control on isolated intersections," TEM Journal, vol. 3, no. 3, pp. 216-222, 2014.
[23] A. Aljaafreh and N. Al-Oudat, "Optimized timing parameters for real-time adaptive traffic signal controller," in Proceedings of the 2014 UKSim-AMSS 16th International Conference on Computer Modelling and Simulation, pp. 243-246, Cambridge, UK, March 2014.
[24] F. Khalighi, "A real-time signal control system to minimize emissions at isolated intersections," M.Sc. thesis, University of Massachussets, Amherst, Massachusetts 2015.
[25] D. Yu, X. Tian, X. Xing, and S. Gao, "Signal timing optimization based on fuzzy compromise programming for isolated signalized intersection," Hindawi Publishing Corporation Mathematical Problems in Engineering, vol. 2016, Article ID 1682394, 12 pages, 2016.
[26] G. B. Castro, A. R. Hirakawa, and J. S. C. Martini, "Adaptive traffic signal control based on bio-neural network," Procedia Computer Science, vol. 109, pp. 1182-1187, 2017.
[27] R. Akcelik, Traffic Signals: Capacity and Timing Analysis, Australian Road Research Board, Vermont South, Australia, 1998.
[28] S. Dabiri and M. Abbas, "Arterial traffic signal optimization using Particle Swarm optimization in an integrated VISSIMMATLAB simulation environment," in Proceedings of the 2016 IEEE 19th International Conference on Intelligent Transportation Systems, pp. 766-771, Rio de Janerio, Brazil, 2016.
[29] S. Akyol and B. Alatas, "The current Swarm intelligence optimization algorithms," Journal of Institute Natural and Applied Sciences of Nevsehir University, vol. 1, pp. 36-50, 2012, in Turkish.
[30] M. Dell'Orco, O. Baskan, and M. Marinelli, "A harmony search algorithm approach for optimizing traffic signal timings," Promet Traffic\&Transportation, vol. 25, no. 4, pp. 349-358, 2013.
[31] M. T. Ayvaz, A. H. Kayhan, H. Ceylan, and G. Gurarslan, "Hybridizing the harmony search algorithm with a spreadsheet "Solver" for solving continuous engineering optimization problems," Engineering Optimization, vol. 41, no. 12, pp. 1119-1144, 2009.
[32] M. Artar, "Optimum design of steel space frames under earthquake effect using harmony search," Structural Engineering and Mechanics, vol. 58, no. 3, pp. 597-612, 2016.
[33] Y. S. Murat and Z. Cakici, "The application of heuristic optimization algorithms on vehicle delay problem," in Proceedings of the 7th National Urban Infrastructure Symposium, Trabzon, Turkey, pp. 615-625, 2015, in Turkish.
[34] O. Baskan and H. Ceylan, "Differential evolution algorithm based solution approaches for solving transportation network design problems," Pamukkale University Journal of Engineering Sciences, vol. 20, no. 9, pp. 324-331, 2014, in Turkish.
[35] O. Baskan and C. Ozan, "Determining optimum configuration of one-way and two-way streets using shortest path travel costs based on results of traffic assignment," Pamukkale University Journal of Engineering Sciences, vol. 24, no. 6, pp. 1087-1092, 2018.
[36] E. Korkmaz and A. P. Akgungor, "Delay estimation models for signalized intersections using differential evolution algorithm," International Journal of Engineering Research, vol. 5, no. 3, pp. 16-29, 2017.
[37] A. P. Akgüngör and E. Korkmaz, "Analysis and modelling of the relationship between stopped and control delays by differential evolution algorithm," The Open Civil Engineering Journal, vol. 10, no. 1, pp. 266-279, 2016.

[38] T. Keskintürk, "Differential evolution algorithm," Journal of Institute of Natural and Applied Sciences of Istanbul Ticaret University, vol. 9, pp. 85-99, 2006, in Turkish.
[39] Z. Yuedong, F. Wei, and Q. Chenchen, "A PSO based signal timing optimization approach of approach of phase combination," in Proceedings of the International Conference on Civil, Transportation and Environment (ICCTE 2016), pp. 314-319, Guangzhou, China, 2016.
[40] Q. Liu and J. Xu, "Traffic signal timing optimization for isolated intersections based on differential evolution bacteria foraging algorithm," Procedia-Social and Behavioral Sciences, vol. 43, pp. 210-215, 2012.
[41] Y. S. Murat and S. Kikuchi, "The fuzzy optimization approach: a comparison with the classical optimization approach using the problem of timing a traffic signal," Transportation Research Record, vol. 2024, pp. 82-91, 2007.
[42] Mathworks, MATLAB R2013b, Mathworks, Natick, Massachusetts, USA, 2013.
[43] Y. Guo and J. Ma, "An improved actuated signal control of intersection based on VISVAP," in Proceedings of the 6th International Conference on Sensor Network and Computer Engineering (ICSNCE 2016), pp. 123-128, Xi'an, China, 2016.
[44] PTV AG, VISSIM 10.0 Software, PTV AG, Karlsruhe, Germany, 2017.
[45] PTV AG, VAP 2.16 User Manual, PTV AG, Karlsruhe, Germany, 2017.
[46] PTV AG, VISVAP 2.16 User Manual, PTV AG, Karlsruhe, Germany, 2017.
[47] N. Swaminathan, N. Rathinawel, S. Duraisamy, and G. Karuppanan, "Design of vehicle actuated signal using simulation," Gradevinar, vol. 7, pp. 635-641, 2014.

![](https://cdn.mathpix.com/cropped/56238cf0-7e8e-4aff-b760-9d9a3d8ec00d-17.jpg?height=2279&width=1747&top_left_y=334&top_left_x=169)

