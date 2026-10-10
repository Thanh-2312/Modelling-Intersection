# A Pedestrian Trajectory Prediction Model for Right-Turn Unsignalized Intersections Based on Game Theory 

Wenli Li ${ }^{\text {(iD) }}$, Yinan Zhang ${ }^{\text {(iD) }}$, Lingxi Li ${ }^{\text {(iD) }}$, Senior Member, IEEE, Yisheng Lv ${ }^{\text {(iD) }}$, Senior Member, IEEE, and Mengxin Wang ${ }^{\text {® }}$


#### Abstract

This paper aims to propose a pedestrian trajectory prediction model based on pedestrian-vehicle game theory to study pedestrian trajectories during pedestrian-vehicle interaction at unsignalized right-turn intersections. First, pedestrian-vehicle interaction scene data at unsignalized rightturn intersections were collected. Then, a novel pedestrianvehicle game theory model was established, where its parameters were calibrated using the Nash equilibrium of a complete information static game and the probabilities of pedestrians and vehicles crossing the street. A new pedestrian-vehicle game utility matrix is embedded into the social-generative adversarial network pedestrian trajectory prediction model, which considers information between pedestrians and vehicles and analyzes the state of pedestrian-vehicle-interactions under various decisions through microscopic motion factors and macroscopic game decisions. The experimental results show that the proposed model is more accurate and explanatory than traditional pedestrian trajectory prediction models, such as long short-term memory (LSTM), Social LSTM, Social generative adversarial network(S-GAN), and Sophie.


Index Terms-Right-turn intersections, pedestrian trajectory prediction, pedestrian-vehicle interaction, game theory, socialgenerative adversarial network.

## I. Introduction

IN TODAY'S densely populated cities, the rise in traffic flow has led to frequent pedestrian-vehicle conflicts. The 2018 Global Status Report on Road Safety, published

Manuscript received 9 January 2023; revised 25 June 2023 and 8 December 2023; accepted 19 April 2024. Date of publication 22 May 2024; date of current version 1 August 2024. This work was supported in part by the Science and Technology Innovation Key Research and Development Program of Chongqing under Grant CSTB2022TIAD-STX0003 and in part by the National Natural Science Foundation of Chongqing under Grant cstc2021jcyjmsxmX0183. The Associate Editor for this article was X. Lei. (Corresponding author: Lingxi Li.)
Wenli Li, Yinan Zhang, and Mengxin Wang are with the Key Laboratory of Advanced Manufacturing Technology for Automobile Parts, International Joint Laboratory of Intelligent Manufacturing \& Control of Key Parts for Energy-Efficient \& New Energy Vehicles, Ministry of Education, Chongqing University of Technology, Chongqing 400050, China.
Lingxi Li is with the Department of Electrical and Computer Engineering, Indiana University-Purdue University Indianapolis, Indianapolis, IN 46202 USA (e-mail: LL7@iupui.edu).
Yisheng Lv is with the State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, Chinese Academy of Sciences, Beijing 100190, China, also with the Shandong Key Laboratory of Smart Transportation (Preparation), Shandong Jiaotong University, Jinan 250353, China, and also with the School of Artificial Intelligence, University of the Chinese Academy of Sciences, Beijing 100049, China.
Digital Object Identifier 10.1109/TITS.2024.3398648 by the World Health Organization (WHO) [1], states that approximately 1.35 million people worldwide die in road traffic accidents per year, with pedestrians and cyclists accounting for up to 26\% of these deaths. Road traffic accidents account for 2.37\% of 56.9 million deaths worldwide and are currently the eighth leading cause of death. In addition, the U.S. Department of Transportation [2] reports that over 70\% of all intersection-related crashes occur at unsignalized intersections.

Ensuring the safety of vulnerable road users, especially pedestrians in road traffic, has become a crucial research issue for academia and industry. At signalized intersections, traffic signals restrain the behavior of vehicles and pedestrians; therefore, the probability of pedestrian-vehicle conflicts is low. However, at unsignalized right-turn intersections, the relationship between pedestrians and vehicles becomes complex, and the behavior of both parties is full of uncertainties and connections. Traffic lights do not need to control the right turn of vehicles through unsignalized rightturn intersections. The random movement of right-turning motor vehicles and the interaction of traffic flows in different directions considerably interfere with pedestrians, thereby increasing the danger for pedestrians crossing the street. As pedestrians cross the street at unsignalized right-turn intersections, they have strong randomness and uncertainty. Furthermore, pedestrians have different crossing intentions. The driver's subjective judgment alone is not accurate enough and cannot reduce the risk of pedestrian-vehicle collision.

In this paper, we consider specific unsignalized rightturn intersections to study pedestrian-vehicle interactions and propose a game theory-based model to predict pedestrians' future paths at these intersections. More specifically, a static game matrix is established and embedded into the deeplearning network model, and together with the Nash equilibrium of a complete information game, future pedestrian trajectories are predicted.

The primary contributions of this paper are summarized as follows.

1. Pedestrian-vehicle motion data with game characteristics for intersections were collected at unsignalized right-turn intersections.
2. An appropriate game payment matrix for vehicles and pedestrians is carefully designed, considering several influencing factors.
3. A novel pedestrian trajectory prediction model is developed, which uses an S-GAN-based model for predicting pedestrian trajectories in the game state.
4. A comparison study was conducted to analyze the performance of the proposed model and existing models in the literature. The experimental results showed that the proposed model could predict pedestrians' future paths more accurately, providing a safer environment for pedestrian and vehicle movement in complex traffic scenes.

The remainder of this paper is organized as follows. Section II describes related research work. Section III describes data collection, preprocessing, and analysis in detail for two real-world scenes in Chongqing, China. In Section IV, we analyze the game decisions during pedestrian-vehicle interaction and develop a new pedestrian trajectory prediction model based on game theory. In Section V, we conduct experiments to compare the performance of the proposed model with other classical models. In Section VI, we visualize and discuss the experimental results, and the conclusions are drawn in Section VII, including several future research directions.

## II. Related Work

Due to the differences in local road traffic rules and the unique characteristics of right-turn intersections. In the existing work, Chen et al. [3] evaluated rightturn pedestrian-vehicle interaction conflicts at intersection pedestrian crossings and developed a behavioral simulation model. Chen verified that large right-turn intersections sizes and large turning angles result in poor safety performance. Kumar et al. [4] evaluated pedestrian safety at rightturn intersection interactions using five time-based conflict metrics and obtained crucial influences on pedestrian risktaking behavior through cluster analysis to identify various factors affecting pedestrian-vehicle conflicts at signalized intersections. Xin et al. [5] studied pedestrian crossings in the right-turn area at signalized intersections, obtained pedestrian-vehicle tracking data, and performed a risk analysis of different conflict types of pedestrian-vehicle interactions by fuzzy clustering.

Along with the rapid development of computer and automotive technology, intelligent vehicles have gained popularity [6], [7]. The vehicle system must consider several factors when an intelligent vehicle is driving in complex traffic intersections, specifically predicting the future path of pedestrians. Along with successfully predicting pedestrians' future trajectories, drivers will considerably improve their ability to cope with potential hazards in complex traffic scenes. Therefore, it is necessary to study pedestrians' future trajectory changes at unsignalized right-turn intersections. The trajectory prediction of pedestrians is primarily divided into modeldriven and deep-learning-based predictions.

Model-driven prediction includes social force [8], Markov [9], and Kalman filter models [10]. Because of the complicated pedestrian-vehicle interaction under different traffic scenes, model-based methods are inaccurate enough to describe these scenes. Therefore, deep-learning-based prediction gradually becomes the mainstream research direction. With the development of deep learning, the mainstream neural networks are recurrent neural network (RNN) [11], long short-term memory (LSTM) network [12], and generative adversarial network (GAN) [13]. RNN has issues of gradient disappearance and explosion in training. GAN has generators and discriminators, which can be welltrained for adversarial training. Gupta et al. [14] proposed a social GAN (S-GAN) on GAN networks to optimize prediction accuracy by capturing the social state among pedestrians. Alahi et al. [15] introduced a social pooling layer on an LSTM network to share the hidden state of pedestrians with each other and their surrounding neighbors to build a social LSTM.

Game theory is a vital branch of modern mathematics. It is used to study a process where two or more players make decisions in a state of mutual influence. The emergence of game theory provides a precise perspective for analyzing the state of cooperation, competition, and mutual decisionmaking. It has been extensively used in transportation to address difficult decision-making traffic scenes. Based on the traditional game [16], various new game ideas, such as noncooperative, cooperative, static, dynamic, complete information, incomplete information, and evolutionary games, have been proposed [17], [18], [19], [20]. In 1952, Wardrop [21] first applied game theory to analyze the road path selection. Several researchers have also used game theory to analyze and solve traffic problems. Recently, Wu et al. [22] presented a game-theoretic approach for describing pedestrian-vehicle interactions at pedestrian crossings and embedded this method into a meta-automata simulation system to classify the severity of conflicts between vehicles and pedestrians. Yang et al. [23] proposed a pedestrian-vehicle interaction model based on the Logit model and incomplete information static game theory, The impact of traffic environment changes on the safety and efficiency of pedestrian-vehicle interaction was obtained from the analysis.

Researchers have extensively studied pedestrian-vehicle conflicts at traffic intersections and analyzed all interaction styles at right-turn and straight intersections. Adding game theory ideas to the safety of pedestrian-vehicle conflicts, crossing styles, and interaction behaviors have been studied [24], [25]. However, analyzing various risk factors in pedestrian-vehicle conflicts and predicting pedestrians' trajectories by incorporating game ideas is less considered. Jayaraman et al. [26] developed a pedestrian dynamics prediction model using game theory and deep-learning visual analysis to model multi-pedestrian decision-making processes and learn the parametric mapping of pedestrian appearance and behavior using visual classifiers. Rahmati et al. [27] developed a prediction model of pedestrian dynamics using the noncooperative game of Nash equilibrium theory and established an interactive decision framework to provide more accurate pedestrian behavior trajectory prediction for vehicles. Bighashdel et al. [28] added the Nash equilibrium idea based on neural networks and proposed an equilibrium correction concept. However, these methods must be further investigated, as the game theory idea is not fully integrated into

TABLE I
Dataset Comparison Table
| Pedestrian Dataset | Amount of Trajectories | Collection Scene | Shooting Angle | Collection Weather | Collecting Information |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DUT | 1793 | campus | $90^{\circ}$ | clear day | Pedestrians position, speed, vehicle position, speed, heading angle |
| PIE | 1842 | street | about 0°-20° | clear day | Pedestrian behavior, hand signals, vehicle type, traffic signals |
| CITR | 340 | specifically designed | $90^{\circ}$ | clear day | Pedestrian position, speed, vehicle position, speed, heading angle |
| ETH | 750 | campus, urban street | about 70°-80° | clear day, snowy day | Pedestrian position, speed |
| UCY | 786 | campus, park, urban street | about 20°-50° | clear day | Pedestrian position, pedestrian gaze direction |
| SDD | over 11000 | campus | $90^{\circ}$ | clear day | Pedestrians, bicyclists, skateboarders, cars, buses |
| GC | over 12000 | urban street | $90^{\circ}$ | clear day | Pedestrian trajectories |
| Town Center | 2200 | urban, street | about 20°-35° | clear day | Pedestrian trajectories and their head positions |
| JAAD | over 390000 | urban, street, park | about 0°-20° | clear day, rainy day, snowy day | Pedestrian behavior, appearance, vehicles behavior |
| CQUT-PVI (ours) | 3000 | unsignalized right turn intersection | $90^{\circ}$ | clear day, cloudy day | Pedestrian position, speed, acceleration, waiting time, vehicle position, speed, acceleration, waiting time, post encroachment time, relative distance |


pedestrian trajectory prediction. The correlation with actual pedestrian-vehicle crossing conflicts is insufficient.

Based on this background, in this research, we propose a new pedestrian trajectory prediction model that captures complex game relationships from human-vehicle interaction trajectories, and can then be used for the task of predicting pedestrian trajectories based on right-turn unsignalized intersections.

## III. Data Preparation

This section processes and analyzes pedestrian-vehicle game data. As the main distribution of the microscopic motion parameters of pedestrians and vehicles are crucial for the decisions of both parties in a complete information static game, the concerned studies in this context are as follows.

## A. Data Preprocessing

Currently, there exists a large number of publicly available datasets on pedestrian trajectories, and although many excellent datasets exist, they may not be able to satisfy the user's requirements in some specific scenarios. The scenario of interest in this study is the pedestrian-vehicle interaction data under the right-turn unsignalized intersection, and after comparative analysis, we found that the actual needs of the research scenario are not fully satisfied, including specific application scenarios, the trajectories of both pedestrians and vehicles, more variables, and the diversity of pedestrianvehicle interactions, as shown in Table I of the specific dataset feature pairs. We need to supplement this gap in many public pedestrian datasets.

We selected two traffic scenes with different road conditions for video acquisition. Scene 1 is an unsignalized rightturn intersection at Hongguang and Hongli Avenues in Banan District, Chongqing. Scene 2 is an unsignalized rightturn intersection at Longzhou Avenue and Huaxi Street, Banan District, Chongqing. In Scene 1, as the location is around the university, student flow is dense with frequent pedestrian-vehicle interactions and the frequency of conflict is high. The first right-turn lane in this scene has parking spaces; right-turning vehicles can only drive into the second lane; and the pedestrian-vehicle interaction area is precise. Scene 2 is in a residential living area; there are more markets around; and the number of trucks is higher than in Scene 1. Conflict between residents and trucks is frequent. These scenes can provide a rich state of pedestrian-vehicle gaming. Both intersections were aerially filmed by a DJI-Mini 2 unmanned aerial vehicle, with a flight height of 25 m, a maximum flight time of 30 min, 12 million effective pixels, complementary metal-oxide-semiconductor image sensors, a video resolution of 3480 × 2160, and a frame rate of 30 fps. Scene 1 is a twoway four-lane right-turn intersection, and Scene 2 is a two-way two-lane right-turn intersection. Table II shows the geometric parameters of the collected scenes and traffic flow. Fig. 1 shows how we specifically use drones for scene acquisition and demonstrate pedestrian-vehicle interaction under right turns.

The video data are divided into commuting and noncommuting hours, and the weather includes sunny, and cloudy. The commuting time is from 5:30 pm to 7:00 pm, and the noncommuting time is from 9:30 am to 11:00 am. The collection took 3 hours per day (270 hours) for 5 months. The pedestrian-vehicle interactions under peak and flat periods were captured separately. From the video data, 1,500 pedestrians with clear game states were extracted from each scene for 3,000 pedestrian-vehicle interaction events and 527382 data frames were collected. The format of the data set is

TABLE II
Acquisition Scene Feature Table
|  | Pedestrian crosswalk size(m) | Interactive acquisition size(m) | Right-turn traffic flow(veh/h) |  | People flow(ped/h) |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  | Commute Period | Noncommute period | Commute Period | Noncommute period |
| Scene 1 | 4 × 16 | 16 × 8 | 396 | 284 | 668 | 274 |
| Scene 2 | 6 × 16 | 16 × 8 | 498 | 316 | 712 | 302 |


TABLE III
Statisticial Table of Data
| Frame | ID | $X_{P / V}$ | $Y_{P / V}$ | $V_{P / V}$ | $A_{P / V}$ | $W_{P / V}$ | $R$ | PET |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1 | 14.36/8.63 | 7.36/4.19 | 0/0 | 0 | 0/0.034 | 6.54 | 0 |
| 2 | 1 | 14.35/8.65 | 7.31/4.21 | 1.68/0.62 | 0 | 0/0.069 | 6.48 | 10.26 |
|  |  |  |  | … |  |  |  |  |
| 16 | 1 | 14.21/8.83 | 6.49/4.39 | 1.71/0.71 | 1.16/-1.45 | 0/0.552 | 5.77 | 8.97 |


![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-04.jpg?height=649&width=810&top_left_y=971&top_left_x=200)
Fig. 1. Data acquisition scene diagram.

$\left(\right.$ frame $\left., i d, x_{\mathrm{P}}, y_{\mathrm{P}}, v_{\mathrm{P}}, a_{\mathrm{P}}, w_{\mathrm{P}}, x_{\mathrm{V}}, y_{\mathrm{V}}, v_{\mathrm{V}}, a_{\mathrm{V}}, w_{\mathrm{V}}, R, P E T\right)$. where $w_{i}$ is the delay time of either pedestrians or vehicles, $R$ is the Euclidean distance between pedestrians and vehicles, and $P E T$ is the post encroachment time. $P E T$ in this paper does not represent the difference of the final time of the pedestrian-vehicle passing the conflict area in the common sense, but the microscopic PET obtained using the speed and distance of pedestrian-vehicle under each frame.

## B. Data Analysis

The primary issues with pedestrian-vehicle collisions are deciding whether there is a conflict and where to divide the conflict area. The pedestrian will walk leisurely across the street if a right-turning vehicle is farther. The pedestrian frequently refrains from crossing if the vehicle is nearby and the passing time is insufficient. Instead, they will wait at the crossroads and observe the vehicle to pass. Through actual scene observations and data collection, we discovered that pedestrians do not feel insecure while crossing the street because right-turning vehicles are slower than straight-line vehicles in certain interaction scenes. In addition, due to the local traffic regulations, when people or vehicles choose to wait to cross the street, they do not stop moving like they would if the intersection were straight. Instead, they continue to try to move ahead at a much slower speed. During interaction, pedestrians and vehicles have different crossing forms and intentions. Due to the slow speed of pedestrian crossing and limited interaction distance at this site, not much delay was observed between pedestrians and vehicles. After comparison, the distribution of pedestrian-vehicle delays is inconsistent with that of straight-line intersections [29]. This study divides the pedestrian-vehicle conflict into different degrees by gathering details about the precise locations, speeds, and acceleration of pedestrians and vehicles and calculating the relative distance, delay time, and PET (Table III).

The statistics of specific pedestrian-vehicle interaction behaviors were obtained by actual observation (Table IV and Table V). In Scene 1, the probability of pedestrians passing during commuting is 70.3\%, whereas the probability of vehicles passing is 27.2\%. The probability of pedestrians passing during noncommuting is 63.6\%, whereas the probability of vehicles passing is 32.8\%. In Scene 2, pedestrians pass with 64.5\% and vehicles with 31.1\% during commuting, whereas pedestrians pass with 58.9\% and vehicles with 38.5\% during noncommuting. These scenes and pedestrian-vehicle crossing probabilities obtained for different periods illustrate that pedestrians are far more eager to cross the intersection than vehicles.

In both scenes, the probability of pedestrians passing during noncommuting hours is lower than during commuting hours because there are more pedestrians during commuting hours. Pedestrians will present a group form when passing, and vehicles tend to give way to hordes of pedestrians. During noncommuting, the pedestrians' crossing time is more scattered, showing a single person crossing, and the drivers are less attentive to pedestrians in this situation. Analyzing the two scenes for comparison, the vehicles in Scene 1 are mostly cars, whereas those in Scene 2 contain many trucks,

TABLE IV
Statistical Table of Scene 1 Pedestrian-Vehicle Interaction Behavior
| Scene 1 Commute Period | Pedestrian passage | Pedestrian wait | Total | Scene 1 Noncommute period | Pedestrian passage | Pedestrian wait | Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Vehicle Passage | 14 | 204 | 218 | Vehicle Passage | 8 | 246 | 254 |
| Vehicle wait | 527 | 5 | 532 | Vehicle wait | 477 | 19 | 496 |
| Total | 541 | 209 | 750 | Total | 485 | 265 | 750 |


TABLE V
Statistical Table of Scene 2 Pedestrian-Vehicle Interaction Behavior
| Scene 2 Commute Period | Pedestrian passage | Pedestrian wait | Total | Scene 2 Noncommute period | Pedestrian passage | Pedestrian wait | Total |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Vehicle Passage | 15 | 233 | 248 | Vehicle Passage | 3 | 289 | 292 |
| Vehicle wait | 484 | 18 | 502 | Vehicle wait | 442 | 16 | 458 |
| Total | 499 | 251 | 750 | Total | 445 | 305 | 750 |


posing a greater danger to pedestrians. In the commuting and noncommuting periods, the pedestrians in Scene 1 are more willing to cross the street than those in Scene 2. However, according to laws and regulations, vehicles must slow down to yield to pedestrians at right-turn unsignalized intersections, and the required crossing clearance for pedestrians [30] is smaller. Therefore, pedestrians perceive less danger from moving vehicles and focus more on themselves. The risks posed by cars are less frightening to pedestrians, who are more concerned with their own traffic efficiency. In addition, most drivers prefer to trade delay times for safety because pedestrians move faster and vehicles have shorter delay times. This phenomenon can also be seen in the higher pedestrian crossing rates than vehicle throughput rates from the analysis of both scenes.

1) Analysis of the Frequency Interaction Variables: Fig. 2 and Fig. 3 show the statistical study of pedestrian-vehicle interaction parameters, including velocity, acceleration, waiting time, relative distance, and PET, for the two scenes. The analysis shows that the velocity of all interacting pedestrians in both scenes is concentrated at 1-2 m/s. This interval is the specific velocity of pedestrians when they gamely decide to move forward, and this range is consistent with the lognormal distribution. The only difference is that the speed of the pedestrians in Scene 2 is considerably greater than that in Scene 1 at 15\% quantile of the cumulative frequency because the pedestrians in Scene 2 must pass at a faster velocity to ensure their safety when facing a truck. The velocity of pedestrians who chose to wait rather than move forward considerably peaked at 0-0.5 m/s.

As pedestrian acceleration is dispersed to both sides with 0 m/s as the center, the pedestrian acceleration during the game is typically smooth and does not fluctuate much, consistent with normal distribution. The comparison between the two scenes shows that the acceleration fluctuation of Scene 1 is larger than that of Scene 2, which may have some relationship with the change in pedestrian decisions in Scene 1. Regarding pedestrians' waiting decisions, pedestrians at right-turn intersections have shorter delay times and less loss than those at straight intersections, consistent with the Logit distribution, and are concentrated in the range of 0-3 s. The delay time of pedestrians under Scene 1 is shorter than under Scene 2, which is related to the excessive velocity of vehicles under Scene 2, resulting in pedestrians waiting longer to ensure their safety.

Statistical analysis of vehicle velocity, acceleration, and delay time under the two scenes was conducted. The primary interval of vehicle velocity under Scene 1 is $0-2 \mathrm{~m} / \mathrm{s}$, and under Scene 2, it reaches $1-4 \mathrm{~m} / \mathrm{s}$, much larger than under Scene 1. This verifies why the pedestrian crossing rate under Scene 2 is lower than under Scene 1. Generally, the speed of right-turning vehicles is lower than that of straight-going vehicles because vehicles consciously slow down during the gaming process, and most vehicles adopt a waiting strategy. However, vehicles will make a trial advance during the waiting process to compensate for the loss of waiting. The vehicle acceleration is the same as that of pedestrians, without drastic changes, conforming to the normal distribution.

The subplot (g) and subplot (h) shows that the relative pedestrian-vehicle distance and PET are log-normally distributed. The relative space between pedestrians and vehicles is 3-8 m, and the PET is 0-6 s. The risk assessment of pedestrian-vehicle game through PET found that pedestrians and vehicles still face certain safety risks, and the degree of danger of pedestrian-vehicle game differs. We use P15\% and P85\% of PET as conflict severity indicators. When PET value is greater than P85\%, mild conflict occurs between the two sides; when the value is between P15\% and P85\%, moderate conflict occurs; and when it is lower than P15\%, severe conflict occurs between the two sides.

Table VI shows that 85\% cumulative frequency statistic was used for each variable, and the mean and standard deviation were calculated for each variable. As vehicles and pedestrians

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-06.jpg?height=746&width=1783&top_left_y=191&top_left_x=168)
Fig. 2. Frequency distribution of pedestrian-vehicle interaction parameters under Scene 1: (a) the velocity frequency distribution of pedestrians, (b) the velocity frequency distribution of the vehicle, (c) the acceleration frequency distribution of pedestrians,(d) the acceleration frequency distribution of the vehicle, (e) the frequency distribution of waiting time under the absence of pedestrian conflicts, (f) the frequency distribution of the waiting time under the vehicle without conflict, (g) the frequency distribution of the relative distance between pedestrians and vehicles, and (h) the frequency distribution of postencroachment time (PET) under pedestrian-vehicle interaction.

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-06.jpg?height=769&width=1785&top_left_y=1164&top_left_x=174)
Fig. 3. Frequency distribution of pedestrian-vehicle interaction parameters under Scene 2: (a) the velocity frequency distribution of pedestrians, (b) the velocity frequency distribution of the vehicle, (c) the acceleration frequency distribution of pedestrians,(d) the acceleration frequency distribution of the vehicle, (e) the frequency distribution of waiting time under the absence of pedestrian conflicts, (f) the frequency distribution of the waiting time under the vehicle without conflict, (g) the frequency distribution of the relative distance between pedestrians and vehicles, and (h) the frequency distribution of postencroachment time (PET) under pedestrian-vehicle interaction.

receive different levels of safety clearance during the game, different choices are made. Regarding velocity between scenes 1 and 2, the pedestrian-vehicle game in Scene 1 seems milder, whereas in Scene 2, it is more intense. Due to the lack of a clear right-of-way distribution, pedestrians typically choose to cross at unsignalized right-turn intersections, whereas drivers choose to slow down and yield to pedestrians, whose delay time is considerably longer than that of pedestrians due to the failure of the vehicle game. This observation is consistent with the statistics of pedestrian-vehicle interaction behavior.

## IV. Method and Model

## A. Pedestrian-Vehicle Game Analysis

When crossing the street at unsignalized traffic crossroads, pedestrians frequently scan the area for potentially hazardous approaching traffic. Before they reach the contact area at rightturn traffic crossroads, drivers and pedestrians form opinions and make decisions. Due to the complexity and diversity of decision-making on both sides, we provided macroscopic choice probabilities by establishing a game formulation and

TABLE VI
Table of Intervals of Pedestrian-Vehicle Interaction Variables
| Interaction variables | Scene1 |  |  |  | Scene2 |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | P15\% | P85\% | Average value | Standard deviation | P15\% | P85\% | Average value | Standard deviation |
| Pedestrian velocity $V_{P}(\mathrm{~m} / \mathrm{s})$ | 0.319 | 1.474 | 1.038 | 0.529 | 0.699 | 1.453 | 1.091 | 0.465 |
| Pedestrian acceleration $A_{P}\left(\mathrm{~m} / \mathrm{s}^{2}\right)$ | -1.111 | 1.062 | 0.055 | 2.057 | -0.518 | 0.433 | 0.080 | 0.942 |
| Pedestrian waiting time $W_{P}(\mathrm{~s})$ | 0.492 | 3.231 | 2.076 | 1.327 | 0.402 | 4.061 | 2.593 | 1.714 |
| Vehicle velocity $V_{V}(\mathrm{~m} / \mathrm{s})$ | 0.063 | 3.246 | 1.623 | 1.472 | 0.785 | 4.199 | 3.660 | 1.587 |
| Vehicle acceleration $A_{V}\left(\mathrm{~m} / \mathrm{s}^{2}\right)$ | -1.309 | 1.120 | 0.037 | 2.081 | -0.855 | 0.826 | 0.214 | 1.426 |
| Vehicle waiting time $W_{V}(\mathrm{~s})$ | 0.423 | 3.517 | 2.399 | 1.694 | 0.482 | 4.688 | 3.676 | 2.390 |
| Pedestrian-vehicle relative distance $R$ (m) | 3.698 | 6.981 | 5.218 | 2.137 | 3.698 | 11.106 | 6.026 | 2.587 |
| Postencroachment time PET (s) | 0.917 | 8.060 | 3.582 | 3.951 | 1.231 | 5.397 | 5.781 | 4.202 |


precisely studied the factors influencing pedestrians when crossing the street. In this section, a pedestrian-vehicle game model is developed.

Definition 1: Drivers and pedestrians are logical beings who will make decisions based on their circumstances.

Definition 2: The game starts when pedestrians and vehicles enter the observation area.

Definition 3: Pedestrians and drivers decide whether to pass obedience to the complete information static game.

Definition 4: A conflict between pedestrians and vehicles occurs when both simultaneously approach the conflict area.

Model building: We developed a division of players, strategies, and benefits for both sides of the game.

Player: The game has two players: $i=A, B, i=A$ for pedestrians and $i=B$ for vehicles.

Strategy: During the pedestrian-vehicle game, pedestrians and vehicles have two identical strategies \{passgae, wait\}.

Utility: During the game, all players experience the influence of other players on themselves and their decisions. This influence includes delayed losses when players wait, losses when two players clash, and gains when one player waits for another player to pass. Player utility in different situations will be analyzed in detail.

Pedestrians and vehicles produce four choice outcomes in the game, and the set is $s_{n}, n \in[1,2,3,4]$. These distributions correspond to pedestrians and vehicles crossing the street simultaneously, pedestrians waiting for vehicles to cross the street, pedestrians crossing the street and vehicles waiting, and both waiting simultaneously. The complete information static game, which pedestrian and vehicle characteristics, strategy spaces and payoff functions are accurately informed and played simultaneously. Drivers and pedestrians study and choose strategies when they simultaneously enter the observation area. These plans are then put into action. Both sides of the game will eventually enter the conflict region, and the PET, which represents the risk degree of this game, is the relative time difference between their entry into the conflict region (Fig.4).

When strategy $s_{1}$ is selected, pedestrians and vehicles choose to cross the street simultaneously and conflict occurs

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-07.jpg?height=610&width=872&top_left_y=928&top_left_x=1083)
Fig. 4. Schematic of the gaming scene. Drivers and pedestrians are playing a game at an unsignalized right-turn intersection, and in the micro-scenario both sides are shortening their distance over time until they enter the conflict area.

at this point. There is no winner for pedestrians and vehicles, and all players are losing. During the conflict, the speed and acceleration of pedestrians and vehicles are crucial for the severity of the conflict. When vehicles and pedestrians cross the street simultaneously, the mutual distance between the two sides in each step indicates the degree of danger for both sides, but by combining with speed, it can be more in line with the realistic interaction scene. Based on the [23] and [31], we propose a collision severity factor in this study and suggest using PET instead of the distance to quantify the hazard level between the two sides. Equations 1 and 2 illustrate the individual pedestrian and vehicle payoff functions at this moment,

$$
\begin{aligned}
& \operatorname{pay}_{s_{1}}^{\mathrm{p}}=-\sigma_{\mathrm{p}} \alpha_{2} \exp \left(\left(v_{\mathrm{p}}+a_{\mathrm{p}}\right)\right) \\
& \operatorname{pay}_{s_{1}}^{\mathrm{v}}=-\sigma_{\mathrm{v}} \alpha_{1} \exp \left(\left(v_{\mathrm{v}}+a_{\mathrm{v}}\right)\right)
\end{aligned}
$$

where $\sigma_{\mathrm{p}}$ and $\sigma_{\mathrm{v}}$ are pedestrian and vehicle collision severity factors, respectively, and 1 and 2 represent Scenes 1 and 2, respectively, that are controlled by $P E T$, as given in Equations 3 and 4. $\alpha_{2}$ and $\alpha_{1}$ are the combined effect factors of
pedestrian and vehicle acceleration and velocity, respectively.

$$
\sigma_{\mathrm{p} 1}, \sigma_{\mathrm{v} 1}= \begin{cases}1 / 1 & P E T>7.43 \\ 3 / 1.5 & 1.94<P E T<7.43 \\ 5 / 2 & P E T<1.94\end{cases}
$$

and

$$
\sigma_{\mathrm{p} 2}, \sigma_{\mathrm{v} 2}= \begin{cases}1 / 1 & P E T>5.39 \\ 3 / 1.5 & 1.23<P E T<5.39 \\ 5 / 2 & P E T<1.23\end{cases}
$$

In Equations 3 and 4, as pedestrians and vehicles do not share the same degree of damage in a collision, pedestrians are more severely injured than drivers; therefore, the pedestrian crash severity factor is higher than that of the vehicle in the degree setting.

When strategy $s_{2}$ is chosen, the pedestrian chooses to wait for the vehicle to choose to pass. The pedestrian loses in this game and the vehicle wins. Compared with pedestrians, vehicles also have their desired speeds; therefore, the vehicle's traveling speed is used as the incentive for its payment function, as shown in Equation 5,

$$
\text { pay }_{s_{2}}^{\mathrm{v}}=\alpha_{3} \exp \left(v_{\mathrm{v}}\right)
$$

where pay $_{s_{2}}^{\mathrm{v}}$ is the value of the vehicle payment under strategy outcome, $s_{2}$, and $v_{\mathrm{v}}$ is the vehicle crossing speed.

The pedestrian is waiting at this time because pedestrians have flexible and variable characteristics and less reaction time than vehicle start; therefore, this period is not counted. Similar to the vehicle waiting, the payment function is shown in Equation 6,

$$
p a y_{s_{2}}^{\mathrm{p}}=-\alpha_{4} \exp \left(t_{\mathrm{p}}\right)
$$

where pay $_{s_{2}}^{\mathrm{p}}$ is the value of pedestrian payment under strategy outcome, $s_{2}, \alpha_{4}$ is the waiting suppression factor during crossing, and $t_{\mathrm{p}}$ is the pedestrian waiting time.

When strategy $s_{3}$ is chosen, the pedestrian chooses to pass and the vehicle chooses to wait. In the game perspective, the pedestrian wins the game and the vehicle fails. Pedestrians will pass with specific gains for themselves and vehicles will lose because of waiting. To resemble the real-world streetcrossing scene more closely and specifically reflect the player's motivation to choose a strategy, pedestrians will want to cross the street at a safer and more efficient speed. The pedestrian crossing payment function is motivated by the speed, as shown in Equation 7,

$$
p a y_{s_{3}}^{\mathrm{p}}=\alpha_{3} \exp \left(v_{p}\right)
$$

where $p a y_{s_{3}}^{p}$ is the value paid by pedestrians under strategy outcome, $s_{3}, \alpha_{3}$ is the speed incentive coefficient when crossing the street, and $v_{p}$ is the pedestrian crossing speed.

Here, the vehicle selects the waiting time and adds the driver response time to represent the vehicle's delay time. The vehicle crossing payment function is inhibited by the delay time, as shown in Equation 8:

$$
p a y_{s_{3}}^{\mathrm{v}}=-\alpha_{4} \exp \left(t_{\mathrm{v}}\right)-0.75
$$

where pay $_{s_{3}}^{\mathrm{v}}$ is the value of the vehicle payment under strategy outcome $s_{3}, \alpha_{4}$ is the waiting suppression coefficient during crossing, and $t_{v}$ is the vehicle delay time. According to [32] and [33], the driver's reaction time is generally 0.75 s.

When strategy $s_{4}$ is selected, the pedestrian and vehicle choose to yield and wait simultaneously. This strategy will considerably increase the rate of traffic congestion when all players are in a loss state. When both players choose to wait simultaneously, they will realize that their strategies are ineffective and take the time lost by waiting. In this paper, we propose a new idea called the regret factor, which is related to the starting acceleration of the waiting process of the pedestrian and vehicle and characterizes the regret of players who take the waiting strategy. The larger the starting acceleration of different players, the larger the regret and loss of the players in the waiting process. Compared with other strategies, the payoff function of the waiting process for both players has a necessary relationship with their waiting time (Equations 9 and 10).

$$
\begin{aligned}
& \text { pay }_{s_{4}}^{\mathrm{v}}=-k \alpha_{5} \exp \left(t_{v}\right) \\
& \text { pay }_{s_{4}}^{\mathrm{p}}=-k \alpha_{6} \exp \left(t_{\mathrm{p}}\right)
\end{aligned}
$$

where pay $_{s_{4}}^{\mathrm{v}}$ is the payment value of the vehicle under strategy outcome $s_{4}$, and pay ${ }_{s_{4}}^{\mathrm{p}}$ is the payment value of the pedestrian under strategy outcome $s_{4} . k$ is the regret factor parameter for both parties and will use $\exp \left(a_{\mathrm{v} / \mathrm{p}}\right)$ to represent its degree of regret. $\alpha_{5}$ and $\alpha_{6}$ are the waiting suppression factors for both parties under joint loss, which differ from those under strategies $s_{2}$ and $s_{3}$.

From the above, the payment functions of both players in the four strategies are known; therefore, the game payment matrix is constructed (Table VII).

The game matrix indicates that two strategies are more reasonable: 1. the vehicle chooses to pass and the pedestrian chooses to wait and 2. the pedestrian chooses to pass and the vehicle chooses to wait. As these two strategies are more dominant, they are unstable in the evolution process. The Nash equilibrium principle indicates that if there is a mix of dominant strategy combinations in the game, there must be a Nash equilibrium point. By calculation, it can be known by the vehicle and pedestrian mixed-expected return of both sides.

First, for the pure strategy expected benefit analysis of vehicle behavior, the expected benefit $E_{\mathrm{v}}^{\text {pass }}$ when the vehicle chooses to pass is shown in Equation 11:

$$
\begin{aligned}
E_{\mathrm{v}}^{\text {pass }}= & -\sigma_{\mathrm{v}} \alpha_{1} \exp \left(v_{\mathrm{v}}+a_{\mathrm{v}}\right) P_{\mathrm{p}}^{\text {pass }} \\
& +\alpha_{3} \exp \left(v_{\mathrm{v}}\right) P_{\mathrm{p}}^{\text {wait }}
\end{aligned}
$$

The expected benefit $E_{\mathrm{v}}^{\text {wait }}$ when the vehicle chooses to wait is shown in Equation 12:

$$
\begin{aligned}
E_{\mathrm{v}}^{\text {wait }}= & -\left(\alpha_{4} \exp \left(t_{\mathrm{v}}\right)+0.75\right) P_{\mathrm{p}}^{\text {pass }} \\
& +\left(-k \alpha_{5} \exp \left(t_{v}\right)\right) P_{\mathrm{p}}^{\text {wait }}
\end{aligned}
$$

The pure strategy gain analysis for pedestrians shows that the expected gain $E_{\mathrm{p}}^{\text {pass }}$ at pedestrian passage is shown in Equation 13:

$$
\begin{aligned}
E_{\mathrm{p}}^{\text {pass }}= & -\sigma_{\mathrm{p}} \alpha_{2} \exp \left(\left(v_{\mathrm{p}}+a_{\mathrm{p}}\right)\right) P_{\mathrm{v}}^{\text {pass }} \\
& +\alpha_{3} \exp \left(v_{\mathrm{p}}\right) P_{\mathrm{v}}^{\text {wait }}
\end{aligned}
$$

TABLE VII
Game Payoff Matrix
|  | Pedestrian passage | Pedestrian wait |
| :--- | :--- | :--- |
| Vehicle passage | $-\sigma_{\mathrm{v}} \alpha_{1} \exp \left(v_{\mathrm{v}}+a_{\mathrm{v}}\right),-\sigma_{\mathrm{p}} \alpha_{2} \exp \left(v_{\mathrm{p}}+a_{\mathrm{p}}\right)$ | $\alpha_{3} \exp \left(v_{\mathrm{v}}\right),-\alpha_{4} \exp \left(t_{\mathrm{p}}\right)$ |
| Vehicle wait | $-\alpha_{4} \exp \left(t_{\mathrm{v}}\right)-0.75, \alpha_{3} \exp \left(v_{\mathrm{p}}\right)$ | $-k \alpha_{5} \exp \left(t_{v}\right),-k \alpha_{6} \exp \left(t_{\mathrm{p}}\right)$ |


TABLE VIII
Estimated Parameter Values
| Parameter | Calibrated value |  | Standard deviation |  |
| :--- | :--- | :--- | :--- | :--- |
|  | Scene 1 | Scene 2 | Scene 1 | Scene 2 |
| $\alpha_{1}$ | 0.024 | 0.306 | 0.004 | 0.050 |
| $\alpha_{2}$ | 1.651 | 1.004 | 0.030 | 0.006 |
| $\alpha_{3}$ | 0.394 | 1.854 | 0.017 | 0.189 |
| $\alpha_{4}$ | 0.478 | 0.179 | 0.008 | 0.088 |
| $\alpha_{5}$ | 0.038 | 0.229 | 0.007 | 0.126 |
| $\alpha_{6}$ | 0.510 | 0.318 | 0.013 | 0.003 |


The expected gain $E_{\mathrm{p}}^{\text {wait }}$ when the pedestrian chooses to wait is shown in Equation 14:

$$
\begin{aligned}
E_{\mathrm{p}}^{\text {wait }}= & -\alpha_{4} \exp \left(t_{\mathrm{p}}\right) P_{\mathrm{v}}^{\text {pass }} \\
& +\left(-k \alpha_{6} \exp \left(t_{\mathrm{p}}\right)\right) P_{\mathrm{v}}^{\text {wait }}
\end{aligned}
$$

The Nash equilibrium occurs when the expected benefit of passing $E_{\mathrm{v}}^{\text {pass }}$ for vehicles is the same as the expected benefit of waiting $E_{\mathrm{v}}^{\text {wait }}$. The probability combination of passing and waiting for pedestrians is shown below. The Nash equilibrium occurs when the expected benefit of passing $E_{\mathrm{p}}^{\text {pass }}$ and waiting $E_{\mathrm{p}}^{\text {wait }}$ for pedestrians are the same, and the probability combinations of passing and waiting for vehicles are (15)-(18), shown at the bottom of the next page.

The above equations were fitted with nonlinear curves by analyzing the real crossing probabilities and variable imputation for 2,000 pedestrian-vehicle interaction datasets for the two scenes separately, generating and calibrating specific parameter values using the Levenberg-Marquardt algorithm (Table VIII).

## B. Pedestrian Trajectory Prediction Based on Social Statics Game SSG-GAN

1) S-GAN Model: In previous studies, other models could not efficiently model pedestrian interactions in a scene but could learn the average behavior. Gupta et al. [14] built an S-GAN pedestrian trajectory prediction model based on generative adversarial networks to overcome the difficulties in probabilistic computation and behavioral inference. S-GAN aims to learn multiple socially acceptable trajectories. As the inputs remain consistent, it encourages the generative network to extend its distribution and cover the space of possible paths and encodes subtle cues from everyone involved in the scene using global pool vectors.

The scene is preprocessed, and S-GAN defines the pedestrian trajectory as a two-dimensional coordinate position change under the time series for the pedestrian $u$ at moment $t$, with coordinates $\chi_{u}^{t}=\left(x_{u}^{t}, y_{u}^{t}\right)$. The set of historical trajectories $X_{u}$ for each step of pedestrian $u$ from 1 to $t_{o}$ is

$$
X_{u}=\left\{\chi_{u}^{t} \mid t=1,2, \ldots, t_{o}\right\}
$$

In Equation 19, $1 \sim t_{o}$ are the observation frames of the pedestrian history trajectory and $t_{o}$ is the observation frame length. Likewise, vehicle $j$ fits this setting.

The set of predicted trajectories $\hat{Y}_{u}$ for each step of the pedestrian $u$ from $t_{o}+1$ to $t_{p}$ is:

$$
\hat{Y}_{u}=\left\{\chi_{u}^{t} \mid t=t_{o}+1, t_{o}+2, \ldots, t_{o}+t_{p}\right\}
$$

In Equation 20, $t_{o}+1 \sim t_{o}+t_{p}$ is the predicted frame of the pedestrian history trajectory and $t_{p}$ is the predicted frame length.

The set of true historical trajectories $Y_{u}$ for each step within the pedestrian $u$ from $t_{o}+1$ to $t_{p}$ is shown in Equation 21:

$$
Y_{u}=\left\{\chi_{u}^{t} \mid t=t_{o}+1, t_{o}+2, \ldots, t_{o}+t_{p}\right\}
$$

The true historical trajectory $T_{u}^{R}$ and predicted generated trajectory $T_{u}^{G}$ for pedestrians $u$ from 1 to $t_{p}$ are $\left[X_{u}, Y_{u}\right]$ and $\left[X_{u}, \hat{Y}_{u}\right]$, respectively.

The S-GAN comprises a generator and discriminator. Like the pedestrian-vehicle game mechanism, the generator and discriminator in S-GAN will play against each other. The generator generates the simulated data, and the discriminator judges whether the input data are real or generated. The generator aims to improve the data it produces to mislead the discriminator, whereas the discriminator aims to improve the judgment. The following describes the pedestrian trajectory prediction model SSG-GAN embedded with the game mechanism module.
2) Game-Theoretic Embedding Model: As numerous scholars have considered various approaches in traditional trajectory prediction models for specific situations, they frequently use microscopic methods to gather interactional data, such as attention mechanisms [34], visual field domain mechanisms [35], [36], and trajectory prediction by the distance, direction, and speed between pedestrians. The macroscopic approach for both sides of the pedestrian-vehicle interaction is not thoroughly considered. This research will construct a new game neural network model called SSG-GAN based on S-GAN to study and determine the macro pedestrian-vehicle interaction strategy under various circumstances. The pedestrian-vehicle interaction stages are split into the observation and conflict decision regions based on the abovementioned analysis. Both parties pay for their expected benefits through probability in the observation region. When they are in the conflict decision region, the existing
decision is judged and the strategy gain of both parties is directly obtained to achieve a more detailed analysis of the pedestrian-vehicle game process. Finally, the neural network model is jointly driven by microscopic pedestrian-vehicle interaction data and macroscopic pedestrian-vehicle game strategy gain to predict pedestrians trajectories.

As the GAN network model can provide more successful results for pedestrian trajectory prediction, this paper builds the SSG-GAN based on S-GAN for the encoder-decoder architecture. The trajectory definition for pedestrians is the same as the S-GAN setting. Fig. 5 depicts the general layout of the framework.

The trajectory generator encodes and decodes the pedestrian historical trajectory and micro pedestrian-vehicle interaction parameters to output the pedestrian-predicted trajectory. It comprises a trajectory encoder, a gaming mechanism module, a pooling module, and a trajectory decoder. First, the trajectory encoder embeds the pedestrian and vehicle coordinate positions at each time step into the embedding function $\phi$ with a nonlinear activation function to obtain fixed-length vectors $e_{G E_{u}}^{t}$ and $e_{G E_{j}}^{t}$. Then, the pedestrian history-trajectory feature vector $h_{G E_{u}}^{t}$ and vehicle historytrajectory feature vector $h_{G E_{j}}^{t}$ are obtained using LSTM cell encoding.

$$
\begin{aligned}
e_{G E_{u}}^{t}, e_{G E_{j}}^{t}= & {\left[\phi\left(\chi_{u}^{t} ; \omega_{\phi}^{\chi}\right), \phi\left(\chi_{j}^{t} ; \omega_{\phi}^{\chi}\right)\right] } \\
h_{G E_{u}}^{t}, h_{G E_{j}}^{t}= & {\left[L S T M_{G E}\left(h_{G E_{u}}^{t-1}, e_{G E_{u}}^{t}, \omega_{l_{G E}}\right),\right.} \\
& \left.\operatorname{LST} M_{G E}\left(h_{G E_{j}}^{t-1}, e_{G E_{j}}^{t}, \omega_{l_{G E}}\right)\right]
\end{aligned}
$$

In Equations 22 and 23, the embedding function $\phi$ is the fully connected neural network layer, $\omega_{\phi}^{\chi}$ is the weight parameter of the embedding function, and $\omega_{l_{G E}}$ is the LSTM cell weight parameter.

The game module is based on the game payment function proposed above for both sides of the vehicles and pedestrians, and microdata, such as velocity, acceleration, relative distance, and waiting time, are extracted. PET at this time is obtained using the velocity of both sides at each time step and the interval distance from the conflict area. The PET value indicates the danger level of the interaction between the two sides at this time step. In addition, the position coordinates of both parties at this time indicate whether they are in the judgment or decision areas. In this paper, all pedestrians and vehicles are calibrated for interaction decision during data processing: passing, waiting, and judging. The real-world interaction decisions of both parties are used for calibration. The waiting time is calibrated to 0 when the pedestrian and vehicle are watching and judging and -1 when both are passing. When one is passing and the other is waiting, the passing party is calibrated to 1 and the waiting party is calibrated to the real-time waiting time. When both sides are waiting, both are calibrated as waiting time. In the game module, the neural network determines the current state of the interaction according to different calibration results. When both sides are observing, the specific expected utilities of both sides are obtained by counting the cross-street probabilities. When both parties make decisions, the game utility is calculated using the above game matrix and real-time microscopic data. The specific expectation utilities $g_{u}^{t}$ and $g_{j}^{t}$ of both parties under the decision are obtained, and the specific expected utility influences the vectors of historical-trajectory features of both parties to obtain the game feature vectors $h_{G A_{u}}^{t}$ and $h_{G A_{j}}^{t}$ is fused into the mixed game feature vector $h_{G A_{u, j}}^{t}$ of the vehicle and pedestrian.

$$
\begin{aligned}
\sigma_{u / j}^{t}, \eta_{u / j}^{t} & =\left[f_{\text {pet }}\left(t_{\text {pet }}, \omega_{\text {pet }}\right), f_{R}\left(\chi_{u}^{t}, \chi_{j}^{t}, \omega_{R}\right)\right] \\
g_{u / j}^{t} & =f_{\text {pay }}\left(\sigma_{u / j}^{t}, \eta_{u / j}^{t}, \text { pay }_{s_{i}, t}^{u / j}\right) \\
h_{G A_{u / j}}^{t} & =f_{\text {inf }}\left(h_{G E_{u / j}}^{t}, g_{u / j}^{t}\right) \\
h_{G A_{u, j}}^{t} & =f_{\text {mix }}\left(h_{G A_{u}}^{t}, h_{G A_{j}}^{t}\right)
\end{aligned}
$$

In Equation 24, $\sigma_{u / j}^{t}$ is the collision severity factor of pedestrian $u$ and vehicle, $j, \eta_{u / j}^{t}$ is the real-time coordinate area of pedestrian $u$ and vehicle $j, f_{\text {pet }}$ is the collision degree determination function, $f_{R}$ is the real-time area judgment function, $t_{\text {pet }}$ is the PET of pedestrian-vehicle interaction, $\omega_{\text {pet }}$ is the collision degree weight parameter, and $\omega_{R}$ is the real-time area weight parameter.

In Equations 25-27, $f_{\text {pay }}$ is the game calculation function, $p a y_{s_{i}, t}^{u / j}$ represents the game payment function under different decisions of the vehicle and pedestrian in Table VI and is the specific payment function at time $t$ for pedestrians or vehicles choosing different strategies $s_{i} . f_{i n f}$ is the game influence function, and $f_{\text {mix }}$ is the game mixture function.

The pooling module embeds the relative pedestrian-vehicle distances into the embedding function $\phi$ to obtain the pedestrian-vehicle relative position feature vector $h_{R P}^{t}$, which is connected with the pedestrian-vehicle mixed game feature vector $h_{G A_{u, j}}^{t}$ and finally output by the multilayer perceptron to obtain the game pooling vector $\gamma_{u / j}^{t}$.

$$
\begin{aligned}
h_{R P}^{t} & =\phi\left(\chi_{u}^{t}, \chi_{j}^{t}, \omega_{\phi}^{R P}\right) \\
\gamma_{u / j}^{t} & =\operatorname{Ml} p_{G P}\left(\operatorname{Cat}\left(h_{R P}^{t}, h_{G A_{u, j}}^{t}\right), \omega_{m l p}^{G P}\right)
\end{aligned}
$$

$$
\begin{aligned}
P_{\mathrm{p}}^{\text {cross }} & =\frac{\alpha_{3} \exp \left(v_{\mathrm{v}}\right)+k \alpha_{5} \exp \left(t_{v}\right)}{\sigma_{\mathrm{v}} \alpha_{1} \exp \left(v_{\mathrm{v}}+a_{\mathrm{v}}\right)+\alpha_{3} \exp \left(v_{\mathrm{v}}\right)+k \alpha_{5} \exp \left(t_{v}\right)+0.75-\alpha_{4} \exp \left(t_{\mathrm{v}}\right)} \\
P_{\mathrm{p}}^{\text {wait }} & =1-\frac{\alpha_{3} \exp \left(v_{\mathrm{v}}\right)+k \alpha_{5} \exp \left(t_{v}\right)}{\sigma_{\mathrm{v}} \alpha_{1} \exp \left(v_{\mathrm{v}}+a_{\mathrm{v}}\right)+\alpha_{3} \exp \left(v_{\mathrm{v}}\right)+k \alpha_{5} \exp \left(t_{v}\right)+0.75-\alpha_{4} \exp \left(t_{\mathrm{v}}\right)} \\
P_{\mathrm{v}}^{\text {cross }} & =\frac{\alpha_{3} \exp \left(v_{\mathrm{p}}\right)+k \alpha_{6} \exp \left(t_{\mathrm{p}}\right)}{\sigma_{\mathrm{p}} \alpha_{2} \exp \left(v_{\mathrm{p}}+a_{\mathrm{p}}\right)+\alpha_{3} \exp \left(v_{\mathrm{p}}\right)+k \alpha_{6} \exp \left(t_{\mathrm{p}}\right)-\alpha_{4} \exp \left(t_{\mathrm{p}}\right)} \\
P_{\mathrm{v}}^{\text {wait }} & =1-\frac{\alpha_{3} \exp \left(v_{\mathrm{p}}\right)+k \alpha_{6} \exp \left(t_{\mathrm{p}}\right)}{\sigma_{\mathrm{p}} \alpha_{2} \exp \left(v_{\mathrm{p}}+a_{\mathrm{p}}\right)+\alpha_{3} \exp \left(v_{\mathrm{p}}\right)+k \alpha_{6} \exp \left(t_{\mathrm{p}}\right)-\alpha_{4} \exp \left(t_{\mathrm{p}}\right)}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-11.jpg?height=443&width=1794&top_left_y=180&top_left_x=165)
Fig. 5. Diagram of the proposed model. Our model consists of a generator and a discriminator, while the features of the pedestrian-vehicle game are recorded and packaged to be uploaded to the game module for training to improve the prediction quality of pedestrian trajectories.

In Equations 28 and 29, $M l p_{G P}$ is the pooling module multilayer perceptron network layer, Cat connects the feature vectors, and $\omega_{\phi}^{R P}$ and $\omega_{m l p}^{G P}$ are the weight parameters corresponding to the respective network layers.

Finally, the trajectory decoder connects the game pooling vector $\gamma_{u / j}^{t}$ with the pedestrian historical-trajectory feature vector $h_{G E_{u}}^{t}$. Through the decoder module multilayer perceptron $M l p_{G D}$, connects it with the network random Gaussian noise $Z$ to finally obtain the decoder feature vector $h_{G D_{u}}^{t} . h_{G D_{u}}^{t}$ is input to the LSTM neural network layer with the pedestrian coordinate vector $h_{C O_{u}}^{t}$ and the initialized cell all-zero vector $c_{u}^{t}$ after encoding using the embedding function to obtain the vector $\lambda_{u}^{t} . \lambda_{u}^{t}$ is passed through the decoder multilayer perceptron to obtain the predicted coordinates $\hat{Y}_{u}$ of the pedestrian trajectory.

$$
\begin{aligned}
h_{G D_{u}}^{t} & =\operatorname{Cat}\left[M l_{p_{G D}}\left(\operatorname{Cat}\left(\gamma_{u / j}^{t}, h_{G E_{u}}^{t}\right) ; \omega_{m l p}^{G D}\right), Z\right] \\
h_{C O_{u}}^{t} & =\phi\left(\chi_{u}^{t} ; \omega_{\phi}^{C O}\right) \\
\lambda_{u}^{t} & =\operatorname{LST} M\left(h_{G D_{u}}^{t}, h_{C O_{u}}^{t}, c_{u}^{t}, \omega_{\lambda}\right) \\
\hat{Y}_{u} & =\operatorname{Mlp}_{G D}\left(\lambda_{u}^{t}, \omega_{m l p}^{G D}\right)
\end{aligned}
$$

In Equations 30-33, $\omega_{m l p}^{G D}, \omega_{\phi}^{C O}$, and $\omega_{\lambda}$ are the weight parameters of the corresponding network layers.

The trajectory discriminator is designed to identify true and false trajectories. The predicted trajectory $\hat{Y}_{u}$ output from the trajectory generator and the true pedestrian history trajectory $Y_{u}$ are input into the discriminator neural network. The high-dimensional feature vector $h_{P_{u}}^{t}$ is output through the embedded fully connected neural network layer and then passed through the LSTM neural network layer and the discriminator multilayer perceptron in turn. The final output is obtained as the probability of the true trajectory.

$$
\begin{aligned}
h_{P_{u}}^{t} & =\phi\left(\hat{Y}_{u}, Y_{u}, \omega_{\phi}^{P}\right) \\
\Psi_{u}^{t} & =\operatorname{LST} M\left(h_{P_{u}}^{t}, \Psi_{u}^{t-1}, \omega_{l_{\Psi}}\right) \\
P_{\text {real }} & =\operatorname{Mlp}_{\Psi}\left(\Psi_{u}^{t}, \omega_{m l p}^{\Psi}\right)
\end{aligned}
$$

In Equations 34-36, $\Psi_{u}^{t}$ is the output vector of the LSTM network layer, $\omega_{\phi}^{P}, \omega_{l_{\Psi}}$, and $\omega_{m l p}^{\Psi}$ correspond to the weight parameters of the respective network layers, and $P_{\text {real }}$ is the probability of discriminating a true trajectory.

In this paper, the loss function $L_{S S G-G A N}$ contains the cross-entropy loss function $L_{G A N}(G, D)$ of the generator and discriminator, with the minimum difference loss function $L_{L 2}(G)$ between the true and predicted trajectories.

$$
\begin{aligned}
L_{S S G-G A N}= & L_{G A N}(G, D)+L_{L 2}(G) \\
L_{G A N}(G, D)= & \min _{G} \max _{D} E_{r \sim D}(\log D(r)) \\
& +E_{Z \sim G}(\log (1-D(G(Z)))) \\
L_{L 2}(G)= & \min _{\Omega}\left\|\left(x^{i}, y^{i}\right)-\left(x^{i}, y^{i}\right)^{(\Omega)}\right\|_{2}
\end{aligned}
$$

In Equations 37-39, $E$ is the resulting expected value, $r$ is the input real trajectory data, $\Omega$ is the number of samples based on the model generated results, and $Z$ is the input Gaussian noise distribution.

## V. Experiments

We collated the collected data and extracted 1,500 valid pedestrian-vehicle interaction trajectories for each Scene, for 3,000 trajectories divided into commuting and noncommuting periods. Four datasets were formed, with 750 pedestrian-vehicle interaction trajectories for each dataset. The format of the trajectories is explained in Table III. The pedestrian trajectory dataset was used as input to the SSG-GAN model. The analysis of pedestrian-vehicle interaction time reveals that most interactions are between 2 and 4 s, and the shorter interactions are in the pedestrian-win or vehiclewin states, whereas the longer interactions are in the conflict and waiting states. Therefore, we chose to compare the average displacement error (ADE) and final displacement error (FDE) of trajectory prediction metrics for three prediction time domains (2.4, 3.2, and 4 s) and visualize the trajectory prediction results. Visualization analysis was performed. Fig. 6 shows some pedestrian-vehicle trajectory calibration results.

In this paper, the pedestrian trajectory prediction model is trained, and the proposed SSG-GAN algorithm is based on the Windows 10 operating system with a deep-learning framework configuration of Pytorch 1.8.1, CUDA 10.2, cuDNN 7.6.5, CPU of Inter i7-10700K, and GPU of NVIDIA Quadro RTX 5000. Using the Adam algorithm optimizer, the learning rate of the trajectory generator is 0.0005, the learning rate of the trajectory discriminator is 0.001, the training batch size is 64, and iterations are 400. The error evaluation metrics are set as ADE and FDE. ADE is expressed as the average distance between the predicted and historical true trajectories of all measured pedestrians at each moment. FDE represents the final

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-12.jpg?height=498&width=868&top_left_y=185&top_left_x=172)
Fig. 6. Part of the pedestrian-vehicle trajectory calibration diagram.

displacement distance between the predicted and historical true trajectories of all measured pedestrians at the last moment, as shown in the following Equations 40-41.

$$
\begin{aligned}
& A D E=\frac{1}{n} \sum_{u=1}^{n} \frac{1}{t_{p}} \sum_{t=t_{0}+1}^{t_{0}+t_{p}} \sqrt{\left(x_{u}^{t}-\hat{x}_{u}^{t}\right)^{2}+\left(y_{u}^{t}-\hat{y}_{u}^{t}\right)^{2}} \\
& F D E=\frac{1}{n} \sum_{u=1}^{n} \sqrt{\left(x_{u}^{t_{p}}-\hat{x}_{u}^{t_{p}}\right)^{2}+\left(y_{u}^{t_{p}}-\hat{y}_{u}^{t_{p}}\right)^{2}}
\end{aligned}
$$

In Equations 40 and 41, $\left(x_{u}^{t}, y_{u}^{t}\right)$ is the true position of pedestrian $u$ at time $t$ and $\left(\hat{x}_{t}^{u}, \hat{y}_{t}^{u}\right)$ is the predicted position of pedestrian $u$ at time $t$.

We use LSTM, S-LSTM, S-GAN, Sophie [37], and SSG-GAN models for the same experimental comparison to highlight the effectiveness of the pedestrian-vehicle interaction game mechanism in the SSG-GAN algorithm to improve the accuracy of pedestrian trajectory prediction. LSTM is a pedestrian trajectory prediction algorithm based on RNNs with the long and short-term memory model, S-LSTM is a pedestrian trajectory prediction algorithm that considers the social status among pedestrians, S-GAN is a pedestrian trajectory prediction algorithm that considers the relative distance between pedestrians, and Sophie is a pedestrian trajectory prediction model that combines social and physical information. Based on the above algorithm, the input observation time is 8 time steps, the output prediction time is 4 time steps (total 2.4 s), 8 time steps (total 3.2 s), and 12 time steps (total 4 s), and the error evaluation index is used for the comparative analysis of different algorithms.

## VI. Results and Discussions

Fig. 7 shows the comparative analysis of ADE and FDE errors between SDG-GAN and S-GAN at prediction times of 2.4, 3.2, and 4 s. From Fig.7, both algorithms show a clear trend of loss-decreasing convergence in the first 100 training iteration cycles of the four-step prediction, but SSG-GAN algorithm does not exceed the loss-decreasing rate of the S-GAN algorithm in the early stage. As the training iterations increase, the loss-decreasing speed of both algorithms decreases and stabilizes. The loss-decreasing speed of the SSG-GAN algorithm considerably exceeds the S-GAN algorithm in the later stage, and the loss value is smaller than that of the S-GAN algorithm. In the prediction 8 and 12 steps, the loss-decline rate of SSG-GAN algorithm is always lower than that of the S-GAN algorithm, and the loss value of the SSG-GAN algorithm is still lower than that of the S-GAN algorithm when the respective algorithms converge.

Table IX shows the results of the comparative analysis of the proposed trajectory algorithm with four different trajectory prediction algorithms for ADE, FDE, and AVG for the prediction times of 2.4, 3.2, and 4 s. The results show that in the four datasets, our proposed model has the lowest error than the other models in most cases. The average ADE loss for the three prediction times was the lowest, and the average FDE loss was the lowest in the 2.4 s prediction. Some FDE loss values are slightly higher than Sophie in the other prediction time domains, and the results of all evaluation metrics are better than the original model. Meanwhile, we also performed the corresponding ablation experiments on the proposed model.

As shown in Table X, we executed different versions of SSG-GAN for all datasets and all prediction time domains, $G_{N}+S_{\mathrm{N}}$ represents the SSG-GAN model without the game module and social features, $G_{\mathrm{N}}+S_{\mathrm{O}}$ represents the SSG-GAN model with social features but without the game module, $G_{\mathrm{O}}+S_{\mathrm{N}}$ represents the SSG-GAN model with the game module but without the social features, and finally $G_{\mathrm{O}}+S_{\mathrm{O}}$ represents the SSG-GAN model contains both game module and social features. The ablation experiment reveals that among the different versions, the model $G_{N}+S_{\mathrm{N}}$ without the gaming module and the social features has the least optimal results, while the version with only the gaming module or the social information alone is clearly optimized, and the optimization brought about by the gaming module in comparison is larger than the enhancement brought about by the social information to a certain extent. Finally, it should be noted that the full-fledged $G_{\mathrm{O}}+S_{\mathrm{O}}$ with both the gaming module and social information undoubtedly brings the greatest optimization improvement.

In addition, the multimodal performance of the model is also an area of concern, and we verified the multimodal performance of the model by drawing multiple samples without loss of diversity. In the next experiments, we performed comparison experiments from 10 samples to 100 samples in increments of 10 samples at a time. The Fig. 8 shows the multimodal and non-multimodal models, respectively. The multimodal model is trained and tested using multiple samples according to the experimental schedule to predict pedestrian trajectories, and the multimodal model has diversity loss. While the nonmultimodal model draws one sample during training and draws the same sample as the experimental progress during testing. From the analysis of the results, it can be seen that the multimodal performance improves the accuracy of our model by 22.7\% on ADE and 24.9\% on FDE.

Fig. 9 shows the visualization comparison of all trajectory prediction algorithms. In this study, the pedestrian-vehicle game is divided into an observation phase and a decision phase. Each column represents a different phase, containing two sets of trajectory samples. In the observation stage, the

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-13.jpg?height=1008&width=1783&top_left_y=180&top_left_x=172)
Fig. 7. Comparison analysis chart:(a) Comparison of the ADE of SSG-GAN and S-GAN algorithms in 2.4s. (b) Comparison of the ADE of SSG-GAN and S-GAN algorithms in 3.2s. (c) Comparison of the ADE of SSG-GAN and S-GAN algorithms in 4s. (d) Comparison of FDE of SSG-GAN and S-GAN algorithms in 2.4s. (e) Comparison of FDE of SSG-GAN and S-GAN algorithms in 3.2s. (f) Comparison of FDE of SSG-GAN and S-GAN algorithms in 4s.

TABLE IX
Comparison of Trajectory Prediction Algorithm Errors
| Metric | Dataset | LSTM | S-LSTM | S-GAN | Sophie | SSG-GAN [Ours] |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ADE | CP1 | 0.223/0.368/0.594 | 0.204/0.315/0.551 | 0.190/0.301/0.538 | 0.175/0.279/0.496 | 0.177/0.270/0.482 |
|  | NCP1 | 0.225/0.371/0.592 | 0.207/0.321/0.563 | 0.187/0.304/0.531 | 0.176/0.274/0.488 | 0.179/0.268/0.484 |
|  | CP2 | 0.336/0.637/1.042 | 0.323/0.626/0.936 | 0.312/0.614/0.917 | 0.281/0.578/0.871 | 0.268/0.571/0.863 |
|  | NCP2 | 0.339/0.644/1.033 | 0.331/0.623/0.941 | 0.316/0.619/0.906 | 0.293/0.564/0.869 | 0.274/0.569/0.866 |
| AVG |  | 0.281/0.505/0.815 | 0.266/0.471/0.747 | 0.251/0.459/0.723 | 0.231/0.424/0.681 | 0.224/0.419/0.673 |
| FDE | CP1 | 0.372/0.738/1.282 | 0.341/0.638/1.180 | 0.303/0.605/1.159 | 0.293/0.533/0.967 | 0.284/0.502/0.938 |
|  | NCP1 | 0.379/0.752/1.257 | 0.349/0.631/1.189 | 0.297/0.614/1.148 | 0.289/0.520/0.959 | 0.286/0.507/0.945 |
|  | CP2 | 0.572/1.297/2.229 | 0.549/1.287/1.986 | 0.515/1.225/1.918 | 0.482/0.994/1.691 | 0.458/1.091/1.732 |
|  | NCP2 | 0.581/1.312/2.137 | 0.546/1.259/2.016 | 0.518/1.217/1.923 | 0.494/0.956/1.632 | 0.466/1.083/1.736 |
| AVG |  | 0.476/1.025/1.726 | 0.446/0.953/1.592 | 0.408/0.915/1.537 | 0.389/0.751/1.312 | 0.373/0.795/1.337 |


CP1 represents the Scene 1 commuting dataset, NCP1 represents the Scene 1 non-commuting dataset, CP2 represents the Scene 2 commuting dataset, and NCP2 represents the Scene 2 non-commuting dataset, AVG is the average loss.
vehicle and pedestrian are not decided and the SSG-GAN algorithm obtains the expected return of the pedestrian game through realistic passage probability and combines the relative positions of the pedestrian and the vehicle to influence the prediction result of the pedestrian trajectory jointly. Therefore, the prediction mechanism is perfect, and the prediction result is the best.

In the decision phase, when the pedestrian game is successful, the pedestrian static game payoff is positive and the vehicle static game payoff is negative. The game mechanism indicates that the vehicle hazard is reduced and motivates the pedestrian to walk forward. When the pedestrian game fails, the pedestrian static game pays negatively, and the vehicle static game pays positively. The game mechanism inhibits the pedestrian from proceeding and amplifies the vehicle passing hazard. The pedestrian and vehicle static game payoffs are negative when a pedestrian-vehicle collision occurs. The game mechanism indicates that the probability of conflict between the two sides increases rapidly, influencing the pedestrian trajectory by refining the severity of the conflict between the two sides based on their microscopic data. When the pedestrian and vehicle are waiting simultaneously, traffic congestion starts, traffic efficiency decreases, and both sides have negative static game payments, and the game mechanism affects pedestrian trajectory prediction through the regret factor.

TABLE X
Comparison of Ablation Experiments
| Metric | Dataset | SSG-GAN (Ours) |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | $\mathbf{G}_{\mathrm{N}}+\mathbf{S}_{\mathrm{N}}$ | $\mathbf{G}_{\mathrm{N}}+\mathbf{S}_{\mathrm{O}}$ | $\mathbf{G}_{\mathrm{O}}+\mathbf{S}_{\mathrm{N}}$ | $\mathbf{G}_{\mathrm{O}}+\mathbf{S}_{\mathrm{O}}$ |
| ADE | CP1 | 0.216/0.349/0.584 | 0.197/0.316/0.544 | 0.198/0.311/0.557 | 0.177/0.270/0.482 |
|  | NCP1 | 0.218/0.353/0.575 | 0.201/0.315/0.550 | 0.191/0.319/0.546 | 0.179/0.268/0.484 |
|  | CP2 | 0.334/0.641/0.964 | 0.314/0.617/0.928 | 0.317/0.632/0.925 | 0.268/0.571/0.863 |
|  | NCP2 | 0.336/0.635/0.971 | 0.320/0.624/0.929 | 0.315/0.626/0.920 | 0.274/0.569/0.866 |
| AVG |  | 0.276/0.495/0.774 | 0.258/0.468/0.738 | 0.255/0.472/0.737 | 0.224/0.419/0.673 |
| FDE | CP1 | 0.354/0.696/1.264 | 0.319/0.630/1.124 | 0.325/0.622/1.133 | 0.284/0.502/0.938 |
|  | NCP1 | 0.357/0.702/1.243 | 0.327/0.616/1.130 | 0.318/0.631/1.126 | 0.286/0.507/0.945 |
|  | CP2 | 0.556/1.278/2.065 | 0.524/1.200/1.921 | 0.529/1.230/1.917 | 0.458/1.091/1.732 |
|  | NCP2 | 0.561/1.273/2.091 | 0.532/1.225/1.925 | 0.526/1.229/1.913 | 0.466/1.083/1.736 |
| AVG |  | 0.457/0.987/1.666 | 0.426/0.918/1.525 | 0.425/0.928/1.521 | 0.373/0.795/1.337 |


$\mathbf{G}_{\mathrm{N}}+\mathbf{S}_{\mathrm{N}}$ represents the SSG-GAN model without the game module and social features, $\mathbf{G}_{\mathrm{N}}+\mathbf{S}_{\mathrm{O}}$ represents the SSG-GAN model with social features but without the game module, $\mathbf{G}_{\mathrm{O}}+\mathbf{S}_{\mathrm{N}}$ represents the SSG-GAN model with the game module but without the social features, and finally $\mathbf{G}_{\mathrm{O}}+\mathbf{S}_{\mathrm{O}}$ represents the SSG-GAN model contains both game module and social features.

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-14.jpg?height=688&width=1656&top_left_y=990&top_left_x=238)
Fig. 8. Model multimodal effects, we generated only one sample during training and drawed N samples during testing as no multimodal effects. Using N samples during training and testing as multimodal influence.

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-14.jpg?height=593&width=1777&top_left_y=1783&top_left_x=178)
Fig. 9. Comparison diagrams of trajectory prediction visualization.

Compared with other algorithms, the SSG-GAN considering the relationship between pedestrians and algorithm proposed in this paper integrates macroscopic vehicles more comprehensively. It can truly reflect game parameters and microscopic motion parameters, pedestrians under the game state and improve the
accuracy and interpretability of predicting pedestrian trajectories.

## VII. Conclusion

Most current pedestrian trajectory prediction algorithms rely on microscopic motion data for analysis. We proposed the SSG-GAN algorithm, which combines microscopic parameters and macroscopic game decisions. At the microscopic level, microscopic data of vehicles and pedestrians are obtained through their relative movements. At the macroscopic level, the decision-making process under game theory is carefully developed. The proposed algorithm could analyze the trajectory change of pedestrians in the pedestrian-vehicle game state through both aspects. Compared with other algorithms, the error values of the proposed model are smaller in the evaluation indices, such as ADE and FDE. It improves the interpretability and accuracy of pedestrian trajectory prediction. The model proposed in this paper could provide reliable path planning [38] for autonomous vehicles and is crucial in reducing traffic accident rates and improving the traffic efficiency. In addition, the game idea proposed by the model can play an important role in vehicle-to-vehicle interaction [39].

The pedestrian-vehicle interaction studied so far is frequently analyzed for single pedestrians and vehicles. In the future, we will generalize the research into a multi pedestrian-vehicle game. It is also interesting to supplement the general scenes of straight and left-turn lanes to develop a more comprehensive algorithm. In addition, more data will be collected, and other microscopic parameters will be added to improve the accuracy and interpretability of the proposed pedestrian trajectory prediction model and algorithm.

## References

[1] Global Status Report on Road Safety 2018, World Health Organization, Geneva, Switzerland, 2018.
[2] H. W. McGee and J. Soika, "Navigating safety at unsignalized intersections," Public Roads., vol. 79, no. 4, Feb. 2016. [Online]. Available: https://highways.dot.gov/public-roads/januaryfebruary-2016
[3] P. Chen, W. Zeng, and G. Yu, "Assessing right-turning vehicle-pedestrian conflicts at intersections using an integrated microscopic simulation model," Accident Anal. Prevention, vol. 129, pp. 211-224, Aug. 2019.
[4] A. Kumar, M. Paul, and I. Ghosh, "Analysis of pedestrian conflict with right-turning vehicles at signalized intersections in India," J. Transp. Eng., A, Syst., vol. 145, no. 6, Jun. 2019, Art. no. 04019018.
[5] F. Xin, X. Wang, and C. Sun, "Risk evaluation for conflicts between crossing pedestrians and right-turning vehicles at intersections," Transp. Res. Rec., J. Transp. Res. Board, vol. 2675, no. 12, pp. 1005-1014, Aug. 2021.
[6] S. Teng et al., "Motion planning for autonomous driving: The state of the art and future perspectives," IEEE Trans. Intell. Veh., vol. 8, no. 6, pp. 3692-3711, Jun. 2023.
[7] L. Li and F.-Y. Wang, "The automated lane-changing model of intelligent vehicle highway systems," in Proc. IEEE 5th Int. Conf. Intell. Transp. Syst., Sep. 2002, pp. 216-218.
[8] D. Helbing and P. Molnár, "Social force model for pedestrian dynamics," Phys. Rev. E, Stat. Phys. Plasmas Fluids Relat. Interdiscip. Top., vol. 51, no. 5, pp. 4282-4286, May 1995.
[9] E. Dynkin, "Markov processes," in Die Grundlehren der Mathematischen Wissenschaften, vols. 121-122. Berlin, Germany: Courier Corporation, 1965, pp. 77-104.
[10] J. H. Lee and N. L. Ricker, "Extended Kalman filter based nonlinear model predictive control," Ind. Eng. Chem. Res., vol. 33, no. 6, pp. 1530-1541, Jun. 1994.
[11] K. Cho et al., "Learning phrase representations using RNN encoderdecoder for statistical machine translation," 2014, arXiv:1406.1078.
[12] Y. Yu, X. Si, C. Hu, and J. Zhang, "A review of recurrent neural networks: LSTM cells and network architectures," Neural Comput., vol. 31, no. 7, pp. 1235-1270, Jul. 2019.
[13] I. J. Goodfellow et al., "Generative adversarial networks," Commun. ACM, vol. 63, no. 11, pp. 139-144, 2020.
[14] A. Gupta, J. Johnson, L. Fei-Fei, S. Savarese, and A. Alahi, "Social GAN: Socially acceptable trajectories with generative adversarial networks," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit., Jun. 2018, pp. 2255-2264.
[15] A. Alahi, K. Goel, V. Ramanathan, A. Robicquet, L. Fei-Fei, and S. Savarese, "Social LSTM: Human trajectory prediction in crowded spaces," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2016, pp. 961-971.
[16] D. Fudenberg and J. Tirole, Game Theory. Cambridge, MA, USA: MIT Press; 1991.
[17] J. F. Nash, "Non-cooperative games," Ann. Math., vol. 54, no. 2, pp. 286-295, 1951.
[18] J. Nash, "Two-person cooperative games," Econometrica, vol. 21, no. 1, pp. 128-140, 1953.
[19] T. Başar and G. J. Olsder, Dynamic Noncooperative Game Theory. Philadelphia, PA, USA: Society for Industrial and Applied Mathematics, 1998.
[20] M. A. Nowak and R. M. May, "Evolutionary games and spatial chaos," Nature, vol. 359, no. 6398, pp. 826-829, 1992.
[21] J. G. Wardrop, "Road paper. Some theoretical aspects of road traffic research," Proc. Inst. Civil Eng., vol. 1, no. 3, pp. 325-362, May 1952.
[22] W. Wu, R. Chen, H. Jia, Y. Li, and Z. Liang, "Game theory modeling for vehicle-pedestrian interactions and simulation based on cellular automata," Int. J. Modern Phys. C, vol. 30, no. 4, Apr. 2019, Art. no. 1950025.
[23] C. Yang, J. Wang, and J. Dong, "Capacity model of exclusive right-turn lane at signalized intersection considering pedestrian-vehicle interaction," J. Adv. Transp., vol. 2020, pp. 1-19, Aug. 2020.
[24] R. Zhang, Z. Wei, H. Gu, and S. Qiu, "Behavior evolution of multigroup in the process of pedestrian crossing based on evolutionary game theory," Sustainability, vol. 13, no. 4, p. 2009, Feb. 2021.
[25] G. Cheng, B. Liu, L. Wu, Q. Fang, and K. Yu, "Noncooperative dynamic game model between drivers and crossing pedestrians," Adv. Mech. Eng., vol. 7, no. 2, Nov. 2014, Art. no. 359528.
[26] S. K. Jayaraman, D. M. Tilbury, X. Jessie Yang, A. K. Pradhan, and L. P. Robert, "Analysis and prediction of pedestrian crosswalk behavior during automated vehicle interactions," in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), France, May 2020, pp. 6426-6432.
[27] Y. Rahmati, A. Talebpour, A. Mittal, and J. Fishelson, "Game theorybased framework for modeling human-vehicle interactions on the road," Transp. Res. Rec., J. Transp. Res. Board, vol. 2674, no. 9, pp. 701-713, Jul. 2020.
[28] A. Bighashdel, P. Meletis, and G. Dubbelman, "Towards equilibriumbased interaction modeling for pedestrian path prediction," in Proc. IEEE 23rd Int. Conf. Intell. Transp. Syst. (ITSC), Sep. 2020, pp. 1-8.
[29] X. Sun, K. Lin, Y. Wang, S. Ma, and H. Lu, "A study on pedestrianvehicle conflict at unsignalized crosswalks based on game theory," Sustainability, vol. 14, no. 13, p. 7652, Jun. 2022.
[30] S. Feng and Y. Pei, "Analysis of vehicle delay on road sections on the condition of pedestrian crossing," J. Transp. Syst. Eng. Inf. Technol., vol. 7, no. 3, pp. 73-77, Jun. 2007.
[31] Y. Zhang and J. D. Fricker, "Incorporating conflict risks in pedestrianmotorist interactions: A game theoretical approach," Accident Anal. Prevention, vol. 159, Sep. 2021, Art. no. 106254.
[32] R. E. Chandler, R. Herman, and E. W. Montroll, "Traffic dynamics: Studies in car following," Oper. Res., vol. 6, no. 2, pp. 165-184, Apr. 1958.
[33] D. C. Gazis, R. Herman, and R. W. Rothery, "Nonlinear follow-theleader models of traffic flow," Oper. Res., vol. 9, no. 4, pp. 545-567, Aug. 1961.
[34] D. Varshneya and G. Srinivasaraghavan, "Human trajectory prediction using spatially aware deep attention models," 2017, arXiv:1705.09436.
[35] W. Li, K. Xiao, and S. Shi, "Micro-interaction model based on pedestrian visual field of attention," Auto Eng., vol. 44, pp. 808-820, Jun. 2022.
[36] W. Li, Y. Zhang, and M. Wang, "Pedestrian trajectory prediction based on field of view mechanism," Comput. Appl. Res., vol. 40, no. 1, pp. 80-85, Jan. 2023.

[37] A. Sadeghian, V. Kosaraju, A. Sadeghian, N. Hirose, H. Rezatofighi, and S. Savarese, "SoPhie: An attentive GAN for predicting paths compliant to social and physical constraints," in Proc. IEEE/CVF Conf. Comput. Vis. Pattern Recognit. (CVPR), Jun. 2019, pp. 1349-1358.
[38] N. Djuric et al., "Uncertainty-aware short-term motion prediction of traffic actors for autonomous driving," in Proc. IEEE Winter Conf. Appl. Comput. Vis. (WACV), Mar. 2020, pp. 2084-2093.
[39] W. Li, F. Qiu, L. Li, Y. Zhang, and K. Wang, "Simulation of vehicle interaction behavior in merging scenarios: A deep maximum entropyinverse reinforcement learning method combined with game theory," IEEE Trans. Intell. Vehicles, vol. 9, no. 1, pp. 1079-1093, Jan. 2024, doi: 10.1109/TIV.2023.3323138.
![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-16.jpg?height=320&width=254&top_left_y=718&top_left_x=168)
Wenli Li received the Ph.D. degree in mechatronic engineering from Southwest Jiaotong University, Chengdu, China, in 2016. He conducted his postdoctoral research with Chongqing University. He has been a Visiting Scholar with the Transportation Active Safety Institute, Indiana University-Purdue University Indianapolis (IUPUI). He is currently an Associate Professor with the Key Laboratory of Advanced Manufacturing Technology for Automobile Parts, International Joint Laboratory of Intelligent Manufacturing \& Control of Key Parts for Energy-Efficient \& New Energy Vehicles, Ministry of Education, Chongqing University of Technology. His research interests include intelligent vehicles, automobile safety tests, and simulation.
![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-16.jpg?height=318&width=256&top_left_y=1280&top_left_x=168)
Yinan Zhang received the B.E. degree in 2021. He is currently pursuing the master's degree with the School of Vehicle Engineering, Chongqing University of Technology. His main research interests include intelligent vehicles, pedestrian-vehicle interaction mechanisms, pedestrian-vehicle behavior simulation, and trajectory prediction.

![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-16.jpg?height=316&width=251&top_left_y=208&top_left_x=1083)

Lingxi Li (Senior Member, IEEE) received the B.E. degree in automation from Tsinghua University, Beijing, China, in 2000, the M.S. degree in control theory and control engineering from Chinese Academy of Sciences, Beijing, in 2003, and the Ph.D. degree in electrical and computer engineering from the University of Illinois at Urbana-Champaign, Champaign, IL, USA, in 2008.
Since August 2008, he has been with Indiana University-Purdue University Indianapolis (IUPUI), where he is currently a Professor of electrical and computer engineering. He has authored/coauthored one book and more than 150 research papers in refereed journals and conferences. His research interests include modeling, analysis, control, and optimization of complex systems, intelligent transportation systems, intelligent vehicles, discrete-event systems, human-machine interaction, and parallel intelligence. He was a recipient of five best paper awards, the 2021 IEEE Intelligent Transportation Systems Society Outstanding Application Award, the 2017 Outstanding Research Contributions Award, the 2012 T-ITS Outstanding Editorial Service Award, and multiple university research/teaching awards. He is serving as an associate editor for five international journals.
![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-16.jpg?height=318&width=258&top_left_y=915&top_left_x=1079)

Yisheng Lv (Senior Member, IEEE) is currently a Professor with the State Key Laboratory of Multimodal Artificial Intelligence Systems, Institute of Automation, Chinese Academy of Sciences, Beijing, China. He is also with the University of Chinese Academy of Sciences, Beijing. His research interests include artificial intelligence for transportation, intelligent vehicles, and parallel traffic management and control systems.
![](https://cdn.mathpix.com/cropped/61b1c59c-aa97-4c6c-a31f-ab552ed86c73-16.jpg?height=318&width=254&top_left_y=1280&top_left_x=1083)

Mengxin Wang received the B.E. degree in 2022. She is currently pursuing the master's degree with the School of Vehicle Engineering, Chongqing University of Technology. Her main research interests include intelligent networked vehicles and pedestrian behavior studies.

