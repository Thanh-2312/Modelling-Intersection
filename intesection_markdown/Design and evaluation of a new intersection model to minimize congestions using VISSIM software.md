Research Article
Jana Fabianova*, Peter Michalik, Jaroslava Janekova, and Michal Fabian

# Design and evaluation of a new intersection model to minimize congestions using VISSIM software 

https://doi.org/10.1515/eng-2020-0019
https://doi.org/10.1515/eng-2020-0019
Received Oct 30, 2019; accepted Dec 11, 2019
Received Oct 30, 2019; accepted Dec 11, 2019

Abstract: Traffic modelling and simulation is one of the frequent tools used in road infrastructure design. Software tools designed for traffic simulations are an important supportive tool in decision-making and in choosing the optimal solution. The aim of this paper is to introduce the application of the VISSIM program, in the design and testing a model of the traffic-light-controlled intersection. The traffic on the selected congested intersection is modelled and simulated first for the current state, then for two models with modifications that are to increase the throughput of the intersection. The monitored criterion of the intersection throughput is the length of queues. Both adjustments have led to a significant reduction of the number of vehicles waiting in direction of the greatest congestions. In the first model, the average line length was reduced by 75\%, and in the second model, the modifications lead to a fluent passage of right-turn vehicles and a significant reduction in vehicle lines for other directions.

Keywords: traffic-light-controlled intersection, traffic modelling, simulation, VISSIM

[^0]
## \section*{1 Introduction}

Traffic modelling and simulations have an irreplaceable place in transport infrastructure planning. Designing road networks and intersections, analysing traffic situations to eliminate congestion, reducing vehicle delays and improving road safety are the subject of many research works. Most of them are based on the creation and analysis of microscopic models. One of the interesting approaches to signal programming was introduced by Yu et al. [1]. In order to optimize signal timing for isolated intersection, the authors proposed a new method based on fuzzy programming approach. This method and the traditional method was compared and analysed through simulation software. In the research by Yuniawan et al. [2] a simulation method was implemented in order to manage the traffic queue. As the tool to modelling the traffic queue line Arena Simulation software was used. Sommer et al. discussed in [3] the need for bidirectional coupling of network simulation and road traffic microsimulation. They developed the hybrid simulation framework Veins (Vehicles in Network Simulation), composed of the network simulator OMNeT++ and the road traffic simulator SUMO. Chen et al. [4] proposed a nearby traffic flow modelling solution based on builtin Cyber-Physical System sensors of autonomous vehicles. Their model helps to select the optimal speed, the optimal distance for timing to brake, and the safe distance from other vehicles. Mesoscopic traffic simulation is used for handling large-scale dynamic traffic problems. In [5] an ideal grid network and a realistic Singapore expressway network were implemented and compared. Further interesting studies presenting traffic modelling and simulation methods were published in [6-11].

Safety is emerging as an area of increased attention and awareness within transportation engineering [12]. This fact is reflected in many works which are focused on the traffic safety issue. Wang et al. [13] proposed a combined usage of microscopic traffic simulation and Extreme Value Theory for safety evaluation. The effect of driver's characteristic on the stability of traffic flow was examined by [14]. The authors investigated the effect of anticipation parameter with more aggressive drivers, and it was found
that it has a positive effect on the stability of traffic flow dynamics. Essa and Sayed [15] investigated the relationship between field-measured conflicts and simulated conflicts estimated from microsimulation model (PARAMICS) using the surrogate safety assessment model. The issue of safety on roads in connection with modelling and simulation was dealt with also in [16-19].

Transport modelling uses a wide range of software tools whose functionality and comparison has been the subject of a number of research works. A comparison of 17 simulation software tools has been conducted by [20]. An online survey with the focus on traffic simulation tool developers, functionalities and planned improvements of softwares was performed. Mahmud et al. [21] critically reviewed micro-simulation modelling applications for traffic safety evaluation with respect to the use of different simulation tools. The study by [22] compared the performance of SimTraffic and VISSIM simulation tool in modelling dual lane and triple lane roundabouts under different scenarios. However, the software tools did not show statistically significant difference. Bloomberg and Dale [23] used CORSIM and VISSIM as tools for the traffic analysis and applied two-model approach to make the analysis more reliable and the results more defensible. The traffic simulation model AVENUE, developed in Japan, was described by [24] in terms of its traffic modelling and applications. As can be seen, there is a wide choice of simulation tools, but one of the most widespread softwares used for micro-simulation modelling in transport is VISSIM. This is also due to its very good performance and outputs quality. Modelling and simulation in VISSIM are also presented in [25-29].

The paper presents the use of the VISSIM microsimulation tool in designing and testing the capacity of a signalized intersection. The main contribution of this paper is the proposal of two intersection models leading to the elimination of congestion during peak hours.

## 2 Research problem definition

The traffic section we will deal with is a traffic-lightcontrolled intersection in Spisská Nová Ves, Slovakia. It is a crossroad of streets Duklianska and Sládkovičova, which is located on the main road of the city and is also an entrance to the city center. The problem of the intersection is the occurrence of traffic congestions, especially in the afternoon, mostly in one direction of the intersection. This congestion is caused by a few of factors, such as the presence of a railroad crossing with a long waiting time, an OMV petrol station, a department store, a bus and railway station. It is also one of the access roads to the housing estate, causing an increased number of vehicles. Traffic congestions are formed on Duklianska Street in direction to the city, most often at the time of the afternoon rush hours. Through a simulation model in the VISSIM environment, real traffic corresponding to peak hours will be simulated and analyzed. Subsequently, based on the layout options of the intersection, its new model will be designed to increase the throughput of the intersection for the most exposed direction.

### 2.1 Description and analysis of the selected intersection

The analyzed intersection is four-armed, light-controlled. Entrance A to the intersection is three-lane (left, straight and right lane), other B, C and D entrances are two-lane. The problematic direction D has two lanes. One lane is for left turn and the other lane is common for straight and right turn. The other entrances B, C are two-lane (Figure 1, 2).

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-2.jpg?height=502&width=818&top_left_y=1285&top_left_x=1034)
Figure 1: Satellite view of the intersection

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-2.jpg?height=407&width=818&top_left_y=1897&top_left_x=1031)
Figure 2: Diagram of driving lanes and sequence of control phases at the intersection [30]

Table 1: Usage of signal programs
| Working days |  | Saturdays |  | Sundays + State holydays |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Time interval | Signal program | Time interval | Signal program | Time interval | Signal program |
| 00:00-06:00 | Amber light | 00:00-06:00 | Amber light | 00:00-06:00 | Amber light |
| 06:00-21:00 | P2/90s | 06:00-14:00 | P2/90s | 06:00-24:00 | P1/75s |
| 21:00-24:00 | P1/75s | 14:00-24:00 | P1/75s |  |  |


![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-3.jpg?height=577&width=1176&top_left_y=599&top_left_x=465)
Figure 3: Number of vehicles crossing the intersection from direction D

### 2.2 Time regime of the regulation

The intersection is equipped with light signals, which is divided into 3 time intervals. The first time interval if the signal program is P1 from 14:00 to 24:00 and the cycle lasts 75 seconds. It is followed by a flashing amber light from 00:00 to 06:00. From 06:00 to 14:00, the P2 signal program is switched on with a 90 seconds cycle. Overall, there are four traffic lights for cars and two pedestrian traffic lights at the intersection. The width of the traffic lanes at the intersection is approximately 3 meters. Time intervals vary across weekdays, Saturdays, Sundays and public holidays. The main signal program is P2/90s, which lasts from 6:00 to 21:00 during weekdays. Table 1 shows the daily usage of signal programs.

The intersection has four control phases for a coordinated controlling mode. Currently the order of the control phases shown in Figure 2 is used. Since the traffic situation for the working day will be addressed, the analysis and simulation concerns only the P2/90s signal program.

### 2.3 Traffic survey

The term of the traffic survey was 6 March 2018 (Tuesday) and 13 March 2018 (Tuesday) on the intersection of the streets Duklianska and Sládkovičova. Due to the fact that

Table 2: Structure of traffic flow
| Vehicle type | Identification | Notes |
| :--- | :--- | :--- |
| Cars | C | Not exceed 3.5 tonnes |
| Motorcycles | M |  |
| Heavy Goods Vehicle | HGV | Over 3.5 tonnes |
| Buses | B |  |


the most problematic situation at the intersection is in the afternoon on weekdays, the term of the traffic survey was 6 March 2018 from 15:00 to 16:00 and 13 March 2018 from 14:00 to 15:00 at the intersection from the direction D. Vehicle numbers were registered for a 15 minute interval and recorded in census sheets.

The numbers of vehicles that have crossed the intersection from the D direction in both lanes are shown in the tables (Table 3, Table 4). The course of traffic intensity in individual time intervals is shown in the graph in Figure 3, where the peak time and the intensity of traffic in peak time are clearly identified. In addition to the traffic intensity, vehicle types were also recorded. The types of vehicles crossing the intersection were passenger cars, motorcycles, Heavy Goods Vehicle and buses. Table 2 presents the structure of the traffic flow and the identification of individual types of vehicles.

Table 3: Traffic intensity - results of traffic survey 1st day [30]
| Date | Time | Direction | Vehicle type |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | C | M | HGV | B | Total |
| 6.3.2018 | 15:00-15:15 | 七 | 95 | 1 | 16 | 4 | 116 |
|  | 15:15-15:30 |  | 97 | 0 | 8 | 2 | 107 |
|  | 15:30-15:45 |  | 93 | 1 | 9 | 3 | 106 |
|  | 15:45-16:00 |  | 83 | 0 | 7 | 3 | 93 |
|  | 15:00-16:00 |  | 368 | 2 | 40 | 12 | 422 |
| 6.3.2018 | 15:00-15:15 |  | 29 | 0 | 4 | 3 | 36 |
|  | 15:15-15:30 |  | 32 | 0 | 1 | 7 | 40 |
|  | 15:30-15:45 |  | 29 | 0 | 3 | 3 | 35 |
|  | 15:45-16:00 |  | 22 | 0 | 5 | 7 | 34 |
|  | 15:00-16:00 |  | 112 | 0 | 13 | 20 | 145 |
| D Total | 15:00-16:00 |  | 480 | 2 | 53 | 32 | 567 |


Table 4: Traffic intensity - results of traffic survey 2nd day [30]
| Date | Time | Direction | Vehicle type |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | C | M | HGV | B | Total |
| 13.3.2018 | 14:00-14:15 | L | 78 | 0 | 6 | 3 | 87 |
|  | 14:15-14:30 |  | 88 | 2 | 12 | 1 | 103 |
|  | 14:30-14:45 |  | 91 | 0 | 12 | 2 | 105 |
|  | 14:45-15:00 |  | 92 | 1 | 14 | 2 | 109 |
|  | 14:00-15:00 |  | 349 | 3 | 44 | 8 | 404 |
| 13.3.2018 | 14:00-14:15 |  | 22 | 0 | 0 | 1 | 23 |
|  | 14:15-14:30 |  | 22 | 0 | 1 | 2 | 25 |
|  | 14:30-14:45 |  | 23 | 0 | 4 | 4 | 31 |
|  | 14:45-15:00 |  | 26 | 0 | 4 | 3 | 33 |
|  | 14:00-15:00 |  | 93 | 0 | 9 | 10 | 112 |
| D Total | 14:00-15:00 |  | 442 | 3 | 53 | 18 | 516 |


## 3 Traffic simulation

### 3.1 Creation of the intersection model

The VISSIM software tool is used to create the intersection model and to simulate the traffic. It is used for microscopic simulation, showing all traffic users and their interactions in one model. It enables accurately simulates automobile, rail and road public transport, pedestrians and cyclists.

The basis for creating the intersection model is a satellite image of the selected section of roads. Based on the scale in the image, the map is scaled to match the model's dimensions to the actual intersection dimensions. The modelling process starts by drawing straight roads and connecting them directly to the intersection map. In places where roads crossing conflict areas arise where the priority of vehicles in the event of an uncontrolled intersection

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-4.jpg?height=383&width=818&top_left_y=1727&top_left_x=1034)
Figure 4: Intersection model - conflict zones visualisation

needs to be defined. In our case, the conflict areas of the intersection remain passive (coloured yellow, see Figure 4), because it is a traffic light- controlled intersection.

Table 5: Traffic flow parameters
| Traffic flow from direction | Intensity of traffic flow [vehicles/h] | Division of traffic flow | Speed of vehicles in front of the crossroads [km/h] | Reduced vehicle speed inside the intersection [km/h] |
| :--- | :--- | :--- | :--- | :--- |
| D | 550 | 36:40:24 (D-A : D-B : D-C) | 40 | 12 |
| A | 300 | 2:1:2 (A-D : A-C : A-B) | 40 | 12 |
| B | 450 | 2:2:1 (B-A : B-D : B-C) | 40 | 12 |
| C | 290 | 1:1:1 (C-B : C-A : C-D) | 40 | 12 |


![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-5.jpg?height=370&width=1593&top_left_y=861&top_left_x=254)
Figure 5: Traffic composition from D direction entered in the simulation environment

### 3.2 Define traffic parameters for the simulation

Based on the data obtained from the traffic survey, the parameters of the traffic flow are defined. The traffic intensity from D direction is approximately 500-600 vehicles per hour, therefore it is set to 550 vehicles/hour in the simulation. According to the traffic survey, the total traffic flow from the D-direction is divided into the individual directions by the following ratio: D-C (24\%) and D-A, B (76\%). Its further division between directions A and B is determined by estimation, as well as the traffic intensity and the division of traffic flow from the other directions. The traffic flow parameters for all directions are given in Table 5. The traffic flow composition is determined for all directions the same according to the data obtained from the survey in direction D (Figure 5).

The traffic lights are only installed for vehicles, as the model only deals with vehicle traffic. Green for pedestrians does not affect the signal program for vehicles. The signal program for the current state entered in the simulation program VISSIM is presented in Figure 6. Locations of the traffic lights in the intersection model are shown in Figure 7.

### 3.3 Simulation results

The results of the simulation during 3,600 s showed the fact that the intersection has a low throughput. From D direction a series of vehicles quickly began to form, with the vehicles having to stop several times before crossing the intersection (Figure 8). The second queue of vehicles formed from the C direction, although the situation was not so critical, the crossing of the intersection also from this direction was not fluent.

To evaluate the overall situation, queue counters were set to the directions D and C to monitor the length of the vehicle line parameter. Average and maximum queue length have been measured. The current queue length is measured upstream by the queue counter and the arithmetic mean and the maximum is thus calculated per time interval. The maximum length of the line of vehicles in the direction D-A, B reached up to 121 m, the average length of the line was 79 m. In the direction C-A, D is the second major delay (max. line length 58 m). The queue length in the directions Cand D is presented in the Figure 9. In other directions the traffic was without significant delays (Figure 9).

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-6.jpg?height=866&width=1593&top_left_y=224&top_left_x=215)
Figure 6: Signal program - current status

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-6.jpg?height=491&width=818&top_left_y=1223&top_left_x=177)
Figure 7: Traffic lights locations - current status

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-6.jpg?height=398&width=816&top_left_y=1826&top_left_x=177)
Figure 8: Traffic congestion on the current intersection model

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-6.jpg?height=332&width=814&top_left_y=1227&top_left_x=1036)
Figure 9: Average and maximum length of the vehicle line: direction C and D

## 4 Design and verification of new intersection models

The problem of low intersection throughput will be solved in two ways in the following simulation models:

1. In the first model, a separate lane for the D-B direction will be added. It will be controlled by the signal sequence red - red/amber - green - orange and by the program alike direction D-B.
2. In the second model, this separate lane will not be controlled by traffic lights, with a flashing amber light. The priority of vehicles in this model will be defined by the priority rules function when vehicles from the D direction must give priority to all other vehicles crossing on green the intersection.

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-7.jpg?height=383&width=820&top_left_y=222&top_left_x=215)
Figure 10: Driving directions from direction D after adding a new driving lane

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-7.jpg?height=422&width=818&top_left_y=749&top_left_x=215)
Figure 11: Traffic situation at the 1st modified intersection model

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-7.jpg?height=319&width=812&top_left_y=1283&top_left_x=220)
Figure 12: Maximum and average line lengths for the1st modified intersection model

The simulation of traffic will be in both models under the same traffic conditions as the original intersection model.

### 4.1 Design of the 1st intersection model: added driving lane

The intersection model for the added driving lane is shown in Figure 10. Division of the original lane into three directions is at a point approximately 80 m from the intersection. The results of the simulation show that by adding a new lane, the throughput of the intersection significantly improved for direction. The average line length was only 19 m (approximately 75\% improvement) and the maximum

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-7.jpg?height=405&width=818&top_left_y=224&top_left_x=1072)
Figure 13: Traffic situation at the 2nd modified intersection model

![](https://cdn.mathpix.com/cropped/cd72a54b-bea4-4fa1-af65-ece5bd58453e-7.jpg?height=314&width=816&top_left_y=741&top_left_x=1074)
Figure 14: Maximum and average line lengths for the 2nd modified intersection model

line length was 75 m (approximately 30\% improvement) (Figure 11, 12).

### 4.2 Design of the 2nd intersection model: added driving lane, change of the signal program

In the second modified intersection model, the signal program was modified by disabling the D-A direction control and setting a continuous flashing orange light. At the same time, elements defining priority rules have been inserted at the intersection, i.e. give priority to drive for the D direction (orange lane) and the marked directions which have priority (green lanes). This modification of the intersection control will significantly accelerate the exit of vehicles from the D-A direction, which leaves the intersection almost fluently. The waiting time of vehicles and the length of the line from other directions have not been affected by this adjustment (Figure 13, 14).

## 5 Conclusions

At present, one of the frequent tools used in road infrastructure design is traffic modelling and simulation. Software tools designed for traffic simulations enable to verify parameters of the future road or intersection in a short
time and at low cost, they are a supportive tool in decisionmaking and in choosing the optimal solution.

The aim of this paper was to introduce the application of the VISSIM program, designed for road traffic microsimulations, in the design and testing of the traffic-lightcontrolled intersection model. The traffic on the selected problematic congested intersection was modelled and simulated first for the current state, then for two models with modifications that were to increase the throughput of the intersection. The monitored criterion of the intersection throughput was the length of vehicles line. The first modification of the intersection was the addition of a separate lane in the most exposed direction, while maintaining the current intersection control conditions by light signals. The second modification of the intersection represented except additional separate lane also adjustment of the traffic lights. Both adjustments have led to a significant reduction of the number of vehicles waiting in direction of the greatest congestions. In the first case, the average line length was reduced by 75\%, and in the second case, the modifications led to a fluent passage of right-turn vehicles and a significant reduction in vehicle lines for other directions. These modifications presented only some of the ways in which the adjustment of the layout or the signal plan could improve the traffic situation. In order to select the optimal solution, it would be necessary to examine more options, including their cost and safety implications. Because of that, these additional aspects, mainly costs and safety impacts, will be considered in future work.

Acknowledgement: This work has been supported by grant projects VEGA 1/0638/19, VEGA 1/0600/20, KEGA 009TUKE-4/2020, KEGA 012TUKE-4/2019 and APVV SK-SRB-18-0053.

## References

[1] Yu D, Tian X, Xing X, et al. Signal Timing Optimization Based on Fuzzy Compromise Programming for Isolated Signalized Intersection. Math Probl Eng; 2016: 1-12.
[2] Yuniawan D, Aang Fajar P., Hariyanto S, et al. Traffic queue modeling using arena simulation software (a case study of Mergan 4-Way intersection in Malang City). In: Puspitasari P, Suryanto AH, Lenggo Ginta T, et al. (eds) MATEC Web of Conferences. EDP Sciences, 2018. Epub ahead of print 21 September 2018. DOI: 10.1051/matecconf/201820402009.
[3] Sommer C, German R, Dressler F. Bidirectionally Coupled Network and Road Traffic Simulation for Improved IVC Analysis. IEEE Trans Mob Comput; 10: 3-15.
[4] Chen B, Yang Z, Huang S, et al. Cyber-physical system enabled nearby traffic flow modelling for autonomous vehicles. In: 2017IEEE 36th International Performance Computing and Communications Conference (IPCCC). IEEE, 2017, pp. 1-6.
[5] Song X, Xie Z, Xu Y, et al. Supporting real-world network-oriented mesoscopic traffic simulation on GPU. Simul Model Pract Theory; 74: 46-63.
[6] Bartuska L, Stopka O, Lizbetin J. Methodology for determining the traflc volumes on urban roads in the Czech Republic. In: 19th Int. Sci. Conf. on Transp. Means (22-23 Oct 2015 Kaunas, 55 Lithuania), Kaunas University of Technology. 2015, pp. 215-218.
[7] Hlatká M, Bartuška L, Ližbetin J. Application of the vogel approximation method to reduce transport-logistics processes. In: MATEC Web of Conferences, 134, In: 18th Int. Sci. Conf., LOGI 2017, Ceske Budejovice. Ceske Budejovice, 2017, pp. 1-8.
[8] Ližbetin J, Stopka O. Proposal of a Roundabout Solution within a Particular Traflc Operation. Open Eng 2016; 6(1):441-445.
[9] Brumerčík F, Krzywonos L. Integrated Transportation System Simulation. Logi - Sci J Transp Logist; 4: 5-10.
[10] Stopka O, Cejka J, Kampf R BL. Draft of the novel system of public bus transport lines in the particular territory. In: 19th Int. Sci. Conf. on Transp. Means (22-23 Oct 2015 Kaunas, Lithuania). Kaunas, 2015, pp. 39-42.
[11] Kubasakova I, Kubanova J, Poliakova B. Modelling of Opened 70 System in the Road Freight Transport and its Impact on the System Characteristics. In: 19th Int. Sci. Conf. on Transp. Means (22-23 Oct 2015 Kaunas, Lithuania). 2015, pp. 405-409.
[12] Gettman D, Head L. Surrogate Safety Measures from Traffic Simulation Models. Transp Res Rec J Transp Res Board; 1840: 104-115.
[13] Wang C, Xu C, Xia J, et al. A combined use of microscopic traffic simulation and extreme value methods for traffic safety evaluation. Transp Res Part C Emerg Technol; 90: 281-291.
[14] Sharma S. Lattice hydrodynamic modeling of two-lane traffic flow with timid and aggressive driving behavior. Phys A Stat Mech its Appl; 421: 401-411.
[15] Essa M, Sayed T. A comparison between PARAMICS and VISSIM in estimating automated field-measured traffic conflicts at signalized intersections. J Adv Transp; 50: 897-917.
[16] Jurecki R, Poliak M, Jaśkiewicz M. Young Adult Drivers: Simulated Behaviour in a Car-following Situation. PROMET - Traf- fic\&Transportation; 29: 381-390.
[17] Metelski A. Analysis of selected methodological problems regarding the examination of traflc events at road intersections. Arch Automot Eng - Arch; 82: 75-85.
[18] Dižo J, Blatnický M, Melnik R. Assessment of the Passenger Ride Comfort for a Coach by Means of Simulation Computations. LOGI - Sci J Transp Logist; 8: 24-32.
[19] Kolla E, Ondruš J, Vertal' P. Reconstruction of traflc situations from digital video-recording using method of volumetric kinetic mapping. Arch Automot Eng - Arch Motoryz; 84: 147-170.
[20] Pell A, Meingast A, Schauer O. Trends in Real-time Traffic Simulation. Transp Res Procedia; 25: 1477-1484.
[21] Mahmud SMMS, Ferreira L, Hoque MS, et al. Micro-simulation modelling for traffic safety: A review and potential application to heterogeneous traffic environment. IATSS Research; 43: 27-36.
[22] Shaaban K, Kim I. Comparison of SimTraffic and VISSIM Microscopic Traffic Simulation Tools in Modeling Roundabouts. Procedia Comput Sci; 52: 43-50.
[23] Bloomberg L, Dale J. A Comparison of the VISSIM and CORSIM Traffic Simulation Models. Transp Res Rec J Transp Res Board; 1727: 52-60.

[24] Kuwahara M, Horiguchi R, Hanabusa H. Traffic Simulation with AVENUE. In: Fundamentals of Traffic Simulation. 2010, pp. 95-129.
[25] Fedorko G, Rosová A, Molnár V. The application of computer simulation in solving traffic problems in the urban traffic management in Slovakia. Theor Empir Res Urban Manag; 9: 5-17.
[26] Nyame-Baafi E, Adams CA, Osei KK. Volume warrants for major and minor roads left-turning traffic lanes at unsignalized Tintersections: A case study using VISSIM modelling. J Traffic Transp Eng (English Ed; 5: 417-428.
[27] Neradilová H, Fedorko G. The Use of Computer Simulation Methods to Reach Data for Economic Analysis of Automated Logistic Systems. Open Eng; 6: 700-710.
[28] Chen M. Modeling and Simulation Analysis of Road Network Based on VISSIM. In: 2019 International Conference on Intelligent Transportation, Big Data \& Smart City (ICITBS). IEEE, 2019, pp. 32-35.
[29] Fellendorf M, Vortisch P. Microscopic Traffic Flow Simulator VIS-SIM. In: Fundamentals of Traffic Simulation. Springer, New York, NY, 2010, pp. 63-93.
[30] Hambor L. Analysis of the traffic situation on the selected transport section in Spišská Nová Ves using simulations. Technical University of Kosice, 2018.

[^0]:    *Corresponding Author: Jana Fabianova: Technical University of Kosice, Faculty of Mining, Ecology, Process Control and Geotechnology, Institute of Logistics, Park Komenskeho 14, 04200 Kosice, Slovak Republic; Email: jana.fabianova@tuke.sk
    Peter Michalik: Technical University of Kosice, Faculty of Manufacturing Technologies, Bayerova 1, 08001 Presov, Slovak Republic; Email: peter.michalik@tuke.sk
    Jaroslava Janekova: Technical University of Kosice, Faculty of Mechanical Engineering, Institute of Management, Industrial and Digital Engineering, Park Komenskeho 9, 04200 Kosice, Slovak Republic; Email: jaroslava.janekova@tuke.sk
    Michal Fabian: Technical University of Kosice, Faculty of Mechanical Engineering, Department of Automotive Production, Kosice, Slovak Republic; Email: michal.fabian@tuke.sk

