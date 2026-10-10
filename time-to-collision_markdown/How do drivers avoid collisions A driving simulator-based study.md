# How do drivers avoid collisions? A driving simulator-based study 

Xiaomeng Li, ${ }^{\mathrm{a}, \mathrm{b}}$ Andry Rakotonirainy, ${ }^{\mathrm{b}}$ Xuedong Yan ${ }^{\mathrm{a}, *}$<br>${ }^{\mathrm{a}}$ MOT Key Laboratory of Transport Industry of Big Data Application Technologies for Comprehensive Transport, School of Traffic and Transportation, Beijing Jiaotong University, Beijing 100044, China<br>${ }^{\mathrm{b}}$ Centre for Accident Research and Road Safety-Queensland (CARRS-Q), Institute of Health and Biomedical Innovation (IHBI), Queensland University of Technology (QUT), Kelvin Grove, Qld 4059, Australia

ARTICLE INFO

Article history:
Received 16 October 2018
Received in revised form 5 March 2019
Accepted 22 May 2019
Available online xxxx

Keywords:
Driving simulator
Collision avoidance behavior
Head-on collision
Right-angle collision
Collision with pedestrian


#### Abstract

Introduction: Drivers' collision avoidance performance in an impending collision situation plays a decisive role for safety outcomes. This study explored drivers' collision avoidance performances in three typical collision scenarios that were right-angle collision, head-on collision, and collision with pedestrian. Method: A high-fidelity driving simulator was used to design the scenarios and conduct the experiment. 45 participants took part in the simulator experiment. Drivers' longitudinal/lateral collision avoidance performances and collision result were recorded. Results: Experimental results showed that brake only was the most common response among the three collision scenarios, followed by brake combining swerve in head-on and pedestrian collision scenarios. In right-angle collision scenario with TTC (time to collision) largest among three scenarios, no driver swerved, and meanwhile drivers who showed slow brake reaction tended to compensate the collision risk by taking a larger maximum deceleration rate within a shorter time. Swerve-toward-conflict was a prevalent phenomenon in head-on and pedestrian collision scenarios and significantly associated with collision risk. Drivers that swerved toward the conflict object had a shorter swerve reaction time than drivers that swerved away from conflict. Conclusions: Long brake reaction time and wrong swerve direction were the main factors leading to a high collision likelihood. The swerve-toward-conflict maneuver caused a delay in brake action and degraded subsequent braking performances. The prevalent phenomenon indicated that drivers tended to use an intuitive (heuristic) way to make decisions in critical traffic situations. Practical applications: The study generated a better understanding of collision development and shed lights on the design of future advanced collision avoidance systems for semi-automated vehicles. Manufactures should also engage more efforts in developing active steering assistance systems to assist drivers in collision avoidance.


© 2019 National Safety Council and Elsevier Ltd. All rights reserved.

## 1. Introduction

Traffic crash is a major public health problem resulting in large numbers of deaths, injuries, and property damage every year worldwide. The World Health Organization (WHO) estimates that each year, over 1.2 million people died from road traffic injuries, and another 20-50 million are injured in road traffic crashes (WHO, 2015). Traffic collisions can be classified into general types (Kaplan \& Prato, 2012), including angle collision, rear-end collision, sideswipe, head-on collision, hit pedestrian and hit animal/object, etc. According to statistics in Queensland, Australia from 2005 to 2013 (Department of Transport and Main Roads, 2015), the most frequent occurring collisions were angle collisions accounting for 34.2\% of all types of collisions, while the collisions with highest death rate and injury rate (including hospitalized, medically treated and minor injury cases) were head-on collisions (death

[^0]rate and injury rate: 0.037 and 1.28 people per collision, respectively), then followed by pedestrian collisions (death rate and injury rate: 0.028 and 1.056 people per collision, respectively).

A lot of effort has been engaged in the research of traffic collisions aiming to understand and learn from these collisions, and further eliminate them. The research in this field has been conducted mainly in two ways either through analysis of historical crash database or experimental data. The historical crash data provide an overall statistical information of all kinds of collisions, which allows a first estimation of why the collision occurred (Harb, Yan, Radwan, \& Su, 2009). Limitation on this basis lies in the lack of driver behavioral information, and therefore it is hard to reconstruct the collision process in detail (Zhang, Yan, Li, Wu, \& Dixit, 2018). Besides, inconsistency exists in the information recording criteria due to different recorders or organizations. The experimental data are usually collected by a driving simulator, which allows the experiment to be conducted in a repeatable and controllable environment (Li, Yan, \& Wong, 2015; Li, Yan, Wu, Radwan, \& Zhang, 2016). More importantly, it facilitates the assessment of driving behaviors in pre-crash situations that could not be achieved in a real world
test for obvious safety concern (Yan et al., 2016; Li, Rakotonirainy, Yan, \& Zhang, 2018).

In recent years, a large body of research has used simulator-based experiment to examine driving behavior/performance in critical situations (Antoniou, Celikoglu, Farah, \& Azevedo, 2018; Wong, Yan, Radwan, \& Li, 2018). For example, Danaf, Hamdar, Abou-Zeid, and Kaysi (2018) focused on the issue of risky driving behaviors such as speeding and red-light violations at signalized intersections using simulation experiments. Wang, Zhu, Chen, and Tremont (2016) investigated the rear-end collision avoidance behaviors of drivers in a car-following situation with different situational urgency levels. Hajiseyedjavadi et al. (2018) evaluated the hazard anticipation, mitigation, and attention maintenance performance of drivers when they were provided with head-up display warnings in advance of a latent threat in a driving simulator. The problem with driving simulator studies is that drivers may perceive and response to the driving risk differently as they do in the real world driving. However, many validation studies of the driving simulators have concluded that data collected from the driving simulators can effectively reflect drivers' behavior patterns in real world (Underwood, Crundall, \& Chapman, 2011).

From the perspective of drivers, several approaches have been attempted to help reduce the collision occurrence. One approach is to target the drivers who are responsible for the collisions so that errors can be prevented from causing the collisions, such as the studies of drink driving or distracted driving (Li, Oviedo-Trespalacios, Rakotonirainy, \& Yan, 2019; Wan et al., 2017). This group of drivers and related adverse factors have been investigated with plenty of focus. Another approach is to support the drivers not responsible for the collisions to react in the best possible way in critical situations, namely to enhance their collision avoidance abilities (Xiang, Yan, Weng, \& Li, 2016; Zhang et al., 2018; Zhang, Yan, Li, \& Xue, 2016). The latter group of drivers is the research target in this study. To understand how drivers behave in various critical situations is an essential task before the best support could be provided.

Drivers' behavior response to imminent collisions, especially seconds before the collision, are extremely crucial, as appropriate evasive response grants drivers great opportunities to avoid the collision or at least reduce its severity (Harb et al., 2009). It has been reported that many of the potential crashes could be avoided by taking simple evasive behaviors, such as releasing the accelerator to yield to a conflict object crossing in front, while other situations require drivers to take a quick reaction and combine behaviors such as braking and steering to avoid a collision (McGehee et al., 2000). Findings from naturalistic studies, test track, and simulator experiment showed that braking is the most common response by drivers to avoid collisions, which constitutes over 80\% of all types of responses in crash reports (Lechner \& Malaterre, 1991; Najm et al., 2013). In contrast, swerve is a less common maneuver (Najm et al., 2013). Drivers chose to brake even when swerve would have been more successful in avoiding collisions (Markkula, Benderius, Wolff, \& Wahde, 2012). However, research also indicated that when it comes to the situations with large time to collision (noncritical events) or short time to collision (imminent collision), drivers are more likely to swerve (Markkula et al., 2012; Lee, McGehee, Brown, \& Reyes, 2002), and meanwhile, swerving while braking could occur in situations with very short TTC (McGehee et al., 2000).

Although drivers' collision avoidance behaviors haven been investigated thoroughly from both longitudinal (speed control) and lateral (steering wheel control) levels, the deriving relationship and the interaction effect between longitudinal and lateral maneuvers were rarely examined. Previous research paid much attention to drivers' decision making and maneuver choice in critical situations while the correlations between different maneuvers and the collision risk were often overlooked (Markkula et al., 2012; Najm et al., 2013). Besides, when investigating drivers' collision avoidance performance, researchers tended to restrict the research scope within a particular type of collision and a large body of them have focused on the rear-end collision or
intersection angle collision (Lee et al., 2002; Weber, Blum, Ernstberger, \& Färber, 2015). In contrast, little attention has been paid on the less-frequent but high-fatality-rate collisions, such as the headon collisions.

Therefore, the primary aim of this study is to understand the decision-making and action execution processes involved in the emergency collision avoidance maneuvers. Three diverse collisions are considered: (a) the head-on collision, (b) the right-angle collision, and (c) the collision with pedestrian. A high-fidelity driving simulator is used for the experiment and data collection. Considering the gaps with previous research, the study focuses on three targets specifically: (a) to capture the common/unique patterns in behaviors across different collision scenarios and the mechanism governing the selection of maneuver types; (b) to quantify the correlation between collision avoidance maneuvers and the likelihood of collisions; (c) to explore the deriving relationship and interaction effect between longitudinal and lateral collision avoidance maneuvers in an imminent collision situation.

## 2. Methodology

### 2.1. Participants

A total of 45 participants were recruited, including 21 female drivers and 24 male drivers. The average age of the participants was 34.5, ranging from 31 to 40 years old with a standard deviation of 3 years. Each participant held a valid driver's license prior to the study, and drove a minimum of 20,000 km per year with at least two years of driving experience.

### 2.2. Apparatus

The Beijing Jiaotong University (BJTU) driving simulator was used to conduct the experiment. As shown in Fig. 1, the BJTU simulator is a highfidelity, high-performance, driving simulator with a linear motion base capable of operating with 1 degree of freedom (pitching). It is composed of a full-size vehicle cabin (Ford Focus) with a real operational interface, environmental noise and movement simulation system, digital video replay system, and vehicle dynamic simulation system. The simulated environment is projected with a front/peripheral field of view of 300 degrees at a resolution of $1400 \times 1050$ pixels and left, middle and right rear-view mirrors. The simulator lab provides the software (Simvista \& Simcreator) for driving scenario design, virtual traffic environment simulation and virtual road modeling.

### 2.3. Scenarios design

The study designed three collision scenarios: head-on collision, right-angle collision, and collision with pedestrian (see Fig. 2). In three scenarios, ambient road users (conflict objects) intruded driver's front pathway and triggered a conflict leading to a potential collision. Consistent with the definition proposed by Amundsen and Hyden (1977), the traffic conflict created in each scenario was an observable situation in which two or more road users approached each other in space and time to such an extent that there was a risk of collision if their movements remained unchanged.

The road network for each scenario was about 5 km long and took 5- 10 min driving. The road was two-way, two-lane with no guardrail or center median divider placed on the road. Each lane was 3.5 m width and the speed limit on the road was 80 km/h. All the three types of collisions were triggered by a pre-set TTC value, which was defined as the expected time for two road users to collide if trajectories and speeds of both users remained unchanged (Debnath, Wilson, \& Haworth, 2014). The conflict objects in three scenarios were visible and stationary before triggering. Once the approaching time of the driver to the conflict position reached the pre-set TTC value, the conflict object would be

![](https://cdn.mathpix.com/cropped/076d19b0-1939-4b89-8402-79e9cbfb7d4b-3.jpg?height=420&width=1193&top_left_y=183&top_left_x=452)
Fig. 1. The BJTU driving simulator.

triggered to move toward the conflict position. Drivers need to respond timely once the conflict object started moving to avoid a collision. Given that the trajectories and speeds of the conflict objects in three scenarios were essentially different, the pre-set TTC value in each scenario was designed differently according to the characteristics of each scenario. In general, the TTC threshold among three scenarios ranged between 3 and 5 s, corresponding to a slightly high conflict level (Hecht, Landwehr, \& Baur, 2009). Specifically, the pre-set TTC values in headon collision, pedestrian collision and right-angle collision scenarios were 3.5 , 3.5, and 5 s, respectively. The reason that two different TTC values were designed was because: (1) the conflict objects in head-on collision and pedestrian collision scenarios suddenly invaded the participant driving lane. A smaller TTC could help create a critical event and also ensure that the participants can perceive the targets before they were triggered; (2) the conflict vehicle in right-angle collision situation kept driving on its original lane. It should to be triggered early to ensure the vehicle was already moving when the participants perceived it. Thus, a relatively larger TTC was required. The equation to calculate pre-set TTC was listed as follows:

## $T T C_{\text {pre }}=D_{\text {conflict }} / V_{\text {conflict }}$

In which, $T T C_{p r e}$ represents the pre-set TTC value in each scenario; $D_{\text {conflict }}$ represents the distance between the initial position of the conflict object to the conflict position; $V_{\text {conflict }}$ represents the speed of the conflict object.

## (1) Head-on collision scenario

The head-on collision scenario was designed on a straight road seg-
The head-on collision scenario was designed on a straight road segment (see Fig. 2a). The conflict vehicle was arranged on the opposite ment (see Fig. 2a). The conflict vehicle was arranged on the opposite lane at a distance of 100 m to the conflict position. When the ap- lane at a distance of 100 m to the conflict position. When the approaching time of the drivers to the conflict position reached 3.5 s, the proaching time of the drivers to the conflict position reached 3.5 s, the 235

![](https://cdn.mathpix.com/cropped/076d19b0-1939-4b89-8402-79e9cbfb7d4b-3.jpg?height=1124&width=1595&top_left_y=1393&top_left_x=250)
Fig. 2. Three collision scenarios.

conflict vehicle would start to move toward the conflict position at a speed of 100 km/h.
(2) Collision with pedestrian scenario

The collision with pedestrian scenario was also designed on a straight segment (see Fig. 2b). Before the conflict was triggered, a pedestrian stood on the roadside and the distance from his location to the conflict position was 15 m. Once the approaching time of the drivers to the conflict position reached 3.5 s, the pedestrian would start to run across the road in front of the simulator at a speed of 15 km/h.
(3) Right-angle collision scenario

The right-angle collision scenario was arranged at a non-signalized intersection (see Fig. 2c). Drivers drove on the main road with a priority to pass the intersection and the conflict vehicle came from the minor road. When the approaching time of the drivers to the conflict position reached 5 s, the conflict vehicle would be triggered to move toward the intersection at a speed of 72 km/h from an initial distance of 100 m to the intersection.
2.4. Procedure

Upon arrival, each participant read and signed an informed consent form (per IRB). The participants were advised to drive as they normally would and to comply with traffic laws as they did in real-life situations. They were also notified that they can quit the experiment at any time in case of motion sickness or any kind of discomfort. Before the experiment, each participant had a 5-10 min practice drive session to familiarize themselves with the vehicle operations, such as acceleration, deceleration, and left/right turn. During the formal experiment, each participant drove on the three road networks with one collision event during each drive. The sequence of three drives was counterbalanced among all participants to eliminate the experiment order effect. Participants had 10 min rest between each round of driving. After the experiment, each participant was paid 300 Chinese RMB (about 45 U.S. dollars) for their participation.
2.5. Data collection and analysis

The simulator raw data were sampled at 60 Hz. Key variables representing the drivers' collision avoidance maneuvers and collision result were extracted from raw data for further analysis. The variables included approaching speed, brake reaction time, maximum deceleration, time to maximum deceleration, swerve direction, swerve reaction time, maximum swerve radian, and collision or not. Definitions of the variables were listed as follows.

- Approaching speed (km/h): the approaching speed refers to the speed of drivers at the time when the conflict object was triggered to move. It was a normal driving speed when drivers had not perceived the potential collision risk yet.
- Brake reaction time(s): the brake reaction time refers to the time duration from when the conflict object was triggered to move to the time when the driver started to decelerate to avoid the collision.
- Maximum deceleration $\left(\mathrm{m} / \mathrm{s}^{2}\right)$ : the maximum deceleration refers to the maximum absolute value of longitudinal deceleration during the driver's collision avoidance process.
- Time to maximum deceleration (TTMs): the time to maximum deceleration refers to the time duration from when the driver started to decelerate to the time when the deceleration rate reached a maximum value.
- Swerve reaction time ( $s$ ): the swerve reaction time refers to the time duration from when the conflict object was triggered to move to the

- Swerve direction: the swerve direction means the turning direction of the steering wheel during the collision avoidance process. According to the moving trajectory of the conflict object, it can also be divided into conflict-avoidance direction and conflict-toward direction. In the right-angle and pedestrian collision scenarios, the conflict vehicle/pedestrian came from the right and moved toward the left, so swerve-to-right was the conflict-avoidance direction and swerve-toleft was the conflict-toward direction. Oppositely, in head-on collision scenario, swerve-to-right was the conflict-toward direction and swerve-to-left was the conflict-avoidance direction.
- Maximum swerve radian (rad): the maximum swerve radian refers to the maximum value of steering wheel swerve radian during the collision avoidance process, which could also represent the swerve angle of the steering wheel by multiplying $180 / \pi\left(57.3^{\circ}\right)$.
- Collision or not (0/1): this binary variable represents whether the driver had a collision with the conflict object or not. 0 represents no collision while 1 represents collision.

In the study, the majority of dependent variables were continuous and the independent variables were different groups of drivers categorized by their maneuver choice or scenario. For the continuous variables, t-test was used as it allowed to examine if there was significant difference between the means of two groups. Linear mixed model was applied to test the difference of variable among three drives. To demonstrate the strength of the difference between groups, the effect size $\left(\eta^{2}\right)$ was also reported. In terms of binary variables such as collision or not, logistic regression model with fixed effects was performed to examine the association between collision avoidance maneuvers and collision risk. The statistical testing in the analysis was based on a 0.05 significance level.
3. Results
3.1. Overview of the collision avoidance maneuvers and collision result

Generally when facing a potential collision risk, the possible response maneuvers that drivers may execute are: (i) changing the vehicle's longitudinal dynamic status by controlling the brake/accelerator pedal, (ii) changing the vehicle's lateral dynamic status by controlling the steering wheel, (iii) the combination of both, (iv) no action (Adams, 1994). In this study, seven types of collision avoidance maneuvers in total were observed in three scenarios. Distribution of the maneuvers and corresponding collision result were listed in Table 1. The most frequent maneuver in three scenarios was brake only, which accounted for 71.1\%, 48.9\%, and 91.1\% respectively, in pedestrian collision, head-on collision and right-angle collision scenarios. Additionally, 28.9\% of drivers in pedestrian collision scenario and 31.1\% in head-on collision scenario chose to brake and swerve toward conflict. The collision rates in three scenarios were $42.2 \%$ (pedestrian collision), $42.2 \%$ (head-on collision), and 13.3\% (right-angle collision), respectively. Descriptive statistics of the detailed maneuver variables were listed in Table 2.
3.2. Collision avoidance maneuver analysis
3.2.1. Pedestrian collision

In pedestrian collision scenario, drivers' collision avoidance maneuvers concentrated on two types: brake only (71.1\%), and brake and swerve toward conflict (28.9\%). Specifically, driver that braked only had a collision rate of 28.1\%, while drivers braked and swerved toward conflict had a collision rate of up to $76.9 \%$. For the group of drivers that chose to brake and swerve toward conflict, a paired-samples

Table 1
Statistics of drivers' collision avoidance maneuvers and collision results.
| Maneuver type | Pedestrian collision |  | Head-on collision |  | Right-angle collision |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | No collision | Collision | No collision | Collision | No collision | Collision |
| Brake only | 23 | 9 | 15 | 7 | 38 | 3 |
| Swerve only (toward conflict) | 0 | 0 | 0 | 1 | 0 | 0 |
| Swerve only (away from conflict) | 0 | 0 | 1 | 0 | 0 | 0 |
| Brake \& swerve toward conflict | 3 | 10 | 4 | 10 | 0 | 0 |
| Brake \& swerve away from conflict | 0 | 0 | 6 | 0 | 0 | 0 |
| Acceleration only | 0 | 0 | 0 | 0 | 1 | 0 |
| No maneuver | 0 | 0 | 0 | 1 | 0 | 3 |
| Total | 26 | 19 | 26 | 19 | 39 | 6 |


t-test on their brake reaction time and swerve reaction time was conducted to identify which maneuver they performed firstly. The t-test results were listed in Table 3 and it showed that drivers' swerve reaction time (Mean = 0.86 s, S.D. = 1.01 s) was significantly shorter than their brake reaction time (Mean = 2.29 s, S.D. = 0.32 s; t (12) = 4.765, $\mathrm{p}<.001, \eta^{2}=0.65$ ). The results indicated that drivers tended to swerve first, even though it was toward a dangerous direction, and then performed braking.

As all the drivers braked in this scenario, to evaluate whether the swerve maneuver decision influenced the subsequent braking performances, an independent samples t-test was conducted on the brake reaction time, maximum deceleration and time to maximum deceleration between swerve drivers and no-swerve drivers. The t-test results (see Table 4) showed that there were significant differences of brake reaction time $\left(\mathrm{t}(43)=-3.684, \mathrm{p}<.01, \eta^{2}=0.24\right)$, maximum deceleration $\left(\mathrm{t}(15)=-4.097, \mathrm{p}<.01, \eta^{2}=0.28\right)$, and time to maximum deceleration ( $\mathrm{t}(43)=-3.757, \mathrm{p}<.01, \eta^{2}=0.25$ ) between swerve drivers and no-swerve drivers. Compared to no-swerve drivers (Mean = 1.93 s, S.D. = 0.28 s), the swerve drivers had a longer brake reaction time (Mean = 2.29 s, S.D. = 0.32 s), which is consistent with the above finding that these drivers delayed their brake actions because of the swerve maneuver. Besides, the swerve drivers also had a smaller maximum deceleration rate (Mean $=-4.36 \mathrm{~m} / \mathrm{s}^{2}$, S.D. $=2.60 \mathrm{~m} / \mathrm{s}^{2}$ ) and shorter time to maximum deceleration (Mean = 0.91 s, S.D. = 0.43 s) than the noswerve drivers (maximum deceleration: Mean $=-7.47 \mathrm{~m} / \mathrm{s}^{2}$, S.D. = $1.36 \mathrm{~m} / \mathrm{s}^{2}$; time to maximum deceleration: Mean = 1.40s, S.D. = 0.39 s).

### 3.2.2. Head-on collision

In head-on collision scenario, drivers mainly demonstrated three types of collision avoidance maneuvers: brake only, brake and swerve toward conflict, and brake and swerve away from conflict. Different from the pedestrian collision scenario, drivers in head-on collision situation demonstrated two swerve directions: toward and away from the conflict. The swerve reaction time of the two directions were compared by an independent samples t-test. The t-test result (see Table 5) showed that the difference between the two reaction times was significant (t $(20)=3.051, p<.01, \eta^{2}=0.32$ ), and the reaction time of swerve toward conflict $($ Mean $=1.41 \mathrm{~s}$, S.D. $=1.38 \mathrm{~s})$ was significantly shorter than that of swerve away from conflict (Mean = 3.38 s, S.D. = 1.49 s). There were 19 collisions observed in this scenario, among which, 36.8\% of them occurred on drivers that braked only, and 52.6\% of them occurred on drivers that braked and swerved toward conflict.

### 3.2.3. Right-angle collision

According to the collision avoidance maneuvers and collision result listed in Table 1, two major differences could be observed in rightangle collision scenario compared to the other scenarios: (1) the majority of drivers (91.1\%) chose to brake only to avoid the collision and no drivers swerved; (2) the collision rate in this scenario (13.3\%) was much lower than the other two scenarios (42.2\%). Furthermore, by analyzing the inter-relationship between longitudinal maneuver variables in three scenarios, another difference existing in right-angle collision scenario was identified. Table 6 showed the correlation between maximum deceleration, time to maximum deceleration, and brake reaction time in three scenarios. The brake reaction time had a significantly positive correlation with maximum deceleration in pedestrian and head-on collision scenarios, while the correlation was significantly negative in right-angle collision scenario. The correlations between brake reaction time and time to maximum deceleration were all significantly negative in three scenarios. The results indicated that: (1) as the brake reaction time increased, the time to maximum deceleration decreased; (2) for pedestrian and head-on collision scenarios, the drivers that took late brake action had a smaller maximum deceleration rate, while the tendency was opposite in right-angle collision scenario.

### 3.3. Collision risk analysis

Binary logistic regression models with fixed effects were developed to examine the association between collision avoidance maneuvers and collision risk in three scenarios. The variables in Table 1 were used as independent variables and whether driver had a collision or not was the dependent variable. As there were only six collisions observed in right-angle collision scenario, the near-miss incidents were identified in this scenario (13 in total, identified by the minimum distance between drivers and the conflict vehicle at the intersection less than 10 $\mathrm{m})$ and involved in the collision samples to compensate for the small

Table 3
T-test results of brake reaction time and swerve reaction time.
| Variables | N | Mean | S.D. | t-test |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  | Mean | t | df | Sig. (2-tailed) | 95\% CI |  |
|  |  |  |  |  |  |  |  | Lower | Upper |
| Brake reaction time | 13 | 2.29 | 0.32 | 1.42 | 4.765 | 12 | <0.001 | 0.79 | 2.06 |
| Swerve reaction time | 13 | 0.86 | 1.01 |  |  |  |  |  |  |


## ARTICLE IN PRESS

Table 4
T-test results of brake reaction time, maximum deceleration and time to maximum deceleration between no swerve and swerve drivers.
| Variables | Type | N | Mean | S.D. | t-test |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  | t | df | Sig. | Mean Difference | 95\% CI |  |
|  |  |  |  |  |  |  |  |  | Lower | Upper |
| Brake reaction time | No swerve | 32 | 1.93 | 0.28 | -3.684 | 43 | 0.001 | -0.35 | -0.55 | -0.16 |
|  | Swerve | 13 | 2.29 | 0.32 |  |  |  |  |  |  |
| Maximum deceleration | No swerve | 32 | -7.47 | 1.36 | -4.097 | 15 | 0.001 | -3.11 | -4.73 | -1.49 |
|  | Swerve | 13 | -4.36 | 2.60 |  |  |  |  |  |  |
| Time to maximum deceleration | No swerve | 32 | 1.40 | 0.39 | 3.757 | 43 | 0.001 | 0.49 | 0.23 | 0.75 |
|  | Swerve | 13 | 0.91 | 0.43 |  |  |  |  |  |  |


sample size. Results of the logistic regression model regarding three collision scenarios were listed in Table 7.

For the pedestrian collision, both brake reaction time and maximum swerve radian were significant variables that entered the model finally. As the brake reaction time increased by 0.1 s, the likelihood of collision would increase by 2.633 times. Increasing maximum swerve radian toward the pedestrian moving direction was also associated with an increased likelihood of driver being involved in a collision. The model can correctly classify 82.2\% of the cases with 73.7\% for non-collision group and 88.5\% for the collision group.

For the head-on collision, both the brake reaction time and the swerve direction were significantly associated with the collision occurrence. As the brake reaction time increased by 0.1 s, the likelihood of collision would increase by 1.714 times. Compared to drivers that did not swerve, drivers that swerved toward conflict were nearly 19 times more likely to collide. The model can correctly classify 83.3\% of the cases (82.4\% non-collision group vs. 84.2\% collision group).

For the right-angle collision, the approaching speed and the brake reaction time were found to be significantly associated with the collision/near-misses risk. The likelihood of collision/near-misses would increase by 1.433 times or 1.862 times if the approaching speed increased by 1 km/h or the brake reaction time increased by 0.1 s, respectively. The model can correctly classify 97.6\% of the cases (66.7\% non-collision group vs. 100\% collision group).

### 3.4. Experiment order effect

It was commonly believed that repeated exposure to a critical event can influence drivers' response behaviors, for example, reduced brake reaction time in response to expected (repeated) events (Benderius, Markkula, Wolff, \& Wahde, 2014; Engström, Aust, \& Viström, 2010). Although the three designed critical events in this study were different in essence, in order to test whether the repeated exposure had an effect on drivers' behavior, a linear mixed model was conducted on the approaching speed in three scenarios. The approaching speed was categorized by Drive 1, Drive 2, and Drive 3 in a time order that drivers experienced the three scenarios. The mean and standard deviation of approaching speed in three drives as well as the model results were presented in Table 8. There was no significant difference of the approaching speed from different drives $(\mathrm{F}(2,45)=0.948, \mathrm{p}>.05)$, which indicates that the potential effect caused by multiple exposure to critical scenarios might be well balanced among the three scenarios.

## 4. Discussion

Drivers' collision avoidance behaviors play a vital role in preventing
Drivers' collision avoidance behaviors play a vital role in preventing
Drivers' collision avoidance behaviors play a vital role in preventing
Drivers' collision avoidance behaviors play a vital role in preventing the occurrence of collisions and reduce the collision severity. Previous the occurrence of collisions and reduce the collision severity. Previous the occurrence of collisions and reduce the collision severity. Previous the occurrence of collisions and reduce the collision severity. Previous the occurrence of collisions and reduce the collision severity. Previous research has investigated drivers' collision avoidance performance in research has investigated drivers' collision avoidance performance in research has investigated drivers' collision avoidance performance in research has investigated drivers' collision avoidance performance in specific imminent collision situations considering the effects of various specific imminent collision situations considering the effects of various specific imminent collision situations considering the effects of various specific imminent collision situations considering the effects of various factors (e.g., weather, road, and driver conditions), and the longitudinal factors (e.g., weather, road, and driver conditions), and the longitudinal factors (e.g., weather, road, and driver conditions), and the longitudinal factors (e.g., weather, road, and driver conditions), and the longitudinal and lateral maneuvers in avoiding collisions were normally deemed as and lateral maneuvers in avoiding collisions were normally deemed as and lateral maneuvers in avoiding collisions were normally deemed as independent responses. This study focused on drivers who were not re- independent responses. This study focused on drivers who were not re- independent responses. This study focused on drivers who were not responsible for the collision or at least, not the trigger of the conflict. Scesponsible for the collision or at least, not the trigger of the conflict. Scesponsible for the collision or at least, not the trigger of the conflict. Scenarios with diverse collision situations (pedestrian collision, head-on narios with diverse collision situations (pedestrian collision, head-on narios with diverse collision situations (pedestrian collision, head-on collision and right-angle collision) were created by a high-fidelity driv- collision and right-angle collision) were created by a high-fidelity drivcollision and right-angle collision) were created by a high-fidelity driv- collision and right-angle collision) were created by a high-fidelity driving simulator. Based on the experiment results, both common features ing simulator. Based on the experiment results, both common features ing simulator. Based on the experiment results, both common features in collision avoidance and typical behavioral patterns were found in collision avoidance and typical behavioral patterns were found in collision avoidance and typical behavioral patterns were found among the three collision situations. The relationship between collision among the three collision situations. The relationship between collision among the three collision situations. The relationship between collision risk and maneuver choice was established and interaction effect be- risk and maneuver choice was established and interaction effect be- risk and maneuver choice was established and interaction effect between longitudinal and lateral maneuver response were explored. tween longitudinal and lateral maneuver response were explored. tween longitudinal and lateral maneuver response were explored.

In general, braking was the most prevalently attempted evasive
In general, braking was the most prevalently attempted evasive
In general, braking was the most prevalently attempted evasive
In general, braking was the most prevalently attempted evasive strategy for drivers in imminent collision situations, which accounted strategy for drivers in imminent collision situations, which accounted strategy for drivers in imminent collision situations, which accounted for $100 \%, 93.3 \%$, and $91.1 \%$ of drivers in pedestrian, head-on, and right- for $100 \%, 93.3 \%$, and $91.1 \%$ of drivers in pedestrian, head-on, and right- for 100\%, 93.3\%, and 91.1\% of drivers in pedestrian, head-on, and rightangle collisions, respectively. Brake in combination with swerve angle collisions, respectively. Brake in combination with swerve angle collisions, respectively. Brake in combination with swerve followed subsequently, accounting for 44.4\% of drivers in head-on colli- followed subsequently, accounting for 44.4\% of drivers in head-on colli- followed subsequently, accounting for 44.4\% of drivers in head-on collision and $28.9 \%$ in pedestrian collision scenarios. No drivers swerved in sion and $28.9 \%$ in pedestrian collision scenarios. No drivers swerved in sion and $28.9 \%$ in pedestrian collision scenarios. No drivers swerved in the right-angle collision scenario. The results were consistent with pre- the right-angle collision scenario. The results were consistent with pre- the right-angle collision scenario. The results were consistent with previous findings showing that drivers preferred to brake when sufficient vious findings showing that drivers preferred to brake when sufficient vious findings showing that drivers preferred to brake when sufficient time was available, and as the TTC decreased, the tendency to swerve time was available, and as the TTC decreased, the tendency to swerve time was available, and as the TTC decreased, the tendency to swerve time was available, and as the TTC decreased, the tendency to swerve in front of the obstacle's path increased (Lechner \& Malaterre, 1991; in front of the obstacle's path increased (Lechner \& Malaterre, 1991; in front of the obstacle's path increased (Lechner \& Malaterre, 1991; Markkula et al., 2012; Najm et al., 2013). Steering alone was the maneu- Markkula et al., 2012; Najm et al., 2013). Steering alone was the maneu- Markkula et al., 2012; Najm et al., 2013). Steering alone was the maneuver least attempted as an evasive action in most studies (Adams, 1994; ver least attempted as an evasive action in most studies (Adams, 1994; ver least attempted as an evasive action in most studies (Adams, 1994; Najm et al., 2013). Moreover, the study found that in the situation with Najm et al., 2013). Moreover, the study found that in the situation with Najm et al., 2013). Moreover, the study found that in the situation with relatively large TTC, drivers tended to increase the maximum decelera- relatively large TTC, drivers tended to increase the maximum decelera- relatively large TTC, drivers tended to increase the maximum deceleration rate to compensate for a late brake reaction. The phenomenon was tion rate to compensate for a late brake reaction. The phenomenon was tion rate to compensate for a late brake reaction. The phenomenon was observed exclusively in right-angle collision scenario. observed exclusively in right-angle collision scenario. observed exclusively in right-angle collision scenario.

Swerve was a common maneuver appeared in pedestrian collision
Swerve was a common maneuver appeared in pedestrian collision
Swerve was a common maneuver appeared in pedestrian collision
Swerve was a common maneuver appeared in pedestrian collision and head-on collision scenarios. However, a conspicuous finding that and head-on collision scenarios. However, a conspicuous finding that and head-on collision scenarios. However, a conspicuous finding that and head-on collision scenarios. However, a conspicuous finding that needs to be noted is that the majority of swerve drivers chose to swerve needs to be noted is that the majority of swerve drivers chose to swerve needs to be noted is that the majority of swerve drivers chose to swerve needs to be noted is that the majority of swerve drivers chose to swerve toward the conflict ( $100 \%$ in pedestrian collision and $68.2 \%$ in head-on toward the conflict ( $100 \%$ in pedestrian collision and $68.2 \%$ in head-on toward the conflict ( $100 \%$ in pedestrian collision and $68.2 \%$ in head-on collision). The phenomenon, also referred to "swerve into danger," has collision). The phenomenon, also referred to "swerve into danger," has collision). The phenomenon, also referred to "swerve into danger," has been previously reported in intersection collisions studies (Hu \& Li, been previously reported in intersection collisions studies (Hu \& Li, been previously reported in intersection collisions studies (Hu \& Li, 2017; Malaterre, Ferrandez, Fleury, \& Lechner, 1988; Weber et al., 2017; Malaterre, Ferrandez, Fleury, \& Lechner, 1988; Weber et al., 2017; Malaterre, Ferrandez, Fleury, \& Lechner, 1988; Weber et al., 2015). For example, an early study of Malaterre et al. (1988) indicated 2015). For example, an early study of Malaterre et al. (1988) indicated 2015). For example, an early study of Malaterre et al. (1988) indicated that at intersections if a lateral movement was attempted in obstacle- that at intersections if a lateral movement was attempted in obstacle- that at intersections if a lateral movement was attempted in obstacleavoidance crashes, it was almost always the same direction as the avoidance crashes, it was almost always the same direction as the avoidance crashes, it was almost always the same direction as the 467 468 468 469 469 470 470 471 471 472 472 473 474 474 475 475 476 476 477 477 478 478 479 480 480 481 481 483 483 484 484 485 485 486 486 487 488 488 489 490 491 491 492 493 493 494 495 495 496 497 500 501 502 502 503 503 504 504 505 506 506 507

Table 5
T-test results of swerve reaction time between different directions.
| Variables | Type | N | Mean | S.D. | t-test |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  | t | df | Sig. | Mean Difference | 95\% CI |  |
|  |  |  |  |  |  |  |  |  | Lower | Upper |
| Swerve reaction time | Away from conflict | 7 | 3.38 | 1.49 | 3.051 | 20 | 0.006 | 1.97 | 0.624 | 3.322 |
|  | Toward conflict | 15 | 1.41 | 1.38 |  |  |  |  |  |  |


| Please cite this article as: X. Li, A. Rakotonirainy and X. Yan, How do drivers avoid collisions? A driving simulator-based study, Journal of Safety Research, https://doi.org/10.1016/j.jsr.2019.05.002 |
| :--- |


Table 6
Correlation between longitudinal maneuver variables.
| Variables | Scenarios | Maximum deceleration |  | Time to maximum deceleration |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | N | Pearson Correlation | N | Pearson Correlation |
| Brake reaction time | Pedestrian | 45 | 0.498** | 45 | -0.569** |
|  | Head-on | 42 | 0.464** | 42 | -0.939** |
|  | Right-angle | 41 | -0.516** | 41 | -0.788** |


** Significant at the 0.01 level.
obstacle was moving. Weber et al. (2015) further found that when drivers at intersections experiencing a situation in which the right of way was taken from the right side vehicle, the percentage of swerving into danger was highest in the situation with lowest TTA (Time-To-Arrival). Up to our knowledge, the present study was the first one suggesting that the phenomenon could be likewise or even more prevalent in head-on collision situation and collision situation with crossing pedestrians. Experiment results also indicated that the swerve-toward-conflict behavior could lead to disastrous consequences: the maximum swerve radian toward conflict direction was found to be significantly associated with the collision risk in pedestrian collision scenario, and in head-on collision situation, drivers that swerved toward conflict had a higher collision risk of nearly 19 times compared with drivers that did not swerve.

Psychology theory in decision-making indicates that people generally apply two approaches to solve a problem: algorithms and heuristics (Fiedler, 2010). An algorithmic approach involves methodical or logical rules or procedures to solve a particular problem, which means in a traffic incident, drivers take all the options and details (e.g., braking, swerving, accelerating, no action, or a combination of these) into consideration in a conscious way and then systematically choose the appropriate response based on all possible outcomes. A heuristics approach usually involves focusing on one aspects of a complex problem and ignoring others, and it is usually governed by automatic intuitive thought, which allows drivers to make judgments and solve problems efficiently and quickly but may lead to more errors. Muttart (2005) suggested that although an algorithm method of decision-making is less likely to results in an error, it is rarely applied as it requires greater mental resources to take all options and outcomes into consideration. Findings of the present study strongly supported this theory. All swerving drivers in pedestrian collision situation and a majority of swerving drivers in head-on collision situation were found to choose the direction toward conflict. Furthermore, compared to the drivers that swerved away from conflict, the swerve-toward-conflict drivers had a significantly shorter reaction time. The results revealed a fact that drivers being able to respond to an emergency traffic situation very promptly implied that they probably did not considered all options and outcomes. In other words, drivers were inclined to use a heuristic, instead of an algorithmic method to make decisions in a critical pre-crash situation, and the intuitively and hastily made decisions normally led to a severer collision result.

Table 7
Results of logistic regression models with fixed effects for three scenarios.
| Scenarios | Variables | Coefficient | S.E. | t | Sig. | Exp(B) | 95\% CI |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  |  |  | Lower | Upper |
| Pedestrian | Brake reaction time (0.1 s) | 0.968 | 0.274 | 3.526 | 0.001 | 2.633 | 0.414 | 1.521 |
|  | Maximum swerve radian | -1.114 | 0.428 | -2.602 | 0.013 | 0.328 | -1.979 | -0.250 |
|  | Intercept | -20.097 | 5.561 | -3.614 | 0.001 | 0.000 | -31.318 | -8.875 |
| Head-on | Brake reaction time (0.1 s) | 0.539 | 0.152 | 3.554 | 0.001 | 1.714 | 0.230 | 0.848 |
|  | Swerve direction (toward conflict) | 2.936 | 1.101 | 2.666 | 0.012 | 18.840 | 0.693 | 5.180 |
|  | Intercept | -19.673 | 5.435 | -3.620 | 0.001 | 0.000 | -30.743 | -8.603 |
| Right-angle | Approaching speed | 0.360 | 0.155 | 2.325 | 0.026 | 1.433 | 0.047 | 0.674 |
|  | Brake reaction time (0.1 s) | 0.622 | 0.253 | 2.458 | 0.019 | 1.862 | 0.110 | 1.134 |
|  | Intercept | -33.888 | 12.230 | -2.771 | 0.009 | 0.000 | -58.648 | -9.129 |


## 5. Conclusion

The simulator study designed three typical collision scenarios (headon collision, collision with pedestrian, and right-angle collision) and tested drivers' collision avoidance maneuvers in these scenarios. The results showed that braking was the most commonly adopted maneuver, followed by brake in combination with swerve in head-on collision and pedestrian collision scenarios. For the right-angle collision situation in which the TTC was largest among three scenarios, no driver swerved and the late-reaction drivers tended to compensate the collision risk by taking a larger maximum deceleration rate. Swerve toward conflict was a prevalent phenomenon in head-on and pedestrian collision scenarios, and it is significantly associated with collision risk. Drivers that swerved toward conflict had a shorter swerve reaction time than drivers that swerved away from conflict, indicating that drivers tended to use a heuristic, instead of an algorithmic, method to make decisions in an emergency traffic situation. Besides, the swerve-toward-conflict phenomenon also caused a delay in brake action and degraded the subsequent braking performances. Findings of the study suggested that development of future vehicle collision avoidance systems should put more effort on the steering assistance control system to assist drivers in emergency collision situations.

## Acknowledgement

This work is supported by Australian Research Council (ARC DP140102895) and National Natural Science Foundation of China (71771014, 71621001).

## References

Adams, L. D. (1994). Review of the literature on obstacle avoidance maneuvers: braking versus steering. Report No. UMTRI-94-19.
Amundsen, F. H., \& Hyden, C. (Eds.). (1977). Proceeding of First Workshop on Traffic Conflicts. Oslo, Norway: Institute of Transport Economics, Oslo/Lund Institute of Technology.
Antoniou, C., Celikoglu, H. B., Farah, H., \& Azevedo, C. L. (2018). Special issue on simulation of traffic safety in the era of advances in technologies. Accident Analysis and Prevention, 116, 1-2.
Benderius, O., Markkula, G., Wolff, K., \& Wahde, M. (2014). Driver behaviour in unexpected critical events and in repeated exposures - a comparison. European Transport Research Review, 6, 51-60.
Danaf, M., Hamdar, S. H., Abou-Zeid, M., \& Kaysi, I. (2018). Comparative assessment of driving behavior at signalized intersections using driving simulators. Journal of Transportation Safety \& Security, 10, 124-158.
Debnath, A. K., Wilson, A., \& Haworth, N. (2014). Proactive safety assessment in roadwork zones: A synthesis of surrogate measures of safety. Proceedings of the 2014 Occupational Safety in Transport Conference, 18-19 September, Gold Coast, Australia.
Department of Transport and Main Roads (2015). Queensland Government. Road safety statistics. https://www.tmr.qld.gov.au/Safety/Transport-and-road-statistics/Road-sa fety-statistics.aspx.
Engström, J., Aust, M. L., \& Viström, M. (2010). Effects of working memory load and repeated scenario exposure on emergency braking performance. Human Factors, 52 (5), 551-559.
Fiedler, K. (2010). How to study cognitive decision algorithms: The case of the priority heuristic. Judgment and Decision making, 5(1), 21-32.
Hajiseyedjavadi, F., Zhang, T., Agrawal, R., Knodler, M., Fisher, D., \& Samuel, S. (2018). Effectiveness of visual warnings on young drivers hazard anticipation and hazard mitigation abilities. Accident Analysis \& Prevention, 116, 41-52.
Harb, R., Yan, X., Radwan, E., \& Su, X. (2009). Exploring precrash maneuvers using classification trees and random forests. Accident Analysis and Prevention, 41, 98-107.
Hecht, H., Landwehr, K., \& Baur, X. R. (2009). Discrimination thresholds for time-tocollision. Paper presented at the European Coneference on Visual Perception, 24-28 August, Regensburg, Germany.
Hu, M., \& Li, Y. (2017). Drivers' avoidance patterns in near-collision intersection conflicts. IEEE 20th International Conference on Intelligent Transportation Systems (ITSC).
Kaplan, S., \& Prato, C. G. (2012). Associating crash avoidance maneuvers with driver attributes and accident characteristics: A mixed logit model approach. Traffic Injury and Prevention, 13, 315-326.
Keller, C. G., Dang, T., Fritz, H., Joos, A., Rabe, C., \& Gavrila, D. M. (2011). Active pedestrian safety by automatic braking and evasive steering. IEEE Transactions on Intelligent Transportation Systems, 12(4), 1292-1304.
Lechner, D., \& Malaterre, G. (1991). Emergency maneuver experimentation using a driving simulator. Presented at Autotechnologies, 5th Conference and Exposition, Monte Carlo, Monaco. Report no. SAE 910016.
Lee, J. D., McGehee, D. V., Brown, T. L., \& Reyes, M. L. (2002). Collision warning timing, driver distraction, and driver response to imminent rear-end collisions in a highfidelity driving simulator. Human Factors, 44(2), 314-334.
Li, X., Oviedo-Trespalacios, O., Rakotonirainy, A., \& Yan, X. (2019). Collision risk management of cognitively distracted drivers in a car-following situation. Transportation Research Part F: Traffic Psychology and Behaviour, 60, 288-298.
Li, X., Rakotonirainy, A., Yan, X., \& Zhang, Y. (2018). Driver's visual performances in rearend collision avoidance process under the influence of cell phone use. Transportation Research Record, 1-9 In press.
Li, X., Yan, X., \& Wong, S. C. (2015). Effects of fog, driver experience and gender on driving behavior on S-curved road segments. Accident Analysis and Prevention, 77, 91-104.
Li, X., Yan, X., Wu, J., Radwan, E., \& Zhang, Y. (2016). A rear-end collision risk assessment model based on drivers' collision avoidance process under influences of cell phone use and gender- A driving simulator based study. Accident Analysis and Prevention, 97, 1-18.
Malaterre, G., Ferrandez, F., Fleury, D., \& Lechner, D. (1988). Decision making in emergency situations. Ergonomics, 31(4), 643-655.
Markkula, G., Benderius, O., Wolff, K., \& Wahde, M. (2012). A review of near-collision driver behavior models. Human Factors: The Journal of the Human Factors and Ergonomics Society, 54(6), 1117-1143.
McGehee, D. V., Mazzae, E. N., Baldwin, G. H. S., Grant, P., Simmons, C. J., Hankey, J., \& Forkenbrock, G. J. (2000). NHTSA light vehicle antilock brake research program task 5. 1: Examination of drivers' collision avoidance behavior using conventional and antilock brake systems on the Iowa Driving Simulator. (DOT HS 809 132) Washington, DC: National Highway Traffic Safety Administration.
Muttart, J. W. (2005). Factors that influence drivers' response choice decisions in video recorded crashes (technical paper 2005-01-0426). Society of Automotive Engineers.
Najm, W., Ranganathan, R., Srinivasan, G., Smith, J., Toma, S., Swanson, E., \& Burgett, A. (2013). Description of Light-Vehicle Pre-Crash Scenarios for Safety Applications Based on Vehicle-to-Vehicle Communications. DOT HS 811 731. NHTSA, U.S. Department of Transportation.
Underwood, G., Crundall, D., \& Chapman, P. (2011). Driving simulator validation with hazard perception. Transportation Research Part F: Traffic Psychology and Behaviour, 14(6), 435-446.
Wan, J., Wu, C., Zhang, Y., Houston, R. J., Chen, C. W., \& Chanawangsa, P. (2017). Drinking and driving behavior at stop signs and red lights. Accident Analysis and Prevention, 104, 10-17.
Wang, X., Zhu, M., Chen, M., \& Tremont, P. (2016). Drivers' rear end collision avoidance behaviors under different levels of situational urgency. Transportation Research Part C: Emerging Technologies, 71, 419-433.
Weber, S., Blum, K., Ernstberger, A., \& Färber, B. (2015). Standard reactions - Driver reactions in critical driving situations. Procedia Manufacturing, 3, 2489-2496.
Wong, S. C., Yan, X., Radwan, E., \& Li, Y. C. (2018). Special issue on "Driving simulation experiments and behavior analyses". Journal of Transportation Safety \& Security, 10, 1-4.
World Health Organization (WHO) (2015). Global status report on road safety 2015. http://www.who.int/violence_injury_prevention/road_safety_status/2015/en/.
Xiang, W., Yan, X., Weng, J., \& Li, X. (2016). Effect of auditory in-vehicle warning information on drivers' brake response time to red-light running vehicles during collision avoidance. Transportation Research Part F: Traffic Psychology and Behaviour, 40, 56-67.
Yan, X., Li, X., He, S., Weng, J., Wong, S. C., \& Pang, H. (2016). Effects of intersection field of view on emergent collision avoidance performance at unsignalized intersections: Analysis based on driving simulator experiments. Journal of Advanced Transportation, 50(5), 683-700.
Zhang, Y., Yan, X., Li, X., Wu, J., \& Dixit, W. (2018). Red-light-running crashes' classification, comparison, and risk analysis based on general estimates system (GES) crash database. International Journal of Environmental Research and Public Health, 15(6), 1290.
Zhang, Y., Yan, X., Li, X., \& Xue, Q. (2016). Drivers' eye movements as a function of collision avoidance warning conditions in red light running scenarios. Accident Analysis and Prevention, 96, 185-197.

Xiaomeng Li is a research fellow from the Centre for Accident Research and Road Safety - Queensland (CARRS-Q), Queensland University of Technology. She was awarded a PhD degree in January, 2017 from Beijing Jiaotong University. Her research mainly focuses on road traffic safety, driving performance, ITS and traffic engineering.

Andry Rakotonirainy is a professor from the Centre for Accident Research and Road Safety - Queensland (CARRS-Q), Queensland University of Technology. He has been proactive in investigating the use of existing and emerging ITS from multiple disciplines. It incorporates disciplines such as computer science, mathematics, human factors, engineering, psychology, and sociology. His research has made extensive use of driving simulators, traffic simulators and instrumented vehicles for developing system prototypes, assessing cost-benefits, understanding human errors and evaluating system deployment.

Xuedong Yan is a professor from the MOT Key Laboratory of Transport Industry of Big Data Application Technologies for Comprehensive Transport, Beijing Jiaotong University. His research expertise includes advanced driving simulator research, driving behavior and human factor, GIS application on traffic engineering, traffic safety and security, statistical analysis, traffic simulation, highway geometric design, highway-rail grade crossing, ITS, and urban design and planning.


[^0]:    * Corresponding author.
    E-mail addresses: xiaomeng.li@qut.edu.au (X. Li), r.andry@qut.edu.au (A. Rakotonirainy), xdyan@bjtu.edu.cn (X. Yan).

