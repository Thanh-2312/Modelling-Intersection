# Assessing right-turning vehicle-pedestrian conflicts at intersections using an integrated microscopic simulation model 

Peng Chen ${ }^{\mathrm{a}, \mathrm{b}}$, Weiliang Zeng ${ }^{\mathrm{c}, *}$, Guizhen Yu ${ }^{\mathrm{a}, \mathrm{b}}$<br>${ }^{\mathrm{a}}$ Beihang University, Beijing Key Laboratory for Cooperative Vehicle Infrastructure Systems and Safety Control, School of Transportation Science and Engineering, No. 37, Xueyuan Road, Haidian District, Beijing, CN, 100191, China<br>${ }^{\mathrm{b}}$ Beihang University, Beijing Advanced Innovation Center for Big Data and Brain Computing, No. 37, Xueyuan Road, Haidian District, Beijing, CN, 100191, China<br>${ }^{\mathrm{c}}$ Guangdong University of Technology, School of Automation, Guangdong, CN, 510006, China

A R T I C L E I N F O

Keywords:
Microscopic simulation
Signalized intersection
Pedestrian
Turning vehicle
Traffic conflict
Safety assessment


#### Abstract

Frequent vehicle-pedestrian conflicts deserve special attention for safety assessment at intersections. This study helps verify how the simulation as an innovative approach can be utilized for right-turning vehicle-pedestrian conflict assessment at intersection crosswalks prior to implementation. Various behavior models such as vehicle turning path, turning speed, gap acceptance model and pedestrian behavior model, have been established. Through integrating the calibrated models into one simulation platform, the stochastic behavior of vehicles and pedestrians under different geometric layouts and operational conditions can be reproduced. Based on the field data collected by an unmanned aerial vehicle (UAV) at two urban intersections in Beijing, China, it was demonstrated through validation of surrogate safety measures (SSMs), i.e., Post Encroachment Time (PET) and vehicle passing speed at conflict points, that the simulation model can reasonably represent the frequency and severity of conflict occurrence at signalized crosswalks. The sensitivity analysis results indicated that large dimensions and turning angles of intersections tend to result in undesirable safety performance.


## 1. Introduction

Intersections are critical elements in transportation network. The operational performance of intersections significantly affect the road traffic system (Chen et al., 2017a). At intersections various types of road users travelling from different directions share the same space, leading to numerous spatial and temporal conflicts.

Pedestrian safety requires special concern at intersections. With dramatic increase of urban traffic flow, turning vehicles pose potential threat to pedestrian safety with frequent interactions at crosswalk. Specifically, turning vehicles have to filter through conflicting pedestrian flow at crosswalk during permitted signal phase as implemented in China and U.S. Under the mixed impact of surrounding environment, crosswalk geometry, signal operation and pedestrians moving in different directions, turning vehicles might take risky behavior by not yielding to pedestrians or passing through small gaps in pedestrian flow. According to the accident statistics from The Ministry of Public Security of China (2011), pedestrians account for about 30\% of traffic accident fatalities in China. The National Highway Traffic Safety Administration Report (2016) indicated that about 15\% of the fatalities in traffic accidents in the U.S. are pedestrians. Evidently, Pedestrian safety has become a major concern worldwide.

Numerous factors may influence vehicle-pedestrian conflict at intersections, such as geometric layout, control strategy, behavioral characteristics of vehicles and pedestrians, etc. It is worth mentioning that the geometric layouts and control strategies implemented in practice have both pros and cons in terms of efficiency and reliability. So far, the reactive strategies for the purpose of safety assessment have been primarily based on identifying sites with high crash rates (Highway Safety Manual (HSM, 2010). However, such approach depends on the number of crash records available and the analysis results may become invalid due to changes of intersection geometry, traffic flow and operational conditions. On the other hand, traffic conflict technique (TCT), as another widely used approach, enables a preventive strategy development. Surrogate safety measures (SSMs) serve as near-crash indicators to measure spatial and temporal proximity of road users (Chen et al., 2017b). However, to date there have been still limited applications of SSM on pedestrian-vehicle conflict assessment (Tarko et al., 2009).

Compared to labour-intensive field observation, simulation provides a flexible and promising approach for traffic flow analysis. The adoption of traffic simulation for safety assessment has been investigated

[^0]and implemented in practice (Yong et al., 2014). However, it has been argued that existing simulation models, e.g., Vissim, Paramics and Aimsun, are mainly developed for the purpose of operational performance evaluation (Essa and Sayed, 2015a). Less consideration has been given to the essential behavior characteristics, e.g., stochastic path and speed related to intersection geometry and operational strategies. It remains a controversial issue whether simulation models can reflect the realistic road users' behavior especially when unsafe interactions and near misses exist. Such deficiencies may prevent the simulation models from achieving a reliable safety evaluation. Recently, several studies have attempted to reproduce the stochastic and interactive features of vehicles and pedestrians (Dang et al., 2012; Zeng et al., 2014; Lu et al., 2016; Zeng et al., 2017), which offer a basis for vehicle-pedestrian assessment. This study, through integrating various behavior models in one platform, will help verify how the simulation as an innovative approach can be utilized for vehicle-pedestrian conflict assessment at intersections prior to implementation. It allows practitioners to evaluate and diagnose the geometric layouts and operational strategies in terms of safety performance.

The remainder is organized as follows. Based on a thorough literature review, a discussion on the requirements of a reliable simulation model for safety assessment is presented. The previously developed key behavioral models are summarized in the case of vehicle-pedestrian conflict. Then, the details of data acquisition for model calibration and validation are provided, and SSMs are first empirically analyzed based on field data. Next, a case study is performed by incorporating the developed behavioral models in an integrated fashion. Simulation validation is conducted by referring to the observed SSMs and a sensitivity analysis conducted to compare the performance of compact layout intersections with wider-sized ones. Last, the paper ends up with conclusions and future work.

## 2. Literature review

Commonly, the safety of traffic facilities can be assessed by the number of crashes, crash types and crash severity. Previous studies (Gettman and Head, 2003; Bauer and Harwood, 2003; El-Basyouny and Sayed, 2009; Highway Safety Manual (HSM, 2010) have focused on the establishment of safety performance functions in relation to historical crash data. Such approach is essentially data driven. In order to obtain statistically significant results, large amounts of data accumulated over a long period of time, e.g., several years, are usually required.

In comparison to historical crash-based methods, TCT have been adopted as another prevalent approach for safety assessment. SSMs serve as near-crash indicators to measure the severity and frequency of traffic conflict events. Numerous SSMs have been suggested as shown in Allen at el. (1978), Gettman and Head (2003) and HSM (2010). In general, a SSM is supposed to satisfy two conditions in order to be helpful for safety prevention (Tarko et al., 2009): 1) an observable noncrash event that is substantially related in a predictable way to crashes, and 2) a practical approach for transforming the non-crash event to a corresponding crash frequency and/or severity. The most commonly used SSMs for pedestrian-conflict assessment are Time to Collision (TTC) (Hayward, 1968), Post-Encroachment Time (PET) (Cooper, 1984); Time to Zebra (TTZ) (Varhelyi, 1996), Deceleration-to-Safety Time (DST) (Hupfer, 1997), and Gap Time (GT) (Archer, 2004).

TCT can be applied via both field observation and traffic simulation. Gettman and Head (2003) pointed out the drawbacks of TCT from observational data. The main limitation is that field surveys are costly to conduct and suffer from inter- and intra-observer variability for the repeatability and consistency of results (Ismail et al., 2009). On the other hand, traffic simulation is supposed to be able to overcome the inadequacy of empirical crash and conflict analysis (Dang et al., 2012). Previously, microscopic simulations, e.g., Vissim, have been extensively used by traffic engineers to estimate the operational performance of road facilities, e.g., capacity, delay and travel time. Recently, there has been a growing interest to apply microscopic simulation to safety assessment of traffic systems (Yong et al., 2014). Gettman and Head (2003) first developed an innovative approach called Surrogate Safety Assessment Model (SSAM), and investigated the potential of extracting SSMs from existing microscopic simulation models. The inputs to SSAM are vehicle trajectories generated by simulation and the outputs are the type, number, severity and locations of simulated conflicts. Gettman et al. (2008) further conducted the validity work of SSAM through establishing the relationship between simulated conflicts and crashes at sites.

However, one of the major controversial issues confronting the simulation models for safety assessment is whether they can reflect the realistic road users' behavior especially when unsafe interactions and near misses exist. Most of the simulation models are based on simplified accident-free sub-models such as car following, lane changing and gap acceptance, etc. A vehicle is commonly assumed a point moving along the lane centerline without considering its size and dimension. A minimum spacing between vehicles is usually set in car-following models by Vissim (2018); Paramics (2002) and Aimsum (2007). For vehicle-pedestrian conflict, priority rule is set for pedestrians and vehicles all to yield to pedestrians when conflicts exist. It is apparently too idealistic to reflect the complicated interactions between vehicles and pedestrians. Based on a comprehensive comparison and analysis, Archer (2004) and Lord and Mannering (2010) concluded that existing simulation models fail to reproduce the stochastic speeds and trajectories of vehicles inside intersections in addition to yield decisions to pedestrians. Thus, applying these tools to safety assessment is questionable or even irrational.

To address these problems, several studies aimed to more accurately reproduce road users' behavior by calibrating the existing simulation models. Archer and Young (2010a, b) highlighted the need to relax the restrictions in car-following and lane-changing models in Vissim, e.g., constant critical gap assumption, in order to accurately represent safety critical aspects of vehicle behavior. Cunto and Saccomanno (2008) developed a framework to calibrate and validate vehicle safety simulation indices at signalized intersections in Vissim. Crash potential index, number of vehicles in conflict and total conflict duration per vehicle were analyzed by resorting to both simulated and observed data. Duong et al. (2010) presented a multi-criteria procedure to calibrate simulation model parameters for safety performance evaluation. By constructing a regional road network in a microscopic model by Paramics, Dijkstra et al. (2010) examined the significant statistical relationship between detected conflicts at junctions in simulation and recorded crashes at the sites. Huang et al. (2013) compared the observed and simulated conflicts through model calibration in Vissim and threshold adjustment for conflict definition in SSAM. In view of more complex behavior of road users in practice than in simplified simulation environment, Essa and Sayed (2015a, b) investigated the spatial distribution of simulated and observed conflicts and found significant difference between. Despite increased correlation achieved after proper validation, the traffic conflict mechanism has not been well captured by the simulation model. This indicates that further study should be conducted of simulated conflicts beyond what can be expected from exposure.

On the other hand, a number of studies conducted safety assessment by developing new simulation models. Chai and Wong (2014) developed a cellular automaton (CA) model to represent vehicular interactions at signalized intersections in Singapore. The occurrence of conflicts was evaluated under different traffic volumes and right-turn movement control strategies. To compare the proposed countermeasures for dilemma zone at signalized intersections, Wu et al. (2018) presents a CA simulation study to evaluate the performance of the warning system PMAIC. Lu et al. (2016) further developed a CA model for vehicle-pedestrian interaction analysis at unsignalized mid-block crosswalks. The development of CA models has enhanced the flexibility of modeling road traffic to a certain extent. However, the above studies
focused on relatively simple environments, and the safety assessment in more complex environments, e.g., turning vehicle versus pedestrian conflict at signalized intersections, require further investigation. For that, a generalized simulation tool is needed.

To sum up, most of the safety assessment studies tend to resort to existing simulation models, which were mainly developed for operational performance evaluation of road facilities. To demonstrate the validity of simulation approach, these studies have focused on examining the correlation between the simulated and observed vehicle-tovehicle conflicts or crashes. Studies of safety assessment involving vehicle-pedestrian conflict are rare. However, desirable correlation only indicates similarity in the exposure (represented by traffic volumes and vehicle interactions) but not similarity in the traffic behavior (Essa and Sayed, 2015b). The key for simulation to capture conflict mechanism is to reproduce more realistic behaviors than those used for traffic operations analysis. As an extension of our continuous work on developing behavior models for safety assessment (Zeng et al., 2014, 2017), this study aimed to incorporate previously developed pedestrian and vehicle behavior models into simulation in an integrated fashion. The conflict of interest for safety assessment is right-turning vehicle-pedestrian conflict at crosswalks of intersections. A thorough calibration and validation of the developed simulation model will be conducted.

## 3. Simulation framework

In order to conduct a reliable safety assessment at intersections, numerous behavior models are supposed to be incorporated in one simulation platform to reasonably characterize the movements of vehicles and pedestrians. Fig. 1 shows the integration of key behavioral models for traffic simulation. To represent the vehicle turning movement, geometric features and layouts of intersections are accounted for when building path and speed models. In the process of making rightturn, vehicles may decide whether to go or yield when encountering pedestrians at crosswalks. Thus, a gap acceptance model is further developed. For pedestrian behavior, two levels are related, i.e., tactical and operational levels. Pedestrians are assumed to plan a path initially at the tactical level and then adjust speeds and directions dynamically according to instantaneous conflicts with surrounding pedestrians and vehicles at the operational level. The vehicle-pedestrian interaction is updated every $\Delta t$ interval by the integrated simulation model. By resorting to TCT the safety analysis is conducted in simulation. Here a traffic conflict can be defined as a scenario in which multiple vehicles or pedestrians would collide if they keep on approaching each other in space and time without changing their speeds and/or directions. Accordingly, the safety performance can be measured by the frequency and severity of the conflicts, for which appropriate SSMs are employed. Note that after empirical modeling and analysis, simulation will be applied to analyze the vehicle-pedestrian conflict under various geometric layouts and operational conditions.

## 4. Model development

### 4.1. Vehicle maneuver model

In essence, vehicles trajectories inside an intersection can be represented by the position of the vehicle over time. Mathematically, both path and speed profile are related to construct the series of vehicle coordinates in the two-dimensional space. Thus, the required models for characterizing turning vehicle maneuvers consist of path, speed profile and gap acceptance, as illustrated in Fig. 1.

### 4.1.1. Path model

As shown in Fig. 2, vehicle path models can be developed by approximating the observed individual paths as a sequence of straight lines, circular curves, and clothoid curves (suggested by Alhajyaseen et al. (2013a)). The model parameters are empirically estimated by referring to intersection angle, corner radius, vehicle entering speed and vehicle type, etc. Mathematically, the curvatures of a straight line and a circular curve are zero and a constant, respectively. To connect and transition the turning path between straight and circular segments, Euler spirals, as also referred to as clothoids, are adopted in road alignment. The curvature of an Euler spiral changes linearly with its curve length and can be represented as follows:

$$
R_{S} L_{S}=A^{2},
$$

where $R_{S}$ is the radius of the spiral curve at the end of the circular curve, $L_{S}$ is the length of spiral curve, measured along the curve from its initial position, and A is the Euler spiral parameter that are modeled as a regression function of intersection geometry.

### 4.1.2. Speed profile model

To characterize the speed profiles of turning vehicles around the corner of the intersection, the model developed by Wolfermann et al. (2011) is applied. As illustrated in Fig. 3, an inflow profile and an outflow profile are constructed separately for a certain vehicle. The whole speed profile is supposed to fit well the real speed data as well as reflect the practical deceleration and acceleration behavior as a derivative of speed. Note that the division between the inflow and the outflow profiles is dependent on the moment when the minimum speed is achieved along the turning path. The deceleration and acceleration rates by two profiles are assumed to follow an approximately parabolic shape. Thus, the speed profile is formulated as a third-degree polynomial:

$$
v(t)=c_{1} t^{3}+c_{2} t^{2}+c_{3} t+c_{4}
$$

where $v(t)$ denotes the speed at time $t$, and $c_{1}, c_{2}, c_{3}$, and $c_{4}$ are the parameters to be estimated.

### 4.1.3. Gap acceptance model

When pedestrians are present at the crosswalk, the turning vehicle will anticipate when it will enter the crosswalk at the current speed profile by examining the available lags/gaps among pedestrian flow (Alhajyaseen et al., 2013b). The decision of whether passing through or yielding the right of way to pedestrians will be made. Such a dynamic process of anticipation and decision is iterated along the turning path. Thus, the behavior of lag/gap acceptance is modeled. A lag refers to the time that a single road user takes to arrive at the conflict point. A gap refers to the time interval between two successive road users, during which the second one arrives at the conflict area after the first one have cleared. In practice, the characteristics of available lags/gaps are largely dependent on traffic demand and dynamics, and the acceptance or rejection of encountered lags/gaps by vehicles are stochastic. Cumulative Weibull distribution, as a versatile distribution, is adopted to generate the gap/lag acceptance probabilities. Depending on the values of the scale and shape parameters, it enables to reflect the characteristics of a variety of distributions, e.g., normal and exponential. Its function is provided in Eq. (3).

$$
P(x)=1-e^{-\left(\frac{x}{\alpha}\right)^{\beta}},
$$

where $P(x)$ denotes the acceptance probability of gap/lag $x$, and $\alpha$ and $\beta$ are the distribution parameters to be estimated.

### 4.2. Pedestrian behavior model

The pedestrian behavior models were developed by following a hierarchical scheme, i.e., tactical and operational (Zeng et al., 2017). At the tactical level, pedestrians choose intermediate destinations and desired moving directions. At the operational level, pedestrians adjust speeds and directions dynamically by interacting with traffic light, conflicting vehicles and pedestrians, and crosswalk boundaries. The basic models to represent pedestrian behavior at the crosswalk include

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-04.jpg?height=1438&width=1677&top_left_y=194&top_left_x=194)
Fig. 1. Simulation framework.

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-04.jpg?height=618&width=672&top_left_y=1727&top_left_x=233)
Fig. 2. Turning path model.

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-04.jpg?height=519&width=840&top_left_y=1727&top_left_x=1081)
Fig. 3. Speed profiles.

a desired direction model and a modified social force model. They are briefly summarized in the following subsections.

### 4.2.1. Desired direction model

The selection of a desired direction for a pedestrian to pass the crosswalk is analogous to route choice from origin to destination in the

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-05.jpg?height=868&width=842&top_left_y=194&top_left_x=146)
Fig. 4. Pedestrian interactions with other agents.

network. In general, the pedestrian will select a shortest route to move to his or her destination. Along the desired route, the walking direction changes dynamically with the time varying density of surrounding pedestrians and turning vehicles at the crosswalk. When a deviation occurs for the current and desired directions, a driving force will be generated to facilitate restoring the desired moving direction within a certain relaxation time, as expressed as

$$
\begin{aligned}
& \overrightarrow{\boldsymbol{F}}_{d}=\frac{1}{\tau_{\alpha}}\left(v_{\alpha}^{d} \overrightarrow{\boldsymbol{e}}_{\alpha}-\overrightarrow{\boldsymbol{v}}_{\alpha}\right) \\
& \overrightarrow{\boldsymbol{e}}_{\alpha}=\frac{\overrightarrow{\boldsymbol{P}_{e}}-\overrightarrow{\boldsymbol{P}}_{\alpha}}{\left\|\overrightarrow{\boldsymbol{P}}_{e}-\overrightarrow{\boldsymbol{P}}_{\alpha}\right\|}
\end{aligned}
$$

where $\overrightarrow{\boldsymbol{F}}_{d}$ denotes the driving force, $\overrightarrow{\boldsymbol{v}}_{\alpha}$ represents the current speed vector of pedestrian $\alpha, v_{\alpha}^{d}$ represents the desired speed of pedestrian $\alpha$, $\overrightarrow{\boldsymbol{e}}_{\alpha}$ represents the desired speed vector, $\tau_{\alpha}$ is the relaxation time, $\overrightarrow{\boldsymbol{P}}_{\alpha}$ represents the current position vector, and $\overrightarrow{\boldsymbol{P}}_{e}$ represents the position of the next point along the desired route.

### 4.2.2. Modified social force model

The social force model at the operational level simulates the microscopic motion of pedestrians when interacting with other road users (Zeng et al., 2014, 2017). As illustrated in Fig. 4, in the process of passing the crosswalk, the subject pedestrian may interact with other pedestrians, conflicting vehicles, crosswalk boundary and traffic light. To be specific, the surrounding pedestrians include both leading and opposing pedestrians.

In addition to a driving force in the desired walking direction and an attractive force from leading pedestrians, a repulsive force will be generated for the subject pedestrian when confronted with opposing pedestrians or conflicting turning vehicles. Considering that certain pedestrians may move outside the crosswalk due to potential conflicts, a repulsive or attractive force generated by the crosswalk boundary is also formulated. Furthermore, the risk taking behavior of pedestrian red light crossing is accounted for in the modeling. In practice, a small subset of pedestrians may cross the road even after the onset of red light. Such a traffic light violation behavior is formulated as a binary discrete choice model. One can refer to Zeng et al. $(2014,2017)$ for detail. Taken together, the resultant force $\left(\overrightarrow{\boldsymbol{F}}\left(t_{k}\right)\right)$ can be represented as

$$
\overrightarrow{\boldsymbol{F}}\left(t_{k}\right)=\overrightarrow{\boldsymbol{F}}_{d}\left(t_{k}\right)+\overrightarrow{\boldsymbol{F}}_{t r}\left(t_{k}\right)+\overrightarrow{\boldsymbol{F}}_{\alpha \beta}^{r}\left(t_{k}\right)+\overrightarrow{\boldsymbol{F}}_{V}\left(t_{k}\right)+\overrightarrow{\boldsymbol{F}}_{b}\left(t_{k}\right)+\overrightarrow{\boldsymbol{F}}_{\varepsilon}
$$

where $\overrightarrow{\boldsymbol{F}}_{d}\left(t_{k}\right)$ is the driving force in the desired walking direction; $\overrightarrow{\boldsymbol{F}}_{t r}\left(t_{k}\right)$ is the attractive force generated by leading pedestrians; $\overrightarrow{\boldsymbol{F}}_{\alpha \beta}^{r}\left(t_{k}\right)$ is the repulsive force generated by opposing pedestrians; $\overrightarrow{\boldsymbol{F}}_{V}\left(t_{k}\right)$ is the repulsive force generated by conflicting vehicles; $\overrightarrow{\boldsymbol{F}}_{b}\left(t_{k}\right)$ is the repulsive or attractive force from the crosswalk boundary (depending on the pedestrian walking inside or outside the crosswalk); $\overrightarrow{\boldsymbol{F}}_{\varepsilon}$ is the term of fluctuation.

Accordingly, the step-wise speed profile is calculated as

$$
\overrightarrow{\boldsymbol{v}}_{\alpha}\left(t_{k}\right)=\overrightarrow{\boldsymbol{v}}_{\alpha}\left(t_{k-1}\right)+\overrightarrow{\boldsymbol{F}}\left(t_{k}\right) \Delta t
$$

where $\overrightarrow{\boldsymbol{v}}_{\alpha}\left(t_{k}\right)$ is the speed vector of pedestrian $\alpha$ at time $t_{k} ; \overrightarrow{\boldsymbol{v}}_{\alpha}\left(t_{k-1}\right)$ is the speed vector at time $t_{k-1} ; \Delta t$ is the simulation time step.

In addition, the time varying positions can be calculated as

$$
\overrightarrow{\boldsymbol{P}}_{\alpha}\left(t_{k}\right)=\overrightarrow{\boldsymbol{P}}_{\alpha}\left(t_{k-1}\right)+\overrightarrow{\boldsymbol{v}}_{\alpha}\left(t_{k}\right) \Delta t+\frac{1}{2} \overrightarrow{\boldsymbol{F}}\left(t_{k}\right)(\Delta t)^{2}
$$

where $\overrightarrow{\boldsymbol{P}}_{\alpha}\left(t_{k}\right)$ is the subject pedestrian's ( $\alpha$ ) position at time $t_{k} ; \overrightarrow{\boldsymbol{P}}_{\alpha}\left(t_{k-1}\right)$ is the corresponding position at time $t_{k-1}$.

### 4.3. SSM-based conflict risk estimation

Appropriate SSMs need to be selected for vehicle-pedestrian conflict risk estimation. According to Allen et al. (1978), Gettman and Head (2003) and Gettman et al. (2008), PET was suggested to be the most common index to examine crossing conflict considering the ease of measurement, consistency over time, and relation to other measures. By comparison, TTC, as another commonly used SSM, requires real-time estimation of the time remaining to the conflict point. It is difficult to obtain precisely in practice, and thus not readily applicable to vehiclepedestrian conflict analysis. On the other hand, in the context of vehicle-pedestrian conflict, PET is defined as the time difference between an encroaching pedestrian leaving the potential collision point and a conflicting vehicle reaching the point, or vice versa. To measure PET in practice, only their passing times at conflict point are necessary. As illustrated in Fig. 5, the trajectories of a crossing pedestrian and a turning vehicle are represented by curve A and curve B, respectively. PET can be calculated as

$$
\mathrm{PET}=t_{4}-t_{3}
$$

where $t_{3}$ is the encroachment end time when the conflicting pedestrian leaves the encroachment point, and $t_{4}$ is the actual arrival time of a turning vehicle at the conflict point.

One notable property of PET over other SSMs is that a threshold

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-05.jpg?height=573&width=842&top_left_y=1897&top_left_x=1079)
Fig. 5. PET of vehicle-pedestrian conflict represented by a time-space diagram. (a) Zhongguancun East Road - Zhichun Road Intersection. (b) Huayuan Road -Beitucheng Road Intersection.

value of zero facilitates the distinction between crash occurrences and crash-free cases. Evidently, a shorter PET indicates a larger risk of vehicle-pedestrian collisions. In practice, Songchitruksa and Tarko (2006) demonstrated the usefulness of the number of short PETs in explaining the variability of crash counts and concluded that the safety operational levels at survey sites can be discriminated in terms of the frequency of short PETs.

In addition, vehicle passing speeds or speed distributions at conflict point are good surrogate indices for safety assessment of turning vehicle versus pedestrian conflict. Westra and Rotherngatter (1993) analyzed the vehicle-pedestrian conflict at intersection crosswalks in four European countries, and concluded that if the passing speeds of vehicles to crosswalks are higher, the probability of conflicts is greater. Speed can also be considered as an indicator of conflict severity. Higher speed at conflict points may contribute to higher conflict severity. It can be measured as the vehicle speed at instant $\mathrm{t}_{4}$, as shown in Fig. 5.

Taken together, PET and vehicle passing speed at conflict point are adopted as SSMs to represent the probability of collision or how close a conflict is to a collision. Both indicators are assumed to carry additional safety information that is unexplained by the other. Their effectiveness to characterize vehicle-pedestrian conflict risk under different geometric and operational conditions will be demonstrated.

## 5. Data acquisition

### 5.1. Study site

Two urban intersections in Beijing, China, namely Zhongguancun East Road - Zhichun Road Intersection and Huayuan Road - Beitucheng Road Intersection, were selected for investigation. Both intersections are on a major arterial to downtown area and characterized by high pedestrian and vehicle demand. Fixed signal control plans are implemented at the study sites. Zhongguancun East Road - Zhichun Road Intersection has four signal phases and a cycle length of 240 s, and Huayuan Road - Beitucheng Road Intersection has three phases and a cycle length of 120 s, as illustrated in Fig. 6. The yellow time and all-red time are 3 s and 1 s, respectively, at all the approaches. Taking Huayuan Road - Beitucheng Road Intersection as an example, vehicle-pedestrian conflict exists at northbound and southbound approaches due to shared traffic signal phases. The north-south crosswalks have a length of 35 m and a width of 5.5 m. The pedestrian green phase for the north-south directions is 45 s. The different geometry characteristics and traffic demands of the study sites are shown in Table 1.

### 5.2. Data collection and extraction

Field experiments were conducted by UAV from 12AM to 1 P M on

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-06.jpg?height=581&width=1516&top_left_y=1957&top_left_x=276)
Fig. 6. Signal phase settings at study sites.

Table 1
Characteristics of survey sites.
| Intersection | Approach | Corner radius $R_{c}(\mathrm{~m})$ | Intersection angle ( ${ }^{\circ}$ ) | Number of exit lanes | Crosswalk setback distance (m) | Number of pedestrians (ped/h) | Number of right-turning vehicles (veh/h) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Zhongguancun East Road Zhichun Road | East | 16 | 105 | 4 | 6.5 | 321 | 280 |
|  | West | 19 | 75 | 5 | 7 | 586 | 377 |
|  | North | 17 | 95 | 5 | 8 | 256 | 502 |
|  | South | 15 | 85 | 5 | 8 | 267 | 521 |
| Huayuan Road - Beitucheng Road | East | 19 | 92 | 3 | 7 | 235 | 204 |
|  | West | 17 | 88 | 3 | 7 | 431 | 268 |
|  | North | 18 | 90 | 2 | 8 | 179 | 397 |
|  | South | 17 | 90 | 2 | 8 | 198 | 348 |


![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-07.jpg?height=504&width=1272&top_left_y=672&top_left_x=398)
Fig. 7. Vehicle and pedestrian detection and tracking.

## 6. Model calibration

6.1. Calibration of vehicle maneuver model
6.1.1. Calibration of the path model

As illustrated in Fig. 2, a combination of straight lines, Euler spirals and circular curves is used to represent the path of right-turning vehicle. The turning vehicle enters the intersection by following a straight line in parallel to the boundary line of the lane. Inside the intersection, the path proceeds with an entering Euler spiral, a circular curve and an exit Euler spiral. Both entering and exiting Euler spirals have linear curvatures with gradients of $1 / A_{1}^{2}$ and $1 / A_{2}^{2}$, respectively. The circular curve has a constant curvature of $1 / R_{\text {min }}^{2}$. Last, the vehicle exits the intersection by following another straight line in the exit approach. Accordingly, five parameters need to be determined for constructing a turning path, i.e., the starting point of entering Euler spiral, $A_{1}, R_{\text {min }}, A_{2}$,

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-07.jpg?height=954&width=1679&top_left_y=1587&top_left_x=194)
Fig. 8. Comparison between observed and estimated paths.

Table 2
Estimated parameters of Euler spiral and circular curve.
| Explanatory variables | $A_{1}$ | $A_{2}$ | $R_{\text {min }}$ |
| :--- | :--- | :--- | :--- |
| Corner radius $R_{c}$ (m) | 0.214 | 0.282 | 0.352 |
| The angle between entering and exit approaches $\theta\left({ }^{\circ}\right)$ | 0.390 | 0.181 | 0.142 |
| Heavy vehicle dummy (heavy vehicle: 1, passenger car: 0) | 2.22 | 2.51 | -0.021 |
| Lateral distance from shoulder to center of exit lane (m) | 0.392 | 1.097 | 0.878 |
| Distance between the IP point and the hard nose in entering approach $D_{H N-I N}(\mathrm{~m})$ | 0.195 | 0.157 | 0.0122 |
| Distance between the IP point and the hard nose in exit approach $D_{\text {HN_out }}(\mathrm{m})$ | 0.210 | 0.261 | 0.0115 |
| Approaching speed $V_{i n}(\mathrm{~km} / \mathrm{h})$ | 0.0842 | 0.0924 | 0.0882 |
| Minimum speed $V_{\text {min }}(\mathrm{km} / \mathrm{h})$ | 0.292 | 0.311 | 0.0352 |
| Constant | -7.52 | 3.61 | 1.86 |
| Sample size | 2027 (70\% of total samples) |  |  |
| Adjusted $\mathrm{R}^{2}$ | 0.689 | 0.701 | 0.649 |


and the ending point of exiting Euler spiral. They were empirically estimated for each observed vehicle trajectory by minimizing the estimation errors. Furthermore, these parameters were modeled by accounting for the impact of geometric features (e.g., intersection angle and corner radius) and operational conditions (e.g., vehicle approaching speed and minimum speed around the corner). Maximum likelihood estimation is used to derive the estimation results, as provided in Table 2. Besides, the differences of observed and estimated path profiles were examined by comparing the distributions of distance to the cross point at three cross sections inside the intersection, as illustrated in Fig. 8. It was found that the estimated distance distributions at three cross sections were not significantly different from the observed ones in the $t$-test at the 95\% confidence level.

### 6.1.2. Calibration of the speed profile model

As aforementioned, an inflow profile and an outflow profile are constructed separately for a turning vehicle, with the boundary corresponding to the moment when the minimum speed is achieved. By referring to Eq. (2), there will be altogether eight coefficients to be estimated, i.e., $c_{1, \text { in }}-c_{4, \text { in }}$ and $c_{1, \text { out }}-c_{4, \text { out }}$. Both entering and exiting speeds are regarded as input variables since they are largely dependent on the desired speed and the link conditions. The accelerations at the beginning and end of turning maneuver are assumed to be zero. The variables $c_{1, \text { in }}$ and $c_{1, \text { out }}$ need to be explicitly provided to construct the inflow and outflow profiles. They are modeled as a gamma distribution. The model parameters are empirically estimated as a linear function of the related factors such as geometric layout (e.g., intersection angle and corner radius) and operational conditions (e.g., entering speed). The estimation results of $c_{1, \text { in }}$ and $c_{1, \text { out }}$ are shown in Table 3. The other parameters ( $c_{2, \text { in }}-c_{4, \text { in }}$ and $c_{2, \text { out }}-c_{4, \text { out }}$ ) can be derived based on the estimation of $c_{1, \text { in }}$ and $c_{1, \text { out }}$ (Wolfermann et al., 2011). Fig. 9 presents the observed and estimated turning vehicle speed profiles. The accuracy was examined by comparing the passing speeds at three cross sections around the

Table 3
Estimation results of $c_{1, \text { in }}$ and. $c_{1, \text { out }}$
| Gamma distribution | Parameters | $c_{1, i n}$ | $c_{1, \text { out }}$ |
| :--- | :--- | :--- | :--- |
| $\alpha$ | Constant | 9.25 | 5.87 |
|  | Entering speed (m/s) | 0.220 | 0.0272 |
|  | Approaching angle (°) | -0.0217 | -0.00871 |
|  | Corner radius (m) | 0.0017 | 0.0024 |
|  | Lateral exit distance (m) | -0.152 | 0.0214 |
|  | Exiting speed (m/s) | 0.231 | -0.262 |
| $\beta$ | Constant | -0.0552 | -0.00228 |
|  | Entering speed (m/s) | -0.00114 | 0.00152 |
|  | Approaching angle (°) | 0.000840 | 0.000152 |
|  | Corner radius (m) | -0.00115 | 0.000210 |
|  | Lateral exit distance (m) | 0.00325 | 0.00122 |
|  | Exiting speed (m/s) | 0.00541 | -0.00385 |
| Sample size | 2027 (70\% of total samples) |  |  |
| Adjusted $\mathrm{R}^{2}$ |  | 0.698 | 0.714 |


corner of the intersection. The $t$-test revealed a non-significant difference between the groups at the 95\% confidence level.

### 6.1.3. Calibration of the gap acceptance model

For turning vehicles, they may react to pedestrians in different crossing directions in a different manner. Thus, before analyzing the laps/gaps in pedestrian flow, near-side and far-side of the crosswalk are defined by referring to turning vehicles. As illustrated in Fig. 10, pedestrians from near-side of the crosswalk stand for those who start crossing near the exit approach of turning vehicles, while pedestrians from far-side stand for those who start crossing near the entering approach on the other side of the crosswalk. In light of the distinction of near-side and far-side pedestrians, lags and gaps can be divided into five types. Note that subject to the physical size of the vehicle, all potential vehicle-pedestrian conflicts occur inside the conflict area along the turning path. When investigating lags or gaps, the time taken by pedestrians to clear the conflict area need to be excluded. For each type of lags or gaps, the acceptance probability was derived at a time interval of 1 s by calculating the number of accepted and rejected gaps/lags based on observation data. The cumulative Weibull distribution, as shown in Eq. (3), was adopted to fit the observed gap/lag acceptance probabilities. The estimation results of the distribution parameters are provided in Table 4. The goodness of fit in terms of the adjusted Rsquare value reveals that the model can reasonably represent the lag/ gap acceptance behavior of turning vehicles.

### 6.2. Calibration of pedestrian behavior model

For calibrating pedestrian behavior models, since the social force is exerted in a two-dimensional space, a genetic algorithm was used to minimize the errors between observed and simulated pedestrian trajectories. As elaborated in the authors' previous work (Zeng et al., 2017), NSGA-II (Deb et al., 2002) was adopted to derive non-dominated solutions for this multi-objective optimization problem. Considering that pedestrians at the crosswalk move in different directions and at different speeds, the relative errors of both walking distance and angles were set as optimization objectives.

For the scenarios of analysis, five typical ones were summarized based on field observation, as illustrated in Table 5. First, depending on whether the vehicle-pedestrian conflict occurred along the walking trajectories at the crosswalk, the pedestrian dataset can be roughly classified into two groups. For the pedestrians encountering no conflicting vehicles, three cases were defined in view of the relative degree of freedom of walking, i.e., one single pedestrian at the crosswalk, one vs. one pedestrian conflicting in the opposite direction, one vs. multiple pedestrians in the opposite direction. On the other hand, for the pedestrians encountering conflicting vehicles at the crosswalk, two cases are related, i.e., the conflict between one single pedestrian and the turning vehicle, and the conflict between multiple pedestrians and the turning vehicle. For each case, one sampled trajectory was extracted

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-09.jpg?height=1365&width=1688&top_left_y=189&top_left_x=189)
Fig. 9. Comparison of observed and estimated speed profiles at three cross sections.

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-09.jpg?height=777&width=1264&top_left_y=1761&top_left_x=400)
Fig. 10. Assumed types of lags/gaps.

Table 4
Parameters of the lag/gap acceptance probability distributions.
| Gap/lag type | Description | Parameters | Estimate | Adjusted $\mathrm{R}^{2}$ | Sample Size |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Type A | Lags of near-side approaching pedestrians | $\alpha$ | 3.32 | 0.974 | 378 |
|  |  | $\beta$ | 2.49 |  |  |
| Type B | Lags of far-side approaching pedestrians | $\alpha$ | 4.41 | 0.985 | 708 |
|  |  | $\beta$ | 3.21 |  |  |
| Type C | Gaps between two successive near-side approaching pedestrians | $\alpha$ | 5.02 | 0.952 | 349 |
|  |  | $\beta$ | 4.74 |  |  |
| Type D | Gaps between two successive far-side approaching pedestrians | $\alpha$ | 7.39 | 0.962 | 574 |
|  |  | $\beta$ | 4.21 |  |  |
| Type E | Gaps between a near-side approaching pedestrian and a far-side one | $\alpha$ | 7.28 | 0.938 | 463 |
|  |  | $\beta$ | 4.59 |  |  |


Table 5
Estimation accuracy of step-wise paths and speeds in different scenarios.
| Scenarios | No. of pedestrians | MAPE of step-wise path |  | MAPE of step-wise speed |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | D $(x)$ | $\mathrm{D}(\mathrm{y})$ | $\mathrm{V}(x)$ | V(y) |
| ![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-10.jpg?height=54&width=117&top_left_y=959&top_left_x=151) | 255 | 10.22\% | 8.21\% | 11.99\% | 9.15\% |
| ![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-10.jpg?height=54&width=114&top_left_y=1021&top_left_x=151) | 215 | 6.97\% | 6.09\% | 9.09\% | 5.11\% |
| ![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-10.jpg?height=53&width=114&top_left_y=1082&top_left_x=149) | 1026 | 10.78\% | 7.12\% | 12.34\% | 7.24\% |
| ![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-10.jpg?height=76&width=152&top_left_y=1142&top_left_x=151) | 175 | 7.98\% | 4.32\% | 9.17\% | 5.67\% |
| ![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-10.jpg?height=78&width=155&top_left_y=1224&top_left_x=149) | 801 | 9.54\% | 8.08\% | 12.65\% | 5.40\% |


from the observation dataset. The behavior of the sampled pedestrian was simulated by the proposed social force model, while maintaining the raw trajectories of other pedestrians in the case. By comparing the

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-10.jpg?height=508&width=842&top_left_y=715&top_left_x=1079)
Fig. 12. Conflict point distribution in each area.

observed and simulated pedestrian trajectories of interest, the estimation errors of step-wise path and speed in two dimensions were calculated in terms of MAPE (Mean Absolute Percentage Error), as presented in Table 5. The desirable accuracy indicates that the proposed social

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-10.jpg?height=1021&width=1262&top_left_y=1520&top_left_x=405)
Fig. 11. Comparison of observed and simulated conflict points (-3 s < PET < 3 s).

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-11.jpg?height=500&width=844&top_left_y=189&top_left_x=144)
Fig. 13. Observed vs. simulated PETs.

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-11.jpg?height=547&width=844&top_left_y=779&top_left_x=144)
Fig. 14. Observed vs. simulated vehicle speeds at conflict point.

force model enables to characterize the pedestrian motion at the crosswalk. For the detailed description of calibration procedures and the obtained model parameters, one can refer to Zeng et al. (2017).

## 7. Simulation study

The following section focuses on the implementation of the simulation model for safety assessment after the integration of various submodels. The simulation platform is implemented in C\# programming language, which integrates four main sub-systems of the platform, i.e., main graphical user interface, simulation calculation Engine, encoding/ decoding engine and data record engine. First, simulation validation was conducted at the site. The conflict of interest is between rightturning vehicles from the south approach and pedestrian flow at the

Table 6
Means and standard deviations of PETs for 90-degree cases.
| $\mathrm{D}_{\mathrm{cw}}$ | R |  |  |
| :--- | :--- | :--- | :--- |
|  | 5 m | 10 m | 15 m |
| $5 m$ | 3.07(1.33) | 3.24(1.25) | 3.11(1.32) |
| 10 m | 3.25(1.24) | 3.34(1.19) | 3.18(1.33) |
| $15 m$ | 3.15(1.23) | 3.33(1.21) | 3.06(1.21) |


Table 7
Means and standard deviations of PETs for 120-degree cases.
| $\mathrm{D}_{\mathrm{cw}}$ | R |  |  |
| :--- | :--- | :--- | :--- |
|  | 5 m | 10 m | 15 m |
| $5 m$ | 3.04(1.36) | 3.06(1.29) | 3.08(1.26) |
| 10 m | 3.03(1.34) | 2.97(1.36) | 3.16(1.35) |
| $15 m$ | 3.04(1.30) | 3.25(1.21) | 3.03(1.33) |


east crosswalk, as illustrated in Fig. 7. The purpose of validation is to examine whether the simulation model is able to reasonably represent vehicle-pedestrian conflicts at signalized intersections. SSMs will be investigated and the conflicts identified by simulation will be compared to empirically observed ones. Then, a sensitivity analysis is carried out to assess the ability of the developed simulation for safety assessment with various geometric characteristics.

### 7.1. SSM validation

To validate the distribution of the conflict events with absolute PET values of less than 3 s, a number of areas both inside and outside the crosswalk were defined, as illustrated in Fig. 11. The areas are surrounded horizontally by the edge and middle cross-section of the crosswalk as well as the boundary lines of vehicle lanes. Considering the fact that some pedestrians walk outside the crosswalk, the areas were divided vertically by referring to the edge of the exit approach. In total, nine conflict areas are divided by referring to A, B, C horizontally and I, II and III vertically.

Fig. 12 shows the observed and simulated conflict points in each area. It can be seen that overall the distribution of simulated conflict points is in line with observations. Worth mentioning is that the conflict points in the areas of BI and BIII appear a certain difference, indicating the pedestrian behavior outside the crosswalk needs further attention. When exerting social force for pedestrian behavior analysis in this study, a repulsive force was initially assumed to keep pedestrians from the crosswalk boundary (Zeng et al., 2014, 2017). However, once the pedestrian density keeps increasing to a certain extent or vehicles pose

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-11.jpg?height=551&width=1270&top_left_y=1989&top_left_x=398)
Fig. 15. Layout of assumed intersections for analysis.

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-12.jpg?height=1092&width=1679&top_left_y=189&top_left_x=196)
Fig. 16. Comparison of PET distributions for each scenario.

Table 8
Means and standard deviations of passing speeds at conflict point for 90-degree cases.
| $\mathrm{D}_{\mathrm{cw}}$ | R |  |  |
| :--- | :--- | :--- | :--- |
|  | 5 m | 10 m | 15 m |
| $5 m$ | 3.30(1.28) | 3.75(1.40) | 4.03(1.53) |
| 10 m | 3.42(1.39) | 4.04(1.18) | 4.34(1.54) |
| $15 m$ | 3.93(1.83) | 4.40(1.63) | 4.47(1.68) |


Table 9
Means and standard deviations of passing speeds at conflict point for 120-degree cases.
| $\mathrm{D}_{\mathrm{cw}}$ | R |  |  |
| :--- | :--- | :--- | :--- |
|  | 5 m | 10 m | 15 m |
| $5 m$ | 3.77(1.36) | 4.23(1.56) | 4.67(1.18) |
| 10 m | 4.07(1.98) | 4.32(1.39) | 4.68(1.57) |
| $15 m$ | 4.48(2.26) | 4.88(1.92) | 4.94(1.74) |


a potential threat, some pedestrians may move outside the crosswalk to avoid serious pedestrian-pedestrian or pedestrian-vehicle conflicts. Once the conflicts appear less severe, most of these pedestrians may pass the boundary and move back to the crosswalk. In future work, further analysis and modeling of pedestrian behavior outside the crosswalk are supposed to be conducted and incorporated into the simulation.

Fig. 13 shows a comparison of observed and simulated PETs. The paired $t$-test indicates that there is no significant difference between at the 95\% confidence level. Thus, PET, as one representative SSM, is demonstrated to be able to assess pedestrian-vehicle conflict at crosswalks. However, it should be noted that there are fewer PETs with smaller absolute values in the simulation. This indicates that the gap acceptance model based on limited data samples needs to be further adjusted.

Regarding conflict events with absolute PET values of less than 3 s, Fig. 14 compares the observed and simulated vehicle passing speeds at conflict points. No significant difference is revealed by the $t$-test at the 95\% confidence level. Thus, vehicle passing speeds at conflict points as another SSM enables to estimate the vehicle-pedestrian conflict level at signalized crosswalks.

### 7.2. Sensitivity analysis

As a demonstration of this study, the established simulation model was used to examine the influence of several geometric factors on the conflict between turning vehicles and pedestrians, such as intersection angle, stop-line position, crosswalk position, and corner radius. The SSMs that were extracted from the simulation were then analyzed. The following steps are generally related: 1) implementation of various intersection layouts and signal timings in a simulation, 2) running a simulation and collecting road users' trajectories and conflict event data, and 3) comparing the results obtained for various scenarios.

### 7.2.1. Hypothesis

Assessing vehicle-pedestrian conflicts at intersection crosswalks requires examination of corner radii and crosswalk positions. With the increasing dimensions of corner radii and crosswalk setback distances, the conflict severity increases, whereas the mobility of vehicles and pedestrians decreases because of longer crossing distances and delays.

### 7.2.2. Designing scenarios

Two typical intersections with four-legs, multiple lanes but different intersection angles, i.e., 90 ° and 120°, were assumed in this study, as

![](https://cdn.mathpix.com/cropped/e2dbe92d-8fb9-49bc-8465-69ab775013a3-13.jpg?height=1111&width=1684&top_left_y=187&top_left_x=194)
Fig. 17. Comparison of vehicle passing speed distributions at conflict point for each scenario.

shown Fig. 15. The signal phasing and timing were set to be the same as those of the study site of interest, as shown in Fig. 6.

For each intersection, 9 scenarios with ranging corner radii and crosswalk setback distances were designed. In some scenarios, the corner radius was kept the same while the crosswalk setback distance was varied $\left(D_{c w}=0,5,10,15 \mathrm{~m}\right)$. In other scenarios, the crosswalk setback distance was kept the same while the corner radius was varied $\left(R_{c}=5,10,15 \mathrm{~m}\right)$. Each scenario was designed by using the developed simulation model. The safety performance of the intersection was evaluated by examining the conflicts between turning vehicles from the east approach and bidirectional pedestrian flow at the north crosswalk, as illustrated in Fig. 15. The traffic volume was assumed to be 100 veh/ lane/h and 150 ped/h (50 ped/h from the near-side crosswalk, 100 ped/h from the far-side crosswalk). Each scenario was run for 4 h to collect sufficient data. Then, SSMs were extracted, including PETs and passing speeds of turning vehicles at the conflict points.

### 7.2.3. Results of analysis

Tables 6 and 7 show the statistical results of PET values in the 90degree and 120-degree cases, respectively. The results indicate that when the turning radii and crosswalk setback distances were increased, the mean PET values showed no apparent changing tendency. However, regarding the PET value distributions for each scenario, as seen in Fig. 16, the cumulative curves of PETs for the 120-degree cases shift to the left side toward smaller PET values. This indicates a relatively dangerous situation for conflicting pedestrians when the right-turning angle becomes larger.

Tables 8 and 9 show the statistical results of passing speed values at conflict point in the 90-degree and 120-degree cases, respectively. The results indicate that when turning radii and crosswalk setback distances were increased, the mean values of passing speeds at the conflict point showed an increasing tendency. Fig. 17 shows that the cumulative curves of passing speeds for the 120-degree cases shift to the right side toward higher speed values. This indicates that vehicles run faster or more smoothly with larger turning angles, setback distances and radii.

To sum up, it was demonstrated by simulation that conflict severity generally increases as the setback distance and turning radius increase. Under the same radius and setback distance, 120-degree cases appear to have higher conflict severity. In reality, at intersections with larger scales and turning angles, turning vehicles might have higher speeds and behave less cautiously towards upcoming pedestrians at the crosswalk. Thus, more severe conflicts are expected to occur at largerscale intersections as indicated by the simulation results.

## 8. Conclusions and future work

Frequent vehicle-pedestrian conflicts deserve special attention for safety assessment at intersections. This study helps verify how simulation can be utilized for vehicle-pedestrian conflict assessment at crosswalks. Empirical models have been established to represent the stochastic behavior of right-turning vehicles and pedestrians under different geometric layouts and operational conditions at signalized intersections. For safety assessment, SSMs were collected by simulation based on road user behavior models running in an integrated fashion and employed to reflect the frequency and severity of vehicle-pedestrian conflicts. The calibration and validation results reveal that the established simulation model enables to characterize vehicle and pedestrian behavior as well as their conflict occurrence at intersection crosswalks. Sensitivity analysis results indicate that larger dimensions and turning angles of intersections result in worse safety performance. An analysis of SSM-based conflict indicators (PET and passing speed at conflict point) indicated that a 90-degree angle corresponds to a safer operational performance than a 120-degree angle with similar turning radii and crosswalk setback distances.

In summary, the integration of developed behavior models in simulation presents a promising approach for safety assessment at intersections. First, it enables a better understanding of conflict risks and the impact of geometric characteristics and signal operation on safety performance. Second, without resorting to field observations, simulated conflict events and extracted SSMs can readily support evaluation of the changes of road design and traffic signal control prior to implementation. Accordingly, the effectiveness of different safety countermeasures can be examined. Third, such an integrated simulation approach helps provide insights into how to improve the applicability of existing microsimulation models for evaluating safety performance. Proper calibration may result in an enhanced correlation between field-measured and simulated conflicts (Guo et al., 2019), however, the underlying mechanism of vehicle-pedestrian conflict is directly related to the basic behavior models which serve as the key to reasonably represent the characteristics of spatiotemporal conflict.

To provide more reliable results and broaden the applicability of the proposed simulation model, it is necessary to update some key behavioral models, such as non-free-flow right-turning vehicle path/speed models and pedestrian behavior outside the crosswalk. Other conflict types, such as left-turning vehicles versus opposing through traffic conflict should also be incorporated into the future development of the simulation model. In addition, to develop SSMs integrating both conflict frequency and severity (Alhajyaseen, 2015) and to establish the statistical linkage between SSMs and crash records (Chen et al., 2014) will support a more sophisticated safety assessment.

## Acknowledgements

The authors appreciate the National Natural Science Foundation of China (No. 61873018 and No. 61803100) for support of this study. Special thanks go to Dr. Yongzheng Xu and Mr. Yalong Ma for their efforts in the UAV data analysis.

## References

Aimsum, 2007. Aimsum NG Manual. Transport Simulation Systems, Barcelona, Spain.
Alhajyaseen, W.K., Asano, M., Nakamura, H., Tan, D.M., 2013a. Stochastic approach for modeling the effects of intersection geometry on turning vehicle paths. Transp. Res. Part C Emerg. Technol. 32, 179-192.
Alhajyaseen, W.K., Asano, M., Nakamura, H., 2013b. Left-turn gap acceptance models considering pedestrian movement characteristics. Accid. Anal. Prev. 50, 175-185.
Alhajyaseen, W.K., 2015. The integration of conflict probability and severity for the safety assessment of intersections. Arab. J. Sci. Eng. 40, 421-430.
Allen, B.L., Shin, B.T., Cooper, P.J., 1978. Analysis of traffic conflicts and collisions. Transp. Res. Rec.: J. Transp. Res. Board 667, 67-74.
Archer, J., 2004. Methods for the Assessment and Prediction of Traffic Safety at Urban Intersections and their Application in Micro-simulation Modeling, PhD Thesis. Division of Transport and Logistics, Royal Institute of Technology (KTH), Stockholm, Sweden.
Archer, J., Young, W., 2010a. A traffic micro-simulation approach to estimate safety at unsignalized intersections. The $89{ }^{\text {th }}$ Annual Meeting of the Transportation Research Board.
Archer, J., Young, W., 2010b. Signal treatments to reduce the likelihood of heavy vehicle crashes at intersections: a micro-simulation modeling approach. J. Transp. Eng.(ASCE) 136 (7), 632-639.
Bauer, K.M., Harwood, D.W., 2003. Statistical Models of At-grade Intersection Accidentsaddendum, Publication No.: FHWA-RD-99-094. Federal Highway Administration, U.S.
Chai, C., Wong, Y.D., 2014. Micro-simulation of vehicle conflicts involving right-turn vehicles at signalized intersections based on cellular automata. Accid. Anal. Prev. 63, 94-103.
Chen, P., Nakamura, H., Asano, M., 2014. Application of surrogate safety measures for assessment of pedestrian versus left-turning vehicle conflict at signalized crosswalks. Adv. Transp. Stud. Int. J. 1, 37-50.
Chen, P., Yu, G., Wu, X., Ren, Y., Wang, Y., 2017a. Estimation of red-light running frequency using high-resolution traffic and signal data. Accid. Anal. Prev. 102, 235-247.
Chen, P., Zeng, W., Yu, G., Wang, Y., 2017b. Surrogate safety measures of pedestrianvehicle conflict at intersections using unmanned aerial vehicle videos. J. Adv. Transp., 520215012 pages.
Cooper, J., 1984. Experience with traffic conflicts in Canada with emphasis on post encroachment time techniques. Int. Study Traffic Conflict Tech. 75, 75-96.
Cunto, F., Saccomanno, F., 2008. Calibration and validation of simulated vehicle safety performance at signalized intersections. Accid. Anal. Prev. 40, 1171-1179.
Deb, K., Pratap, A., Agarwal, S., Meyarivan, T., 2002. A fast and elitist multi-objective genetic algorithm: NSGA-II. IEEE Trans. Evol. Comput. 6 (2), 182-197.
Dang, M.T., Alhajyaseen, W.K.M., Asano, M., Nakamura, H., 2012. Development of microscopic traffic simulation model for safety assessment at signalized intersections. Transp. Res. Rec.: J. Transp. Res. Board 2316, 122-131.
Dijkstra, A., Marchesini, P., Bijleveld, F., Kars, V., Drolenga, H., Maarseveen, M., 2010. Do calculated conflicts in microsimulation model predict number of crashes? Transp. Res. Rec.: J. Transp. Res. Board 2147, 105-112.
Duong, D., Saccomanno, F., Hellinga, B., 2010. Calibration of microscopic traffic model for simulating safety performance. The $89{ }^{\text {th }}$ Annual Meeting of the Transportation Research Board.
El-Basyouny, K., Sayed, T., 2009. Collision predication models using multivariate Poissonlognormal regression. Accid. Anal. Prev. 41 (4), 820-828.
Essa, M., Sayed, T., 2015a. Transferability of calibrated microsimulation model parameters for safety assessment using simulated conflicts. Accid. Anal. Prev. 84, 41-53.
Essa, M., Sayed, T., 2015b. Simulated traffic conflicts: Do they accurately represent fieldmeasured conflicts? Transp. Res. Rec.: J. Transp. Res. Board 2514, 48-57.
Gettman, D., Head, L., 2003. Surrogate Safety Measures from Traffic Simulation Models, Publication No.: FHWA-RD-03-050. Federal Highway Administration, U.S.
Gettman, D., Pu, L., Sayed, T., Shelby, S., 2008. Surrogate Safety Assessment Model and Validation, FHWA Report, Publication No.: FHWA-HRT-08-051. Federal Highway Administration, U.S.
Guo, Y., Essa, M., Sayed, T., Haque, M., 2019. A Comparison between simulated and fieldmeasured conflicts for safety assessment of signalized intersection in Australia. Transp. Res. Part C Emerg. Technol. 101, 96-110.
Hayward, J.C., 1968. Near-miss determination through use of a scale of danger. Highway Res. Rec. 384, 24-34.
Highway Safety Manual (HSM), 2010. American Association of State Highway and Transportation Officials. U.S.. first edition. .
Huang, F., Liu, P., Yu, H., Wang, W., 2013. Identifying if VISSIM simulation model and SSAM provide reasonable estimates for field measured traffic conflicts at signalized intersections. Accid. Anal. Prev. 50, 1014-1024.
Hupfer, C., 1997. Deceleration to safety time (DST) - a useful figure to evaluate traffic safety. ICTCT Conference Proceedings of Seminar 3.
Ismail, K., Sayed, T., Sauiner, N., Lim, C., 2009. Automated analysis of pedestrian-vehicle conflicts using video data. Transp. Res. Rec.: J. Transp. Res. Board 2140, 44-54.
Lord, D., Mannering, F., 2010. The statistical analysis of crash-frequency data: a review and assessment of methodological alternatives. Transp. Res. Part A Policy Pract. 44 (5), 291-305.
Lu, L., Ren, G., Wang, W., Chan, C.Y., Wang, J., 2016. A cellular automaton simulation model for pedestrian and vehicle interaction behaviors at unsignalized mid-block crosswalks. Accid. Anal. Prev. 95, 425-437.
Ma, Y., Wu, X., Yu, G., Xu, Y., Wang, Y., 2016. Pedestrian detection and tracking from low-resolution unmanned aerial vehicle thermal imagery. Sensors 16, 446.
Ministry of Public Security of China, 2011. Road Traffic Accident Statistics.
National Highway Traffic Safety Administration, 2016. Traffic Safety Facts: 2015 Motor Vehicle Crashes: Overview. U.S. Department of Transportation, Washington D.C DOT HS 812318.
Ni, Y., Wang, M., Sun, J., Li, K., 2016. Evaluation of pedestrian safety at intersections: a theoretical framework based on pedestrian-vehicle interaction patterns. Accid. Anal. Prev. 96, 118-129.
Paramics, 2002. Paramics systems overview V3. Internal Report.
Songchitruksa, P., Tarko, A.P., 2006. The extreme value theory approach to safety estimation. Accid. Anal. Prev. 38, 811-822.
Tarko, A., Davis, G., Saunier, N., Sayed, T., Washington, S., 2009. Surrogate measures of safety white paper. Subcommittee on Surrogate Measures of Safety and Committee on Safety Data Evaluation and Analysis. Transportation Research Board, Washington D.C.
Vissim, 2018. PTV Vissim 10 User Manual. PTV AG, Karlsruhe, Germany.
Westra, E.J., Rotherngatter, J.A., 1993. Behaviour-conflict-safety Relations for Pedestrians. Traffic Research Centre, University of Groningen, the Netherlands.
Wolfermann, A., Alhajyaseen, W.K.M., Nakamura, H., 2011. Modeling speed profiles of turning vehicles at signalized intersections. The 3rd International Conference on Road Safety and Simulation.
Wu, Y., Abdel-Aty, M., Ding, Y., Jia, B., Shi, Q., Yan, X., 2018. Comparison of proposed countermeasures for dilemma zone at signalized intersections based on cellular automata simulations. Accid. Anal. Prev. 116, 69-78.
Xu, Y., Yu, G., Wang, Y., Wu, X., Ma, Y., 2016. A hybrid vehicle detection method based on viola-jones and HOG + SVM from UAV images. Sensors 16, 1325.
Yong, W., Sobhani, A., Lenne, M.G., Sarvi, M., 2014. Simulation of safety: a review of the state of the art in road safety simulation modeling. Accid. Anal. Prev. 66, 89-103.
Zeng, W., Chen, P., Nakamura, H., Iryo-Asano, M., 2014. Application of social force model to pedestrian behavior analysis at signalized crosswalk. Transp. Res. Part C Emerg. Technol. 40, 143-159.
Zeng, W., Chen, P., Yu, G., Wang, Y., 2017. Specification and calibration of a microscopic model for pedestrian dynamic simulation at signalized intersections: a hybrid approach. Transp. Res. Part C Emerg. Technol. 80, 37-70.


[^0]:    *Corresponding author.
    E-mail addresses: cpeng@buaa.edu.cn (P. Chen), weiliangzeng@gdut.edu.cn (W. Zeng), yugz@buaa.edu.cn (G. Yu).

