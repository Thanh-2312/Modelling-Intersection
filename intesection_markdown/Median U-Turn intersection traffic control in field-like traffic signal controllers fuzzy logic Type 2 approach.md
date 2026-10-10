# Assessing impacts of traffic signal countdown timers on safety and efficiency at signalized intersections 

Vadhul Krishnan Veerakumar ${ }^{\text {(1) }}$, Chris Lee ${ }^{\text {* }}$<br>Department of Civil and Environmental Engineering, University of Windsor, ON N9B 3P4, Canada

ARTICLE INFO

Keywords:
Traffic signal countdown timers
Signalized intersection
Traffic conflicts
Traffic simulation
Car
Truck


#### Abstract

Introduction: Traffic Signal Countdown Timer (TSCT) displays the remaining times of green, yellow, and red intervals at a traffic signal. While TSCT has widely been implemented in various countries, there is a lack of studies that comprehensively assess the effects of TSCT on traffic safety and efficiency using a simulation based on understanding of changes in driver behavior in different signal phases in the presence of TSCT. Methods: This study investigates the impacts of TSCT on traffic safety and efficiency at signalized intersections with high truck volume along the Huron Church Road in Windsor, Ontario, Canada. Driver behavior and traffic flow were simulated using PTV Vissim for the four scenarios - no-timer, Green Signal Countdown Timer (GSCT), Red Signal Countdown Timer (RSCT), and a combination of GSCT and RSCT (GSCT + RSCT). Based on the observational data from previous field studies, changes in driver behaviors in the presence of TSCT were replicated by dynamically adjusting the simulation parameters in different signal phases using Vissim-COM interface. Results: The Crash Potential Index (CPI) decreased by 37\% while the speed of the road network increased by 6\% in the GSCT + RSCT scenario compared to the no-timer scenario. The RSCT reduced the CPI more than the GSCT but did not significantly improve the traffic efficiency. The increase in speed near the intersection during the green phase was observed in the GSCT scenario, whereas smoother deceleration rate of approach vehicles during the red phase was observed in the RSCT scenario. Due to these changes, the average number of vehicles entering the intersection during the green phase in each cycle increased in the GSCT + RSCT scenario. Moreover, the TSCT helped cars avoid rear-end conflicts and increased truck speed. Practical Applications: Both GSCT and RSCT can be implemented to improve traffic safety and efficiency at signalized intersections.


## 1. Introduction

Traffic Signal Countdown Timers (TSCT) indicate the remaining time for green, yellow, and red phases at intersections, aiding drivers in making informed decisions on whether to stop or proceed. TSCT is divided into three categories based on the signal phase they address: Red Signal Countdown Timer (RSCT), Green Signal Countdown Timer (GSCT), and Yellow Signal Countdown Timer (YSCT). Past studies have demonstrated that the TSCT had both positive and negative effects on traffic safety and efficiency through field studies and simulation analyses (Jatoth et al., 2021; Paul et al., 2022; Chiou \& Chang, 2010; Long et al., 2011).

Despite significant global research on the impacts of TSCT on traffic safety and efficiency, there are several limitations. First, the studies that assessed the impacts of TSCT using field data did not explicitly control external effects of all changes in traffic, environmental, and enforcement conditions on driver behavior with and without the presence of TSCT.

Second, although Paul et al. (2022) assessed the impacts of TSCT using traffic simulation models to address this limitation, there is a lack of explanation on how the spatial and temporal variations in driver behavior with the presence of TSCT were simulated. More specifically, the study has not realistically modeled changes in driver reactions to different signal phases (e.g., green and red) in the presence of TSCT. Additionally, the behavioral factors underlying observed changes in traffic flow due to TSCT have not been thoroughly examined in prior research.

Third, there is a lack of studies on the effects of TSCT on conflicts between different types of vehicles such as cars and trucks at signalized intersections unlike freeways. This is mainly because most vehicles are passenger cars at urban streets. However, high volume of trucks also travels at urban streets in the areas closer to freeways. Since trucks require longer deceleration distance and have slower acceleration than

[^0]passenger cars, this difference in behavior increases the conflicts between cars and trucks at a signalized intersection. For instance, heavy vehicles require longer time and distance to stop to avoid a collision with the stopped lead vehicle and their risk of rear-end collision is higher than cars.

Lastly, previous field studies have focused on individual intersections and neglected network-wide impacts of TSCT. Thus, this study addresses these gaps by using a simulation-based approach to predict the driver behavior in the presence of different types of TSCT and evaluate the impacts of TSCT on traffic safety and efficiency at signalized intersections with car-truck mixed traffic.

## 2. Literature review

### 2.1. Impacts of TSCT on collisions

Some studies investigated the impacts of TSCT on collisions using crash records. For instance, Spigolon et al. (2015) found that the number of collisions decreased after installation of TSCT. Similarly, Anjana and Anjaneyulu (2015) inferred that the crashes occurred less frequently at the signalized intersections with the TSCT based on the analysis of 3 years of crash data from 32 intersections in India. In contrast, Chen et al. (2007) found that the GSCT increased the number crashes at 187 signalized intersections in Taiwan. In addition, crashes increased by 19\% at the signalized intersections with both GSCT and RSCT. However, Chiou and Chang (2010) found that the RSCT did not have a significant effect on crashes in the long term. They found that the number of crashes did not significantly change after 4.5 months of installation of RSCT. Thus, the effects of TSCT on collisions were inconsistent.

### 2.2. Impacts of TSCT on driver behavior

The impacts of TSCT on driver behavior such as red-light violations, approach speed of vehicles, and decision to stop at intersections were evaluated using individual vehicle data. Several studies suggested that the GSCT discouraged drivers from crossing the intersection before the onset of red light and thereby it decreased the number of red-light violation (Chiou \& Chang, 2010; Jatoth et al., 2021; Kidwai et al., 2005; Kłos et al., 2020; Devalla et al., 2015). On the other hand, some studies found that the RSCT increased red-light violations because the drivers tend to start before red phase ends when they can estimate the end time of red phase based on the countdown on the RSCT (Kashani et al., 2020; Biswas et al., 2017; Jatoth et al., 2021). But Kłos et al. (2020) suggested that the RSCT without showing countdown in the last 3 s of red phase was effective in reducing red-light violations.

Huang et al. (2017) observed that the average maximum deceleration rate was reduced by 1 to $1.8 \mathrm{~m} / \mathrm{s}^{2}$ in the presence of GSCT due to earlier decision to stop at the intersection. Moreover, Islam et al. (2017) revealed that the probability of stopping at the intersection increased by 25\% and the deceleration decreased in the presence of green light counters during the last 10 s of the phase. Haperen et al. (2016) found that the drivers used lower deceleration rates to stop at the intersection and applied brakes in a longer stretch in the presence of GSCT. Also, Yan et al. (2022) suggested that the variation in acceleration while crossing and deceleration during stopping was higher in the presence of GSCT.

Some studies found that the GSCT increased approach speed and decreased headway. Krukowicz et al. (2021) suggested that approach speed of vehicles increased with the presence of GSCT. Ma et al. (2010) also found that the GSCT increased the approach speed of vehicles at the intersections to pass the intersection without any violation when encountering yellow light. Devalla et al. (2015) also suggested that the presence of the GSCT encouraged the drivers to travel at higher speeds. Ni and Li (2014) observed that the vehicles tend to maintain a smaller headway with the presence of GSCT.

### 2.3. Impacts of TSCT on traffic efficiency

Some studies found that the TSCT increased the traffic flow efficiency by reducing discharge time gaps. For instance, Sharma et al. (2009) found that the discharge time gap continuously decreased towards the end of green with the presence of the GSCT in India. Similarly, Wenbo et al. (2013) observed that the RSCT reduced the saturation headway of discharge vehicles and the capacity of through movement increased by about 5 to 10\%. They explained that this was because more drivers tried to start earlier at the end of red.

In contrast, some studies found that the GSCT reduced the traffic flow efficiency. Limanond et al. (2010) found that the GSCT reduced the saturation flow rate because the drivers generally increased the discharge headway. Haperen et al. (2016) also suggested that the GSCT decreased the traffic flow efficiency as more vehicles decided to stop in the presence of counter. In particular, higher number of vehicles stopped at the intersection when displaying the countdown for the final 3 s of green and red phases compared to displaying the countdown for the entire phases. However, Biswas et al. (2017) found that the GSCT was not effective in improving efficiency as the saturation flow rate remained unaffected.

Some studies suggested that the RSCT reduced the start-up lost time and the saturated headway, and thereby increased the traffic efficiency (Biswas et al., 2017; Raksuntorn, 2012; Chiou \& Chang, 2010; Jatoth et al., 2021; Haperen et al., 2016; Islam et al., 2016; Krukowicz et al., 2021). Li et al. (2014) also inferred that the RSCT decreased the perception-reaction time from 2.12 s to 1.48 s and the variation in perception-reaction time. On the other hand, Liu et al. (2012) and Limanond et al. (2010) stated that the RSCT increased the saturation headway and decreased the intersection capacity. On the other hand, Islam et al. (2016) observed that the RSCT reduced the headway of the first queued vehicle by 0.82 s and improved the traffic efficiency at signalized intersections.

### 2.4. Impacts of TSCT on driver satisfaction and comfort

The TSCT also positively affects driver satisfaction and comfort, contributing to a better overall driving experience. Chang and Jung (2017) observed from the survey that the TSCT generally had higher satisfaction score than the standard signals. Similarly, Fujita et al. (2007) found that the TSCT also had positive impact on the driver's state of mind and reduced driver aggression.

Rijavec et al. (2013) conducted a survey for 411 participants in Slovenia and inferred that 84\% of the respondents deemed the TSCT to be a positive impact on safety. Driver's ability to prepare for starting and stopping, and the information on duration of individual phases were found to be the major reasons for the response. Limanond et al. (2010) also conducted a public survey in Thailand and found that 64\% of the car drivers and 52\% of the motorcycle riders agreed that the TSCT reduced their frustration level. A survey-based study by Pan et al. (2017) also highlighted that the red-light violation at the intersections with GSCT was expected to decrease.

## 3. Methods

### 3.1. Description of data

This study evaluated the impacts of TSCT on traffic safety and efficiency at two signalized intersections along Huron Church Road between Totten Street and Dorchester Road in Windsor, Ontario, Canada as illustrated in Fig. 1. The signals have the pre-timed signal timing plans. This section was selected due to its higher incidence of red-light violations compared to other intersections in the city and its high volume of truck traffic, attributed to its proximity to the Windsor-Detroit international border crossing. This results in frequent interactions between passenger cars and trucks at signalized intersections, presenting

![](https://cdn.mathpix.com/cropped/cd1c1d0d-c2de-4094-a3e7-73c276d50eca-03.jpg?height=767&width=857&top_left_y=189&top_left_x=138)
Fig. 1. Aerial view of signalized intersections on Huron Church Road (Source: Google, 2024).

unique traffic characteristics that are not common at urban streets.
Traffic data were obtained from the City of Windsor including hourly traffic volumes, vehicle type composition (passenger cars and commercial trucks), signal timing plans (cycle length, signal phases, and durations) during afternoon peak hours (4 to 5 pm ), and road geometry (number of lanes, lane width). In the studied section, the afternoon peak hour traffic volumes on northbound and southbound Huron Church Road are 1,287 and 1,673 vehicles/hour, respectively, and the percentage of trucks is 24\% in both directions.

Huron Church Road features six through lanes (three in each direction) with dedicated left-turn and right-turn lanes. The intersections at Totten Street and Dorchester Road are four-legged signalized intersections with a cycle time of 120 s, featuring yellow phases of 4 s for through movements and 3 s for left-turn movements. Left turns from Huron Church Road are protected, while left turns from side roads (Totten Street and Dorchester Road) are unprotected, allowing vehicles to turn left during the green phase if no oncoming traffic is present. The posted speed limits are 60 km/h on Huron Church Road and 50 km/h on the side roads.

Since the TSCT has not been implemented in Canada yet and the observed traffic data in the presence of TSCT at the study site are not available, the impacts of TSCT on traffic safety and efficiency were evaluated using the PTV Vissim traffic simulation software (PTV AG, 2022). Traffic volume and signal timing data were imported into the software, and simulations were conducted in the following four scenarios: (1) No timer, (2) GSCT only, (3) RSCT only, and (4) a combination of GSCT and RSCT (GSCT + RSCT). It is important to note that the GSCT + RSCT scenario does not represent the additive effects of GSCT only and RSCT only as the sequential influence of GSCT and RSCT on driver behavior across successive green and red phases alters traffic patterns. The YSCT was not evaluated since it is less prevalent due to the short duration of the yellow phase where driver behavior is more influenced by the distance to the stop line and vehicle speed rather than the timer.

Additionally, the data collected from Vissim were utilized to conduct a spatiotemporal analysis of approach speeds and acceleration/deceleration at intersections for each scenario. Surrogate safety measures and traffic conflicts were estimated using the vehicle trajectory dataset obtained from Vissim. The Vissim simulation and conflict analysis methods are explained in detail in the following sections.

### 3.2. Vissim traffic simulation

The Vissim model was developed for the existing conditions (i.e., notimer scenario) using the default distributions of acceleration and deceleration for cars and trucks, and the default driving behavior (carfollowing and lane-changing) parameters in Vissim as the observed vehicle trajectories were not available. However, other model parameters were calibrated to reflect local traffic conditions in the study area. These parameters include distributions of speed for different speed limits on Huron Church Road and side roads, car and truck inputs for different approaches, signal timing plans, and speed transition while entering or exiting Huron Church Road due to changes in speed limit. In particular, car and truck inputs were determined based on the observed turning movement counts at the two intersections provided by the City of Windsor.

To reflect differential impacts of different types of TSCT on driver behavior, the changes in key driving behavior parameter in respective signal phases compared to the no-timer scenario were determined based on the literature. For the GSCT, the driver behavior was simulated according to the changes in compliance rate during the red phase (or redlight violation), and acceleration/deceleration and approach speed during green and yellow phases. This is because the compliance rate during the green phase is generally 100\% as it is highly unlikely that drivers stop during the green phase (i.e., green-light violation). It is expected that in the presence of GSCT, drivers are more likely to cross the intersection at the end of green phase, but this will increase the chances of red-light violation at the beginning of red phase. For the RSCT, the driver behavior was simulated according to the changes in acceleration/deceleration and approach speed during the red phase and reaction time to onset of the green phase. Vissim parameter values were determined based on the literature as shown in Table 1. The reasons for different parameter values for each type of TSCT, signal phase and vehicle type were explained in Table 1.

Drivers' compliance rates in Vissim were adjusted to account for the effects of the TSCT on red-light violations (RLV). In the no-timer scenario, a compliance rate of 99.95\% was assumed based on the data reported by CTV News Windsor (2023). The report identified Huron Church Road as the location with the highest number of issued tickets in Windsor. Using the number of issued tickets and the average hourly traffic flow on Huron Church Road, the rate of RLV was calculated to be 0.05\%. The compliance rate for the GSCT scenario was increased to $99.96 \%$ (100-0.05 * (1-0.2)) based on a 20\% reduction in RLV observed in Paul and Ghosh (2020). The RSCT scenario maintained the same compliance rate as the no-timer-scenario based on the findings from Biswas et al. (2017) indicating no significant increase in RLV after the installation of RSCT.

Speed distribution, acceleration, and deceleration values in the GSCT scenario were also adjusted based on the observed driver behavior in the literature. Past studies observed that the drivers generally increased approach speeds (Krukowicz et al., 2021; Ma et al., 2010; Devalla et al., 2015) in the presence of GSCT. Thus, the 85th percentile speed was assumed to be the posted speed limit for a given road (60 or 50 km/h) in the no-timer scenario and it was increased by 9\% in the presence of GSCT as observed in the previous field studies (Paul et al., 2022; Paul \& Ghosh, 2020) during the green and yellow signal phases. Past studies also observed that the drivers increased acceleration (Milaszewicz, 2018; Yan et al., 2022; Paul et al., 2022) and decreased deceleration (Huang et al., 2017; Islam et al., 2017; Haperen et al., 2016; Paul et al., 2022). Default distributions for acceleration and deceleration in Vissim were used for the no-timer scenario. Based on the average percentage changes in acceleration and deceleration after the installation of GSCT at 5 different sites observed in Paul et al. (2022), the acceleration distribution was increased by 53.4\% and the deceleration distribution was decreased by 18.2\% for the GSCT scenario.

Driver reaction times after the start of green phase were also modified based on the finding from Li et al. (2014) that the RSCT significantly

Table 1
Parameters of Vissim simulation.
| Parameters for Calibration | No timer | GSCT-only |  |  | RSCT-only |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | Green phase | Yellow phase | Red phase | Green phase | Yellow phase | Red phase |
| Compliance rate | $99.95 \%^{(1)}$ | $99.96 \%^{(2)}$ (only applies to red phase) |  |  | $99.95 \%^{(3)}$ (only applies to red phase) |  |  |
| Approach speed distribution (km/h) (minimum-85th percentile-maximum) |  |  |  |  |  |  |  |
| Huron Church Road | 50-60-70* | $50-66^{(4)}-70$ | $50-66^{(4)}-70$ | 50-60-70* | 50-60-70* | 50-60-70* | 50-60-70* |
| Desired acceleration distribution ( $\mathrm{m} / \mathrm{s}^{2}$ ) |  |  |  |  |  |  |  |
| Car | 0-3.5* | $0-5.37^{(4-6)}$ | $0-5.37^{(4-6)}$ | 0-3.5* | 0-3.5* | 0-3.5* | 0-3.5* |
| Truck | 0-2.5* | $0-3.83^{(4-6)}$ | $0-3.83^{(4-6)}$ | 0-2.5* | 0-2.5* | 0-2.5* | 0-2.5* |
| Desired deceleration distribution ( $\mathrm{m} / \mathrm{s}^{2}$ ) |  |  |  |  |  |  |  |
| Car | 2.55-3* | 2.09-2.45 ${ }^{(4,7-9)}$ | $2.09-2.45^{(4,7-9)}$ | 2.55-3* | 2.55-3* | 2.55-3* | $2.09-2.45^{(7-9)}$ |
| Truck | 1.05-1.5* | $0.86-1.23^{(7-9)}$ | $0.86-1.23^{(7-9)}$ | 1.05-1.5* | 1.05-1.5* | 1.05-1.5* | $0.86-1.23^{(7-9)}$ |
| Reaction time to onset of green signal | $2 \mathrm{~s}^{*}$ | $2 \mathrm{~s}^{*}$ | $2 \mathrm{~s}^{*}$ | $2 \mathrm{~s}^{*}$ | $2 \mathrm{~s}^{*}$ | $2 \mathrm{~s}^{*}$ | 0.5 s** |
| Parameters for Calibration | No timer |  | GSCT+RSCT |  |  |  |  |
|  |  |  | Green phase |  | Yellow phase |  | Red phase |
| Compliance rate | $99.95 \%^{(1)}$ |  | $99.96 \%^{(2)}$ (only applies to red phase) |  |  |  |  |
| Approach speed distribution (km/h) (minimum-85th percentile-maximum) |  |  |  |  |  |  |  |
| Huron Church Road |  | 50-60-70* | $50-66^{(4)}-70$ |  | $50-66^{(4)}-70$ |  | 50-60-70* |
| Desired acceleration distribution ( $\mathrm{m} / \mathrm{s}^{2}$ ) |  |  |  |  |  |  |  |
| Car |  | 0-3.5* | $0-5.37^{(4-6)}$ |  | $0-5.37^{(4-6)}$ |  | 0-3.5* |
| Truck |  | 0-2.5* | $0-3.83^{(4-6)}$ |  | $0-3.83^{(4-6)}$ |  | 0-2.5* |
| Desired deceleration distribution ( $\mathrm{m} / \mathrm{s}^{2}$ ) |  |  |  |  |  |  |  |
| Car |  | 2.55-3* | 2.09-2.45 ${ }^{(4,7-9)}$ |  | 2.09-2.45 ${ }^{(4,7-9)}$ |  | 2.09-2.45 ${ }^{(4,7-9)}$ |
| Truck |  | 1.05-1.5* | 0.86-1.23 ${ }^{(4,7-9)}$ |  | $0.86-1.23^{(4,7-9)}$ |  | 0.86-1.23 ${ }^{(4,7-9)}$ |
| Reaction time to onset of green signal |  | $2 \mathrm{~s}^{*}$ | $2 \mathrm{~s}^{*}$ |  | $2 \mathrm{~s}^{*}$ |  | 0.5 s** |


* Default values in Vissim.
**Shortest reaction time in Vissim.
${ }^{1}$ (News, 2023), ${ }^{2}$ (Paul and Ghosh, 2020), ${ }^{3}$ (Biswas et al., 2017), ${ }^{4}$ (Paul et al., 2022), ${ }^{5}$ (Milaszewicz, 2018), ${ }^{6}$ (Yan et al., 2022), ${ }^{7}$ (Huang et al., 2017), ${ }^{8}$ (Islam et al., 2017), ${ }^{9}$ (Haperen et al., 2016).
reduced start-up lost time (from 1 to 3 s to 0-2 s). In Vissim, reaction time is the delay between the start of green phase and the first vehicle's movement. A default reaction time of 2 s was used in the no-timer and GSCT scenarios, while the reaction time was reduced to 0.5 s, the minimum value in Vissim, in the RSCT scenario.

TSCTs were implemented exclusively in the through lanes of the Northbound (NB) and Southbound (SB) Huron Church Road corridor. Due to the lower overall traffic volume and minimal truck traffic on the side roads compared to Huron Church Road, it was assumed that the TSCT would not be implemented on the side roads. The TSCT was also excluded from right-turn and left-turn traffic due to the absence of a right-turn signal and the shorter duration of exclusive left-turn phases.

The simulation did not account for variations in driver behavior during specific times of signal phases such as the final seconds of the green phase due to a lack of the data. Instead, the effect of TSCT on driver behavior was modeled based on the proximity to the signals. In this study, all vehicles within the Region of Influence (ROI) were considered influenced by the TSCT, while those outside the ROI were unaffected due to visibility and the location of the dilemma zone. The ROI was determined to be 100 m before the traffic signal based on the survey study conducted by the authors that drivers could generally read the countdown at similar traffic signals in Windsor.

The Wiedemann 74 car-following model in Vissim was used to simulate car-following behavior as the model is suited for interrupted traffic flow on urban streets. Lane-changing behavior was simulated based on free lane selection. Due to absence of the observed driver behavior data in the study area, the default values of the model parameters were used.

### 3.3. Vissim Component Object model (COM) interface

To implement changes in driver behavior parameter values in different signal phases due to the TSCT during the Vissim simulation, dynamic adjustments of driver behavior parameters are required. Thus, the Component Object Model (COM) (PTV AG, 2024) interface was utilized to modify Vissim functions and parameters. In this study, Python programming language was used to change the parameter values for the respective signal phases throughout the simulation and was accessed through the Visual Studio Code platform.

Events within specific start and end times of each signal phase in each cycle were created in Vissim and the intervals were identified by synchronizing signal controller data with the simulation seconds. The event-based scripts, which included a Python code snippet written in Visual Studio Code, were executed during these events to modify the required driver behavior parameter values. The flow chart of the script execution sequence is shown in Fig. 2.

Owing to the offset between the signal controllers at both the intersections, the signal phase timings differ for each of the controllers. Thus, each event or signal phase duration was divided into three time intervals as follows: (1) Interval 1: Only the Totten intersection had red (or green) phase, (2) Interval 2: Both intersections had red (or green) phase, and (3) Interval 3: Only the Dorchester intersection had red (or green) phase. Then, the classification based on vehicle types (Cars and Trucks), the road link they are on (NB Huron Church Road, SB Huron Church Road), and their position on the link, were performed in each timer interval. As the ROI of the timers was different in each time interval, the code was scripted in such a way that when a vehicle enters the ROI when approaching a signal, the driver behavior parameter values were changed accordingly. When the vehicle is outside the ROI, the parameter values revert to their original ones.

As observed from the previous studies, the RSCT reduced the deceleration rate of the approaching vehicles and the reaction time of the vehicles to the onset of green signal. This was achieved by accessing the attributes "IndivDesDecelFunc" and "ReactTmDistr" in vehicle class and driver behavior class, respectively, when the vehicle followed the conditions and was in the ROI of the signal controller it approaches. In the presence of the GSCT, traffic compliance rate, acceleration rate, and speed of vehicles increased but the deceleration rate decreased. The compliance rate remained the same irrespective of the signal phases for a signal controller and was set to its respective value based on the TSCT scenario before the simulation started. Acceleration rate, deceleration rate and speed of the vehicles were modified through attributes such as

![](https://cdn.mathpix.com/cropped/cd1c1d0d-c2de-4094-a3e7-73c276d50eca-05.jpg?height=1206&width=1475&top_left_y=187&top_left_x=295)
Fig. 2. Flow chart of an event-based script for the traffic signal countdown timers.

"IndivDesAccelFunc," "IndivDesDecelFunc," and "DesSpeed," respectively, in the vehicle class, similar to the RSCT scenario. In the GSCT + RSCT scenario, the scripts for GSCT and RSCT were combined. Therefore, during the red and green phases, the parameter values were respectively changed in each phase throughout the simulation.

### 3.3.1. Surrogate Safety Assessment Model

A preliminary analysis of vehicle trajectory data was conducted to assess the impact of timers on safety in the entire road network using the Surrogate Safety Assessment Model (SSAM) (Federal Highway Administration, 2008). The SSAM calculates conflicts based on Post Encroachment Time (PET) and Time-to-Collision (TTC). A conflict is defined as an event when PET is shorter than 5 s and TTC is shorter than 1.5 s. The model classifies conflict events into crossing (85-180 degrees), lane change (30-85 degrees), and rear-end conflicts (0-30 degrees) based on the collision angle between vehicles. The total number of conflicts and their types were compared among different scenarios to understand the safety effects of TSCT on the road network.

### 3.4. Spatiotemporal analysis of traffic flow parameters

Traffic flow parameters such as average speed and acceleration/ deceleration were collected for cars, trucks, and overall traffic at 10 locations before the stop line up to 100 m in 10 m intervals using the data collection points in Vissim. Although the data were recorded for both intersections in both directions on Huron Church Road, data analysis was performed only for NB Huron Church Road at the Totten intersection for a demonstration purpose. The data were collected every second throughout the simulation, excluding the first 360 s of warm-up period (i.e., three signal cycles) and the average values of 10 simulation runs were calculated. The average values of the traffic flow parameters per second were calculated for each second of a signal cycle (0-120 s) from all 27 signal cycles in the simulation. The parameter values were plotted against the time in each cycle (0-120 s) and the distance from the stop line (the location of data collection points 10-100 m from the stop line) to observe spatiotemporal patterns of speed and acceleration/ deceleration in different scenarios. This spatiotemporal analysis helps understand the effect of TSCT on traffic flow and efficiency.

### 3.5. Spatial analysis of rear-end conflicts

Past studies found that rear-end conflicts significantly contributed to overall conflict events and were a key indicator of traffic safety in the presence of TSCT. To estimate rear-end conflicts, vehicle trajectory data were extracted from the simulation and the Crash Potential Index (CPI) was calculated for cars and trucks separately. The CPI represents the likelihood that the following vehicle's minimum required deceleration to avoid a collision with the lead vehicle (DRAC) exceeds its maximum available deceleration rate (MADR). The CPI can account for differences in deceleration capabilities between cars and trucks, and their risk of collision. The average MADRs for cars and trucks were assumed to be 8.45 and 5.01 m/s2, respectively, based on the study by Cunto and Saccomanno (2008). To account for delays in drivers' deceleration due to driver reaction time, the modified DRAC proposed by Zhao and Lee (2018) was employed in this study as follows:

$$
\operatorname{DRAC}(\mathrm{t})=\frac{\left(\mathrm{V}_{\mathrm{L}}(\mathrm{t})-\mathrm{V}_{\mathrm{F}}(\mathrm{t})\right)^{2}}{2 \mathrm{~S}(\mathrm{t})-\left(\mathrm{V}_{\mathrm{F}}(\mathrm{t})-\mathrm{V}_{\mathrm{L}}(\mathrm{t})^{*} \mathrm{t}_{\mathrm{r}}\right)}, \mathrm{V}_{\mathrm{F}}(\mathrm{t})>\mathrm{V}_{\mathrm{L}}(\mathrm{t})
$$

where $\mathrm{V}_{\mathrm{L}}(\mathrm{t})$ and $\mathrm{V}_{\mathrm{F}}(\mathrm{t})$ are the speeds of the lead and following
vehicles at time t , respectively; $\mathrm{S}(\mathrm{t})$ is the front-to-rear spacing between the lead and following vehicles at time t, and $\mathrm{t}_{\mathrm{r}}$ is the driver's reaction time. Based on the study by Dozza (2013), the reaction times were set at 1.45 s for car drivers and 0.26 s for truck drivers.

Initially, DRAC values were calculated for all vehicle pairs on the NB and SB Huron Roads and these values were compared with the MADR values to identify the number of conflicts and compute the CPI. For each scenario, the average of CPI in 10 simulation runs was computed. Additionally, the position of the following vehicle in each pair was recorded during conflict events, and a spatial analysis was performed to identify the distribution of CPI over the distance to the stop line. This approach provides insights into how the effects of TSCT on rear-end conflicts vary across different distances to the intersection and identifies the location with high risk of collision.

## 4. Results and discussions

### 4.1. Impacts of TSCT on traffic safety

The average number of conflicts obtained from 10 simulation runs for each of the scenarios were estimated using the SSAM model and compared among different scenarios as shown in Table 2. Due to a small number of observations, statistical significance of the difference in mean values between the TSCT scenarios and the no-timer scenario was assessed using the Mann-Whitney $U$ test, one of non-parametric statistical tests. Although the presence of any timer reduced the total number of conflicts compared to the no-timer scenario, the difference was not statistically significant at a 95\% confidence interval (p-value > 0.05). This result contrasts the finding from Paul and Ghosh (2020) that the crossing conflicts were significantly reduced (57.7\% reduction) in the presence of GSCT. This is because the rate of red-light violation was assumed to be lower based on higher compliance rate in Windsor compared to the studied intersections in Paul and Ghosh (2020), which reduced the probability of crossing the intersections during the red phase.

However, it was found that the proportion of rear-end conflicts in the total conflicts was the highest when compared to the other types of conflicts such as Crossing and Lane change conflicts in all the scenarios. This is consistent with the findings from the previous studies that rearend conflicts are most common types of conflicts at signalized intersections due to more frequent reactions required to avoid a collision with the lead vehicle during signal changes (Shahana \& Vedagiri, 2024; Yan et al., 2005).

The CPI was also calculated to assess the effects of timers on the rearend conflicts. As shown in Table 3, the mean CPI was reduced in the presence of all timers. The GSCT + RSCT scenario was the most effective as it reduced the CPI by 37\% compared to the no-timer scenario, followed by the RSCT scenario which reduced the CPI by 23\%. The reduction is statistically significant at a 95\% confidence interval (pvalue < 0.05). In particular, the reduction in the CPI was higher for cars than trucks. This result indicates that the GSCT + RSCT is more effective in reducing rear-end collision risk for cars than trucks.

The spatial analysis of rear-end conflicts using the CPI was performed based on the mean CPI at different distances to the stop line (0 to 100 m).

Table 2
Average number of conflicts predicted using SSAM.
| Scenario | Crossing | Rear-end | Lane change | Total |
| :--- | :--- | :--- | :--- | :--- |
| No timer | 17.5 | 188.8 | 88.6 | 294.9 |
| (\% of total conflicts) | 5.9 | 64.0 | 30.0 |  |
| GSCT | 18.9 | 179.4 | 94.4 | 292.7 |
| (\% of total conflicts) | 6.5 | 61.3 | 32.3 |  |
| RSCT | 15.3 | 178.2 | 83.7 | 277.2 |
| (\% of total conflicts) | 5.5 | 64.3 | 30.2 |  |
| GSCT + RSCT | 14.8 | 169.2 | 89.8 | 273.8 |
| (\% of total conflicts) | 5.4 | 61.8 | 32.8 |  |


Table 3
Comparison of Mean Crash Potential Index among timer scenarios.
| Timer Scenario | Cars |  | Trucks |  | Overall |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Number of conflicts | CPI $\left(\times 10^{-}\right. { }^{4}$ ) | Number of conflicts | CPI $\left(\times 10^{-}\right. { }^{4}$ ) | Number of conflicts | CPI $\left(\times 10^{-}\right. { }^{4}$ ) |
| No timer | 31.9 | 9.8 | 1.1 | 1.1 | 33.0 | 7.8 |
| GSCT | 29.9 | 9.5 | 0.7 | 0.7 | 30.6 | 7.3 |
| RSCT | 24.7 | 7.4 | 0.8 | 0.8 | 25.5 | 6.0 |
| GSCT + RSCT | 19.6 | 6.3 | 0.5 | 0.5 | 20.1 | 4.9 |


A regression model was fit to the observed data as follows:

$$
C P I=\alpha+\beta \bullet D
$$

where $C P I=$ CPI at a given distance to the stop line $\left(\times 10^{-4}\right), \alpha=$ intercept, $\beta=$ coefficient for the distance to stop line, and $D=$ distance to the stop line. The estimated parameters of regression models and goodness-of-fit of the models $\left(R^{2}\right)$ for each timer scenario are shown in Table 4.

Table 4 shows that the CPI generally decreased as the distance to the stop line decreased based on positive $\beta$ values. In particular, this trend is significant for the GSCT and RSCT scenarios at a 95\% confidence interval (p-value < 0.05). However, there is no significant relationship between the CPI and the distance to the stop line for the no-timer scenario as indicated by $\beta$ value close to zero and poor model fit ( $R^{2}$ close to zero).

This indicates that the GSCT and RSCT are more effective in reducing the CPI at the location closer to the stop line. This spatial pattern of CPI is similar to the finding from Ni and Li (2014) that the probability of rear-end crashes was lower at the intersections with GSCT compared to the intersections without GSCT in a zone closer to the stop line.

### 4.2. Impacts of TSCT on traffic efficiency

To evaluate the impacts of TSCT on traffic efficiency, spatiotemporal patterns of speed were compared among different scenarios. Fig. 3 shows average speed at each data collection point and each second in a cycle were calculated using the speeds for each cycle in 10 simulation runs. In the figure, the red phase occurs at 0 to 44 s and 117 to 120 s whereas the green phase starts at 45 s and ends at 116 s. The total length of one cycle is 120 s. Lighter yellow color represents higher speed and darker blue color represents lower speed and varied between 0 to 70 km/h.

Fig. 3 shows that the speed was initially slower at the beginning of green phase (45 s) and it gradually increased until the end of green phase in all scenarios. However, the speed near the stop line during the green phase as indicated by the red box was generally higher for the GSCT and GSCT + RSCT scenarios (average speed of 61.8 and 61.9 km/h, respectively) than the no-timer and RSCT scenarios (average speed of 57.0 km and 56.9 km/h, respectively). This result is consistent with the results from previous studies that drivers tend to increase the speed to cross the intersection during the green phase in the presence of GSCT (Krukowicz et al., 2021; Ma et al., 2010; Devalla et al., 2015).

The figure also shows that the speed 70-100 m from the stop line while approaching the intersection during the red phase was lower in the RSCT scenario (average speed of 46.7 km/h) compared to the notimer and GSCT scenarios (average speed of 48.0 km/h and 47.5 km/ h, respectively) as indicated by darker blue color. This indicates that the drivers were able to make an earlier decision to reduce speed while approaching during the red phase in the presence of RSCT.

Based on these observed speed patterns, the reasons for reduction in the CPI in the GSCT and RSCT scenarios can be explained as follows. In the GSCT scenario, as more vehicles pass the intersection at higher speed than the no-timer scenario, they are less likely to reduce speed near the

Table 4
Estimated parameters of regression models.
|  | No timer |  | GSCT |  | RSCT |  | GSCT + RSCT |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Parameter | p-value | Parameter | p-value | Parameter | p-value | Parameter | p-value |
| $\alpha$ | 21.6 | 0.149 | 21.9 | 0.030 | 40.1 | 0.002 | 41.7 | 0.016 |
| $\beta$ | 0.003 | 0.989 | 1.5 | 0.001 | 1.9* | 0.026 | 0.8 | 0.227 |
| $R^{2}$ | $2.48 \mathrm{e}-05$ |  | 0.76 |  | 0.48 |  | 0.18 |  |


* Significant at a $95 \%$ confidence interval.

![](https://cdn.mathpix.com/cropped/cd1c1d0d-c2de-4094-a3e7-73c276d50eca-07.jpg?height=1264&width=1561&top_left_y=579&top_left_x=256)
Fig. 3. Spatiotemporal distributions of speeds (km/h) for all scenarios.

intersection at the end of the green phase, which can decrease rear-end conflicts. In the RSCT scenario, as vehicles start decelerating earlier during the red phase, they can reduce speed more gradually as they approach the intersection and this results in the reduction in rear-end conflicts.

The spatiotemporal patterns of acceleration and deceleration were also compared among all scenarios as shown in Fig. 4. It was found that the GSCT and GSCT + RSCT increased acceleration 80-100 m from the stop line during the green phase (average acceleration of 0.47 and 0.49 $\mathrm{m} / \mathrm{s}^{2}$, respectively) compared to the no-timer and RSCT scenarios (average acceleration of $0.15 \mathrm{~m} / \mathrm{s}^{2}$ for both scenarios). This indicates that the GSCT facilitated earlier decision-making and helped drivers cross the intersection by increasing speed as they approach the intersection during the green phase. Fig. 4 also shows that the deceleration started 70-100 m from the stop line during the red phase was higher for the RSCT scenario (average deceleration of $-1.03 \mathrm{~m} / \mathrm{s}^{2}$ ) than the notimer, GSCT and GSCT + RSCT scenarios (average deceleration of $-0.81 \mathrm{~m} / \mathrm{s}^{2},-0.79 \mathrm{~m} / \mathrm{s}^{2}$, and $-0.99 \mathrm{~m} / \mathrm{s}^{2}$, respectively). Also, there was no clear difference in the acceleration rates between the no-timer and RSCT scenarios at the start of the green phase. This shows that although the RSCT facilitated early start of vehicles at the beginning of green, it did not significantly affect the speed.

Overall average speed in the entire road network was also compared as traffic signal operations can have a chain effect on other roads connected to the intersection as shown in Table 5. The difference in average speed between the no-timer and TSCT scenarios was statistically significant at a 95\% confidence interval based on the result of Mann Whitney $U$ test. The table shows that the GSCT + RSCT scenario had the highest increase in the speed (6.1\%) compared to the no-timer scenario among the TSCT scenarios. The GSCT also increased the speed by 4.4\%. However, the RSCT rather slightly decreased the speed by $0.9 \%$. This is because in spite of earlier start at the beginning of green, the deceleration also started earlier when approaching the intersection during the red phase in the presence of RSCT. It is worth noting that the increase in

![](https://cdn.mathpix.com/cropped/cd1c1d0d-c2de-4094-a3e7-73c276d50eca-08.jpg?height=1257&width=1557&top_left_y=202&top_left_x=256)
Fig. 4. Spatiotemporal distributions of acceleration/deceleration $\left(\mathrm{m} / \mathrm{s}^{2}\right)$ for all scenarios.

Table 5
Overall average speed (km/h) of entire road network.
|  | No-timer | GSCT | RSCT | GSCT + RSCT |
| :--- | :--- | :--- | :--- | :--- |
| Car | 28.4 | 29.4 | 28.1 | 29.9 |
| \% Change | - | 3.6 | -1.0 | 5.2 |
| Truck | 30.9 | 33.0 | 30.7 | 33.7 |
| \% Change | - | 7.1 | -0.5 | 9.0 |
| All | 29.0 | 30.3 | 28.7 | 30.7 |
| \% Change | - | 4.4 | -0.9 | 6.1 |


speed was higher for trucks than cars in the presence of GSCT and GSCT + RSCT. This shows that the GSCT can increase truck speed more effectively than car speed. Moreover, Table 5 shows that the average speed of car was lower than the average speed of truck. This is because a majority (70-75\%) of vehicles on Huron Church Road were cars which had to stop and go more frequently than trucks. Also, all vehicles on the side roads were assumed to be cars. In particular, these cars stopped for a long period of time during the red phase to yield to car and truck traffic on Huron Church Road. Thus, their low average speeds on the side roads decreased overall average car speed for the entire road network.

The average number of vehicles entering the intersections during the green phase for all cycles was compared as an operational measure of efficiency. Higher number of entering vehicles is closely correlated with higher saturation flow rate and capacity. Table 6(a) shows the number of vehicles crossing the stop line during the first 5 s of the green phase using the data collection points at the stop line in Vissim. The table shows that the GSCT + RSCT scenario allowed the highest number of

Table 6
Average number of vehicles entering the intersection during green phase.
| (a) First 5 s of green phase |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  | No-timer | GSCT | RSCT | GSCT + RSCT |
| Car | 15.3 | 16.4 | 26.9* | 31.2* |
| \% Change | - | 7.2 | 75.8 | 103.9 |
| Truck | 11.6 | 11.5 | 16.5* | 18.6* |
| \% Change | - | -0.9 | 42.2 | 60.3 |
| All | 26.9 | 27.9 | 43.4* | 49.8* |
| \% Change | - | 3.7 | 61.3 | 85.1 |


| (b) Entire green phase |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  | No-timer | GSCT | RSCT | GSCT + RSCT |
| Car | 237 | 250 | 239 | 250 |
| Truck | 133 | 130 | 136 | 130 |
| All | 370 | 380 | 375 | 380 |

*The difference in the number of vehicle entries between the no-timer and TSCT scenarios is statistically significant at a 95 \% confidence interval.
vehicle entries during the first 5 s of the green phase at the intersection with 50 vehicles in all cycles, marking an 85.1\% increase over the notimer scenario. The RSCT scenario also showed the increase by 61.3\% compared to the no-timer scenario. A Mann-Whitney U Test showed a statistically significant difference in the number of vehicle entries for both RSCT and GSCT + RSCT scenarios compared to the no-timer scenario at a 95\% confidence interval ( $\mathrm{p}<0.05$ ), but no significant difference between GSCT and no-timer scenarios. This suggests that the
reduced reaction time in the RSCT scenario led to an earlier start in the green phase and an increase in the number of vehicle entries. Additionally, the increase in the number of vehicle entries was higher for cars than trucks due to their higher speed and acceleration. Table 6(b) shows that the average number of vehicle entries during entire the green phase for all cycles was slightly higher in all TSCT scenarios than the no-timer scenario. However, the differences in vehicle entries between TSCT and no-timer scenarios were not statistically significant at a 95\% confidence interval ( $\mathrm{p}>0.05$ ).

## 5. Conclusions and recommendations

This study evaluated the impacts of TSCT on traffic safety and efficiency at signalized intersections. Driver behavior and traffic flow were simulated for signalized intersections on a section of Huron Church Road in Windsor, Ontario, Canada using Vissim traffic simulation. The simulation results were compared among four scenarios: no-timer, GSCT, RSCT, and a combination of GSCT and RSCT (GSCT + RSCT). The Vissim simulation was calibrated to replicate the existing conditions (i.e., no-timer scenario). Changes in driver behavior in different phases in the presence of GSCT and RSCT were simulated through Vissim-COM interface based on previous field observations and simulation studies. The key findings from the study are summarized as follows.

First, among different types of TSCT, the GSCT + RSCT scenario was the most effective in improving both traffic safety and efficiency compared to the no-timer scenario. The GSCT + RSCT showed the largest reduction in the CPI and the largest increase in the average number of vehicles entering the intersection during green phase in each cycle.

Second, the GSCT increased speed near the stop line during the green phase and the RSCT induced earlier start of deceleration for approach vehicles longer distance from the stop line during the red phase. Due to these effects, more vehicles can pass the intersection without speed reduction during the green phase and gradually reduce the speed during the red phase. Consequently, these behavioral changes help reduce rearend conflicts and also improve the traffic flow thereby increasing the overall traffic efficiency.

Third, the impacts of TSCT on car and truck were different. It was found that cars showed higher reduction in the CPI than trucks in the GSCT + RSCT scenario compared to the no-timer scenario. However, trucks showed higher increase in speed than cars in all TSCT scenarios. This indicates that the TSCT can help cars avoid conflicts with trucks and also allow trucks move faster without conflicts with cars.

This study addresses the research gap that there is a lack of simulation-based studies that examined the network-wide impacts of TSCT on traffic safety and efficiency, especially at signalized intersections with high truck volume. Moreover, the existing simulationbased study did not explicitly consider how the TSCT influences on driver behavior in different signal phases, which is required for more accurate predictions of the impacts of TSCT. Thus, this study contributes to better understanding of how the TSCT can improve traffic safety and efficiency based on analysis of changes in driver behavior in the presence of TSCT.

The findings in this study imply that the TSCT should be designed to help drivers adjust their speed more safely and efficiently according to conditions during green and red phases and the transition period between the two phases. More specifically, the countdown should be clearly visible from a long distance and displayed for a sufficient amount of time so that drivers can make decisions in advance. Since the changes in the observed driver behavior in the presence of TSCT were generally common in different countries (e.g., Poland, China, India, United States, Belgium) based on the literature review, it is expected that the findings in this study that reflected these changes are transferrable to other study areas.

However, there are some limitations in this study. First, the difference in compliance rate of traffic signal and reactions to the TSCT between car and truck drivers could not be captured due to a lack of data. For instance, truck drivers may have higher compliance rate than car drivers since they are more likely to be cautious and avoid red-light violation. Consequently, the conflicts between cars and trucks are likely to be higher during the transition period from the green phase to the red phase. Also, this study made a hypothetical assumption that all drivers would respond to the TSCT, although some drivers may ignore the TSCT in real world. For instance, when not all drivers start earlier in the beginning of green phase in the presence of RSCT, the traffic efficiency will not significantly increase.

In the future study, it is recommended to evaluate the impacts of various TSCT designs on driving behavior, traffic conflicts, and overall traffic efficiency. For example, a countdown is not displayed in the last 5 s of the red phase to prevent risky behaviors such as red-light violations (e.g., early starts before the green phase begins). It is also recommended to extensively analyze the impacts of TSCT for more consecutive intersections with different traffic and environmental conditions. Lastly, it is recommended to examine the effects of TSCT on safety and efficiency in mixed traffic conditions, involving both human-driven and autonomous vehicles, considering their unique performance characteristics and interactions.

## CRediT authorship contribution statement

Vadhul Krishnan Veerakumar: Writing - original draft, Software, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. Chris Lee: Writing - review \& editing, Supervision, Investigation, Funding acquisition, Conceptualization.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgment

This research was supported by Natural Sciences and Engineering Research Council of Canada [Grant number: RGPIN-2019-04430].

## References

Anjana, S., \& Anjaneyulu, M. V. L. R. (2015). Safety analysis of urban signalized intersections under mixed traffic. Journal of Safety Research, 52, 9-14.
Biswas, S., Ghosh, I., \& Chandra, S. (2017). Influence of signal countdown timer on efficiency and safety at signalized intersections. Canadian Journal of Civil Engineering, 44(4), 308-318.
Chang, J., \& Jung, K. (2017). Effects of traffic signals with a countdown indicator: Driver's reaction time and subjective satisfaction in driving simulation. Journal of Ergonomics Society of Korea, 36(5), 459-466.
Chen, I. C., Chang, K. K., Chang, C. C., \& Lai, C. H. (2007). The impact evaluation of vehicular signal countdown displays. Institute of Transportation, Ministry of Transportation and Communications, Taiwan.
Chiou, Y., \& Chang, C.-H. (2010). Driver responses to green and red vehicular signal countdown displays: Safety and efficiency aspects. Accident Analysis and Prevention, 42, 1057-1065. https://doi.org/10.1016/j.aap.2009.12.014
CTV News Windsor. (2023). These two red light camera intersections in Windsor collect the most tickets. April 24, 2023. Retrieved from https://windsor.ctvnews.ca/thesetwo-red-light-camera-intersections-in-windsor-collect-the-most-tickets-1.6368409.
Cunto, F., \& Saccomanno, F. F. (2008). Calibration and validation of simulated vehicle safety performance at signalized intersections. Accident Analysis and Prevention, 40 (3), 1171-1179.
Devalla, J., Biswas, S., \& Ghosh, I. (2015). The effect of countdown timer on the approach speed at signalised intersections. Procedia Computer Science, 52, 920-925.
Dozza, M. (2013). What factors influence drivers' response time for evasive maneuvers in real traffic? Accident Analysis and Prevention, 58, 299-308.
Federal Highway Administration. (2008). Surrogate Safety Assessment Model and Validation: Final Report. McLean: Research, Development, and Technology.
Fujita, M., Yilmaz, C., \& Suzuki, K. (2007). Behavior and consciousness analyses on effect of traffic signals including countdown device for vehicles. Journal of the East Asian Society for Transportation Studies, 7, 2289-2304.
Google (2024). Google Earth, 2024.

Haperen, W., Pirdavani, A., Brijs, T., \& Bellemans, T. (2016). Evaluating traffic safety and performance effects of countdown timers on signalized intersections: A driving simulator study. Advances in Transportation Studies an International Journal, Special Issue, 1, 7-22.
Huang, M., Fujita, M., \& Wisetjindawat, W. (2017). Countdown timers, video surveillance and drivers' stop/go behavior: Winter versus summer. Accident Analysis and Prevention, 98, 185-197. https://doi.org/10.1016/j.aap.2016.09.020
Islam, M. R., Wyman, A. A., \& Hurwitz, D. S. (2017). Safer driver responses at intersections with green signal countdown timers. Transportation Research Part F: Traffic Psychology and Behaviour, 51, 1-13.
Islam, M. R., Hurwitz, D. S., \& Macuga, K. (2016). Improved driver responses at intersections with red signal countdown timers. Transportation Research Part C: Emerging Technologies, 63, 207-221.
Jatoth, J., Singh, N. K., \& Mehar, A. (2021). Evaluating the performance of signalized intersection with signal countdown timer. International Journal of Intelligent Transportation Systems Research, 19(1), 182-190. https://doi.org/10.1007/s13177-020-00233-2
Kashani, A., Nezhad, A., \& Afshar, A. (2020). Evaluating the effects of countdown timers on intersection safety: A case study in Arak, Iran. AUT Journal of Civil Engineering, Online First. https://doi.org/10.22060/ajce.2019.16656.5596.
Kidwai, F. A., Ibrahim, M. R., \& Karim, M. R. (2005). Traffic flow analysis of digital count down signalized intersection. In Proceedings of the Eastern Asia Society for Transportation Studies (p. 5).
Kłos, M. J., Sobota, A., Żochowska, R., \& Karoń, G. (2020). Effects of countdown timers on traffic safety at signalized intersections. Transactions on Transport Sciences, 11(2), 19-27. https://doi.org/10.5507/tots.2020.010
Krukowicz, T., Firlag, K., Suda, J., \& Czerlinski, M. (2021). Analysis of the impact of countdown signal timers on driving behavior and road safety. Energies, 14, 7081.
Li, Z., Zhang, J., Rong, J., Ma, J., \& Guo, Z. (2014). Measurement and comparative analysis of driver's perception-reaction time to green phase at the intersections with and without a countdown timer. Transportation Research Part F: Traffic Psychology and Behaviour, 22, 50-62.
Limanond, T., Prabjabok, P., \& Tippayawong, K. (2010). Exploring impacts of countdown timers on traffic operations and driver behavior at a signalized intersection in Bangkok. Transport Policy, 17(6), 420-427. https://doi.org/10.1016/j. tranpol.2010.04.009
Liu, P., Yu, H., Wang, W., Ma, J., \& Wang, S. (2012). Evaluating the effects of signal countdown timers on queue discharge characteristics at signalized intersections in China. Transportation Research Record: Journal of the Transportation Research Board, No., 2286, 39-48.
Long, K., Han, L. D., \& Yang, Q. (2011). Effects of countdown timers on driver behavior after the yellow onset at Chinese intersections. Traffic Injury Prevention, 12(5), 538-544. https://doi.org/10.1080/15389588.2011.593010
Ma, W., Liu, Y., \& Yang, X. (2010). Investigating the impacts of green signal countdown devices: Empirical approach and case study in China. Journal of Transportation Engineering, 136(11), 1049-1055. https://doi.org/10.1061/(ASCE)TE.1943-5436.0000181
Milaszewicz, B. (2018). The issue of using countdown timers at intersections with traffic lights: a literature review. In , XI. Proceedings of. International Science-Technical Conference Automotive Safety.
Ni, Y., \& Li, K. (2014). Estimating rear-end accident probabilities at signalized intersections: A comparison study of intersections with and without green signal countdown devices. Traffic Injury Prevention, 15(6), 583-590. https://doi.org/10.1080/15389588.2013.845752
Pan, F., Zhang, L., Ma, C., Li, H., Yang, J., Liu, T., Wang, F., \& Chai, S. (2017). Impact of vehicular countdown signals on driving psychologies and behaviors: Taking China as an example. Journal of Advanced Transportation, 2017, 1-11.
Paul, M., \& Ghosh, I. (2020). Influence of green signal countdown timer on severe crash types at signalized intersections due to red light violations. Transportation Letters, 12 (8), 528-539.
Paul, M., Ghosh, I., \& Haque, M. (2022). The effects of green signal countdown timer and retiming of signal intervals on dilemma zone related crash risk at signalized intersections under heterogeneous traffic conditions. Safety Science, 154, Article 105862.
PTV AG. (2022). PTV Vissim 2023. Karlsruhe, Germany.
PTV AG. (2024). PTV Vissim COM Help.
Raksuntorn, W. (2012). The effects of countdown signals on intersection capacity. International Transaction Journal of Engineering, Management, \& Applied Sciences \& Technologies, 3(2), 159-165.
Sharma, A., Vanajakshi, L., \& Rao, N. (2009). Effect of phase countdown timers on queue discharge characteristics under heterogeneous traffic conditions. Transportation Research Record: Journal of the Transportation Research Board, 2130, 93-100. https://doi.org/10.3141/2130-12
Rijavec, R., Zakovšek, J., \& Maher, T. (2013). Acceptability of countdown signals at an urban signalized intersection and their influence on drivers behaviour. PROMET -Traffic \& Transportation, 25(1), 63-71. https://doi.org/10.7307/ptt.v25i1.1248
Shahana, A., \& Vedagiri, P. (2024). Developing rear-end and side-swipe conflict prediction models for urban signalized intersections under disordered traffic conditions. IATSS Research, 48, 1-13.
Spigolon, L. G., Bezerra, B. S., Bastos, J. T., Ferraz, A. C. P., \& Battistelle, R. A. G. (2015). Comparison between common traffic lights and three types of traffic lights with visual cycle - a safety and capacity analysis. Journal of Transport Literature, 9(4), 5-9.
Wenbo, S., Zhaocheng, H., Xi, X., \& Feifei, X. (2013). Exploring impacts of countdown timers on queue discharge characteristics of through movement at signalized intersections. Procedia - Social and Behavioral Sciences, 96, 255-264.
Yan, W., Wong, S. C., Loo, B., Wu, C., Huang, H., Pei, X., \& Meng, F. (2022). An assessment of the effect of green signal countdown timers on drivers' behavior and on road safety at intersections, based on driving simulator experiments and naturalistic observation studies. Journal of Safety Research, 82, 1-12.
Yan, X., Radwan, E., \& Abdel-Aty, M. (2005). Characteristics of rear-end accidents at signalized intersections using multiple logistic regression model. Accident Analysis and Prevention, 37, 983-995.
Zhao, P., \& Lee, C. (2018). Assessing rear-end collision risk of cars and heavy vehicles on freeways using a surrogate safety measure. Accident Analysis \& Prevention, 113, 149-158. https://doi.org/10.1016/j.aap.2018.01.033

Vadhul Krishnan Veerakumar is a Research Assistant in the Department of Civil and Environmental Engineering at the University of Windsor, Canada. He received the Master of Applied Science (MASc) degree from the University of Windsor. His research interests are in road safety, Intelligent Transportation Systems (ITS), and advanced traffic operations and control. His previous research experience involves understanding the driver behaviour in mixed vehicle population consisting human and autonomous vehicles, crash data analysis utilizing statistical models to identify the causal factors and spatial data analysis of high frequency crash locations using Geographical Information Systems (GIS).

Chris Lee, Ph.D., P.Eng. is a Professor of Civil and Environmental Engineering at the University of Windsor, Canada. He received the Ph.D. degree in Civil Engineering (Transportation) from the University of Waterloo. His main research interests are in traffic safety, driver behavior, and traffic operation and control. Dr. Lee has conducted research on vehicle interaction and conflicts in car-truck mixed traffic and manual-autonomous vehicle mixed traffic, prediction of car-following behavior using mathematical and datadriven models, prediction of crash frequency and injury severity, safety evaluation of countermeasures, advanced real-time speed control for freeways, driver safety in partiallyautomated vehicles, and aggressive and distracted driving behavior. Dr. Lee is an Associate Editor of two academic journals - Accident Analysis and Prevention and Canadian Journal of Civil Engineering.


[^0]:    * Corresponding author.
    E-mail addresses: veerakuv@uwindsor.ca (V.K. Veerakumar), cclee@uwindsor.ca (C. Lee).

