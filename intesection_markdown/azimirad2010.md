# A Novel Fuzzy Model and Control of Single Intersection at Urban Traffic Network 

Ehsan Azimirad, Naser Pariz, and M. Bagher Naghibi Sistani


#### Abstract

This paper presents a novel fuzzy model and a fuzzy logic controller for an isolated signalized intersection. The controller controls the traffic light timings and phase sequence to ensure smooth flow of traffic with minimal waiting time and length of queue. Usually fuzzy traffic controllers are optimized to maximize traffic flows/minimize traffic waiting time under typical traffic conditions. Consequentially, these are not the optimal traffic controllers under exceptional traffic cases such as roadblocks and road accidents. We apply state-space equations to formulate the average waiting time vehicles in traffic network at fixed time control. also, We propose a novel fuzzy model and new fuzzy traffic controller that can optimally control traffic flows under both normal and exceptional traffic conditions. Results show that the performance of the proposed traffic controller at novel fuzzy model is better that of conventional fuzzy traffic controllers under normal and abnormal traffic conditions.


Index Terms-Fuzzy model, state-space equations, traffic flow, fuzzy controller.

## I. Introduction

TRAFFIC signal control has been one of the most active research areas in intelligent transportation systems (ITS), because such control directly affects the efficiency of urban transportation systems. For years many investigators have conducted research into optimal signal control algorithms. Webster [1] gave equations for the optimal cycle length and the green phase time assignment, which are the basis of fixed-time control which has been widely used. Akcelik [2], [3] modified Webster's theory for the over-saturated scenario in a new signal timing algorithm called ARRB. These methods perform well with low calculational costs when traffic conditions are consistent with historical records, but cannot respond to real-time variations. With the development of a variety of inexpensive sensors and computer and communication technologies, many advanced methods have been developed to adjust signal timings according to real-time traffic data. For instance, vehicle actuated control, which extends green signals according to the detected headway in real time, is one such method. A number of adaptive traffic control systems have been deployed all over the world, such as SCOOT [4], SCATS [5], OPAC [6], and RHODES

[^0][7]. In recent years, artificial intelligence techniques have been introduced into signal control using fuzzy logic controllers [8] and genetic algorithms (GA) [9]. These systems have various properties and varying effectiveness in field applications.

Transportation systems are complex dynamic systems that are hard to be modeled exactly. For this reason, many current methods do not have good theoretical bases. However, without a model description, the inner properties of the transportation system cannot be identified to evaluate existing algorithms and to recognize potential problems and improve them. Sen and Head [10] proposed a general formulation to model signal controls as discrete-time optimal control problems. They also pointed out that the problem can, in principle, be solved using the dynamic programming (DP) method when the performance index is separable in the DP sense, and that this solution is not virtually feasible due to "the curse of dimensionality." In this paper, state-space equations are used to formulate the signal control problem for a single intersection in a simplified mathematical model, which can lead to designing better signal controllers [12].

Modeling of systems is a very essential concept to develop an effective control system and for simulation of a physical process. Fuzzy logic is a distinct idea for developing models of physical processes. Fuzzy models are less externally complex; they can be understood easily and very much suitable for non-linear processes. Models with fewer rules are more advantageous. The process chosen in this work is decreasing waiting time vehicles in single intersections, which is a vital component of a urban traffic network. The model is developed using MATLAB 7.4 [13], [14].

As the complexity of the target system increases, our ability to make precise and yet significant statements about its behaviour diminishes until a threshold is reached beyond which significance become almost mutually exclusive characteristics. In such a case, the underlying mechanics are better represented linguistically rather than mathematically. Thus fuzzy models have gained significance [13].

## II. Fuzzy Modeling of Single Intersection

## A. State-Space Equations

The two Phases Signalized Intersection shape that utilizes it for mentioning modeling single intersections in this paper was demonstrating in Fig. 1. In this shape, The Leg 1 and Leg 3 are phase 1 and The Leg 2 and Leg 4 are phase 2.

The queue length is an important variable that describes the traffic state of an intersection. The queue evolves as

$$
Q_{i}(n+1)=Q_{i}(n)+q_{i}(n)-d_{i}(n) S_{i}(n)
$$

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-2.jpg?height=705&width=677&top_left_y=226&top_left_x=234)
Fig. 1. Two phase signalized intersection shape.

where $i=1,2, \ldots, M$ is the index of the traffic streams; $n=$ $0,1, \ldots, N-1$ is the index of the discretized time intervals; $Q_{i}(n)$, in unit of number of vehicles, is the queue length of the $i$ th stream at the onset of the $n$th time interval; $q_{i}(n)$ is the number of vehicles that join the $i$ th queue in the $n$th time interval; $d_{i}(n)$ is the number of vehicles that depart from the $i$ th queue in the $n$th time interval; and $S_{i}(n)$, which takes 0 (for stop) or 1 (for go), is the signal state of the $i$ th stream in the $n$th time interval. $q_{i}$ and $d_{i}$ are normally distributed random signals.

In fixed-time control and fuzzy intelligent control model, the control variables was considered as follows. For phase 1 intersection, $\left(S_{1}, S_{2}, S_{3}, S_{4}\right)=(0,1,0,1)$ means that traffic light is green in lanes 2 and 4 and red in lanes 1 and 3. Therefore, the vehicles can go in lanes 2 and 4 and they should stop in s 1 and 3. On the other hand, for phase 2 intersection, $\left(S_{1}, S_{2}, S_{3}, S_{4}\right)=$ (1, 0, 1, 0) means that traffic light is green in lanes 1 and 3 and red in lanes 2 and 4. Therefore, the vehicles can go in lanes 1 and 3 and they should stop in lanes 2 and 4.

Integrating the length of queue with respect to time yields the average vehicle's waiting time in the queue. Let $T$ denote the length of the discretized time interval. If $T$ is short enough, the vehicles arrivals can be treated as being uniform in every time interval. Hence, integrating (1) yields

$$
W_{i}(n+1)=W_{i}(n)+T Q_{i}(n)+\frac{1}{2} T q_{i}(n)-\frac{1}{2} T d_{i}(n) S_{i}(n)
$$

where $W_{i}(n)$ is the average vehicle-wise waiting time of the $i$ th queue from the beginning of the period to the onset of the $n$th time interval.

Equations (1) and (2) are the state-space equations describing the dynamic evolution of the traffic state at a single intersection. The waiting time and the number of vehicles are popular performance indices for signal controls. The waiting time is used here as the performance index. Therefore, the optimization objective is

$$
\min \left\{W(N)=\sum_{i=1}^{M} W_{i}(N)\right\} .
$$

To facilitate the formulation, the state-space equations and the optimization objective can be rewritten in matrix form as

$$
\begin{aligned}
X(n+1) & =A X(n)+B(n) S(n)+C(n) \\
y(n) & =C X(n)
\end{aligned}
$$

where
$X(n)=\left[Q_{1}(n) Q_{2}(n) \ldots Q_{M}(n) W_{1}(n) W_{2}(n) \ldots W_{M}(n)\right]^{T}$ are the state variables and $S(n)=\left[S_{1}(n) S_{2}(n) \ldots S_{M}(n)\right]^{T}$ are the control variables. The various coefficient matrices and vectors are [12]

$$
\begin{aligned}
A & =\left[\begin{array}{cc}
I_{M} & 0 \\
T I_{M} & I_{M}
\end{array}\right], \\
B(n) & =-\left[\begin{array}{cccc}
d_{1}(n) & 0 & \cdots & 0 \\
0 & d_{2}(n) & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & & & \\
\frac{1}{2} T d_{1}(n) & 0 & \cdots & d_{M}(n) \\
0 & \frac{1}{2} T d_{2}(n) & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \frac{1}{2} T d_{M}(n)
\end{array}\right), \\
C & =\left[\begin{array}{cc}
I_{M} & 0 \\
0 & I_{M}
\end{array}\right], \\
C(n) & =\left[\begin{array}{cccc}
q_{1}(n) q_{2}(n) \cdots q_{M}(n) \frac{1}{2} T q_{1}(n) \frac{1}{2} T q_{2}(n) \cdots \frac{1}{2} T q_{M}(n)
\end{array}\right]^{T} .
\end{aligned}
$$

## B. Novel Fuzzy Model of Single Intersection

The first stage of fuzzy modeling is the selection of performance variables. Here the input and output variables of the traffic in single intersection are selected. The input variables are $d_{i}(n), q_{i}(n)$ and $S_{i}(n)$. The output variables are $Q_{i}(n)$ for $i=1,2, \ldots, 4$, that were explained in before section. $W_{i}(n)$ and $Q_{i}(n)$ are state variables that were considered as the input of fuzzy model.

The second stage of fuzzy modeling is the determination of variables surface i.e., fuzzy sets (fuzzification). The fuzzy sets or the linguistic variables for the inputs and outputs given above are designed. $W_{i}(n), Q_{i}(n)$ and $q_{i}(n)$ are divided into three fuzzy sets: "Low(L)," "Medium(M)," and "High(H)." The next stage of fuzzy modeling is to form the fuzzy relationship between the inputs and outputs i.e., rules. The rules are formed from the available inputs-outputs data sequences of the urban traffic network, based on if-then statement. The general format of the fuzzy rules of controller is as follows:

If $\left\{W_{i}\right.$ is $\left.X_{i}\right\}$ and $\left\{Q_{i}\right.$ is $\left.Y_{i}\right\}$ Then $\left\{q_{i}\right.$ is Go or STOP $\}$ where $X_{i}, Y_{i}, q_{i}$ and Go or STOP are linguistic variables; Go is the Extension of green phase and STOP is the Termination of green phase. In this paper, the number of fuzzy rules is 81. The

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-3.jpg?height=281&width=625&top_left_y=228&top_left_x=256)
Fig. 2. Fuzzy sets for $W_{1}, W_{2}, W_{3}, W_{4}$.

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-3.jpg?height=273&width=595&top_left_y=642&top_left_x=269)
Fig. 3. Fuzzy sets for $Q_{1}, Q_{2}, Q_{3}, Q_{4}$.

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-3.jpg?height=273&width=591&top_left_y=1046&top_left_x=271)
Fig. 4. Fuzzy sets for $q_{1}, q_{2}, q_{3}, q_{4}$.

parameters $W_{i}, Q_{i}$ and $q_{i}$ for $(i=1, \ldots, 4)$ are characterized by fuzzy numbers as shown in Figs. 2-4.

The exact numerical crisp value of the output number of vehicles that join the $i$ th queue in the $n$th time interval for the given inputs is calculated using the defuzzification techniques, which is the last stage of fuzzy modeling. There are several methods of defuzzification available. The exact value of output is calculated from the centre of gravity defuzzification technique, which is mostly used in the fuzzy logic system.

## III. Simulation Results

The simulation is carried out using MATLAB 7.4 and the Fuzzy Logic Toolbox. The Fuzzy logic toolbox is useful to build quickly the required rules and changes are easily made. This significantly reduces the development time of the simulation model. The novel fuzzy model and new fuzzy traffic controller that can optimally control traffic flows under both normal and exceptional traffic conditions. The Criterion of optimization are the decrement length of queues and the average of waiting time vehicles in intersection. the results of simulation of model was stated in the both of open and close loop models. In simulation, $T=5$ is sampling time and the cycle time of traffic light is 100 s. The simulator is run 1000 s with the following assumptions:

1) A four arm intersection and each arm has three lanes.
2) The arrival of vehicles is independent on each lane.

The inter-arrival of vehicles is also independent and normal distribution is used to generate arrivals.

This results in inter-arrival of vehicles is 5 s.

TABLE I
The Position of Traffic by Variations of $\beta$
| The Position of Traffic | $\beta$ |
| :--- | :--- |
| Non Saturation | $\beta \geq 0.7$ |
| Saturation | $0.4 \leq \beta \leq 0.6$ |
| Super Saturation | $0.1 \leq \beta \leq 0.3$ |
| Instable | $\beta=0$ |


3) Pedestrian crossing is considered.
4) Sensors are placed at a certain distant from the intersection, the maximum vehicle that can be detected queuing is 30 vehicles.
5) Maximum green time is 40 s and the minimum green time is 5 s.

The number of vehicles that depart from the $i$ th queue in the $n$th time interval is adapted by equation

$$
d_{i}(n)=\min \left(Q_{i}(n)+q_{i}(n), d_{s i}(n)\right)
$$

such that saturation flow rate is

$$
d_{s i}(n)=d_{\text {cons. }}(n)+\beta q_{i}(n)
$$

for $i=1,2,3,4$. The $d_{\text {cons. }}$ parameter is greater equal fifty, $\left(d_{\text {cons. }} \geq 50\right)$. The $\beta$ parameter is between 0 and 1 , such that it's variations are related to follows table (Table I). The traffic informations was recorded every 5 s and was used in the simulations. The $q_{i}$ and $d_{i}$ variables are normally distributed random signals in this fuzzy model.

The results of simulation of fuzzy model for Fixed time control and Fuzzy intelligent control were demonstrated in Fig. 8.

## A. Fixed-Time Control

The traffic lights of Leg1 and Leg3 in Fig. 1 were considered green in 140 s and red in after 60 s. On the other hand, The traffic lights of Leg2 and Leg4 in Fig. 1 were considered red in 140 s and green in after 60 s. The goal of simulation is the decrement of waiting time vehicles and the queue of length. The output of fuzzy model was demonstrated in follows on intersection Fig. 1 in fixed time control. The fuzzy model of Two Phase Signalized Intersection was designed in Fig. 5 without controller.

The summation of number vehicles in Queues on intersection were demonstrated in every 5 s in Fig. 6. The simulation of time is 1000 s.

## B. Fuzzy Intelligent Control

The output of controller is the control of variables $\left(S_{i}\right)$. This control of variables for the Leg1 and Leg3 of intersection were demonstrated in Fig. 7. also, The summation of number vehicles

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-4.jpg?height=778&width=851&top_left_y=228&top_left_x=146)
Fig. 5. Fuzzy model of Two Phase Signalized Intersection.

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-4.jpg?height=685&width=806&top_left_y=1119&top_left_x=170)
Fig. 6. The number of vehicles in four queues of intersection without controller.

in Queues on intersection were demonstrated in every 5 s in follows. The simulation of time is 1000 s.

## IV. Conclusion

The fuzzy model of urban traffic network was designed for a single intersection, with the length of queues and the average waiting time vehicles in any lane as the state of variables. However, for demonstrating the percentage of improvement traffic, a Fuzzy signal controller was designed. The controller was tested using simulink program on Matlab 7.4. Simulation results and the percentage of improvement show that the Fuzzy intelligent of controller reduces the average waiting time vehicles in any lane of intersection compared to Fixed-time control (Table II). The methods of other for fuzzy modeling and control in complicated intersections and nonisolated intersections in urban traffic network and investigation into heuristic methods

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-4.jpg?height=743&width=804&top_left_y=223&top_left_x=1083)
Fig. 7. The control of variables of Leg1 and Leg3.

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-4.jpg?height=681&width=797&top_left_y=1089&top_left_x=1085)
Fig. 8. The number of vehicles in four queues of intersection with fuzzy controller.

Fig. 8. The number of vehicles in four queues of intersection with fuzzy controller.
| TABLE II The Compare of Results Average Waiting Time in any Lane of Fuzzy Model |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Average Waiting Time (second) | Queue 1 | Queue 2 | Queue 3 | Queue 4 | Summation of Queues |
| Fixed Time Control | 11000 sec. | 5000 sec. | 11000 sec. | 5000 sec. | 32000 sec. |
| Fuzzy Intelligent Control | 1350 sec. | 1335 sec. | 1300 sec. | 1313 sec. | 5300 sec. |
| Improvement Percentage | 87.72 | 73.3 | 88.18 | 73.74 | 83.43 |


of solving the developed optimal control problem based on the state-space equations should be done in the future.

## References

[1] F. V. Webster, "Traffic signal settings," Road Research Technical. London, U.K., 1958, Paper No. 39, Road Res. Lab.
[2] R. Akcelik, "Time-dependent expressions for delay, stop rate and queue length at traffic signals," Australia, 1980, Australian Road Res. Board.
[3] R. Akcelik, "Traffic signals: Capacity and timing analysis," Australia, 1981, Australian Road Res. Board.
[4] D. I. Robertson and R. D. Bretherton, "Optimizing networks of traffic signals in real-time: The SCOOT method," IEEE Trans. Veh. Technol., vol. 40, no. 1, pp. 11-15, 1991.
[5] P. R. Lowrie, "The Sydney coordinated adaptive traffic system- principles, methodology, algorithms," in Proc. Int. Conf. Road Traffic Signalling, London, UK, 1982, pp. 67-70, Inst. Elect. Eng..
[6] N. H. Gartner, "A demand-responsive strategy for traffic signal control," Transport. Res. Rec., vol. 906, pp. 75-81, 1983.
[7] P. Mirchandani and L. Head, "A real-time traffic signal control system: Architecture, algorithms, and analysis," Transport. Res. C, vol. 9, no. 6, pp. 415-432, 2001.
[8] C. P. Pappis and E. H. Mamdani, "A fuzzy logic controller for a traffic junction," IEEE Trans. Syst., Man, Cybern., vol. SMC-7, pp. 707-717, 1977.
[9] J. Horn, N. Nafpliotis, and D. E. Goldberg, "A niched pareto genetic algorithm for multi-objective optimization," in Proc. First IEEE Conf. Evolutionary Computation, IEEE World Congr. Computational Intelligence, 1994, vol. 1, pp. 82-87.
[10] S. Sen and L. Head, "Controlled optimization of phases at an intersection," Transportation. Sci., vol. 31, pp. 5-17, 1997.
[11] W.-M. Wey and R. Jayakrishnan, "Network traffic signal optimization formulation with embedded platoon dispersion simulation," Transport. Res. Rec., vol. 1683, pp. 150-159, 1999.
[12] J. Li, X. Pan, and X. Wang, "State-space equations and the first-phase algorithm for signal control of single intersections," Tsinghua Sci. Technol., vol. 12, no. 2, pp. 231-235, Apr. 2007, ISSN 1007-0214 14/14.
[13] S. Samyuktha and P. Kanagasabapathy, "Optimized fuzzy modeling of a boiler superheater," Depart. Instrum. Eng, M.I.T Anna Univ.. Chennai, India.
[14] B. M. Nair and J. Cai, "A fuzzy logic controller for isolated signalized intersection with traffic abnormality considered," in Proc. 2007 IEEE Intelligent Vehicles Symp. Istanbul, Turkey, Jun. 13-15, 2007.

![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-5.jpg?height=318&width=256&top_left_y=243&top_left_x=1044)

Ehsan Azimi Rad received the B.Sc. degree in computer engineering and the M.Sc. degree in control engineering with honors from the Ferdowsi University of Mashhad, Mashhad, Iran, in 2006 and 2009, respectively.

His research interests are fuzzy control systems and its applications in urban traffic and any other problems, nonlinear control and etc.
![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-5.jpg?height=320&width=254&top_left_y=666&top_left_x=1044)

Naser Pariz received the B.Sc. and M.Sc. degrees in electrical engineering with honors from the Ferdowsi University of Mashhad, Mashhad, Iran, in 1988 and 1991, respectively. He received the Ph.D. degree from the Department of Electrical Engineering at Ferdowsi University of Mashhad, in 2001.

He was a Lecturer at Ferdowsi University of Mashhad from 1991 to 1995, where he is now Associate Professor. His research interests are power and control systems.
![](https://cdn.mathpix.com/cropped/61350a6e-025c-4ebb-bd7c-2c237b499d44-5.jpg?height=316&width=251&top_left_y=1098&top_left_x=1044)
M. B. Naghibi Sistani received the B.Sc. and M.Sc. degrees in control engineering with honors from the University of Tehran, Tehran, Iran, in 1991 and 1995, respectively and the Ph.D. degree from the department of Electrical Engineering at Ferdowsi University of Mashhad in 2005.

He was a Lecturer at Ferdowsi University of Mashhad from 2001 to 2005, where he is now Assistant Professor. His research interests are artificial intelligence and control systems.


[^0]:    Manuscript received July 08, 2009; revised November 02, 2009; accepted November 02, 2009. Date of publication March 29, 2010; date of current version April 07, 2010.
    E. Azimirad is with the Ferdowsi University of Mashhad, Mashhad, Iran, and also with the Electrical Engineering Department, Khorasan University, Mashhad, Iran (e-mail: eh_az77@yahoo.com).
    N. Pariz was with the Ferdowsi University of Mashhad, Mashhad, Iran. He is now with the Electrical Engineering Department, Ferdowsi University of Mashhad, Mashhad, Iran (e-mail: n-pariz@um.ac.ir).
    M. B. M. Sistani was with the Ferdowsi University of Mashhad, Mashhad, Iran. He is now with the Department of Electrical Collage, Ferdowsi University of Mashhad, Mashhad, Iran (e-mail: naghib@yahoo.com).
    Digital Object Identifier 10.1109/JSYST.2010.2043159

