# Defining Time-to-Collision Thresholds by the Type of Lead Vehicle in Non-Lane-Based Traffic Environments 

Sanhita Das ${ }^{\text {® }}$ and Akhilesh Kumar Maurya


#### Abstract

While anecdotal evidence suggests the consideration of a constant time-to-collision (TTC) threshold in advanced driver assistance systems, yet the prospect of the warning criterion acting as a catalyst for the evaluation of conflict severities in non-lane based traffic environments needs further assessment. The current study attempts to provide a copula-based framework to capture the potential dependence between TTC and centerline separation between the interacting vehicles in staggered-following events according to lead vehicle type. Detailed trajectory data extracted from the video footage of urban roads were used for the purpose of this study. Considering negative association between the considered variables and checked by the performance measures, the bivariate Frank copula model is found acceptable to model the bivariate dependency structure between TTC and CS. In particular, the results of the study corroborate a pragmatic decreasing relationship of TTC with increasing CS and decrease in lead vehicle size- a finding which indicates that the risk level of riders in staggered-following scenario varies by the type of front vehicle ahead and the lateral positioning of the vehicles. Based on the results presented in this paper, our recommendation is to use different minimum TTC thresholds for different centerline separations and leader-follower pairs to suitably evaluate traffic safety in such non-lane based traffic environments.


Index Terms-Time-to-collision, centerline separation, mixed traffic, adaptive cruise control.

## I. Introduction

AS WITH automated driving, collision warning, collision avoidance, assisted lane-change, adaptive cruise control (ACC), automated parking assistance and advanced vehicle-to-vehicle communication, advanced driver assistance system (ADAS) has been a burgeoning topic within safety research since decades [1]-[8]. ADAS is designed to assist drivers during the primary driving task with an aim to improve safety, reduce the risks of accidents, increase capacity, benefit to traffic oscillations and enhance overall comfort level of riders. The ADAS 'inform and warn the driver, provide feedback on driver actions, increase comfort and reduce the workload by actively stabilizing or maneuvering the car' [9]. The most prominent example of ADAS is the ACC system that became available in Japan, Europe and USA [10], mainly on high-end vehicles and even in the near future, it is supposed to be accessible on lower grade vehicles as well [11].

[^0]An ACC system aims toward partial automation of the vehicle's longitudinal control and the alleviation of driver's workload in a more efficient manner [12], that can not only modulate the desired speed but also maintain a safe headway to a preceding vehicle conforming to the settings predefined by the users. The steering wheel buttons or lever switches allow drivers to select an automation level mode by setting the desired speed and headway in ACC-equipped systems. In response to the settings imposed by the user, when a vehicle is detected in its trajectory ahead, the system automatically controls the speed to keep safe distance with the vehicle in-front.

In particular, an ACC integrated with collision warning/collision avoidance systems can significantly reduce the severity of rear-end collisions by alerting drivers of upcoming potential threats and imminent collisions. In extreme events, whenever the driver fails to react and a collision is assessed to be unavoidable, the system performs an autonomous action in an appropriate manner. As a matter of fact, a consistent theme emerging from the peer-reviewed literature on the design of driver assistance systems is the selection of an appropriate warning threshold to essentially distinguish between safe and unsafe encounters.

Recent literature has systematically underlined temporal surrogate safety measure as an appropriate indicator for evaluating rear-end collision risks since they amalgamate both spatial proximity and speed. On one hand, surrogate events evince the potential crash causality and the intrinsic mechanism with evident probabilistic theories; while on the other hand, these measures are contemplated as a proactive approach, which assess safety before crashes actually eventuate. Amongst all the temporal safety indicators, time-to-collision (TTC) has been widely considered as a potential parameter in defining warning threshold of an ACC/collision avoidance system [8], [13], [14] and in different traffic situations as well [15]-[19] due to its simplicity and reliability.

Hydén [20] defined time-to-collision as 'the time that remains until a collision between two vehicles would have occurred if the collision course and speed difference are maintained'. A minimum TTC value ( $\mathrm{TTC}_{\text {min }}$ ) is often used as an indicator to estimate the criticality of an encounter. In essence, lower the $\mathrm{TTC}_{\text {min }}$ threshold, higher will be the severity of a collision. So far, research on TTC in traffic safety evaluation has been mainly confined to lane-based traffic scenario and has focused on defining different $\mathrm{TTC}_{\text {min }}$ thresholds in order to discriminate critical from normal behavior
in car-following processes [21], distinguish between safe and unsafe vehicle encounters [22], [23], provide an early collision avoidance warning indication to the drivers when TTC exceeds a recommended/defined threshold [8], [24] and also to characterize low, moderate and high risks of collisions [25]. In a recently published research conducted on the US 101 freeway, Zhao and Lee [26] found that the mean TTC values of different vehicle pair combinations (a car following a car, a car following a heavy vehicle and a heavy vehicle following a car) vary by the type of leading and following vehicles.

Although a plethora of literature is available on the development of TTC for lane based homogeneous traffic, there is still a paucity of research concerning the applicability of the safety indicator to non-lane based heterogeneous traffic environments. In essence, vehicles in non-lane based traffic scenario have varying static and operational characteristics due to which they seldom follow strict lane-discipline and have the flexibility to occupy any available lateral space on the road irrespective of lane markings. Therefore, with regard to non-lane based traffic scenario, while TTC can be regarded as a longitudinal descriptor of traffic, the lateral interaction can be well-described by a commonly-used indicator, namely centerline separation [28] which is defined as the lateral separation between the centerlines of two interacting vehicles in car-following processes. Understanding that the utilization of TTC indicator in weak-lane discipline traffic requires an integration of the longitudinal as well as the lateral descriptor, the $\mathrm{TTC}_{\text {min }}$ thresholds recommended in the literature may not represent the actual scenario in non-lane based traffic environments as these minimum thresholds are envisaged to vary across different lateral positions of vehicles and according to the type of interacting vehicle pair as well.

Based on these premises, this paper aims to provide a framework that will facilitate the application of temporal proximity measure for safety evaluation in vehicle-following events of non-lane based traffic environments for different leading vehicle types. More specifically, the interactions of car drivers with the leading motorized two-wheelers (2Ws), motorized three-wheelers (3Ws), cars and trucks are only considered in this study.

The contribution of this paper is threefold. First, the dependence structure of TTC with the lateral descriptor of traffic flow is analyzed according to the lead vehicle type, which will provide a wider perspective in understanding the rear-end collision risks in non-lane based traffic environments. Second, a methodological approach using copulas is employed in this research to evaluate the joint dependence behavior of timeto-collision with CS in an attempt to suitably ameliorate the detailed characterization of TTC thresholds with CS as well as with the type of leading vehicle. Finally, an assessment of the research implications, highlighting the importance of considering different safety thresholds for non-lane based traffic environments complete the paper.

## II. Temporal Surrogate Safety Measure

In order to assess rear-end collision risks, many effective temporal proximity indexes were proposed, one of which was time-to-collision that has now been widely accepted as a beneficial and valid safety indicator for traffic conflicts [15], [29]. The TTC indicator can be used to estimate the collision risk between two individual vehicles on the scale of seconds [8].

The TTC notion denotes the time taken by the front end of the following vehicle to reach the rear end of the leading vehicle if both the vehicles proceed at their present speeds and on the same path, which can be determined as:

$$
\operatorname{TTC}_{\mathrm{i}}(\mathrm{t})= \begin{cases}\frac{x_{i-1}(t)-x_{i}(t)-l_{i-1}}{v_{i}(t)-v_{i-1}(t)}, & \text { if } v_{i}(t)>v_{i-1}(t) \\ \infty, & \text { if } v_{i}(t) \leq v_{i-1}(t)\end{cases}
$$

where $\mathrm{TTC}_{\mathrm{i}}(\mathrm{t})$ denotes the TTC value of the following vehicle $i$ at a time instant $t, x$ and $v$ denote the positions and velocities of the vehicles respectively, and $l_{i-1}$ representing the length of the leading vehicle. The smaller TTC value indicates the higher risk of collision at a certain time instant.

To evaluate the risks associated with the vehicle-following processes, a threshold of time-to-collision should be determined which can discern unsafe vehicle-following events from the safe ones. Defining a standard TTC threshold has emerged as a contentious issue for evaluating collision risks. A synthesis of previous work demonstrated different thresholds within the range of 0.90-5s, which have been propounded for varying traffic and driving scenarios. Maretzke and Jacob [30] proposed a critical cut-off value of 5s for urban areas, while other researchers suggested a TTC-criterion of 4s for activating a collision avoidance system [13], [22] and for ascertaining the crash risk of a vehicle. Hirst and Graham [22] and Brown et al. [27] reported a TTC threshold of 3s for developing rear-end collision avoidance systems. Hirst and Graham [22] indicated that a 4 or 5s TTC warning criterion resulted in too false alarms while a 3s criterion produced the least number of alarms even in some critical situations. In a later paper, Bella and Russo [24] suggested the TTC thresholds of 2.5s and 3s to distinguish unsafe car-following maneuvers. Besides, other researchers also recommended a critical threshold of 3s [16], [18], [19], [31]. A previous study conducted by Hogema and Janssen [32] at the approach of a queue found the minimum values as 3.5s and 2.6s for non-supported and supported drivers respectively, where 2.6s TTC value was regarded as a safety concern. Several researchers have documented even lower critical values of TTC: 1s TTC threshold being considered as the critical conflict severity [23]; a TTC of 1.5 s is considered as desirable [23] while other studies suggested that encounters with TTC lower than 1.5s are critical [13], [23], [25].

A concoction of the peer-reviewed literature appears that the conflicts and the levels of severity depend to a large extent on the threshold value, where no definite clear-cut standard value has been established to distinguish conflicts and normal events. As indicated in the peer-reviewed literature, a TTC criterion of 3s has been recommended for developing rear-end collision avoidance systems [22], [27], distinguish unsafe car-following maneuvers [24] and for identifying the exposure to traffic conflicts [16], [18], [19], [31]. In accordance with the TTC values suggested by several researchers, a threshold of 3s is hence employed in this research work to investigate the joint

![](https://cdn.mathpix.com/cropped/8123e0ae-b28e-4c14-a218-d71ffd659d64-03.jpg?height=432&width=602&top_left_y=198&top_left_x=305)
Fig. 1. Prospect of rear-end collision occurrence in lane-based and non-lane based traffic environments at a time $t$.

crash-risk probabilities of riders in vehicle-following cases of non-lane based traffic environments.

## III. Methodological Framework

For the traffic safety assessment in car-following scenario, previous studies have proposed different methodologies [19], [33], simulated environments [13], [16], [18], [19] and microsimulation software [27] in order to validate the surrogate safety measures. Conversely, similar methodologies may not be suitable to define critical thresholds of surrogate measures in non-lane based traffic environments, where vehicles often evaluate the opportunities to perform a lateral movement while making longitudinal progression, due to the differences in vehicle dimensions, performance capabilities and sporadic driver behavior. Fig. 1 depicts the following scenario of a vehicle $i$ in lane-based and non-lane based traffic environments.

As importantly, vehicles in lane-based traffic can even be observed to follow the leading vehicles with certain lateral separation between the leaders. In a recent research by Gunay [34], vehicles in lane-based driving discipline traffic were observed to maintain a mean distance of 1.78m from the left edge of the lane, with 0.34m standard deviation- a finding which can be contemplated as a threshold criteria for classifying a lane-based and non-lane based car-following events. More specifically, $\mathrm{CS} \leq 0.34 \mathrm{~m}$ can be assumed as a replication of actual car-following events while $0.34 \mathrm{~m}<\mathrm{CS}<3 \mathrm{~m}$ can be considered as a typical staggered-following scenario of nonlane based traffic environments.

With regard to non-lane based traffic, recent literature has underlined the ability of copula models to accommodate the dependence structure of longitudinal and lateral descriptors of traffic flow (centerline separation) in vehicle-following cases [35], [36]. With an aim to ameliorate the realistic characterization of TTC thresholds in non-lane based traffic environments, a methodological approach using copulas is employed in this research in which the following steps were followed:

1) Analysis of surrogate safety measure, TTC and CS between vehicles in vehicle-following scenario.
2) Determination of dependence structure between TTC and CS
3) Models of probabilistic properties of TTC and CS for each lag-lead vehicle pair.
4) Selection of suitable bivariate copula models based on goodness-of-fit criteria.

A. Analysis of Surrogate Safety Measure TTC and CS Between Vehicles in Vehicle-Following Scenario

The first step entails investigation of the randomness or probabilistic properties of TTC and CS (for example: mean, median, standard deviation, skewness and kurtosis) that assist the selection of appropriate univariate marginal models. This analysis is very useful in understanding the behavioral differences and the rear-end collision risks associated with the riders according to lead vehicle type.

## B. Determination of Dependence Structure Between TTC and CS

To suitably explicate the dependence relationship between the random variables, two non-parametric rank-based dependence measures namely Kendall's $\tau$ and Spearman's $\rho_{S}$ are widely used in the copula literature. These measures utilize the concept of concordant and discordant pairs of observations. Because rank correlation measures are considered to be invariant with non-linear monotonic increasing transformations of the marginals and are easier to calculate for multivariate distributions possessing a simple closed-form copula [37], Kendall's $\tau$ and Spearman's $\rho_{S}$ dependence measures are considered in this study. Furthermore, to provide useful information regarding the association between TTC and CS, the chi-plot is evaluated, which is a rank-based graphical representation of dependence in which $n$ pairs of $\left(X_{i}, Y_{i}\right)$ are transformed into $n$ pairs of $\left(\lambda_{n i}, \chi_{n i}\right)$. Specifically, for a given pair $\left(X_{i}, Y_{i}\right)$, let

$$
\begin{aligned}
H_{n i} & =\frac{1}{n-1} \sum_{j \neq i} I\left\{X_{j} \leq X_{i}, Y_{j} \leq Y_{i}\right\} \\
F_{n i} & =\frac{1}{n-1} \sum_{j \neq i} I\left\{X_{j} \leq X_{i}\right\} \text { and }, \\
G_{n i} & =\frac{1}{n-1} \sum_{j \neq i} I\left\{Y_{j} \leq Y_{i}\right\}
\end{aligned}
$$

where $I\{A\}=0,1$ according as the condition is false or true. According to Fisher and Switzer [38], the chi-plot is a scatter plot of the pairs $\left(\lambda_{i}, \chi_{i}\right)$ where

$$
\begin{aligned}
\chi_{n i} & =\frac{H_{i}-F_{i} G_{i}}{\sqrt{F_{i}\left(1-F_{i}\right) G_{i}\left(1-G_{i}\right)}} \\
\lambda_{n i} & =4 \operatorname{sign}\left(F_{i}-0.5\right)\left(G_{i}-0.5\right) \max \left\{\left(F_{i}-0.5\right)^{2},\left(G_{i}-0.5\right)^{2}\right\}
\end{aligned}
$$

Fischer and Switzer [38], [39] argue that $\lambda_{n i}, \chi_{n i} \in[-1,1]$ where $\lambda_{n i}$ measures the distance of the pair ( $X_{i}, Y_{i}$ ) from the bivariate median, with 'control limits' be drawn at $\pm c_{p} / \sqrt{n}$. The pairs of observations from independent and continuous margins are expected to fall within the horizontal confidence bands. For negatively correlated margins, the pairs tend to be located below the lower confidence band.
C. Models of Probabilistic Properties of TTC and CS for Each Lag-Lead Vehicle Pair

The estimation of a copula model requires optimal selection of marginal probability distribution functions. In this sudy, five univariate probability distributions namely Burr, log-logistic, Weibull, Generalised Extreme Value [39] and lognormal were assumed to describe time-to-collision data whereas for the CS data, five mathematical models- lognormal, logistic, Weibull [35], gamma and normal- were considered.

The maximum likelihood method was used to estimate parameters of the univariate models while the validity of each distribution was evaluated based on log-likelihood and the Akaike Information Criteria (AIC) [43], which is defined as:

$$
A I C=2 K-2 \ln (\hat{\theta})
$$

where $\ln (\hat{\theta})$ is the logarithm of the log-likelihood function for a vector of parameters $\hat{\theta}$ of the density function, and $K$ is the number of estimated parameters. The combined criteria of the largest log-likelihood and minimum AIC value is considered for the selection of the optimal model.

Furthermore, three goodness-of-fit statistical tests, namely Kolmogorov-Smirnov (K-S) test, Cramer-von Mises (CvM) and Anderson-Darling (A-D) test are employed in this study to assess the suitability of each marginal distribution function. The K-S test is a non-parametric goodness-of-fit test that does not depend on the hypothesized distribution. It measures the largest deviation of the observed cumulative distribution from a hypothesized cumulative distribution function. Similar to K-S test, the CvM test is also a distribution free test and for certain deviations, it can be more powerful than K-S test. In particular, the CvM test is considered as an alternative to K-S test. This test measures the squared deviations of empirical and hypothesized distributions and it involves integration over the whole spectrum of data. The A-D test, on the contrary, is a modification of CvM test and it emphasizes more on the tails of the distribution than CvM does. Unlike K-S and CvM test, the A-D test is more sensitive to a specific hypothesized distribution. The best-fitted probabilistic distribution function was selected as the one for which the K-S, CvM and A-D test statistics and AIC criterion were minimal, failing to reject the null hypothesis at a nominal significance level of 5\% $(\alpha=0.05)$.

## D. Selection of Suitable Bivariate Copula Based on Goodness-of-Fit Measures

Modeling the bivariate relationship of the considered 2D variables (TTC, CS) requires prudent assessment of appropriate copula models. A set of bivariate copulas with different dependence domain is presented in Das and Maurya's [35] work. Considering the negative degree of association between the 2D variables (TTC and CS), four copula functions namely Gaussian, Farlie-Gumbel-Morgenstern (FGM), Frank and AliMikhail-Haq (AHM), rendering a wide range of negative pairwise dependence were considered in this study.

The inversion of Kendall's tau method was used to estimate parameters of each copula model. In particular, for every parametric copula family, there exists a one-to-one correspondence between Kendall's $\tau$ and copula parameter and solving the functional relationship between $\tau$ and copula parameter provides an estimate of the parameter. Although inversion of Spearman's rho is another alternative, literature has underlined the better performance of Kendall's $\tau$ than Spearman's $\rho_{S}$ [42]. Considering the popularity of inversion of Kendall's tau, mainly because of its explicit form and ease in computing parameters, this approach is used in the current paper for parameter estimation of copulas. Similar to the selection criteria described in subsection III.C, the best fitted copula model is identified based on large log-likelihood and minimum AIC values.

## IV. Study Area and Description of Dataset

Data collection in this research work was conducted by video-recording technique from five different cities of India (Kolkata, Mumbai, Pune, Guwahati and Bengaluru). Videos of the traffic stream were recorded from the top by placing the cameras at a high vantage point (high rise buildings). A total of nine unidirectional sections: three 2-lane, five 3-lane and one 5-lane sections were considered in the study to capture all behavioral variation (if any) with the width of the road. Recordings were collected for a total duration of 3hours for Kolkata and Bengaluru sections; and 2hour for Mumbai, Pune and Guwahati sections. The road sections considered in the study were straight and far from the upstream (250-300m) and downstream (100-150m) of the signalized intersections. For all the considered sections, the trap length of the sections was approximately 45m. In all the days, weather was clear and the visibility was good.

A semi-automated trajectory extracting approach is utilized in this research to analyze video footage and extract microscopic data and vehicles' positions on the studied sections. In general, semi-automatic detection involves clicking on the identified vehicles manually where the trajectory system recognizes and tracks the position of each vehicle on the screen across multiple frames using frame-by-frame analysis. For each tracking, each vehicle's position on the screen is recorded and the image coordinates of the mouse-clicks are then converted to real-world coordinates. In this paper, the camera calibration equations devised by Fung et al. [43] are employed for conversion of the coordinates which basically relies on obtaining four reference points in the video sequence and their respective coordinates in the real world. These transformed real-world coordinates are then processed further to obtain desired kinematic parameters of the trajectories (such as vehicle speeds, longitudinal gap, centerline separation, etc.) from which the interacting vehicle pair combination is identified. To capture the safety aspects of the drivers at different possible lateral positions of the interacting vehicle-pairs in such non-lane based traffic environments, the vehicle trajectories are extracted at every 1s (corresponding to 25 frames) corresponding to each vehicle-pair observation within the 45m section length. Accordingly, TTC is estimated at every 1s of the interaction period for each car-following event (equation 1).

Though data acquisition through trajectory tracking is a time-consuming process, a concise understanding of the unsafe

TABLE I
Summary Statistics of TTC and CS for Different Combinations of Follower-Leader Pairs
|  | Time-to-Collision (s) |  |  |  | Centerline separation (m) |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Car2W | Car3W | CarCar | CarTruck | Car2W | Car3W | CarCar | CarTruck |
| Mean | 3.44 | 5.27 | 5.62 | 5.91 | 1.17 | 1.19 | 1.02 | 1.13 |
| Median | 2.91 | 3.79 | 4.27 | 4.36 | 1.11 | 1.14 | 0.85 | 1.02 |
| Std. dev | 2.40 | 4.60 | 4.56 | 6.26 | 0.75 | 0.71 | 0.76 | 0.77 |
| Skew ${ }^{\text {a }}$ | 1.55 | 1.16 | 1.12 | 2.09 | 0.48 | 0.20 | 0.69 | 0.40 |
| Kurt ${ }^{\text {b }}$ | 2.18 | 0.62 | 0.61 | 4.72 | -0.52 | -1.05 | -0.46 | -0.83 |
| Sample | 242 | 341 | 2801 | 401 | 242 | 341 | 2801 | 401 |


${ }^{\mathrm{a}}$ Skewness, ${ }^{\mathrm{b}}$ Kurtosis
traffic events (high risk situations corresponding to lower TTC values) between two moving vehicles and a detailed dataset of each vehicle's coordinates can be achieved. This could be fundamental to apprehending and identifying any unsafe events depicting higher crash-risks for the interacting vehicle-pairs.

This research work concentrates on car-following events of non-lane based traffic environments. For the purpose of the analysis, any case of free-following conditions or other events with positive relative speed (leaders are faster) were excluded from analysis. Similar to the methodology used by Das and Maurya [35], the following vehicles with CS lower than 3m and longitudinal gap within 20m distance are assumed to interact with the vehicles in-front. However, considering the compact sizes of 2Ws, the criteria of CS lower than 2.5m was employed to define the interaction between cars and 2Ws.

The overall accuracy of data extraction however depends on precise mouse-clicks of the position of each tracked vehicle as well as the resolution of the video footage. In the current study, an error of 5.03 pixels was obtained due to imprecise mouse clicks on the screen, which thereby resulted in an average error of 6.82cm of the obtained trajectory data.

## V. Results and Discussion

A. Statistical Analysis of TTC and CS According to Lead Vehicle Type

The derived trajectory dataset resulted in 242 cases of car-2W, 341 cases of car-3W, 2801 cases of car-car and 401 cases of car-truck following events which would essentially elucidate the characteristics of the proximal safety indicator in non-lane based traffic conditions. The descriptive statistics of the traffic variables (TTC and CS) including asymmetry, dispersion and peakedness for the processed data are summarized in Table 1.

It is evident from the table that TTCs are specified by a wide spectrum of mean values ranging from 3.44s for car2W to a maximum of 5.91s for car-truck. Because bigger sized vehicles impose physical and psychological effects on the subject vehicle, car drivers usually tend to maintain a longer longitudinal spacing with trucks than 2Ws, hence the TTC values follow a decreasing trend from car-truck, car-car, car-3W to car-2W. Therefore, the results indicate that the risks associated with the car drivers depend to a large extent on the type of lead vehicle ahead.

![](https://cdn.mathpix.com/cropped/8123e0ae-b28e-4c14-a218-d71ffd659d64-05.jpg?height=647&width=872&top_left_y=200&top_left_x=1083)
Note: Upper and lower connecting lines representing mean and median values respectively.

Fig. 2. Plots of time-to-collision and centerline separation for (a) car-2W, (b) car-3W, (c) car-car and (d) car-truck. Note: Upper and lower connecting lines representing mean and median values respectively.

The skewness and kurtosis values of TTC further indicate that the distributions have sharper peaks and heavier tails than that of a normal distribution; while lower positive skewness values of CS imply a more symmetrical distribution for CS data as compared to that of TTCs; minimal deviations in the mean and median values further substantiate this result. Kurtosis on the contrary, characterizes the outliers (or, heavytails) of a distribution. The negative kurtosis values for CS data signify a flat-peaked distribution with lighter tails than that of a normal distribution while positive kurtosis value for TTC data indicate a heavy-tailed distribution with sharper peak.

To provide additional insights into the statistical differences of TTCs according to lead vehicle type, a one-way analysis of variance test is conducted; the results of which indicated significant statistical difference among different vehicle pairs $\left(\mathrm{F}_{(3,3782)}=7.6>F_{\text {critical }}=2.60, \mathrm{p}<0.001\right)$. This finding justifies that the rear-end collision risks associated with car drivers varies by the type of vehicle in front.

Understanding that a precise characterization of the following processes of vehicles in non-lane based traffic environments entails an integration of longitudinal and lateral descriptors of vehicle interactions, the variation of TTCs with CS for different follower-leader pair is further investigated in this section. The variations of TTC for different level of CSs according to lead vehicle type are presented in Fig. 2.

The figure depicts that the mean and median values of timeto-collisions gradually decrease with the increase in CSs for all vehicle pairs. This observed trend is indicative of the fact that TTCs are dependent on the lateral positioning of vehicles in vehicle-following processes of non-lane based traffic streams. Because following vehicles at large CS, encounter a wide visual forward field of view and little encumbrance of the vehicles in-front, they tend to follow the leaders closely maintaining lower longitudinal spacing in staggered-following events and subsequently when they perceive increased risks,

TABLE II
Dependence Between TTC and CS for Different Vehicle Pairs
| Follower-Leader | Kendall's tau, $\tau$ | Spearman's rho, $\rho_{S}$ |
| :--- | :--- | :--- |
| Car-2w | -0.121 | -0.183 |
| Car-3W | -0.227 | -0.333 |
| Car-Car | -0.237 | -0.347 |
| Car-Truck | -0.151 | -0.229 |


they can avoid the criticality of the situation by veering laterally beside the leader. The field of view is however dependent on the clear lateral separation between vehicles and the type of vehicle ahead. Comparing the mean and median values at each CS range, TTC values can be observed to be decreasing with the decrease in the size of lead vehicle. This, indeed justifies the interpretation that the critical values of TTC suggested by different researchers for homogeneous and lane-based traffic cannot be directly applied for non-lane based traffic environments as TTC depends to a large extent on the staggered positions of vehicles and type of lead vehicle in the latter. A small value of TTC represents a high risk situation in car-following events but the same level of risk may not be perceived by riders in staggered-following processes since in the latter, car drivers can maintain even smaller longitudinal gap at large centerline separation, thereby having even lower TTC values.

As identified above, the risk level of riders in staggeredfollowing scenario varies by the type of front vehicle ahead and the lateral positioning of the vehicles. It, therefore, necessitates the need to propose a methodological framework that can address the bivariate relationship of proximal safety indicator with the lateral descriptor which will, in turn, ascertain the propensity of crash risks at any lateral positioning of vehicle in non-lane based traffic streams.

## B. Determination of Dependence Between TTC and CS

The Kendall's $\tau$ and Spearman's $\rho_{S}$ correlation coefficients computed between TTC and CS for different follower-leader vehicle pairs are demonstrated in Table 2.

For all vehicle-pair combinations, the correlation coefficients illustrate significant negative degree of association between time-to-collision and centerline separation. Kendall's tau and Spearman's rho values indicate that the rear-end collision risks show a weaker dependence relationship with CS when cars follow 2Ws than the lead trucks, 3Ws and cars. This difference is mainly attributed to the field of clear view available to the subject vehicle in the staggered-following events. Because of smaller widths and heights of 2Ws, drivers in the following vehicles perceive the forward scenario more clearly which gives them more confidence about the anticipated actions of the lead vehicle. Conversely, for any CS (0-3m) trucks obstruct the forward view of the following cars because of which car drivers maintain lower CS with the trucks, and no prominent dependent relationship was observed. On the other hand, car drivers tend to follow the leading 3Ws and cars (having moderate widths) closely in staggered-following events so as to have a broader front view, hence a moderate

![](https://cdn.mathpix.com/cropped/8123e0ae-b28e-4c14-a218-d71ffd659d64-06.jpg?height=406&width=879&top_left_y=204&top_left_x=1079)
Fig. 3. Chi-plot of TTC and CS for (a) Car-2W (b) Car-3W (c) Car-Car and (d) Car-Truck.

TABLE III
Goodness-of-Fit Test Results for Different Vehicle Pairs
| Variables | FollowerLeader | LogLikelihood | AIC | Goodness-of-fit measures |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  | K-S | CvM | A-D |
| TTC (LN ${ }^{\mathrm{a}}$ ) | Car-2w | -711.32 | 1426.62 | 0.084 | 0.470 | 3.007 |
|  | Car-3W | -1010.74 | 2025.48 | 0.089 | 0.926 | 6.126 |
|  | Car-Car | -1532.34 | 3070.67 | 0.021 | 0.047 | 0.349 |
|  | Car-Truck | -1117.31 | 2238.62 | 0.061 | 0.325 | 2.038 |
| CS ( $\mathrm{WL}^{\mathrm{b}}$ ) | Car-2w | -286.51 | 577.22 | 0.056 | 0.218 | 1.489 |
|  | Car-3W | -435.04 | 874.08 | 0.095 | 0.632 | 4.341 |
|  | Car-Car | -716.30 | 1436.62 | 0.069 | 0.690 | 0.364 |
|  | Car-Truck | -428.64 | 861.28 | 0.079 | 0.651 | 4.414 |


${ }^{\mathrm{a}}$ Lognormal, ${ }^{\mathrm{b}}$ Weibull
dependence relationship is observed for car-3W and car-car. To reveal more explicit information concerning the nature of dependence between TTC and CS, the chi-plots for different vehicle pairs are depicted in Fig. 3.

Dashed lines in the chi-plot correspond to 95\% confidence band and the area inside the band signifies absolutely independent relationship. The pattern of chi-plot in Fig. 3 further manifests apparent negative dependent relationship between TTC and CS for different follower-leader pairs.

## C. Models of Probabilistic Properties of TTC and CS for Each Combination of Vehicle Pair

Five statistical models-Burr, log-logistic, Weibull, Generalized Extreme Value and lognormal- were considered in this study to select the best fitted univariate marginal probability distribution function for TTC whereas for the CS data, lognormal, logistic, Weibull, gamma and normal were considered. The best fitted distribution was selected as the one for which the K-S, CvM and A-D test statistics and AIC criterion were minimal, failing to reject the null hypothesis at a nominal significance level of $5 \%(\alpha=0.05)$. Based on goodness-offit measures, log-likelihood and AIC criterion, lognormal and Weibull distributions were found to provide the best fits for TTC and CS respectively for different vehicle pair combinations. However, the estimated parameters of the lognormal and Weibull distributions were observed to vary according to lead vehicle type. The goodness-of-fit test results for the lognormal and Weibull distributions of TTC and CS data for all followerleader vehicle pairs are presented in Table 3.

TABLE IV
Results of Goodness-of-Fit Tests for Different Vehicle Pairs
| FollowerLeader | Est. param \& GoF* | Gaussian | FGM | AMH | Frank |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Car-2W | $\theta$ | -0.188 | -0.544 | -0.623 | -1.099 |
|  | LL | -996.57 | -993.62 | -993.83 | -992.12 |
|  | AIC | 1995.14 | 1989.24 | 1989.66 | 1986.24 |
| Car-3W | $\theta$ | -0.348 | NA |  | -2.129 |
|  | LL | -1425.58 |  |  | -1422.97 |
|  | AIC | 2853.16 |  |  | 2847.94 |
| Car-Car | $\theta$ | -0.364 | -1.068 | NA | -2.240 |
|  | LL | -2217.78 | -2220.36 |  | -2216.78 |
|  | AIC | 4437.56 | 4442.72 |  | 4435.56 |
| CarTruck | $\theta$ | -0.235 | -0.679 | -0.803 | -1.389 |
|  | LL | -1535.18 | -1535.47 | -1535.64 | -1533.77 |
|  | AIC | 3072.36 | 3072.94 | 3073.28 | 3069.54 |


Note: *Estimated parameter and goodness-of-fit

In all the cases, estimated test statistics of the K-S, CvM and A-D tests were lower than the critical values, rendering the goodness-of-fit hypothesis unable to be rejected at $\alpha=0.05$. Hence, lognormal and Weibull distributions were considered satisfactory for describing TTC and CS data respectively for all vehicle-pair combinations and are therefore employed for bivariate distribution modelling using copula models.

## D. Selection of Suitable Bivariate Copula Functions Based on Goodness-of-Fit Measures

Constructing bivariate relationship of the considered 2D variables (TTC, CS) requires prudent assessment of appropriate copula models. Considering negative association between TTC and CS, four copula functions namely Gaussian, FGM, AMH and frank are considered in this study, and the inversion of Kendall's tau approach is utilized to estimate their corresponding parameters. The log-likelihood and AIC values of each copula along with the estimated parameter are listed in Table 4.

The Frank copula exhibited the largest log-likelihood and the least AIC values for time-to-collision and centerline separation data for all vehicle pairs. Based on the combined goodness-of-fit criteria and performance measures of copula models presented in Table. 4, it is thus adjudged that Frank copula model, with lognormal and Weibull distributions for TTC and CS respectively, should be further investigated to assess the collision risks in non-lane based traffic environments.

## E. Application of Copulas in Evaluating Rear-End Collision Risks

This section is aimed to assess the applicability of the recommended TTC thresholds in staggered-following events of non-lane based traffic environments. Firstly, this section discusses the crash-risk probabilities of riders in vehicle-following scenario according to the lead vehicle type. Secondly, the variations in the minimum TTC thresholds across different centerline separations are investigated for different follower-leader pairs, and finally the prospect of crash-risk severities in staggered-following events is examined.

1) Associated Crash-Risks in Vehicle-Following Events: Existing literature recommends different values of time-tocollision which could essentially distinguish safe and risky encounters, but anecdotal evidence suggests that those studies are mainly confined to lane-based homogeneous traffic streams. This subsection is aimed to attain a detailed understanding of the riders' prospect of having TTCs lower than the minimum recommended thresholds for actual vehicle-following events (that is, for lower CS values).

As discussed in section III, $\mathrm{CS} \leq 0.34 \mathrm{~m}$ can be assumed to replicate actual car-following events of lane-based traffic while $0.34 \mathrm{~m}<\mathrm{CS}<3 \mathrm{~m}$ can be considered as a typical staggered car-following scenario of non-lane based traffic environments. It can, therefore be contemplated that the recommended minimum TTC thresholds suggested by different researchers for lane-based traffic will be applicable to non-lane based traffic environments only for lower values of lateral separations $(\mathrm{CS} \leq 0.34 \mathrm{~m})$. With an aim to apprehend the car drivers' probability of maintaining lower centerline separation $(\leq 0.34 \mathrm{~m})$ with different leaders in non-lane based traffic streams (for a minimum TTC threshold criteria), the conditional nonexceedance probabilities are estimated from the developed copula model using Equation 2.

$$
\mathbb{P}(T T C \leq t t c \mid C S \leq c s)=\frac{C\left(v_{1}, v_{2}\right)}{v_{2}}
$$

where $v_{1}=F_{1}\left(x_{t t c}\right), v_{2}=F_{2}\left(x_{c s}\right)$ represent continuous univariate marginal distributions of TTC and CS; ttc and cs represent time-to-collision and centerline separation respectively, and $C$ is the bivariate copula which captures dependence structure between TTC and CS. ttc is considered as 3s in this study. As importantly, the conditional non-exceedance probabilities of riders in actual vehicle-following events $(\mathrm{CS} \leq 0.34 \mathrm{~m})$ are initially estimated from the developed Frank copula model (with TTC < 3s) for each vehicle-pair combination. These conditional probabilities corresponding to CS lower than 0.34m are obtained as 0.3913, 0.2871, 0.1992 and 0.1496 for car2W, car-3W, car-car and car-truck respectively. It clearly implies that at lower CS $(\leq 0.34 \mathrm{~m})$, the probability of car drivers maintaining lower than 3s-TTC threshold increases with decrease in lead vehicle size.
2) Defining TTC Thresholds According to Lead Vehicle Type: With an aim to entail a detailed characterization of time-to-collision thresholds, the conditional probabilities obtained for a 3s TTC threshold of actual vehicle-following events $(\mathrm{CS} \leq 0.34 \mathrm{~m}$, as discussed in section V.E.1) are further extended for different values of centerline separations. From the functional form of Equation 2, given a discrete non-exceedance probability value $P$ and bivariate Frank copula model (with the estimated dependence parameter), the value $t t c$ corresponding to any $c s$ for the corresponding variables TTC and CS can be evaluated by solving the equation. In particular, for explicating the TTC thresholds according to lead vehicle type in staggered-following events (for different CS values), two cases are considered; (a) when a constant threshold of 3s is chosen for all vehicle pairs, and (b) when the same conditional probability of cars is chosen across all vehicle-pairs.

![](https://cdn.mathpix.com/cropped/8123e0ae-b28e-4c14-a218-d71ffd659d64-08.jpg?height=473&width=868&top_left_y=198&top_left_x=168)
Fig. 4. Estimation of minimum TTC thresholds at different CS values considering TTC as 3s for all the follower-leader pairs $(T T C \leq t t c \mid C S \leq c s)$.

For the first case, a constant 3s-TTC threshold depicting an actual car-following scenario (that is, for CS lower than 0.34m) is considered across all lag-lead vehicle pairs. This constant TTC threshold corresponded to different vehiclespecific non-exceedance conditional probabilities (as indicated in section V.E.1). Corresponding to each vehicle-specific conditional probability for 3s-TTC threshold and $\mathrm{CS} \leq 0.34 \mathrm{~m}$, the time-to-collision thresholds are further estimated at different centerline separation values for all vehicle pairs as presented in Fig. 4.

The contour plots signify a decreasing trend in TTCs with the increase in CS, which indeed manifests the driving behavioral pattern of a non-lane based disordered traffic system as discussed in the foregoing sections. However for a particular CS (say 2m), the TTC thresholds are observed to be the highest for car-2W followed by car-truck, car-car and car-3W. But as identified previously, we expect the TTC thresholds to decrease from car-truck, car-car, car-3W to car-2W because car drivers usually tend to maintain larger spacing, thereby higher TTC values with the increase in lead vehicle size which eventually contradicts the obtained results. It is therefore evident that the consideration of a constant TTC threshold across all vehicle-pairs fails to represent the rear-end collision risks and the actual following behavior of car drivers.

In an attempt to suitably elucidate the variations of TTC according to the type of lead vehicle, the conditional probability of TTC $\leq 3 \mathrm{~s}$ for car-car pair is assumed to be consistent across all vehicle-pairs. Specifically, as the reported TTC thresholds are recommended for homogeneous traffic (mostly car-car case), the probability of $\mathrm{TTC} \leq 3 \mathrm{~s}$ for car-car interaction in non-lane based traffic environments is assumed to be constant irrespective of the lead vehicle type and the corresponding probability value is used to define the minimum TTC thresholds. Fig. 5 represents the contour plots of minimum TTC thresholds across centerline separations according to the lead vehicle type considering equal probability as that of car-car.

Considering 19.92\% non-exceedance conditional probability value as constant across all vehicle pairs, the contour plots clearly demonstrate that at CS lower than 0.34 m , time-tocollision values lie within a maximum threshold of 1.58-3.77s, the minimum and maximum values being observed for car-2W $(\mathrm{TTC}=1.58 \mathrm{~s})$ and car-truck $(\mathrm{TTC}=3.77 \mathrm{~s})$ respectively.

![](https://cdn.mathpix.com/cropped/8123e0ae-b28e-4c14-a218-d71ffd659d64-08.jpg?height=503&width=862&top_left_y=196&top_left_x=1085)
Fig. 5. Estimation of minimum TTC thresholds at different CS values considering same probability $(\mathrm{P}=0.1992)$ for all the follower-leader pairs $(T T C \leq t t c \mid C S \leq c s)$.

The threshold range is further observed to follow a gradual decreasing pattern with the increase in CS, the minimum being obtained as $1.05-2.57 \mathrm{~s}$ at $\mathrm{CS}=3 \mathrm{~m}$. As expected, the observed trend is indicative of the fact that TTCs decrease with increasing CS and decrease in size of the lead vehicle. However, the severity of crash-risks evaluated for lane-based traffic appears to be somewhat different for non-lane based traffic environments. For instance, the rear-end collision risk (TTC <3s) [22], [27] for car-following case may not represent the same level of risks in staggered-following case for carcar and even for other vehicle pairs. It can be envisaged from the figure that the rear-end collision risks associated with car drivers in actual car-following events $(\mathrm{CS} \leq 0.34 \mathrm{~m})$ are reflected by the same proportion of car-drivers when they follow trucks at a CS of 1.25m. This observation further justifies that the 3s-TTC threshold does not remain consistent with CS as well as with the type of lead vehicle.
3) Safety Enhancement With Aid of variable TTC-Thresholds: As identified in the peer-reviewed literature, the 3s-TTC threshold is often used as a warning criterion in collision avoidance systems [22], [27], [43] and is considered as adequate for distinguishing dangerous encounters from safe ones [22]. Up to now, the research conducted did not yield concordant results regarding the assumption of a constant warning TTC-strategy in non-lane based traffic environments. Contrary to previous studies, the current research however shows strong evidence that the rear-end collision risks vary with the lateral deviations between the interacting vehicles and the type of vehicle ahead.

Compared to the TTC thresholds obtained in actual vehiclefollowing events (that is, TTC values corresponding to CS $=0.34$ from Fig. 5), the results in Table 5 demonstrate that for each vehicle pair, the percentage reduction in TTC thresholds at different staggered positions of vehicles increase drastically with the increase in CS. This result is reasonable because at large CS, riders in non-lane based traffic usually have a wide visual field and can anticipate the behavior of vehicles in-front with more confidence, therefore they tend to follow the leaders closely maintaining lower longitudinal gaps, thereby resulting in lower TTC values and higher percentage reduction in TTCs.

TABLE V
Percentage Decrease in TTC Thresholds With Respect to the Obtained Minimum TTC Values
| FollowerLeader | TTC (s) at $\mathrm{CS}=0.34 \mathrm{~m}$ |  | Percentage reduction in TTC at different values of CS |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 0.5 m | 1 m | 1.5 m | 2 m | 2.5 m | 3m |
| Car-2w | 1.58 | 3.16 | 12.66 | 19.62 | 24.05 | 31.01 | 33.54 |
| Car-3W | 2.12 | 6.13 | 23.58 | 36.79 | 41.98 | 44.81 | 45.75 |
| Car-Car | 3.00 | 7.67 | 25.97 | 36 | 41.33 | 44 | 45.33 |
| Car-Truck | 3.77 | 4.51 | 16.18 | 23.87 | 28.38 | 30.77 | 31.83 |


This outcome reveals that different TTC control threshold values should be considered in the ACC/CA system to reduce false warnings and enhance safety in staggered-following scenario. Based on the TTC values, CA systems can recognize the severity of an upcoming hazard and provide real-time collision warning information to the drivers. Eventually, consideration of a constant TTC threshold across all CSs may generate frequent false alarms because TTC thresholds are usually expected to decrease with the increase in lateral deviation between vehicles. A system with a high false alarm rate can potentially annoy or distract the driver from real hazards and has often been proved to be a source of risk and irritation caused to the drivers [44]. As highlighted by Baber [45], false alarms often cause driver distractions, thereby diverting the operators away from the primary driving task. Although ACC/CA systems are already in market since 1960s, the algorithms used in developing ACC/CA systems should consider lateral descriptor of traffic in addition to longitudinal dynamics to reduce high false alarm rates and enhance safety in vehiclefollowing events of such non-lane based environments.

But, there are some aspects which still requires elaboration. Based on this research work, the findings provide evidence of the variation in TTC thresholds according to the lead vehicle type. Interestingly, the percentage decrement in TTC thresholds for car-2W and car-3W with respect to 3s-TTC criteria (defined for cars) are obtained as 47.33\% and 29.33\% respectively while the TTC threshold increases by 25.67\% when cars follow the lead trucks in actual vehicle-following events $(\mathrm{CS} \leq 0.34 \mathrm{~m})$. This corroborates that the rear-end collision risks associated with the car-drivers vary with the type of vehicle ahead. What is more critical is the imminent risk associated with the riders when a constant warning criterion is chosen for cars following the leading trucks. Had a constant 3s-TTC threshold been considered for car-truck case, it would result in dangerous encounters if car drivers failed to avoid the criticality of the upcoming hazard by applying emergency braking. However, since driver assistance systems take over a part of the primary driving task by alleviating drivers' workload in a convenient manner, perfect ACC/CA systems would be required which minimizes drivers' intervention and warns the driver when a crash is imminent. This essentially necessitates the development of warning and intervention systems which can assist and support the drivers in detecting safety hazards or dangerous situations in non-lane based traffic environments.

The results from this study, henceforth, signify that the ACC/CA systems should incorporate different TTC-thresholds corresponding to the interacting lead vehicle type and the lateral deviation between the interacting vehicles, to evaluate and enhance traffic safety, rather than considering a constant $\mathrm{TTC}_{\text {min }}$ threshold across all CSs and lead vehicle types.

## VI. Discussion and Conclusion

Although an ACC integrated with collision avoidance/collision warning system is a widespread driver assistance system, yet, the prospect of the warning criterion acting as a catalyst for the evaluation of conflict severities according to different leading vehicle types has not yet been critically examined. The purpose of this study was therefore to provide a methodological framework for facilitating the application of temporal surrogate safety indicator while taking into account the staggered-following events according to the type of lead vehicle in non-lane based traffic environments, by utilizing detailed trajectory data of urban roads. Understanding that the utilization of TTC indicator in weak-lane discipline traffic requires an integration of the longitudinal as well as the lateral descriptor, the methodology employed in this research incorporated copula approach to suitably elucidate the applications of TTC in non-lane based traffic scenario.

An initial statistical assessment on the time-to-collision values for car drivers following the lead motorized two-wheelers (2W), motorized three-wheelers (3W), cars and trucks revealed that TTCs follow a decreasing trend with increasing CS and decrease in size of the vehicle in-front. In particular, a small value of TTC represents a high risk situation in car-following events but the same level of risk may not be perceived by riders in staggered-following processes since in the latter, car drivers can maintain even smaller longitudinal gap at large centerline separation (CS), thereby having lower TTC values. This, indeed justifies the interpretation that the risk level of riders in staggered-following scenario varies by the type of front vehicle ahead and the lateral positioning of the vehicles.

To suitably elucidate the propensity of crash risks at any lateral positioning of vehicle in non-lane based traffic streams, Frank copula was deemed appropriate to provide satisfactory performance in modelling the 2-dimensional joint distribution for car-2W, car-3W, car-car and car-truck in staggered following events, although with different parameters. In particular, for explicating the TTC thresholds according to lead vehicle type in staggered-following events, the assumption of constant conditional probability across all vehicle pairs appeared to be more clearly delineated than that of a constant TTC threshold value. Eventually, the selection of a constant TTC threshold irrespective of all lead vehicle types contradicted the actual behavioral phenomena while the assumption of constant probability reflected the rear-end collision risks in accordance with the actual observations.

While the rear-end collision risk is defined for TTC lower than 3s [22], [27] for lane based traffic, a comparative analysis with staggered following case for car-car indicated the minimum TTC thresholds as 2.77s, 2.22s, 1.92s, 1.76s, 1.68s and 1.64s for CS of 0.5m, 1m, 1.5m, 2m, 2.5m and 3m respectively. Moreover, congruous with the previous explanations,
a comparative assessment on the TTC thresholds obtained in staggered-following events for CS<0.34m depicted that the percentage decrement in TTC thresholds for car-2W and car3W with respect to a critical value of 3s were 47.33\% and $29.33 \%$ respectively while the TTC threshold increased by $25.67 \%$ when cars follow the lead trucks. This corroborates that the minimum TTC value recommended for lane based traffic (3s) varies for non-lane based traffic systems which indeed, leads to an over-prediction of the conflict-severities in staggered-following events.

Based on the proposed methodology and recommended threshold values, the severity of an encounter in car-following state seems to be completely different for staggered following cases, which entails an exhaustive characterization of minimum TTC thresholds for different lateral positions to evaluate traffic safety in such non-lane based traffic environments. It is worthwhile to mention that the collision avoidance model generally developed for describing only longitudinal vehicle dynamics should incorporate the lateral descriptor of traffic and lead vehicle type as well, to evaluate safety performance in non-lane based traffic environments. This research will therefore, be the new impetus in the target of providing advanced collision warning system adaptation databases in staggered following scenario, which may indeed be useful for conflict severity evaluation in a cognitive architecture.

While the results are promising, the work undertaken in this paper has its limitations. In order to explicate the minimum TTC thresholds for staggered-following events, it is assumed that the probability of riders having lower minimum TTC thresholds (as reported in the literature) for car-following cases will be similar for staggered following cases. The severity of conflicts estimated in the study is also based on recommended minimum thresholds and therefore it cannot be interpreted as an actual outcome of the situation; further investigation needs to be conducted to uphold the assumed proposition. Indeed, by analyzing accidents in terms of TTC thresholds might possibly improve conflict-severity estimation of the safety critical event. Further studies defining minimum TTC thresholds for non-lane based traffic may corroborate the credibility of TTC thresholds defined based on the concept of copula-based models.

## References

[1] M. Börner and R. Isermann, "Model-based detection of critical driving situations with fuzzy logic decision making," Control Eng. Pract., vol. 14, no. 5, pp. 527-536, 2006.
[2] S. E. Shladover, "Longitudinal control of automotive vehicles in closeformation platoons," J. Dyn. Syst., Meas., Control, vol. 113, no. 2, pp. 231-241, 1991.
[3] J. Wang and R. Rajamani, "Should adaptive cruise-control systems be designed to maintain a constant time gap between vehicles?" IEEE Trans. Veh. Technol., vol. 53, no. 5, pp. 1480-1490, Sep. 2004.
[4] S. Moon, I. Moon, and K. Yi, "Design, tuning, and evaluation of a fullrange adaptive cruise control system with collision avoidance," Control Eng. Pract., vol. 17, no. 4, pp. 442-455, 2009.
[5] M. Bueno, C. Fabrigoule, D. Ndiaye, and A. Fort, "Behavioural adaptation and effectiveness of a Forward Collision Warning System depending on a secondary cognitive task," Transp. Res. F, Traffic Psychol. Behav., vol. 24, pp. 158-168, May 2014.
[6] K. Zeeb, A. Buchner, and M. Schrauf, "What determines the take-over time? An integrated model approach of driver take-over after automated driving," Accident Anal. Prevention, vol. 78, pp. 212-221, May 2015.
[7] V. P. Harigovindan, A. V. Babu, and L. Jacob, "Proportional fair resource allocation in vehicle-to-infrastructure networks for drive-thru Internet applications," Comput. Commun., vol. 40, pp. 33-50, Mar. 2014.
[8] Y. Li, Z. Li, H. Wang, W. Wang, and L. Xing, "Evaluating the safety impact of adaptive cruise control in traffic oscillations on freeways," Accident Anal. Prevention, vol. 104, pp. 137-145, Jul. 2017.
[9] Code of Practice for the Design and Evaluation of ADAS. document Deliverable D11.2, Integrated Project PREVENT, 2006.
[10] D. A. Dickie, "The effects of trust on the use of adaptive cruise control," M.S. thesis, department, Ind. Eng., Univ. Iowa, Iowa, USA, 2010.
[11] S. Young, "Ergonomics issues with advanced driver assistance systems (ADAS)," in Automotive Ergonomics Driver-Vehicle Interaction, N. Gkikas ed. Boca Raton, FL, USA: CRC Press, 2012.
[12] Intelligent Transport Systems-Adaptive Cruise Control Systems- Performance Requirements and Test Procedures, document ISO 15622, International Organization for Standardization [ISO], Geneva, Switzerland, 2010.
[13] R. Van der Horst and J. Hogema, "Time-to-collision and collision avoidance systems," in Proc. 6th ICTCT Workshop Saf. Eval. Traffic Syst., Traffic Conflicts Other Measures, Oct. 1993, pp. 109-121.
[14] I.-C. Han, B.-C. Luan, and F.-C. Hsieh, "Development of autonomous emergency braking control system based on road friction," in Proc. IEEE Int. Conf. Automat. Sci. Eng. (CASE), Taipei, Taiwan, Aug. 2014, pp. 933-937.
[15] H. Farah, S. Bekhor, and A. Polus, "Risk evaluation by modeling of passing behavior on two-lane rural highways," Accident Anal. Prevention, vol. 41, no. 4, pp. 887-894, 2009.
[16] X. Qu, Y. Kuang, E. Oh, and S. Jin, "Safety evaluation for expressways: A comparative study for macroscopic and microscopic indicators," Traffic Injury Prevention, vol. 15, no. 1, pp. 89-93, 2014.
[17] X. Qu, Y. Yang, Z. Liu, S. Jin, and J. Weng, "Potential crash risks of expressway on-ramps and off-ramps: A case study in Beijing, China," Saf. Sci., vol. 70, pp. 58-62, Dec. 2014.
[18] Q. Meng and X. Qu, "Estimation of rear-end vehicle crash frequencies in urban road tunnels," Accident Anal. Prevention, vol. 48, pp. 254-263, Sep. 2012.
[19] S. Jin, X. Qu, and D. Wang, "Assessment of expressway traffic safety using Gaussian mixture model based on time to collision," Int. J. Comput. Intell. Syst., vol. 4, no. 6, pp. 1122-1130, 2011.
[20] C. Hydén, "Traffic conflicts technique: State-of-the-art," in Traffic Safety Work With Video Processing, H. H. Topp, Ed. Kaiserslautern, Germany: Univ. of Kaiserslautern, 1996, pp. 3-14.
[21] H., Behbahani, N. Nadimi, and S. S. Naseralavi, "New time-based surrogate safety measure to assess crash risk in car-following scenarios," Transp. Lett., vol. 7, no. 4, pp. 229-238, 2015.
[22] S. Hirst and R. Graham, "The format and perception of collision warnings," in Ergonomics and Safety of Intelligent Driver Interfaces, Y.I. Noy, Ed. Mahwah, NJ, USA: Lawrence Erlbaum Associates, 1997, pp. 203-219.
[23] A. R. A. Van der Horst, "A time-based analysis of road user behaviour in normal and critical encounters," Ph.D. dissertation, Dept. Elect. Eng., Delft Univ. Technol., Delft, The Netherlands, 1990.
[24] F. Bella and R. Russo, "A collision warning system for rear-end collision: A driving simulator study," Procedia-Social Behav. Sci., vol. 20, pp. 676-686, Jan. 2011.
[25] T. Sayed, G. Brown, and F. Navin, "Simulation of traffic conflicts at unsignalized intersections with TSC-Sim," Accident Anal. Prevention, vol. 26, no. 5, pp. 593-607, 1994.
[26] P. Zhao and C. Lee, "Analysis and validation of surrogate safety measures by types of lead and following vehicles," Transp. Res. Rec., vol. 2659, no. 1, pp. 137-147, 2017.
[27] T. L. Brown, J. D. Lee, and D. V. McGehee, "Human performance models and rear-end collision avoidance algorithms," Hum. Factors, vol. 43, no. 3, pp. 462-482, 2001.
[28] B. Gunay, "Car following theory with lateral discomfort," Transp. Res. B, Methodol., vol. 41, no. 7, pp. 722-735, Aug. 2007.
[29] K. Vogel, "A comparison of headway and time to collision as safety indicators," Accident Anal. Prevention, vol. 35, no. 3, pp. 427-433, May 2003.
[30] Maretzke, and U. Jacob, "Distance warning and control as a means of increasing road safety and ease of operation,"in Proc. 24th Fisita Congr., Inst. Mech. Eng., London, U.K., Jun. 1992, pp. 105-114.
[31] M. M. Minderhoud and P. H. Bovy, "Extended time-to-collision measures for road traffic safety assessment," Accident Anal. Prevention, vol. 33, no. 1, pp. 89-97, Jan. 2001.

[32] H. Hogema and W. H. Janssen, Effects of Intelligent Cruise Control on Driving Behaviour. Soesterberg, Netherlands: TNO Human Factors Research Institute, 1996, p. C012.
[33] S. Jin, D.-H. Wang, C. Xu, and D.-F. Ma, "Short-term traffic safety forecasting using Gaussian mixture model and Kalman filter," J. Zhejiang Univ. Sci. A, vol. 14, no. 4, pp. 231-243, 2013.
[34] B. Gunay, "Methods to quantify the discipline of lane-based-driving," Traffic Eng. Control, vol. 44, no. 1, pp. 22-27, 2003.
[35] S. Das and A. K. Maurya, "Multivariate analysis of microscopic traffic variables using copulas in staggered car-following conditions," Transportmetrica A, Transp. Sci., vol. 14, no. 10, pp. 829-854, 2018.
[36] S. Das, A. K. Maurya, and A. K. Budhkar, "Determinants of time headway in staggered car-following conditions," Transp. Lett., vol. 11, no. 8, pp. 447-457, 2019.
[37] P. Embrechts, A. Höing, and A. Juri, "Using copulae to bound the valueat-risk for functions of dependent risks," Finance Stochastics, vol. 7, no. 2, pp. 145-167, 2003.
[38] N. I. Fisher, and P. Switzer, "Chi-plots for assessing dependence," Biometrika, vol. 72, no. 2, pp. 253-265, 1985.
[39] N. I. Fisher and P. Switzer, "Graphical assessment of dependence: Is a picture worth 100 tests?" Amer. Statistician, vol. 55, no. 3, pp. 233-239, 2001.
[40] R. Chen, "Driver behavior in car following-the implications for forward collision avoidance," Ph.D. dissertation, Dept. Biomed. Eng., Virginia Technol., Richmond, VA, USA, 2016.
[41] H. Akaike, "A new look at the statistical model identification," IEEE Trans. Autom. Control, vol. 19, no. 6, pp. 716-723, Dec. 1974.
[42] I. Kojadinovic and J. Yan, "Comparison of three semiparametric methods for estimating dependence parameters in copula models," Insurance: Math. Econ., vol. 47, no. 1, pp. 52-63, 2010.
[43] G. S. Fung, N. H. Yung, and G. K. Pang, "Camera calibration from road lane markings," Opt. Eng., vol. 42, no. 10, pp. 2967-2977.
[44] M. N. Lees and J. D. Lee, "The influence of distraction and driving context on driver response to imperfect collision warning systems," Ergonomics, vol. 50, no. 8, pp. 1264-1286, 2007.
[45] C. Baber, "Psychological aspects of conventional in-car warning devices," in Human Factors in Alarm Design, N. Stanton, ed. London, U.K.: Taylor \& Francis, 1994.

![](https://cdn.mathpix.com/cropped/8123e0ae-b28e-4c14-a218-d71ffd659d64-11.jpg?height=318&width=251&top_left_y=217&top_left_x=1083)

Sanhita Das received the M.Tech. degree in transportation engineering from the Indian Institute of Technology Guwahati, India, where she is currently pursuing the Ph.D. degree in traffic operations and safety. Her research interests include traffic flow modeling, safety evaluation, and intelligent transportation systems and its applications.
![](https://cdn.mathpix.com/cropped/8123e0ae-b28e-4c14-a218-d71ffd659d64-11.jpg?height=314&width=249&top_left_y=1070&top_left_x=1083)

Akhilesh Kumar Maurya received the Ph.D. degree from the Indian Institute of Technology Kanpur, India. He is currently an Associate Professor with the Department of Civil Engineering, Indian Institute of Technology Guwahati, India. His main research areas include traffic flow theory and modeling, driver behavior modeling, traffic data collection and analysis, road safety and accident analyses, and vehicle emission modeling.


[^0]:    Manuscript received July 25, 2018; revised July 17, 2019 and September 17, 2019; accepted October 2, 2019. The Associate Editor for this article was A. Amditis. (Corresponding author: Sanhita Das.)
    The authors are with the Indian Institute of Technology Guwahati, Guwahati 781039, India (e-mail: sanhi.das25@gmail.com; akmaurya@gmail.com).
    Digital Object Identifier 10.1109/TITS.2019.2946001

