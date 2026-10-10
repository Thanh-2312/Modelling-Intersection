![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-01.jpg?height=339&width=323&top_left_y=165&top_left_x=77)

Transportation Letters
The International Journal of Transportation Research

ISSN: (Print) (Online) Journal homepage: https://www.tandfonline.com/loi/ytrl20

# Assessment of service quality at unsignalized intersections using traffic simulation and computational intelligence 

Suprava Jena , Sharmili Patro , Manish Dutta \& P.K. Bhuyan

To cite this article: Suprava Jena , Sharmili Patro , Manish Dutta \& P.K. Bhuyan (2020): Assessment of service quality at unsignalized intersections using traffic simulation and computational intelligence, Transportation Letters, DOI: 10.1080/19427867.2020.1868179

To link to this article: https://doi.org/10.1080/19427867.2020.1868179

Published online: 26 Dec 2020.

Submit your article to this journal

Article views: 53

View related articles

View Crossmark data

# Assessment of service quality at unsignalized intersections using traffic simulation and computational intelligence 

Suprava Jena ${ }^{\text {(1) }}$, Sharmili Patro ${ }^{\text {b }}$, Manish Dutta ${ }^{\text {c }}$ and P.K. Bhuyan ${ }^{\text {b }}$<br>${ }^{\mathrm{a}}$ Department of Civil Engineering, National Institute of Technology Silchar, Silchar, India; ${ }^{\mathrm{b}}$ Department of Civil Engineering, National Institute of Technology Rourkela, Rourkela, India; ${ }^{\mathrm{c}}$ Department of Civil Engineering, G H Raisoni College of Engineering, India


#### Abstract

The focus of this study is to examine the service quality of unsignalized intersections based on the perception of automobile drivers. This was achieved by developing Automobile Level of Service (ALOS) models using two computational intelligence methods - Functional Linked Artificial Neural Network (FLANN) and Differential Evolution (DE). The required data were collected at 47 unsignalized intersections in India with widely varying driving environments. Traffic simulation models were developed to estimate parameters that could not be directly measured in the field. DE model exhibited higher prediction efficiencies with coefficient of determination $\left(R^{2}\right)$ of 0.94 and 0.93 for training and testing datasets, respectively. Applying sensitivity analysis, significant parameters affecting ALOS were arranged in descending rank of their relative influence. Pavement condition is the most significant parameter influencing ALOS of unsignalized intersections. The proposed model will help the transportation administrators in prioritizing the key factors for investment in infrastructural development.


## KEYWORDS

- Unsignalized Intersections; automobile level of service; traffic simulation; functional linked artificial neural network; differential Evolution; sensitivity analysis


## Introduction

Since the start of rapid urbanization, road networks over many parts of the world have witnessed considerable growth in traffic volume, leading to congestion. Simultaneously, the supply of transportation infrastructure has gradually increased to improve accessibility and meet the requirements of road users. Ensuring the sustainability of infrastructure has become a primary concern due to more number of traffic conflicts, especially at road crossings and intersections. Therefore, the establishment of an efficient transportation network is obligatory to manage the traffic growth at road crossings and intersections. However, there exist a significant proportion of unsignalized intersections in developing cities, in which, entrance into the intersection from none of the approaches is controlled by regulatory signs (i.e. STOP or YIELD) (Patil and Pawar 2014). Analyzing such intersections is complex, as the arrival rate and the manner of vehicular operation are generally determined by individual drivers. The resultant performance is derived from collective replication of flow environments, drivers' decision and behavior patterns. Generally, unsignalized intersections are more prone to accidents, as vehicles of nonpriority streams frequently seek gaps in the opposing streams (Patil and Pawar 2016). Hence, these intersections require an improved driving environment and a better Level of Service (LOS) to map its user satisfaction for comfortable and safer vehicular movement under the prevailing road conditions.

## Background studies

Some researchers have carried out comprehensive research work related to the performance assessment of unsignalized intersections. The main service attributes that significantly affect LOS at unsignalized intersections were found to be traffic volume for each approach, critical gap, and traffic volume by Jamil and Ibrahim (2013). Caliendo (2014) developed a delay-time model and concluded that, the delay time and stop time on minor roads increases with conflict traffic volume than approach traffic volume, while the reverse was found for maximum queue length. Performance of unsignalized intersections was assessed by Chodur and Ostrowski (2015) considering the randomness of traffic sub-processes as well as the non-stationarity of vehicles like vehicle speed, critical headways, and headways between vehicles entering from a queue and driver behavior to estimate the capacity and to assess. Aakre and Aakre (2017) suggested one micro-simulation model by considering drivers' cooperative behavior and queue spillbacks on major road traffic stream to assess unsignalized intersections, where, the drivers' co-operative behavior combines both gap-acceptance behavior and turn-taking process of drivers.

The conception of safety LOS was proposed by Pan et al. (2013) for unsignalized intersections, and it was found that the combined effect of delay and risk index improves the overall LOS at unsignalized intersections. Safety performance at unsignalized intersections also revealed that traffic conflicts at intersection increase with the increase of time headway and speed of vehicles in eastbound major road traffic (Zhang, Chen, and Zhao 2017). Likewise, with the increase in volume and speed of left-turning minor road vehicles increases the traffic conflicts at unsignalized intersections.

Unsignalized intersections in India are characterized by the absence of explicit priority rules and mixed traffic conditions. As a result, traffic operation and management at such intersections have always been a challenge. One of the studies shows that service delay experienced by the priority stream vehicles becomes more, if the traffic flows heterogeneous (Ashalatha and Chandra 2011a). On estimating the performance of two-wheelers at limited priority T-intersections, it was found that the driving attitude depends on demographic characteristics, and conflicting vehicle types encountered by the subject vehicles (Patil and Sangole 2016). Spatial critical gaps estimated under Indian unsignalized intersections show that
the values are smaller than those reported in developed countries indicating aggressive driving behavior (Patil and Pawar 2014, 2016; Pawar and Patil 2019). Mohan and Chandra $(2016,2018)$ have compared popular critical gap estimation techniques for two-way stop-controlled intersections and introduced a new method of estimation using the occupancy time of a vehicle.

To improve the service quality of unsignalized intersections, the prevailing geometric, traffic, and built-environmental characteristics along with drivers' perception need to be assessed. Highway Capacity Manual (HCM) estimates LOS based on control delay, which appears as inappropriate for the context of Indian traffic because of drivers' aggressiveness (HCM 2010). Hence, a modified version of HCM has been published in India, which is popularly known as Indo-HCM (2017). This manual considers volume to capacity ratio as the influencing parameters to assess the performance of unsignalized intersections in developing countries. However, the driving environment at unsignalized intersections is influenced by several in-built environmental elements like, unauthorized on-street parking turnover, vending activities, disruptions by slow-moving traffic or opposing encounters, etc., which are not addressed in previous studies. Ignoring drivers' perception, any intersection improvement measure might experience a strong condemnation. In light of this, the present study investigates the influence of a varied range of road characteristics in mixed traffic flow conditions to justify existing approaches of evaluating offered service quality at unsignalized intersections.

This study proposes a novel approach for modeling Automobile Level of Service (ALOS) offered by unsignalized intersections. The overall methodological framework is divided into different phases. The first phase is to investigate the influential service attributes, which were gathered from unsignalized intersections having extensively varying driving environments. The second phase is to develop simulation models of the study intersections in VISSIM to ease the process of estimating some traffic parameters, which requires an extensive data collection effort. The third phase includes the implementation of evolutionary algorithms to identify the most efficient ALOS model to enhance the service quality of unsignalized intersections. The fourth phase includes the execution of sensitivity analysis, which arranges the road service attributes in decreasing value of their relative significance. Lastly, several improvement strategies are outlined based on the sensitivity analysis report, which would support the transportation engineers to prioritize investments in prevailing intersection facilities. The detailed methodology to achieve the objective of this study is shown in Figure 1.

## Selection of study intersections

Detailed exploration of an urban driving environment will require the setting up of a well-diversified database, which is given due consideration in this study for carrying out a comprehensive analysis of the ALOS. Essential quantitative as well as qualitative information were gathered from 193 approaches of 47 unsignalized intersections from three Indian cities, namely, Hyderabad, Kolkata,

![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-03.jpg?height=1268&width=1191&top_left_y=1294&top_left_x=463)
Figure 1. Methodology followed to estimate $A L O S_{\text {unsig }}$ for unsignalized intersections.

and Rourkela. Out of these, 40 intersections are four-legged and seven- are three-legged intersections. The intersections were selected so that there is variation in lane configuration, speed limit, road surface quality, land use, parking density, and percentage of heavy vehicles. Figure 2(a) shows the locations of the selected cities on a map, and (b) some typical images of unsignalized intersections operating under a range of best to the worst driving environment during peak hours of the day.

## Data collection and extraction

To attain the objective of this study, both quantitative and qualitative parameters affecting the driver's comfort level at unsignalized intersections were considered in the process of data collection. These variables were extracted 'approach wise,' which served as a database while developing the ALOS model for unsignalized intersections. The timings of data collection were chosen during both morning (8:00 AM-11:00 AM) and evening peak hours (3:30 PM-6:30 PM), to replicate the worst traffic situations, when drivers had frequently reported to find insufficient space to maneuver or park their vehicles. The traffic flow data on weekends and holidays were not recorded as the vehicular maneuvers are comparatively low and irregular on these days.

## Selection of quantitative service attributes

To summarize the most expected Quality of Service (QOS) parameters for a comprehensive ALOS model, difference in drivers' level of satisfaction regarding the existing transportation facilities have been exposed to a lot of research and discussion. The term quantitative parameter refers to the road geometrical, traffic operational, and builtenvironmental variables, which were quantified by in-situ investigations and videotaping. A pilot questionnaire survey was conducted to gather basic information related to the QOS attributes affecting drivers' comfort level on urban unsignalized intersections. Based on the findings of the pilot survey, feasible quantitative parameters considered in this study were listed out with their corresponding units in Table 1.

The road dimensional or geometric parameters like the width of median, effective road width, etc. were recorded using a measuring tape and expressed in meters. In-situ investigations were carried out to

![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-04.jpg?height=1555&width=1199&top_left_y=1012&top_left_x=459)
Figure 2. (a) Map showing locations of the study intersections in India. (b) Unsignalized intersections operating under best to worst driving environment.

Table 1. Extracted QOS parameters collected from unsignalized intersections.
| Sl. no. | QOS parameters | Units |  |
| :--- | :--- | :--- | :--- |
| 1 | No. of lanes | in number |  |
| 2 | No. of Intersection legs | in number |  |
| 3 | Effective road width | in metre |  |
| 4 | Pavement condition index | rating scale: 1-5 |  |
| 5 | Service delay | in second |  |
| 6 | Speed of vehicles | in km/h |  |
| 7 | Critical gap | in second |  |
| 8 | Motorized traffic volume | in PCU/h |  |
| 9 | Non-motorized traffic volume | in PCU/h |  |
| 10 | On street pedestrian volume | in number |  |
| 11 | Composition of heavy vehicles | \% in total traffic |  |
| 12 | Direction of traffic movement | one-way | 1.0 |
|  |  | both way | 0.5 |
| 13 | Presence of median barrier | absent | 0.0 |
|  |  | present | 0.5 |
|  |  | raised median and width $\geq 500 \mathrm{~mm}$ | 1.0 |
| 14 | Presence of camber | absent | 0.0 |
|  |  | present | 0.5 |
|  |  | proper | 1.0 |
| 15 | Presence of grade separated sidewalk | absent | 0.0 |
|  |  | present | 1.0 |
| 16 | Presence of separate bike lane | absent | 0.0 |
|  |  | present | 1.0 |
| 17 | Land use pattern | residential (no/low on-street commercial density) | 0.0 |
|  |  | mixed (medium on-street commercial density) | 0.15 |
|  |  | commercial (high on-street commercial density) | 0.3 |
| 18 | On-street parking turnover | absent (< 5\%) | 0 |
|  |  | low (5-25\%) | 0.13 |
|  |  | moderate (25-45\%) | 0.27 |
|  |  | high (> 45\%) | 0.4 |
| 19 | Interruptions due to frequently stopping public transits ahead | presence of bus pull-out lane | 0.0 |
|  |  | frequency | 0.15 |
|  |  | moderate | 0.3 |
|  |  | high | 0.45 |
|  |  | very high | 0.6 |
| 20 | Average time interval to face an encounter |  |  |
|  |  | in minute |  |


examine the pavement surface quality, road markings, camber slope, presence or absence of median, etc. High-resolution video cameras fitted on tripod stands were used to directly record the traffic flow parameters like, service delay, on-street pedestrian volume, and composition of different types of vehicles in the traffic mix during the period of data collection. The running average method was used to decide one peak hourly traffic volume (PHV) among the periods of rush conditions. The conversion factors cited for various groups of automobiles in Indian Road Congress IRC: 106 (1990) were used to compute the PHV. The obstructions in driving originated from few other sources, like road-side parking, the intensity of vending activities in the adjoining areas, bus-stops, slow-moving nonmotorized vehicle, and encounters, are examined with reference to the adjustment factors, proposed by Jena, Chakraborty, and Bhuyan (2018).

## Estimation of critical gaps and service delays using traffic simulation

Among the various input variables considered in Table 1, critical gap and service delay estimation require a large data extraction effort. These need to be estimated using other measurable data such as gap, occupancy time, waiting time, etc. (Chandra, Agrawal, and Rajamma 2009; Mohan and Chandra 2018). To reduce the computation time, critical

Table 2. Default and calibrated values of the global calibration parameters in VISSIM.
| Driving behavior | Parameter | Symbols | Units | Default values | Calibrated values |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Wiedemann-74 Car Following Parameters | average standstill distance | ax | m | 2.00 | 1.40 |
|  | additive part of safety distance | bx_add | - | 2.00 | 0.24 |
|  | multiplicative part of safety distance | bx_mult | - | 3.00 | 0.19 |
| Lateral Behavior | minimum look ahead distance | lad_min | m | 0 | 28 |
|  | minimum look back distance | lbd_min | m | 0 | 21 |
|  | minimum headway front rear | hw_min | m | 0.50 | 0.25 |
|  | Desired position at free flow |  |  | Middle | Any |
|  | Diamond shaped queuing |  |  | No | Yes |
|  | Consider next turning direction |  |  | No | Yes |
|  | Overtake on same lane |  |  | No | On left and right |
| Lane Change Behavior | minimum lateral distance (standing) | mld_st | m | 0.20 | 0.22 |
|  | minimum lateral distance (driving) | mld_dr | m | 1.00 | 0.50 |


[^0]![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-06.jpg?height=545&width=1690&top_left_y=183&top_left_x=213)
Figure 3. Positions of data collection points on the intersection corresponding to (a) minor road right turn movement, (b) minor road right through movement, (c) major road right turn movement at a typical four-legged intersection.

gaps and service delays of the study intersections were estimated using simulated data. The driving behavior of the study intersections was represented by car following behavior, lateral behavior, and lane change behavior using the global calibration parameters reported in Dutta and Ahmed (2019) (Table 2). The gap-acceptance behavior at unsignalized intersections is configured by representing the right-of-way rules followed by typical drivers at the study intersections. This was done by setting up priority rules as explained in Dutta and Ahmed (2019). To ensure that the adopted global calibration values represent the study intersections, the models were validated using the traffic flow and occupancy time as measures of effectiveness. The simulation models, having been validated, were run to generate the necessary data for estimating the critical gaps and service delays of the study intersections.

## Critical gap

Critical gaps have been estimated using the occupancy time method, which requires measuring gaps accepted and occupancy times (Mohan and Chandra 2018). The gap-acceptance data were extracted from the simulation models based on the concept of Influence Area For Gap Acceptance (INAFOGA) (Ashalatha and Chandra 2011b; Dutta and Ahmed 2020). Simulated gapacceptance data were obtained by placing data collection points at suitable locations to record the time stamps (Figure 3).

The gaps were estimated by recording the time stamps when the front and rear end of major street vehicles pass over the data collection point $\mathrm{D}_{2}$. The recorded time stamps were transferred to a spreadsheet to filter out the accepted gaps. A sample of the event timeline constructed from the raw data is presented in Table 3. The procedure is explained with reference to Table 3 and Figure 3.

- The time instant $\left(\mathrm{t}_{\mathrm{a}}\right)$ when the front bumper of a vehicle on any non-priority movement reaches $\mathrm{D}_{1}$ is noted. $\mathrm{D}_{1}$ is placed at the position of the conflict point inside the INAFOGA.
- The time interval between the instant when the rear bumper of a major road vehicle exits $\mathrm{D}_{2}$ just before $\mathrm{t}_{\mathrm{a}}\left(\mathrm{t}_{\mathrm{i}, \text { exit }}\right)$ and the instant when front bumper of the next major road vehicle reaches $\mathrm{D}_{2}$ just after $\mathrm{t}_{\mathrm{a}}\left(\mathrm{t}_{\mathrm{i}+1, \text { entry }}\right)$ is the accepted gap. In Table 3, the subject vehicle has reached $\mathrm{D}_{1}$ at $\mathrm{t}_{\mathrm{a}}=802.12 \mathrm{~s}$ which is between $\mathrm{t}_{\mathrm{i}, \text { exit }}=799.15 \mathrm{~s}$ and $\mathrm{t}_{\mathrm{i}+1, \text { entry }}=808.94 \mathrm{~s}$. So, the accepted gap is $\mathrm{t}_{\mathrm{i}+1 \text {, entry }}-\mathrm{t}_{\mathrm{i}, \text { exit }}=808.94 \mathrm{~s}-799.15 \mathrm{~s}=9.79 \mathrm{~s}$.

Table 3. Sample event time-line (in seconds) of a typical intersection showing gap and lag computation.
| Time tamps (s) |  |  |  | Gap (s) | Lag (s) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\mathrm{D}_{1}(\mathrm{~s}) \left(\mathrm{t}_{0}\right)$ | $\mathrm{D}_{2}(\mathrm{~s}) \left(\mathrm{t}_{\mathrm{a}}\right)$ | $\mathrm{D}_{5}(\mathrm{~s})$ ( $\mathrm{t}_{\mathrm{i}, \text { entry }}$ ) | $\mathrm{D}_{5}(\mathrm{~s})$ |  |  |
|  |  | ( $\mathrm{t}_{\mathrm{i}, \text { entry) }}$ ) | ( $\mathrm{t}_{\mathrm{i}, \text { exit }}$ ) $\left(\mathrm{t}_{\mathrm{i}, \text { exit }}\right)$ -- |  |  |
|  |  |  |  |  |  |
|  |  | 703.21 | 704.54 |  |  |
|  |  | 706.03 | 706.21 |  |  |
|  |  | 722.05 | 722.65 |  |  |
|  |  | 747.21 | 747.43 |  |  |
|  |  | 749.21 | 749.92 |  |  |
| 772.15 <br> 772.15 |  | $774.51\left(\mathrm{t}_{1 \text {,entry }}\right)$ | $775.9\left(\mathrm{t}_{1, \text { exit }}\right)$ |  |  |
|  |  | 778.98 | 785.45 | 3.08 |  |
|  |  | 786.34 | 791.66 | 0.89 |  |
|  |  | 795.85 | 796.11 | 4.19 |  |
|  |  | 798.82 | 799.15 | 2.71 |  |
|  | 802.12 | 808.94 | 812.54 | 9.79 (Accepted Gap) |  |
|  |  | 819.01 | 820.14 |  |  |
|  |  | 832.72 | 832.99 |  |  |
|  |  | 836.77 | 836.95 |  |  |
|  |  | 857.01 | 857.37 |  |  |
|  |  | 859.65 | 859.82 |  |  |
|  |  | 863.69 | 864.03 |  |  |
|  |  | 867.12 | 869.24 |  |  |
|  |  | - | - |  |  |
|  |  | - | - |  |  |


![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-07.jpg?height=482&width=799&top_left_y=181&top_left_x=192)
Figure 4. Critical gap estimation using occupancy time method.

The occupancy time of a vehicle on any non-priority movement is the duration between the instants when the front end of the vehicle enters $\mathrm{D}_{3}$ and when rear-end exits $\mathrm{D}_{4}$. The critical gaps of the three nonpriority movements were estimated by plotting the cumulative distribution curves of accepted gap and occupancy time (Mohan and Chandra 2018). The time coordinate corresponding to the point of intersection between the two curves is the critical gap (Figure 4).

## Service delay

Service delay is the average duration for which vehicles on the nonpriority movements wait at the stop line. This can be done using node evaluations. Nodes were created on the intersection approaches in such a way that only the front ends of the vehicles waiting at the stop line are accommodated within the node (Figure 5). This will ensure that the stopped delay of only the vehicles waiting at the stop line is recorded while running the simulation models. The node results will give the average-stopped delay of an approach, which is the service delay.

## Extraction of qualitative service attributes

This research includes a comprehensive questionnaire, which is divided into two phases (Figure 6). 'Phase-1' is prepared to record the demographic information of survey participants and 'Phase 2' is to rate the influencing service attributes affecting drivers' satisfaction level. People of different socio-economic classes were included in 'Traveler's intercept survey' to judge how the real-time response of drivers varies with respect to diverse road and traffic environments.

Real-time perception of 3700 drivers about the road attributes is extracted on an excel sheet to determine the overall satisfaction of each driver on respective approaches of an intersection. The percentage distribution based on different demographic characteristics of survey participants is presented in Table 4. Approximately 56\% of the drivers are male whereas the rest are females. Age classification shows that young population comprises of $38 \%$, the middleaged are found to be 48\% and the elderly people constitute 14\% of the total population, considered for the survey. A major percentage of automobile users ( $79 \%$ ) have a sound educational background above $10^{\text {th }}$ standard or equivalent. The remaining 21\% of the participants needed simplification of the questionnaire to give accurate responses. Thirty-one percent of drivers reported to have driving experience of $2-5$ years, $55 \%$ have an experience of 5-15 years while 14\% have greater than 15 years of driving experience. Fifty-three percent drivers are found to be using bikes, while, $23 \%, 10 \%$, and $14 \%$ drivers use cars, LCVs, and autos, respectively. All the trips were intended for various purposes like official work, business, school, marketing, etc. The purpose of reviewing sociodemographic variables in the dataset is to integrate contextual variation in data for considering as many differences as possible in drivers' behavior. The proposed methodology will thus have unanimous applicability of these study outcomes in forecasting unsignalized intersection service quality in developing countries.

The automobile drivers were either orally interviewed about the trip quality or were asked to fill the survey form based on their stated preference immediately after driving on a certain road. The motorists were well explained about the purpose of this study, and requested to answer their stated preferences on the service attributes included in 'Section B: Main Interview' of the prepared questionnaire on a Likert scale of 1 = extremely disappointed to $6=$ extremely satisfied. From each intersection, the average score of all responses with respect to different attributes of service quality were taken to determine the perceived Automobile Level of Service $\left(A L O S_{\text {unsig }}\right)$ on respective road intersections.

## Modeling approaches

Computational intelligence techniques are capable of achieving robustness on simulating human decision-making behavior with drastically reduced processing interval and great accuracy under minute control. Therefore, the current work has introduced the application of two novel evolutionary algorithms to develop a suitable ALOS model.

![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-07.jpg?height=512&width=1688&top_left_y=1964&top_left_x=215)
Figure 5. Positions of nodes corresponding to (a) minor road right turn movement, (b) minor road through movement, and (c) major road right turn movement for calculating service delay at a typical four-legged intersection.

## Road user's satisfaction survey

Dear user,
I would be grateful if you will spare some time to answer these questions. Your answer will be helpful for my research work on analyzing the extent of drivers' satisfaction for an unsignalized intersection. All responses will remain fully confidential and your answers will be used just as basic information for my research work, and not for any other purpose. Please indicate how important each of the following factors are to you by putting a tick mark (✓) next to the appropriate number. Your views are important to us in helping you with improved road infrastructure in our country.

Section A: Driver's personal profile
A1. Place of interview: $\_\_\_\_$
A2. Participant's Name (optional): $\_\_\_\_$
A2. Gender: □
□ Female

A3. Age: □ 18-25 years □ 26-45 years □ Above 45 years

A4. Educational level: □ >10th or equivalent □ <10th standard

A6. Driving experience (in years): $\_\_\_\_$
A7. Employment status: $\_\_\_\_$
A8. Category of Vehicle: $\_\_\_\_$
A9. Frequency of travel (per week): □ Once or less □ 2-5 times □ More than 5 times

Section B: Main interview
| Please indicate the extent to which you are satisfied with the following service attributes. Scale: 1= Highly dissatisfied, 6= Highly satisfied |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sl. No. | Factors | Rank |  |  |  |  |  |
| B1. | No. of lanes and width of the carriage-way to handle the traffic volume at peak hour | 1 | 2 | 3 | 4 | 5 | 6 |
| B2. | Availability of space to enter in to the main street from cross street during peak hour | 1 | 2 | 3 | 4 | 5 | 6 |
| B3. | U-turn capacity | 1 | 2 | 3 | 4 | 5 | 6 |
| B4. | Speed limit for through movement | 1 | 2 | 3 | 4 | 5 | 6 |
| B5. | Riding quality and smoothness of road surface | 1 | 2 | 3 | 4 | 5 | 6 |
| B6. | Cross slope of carriage way to promote drainage of surface water | 1 | 2 | 3 | 4 | 5 | 6 |
| B7. | Quality of road markings and visibility during day and night | 1 | 2 | 3 | 4 | 5 | 6 |
| B8. | Visual impact of frontage development like amount of landscaping on the street sides, median with trees etc. | 1 | 2 | 3 | 4 | 5 | 6 |
| B9. | On-street parking bays/facility, size and shape of the parking lot | 1 | 2 | 3 | 4 | 5 | 6 |
| B10. | Mixed zoning/ commercial activities on sides of the road way | 1 | 2 | 3 | 4 | 5 | 6 |
| B11. | Speed reduction due to public transits ahead, while loading/unloading passengers | 1 | 2 | 3 | 4 | 5 | 6 |
| B12. | Interruptions due to slow moving non-motorized traffic on the driveway | 1 | 2 | 3 | 4 | 5 | 6 |


B13. On an average how much delay do you experience?
□ No delay □ 1-5 min □ 5-10 min □ 10-15 min □ More than 15 min

And the delay is generally due to $\_\_\_\_$
If you have any additional comments/suggestion for further improvement in road intersection:

Thank you for your co-operation. Have a wonderful journey...

Figure 6. Survey questionnaire format.

## Functional linked ANN (FLANN)

FLANN is a single-layer feed-forward neural network with an extended width of input variables. ANN has one or more hidden layers. Hence, the overall figure of links is relatively outsized because of the association of neurons from individual input, hidden, and output layer. In the current perspective, FLANN is fairly strategic, as the number of links is fewer, which usually helps attaining a lower error assessment as preferred. In the linear expansion, the inputs are expanded with simple mathematical equations as addition, multiplication, division, and powers. E.g. $\mathrm{X}=\left[\mathrm{x}_{1}, \mathrm{x}_{2}\right]$ is the input parameters. In FLANN architecture, it can be expanded as $\mathrm{X}=\left[\mathrm{x}_{1}, \mathrm{x}_{2}, \mathrm{x}_{1} \mathrm{x}_{2}, \mathrm{x}_{12}, \mathrm{x}_{22}\right]$ as linear expansion and $\mathrm{X}=\left[\mathrm{x}_{1}, \mathrm{x}_{2}, \sin \left(\mathrm{x}_{1}\right), \cos \left(\mathrm{x}_{2}\right)\right]$ as trigonometric expansion. Sometimes, it is quite difficult to choose the number of hidden layers and the number of nodes for each layer in traditional neural networks. Hence, FLANN is a better option, to increase or decrease the input nodes with functional expansion upon the variables decidingALOS. During the expansion of the input space, it mimics the hidden layers and the input variables are directly connected with the output layer to show better optimization with faster convergence. Increasing the expansion size gives better prediction accuracy. The general form of single-layer FLANN architecture to develop an ALOS model is shown in Figure 7.

While training a FLANN network, the weights are updated as per the error plus a control factor (mu) to govern the error conjunction of individual phase (Jiang, Maskell, and Patra 2012). To improve the FLANN input space matrix, various trials were undertaken to discover the optimum expansion of input variables. Each trial consists of iterations, which update previously assigned weights in every step based on the accumulated error. The process is terminated in each step, when the maximum iteration is achieved

Table 4. Percentage distribution in demographic variables of Drivers.
| Attributes | Distributions | Percentage |
| :--- | :--- | :--- |
| Gender | Male | 56\% |
|  | Female | 44\% |
| Age | 18-25 years (Young age) | 38\% |
|  | 26-45 years (Middle age) | 48\% |
|  | >45 years (Old age) | 14\% |
| Educational background | Proper ( $>10^{\text {th }}$ or equivalent) | 79\% |
|  | Poor ( $\leq 10^{\text {th }}$ standard) | 21\% |
| Driving experience | 2-5 years | 31\% |
|  | 5-15 years | 55\% |
|  | >15 years | 14\% |
| Employment status | Employed | 88\% |
|  | Unemployed | 12\% |
| Types of vehicles | Bikes/Two- wheelers | 53\% |
|  | Cars | 23\% |
|  | LCVs | 10\% |
|  | Autos | 14\% |
| Frequency of using the road | Often | 79\% |
|  | Less frequently | 21\% |


![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-09.jpg?height=454&width=801&top_left_y=900&top_left_x=192)
Figure 7. Schematic diagram of FLANN architecture to predict ALOS_score.

or the target error is achieved. The process of weight update of individual iteration is governed by a Gradient Descent technique. So, ALOS is anticipated by using Eq. (1):

$$
\operatorname{ALOS}_{\text {unsig }}=\varphi\left[b+\sum_{i=1}^{n}\left(w_{i} * x_{i}\right)\right]
$$

where

$$
\begin{aligned}
& A L O S_{N}=\text { normalized ALOS value rang } \\
& b=\text { bias for output level, } \\
& w_{i}=\text { weight of } i^{t h} \text { input, } \\
& x_{i}=i^{t h} \text { input, } \\
& n=\text { number of inputs in extended space, } \\
& \varphi=\text { activation function }
\end{aligned}
$$

Each input parameter is normalized between an array [-1,1]. Hence, $A L O S_{\text {unsig }}$ was found out after denormalizing $A L O S_{N}$.

## Differential evolution (DE)

DE is a stochastic, population-based optimization algorithm evolved in optimizing real-valued functions (Reddy and Kumar 2007). Through several iterations, DE makes a population of candidate solutions, which converges to an optimum of the function. It is a variant of the Genetic Algorithm (GA) and can solve a global optimization problem over continuous space. DE, being an evolutionary algorithm, follows the general Evolutionary algorithm procedure, which is shown in Figure 8.

## Mechanism of DE

DE algorithm uses three main operators analogous to GAs, such as: mutation, crossover, and selection. Yet, DE relies greatly on mutation like a prime search mechanism to be discriminated from GA. Unlike GA, the candidate solutions are not reflected as binary strings, however, considered as real vectors. The focal aspect of DE is the dynamic mutation step size. That means, it adjusts to the alignment of the population and tends to become zero, when it converges. The predicted 'ALOS ${ }_{\text {unsig }}$ ' can be estimated using Eq. (2):

$$
A L O S_{\text {unsig }}=a_{0}+\sum_{i=1}^{n} a_{i} x_{i}
$$

where

$$
\begin{aligned}
& a_{0}=\text { the bias parameter, } \\
& n=\text { number of input variables in the target expression, } \\
& a_{i}=\text { linear coefficient of ' } i \text { th' variable } x_{i} \text {. }
\end{aligned}
$$

## Result and analysis

## Traffic simulation

Mean Absolute Percentage Errors (MAPEs) of traffic flow and occupancy time were found to be less than $15 \%$ for simulation models of all study intersections (Dowling et al. 2004). The models were also validated using GEH statistic, and the values were found to be less than 5, which indicates a good fit (Hollander and Liu 2008). This shows that the global calibration parameters presented in Table 2 represent the study intersections with reasonable accuracy. Out of 193 intersection approaches, field values of critical gaps and service delays were estimated for 10\% of the randomly selected approaches, i.e. 20 approaches, for comparing with those obtained from simulated data. It was found that the absolute percentage difference between the values obtained from field data and simulated data is less than $10 \%$ for each approach, which is considered acceptable. Having checked the reliability of the simulated data, critical gaps, and service delays were estimated for the rest of the intersection approaches using simulated data.

## Variables selection

Spearman's correlation analysis has been carried out to detect the sets of attributes having significant effects on perceived ALOS scores at approaches of unsignalized intersections. From Spearman's correlation analyses presented in Table 5, six variables with two-tailed significance $(p)<0.001$ are revealed - Pavement condition index (PCI), Presence of median (PoM), Critical gap $\left(t_{c}\right)$ for minor road vehicles, Land use pattern (LU), Interruptions due to oppositely moving encounters $\left(O_{E}\right)$, and Service delay $\left(T_{s}\right)$. These variables are accounted for the ALOS model development process in the present context for unsignalized intersections. A positive Spearman's correlation ( $\rho$ ) value for $P C I$, $P o M$, and $t_{c}$ indicates that the comfort level of automobile drivers increases with the

![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-09.jpg?height=121&width=995&top_left_y=2444&top_left_x=560)
Figure 8. General evolutionary algorithm procedure.

Table 5. Descriptive statistics and Spearman's correlation among variables.
| Variables |  |  |  | Spearman's correlation ( $\rho$ ) | Significance $(p)$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Pavement condition index (PCI) |  |  |  | 0.660 | 0.000 |
| Presence of median (PoM) |  |  |  | 0.546 | 0.000 |
| Critical gap $\left(t_{c}\right)$ |  |  |  | 0.416 | 0.000 |
| Land use pattern (LU) |  |  |  | -0.388 | 0.000 |
| Interruptions due to encounters ( $O_{E}$ ) |  |  |  | -0.467 | 0.000 |
| Service delay $\left(T_{s}\right)$ |  |  |  | -0.557 | 0.000 |
| Motorized traffic volume (PHV) |  |  |  | -0.120 | 0.070 |
| Non-motorized traffic volume (NMV) |  |  |  | -0.003 | 0.150 |
| On street pedestrian volume |  |  |  | -0.180 | 0.059 |
| Direction of traffic movement |  |  |  | 0.003 | 0.205 |
| Effective road width |  |  |  | 0.054 | 0.085 |
| \% of heavy vehicles |  |  |  | -0.211 | 0.058 |
| Presence of camber |  |  |  | 0.091 | 0.110 |
| Presence of grade separated sidewalk |  |  |  | 0.110 | 0.077 |
| Presence of separate bike lane |  |  |  | 0.070 | 0.073 |
| On-street parking turnover |  |  |  | -0.307 | 0.087 |
| Interruptions due to frequently stopping public transits ahead |  |  |  | -0.071 | 0.089 |
| Correlation among input variables |  |  |  |  |  |
| Variables |  | PoM | $t_{c}$ | LU | $O_{E}$ |
| PCI |  | 0.513 | 0.348 | -0.224 | -0.275 |
| PoM |  | 1.000 | 0.471 | -0.110 | -0.165 |
| $t_{c}$ |  | 0.471 | 1.000 | -0.084 | -0.095 |
| LU |  | -0.110 | -0.084 | 1.000 | 0.532 |
| $O_{E}$ |  | -0.165 | -0.095 | 0.532 | 1.000 |
| $T_{s}$ |  | -0.203 | -0.017 | 0.028 | 0.104 |
| Descriptive statistics of model attributes for unsignalized intersections |  |  |  |  |  |
| Variables | Range |  |  | Mean | Standard Deviation |
| PCI | 1-5 |  |  | 3.358 | 0.065 |
| PoM | 0-1 |  |  | 0.326 | 0.034 |
| $t_{c}$ | 0-3.73 |  |  | 1.445 | 0.080 |
| LU | 0-0.45 |  |  | 0.142 | 0.007 |
| $O_{E}$ | 0-0.2 |  |  | 0.096 | 0.004 |
| $T_{s}$ | 0-8.45 |  |  | 2.790 | 0.135 |
| $A L O S_{\text {unsig }}$ | 1.37-5.7 |  |  | 3.904 | 0.070 |


increase in pavement condition index, critical gap, and presence of median. Conversely, the negative $\rho$ value for $L U, O_{E}$, and $T_{s}$ indicates the reverse. The drivers do not experience smooth riding, if they encounter illegal on-street commercial activities, oppositely moving vehicles or pedestrians on the sides of drive ways. The remaining service attributes (with $p>0.001$ ) have comparatively more than one in a thousand chance of getting a more extreme value than the experimental value. Hence, they were dropped out from the process of model development for better accuracy and higher prediction performance.

## Prediction of ALOS ${ }_{\text {unsig }}$

FLANN model
FLANN model was developed by considering PCI, PoM, $t_{c}, L U$, $O_{E}$, and $T_{s}$, as input neurons and $A L O S$ score as an output node. During the development FLANN model, various trials were performed to expand the configuration of six input variables. Until that time, a fixed bias and weights are selected arbitrarily. Weights connected to them were found out by training the model using MATLAB. As there exists no hidden layer, the expanded input variables are directly linked with the output in this scenario. Within 50-60 iterations, the minimal value of error in the prevailing condition (i.e. RMSE<0.5) has been achieved. Different such FLANN models were configured, having fixed bias or without bias. Comparing the $R^{2}$, Root Mean Square Error (RMSE), and Overfitting Ratio (OR) values of different FLANN models, it was observed that in absence of bias, the model is predicting better results. The suitability of getting the best model expansion is found to have a combination of algebraic and trigonometric functions. The six input parameters are expanded to produce an extended

Table 6. Expansion and weights of input variables in FLANN model for unsignalized intersections.
| Sl. no. | Input variable | Weight | Sl. no. | Input variable | Weight | Sl. no. | Input variable | Weight |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | $a$ | 0.0006 | 9 | $c$ | 0.5994 | 17 | $e$ | -0.4858 |
| 2 | $\cos (a)$ | -0.1013 | 10 | $\cos (c)$ | 0.8073 | 18 | $\cos (e)$ | 1.4090 |
| 3 | $\sin (a)$ | -0.7887 | 11 | $\sin (c)$ | 0.2231 | 19 | $\sin (e)$ | -0.4814 |
| 4 | $\sin \left(\pi^{*} a\right)$ | 0.0004 | 12 | $\sin \left(\pi^{*} c\right)$ | 0.1395 | 20 | $\sin \left(\pi^{*} e\right)$ | -1.3826 |
| 5 | $b$ | 0.4178 | 13 | $d$ | -0.0142 | 21 | $f$ | -0.1201 |
| 6 | $\cos (b)$ | 1.1516 | 14 | $\cos (d)$ | 1.3110 | 22 | $\cos (f)$ | 0.0194 |
| 7 | $\sin (b)$ | 0.3509 | 15 | $\sin (d)$ | -0.0191 | 23 | $\sin (f)$ | 0.0821 |
| 8 | $\sin \left(\pi^{*} b\right)$ | 0.0002 | 16 | $\sin \left(\pi^{*} d\right)$ | -0.1947 | 24 | $\sin \left(\pi^{*} f\right)$ | -0.0220 |


input space of twenty-four transformations. Hence, the input variables PCI, PoM, $t_{c}, L U, O_{E}$, and $T_{s}$ are denoted by means of ' $a$,' ' $b$,' ' $c$,' ' $d$,' ' $e$,' and ' $f$ correspondingly to minimize the intricacy of presenting particulars of twenty-four expansions beside their linked connection weights. A detailed expansion of input space corresponding to their weights is presented in Table 6.

Since no hidden layer exists among input and output level, the sum of products of input variables along with their resultant weight co-efficient gives the $A L O S_{\text {unsig }}$ of respective approaches of unsignalized intersections.

Mathematically, predicted $A L O S_{N}$ using FLANN modeling approach is expressed as shown in Eq. (3):

```
ALOS N = 0.0006 * a - 0.1013 * cos (a) - 0.7887 * sin (a) + 0.0004 * sin (π *a) + 0.4178 * b + 1.1516 * cos (b)
+ 0.3509 * sin(b) + 0.0002 * sin( / * b) + 0.5994 * c + 0.8073 * cos (c) + 0.2231 * sin(c) + 0.1395 * sin( n * c)
-0.0142*d+1.311*cos(d)-0.0191*sin(d) - 0.1947*sin(π*d) - 0.4858*e+1.409* cos(e)
-0.4814*sin(e)-1.3826*sin(π*e)-0.1201*f+0.0194* cos(f)+0.0821*sin(f)-0.022*sin(π*f)
```

At the end, $A L O S_{N}$ was denormalized to estimate the $A L O S_{\text {unsig }}$ for respective approaches of unsignalized intersections. Figure 9(a) shows the plotted graphs of FLANN model validation, which shows an $R^{2}$ value of 0.908 and 0.886 correspondingly for training and testing datasets.

## DE model architecture

By coding the DE algorithm in MATLAB, the coefficient of each input variable and the constant term was estimated for unsignalized intersections. Many trials with different lower and upper bounds for the coefficient of predictor variables and constant term were changed to achieve a reliable model with better $R^{2}$ value and lesser RMSE. The values of particle best obtained from the DE algorithm are represented in Table 7. Figure 9(b) shows the plotted graphs of the DE model validation, which shows an $R^{2}$ value of 0.940 and 0.929 correspondingly for training and testing datasets.

The mathematical interpretation of the DE model to determine $A L O S_{\text {unsig }}$ is as shown in Eq. (4):

![](https://cdn.mathpix.com/cropped/fda6e382-da16-4484-9e3c-1f1ed875df31-11.jpg?height=1079&width=1395&top_left_y=980&top_left_x=362)
Figure 9. Validation of (a) FLANN model and (b) DE model for unsignalized intersections.

Table 7. Particle best results obtained from DE model for unsignalized intersections.
| Variables | Coefficients | Particle best values | Standard error of the estimates | Significance |
| :--- | :--- | :--- | :--- | :--- |
| Constant | $a_{0}$ | 2.1 | 0.10 | 0.00 |
| PCI | $a_{1}$ | 0.65 | 0.02 | 0.00 |
| PoM | $a_{2}$ | 0.03 | 0.05 | 0.01 |
| $t_{c}$ | $a_{3}$ | 0.06 | 0.02 | 0.00 |
| LU | $a_{4}$ | -1.35 | 0.21 | 0.00 |
| $O_{E}$ | $a_{5}$ | -3.32 | 0.39 | 0.00 |
| $T_{s}$ | $a_{6}$ | -0.16 | 0.01 | 0.00 |
| Model summary |  |  |  |  |
| Number of observations | $R$ | $R^{2}$ | Standard error | Significance |
| 136 | 0.969 | 0.939 | 0.247 | 0.00 |


Table 8. Model comparison using MRI.
| Model | FLANN |  |  |  | DE |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Data type |  |  | Train | Test | Train | Test |
| Best fit calculation | $R^{2}$ |  | 0.908 | 0.886 | 0.939 | 0.929 |
|  | $E$ |  | 0.813 | 0.76 | 0.661 | 0.715 |
|  | $\mathrm{R}_{1}$ |  | 2 |  |  |  |
| Error easuring parameters | RMSE |  | 0.42 | 0.48 | 0.566 | 0.526 |
|  | AAE |  | 0.347 | 0.366 | 0.515 | 0.457 |
|  | MAE |  | 1.149 | 1.456 | 1.059 | 1.024 |
|  | $\mathrm{R}_{2}$ |  | 1 |  |  |  |
| $A L O S_{\text {Pred }} / A L O S_{\text {Obs }}$ | Mean |  | 1.094 | 1.113 | 0.868 | 0.886 |
|  | Sigma |  | 0.121 | 0.165 | 0.062 | 0.066 |
|  | $\mathrm{R}_{3}$ |  | 2 |  |  |  |
| Cumulative probability | Probability | $P_{50}$ | 1.08 | 1.099 | 0.869 | 0.862 |
|  | $P_{90}$ |  | 1.22 | 1.229 | 0.938 | 0.975 |
|  | $\mathrm{R}_{4}$ |  | 2 |  |  |  |
| 20\% accuracy | Log-Normal |  | 79.868 | 63.51 | 86.314 | 91.008 |
|  | Histogram |  | 88.971 | 80.70 | 87.5 | 92.982 |
|  | $\mathrm{R}_{5}$ |  | 2 |  |  |  |
| Overall rank | MRI |  | 9 |  |  |  |
|  | Final Rank |  | 2 |  |  |  |


$$
\begin{aligned}
A L O S_{\text {unsig }}= & 2.1+0.65 P C I+0.03 P o M+0.06 t c-1.35 L U \\
& -3.32 O_{E}-0.164 T s
\end{aligned}
$$

## Predictive capabilities of the ALOS models

To compare the predictive capabilities of the proposed models; Rank Index (RI) was recommended by Cai et al. (2009). Along with that, a modified rank index (MRI) was suggested by Beura and Bhuyan (2017). The statistical evaluation factors, picked from them are summarized in Table 8. The prediction performances of ALOS models proposed for the assessment of unsignalized intersections are compared in training and testing data sets. Based on various statistical parameters of MRI, the lowest MRI of '6' is assigned to the DE modeling approach (Table 8). Therefore, the DE model is concluded to have highly precise prediction efficiency during training and testing to predict $A L O S_{\text {unsig }}$ of different approaches of unsignalized intersections, as the prediction efficiency of the FLANN model is comparatively inferior to DE. It is found out from Figure 9(b) that the model is well validated with $R^{2}$ values for training and testing datasets of 0.94 and 0.93 , respectively.

## Ranges of ALOS Categories (A-F)

The estimated $A L O S_{\text {unsig }}$ obtained for unsignalized intersections was classified on a 6-point scale (1-6), where '1' represents the worst and '6' represents the best driving environment perceived by the users. By considering the symmetry of six ALOS classes, the mean estimation of the ALOS scores is 3.5, which match up with the boundary between service categories 'C' and 'D'. Thus, overall symmetrical partitions were made accordingly, and the ranges of $A L O S_{\text {unsig }}$ for different ALOS classes are presented in Table 9.

Table 9. Ranges of $A L O S_{\text {unsig }}$ scores for ALOS (A-F).
| LOS category | Level of overall satisfaction | Ranges of $A L O S_{\text {unsig }}$ |
| :--- | :--- | :--- |
| A | Excellent | > 5.1 |
| B | Very good | >4.33- $\leq 5.1$ |
| C | Good | >3.5- $\leq 4.33$ |
| D | Average | $>2.67-\leq 3.5$ |
| E | Poor | $>1.84-\leq 2.67$ |
| F | Very poor | $\leq 1.84$ |


## Model application

The application of the proposed model for genuine implementation of the suggested ALOS model in the field can be understood clearly from the following example. The following are the observations collected from one of the three-legged unsignalized intersections having Through (T), Right Turn (RT), and Left Turn (LT) approaches. The steps followed to calculate $A L O S_{\text {unsig }}$ using the DE model for this intersection are given below:

For major road 1 (T): $P C I=4, P o M=1, t_{c}=2.9 \mathrm{~s}, L U=0, O_{E}=$ 0.08 and $T_{s}=3.15 \mathrm{~s}$.

By putting these input values in equation (5), the respective values of $A L O S_{\text {unsig }}$ are anticipated as 4.77 with ALOS category 'B.'

Likewise, for major road 2(T): $P C I=4, P o M=1, t_{c}=2.95 \mathrm{~s}, L U=$ $0, O_{E}=0.08$ and $T_{s}=0.03 \mathrm{~s}$. The predicted $A L O S_{\text {unsig }}$ is calculated as 5.255 with ALOS category 'A.'

For major road 2 (RT): $P C I=3.5, P o M=0, t_{c}=0 \mathrm{~s}, L U=0, O_{E}=$ 0.08 and $T_{s}=2.36 \mathrm{~s}$. The predicted $A L O S_{\text {unsig }}$ is calculated as 4.55 with ALOS category 'B.'

For minor road (RT): $P C I=4$, $P o M=1, t_{c}=2.95 \mathrm{~s}, L U=0, O_{E}=$ 0.08 and $T_{s}=2.13 \mathrm{~s}$. The predicted $A L O S_{\text {unsig }}$ is calculated as 4.94 with ALOS category 'B.'

Hence, the $A L O S_{\text {Overall }}$ score for the intersection is obtained as 4.879 by taking the average of all approaches of an intersection. From the field observation, the perceived ALOS scores for the approaches major road 1 (T), major road 2 (T), major road 2 (RT) and minor road (RT) are 4.67, 4.8, 4.7 and 4.8, respectively. The perceived $A L O S_{\text {Overall }}$ score for the intersection can be averaged out to be 4.74. By referring to the LOS ranges, the predicted ALOS category for the intersection is designated as a category of ALOS 'B.'

Similarly, the predicted $A L O S_{\text {unsig }}$ anticipated by every approach of the study intersections and found that, around, 9\%, 25\%, 39\%, $17 \%, 9 \%$, and $1 \%$ of the investigated unsignalized intersections are offering service categories of 'A,' 'B,' 'C,' 'D,' 'E,' and 'F,' respectively, for automobile mode of transport.

## Improvement strategies for unsignalized intersections

The variation in drivers' satisfaction level at unsignalized intersections related to input variables, was tested with the help of a model sensitivity analysis (Gandomi, Yun, and Alavi 2013). Based on the obtained $S_{i}$ values in Table 10, PCI, PoM, $T_{s}, O_{E}, L U$, and $t_{c}$ are ranked with the relative impact of $21.73 \%, 19.77 \%, 9.48 \%, 8.7 \%$, and 3.19\%, respectively.

Referring to the rank of variables, several strategies are made for the improvement of the driving condition at unsignalized intersections.

- The highest $S_{i}$ value of ' $P C I$ ' indicates that $A L O S_{\text {unsig }}$ is most influenced by the quality of pavement surface which needs regular maintenance for the comfortable ride of automobile drivers.
- 'PoM' has a significant positive influence on the ALOS standards at unsignalized intersections in the present context. It assures safety at intersections from opposing traffic. Raised median barriers are also helpful for minimizing headlight

Table 10. Sensitivity analysis of ALOS model attributes for unsignalized intersections.
| Variables | PCl | PoM | $t_{c}$ | LU | $O_{E}$ | $T_{s}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $N_{i}$ | -2.6 | 1.52 | -0.22 | 0.61 | 0.66 | 1.38 |
| $S_{i}$ (\%) | 37.12 | 21.73 | 3.19 | 8.7 | 9.48 | 19.77 |
| Rank | 1 | 2 | 6 | 5 | 4 | 3 |


glare from opposing traffic. Hence, drivers feel comfortable if medians are present on the intersection approaches.
- Service delay is the third most influential variable, having a negative impact on the $A L O S_{\text {unsig }}$ of unsignalized intersections. Better serviceability can be achieved by minimizing the service delay of an intersection with improved roadway geometrical designs. As a result, the major conflict points will be eliminated, leading to a smoother flow of traffic.
- The factor ' $O_{E}$ ' occupies the fourth position and has a negative influence on $A L O S_{\text {unsig }}$. Hence, the illegal movement of vehicles or pedestrians on the sides of drive ways in the opposite direction should be restricted by imposing strict regulations.
- The parameter ' $L U$ ' has a considerable negative impact on $A L O S_{\text {unsig }}$. That means the road users driving in urban residential zones are more satisfied with the driving environment than the commercial zones. So, seizing illegal on-street commercial activities will considerably improve service quality at unsignalized intersections.
- Critical gap holds a positive influence on drivers' perception of unsignalized intersections. The larger the value of ' $t_{c}$ ', more frequent is the availability of large gaps to the minor road vehicles for clearing the intersections. So, the serviceability of the unsignalized intersections can be improved by adopting various measures for decongesting intersection approaches, which will ensure smooth clearing of vehicles.

## Conclusion

Research practices carried out to evaluate the service quality of unsignalized intersections in developed countries cannot be transferred to developing countries to suggest improvement measures. The present study has justified the existing limitations and developed a reliable ALOS model taking a wide spectrum of geometrical, traffic operational, built-environmental, and perception information, collected from intersections in three cities of India. Spearman's correlation analysis shows that Pavement condition index (PCI), Presence of median (PoM), Critical gap $\left(t_{c}\right)$, Land use pattern $(L U)$, Oppositely moving encounters $\left(O_{\mathrm{E}}\right)$, and Service delay $\left(T_{s}\right)$ have a significant impact on drivers' riding quality at unsignalized intersections.

The parameters, $T_{s}$ and $t_{c}$, which cannot be measured directly on the field, have been estimated by developing traffic simulation models in VISSIM. The validation errors (MAPE) were found to be less than $15 \%$ for all the study intersections. Estimating service delay and critical gap using simulated data have saved a considerable amount of time, as manual extraction of gap acceptance and delay data from traffic videos are a strenuous task. Results show that the DE model can predict the ALOS scores of unsignalized intersections with better accuracy, having $R^{2}$ values of 0.94 and 0.93 for training and testing datasets, respectively. The resulting $A L O S_{\text {unsig }}$ anticipated by approaches of intersections illustrates that 9\% of the considered intersections are labeled under ALOS class 'A.' Most of the intersections are observed to provide inferior service quality, which have vital issues related to the provided service quality. Sensitivity analysis of the ALOS model yielded specific percentage values of service attributes, which were used to sort these attributes in order of their degree of relative importance. PCI plays the most significant role in improving the ALOS standards of unsignalized intersections, which has a maximum positive impact of $37.12 \%$. Hence, road pavement surface necessitates consistent maintenance for the smooth drive of vehicles to improve the service quality of the corresponding intersections. Sensitivity analysis has helped in suggesting a number of enhancement strategies, which will assist the transportation officials to recognize operational issues of unsignalized intersections, and to plan a user-friendly transportation network.

The ALOS models developed in this study provide a new insight into the satisfaction level of road users at unsignalized intersections under highly heterogeneous traffic conditions. The proposed model will be extensively used in developing countries like India to judiciously invest their scarce financial resources in development projects. It can also find applications in developed countries by iteratively changing the input parameters in prevailing conditions.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## ORCID

Suprava Jena (D) http://orcid.org/0000-0002-2476-6831
Sharmili Patro (iD) http://orcid.org/0000-0001-7875-3588
Manish Dutta (D) http://orcid.org/0000-0002-9312-5077

## References

Aakre, E., and A. Aakre. 2017. "Modeling Cooperation in Unsignalized Intersections." Procedia Computer Science 109: 875-880. Elsevier.
Ashalatha, R., and S. Chandra. 2011a. "Service Delay Analysis at TWSC Intersections through Simulation." KSCE Journal of Civil Engineering, 15 (2): 413-425. Springer.
Ashalatha, R., and S. Chandra. 2011b. "Critical Gap through Clearing Behavior of Drivers at Unsignalised Intersections." KSCE Journal of Civil Engineering 15 (8): 1427-1434. doi:10.1007/s12205-011-1392-5.
Beura, S. K., and P. K. Bhuyan 2017. Modeling Quality of Bicycle Accommodations on Urban Road Segments Using Functional Networks and Multivariate Adaptive Regression Spline Techniques. In 96th Annual Meeting of the Transportation Research Board. Transportation Research Board, Washington, DC.
Cai, G., S. Liu, L. Tong, and G. Du. 2009. "Assessment of Direct CPT and CPTU Methods for Predicting the Ultimate Bearing Capacity of Single Piles." Engineering Geology 104 (3-4): 211-222. Elsevier.
Caliendo, C. 2014. "Delay Time Model at Unsignalized Intersections." Journal of Transportation Engineering, 140 (9): 4014042. American Society of Civil Engineers.
Chandra, S., A. Agrawal, and A. Rajamma. 2009. "Microscopic Analysis of Service Delay at Uncontrolled Intersections in Mixed Traffic Conditions." Journal of Transportation Engineering 135 (6): 323-329. doi:10.1061/(ASCE) 0733-947X(2009)135:6(323).
Chodur, J., and K. Ostrowski 2015. Unsignalised Intersections Capacity and Performance Estimation Methods. In Recent Advances in Civil Engineering: Road and Transportation Engineering.
Dowling, R., A. Skabardonis, J. Halkias, G. McHale, and G. Zammit. 2004. "Guidelines for Calibration of Microsimulation Models: Framework and Applications." Transportation Research Record, no. 1876: 1-9. doi:10.3141/ 1876-01.
Dutta, M., and M. A. Ahmed. 2019. "Calibration of VISSIM Models at Three-legged Unsignalized Intersections under Mixed Traffic Conditions." Advances in Transportation Studies 48: 31-46. doi:10.4399/9788255254723.
Dutta, M., and M. A. Ahmed. 2020. "Critical Gaps at Three-legged Unsignalised Intersections Using Microsimulation." Proceedings of the Institution of Civil Engineers - Transport. doi:10.1680/jtran.20.00050.
Gandomi, A. H., G. J. Yun, and A. H. Alavi. 2013. "An Evolutionary Approach for Modeling of Shear Strength of RC Deep Beams." Materials and Structures, 46 (12): 2109-2119. Springer.
Highway Capacity Manual. 2000. Transportation Research Board. Washington, D.C: National Research Council.
Highway Capacity Manual. 2010. Transportation Research Board. Washington, D.C: National Research Council.
Hollander, Y., and R. Liu. 2008. "The Principles of Calibrating Traffic Microsimulation Models." Transportation 35: 347-362.
Indian Highway Capacity Manual. 2017. Central Road Research Institute, Council of Scientific and Industrial Research, New Delhi.
Jamil, W. A.-J., and W. H. W. Ibrahim. 2013. "An Analysis of Unsignalised Intersection Using aaSIDRA Software. Journal of Civil Engineering." Science and Technology 4 (2): 13-17.
Jena, S., A. Chakraborty, and P. K. Bhuyan. 2018. "Performance Assessment of Urban Streets Addressing Improvement Issues for Automobile Mode of Transport." Transportation Research Record 2672 (45): 232-241. SAGE Publications Sage CA: Los Angeles, CA.

Jiang, L. L., D. L. Maskell, and J. C. Patra 2012. A FLANN-based Controller for Maximum Power Point Tracking in PV Systems under Rapidly Changing Conditions. In 2012 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Kyoto, Japan. IEEE. 2141-2144.
Mohan, M., and S. Chandra 2016. Review and Assessment of Techniques for Estimating Critical Gap at Two-way Stop-controlled Intersections. European Transport - Trasporti Europei, (61).
Mohan, M., and S. Chandra. 2018. "Critical Gap Estimation at Two-way Stop-controlled Intersections Based on Occupancy Time Data." Transportmetrica A: Transport Science 14 (4): 316-329. Taylor \& Francis.
Pan, F., L. Zhang, J. Lu, J. J. Zhao, and F. Wang. 2013. "A Method for Determining the Number of Traffic Conflict Points between Vehicles at Major-Minor Highway Intersections." Traffic Injury Prevention, 14 (4): 424-433. Taylor \& Francis.
Patil, G. R., and D. S. Pawar. 2014. "Temporal and Spatial Gap Acceptance for Minor Road at Uncontrolled Intersections in India." Transportation Research Record 2461 (1): 129-136. SAGE Publications Sage CA: Los Angeles, CA.
Patil, G. R., and D. S. Pawar. 2016. "Microscopic Analysis of Traffic Behavior at Unsignalized Intersections in Developing World." Transportation Letters 8 (3): 158-166. Taylor \& Francis.
Patil, G. R., and J. P. Sangole. 2016. "Behavior of Two-wheelers at Limited Priority Uncontrolled T-intersections." IATSS Research, 40 (1): 7-18. Elsevier. doi10.1016/j.iatssr.2015.12.002.
Pawar, D. S., and G. R. Patil. 2019."Analyzing Variations in Spatial Critical Gaps at Two-way Stop Controlled Intersections Using Parametric and Non-parametric Techniques." Journal of Traffic and Transportation Engineering (English Edition). (Article in press), Elsevier.
Reddy, M. J., and D. N. Kumar. 2007. "Multiobjective Differential Evolution with Application to Reservoir System Optimization." Journal of Computing in Civil Engineering 21 (2): 136-146. American Society of Civil Engineers.
Zhang, G., J. Chen, and J. Zhao 2017. Safety Performance Evaluation of a Three-Leg Unsignalized Intersection Using Traffic Conflict Analysis. Mathematical Problems in Engineering, 2017. Hindawi.


[^0]:    *Adopted from Dutta and Ahmed (2019)

