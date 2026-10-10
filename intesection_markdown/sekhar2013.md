# Estimation of Delay and Fuel Loss during Idling of Vehicles at Signalised Intersection in Ahmedabad 

Ch.Ravi Sekhar ${ }^{\text {a* }}$ Pranoy Raj ${ }^{\text {b }}$, Purnima Parida ${ }^{\text {c }}$, S.Gangopadhyay ${ }^{\text {d }}$<br>${ }^{a}$ Senior Scientist, Transportation Planning Division, CSIR-Central Road Research Institute,New Delhi 110025,India<br>${ }^{b}$ Master Student, Transportation Engineering, National la Institute of Technology, Suratkal, Suratkal, Rajasthan-333031<br>${ }^{c}$ Principal Scientist and Head Transportation Planning Division, CSIR-Central Road Research Institute,New Delhi 110025,Indiae<br>${ }^{d}$ Director, CSIR-Central Road Research Institute,New Delhi 110025,India


#### Abstract

The fuel consumption of the vehicles is increasing day by day as a result of enhanced trip lengths, personal mode of transport and congested intersections. When the vehicles are waiting for their turn to cross the intersection at signals, the drivers normally keep their vehicle's engine on and a result of this extra fuel is consumed. This small amount of fuel wasted aggregated over a number of cycles per day, number of days per year and number of signalized intersections results in a huge quantity of fuel. Measuring delay is important in computing the level of service provided to road users at signalized intersection. Intersection delays may include queue delay and control delay. The signalized intersection capacity and LOS estimation procedures are built around the concept of average control delay per vehicle. Control delay is the portion of the total delay attributed to traffic signal operation for signalized intersections and this delay can be categorized into deceleration delay, stopped delay and acceleration delay. In India mainly two methods were using to estimate control delay those are field measurement and theoretical/analytical measurement. Field measurement of control delay includes the use of test-car observations, path tracing of individual vehicles, and the recording of arrival and departure volumes at Intersection but this expensive for long period. Analytical delay models of traffic systems are structured in a demand-supply framework and these models deals with the macroscopic method to estimate delay measurements. Whereas micro simulation based models are capable to estimate the individual delay of each vehicle at intersection and these models works on car following theory. The main objective of present study is to estimate delay and fuel loss during idling vehicles at signalized intersections in Ahmedabad city. For estimation of delay at intersections, typical corridor on drive in road in Ahmedabad city has been considered. Drive in road is one the busiest urban arterial corridor and this corridor connects the traffic coming from Thaltej intersection to Vijay Char Rasta Intersection.


16 hours classified traffic volume count surveys were conducted at four intersections falls in study corridor to observe the traffic volume and traffic composition. GPS based Velocity-Box (V-Box) apparatus was fitted in car to identify the existing speed and delay characteristics on the study corridor. VISSIM micro simulation software was adopted to simulate the traffic movement on the study corridor and to estimate the total delay including idling delay at the intersection. Base Case model

[^0]was developed for the study corridor and the model has been validated on statistical grounds by using GEH statistics. The GEH is a widely used statistics for comparing the modelled values and observed values evolved through simulation tools. After validation, the developed model has been deployed to estimate the idling delay of each vehicle type at the intersection and this was compared with the observed data collected through floating car method. Fuel loss due to idling of vehicles at each intersection was estimated by considering available fuel loss data exists with CSIR-CRRI. Mitigation measures such as grade separated intersection were proposed in this study to reduce the fuel consumption on the study corridor. Further these mitigation measures were implemented in VISSIM model to quantify the reduction in fuel loss due to idling at each intersection. Comparative evaluation was made between base case and proposed scenario for the study corridor. It can be concluded that the micro simulation based technique is the most suited approach to estimate idling delay at the intersection. It was concluded from the study that minor geometric improvements and stabilizing the signal timings suggested for the corridor seems to reduce the delays and idling time drastically on the study corridor.
© 2013 The Authors. Published by Elsevier Ltd.
Selection and peer-review under responsibility of International Scientific Committee.
Key words: Idling Delay,VISSIM, Fuel Consumption

## 1. Introduction

The fuel consumption of the vehicles is increasing day by day as a result of enhanced trip lengths, personal mode of transport and congested intersections. When the vehicles are waiting for their turn to cross the intersection at signals, the drivers normally keep their vehicle's engine on and as a result of this extra fuel is consumed. This small amount of fuel wasted is aggregated over a number of cycles per day, number of days per year and number of signalized intersections resulting in a loss of huge quantity of fuel. Ahmedabad, commercial capital of Gujarat, is one of the emerging urban centres of India. The Greater Ahmedabad Urban Agglomeration (GAUA) has a population of 6.3 million (Census of India, 2011) that accounts for $25 \%$ of the urban population of the State of Gujarat. The city has the fourth highest share (9.2\%) amongst the total registered vehicles in India (MoRTH, 2009) and this city has a registered motor vehicle population of 12.9 millions. The urban agglomeration of Ahmedabad comprises a roadway system of approximately 3478 km excluding the National Highways (CRRI, 2012). The exponential increase in the number of vehicles in the city has resulted in congestion at intersections. This has in-turn resulted in the need to install traffic signals. However, the ever increasing vehicular flow is found to cause heavy delays at intersections due to stoppage of vehicles during the red-phases of the signals. The wastage of fuel at these junctions result in a huge amount of valuable fuel resources.

This study provides an estimate of the total fuel loss in the study corridor due to stoppage of vehicles at intersections. The study area considered in this work is a 2.9 km stretch starts from Sal Hospital intersection to Vijay Char Rasta intersection. The objectives of this study include the study of delays and turning movements at each intersection, quantification of fuel loss during idling, estimation of total fuel loss, and estimation of benefits in terms of fuel savings by implementing improvement measures. The vehicle characteristics were defined and classified traffic volume data was provided as input to VISSIM model. The model parameters such as the vehicle characteristics and driver behavior characteristics are calibrated. So that the simulated values of arrival volumes at the approaches to intersections tallied with the observed values. This exercise was performed using traffic volume related data compiled by CRRI ( CRRI 2012). After model calibration and validation was performed so that the simulated traffic volumes, speeds and delay tally closely with the field-data. The simulation of speed and delay was performed for the existing scenario and for the proposed improvements in the road network. The estimated savings in fuel was also computed.

## 2. Literature Review

Delay at signalized intersections is associated with the time lost to a vehicle and or driver because of the operation of the signal and the geometric and traffic conditions present at the intersection. Delay in the Highway Capacity Manual (HCM 2000) context is defined as the difference between the travel time actually experienced and the reference travel time that would result during ideal conditions; in the absence of traffic control, in the absence of geometric delay, in the absence of any incidents, and when there are no other vehicles on the road. There are several different types of delay that can be measured at an intersection, and each serves a different purposes in the transportation engineering. The signalized intersection capacity and LOS (level of service) estimation procedures are built around the concept of average control delay per vehicle. Control delay is the portion of the total delay attributed to traffic signal operation for signalized intersections. Control delay (overall delay) can be categorized into deceleration delay, stopped delay and acceleration delay. Stopped delay is easier to measure, while overall delay reflects better the efficiency of traffic signal operation. Stopped delay is defined as the delay incurred when a vehicle is fully immobilized, while the delay incurred by a decelerating or accelerating vehicle is categorized as deceleration and acceleration delay, respectively.

Various components of vehicular delay at signalized intersection, including control delay used in the HCM, are shown in Fig. 1 (Quiroga and Bullock, 1999). In HCM 2000, control delay is comprised of initial deceleration delay, queue move-up time, stopped delay, and final acceleration delay, though in earlier versions it included only stopped delay. From the figure 1, it is observed that several vehicles reaching the intersection come to a complete stop. These vehicles need to stop either as a consequence of their arrival during the red interval or during the green interval when the queue of vehicles that had formed during the previous red interval has not yet fully dissipated. While it is further observed that the rest vehicles only experience deceleration and acceleration delay, as these vehicles reach the intersection when all previously queued vehicles have already started to move and therefore only need to slow down to maintain a safe distance with the vehicles ahead of them.

![](https://cdn.mathpix.com/cropped/bbf5beed-4378-4e1b-8f32-ea2c9e9bd04c-03.jpg?height=324&width=556&top_left_y=1219&top_left_x=653)
Fig. 1. Delay Terms at Signalized Intersection

Shipchandler et al. (2008) estimated the total quantity of emissions produced from idling vehicles in the Chicago metropolitan area using reasonable assumptions. It was done by developing an emission factor and multiplying it with total number of vehicles and total idling time. Li et al. (2009), an advanced driving alert system that provides traffic signal status information to help drivers avoid hard braking at intersections, defines a method for evaluating vehicle energy consumption and emissions at intersections. According to the preliminary simulation study, the savings on fuel consumption was as much as 8\% and the reduction of CO2 emissions can be around 7\% for each vehicle when traffic was in medium congestion (Velocity to Capacity is 0.7) under the current settings.. Lim (2012), study on 'Exhaust Emissions from Idling Heavy-Duty Diesel Trucks and Commercially Available Idle-Reducing Devices', the emissions and fuel consumption data generated from this study, the test data showed that on average, a class-8 truck could emit 144 g/hr of NOX and $8224 \mathrm{~g} / \mathrm{hr}$ of $\mathrm{CO}_{2}$, and could consume about 0.82 gal/hr of diesel fuel and the use of idling reduction devices lessen the emissions and fuel consumption.

VISSIM is a microscopic, time step and behavior based simulation model developed to model urban traffic and public transit operations. The program can analyze traffic and transit operations under constraints such as
lane configuration, traffic composition, traffic signals, transit stops, etc., thus making it a useful tool for the evaluation of various alternatives based on transportation engineering and planning measures of effectiveness. The traffic simulator in VISSIM is a microscopic traffic flow simulation model including the car following and lane change logic. Gomes, et al. (2004) presented a construction and calibration of a detailed congestion micro simulation model of free way and this was applied to a fifteen mile stretch I-210 west of Pasadena in California. Menedez (2012), has done a sensitivity analysis on Zurich road network. Trueblood et al. (2003) studied the effectiveness of using the VISSIM in simulating six proposed two-lane roundabouts along Missouri Avenue in St. Robert, Missouri, U.S.A. It was observed that VISSIM was capable of providing a reasonable assessment of the traffic flow at the roundabouts. VISSIM was found to be flexible, allowing the user to code different roadway scenarios, and fine-tune driver behavior through lane choice and travel speeds. Stanek et al. (2004) performed study on comparing macro-simulation software such as RODEL, and SIDRA against micro-simulation software such as VISSIM, and PARAMICS for a high capacity roundabout in East First Avenue interchange on State Route 99 (SR-99) in Chico, California and for the Placerville Drive/Forni Road interchange on U.S. Highway 50 (US-50) in Placerville, California. The micro-simulation approach was found to be more suited in modeling individual driving behavior, and in calibrating real field traffic conditions. The motivation of using VISSIM tool to the present study is to estimate idling delay at various intersection on the study corridor. This is discussed in the subsequent sections.

## 3. Study Area

The city of Ahmedabad was founded in 1411 AD as a walled city on the eastern bank of the river Sabarmati, now the seventh largest metropolis in India and the largest in the state of Gujarat. In the region, several SEZ's are being proposed. Given these trends the city will experience rapid growth in population and travel demand. The city is preparing for future challenges, more importantly in terms of sustaining its contributions to the growth of vehicle population. Drive in road is one of the most busy corridor in Ahmedabad city. In this study, a corridor of 2.9 kilometers length starting from Sal Hospital Intersection to Vijay Char Rasta Intersection has been considered in this study. Figure 2 presents the study area and various intersections between the study corridor.

![](https://cdn.mathpix.com/cropped/bbf5beed-4378-4e1b-8f32-ea2c9e9bd04c-04.jpg?height=252&width=993&top_left_y=1348&top_left_x=288)
Fig. 2. Study Area: Drive in Road from Sal Hospital to Vijaya Char Rasta Intersection, Ahmedabad

## 4. Traffic Data Collection

Classified traffic volume counts and speed and delay surveys were carried out to assess the existing traffic volume, composition and travel speed characteristics at the identified intersections and in their vicinity. These are briefly discussed in the following subsequent sections.

### 4.1 Classified Traffic Volume Count Data

Classified traffic volume with turning movement's survey was carried out for all the four intersections fall in this corridor. Intersection traffic surveys were conducted to assess the mode-wise traffic volume and composition observed at each intersection. Traffic surveys at intersections were carried out on normal working days of the week for a 16-hour period from 7:00 AM to 10:00 PM and thus classified turning movements at the
intersections were arrived at. The composition-wise observed traffic flows were converted into equivalent Passenger Car Units (PCU) by considering static PCU Factors for Various Types of Vehicles on Urban Roads (IRC: 106-1990). The summary of Total volume of traffic(16 Hours) and the peak hour traffic for all the four intersections is presented in Table 1. The hourly distribution of traffic volume and composition of traffic presented in Figure 3. This corridor contains the mix of high volume, medium volume and low volume intersections.

![](https://cdn.mathpix.com/cropped/bbf5beed-4378-4e1b-8f32-ea2c9e9bd04c-05.jpg?height=1175&width=860&top_left_y=506&top_left_x=506)
Fig. 3. Hourly Variation and Composition of Vijay Char Rasta Intersection

Sal Hospital Intersection is four arms signalized intersection. At this junction motorized two wheelers composition (44\%) are predominant than the car (34.5\%) followed by Autos 13.6\%. It was observed that cycles compositions is significant at this junction is about 4.3\%. The total percentage of goods vehicles was about 2.2\% and also the share of buses is $1 \%$. Himalaya Intersection is three arm junction formed by meeting of Drive in road and sunrise park road. At this intersection motorized two wheelers composition (48\%) are predominant than the car (26.1\%) followed by Autos 18\%. Helmet Intersection is one of the major four arm intersections falling on the end of Driving Road. This junction is formed by meeting of Drive in Road, Manav Mandir Road and 132 ft Ring Road. The straight traffic plying from Gujarat University to Mem Nagar does not pass through this intersection because of the flyover. This is signalized intersection facilitating operation of Bus Rapid Transport (BRT) at
grade in the direction of Gujarat University to Mem Nagar. Two wheelers (40\%) are dominant traffic than the car traffic (25\%) followed by Goods vehicles (15.2\%) and Autos 13.5\%. Vijay Char Rastais is four arm signalized intersection formed by meeting of Manav Mandir road and 120 ft Circular Road. This one of the busiest intersections on Manav Mandir road located after Helmet intersection. Two wheelers composition (45\%) are predominant in the traffic stream compared to cars (29.5 \%) and autos (14\%).

Table 1 Summary of Total volume of traffic(16 Hours) and the peak hour traffic for all the four intersections.
| Sr No | Name of the Intersection. | Type of Intersection | Total Volume (16 Hours) |  | Peak Hour Volume |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | Vehicles | PCU | Vehicles | PCU |
| 1 | Sal Hospital intersection | Four | 107233 | 111016 | 10754 | 10855 |
| 2 | Himalaya intersection | Three | 74972 | 79991 | 6916 | 7355 |
| 3 | Helmet intersection | Four | 17345 | 19091 | 17345 | 19091 |
| 4 | Vijay Char Rasta | Four | 93645 | 99,517 | 8921 | 8915 |


### 4.2 Speed and Delay Data Collection

Speed and delay survey was carried out on Drive in Road starting from Thaltej intersection(Before 1km from al Hospital Intersection ) to Vijay Char Rasta Intersection. The total length of 4.5 km corridor was considered to study the travel speed characteristics of the study corridor. The speed profiles of the entire corridor during morning peak, evening peak and off peak hours are presented at Figure 4. These speed profile data were collected through probe vehicle technique (V-Box). Red color profile from the figure indicates that the speed profile along the study corridor (Thaltej to Vijay Char Rasta) during the early morning hours (6:44AM). Similarly Speed profile was measured during morning peak hour (Blue color) and Evening peak hour (Green line). From the figure it can be observed that the average journey speed is 19 kmph during morning peak and 20 kmph during evening peak.. The average running speed is 26 kmph for morning and evening periods. The main delays on this corridor are due to traffic signal and merging of traffic at un-signalized intersection. The maximum delays during morning peak hour were at Sal Hospital junction Helmet and Vijay Char Rasta. During evening peak hours maximum delays were observed at Helmet junction.

![](https://cdn.mathpix.com/cropped/bbf5beed-4378-4e1b-8f32-ea2c9e9bd04c-06.jpg?height=266&width=643&top_left_y=1433&top_left_x=490)
Fig. 4 Travel Speed Characteristics on Study Corridor

## 5. Estimation of Idling Delay and Fuel Consumption

### 5.1 Development of Model in VISSIM

Heterogeneous traffic on Indian roads, compounded with highly transient traffic composition and presence of motorized and non-motorized vehicles having diverse static and dynamic characteristics brings in the need for a carefully developed simulation model. It is required to maintain precision and compliance to real-world scenario in modeling traffic, as it affects the predictive capability of the model. VISSIM is a stochastic, time step based
microscopic traffic flow simulation program developed to model urban and highway operations. The model has two main internal components such as traffic flow simulator that replicates vehicle movements and the signal state generator, which determines the signal status based on detector information coming from the traffic simulator on time-step basis. The traffic flow model used by the traffic simulator relies mainly on two models named as "Wiedemann 74" car following model or the "Wiedemann 99" car following model. Both of these models developed based on a psycho-physical car-following model and a rule-based algorithm for lateral movements. In this study Wiedemann 99 car-following model was considered and this model is similar to Wiedemann 74 car following model, except that some of the thresholds in the Wiedemann 99 model are defined in a different way to model traffic better. This model employs ten different driver behaviour related parameter sets such as CC0 to CC9 to describe the different driving scenarios such as free-driving, approaching, following and braking. The input model parameters have to be appropriately defined while developing simulation model in VISSIM. These parameters mainly include vehicular characteristics, desire speed distributions, Traffic flows and composition, signal control parameters and driving behavior parameters namely car-following and lane change. Except driving behavior parameters all other parameters were considered from the observed field data. The adopted methodology considered in VISSIM model has been discussed briefly in the following paragraphs

### 5.2 Model Calibration and Validation

The value of CC0 (Standstill distance) was considered as 0.50 m instead of 1.50 m based on free flow speed and jam density conditions observed on urban arterial conditions in the Ahmedabad. All other parameters from CC1 to CC9, the default values of VISSIM were considered (VISSIM ). By giving these parameters as an input, simulation runs have been carried out and estimated the output. In the present simulation model, travel times ,travel speed and delay of the vehicles are considered as output since the observed data on this parameter was collected in the field for validation of the developed simulation model. The comparison of estimated values with observed values is carried out and error is estimated. Based on the estimated error, the modification of the parameters has been done and simulation runs are carried out. This process is carried out and simulation runs are made till the error is in the satisfactory level. Further the validated simulation model was considered for estimation of travel time, Speed and delay under mitigation measures. In this study, provision of fly over was considered on every intersection along the direction drive in road. The travel time and travel speed behavior under this scenarios is further used to measure the fuel estimation before and after scenario. Model validation was done by comparing between modeled and observed traffic volume using Geoffrey E. Havers (GEH) statistic. GEH statistic, widely used in traffic simulation model to compare two sets of traffic volume. The formula for estimation GEH statistics is given in equation (1).

$$
G E H=\sqrt{\frac{2(M-C)^{2}}{M+C}}
$$

Where M is the traffic volume obtained from simulation model and C is the observed traffic volume. A GEH value lesser than 5 between modeled and observed data is considered a good match for traffic modeling work. A lower GEH value indicates a much higher accuracy for the data set. The simulated traffic volume was compared with the real-world traffic volume data available, for the entire road network. Initially the least GEH statistic value was found to be 7, which was greater than the limiting value of 5. Further simulations were performed by fine-tuning the Driver Behavior parameters. The GEH values were then found to be mostly lesser than 5. The calibration of the model was done and the GEH statistic was found out for the 165 links in the developed simulation model. The calibration results shows that 89.1 percent of links (147 links) have GEH statistic within 5 and the rest 10.9 percent of links (18 links) have a GEH statistic between 5 and 10. Since more than 85 percent of links have GEH statistic less than 5 the flows can be considered a good fit. Validation is usually done with a traffic volume data of another data of another day. But validation is also comparing the data
on the field to the data from the simulation. So here the validation is done with the comparison of the delays obtained in the junction with respect to the V-box data collected from the field. The data for validation is from the speed and delay survey and calibration is done using the traffic volume data survey. The average error in Sal Hospital to Vijay Char Rasta was observed as $13.89 \%$ (Table 2)

Table 2 Validation of the Simulation For Morning Peak Hour
| Time | Junction | Delay observed from field by V-box (seconds) | Delay estimated by Simulation model (seconds) | Percentage of error (\%) |
| :--- | :--- | :--- | :--- | :--- |
| Sal Hospital to Vijay Char Rasta | Sal Hospital | 39.4 | 44.24 | 12.28 |
|  | HImalaya | 21 | 23.21 | 10.47 |
|  | Helmet | 56.5 | 67.19 | 18.94 |


### 5.3 Delay and Idling Time Estimation

The validated VISSIM model was considered to estimate total delay measurement at intersection. Total delay is defined as a combination of a single or several travel time measurements; regardless of the selected vehicle classes, all vehicles concerned by these travel time measurements are also regarded for delay time measurement. The delays in the developed VISSIM model were estimated by introducing travel time sections in all the arms of a intersection with more than the observed queue length. The delays are calculated in when the vehicle speed goes below 5km/hr. The delay output in the weighted average of the total delay occurring in the junction comparing the three or four arms for each vehicle category. The output file also has a stopped time or idle time in delays which is the total time when the vehicle is not moving i.e. at zero km/hr. Table 3 presents the summary of total delays and Idling delay for 16hours (7:00AM to 10 PM)at various intersections on the study corridor.

Table 3 Summary of Total delays and Idling Delay for 16 hours at various Intersection on Study Corridor
| Veh Type | Helmet |  | Himalaya |  | Sal Hospital |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Total Delay (Sec) | Idling Delay (Sec) | Total Delay (Sec) | Idling Delay (Sec) | Total Delay (Sec) | Idling Delay (Sec) |
| Car | 842.5 | 641 | 497.8 | 419 | 654.9 | 567.4 |
| Minibus | 780.5 | 621.3 | 620.2 | 543.5 | 614.9 | 526.6 |
| Bus | 962.2 | 712.1 | 611.9 | 484.8 | 681.9 | 548.6 |
| 2 wheelers | 846.7 | 626.2 | 492.3 | 404.2 | 643.4 | 551.5 |
| Light | 766.2 | 657.2 |  |  |  |  |
| Vehicles(LCV) |  |  | 818.6 | 737 | 754.7 | 669.1 |
| Heavy | 922.6 | 748.6 |  |  |  |  |
| Vehicles |  |  | 815 | 718.7 | 653.9 | 559.7 |
| Multi axis Vehicles | 625 | 557.4 | 400 | 357.9 | 297.1 | 251.1 |
| 3 Wheeler Passenger | 825.3 | 627 | 452.6 | 382.9 | 619.8 | 542.8 |
| 3 Wheeler Goods | 848.8 | 703.2 | 568.5 | 499.6 | 633.1 | 562.5 |
| Total | 7419.8 | 5894 | 5276.9 | 4547.6 | 5553.7 | 4779.3 |


### 5.4 Estimation of idling fuel consumption

Fuel consumption test at idling flow measurement system comprising FP 213S detectors DF 210A flow meters (CSIR-CRRI 2009 and Gangopadhyay, S and Parida, P. (2009). The Idling fuel consumption in ml/hour and gm/hour of different type of vehicles is given Table 4. These values are considered for estimating of Idle fuel consumption at
three main Junctions in the study corridor. The total fuel consumption is estimated by multiplying the idle time with the idling fuel consumption and with the total number of vehicles of each category in each intersection Table presents the idling fuel consumption per day for Sal Intersection, Himalaya Intersection and Helmet Intersection.

Table4 Idling Fuel Consumption in ml/hr ( CSIR-CRRI 2009 and Gangopadhyay, S and Parida, P. (2009) )
| Sl. no | Vehicle Type | Fuel Consumption (ml/Hr) | Remark | Sl. no | Vehicle Type | Fuel Consumption (ml/Hr) | Remark |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Maruti Gypsy | 1045 | Petrol | 10 | Taxi | 1010 | CNG |
| 2 | Maruti Van | 692 | Petrol | 11 | Tata Sumo | 717 | Turbo Change |
| 3 | LML Motor Cycle | 129 | 4 stroke | 12 | Tata Indica | 547 | Diesel |
| 4 | Pulsar Motor Cycle | 166 | 4 stroke | 13 | Esteem | 740 | Petrol |
| 5 | Bajaj Scooter | 216 | 2 stroke | 14 | LCV | 690 | Diesel |
| 6 | Honda Activa | 118 | Petrol | 15 | HCV | 920 | Diesel |
| 7 | Ambassador Car | 952 | Diesel | 16 | MAV | 1240 | Diesel |
| 8 | Mahindra Jeep | 1052 | Diesel | 17 | Bus | 3610 | CNG |
| 9 | Hyundai Santro | 563 | Petrol | 18 | Autorickshaw | 700 | CNG |


Table5 Idling Fuel Consumption in ml/hr
| Name of Intersection | PETROL (Liters) | DIESEL Liters) | CNG Liters) |
| :--- | :--- | :--- | :--- |
| Sal Hospital Intersection | 307.4386 | 81.94491 | 178.1452 |
| Himalya Intersection | 127.4014 | 39.07578 | 107.586 |
| Helmet Intersection | 486.6723 | 358.1164 | 361.2284 |


### 5.5 Mitigation measures

To reduce the delay at intersections mitigation measures such as optimisation traffic signals based on the traffic on various arms, Geometric improvements at intersections and provision of grade separated facilities along the main direction of traffic flow. In this study, the Flyovers are proposed along the drive in road and the same has been implemented in validated VISSIM model. Flyovers are developed in the simulation model to assess the forecasting of delays. It was found there has been a drastic reduction in the total delay and Idling delay when the flyovers are provided on the study Intersections. This has been presented in table 6. From Table 6 it can be identified that on an average 74\% of idling delay can be reduced by considering the provision of Flyovers on Drive in road . High percentage of idling time savings was observed at Helmet Intersection (88.5\%) because this junction is three arm intersection. The idling delay at Helmet will be reduced to 79\% , high reduction in idling delay was observed because, at this intersection already splitted Fly over exits on the direction of BRTS corridor.

Table 6 Total delays and Idling Delay at various Intersection by Provision of Grade Separated Facility
| Delay Category | Helmet |  | Himalaya |  | Sal Hospital |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Total Delay (Sec) | Idling Delay (Sec) | Total Delay (Sec) | Idling Delay (Sec) | Total Delay (Sec) | Idling Delay (Sec) |
| Existing Total Delay (Sec) | 7419.8 | 5894 | 5276.9 | 4547.6 | 5553.7 | 4779.3 |


| Estimated Delay With Grade Separated |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Facility along Drive in Road (Sec) | 1897.3 | 1244.8 | 733.1 | 522.4 | 2602.1 | 2177.1 |
| Reduction of Delay | 5522.5 | 4649.2 | 4543.8 | 4025.2 | 2951.6 | 2602.2 |
| Reduction of Delay (\%) | 74.4\% | 78.9\% | 86.1\% | 88.5\% | 53.1\% | 54.4\% |

## 6. Conclusions

This study proposes a methodology for development, calibration, and validation of a micro simulation model of a 2.9km long stretch. it was observed that the errors for the simulation model in VISSIM were varying from 10.47 to $18.94 \%$ for all the three major intersections in the forward flow with an average error of $13.89 \%$. Comparing the observed and estimated classified volumes for the calibration of the selected route, it is also observed that the prediction-errors for the simulation model in VISSIM were in the permissible range. The error is found to vary from $0.1 \%$ to $15 \%$ with an average error of $4.95 \%$ which is considered good fit.

The fly-over was proposed to be provided with a gradient of 1 in 30, and a straight level span of 50 m extending over a total length of varying from 300m to 500m. The future model developed with flyovers gave results which showed that the delays and traffic flow were more desirable after the introduction of the fly-overs at the intersections. Further fine tuning of the model is required to improve the reliability of the results. From this study, it could be concluded that VISSIM is a very powerful software tool for traffic simulation. It could handle large networks and also simulate the Indian traffic scenario satisfactorily. However, the parameters of vehicle and driver characteristics are to be fine-tuned in calibration.

## References

Census of India (2011) Rural Urban Distribution of Population, Ministry of Home Affairs to Government of India, India. Available at http://pib.nic.in/prs/2011/latest31mar.pdf. Accessed on 16th November, 2012.
CRRI Report ( 2009) Study on Losses of Petroleum Products at Traffic Intersections due to idling of vehicles at Delhi
CRRI Report (2012) Traffic Studies for Junction Improvement of major corridors of Ahmedabad City, Submitted by Central Road Research Institute (CRRI), New Delhi to Ahmedabad Municipal Corporation.
Gangopadhyay, S and Parida, P. (2009), Estimation of Fuel Loss during Idling at Signalized Intersections in Delhi, Indian Roads Congress (IRC) ,Vol.12, pp.61-69.
Gomes, G. and Horowitz, R., (2004) Congested Freeway Micro simulation Model using VISSIM, Journal of Transportation Research Board no.1876, National Research Council, Washington D.C.
Highway Capacity Manual, (2000), Fourth Edition published by Transportation Research Board and National Academics of Sciences, Washington D.C., http://books.trbbookstore.org/hcm2km.aspx
Li, C. and Shimimoto, S.,(2012), ETC Assisted Traffic Light Control Scheme for Reducing Vehicles CO2 Emissions, International Journal of Managing Information Technology (IJMIT) Vol.4, No.2.
Lim, H.,(2012), Study of Exhaust Emissions from Idling Heavy-Duty Diesel Trucks and Commercially Available Idle-Reducing Devices submitted at U.S. Environmental Protection Agency.
Menedez, M., (2012) Sensitivity Analysis for calibrating VISSIM in Modelling the Zurich Network, 12th Swiss Transport Research Conference.
MoRTH Road Transport Year book (2009), Ministry of Road Transport and Highways (MoRTH). Available at website: http://morth.nic.in/ writereaddata/ mainlinkFile/ File420.pdf. Accessed on 23rd Dec 2012.
PTV (2011) VISSIM 5.4 User Manual, PTV-AG (Planung Transport Verkehr) , Karlsruhe, Germany (CD-ROM),
Quiroga, C. A., and Bullock, D. (1999), Measured Control Delay at Signalized Intersections, Journal of Transportation Engineering Vol. 12No. 4.
Shipchandler, R. and Miller, J., (2008), Estimating Smog Precursor Emissions From Idling Vehicles In The Chicago Metropolitan Area Illinois Sustainable Technology Center Institute of Natural Resources Sustainability University of Illinois at Urbana-Champaign Submitted to the Metropolitan Mayors Caucus 177 North State Street, Suite 500 Chicago, Illinois
Stanek, David and Milam, Ronald T. (2004), High-Capacity Roundabout Intersection Analysis: Going Around in Circles, Fehr \& Peers Associates, Inc., Roseville, California
Trueblood, M and Dale, J (2003), Simulating Roundabouts with VISSIM, Proc. 2nd Urban Street Symposium, Transportation Research Board, Anaheim, California, July.


[^0]:    * Corresponding author: Tel.: +98698501882; fax: +91-11-26845943
    E-mail address: chalumuri.ravisekhar@gmail.com

