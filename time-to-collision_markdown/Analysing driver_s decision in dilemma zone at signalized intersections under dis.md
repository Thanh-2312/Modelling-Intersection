# Analysing driver's decision in dilemma zone at signalized intersections under disordered traffic conditions 

Ritvik Chauhan, Ashish Dhamaniya *, Shriniwas Arkatkar<br>Department of Civil Engineering, Sardar Vallabhbhai National Institute of Technology (SVNIT), Surat 395007, India

## ARTICLE INFO

Keywords:
Signalized Intersection
Mixed traffic conditions
Dilemma zone
Stopping probability


#### Abstract

Delay in the decision-making process of stop or go during the amber phase of the signal cycle often leads to abrupt hard deceleration or red light violations at signalized intersections. The indecisiveness or the dilemma in decision making often results in compromised safety of the road users. The present study attempts to analyze the driver's behaviour in order to make the decision of stop or go and developed a binary logistic regression model while considering different traffic behaviour parameters exhibited and observed after the onset of the amber phase. Empirical vehicular trajectory data from three signalized intersections covering 121 signal cycles and 1347 vehicles are used in the study. The study presents two dilemma zone identification models based on distance from the stop line, focusing on easy-to-use and static driver assistance and dynamicrealtime driver assistance systems. Both the models are observed to show good fit and prediction accuracy. The models are validated internally and externally for their adaptability in the field. The effect of different traffic parameters on the dilemma zone is explored, and a possible real-time application of the dynamic model as a driver assistance system in decision-making is explored.


## 1. Introduction

### 1.1. Background

Road traffic signals are pivotal devices installed for efficient traffic management and safe operations. These instruments are usually deployed when two or more conflicting traffic streams are merging, diverging, or crossing at a node of a road network. An efficient design and appropriation of the signal cycle \& different phases of the signal cycle significantly influence the capacity and traffic safety aspects (Tang et al., 2019). Studies report that 40\% of road accidents occur at signalized intersections (World Health Organization, 2018). The signal cycle is divided into three phases during which the vehicle must stop (red phase), vehicles are assigned the right of way and allowed to go (green phase), and an information cum warning to the drivers of a forthcoming change in the right-of-way allocation (amber/yellow phase). The functioning of the red and green phases is clear and easily understood. However, after the onset of the amber phase, the drivers close to the stop line may cross, and drivers at a significant distance should decelerate and stop to safely arrive at the intersection before the onset of the red phase and avoid red-light violations. Hence, the amber phase also serves as a buffer zone between two conflicting green phases (Pathivada \& Perumal, 2019). In many instances, a driver is unable to decide whether to stop or go during the amber phase. This delay or dilemma in decision making often leads to aggressive decelerations to stop

[^0]or red-light violations that often result in rear-end or side-impact/head-on collision (Najmi et al., 2019; Papaioannou, 2007).
For developing economies like India, the urban roads are characterized by a high degree of heterogeneous traffic with very weak or absence of lane discipline (Biswas et al., 2017; Majhi \& Senathipathi, 2021), hereafter referred to as disordered traffic. In disordered traffic conditions, the traffic behaviour of different vehicle classes is significantly different (Kanagaraj et al., 2015). Additionally, the behaviour at signalized intersections statistically varies at different locations and during different traffic phases (Chauhan et al., 2021a). Lastly, the speeds of the vehicle at the end of the Green phase and the onset of amber phases are observed to be the highest (Chauhan et al., 2021a, b). When added with the effect of dilemma in stop or go decision making during the amber phase, the safety aspects are significantly compromised in disordered traffic conditions. Reports state that around 6300 fatalities and 18,100 persons were injured in road accidents at controlled intersections in India in 2019 (MoRTH, 2019). Hence assessment of stop and go decisions by drivers becomes pivotal in assessing the safety aspects and design efficiency of the signalized intersections (Baratian-Ghorghi et al., 2017; Biswas et al., 2017; Yan et al., 2009).

### 1.2. The dilemma of stop or go decision during the amber phase

The indecisiveness in making a stop or go decision during the amber phase is observed to significantly depend upon the speed of the vehicle, distance from the stop line, and time remaining in the amber phase (time to phase change from amber to red) (Biswas et al., 2017; Wei et al., 2011). In addition to the speed and distance from the stop line, factors like vehicle class, time of the day, reaction or perception type, acceleration rates, presence of countdown timers are also found to be statistically affecting the location and length of the dilemma zone (Abbas et al., 2014; Gates \& Noyce, 2010; Liu et al., 2007). However, for disordered traffic conditions, the studies on analyzing the driver's decision-making behaviour and dilemma zone length-location are limited to exploring the effect of speed, distance from stop line, vehicle class, and type of intersection (4-legged or 3-legged) (Pathivada \& Perumal, 2019). However, the location of the vehicles (distance from the stop line) was recorded at an accuracy of 10 m and hence might possibly compromise the accuracy of the results. Another study measures the effect of the lane in which the vehicle is present, in addition to the speed and distance of the vehicle (Pawar et al., 2020). However, the study did not consider the vehicle present in extreme kerbside lanes stating that it was used for only free left-turning manoeuvres (left-hand traffic is followed in India). The dominant vehicle class of motorized Two-wheelers (2 W) travels in intermediate and kerbside lanes compared to median side lanes (Chauhan et al., 2021a; Kanagaraj et al., 2015). In addition, with the absence of lane discipline determining the significant lateral movements performed by vehicles, a vehicle starting in intermediate lanes might end up crossing or stopping at the stop line in median or kerbside lanes. Due to this, instead of lane numbers, the lateral location of the vehicle during data recording and lateral movement performed by a vehicle should be considered for model development to identify the dilemma zones. Also, both the available studies provide a model that is developed from the data collected from one metropolitan in each study, respectively. Studies report that models developed using characteristics of one study section might not accurately simulate the driving behaviours, or traffic scenarios can only predict the traffic behaviour to an acceptable approximated level (Bhattacharyya et al., 2020). The efficiency of any developed model depends on its ability to replicate the local traffic characteristics (Chauhan et al., 2021a). Hence, a robust stop or go decision-making model that is validated and transferable to other locations is needed.

Studies report that the dilemma zone can be rendered nullified with effective design practices involving the adequate provision of amber and red-clearance time (all red conditions) (Jianwen et al., 2007). However, in general, a constant time interval of 3 s is provided for the amber phase, and the provision of all red conditions is rarely provided in a developing economy like India. The 3 s time interval might be small for the drivers to avoid the dilemma zone after accounting the perception and reaction times of different drivers (Tang et al., 2017, 2019), especially because the vehicular speeds are observed to be highest during the onset of the amber phase (Chauhan et al., 2021a). In lieu of this, accurate identification of the dilemma zone and providing information to the drivers in advance might aid in decision-making, mitigating the ill effects caused by indecisiveness (Hussein et al., 2020; Pathivada \& Perumal, 2019; Wu et al., 2018; Yan et al., 2009).

### 1.3. Dilemma zone identification

The dilemma zone name came into effect in the early 1960s and as a research interest first referred to in a study by (Gazis et al., 1960). Further studies identified that the dilemma during the amber phase at the signalized intersection is of two types. Type I dilemma Zone shows that the driver cannot pass or stop due to poor intersection design and signal timing. The type I dilemma zone is deterministic and can be eliminated by proper amber timing (Gazis et al., 1960). Type II dilemma zone was first recognized in a technical committee report produced by the southern California section of the Institute of Transportation Engineers (ITE) in 1974. The study explored the driver's indecisiveness or making a wrong decision during the onset of amber, and hence the stochastic nature of the Type-II dilemma zone was defined (Zhang et al., 2014). Type-II dilemma zone is also called indecision zone or option zone. A frequency-based approach is used to obtain the stopping probability of the driver's onset of amber. The percentage of drivers stopping for a given distance/time from the stop line and vehicle speed is used to develop the dilemma zone curves (Zegeer \& Deen, 1978). The dilemma zone curves are observed to be influenced by several factors like Vehicle speed, distance to stop line, vehicle class, lane position of the vehicle, acceleration of the vehicles at the onset of the amber phase, among many others (Köll et al., 2004; Papaioannou, 2007; Pathivada \& Perumal, 2019; Pawar et al., 2020; Rakha et al., 2008; Zhang et al., 2014). Studies have used the Binary Logistic approach to model the decision to stop and go to stop or pass probability during the amber phase and identify the dilemma zone (Pathivada \& Perumal, 2019; Zegeer \& Deen, 1978). A dilemma zone at the signalized intersection is defined where more than $10 \%$ and less than $90 \%$ of drivers make stop decisions (Pawar et al., 2020). Additionally, researchers have also tried to use Fuzzy logic-based
approach for dilemma zone identification (Hurwitz et al., 2012). The fuzzy-based approach enables incorporation and overcoming the imprecise information pertaining to the driver's behavior and drivers perception given the time to phase change (amber to red), speed and distance to clear. However fuzzy logic-based approach also has challenges related to the formulation of the membership function and defining the lower and upper function bounds for validation of logic. Based on the results of the study, the authors have proven the feasibility of the Fuzzy based approach and its benefits in identifying the dilemma zone. It is expected that the incorporation of uncertainty in driver's behavior shall lead to defining the "true dilemma zone". However, considering the high degree of heterogeneity in the driver behavior, composition, and challenges in acquiring drivers perceiving behavior in disordered traffic, the dilemma zone identification is still primarily performed using binary logistic regression, and the same is used in the present study.

Based on the findings, driver behaviour during the dilemma zone is observed to be dependent on a multitude of factors. Some of which might be hard to measure on the field. Hence, the data collection process needs to a thorough to enable the extraction of a multitude of factors for a robust analysis.

### 1.4. Data for analysis

Research related to traffic flow theory is more than often affected by the inadequacy of data qualitatively and quantitatively. The available datasets are either conventional aggregated data or small trajectories that hinder the possibility of supporting and corroborating microscopic theories. This results in the research being driven towards model-based theoretical analysis (Montanino \& Punzo, 2015). Hence, a major challenge in conducting research related to traffic flow theory is to enhance the study of traffic models with the study of their characteristics and properties. Detailed and wide-ranging traffic data is vital to meet this aim. Accessibility to vehicle trajectories from the study section and of all the vehicles permits validating the theories and models at the microscopic and macroscopic levels (Wei et al., 2019). The binary logistic models developed for identifying the dilemma zones for disordered traffic conditions in available studies are based on the point data recorded at the onset of the amber phase with a limited number of traffic parameters (Pathivada \& Perumal, 2019; Pawar et al., 2020). However, traffic behaviour is observed to be dependent on various factors. Point data restricts the number of parameters that can be extracted. Contrarily trajectory data enables the extraction of a multitude of traffic parameters for analysis.

### 1.5. Objectives of the study

Based on the identified advantages and research gaps from the detailed review of past studies, the present study aims to

a) Develop a validated and transferable dilemma zone identification model for disordered traffic conditions based on the point data for easy application in the field.
b) Develop an alternate dilemma zone identification model for real-time and dynamic applications based on detailed traffic behaviour parameters using vehicular trajectory data
c) To study the effect of different traffic behaviour parameters on the identified dilemma zone

## 2. Methodology

### 2.1. Model development

Binary discrete choice models are well suited for describing and testing the hypothesis about the relationship between a binary response outcome and one or more explanatory variables that can be categorical or quantitative. In the present case, drivers approaching intersections during amber intervals must decide whether to Stop (0) or Go (1). Binary discrete choice models are developed to determine the probability of stopping for a given distance and speed of the approaching vehicle during the amber interval. Equation (1) gives the probability of stopping for a given distance/speed Y.

$$
P_{i}(\text { stopping })=\frac{\exp \left(-U_{i}(\text { passing })\right.}{1+\exp \left(-U_{i}(\text { passing })\right)}
$$

Where $\mathrm{P}_{\mathrm{i}}$ is the probability of stopping, and $\mathrm{U}_{\mathrm{i}}$ is the utility given by Equation (2).

$$
U_{i(\text { passing })}=\beta_{0}+\beta_{j 1}{ }^{*} X_{j 1}+\beta_{j 2}{ }^{*} X_{j 2}+\beta_{j 2}{ }^{*} X_{j 2}+\cdots \cdots \cdots+\beta_{j n}{ }^{*} X_{j n}
$$

Where;
$U_{j i}$ : Utility of driver ' $i$ ' deciding an alternative ' $j$ '
j: Decision to Stop or Go
$\beta$ : model coefficients of independent variables
$n$ : number of independent variables
X: Independent explanatory variables
In the present study, two models are developed in the present study, namely the Point Data model (PDM) and Trajectory Data

Model (TDM). PDM is developed based on the parameters that can be easily observed and recorded in the field, like the vehicle's speed, distance from the stop line, vehicle class, and lane in which the vehicle is present. The data is recorded after the onset of an amber phase and hence is easier to compute. Thus, the development of PDM is aimed to provide easier applicability of identifying the dilemma zone and hence providing pavement markings as a static means of assisting the driver's decision-making process. However, due to the absence of lane discipline at the signalized intersection in disordered traffic conditions, a vehicle might change its lane between the point of recording (onset of amber phase) and the point of arriving at the stop line. There is a possibility that the vehicle might undergo acceleration and deceleration due to changing decisions and conditions. As also reported in the earlier part of the manuscript, the dilemma zone depends on multiple factors. Many of these factors are hard to measure when considering only point data as recorded in available studies for disordered traffic conditions (Pathivada \& Perumal, 2019; Pawar et al., 2020). With variations in the value of different traffic behaviour parameters, how the dilemma zone's length and the driver's decision are affected can be accurately captured with the trajectory data. Hence, TDM is developed using additional parameters compared to PDM. After the onset of the amber phase, due to weak lane discipline and freedom to shift laterally, the total lateral movement by each vehicle is calculated. The average acceleration of the vehicle during this specific time is also measured. In addition, instead of lane number, the lateral location of the vehicle on the carriageway during the onset of the amber phase in support of the total carriageway width is also considered. TDM considers the dependent decision (stop or go) and the traffic behaviour parameters that were exhibited from the inception of the decision-making process (onset of amber phase) until the decision is executed (crossing or stopping at the stop line). TDM is developed to provide a more robust model (than PDM) and an active and dynamic method of estimating the dilemma zone and stopping probability of a vehicle given. With advanced driver assistance systems, and connected vehicular environment (vehicle to vehicle and vehicle to infrastructure), TDM can also aid the driver in decision-making. The parameters and their characteristics used for the development of PDM and TDM are detailed in Table 1.

### 2.2. Model validation

The developed models are validated on two levels. The first stage is internal validation, where the data is randomly divided into two sets. The set used for model development comprises 70\% of the data, and the remaining 30\% is used for validating the model as a second set. Following the internal validation of the model, the developed model is tested for external validation (transferability). Data from an entirely different study section that is not used for model development is used to check the transferability of the model.

Table 1
Parameters considered for model development.
| Parameter | Category | Description | Used for |
| :--- | :--- | :--- | :--- |
| Decision to stop or go | Categorical | Dependent Variable; Passing: 1, Stopping: 0 | - |
| Distance from stop line | Continuous | 0 m signifies the stop line | PDM and TDM |
| Longitudinal Speed | Continuous | In m/s, calculated at every 0.4 s interval | PDM and TDM |
| Acceleration | Continuous | In $\mathrm{m} / \mathrm{s}^{2}$ and calculated at every 0.4 s interval | TDM |
| Lateral Speed | Continuous | Lateral speed of the vehicle during lateral movement (m/s) | TDM |
| Carriageway width | Continuous | Including the auxiliary lanes (m) | TDM |
| Lateral location | Continuous | Ratio of the vehicle's lateral position (median represents 0 m) and carriageway width (m) in decimals. 0: Median side \& 1: Kerbside | TDM |
| Lane Number | Categorical | 1: Median side, 2: Intermediate lanes, 3: Kerbside | PDM |
| Vehicle class | Categorical | 1: 3W, 2: 2W, 3: Car, 4: Bus \& LCV | PDM and TDM |
| Lateral Movement | Continuous | Cumulative Lateral Moment by a vehicle (m) | TDM |
| Direction of Movement | Categorical | Lateral movement towards median (0), Kerb (1) | TDM |
| Signal Cycle Length (c) | Continuous | Total signal cycle length (s) | TDM |
| Amber Time | Continuous | Amber/yellow phase duration (s) | TDM |
| Green Time (g) | Continuous | Duration of Green phase at each location (s) | TDM |
| g/c ratio | Continuous | Ratio of 'g' and 'c' in decimals | TDM |
| Type of Intersection | Categorical | 4-legged Intersection (0), 3-legged intersection (1) | PDM and TDM |
| Crosswalk Present | Categorical | Yes (0); No (1) | PDM and TDM |
| Auxiliary Lane | Categorical | Yes (0); No (1) | PDM and TDM |


## 3. Study locations and data acquisition

### 3.1. Data collection

Videography data is collected from three isolated signalized intersections in the metropolitan cities of Ahmedabad (Gujarat) and Jaipur (Rajasthan). All the study intersections observe under-saturated and disordered traffic conditions and are free from side friction parameters, gradients, and curvature. All the intersections have a three-phase signal scheme (Red-Green-Amber-Red). Data is collected on a bright day with dry weather conditions and clear visibility using high-resolution video cameras mounted at good vantage points (Chauhan et al., 2021a; Wang et al., 2016). Fig. 1 shows the study locations with a view captured. Details of the study signalized intersections, signal operations, and traffic details are summarised in Table 2.

### 3.2. Data extraction

Due to disordered traffic conditions, reliable automated traffic data extraction is still difficult (Chauhan et al., 2022). In the present study, vehicular trajectory data from the field-recorded video is extracted using the Traffic Data Extractor, a semi-automated tool developed by the Indian Institute of Technology Bombay, India (Munigety et al., 2014). For trajectory extraction, the position of a vehicle is traced by manually clicking at desired intervals. The trajectory data is extracted by classifying the vehicles into four vehicle classes of Motorized Two-Wheeler (2 W), Motorized Three-Wheelers (3 W), Passenger Cars (Car), and Light Commercial Vehicles (LCV). The trajectory data is extracted at an interval of 0.4 s while using the Windows Magnification tool at 200\% magnification throughout the process to avoid or minimize mistracking of a vehicle's position. A detailed data extraction methodology is well depicted in existing literature (Chauhan et al., 2021a, b). The trajectory of vehicles is extracted considering a buffer time of three seconds before the onset of amber time and after the onset of red time to avoid data loss during data smoothing and calculation of speeds \& acceleration. Due to human error in mistracking a vehicle's position, the extracted data might contain local errors (Punzo et al., 2011). When applied to position data, smoothing can remove the random component of the error (Punzo et al., 2011). Past studies also report that the smoothing technique could eliminate outliers and reduce the errors in the trajectory data (Kanagaraj et al., 2015; Venthuruthiyil \& Chunchu, 2018), even when applied for data extracted using a semi-automated tool for disordered traffic conditions. Averaging is one form of smoothing (Punzo et al., 2011); hence a 5-point moving average technique is used to smoothen the extracted vehicular trajectories (Franses, 1991; Raju et al., 2017). After post-processing the data, the trajectory data is trimmed down to represent only the trajectories of vehicles after the onset and during the amber time. The total number of cycles for which the data was extracted and the number of vehicles observed during the amber time are specified in Table 2. Additionally, the decision of a vehicle to cross or stop was marked simultaneously with respect to the unique vehicle ID assigned during the data extraction process. Fig. 2 shows the distance-speed plot of vehicles opting to cross or stop at the stop line after the onset of amber time at L1.

### 3.3. Preliminary analysis

Literature review shows that the traffic behaviour of vehicle classes between different study locations is statistically different (Chauhan et al., 2021a). Hence parameters of speed, acceleration, lateral position, and lateral movement (weak lane discipline) exhibited by the vehicles during the amber phase are analyzed (Fig. 3).

It is observed that the speed, lateral movement, acceleration, and lateral location of vehicles at all three study sections are varying.

![](https://cdn.mathpix.com/cropped/3517ba1b-38be-4b61-b7f2-f98a4ae36d04-05.jpg?height=683&width=1535&top_left_y=1652&top_left_x=177)
Fig. 1. Study Intersections for the Study (a) Intersection near IIM Gujarat (L1); (b) MI Road Jaipur (L2); (c) Intersection at Birla Temple, Jaipur (L3).

Table 2
Study Intersection and corresponding traffic characteristics.
| Study Section | L1 | L2 | L3 |
| :--- | :--- | :--- | :--- |
| Intersection location | Indian Institute of Management and Sargam Marg Junction | Mirza Ismail Road and Motilal Atal Road Junction | Birla Temple and Jaipur Development Authority Circle junction |
| Data collection Period | Morning peak hour of weekday in February | Morning peak hour of weekday in October | Evening peak hour of weekday in October |
| Direction of traffic | Southbound Traffic | Eastbound traffic | Southbound Traffic |
| Type of intersection | 4-legged | 3-legged | 4-legged |
| Approach width | $14 m$ | $9 m$ | $11 m$ |
| Number of lanes | 4 | 3 | 3 |
| Peak hour Volume (PCU) | 4500-6000 | 4000-4500 | 4500-5500 |
| Signal Cycle length | 220 sec | 118 sec | 130 |
| Amber duration | 3 sec | 4 sec | 3 sec |
| Green phase duration | 65 sec | 70 sec | 47 sec |
| Number of Signal Cycles | 27 | 52 | 42 |
| No. of Vehicles in amber | 337 | 599 | 411 |
| Stopping:Passing (\%) | 38:62 | 45:55 | 40:60 |
| Traffic Composition | 59:17:21:3 | 49:14:33:4 | 45:16:36:3 |
| (2 W:3W:Car: Bus-LCV) | 63:6:29:2 | 54:7:35:4 | 43:15:38:4 |
| Stopping | 52:9:36:2 | 47:8:40:5 | 39:22:36:3 |
| Passing | 66:4:29:0 | 57:7:32:3 | 46:11:40:3 |
| 98th,85th,50th,15th Percentile speeds (m/s) | 20,16,10,6.5 | 19,15,11,7 | 19, 14, 10, 5 |
| Speed Limit (m/s) | 13.9 | 11.11 | 13.9 |
| Upstream distance of trajectory (m) | 135 | 150 | 180 |
| Crosswalk Present | Yes | No | Yes |
| Auxiliary Lanes (free left) | Yes | No | Yes |
| Data used for | Model Development and Internal Validation |  | External Validation |
| Lane preference (\%) |  |  |  |
| Combined (Median:Intermediate: kerb) | 25:65:10 | 31:58:11 | 15:62:23 |
| Median side lane (2 W:3W:Car:BusLCV) | 30:2:64:4 | 25:3:65:7 | 35:13:52:0 |
| Intermediate lane (2 W:3W:Car:BusLCV) | 70:8:22:0 | 63:11:23:3 | 38:13:45:4 |
| Kerb side lane (2 W:3W:Car:BusLCV) | 81:3:16:0 | 88:3:7:2 | 63:21:13:3 |


![](https://cdn.mathpix.com/cropped/3517ba1b-38be-4b61-b7f2-f98a4ae36d04-06.jpg?height=492&width=1167&top_left_y=1463&top_left_x=361)
Fig. 2. Decision-making behavior with distance and speed (a) IIM S.I. Ahmedabad.

Additionally, upon further probing, it is observed that the speeds of the vehicle class of 2 W and in median side lanes are highest, followed by Cars and intermediate lanes, respectively. However, the lateral movements are highest for 2 W, followed by 3 W, and least for cars. In terms of lanes, lateral movement is observed highest towards the kerbside and least in the median side sections of the carriageways. The acceleration is observed to vary between $\pm 2.5 \mathrm{~m} / \mathrm{s}^{2}$, with outlier values ranging till $-6 \mathrm{~m} / \mathrm{s}^{2}$ observed in the vicinity of the stop line.

![](https://cdn.mathpix.com/cropped/3517ba1b-38be-4b61-b7f2-f98a4ae36d04-07.jpg?height=808&width=1539&top_left_y=179&top_left_x=175)
Fig. 3. Distribution of Speed, Acceleration, lateral location, acceleration for different study locations, vehicle class, and lanes.

4. Results
4.1. Dilemma zone model
4.1.1. Point data model

Data from two study sections of L1 and L2 is used for model development. From the data of 936 vehicles, 70\% (665 vehicles) are randomly selected for model development and the remaining 30\% (271 vehicles) of the data. Model development was done using STATA V15 statistical software package by StataCorp. Parameter estimates and statistical significance of the developed generalized binary logit model are given in Table 3. The model is developed with the dependent variable of the decision to pass or stop. Hence, the model and estimated coefficients estimate the utility of the driver opting for a decision to pass. The results show that the speed, distance of vehicles, vehicle class, and lane of the vehicle are statistically significant factors that influence the approaching vehicles' decisions at a $95 \%(\mathrm{p}<0.05)$ confidence interval, as also observed by past studies on disordered traffic (Pathivada \& Perumal, 2019; Pawar et al., 2020). The developed model exhibits the pseudo $\mathrm{R}^{2}$ value of 0.41 with a prediction accuracy of 81.80\%. The Receiver

Table 3
Model coefficients and accuracy details for Point Data Model.
| Parameter |  | Coefficient | Std. Err. | z | $\mathbf{P}>\|\mathbf{z}\|$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Longitudinal speed |  | 0.106 | 0.032 | 3.33 | 0.001 |
| Distance |  | -0.083 | 0.006 | -13.34 | 0.000 |
| Vehicle Type | 3 W | -0.695 | 0.448 | -2.34 | 0.019 |
|  | 2 W | 0.00 (base vehicle) |  |  |  |
|  | Car | -1.068 | 0.274 | -3.89 | 0.000 |
|  | Bus \& LCV | -1.471 | 0.627 | -1.55 | 0.121* |
| Lane Number | Median-side Lane | -1.049 | 0.482 | -2.18 | 0.029 |
|  | Intermediate lane | -0.923 | 0.438 | -2.11 | 0.035 |
|  | Kerb-side Lane | 0 (base lane) |  |  |  |
| Constant |  | 4.518165 | 0.559 | 8.09 | 0.000 |
| Log-Likelihood |  | -266.14 |  |  |  |
| No. of Observation |  | 665 |  |  |  |
| Pseudo R2 |  | 0.41 |  |  |  |
| Prediction Accuracy |  | Passing | Stopping | Total | \% Correct |
|  | Passing | 330 | 62 | 392 | 84.83 |
|  | Stopping | 59 | 214 | 273 | 77.54 |
|  | Total | 389 | 276 | 665 | 81.80 |
| ROC |  | 90.01\% |  |  |  |
| AIC |  | 548.28 |  |  |  |
| BIC |  | 585.26 |  |  |  |


[^1]Operating Characteristic (ROC) curve that depicts the indicative ability of binary classifier and is calculated based on the sensitivity (True positive prediction), and specificity (false positive prediction) shows the area under the curve value of 90.01\%. In addition, the goodness-of-fit parameter Akaike's Information Criteria (AIC) is less than Bayesian Information Criteria (BIC). Hence, the developed model observes a good fit and is robust enough to predict the driver's decision with acceptable accuracy.

The estimated parameters are then used to measure the utility of each driver's decision using equation (2), following which the stopping probability is estimated using equation (1). The model coefficients show that the variable of "speed" has a positive coefficient, implying that drivers are more likely to pass the intersection when travelling at a higher speed. In contrast, the coefficient of distance is negative, implying that drivers are more likely to decide to stop for a larger distance from the stop line. Accordingly, for the model developed with the vehicle class of 2 W as the base vehicle, it is observed that as the vehicle size increases, the stopping probability (decision to stop) also increases. As for the lane in which the vehicle is travelling, the vehicles travelling in the median side lane exhibit higher chances of stopping (negative coefficient for passing) than those travelling in intermediate and kerbside lanes.

The estimated parameters (Table 3) are observed to exhibit similar trends as estimated by the available studies focusing on the dilemma zone identification for disordered traffic conditions (Pathivada \& Perumal, 2019; Pawar et al., 2020) (Table 4). The model developed by Pathivada and Perumal (2019) models the decision to stop compared to the decision to pass modelled in the present study and the study by Pawar et al. (2020); hence the magnitudes for the coefficient are reversed. However, all the models exhibit a good fit with pseudo $\mathrm{R}^{2}>0.41$. The model by Pawar et al. (2020) yield's the highest prediction accuracy of 90.8\% compared to the 81.8\% observed for the PDM developed in this study. In terms of internal validation of the models, similar to the method followed by Pathivada and Perumal (2019). The results show that the PDM model can correctly predict 87.78\% of the decision compared to 82.3\% accurate prediction by Pathivada and Perumal (2019).

However, the available dilemma zone identification models for disordered traffic are developed using data from multiple signalized intersections from the same metropolitan city. However, models developed using characteristics of one study section might not accurately simulate the driving behaviours and only predict the traffic behaviour to an acceptable approximated level (Bhattacharyya et al., 2020). The efficiency of any developed model depends on its ability to replicate the local traffic characteristics (Chauhan et al., 2021a). Hence, the available models and developed PDM are tested for their transferability (external validation) to other study locations. The data from the L3 study section is used for external validation of the models. All the models show good transferability of > 60\%. The PDM, though developed using data from fewer intersections compared to the other two models, since the driver's decision to stop or pass during the amber phase from two different metropolitan cities are considered for model development, PDM is observed to correctly estimate the driver's decision at an entirely different study section with an accuracy of 70.28\% compared to the accuracy of 62\% and 64\% by other two models.

### 4.1.2. Trajectory data model

The TDM is developed using additional parameters than those considered for PDM. Table 5 details the coefficients and statistical significance of different parameters. Similar to PDM, TDM is also developed using the data from the L1 and L2 study section with similar classification for internal validation and then checked for transferability using the dataset of L3. With higher values of Pseudo $\mathrm{R}^{2}$ of 0.47 , ROC of $93.4 \%$, and lower values of AIC-BIC \& log-likelihood compared to PDM, it is evident that, since more traffic behaviour parameters are considered, the model exhibits better fit and accuracy than PDM. The TDM observes prediction accuracy of 88.27\%, with internal validation accuracy at 90.08\% and transferability accuracy at 79.26\%. Consideration of additional traffic

Table 4
Comparison of results with existing models.
| Parameter |  | Coefficients |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  |  | Present Study (PDM) | Pathivada and Perumal (2019) | (Pawar et al., 2020) |
| Longitudinal speed <br> Distance |  | 0.106 | -0.075 | 0.232 |
|  |  | -0.083 | 0.055 | -0.099 |
| Vehicle Type | 3 W | -0.695 | 0.694 | - |
|  | 2 W | 0.00 | - | - |
|  | Car | -1.068 | 0.941 | - |
|  | Bus \& LCV | -1.471* | 0.536* | - |
| Lane Number | Median-side Lane | -1.049 | - | -0.577 |
|  | Intermediate lane | -0.923 | - | 0.000 |
|  | Kerb-side Lane | 0 | - | - |
| Type of Intersection |  | - | -1.523 | - |
| Constant |  | 4.518 | 0.858 | 0.945* |
| No. of Observation |  | 665 | 843 | 893 |
| Pseudo $\mathrm{R}^{2}$ |  | 0.41 | 0.41 | 0.59 |
| Model Accuracy (\%) |  | 81.80 | - | 90.8 |
| Internal Validation | Sample for Prediction | 271 | 210 | - |
|  | Prediction Accuracy (\%) | 87.78 | 82.3 | - |
| External Validation | Sample for Prediction | 411 | 411 | 411 |
|  | Prediction Accuracy (\%) | 70.28 | 61.7 | 63.7 |


[^2]Table 5
Model coefficients and accuracy details for Trajectory Data Model.
| Parameter |  | Coefficient | Std. Err. | z | $\mathrm{P}>\|\mathrm{z}\|$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Distance |  | -0.09 | 0.01 | -13.44 | 0.000 |
| Longitudinal Speed |  | 0.13 | 0.03 | 3.83 | 0.000 |
| Acceleration |  | 0.32 | 0.10 | 3.32 | 0.000 |
| Lateral Movement |  | 0.45 | 0.09 | 4.84 | 0.000 |
| Carriageway Width |  | -0.28 | 0.06 | -4.53 | 0.000 |
| Lateral Location |  | -0.98 | 0.64 | -1.52 | 0.093* |
| Vehicle Type | 3 W | -0.46 | 0.66 | -1.78 | 0.076* |
|  | 2 W | 0 |  |  |  |
|  | Car | -0.87 | 0.29 | -3.01 | 0.000 |
|  | Bus \& LCV | -1.18 | -1.26 | 1.61 | 0.109* |
| Constant |  | 6.63 | 0.85 | 7.84 | 0.000 |
| Log-Likelihood |  | -236.17 |  |  |  |
| No. of Observation |  | 665 |  |  |  |
| Pseudo R2 |  | 0.47 |  |  |  |
| Prediction Accuracy |  | Passing | Stopping | Total | \% Correct |
|  | Passing | 352 | 40 | 392 | 89.80 |
|  | Stopping | 38 | 235 | 273 | 59.95 |
|  | Total | 390 | 275 | 665 | 88.27 |
| ROC |  | 93.39\% |  |  |  |
| AIC |  | 502.34 |  |  |  |
| BIC |  | 547.33 |  |  |  |
| Internal Validation | Sample for Prediction | 271 |  |  |  |
|  | Prediction Accuracy | 90.08 |  |  |  |
| External Validation | Sample for Prediction | 411 |  |  |  |
|  | Prediction Accuracy | 79.26 |  |  |  |


* Insignificant at 95\% confidence interval but observed to be significant at 90\% confidence interval.
${ }^{\#}$ Parameter observed to be insignificant.
behaviour parameters for dilemma zone identification is observed to yield better and more reliable results.
The parameters of speed, distance, and vehicle type in TDM are observed to exhibit a similar trend compared to PDM. The traffic parameters of acceleration and lateral movement are found to affect the decision to pass positively. In other words, the higher the average acceleration and total lateral movement of a vehicle, the higher the probability that a vehicle will decide to pass and consequently lower the probability of stopping. The parameter of lateral location also exhibits similar results as observed for the lane numbers (Table 3). The probability of stopping is higher as the vehicle position shift towards median side lanes. The effect of different parameters sed in TDM on the dilemma zone is further portrayed in section 4.2. In addition to the parameters specified in Table 5, the presence of crosswalk, auxiliary lanes, g/c ratio, amber time, signal cycle length, and type of intersection were also observed to be statistically significant in affecting the dilemma zone. However, since only two study locations are used for model development, these parameters were omitted due to co-linearity. However, when studied individually by replacing the carriageway width, all the parameters are statistically significant. The parameter with least standard error value (i.e. carriageway width) was selected for the model development.

![](https://cdn.mathpix.com/cropped/3517ba1b-38be-4b61-b7f2-f98a4ae36d04-09.jpg?height=598&width=1535&top_left_y=1737&top_left_x=177)
Fig. 4. (a) Stopping probability vs distance from stop line for the individual vehicles at L3; (b) Average Dilemma zone at L3.

### 4.1.3. Effect of different traffic parameters on dilemma zone

The dilemma zone for the arriving vehicles is identified as the region between the stopping probability of $10 \%$ and $90 \%$ (Pathivada \& Perumal, 2019; Pawar et al., 2020). With a stopping probability of 90\% denoting starting of the dilemma zone and a stopping probability of 10\% as the end of the dilemma zone. Accordingly, the probable region of the dilemma zone is also highlighted in Fig. 4. Fig. 4a shows the stopping probability for individual vehicles corresponding to their distance from the stop line after the onset of the amber phase at the L3 study section estimated using PDM and TDM. It can be observed that, due to variations in traffic behaviour for the same vehicle class, similar stopping probability is observed at varying distances. This is due to heterogeneity in the traffic

![](https://cdn.mathpix.com/cropped/3517ba1b-38be-4b61-b7f2-f98a4ae36d04-10.jpg?height=1858&width=1537&top_left_y=480&top_left_x=175)
Fig. 5. Variation in the stopping probability and hence the Dilemma zone with respect to changes in different parameters.

behaviour at the same study locations. Hence, for ease of understanding, an average dilemma zone is identified by normalizing the values to a set of standards. Stopping probability for identifying the dilemma zone in Fig. 4b is estimated using 50th percentile speed (10 m/s), zero lateral movement, zero acceleration values, location of vehicles in the middle of the carriageway (0.5), carriageway width restricted to three lanes (10.5 m), and base vehicle class of 2 W (dominant in traffic composition). The dilemma zone from TDM and PDM is identified to exist between 20 m and 80 m from the stop line with a dilemma zone length of about 50 m. Additionally, TDM identifies the dilemma zone in a more compact region (48 m) than PDM (53 m), supplementing a concise dilemma zone identification.

Using average values also supports characterizing the dilemma zone with respect to different traffic parameters used in model development. The effect of different parameters (Table 5) is measured by keeping the parameters value the same as used for Fig. 4b. Only the specific parameter whose effect is to be studied is varied. Fig. 5 depicts the variation in the dilemma zone after the value of the specific parameter is changed. The observed trends in dilemma zone variations are already discussed in sections 4.1.1 and 4.1.2 of the manuscript. This section and Fig. 5 support the observations by depicting the change in the dilemma zone and correlating the observations with other findings.

Speed is observed to be inversely proportional to the estimated stopping probability. Hence, the carriageway sections (median side) with lower operating speeds (Fig. 3e) observe higher stopping probability at the same distance (Fig. 5d). Similarly, vehicle class of 2 W observes more speed than Cars, and hence stopping probability of Cars is lower than for 2 W at the same distance from the stop line. Additionally, studies report that bigger vehicle classes prefer median side lanes in disordered traffic conditions, and smaller vehicles opt to move in kerbside lanes (Chauhan et al., 2021a; Kanagaraj et al., 2015). This might also supplement and correlate the findings particular to the estimated stopping probability for vehicle class and lateral position of vehicles on the carriageway. In addition, most of the intersections in India follow a cyclic pattern for appropriating the Right of Way at signalized intersections. Hence, a vehicle opting to undertake a right turn (Left Hand Traffic) at the intersection might end up conflicting with the adjacent traffic stream allocated the ROW after the amber phase. Consequently, the vehicles might opt to stop than cross the stop line, and hence, the stopping probability for vehicles towards the median side is more than vehicles on the kerbside.

A vehicle opting to cross the stop line instead of stopping is observed to exhibit more lateral movement to manoeuvre through the traffic if needed. Hence, a vehicle exhibiting more lateral movement is observed to have a lower stopping probability. The presence of more carriageway width also provides more freedom for the vehicle to traverse laterally. However, a higher carriageway width results in a higher stopping probability. Alternatively, it can be interpreted as, during the under saturated conditions, the vehicles have sufficient lateral spacing available and hence do not need to traverse laterally to gain a longitudinally advantageous position. In addition, at signalized intersections with disordered traffic, smaller vehicle classes exhibit more lateral movement due to high manoeuvrability (Chauhan et al., 2021a), as observed at the present study locations (Fig. 3g). Hence, the different traffic behaviour parameters are interdependent and accordingly affect different aspects of traffic operations, resulting in variations in exhibited behaviour (dilemma zone length in the present instance). This again highlights the significance of considering several parameters for computing or simulating traffic behaviour in disordered traffic conditions.

### 4.2. Driver assistance during dilemma zone

From the results, TDM was observed to provide more reliable predictions of decision-making than PDM. Additionally, TDM was developed to provide reliable results and possibly account for the dynamic method of estimating the dilemma zone and stopping probability. Fig. 6 depicts an example of a possible application of TDM in driver assistance systems. With the advancement in vehicular, traffic infrastructure, and connected environment technologies, modern vehicles are well equipped to support the driver with safe and optimal decision-making. Vehicle to vehicle (V2V) and Vehicle to Infrastructure (V2I) communications have proven to be effective in enhancing traffic safety during dilemma at signalized intersection (Calvi \& Petrella, 2022). Based on the available parameters stopping probability of a vehicle can be constantly calculated. The onboard vehicle system could inform the driver of possible stopping or passing decisions if a threshold is decided. For example, the model prediction uses 0.5 as a threshold value to estimate the decision to stop or pass. Delay in decision-making often leads to vehicles often opting to decelerate at higher rates, as observed in Fig. 4a (High stopping probability for some vehicles between 0 and 15 m).

Thus, also creating chances of rear-end conflicts and possible collisions. Following the stopping probability threshold value of 0.5, Fig. 6 depicts the driver's decision to stop, those should stop, and those should have passed. Similar observations are also depicted for drivers opting to make the passing decision. It turns out that 10.6\% of the vehicle that opted to stop should have passed; meanwhile, 24\% of the vehicles that decided to pass the stop line should have stopped. If the combined 34.6\% of the drivers could be informed or assisted in making a safe and optimal decision, the dilemma zone length can be significantly mitigated. Additionally, a buffer zone (±10\%) can also be decided to provide decision-making assistance that is more weighted towards the driver's safety and helps avoid sweeping confusion or immediate changes in the display messages.

## 5. Summary and conclusions

The present study is carried out to identify the zone where the dilemma in decision-making during the amber phase occurs. Using empirical vehicular trajectory data, different traffic behaviour parameters and factors pertaining to the traffic infrastructure are recorded for several vehicles traversing through the intersection during the amber phase. Simultaneously, the driver's decision to stop or pass (go) during the amber phase is also recorded for respective vehicles. Since the decision to stop or pass is binary, a binary logistic regression analysis is performed to model the driver's decision based on the exhibited traffic behaviour parameters and functional aspects of traffic infrastructure.

![](https://cdn.mathpix.com/cropped/3517ba1b-38be-4b61-b7f2-f98a4ae36d04-12.jpg?height=598&width=1541&top_left_y=179&top_left_x=173)
Fig. 6. Driver Assistance in decision making during dilemma zone.

Data from two study intersections are used for model development and internally validated using an 80-20 random split for development and validation. The transferability of the model is also checked using external validation on the data set for the third location (L3). Two models are developed in this study. The Point Data model (Table3) focuses on easier applicability and a passive measure for driver's decision assistance. The Trajectory Data model (Table 5) provides an active and dynamic method for stopping probability and dilemma zone identification. A possible application of TDM for in-vehicle driver assistance is also studied (Fig. 6). TDM also provides more concise dilemma zone identification (Fig. 4b) and accurate stopping probability estimation (better model fit results from Table 5) compared to PDM.

The effect of different traffic parameters on the dilemma zone is also highlighted (Fig. 6). The parameters of vehicle speed, acceleration, and lateral movement are inversely proportional to the stopping probability. Moreover, the parameters of distance from the stop line, and carriageway width appear to be directly proportional to the stopping probability. For the vehicle type, as the vehicle size increase, the stopping probability is observed to increase. In addition, as for lateral location, in simple words, it can be said that, as the vehicle position shifts towards median side lanes, the stopping probability is observed to increase.

The study focuses only on the distance-based dilemma zone, and hence, the time-based dilemma zone is not studied. However, the authors believe that integrating distance and time-based dilemma zone models shall lead to a more precise and robust model to aid and stimulate the driver's decision and hence forms the basis of the future scope of this study. Additionally, the data for this study was collected from under saturated conditions. As the saturation ratio at an intersection increases, the speed decreases, and the dilemma zone will shift towards the stop line. Still considering the complexities between different traffic behaviour parameters at signalized intersections observed in this study and reported in the literature (Chauhan et al., 2021a), data from intersections with varying degrees of saturation shall help enhance the model's reliability and fit. Lastly, multiple parameters related to traffic infrastructure were found significant in past literature and in this study, although many were omitted due to co-linearity. Hence, the upgradation of the proposed model from different metropolitans and varying degrees of traffic infrastructure parameters serves as another future scope for this research.

## 6. Contribution of the study

The present study analyzed the dilemma in making the stop and go decision by the vehicle drivers in mixed traffic conditions during the amber phase at signalized intersections. The specific research contributions of the present study to the existing body of literature are as follows

- The present study uses empirical trajectory data acquired from three signalized intersections with varying traffic operations and infrastructure characteristics to develop driver decisions to stop or pass during the amber phase of the signal cycle.
- Two models are developed to predict the driver's decision and hence supplement in identifying the dilemma zone to provide active and passive drivers decision assistance systems for safe and efficient traffic movement.
- Both the models proposed are tested for prediction accuracy and transferability. Upon comparison with the existing models (past literature), both the developed models are observed to exhibit a higher degree of accuracy and dependable results.
- The Point data model is developed to provide reliable dilemma-zone identification from the most basic of data easily observable on the field and hence aid in providing passive measures to inform the drivers of the dilemma zone.
- The Trajectory data model is developed by considering multiple traffic behaviour parameters that are exhibited by the vehicle drivers after observing the onset of the amber phase. Using multiple factors is observed to aid in a more accurate and concise dilemma zone.

- Additionally, with a connected environment system and advances in onboard vehicular technology, the TDM can also aid in a safer decision-making process (to stop or go) during the amber phase in real-time, hence functioning as a dynamic driver decision assistance system.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgement

The authors also acknowledge the contribution of Mr. Harendra Pratap Singh in data collection. No funding was received for the excution of this study.

## References

Abbas, M., Machiani, S. G., Garvey, P. M., Farkas, A., \& Lord-Attivor, R. (2014). Modeling the Dynamics of Driver's Dilemma Zone Perception Using Machine Learning Methods for Safer Intersection Control. Mid-Atlantic Universities Transportation Center. https://rosap.ntl.bts.gov/view/dot/27315. (Accessed April 2021).
Baratian-Ghorghi, F., Zhou, H., \& Franco-Watkins, A. (2017). Effects of red light cameras on driver's stop/go decision: Assessing the green extension hypothesis. Transportation Research Part F: Traffic Psychology and Behaviour, 46, 87-95. https://doi.org/10.1016/j.trf.2017.01.008. Elsevier Ltd.
Bhattacharyya, K., Maitra, B., \& Boltze, M. (2020). Calibration of Micro-Simulation Model Parameters for Heterogeneous Traffic using Mode-Specific Performance Measure. Transportation Research Record: Journal of the Transportation Research Board, 2674(1), 135-147. https://doi.org/10.1177/0361198119900130
Biswas, S., Ghosh, I., \& Chandra, S. (2017). Influence of signal countdown timer on efficiency and safety at signalized intersections. Canadian Journal of Civil Engineering, 44(4), 308-318. https://doi.org/10.1139/cjce-2016-0267
Calvi, A., \& Petrella, C. (2022). An evaluation of the effectiveness of countermeasures for improving the safety of dilemma zones: A driving simulator study. Transportation Research Part F: Traffic Psychology and Behaviour, 87(May), 295-312. https://doi.org/10.1016/j.trf.2022.04.013
Chauhan, R., Dhamaniya, A., \& Arkatkar, S. (2021a). Driving Behavior at Signalized Intersections Operating under Disordered Traffic Conditions. Transportation Research Record: Journal of the Transportation Research Board. https://doi.org/10.1177/03611981211033863
Chauhan, R., Dhamaniya, A., \& Arkatkar, S. (2021b). Spatiotemporal Variation of Rear-End Conflicts at Signalized Intersections under Disordered Traffic Conditions. Journal of Transportation Engineering, Part A: Systems, 147(11), 14. https://doi.org/10.1061/jtepbs. 0000589
Chauhan, R., Dhamaniya, A., \& Arkatkar, S. (2022). Challenges in Rear-end Conflicts Based Safety Assessment of Highly Disordered Traffic Conditions. Transportation Research Record: Journal of the Transportation Research Board. In press.
Franses, P. H. (1991). Moving average filters and unit roots. Economic Letters, 37(4), 399-403. https://doi.org/10.1016/0165-1765(91)90077-X
Gates, T. J., \& Noyce, D. A. (2010). Dilemma zone driver behavior as a function of vehicle type, time of day, and platooning. Transportation Research Record, 2149, 84-93. https://doi.org/10.3141/2149-10
Gazis, D., Herman, R., \& Maradudin, A. (1960). The Problem of the Amber Signal Light in Traffic Flow. Operations Research, 8(1), 112-132. https://doi.org/10.1287/opre.8.1.112
Hurwitz, D. S., Wang, H., Knodler, M. A., Ni, D., \& Moore, D. (2012). Fuzzy sets to describe driver behavior in the dilemma zone of high-speed signalized intersections. Transportation Research Part F: Traffic Psychology and Behaviour, 15(2), 132-143. https://doi.org/10.1016/j.trf.2011.11.003. Elsevier Ltd.
Hussein, M., Sayed, T., El-Basyouny, K., \& de Leur, P. (2020). Investigating safety effects of wider longitudinal pavement markings. Accident Analysis \& Prevention, 142 (July), 105527. https://doi.org/10.1016/j.aap.2020.105527. Elsevier.
Jianwen, S., Urbanik, T., \& Han, L. D. (2007). Effectiveness of alternative detector configurations for option zone protection on high-speed approaches to traffic signals. Transportation Research Record, 2035, 107-113. https://doi.org/10.3141/2035-12
Kanagaraj, V., Asaithambi, G., Toledo, T., \& Lee, T.-C. (2015). Trajectory Data and Flow Characteristics of Mixed Traffic. Transportation Research Record: Journal of the Transportation Research Board, 2491(1), 1-11. https://doi.org/10.3141/2491-01
Köll, H., Bader, M., \& Axhausen, K. W. (2004). Driver behaviour during flashing green before amber: A comparative study. Accident Analysis \& Prevention, 36(March), 273-280. https://doi.org/10.1016/S0001-4575(03)00005-8
Liu, Y., Chang, G. L., Tao, R., Hicks, T., \& Tabacek, E. (2007). Empirical observations of dynamic dilemma zones at signalized intersections. Transportation Research Record, 2035, 122-133. https://doi.org/10.3141/2035-14
Majhi, R. C., \& Senathipathi, V. (2021). Analyzing driver's response to yellow indication subjected to dilemma incursion under mixed traffic condition. Journal of Traffic and Transportation Engineering (English Edition), 8(1), 107-116. https://doi.org/10.1016/j.jtte.2019.05.005. Elsevier Ltd.
Montanino, M., \& Punzo, V. (2015). Trajectory data reconstruction and simulation-based validation against macroscopic traffic patterns. Transportation Research Part B: Methodological, 80, 82-106. https://doi.org/10.1016/j.trb.2015.06.010. Elsevier Ltd.
MoRTH. (2019). Road Accidents in India. Ministry of Road Transport and Highway. New Delhi: Government of India. https://morth.nic.in/sites/default/files/RA_Uploading.pdf. (Accessed March 2020).
Munigety, C. R., Vicraman, V., \& Mathew, T. V. (2014). Semiautomated Tool for Extraction of Microlevel Traffic Data from Videographic Survey. Transportation Research Record: Journal of the Transportation Research Board, 2443(1), 88-95. https://doi.org/10.3141/2443-10
Najmi, A., Choupani, A. A., \& Aghayan, I. (2019). Characterizing driver behavior in dilemma zones at signalized roundabouts. Transportation Research Part F: Traffic Psychology and Behaviour, 63, 204-215. https://doi.org/10.1016/j.trf.2019.04.007. Elsevier Ltd.
Papaioannou, P. (2007). Driver behaviour, dilemma zone and safety effects at urban signalized intersections in Greece. Accident Analysis \& Prevention, 39(1), 147-158. https://doi.org/10.1016/j.aap.2006.06.014
Pathivada, B. K., \& Perumal, V. (2019). Analyzing dilemma driver behavior at signalized intersection under mixed traffic conditions. Transportation Research Part F: Traffic Psychology and Behaviour, 60, 111-120. https://doi.org/10.1016/j.trf.2018.10.010. Elsevier Ltd.
Pawar, D. S., Pathak, D., \& Patil, G. R. (2020). Modeling dynamic distribution of dilemma zone at signalized intersections for developing world traffic. Journal of Transportation Safety \& Security, 1-19. https://doi.org/10.1080/19439962.2020.1852464. Taylor \& Francis.
Punzo, V., Borzacchiello, M. T., \& Ciuffo, B. (2011). On the assessment of vehicle trajectory data accuracy and application to the Next Generation SIMulation (NGSIM) program data. Transportation Research Part C: Emerging Technologies, 19(6), 1243-1262. https://doi.org/10.1016/j.trc.2010.12.007
Raju, N., Kumar, P., Reddy, C., Arkatkar, S., \& Joshi, G. (2017). Examining Smoothening Techniques for Developing Vehicular Trajectory Data under Heterogeneous Conditions. Journal of the Eastern Asia Society for Transportation Studies, 12(2017), 1549-1568. https://doi.org/10.11175/easts.12.1549.
Rakha, H., Amer, A., \& El-Shawarby, I. (2008). Modeling driver behavior within a signalized intersection approach decision-dilemma zone. Transportation Research Record, 2069, 16-25. https://doi.org/10.3141/2069-03
Tang, K., Boltze, M., Nakamura, H., \& Tian, Z. (2019). Global Practices on Road Traffic Signal Control. WCTRS Book Series. Elsevier. https://doi.org/10.1016/C2017-0-02878-1
Tang, K., Wang, F., Yao, J., \& Sun, J. (2017). Empirical Analysis and Modeling of Stop-Line Crossing Time and Speed at Signalized Intersections. International Journal of Environmental Research and Public Health, 14(9), 1-13. https://doi.org/10.3390/ijerph14010009

Venthuruthiyil, S. P., \& Chunchu, M. (2018). Trajectory reconstruction using locally weighted regression: A new methodology to identify the optimum window size and polynomial order. Transportmetrica A: Transport Science, 14(10), 881-900. https://doi.org/10.1080/23249935.2018.1449032
Wang, F., Tang, K., Xu, Y., Sun, J., \& Li, K. (2016). Modeling Risky Driver Behavior Under the Influence of Flashing Green Signal with Vehicle Trajectory Data. Transportation Research Record: Journal of the Transportation Research Board, 2562, 53-62. https://doi.org/10.3141/2562-07
Wei, H., Li, Z., Yi, P., \& Duemmel, K. (2011). Quantifying dynamic factors contributing to dilemma zone at high-speed signalized intersections. Transportation Research Record, 2259, 202-212. https://doi.org/10.3141/2259-19
Wei, Y., Li, K., \& Tang, K. (2019). Trajectory-based identification of critical instantaneous decision events at mixed-flow signalized intersections. Accident Analysis \& Prevention, 123(February), 324-335. https://doi.org/10.1016/j.aap.2018.11.019. Elsevier.
Wu, Y., Abdel-Aty, M., Ding, Y., Jia, B., Shi, Q., \& Yan, X. (2018). Comparison of proposed countermeasures for dilemma zone at signalized intersections based on cellular automata simulations. Accident Analysis \& Prevention, 116(November), 69-78. https://doi.org/10.1016/j.aap.2017.09.009. Elsevier.
Yan, X., Radwan, E., Guo, D., \& Richards, S. (2009). Impact of 'Signal Ahead' pavement marking on driver behavior at signalized intersections. Transportation Research Part F: Traffic Psychology and Behaviour, 12(1), 50-67. https://doi.org/10.1016/j.trf.2008.07.002. Elsevier Ltd.
Zegeer, C. V., \& Deen, R. C. (1978). Green-extention systems at High-speed Intersection. Kentucky Transportation Center, University of Kentucky, 496(April). https://doi. org/10.13023/KTC.RR.1978.496
Zhang, Y., Chuanyun, Fu, \& Hu, L. (2014). Yellow light dilemma zone researches: a review. Journal of Traffic and Transportation Engineering, (October), 338-352. https://doi.org/10.1016/S2095-7564(15)30280-4
World Health Organization (2018). Global Status report on Road Safety. https://apps.who.int/iris/rest/bitstreams/1164010/retrieve (Accessed July 2019).


[^0]:    * Corresponding author.
    E-mail addresses: ritvikdchauhan@gmail.com (R. Chauhan), adhamaniya@gmail.com (A. Dhamaniya), sarkatkar@gmail.com (S. Arkatkar).

[^1]:    * Insignificant at 95\% confidence interval but observed to be significant at 90\% confidence interval.

[^2]:    - value not available.
    * Insignificant at 95\% confidence interval but observed to be significant at 90\% confidence interval.

