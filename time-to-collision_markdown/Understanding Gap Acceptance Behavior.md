Yingfeng (Eric) Li ${ }^{\mathbf{1}}$, Haiyan Hao ${ }^{\mathbf{1}}$, Ronald B. Gibbons ${ }^{\mathbf{1}}$, and Alejandra Medina ${ }^{\mathbf{1}}$


#### Abstract

Even though drivers disregarding a stop sign is widely considered a major contributing factor for crashes at unsignalized intersections, an equally important problem that leads to severe crashes at such locations is misjudgment of gaps. This paper presents the results of an effort to fully understand gap acceptance behavior at unsignalized intersections using SHPR2 Naturalistic Driving Study data. The paper focuses on the findings of two research activities: the identification of critical gaps for common traffic/roadway scenarios at unsignalized intersections, and the investigation of significant factors affecting driver gap acceptance behaviors at such intersections. The study used multiple statistical and machine learning methods, allowing a comprehensive understanding of gap acceptance behavior while demonstrating the advantages of each method. Overall, the study showed an average critical gap of 5.25 s for right-turn and 6.19 s for left-turn movements. Although a variety of factors affected gap acceptance behaviors, gap size, wait time, major-road traffic volume, and how frequently the driver drives annually were examples of the most significant.


Across the nation, unsignalized intersections comprise 90\% of all intersections and are responsible for about 70\% of the fatalities occurring at intersections ( 1,2 ). Even though drivers disregarding a stop sign is widely considered a major contributing factor for crashes at unsignalized intersections, an equally important problem that leads to severe crashes at such locations is misjudgment of gaps.

Gap acceptance at unsignalized intersections has long been an important research topic. When a driver on a minor-road approach arrives at the stop line of an unsignalized intersection, they need to decide when to enter the intersection based on the right of way hierarchy and the availability and distribution of gaps. This decision-making process involves the identification and acceptance of safe gaps. Intersection gap acceptance behaviors are affected by several variables, such as those related to roadway, traffic, driver, vehicle, and the environment. To date, a fair amount of research has been conducted to understand this behavior.

Typically, gap acceptance has been studied using observational data based on videotaping or manual timing at intersections. By using observational data, previous research has tended to study driver gap judgments from an external point of view, with limited consideration of driver factors (e.g., driving history and driver age). Naturalistic driving data, conversely, collects detailed driver information that may help better understand the topic. SHRP2 Naturalistic Driving Study (NDS) data contain detailed driver, trip, and synchronized forwardview, rear-view, and face-view video data for thousands of drivers in a naturalistic driving environment.

This paper presents the partial results of an effort to fully understand gap acceptance behavior at unsignalized intersections using SHPR2 NDS data. The paper focuses on the findings of two research activities: the identification of critical gaps for common traffic/roadway scenarios at unsignalized intersections, and the investigation of significant factors affecting driver gap acceptance behaviors at such intersections.

## Literature Review

Critical Gap Determination Methods
Critical gap is an important concept for understanding gap acceptance behaviors at unsignalized intersections

[^0]and for conducting intersection-related operations and safety analyses. Critical gaps refer to the gap size thresholds, larger than which drivers would be likely to acceptunder given roadway/traffic settings. Widely accepted critical gap values for different scenarios are required for an extensive range of engineering applications relevant to intersections, such as capacity analyses, roadway geometric design, and traffic control analyses.

Over the years, the research community has developed several methods for the determination of critical gaps. These methods each have pros and cons and vary in assumptions, level of sophistication, and ease of use. The following briefly summarizes a sample of the critical gap determination methods (3-5):

- Gap acceptance curve. This method plots the percent of accepted gaps against gap values and the critical gap is the gap accepted by a predetermined percentage of drivers (e.g., 50\% or 85\%) (6).
- Greenshield's method. This method is based on a histogram of the frequencies of rejected and accepted gaps. A critical gap is determined as the gap corresponding to an equal number of drivers that accepted and rejected it (7). The method is straightforward to use but is prone to impacts of sample size or gap distribution.
- Ashworth's method. This method fits the critical gap and the accepted gap values into normal distributions and determines the average critical gap as a function of the mean and variance of the accepted gaps (8). The method is considered easy to use and relatively accurate during suitable traffic conditions, but is dependent on the conflicting traffic volume and could be inaccurate for certain traffic and headway patterns.
- Raff's method. This method uses the intersection of the cumulative distribution of accepted gaps and the inverse curve of the cumulative distribution of rejected gaps as the critical gap. The method makes no assumption of data distribution and is straightforward to use. However, it is susceptible to the impacts of gap data composition and a large proportion of long gaps in the data would result in an increased critical gap value (9). The results of Raff's method may be improved by the exclusion of long accepted gaps (10, 11).
- Logit method. This method is also referred to as the logistic regression method, which models the gap acceptance and rejection decisions as a binomial response of gap size (3). The critical gap is determined to be the gap size corresponding to a certain level of acceptance probability (e.g., 50\% or 85\%). This method tends to produce lowercritical gap values, particularly when both gap and lag data are used.
- Maximum likelihood method. This method assumes that the critical gaps for a given driver population follow a lognormal distribution and the mean critical gap is selected as the general critical gap for the population (12). The critical gap is determined with distribution coefficients that maximize the likelihood that the critical gap for an individual will be higher than the highest rejected gap and lower than the actual accepted gap. McGowen and Stanley modified the maximum likelihood method to analyze data with only accepted gaps or rejected gaps (13). The maximum likelihood method can be less reliable when analyzing data from an inhomogeneous population.
- Probability equilibrium. This method was developed to estimate the critical gaps based on cumulative distributions of accepted and rejected gaps (14). The method does not make preassumptions about data distribution, and even though it requires less computation than the maximum likelihood method, in many cases it is able to produce similar results.
- Hewitt's method. This method assumes that the accepted and rejected gaps follow normal distribution, and estimate the average value and variance of critical gaps using the cumulative distribution function of major stream gaps and an iterative process (5). However, the method can yield unreasonably low critical gap values particularly when applied on inhomogeneous traffic conditions.

In addition to the estimation methods, estimated critical gap values are also influenced by the selection and preprocessing of the collected data. Common considerations for researchers processing the collected gap data include,

- Inclusion or exclusion of large gaps. Several studies have indicated that gaps larger than 12 s are generally accepted by all minor-road drivers. Such gaps will not provide meaningful information about gap acceptance behavior and bias the estimation results, thus should be excluded from the analysis (9, 15, 16).
- Use of gaps and lags. A previous study (17) suggested that estimations with only lag information could be less accurate than those utilizing all gaps, possibly owing to the limited information lags represent and potential accuracy issues associated with measuring lags. Another study, conversely, showed that there was no statistically significant difference between using lags and gaps (7).

Table I. Determined Critical Gaps in Previous Studies
| Study site |  | Critical gap |  |
| :--- | :--- | :--- | :--- |
|  |  | Type | Value (s) |
| Illinois, Missouri, and Pennsylvania (23) | 13 stop-controlled intersections, 5 three-leg intersections and 8 four-leg intersections | Passenger car, right turn | 6.3 |
|  |  | Passenger car, left turn | 8 |
|  |  | Single-unit truck, right turn | 8.4 |
|  |  | Single-unit truck, left turn | 9.8 |
|  |  | Combination truck, right turn | 10.7 |
|  |  | Combination truck, left turn | 10 |
| Multistate (24) | 8 stop-controlled T-intersections | Right turn | 5 |
|  |  | Left turn | 4.25 |
| San Francisco (25) | 5 intersections | Not available | 5.6-7.6 |
|  | 60 sites | Right turn | 4.5-24.7 |
|  |  | Left turn | 3.5-14.7 |
| Christinsburg, VA (26) | A four-leg signalized intersection | Left turn, first lane | 6.0-7.2 |
|  |  | Left turn, second lane | 8.1-9.2 |
| Pennsylvania (7) | 6 intersections with different traffic pattern, each has 2 two-lane roads | Passenger car, left turn | 5.00-8.08 |
|  |  | Passenger car, right turn | 4.50-7.49 |
|  |  | Passenger car, through | 6.00-7.80 |
|  |  | 5-axle truck, left turn | 7.25-8.27 |
|  |  | 5-axle truck, right turn | 8.25-12.50 |
|  |  | Less-than-5-axle truck, left turn | 10.25-11.16 |
|  |  | Less-than-5-axle truck, right turn | 6.25-13.17 |


- Use of maximum rejected gaps or all rejected gaps. Tupper (18) compared multiple methods with the variation of using the maximum rejected gaps and all rejected gaps. It was found that use of only maximum rejected gaps gave lower critical gaps for Raff's method, but resulted in higher critical gap values for the probability equilibrium method (9, 14).

Based on the data used, different methods frequently perform differently (17-19). For example, a previous NCHRP study (20) applied both the logit and Raff methods and showed that the results of the Raff method were approximately 0.2 s shorter than those of the logit method.

## Critical Gap Values

The Highway Capacity Manual (HCM) (21) and the American Association of State Highway Transportation Officials (AASHTO) Green Book (22) include critical gaps for several scenarios for roadway design and capacity analysis purposes. In general, HCM suggests a base critical gap between 6.2 and 6.9 s for right turn from minor and between 7.1 and 7.5 s for left turn from minor. The Green Book recommends a 6.5 s base critical gap for right turn from minor and 7.5 s for left turn from minor with an additional 0.5 s for each additional lane on the major road. In addition to the values outlined in the manuals, Table 1 summarizes the critical gap values determined by previous studies based on U.S. data.

## Data Collection and Methodology

## SHRP2 Data Collection

SHRP2 conducted the NDS project between 2010 and 2013 to investigate driver behavior and performance relevant to safety for real-world scenarios (27). With more than 3,500 participating drivers recruited, the study collected naturalistic driving and related data surrounding six sites across the country: Bloomington, IN; Central Pennsylvania; Tampa Bay, FL; Buffalo, NY; Durham, NC; and Seattle, WA.

SHRP2 NDS used the onboard Data Acquisition Systems (DAS) for vehicle kinematic and driver behavior data collection. The DAS consisted of a forward radar, four video cameras (observing driver's face and hand, passenger side, forward and rear roadway), accelerometers, Global Positioning System (GPS) receivers, computer vision lanetracking capability, and data storage equipment (28). The final NDS database contained information on more than 5 million trips and 41,000 events, with additional events and data being added as data processing continued (29). As part of the same effort, the SHRP2 project also developed the Roadway Information Database (RID) with relatively detailed traffic and roadway information for the six participating sites. RID incorporates both data originating at the state transportation agencies and data collected by instrumented vehicles. The linkage between the SHRP2 driving and roadway data provides researchers with an opportunity to effectively identify driving data on particular roadway segments of interest (30).

![](https://cdn.mathpix.com/cropped/89a26f37-9815-4c7e-873c-179cc15d868d-04.jpg?height=1093&width=1750&top_left_y=249&top_left_x=163)
Figure 1. Locations of the studied intersections.

For this study, the research team selected unsignalized intersections at two NDS sites: Seattle, WA and Raleigh, NC. The team initially identified 113 intersections based on RID and using satellite images at Esri ${ }^{\text {® }}$ ArcGIS ${ }^{\text {TM }}$ and Google ${ }^{\text {® }}$ Maps ${ }^{\text {TM }}$. All intersections met the following criteria:

- Unsignalized T-intersections with the minor road being the third leg. The use of T-intersections reduced potential turning movement conflicts at the intersections and therefore allowed the team to better study critical gaps. It also significantly increased the usable data points at each intersection owing to fewer interruptions from throughtraffic on the minor-road crossing the major road.
- Major roads at the intersections are not divided by a median wider than 6 ft . This criterion eliminated two-stage left-turning behaviors using the median area as a protection during turning.
- Intersections are located at least 500 ft away from other nearby intersections. This criterion reduced unnecessary interruptions from traffic turning onto the major road from nearby intersections.
- Major roads at intersections have an average daily traffic (ADT) greater than 10,000. This criterion ensured that the major roads would havesignificant traffic to allow the team to collect sufficient and relatively balanced rejected/accepted gap data.
- The intersections are not in interchange areas. This criterion avoided potential effects from freeway driving behaviors.

The research team requested 1,000 NDS trip segments entering the 113 intersections from the minor approaches from the SHRP2 data team. Unfortunately, several intersections did not have NDS trips. As a result, the research team received 1,000 trips from 64 intersections (Figure 1). Note that all subject vehicles were passenger vehicles as the SHRP2 NDS database only includes passenger vehicle participants.

For each trip, the research team requested the following SHRP2 data for further analysis:

- Time series data, which are detailed vehicle kinematics data collected at 10 Hz frequency coupled with GPS speed and location data collected at 1 Hz frequency.
- Forward-facing, rear-view, and face-view videos providing continuous, candid video recordings of the outside and inside of the subject vehicle during each trip.

![](https://cdn.mathpix.com/cropped/89a26f37-9815-4c7e-873c-179cc15d868d-05.jpg?height=859&width=1512&top_left_y=281&top_left_x=333)
Figure 2. Example front- and rear-view video images.

- Driver demographic and driving history data, which include information about driver age, years of driving, and past violations/crash history for the subject drivers of the trips selected.

## Data Processing

Video Data Collection. The research team collected the following time-related variables to describe the drivers' gap acceptance behavior:

- Queue start time. The timestamp at which the subject vehicle started queuing, waiting to turn on the minor road (i.e., after coming to a stop on the minor approach).
- Intersection arrival time. The timestamp at which the subject driver arrived at the intersection, that is, the time when the subject vehicle stopped at the stop sign or stop line. In cases in which the subject driver did not stop completely, the intersection arrival time was determined as the time when the subject vehicle's front bumper began to cross the stop line/sign.
- Maneuver start time. The timestamp at which the driver finished gap observation and started the turning maneuver. A variety of indicators were used to determine this timestamp accurately, including the time when the subject vehicle's speed increased from zero as seen in the speed profile,the beginning time of a positive peak in the longitudinal acceleration profile, or the beginning of a positive (for right-turn trips) or a negative (for left-turn trips) peak in the lateral acceleration profile. In addition, the subject drivers' facial expressions or hand movements were also considered to determine this information.
- Major-road vehicle arrival time. The timestamp at which a major-road vehicle arrived at the intersection. This variable was used to calculate the gap/ lag size. The researchers recorded the vehicle arrival time according to the forward-facing and rearview videos based on a suitable fixed reference point at the intersection. Figure 2 shows examples of forward-facing and rear-view camera images at a study intersection. In this case, the sign post, the fire hydrant, or the triangular pavement marking would be used as a reference point and the timestamps at the precise points when the vehicles arrive at such reference points would be recorded.
- Wait time. The researchers calculated the wait time for each accepted and rejected gap as the time difference between the major-road vehicle arrival time (for a rejected gap) or maneuver start time (for an accepted gap) and the intersection arrival time or queue start time.

In addition to the aforementioned time-related variables, the researchers also collected the following trip-related

![](https://cdn.mathpix.com/cropped/89a26f37-9815-4c7e-873c-179cc15d868d-06.jpg?height=476&width=1139&top_left_y=280&top_left_x=467)
Figure 3. Probability and cumulative distributions of accepted and rejected gaps.

variables from the trip video files: lighting conditions, driver distraction, the presence of leading vehicles, following vehicles, or both, and weather conditions. Note that the project team deleted all trips involving severe adverse weather conditions that significantly reduced visibility (e.g., rain, snow, or heavy fog). The team however kept several cases with minor weather conditions such as light rain or fog that did not significantly affect the video quality.

Other Data Items. In addition to the video data, the team also collected the following data items:

- Intersection data, including many variables depicting the major- and minor-road geometry, traffic control, speed limit, and average annual daily traffic (AADT) information from a combination of sources including the SHRP 2 RID database, Google Maps, and the satellite images in ArcGIS.
- Driver data, including driver age, driver visual acuity (used as a screening variable), driving history, and crash/violation history.
- Time series data, including average speed, maximum longitudinal and lateral accelerations, and standard deviation of longitudinal and lateral accelerations.

## Summary of Collected Data

Among the original 1,000 trips, the research team was able to collect 270 accepted gaps and 900 rejected gaps, including 466 lags. Figure 3 shows the percentages and cumulative distributions of the accepted and rejected gaps based on a simple frequency analysis. The figure shows, for example, that 15\% of the rejected gaps were approximately 3 s long and the cumulative distribution curves of rejected and accepted gaps intersected at approximately 6 s. Note that several trips were not used during this process for one or more of the following reasons:

- No gap data collected;
- There were conflicting left-turning vehicles from the major roads that potentially affected the gap acceptance behaviors of the subject driver;
- Trips occurred during severe adverse weather conditions; and
- Trip videos could not be processed owing to low quality.

To improve data analysis accuracy, however, the researchers only used data from trips involving accepted gaps with a size between 2.0 and 12.0 s. This further reduced the total number of gaps to 785 including 235 accepted gaps. Among the gaps, 423 were right-turn gaps (132 accepted and 291 rejected) and 362 were left-turn gaps (103 accepted and 259 rejected). In addition, 92 gaps were collected from trips occurring during light rain/foggy conditions.

The data collection effort resulted in 35 variables depicting the roadway and traffic (18 variables), trip (4 variables), driver (4 variables), gap (2 variables), and environment (7 variables). Before the data analyses, the team conducted a preliminary correlation analysis using Pearson's correlation test and deleted/merged some highly correlated variables to reduce the total number of variables and avoid collinearity issues.

## Data Analysis Methodology

This study involved the determination of critical gaps and the development of gap acceptance decision models. The analyses were designed to fully understand the factors affecting driver gap acceptance behaviors and the critical gaps under different traffic/roadway settings. The team selected the following three methods to determine the critical gaps based on SHRP 2 NDS data:

- Maximum likelihood method. As previously stated, the maximum likelihood method considers drivers' gap acceptance behavior to be consistent

but inhomogeneous. Each driver has their own fixed critical gap and will accept all gaps larger than that while rejecting smaller gaps. Critical gaps among the driver population are assumed to follow a lognormal distribution. The critical gap was determined based on accepted and maximum rejected gap sizes for the studied drivers and therefore this method was "driver-based." The optimization process is usually achieved with iterations. Troutbeck previously recommended a spreadsheet approach to simplify the calculation process (31). The current study adopted the spreadsheet approach but improved it by changing the driverbased into a "trip-based" calculation, considering that a driver might have appeared at multiple intersections and behaved very differently under different conditions.
- Binary logistic regression. This models the log probabilities of gap acceptance as a response of gap size (32). During this study, the critical gap was the gap size associated with equal probability of acceptance and rejection by drivers. The researchers used SAS ${ }^{\text {® }}$ to perform this analysis.
- Probability equilibrium method. Compared with the maximum likelihood method, this method does not make assumptions about critical gap distribution. It is not driver-based and uses all collected rejected gaps. When applying this method, the project team arranged all the accepted and rejected gaps in ascending order and then calculated the probability of the critical gap falling between each adjacent pair of gap lengths. The critical gap was estimated as the weighted sum of the observed gap lengths and their associated probabilities (14).

The researchers modeled the drivers' gap acceptance decisions with three statistical and machine learning methods:

- Binary logistic regression and odds ratio. Similar to the critical gap determination, the binary logistic regression was also used for modeling gap acceptance decisions as a binary response. This analysis, however, considered not only gap sizes but also a variety of other independent variables in the modeling process. In addition to the estimated variable coefficients, SAS also outputted the corresponding odds ratios to measure the association between the independent variables and the responses.
- Decision tree. The decision tree approach is a popular supervised machine learning method that is capable of both classification and regressiontasks (33, 34). It is a nonparametric method that makes no assumptions about data distribution. Compared with other nonparametric machine learning techniques, the decision tree method is able to handle both numerical and categorical variables. The resulting tree structure provides direct visualization of the model, making it simple to interpret. In addition, the decision tree technique is designed to mirror the human decisionmaking process, therefore making it ideal for modeling gap acceptance decisions.
- During a decision tree growing process, all training observations with different classes are input into the root node. The algorithm then selects a feature to split the observations in the parent node into different groups, or children nodes. The algorithm then measures the impurity of the parent node and the weighted sum of the children nodes, and selects the feature that can reduce the impurity to the greatest extent for further splitting. This process runs in a top-down recursive manner until all observations in each node are of the same class.
- Random forest. Without control, a decision tree can grow to be very deep until the impurity of the node can no longer decrease. However, such a tree is often over-complicated and severely suffers from overfitting. To avoid overfitting, it is common to use pruning to reduce the size of the decision tree by removing branches that contribute little to the overall model. In addition to the potential overfitting problem, a slight change in the training dataset or predictors for a decision tree can result in great variance in the output.
- The random forest method is based on the decision tree technique but is less susceptible to both overfitting and result variation at a cost of reduced interpretability (35). When developing a random forest model, an algorithm creates multiple datasets using the bootstrap technique where each dataset randomly takes a portion of the training data to develop an individual decision tree. The individually and randomly developed decision trees therefore form the so-called forest of decision trees. The random forest approach outputs the averages or the majority votes of the estimation results based on the multiple decision trees it develops during the process. During this study, the research team developed both decision tree and random forest models using the Scikit-learn toolkit in Python (36).

For all analyses, the research team considered nine analysis scenarios including all collected trips, right-turn trips, left-turn trips, left-turn trips with two-way left-turn
lane (TWLTL) on the major road, left-turn trips without TWLTL on the major road, right-turn trips with leading vehicle, right-turn trips without leading vehicle, left-turn trips with leading vehicle, and left-turn trips without leading vehicle.

## Results and Discussions

Owing to limited space, this paper selectively presents some major findings of the data analyses. Detailed descriptions of all analyses and results are available in research by Li et al. (37).

## Critical Gap Determination

Table 2 compares the critical gap values for the different scenarios according to the three different approaches. Overall, the three methods showed an average critical gap size of 5.63 s for all trips. For right-turn movement, the methods suggested a critical gap ranging between 4.88 and 5.47 s with an average of 5.25 s. For left-turn movement, the methods showed a critical gap ranging between 6.16 and 6.24 s with an average of 6.19 s, almost a second longer than that for right-turn movements. In addition,

- The data showed a shorter critical gap (i.e., 5.93 versus 6.31 s) for left-turn movement when a leading vehicle was present. The presence of leading vehicles was highly significantly correlated with the presence of following vehicles. This finding seemed to suggest that drivers would take a shorter gap when turning left onto the major roadway when there was more traffic on the minor approach. For the right-turn movement, however, this effect was much less evident. In fact, right-turn drivers tended to take a slightly longer gap (i.e., 5.41 versus 5.20 s) when leading or following vehicles were present. Overall, the presence of a TWLTL corresponded to a shorter critical gap size (i.e., 6.15 versus 6.32 s) for left-turn traffic. This fact could suggest that the presence of a TWLTL provides potential space for left-turn drivers to wait in case of a conflict with major street traffic and therefore increases driver confidence during the gap acceptance process.
- In most cases, the maximum likelihood method produced lower critical gap sizes. In particular, the critical gap sizes for the right-turn scenarios estimated by this method were evidently shorter than the other two methods. However, both the binary logistic regression and the probability equilibrium methods showed comparable results for all scenarios. Both the logistic regression and

## Factors Affecting Gap Acceptance Decision

Table 3 lists the significant parameters and their associated odds ratios for three scenarios: all trips, all right-turn trips, and all left-turn trips. SAS uses maximum likelihood for model estimation and outputted the Akaike Information Criterion, the Schwarz Criterion, and the -2 log likelihood as indicators of the overall model goodness of fit. It also uses likelihood ratio test, score test, and the Wald test to show the significance of independent variables.

Table 4 summarizes the decision tree model information, the important features with an importance score $\geqslant 5 \%$, and their associated importance scores; this is followed by Figure 4 that shows the decision tree model for all trips as an illustration of the decision process. During this study, the dataset for each analysis scenario was split into 70\% training and 30\% testing sets. Observations of the different classes, that is, gap acceptance and gap rejection, were balanced by adjusting their associated weights. The team used entropy for node impurity measurement and trimmed the tree by controlling the minimum impurity decrease and minimum sample size on a splitting node. The importance scores of analyzed features were calculated as the normalized reduction of the impurity brought by that feature.

Table 5 lists the random forest modeling information, prediction performance, important features (with a feature importance $\geqslant 3 \%$ ), and feature importance scores. During this analysis, the dataset was split into 70\% training and 30\% testing. Observations of different groups were balanced by adjusting their associated weights. Entropy was also used as the criterion of selecting splitting features.

Overall, the analysis results showed many factors that affected drivers' gap acceptance decisions. For example, being a gap instead of a lag, the presence of leading vehicles, following vehicles, or both, higher ADT, the intersection being unskewed, and a higher number of through lanes all increased the probability of a driver accepting a given gap for multiple scenarios. Conversely, adverse weather conditions reduced the probability of acceptance for a given gap. In addition, the decision tree results

Table 2. Comparison of Critical Gaps Determined by Different Methods
| Scenario | Critical gap size (s) |  |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  | Maximum likelihood | Logistic regression | Probability equilibrium | Mean |
| All right turn | 4.877 | 5.411 | 5.466 | 5.251 |
| Right turn without leading vehicle | 4.899 | 5.349 | 5.365 | 5.204 |
| Right turn with leading vehicle | 4.846 | 5.638 | 5.759 | 5.414 |
| All left turn | 6.164 | 6.155 | 6.238 | 6.186 |
| Left turn without leading vehicle | 6.332 | 6.198 | 6.400 | 6.310 |
| Left turn with leading vehicle | 5.633 | 6.189 | 5.981 | 5.934 |
| Left turn without TWLTL | 6.583 | 6.141 | 6.232 | 6.319 |
| Left turn with TWLTL | 6.025 | 6.176 | 6.240 | 6.147 |
| All movements | 5.390 | 5.715 | 5.782 | 5.629 |


Note: TWLTL = two-way left-turn lane.

Table 3. Significant Variables and Odds Ratios
| Parameter | Estimate | Standard error | Wald chi-square | Pr > chi ${ }^{2}$ | Odds ratio (95\% confidence interval) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| All trips |  |  |  |  |  |
| Intercept | -7.8973 | 0.7846 | 101.3096 | <. 0001 | Not applicable |
| Is gap (as against a lag) | 1.6701 | 0.3035 | 30.2766 | <. 0001 | 5.313 (2.931-9.632) |
| Gap size | 1.2618 | 0.0908 | 192.9732 | <. 0001 | 3.532 (2.956-4.220) |
| Wait time | -0.0254 | 0.0117 | 4.7114 | 0.0300 | 0.975 (0.953-0.998) |
| Weather | -0.8034 | 0.4510 | 3.1731 | 0.0749 | 0.448 (0.185-1.084) |
| Turn type | -1.1271 | 0.3402 | 10.9758 | 0.0009 | 0.324 (0.166-0.631) |
| Leading vehicle | 1.3679 | 0.3543 | 14.9035 | 0.0001 | 3.927 (1.961-7.864) |
| Major road AADT | 0.078 | 0.028 | 8.0464 | 0.0046 | 1.081 (1.023-1.142) |
| Major approach left turn lane-right | -1.1817 | 0.3263 | 13.1163 | 0.0003 | 0.307 (0.162-0.581) |
| Major road TWLTL | -1.1794 | 0.3338 | 12.4857 | 0.0004 | 0.307 (0.160-0.591) |
| Minor road on-street parking left side | -1.2803 | 0.5465 | 5.4886 | 0.0191 | 0.278 (0.095-0.811) |
| Intersection alignment-skew to right | 0.1060 | 0.3216 | 0.1086 | 0.7417 | 0.651 (0.259-1.635) |
| Intersection alignment-skew to left | -0.6411 | 0.2694 | 5.6642 | 0.0173 | 0.308 (0.153-0.622) |
| All right-turn trips |  |  |  |  |  |
| Intercept | -7.5364 | 0.9061 | 69.1789 | <. 0001 | Not applicable |
| Is gap (as against a lag) | 1.5426 | 0.3880 | 15.8108 | <. 0001 | 4.677 (2.186-10.004) |
| Gap size | 1.3599 | 0.1316 | 106.8534 | <. 0001 | 3.896 (3.010-5.042) |
| Leading vehicle | 0.6930 | 0.4095 | 2.8637 | 0.0906 | 2.000 (0.898-4.462) |
| Major approach left turn lane-right | -1.1792 | 0.3824 | 9.5107 | 0.0020 | 0.308 (0.145-0.651) |
| Major road TWLTL | -0.8054 | 0.3971 | 4.1134 | 0.0425 | 0.447 (0.205-0.973) |
| Intersection alignment-skew to right | -0.3548 | 0.4680 | 0.5748 | 0.4484 | 0.372 (0.091-1.523) |
| Intersection alignment-skew to left | -0.2802 | 0.3041 | 0.8493 | 0.3567 | 0.400 (0.193-0.829) |
| All left-turn trips |  |  |  |  |  |
| Intercept | -9.8343 | 1.1844 | 68.9430 | <. 0001 | Not applicable |
| Is gap (as against a lag) | 1.5302 | 0.4526 | 11.4324 | 0.0007 | 4.619 (1.903-11.214) |
| Gap size | 1.2214 | 0.1329 | 84.4220 | <. 0001 | 3.392 (2.614-4.402) |
| Wait time | -0.0342 | 0.0129 | 7.0253 | 0.0080 | 0.966 (0.942-0.991) |
| Weather | -1.1693 | 0.6269 | 3.4792 | 0.0621 | 0.311 (0.091-1.061) |
| Leading vehicle | 2.0525 | 0.5329 | 14.8317 | 0.0001 | 7.787 (2.740-22.132) |
| Major road no. of through lanes | 1.0860 | 0.3898 | 7.7608 | 0.0053 | 2.962 (1.380-6.360) |
| Major road crosswalk-left approach | 1.8090 | 1.0081 | 3.2199 | 0.0727 | 6.105 (0.846-44.034) |


Note: TWLTL = two-way left-turn lane; AADT = average annual daily traffic.
suggested that a waiting time longer than 9 s tended to increase the probability of gap acceptance when analyzing all trips together.

The decision tree models further suggested that gap sizes were the determinant factor for gap acceptance, responsible for 60\% to 85\% of the model weights

Table 4. Model Information and Important Features of Decision Tree Models
| Scenario | Model information |  | Major features: importance |
| :--- | :--- | :--- | :--- |
| All trips (785 gaps) | Minimum decreased impurity | 0.01 | - Gap size: 73.14\% |
|  | Minimum samples split | 10 | - Is gap (as against a lag): 5.33\% |
|  | Accuracy in training set | 88.71\% | - Wait time: 21.53\% |
|  | Accuracy in testing set | 88.14\% |  |
| Right turn (423 gaps) | Minimum decreased impurity | 0.02 | - Gap size: 62.00\% |
|  | Minimum samples split | 10 | - Wait time: 24.93\% |
|  | Accuracy in training set | 92.23\% | - Is gap (as against a lag): 4.36\% |
|  | Accuracy in testing set | 83.46\% | - Major ADT: 8.70\% |
| Left turn (362 gaps) | Minimum decreased impurity | 0.02 | - Gap size: 85.44\% |
|  | Minimum samples split | 10 | - Wait time: 14.56\% |
|  | Accuracy in training set | 90.12\% |  |
|  | Accuracy in testing set | 83.49\% |  |
| Left turn with TWLTL (243 gaps) | Minimum decreased impurity | 0.03 | - Gap size: 85.08\% |
|  | Minimum samples split | 10 | - Wait time: 7.83\% |
|  | Accuracy in training set | 90.00\% | - Major sidewalk: 7.09\% |
|  | Accuracy in testing set | 80.82\% |  |
| Left turn without TWLTL (119 gaps) | Minimum decreased impurity | 0.05 | - Gap size: 73.69\% |
|  | Minimum samples split | 10 | - Major ADT: 14.00\% |
|  | Accuracy in training set | 91.57\% | - Major crosswalk left: 12.31\% |
|  | Accuracy in testing set | 80.56\% |  |
| Right turn with leading vehicle (87 gaps) | Minimum decreased impurity | 0.05 | - Gap size: 69.67\% |
|  | Minimum samples split | 10 | - Annual miles traveled: 18.08\% |
|  | Accuracy in training set | 93.33\% | - Major sidewalk: 12.26\% |
|  | Accuracy in testing set | 74.07\% |  |
| Right turn no leading vehicle (336 gaps) | Minimum decreased impurity | 0.03 | - Gap size: 59.79\% |
|  | Minimum samples split | 10 | - Is gap (as against a lag): 17.04\% |
|  | Accuracy in training set | 90.38\% | - Wait time: 23.17\% |
|  | Accuracy in testing set | 73.91\% |  |
| Left turn with leading vehicle (75 gaps) | Minimum decreased impurity | 0.05 | - Gap size: 75.75\% |
|  | Minimum samples split | 10 | - Major-road alignment = curve-outwards: 9.30\% |
|  | Accuracy in training set | 88.71\% | - Is gap (as against a lag): 7.71\% |
|  | Accuracy in testing set | 88.14\% | - Annual miles traveled: 7.24\% |
| Left turn no leading vehicle (287 gaps) | Minimum decreased impurity | 0.03 | - Gap size: 78.77\% |
|  | Minimum samples split | 10 | - Is gap (as against a lag): 9.48\% |
|  | Accuracy in training set | 92.50\% | - Wait time: 11.75\% |
|  | Accuracy in testing set | 91.95\% |  |


Note: TWLTL = two-way left-turn lane; ADT = average daily traffic.
depending on the analysis scenario. In addition to gap size, the analysis found that wait time, gap type (i.e., gap versus lag), and major road ADT had relatively substantial impacts on model performance. The random forest analysis once again showed that gap size had the dominant effect on the gap acceptance decision, albeit at a lower level of importance (30\% to 51\% of model weight) compared with the decision tree models.

Each of the three methods revealed advantages and disadvantages during this analysis. The logistic regression method was straightforward in identifying significant variables and quantifying their impacts. However, the method was unable to explain nonlinear correlations. The decision tree method, however, was able to reveal some complex correlations in the data and identified critical data points that served as thresholds in decision making. Using waiting time as an example, this variable was identified to be significant in the overall model, and the models for all left-turn trips, left-turn with TWLTL trips, left-turn without leading vehicle trips, and right-turn without leading vehicle trips in the logistic regression. In addition, the models showed an associated negative parameter, suggesting that drivers were more likely to reject a gap the longer they waited, with odds ratios ranging between 0.93 and 0.98 . To explore this correlation further, Figure 5 shows a scatterplot of rejected gaps by waiting time. The plot seemingly suggests that the rejected gaps tended to be longer initially as drivers waited, but after waiting for more than 20 s, the rejected gaps tended to be shorter as the waiting time lengthened. This relationship was however better reflected by the decision tree models.

The dichotomous structure associated with decision trees was able to show which decision was more likely to

![](https://cdn.mathpix.com/cropped/89a26f37-9815-4c7e-873c-179cc15d868d-11.jpg?height=1335&width=1750&top_left_y=252&top_left_x=215)
Figure 4. Decision tree for all trips scenario.

be taken under different conditions, but it could not quantify the influence of the factor in the way that logistic regression did. Random forest models worked like a black box and did not provide information about the influence of the analyzed features' presence on responses, but they were able to identify a more complete set of variables that affected the output than the decision tree models. Although the logistic regression models quantified the impact of individual variables on the model outcome, it could not, however, measure the importance of the variable for the overall performance of the model. The machine learning methods, therefore, are superior in this regard.

## Conclusion

Safety at unsignalized intersections continues to be a major concern for transportation agencies and roadway users. To improve intersection safety, this project conducted a comprehensive study of gap acceptance behaviors at unsignalized intersections using SHRP2 NDS data. For the purpose of this project, the team collected detailed information for 1,170 accepted and rejected gaps/lags based on 466 NDS trips at 64 unsignalized T-intersections in Washington and North Carolina.

Based on naturalistic driving data at many intersections, the project team identified critical gaps for nine scenarios. During this process, the project team also compared the results of three different methods for critical gap determination. In addition, the study comprehensively identified the factors affecting gap acceptance behavior and quantified their effects using three statistical and machine learning methods. The three methods showed different advantages that, when combined, provided a complete picture of how different factors affected drivers' gap acceptance decisions.

Typically, gap acceptance has been studied using observational data collected from outside the vehicles

Table 5. Model Information and Important Features of Random Forest Models
| Scenario | Model information |  | Major features: importance |
| :--- | :--- | :--- | :--- |
| All trips (785 gaps) | Number of trees | 1,000 | - Gap size: 44.36\% |
|  | Maximum tree depth | 3 | - Wait time: 21.91\% |
|  | Accuracy in training set | 86.70\% | - Major road ADT: 4.30\% |
|  | Accuracy in testing set | 86.86\% | - Leading vehicle: 3.31\% |
| Right turn (423 gaps) | Number of trees | 1,000 | - Gap size: 40.38\% |
|  | Maximum tree depth | 3 | - Wait time: 22.18\% |
|  | Accuracy in training set | 90.88\% | - Major road ADT: 4.91\% |
|  | Accuracy in testing set | 82.68\% |  |
| Left turn (362 gaps) | Number of trees | 1,000 | - Gap size: 48.15\% |
|  | Maximum tree depth | 4 | - Wait time: 16.38\% |
|  | Accuracy in training set | 90.91\% | - Major road ADT: 4.59\% |
|  | Accuracy in testing set | 83.49\% | - Annual miles traveled: 3.77\% |
| Left turn with TWLTL (243 gaps) | Number of trees | 1,000 | - Gap size: 39.23\% |
|  | Maximum tree depth | 3 | - Wait time: 17.94\% |
|  | Accuracy in training set | 90.59\% | - Leading vehicle: 5.17\% |
|  | Accuracy in testing set | 84.93\% | - Annual miles traveled: 5.12\% |
|  |  |  | - Major road ADT: 3.71\% |
| Left turn without TWLTL (119 gaps) | Number of trees | 100 | - Gap size: 30.79\% |
|  | Maximum tree depth | 2 | - Wait time: 16.52\% |
|  | Accuracy in training set | 92.77\% | - Major road ADT: 11.8\% |
|  | Accuracy in testing set | 80.56\% | - Major-road alignment: 10.79\% |
|  |  |  | - Intersection alignment: 6.51\% |
|  |  |  | - Minor approach number of lanes: 3.1\% |
|  | Number of trees | 100 |  |
| Right turn with leading vehicle (87 gaps) | Maximum tree depth | 2 | - Gap size: 32.69\% |
|  | Accuracy in training set | 97.59\% | - Major road ADT: 9.94\% |
|  | Accuracy in testing set | 83.33\% | - Annual miles traveled: 7.2\% |
|  |  |  | - Major-road alignment: 6.58\% |
|  |  |  | - Age group: 5.50\% |
| Right turn no leading vehicle (336 gaps) | Number of trees | 1,000 | - Gap size: 43.61\% |
|  | Maximum tree depth | 5 | - Wait time: 23.43\% |
|  | Accuracy in training set | 95.74\% | - Annual miles traveled: 3.46\% |
|  | Accuracy in testing set | 91.09\% | - Major road ADT: 3.4\% |
| Left turn with leading vehicle (75 gaps) | Number of trees | 1,000 | - Gap size: 42.38\% |
|  | Maximum tree depth | 4 | - Wait time: 23.73\% |
|  | Accuracy in training set | 95.32\% | - Major road ADT: 3.84\% |
|  | Accuracy in testing set | 86.14\% | - Is gap (as against a lag): 2.65\% |
|  |  |  | - Major approach left turn lane-right: 2.55\% |
| Left turn no leading vehicle (287 gaps) | Number of trees | 100 | - Gap size: 51.55\% |
|  | Maximum tree depth | 5 | - Wait time: 14.62\% |
|  | Accuracy in training set | 93.00\% | - Major ADT: 4.65\% |
|  | Accuracy in testing set | 87.36\% | - Intersection alignment: 3.72\% |


Note: TWLTL = two-way left-turn lane; ADT = average daily traffic.
based on video or manual timing at intersections. The availability of the SHRP2 NDS data provided a unique opportunity to study driver gap acceptance behavior from a different angle. SHRP2 NDS data allowed the researchers to understand not only how gap acceptance behaviors vary with different traffic and intersection conditions, but also how different driver characteristics such as age and driving history correlated with their gap acceptance behaviors. The detailed driver, trip, and vehicle kinematical data enabled from the NDS database was fully utilized in this study and therefore provided new insights into gap acceptance behaviors at unsignalized intersections. In addition, the use of both parametric and nonparametric methods in this study allowed better quantification of the factors that influenced gap acceptance behaviors at unsignalized intersections.

![](https://cdn.mathpix.com/cropped/89a26f37-9815-4c7e-873c-179cc15d868d-13.jpg?height=530&width=844&top_left_y=254&top_left_x=215)
Figure 5. Scatterplot for rejected gaps by waiting time.

## Author Contributions

The authors confirm contribution to the paper as follows: study conception and design: Y. Li, H. Hao, R. Gibbons, A. Medina; data collection: H. Hao; analysis and interpretation of results: H. Hao, Y. Li; draft manuscript preparation: Y. Li, H. Hao, R. Gibbons, A. Medina. All authors reviewed the results and approved the final version of the manuscript.

## Declaration of Conflicting Interests

The author(s) declared no potential conflicts of interest with respect to the research, authorship, and/or publication of this article.

## Funding

The author(s) disclosed receipt of the following financial support for the research, authorship, and/or publication of this article: This paper is based on research funded by the National Surface Transportation Safety Center for Excellence.

## References

1. National Highway Traffic Safety Administration. Fatality Analysis Reporting System (FARS). https://www.nhtsa .gov/research-data/fatality-analysis-reporting-system-fars. Accessed December 21, 2019.
2. Federal Highway Administration. Safety - Unsignalized Intersections. https://safety.fhwa.dot.gov/intersection/conventional/unsignalized/. Accessed November 15, 2020.
3. Troutbeck, R. J., and W. Brilon. Revised Monograph on Traffic Flow Theory. Federal Highway Administration. https://www.fhwa.dot.gov/publications/research/operations/ tft/.
4. Brilon, W., R. Koenig, and R. J. Troutbeck. Useful Estimation Procedures for Critical Gaps. Transportation Research Part A: Policy and Practice, Vol. 33, No. 3-4, 1999, pp. 161-186.
5. Mohan, M., and S. Chandra. Review and Assessment of Techniques for Estimating Critical Gap at Two-Way StopControlled Intersections. European Transport, Vol. 61, No. 61, 2016, pp. 1-18.
6. Maze, T. H. A Probabilistic Model of Gap Acceptance Behavior. Transportation Research Record: Journal of the Transportation Research Board, 1981. 795: 8-13.
7. Fitzpatrick, K. Gaps Accepted at Stop-Controlled Intersections. Transportation Research Record: Journal of the Transportation Research Board, 1991. 1303: 103-112.
8. Ashworth, R. The Analysis and Interpretation of Gap Acceptance Data. Proc., 1st Annual Conference of the British Universities Transport Study Group, University of Leeds, West Yorkshire, 1969.
9. Gattis, J., and S. Low. Gap Acceptance at Atypical StopControlled Intersections. Journal of Transportation Engineering, Vol. 125, No. 3, 1999, pp. 201-207.
10. Shaaban, K., and H. Hamad. Group Gap Acceptance: A New Method to Analyze Driver Behavior and Estimate the Critical Gap at Multilane Roundabouts. Journal of Advanced Transportation, Vol. 2018, No. 3, 2018, pp. 1-9. https://doi.org/10.1155/2018/1350679.
11. Guo, R. Estimating Critical Gap of Roundabouts by Different Methods. Proc., 6th Advanced Forum on Transportation of China, Beijing, 2010, pp. 84-89.
12. Troutbeck, R. J. Estimating the Critical Acceptance Gap from Traffic Movements. Research Report 92-5. Queensland University of Technology, Brisbane, Australia, 1992.
13. McGowen, P., and L. Stanley. Alternative Methodology for Determining Gap Acceptance for Two-Way Stop-Controlled Intersections. Journal of Transportation Engineering, Vol. 138, No. 5, 2012, pp. 495-501.
14. Wu, N. A New Model for Estimating Critical Gap and its Distribution at Unsignalized Intersections Based on the Equilibrium of Probabilities. Proc., 5th International Symposium on Highway Capacity and Quality of Service, Yokohama, Japan, 2006, pp. 1-10.
15. Ragland, D. R., S. Arroyo, S. E. Shladover, J. A. Misener, and C. Y. Chan. Gap Acceptance for Vehicles Turning Left across On-Coming Traffic: Implications for Intersection Decision Support Design. Presented at 85th Annual Meeting of the Transportation Research Board, Washington, D.C., 2006.
16. Zhong, X., X. Zhu, Y. Zhang, and X. Liu. Left-Turn Gap Acceptance Behavior of Tee Type of Unsignalized Intersection. Proc., International Conference on Transportation Engineering 2007, Chengdu, China, 2007, pp. 2975-2980.
17. Miller, A. J. Nine Estimators for Gap-Acceptance Parameters. Proc., International Symposium on the Theory of Traffic Flow and Transportation, Berkeley, CA, 1971.
18. Tupper, S. M. Safety and Operational Assessment of Gap Acceptance through Large-Scale Field Evaluation. MS thesis. University of Massachusetts, Amherst, 2011.
19. Akçelik, R. A Review of Gap-Acceptance Capacity Models. Proc., 29th Conference of Australian Institutes of Transport Research (CAITR), University of South Australia, Adelaide, 2007.
20. Maurya, A. K., H. J. Amin, and A. Kumar. Estimation of Critical Gap for through Movement at Four Leg Uncontrolled Intersection. Transportation Research Procedia, Vol. 17, 2016, pp. 203-212.
21. Highway Capacity Manual. Transportation Research Board, Washington, D.C., 2000.

22. AASHTO. A Policy on Geometric Design of Highways and Streets. American Association of State Highway and Transportation Officials, Washington, D.C., 2010.
23. Harwood, D., J. Mason, R. Brydia, M. Pietrucha, and G. Gittings. Intersection Sight Distance. NCHRP Report 383. Transportation Research Board, Washington, D.C., 1996.
24. Nabaee, S. An Evaluation of Gap Acceptance Behavior at Unsignalized Intersections. MS thesis. Oregon State University, Corvallis, 2011.
25. Ragland, D. R., S. Arroyo, S. E. Shladover, J. A. Misener, and C. Chan. Gap Acceptance for Vehicles Turning Left across On-Coming Traffic: Implications for Intersection Decision Support Design. Research Report. Safe Transportation Research \& Education Center, UC Berkeley, 2005.
26. Zohdy, I. H. Modeling Permissive Left-Turn Gap Acceptance Behavior at Signalized Intersections. Doctoral dissertation. Virginia Tech, Blacksburg, 2009.
27. Hankey, J. M., M. A. Perez, and J. A. McClafferty. Description of the SHRP2 Naturalistic Database and the Crash, Near-Crash, and Baseline Data Sets. Task Report for the Strategic Highway Research Program 2. Virginia Tech, Blacksburg, 2016.
28. Campbell, K. The SHRP2 Naturalistic Driving Study: Addressing Driver Performance and Behavior in Traffic Safety. TR News, No. 282, September 2012, pp. 30-35.
29. SHRP2 NDS. InSight. https://insight.shrp2nds.us. Accessed December 7, 2017.
30. McLaughlin, S. B., and J. M. Hankey. Naturalistic Driving Study: Linking the Study Data to the Roadway InformationDatabase. Publication SHRP2 Report S2-S31-RW-3. Transportation Research Board of the National Academies, Washington, D.C., 2015.
31. Troutbeck, R. J. Estimating the Mean Critical Gap. Transportation Research Record: Journal of the Transportation Research Board, 2014. 2461: 76-84.
32. SAS. SAS/STAT 9.2 User's Guide, 2nd ed. SAS Institute Inc. https://support.sas.com/documentation/cdl/en/statug/ 63033/HTML/default/viewer.htm\#statug_reg_sect038.htm. Accessed December 12, 2019.
33. Wikipedia.org. Decision Tree Learning. https://en.wikipedia.org/wiki/Decision_tree_learning. Accessed June 12, 2020.
34. Nagalla, R., P. Pothuganti, and D. S. Pawar. Analyzing Gap Acceptance Behavior at Unsignalized Intersections Using Support Vector Machines, Decision Tree and Random Forests. Procedia Computer Science, Vol. 109, 2017, pp. 474-481.
35. Wikipedia.org. Random Forest. http://en.wikipedia.org/ wiki/Random_forest. Accessed June 12, 2020.
36. Pedregosa, F., G. Varoquaux, A. Gramfort, V. Micheal, B. Thirion, O. Grisel, and J. Vanderplas. Scikit-Learn: Machine Learning in Python. Journal of Machine Learning Research, Vol. 12, No. October, 2011, pp. 2825-2830.
37. Li, Y., H. Hao, R. B. Gibbons, and A. Medina. Analyzing Intersection Gap Acceptance Behavior with Naturalistic Driving Data. Draft Research Report. National Surface Transportation Safety Center for Excellence, Virginia Tech, Blacksburg, 2020.

[^0]:    ${ }^{1}$ Virginia Tech Transportation Institute, Blacksburg, VA
    Corresponding Author:
    Yingfeng (Eric) Li, eli@vtti.vt.edu

