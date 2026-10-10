# Conflict-Based safety evaluations at unsignalized intersections using surrogate safety measures 

Dungar Singh ${ }^{\mathrm{a}, *}$, Pritikana Das ${ }^{\mathrm{a}}$, Indrajit Ghosh ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}}$ Department of Civil Engineering, Maulana Azad National Institute of Technology Bhopal, 262003, India<br>${ }^{\mathrm{b}}$ Department of Civil Engineering, 247667, Indian Institutes of Technology Roorkee, India

## ARTICLE INFO

Keywords:
Traffic safety management
Traffic conflicts
Proactive approach
Surrogate safety measures


#### Abstract

Conflict-based road safety assessments may provide a deeper insight into the processes leading to crashes compared to assessments solely based on field crash data. The evaluation of road safety is conducted on specific road segments using different surrogate measure of safety indicators, such as temporal, spatial, and kinematic proximity measures, depending on the relevant context and applicability of these measures. Therefore, this study endeavored to develop a methodology by adopting safety measures such as post encroachment time (PET) and conflicting speeds of through vehicles for crossing maneuvers and time to collision (TTC) for rear-end collisions at five unsignalized intersections in urban mixed traffic conditions. Critical conflicts are calculated by calculating a speed variable known as the critical speed, which is based on the braking distance. A study found that the motorized two wheeler (MTW) categories involve the highest proportion of critical conflict with right-turning vehicles, followed by cars, autos, and light commercial vehicle (LCVs). Furthermore, crossing conflicts were modeled as a function using the generalized linear regression approach. The findings revealed that the most significant factors were traffic volume and vehicular composition in a conflicting stream. The unsupervised classification technique kmean clustering was used to determine the defined severity level threshold for rear-end maneuvers. The result observed was that a TTC threshold of less than 1.15 s was identified as highrisk vehicular interaction.

Additional investigation indicated that presence of certain moving vehicle categories, including MTWs and cars, led to a higher proportion of critical crossing conflicts. The conceptualized safety framework can be applied to evaluate safety at unsignalized intersections in the mixed traffic scenarios.


## 1. Introduction

Road safety is poses a significant concern in growing economies such as India. Where vehicles frequently permeate through traffic along an intended path, the traffic is known as non-lane base movement. This frequently results in less attention being focused on safety issues, which causes too many crashes. With approximately 1.5 million fatal crashes annually, India currently holds the worst road crash rate worldwide [1].

According to a recent accident report, 2020 has seen a $12.86 \%$ decrease from the prior year owing to COVID restrictions.

[^0]Approximately $19.84 \%$ of the 11,654 crashes and $18.72 \%$ of the 2535 fatalities occurred at unsignalized T-intersections [1]. The complexity of a right turn and through movements at unsignalized T-intersections make conflicts more serious [2-4]. These facilities mainly use priority rules and stop control to regulate traffic. Therefore, a safe space opens, and the vehicles in the minor approach merge into the major approach, which has priority for right-of-way. In contrast, in developing countries such as India, priority regulations and rules are not obeyed by drivers; therefore, drivers sense equal priority when navigating an intersection [4-8]. Henceforth, due to their ease of manoeuvrability and driver propensity for aggressive driving, drivers of smaller vehicles, such as MTWs and auto rickshaws, are responsible for 21\% of all crashes and fatalities in Indian mixed traffic situations [1]. At intersections, the manoeuvre of left-turning traffic rarely causes severe problems. However, critical conflict situations mostly occur between vehicles making right turns and through traffic, leading to hazardous conditions and an increased risk of collisions. So that, there is necessary to conduct trustworthy safety analysis to greatly enhance safety and reduce the number of crashes. Over the years, researchers have devised various methods to evaluate traffic safety. These approaches include crash-based before-and-after studies [9], the identification of black spot programs [10], statistical modeling [11], and road safety audits, [10]. These techniques mostly rely on crash data from the past and expert, knowledgeable field observations. Safety is evaluated through various statistical methods, primarily focusing on crash occurrences as a measure. Traffic crash assessment can assist in understanding the common pattern and help identify key contributing elements that facilitating the implementation of appropriate countermeasures. Therefore, a crash-based assessment is logically sound and trustworthy. The conventional crash-based assessment follows a reactive approach that shows significant drawbacks relying on police-reported crash data, which suffers from under-reporting and inaccurate information about crash patterns. Crash data is generally biased across multiple resources and does not define a pre-crash scenario based on location [12,13]. Therefore, safety evaluation methods that are reliable, fast, and do not solely rely on crash data are desperately needed. A traffic based conflict assessment can assess high-risk circumstances that may result in a potential crash, as illustrated by Hyden's pyramid [14]. In keeping with this, a couple of review papers are available on the utilization of traffic conflict approach in road facilities safety assessments [15-19]. The traffic conflict approach may be determined the frequency of near-miss crashes directly in moving traffic. Globally, researchers have advocated for the proactive use of traffic conflicts for safety analysis. Traffic conflict-based safety assessment is preferable to crash-based analysis because it complements (1) improving the efficiency and speed of road safety evaluation, (2) elucidating the relationship between risk and various design features, (3) providing information on hazardous interactions, thus establishing a link between risky driving and driver behavior, (4) describing the failure mechanisms that cause crashes, and (5) defining the collision risk process more precisely in both peak and non-peak traffic situations. Researchers have developed several proximal indicators that indicate proximity to crashes and may be employed to evaluate different road facilities safety through the traffic conflict technique. However, prior to implementing this type of process, vehicle trajectories must be used to determine the number or seriousness of potentially dangerous scenarios that might appear on certain road infrastructure to determine standards of safety. The most well-known of these surrogate measure of safety (SMoS) indicators are PET and TTC.

The procedure for extracting PET from the recorded video is demonstrated in Fig. 1. PET is calculated using equation (1) as follow:

$$
P E T=t_{2}-t_{1}(\mathrm{sec})
$$

It is depict the duration between the departure of the first road user $\left(\mathrm{t}_{1}\right)$ from a shared spatial zone and the arrival of the second user $\left(\mathrm{t}_{2}\right)$ in that same zone [20].

TTC value at instant is times left until a potential collision between two vehicles has occurred if the their current trajectories and speed difference are unchanged [21,22], as depicted in Fig. 2: a leader-follower pair. Therefore, equation (2) shows, that TTC can be determined as subsequent vehicle (F) at instant relative to a leading vehicle (L) against a rear-end collision.

$$
\text { TTC }=\frac{X_{l}-X_{f}-L_{l}}{V_{f}-V_{l}}(\mathrm{sec}) \forall X_{f}>X_{l}
$$

![](https://cdn.mathpix.com/cropped/1cf93c9c-4996-436f-b825-7ba5fa514336-02.jpg?height=540&width=768&top_left_y=1797&top_left_x=562)
Fig. 1. PET data extraction procedure.

![](https://cdn.mathpix.com/cropped/1cf93c9c-4996-436f-b825-7ba5fa514336-03.jpg?height=330&width=1092&top_left_y=181&top_left_x=399)
Fig. 2. TTC data extraction procedure.

Whereas:
$\mathrm{V}_{\mathrm{f}}=$ following vehicle speed $(\mathrm{m} / \mathrm{s}) ; \mathrm{V}_{1}=$ leading vehicle speed $(\mathrm{m} / \mathrm{s}) ; \mathrm{X}_{1}=$ position of leading vehicle, $\mathrm{X}_{\mathrm{f}}=$ position of following vehicle, $\mathrm{l}_{\mathrm{l}}=$ Conflicting vehicle length. TTC appears to be important only in situations where the follower vehicle has a greater speed than the leader vehicle. Consequently, in normal vehicular interaction, the vehicle of follower vehicle was lower than that of the leader vehicle.

With this research motivation, the current study objective is to develop separate conflict-based assessments for unsignalized intersections with diverse geometries and traffic characteristics in mixed traffic conditions. The study assesses the percentage of critical crossing conflicts using important surrogate measures PET and conflicting speed vehicles (CSVs), and generalized linear regression will be used to identify significant parameters influencing target variable number conflicts, whereas TTC is being used to determine the severity risk of approaching vehicle flow at intersections.

## 2. Literature review

Over the past few decades, there has been a plethora of studies aimed at assessing the safety of different road facilities. Urban road traffic management is a critical issue because only efficient traffic control strategies can improve the safety of urban roads. Researchers have focused on using traffic conflict approach with the implementation of different SMoS to evaluate vehicle safety in various traffic facilities because of issues with road crash data, both qualitatively and quantitatively. Utilizing of the micro-simulation model in roundabout safety analysis [23], calibrated VISSIM and AIMSUM for different types of roundabouts, and vehicle trajectories from micro-simulation software were used to determine traffic conflict in Surrogate Safety Assessment Model (SSAM) software. [24], developed a novel safety indicator, namely the rear-end crash risk index (RCRI), to access continuous moving vehicles conflicts extracted from the Shanghai naturalistic driving study dataset. Additionally, the authors of the implemented linear regression model observed significant effects of traffic density, driving behavior, day of the week, and time of day on vehicle driving risks [25]. used PET to recommend that left-turn path-coordinated intersection management improve safety levels and travel efficiency at intersections. Analyze the safety of signalized intersections, researchers [26], used safety measures PET and $\mathrm{T}_{2}$ to analyze near-crash critical bicycle-vehicle conflict. Their study authors found that the prediction of conflict using random forest is better than other algorithms such as logistic regression and support vector machine (SVM). Analyzing skid safety hazards [27], revealed that SMoS, skid marks, show a strong linear correlation between rear-end crashes on freeway sections. The authors [6] had success in developing a classification and regression tree (CART) model with an accuracy rate of $83 \%$ and a logistic regression model that correctly predicted $79 \%$ of fatal crashes. These models are essential for comprehending and tackling the causes of road collision deaths in India. Researchers [28] assessed the safety of pedestrians that considered highly vulnerable at intersections. The researcher used an unmanned aerial vehicle video technique for the analysis of PET and relative-TTC (RTTC). The results revealed many risky driving behaviors of right-turn vehicles around and outside crosswalks. [29], taking into account the vehicle speed variation coefficient throughout the highway to different truck proportions and the SMoS 85th percentile speed minus the 15th percentile speed (85\%V-15\%V). These tests were conducted at different times, and machine learning algorithms such as the k -mean and SVM were used to assess the traffic conflict conditions at various times. In their analysis of road safety in Indian mixed traffic flow, researchers such as [30], evaluated crossing conflict at unsignalized intersections. Surrogate measures PET used to categorize critical and noncritical conflicts. The implemented Tweedie distribution regression model revealed that critical and non-critical conflicts are significantly influenced by factors like as traffic volume, composition, time of day, and intersection geometry. But some researchers, like [3,30-32] found critical conflict using the critical speed, which was developed by combining the vehicle's speed and the PET. In their study [33], analyzed the impact of traffic conflict, MTW, and auto on critical and noncritical conflicts at an unsignalized intersection using a truncated negative binomial regression model. The authors observed that smaller vehicles have a significant influence on traffic conflicts [7]. revealed that key crossing conflicts are significantly Influenced by the number and make-up of both violating and conflicting traffic streams. Higher offending volume correlates with an rise in conflicts, while conflicting volume shows a decrease in conflicts. Intersection geometry plays a crucial role, with central islands reducing negative conflicts but increasing positive conflicts. Using many SMoS indicators, including PET, Delta t ( $\Delta \mathrm{t}$ ), and the predicted loss of kinetic energy ( $\Delta \mathrm{KE}$ ) at unsignalized intersections [34], created the conflict severity index (CSI). The authors observed that at a specific PET and $\Delta \mathrm{t}$ threshold, the severity index (CSI) increases with increasing vehicle speed, relative mass difference, and conflict angle. [3], used quantitative and qualitative techniques to evaluate critical conflict at unsignalized intersections. It was found that the PET threshold of 1 s was used to define critical conflict. However [35], employed modified TTC (MTTC) to analyze the safety of ordered and disordered traffic conditions. The author estimated the conflict using
simulated vehicle Next Generation Simulation (NGSIM) trajectory data and compared it with real-time crash data. The results revealed a strong temporal and spatial correlation with actual crashes. The exhaustive literature review reveals that road safety is a major concern in both homogenous and heterogenous traffic conditions. Researchers use multiple surrogate safety measures to evaluate the safety of various road facilities, whereas few studies have used a virtual environment, such as a micro-simulation tool, in addition to SSAM software. However, it shows that there is no standard for selecting traffic surrogate indicators and severe conflict levels. Each surrogate indicator has advantages, disadvantages, and appropriateness that the scenario must weigh. However, research evaluating the influence of road geometry traffic volume and composition, using an empirical approach is scarce. The assessment of rear-end conflict in approaching lanes at unsignalized intersections has been heavily ignored in previous research. Based on rear-end conflict severity, it can be defined as critical or non-critical, leading to the development of suitable surrogate indicators. In disordered traffic scenarios, vehicles with diverse static and dynamic features and poor lane discipline interact in several dimensions of space and time. Therefore, assessing safety at traffic facilities in heterogeneous areas is more difficult. Henceforth, above the concern, current study endeavors to assess safety at unsignalized intersections in the hope that the contribution made by this study will serve as a foundation and insights and initiate discussions on operational policy changes in traffic conditions, focusing on enhancing safety. These discussions can lead to proactive measures for improving safety in transportation systems.

## 3. Study methodology

In this study, the safety of five three-arm unsignalized intersections was analyzed using different SMoS. All intersections have two approaches along a major road, and a third approach merge a minor road. Indian traffic scenario: vehicles drive on the left, so that the left turn from a minor road and a major road at unsignalized intersection, rarely involved in the conflict, whereas vehicles from both major and minor approaches must stop and yield at the intersection before proceeding to cross the through traffic on the major road. Right-turning vehicles (offending vehicles) have to identify an acceptable gap to cross through conflicting traffic on major roads. In cases where major roads have high traffic volumes, crossing vehicle drivers will have to wait longer to find adequate gaps to cross the road. In high traffic volumes, vehicles on major roads take evasive actions to decelerate or stop vehicles simultaneously. Based on an indepth overview of the available literature Fig. 3 depicts the study methodology. The study used a SMoS, namely TTC, PET, and conflicting vehicle speed to identify conflict. On major roads, there could be problems with every right-turning vehicle and approaching vehicles in every lane at the intersection. For both major and minor approaches, a crossing conflict occurs when the offending vehicle collides with a through-moving vehicle at the intersection. Rear-end collisions occur when two consecutive vehicles move upstream and downstream at an intersection, and the leader vehicle takes an evasive action, such as braking, while the following vehicle, which is decelerating, reacts to avoid collision. The following sections outline the safety analysis of unsignalized intersections and the application of SMoS in this study.

### 3.1. Site selection and data collection

The study selected three-arm unsignalized intersections situated in tier-2 Bhopal city. To collect real data, careful consideration was taken while selecting the study area for field data collection. The intersections were identified based on various selection criteria, geometric specification, and traffic characteristics such as (a) all the intersections had similar types of traffic facilities such as threelegged intersections, (b) moderate traffic volume on both priority and non-priority streams, (c) sites were devoid of side friction

![](https://cdn.mathpix.com/cropped/1cf93c9c-4996-436f-b825-7ba5fa514336-04.jpg?height=687&width=1082&top_left_y=1640&top_left_x=405)
Fig. 3. Flow chart of the proposed framework.

activities, bus stops, or roadside vendors, (d) motorist vehicle travel at their desired speed in urban conditions, (e) there were very few activities for pedestrians and bicycles, and (f) high vantage points were present near the location to capture video-graphic data. As per the above selection criteria, this study focuses on the speed of approaching vehicles at the intersection and right-turning vehicles for crossing conflicts. Fig. 4 shows snapshots of selected study locations. In terms of traffic flow characteristics, the selected study locations differ considerably. All selected intersection geometric and traffic characteristic details are demonstrated in Table 1. Traffic data were gathered from 12 p.m. to 6 p.m. encompassing both peak and off-peak hours, and recorded under favourable weather conditions. To obtain a clear view of the intersection area, a high-definition video camera is positioned at a high vantage point. where intersection areas are selected on the basis of the internal geometry of the influence area of interaction between different conflicting vehicles. Video graphic techniques were employed to collect data related to traffic conflict and operational traffic data from the study sites. To collect these data, different trap lengths were drawn on the intersection conflict area in recorded video using the semi-automated software Kinovea 9.4 [36]. Each intersection is represented by a unique identifier: 6-No Intersection (S1), Board Office Intersection (S2), Vaishali Nagar Intersection (S3), Ratnagiri Intersection (S4), and Neelbad Intersection (S5) for clearer visualization as shown in Fig. 4. Snapshot samples of Kinovea 9.4 grids placed on videographic-recorded sites (S1, S4) are shown in Fig. 4. The geometric configuration of each intersection was physically measured at each site to minimize obstructing traffic flow. At all intersections, two types of rear-end and crossing maneuvers are observed: (1) right-turning vehicles on both major and minor roads, as well as through-moving vehicles on the major roads; and (2) approaching vehicle maneuvers on the through movement at the intersections. Although both traffic movement crossing maneuvers and approaching maneuvers are observed to be more common at all intersections, the reason for this is that a single vehicle is involved in conflict with multiple vehicles. However, previous researchers have observed that crossing conflict is more severe at unsignalized intersections, [2,8,30,33,37].

### 3.2. Data extraction

Following data collection of intersections, the recorded video is transferred to a PC where all necessary traffic data are extracted for further analysis, such as vehicular traffic volume, number of conflicts vehicular composition, and vehicle categories involved in conflict situations. Furthermore to obtain conflict data involves dividing the intersection conflict area into equal-sized square grids. Conflict data such as SMoS namely PET, TTC, and conflicting vehicle speed are extracted by overlapping a grid size to $3.5 \times 3.5 \mathrm{~m}$ using the semi-automated software Kinovea; 9.4. The grid aid in determining the precise physical location of the conflict by splitting the intersection area into smaller sections. This open source video processing program is often employed for sports assessment that demands the maximum degree of precision, such as monitoring a cricket ball and calculating the bowler's speed when the ball has been thrown [38]. These grids are spatial spots at an intersection where two conflicting vehicles are moving simultaneously. Recorded video graphics are displayed on the PC screen at a rate of 25 frames per second. The SMoS indicator PET and TTC are computed using the above section mentioned in equations (1) and (2). For calculating CSV that are conflicting through vehicles, the time for covering the distance over grids is recorded, and their speed is calculated. Furthermore, to reduce human error, operational traffic data, and conflict

![](https://cdn.mathpix.com/cropped/1cf93c9c-4996-436f-b825-7ba5fa514336-05.jpg?height=903&width=1392&top_left_y=1435&top_left_x=250)
Fig. 4. Camera views of the intersection sites.

Table 1
Intersection Inventory details of road geometric and traffic characteristic.
| Sn. No. | Intersection (Case) | Lane configuration | Peak hour volume (Veh/h) | Off-peak hour volume (Veh/h) | Avg. traffic volume (Veh/h) | Intersection area (sqm) | Coordinate (Longitude, Latitude) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 6-No Intersection (S1) | 4-lane X 2-lane | 3688 | 2456 | 3072 | 369 | 23.228435, 77.428528 |
| 2 | Board office Intersection (S2) | 6-lane X 2-lane | 4381 | 2765 | 3573 | 300 | 23.230611, 77.430229 |
| 3 | Vaishali Nagar Intersection (S3) | 4-lane X 2-lane | 3784 | 2036 | 2910 | 204 | 23.218075, 77.397720 |
| 4 | Ratnagiri Intersection (S4) | 6-lane X 6-lane | 4092 | 2484 | 3288 | 369 | 23.250986, 77.479554 |
| 5 | Neelbad Intersection (S5) | 4-lane X 2-lane | 2579 | 1667 | 2123 | 191 | 23.193503, 77.343529 |


are extracted by two skilled persons. For the current study, TTC for rear-end conflict for downstream movement and PET, the conflicting vehicle speed for right-turning movement, and crossing conflict were extracted. To facilitate comprehension, Fig. 5 provides a schematic illustration of crossing conflicts and rear-end conflicts with interacting vehicles at an unsignalized intersection. Conflicting vehicles are straight-moving vehicles on major roads, the offending vehicle is arriving from a minor road, and trialling vehicles in a rear-end collision where the vehicle speed is higher than that of the leading vehicle.

The hourly vehicular traffic volume of intersection sites varies from 1667 to 4381 veh/hour. Five types of vehicle categories were observed in the selected study sites: MTW, auto, car, LCV including passenger taxi, light and median goods vehicle, and other heavy commercial vehicle (HCV) including buses and small trucks. Tables 2 and 3 shows the composition of all vehicles involved in the observed conflict, both right-turning conflicts and conflicting vehicles. The proportion of MTWs is dominant, accounting for $46 \%-58 \%$ of all vehicle classifications at all sites. The proportion of cars is found to be the second largest followed by auto. Selected urban sites offer diverse traffic conditions and complex road infrastructure, making them ideal for safety assessments. Thus, MTWs accounted for the highest proportion as they are the main way of moving passengers from their origin to their destination.

### 3.3. Modelling of conflicts

Modelling of conflicts PET values use as crucial metric to examine crossing conflicts within the temporal proximity of a crossing event; a lower PET indicates closer proximity to a crash occurrence. Likewise, all traffic conflict interactions are not converting into crashes. Previous research identified critical conflicts based on the critical speed. Critical conflicts are identified from other non-critical events based on the critical speed. The fundamental idea is that a conflict should be classified as critical if the through moving vehicle conflicting speed appears to be higher than the related the critical speed [30,31,37]. Using this concept, critical speeds for various PET levels are calculated by assuming $\mathrm{g}=9.81 \mathrm{~m} / \mathrm{s} 2$ and coefficient of friction $=0.35$, as indicated in equation (3) below.

Critical speed, $\mathrm{v}=2 \mathrm{gf} \times$ PET Equation
In order to evaluate the safety of unsignalized intersections, considering critical crossing conflicts helps to better understand and quantify traffic safety that reflects near-crash scenarios. Only important crossing conflicts are considered in this current study. Crash and conflict prediction models are often developed using generalized linear models [39]. GLM comprises three elements: the response distribution (with mean ui), linear predictor BTX, and link function. It is commonly used when the sample being analyzed is a count dataset with flexible models that include a link function to link a linear predictor and its variability characterized by a distribution in an exponential dispersion group. The primary aims of the GLMs is to apply the concept of linear modeling to circumstances in which the independent variable and mean response have a linear relationship. The following criteria apply to this model: (1) it preserves the linear element; (2) distributions are limited to the exponential dispersion group; and (3) responses need to be independent.

![](https://cdn.mathpix.com/cropped/1cf93c9c-4996-436f-b825-7ba5fa514336-06.jpg?height=455&width=1388&top_left_y=1882&top_left_x=250)
Fig. 5. Conflict between the offending and conflicting vehicles: (a) crossing conflict; (b) rear-end conflict.

Table 2
Characteristics of PET and conflicting vehicle speed.
| Study sites | Intersection (S1) | Intersection (S2) | Intersection (S3) | Intersection (S4) | Intersection (S5) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| No of observed conflicts | 755 | 585 | 556 | 870 | 497 |
| Average PET (s) | 1.85 | 1.82 | 2.06 | 1.94 | 2.06 |
| Minimum PET (s) | 0.23 | 0.13 | 0.29 | 0.11 | 0.05 |
| Maximum PET (s) | 5.72 | 5.34 | 5.80 | 5.80 | 5.47 |
| Minimum CSV (km/h) | 13.21 | 11.92 | 10.55 | 11.52 | 13.82 |
| Average CSV (km/h) | 28.40 | 30.28 | 25.33 | 32.03 | 28.05 |
| Maximum CSV (km/h) | 50.47 | 54.11 | 50.33 | 52.38 | 49.28 |
| Composition of vehicles involved conflict (\%) MTW:Auto:Car:LCV:HCV | 58:5:24:8:5 | 47:12:26:11:4 | 53:12:26:6:3 | 46:7:27:7:13 | 53:10:26:7:4 |


Table 3
Characteristics of the TTC.
| Study sites | Intersection (S1) | Intersection (S2) | Intersection (S3) | Intersection (S4) | Intersection (S5) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| No of observed conflicts | 900 | 1165 | 1100 | 996 | 933 |
| Average TTC (s) | 1.83 | 1.43 | 2.30 | 1.40 | 2.03 |
| Minimum TTC (s) | 0.24 | 0.28 | 0.36 | 0.67 | 0.34 |
| Maximum TTC (s) | 4.92 | 4.97 | 4.93 | 4.91 | 2.02 |
| Composition of vehicles involved conflict (\%) MTW:Auto:Car:LCV:HCV | 56:9:19:12:4 | 54:9:26:9:2 | 55:8:20:11:6 | 49:4:25:9:13 | 57:9:18:12:4 |


where 'link function' refers to a mathematical function that employs a linear combination of explanatory variables to represent the categorical variable. When dealing with data involving continuous, categorical, and count-dependent variables, function g() frequently accommodates an identity, a logit, or a log transformation.

The GLM can be expressed in equation (4) as:

$$
\boldsymbol{g}(\boldsymbol{u} \boldsymbol{i})=\beta i X i
$$

Where $\boldsymbol{u} \mathbf{i}=E(y i)=g-(\beta i X i) . g()$ is a link function that uses a linear combination of explanatory variables to display the category variable. Function g() typically employs an identity, a log, or a logit transformation for continuous, categorical, and count-dependent variables, respectively.

The conflict model is expressed statistically as follows in Equation (5):

$$
\ln (Y i)=\beta o+\beta 1 * X i 1+\ldots \ldots+\beta m * X i m,
$$

where $\ln (\mathrm{Yi})=$ predicted the crossing conflicts; Xi1, Xim = covariates representing traffic related; $\beta 0, \beta 1, \beta \mathrm{~m}=$ model parameters.
The examination of crossing conflicts through PET analysis focuses on the temporal closeness to a potential crash event; with lower PET values indicating a higher degree of temporal proximity. However, it's essential to note that not all conflicts result in crashes. Research indicates that crossing conflicts with PET values less than or equal to 1 s closely resemble crash scenarios, irrespective of traffic composition [3,40]. As a result, this study uses the PET values to classify crossing conflicts as critical and noncritical crossing conflicts.

## 4. Analysis and discussion

From the videography data, the crossing conflict safety measure PET and rear-end conflict safety measure TTC were extracted from all study sites. Further estimated PET and TTC frequency distributions and exploratory analyses are conducted.

### 4.1. Frequency distribution of proximal indicators

The proximal distribution SMoS of PET and TTC thresholds, which vary from 0 to 6 s and 0-5 s, has been examined for all sites. Fig. 6 shows that at sites S-1, S-2, and S-4, the maximum PET thresholds are distributed from 0 to 2.5 s, respectively. At the intersection (S-3; S-5), a significant portion of the PET threshold lies within the range of 1-3 s.

The significant amount lies within the range of 1.5-2.5 s in the case of the TTC threshold distribution shown in Fig. 7 at that site (S-2; S-5). Whereas the TTC threshold at (S-1) ranges from 1.5 to 3 s, it ranges from 2 to 3 sat (S-3). At S-4, a significant amount of the TTC threshold lies within a range of 1-1.5 s.

### 4.2 Characteristics of the proximal indicators

Exploratory data analysis was conducted to ascertain the characteristics of safety measures, PET, TTC, and conflicting vehicle

![](https://cdn.mathpix.com/cropped/1cf93c9c-4996-436f-b825-7ba5fa514336-08.jpg?height=1416&width=1636&top_left_y=179&top_left_x=133)
Fig. 6. PET frequency distribution for intersections.

speed. Therefore, several parameters are estimated for this purpose, including the minimum, average, and maximum values of SMoS indicators as well as the preparation of vehicles presented at each site, as shown in Tables 2 and 3 The extracted data shows that for all study sites, 8357 conflicts are observed. Each crossing conflict analysis was relied on PET values and CSV, whereas the rear end conflict analysis was based on the TTC indicator. The PET and TTC threshold ranges are 0-6 s and 0-5 s, respectively, considered identifying conflicts. Conflicts with PET and TTC thresholds greater than 6 s and 5 s are common conflicts and are not harmful since the driver has enough time to keep maintain control of the vehicle and while take evasive action if necessary. The average PET value for all sites ranged from 1.82 to 2.06 s, and the TTC value ranged from 1.4 s to 2.30 s, which is a very low threshold. From this observation, both vehicles on the right of way and non-priority vehicles are at high risk at a three-legged intersection. However, the average speed of vehicles varies from 25 to 31 km/h. The average vehicle speed at the site (S-4) is higher than that at the other intersections because of the suburban area at the intersection. The average TTC threshold at site (S-4) is 1.4 s, which indicates that the right-hand vehicle is involved in a higher degree of collision compared to non-priority vehicles. It was discovered that MTWs accounted for the highest proportion of all sites, ranging from 46 \% to 58\%. Because MTWs are a more prevalent mode of transportation for moving passengers between locations, they are found in higher proportions across all sites. The proportion of cars was observed to be the second largest, followed by LCV.

### 4.3. Distribution of crossing critical conflicts

The observed conflict is based on safety measures such as PET from 0.5 to 6 s from each site, which are separated into different categories with an increment of 0.5 s. When there is a conflict, the lower threshold of safety measures for each group is used to calculate

![](https://cdn.mathpix.com/cropped/1cf93c9c-4996-436f-b825-7ba5fa514336-09.jpg?height=1646&width=1636&top_left_y=179&top_left_x=133)
Fig. 7. TTC frequency distribution for intersections.

the group critical speed. Critical conflicts are those having a certain PET threshold and conflicting speed higher than the corresponding calculated critical speeds [8,30,31]. The concept has been employed to identify the critical conflicts by on through moving vehicle, MTW, auto, car, LCV, and HCV, respectively. The sum of all vehicles involved in a critical conflict were found at each intersection is given as the total critical conflict. It is found at critical conflicts at the site S-1 (43.2\%), S-2 (40.51\%), S-3 (25.19\%), S-4 (43.44\%) and S-5 (30.37\%) respectively. Depending on the PET threshold and the vehicle conflicting speed, Table 4 shows that at all sites, through moving vehicle, MTW categories are involving the highest proportion of critical conflict with right turning movement vehicle followed by car, auto and LCV. It is thus pretty clear that there is a very high chance of collisions of MTW. Although the MTW has higher speed and manoeuvrability compared to other vehicles, which could increase the probability of collision, The reasons for that are the relatively small temporal gap between the right-turning vehicle and approaching through moving MTW in the conflict area, which in turn leads to a higher proportion of critical conflict. On the contrary, HCV, characterized by larger size and reduced manoeuvrability, tend to experience fewer critical conflicts at intersections. The decreased speed of HCVs at intersections contributes to lower critical conflict rates compared to other vehicles.

The study employs PET and CSV to differentiate critical conflicts from the overall crossing conflicts observed across all intersection

Table 4
Distribution of conflicts for through traffic with right-turning conflict.
| Study Site (Intersection) | Total number of conflict at Intersection | Through moving vehicle categories |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | MTW |  |  | Auto |  |  | Car |  |  | LCV |  |  | HCV |  |  |
|  |  | Total number of conflicts | Number of critical conflict | Percentage of critical conflict | Total number of conflict | Number of critical conflict | Percentage of critical conflict | Total number of conflict | Number of critical conflict | Percentage of critical conflict | Total number of conflict | Number of critical conflict | Percentage of critical conflict | Total number of conflict | Number of critical conflict | Percentage of critical conflict |
| S-1 | 755 | 435 | 218 | 28.9 | 36 | 16 | 2.1 | 183 | 55 | 7.3 | 62 | 28 | 3.7 | 39 | 9 | 1.2 |
| S-2 | 585 | 276 | 129 | 22.05 | 70 | 26 | 4.44 | 151 | 52 | 8.89 | 64 | 30 | 5.13 | 24 | 0 | 0 |
| S-3 | 556 | 297 | 79 | 14.21 | 61 | 18 | 3.24 | 143 | 32 | 5.76 | 36 | 8 | 1.44 | 19 | 3 | 0.54 |
| S-5 | 497 | 265 | 102 | 20.52 | 50 | 11 | 2.21 | 129 | 27 | 5.43 | 35 | 10 | 2.01 | 18 | 1 | 0.20 |
| S-4 | 870 | 399 | 189 | 21.72 | 59 | 36 | 4.14 | 231 | 108 | 12.41 | 61 | 30 | 3.45 | 120 | 15 | 1.72 |


sites. CSV that are higher than the critical speed is deemed critical conflict. The above Table 5 shows the frequency of conflicts at each site and the percentage of critical conflicts. The data indicate that there are between 140 and 378 critical conflicts at the selected study locations. Consequently, there is a noticeable increase in the proportion of critical conflicts, from 25.19\% to 43.44\%. All the locations are therefore equally risky; nevertheless, based on the critical conflict frequency and their proportional share, the study sites (S-1, S-4) are the most dangerous. Because the primary cause of critical crossing conflict situations at unsignalized intersections is the undisciplined driver behavior of non-prioritized vehicles right-turners, their movement must be managed to address these dangerous places. Therefore, to improve junction safety, several traffic control and calming techniques could be implemented. Warning signs can be implemented to draw attention to driver manoeuvrability. While installing camera intersections can help increase driver adherence to traffic regulations, on minor roads, Speed humps and speed tables can be built to restrict speed and enhance safety, and on major roads, a right turn lane can be given to encourage orderly movements.

### 4.3.1. Development of a generalized linear model crossing conflict

For the combination of all selected intersection datasets, PET data of each intersection was conducted to evaluate the significance of the different means of two different intersection datasets. It has been observed that the intersection p-value range varies from 0.209 to 0.870 . This denotes the null hypothesis, which claims that the PET values of the chosen dataset from intersections do not significantly differ from one another. Therefore, further analysis data have been compiled. At a 5-min data aggregation period, the total number of conflicts, traffic volume, critical conflicts, and vehicle composition were aggregated together. Table 6 provides an overview descriptive statistics of the dependent and independent variables.

The generalized linear model (GLM) was developed using a 5-min data aggregation period. GLM analysis was performed using independent variables that correlated with the dependent conflict. Descriptive statistics are shown in Table 6, which lists the variables considered for the analysis. The GLM analysis output, considering six parameters (MTW, Car, Auto LCV, HCV, and Volume), resulted in a model from SPSS 20.0, as illustrated in Table 7. The standard deviation of the output variable changed as a result of changes in the input variable is represented by coefficient B, and the positive or negative sign of coefficient B indicates a rise or fall in the output value resulting from changes in the input variable. Included in the model were the variables with $\mathrm{p}<0.05$. There is a substantial correlation between the MTW, Car, LCV, HCV, and volume with the number of conflicts. The model developed after considering six independent variables is displayed in equation (6).

Conflict $=-1.717+1.016(\mathrm{MTW})+0.988(\mathrm{Car})+0.973(\mathrm{LCV})+1.072(\mathrm{Auto})+1.018(\mathrm{HCV})-0.025($ Volume $)$ Equation (6)
Table 7 illustrates the significant influence of traffic volume on the number of crossing conflicts within conflict intervals. As traffic volume increases, there is a corresponding decrease in the number of conflicts. This is explained by the fact that when traffic volume increases, the gap in the traffic stream narrows. As a result, the offending stream's vehicles roll over narrower gaps, which lowers their speed, increases their PET, and reduces conflicts. The relationship between traffic volume and confrontations crossing conflicts is consistent with the results obtained by Refs. [2,7,41]. As there are more conflicts, there are more motor vehicles (MTW, Auto, Car, LCV, and HCV) in the conflicting stream. The developed GLM model yielded results for the Akaike information criterion (AIC) of 74.35 and the Bayesian information criterion (BIC) of 97.39. The model showed the best fit when the BIC was greater than the AIC.

In order to verify the model accuracy, the Poisson-Tweedie model was developed for conflict using the same variables. The established model produced findings with a BIC of 257.02 and an AIC of 233.98. Therefore, the GLM is shown to have a superior goodness-of-fit. As a result, based on traffic flow as well as intersection-related variables, the developed model is helpful in predicting crossing conflicts at other unsignalized intersections and accurately demonstrates the field situation.

### 4.4. Classification of the severity level

The TTC indicator was categorized based on several groups in order to measure the severity of conflict using the k-means clustering technique. In order to address clustering issues in machine learning, k-means is centroid-based algorithm [42]. Cluster validation was carried out to assess the quality of the clusters. Moreover, silhouette analysis is employed to identify the optimal number of clusters within a specific range of datasets. The MATLAB program was used to classify data for various k-values, producing groups that were divided into two, three, four, and five clusters. Fig. 8(a-c) displays the silhouette plots and average values for each cluster. The average of all-cluster silhouettes is known as the global silhouette value, and it functions as a useful validity metric for clustering. A higher global silhouette value denotes a robust structure, whereas a lower value indicates insufficient clustering [43,44]. [43], stated that a strong-quality cluster has a global silhouette value of 0.71-1.0. A value between 0.51 and 0.70 shows an average structure, 0.26 and 0.50 is a poor structure, and less than 0.25 is no appreciable structure. In this investigation, $\mathrm{k}=2$ had a global silhouette value of 0.75, $\mathrm{k}=3$ had a value of 0.54 , and $\mathrm{k}=4$ had a value of 0.74 . These values show that $\mathrm{k}=2$ was the maximum value; the two clusters were determined to be optimal. Thus, conflict intensity was divided into two groups. The first category indicates high-risk vehicular interaction, whereas a quick action is required from at least one user because of the very narrow spacing between the two vehicular.

Table 5
Characteristics of critical conflicts.
| Study Site | Intersection (S1) | Intersection (S2) | Intersection (S3) | Intersection (S4) | Intersection (S5) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| No. of observed conflicts | 755 | 585 | 556 | 870 | 497 |
| No. of critical conflicts | 326 | 237 | 140 | 378 | 151 |
| Percentage of critical conflicts (\%) | 43.2 | 40.51 | 25.19 | 43.44 | 30.37 |


Table 6
Descriptive statistics of selected variables.
| Variable Details |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | N | Minimum | Maximum | Mean | Std. Deviation |
| Dependent Variable | Conflict | 60 | 34.00 | 87.00 | 54.08 | 13.59 |
|  | MTW | 60 | 15.64 | 46.11 | 27.09 | 7.87 |
|  | Car | 60 | 8.10 | 31.32 | 16.57 | 5.29 |
|  | LCV | 60 | 0.82 | 8.96 | 4.35 | 1.70 |
|  | Auto | 60 | 0.00 | 10.20 | 3.84 | 2.00 |
|  | HCV | 60 | 0.00 | 7.83 | 2.25 | 2.23 |
|  | Volume | 60 | 18.00 | 49.00 | 30.17 | 7.51 |


Table 7
Model summary.
| Parameter | B | Std. Error | Exp(B) Sig. |
| :--- | :--- | :--- | :--- |
| (Intercept) | -1.717 | 0.9952 | 0.085 |
| MTW | 1.016 | 0.0133 | 0.000 |
| Car | 0.988 | 0.0182 | 0.000 |
| LCV | 0.973 | 0.0389 | 0.000 |
| Auto | 1.072 | 0.0281 | 0.000 |
| HCV | 1.018 | 0.0504 | 0.000 |
| Volume | -0.025 | 0.0120 | 0.039 |


The second is moderate-risk interaction; there is sufficient space between the two vehicles, and one user needs to act right away. Cluster analysis was used to determine the threshold value, which denotes the collision risk threshold from high to moderate. Fig. 8 (d) shows that when TTC is less than 1.15 s, the vehicular interaction is at high risk of collision. While the most commonly cited TTC threshold is 1.5 s, some earlier studies have increased the threshold to 2.5 s [31]. This shows that a determined threshold could be used to identify conditions for the analysis of high-risk vehicle interactions in mixed traffic conditions.

## 5. Conclusion

At an unsignalized intersection, traffic flow becomes very challenging in mixed traffic conditions. This is due to fast-moving approaching vehicle's potential to collide with other oncoming and turning vehicles at intersections due to their undisciplined behaviour of driver. As a result, this intricate move intensifies the conflict and increases the likelihood of a collision. For that reason, this study adopted a conflict-based safety evaluation approach to analyze the safety of five unsignalized intersections. The crossing conflict manoeuvre were characterized by incorporating vehicular CSV and PET. As a result, critical crossing conflicts are identified by determining another variable known as critical speed. Traffic Conflicts are identified as critical when conflicting vehicular speeds exceed the estimated critical speeds. Along with the potential surrogate indicator, TTC was used to identify rear-end conflicts in approaching traffic movements at intersections. The optimal TTC threshold for identifying significant rear-end conflict situations in approaching movements is observed to be 1.15 s. The result shows that a significant number of critical conflicts occurred in the turning movement at all intersections, from 25.19\% to 43.44\% This demonstrates that the driver of the vehicle accepts minor gaps and takes, which are essential and harmful to their safety. The percentage of critical conflicts involving MTWs is higher than that of other vehicles in conflicting maneuvers. As a result, this very short interval between the end of a right-turning vehicle's intrusion and the arrival of a moving MTW at the conflict zone rise the percentage of critical crossing conflicts. Moreover, a generalized linear model is employed to predict the occurrence of crossing conflicts based on factors such as traffic volume and composition. The frequency of crossing conflicts in the movement of traffic is highly influenced by the composition of the traffic. The potential for conflict increases with the proliferation of MTW, autos, cars, LCV, and HCV in conflicting streams. On the other hand, conflict drastically decreases when traffic volume increases. Overall, the study concluded that the conflict-based approach is efficient for evaluate of safety at unsignalized intersections, which are most vulnerable to all types of road facilities. Thus, the insights may be used to enhance safety at unsignalized intersections that have road geometry comparable to the chosen sites, where traffic volume ranges from 1667 to 4381 vehicles per hour. This study contains constraints that can be expanded to identify rear-end critical conflict in the approaching stream for the inclusion of more types of traffic facilities. It can also be performed through simulation using this concept. In conclusion, it can be argued that most India and other developing nations have severe problems with the accessibility and reliability of crash records.

## Data availability statement

Data will be available on request.

![](https://cdn.mathpix.com/cropped/1cf93c9c-4996-436f-b825-7ba5fa514336-13.jpg?height=1372&width=1390&top_left_y=179&top_left_x=250)
Fig. 8. Silhouette value for optimum cluster and TTC threshold value.

## Additional information

No additional information is available for this paper.

## CRediT authorship contribution statement

Dungar Singh: Writing - original draft, Visualization, Validation, Methodology, Investigation, Data curation, Conceptualization. Pritikana Das: Writing - review \& editing, Supervision, Conceptualization. Indrajit Ghosh: Writing - review \& editing, Supervision, Software, Conceptualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgment

The authors thank the anonymous referees for their helpful comments that improved the quality of the manuscript.

## References

[1] MoRTH, Road Accidents in India, Ministry of Road Transport \& Highways, Transport Research Wing, New Delhi, 2021.
[2] G. Zhang, Y. Qi, J. Chen, Exploring factors impacting paths of left-turning vehicles from minor road approach at unsignalized intersections, Math. Probl Eng. (2016), https://doi.org/10.1155/2016/1305890.
[3] M. Paul, I. Ghosh, Post encroachment time threshold identification for right-turn related crashes at unsignalized intersections on intercity highways under mixed traffic', Int. J. Inj. Control Saf. Promot. 27 (2) (2020) 121-135, https://doi.org/10.1080/17457300.2019.1669666.
[4] S.R. Bonela, B.R. Kadali, Review of traffic safety evaluation at T-intersections using surrogate safety measures in developing countries context', IATSS Res. 46 (3) (2022) 307-321, https://doi.org/10.1016/j.iatssr.2022.03.001.
[5] M. Advani, N.J. Gupta, S. Velmurugan, E. Madhu, S. Chandra, Defining and analyzing forceful gap behavior at unsignalized intersections, Transport. Res. Rec. 2674 (8) (2020) 420-428, https://doi.org/10.1177/0361198120925258.
[6] M. Mohanty, R. Panda, S.R. Gandupalli, R.R. Arya, S.K. Lenka, Factors propelling fatalities during road crashes: a detailed investigation and modelling of historical crash data with field studies, Heliyon. Nov 108 (11) (2022) e11531, https://doi.org/10.1016/j.heliyon.2022.e11531. PMID: 36387487; PMCID: PMC9663901.
[7] Aninda Paul, Ninad Gore, Shriniwas Arkatkar, Gaurang Joshi, Investigating and modeling the influence of PET types on crossing conflicts at urban unsignalized intersections in India, Int. J. Inj. Control Saf. Promot. (2023) 30, https://doi.org/10.1080/17457300.2022.2147194.
[8] M. Paul, I. Ghosh, Post encroachment time threshold identification for right-turn related crashes at unsignalized intersections on intercity highways under mixed traffic', Int. J. Inj. Control Saf. Promot. 27 (2) (2019) 121-135, https://doi.org/10.1080/17457300.2019.1669666.
[9] R. Elvik, The importance of confounding in observational before-and-after studies of road safety measures', Accid. Anal. Prev. 34 (5) (2002) 631-635, https://doi.org/10.1016/S0001-4575(01)00062-8.
[10] G. Kanellaidis, Aspects of road safety audits, J. Transport. Eng. 1 (December) (1999) 481-486.
[11] S. Daniels, T. Brijs, E. Nuyts, G. Wets, Extended prediction models for crashes at roundabouts, Saf. Sci. 49 (2) (2011) 198-207, https://doi.org/10.1016/j.ssci.2010.07.016.
[12] P. Songchitruksa, A.P. Tarko, The extreme value theory approach to safety estimation', Accid. Anal. Prev. 38 (4) (2006) 811-822, https://doi.org/10.1016/j.aap.2006.02.003.
[13] A. Chang, N. Saunier, Proactive methods for road safety analysis', SAE International (2017).
[14] C. Hydén, The Development of a Method for Traffic Safety Evaluation: the Swedish Traffic Conflicts Technique, Dept. of traffic planning and engineering, Lund University, Lund, Sweden, 1987.
[15] A. Arun, M.M. Haque, S. Washington, T. Sayed, F. Mannering, A systematic review of traffic conflict-based safety measures with a focus on application context, Analytic Methods in Accident Research 32 (2021) 100185, https://doi.org/10.1016/j.amar.2021.100185.
[16] D. Singh, P. Das, I. Ghosh, Surrogate safety assessment of traffic facilities under ordered and disordered traffic condition: systematic literature review, KSCE J. Civ. Eng. 27 (2023) 5008-5029, https://doi.org/10.1007/s12205-023-0979-y.
[17] D. Singh, P. Das, I. Ghosh, A review on surrogate safety measures using extreme value theory, in: Lecture Notes in Civil Engineering, vol. 434, Springer, Singapore, 2024, https://doi.org/10.1007/978-981-99-6090-3_51.
[18] D. Singh, P. Das, A review on surrogate safety measures in safety evaluation and analysis', Lecture Notes in Civil Engineering 273 (September) (2023) 113-129, https://doi.org/10.1007/978-981-19-4204-4_7.
[19] D. Ray Sarkar, K. Ramachandra Rao, N. Chatterjee, A review of surrogate safety measures on road safety at unsignalized intersections in developing countries, Accid. Anal. Prev. 195 (2024) 107380, https://doi.org/10.1016/j.aap.2023.107380.
[20] B.L. Allen, B.T. Shin, P. Cooper, Analysis of traffic conflicts and collisions.', Transport. Res. Rec. (667) (1978) 67-74.
[21] Hayward, Near-miss Determination through Use of Scale of Danger, Highway Research Board, 1971, pp. 24-35.
[22] K. Vogel, A comparison of headway and time to collision as safety indicators, Accid. Anal. Prev. 35 (3) (2003) 427-433.
[23] Orazio Giuffrè, Anna Grana, Maria Tumminello, Tullio Giuffrè, Salvatore Trubia, Antonino Sferlazza, Marko Rencelj, Evaluation of roundabout safety performance through surrogate safety measures from microsimulation, J. Adv. Transport. 1-14 (2018) (2018), https://doi.org/10.1155/2018/4915970.
[24] Q. Shangguan, T. Fu, J. Wang, R. Jiang, S. Fang, Quantification of rear-end crash risk and analysis of its influencing factors based on a new surrogate safety measure, J. Adv. Transport. (2021), https://doi.org/10.1155/2021/5551273.
[25] M. Yang, H. Yu, L. Bai, Simulation-based evaluation of variation in left-turn paths in the coordinated intersection management', J. Adv. Transport. (2021) https://doi.org/10.1155/2021/6243530.
[26] D. Rostami, A. Katthe, A. Sohrabi, Aryan, J. Arash, Predicting critical bicycle-vehicle conflicts at signalized intersections, J. Adv. Transport. (2020) 1-16, https://doi.org/10.1155/2020/8816616Shangguan.
[27] Y. Ma, W. Huang, Z. Tian, D. Li, H. Cai, J. Su, Research of surrogate measure for freeway crashes based on tire skid marks, J. Adv. Transport. (2021), https://doi. org/10.1155/2021/6673933.
[28] P. Chen, W. Zeng, G. Yu, Surrogate safety analysis of pedestrian-vehicle conflict at intersections using unmanned aerial vehicle videos', J. Adv. Transport. (2017) https://doi.org/10.1155/2017/5202150.
[29] Shengdi Chen, Shiwen Zhang, Yingying Xing, Jian Lu, Yichuan Peng, H. Zhang, The impact of truck proportion on traffic safety using surrogate safety measures in China, J. Adv. Transport. (2020) 1-15, https://doi.org/10.1155/2020/8636417.
[30] S. Shekhar Babu, P. Vedagiri, Proactive safety evaluation of a multilane unsignalized intersection using surrogate measures, Transportation Letters 10 (2) (2018) 104-112, https://doi.org/10.1080/19427867.2016.1230172.
[31] D. Singh, P. Das, P. Noor, Surrogate Safety Evaluation at Uncontrolled Intersection in Non-lane Base Traffic Conditions', vol. 93, European Transport/Trasporti Europei, 2023, pp. 1-16, https://doi.org/10.48295/et.2023.93.11.
[32] K.A. Srinivasula Reddy, Akhilesh Chepuri, Shriniwas S. Arkatkar, Gaurang Joshi, Developing proximal safety indicators for assessment of un-signalized intersection - a case study in Surat city, Transportation Letters 12 (5) (2020) 303-315, https://doi.org/10.1080/19427867.2019.1589162.
[33] Aninda Paul, Jaydip Goyani, Shriniwas Arkatkar, Gaurang Joshi, Modeling the effect of motorized two-wheelers and autorickshaws on crossing conflicts at urban unsignalized T- intersections in India using surrogate safety measures, Transport. Res. Procedia 62 (2022) 774-781, https://doi.org/10.1016/j.trpro.2022.02.096.
[34] M. Paul, I. Ghosh, Development of conflict severity index for safety evaluation of severe crash types at unsignalized intersections under mixed traffic', Saf. Sci. 144 (August) (2021) 105432 https://doi.org/10.1016/j.ssci.2021.105432.
[35] A. Charly, T.V. Mathew, Estimation of traffic conflicts using precise lateral position and width of vehicles for safety assessment', Accid. Anal. Prev. 132 (July) (2019) 105264 https://doi.org/10.1016/j.aap.2019.105264.
[36] Kinovea, C. Dehwko, Kinovea (2019). http://www.kinovea.org.
[37] M. Paul, I. Ghosh, Speed-based proximal indicator for right-turn crashes at unsignalized intersections in India', J. Transport. Eng., Part A: Systems 144 (6) (2018) https://doi.org/10.1061/jtepbs. 0000139.
[38] A. Kathuria, P. Vedagiri, Evaluating pedestrian vehicle interaction dynamics at un-signalized intersections: a proactive approach for safety analysis', Accid. Anal. Prev. 134 (2019) 105316 https://doi.org/10.1016/j.aap.2019.105316.
[39] M.V. Wüthrich, M. Merz, Introduction, in: Statistical Foundations of Actuarial Learning and its Applications, Springer Actuarial. Springer, Cham, 2023, https://doi.org/10.1007/978-3-031-12409-9_1.
[40] L. Peesapati, M. Hunter, M. Rodgers, Evaluation of post encroachment time as surrogate for opposing left-turn crashes, Transportation Research Record:Journal of the Transportation Research Board 2386 (2013) 42-51.
[41] J. Goyani, N. Gore, S. Arkatkar, Crossing conflict models for urban un-signalized T-intersections in India', Transportation Letters 00 (00) (2023) 1-9, https://doi.org/10.1080/19427867.2023.2250161.
[42] S. Guha, R. Rastogi, K. Shim, CURE: an Efficient Clustering Algorithm for Large Databases, ACM SIGMOD Conference, 1998.
[43] P. Spector, Stat 133 Class Notes 2013-Spring, Univ.of California, Berkeley, 2011. http://www.stat.berkeley.edu/\~s133/all2011.pdf. (Accessed 25 July 2016).
[44] Abhinav Kumar, Madhumita Paul, Indrajit Ghosh, Analysis of pedestrian conflict with right turning vehicles at signalized intersections in India, J. Transport. Eng. (2019) 145, https://doi.org/10.1061/JTEPBS.0000239.


[^0]:    * Corresponding author. Maulana Azad National Institute of Technology Bhopal, India.
    E-mail address: dsdudi97@gmail.com (D. Singh).

