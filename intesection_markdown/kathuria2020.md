# Evaluating pedestrian vehicle interaction dynamics at un-signalized intersections: A proactive approach for safety analysis 

Ankit Kathuria ${ }^{\mathrm{a}, *}$, Perumal Vedagiri ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}}$ Department of Civil Engineering, Indian Institute of Technology Bombay, Powai, 400076, Mumbai, Maharashtra, India<br>${ }^{\mathrm{b}}$ Transportation System Engineering, Department of Civil Engineering, Indian Institute of Technology Bombay, India

ARTICLE INFO

Keywords:
Un-signalized intersection
Surrogate safety measures
Pedestrian safety
Trajectory data
Interaction pattern


#### Abstract

The present research demonstrates the use of advanced trajectory based data to analyze road user interactions at an un-signalized intersection under heterogeneous traffic complexities. This study demonstrates an improvement over the conventional grid-based analysis to estimate surrogate safety measures (SSM). An advanced patternbased approach to categorize pedestrian-vehicle interactions based on the road user behavior is proposed in the study. A concept of a two-interaction pattern has been applied, which deals with the responsive and non -responsive behavior of the road users, respectively. The behavior-based patterns were categorized based on the SSM like Speed, Time to Collision, and Gap Time profiles of the pedestrian and vehicle interacting on an unsignalized intersection. On conducting a variable importance test, i.e., k-fold test, it was comprehended that, for pattern-1, Time to collision (TTC), and for pattern-2 both TTC and Post Encroachment Time (PET) were showing required importance. Further, Import Vector Machine (IVM) approach was used to classify the severity levels based on selected indicators computed from 1486 events, occurring at three Un-Signalized intersections in India. The proposed severity levels will help to test and evaluate various infrastructure and control improvements for making urban intersections safe for road users. It was observed from the severity levels of both the patterns that, events involving non-evasive behavior can also result in critical interaction. Overall, the research provides an advanced framework for evaluating and improving the safety of the uncontrolled intersections.


## 1. Introduction

Pedestrian and cyclists are the most vulnerable road user as they account for 26\% of the total road accident related fatalities in World (WHO, 2018; Jain and Rastogi, 2016). In India, 13.8\% of total road accident fatalities in 2017 have been reported to be pedestrians (MORTH, 2017), this account to a total number of 20,457 fatalities. The pedestrian safety becomes more critical when the traffic is heterogeneous in nature like in India, where different categories of vehicles share the same road space without any segregation or lane following. Therefore, it becomes essential to carry out safety analysis at different types of road facilities for proposing measure to reduce accidents.

The conventional methods of road safety analysis in India are based on the occurrence of accidents given in police First Information Reports (FIR). The level of reporting in these records is basic and cannot be used for advanced safety analysis. Analyzing pedestrian safety based on limited quality and quantity collision data will not give accurate results. Therefore, the importance of using surrogated safety measures (SSM) is now the need of the hour for a developing country like India, where high-quality accident data is not readily available. Before applying SSM for safety analysis, the first question that comes to mind is that, which indicators should be used? Alternatively, whether to use the selected indicator individually or in aggregation. There is a list of indicators present in literature like the Time to Collision (TTC), Deceleration to Safety Time (DST), Post Encroachment Time (PET), Gap Time(GT), Time to Accident (TA) and Conflicting Speed (CS). Selecting the best indicator to represent evasive actions of the road users is important for the pedestrian safety analysis. The second question is that how these indicators can be estimated, using conventional grid-based estimation presented in literature is time-consuming and less accurate because of the more chances of human error that are involved in the estimation. The third important question is that which interaction needs to be studied i.e. there are few interactions that might involve evasive action of road user whereas some interaction which despite being severe, might not involve any evasive action. The term 'evasive action' means the action performed by any road user to avoid a collision. This action can be like changing path while crossing or increasing/decreasing speed to avoid a collision. Finally, using the selected indicator and

[^0]appropriate interaction, the severity levels suitable for mixed traffic condition needs to be computed.

The advancement in video processing software's has made it possible to apply automated conflict analysis to pedestrian safety analysis using SSM. Researchers (Ismail et al., 2009, 2010; Kaparias et al., 2010; Laureshyn et al., 2010; Salamati et al., 2011; Ren et al., 2012; Ni et al., 2016) have demonstrated the use of trajectory based data for computing various SSM for vehicle-vehicle and pedestrian-vehicle interaction. In terms of interactions, the pedestrian-vehicle interactions are of high inequality because the pedestrian move on slow speed and are capable of stopping and accelerating quickly compared to vehicle-vehicle interaction (Vanderhost and Kraay 1986). Complexities in analyzing pedestrian and vehicle interactions, especially when interactions are under heterogeneous traffic conditions, making it difficult to use the available conflict indicators in the same way. Hence, there is a need to revise the way by which the available indicators are computed such that it fits in for countries where the traffic movement is not lane based but heterogeneous. Therefore, the present study aims at evaluating pedestrian-vehicle interaction behavior using semi-automated safety diagnosis. The trajectory data will be used to analyze the road user behaviour and pedestrian interaction with different types of vehicles moving under heterogeneous traffic condition. For understanding the road user behaviour two pattern approach is proposed in the study. The patterns are based on continuous conflict indicators. After the pattern analysis, the selected conflict indicators are categorized into different severity levels viz., safe passage, critical event and conflict.

## 2. Literature review

Traffic conflict Techniques (TCT) helps in evaluating the safety of the road facility based on surrogate safety measures (Ni et al., 2016). Conventional methods of evaluating safety were concerned with the occurrence of accidents and their consequences. There are disadvantages in using accident data for road safety analysis and is discussed under various reports (Englund et al., 1998). Accidents are rare events and do not occur frequently therefore, surrogated measures were introduced to replace the conventional method of safety evaluation. The term conflict in TCT is a situation where two or more road users approach close to each other in time and space to such an extent that a collision is imminent if their movements remain unchanged (Svensson and Hyden, 2006). The definitions of various indicators along with type (continuous/ discrete) and important remarks are listed in Table 1.

There are two schools of thoughts in using SSM, the first is based on the Dutch TCT i.e. DOCTOR (Dutch Objective Conflict Technique for Operation and Research) developed by Institute of Road Safety Research in the Netherlands (Vanderhorst and Kraay 1986), a probability of collision by Dutch TCT's is determined by TTC and PET. The second is the Swedish school of thought, which implies TCT based on TA and CS (Svensson and Hyden, 2006). As per its definition, 'TA' might seem similar to TTC, but TTC is a continuous estimation of time to collision, whereas TA is a discrete value time. A study by Svensson and Hyden (2006) reports that all these measures have either been validated by using actual accident data or by an error in observation of the observers. Svensson and Hyden (2006) used surrogate measures (TA and CS) to evaluate the safety of both signalized and un-signalized intersection under homogeneous traffic conditions. Few studies (Kadali and Vedagiri, 2016; Koh et al., 2014; Tapiro et al., 2018; Huang et al., 2018) presented proactive approaches to evaluate pedestrian safety at different road facilities like mid-block crosswalk and signalized pedestrian crossing. Liu et al. (2017) developed a quantitative model of driver's risk perception for the crossing processes between two straight moving vehicles from the orthogonal direction for an un-signalized intersection. The model was based on cognitive psychology theory and an adaptive neuro-fuzzy inference system. In a motion tracking study, Aurell and Djehiche (2018) modelled the motion of tagged pedestrian, providing a tool for the positioning firefighters in a pedestrian environment. Bode et al. (2019) studied interactions between pedestrian streams that arise when pedestrian walk into and through four-way intersections from different directions. Ni et al. (2016) introduced a pattern-based approach by extracting 1144 events of pedestrian-vehicle interactions from a video of 3 intersections. The severity levels were then computed using the Support Vector Machine (SVM) technique.

Video data based trajectories provide a permanent, verifiable account of road user behavior (Ismail et al., 2009). The accurate estimation of exposure as well as other quantities fundamental to road safety analysis, e.g., severity of a traffic interaction, can significantly benefit by analyzing road users' positions in space and time, i.e., trajectories (Ismail et al., 2009). However, despite the research on pedestrian conflict analysis, there are still some gaps in research. Few studies have demonstrated the use video data for SSM estimation using conventional grid analysis (Shekhar Babu and Vedagiri, 2016 and Killi and Vedagiri, 2014), but analyzing pedestrian interactions using automated trajectory with different types of vehicle, having varying widths and moving under heterogeneous traffic condition is still a potential gap. Using severity levels developed under homogenous traffic condition for heterogeneous traffic condition might give erroneous results because of altogether different road user behavior in both the conditions. Also, unlike the conventional process of estimating conflict indicators to understand pedestrian-vehicle interaction dynamics, this paper uses a pattern-based approach, which will be able to represent user behavioral features. Further, based on both sophisticated approach of pattern analysis and indicators, it is essential to categorize events into the safe passage, critical event, and a conflict.

Table 1
Definition of TCT Indicators.
| Indicator | Definition | Type of Indicator | Remarks |
| :--- | :--- | :--- | :--- |
| Time to Collision (TTC) | The time until two road users collide if they continue at their present speed and along the same paths (Hayward, 1971) | A continuous measure of time | Needs trajectory data for its computation making it time-consuming if done using conventional video grid-based analysis |
| Deceleration to Safety Time (DST) | Deceleration required so that a second road user reaches the conflict point no earlier than when the first user leaves it (Hupfer, 1997) | A continuous measure of time | Needs trajectory data for its computation |
| Post Encroachment Time (PET) | It is the time between the first road user leaving a common spatial zone and the second user arriving in that zone (Allen et al., 1977) | Discrete value of time | It is a measure of time after the first vehicle has already crossed the conflict zone |
| Gap Time (GT) | It is the time difference between the second user arriving at the conflict point after the first user leaves it when both continue at the same speed and along the same paths (Vogel, 2002) | A continuous measure of time | Needs trajectory data for its computation making it time-consuming if done using conventional video grid-based analysis |
| Time to Accident (TA) | The time that remains to an accident from the moment that one of the road users starts an evasive action if they had continued with changed speeds and directions (Liu et al., 2017) | Discrete value of time | It is related to evasive action of the road users |
| Conflicting Speed (CS) | It is the speed of the road user taking evasive action, for whom the TA value is estimated, at the moment just before the start of evasive action (Bode et al., 2019) | Discrete value of time | It is related to evasive action of the road users |


## 3. Study approach

In the past, road accident data and SSM have been extensively used by the researchers to investigate and evaluate the safety of various road facilities. The present study considers the use of pattern-based approach using trajectory data to analyze the pedestrian-vehicle interaction behavior. The interaction behavior will depend on the road user, which crosses the conflict zone first, given as under:

a) When a vehicle passes first, any of the following behavior can be observed
b) Pedestrian withdraws, slows down or stops until the vehicle passes
c) A pedestrian might change the path and move to the end of a vehicle
d) Vehicle may accelerate and pass the conflict zone before a pedestrian arrives
e) When pedestrian passes first, any of the following behavior can be observed
f) Vehicle brakes stop or change the path
g) Pedestrian accelerates and passes the conflict zone before a vehicle arrives

The above behavior, along with the evasive action taken by any of the road users will be studied in detail using the trajectory data. The present study will categorize the interaction events into patterns with each pattern category showing specific road user behavior. The pattern is computed based on the profiles of the continuous SSM as listed in Table 1. Fig. 1 illustrates, that SSM indicators like TTC, GT, Speed, and PET were selected for this study.

The explanation pertaining to the selection of the indicators is present in the subsequent section. TTC, Speed, and GT being continuous indicators helped in categorizing events into different patterns. Whereas, minimum values of TTC, GT, and PET were used to get severity dimensions to evaluate the safety of the un-signalized intersection. The events will also be evaluated by six trained observers manually to compare it with trajectory based data. Finally, different conflict severity index levels will be proposed in this research. It is important to note that in the present paper conflict severity means nothing but the conflict probability i.e. a probability of a conflict becoming a crash and is represented by TCT indicators (Alhajyaseen, 2015; Alhajyaseen et al., 2012). Fig. 1 illustrates a brief methodology of the study; the different steps of the methodology are explained in detail in the subsequent sections.

## 4. Data acquisition

In the present study, videography data acquisition was carried out at four intersections in Navi Mumbai and Nagpur city, India: J.A. Shankaracharya Road - Seawod Road, Krishna Naik Road - Ramesh SH Road and Tekdi Road-NH6. Video cameras were installed on a height to capture the desired crosswalks of the intersection on which the interactions were supposed to be analyzed. More than one camera was installed to capture the road user interaction on different crosswalks of the intersections. Information on each intersection, including vehicle and pedestrian volume information, is listed in Table 2. The four intersections considered in the study are un-signalized, out of which three intersections were used to develop the study framework, and the fourth intersection was used to apply the proposed framework.

The study considers pairwise interaction, i.e., the interaction involving only one pedestrian and one vehicle were analyzed in the study. For analyzing the interactions, road users must be detected from the video (frame by frame). Doing this is a very challenging task, specifically when vehicles are moving under mixed traffic conditions with no lane following. In addition to the specific problem in tracking road users, some other common problems are proper illumination, tracking

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-03.jpg?height=1143&width=1094&top_left_y=1391&top_left_x=487)
Fig. 1. Proposed brief methodology of the study.

Table 2
Information for observed intersection.
| S.No. | 1 | 2 | 3 | 4 |
| :--- | :--- | :--- | :--- | :--- |
| Intersection | JA Shankaracharya Rd - Seawod Rd (Navi Mumbai) | Krishna Naik Rd - Ramesh SH Rd (Navi Mumbai) | Tekdi Rd.- NH6 (Nagpur) | Sector 19 Rd- GP Road (Navi Mumbai) |
| Crosswalk for observation Marked in red | ![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-04.jpg?height=200&width=318&top_left_y=406&top_left_x=395) | ![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-04.jpg?height=226&width=339&top_left_y=406&top_left_x=794) | ![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-04.jpg?height=215&width=347&top_left_y=406&top_left_x=1208) | ![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-04.jpg?height=231&width=299&top_left_y=404&top_left_x=1580) |
| Video collection duration | 120 min | 120 min | 120 min | 90 min |
| Pedestrian volume at each crosswalk | Arm 1-357 ped/h <br> Arm 2-443 ped/h <br> Arm 3-394 ped/h | Arm 1-321 ped/h <br> Arm 2-196 ped/h <br> Arm 3-392 ped/h <br> Arm 4-382 ped/h | Arm 1-273 ped/h <br> Arm 2-313 ped/h <br> Arm 3-310 ped/h | Arm 1-212 ped/h <br> Arm 2-298 ped/h <br> Arm 3-302 ped/h |
| Road Facility <br> Right-turning volume for selected approach | Un-signalized 3 arm Intersection <br> Arm 2 to 1-322 veh/h <br> Arm 3 to 2-387 veh/h | Un-signalized 4 arm Intersection <br> Arm 1 to 4-449 veh/h <br> Arm 2 to 1-326 veh/h <br> Arm 3 to 2-315 veh/h <br> Arm 4 to 3-412 veh/h | Un-signalized 3 arm Intersection <br> Arm 2 to 1-296 veh/h <br> Arm 3 to 2-306 veh/h | Un-signalized 4 arm Intersection <br> Arm 1 to 4-409 veh/h <br> Arm 2 to 1-312 veh/h <br> Arm 3 to 2-291 veh/h <br> Arm 4 to 3-198 veh/h |
| Left-turning volume for selected approach | Arm 1 to 2-231veh/h | Arm 1 to 2-254 veh/h | Arm 1 to 2-190 veh/h | Arm 1 to 2-181 veh/h |
|  | Arm 2 to 3-239 veh/h | Arm 2 to 3-261 veh/h <br> Arm 3 to 4-297 veh/h <br> Arm 4 to 1-288 veh/h | Arm 2 to 3-286 veh/h | Arm 2 to 3-232 veh/h <br> Arm 3 to 4-246 veh/h <br> Arm 4 to 1-176 veh/h |


of multiple objects, and handling shadows of the road users. The authors' extracted data using various automatic tracking software but the level of tracking accuracy was low.

In order to overcome multiple object tracking problem, the present paper used semi-automated tracking software, i.e. Kinovea 8.26 (Kinovea, 2019), which is a tool that provides an acceptable level of accuracy in angular and linear measurements obtained via the digitization of x- and y-axis coordinates (Landis and Koch, 1977). It is an open source video processing software, which is commonly used for sports analysis requiring the highest level of accuracy, e.g. tracking a cricket ball and estimating its speed by which the bowler has bowled. Diví et al. (2017) carried out a study to estimate the reliability of this software in obtaining distance dimensions, to evaluate Kinovea reliability and validity a multiple approaches were applied involving the following analysis: -systematic error with a two-way ANOVA 2 × 4; -relative reliability with ICC and CV (95\% confidence interval); -absolute reliability with Standard Error. The results indicated that it is a reliable tool in both distance measurement and trajectory-based analysis (Landis and Koch, 1977). Considering its high performance in sport analysis this tracking software was therefore used in the present study to obtain trajectory data of the road users.

The interactions were studied using trajectory data for the mixed traffic condition with no lane following behaviour. Trajectory-based data acquisition includes the following steps:

- Adjusting frames: The video was captured at 30 frames per minutes and was imported in a motion tracking software i.e., Kinovea 8.26 (Kinovea, 2019). The video was configured with software by adjusting it for 30 frames per minute using camera speed command.
- Coordinate Transformation: The coordinate transformation was done using the homography matrix, Fig. 2 presents a snaphot to show how coordinate transformation was carried out in the Kinovea software.
- Tracking Workflow: The desired vehicle and pedestrian were selected using track path option to frame by frame track both the road users.

The tracking in Kinovea is semi-automatic because the user can correct the track point location using outer rectangle, whenever the automatic tracking fails to track the actual path. Control over the track is required because sometimes the object being tracked is not well contrasted and feature rich therefore, it might result in an incorrect track path. It usually happens when pedestrians are being tracked. The dynamic rectangles i.e. feature region and search region recognizes the tiny pedestrians because of its movement over the static background and also because of the colour contrast. But this is only possible if the video is recorded at 1080 P and at 30 frames per second.

Also, wherever one camera could not capture the entire intersection, two cameras were used to observe the interactions at the crosswalks. In the software one frame is compared with the other frame pixel by pixel, places, where differences are detected, are classified as moving objects no matter how tiny they are. Fig. 3 presents the steps followed by the software to detect a moving object.

- Exporting data to Spreadsheet: Once the tracking of road user is complete, the software assists in exporting to an XML dialect which can be understood as a spreadsheet which includes key images (time and title), lines (length), cross-marker (coordinates) and path tracking trajectory.

The Trajectory profiles were analysed to estimate the continuous indicators i.e. TTC, GT and PET. This was done using video data of intersections which were analysed using semi-automated video image processing tool. The speed data from the video was obtained for every 0.03 s interval of time in order to generate the speed profiles for the entire interaction process. Trajectories that overlap in space during given intervals were recorded as an event, resulting in total 1486 events recorded at two intersections. A revised detailed calculation of TTC and GT is proposed in this paper because the previous definition given by Ni et al. (2016) does not consider the effect of vehicle width into its formulation. Since PET is a discrete indicator hence, no change in its calculation was proposed. The revised formulation to estimate TTC and GT considering effect of width of vehicle is as under:

### 4.1. Selection and calculation of surrogate safety indicators

It has been discussed in the literature that various conflict indicators

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-05.jpg?height=859&width=1260&top_left_y=196&top_left_x=405)
Fig. 2. Video calibration using the perspective grid.

(Dutch and Swedish) have been used in the past. Some studies either selected a single indicator, whereas others used the aggregation of indicators for analyzing the safety of road user interaction. Swedish indicators like TTC, GT, and PET, were commonly used for studying both vehicle-vehicle and pedestrian-vehicle interaction, whereas various other indicators were majorly used to study vehicle- vehicle interaction. Two more indicators, i.e. Dutch indicators like TA and speed, were also used in analyzing the pedestrian-vehicle interaction. TA, as already

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-05.jpg?height=1186&width=1266&top_left_y=1348&top_left_x=400)
Fig. 3. Steps to explain Road User Tracking.

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-06.jpg?height=562&width=846&top_left_y=192&top_left_x=142)
Fig. 4. Schematic diagram to show vehicle pedestrian interaction for estimating TTC and GT.

explained in the literature, is a discrete value of the continuous TTC profile just before the start of evasive action. Hence, the present study used the continuous indicator TTC rather than TA to get the profile of the entire interaction process. Based on understanding mentioned above, finally, the present study selected the four surrogate safety indicators viz., speed, TTC, GT, and PET to categorize the road user interaction. Speed was used to categorize events into patterns (explained below) whereas the TTC, GT, and PET to study the severity level. The calculation of the indicators can be seen below: The $d v(i)$ is the distance from the front of the vehicle to the conflicting zone which is also extrapolated outline of the conflicting pedestrian at time ' $i$ '. The $d p(i)$ is the distance from the front of the pedestrian to the conflicting zone or in other words, the extrapolated outline of the conflicting vehicle at the time ' $i$ '. Length and width of the conflicting vehicle are given by $l(j)$ and $w(j)$ respectively, Where ' $j$ ' is the vehicle type like a car, two wheeler, three-wheelers, bus, light commercial vehicles etc. Speed of vehicle and pedestrian at time ' $i$ ' is given by $v v(i)$ and $v p(i)$ respectively. Fig. 4 illustrates the aforementioned variables using a schematic diagram with the dark portion showing the conflict zone

To estimate any of the indicators, two scenarios are considered, the scenario -1, when the pedestrian passes first and scenario-2, when the vehicle passes first (all the indicators are estimated in seconds). The calculation of TTC, GT, and PET are as follows:

### 4.1.1. Time to collision (TTC)

A modification in the calculation of TTC was proposed in the present study. It can be observed from the numerator of Eq. 1 that a factor ' $w(j)$ ' is being considered to cater to the different widths of the vehicles. Considering the concept of varying widths is important to study pedestrian interaction with different categories of vehicles. The previous studies have presented pedestrian-vehicle interaction with only one category of vehicle, i.e. car. In the present study, along with the pedestrian-car interaction, other combinations of pedestrian-vehicle interactions were also studied. Hence, this study incorporates the effect of vehicle type. With the change in the type of vehicle the width of the conflict zone increases or decreases, this effects the TTC estimation when the pedestrian crosses the conflict zone first as shown in Eq. 1, same is true with GT estimation.

$$
\text { When pedestrian passes first, } T T C(i)=\max \left(\frac{d_{p}(i)+w(j)}{v_{p}(i)}, \frac{d_{v}(i)}{v_{v}(i)}\right)
$$

In Eq. 1, the reason for using term maximum instead of a minimum can be explained with the help of example showing two-time instances:

Fig. 5 presents an interaction happening between car and pedestrian at two instance of time i.e. ' $i$ ' and ' $j$ '. At time instance ' $i$ ' the TTC is 4 s Time Instance 'i'

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-06.jpg?height=295&width=510&top_left_y=235&top_left_x=1395)
Time instance ' $j$ '

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-06.jpg?height=250&width=538&top_left_y=633&top_left_x=1382)
Fig. 5. Example showing TTC estimation.

(max $(4,2)$ ) and at time instance ' $j$ ' the TTC is 2.5 s (max(2.5,0)). Suppose if the term 'max' is removed from the Eq. 1 and TTC is calculated based on pedestrian (considering Pedestrian crosses first), then the TTC would be calculated as 0 s, at time instance ' $j$ ', which means collision has occurred, but actually the collision is avoided by 2.5 s as observed in instance ' $j$ '.

Therefore, using the term 'max' in Eq. 1 is essential. Also, it helps in getting a clear $\mathrm{TTC}_{\text {min }}$ as can be observed in the graph shown in Fig. 6(a). Similar is the case in Eq. 2

$$
\text { When vehicle passes first, } T T C(i)=\max \left(\frac{d_{p}(i)}{v_{p}(i)}, \frac{d_{v}(i)}{v_{v}(i)}\right)
$$

Eq. 2 will give continuous data of TTC
$\mathrm{TTC}_{\text {min }}=\min (\mathrm{TTC}(\mathrm{i}))$
The TTC is continually calculated between conflicting vehicles and pedestrian, and thus, a set of values is returned for each conflict. The $\mathrm{TTC}_{\text {min }}(\mathrm{s})$, is extracted from this set to indicate the maximum severity of this interaction.

### 4.1.2. Gap time (GT)

$$
\text { When pedestrian passes first, } G T(i)=\left|\frac{d_{p}(i)+w(j)}{v_{p}(i)}-\frac{d_{v}(i)}{v_{v}(i)}\right|
$$

$$
\text { When vehicle passes first } G T(i)=\left|\frac{d_{p}(i)}{v_{p}(i)}-\frac{d_{v}(i)+l(j)}{v_{v}(i)}\right|
$$

$$
\mathrm{GT}_{\min }=\min (\mathrm{GT}(\mathrm{i}))
$$

The GT is also a continually calculated between conflicting vehicles and pedestrian, and thus, a set of values is returned for each conflict. The $\mathrm{GT}_{\text {min }}(\mathrm{s})$, is extracted from this set to indicate the maximum severity of this interaction.

### 4.1.3. Post encroachment time (PET)

Given Tv1 and Tv2 is the time when vehicle enters and leaves the conflict zone respectively, Tp1 and Tp2 are the time when the pedestrian enters and leaves the conflict zone respectively. The two scenarios of PET are as under:

$$
\text { If vehicle passes first,PET }=T_{p 1}-T_{v 2}
$$

$$
\text { If pedestrian passes first,PET }=T_{v 1}-T_{p 2}
$$

Eqs. 5 and 6 will get more clear by the schematic diagram presented in Fig. 6(a) and (b) respectively.

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-07.jpg?height=646&width=1275&top_left_y=189&top_left_x=396)
Fig. 6. Schematic diagram a) vehicle passes first, b) pedestrian passes first.

Below is an example showing how the traffic conflict indicators like TTC, GT, and PET were extracted from the video data. For e.g. The event presented in Fig. 7(b) can be observed as an interaction of car with a pedestrian. The interaction process starts from t1, at this point pedestrian observes the incoming vehicle and starts to decelerate and hence both the TTC and GT starts decreasing.

At $\mathrm{t}_{2}$, the pedestrian and vehicle are approaching more close to each other therefore, TTC is further reduced until GT reaches a minimum value at $\mathrm{t}_{3}$, TTC reaches the minimum value just after a $\delta t$ time late than $\mathrm{t}_{3}$. The vehicle arrived at the conflict point between $\mathrm{t}_{3}$ and $\mathrm{t}_{4}$ while pedestrian adjusted his speed and passed the conflict point as soon as the vehicle cleared it. The value of $\mathrm{TTC}_{\text {min }}$ and PET for the above event were 1.1 s and 2.5 s.

### 4.2 Estimating accuracy of trajectory software

Once the road users were identified, the first parameter of interest was the vehicle and pedestrian speed. Many studies have used Mean Relative Error (MRE) to quantify the error of video speed extraction from the trajectory data. The vehicle speed validation process begins by plotting automatically extracted speeds against manually measured speeds (speeds calculated based on known distances and video frame rate) in order to observe trends. The line $y=x$ represents ideal software performance, and data points above the line indicate overestimation of speed, while points below the line indicate underestimation. As the overestimation bias is typically constant, a line with slope equal to one is fitted to the data (Fig. 8).

The y-intercept and R-squared values of this fitted line represent accuracy and precision, respectively. However, converting these results to relative error values matches the approach utilized in existing literature. The Mean Relative Error can be estimated by Eq. 7

$$
\text { Mean Relative Error }(M R E)=\frac{1}{100} \sum \frac{\left|V_{e}-V_{o}\right|}{V_{o}}
$$

Where $\mathrm{V}_{\mathrm{e}}$ and $\mathrm{V}_{\mathrm{o}}$ stand for the automatically extracted and manually measured speeds, respectively. Fu et al. (2017) reported that MRE is insufficient at capturing the true behaviour of software in terms of the precision of software. To understand clearly, the software accuracy is its error or bias and precision is the residual error. The Relative Precision Error can be estimated as given in Eq. 8.

$$
\text { Relative Precision Error }(R P E)=\frac{1}{100} \sum \frac{\mid\left(V_{e}-y \text { intercept }\right)-V_{o} \mid}{V_{o}}
$$

Further, the relative accuracy error (RAE) is estimated to present over or underestimation bias in video data. The RAE is estimated as given in Eq 9

$$
\text { Relative Accuracy Error }(\text { RAE })=\frac{1}{100} \sum \frac{\mid y \text { intercept } \mid}{V_{o}}
$$

To estimate the accuracy of Kinovea software, Fig. 8 shows a plot between extracted speed and the actual speed. The MRE, RPE and RAE were computed as $3.9 \%, 4.1 \%$ and $2.7 \%$ respectively showing a high accuracy of the extracted data (Fu et al., 2017).

## 5. Analyzing evasive action

As per the definition of the evasive action, the road user behavior can be termed as an evasive action when either change is speed or change in the path for road user is observed. Therefore, the preset section presents changing path analysis to observe any change in the path of the crossing pedestrian (before the collision zone) and pattern analysis to observe the change in speeds and patterns of TTC \& GT. Using both the changing path behaviour and the change in speed, the interaction patterns were categorized into pattern 1 and pattern 2.

### 5.1. Changing path analysis

Two types of changes in paths were observed for pedestrians, the first for avoiding collision (evasive behaviour) and second to reduce travel distance. The first type of the change in the path was observed before the collision zone and second after the collision zone. Any change in the path of a pedestrian after the collision zone, was not of interest, as it does not present an evasive behaviour until the pedestrian is encountered by a second approaching vehicle. The change in the path was categorized based on lateral deviation estimated from the trajectory data. To start with, first, the maximum lateral deviation (LD) was observed for all non-evasive interactions of the pedestrian (i.e., for normal behavior). Fig. 9(a) presents the estimation of lateral deviation based on the assumption that the ideal path of the pedestrian is the perpendicular path from the starting point when the pedestrian decision for crossing is made. The LD is estimated as $x_{2}-x_{1}$ shown in Fig. 9(a). The $85^{\text {th }}$ percentile of the maximum lateral deviations was estimated (Fig. 9). Based on the $85^{\text {th }}$ percentile LD value, the interactions were categorized into patterns. When the maximum LD for a pedestrian path in an interaction was more than 1.34 m (Fig. 9(b)), then it was considered in pattern 1 else pattern 2. The definitions of pattern 1 and 2 can be observed in the subsequent section.

### 5.2. Pattern analysis

The word 'pattern' in this section means the profile of the continuous Traffic Conflict Technique indicators w.r.t to time, as shown in

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-08.jpg?height=1787&width=1527&top_left_y=187&top_left_x=269)
Fig. 7. Example of interaction and profile of continuous indicators.

Fig. 10. As explained in Fig. 10(a), the patterns of pedestrian interaction with the different classification of the vehicles were plotted to observe any significant differences in the profile of indicators with a change in the type of vehicle (Fig. 10). Fig. 10 is a sample showing individual pedestrian interaction with different categories of the vehicle for the scenario when the pedestrian passes first. The patterns were categorized into two types based on the similarity in shape of indicator profile and the occurrence of the evasive action. As already explained, the term 'evasive action' means the action performed by any road user to avoid a collision. This action can be like changing path while crossing and/or increasing/decreasing speed to avoid the collision.

The details of pattern 1 and 2 can be observed as under:
Pattern 1: When either pedestrian or vehicle or both take an evasive action (observed by speed profile)

Pattern 2: When neither pedestrian nor vehicle takes an evasive action

Mathematically, the patterns were classified based on Eq. 10, which would be discussed later in this section. Pattern 1 deals with the responsive behaviour of the road user (involving evasive action) and pattern 2 consider the normal road user behaviour (with no evasive action). The normal road user behavior is considered in present study to prove the hypothesis that even non-evasive events can lead to critical interactions. To know if a road user is taking evasive action, speed profiles of road users involved in interaction were plotted. Fig. 10 illustrates sample speed profiles, TTC and GT plots to understand the shape of patterns for pedestrian interaction with different categories of vehicle. TTC and GT are continuous indicators and reflect different aspects of interaction, TTC represents proximity to collision point and

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-09.jpg?height=532&width=633&top_left_y=196&top_left_x=250)
Fig. 8. Relationship between extracted and actual speed.

GT represents temporal closeness. Fig. 10 illustrates the profiles of speed, TTC and GT when pedestrian passes first.

On observing the speed profile in pattern 1 as shown in Fig. 10(b), it can be clearly comprehended that either or both the road users take significant evasive action. This can be confirmed because the speed profiles are not constant, the vehicle speed is decreasing with time, and pedestrian speed is increasing with time, the opposite might also happen if the vehicle passes the conflict zone first. Therefore, we can call the pattern a hard interaction because an evasive action is involved in the interaction falling under this pattern. On observing the profile of TTC and GT in Fig. 10(a), it can be comprehended that the pedestrian interaction with different types of vehicle is resulting in almost similar kind of profile shape. Both the minimum TTC and minimum GT appears in the middle or end of the interactive process. Further, it can be comprehended from the speed profile of pattern 2 (Fig. 10(d)) that neither the pedestrian nor the vehicle was taking any evasive action, as the speed profile is almost horizontal to the time axis. However, slight fluctuations in the speed profiles were observed showing that the road users adjust their speeds; this might be related to adjustments made by the road users to manoeuver with ease. Therefore, this pattern can be said having soft or no interaction. It was observed in this pattern that TTC and GT were showing different trends, and the same was common for pedestrian interaction with a different type of vehicle.

Separating interaction in pattern 1 and 2 visually based on speed profiles is a tedious job therefore; interaction patterns can be recognized according to the time when either the $\mathrm{TTC}_{\text {min }}$ or $\mathrm{GT}_{\text {min }}$ will occur. It can be observed in pattern 1 (Fig. 10(a)) that $\mathrm{TTC}_{\text {min }}$ and min $\mathrm{GT}_{\text {min }}$ were occurring simultaneously (either in end or middle of process) for all categories of vehicle. However, the same was not true for pattern 2. In pattern 2 a clear distinction can be observed in the occurrence of $\mathrm{TTC}_{\text {min }}$ and $\mathrm{GT}_{\text {min }}$. This discrepancy in time of occurrence of $\mathrm{TTC}_{\text {min }}$ and $\mathrm{GT}_{\text {min }}$ was attempted to be demonstrated in a mathematical form. To do so, it was assumed that if the interaction starts at time $T_{o}$ then the two parties will arrive at the conflict zone at time $T_{1}$ and $T_{2}$ respectively. $T_{1}$ therefore is the time when the first road user reaches the conflict zone (can be pedestrian or vehicle), $T_{2}$ is the time when the second road user reaches the conflict zone (can be pedestrian or vehicle) Also, $t_{a}$ and $t_{b}$ are the time when TTC and GT are minimum and $\delta t$ is a time difference between $\mathrm{TTC}_{\text {min }}$ and $\mathrm{GT}_{\text {min }}$. Therefore, in an easy way it can be computed that an event belongs to Pattern 1 if the Eq. 10 is satisfied or else it is pattern 2.

$$
\text { if } t_{b}=t_{a} \pm \delta t, t_{a}, t_{b} \in\left(T_{0}, T_{1}\right)
$$

Based on Equation 7, 1486 events were categorized into two patterns, as illustrated in Table 3. It can be observed from Table 3 that interaction in which the vehicle involved is either a bus or LCV are categorized as pattern 1, the one major reason of this is the larger size and width of vehicles, which psychologically forces the pedestrian to take evasive action.

On the contrary, the pedestrian interactions with two-wheelers are majorly categorized in pattern 2 . The variation in the composition of interaction pattern may also vary with intersection location, geometry and road user characteristics such as age gender, and their familiarity with the surroundings. The pattern analysis presented in this section helps only in categorizing the interaction events based on road user evasive action. But, the paper still has not discussed the severity of the individual events. Therefore, the next section talks about severity level classification to analyze and comment about the individual event's severity.

## 6. Indicator based severity level classification

Due to the high dimensionality of the TTC and PET data; import vector machine (IVM) approach was used in the present study for severity level classification. Although support vector machine (SVM) is commonly known for its good performance in classification, a comparatively newer approach of classification, i.e. IVM has been reported performing better than SVM for both binary class and multi-class cases (Ji and Trevor, 2005). The IVM uses the import data that is similar to support data in SVM, but the only difference is that IVM model uses only a fraction of training data to index kernel basis function which is a much smaller fraction than the SVM. This, therefore, gives a computational edge to IVM over SVM. The basic algorithm of the IVM is

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-09.jpg?height=661&width=1272&top_left_y=1878&top_left_x=398)
Fig. 9. Pedestrian path changing behavior.

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-10.jpg?height=1113&width=1520&top_left_y=192&top_left_x=273)
Fig. 10. Speed profiles and TTC-GT profiles (when pedestrian passes first).

Table 3
Observed pedestrian-vehicle interaction patterns.
| Vehicle Involved | Pattern -1 | Pattern- 2 |
| :--- | :--- | :--- |
| Car | 397 | 234 |
| Two-wheeler | 200 | 354 |
| Three-wheeler | 98 | 39 |
| LCV | 117 | 15 |
| Bus | 29 | 3 |
| Total | 841 (57\%) | 645 (43\%) |


explained in brief in Appendix A. Once the classification of data was done using IVM. The performance of the classifications was evaluated by the K-fold cross-validation. In this cross-validation algorithm, data is split into k folds, the training data set is k-1 fold, and testing is the last one. This is repeated k times and in the end, prediction for the whole data set is done. In the present case $\mathrm{k}=4$, the 1486 events were randomly stratified into the four folds that are equal in size. Out of the four folds, three folds were used as the training data and the last one as testing dataset. The goal of the k-fold cross-validation approach is to compute test error on the held out points in classification. The computed averaged test errors are presented in Fig. 11(a). It was observed that the average errors are ranging between 17\% to 24\% which clearly satisfies the accuracy requirement of classification (Wong, 2015). After k fold test, the variable importance is analyzed by standardizing the analysis between 0 and 1 as presented in Fig. 11(b). It can be observed from Fig. 11(b) that, for Pattern 1 TTC was showing more importance than PET, whereas for Pattern 2, both TTC and PET were showing approximately similar kind of importance.

IVM Classification based on the patterns and selected indicators

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-10.jpg?height=556&width=1511&top_left_y=1985&top_left_x=280)
Fig. 11. a) Pattern based test error b) variable importance analysis.

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-11.jpg?height=607&width=1516&top_left_y=189&top_left_x=276)
Fig. 12. Severity dimension composition evaluated by trained observers.

1 For pattern 1, $\mathrm{TTC}_{\text {min }}$ was adopted as an indicator. The event was a safe passage if $\mathrm{TTC}_{\text {min }}>2.5 \mathrm{~s}$, mild interaction if $1.2 \mathrm{~s}>\mathrm{TTC}_{\text {min }} \leqslant$ 2.5 s and a critical interaction if $\mathrm{TTC}_{\text {min }}<1.2 \mathrm{~s}$
2 For Pattern 2, both $\mathrm{TTC}_{\text {min }}$ and PET were adopted as an indicator. The event was a safe passage if $\mathrm{TTC}_{\text {min }}>2.3 \mathrm{~s}$ and PET $>2.6 \mathrm{~s}$ and a critical interaction when $\mathrm{TTC}_{\text {min }}<1.3 \mathrm{~s}$ and PET $<1 \mathrm{~s}$. Otherwise, it is a mild interaction.

On comparing the TTC based severity levels of pattern 1 and pattern 2, it was observed that the computed levels were very close. E.g. an event in pattern 1 can be called as a critical interaction if $\mathrm{TTC}_{\text {min }}<1.2 \mathrm{~s}$, whereas an event in pattern 2 can be called as a critical event if $\mathrm{TTC}_{\text {min }}<1.3 \mathrm{~s}$ (along with PET $<1 \mathrm{~s}$ ). A normal question that comes to mind after looking at these two values is that, if the severity levels are so close (1.2 s and 1.3 s) then what is the need of putting it into two different patterns. The reason for dealing with two patterns separately was to provide evidence that the interactions involving nonevasive behavior (presented under pattern 2) can also lead to critical interactions. The targeted traffic education to the users should, therefore, be decided based on studying the road user behavior in both the patterns separately.

### 6.1. Validating severity levels

Van der Horst and Kraay (1986) and Ni et al. (2016) used observer's rating based approaches for understanding traffic conflict and behaviour through video observations. The present study also adopts a similar approach to validate the severity levels computed using IVM approach. To accomplish the same, six observers were trained to evaluate 1486 interaction events by watching the site videos. The interactions were evaluated based on the following behavioral responses of the road users as under:

1 Pedestrian sees the vehicle coming and slows down or stops till the vehicle passes,
2 Pedestrian increases speed (accelerates) and crosses the conflict zone even before the vehicle arrives, also in some cases when a large-sized vehicle, i.e. buses were involved then the pedestrian changed the path by walking towards the end of the vehicle.
3 Vehicle driver sees the pedestrian and then brakes, stops or changes the path to avoid a collision, on the contrary in some events vehicle accelerates on observing a pedestrian and passes even before a pedestrian arrives at the conflict zone.
4 In some of the less often-occurring events, both parties i.e., pedestrian and vehicle take actions, and one party passes first after negotiation.
5 In some safe interactions, no road user takes evasive action, and one

Based on the behaviors mentioned above, the observers were asked to estimate the severity level of each interaction. The severity levels were categorized into three parts, safe passage, mild interaction, and critical interaction and were coded as 0, 1, and 2, respectively. Six observers were recruited to watch the same video clips and for extracting interaction features and for evaluating the event by estimating severity level. To test the agreement in the severity level estimation done by six observers, Fleiss Kappa statistics is used in the present paper. The Fleiss Kappa coefficient $(\kappa)$ measures the inter-related agreement of the observers (raters) for the qualitative or subjective items. This measure takes into account the possibility of the agreement occurring by chance. Step by step procedure of calculating Fleiss Kappa coefficient ( $\kappa$ ) can be observed in Annexure B, the ' $\kappa$ ' value in the present study was coming out to be 0.64 which can be interpreted as 'substantial agreement' as per the k-value table is given by Landis and Koch (Landis and Koch 1997). The resulted severity levels estimated by all observers were averaged out and rounded to integers between 0 and 2. Out of the total 1486 events, 563 were categorized as a safe passage, 756 as mild interactions, and 167 as critical events.

It can be observed from Fig. 12(a) that mild interactions (green dots) in pattern 1 are located in TTC range between 1 to 2.5 (demarcated by dotted lines) however, the PET was large and spread longitudinally.

The critical interactions (red dots) in pattern 1 were concentrated and located with a TTC < 1 and PET < 3. Less number of events were categorized as safe interaction in pattern 1. Meanwhile, for pattern 2 the events were more scattered, safe interaction in pattern 2 was observed to be more than that of pattern 1. It can be observed from Fig. 12(a) and (b) that for pattern 1 a clear classification can be observed based on TTC but for pattern 2 a clear classification can be observed considering both TTC and PET. These visual classifications are similar to the theoretical classifications and variable importance estimates carried out in previous section.

On comparing the results of theoretical classification of severity levels with the categorizations done by trained observers it can be comprehended that the accuracy of theoretical classification was high i.e. 88\% events were correctly estimated, 7\% were underestimated and 5\% were overestimated. Therefore, based on the sections above, it can be comprehended that the new framework proposed in the present paper is majorly based on the trajectory data extracted by processing the intersection videos.

Pair-wise interactions were recorded as an event, based on the continuous indicator profiles, the interaction pattern can be recognized and can be taken into consideration to select the indicators for evaluating the severity level of the facility type. Compared with the
conventional approaches, the present research is more sophisticated as it is based on semi-automated safety diagnosis tools.

## 7. Implementation

The proposed framework and methodology was subsequently implemented at the fourth intersection in Navi Mumbai India. Based on the 90 min of video, 190 events were extracted. The steps of implementation can be observed as under:

Step-1: For each event, the TTC and GT were estimated continuously during the interactive process, and the PET was available at the end of the process.

Step-2: The lateral deviation was estimated based on the tracking coordinates of the pedestrian. If the maximum lateral deviation in a crossing path before approaching conflict zone was more than 1.34 m then the interaction was categorized as pattern 1, else pattern-2

Step-3 Apart from the change in path analysis the pattern for TTC and GT were observed and based on Eq. 7; events were categorized into pattern 1 and pattern 2.

Step -4 The severity of the interactions under both the patterns were classified as safe passage mild interactions and critical interactions based on the IVM based classification given in Section 6.

Step-5 The probability of collision of pedestrian interaction with straight, left and right turning traffic was analysed.

Step-6 Similar to step 4, the probability of collision for pedestrian interactions with different categories of the vehicle was evaluated based on the given approach.

Fig. 13 presents the result comparison based on the TTC and PET. It can be observed from Fig. 13(a) the pedestrian interaction with the right turning traffic is the most critical whereas, on the other hand, the pedestrian interaction with the straight moving vehicle is the safest as can be observed by comparing the median values.

Similar to TTC min plot in Fig. 13(a), Fig. 13(b) presents a comparison of PET values of the pedestrian interaction with traffic approaching from different directions. The results based on the PET confirms the observations obtained from Fig. 13(a). Fig. 14 illustrates a comparison of pedestrian interaction with different categories of vehicles. It is clearly visible from the Fig. 14(a) that the pedestrian interaction with three-wheelers is most critical and the same was confirmed by Fig. 14(b). The critical interaction with 3 wheeler may be a result of the non-yielding behavior of this category of the vehicle. The safest pedestrian interactions were reported with car and bus.

Fig. 15 illustrates the pattern-wise severity levels obtained from the proposed IVM based classification for 190 interactions. It can be observed that the pattern 1 has the highest number of critical interactions which was evident from the evasive actions taken by road use in this pattern. On the other hand pattern 2, in which no evasive action was taken is still showing 19 percent of its events as critical interaction. The results from Fig. 15 supports to the previous claim made in this paper that the events which do not involve evasive action can also lead to critical interactions.

## 8. Discussion and conclusions

The present paper attempts to develop a framework for understanding the role of road user behaviour in pedestrian interaction with different types of vehicles. Doing this was possible by extracting information from the pedestrian-vehicle interaction trajectories. The research contributions and major findings of the study are explained as under:

- The study demonstrated the use of a semi-automated motion tracking software (Kinovea) for estimating SSM. In the past, it was used for sports analysis, i.e. for analyzing various games, which required trajectory data analysis. For e.g. to analyze a basketball shot, or a Javelin throw, trajectory data analysis is required. In the present study, this software helped in extracting trajectory based data semi-automatically; the data was extracted for both pedestrian and vehicle moving under heterogeneous traffic conditions. It also helped in increasing the accuracy, and quality of data for estimating SSM, because of its advantage in extracting road user coordinates after every 0.03 s interval of time. Achieving this accuracy was not possible by manual (grid based) methods demonstrated in conventional studies. Few precautions that needs to be taken before its use were also highlighted in the study. One important precaution was, that the video to be analyzed must be captured at 30 frames per second, and this was confirmed after trial and error. It was observed that the software tracks the road user to its best when the video is captured at 30 frames per second. By best, it means that tracking was smooth and least or no human action was required to correct it.
- The concept of two interaction patterns (pattern 1 and pattern2) proposed in this study, helped in segregating the responsive (involving evasive action) and non-responsive (not involving evasive action) behaviour of both the pedestrians and vehicles. Unlike the previous studies, the necessity of studying only those events, in which any of the road users takes evasive action was removed. Therefore, in the present study, all the interacting events were studied. Doing this was important to highlight that, critical interactions can also occur in events where neither the pedestrian nor the vehicle is taking any evasive action. The patterns were categorized using continuous SSM indicators like speed, TTC, and GT, which helped in analyzing the whole interactive process. A new formulation was

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-12.jpg?height=614&width=1268&top_left_y=1925&top_left_x=400)
Fig. 13. Comparison of pedestrian interaction with directional traffic.

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-13.jpg?height=624&width=1270&top_left_y=189&top_left_x=398)
Fig. 14. Comparison of pedestrian interaction with different categories of vehicles.

![](https://cdn.mathpix.com/cropped/53753396-bf9a-497d-aea1-05d0ec8379d9-13.jpg?height=708&width=754&top_left_y=904&top_left_x=189)
Fig. 15. Comparing pattern-wise severity levels.

proposed for estimating TTC and GT to consider the effect of the width of vehicle in interacting scenarios. Pattern 1 (involving evasive action) had more number of critical events because either the vehicle or pedestrian or sometimes both increase their speed for negotiating interaction. However, Pattern 2, though involving a non-evasive behavior of road user still had critical interactions because of the high risk-taking behavior, of the interacting users resulting in a riskier situation. Pattern 2 also helped in putting evidence that, just making infrastructural improvement is not sufficient to enhance the safety of a facility. But, feedback based on patterns will help in increasing safety by giving traffic education on proper road user behavior. Educating drivers about slowing down, yielding and telling pedestrians to be more attentive to the vehicles coming from behind and also by having good communication with the approaching vehicle are some of the important feedback that needs to be given.

- The severity level classification proposed in this study will help in evaluating the level of safety provided by various un-signalized intersections operating under heterogeneous traffic conditions. The severity levels were classified into three classifications viz., safe passage, mild interaction, and critical interaction. Any road safety stakeholder should always be concerned in reducing the events falling under critical and mild interaction and should make all possible efforts in making an event as a safe passage. This could beachieved by doing necessary road safety-related infrastructure improvements and providing feedback to road user on proper driving behavior.
- Out of three un-signalized intersections used in the present study, the Intersection-1 (JA Shankaracharya Rd - Seawod Rd) was showing a minimum number of critical interactions (21.5\% of total critical interactions in 1486 events), whereas the Intersection-3 (Tekdi Rd.- NH6) was showing a maximum number of critical interactions, i.e. 42\%. The Intersection-1 was the safest in terms of pedestrian-vehicle interactions with a maximum of its events falling under safe-passage. The safety of the intersection 2 and 3 can be improved by implementing various traffic control measures (countermeasures) like providing crosswalk visibility enhancements, rumbles strips before crosswalks, raised crosswalks, proper pedestrian crossing signs, advanced yield signs, and Marked crosswalks. This will help in bringing down the number of critical interactions. The present study framework can be applied to any uncontrolled intersection by first extracting the SSM indicators using the open source Kinovea tool. Then, the events will be divided under different patterns based on Eq. 7, and as a last step, the events will be divided into different severity dimensions based on the suggested ranges using $\mathrm{TTC}_{\text {min }}$, and PET values.
- The proposed framework was implemented on the fourth intersection. A comparison of pedestrian interactions with directional traffic and with different categories of vehicles was carried out from the results. It was interesting to note that the pedestrian interaction with the right turning vehicle was the most unsafe may be because of the less yielding time available for the right turning traffic. In terms of categories of vehicles, the pedestrian interaction with three wheeler was the most unsafe.

The study approach presented in paper was clearly different from the conventional approaches which used either a single indicator or aggregation of indicators ignoring the behavioral differences of the interacting road users. Not just this, but to the best knowledge of the authors', no previous study evaluated the pedestrian interaction with different types of vehicle under mixed traffic condition for a developing country like India. The study still has some limitations. Firstly, the present study although shows an improvement over other similar kind of studies by using pairwise pattern interaction of pedestrian with different types of vehicle, but still, it is further important to study the pedestrian platoon interaction with different types of vehicles. For e.g. pedestrian platoon interaction with car would be very different with that of a bus. This study was based on three intersections with certain type of characteristics hence, more efforts are needed to develop threshold values that are more transferable. Also, the study can be
further extended by carrying out a sensitivity analysis to analyze the effect of various infrastructural improvement alternatives to increase the safety of road users at intersections. This would be done by comparing the increase or decrease in the level of severity before and after the infrastructural improvement.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Appendix A

The basic algorithm of IVM is briefly explained as follows (19,20). The steps of the algorithm shown below starts with an empty subset $S$ of import vectors.

$$
\text { Step }-1: \text { Let } S=\emptyset, R=\left\{x_{1}, x_{2}, \ldots . ., x_{n}\right\}, k=1
$$

Step - 2: $x_{1} \in R$, let

$$
f_{1}(x)=\sum_{x_{j} \in S \cup\left\{x_{i}\right\}} a j K\left(s, x_{j}\right)
$$

Find $\overrightarrow{\mathrm{a}}$ to minimize

$$
\begin{aligned}
& \sum_{i=1}^{N}\left[y_{i} f_{l}\left(x_{i}\right)-\ln \left(1+\exp \left(f_{l}\left(x_{i}\right)\right)\right)\right]+\frac{\lambda}{2}\left\|f_{1}(x)\right\|^{2} H_{k} \\
& =-\vec{y}^{T}\left(K_{a}^{l} \vec{a}^{l}\right)+\overrightarrow{1}^{t} \ln \left(1+\exp \left(K_{a}^{l} \vec{a}^{l}\right)\right)+\frac{\lambda}{2} \vec{a}^{l T} K_{q}^{l} \vec{a}^{l}
\end{aligned}
$$

Where the regressor matrix $K_{a}^{l}=\left[K\left(x_{i}, x_{j}\right)\right]_{N(q+1)}, x_{i} \in\left\{x_{1}, x_{2}, \ldots x_{N}\right\}, x_{j} \in S \cup\left\{x_{l}\right\}$ :
The regularization matrix $K_{q}^{l}=\left[K\left(x_{j}, x_{l}\right)\right]_{(q+1)(q+1)}, x_{j}, x_{l} \in S \cup\left\{x_{l}\right\} ; q=|S|$
Step - 3: Let $x_{l^{*}}=\operatorname{argmin}_{x_{l} \in R} H\left(x_{l}\right)$
Let $S=S \cup x_{l^{*}}, R=R\left\{x_{l^{*}}\right\}, H_{k}=H\left(x_{l^{*}}\right), k=k+1$

Step - 4: Repeat steps 2 and 3 until $H_{k}$ converges

## Appendix B

Let $N$ be the total number of severity dimension $(0,1,2)$, let $n$ be the number of ratings per severity dimension, and let $k$ be the number of categories into which assignments are made, which in present case is 3 . The subjects are indexed by $i=1, \ldots N$ and the categories are indexed by $j=1, \ldots k$. Let $n_{i j}$ represent the number of raters who assigned the $i$-th subject to the $j$-th category.

First calculate $p \mathrm{j}$, the proportion of all assignments which were to the $j$-th category:

$$
p_{j}=\frac{1}{N_{n}} \sum_{i=1}^{N} N_{i j}, 1=\sum_{j=1}^{k} p_{j}
$$

Now calculate $p_{i}$, the extent to which raters agree for the $i$-th subject (i.e., compute how many rater-rater pairs are in agreement, relative to the number of all possible rater-rater pairs):

$$
\begin{aligned}
& P_{i}=\frac{1}{n(n-1)} \sum_{j=1}^{k} n_{i j}\left(n_{i j}-1\right) \\
& =\frac{1}{n(n-1)} \sum_{j=1}^{k}\left(n_{i j}^{2}-n_{i j}\right) \\
& =\frac{1}{n(n-1)}\left[\left(\sum_{j=1}^{k}\left(n_{i j}^{2}\right)-(n)\right]\right.
\end{aligned}
$$

Now compute $\bar{P}$, mean of the $P_{i}$ 's and $\bar{P}_{e}$ which goes into the formula of kappa ( $\kappa$ )

$$
\begin{aligned}
& \bar{P}=\frac{1}{N} \sum_{i=1}^{N} p_{i} \\
& =\frac{1}{N(n-1)}\left(\sum_{i=1}^{N} \sum_{j=1}^{k} n_{i j}^{2}-N n\right) \\
& \bar{P}_{e}=\frac{1}{N} \sum_{j=1}^{k} p_{j}^{2}
\end{aligned}
$$

After estimating $\bar{P}$ and $\bar{P}_{e}$, the kappa coefficient ( $\kappa$ )would be computed as under:

$$
\kappa=\frac{\bar{P}-\bar{P}_{e}}{1-\bar{P}_{e}}
$$

The $1-\bar{P}_{e}$ gives the degree of agreement that is attained above chance and $\bar{P}-\bar{P}_{e}$ gives the degree of the agreement actually achieved above chance. If the rates are in complete agreement then $\kappa=1$, if there is no agreement among the raters then $\kappa \leq 0$. After estimating $\kappa$ value, a table given by Landis and Koch (1977) needs to be referred for interpretation of the $\kappa$ value as under:

| $\kappa$ | Interpretation |
| :--- | :--- |
| < 0 | Poor agreement |
| 0.01-0.20 | Slight agreement |
| 0.21-0.40 | Fair agreement |
| 0.41-0.60 | Moderate agreement |
| 0.61-0.80 | Substantial agreement |
| 0.81-1.00 | Almost perfect agreement |

## References

Alhajyaseen, W.K., Asano, M., Nakamura, H., 2012. Estimation of left-turning vehicle maneuvers for the assessment of pedestrian safety at intersections. Iatss Res. 36 (1), 66-74.
Alhajyaseen, W.K., 2015. The integration of conflict probability and severity for the safety assessment of intersections. Arab. J. Sci. Eng. 40 (2), 421-430.
Allen, B.L., Shin, B.T., Cooper, P.J., 1977. Analysis of Traffic Conflicts and Collisions. Department of Civil Engineering, McMaster University.
Aurell, A., Djehiche, B., 2018. Modeling tagged pedestrian motion: a mean-field type control approach. Transp. Res. Part B Methodol. 121, 168-183.
Bode, N.W., Chraibi, M., Holl, S., 2019. The emergence of macroscopic interactions between intersecting pedestrian streams. Transp. Res. Part B Methodol. 119, 197-210.
Diví, A., Padullés-Riu, J.M., Busquets-Faciaben, A., Padullés-Chando, X., Escalona Marfil, C., Marcos-Ruiz, D., 2017. Validity and reliability of the kinovea program in obtainin angular and distance dimensions. Preprints 2017. https://doi.org/10.20944/preprints201710.0042.v1. 2017100042.
Englund, A., Gregersen, N.P., Hyden, C., Lovsund, P., Aberg, L., 1998. Trafiksakerhet - En kunskaps "oversikt. KFB. Art. nr. 6319. Printed by Studentlitteratur, Lund, Sweden.
Fu, T., Stipancic, J., Zangenehpour, S., Miranda-Moreno, L., Saunier, N., 2017. Automatic traffic data collection under varying lighting and temperature conditions in multimodal environments: thermal versus visible spectrum video-based systems. J. Adv. Transp 2017.
WHO, 2018. Global Status Report on Road Safety 2018: Summary. World Health Organization, Geneva, pp. 2018 (WHO/NMH/NVI/18.20). Licence: CC BY-NC-SA 3.0 IGO). (Accessed 19 January 2019).
Hayward, J., 1971. Near Misses as a Measure of Safety at Urban Intersections. PhD Thesis. Department of Civil Engineering, The Pennsylvania State University, Pennsylvania.
Huang, Z., He, Y., Wen, Y., Song, X., 2018. Injured probability assessment in frontal pedestrian-vehicle collision counting uncertainties in pedestrian movement. Saf. Sci. 106, 162-169.
Hupfer, C., 1997. Deceleration to safety time (DST)-a useful figure to evaluatetraffic safety. 1997 ICTCT Conference Proceedings of Seminar 3, Departmentof Traffic Planning and Engineering.
Ismail, K., Sayed, T., Saunier, N., 2010. Automated analysis of pedestrian-vehicle conflicts: context for before-and-after studies. Transp. Res. Rec. J. Transp. Res. Board 2198, 52-64.
Ismail, K., Sayed, T., Saunier, N., Lim, C., 2009. Automated analysis of pedestrian-vehicle conflicts using video data. Transp. Res. Rec. J. Transp. Res. Board 2140, 44-54.
Jain, U., Rastogi, R., 2016. Pedestrian crossing warrants: a review of Global Practices. Curr. Sci. 111 (6).
Ji, Z., Trevor, H., 2005. Kernel logistic regression and the import vector machine (2005). J. Comput. Graph. Stat. 14 (1), 185-205.
Kadali, B.R., Vedagiri, P., 2016. Proactive pedestrian safety evaluation at unprotected mid-block crosswalk locations under mixed traffic conditions. Saf. Sci. 89, 94-105.
Kaparias, I., et al., 2010. Development and implementation of a vehicle-pedestrian conflicts analysis method: adaptation of a vehicle-vehicle technique. Transp. Res. Rec. J. Transp. Res. Board 2198, 75-82.
Killi, D.V., Vedagiri, P., 2014. Proactive evaluation of traffic safety at an unsignalized intersection using micro-simulation. J. Traffic Logist. Eng. 2 (2).
Kinovea, 2019. Dehwko, C. Kinovea. http://www.kinovea.org.
Koh, P.P., Wong, Y.D., Chandrasekar, P., 2014. Safety evaluation of pedestrian behaviour and violations at signalised pedestrian crossings. Saf. Sci. 70, 143-152.
Landis, J.R., Koch, G.G., 1977. The measurement of observer agreement for categorical data. Biometrics 33, 159-174.
Laureshyn, A., Svensson, Å., Hydén, C., 2010. Evaluation of traffic safety, based on microlevel behavioural data: theoretical framework and first implementation. Accid. Anal. Prev. 42 (6), 1637-1646.
Liu, M., Chen, Y., Lu, G., Wang, Y., 2017. Modeling crossing behavior of drivers at unsignalized intersections with consideration of risk perception. Transp. Res. Part F: Traffic Psychol. Behav. 45, 14-26.
MoRTH, 2017. Road Accidents in India. Transportation Research Wing. Ministry of Road Transport and Highways, Government of India. http://morth.nic.in/showfile.
Ni, Y., Wang, M., Sun, J., Keping, L., 2016. Evaluation of Pedestrian Safety at Intersections: a theoretical framework based on pedestrian-vehicle interaction patterns. Accid. Anal. Prev. 96, 118-129.
Ren, G., Gu, C., Lu, L., Zhou, Z., Ding, C., 2012. Modeling risk degree of conflicts between crossing pedestrians and vehicles at signalized intersections. J. Transp. Syst. Eng. Inf. Technol. 12 (5), 76-81.
Shekhar Babu, S., Vedagiri, P., 2016. Proactive safety evaluation of a multilane unsignalized intersection using surrogate measures. Transp. Lett. 10 (2), 104-112. https://doi.org/10.1080/19427867.2016.1230172.
Salamati, K., Schroeder, B., Rouphail, N.M., Cunningham, C., Long, R., Barlow, J., 2011. Development and implementation of conflict-based assessment of pedestrian safety to evaluate accessibility of complex intersections. Transp. Res. Rec. J. Transp. Res. Board 2264, 148-155 Saunier.
Svensson, A., Hyden, C., 2006. Estimating the severity of safety related behaviour. Accid. Anal. Prev. 38, 379-385.
Tapiro, H., Oron-Gilad, T., Parmet, Y., 2018. The effect of environmental distractions on child pedestrian's crossing behavior. Saf. Sci. 106, 219-229.
Van der Horst, R., Kraay, R.J., 1986. The Dutch Conflict Technique-DOCTOR. ICTCT Workshop, Budapest.
Vogel, K., 2002. What characterizes a free vehicle in an urban area? Transp. Res. F. 5, 15-29.
Wong, T.-T., 2015. Performance evaluation of classification algorithms by k-fold and leave one out cross validation. Pattern Recognit. 48, 2839-2846.


[^0]:    *Corresponding author.
    E-mail addresses: ankit.kathuria@iitjammu.ac.in (A. Kathuria), vedagiri@civil.iitb.ac.in (P. Vedagiri).

