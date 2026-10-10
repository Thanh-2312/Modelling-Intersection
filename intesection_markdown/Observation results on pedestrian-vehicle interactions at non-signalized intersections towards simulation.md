# Observation results on pedestrian-vehicle interactions at non-signalized intersections towards simulation 

Andrea Gorrini ${ }^{\mathrm{a}, *}$, Luca Crociani ${ }^{\mathrm{a}}$, Giuseppe Vizzari ${ }^{\mathrm{a}}$, Stefania Bandini ${ }^{\mathrm{a}, \mathrm{b}}$<br>${ }^{\mathrm{a}}$ Complex Systems and Artificial Intelligence research center, Department of Computer Science, Systems and Communication, University of Milano-Bicocca, Viale Sarca 336 - Ed. U14, 20126 Milan, Italy<br>${ }^{\mathrm{b}}$ Research Center for Advanced Science and Technology, The University of Tokyo, 4-6-1 Komaba, Meguro-ku, Tokyo 153-8904, Japan

## ARTICLE INFO

Article history:
Received 20 March 2017
Received in revised form 13 September 2018
Accepted 13 September 2018
Available online 1 October 2018

Keywords:
Pedestrian
Crossing behaviour
Ageing
Observation
Simulation


#### Abstract

The modelling and simulation of pedestrian-vehicle interactions is an open challenge for both research and practical computational solutions aiming at supporting urban/traffic decision makers and managers. The social cost of pedestrian-car accidents pushes the development of more effective and expressive computational models and simulation systems, integrating analytical knowledge, data and experience about pedestrian-vehicle interactions. The paper presents the results of a significant data gathering campaign focused on the considered phenomenon and aimed at supporting the extension and calibration of an existing model. A video-recorded naturalistic observation was executed in an area of the City of Milan (Italy) characterized by a significant presence of elderly inhabitants and by a high number of road accidents involving pedestrians in the past years. The achieved results include both macroscopic and microscopic indicators about pedestrianvehicle interactions at the observed non-signalized intersection, with reference to: (i) traffic volumes; (ii) Level of Service; (iii) drivers compliance to pedestrians right of way on zebra crossing; (iv) age-driven pedestrian crossing behaviour, focusing on motor skills (speeds and trajectories) and decision making (accepted time gap to cross). Since elderlies represent one of the most vulnerable pedestrians in terms of road accidents, data analysis is focused on comparing results among two samples composed of adults and aged pedestrians. Results showed that crossing behaviour is characterized by three main phases: approaching, appraising (evaluation of the distance and speed of oncoming vehicles) and crossing. Moreover, results showed a significant difference in the crossing behaviour of adult and elderly pedestrians. The final objective of the research is to support the development of a microscopic agent-based tool for simulating pedestrian-vehicle interactions at non-signalized crosswalks.


© 2018 Elsevier Ltd. All rights reserved.

## 1. Introduction

The role of computer-based systems for the simulation of vehicular traffic is a consolidated field of research and application that produced results whose level of maturity led to a significant impact on the activity of traffic engineers and planners in the design of efficient transportation networks (e.g., transportation planning, design and operations). Several successful models for the simulation of different aspects of vehicular traffic have been developed and applied: see Nagel,

[^0]Wagner, and Woesler (2003) for a review of different approaches, which include both cellular automata discrete models (Wang \& Ruskin, 2006) and continuous ones like car-following models (Kesting, Treiber, \& Helbing, 2007).

In parallel, the micro-simulation of pedestrian dynamics have also emerged and affirmed as supports to the assessment of the level of comfort and safety of crowded facilities in case of both ordinary and emergency operations. Computer-based simulations allow, in fact, to properly assess pedestrian circulation dynamics in mass transit and gathering spaces, and to support the design and planning of crowded facilities (e.g., effective positioning of entry and exit points). In analogy with vehicular traffic, the simulation of pedestrian behaviour has been tackled by different approaches, considering both continuous models, such as the social force (Helbing \& Molnar, 1995), and discrete ones based on the floor field method, such as cellular automata (Burstedde, Klauck, Schadschneider, \& Zittartz, 2001).

Whereas separately the above mentioned simulation approaches have produced a significant impact, efforts characterized by an integrated investigation on the simultaneous presence of vehicular traffic and pedestrian dynamics are not as frequent or advanced as isolated vehicular traffic and pedestrian models. With the exception of Helbing, Jiang, and Treiber (2005) and Zeng, Chen, Nakamura, and Iryo-Asano (2014), most efforts in this direction are relatively recent or they just analyse simple scenarios not even validated against real data about human behaviour.

In general, computer-based simulations of pedestrian-vehicle interactions allow to import a digital representation of a determined transportation facility and to populate it with a certain number of heterogeneous agents, which navigate the environment according to a set of behavioural rules and individual goals/preferences. Then, a series of analyses on simulation results can be performed to evaluate key performance indicators in order to test the efficiency and safety of alternative spatial layouts. Of course, to finalize simulations into decisions and operational steps it is necessary to consider the crucial contribution of social science in the definition of theories and empirical methods to study pedestrian-vehicle interactions. This is aimed at defining descriptive sets of metrics and parameters for characterizing the phenomenon and at supporting the development of computational models against real data (i.e. validation).

The most consolidated methodology to empirically study pedestrian-vehicle interactions is represented by the execution of unobtrusive naturalistic observations at urban intersections (the execution of controlled experiments is limited indeed by practical and ethical issues). The Highway Capacity Manual (HCM, 2010), for example, presents a series of results achieved through the systematic observation of traffic networks, describing general design standards for enhancing the efficiency of transportation facilities and the safety of road users. Other studies highlighted the impact of traffic volumes and quality of infrastructures on drivers compliance with crossing pedestrians (Varhelyi, 1998), as well as on pedestrians crossing decisions (Perumal, 2014). Several contributions coming from traffic psychology and safety science showed that crossing behaviour is determined by locomotion capability (Sisiopiku \& Akin, 2003), perceptive and attentional skills in evaluating the distance away and the speed of approaching vehicles (Hamed, 2001; Sun, Zhuang, Wu, Zhao, \& Zhang, 2015) and individual attitude towards hazardous situations (Evans \& Norman, 1998). In this framework, an innovative methodology is based on the possibility to use immersive virtual reality technologies (e.g., image-generation and projection system, virtual reality headmounted displays) to systematically measure pedestrian/vehicle interactions in a controlled and safe environment (Cavallo et al., 2016; Dommes, Cavallo, Dubuisson, Tournier, \& Vienne, 2014; Lehsing, Kracke, \& Bengler, 2015).

All these research efforts are driven by the necessity to develop advanced transportation strategies and safe infrastructure to contrast the social costs of pedestrian-car accidents. As highlighted by World Health Organization (2015), road accidents represent the eighth leading cause of death in the world population: 1.2 million people are killed on roads every year. Despite recent efforts, the measures currently in place to reduce the phenomenon are mainly aimed at protecting car occupants. However, pedestrians are some of the most vulnerable road users, with a percentage of fatalities corresponding to 22\% of the overall victims (26\% in EU, 14\% in USA).

Within vulnerable road users, we focused on the need to take into account the specific needs of elderly pedestrians. Aged pedestrians are indeed more likely to die or be seriously injured in road traffic collisions than adult people (Asher, Aresu, Falaschetti, \& Mindell, 2012) due to: (i) locomotion limitations (Oxley, Fildes, Ihsen, Charlton, \& Day, 1997; Winogrond, 1981) (e.g., reduced range of motion, loss of muscle strength and coordination, changes in posture, decreased walking speed) and (ii) perceptual-cognitive decline (Dommes, Cavallo, \& Oxley, 2013; Lobjois \& Cavallo, 2007; Webb \& Weber, 2003) (e.g., limited perception of light and colours, inability to tune out background noise, diminished attention and reaction time, spatial disorientation, slower decision-making). Previous works on the analysis and characterisation of age-driven pedestrian behaviour (Gorrini, Vizzari, \& Bandini, 2016) highlighted statistically significant differences between adult and elderly pedestrians, which might have an even greater importance within this context.

The rich and composite scenario depicted by the above considerations about pedestrian-vehicle interactions, led us to consider that additional empirical evidences could help the overall understanding of the phenomenon, and of the behavioural aspects of the involved stakeholders, towards the improvement of the results of initial experiences and explorations on its simulation. Earlier works on this line of research (Bandini et al., 2016; Crociani et al., 2014; Feliciani et al., 2017) represent, in fact, an attempt to define a baseline model, deliberately simplified, to evaluate its adequacy to reproduce the coordination between vehicles and pedestrians while, at the same time, successfully generate dynamics respecting stylized facts (e.g. increased pedestrian arrival rates reduce vehicular flow) and within plausible ranges when compared to empirical measurements available in the literature. Results of the present work represent a way to increase the expressiveness of such model and improve the quality of achieved simulation results.

Starting from these preliminary research efforts, the paper presents the results of an unobtrusive video-recorded observation focused on the direct interactions between crossing pedestrians and vehicles at a non-signalized intersection
(i.e. zebra cross-walk) in a two-way street located in the city of Milan (Italy). The achieved results rely on the systematic analysis of the collected video-images by means of different techniques, which allowed us to investigate the phenomenon considering both macroscopic and microscopic influencing factors. Moreover, data analysis is focused also on the study of age-driven pedestrian crossing behaviour, comparing results among adult and elderly pedestrians.

At a macroscopic level, data analysis was aimed at assessing the capacity of the infrastructure, considering the variability of the traffic demand over the time and the characteristics of the road users. Moreover, we also focused on the analysis of several significant indicators about the efficiency, comfort and safety of the observed intersection. First of all, we measured the traffic volumes in the considered scenario, by counting and characterizing the typologies and direction of travel of vehicles, as well as the direction of movement and profiles of pedestrians. Then, we measured the Level of Service of the observed scenario, by measuring the additional travel time experienced by drivers and pedestrians due to contextual traffic conditions. Moreover, we estimate the level of compliance of drivers to pedestrians right of way on zebra, considering different typologies of interactions among them and the impact of traffic volumes.

At a microscopic level, instead, we performed a video tracking analysis to achieve a microscopic parametric definition of crossing behaviour. In particular, results relies on the possibility to investigate pedestrians crossing decision, which is based on complex cognitive processes, by means of the analysis of observable behavioural indicators in case of direct interactions with approaching vehicles. Data analysis of pedestrians speeds allowed us to define the phenomenon as composed of three distinctive phases: (i) approaching; (ii) appraising (evaluation of the distance and speed of oncoming vehicles); (iii) crossing. Then, we focused on pedestrians crossing trajectories to test the impact of the spatial characteristics of the observed intersection on the phenomenon. Finally, we focused on the pedestrians evaluation of the distance and speed of approaching vehicles (time gap) to decide to pass safely avoiding collision.

The methodology which sets the current work is presented in Section 2, with reference to the description of the observed scenario and the data collection procedure. The results of the observation are presented in Section 3. The paper concludes with remarks about the achieved results and their future use as supports for the development and calibration of an integrated simulation tool for the representation of pedestrian/vehicle interaction in urban contexts. Future works based on ongoing data collection campaigns are presented at the end of the paper.

## 2. Methodology

The proposed methodology is based on the integration of data collection techniques (i.e. analysis), and the related activity of agent-based modelling and simulation (i.e. synthesis) (Bandini, Gorrini, \& Vizzari, 2014). In this framework, the current research work is based on the design and execution of a video-recorded observation, which was aimed at collecting a large dataset for characterizing pedestrian crossing behaviour at non-signalized intersections, considering also the potentially combined impact of pedestrians age and gender. From a general point of view, direct observation represents the true foundation of behavioural research (Gifford, 2016), since it allows to unobtrusively collect empirical data about human behaviour (subjects are not aware to be observed), and to consider the dynamic interaction with the physical features of the environment and the social context in which the subjects are situated.

Considering the objectives of the study, a preliminary analysis was performed to select the most appropriate scenario to perform the video-recorded observation. The analysis was based on crossing the geo-referred information related to the socio-demographic characteristics of the inhabitants of the city of Milan (Italy) and the localization of road traffic accidents. Results showed that the residential area of Via Padova is characterized by a significant presence of elderly inhabitants and an high number of pedestrian/car accidents involving pedestrians in the past years. ${ }^{1}$

A series of inspections were executed in the identified residential area in order to select a non-signalized intersection among others in Via Padova. The intersection between Via Padova, Via Cambini and Via Cavezzali (see Fig. 1) has been selected considering the large amount of people which pass through it due to several points of interest (e.g., local market, public offices, bank, supermarket, Church, Islamic cultural centre). The chosen scenario is characterized by a zebra striped (length: 11 m ) and a two-way street (speed limit: $50 \mathrm{~km} / \mathrm{h}$ ).

The video-footages were performed on May 18th, 2015 (from 10:45 am to noon) during the open-air local market, which is held every Monday in Via Cambini. The vehicular traffic toward Via Cambini was interdicted during the time of the observation due to the presence of the local market. Weather conditions during the observation were stable and sunny.

A HD camera with wide lens (1080p video resolution, 25 fps, ultra wide FOV) was positioned at a height of 25 m in correspondence of the selected zebra crossing. The camera was mounted on a light stand tripod overhung from the balcony of a private flat. The camera's built-in wireless allowed to control it by a remote device. The hidden position of the camera allowed to not influence the behaviour of drivers and pedestrians. Some spatial reference points have been taken to correct the distortion of video frames due to the wide lens and the nearly zenith perspective of the camera (see Fig. 1a).

[^1]![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-04.jpg?height=870&width=1213&top_left_y=179&top_left_x=338)
Fig. 1. (a) A video frame of the analysed measurement area. (b) A reproduction in scale of the observed scenario, with some annotations about vehicular traffic directions and the length of the zebra striped.

## 3. Results

### 3.1. Vehicular traffic volumes and pedestrian flows

A preliminary macroscopic analysis was focused on the estimation of the observed traffic volumes by measuring the bidirectional vehicular flows and pedestrian flows in the considered two-way street. According to traditional approaches in the field of transportation studies (HCM, 2010), this kind of analysis allows to assess the capacity of the infrastructure considering the variability of the traffic demand over the time. Moreover, the analysis of traffic volumes at non-signalized intersections can support decision makers and traffic managers in the design of practical solutions to enhance the safety of the infrastructure, considering for example the possibility to evaluate the necessity to implement a traffic light system and to intervene on its spatial layout (e.g., signage, speed bump, safety barrier for pedestrians). Beyond quantifying traffic volumes, we also characterized the observed vehicular and pedestrian flows to reach a more detailed dataset about vehicles typologies and pedestrians profiles.

According to the above described methodology, the vehicles travelling through the observed two-way street have been firstly counted minute by minute, and then classified considering to their directions of travel and typologies. Results (see Table 1) showed that the total amount of vehicles ( 1379 vehicles, 18.89 veh $/ \mathrm{min}$ ) was equally distributed in terms of direction of travel (see Fig. 2), and that cars were the large majority of vehicles (67\% of the total).

The pedestrians crossing on the observed intersection have been counted minute by minute and profiled according to their directions of movement, gender and age. The estimation of pedestrians gender and age has been performed by two independent coders, asking them to analyse the recorded video-images item by item considering a set of locomotion and physical indicators (e.g., walking pace, gait, posture, clothing, use of artefact for walking). To more thoroughly evaluate all these indicators the coders were asked to rewind the video and take the necessary time to profile pedestrians. A series of Cohen's Kappa analysis (Landis \& Koch, 1977) showed a substantial agreement between the two independent coders in the estimation of pedestrians age $(\mathrm{K}=0.69)$ and gender $(\mathrm{K}=0.77)$, confirming the consistency of results.

Results (see Table 1) showed that the $58 \%$ of the total amount of pedestrians ( 585 ped, 8.01 ped/min) walked from the crossing point A to B, while the 42\% of them crossed from point B to A. The observed pedestrian flows were mainly directed towards or were oncoming from the local market area situated in Via Cambini (see Fig. 2), which represents the main point of interest in the observed scenario. Pedestrians were equally distributed in terms of gender. Adults were the large majority of the total amount of pedestrians (71\%), but elderlies were a significant portion of it (24\%).

According to HCM (2010), the measured bidirectional traffic volumes are sufficiently high to envisage the implementation of a traffic light system to regulate the alternation of vehicular and pedestrian flows at the observed crossing. However, to reach an informed decision about this issue further and more extended observations should be performed, considering the potentially combined effect of peak hours and/or weather conditions on vehicular traffic volumes. Results about the

Table 1
Results about traffic volumes, with reference to vehicular and pedestrian flows.
| Vehicles | 1379 vehicles, 18.89 veh/min |
| :--- | :--- |
| Direction | 685 (50\%) vehicles toward the city centre, 693 (50\%) toward the neighbours |
| Typologies | 922 (67\%) cars, 181 (13\%) motorbikes, 115 (8\%) vans, 82 (6\%) bicycles, 43 (3\%) buses, 36 (3\%) trucks |
| Pedestrians | 585 crossing pedestrians, 8.01 ped/min |
| Direction | 340 (58\%) ped from point A to B, 245 (42\%) from point B to A |
| Gender | 307 (52\%) males, 278 (48\%) females |
| Age | 415 (71\%) adults (from about 18 y.o. until about 65 y.o.), 138 (24\%) elderly (from about 65 y.o.), 32 (5\%) young (until about 18 y.o.) |


![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-05.jpg?height=558&width=1060&top_left_y=627&top_left_x=409)
Fig. 2. The observed intersection, with the local market area in Via Cambini highlighted with a red dot (a). The origin and destination map of the counted vehicles and crossing pedestrians in the observed cross-walk (b). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

variability of the traffic demand over the time (see Table 2) showed indeed that the measured traffic volumes were stable during the observation, but a slight low peak level occurred at the end of the video-footages.

### 3.2. Level of service

Level of Service (LOS) (HCM, 2010) is a concept developed in the field of transportation studies to standardly describe the degree of comfort and safety afforded to drivers and pedestrians as they travel/walk through an intersection. Six grades are used to denote the various LOS from A to F, which are estimated by measuring the additional travel time experienced by drivers and pedestrians (i.e. stop-controlled delay) due to contextual traffic conditions, as an important indicator of the efficiency of an intersection.

LOS performance evaluation criteria change depending on the typology of the analysed transportation facility: the delay threshold for any given level of service is indeed less for non-signalized intersections than signalized intersections regulated by traffic light systems. Moreover, LOS criteria change depending on the estimation of the stop-controlled delay experienced by drivers and pedestrians at the same typology of intersection. At two-way non-signalized intersections LOS E is considered to represent the minimum acceptable design standard (see Table 3).

Stop-controlled delay of vehicles at non-signalized intersections is defined to include the initial deceleration delay, queue move-up time, stopped delay, and final acceleration delay, and it is caused by the contextual traffic conditions (vehicular

Table 2
Results about the variability of vehicular traffic volumes and crossing pedestrian flows during the time of the observation.
| Time intervals [min] | Bidirectional vehicular flows | Bidirectional pedestrian flows |
| :--- | :--- | :--- |
| 00:01-00:15 | 299 (22\%) | 138 (24\%) |
| 00:16-00:30 | 312 (23\%) | 136 (23\%) |
| 00:31-00:45 | 270 (20\%) | 138 (24\%) |
| 00:46-01:00 | 301 (22\%) | 102 (17\%) |
| 01:01-01:15 | 197 (14\%) | 71 (12\%) |
| Total | 1379 | 585 |


Table 3
Level of Service performance evaluation criteria for stop-controlled delay at two-way non-signalized intersections (HCM, 2010).
| LOS | Description of vehicular traffic/pedestrian dynamics | Delay of vehicles [s/veh] | Delay of pedestrians [s/ped] |
| :--- | :--- | :--- | :--- |
| A | - Nearly all drivers find freedom of operation<br>- Very seldom is there more than one vehicle in queue<br>- Very small delay to cross<br>- Low likelihood of risk-taking behaviour by pedestrians<br> | < 5 | < 10 |
| B | - Some drivers begin to consider the delay an inconvenience<br>- Occasionally there is more than one vehicle in queue<br>- Small delay to cross<br>- Low likelihood of risk-taking behaviour by pedestrians<br> | 5-10 | 10-15 |
| C | - Many times there is more than one vehicle in queue<br>- Most drivers feel restricted, but not objectionably so<br>- Small delay to cross<br>- Low likelihood of risk-taking behaviour by pedestrians<br> | 10-20 | 15-25 |
| D | - Often there is more than one vehicle in queue<br>- Drivers feel quite restricted<br>- Big delay to cross<br>- Moderate likelihood of risk-taking behaviour by pedestrians<br> | 20-30 | 25-35 |
| E | - Represents a condition in which the demand is near or equal to the probable maximum number of vehicles that can be accommodated by the movement<br>- There is almost always more than one vehicle in queue<br>- Drivers find the delays approaching intolerable levels<br>- Very big delay to cross<br>- High likelihood of risk-taking behaviour by pedestrians<br> | 30-45 | 35-50 |
| F | - Forced flow<br>- Represents an intersection failure condition that is caused by geometric and/or operational constraints external to the intersection<br>- Very big delay to cross<br>- High likelihood of risk-taking behaviour by pedestrians<br> | > 45 | > 50 |


traffic volumes and crossing pedestrian flows). Stop-controlled delay of pedestrians at non-signalized intersections, instead, includes the waiting and start-up delay, and it is caused by the non-compliance of drivers to their right-of-way on zebra crossings.

The Level of Service of the observed intersection has been estimated by time stamping minute by minute the amount of delay experienced by the total number of counted drivers and crossing pedestrians (see Table 4). Results showed that both the average stop-controlled delay of vehicles (3.11 s/veh ± 2.73 sd) and pedestrians (1.31 s/ped ± 0.31 sd) corresponded to LOS A. In conclusion, results about the measured Level of Service showed that a good degree of comfort and safety for those drivers and pedestrians who were travelling/walking through the observed non-signalized intersection: nearly all drivers found freedom of operation, and pedestrians experienced a very small delay to cross with low risk-taking crossing behaviour.

### 3.3. Drivers' compliance to crossing pedestrians' right-of-way

The non-compliance of road users to traffic norms is caused by several factors (e.g., deliberate violation of norms, inattention, scarce visibility of signage) and it is undoubtedly one of the main causes of accidents at intersections. At non-signalized zebra crossings the compliance of drivers to traffic laws, which require them to slow down or to arrest in proximity of the zebra yielding crossing pedestrians, plays a crucial role to avoid accidents, due to the absence of semaphore systems regulating the alternation of traffic flows.

Table 4
Results about the measured stop-controlled delay of vehicles and pedestrians at the observed intersection, and the estimated Level of Service.
| Time intervals [min] | Delay of vehicles [s/veh] | LOS | Delay of pedestrians [s/ped] | LOS |
| :--- | :--- | :--- | :--- | :--- |
| 00:01-00:15 | 3.79 | A | 1.38 | A |
| 00:16-00:30 | 2.18 | A | 1.40 | A |
| 00:31-00:45 | 7.52 | A | 1.73 | A |
| 00:46-01:00 | 1.50 | A | 1.15 | A |
| 01:01-01:15 | 0.57 | A | 0.91 | A |
| Average | $3.11 \pm 2.73 \mathrm{sd}$ | A | $1.31 \pm 0.31 \mathrm{sd}$ | A |


![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-07.jpg?height=423&width=1068&top_left_y=582&top_left_x=399)
Fig. 3. The work flow which guided the coders in the selection and analysis of the crossing episodes from the video-images.

A preliminary analysis of the video images made clear a scarce level of compliance of drivers to pedestrians right-of-way at the considered zebra crossing. For this reason, we systematically studied the phenomenon by selecting a sample of 812 crossing episodes from the video (59\% of the total sample of counted vehicles). To do so, we considered only the cases in which one vehicle directly interacted with one or more pedestrians crossing from the near or the opposite side-walk (see Fig. 3). Then, we measured the level of compliance of drivers to pedestrians right of way, considering four typologies of interaction:

1. pedestrian approaching the zebra from the near side-walk;
2. pedestrian waiting at the curb of the near side-walk to cross;
3. pedestrian crossing on the zebra from the near side-walk;
4. pedestrian approaching/waiting/crossing from the opposite side-walk.

Results (see Table 5) showed that the 48\% of the total number of crossing episodes was characterized by non-compliant drivers with crossing pedestrians, either if they were approaching, waiting or crossing from the two side-walks. The 52\% of the total, instead, was characterized by compliant drivers. In particular, 6 episodes were characterized by non-compliant drivers with pedestrians crossing from the near side-walk and already occupying the zebra. Instead of stopping or slowing down in proximity of the zebra crossing, drivers accelerated or sharply steered, with potentially risky interactions. Moreover, results showed that drivers were more compliant to pedestrians approaching/waiting/crossing from the opposite side-walk (58\% of the total), compared to the crossing episodes from the near side-walk (46\% of the total).

We further analysed data by computing a Person correlation coefficient ${ }^{2}$ in order to test the effect of traffic volumes on drivers compliance (see Fig. 4a and b). There was a negative correlation between the percentage of non-compliant drivers and the total number of vehicles per minute $[\mathrm{r}=-0.285, \mathrm{n}=73, \mathrm{p}=0.015]$, and a positive correlation between the percentage of non-compliant drivers and the total number of pedestrians per minute $[\mathrm{r}=0.465, \mathrm{n}=73, \mathrm{p}<0.001]$. A multiple linear regression (see Fig. 4c) was calculated to predict the percentage of non-compliant drivers based on: (i) total number of vehicles per minute ( $\mathrm{p}=0.007$, significant predictor) and (ii) total number of crossing pedestrians per minute ( $\mathrm{p}<0.001$, significant predictor). A significant regression equation was found $[\mathrm{F}(2,70)=14.526, \mathrm{p}<0.001]$, with $\mathrm{R}^{2}$ of 0.293 . The predicted non-compliance of drivers is equal to 0.303-0.008 (number of vehicles) +0.18 (number of pedestrians).

In conclusion, results highlighted the scarce level of compliance of drivers to pedestrians right of way at the considered non-signalized intersection. Despite that, no accidents have been detected from the video-images, thanks to a general cautious attitude of pedestrians which yielded non-compliant drivers. The analysis showed also that drivers are more compliant to crossing pedestrian when vehicular traffic volumes increase, probably due to an overall speed reduction and queues

[^2]Table 5
Results about drivers compliance to pedestrians right of way at the observed non-signalized intersection.
| Typologies of pedestrian/vehicle interactions | Compliant drivers | Non-compliant drivers |
| :--- | :--- | :--- |
| 1. Ped. approaching the zebra from the near side-walk | 95 (38.46\%) | 152 (61.54\%) |
| 2. Ped. waiting at the curb of the near side-walk to cross | 70 (51.85\%) | 65 (48.15\%) |
| 3. Ped. crossing on the zebra from the near side-walk | 26 (81.25\%) | 6 (18.85\%) |
| 4. Ped. approaching/waiting/crossing from the far side-walk | 230 (57.69\%) | 168 (42.21\%) |
| Ped. from the near side-walk | 191 (46.14\%) | 223 (53.86\%) |
| Ped. from the far side-walk | 230 (57.79\%) | 168 (42.21\%) |
| Total (812 crossing episodes) | 421 (51.85\%) | 391 (48.15\%) |


![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-08.jpg?height=1144&width=1086&top_left_y=621&top_left_x=403)
Fig. 4. The significant correlation between: (a) the percentage of non-compliant drivers and vehicular flow, (b) the percentage of non-compliant drivers and crossing pedestrian flow. The results of the multiple linear regression analysis (c) about the predicted percentage of drivers non-compliance considering the combined impact of vehicular and pedestrian flows. Each data refers to one minute of the video.

formation. Moreover, the increase of pedestrian flows on the zebra made drivers generally less compliant, probably due to their deliberative violation of norms to do not accumulate excessive delay yielding a large number of crossing pedestrians.

### 3.4. Pedestrian speeds and crossing phases

Beyond the above presented results about the measured traffic volumes, Level of Service and drivers compliance, which described the observed pedestrian and vehicular traffic dynamics at a macroscopic level of investigation, the collected videoimages have been further analysed to achieve a microscopic parametric definition of pedestrian crossing behaviour at the observed non-signalized intersection. A notable remark about this Section consists in the possibility to achieve an inductive definition of crossing decision, which is based on perceptive-attentional skills and complex cognitive processes, by means of the analysis of observable behavioural indicators about pedestrians locomotion (i.e. trajectories, speeds) in case of direct interactions with approaching vehicles. This kind of result is a fundamental element for the definition of an integrated

Table 6
The description of the sub-sample of crossing episodes considered for the video tracking analysis.
| Number of crossing episodes | 50 episodes |
| :--- | :--- |
| Types of crossing episodes | 21 episodes with only one vehicle from the near lane, 29 multiple interactions with two vehicles (near and far lanes) |
| Direction of pedestrians | 27 ped. crossing from point A to B, 23 ped. from point B to A |
| Age of pedestrians | 27 adults (from about 18 y.o. until about 65 y.o.), 23 elderly (from about 65 y.o.) |
| Gender of pedestrians | 22 males, 28 females |
| Typology of vehicles | 77 cars, 1 motorbike, 1 bus |


microscopic simulator of pedestrian and vehicle interaction, able to generate what-if scenarios complementing and potentially providing additional insights with respect to existing forms of static analyses.

In particular, a video tracking analysis has been performed considering a sub-sample of 50 crossing episodes (see Table 6), which were selected avoiding situations such as: platooning of vehicles on the roadway inhibiting a crossing episode, the joining of pedestrians already crossing, the presence of cars parked nearby the zebra limiting the visibility of road users, and in general situations influencing the direct interaction between the pedestrian and the driver. Part of the selected episodes was characterized by the multiple interaction between the pedestrian and two vehicles oncoming from the near and the far lane. Moreover, the episodes have been sampled considering the impact of pedestrians age and gender, and the effect of the different spatial layout of crossing points A and B.

The analysis was performed by using the software Tracker Video Analysis and Modeling Tool, ${ }^{3}$ which allowed to correct the distortion of the video images, and then to track the positions of pedestrians and vehicles while interacting in the observed intersection. The tracking analysis was executed by pointing at the frontal plates of vehicles and at the space in between the feet of pedestrians. The data set (including the $X, Y$ coordinates and the associated frames $t$ ) was exported for data analysis.

The speed of pedestrians have been analysed among the time series of video frames (i.e. time series analysis) (Wei, 2006), as characterized by: (i) a stable trend on side-walk; (ii) a significant deceleration in proximity of the curb; (iii) an acceleration on the zebra-striped. The time series of speed values was executed by calculating the difference between: the moving average of pedestrian speed values (MA, time period length: 0.8 s, three frames) and the cumulative average (CA) of the all speed values (entire frames series). This allowed to smooth out short-term fluctuations of data (intrinsically due to pedestrian gait, but also caused by the frame discretization) and to highlight longer-term trends (deceleration/acceleration). According to results, we defined a parametric description of crossing behaviour as composed of three distinctive phases (see Fig. 5):

1. Approaching phase: the pedestrian travels on the side-walk with a relatively stable speed (Speed MA - CA $\simeq 0$ );
2. Appraising phase: the pedestrian approaching the cross-walk decelerates to evaluate the distance and speed of oncoming vehicles (decision making). We decided to consider that this phase starts with the first value of a long-term deceleration trend (Speed MA - CA < 0);
3. Crossing phase: the pedestrian decides to cross and speeds up. The crossing phase starts from the frame following the one with the lowest value of speed before a long-term acceleration trend (Speed min).

A two-factors analysis of variance (two-way ANOVA) showed a significant difference among the speeds of pedestrians while approaching, appraising and crossing $[\mathrm{F}(2,144)=61.944, \mathrm{p}<0.0001]$, and a significant effect of pedestrian age on results $[\mathrm{F}(1,144)=63.751, \mathrm{p}<0.0001]$ (see Table 7 and Fig. 6). A series of post hoc Tukey test showed a non significant difference between the speeds of pedestrians while approaching and crossing, considering both adults and elderlies (p > 0.05). The difference between the speed of adults and elderlies was significant among all the three crossing phases (p < 0.0001). A one-factor analysis of variance (one-way ANOVA) showed that there was no a significant effect of gender on the speeds of pedestrians while approaching $(\mathrm{p}>0.05)$, appraising $(\mathrm{p}>0.05)$ and crossing $(\mathrm{p}>0.05)$ (see Table 7).

In conclusion, results (see Fig. 7) demonstrated that pedestrian crossing behaviour is based on a significant deceleration in proximity of the curb (appraising phase) to evaluate the distance and speed of oncoming vehicles and safely cross. While the existence of such phase might not necessarily represent an original evidence, its characterisation and measurement represents an interesting result once again especially considering the final aim of supporting the definition of microscopic models and simulators for this kind of scenario. A further consideration, concerns the need to embed heterogeneity in these models: in fact, results showed also that elderlies walked in average 22\% slower than adults among the three crossing phases, and they decelerated 6\% more than adults while appraising. This demonstrated the impact of ageing on crossing behaviour in terms of motor skills decline.

The presented results highlighted the possibility to achieve a microscopic parametric definition of crossing decision, by means of the analysis of observable behavioural indicators about pedestrians trajectories and speeds. This allows to define crossing behaviour as characterized by three distinctive phases (i.e. approaching, appraising, crossing), which are referred to the direct interactions with oncoming vehicles and to the contextual spatial information of the observed non-signalized intersection.

[^3]![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-10.jpg?height=413&width=1013&top_left_y=183&top_left_x=443)
Fig. 5. An exemplification of the trend analysis performed on the time series of speeds. The starting time of the appraising and crossing phases are highlighted with black dots.

Table 7
The speeds of adult and elderly pedestrians, and the speeds of male and female pedestrians, among the three phases: approaching, appraising, crossing.
| Phases | Speed of adult pedestrians | Speed of elderly pedestrians |
| :--- | :--- | :--- |
| Approaching phase | $1.28 \mathrm{~m} / \mathrm{s} \pm 0.18 \mathrm{sd}$ | $1.03 \mathrm{~m} / \mathrm{s} \pm 0.18 \mathrm{sd}$ |
| Appraising phase | $0.94 \mathrm{~m} / \mathrm{s} \pm 0.21 \mathrm{sd}$ | $0.69 \mathrm{~m} / \mathrm{s} \pm 0.23 \mathrm{sd}$ |
| Crossing phase | $1.35 \mathrm{~m} / \mathrm{s} \pm 0.18 \mathrm{sd}$ | $1.09 \mathrm{~m} / \mathrm{s} \pm 0.17 \mathrm{sd}$ |
| Phases | Speed of male pedestrians | Speed of female pedestrians |
| Approaching phase | $1.19 \mathrm{~m} / \mathrm{s} \pm 0.19 \mathrm{sd}$ | 1.13 m/s ± 0.24 sd |
| Appraising phase | $0.81 \mathrm{~m} / \mathrm{s} \pm 0.25 \mathrm{sd}$ | $0.85 \mathrm{~m} / \mathrm{s} \pm 0.26 \mathrm{sd}$ |
| Crossing phase | $1.25 \mathrm{~m} / \mathrm{s} \pm 0.20 \mathrm{sd}$ | $1.21 \mathrm{~m} / \mathrm{s} \pm 0.24 \mathrm{sd}$ |


![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-10.jpg?height=544&width=1183&top_left_y=1191&top_left_x=357)
Fig. 6. The trajectories of crossing pedestrians plotted with the results of the trend analysis of speeds, which highlighted the difference of speeds among the crossing phases. Pedestrians trajectories are superimposed on a reproduction in scale of the observed zebra crossing.

### 3.5. Spatial analysis of crossing phases and pedestrians trajectories

The above presented results about pedestrians trajectories and speeds allowed to achieve a microscopic definition of crossing behaviour as characterized by three distinctive phases (i.e. approaching, appraising, crossing). The following Section is aimed at contributing in the understanding of the phenomenon, focusing on the spatial characteristics of the observed intersection.

Generally speaking, the crossing point A is characterized by a large side-walk area, and by the presence of a ramp to facilitate the access to the side-walk for those people with limited mobility. The crossing point B is characterized, instead, by a small and interrupted side-walk area, and by the presence of various obstacles (e.g., traffic signal pals, taxi station telephone exchange) (see Fig. 1b). According to these preliminary considerations about the observed scenario, data analysis was firstly focused on the localization of pedestrians when they started appraising and crossing to estimate their distance from the curbs at the two side-walks (see Fig. 8). Then, we tested the impact of the different spatial layouts of points A and B on crossing behaviour.

![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-11.jpg?height=554&width=1157&top_left_y=177&top_left_x=351)
Fig. 7. The speed of adult and elderly pedestrians among the crossing phases. The Box and Whisker plot reports: local maximum value, 75th percentile, mean, median (highlighted in red), the 25th percentile and the local minimum value. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-11.jpg?height=651&width=1171&top_left_y=913&top_left_x=349)
Fig. 8. The positions of pedestrians when they started appraising (blue dots) and crossing (red ones) at points A and B. Pedestrians trajectories are superimposed on a reproduction in scale of the observed zebra crossing. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

Moreover, since preliminary analysis showed that pedestrians walked partially outside the cross-walk by taking an oblique path, we further analysed the length and direction of crossing trajectories to evaluate how the spatial features of the observed intersection and the presence of the local market situated in Via Cambini affected the crossing behaviour of the tracked pedestrians.

Results showed that at point A, pedestrians started appraising $2.85 \mathrm{~m}( \pm 1.45 \mathrm{sd})$ before the curb and they started crossing 0.12 m (±1.02 sd) before the curb. At point B, pedestrians started appraising 0.89 m (±1.19 sd) before the curb, but they started crossing 1.17 m (±1.51 sd) after it, occupying the road way. A series of independent samples t-tests showed that the age and gender of pedestrians did not significantly impact results $(\mathrm{p}>0.05)$, considering both crossing points A and B.

Results showed that the average length of trajectories of crossing pedestrians (12.05 m ± 0.58 sd) was 9\% longer compared to the shortest path between the curb of points A and point B (which corresponds to 11 m). Instead of walking straight, pedestrians walked partially outside the cross-walk by taking an oblique path which made them partially occupying the road way (see Fig. 8). A series of independent sample t-test analyses showed that the direction of movement (from crossing point A to B, and vice versa) did not significantly impact results $(\mathrm{p}>0.05)$, as well as the age and gender of pedestrians $(\mathrm{p}>0.05)$.

In conclusion, results demonstrated that the spatial features of the crossing point A allowed pedestrians to safely evaluate the distance and speed of oncoming vehicles (appraising phase) from the large side-walk area. Moreover, the ramp was found to make pedestrians crossing more safely, by gathering them toward the centre of the zebra-striped. Results showed also the negative impact of the spatial layout of crossing point B on pedestrian crossing behaviour. The small and interrupted
side-walk, and the presence of various obstacles, impeded pedestrians to cross in a safe manner making them occupying the road way during the appraising phase, with potentially risky situations and collisions with oncoming vehicles.

Moreover, the presence of the local market situated in Via Cambini negatively affected the crossing behaviour of pedestrians, who were found to walked partially outside the zebra occupying the road way. This phenomenon, defined as overflow violation (HCM, 2010), is indeed generally caused by the tendency of pedestrians to take the shortest path to their destination (Turner \& Penn, 2002). For these reasons, results suggest the possibility to implement practical design solutions to avoid overflow violation at the observed intersection (e.g., enlarging the side-walk area at crossing point B , setting safety barriers to direct pedestrians to the local market in Via Cambini).

### 3.6. Crossing decision and accepted time gap

As previously described in Section 3.4 one of the most innovative results presented in this paper is based on the possibility to inductively investigate pedestrians crossing decision by means of the analysis of observable behavioural indicators about their trajectories and speeds. The following Section is aimed at deepening the understanding of the phenomenon, presenting the results of a series of analyses focused on pedestrians decision to cross in case of direct interactions with approaching vehicles.

In particular, we use the term accepted time gap to denote the ratio between the pedestrians's evaluation of the distance of an approaching vehicle (measured on the X-axis) and its average speed (not taking into account acceleration/deceleration trends). In analogy with the previously proposed definition of the appraising phase, the evaluation of the accepted time gap allows pedestrians to decide to pass safely avoiding collision.

The achieved results relies on a supplementary video tracking analysis which was aimed at measuring the trajectories and speeds of vehicles, while directly interacting with the considered sample of crossing pedestrians. In particular, results are based on the estimation of the distance and speed of vehicles when pedestrians decide to cross and speed up (i.e. starting time of crossing phase, from the frame after the one with the lowest value of speed before a long-term acceleration trend).

The results presented in this Section (see Table 8, Figs. 9 and 10) are based on the analysis of the time gap accepted by pedestrians in case of different typologies of interactions with vehicles and different, as well as considering different pedestrians profiles in terms of age and gender. In particular, since crossing decision involves the complex coordination of locomotor abilities and perceptive/attentional skills, we considered several factors potentially influencing pedestrians crossing decision. First of all, we compared results considering the lane occupied by the oncoming vehicle (oncoming from near lane or far lane). Then, focused on single and multiple pedestrian/vehicle interactions (one pedestrian interacting with only one vehicle or two vehicles oncoming from the near and the far lanes). Finally, we tested the impact of pedestrians age and gender on results.

A series of independent samples t-tests showed that crossing pedestrians did not discriminate between the distances and speeds of vehicles oncoming from the near (accepted time gap $=4.10 \mathrm{~s} \pm 2.43 \mathrm{sd}$ ) and the far lanes (accepted time gap $=4.39$ $\mathrm{s} \pm 1.92 \mathrm{sd}$ ). Data analysis showed also that there was not a significant difference (p > 0.05) between the accepted time gaps

Table 8
The average time gap accepted by crossing pedestrians, considering the impact of different typologies of interactions with vehicles and pedestrians profiles.
| Veh. from the near lane | Veh. from the far lane | Single int. | Multiple int. |
| :--- | :--- | :--- | :--- |
| $4.10 \mathrm{~s} \pm 2.43 \mathrm{sd}$ Adult ped. | $4.39 \mathrm{~s} \pm 1.92 \mathrm{sd}$ Elderly ped. | $3.61 \mathrm{~s} \pm 2.18 \mathrm{sd}$ Male ped. | $4.20 \mathrm{~s} \pm 2.24 \mathrm{sd}$ Female ped. |
| $3.98 \mathrm{~s} \pm 2.55 \mathrm{sd}$ | $4.49 \mathrm{~s} \pm 1.77 \mathrm{sd}$ | $3.84 \mathrm{~s} \pm 1.86 \mathrm{sd}$ | $4.62 \mathrm{~s} \pm 2.57 \mathrm{sd}$ |


![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-12.jpg?height=441&width=1007&top_left_y=1844&top_left_x=441)
Fig. 9. The accepted time gap by crossing pedestrians, considering the impact of different typologies of interactions with vehicles and pedestrians profiles. The Box and Whisker plot reports: local maximum value, 75th percentile, mean, median (highlighted in red), the 25th percentile and the local minimum value. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-13.jpg?height=874&width=1167&top_left_y=177&top_left_x=349)
Fig. 10. The positions of pedestrians when they started crossing (red dots). Squared dots refer to the position of vehicles on the near and far lanes, and their speeds. The charts report the central line of the road way and spatial references of the zebra-striped crossing. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

in a situation comprising one vehicle approaching from the near lane (4.12 s ± 2.45 sd) or two vehicles respectively oncoming from the near and far lane (4.20 s ± 2.24 sd). A series of two-way ANOVA showed the non significant impact of the factors age $(\mathrm{p}>0.05)$ and gender (p > 0.05) on results. The accepted time gaps of adult (3.98 s ± 2.55 sd) and elderly pedestrians (4.49 s ± 1.77 sd) did not differ significantly in any of the tested crossing typologies (approaching vehicle from the near or far lane; single or multiple interaction), as well as the ones of male (3.84 s ± 1.86 sd) and female pedestrians (4.62 s ± 2.57 sd).

In conclusion, data analysis showed that the achieved results did not significantly differ considering the impact of the typologies of interaction with oncoming vehicles and pedestrians profiles. The average time gap accepted by the tracked pedestrians to safely cross in the observed non-signalized intersection corresponded to 4.20 s ± 2.24 sd (average distance of vehicle $=16.83 \pm 8.71 \mathrm{sd}$; average speed of vehicles $=15.93 \pm 7.02 \mathrm{~km} / \mathrm{h}$ ). However, further data analysis on age-driven crossing decision have been performed, comparing data between adult and elderly pedestrians. In particular, an independent samples t-test showed a significant difference between the time duration of the appraising phase among elderly (4.12 s ± $2.54 \mathrm{sd})$ and adult pedestrians $(2.79 \mathrm{~s} \pm 1.47 \mathrm{sd}), \mathrm{t}(48)=2.40658, \mathrm{p}=0.012$. Although pedestrians have the right of way on zebra-striped, elderly were found to be more cautious than adults: $57 \%$ of them gave way to at least one approaching vehicle, compared to 30\% of adults. This result suggested that, when elderly pedestrians decided to cross, they were able to regulate their behaviour by adapting the accepted time gap to their own crossing capacities (lower walking speed).

## 4. Requirements for integrated pedestrian crossing models

The above described results can be considered from the perspective of a modeller that wishes to represent crossing dynamics in a model incorporating both vehicles and pedestrians, for the evaluation of alternative choices for the regulation of the crossing itself or environmental configurations. Specific take home messages for such an enterprise are:

- pedestrians are heterogeneous: they should be classified into categories related to age, which influences several observable indicators on their dynamics (i.e. walking and crossing speed, appraising time) whereas gender is not statistically significant from this perspective;
- pedestrian appraising of the possibility to safely cross is a measurable and significant phase (again, depending on the type of pedestrian), not an instantaneous decision;
- this phase does not necessarily begin in a specific position with respect to the curb, but it rather depends on the actual distance between the approaching pedestrian and the area potentially occupied by a crossing vehicle, as shown in Fig. 8.

Previously mentioned integrated models for the simulation of the impact of pedestrian crossing on vehicle flow can be easily extended to represent heterogeneous pedestrian types (see, e.g. Bandini, Crociani, \& Vizzari, 2017 for discrete
modeling approaches that are the ones for which this requirement seems more problematic). Some of them employ the notion of anticipation of the movement of other relevant entities to perform crossing decisions (Bandini et al., 2016; Crociani et al., 2014; Feliciani et al., 2017): all relevant entities project in the model of the environment an intention of movement; when two intentions overlap a potential conflict is detected and the involved entities negotiate who will cross or yield, according to contextual conditions (e.g. a pedestrian could yield to a car too close or fast to safely stop before the crossing site). In general, however, this negotiation is instantaneous. The results of this analysis call for modifications on this approach to achieve better results, and in particular:

- a crossing appraising phase must be introduced for pedestrians;
- the anticipation mechanism can be plausibly employed to trigger the beginning of this phase: as shown in Fig. 11, if both vehicles and pedestrians project in the environmental model a potential future occupation of space, whose size is to be determined on employing the achieved data but is intuitively associated to the actual velocity of the generating entity (i.e. longer for a vehicle and much smaller for a pedestrian), the model can trigger the appraising phase for pedestrians in different points according to the fact that they can perceive a potential future conflict with a vehicle, irrespectively of the actual position (close or relatively far from the curb);
- the duration of the appraising phase is, according to the acquired data, relatively stable and, again, age dependent; from this perspective, we could consider the possibility to reduce the pedestrian desired walking speed gradually during this phase which lasts a different number of turns according to the type of pedestrian and finally leads to a cross/do not cross decision.

A model based on earlier approaches modified according to these lines of work still considers drivers to be uniformly compliant to pedestrians right of way: acquired data show that this does not happen in reality (with different rates of compliance also in relationship to the specific cultural contexts). From this perspective, this study calls for additional analyses about the factors influencing the drivers' decisions to comply to the rules. The basic assumption of some of the above cited approaches, that is, a collaborative attitude of the involved actors (e.g. a pedestrian detecting a vehicle that is too close and/ or too fast to safely reach a stop will yield, despite having the right of way), seem a plausible starting point for further analyses.

## 5. Conclusions and future works

The issue of developing efficient transportation strategies is becoming a mandatory requirement for municipalities to enhance the quality of life and the safety of the citizens. In particular, the social cost of pedestrian-car accidents pushes the development of a new generation of computational models integrating analytical knowledge, data and experience about the complex dynamics occurring in pedestrian/vehicle interactions, supporting urban and traffic decision makers and managers.

The current work presented the results of a video-recorded observation focused pedestrian crossing behaviour at nonsignalized intersection. Moreover, since old people are the most vulnerable road users in terms of pedestrian-car accidents (Asher et al., 2012), we focused the impact of age on crossing behaviour. The observation was performed in an area of the city of Milan (Italy) characterized by a significant presence of elderly inhabitants and by a high number of pedestrian accidents in

![](https://cdn.mathpix.com/cropped/a8c36d29-747c-476c-aec0-d55e2f322c16-14.jpg?height=610&width=1142&top_left_y=1701&top_left_x=377)
Fig. 11. A schematic representation of the anticipation mechanism for the triggering of the crossing appraising phase: pedestrians A and B are about to start their appraising phases, despite having different distances from the curb, whereas pedestrian C is still too far from the crossing zone.

Table 9
The results of the interviews which focused on the walkability degree perceived by the elderly pedestrians while walking and crossing in the observed intersection.
| Questions (1-10 rating scale) and most cited critical aspects | Rating score |
| :--- | :--- |
| 1. How much pleasant is to walk in this area of the neighbourhood?<br>- Danger (38\%)<br>- Dirt (28\%)<br>- Scarce greenery (26\%)<br> | $5.27 \pm 1.55 \mathrm{sd}$ |
| 2. Is there enough space to walk on the side walks?<br>- Irregular parking (30\%)<br>- Bad pavements conditions (21\%)<br>- Cycling on the pavements (20\%)<br> | $6.05 \pm 1.28 \mathrm{sd}$ |
| 3. Is it easy to cross the street?<br>- Absence of a traffic light (62\%)<br>- Insufficient time to cross the road (34\%)<br>- Parked cars obstructing pedestrians' view (25\%)<br> | $4.37 \pm 1.59 \mathrm{sd}$ |
| 4. How much do you think drivers behave well toward pedestrians?<br>- Driving speed (57\%)<br>- Drivers not stopping near zebra crossing (56\%)<br>- Double-parking habit (28\%)<br> | $4.30 \pm 1.58 \mathrm{sd}$ |


the past years. The achieved results are aimed at supporting the development and the parametric calibration of advanced simulation systems, focusing on several behavioural rules regulating pedestrians crossing decision making (Crociani et al., 2014; Feliciani et al., 2017).

Result showed that crossing behaviour is based on three sequential phases (approaching, appraising, crossing), characterized by deceleration/acceleration trends. In particular, pedestrians appraising phase is based on a significant deceleration of speeds in proximity of the zebra-striped crossing to evaluate in time the distance and speed of oncoming vehicles (decision making). Results showed that elderly pedestrians walked significantly slower than adults on the zebra and that they spent more time to take decision to cross. This demonstrated the negative impact of ageing on crossing behaviour in terms of motor skills decline and decision making.

Other analogous studies (Dommes et al., 2014; Oxley et al., 1997) demonstrated that older people have difficulty to take the far lane into account in their crossing decision. However, the achieved results showed no significant difference between the time gap accepted by adults and aged pedestrians while evaluating the distance and speed of vehicles oncoming from the near and the far lanes (in average: 4.13 s ± 2.30 sd), with no risk-taking crossing decision. In particular, elderly pedestrians were found to regulate their crossing behaviour by behaving in a more cautious manner and by adapting the accepted time gap to their own crossing capacities (lower walking speed).

The results about the observed LOS showed that nearly all drivers found freedom of operation and that pedestrians experienced a very small delay to cross with low risk-taking crossing behaviour. However, the comparison of results among the spatial analysis of crossing phase at point A and B highlighted that the lack of adequate space and ramp on side-walk at point B made pedestrian crossing in a unsafe manner, occupying the road way. Results demonstrated how much is important to design accessible and safe infrastructures to guarantee the security of pedestrians in urban intersections (e.g., side-walk discontinuity and condition, lack of curb ramps, obstructions in walkway, limited visibility).

In order to assess the level of comfort and safety perceived by pedestrians while walking and crossing in the observed intersection (i.e. walkability degree) (Speck, 2013), we performed a further analysis based on a series of interviews executed on May and June 2015 with a sample of aged pedestrians (122 people, 59 males, 63 females, 77 y.o. ± 6.9 sd). The interviews have been performed by using the "Walkability Checklist: How Walkable is your Community?", a standard measure of walkability designed by the US Department of Transportation, United States Environmental Protection Agency. ${ }^{4}$

Results (see Table 9) showed that the interviewed elderly pedestrians perceived the walkability degree of the area as medium-low $(5.00 \pm 1.11 \mathrm{sd})$, above all considering the perceived safety while crossing at the non-signalized intersection. This could be generally explained as related to the scarce compliance of drivers in giving to pedestrians the right of way on zebra crossing, and the consequent perceived risky interaction with vehicles while crossing.

Ongoing works are based on further analyses of the recorded video frames to investigate the speed adaptation of vehicles in proximity of the zebra crossing (drivers appraising phase) (Varhelyi, 1998), as well as non-compliant jaywalking behaviour of pedestrians out of zebra-striped crossing. Moreover, since the analysis of pedestrian profiles showed that the 35\% of the observed population was composed of walking groups, future works will be aimed at testing the impact of grouping on crossing behaviour, comparing results among single pedestrians and dyads. Several works present in the literature, such as Wagner (1981), highlighted indeed that group members use social information, such as the crossing behaviour of others, to judge the safety gap from oncoming vehicles with potentially dangerous crossing decisions.

[^4]In conclusion, the results presented in this paper could be of notable interest for those involved in modelling pedestrian decision making at non-signalized intersections for developing integrated computer-based simulation tools. Ongoing activities are focused on modelling speed-related crossing phases (approaching, appraising, crossing) and pedestrian-vehicle competitive vs collaborative interactions. We observed indeed that the 48\% of drivers were non-compliant with the pedestrians right of way on the zebra striped. At the same time, elderly pedestrians were found to be more cautious than adults giving way to approaching vehicles in order to have more time to evaluate the time gap and avoid collision.

The gathered results will be employed as supports to the calibration and validation of the model presented in Crociani et al. (2014) and Feliciani et al. (2017), with reference to the implementation of a parametric discretization of age-driven speed profiles, appraising duration time and accepted time gap. Once calibrated, a series of analyses on simulation results will allow to test the efficiency of different planning and architectural hypotheses aimed at exploring potential ways to improve the overall safety of the observed zebra crossing.

Despite the specific context of the performed observation, and the limited time duration of the video footage (from 10:45 am to 12:00 am, during peak hour period), the results about the speeds of adult and elderly pedestrians while crossing could be used as threshold values for design purposes of pedestrian traffic lights at crossing points (start up and clearance time), but also as supports for the parametric calibration of automated sensor systems for the development of driver-less robotic systems (e.g., collision avoidance from crossing pedestrians). Future and more extended data collection campaigns could be executed on other urban non-signalized intersections, in order to gather more consistent data and considering also critical environmental conditions (e.g., traffic volumes, weather conditions, spatial layout of side-walks). For example, future analyses will be focused on the impact of parking cars on vehicular flows, stop-controlled delay and visibility of road users.

## Acknowledgement

The Italian policy was complied in order to exceed the ethical issues about the privacy of the people recorded without their consent. The Italian policy was complied in order to exceed the ethical issues about the privacy of the people recorded without their consent. The authors thank the students Fatima Zahra Anouar, Daniele Loliva, Riccardo Perego, Ivan Tricella, Claudia Prosperi and Nami Avento for their fruitful contributions in data collection. The recorded video tape and the annotated data set are available only for research purposes (contact: andrea.gorrini@unimib.it).

## References

Asher, L., Aresu, M., Falaschetti, E., \& Mindell, J. (2012). Most older pedestrians are unable to cross the road in time: a cross-sectional study. Age and Ageing, 41, 690-694.
Bandini, S., Crociani, L., \& Vizzari, G. (2017). An approach for managing heterogeneous speed profiles in cellular automata pedestrian models. Journal of Cellular Automata, 12, 401-421.
Bandini, S., Gorrini, A., \& Vizzari, G. (2014). Towards an integrated approach to crowd analysis and crowd synthesis: A case study and first results. Pattern Recognition Letters, 44, 16-29. https://doi.org/10.1016/j.patrec.2013.10.003.
Bandini, S., \& Vizzari, G. (2016). Heterogeneous dynamics through coupling cellular automata models. In S. E. Yacoubi, J. Was, \& S. Bandini (Eds.), Cellular automata - 12th international conference on cellular automata for research and industry, ACRI 2016, Fez, Morocco, September 5-8, 2016. Proceedings. Lecture Notes in Computer Science (vol. 9863, pp. 387-395). Springer. https://doi.org/10.1007/978-3-319-44365-2_38.
Burstedde, C., Klauck, K., Schadschneider, A., \& Zittartz, J. (2001). Simulation of pedestrian dynamics using a two-dimensional cellular automaton. Physica A: Statistical Mechanics and its Applications, 295, 507-525.
Cavallo, V., Dang, N. -T., Thomson, J., Gorrini, A., Piwowarczyk, A., \& Bandini, S. (2016). Social influences on pedestrian behaviour: comparison of streetcrossing decisions in singles and dyads. In ICP2016-International Congress of Psychology (p. 1).
Crociani, L. \& Vizzari, G. (2014). An integrated model for the simulation of pedestrian crossings. In Cellular automata - 11th international conference on cellular automata for research and industry, ACRI 2014, Krakow, Poland, September 22-25, 2014. Proceedings (pp. 670-679).
Dommes, A., Cavallo, V., Dubuisson, J.-B., Tournier, I., \& Vienne, F. (2014). Crossing a two-way street: comparison of young and old pedestrians. Journal of Safety Research, 50, 27-34.
Dommes, A., Cavallo, V., \& Oxley, J. (2013). Functional declines as predictors of risky street-crossing decisions in older pedestrians. Accident Analysis \& Prevention, 59, 135-143.
Evans, D., \& Norman, P. (1998). Understanding pedestrians' road crossing decisions: an application of the theory of planned behaviour. Health Education Research, 13, 481-489.
Feliciani, C., Crociani, L., Gorrini, A., Vizzari, G., Bandini, S., \& Nishinari, K. (2017). A simulation model for non-signalized pedestrian crosswalks based on evidence from on field observation. Intelligenza Artificiale, 11, 117-138.
Gifford, R. (2016). Research methods for environmental psychology. Oxford, UK: Wiley Blackwell \& Sons.
Gorrini, A., Vizzari, G., \& Bandini, S. (2016). Age and group-driven pedestrian behaviour: From observations to simulations. Collective Dynamics, 1, 1-16.
Hamed, M. M. (2001). Analysis of pedestrians' behavior at pedestrian crossings. Safety Science, 38, 63-82.
HCM (2010). Highway capacity manual. Washington, DC: Transportation Research Board, National Research Council.
Helbing, D., Jiang, R., \& Treiber, M. (2005). Analytical investigation of oscillations in intersecting flows of pedestrian and vehicle traffic. Physical Review E, 72, 046130.
Helbing, D., \& Molnar, P. (1995). Social force model for pedestrian dynamics. Physical review E, 51, 4282.
Kesting, A., Treiber, M., \& Helbing, D. (2007). General lane-changing model mobil for car-following models. Transportation Research Record: Journal of the Transportation Research Board.
Landis, J. R., \& Koch, G. G. (1977). The measurement of observer agreement for categorical data. Biometrics, 0, 159-174.
Lehsing, C., Kracke, A., \& Bengler, K. (2015). Urban perception-a cross-correlation approach to quantify the social interaction in a multiple simulator setting. In 2015 IEEE 18th international conference on intelligent transportation systems (pp. 1014-1021). IEEE.
Lobjois, R., \& Cavallo, V. (2007). Age-related differences in street-crossing decisions: The effects of vehicle speed and time constraints on gap selection in an estimation task. Accident Analysis \& Prevention, 39, 934-943.
Nagel, K., Wagner, P., \& Woesler, R. (2003). Still flowing: Approaches to traffic flow and traffic jam modeling. Operations Research, 51, 681-710.
Oxley, J., Fildes, B., Ihsen, E., Charlton, J., \& Day, R. (1997). Differences in traffic judgements between young and old adult pedestrians. Accident Analysis \& Prevention, 29, 839-847.

Perumal, V. et al (2014). Study on pedestrian crossing behavior at signalized intersections. Journal of Traffic and Transportation Engineering (English edition), 1, 103-110.
Sisiopiku, V. P., \& Akin, D. (2003). Pedestrian behaviors at and perceptions towards various pedestrian facilities: An examination based on observation and survey data. Transportation Research Part F: Traffic Psychology and Behaviour, 6, 249-274.
Speck, J. (2013). Walkable city: How downtown can save America, one step at a time. Macmillan.
Sun, R., Zhuang, X., Wu, C., Zhao, G., \& Zhang, K. (2015). The estimation of vehicle speed and stopping distance by pedestrians crossing streets in a naturalistic traffic environment. Transportation Research Part F: Traffic Psychology and Behaviour, 30, 97-106.
Turner, A., \& Penn, A. (2002). Encoding natural movement as an agent-based system: An investigation into human pedestrian behaviour in the built environment. Environment and Planning B: Planning and Design, 29, 473-490.
Varhelyi, A. (1998). Drivers' speed behaviour at a zebra crossing: a case study. Accident Analysis \& Prevention, 30, 731-743.
Wagner, J. (1981). Crossing streets: Reflections on urban pedestrian behavior. Man-environment Systems.
Wang, R., \& Ruskin, H. (2006). Modelling traffic flow at multi-lane urban roundabouts. International Journal of Modern Physics C, 17, 693-710.
Webb, J. D., \& Weber, M. J. (2003). Influence of sensory abilities on the interpersonal distance of the elderly. Environment and Behavior, 35, 695-711.
Wei, W. W. (2006). Time series analysis. In The oxford handbook of quantitative methods in psychology (Vol. 2).
Winogrond, I. R. (1981). A comparison of interpersonal distancing behavior in young and elderly adults. The International Journal of Aging and Human Development, 13, 53-60.
World Health Organization (2015). Global status report on road safety 2015. World Health Organization.
Zeng, W., Chen, P., Nakamura, H., \& Iryo-Asano, M. (2014). Application of social force model to pedestrian behavior analysis at signalized crosswalk. Transportation Research Part C: Emerging Technologies, 40, 143-159.


[^0]:    * Corresponding author.
    E-mail address: andrea.gorrini@unimib.it (A. Gorrini).

[^1]:    ${ }^{1}$ See http://aim.milano.it/en/pubblicazioni-en/archivio-pubblicazioni-en

[^2]:    ${ }^{2}$ All statistics presented in this paper have been performed by using the software IBM SPSS Statistics v.24, and they have been conducted at the $\mathrm{p}<0.01$ level.

[^3]:    ${ }^{3}$ See http://www.cabrillo.edu

[^4]:    ${ }^{4}$ See http://www.walkableamerica.org/checklist-walkability.pdf

