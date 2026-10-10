# How many are enough?: Investigating the effectiveness of multiple conflict indicators for crash frequency-by-severity estimation by automated traffic conflict analysis 

Ashutosh Arun ${ }^{\mathrm{a}}$, Md. Mazharul Haque ${ }^{\mathrm{a}, *}$, Simon Washington ${ }^{\mathrm{b}}$, Tarek Sayed ${ }^{\mathrm{c}}$, Fred Mannering ${ }^{\mathrm{d}}$<br>${ }^{\mathrm{a}}$ School of Civil and Environmental Engineering, Queensland University of Technology, Brisbane, Australia<br>${ }^{\mathrm{b}}$ Advanced Mobility Analytics Group (AMAG), Brisbane, Australia<br>${ }^{\mathrm{c}}$ Department of Civil Engineering, University of British Columbia, Vancouver, Canada<br>${ }^{\mathrm{d}}$ College of Engineering, University of South Florida, Tampa, FL 33620, USA

## ARTICLE INFO

Keywords:
Traffic conflict techniques
Crash severity
Crash-conflict relationship
Peak over threshold
Extreme value copulas
Multivariate modelling


#### Abstract

Traffic conflict techniques are a viable alternative to crash-based safety assessments and are particularly well suited to evaluating emerging technologies such as connected and automated vehicles for which crash data are sparsely available. Recently, the use of multiple traffic conflict indicators has become common in methodological studies, yet it is often difficult to determine which conflict indicators are appropriate given the application context, and the net benefit, in terms of improved crash prediction accuracy, of considering additional conflict indicators. Addressing these concerns, this study investigates the potential benefits of multiple conflict indicators for conflict-based crash estimation models by using a multivariate extreme value modeling framework (with Gumbel-Hougaard copulas) to estimate crash frequency by severity. The selected conflict indicators include Modified Time-To-Collision (MTTC), Deceleration Rate to Avoid a Collision (DRAC), Proportion of Stopping Distance (PSD) and expected post-collision change in velocity (Delta-V). The proposed framework was applied to estimate the total, severe (Maximum Abbreviated Injury Scale $\geq 3$; MAIS3+), and non-severe (MAIS < 3) rear-end crash frequencies at three four-legged signalized intersections in Brisbane, Australia. Rear-end traffic conflicts were extracted from video data using state-of-the-art Computer Vision analytics. Results show that the prediction performance improvements are not necessarily proportional to the number of conflict indicators used in extreme value models. MTTC and DRAC, combined with the severity indicator Delta-V, were the most suitable predictors of rear-end crashes at signalized intersections. Results suggest that instead of adding more and more conflict indicators, careful selection of compatible conflict indicators (considering their functional differences and empirical correlations) is the best way to enhance the predictive performance of conflict-based models.


[^0]
## 1. Introduction

Emerging technologies such as Connected and Automated Vehicles (CAV) require real-time crash-risk estimation to safely maneuver through their surroundings (Liu et al., 2017; Wu et al., 2018). Infrastructure-based intelligent transport system (ITS) technologies such as adaptive traffic signal control (Essa and Sayed, 2020; Jin et al., 2021) require real-time safety-related information to enable joint optimization of traffic signal timing for both safety and delay minimization. Legacy safety evaluation methods based on historical crash data are largely unsuitable for such applications due to the need for immediate information to undertake risk mitigation actions in real-time. Moreover, for novel technologies such as Active Vehicle Safety Systems (AVSS), the small number of observed crashes involving such technologies make traditional crash-based analyses problematic (Jeong and Oh, 2017). Thus, traffic conflict-based safety analysis is an attractive alternative to evaluate the safety-related impacts of novel technologies.

A critical element in the safety assessment of emerging technologies relates to the ability to interpret the traffic environment to account for the various safety threats and risks that dynamically arise with the interaction of various types of road users. Traffic conflict indicators such as Modified Time-to-Collision (MTTC) are valuable measures of crash risk in real-time (Zheng and Sayed, 2020). However, due to the variability in the types of road users and transport facilities, it is unreasonable to expect a single traffic conflict indicator to capture all safety-relevant information (Ismail et al., 2011, Arun et al., 2021c). In response to this, there has been a growing trend to include multiple conflict indicators in conflict-based analysis.

Further, it is also uncertain how using multiple conflict indicators actually affects the measurement of crash risk. It is necessary to investigate the relationship between the various conflict indicators and the actual crash probability to ensure that the observed conflicts adequately capture the risk profile of the interaction between two road users (or a road user and a fixed object). In the absence of such a relationship, the use of multiple conflict indicators is fraught with risks. It is possible that the various indicators have associations with crash probability such that using them together may actually adversely affect the accuracy of conflict analysis. For instance, Zheng et al. (2019a) showed that using Post-Encroachment Time (PET) together with Deceleration Rate to Avoid a Crash (DRAC) for video analytics-based safety assessments of intersections could introduce significant errors due to the dependence of these two indicators. Therefore, investigating crash-conflict relationships in the case of multiple conflict indicators is crucial.

Extreme value theory (EVT) models provide an attractive, theoretically consistent methodology to estimate crash risk from conflict indicators (Zheng et al., 2021) and assess the potential benefits of including additional indicators. The EVT modelling technique predicts an unobserved quantity, the crash occurrence probability, by modelling the tail distribution of observed extreme conflicts. The crash probability can then be suitably scaled to estimate the crash frequency for any required horizon period. In previous research, Asljung et al. (2017) used EVT to estimate vehicle level safety for autonomous vehicles using prevalent conflict indicators like Time-toCollision (TTC) and Brake Threat Number (BTN). Zheng and Sayed (2020) demonstrated real-time rear-end crash risk prediction using the Modified Time-to-Collision (MTTC) indicator in an EVT model. Fu et al. (2021) extended the method by introducing a hierarchical extreme value method to estimate the crash risk of rear-end and side-swipe conflicts with a single TTC indicator. Among other possible applications relating to emerging technologies, most significantly, their models can be implemented for enhanced remote safety monitoring of transport facilities such as signalized intersections using closed-circuit television (CCTV) cameras, which is a common component of advanced traffic management systems.

While the above studies were based on the univariate (one conflict indicator) implementation of the extreme value theory, multivariate extreme value methods (using multiple indicators) have been undertaken to improve the accuracy of crash-risk predictions. For example, Zheng et al. (2018) introduced bivariate extreme value modelling for total crash frequency estimation at freeway merging areas by employing Post-encroachment Time (PET) and Length Proportion of Merging (LPM) indicators. Since then, several studies (Cavadas et al., 2020; Gastaldi et al., 2020; Zheng and Sayed, 2019c) have implemented bivariate extreme value models for estimating total crash frequency at various transport facilities such as intersections, roundabouts, and two-lane road segments. Recently, Fu et al. (2020) and Fu and Sayed (2021b) introduced Bayesian hierarchical methods for multivariate estimation of total crash frequency at signalized intersections using three indicators; Modified Time-to-Collision (MTTC), Post-encroachment Time (PET), and Deceleration Rate to Avoid Collision (DRAC). They parameterized the location and modified scale parameters of the marginal Generalized Extreme Value (GEV) models as functions of traffic signal cycle-level variables including traffic volume, shockwave area, and platoon ratio to account for temporal trends present in the conflict data. Notably, both the studies found that the higherdimensional trivariate models outperformed the more parsimonious bivariate models in terms of prediction accuracy, although the bivariate MTTC and PET and the bivariate MTTC and DRAC models also provided reasonably accurate results. Fu and Sayed (2021b) further noted that the multivariate estimation using a copula modeling method slightly outperformed the multivariate EVT estimation method introduced in their earlier study (Fu et al., 2020), which they reasoned was due to the additional dependence information of conflict indicators captured by the copula models.

The trend toward including multiple conflict measures raises an important question; how many conflict indicators should be included in extreme value models to estimate crash frequencies adequately? While this is likely to be data and application-context dependent, higher-dimensional conflict data does increase modeling complexity, and the potential benefits of this additional dimensionality have not been empirically explored. Thus, the question is whether there are significant benefits from the increasingly complex trivariate and higher dimensional extreme value models and whether there is a number or combination of conflict indicators for a given context, beyond which further improvements in the accuracy and precision of crash estimates cannot be expected from extreme value models. Thus far, this question has not been adequately investigated in conflict-based safety assessment.

Another element in the conflict-based multivariate extreme value crash estimation framework that has not been adequately investigated is crash-injury severity. The capability of estimating crash frequencies by injury severity is an essential element of safety evaluation that can significantly improve the efficacy of potential crash countermeasures. To date, only a few studies have tried to
estimate the severity of potential crashes using traffic conflict measures (for a detailed review, see Arun et al., 2021c). However, their attempts to capture the possible severity of a traffic conflict do not represent crash outcome injury severity as it is widely understood. For instance, recently, Shangguan et al. (2021) introduced Rear-end Collision Risk Index (RCRI) that uses the square of the absolute speed difference of conflicting vehicles as an indicator of crash severity. However, they do not explore the relationship of that indicator with the actual crash injury outcome, which is typically measured in terms of prevalent severity scales such as the Abbreviated Injury Scale (AIS). As such, the applicability of such new indicators for practical crash risk estimation is limited.

In a recent study, Arun et al. (2021a) utilized the established relationship of the Delta-V crash severity conflict indicator with the actual crash outcome severity measured according to the Maximum Abbreviated Injury Scale (MAIS) (Bahouth et al., 2014) to estimate crash frequency-by-severity levels by combining Delta-V with crash frequency indicators (TTC and MTTC) in bivariate extreme value models. However, the prediction intervals of the estimated crash frequencies were somewhat wide, which could be attributed to the exclusion of other relevant conflict indicators that capture different dimensions of nearness to collisions. As such, it is important to determine which conflict indicators are suitable in a crash frequency-by-severity multivariate estimation framework.

Given the above research gaps, the current study intends to investigate the effectiveness of multiple conflict indicators for crash frequency-by-severity estimation. In particular, the study proposes a novel framework combining extreme value and copula theories to estimate total crash frequency as well as crash frequency-by-severity of rear-end crashes at signalized intersections using multiple conflict indicators extracted from automated traffic conflict analysis. This study utilized a maximum of three crash frequency indicators and one crash severity indicator in a multivariate framework to test the appropriateness of these indicators and to identify the best combination of traffic conflict indicators in estimating crash frequencies for the data considered.

The paper first presents the methodology for selecting candidate conflict indicators and the proposed novel modeling approaches for the multivariate extreme value estimation of crash frequency-by-severity. It is followed by a section providing details of the traffic conflict extraction method from video data and a summary of the extracted data. Model estimation results are then presented and discussed, including interpretations of the critical findings. The paper concludes by highlighting the important contributions and identifying the crucial directions for future research.

## 2. Methodology

Fig. 1 gives the overall methodological approach of this study, describing the complete analytical process starting from observing road user movements through video cameras, then extracting road user trajectories, followed by identification of traffic conflicts between two road users based on a time-to-collision criterion, joint distribution modelling of multiple conflict indicators using Extreme Value Copulas, and finally yielding the crash frequency-by-severity estimates. The different elements of this framework and the modelling methods are explained in detail in the following subsections.

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-03.jpg?height=848&width=1467&top_left_y=1491&top_left_x=214)
Fig. 1. The proposed Extreme Value Copula modeling framework for multivariate crash frequency-by-severity estimation.

### 2.1. Selection of conflict indicators

Conflict indicators seek to determine how close a conflict is to evolving into a crash and the probable injury-severity outcome of that potential crash. Accordingly, conflict indicators can be divided into two major classes: crash frequency and crash severity indicators. Among crash frequency indicators, the five major families are temporal proximity, spatial proximity, kinematic, mixed, and combinations of indicators categorized based on the conflict properties measured by the indicators (Arun et al., 2021c). For instance, while temporal proximity indicators define the physical nearness of conflict participants in time, the spatial proximity indicators measure the separation between the conflict participants in physical space. In contrast, the kinematic indicators typically measure the kinematic properties that govern the response of one or more conflicting participants to the emerging conflict. Combining complementary indicators from these families can account for all three elements of a road safety problem: the driver, the vehicle, and the road. The temporal proximity indicators reflect the perception-reaction failure of the road user in a conflict. If the value of a temporal proximity indicator is less than the reaction time of the road user, there is a higher probability of crash occurrence. The spatial proximity indicators measure the nearness of road users in space and account for the varying pavement surface characteristics that can affect the outcome of a conflict. In contrast, the kinematic indicators define the limit of mechanical capabilities of a vehicle in a traffic interaction. Thus, in case of a conflict, even if a road user perceives and reacts early, meaning that the temporal proximity is greater than the limit defined by their response time, a crash could still occur if the required deceleration rate for avoiding a crash is higher than the maximum available deceleration rate (MADR) for the vehicle. Thus, using multiple indicators can capture the different dimensions of the crash mechanism and improve the underlying relationship between crashes and conflicts.

The current study will focus on rear-end collisions at signalized intersections (additional details of the study environment is provided later). Given this context, after conducting an extensive literature review (Arun et al., 2021c) and building upon the recent research findings, this study selected Modified Time to Collision (MTTC) as the temporal proximity, Proportion of Stopping Distance (PSD) as the spatial proximity, and Deceleration Rate to Avoid Collision (DRAC) kinematic indicators (Fig. 2). These three indicators are used for crash frequency estimations. In addition, Delta-V has been selected as an indicator for estimating crash injury severity in the forthcoming multivariate extreme value model. It is important to note here that it is recognized that Delta-V is only an approximation of the complex energy transfer that occurs during a crash and ultimately determines injury severity. Factors such as individual vehicle structures, biomechanics of crash participants, etc., all influence the resultant injury severity. In traditional injury-severity analyses, based on observed crashes, such factors are handled with information on the characteristics of vehicles and drivers, as well as potential unobserved heterogeneity (Mannering et al., 2016). Since such detailed data are not currently available from existing real-time data-collection sources, it is recognized that this matter could impact the forthcoming severity findings. Access to richer data in the future (from vehicle-infrastructure communications, etc.) could resolve this matter within the modeling framework proposed herein.

For temporal proximity, MTTC was selected instead of the more prevalent time-to-collision (TTC) because it is a more suitable indicator than the latter for rear-end crashes at signalized intersections (Zheng and Sayed, 2019b). Further, a recent study suggested

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-04.jpg?height=889&width=1148&top_left_y=1451&top_left_x=371)
Fig. 2. Selection method of conflict indicators for multivariate analysis.

that MTTC is a more suitable indicator than TTC for jointly estimating crash frequency and severity using traffic conflicts (Arun et al., 2021a). The advantage of selecting PSD from the possible spatial proximity indicators is that it has a natural conflict threshold of 1 (with a PSD less than 1 indicating that the traffic interaction can be labelled as a conflict). PSD further accounts for the effect of pavement surface characteristics by specifically including a variable corresponding to the friction coefficient of the road surface in its specification, which is typically not considered in other conflict indicators. Shi et al. (2018) compared the performance of the most popular spatial proximity measures, PSD and Potential Index for Collision with Urgent Deceleration (PICUD), for identifying the key risk indicators along with the temporal indicators like time-integrated TTC and a crash potential index derived from DRAC. They found that PSD was the better spatial proximity indicator and especially useful in detecting conditions with small crash probabilities. Fu et al. (2020) recently found that a trivariate extreme value theory model including MTTC and DRAC along with Post-encroachment Time (PET) was more accurate than bivariate models. Moreover, previous studies have shown that DRAC, in combination with the maximum available deceleration rate of the vehicles, is a particularly good indicator of rear-end crash risk (He et al., 2018, Shi et al., 2018, Fu and Sayed, 2021a). Based on these findings and other past work, the current study adopted DRAC as the kinematic indicator. The formulas for the three selected indicators are,

$$
\begin{aligned}
& M T T C=\frac{-\Delta s \pm \sqrt{\Delta s^{2}+2 \Delta a\left(x_{l}-x_{f}-D_{l}\right)}}{\Delta a} \\
& D R A C=\frac{\Delta s^{2}}{2\left(x_{l}-x_{f}-D_{l}\right)} \\
& \text { and, PSD }=\frac{\left(x_{l}-x_{f}-D_{l}\right)}{\left(\frac{v_{f}^{2}}{2 \mu g}\right)}
\end{aligned}
$$

where, $x_{l}$ and $x_{f}$ are the respective positions of the front bumpers of the leading and the following vehicles at the time of observation; $D_{l}$ is the length of the leading vehicle; $v_{l}$ and $v_{f}$ are the respective speeds of the leading and following vehicles at the time of observation; $a_{l}$ and $a_{f}$ are the respective accelerations of the leading and following vehicles at the time of observation; $\Delta s=v_{f}-v_{l}$ is the difference in the speeds of the vehicles; $\Delta a=a_{f}-a_{l}$ is the difference in their accelerations; $\mu$ is the friction coefficient of the road surface, and $g$ is the acceleration due to gravity. Based on Guido et al. (2011), $\mu$ was assumed to be 0.4 , while $g=9.81 m / s^{2}$.

Delta-V is the most popular crash severity indicator and was demonstrated as a viable indicator for crash frequency-by-severity estimation by Arun et al. (2021a). Delta-V is defined as the change in vehicle velocity resulting from a collision (assumed to be perfectly inelastic) (Shelby, 2011) and is appropriately adopted as the severity indicator in this study. As per Laureshyn et al. (2017), the absolute value of Delta-V for two road users ( $i, j ; i$ and $j$ are interchangeable) involved in a perfectly inelastic collision is given as:

$$
\begin{aligned}
& \Delta v_{i}=\frac{m_{j}}{m_{j}+m_{i}} \sqrt{v_{i}^{2}+v_{j}^{2}-2 v_{i} v_{j} \cos \theta} \\
& \Delta v_{j}=\frac{m_{i}}{m_{j}+m_{i}} \sqrt{v_{i}^{2}+v_{j}^{2}-2 v_{i} v_{j} \cos \theta}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-05.jpg?height=697&width=1479&top_left_y=1642&top_left_x=206)
Fig. 3. The aspects of a hypothetical collision event captured by the conflict measures selected in this study.

where, $m_{i}, m_{j}$ are the masses of the two road users; $v_{i}, v_{j}$ are their speeds, and $\theta$ is their approach angle. The severity of the entire interaction can be taken as the larger of $\Delta v_{i}$ and $\Delta v_{j}$.

The indicators selected in this study are supposed to capture distinct characteristics of a traffic conflict event as illustrated in Fig. 3, which presents a traffic interaction at an instant $t$ between a leader-follower vehicle pair that hypothetically collide at a collision point distant $d_{f}$ from the follower (or $d_{l}$ from the leader). Here, MTTC is the current separation in time of the follower from this hypothetical collision point, if both the leader and follower vehicles will continue moving onward with the same amount of acceleration/deceleration that they have at the current time $t$. PSD measures the distance of the follower from the hypothetical collision point, but this distance is relative to the distance that the follower can cover if it starts braking at the maximum possible deceleration rate from the current time $t$. Thus, PSD is a simpler conflict indicator because it does not account for the actions taken by the leader vehicle. It also does not consider any possible deceleration already initiated by the follower anticipating a possible collision with the leader, depending on the risk affinity of the driver. However, it does account for the tire-pavement interaction of the following vehicle that can also affect the possible crash outcome. Meanwhile, DRAC provides the objective deceleration value that the follower must apply at the current instant $t$ to avoid colliding with the leader at the predicted collision point. Finally, Delta-V is distinct from all these indicators as it analyzes the aftermath of the hypothetical collision. Objectively, it provides the difference in the velocities of the collided mangled mass of the two vehicles that are assumed to stick and travel together in a perfectly inelastic collision and the hypothetical impact velocities of the individual vehicles. These hypothetical impact velocities of the vehicles are assumed to be the same as those at the current instant $t$. Notice the use of velocities in the definition of Delta-V because it accounts for the directions of the individual velocity vectors in addition to their magnitudes (vehicle speeds).

### 2.2. Multivariate extreme value theory

Extreme Value Theory (EVT) consists of methods that essentially model the tail distribution of the conflict measures and extrapolate the information from the observed data (conflicts) to estimate the unobserved levels (crashes). Multivariate extreme value theory leverages copula theory that enables modelling of the dependence among the variables distinctly from the univariate margins (Nelsen, 2007), thus allowing for the inclusion of more than one variable in the estimation. The margins can be estimated using either of the two popular approaches: the Block Maxima (BM) approach and the Peak-Over Threshold (POT) approach. In the block maxima approach, the extreme values are defined as the maximum occurring within a block of time like an hour or a year and are modelled using Generalized Extreme Value (GEV) distribution. In the peak-over threshold approach, the extreme values are defined as the excesses over a predefined threshold and are modelled using the Generalized Pareto (GP) distribution. The block maxima approach can suffer from inefficient data utilization since only one extreme value is analyzed in a block of time, which may not even be a truly extreme value (Coles, 2001). Thus, this study adopted the peak-over threshold approach, explained for the univariate and the multivariate cases below.

### 2.3. Univariate peak-over threshold model

Let $\left\{x_{1}, x_{2} \cdots x_{n}\right\}$ be a set of independent random observations with the unknown cumulative distribution function $F(z)=\operatorname{Pr}\left(x_{i} \leq z\right)$, $i=1 \cdots n$. The tail of the distribution (the extreme values) can be defined as the threshold exceedances $x_{u}=x_{i}>u$ over a threshold $u$. If the threshold $u$ is "large" enough, the tail distribution can be approximated by generalized Pareto distribution given by

$$
y=\left[1+\xi\left(\frac{\mathrm{x}_{i}-\mathrm{u}}{\sigma}\right)\right]^{-\frac{1}{\xi}} ; i=1, \cdots, n
$$

where, $\sigma \in(0, \infty)$ and $\xi \in(-\infty, \infty)$ are the scale and shape parameters, respectively, of the generalized Pareto distribution.

### 2.4. Multivariate peak-over threshold model

Multivariate peak-over threshold makes use of Sklar's theorem that describes the relationship between multivariate distribution functions and their univariate margins (Sklar, 1959). Mathematically, it expresses that for a $d$-dimensional joint distribution function $F$ with margins $F_{1}\left(w_{1}\right), \cdots, F_{d}\left(w_{d}\right)$ where $F_{\mathrm{j}}$ are continuous, there exists a unique $d$-dimensional copula function $C$ with uniform margins on $(0,1)$ such that

$$
F(\boldsymbol{x})=C\left[F_{1}\left(w_{1}\right), \cdots, F_{d}\left(w_{d}\right)\right], \boldsymbol{x}=\left\{x_{1}>w_{1}, \cdots, x_{d}>w_{\mathrm{d}}\right\} \in \mathbb{R}^{d}
$$

The Extreme Value (EV) Copula family is exclusively meant for modelling the dependence structure of extreme values (the dependence in the upper tail of the distribution) (Nelsen, 2007). In the peak-over threshold approach, the margins are approximately generalized extreme value (GEV) distributed for large enough thresholds, while the dependence can be modelled using any suitable extreme value copula with non-degenerate margins (Beirlant et al., 2006). The most popular copula is the Gumbel-Hougaard Copula, also known as the multivariate logistic extreme value distribution. The distribution function for a $d$-dimensional multivariate logistic extreme value distribution is given as

$$
F(\boldsymbol{x})=\exp \left\{-\left(\sum_{j=1}^{d}\left(-\log y_{j}\right)^{\theta}\right)^{1 / \theta}\right\} ; \theta \in[1, \infty), j=1, \cdots, d
$$

where, $\theta \in[1, \infty)$ is the measure of the degree of dependence, ranging from independence $(\theta=1)$ to complete dependence $(\theta \rightarrow \infty)$.

### 2.5. Threshold selection

In peak-over threshold analysis, threshold selection is essential because the generalized Pareto distribution is only valid for approximating the unknown distribution of extremes in the asymptotic case. Thus, choosing a low threshold for defining the extremes will result in ordinarily expected values characterized as extremes that will violate the basis of the above asymptotic approximation. Alternatively, a very high threshold will lead to an inadequate number of exceedances for modelling. Therefore, a threshold needs to be selected as low as possible, subject to the condition that the limit provides a reasonable generalized Pareto approximation (Coles, 2001).

For the univariate margins, the validity of the generalized Pareto approximation can be checked based on two graphs: the Mean Residual Life Plot and Threshold Stability Plot. If the generalized Pareto distribution is valid for threshold exceedances over $u_{0}$, then it should be equally valid for excesses over all thresholds $u>u_{0}$ subject to the appropriate change of scale parameter $\sigma_{u}$ (Coles, 2001) and the shape parameter $\xi$ is independent of the threshold. Thus, for $u>u_{0}$, the mean of threshold excesses $\mathrm{E}(x-u \mid x>u)$ is a linear function of $u$, and the Mean Residual Life plot should be linear above the appropriate threshold. The Threshold Stability plot checks that in case the GP approximation is valid for threshold exceedances over $u_{0}$, then the reparametrized scale parameter $\sigma^{*}=\sigma_{u}-\xi u$ and the shape parameter $\xi$ are both constant for any threshold $u>u_{0}$ after allowing for variability due to sampling errors. Thus, these two graphs can be used as a guidance for selecting a suitable threshold. The final thresholds were iteratively obtained through model estimation based on improvements in Akaike Information Criterion (AIC) values and the estimated crash frequencies (Cavadas et al., 2020).

### 2.6. Crash frequency-by-severity estimation

For extreme value analysis, the modified time-to-collision (MTTC) and proportion of stopping distance (PSD) values are transformed by taking their negated values to transform the problem from a minima estimation to maxima one. Thus, if negated MTTC, negated PSD, or both increase to zero, a crash is expected. The deceleration rate to avoid a crash (DRAC) owing to its nature remains untransformed, and a crash becomes more likely if the DRAC value is greater than or equal to the maximum available deceleration rate (MADR) for a vehicle. For crash severity indicator Delta-V, Arun et al. (2021a) computed a threshold of approximately $16 \mathrm{~m} / \mathrm{s}$ to distinguish between severe and non-severe crashes based on the Delta-V-crash severity relationship developed by Bahouth et al. (2014). Crash severity was defined based on the widely used Abbreviated Injury Scale (AIS), where crashes with a severity higher than the Maximum Abbreviated Injury Scale value of 3 (MAIS3+) were defined as severe, and those with a lower value were defined as nonsevere. The crash frequencies can be calculated using these relationships and the threshold exceedance probability estimations from the extreme value theory. Please note that MTTC denotes negated MTTC, and PSD denotes negated PSD in the subsequent discussion.

In the univariate case, the total crash probability is simply the crash threshold exceedance probability of the variable, which can be obtained by subtracting the value of the distribution function from 1. However, in the multivariate case, a crash is obtained when either variable exceeds its threshold. Thus, in the multivariate case, the crash probability is the union of exceedance probabilities of the variables calculated as the difference of the value of the joint distribution function from 1. Mathematically, the generalized formula of total crash probability estimation can be given as below:

$$
R=1-F^{d}\left(w^{d}\right)
$$

where, $R$ is the crash risk measure (total crash probability), and $F^{d}$ is the joint distribution function of the $d$-dimensional vector of crash frequency indicators $w^{d}$. In the degenerate case, $F$ in Eq. (6) is the distribution function of the univariate vector. The exact formulae for each case (univariate, bivariate, trivariate) are presented in the appendix.

For crash probabilities by severity, the quantity of interest is the conditional probability of obtaining $\Delta v=\Delta v^{*}$ given a crash has happened $\left(\operatorname{Pr}\{\operatorname{Severe} \mid \operatorname{Crash}\}=\operatorname{Pr}\left\{\Delta v^{*} \mid \operatorname{Crash}\right\}\right)$. The crash probability is the total crash probability (the sum of severe and non-severe crash probability), computed per the formulae given above. Thus, the problem is finding the intersection of the exceedance probability of $\Delta v$ and the total crash probability. Mathematically, the generalized formula of total crash probability estimation can be given as below:

$$
S=F(\Delta v)+F^{d}\left(w^{d}\right)-F^{d, \Delta v}\left(w^{d}, \Delta v\right)
$$

where, $S$ is the severe crash probability, $F(\Delta v)$ is the univariate distribution function of the severity indicator $\Delta v, F^{d}$ carries the same meaning as in Eq. (4), and $F^{d, \Delta v}$ is the joint distribution function of the crash frequency and severity indicators. The probability of nonsevere crashes is calculated as the difference between the probabilities of total crashes and severe crashes. The derivation of the above equation and crash frequency by severity formulae for the different cases (bivariate, trivariate, and quadrivariate) are given in the appendix.

The frequencies of total $\left(N_{\text {Total }}\right)$ and severe $\left(N_{\text {Severe }}\right)$ crashes are calculated as the inflation of their respective probability values from the period of conflict observation $t$ to the longer period $T$ for which crashes are being estimated, which is typically one year $(T=1)$ yielding annual crash frequency estimates. The frequency of non-severe crashes $\left(N_{\text {Non-sever }}\right)$ is the difference between the total and severe crashes. The Eqs. (8), (9), and (10) give the formulae for calculating the total, severe, and non-severe crash frequencies, respectively:

$$
\begin{aligned}
& N_{\text {Total }}=\frac{T}{t} \times R \\
& N_{\text {Severe }}=\frac{T}{t} \times S \\
& N_{\text {Non-svever }}=N_{\text {Total }}-N_{\text {Sever }}
\end{aligned}
$$

Finally, for comparisons to observed crashes, Songchitruksa and Tarko (2006) introduced Poisson Confidence Intervals constructed over the observed crash frequency values, as shown in Eq. (11).

$$
\left\{\lambda: \frac{1}{2 T} \chi_{2 y_{0}, 1-\alpha / 2}^{2} \leq \lambda \leq \frac{1}{2 T} \chi_{2\left(y_{0}+1\right), \alpha / 2}^{2}\right\}
$$

where, $y_{0}$ is the observed crash frequency in time period $T, \lambda$ is the estimated crash frequency for time period $T$, and $\alpha$ is the level of significance. This study compares the estimated crash frequency values from the multivariate extreme value models with the estimated Poisson Confidence intervals for model validation.

## 3. Data

The data used in this study were collected in August and November 2019 from three four-legged signalized intersections in Brisbane, Australia. The primary data consisted of video recordings of traffic movement from a dedicated overhead camera assembly mounted on a $6.5-\mathrm{m}$ high mast installed at the intersections. For covering all the targeted road user movements at the intersections, two cameras with two views from each camera on different days of recordings were used for each intersection. The video traffic observations were conducted for four consecutive weekdays (Tuesday to Friday inclusive). Table 1 details the study intersections and the data collection schedule, while Fig. 4 shows a plan view of one of the intersections (Kessels Rd - Logan Sub-Arterial Rd intersection) and the camera placement and intersection areas covered in the camera views. One camera mast was placed on the pedestrian refuge island at the corner of Logan Road (North) and Kessels Road, while the other camera mast was placed on the median of the Logan Road (South) (Fig. 4). Each camera captured two different views (the shaded areas), as illustrated in Fig. 4. Similarly, the traffic movements

Table 1
Details of study intersections and the data collection schedule.
| Intersection name | Camera Number | Camera position | Data Collection | Total Duration |
| :--- | :--- | :--- | :--- | :--- |
| Beaudesert Rd - Granard Rd (BG) Intersection | 1 | View 1 | 20/08/2019 (Tuesday; 6 am to 6 pm) 21/08/2019 (Wednesday; 6 am to 6 pm) | 24 h |
|  |  | View 2 | 22/08/2019 (Thursday; 6 am to 6 pm) 23/08/2019 (Friday; 6 am to 6 pm) | 24 h |
|  | 2 | View 1 | 20/08/2019 (Tuesday; 6 am to 6 pm) 21/08/2019 (Wednesday; 6 am to 6 pm) | 24 h |
|  |  | View 2 | 22/08/2019 (Thursday; 6 am to 6 pm) 23/08/2019 (Friday; 6 am to 6 pm) | 24 h |
| Kessels Rd - Logan Rd (KL) Intersection | 1 | View 1 | 20/08/2019 (Tuesday; 6 am to 6 pm) 21/08/2019 (Wednesday; 6 am to 6 pm) | 24 h |
|  |  | View 2 | 22/08/2019 (Thursday; 6 am to 6 pm) 23/08/2019 (Friday; 6 am to 6 pm) | 24 h |
|  | 2 | View 1 | 20/08/2019 (Tuesday; 6 am to 6 pm) 21/08/2019 (Wednesday; 6 am to 6 pm) | 24 h |
|  |  | View 2 | 22/08/2019 (Thursday; 6 am to 6 pm) 23/08/2019 (Friday; 6 am to 6 pm) | 24 h |
| Appleby Rd - Stafford Rd (AS) Intersection | 1 | View 1 | 12/11/2019 (Tuesday; 6 am to 6 pm) 13/11/2019 (Wednesday; 6 am to 6 pm) | 24 h |
|  |  | View 2 | 14/11/2019 (Thursday; 6 am to 6 pm) 15/11/2019 (Friday; 6 am to 6 pm) | 24 h |
|  | 2 | View 1 | 12/11/2019 (Tuesday; 6 am to 6 pm) 13/11/2019 (Wednesday; 6 am to 6 pm) | 24 h |
|  |  | View 2 | 14/11/2019 (Thursday; 6 am to 6 pm) 15/11/2019 (Friday; 6 am to 6 pm) | 24 h |


![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-09.jpg?height=1013&width=1537&top_left_y=177&top_left_x=175)
Fig. 4. Camera positions and views from the cameras at the Logan Rd - Kessels Rd Intersection.

data were collected at the other two intersections.
The raw video data were then processed using an automated traffic conflict extraction method, which typically consists of six main procedures: camera calibration, object detection and tracking, prototype generation, prototype matching, event generation, and conflict identification. The system developed at the Queensland University of Technology used the YOLOv3 algorithm for road user detection and the Deep SORT algorithm for tracking them. YOLOv3 ('You only look once') is a fast and accurate single-step algorithm that uses only forward propagating convolutional neural networks for real-time object detection (Farhadi and Redmon, 2018). It first divides the image into a grid-like structure, detecting objects within each grid cell. The objects in a grid cell are captured within initial bounding boxes, and logistic regression is then used to predict the object's height, width, and center and assign class probabilities to the objects within each bounding box. The class probabilities help classify the objects into various road users. Given that there could be multiple bounding boxes surrounding one object, the algorithm uses an Intersection Over Union approach to ensure that the predicted bounding boxes capture the identified object. The off-the-shelf YOLOv3 was further trained on a subset of the data collected in this study to accurately identify very large road users like articulated buses that may span across several frames and smaller road users such as motorcyclists that could be difficult to distinguish from similar road users such as bicyclists and pedestrians from a height of 6.5 m.

The detected objects are then passed onto the Deep SORT ('Simple online and real-time tracking') algorithm (Wojke et al., 2017). The SORT algorithm implements Kalman filtering to model the state of each tracked object as a vector of the bounding box center, box scale, box aspect ratio, and their time derivatives. In the final step, the SORT algorithm uses the Hungarian algorithm to associate the predicted states from Kalman filtering and the newly detected bounding box in the current frame with the old object tracks in the

Table 2
Descriptive statistics of the conflict measures.
| No. of rear-end conflicts | No. of severe rear-end crashes (2015-19) | No. of non-severe rear-end crashes (2015-19) | Conflict measures | Mean | Median | Std. Dev. | Minimum | Maximum |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 12,471 | 2 | 29 | MTTC | 1.123 | 0.999 | 0.548 | 0.006 | 2.867 |
|  |  |  | DRAC | 1.65 | 1.252 | 1.35 | 0.001 | 9.952 |
|  |  |  | PSD | 1.144 | 1.116 | 0.523 | 0.009 | 3.166 |
|  |  |  | Delta-V | 6.566 | 6.419 | 3.219 | 0.001 | 25.917 |


Notation:
MTTC: Modified Time-to-Collision; DRAC: Deceleration Rate to Avoid a Crash; PSD: Proportion of Stopping Distance; Delta-V: Expected Post-Collision Change in Vehicle's Velocity
Std. Dev.: Standard Deviation.
previous frame. The Deep SORT algorithm applies a trained convolutional neural network to solve the problem of the high number of identity switches in the basic SORT that helps increase robustness against object detection misses and occlusions in real-time tracking.

The overlapping of the predicted vehicle trajectories generates conflicts. All interactions with a time-to-collision value below 3 s are recorded as conflicts and are utilized in further analysis. The required traffic conflict indicators (modified time-to-collision (MTTC), deceleration rate to avoid a crash (DRAC), the proportion of stopping distance (PSD) and the expected post-collision change in velocity (Delta-V)) were subsequently calculated from the vehicle trajectories for the observed conflicts. To limit the scope of the study in the demonstration of the methodological approach, only the rear-end conflicts data were utilized for crash prediction modelling. The details of conflict observation and extraction systems can be found in Arun et al. (2021a).

Table 2 provides the descriptive statistics of the conflict measures used in this study for the combined dataset of the three intersections. The crash data presented in Table 2 are used to associate crash events with the multivariate extreme value models developed in this study. The five-year (2015-2019) crash data for the study intersections were provided by the Department of Transport and Main Roads, Queensland Government. The crash data's key information parameters were each crash's time, location, severity, road user information, and collision type. It was necessary to filter the crash data to correspond to the conditions under which the conflicts were observed for accurate comparisons with the crashes predicted by the peak-over threshold models. Hence, the crash data were filtered to include only the cases corresponding to the following criteria: the crashes that occurred during weekdays, during the daytime (between 6 am to 6 pm), and during fair weather conditions. As per the Queensland crash data, the crash severity classes are Minor Injury, Medical Treatment-Only, Hospitalization, and Fatality in the increasing order of severity. Following Arun et al. (2021a), fatal and hospitalization severity crashes were classified as severe (Maximum Abbreviated Injury Scale $\geq 3$; MAIS3+) crashes, while the minor injury and medical treatment-only crashes were classified as non-severe ones.

Table 3 gives the value of Kendall's correlation parameter (Tau, $\tau$ ) between the conflict indicator pairs. Table 3 indicates that the PSD indicator is significantly correlated with both MTTC and DRAC indicators. However, given that the three frequency indicators could be tail-independent, hence all the three indicators were further investigated for multivariate crash frequency-by-severity estimation. Crucially, all the crash frequency indicators have weak $(\tau<0.5)$ but statistically significant correlations ( p -value $<0.05$ ) with the crash severity indicator Delta-V. These weak correlations arise because the frequency and severity indicators measure fundamentally different properties of a crash. However, such statistically significant weak correlations are still potentially important for the Extreme Value models.

## 4. Results

This study estimated several univariate and multivariate models following the methodology explained in Section 2 to estimate the frequencies of the total, severe, and non-severe rear-end crashes. All the univariate and multivariate models were estimated using the maximum likelihood estimation. The log-likelihood function of the joint distributions is the summation of the log-likelihoods of the copula and the margins. The marginal values were censored in that only the threshold exceedances were used for likelihood estimation and transformed to a uniform distribution on the interval (0, 1) for fitting the copulas. The goodness-of-fit of the margins was examined by inspecting the probability and quantile plots, while the comparison between competing models was made using the Akaike Information Criterion (AIC) and log-likelihood values. The results of the estimation are given below. Please note that MTTC denotes negated MTTC, and PSD denotes negated PSD in the subsequent discussion.

### 4.1. Data declustering

The peak-over threshold models are sensitive to clustered data. If the conflicts are serially dependent (for example, cars behind one another braking hard to avoid crashing after the first one in the queue brakes), they violate the inherent assumption that the extreme events are independent of each other. Therefore, following Arun et al. (2021a), a runs-based clustering approach was adopted wherein the time-series data for each conflict measure was first chronologically arranged, and more than three successive values within 5 s lying above a chosen threshold were identified as belonging to a cluster. Then, only the maximum of the clustered observations was selected for subsequent analysis. The thresholds used for the indicators were -3.0 s for Modified Time-To-Collision (MTTC), $0.0 \mathrm{~m} / \mathrm{s}^{2}$ for Deceleration Required to Avoid a Crash (DRAC), and -1.0 for Proportion of Stopping Distance (PSD). These thresholds were chosen to

Table 3
Kendall's correlation parameter values of the conflict measures.
|  | Conflict Indicators |  |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  | MTTC | DRAC | PSD | Delta-V |
| MTTC | 1.000 |  |  |  |
| DRAC | -0.238 (<0.001) | 1.000 |  |  |
| PSD | 0.512 (<0.001) | -0.565 (<0.001) | 1.000 |  |
| Delta-V | 0.037 (<0.001) | 0.109 (<0.001) | -0.087 (<0.001) | 1.000 |


The correlation test $p$-values are given in the parentheses.
Notation:
MTTC: Modified Time-to-Collision; DRAC: Deceleration Rate to Avoid a Crash; PSD: Proportion of Stopping Distance; Delta-V: Expected Post-Collision Change in Vehicle's Velocity.
make the most efficient use of the data for each of these indicators.

### 4.2 Estimation of the margins

It is challenging to present plots for all the models, specifically for models with higher than three dimensions of data. Therefore, as an illustrative example, the 3-dimensional Modified Time-To-Collision (MTTC), Deceleration Required to Avoid a Crash (DRAC), and Delta-V model marginal and copula plots are produced below to explain the estimation process. All conflicts with negated MTTC > -3.0 s and DRAC $>0.0 \mathrm{~m} / \mathrm{s}^{2}$ were used in this model. Delta-V values were computed for the censored data. Fig. 5 illustrates the scatter of the trivariate vector. The positive correlation between the frequency indicators (Fig. 5) is evident in the plot, where conflicts with high negative MTTC values have high DRAC values. However, there is no apparent tail dependence between the frequency and severity indicators, with high Delta-V values occurring randomly throughout the variable space. This observation points to the possibility of independent copulas for modelling the joint distribution of the three variables, where the joint distribution function is simply the product of the marginal distribution functions. This aspect was then formally investigated by conducting a nonparametric test of extreme value dependence among the three variables (Bücher and Kojadinovic, 2015). The test statistic was computed as 0.118 with a $p$-value of 0.568, meaning that the study failed to reject extreme value dependence in the data. Thus, extreme value methods were used to model the marginal and joint distributions.

Threshold selection plots were used to select the appropriate thresholds for peak-over threshold analysis. Fig. 6 and Fig. 7 respectively present the Mean Residual Life (MRL) and Threshold Stability (TS) plots for the three variables. From these plots, the initial threshold ranges of the variables were inferred as (-0.6, -0.4) for MTTC, (1.6, 2.4) for DRAC, and (9, 10.5) for Delta-V. The final thresholds for the most optimal models were selected based on the iterative procedure described earlier using Akaike Information Criterion (AIC).

Fig. 8 presents the results of distribution fitting in terms of marginal distribution and quantile plots of the three variables. The marginal peak-over threshold distributions are seen to fit the data well even when extrapolated to crash-relevant thresholds, 0 s, 8.5 m/ $\mathrm{s}^{2}$ and $16 \mathrm{~m} / \mathrm{s}$, for MTTC, DRAC, and Delta-V, respectively. The results of the subsequent copula fitting are described in the next section.

### 4.3. Estimation of the copula structure

Continuing the illustrative example with trivariate Modified Time-To-Collision (MTTC), Deceleration Required to Avoid a Crash (DRAC), and Delta-V model, for estimating the crash frequency and crash frequency-by-severity according to the Eqs. (8), (9), and (10), the bivariate distributions between the frequency variables MTTC and DRAC, and a trivariate distribution of all three variables were required. Thus, Gumbel-Hougaard copulas (hereafter referred to as Gumbel copulas) were used to model these multivariate joint distributions and estimated using the maximum likelihood estimation method.

Figs. 9(a), 9(b), and 10 present the fit of the Gumbel copulas to the bivariate and trivariate joint distributions to that of the empirically estimated copulas. While the Gumbel copula provided a good fit to the data for the bivariate distribution of frequency indicators, the same was not observed in the trivariate joint distribution of frequency and severity indicators. Therefore, a formal goodness-of-fit test was conducted according to the method given by Kojadinovic et al. (2011) to test the null hypothesis that joint probability distribution from the estimated parametric copula is significantly different from the one obtained from an empirical copula. The alternate hypothesis practically means that the dependence among the modelled indicators is not significant, and inde-pendent copulas could characterize the joint distribution of the three variables. The chi-squared test statistic was estimated as 0.576 with an associated $p$-value of 0.001 , leading to rejection of the null hypothesis. However, the Gumbel copula was also considered for the trivariate distribution to maintain parity among the models.

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-11.jpg?height=576&width=727&top_left_y=1761&top_left_x=580)
Fig. 5. Scatterplot of the trivariate vector.

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-12.jpg?height=1592&width=1495&top_left_y=175&top_left_x=193)
Fig. 6. Mean Residual Life (MRL) plots of the three variables.

A similar exercise was followed for modelling the joint distributions of all the other combinations of traffic conflict indicators (MTTC-PSD, DRAC-PSD, and MTTC-DRAC-PSD). The results of the total, severe, and non-severe crash frequency estimations using the best overall frequency and frequency-by-severity prediction models are given in Tables 4 and 5, respectively.

### 4.4. Crash frequency estimation

Given that this paper aims to investigate the suitability of using multiple conflict indicators for estimating crash risks, a straightforward comparison between the efficiency of various models can be made using their crash prediction accuracy and precision.

As indicated in Table 4, all the models have a reasonable level of prediction accuracy. The estimated number of annual crashes falls within the 95\% Poisson confidence interval over observed annual crashes. Further comparisons were made using the mean absolute percentage error values, which indicated that the bivariate DRAC and PSD model (Mean Absolute Percentage Error, MAPE $=0.016 \%$ ) as well as the trivariate MTTC, DRAC, and PSD model (MAPE = 0.016\%) were the most accurate among all the crash frequency prediction models with the lowest prediction errors, closely followed by the bivariate MTTC and DRAC model (MAPE $=0.032 \%$ ). However, the precision of the estimates is also important, with the best prediction being the one where the prediction interval perfectly

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-13.jpg?height=1159&width=1543&top_left_y=175&top_left_x=173)
Fig. 7. Threshold Stability (TS) plots of the three variables.

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-13.jpg?height=828&width=1537&top_left_y=1447&top_left_x=177)
Fig. 8. Probability-Probability (top row) and Quantile-Quantile (bottom row) plots for the three marginal vectors.

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-14.jpg?height=681&width=1302&top_left_y=175&top_left_x=292)
Fig. 9. Comparison between the fitted Gumbel-Hougaard Bivariate Copula and Empirical Copula for a) Modified Time-to-Collision (MTTC) and Deceleration Rate to Avoid a Crash (DRAC), and b) Modified Time-to-Collision (MTTC) and Delta-V models.

![](https://cdn.mathpix.com/cropped/086daacf-7c90-4aa7-97f8-cee3094cafc1-14.jpg?height=727&width=1491&top_left_y=1011&top_left_x=197)
Fig. 10. Comparison between the fitted Gumbel-Hougaard Trivariate Copula and Empirical Copula for Modified Time-to-Collision (MTTC), Deceleration Rate to Avoid a Crash (DRAC), and Delta-V conditioned on (transformed) Delta-V values.

overlaps the Poisson confidence interval over the observed crashes. Using this criterion, the bivariate MTTC and DRAC model was the best performing model, as it had a minimal prediction error and the prediction interval closely approximated the observed confidence interval. The trivariate MTTC, DRAC, and PSD model (MAPE = 0.016\%) had the lowest error, but its prediction interval was wider than the observed confidence interval compared to the bivariate MTTC and DRAC model. In addition, having one less indicator, the bivariate MTTC and DRAC model was more parsimonious than the trivariate model. Among the univariate models, DRAC had the best crash prediction with minimal error (MAPE $=0.613 \%$ ), and its prediction interval also approximately coincided with the observed confidence interval.

### 4.5. Crash frequency-by-severity estimation

Given the good performance of the MTTC and DRAC combination in accurately predicting overall crash frequency, it was expected that the same combination would provide the best crash frequency-by-severity estimates as well when combined with the Delta-V indicator. However, the results from Table 5 indicate that was not the case. The bivariate DRAC and Delta-V model was the best performing model as reflected by the lowest prediction errors and the narrowest prediction intervals for severe and non-severe crash

Table 4
Best performing crash frequency prediction models.
| Parameter | Conflict Indicator Combinations |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | MTTC | DRAC | PSD | MTTC, DRAC | MTTC, PSD | DRAC, PSD | MTTC, DRAC, PSD |
| Marginals | 0.126 (0.006) | - | - | 0.238 (0.004) | 0.161 (0.005) | - | 0.213 (0.005) |
|  | -0.019 (0.034) | - | - | -0.29 (0.01) | -0.128 (0.023) | - | -0.266 (0.014) |
|  | -0.5 | - | - | -0.74 | -0.58 | - | -0.68 |
|  | 1206 | - | - | 3816 | 1843 | - | 2675 |
|  | - | 1.008 (0.022) | - | 1.008 (0.022) | - | 1.786 (0.037) | 1.692 (0.037) |
|  | - | 0.252 (0.018) | - | 0.252 (0.018) | - | -0.005 (0.014) | 0.023 (0.016) |
|  | - | 1.34 | - | 1.34 | - | 1.13 | 1.28 |
|  | - | 5678 | - | 5678 | - | 4490 | 4233 |
|  | - | - | 0.142 (0.012) | - | 0.144 (0.009) | 0.107 (0.007) | 0.226 (0.006) |
|  | - | - | -0.368 (0.069) | - | -0.296 (0.047) | -0.209 (0.045) | -0.384 (0.016) |
|  | - | - | -0.3 | - | -0.35 | -0.33 | -0.56 |
|  | - | - | 453 | - | 667 | 505 | 1836 |
| Dependence | - | - | - | 1.23 (0.01) | 1.688 (0.032) | 1.903 (0.023) | 1.546 (0.012) |
|  | - | - | - | 6894 | 1883 | 4512 | 4662 |
| Log-likelihood | 1312.472 | -7152.63 | 598.581 | 427.668 | 481.822 | 1490.554 | 2123.296 |
| Akaike Information Criterion (AIC) | -2620.944 | 14309.26 | -1193.162 | -853.337 | -961.645 | -2979.108 | -4244.593 |
| Observed $N_{\text {Total }}$ (95\% Confidence Interval) | 6.2 (4.213-8.8) |  |  |  |  |  |  |
| Estimated $N_{\text {Total }}$ (95\% Confidence Interval) | 5.892 | 6.162 | 6.013 | 6.202 | 6.160 | 6.199 | 6.201 |
|  | (1.574-12.537) | (4.337-8.287) | (0-32.428) | (4.337-8.624) | (0.657-21.760) | (3.519-14.935) | (3.862-9.908) |
| Mean Absolute Percentage Error (\%) | 4.967 | 0.613 | 3.016 | 0.032 | 0.645 | 0.016 | 0.016 |


Notations:
MTTC: Modified Time-to-Collision; DRAC: Deceleration Rate to Avoid a Crash; PSD: Proportion of Stopping Distance
$\boldsymbol{N}_{\text {Total }}$ : Number of total crashes
$\left(\widehat{\boldsymbol{\sigma}}_{z}, \widehat{\boldsymbol{\xi}}_{z}, \boldsymbol{u}_{z}\right)$ are the marginal scale, shape, and threshold parameters for a given conflict indicator $\boldsymbol{z} \in\{\boldsymbol{M}$ TTC,DRAC,PSD $\} ; \widehat{\theta}$ is the Copula dependence parameter
ME $_{z}$ : Marginal Exceedances of the conflict threshold of the given conflict indicator $z \in\{$ MTTC, DRAC, PSD $\}$
JE: Joint Exceedances of the conflict thresholds of the given conflict indicator combination
SE: Standard Error.

Table 5
Best performing crash frequency-by-severity prediction models.
| Parameter | Conflict Indicator Combinations |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | MTTC, $\boldsymbol{\Delta} \boldsymbol{v}$ | DRAC, $\Delta \boldsymbol{v}$ | PSD, $\Delta \boldsymbol{v}$ | MTTC, DRAC, $\Delta \boldsymbol{v}$ | MTTC, PSD, $\Delta \boldsymbol{v}$ | DRAC, PSD, $\Delta \boldsymbol{v}$ | MTTC, DRAC, PSD, $\boldsymbol{\Delta} \boldsymbol{v}$ |
| Marginals | 0.118 (0.006) | - | - | 0.173 (0.002) | 0.122 (0.007) | - | 0.105 (0.01) |
|  | -0.008 (0.042) | - | - | -0.242 (0.002) | -0.024 (0.047) | - | -0.007 (0.072) |
|  | -0.47 | - | - | -0.72 | -0.49 | - | -0.52 |
|  | - | 1.793 (0.07) | - | 1.793 (0.07) | - | 1.681 (0.08) | 2.218 (0.084) |
|  | - | -0.119 (0.03) | - | -0.118 (0.03) | - | 0.009 (0.036) | -0.13 (0.025) |
|  | - | 2.72 | - | 2.71 | - | 1.35 | 0.72 |
|  | - | - | 0.107 (0.021) | - | 0.132 (0.015) | 0.054 (0.01) | 0.045 (0.009) |
|  | - | - | -0.409 (0.164) | - | -0.445 (0.098) | -0.019 (0.145) | 0.086 (0.165) |
|  | - | - | -0.22 | - | -0.26 | -0.26 | -0.25 |
|  | 5.264 (0.185) | 5.778 (0.144) | 3.674 (0.528) | 5.253 (0.011) | 4.023 (0.167) | 2.51 (0.104) | 2.717 (0.098) |
|  | -0.211 (0.012) | -0.242 (0.007) | -0.083 (0.087) | -0.225 (0.000) | -0.166 (0.017) | -0.075 (0.027) | -0.101 (0.023) |
|  | 2.42 | 2.58 | 7.9 | 2.64 | 5.0 | 9.27 | 9.19 |
| Dependence | 1.028 (0.021) | 1.019 (0.012) | 1.007 (0.087) | 1.029 (0.006) | 1.172 (0.022) | 1.107 (0.015) | 1.149 (0.012) |
|  | 869 | 1633 | 76 | 3459 | 677 | 997 | 1260 |
| Log-likelihood | 0.993 | 1.529 | 0.004 | 15.372 | 54.118 | 39.008 | 148.206 |
| Akaike Information Criterion (AIC) | 0.014 | -1.058 | 1.993 | -28.745 | -106.237 | -76.016 | -294.413 |
| Observed $N_{\text {Severe }}(95 \% \mathrm{CI})$ | 0.4 (0.048-1.445) |  |  |  |  |  |  |
| Estimated $N_{\text {Severe }}(95 \% \mathrm{CI})$ | 0.419 | 0.404 | 0.401 | 0.408 | 0.426 | 0.476 | 0.418 |
|  | (0.013-1.797) | (0.033-1.374) | (0-22.064) | (0.104-0.843) | (0.176-1.638) | (0.316-1.46) | (0.259-1.45) |
| MAPE for $N_{\text {Severe }}$ (\%) Observed $N_{\text {Non-severe }}(95 \% \mathrm{CI})$ | 4.75 | 1.0 | 0.25 | 2.0 | 6.5 | 19.0 | 4.5 |
|  |  |  |  |  |  |  |  |
|  | (1.15-12.825) | (1.516-11.844) | (0-44.395) | (1.457-12.385) | (0.361-44.186) | (1.125-30.455) | (0.379-36.601) |
| MAPE for $N_{\text {Non-severe }}$ (\%) | 0.052 | 0.017 | 41.035 | 0.155 | 1.69 | 1.69 | 0.0 |


MTTC: Modified Time-to-Collision; DRAC: Deceleration Rate to Avoid a Crash; PSD: Proportion of Stopping Distance; $\Delta v$ : post-collision change in velocity (Delta-V) $\boldsymbol{N}_{\text {Severe }}$ : Number of severe (MAIS3+) crashes; $\boldsymbol{N}_{\text {Non-severe }}$ : Number of non-severe (MAIS < 3) crashes $\left(\widehat{\boldsymbol{\sigma}}_{z}, \widehat{\boldsymbol{\xi}}_{z}, \boldsymbol{u}_{z}\right)$ are the marginal scale, shape, and threshold parameters for a given conflict indicator $\boldsymbol{z} \in\{\boldsymbol{M}$ TTC,DRAC,PSD, $\Delta \boldsymbol{v}\} ; \widehat{\theta}$ is the Copula dependence parameter JE: Joint Exceedances of the conflict thresholds of the given conflict indicator combination; SE: Standard Error; MAPE: Mean Absolute Prediction Error.
frequencies. The trivariate MTTC, DRAC, and Delta-V model also provided accurate predictions of severe and non-severe crashes. However, its severe crash frequency prediction interval was very narrow compared to the observed confidence interval, suggesting that the model did not accurately capture the underlying crash-generating process.

Among other models, all of them, except the trivariate MTTC, PSD, and Delta-V and the DRAC, PSD, and Delta-V models had good prediction accuracy with prediction errors of less than $5 \%$ for both severe $\left(N_{\text {Severe }}\right)$ and non-severe $\left(N_{\text {Non-severe }}\right)$ crashes. The highest dimensional quadrivariate model, including all the four conflict indicators, namely MTTC, DRAC, PSD, and Delta-V, also accurately predicted both severe and non-severe crash frequencies, but the prediction interval of non-severe crashes was quite wide. These results highlight that accuracy improvement of both overall crash frequency and crash frequency-by-severity prediction models may not be necessarily proportional to the number of indicators included in the models. In fact, indiscriminate inclusion of indicators may adversely affect the model performance.

From Table 5, for severe crashes, the bivariate PSD and Delta-V model seems the most accurate with the lowest prediction error (0.25\%), but it has a substantial prediction error associated with non-severe crashes (41.035\%), which makes it non-ideal for crash frequency-by-severity prediction. The poor performance of the PSD and Delta-V bivariate model may be that the chosen Gumbel-Hougaard Copula is not suitable for this indicator combination. Indeed, when testing the goodness-of-fit of the Gumbel-Hougaard Copula for the PSD and Delta-V data, the chi-squared test statistic was 0.049 with a statistically non-significant p-value of 0.014 (<0.05), indicating its unsuitability. For comparison, the chi-squared test statistic was 0.029 with a p-value of 0.23 (>0.05) for the bivariate DRAC and Delta-V model using the Gumbel-Hougaard copula.

The inclusion of the PSD indicator generally led to a loss of precision in the crash frequency-by-severity models. This result may be because the PSD indicator was correlated with both the other crash frequency indicators and was, therefore, capturing redundant safety information already captured by the other indicators. These observations are further discussed in detail below.

## 5. Discussion

Following the trend of recent literature (Arun et al., 2021c) that has used multivariate extreme value modelling approach for crash frequency estimation, this study investigated the effect of multiple conflict indicators in estimating crash frequency-by-severity through copula-based extreme value modelling. Specifically, this study investigated whether higher dimensionality (more than two indicators) in multivariate crash frequency-by-severity prediction models will result in more accurate and precise estimates. Given that emerging technologies like adaptive traffic signal control and connected-and-automated vehicles can benefit from meaningful crash-conflict relationships, the study also identified the best conflict indicators that can accurately predict the frequency of total, severe (maximum abbreviated injury scale $\geq 3$; MAIS3+), and non-severe rear-end crashes at signalized intersections.

Using intersection data from Brisbane, Australia, the study results revealed that using higher-dimensional conflict datasets may not be proportional to improvements in the crash prediction performance of the extreme value models. The bivariate Modified Time-To-Collision (MTTC) and Deceleration Required to Avoid a Crash (DRAC) model had comparable prediction accuracy and precision for total crash frequency estimation while being more parsimonious than the higher dimensional trivariate model that included all three frequency indicators. This observation highlights the utility of capturing the different aspects of a traffic conflict, namely, the op-portunity available for a road user to react to an emerging threat (represented by MTTC) and the mechanical capability of the vehicle to carry out the evasive response (represented by DRAC).

Indeed, the MTTC and DRAC combination was also a good indicator of crash frequency-by-severity in conjunction with Delta-V, given the low mean absolute percentage errors and narrow prediction intervals of the severe and non-severe crash estimates. However, as indicated in Table 5, the bivariate DRAC and Delta-V model also had a good prediction performance, with low mean absolute percentage errors and narrow prediction intervals. Indeed, the prediction intervals of the latter bivariate model coincided better with the observed Poisson confidence intervals, which represent the naturally expected variability in observed mean crash frequency due to unobserved factors given that the crashes were observed over 5 years. Thus, the more parsimonious bivariate DRAC and Delta-V model could be preferred over the higher dimensional MTTC, DRAC, and Delta-V model.

A reason for the reduced performance of higher dimensional models could be the high correlation of Proportion of Stopping Distance (PSD) indicator with the other two frequency indicators, meaning that including the PSD indicator only captured redundant information already being captured by the other indicators. Zheng et al. (2019a) had a similar observation where they found that higher correlation among indicators led to higher prediction error in multivariate extreme value models. Thus, without careful preanalysis of conflict indicators, higher-dimensional multivariate analysis can result in unsatisfactory prediction performance while increasing the estimation complexity.

This study highlighted the advantage of crash frequency-by-severity estimation over simple overall crash frequency estimation that has been typically followed in conflict studies. The overall prediction errors of the trivariate MTTC, DRAC and Delta-V model and the bivariate DRAC and Delta-V model were comparable for estimating crash frequency-by-severity. Thus, in crash frequency-by-severity estimation, additional information regarding the crucial severity aspect is uncovered with acceptable overall prediction accuracy using the same number of indicators.

The study results also showed that the Proportion of Stopping Distance (PSD) indicator could provide accurate but somewhat imprecise estimates of total crash frequency through extreme value modeling. However, it is not suitable for estimating crash frequency-by-severity with the Delta-V indicator. A possible reason could be model misspecification since the Gumbel-Hougaard copulas were used uniformly to maintain parity across all the models in this study. Thus, testing PSD with another copula specification or in combination with any other severity indicator like acceleration severity index (ASI) could be possible future research directions.

A crucial implication of the study results is regarding the conflict thresholds of the indicators. Typically, the studies have adopted a threshold of $3.4 \mathrm{~m} / \mathrm{s}^{2}$ for DRAC, which is the recommended deceleration rate for stopping sight distance calculation (AASHTO, 2018). However, this study found that the DRAC thresholds for rear-end conflicts range between 0.72 and $2.72 \mathrm{~m} / \mathrm{s}^{2}$. This discrepancy means that studies adopting a higher DRAC threshold could be failing to incorporate significant crash-relevant information available in traffic interactions with lower DRAC values. For instance, Xie et al. (2019) investigated optimal thresholds of three conflict indicators, including DRAC, using real-world connected vehicle data and found that the DRAC threshold of $3.0 \mathrm{~m} / \mathrm{s}^{2}$ was the highest correlated to observed crashes, but the value of the correlation coefficient was relatively low (0.39). The contentious issue is that they only investigated the range of DRAC thresholds between $2.0 \mathrm{~m} / \mathrm{s}^{2}$ and $4.5 \mathrm{~m} / \mathrm{s}^{2}$, which means that they did not test lower DRAC thresholds that could have had a higher and more meaningful correlation with crashes, as shown in this study. On the other hand, in the case of MTTC, Ozbay et al. (2008) had suggested a threshold of 4.0 s, reasoning that their simulation environment did not represent an actual crash environment because the simulated drivers were not affected by distractions and misjudgements. However, subsequent research has consistently found that conflicts with lower MTTC thresholds are more highly correlated to crashes at intersections (Zheng and Sayed, 2019b; Zheng and Sayed, 2019a). The negated MTTC threshold values in this study range between -0.47 and -0.74 s. Thus, in the case of MTTC, using a higher 4.0 s threshold at signalized intersections can potentially decrease the conflicts' correlation with crashes and mitigate the safety benefits expected from a conflict-based evaluation.

It is also important to acknowledge the effect of the longer duration of conflict observations on the accuracy and precision of crash estimates. Extreme value models are extremely data-hungry, and previous studies have noted that the low accuracy and precision of the crash estimates could be an outcome of the low conflict observation durations (Zheng et al., 2019b). On the other hand, this study observed conflicts for 24 h (12 h each for two days), which consequently yielded a significantly higher number of joint threshold exceedances (extreme conflicts in all margins) than similar previous studies (Zheng et al., 2019; Zheng and Sayed, 2019c). As a result, the crash estimates from most models were highly accurate. More importantly, the prediction intervals in this study also closely coincided with the observed confidence intervals, often becoming the major point of distinction between competing models from different conflict indicator combinations. This result is similar to that obtained by Zheng and Sayed, 2019c, where the prediction intervals of the Bivariate Time-to-Collision and Post-Encroachment Time peak-over threshold model estimated for conflicts observed for 15-17 h were also relatively narrow.

## 6. Summary and conclusions

Improved models of crash-risk estimation using traffic conflict indicators could hasten the real-world implementation of various emerging technologies by quickly providing valuable safety information without having to wait for the accumulation of crashes. An obvious example would be the introduction of autonomous vehicles and how human drivers interact with these vehicles over time in real-time. Traffic conflict indicators (collected in real-time) could provide valuable safety information that could be used to alter autonomous vehicle behavior and study how the driving behavior of humans adjusts to the presence of autonomous vehicles over time (Mannering et al., 2018). Indeed, traffic-conflict indicators are likely to play a fundamental role in the safety evaluation of emerging technologies.

This study investigated the application of traffic conflict methods in jointly predicting rear-end crash frequency and severity at signalized intersections through multivariate extreme value modelling using copulas. Candidate conflict indicators were carefully selected from different families of conflict indicators (Fig. 2) to minimize capturing the same information regarding the underlying crash generating process by the various indicators. Thus, four candidate indicators, namely, Modified Time-To-Collision (MTTC, temporal proximity), Proportion of Stopping Distance (PSD, spatial proximity), Deceleration Required to Avoid a Crash (DRAC, kinematic), and the expected post-collision change in velocity (Delta-V, crash severity), were selected and analyzed using multivariate copulas. While MTTC and PSD represent the proximities of conflicting vehicles in temporal and spatial dimensions, DRAC represents the opportunity for evasive action available to a conflicting vehicle, and Delta-V captures the scale of outcome severity in case of an eventual collision. A multivariate Peak-Over Thresholds approach was adopted where the margins were modelled using Generalized Pareto Distributions, and the dependence structure was modelled using extreme value Gumbel-Hougaard copulas. Significantly, the study formulated a generalized method of predicting the frequency of severe and non-severe crashes from multiple conflict indicators. The data for validating the study hypotheses were collected from three four-legged signalized intersections in Brisbane using an automated conflict extraction method.

The study results indicate that including more than one crash frequency indicator in overall crash frequency estimation can improve the accuracy and precision of the estimates; however, this improvement may not be proportional to the number of modelled indicators. Both the bivariate and trivariate models yielded better estimates than the univariate models, but the bivariate MTTC and DRAC model provided slightly more precise estimates than the trivariate MTTC, DRAC, and PSD model, with comparable accuracy. Indeed, MTTC and DRAC together are consistent estimators of both total crash frequency and crash frequency-by-severity, as they yielded accurate and precise estimates of both severe and non-severe crashes when combined with the crash severity indicator Delta-V. In the case of the crash frequency-by-severity models, it was again observed that the improvements in prediction performance were not proportional to the dimensionality of the multivariate conflict data, and the more parsimonious DRAC and Delta-V bivariate model yielded comparable estimates to the trivariate MTTC, DRAC, and Delta-V, and both outperformed the full specification quadrivariate MTTC, DRAC, PSD, and Delta-V model. Thus, including more traffic conflict indicators in safety evaluations may not always be advantageous. In addition to theoretical considerations, practical aspects like correlations among conflict indicators should be carefully investigated as they could reduce the crash prediction performance of the multivariate models.

A crucial takeaway from this study is the demonstration of the superiority of crash frequency-by-severity estimation from conflict
indicators over simple crash frequency estimation, which has far-reaching implications regarding the confidence in the applicability of traffic conflict analysis. As argued elsewhere, a significant drawback of many past conflict studies has been their focus on total crashes (regardless of severity), since overlooking the severity of crashes in conflict-based safety assessment can result in safety measures that may reduce the frequency of crashes but increase the severity of the crashes (Arun et al., 2021b). The generalized crash frequency-byseverity prediction models developed in this study have the potential to significantly improve the functioning of active vehicle safety technologies (such as adaptive cruise control (ACC) and automated emergency braking (AEB)), which form the backbone of the upcoming connected-and-automated vehicle revolution. They can also broaden the scope of infrastructure-based real-time systems proposed for safety monitoring of traffic operations (Essa and Sayed, 2020; Zheng and Sayed, 2020) that can further aid the safe deployment of connected-and-automated vehicles.

The work done in this study is not without limitations and can be extended to address these limitations in the future. There are a least five points worthy of mention. First, this study did not consider non-stationarity in the conflict indicator extremes, as it was not central to the topic of investigation. Temporal trends might be present in conflict extremes, which could be addressed in future research. More importantly, considering temporal and spatial characteristics such as traffic volumes and compositions in model estimation will help enhance the applicability of the developed models to other sites not included in the models and at the modelled sites over time. Second, the Gumbel-Hougaard copulas adopted in this study were not suitable for modelling all indicator combinations, and, as such, their relationships were characterized by independent copulas. Therefore, the performance of the models could be improved further by using other exchangeable extreme value copula distributions, such as the Galambos and Husler-Reiss copulas, which have not been investigated in this study. Third, some studies have argued for considering the effect of Perception-Reaction Time (PRT) of the road users in the Deceleration Required to Avoid a Crash (DRAC) calculations to improve its efficiency (Kuang et al., 2015; Fazekas et al., 2017; He et al., 2018). Thus, such modifications to DRAC can be tested in the multivariate environment to estimate crash frequency-by-severity. Moreover, the inclusion of perception-reaction time into the modified time-to-collision estimation and relaxation of the constant velocity assumption in Delta-V estimation are interesting research frontiers. Fourth, longer durations of conflict observations (24 h) and combining data from multiple similar sites (three intersections) helped improve the accuracy and precision of the study results despite the increased dimensionality of the multivariate data. It is expected that larger conflict datasets will help improve the efficiency of joint frequency and severity prediction models even further. Finally, real-time crash frequency-by-severity estimation models can be developed to coordinate vehicle movements through signalized intersections by leveraging vehicle-toeverything communication technologies; this was not considered in the current study but could be a fruitful direction for future work.

## CRediT authorship contribution statement

Ashutosh Arun: Conceptualization, Methodology, Software, Data curation, Formal analysis, Writing - original draft, Visualization. Md. Mazharul Haque: Conceptualization, Methodology, Investigation, Validation, Writing - review \& editing, Supervision, Project administration, Funding acquisition. Simon Washington: Conceptualization, Methodology, Co-supervision, Writing - review \& editing. Tarek Sayed: Methodology, Writing - review \& editing. Fred Mannering: Conceptualization, Validation, Writing - review \& editing.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

The data that has been used is confidential.

## Appendix A

Let

$$
\begin{gathered}
M T T C^{*}=M T T C>0 \\
P S D^{*}=P S D>0 \\
D R A C^{*}=D R A C>M A D R, \\
\text { and } \Delta v^{*}=\Delta v>16
\end{gathered}
$$

where, MTTC is the modified time-to-collision, PSD is the proportion of stopping distance, DRAC is the deceleration rate to avoid a crash, and Delta-V is the expected post-collision change in a vehicle's velocity. Then, the probability and frequency of total, severe, and non-severe crashes given a conflict can be computed as illustrated in the following sections.

## Crash frequency estimation

The total crash probability formulas for the univariate and multivariate cases are given below:

Univariate case $\left(R_{x}\right)$ :

$$
R_{x}=1-F_{x}=1-F\left(w_{x}\right)
$$

where, $w$ is the set of crash thresholds such as 0 in the case of MTTC. Therefore,

$$
\begin{aligned}
& R_{M T T C}=1-F_{M T T C}=1-F\left(M T T C^{*}\right) \\
& R_{P S D}=1-F_{P S D}=1-F\left(P S D^{*}\right) \\
& R_{D R A C}=1-F_{D R A C}=1-F\left(D R A C^{*}\right)
\end{aligned}
$$

Bivariate case $\left(R_{x, y}\right)$ :
From Eq. (2),

$$
F_{x, y}=C_{x y}\left[F_{\mathrm{x}}\left(w_{\mathrm{x}}\right), F_{y}\left(w_{y}\right)\right]
$$

where, $C$ denotes the Gumbel-Hougaard Copula estimated according to Eq. (3). Thus,

$$
\begin{aligned}
& R_{x, y}=1-F_{x, y} \\
& \therefore R_{M T T C, P S D}=1-F_{M T T C, P S D} \\
& R_{D R A C, P S D}=1-F_{D R A C, P S D} \\
& R_{M T T C, D R A C}=1-F_{M T T C, P S D}
\end{aligned}
$$

Trivariate case $\left(R_{x, y, z}\right)$ :
Formulating similarly as the bivariate case,

$$
\begin{aligned}
& R_{x, y, z}=1-F_{x, y, z}=1-C_{x y z}\left[F_{\mathrm{x}}\left(w_{\mathrm{x}}\right), F_{y}\left(w_{y}\right), F_{\mathrm{z}}\left(w_{z}\right)\right] \\
& \therefore R_{M T T C, P S D, D R A C}=1-F_{M T T C, P S D, D R A C}
\end{aligned}
$$

## Crash frequency-by-severity estimation with one severity indicator

The conditional probability of severe crashes, i.e., $\operatorname{Pr}\{$ Severe $\mid$ Crash $\}$ is given by:

$$
\operatorname{Pr}\{\text { Severe } \mid \text { Crash }\}=\operatorname{Pr}\left\{\Delta v^{*} \mid \text { Crash }\right\}
$$

Therefore, the conditional probability of non-severe crashes $\operatorname{Pr}\{$ Non - Severe $\mid$ Crash $\}$ can be computed as:

$$
\operatorname{Pr}\{\text { Non }- \text { Severe } \mid \text { Crash }\}=\operatorname{Pr}\{\text { Crash } \mid \text { Conflict }\}-\operatorname{Pr}\{\text { Severe } \mid \text { Crash }\}
$$

An example of the derivation of the formulas for the quadrivariate case is given below:

$$
\operatorname{Pr}\{\text { Crash }\}=\operatorname{Pr}\left\{M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}=1-C\left[F_{M T T C}(0), F_{P S D}(0), F_{D R A C}(8.5)\right]
$$

Conditional Probability of Severe Crashes using Bayes' Rule and general rules of arithmetic involving probabilities:

$$
\begin{aligned}
& \operatorname{Pr}\{\operatorname{Severe} \mid \operatorname{Crash}\}=\operatorname{Pr}\left\{\Delta v^{*} \mid \operatorname{Crash}\right\} \\
&=\frac{\operatorname{Pr}\left\{\Delta v^{*} \cap\left(M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right)\right\}}{\operatorname{Pr}\left\{M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}}=\frac{\operatorname{Pr}\left\{\Delta v^{*}\right\}+\operatorname{Pr}\left\{M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}-\operatorname{Pr}\left\{\Delta v^{*} \cup M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}}{\operatorname{Pr}\left\{M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}} \\
&=\frac{\left(1-F_{\Delta v}(16)\right)+\left(1-C\left[F_{M T T C}(0), F_{P S D}(0), F_{D R A C}(8.5)\right]\right)-}{\left(1-C\left[F_{M T C}(0), F_{P S D}(0), F_{D R A C}(8.5), F_{\Delta v}(16)\right]\right)}
\end{aligned}
$$

Similarly, Conditional Probability of Non-Severe Crashes:

$$
\operatorname{Pr}\{\text { Non-severe } \mid \text { Crash }\}=\operatorname{Pr}\left\{\Delta v^{* *} \mid \text { Crash }\right\}=\frac{\operatorname{Pr}\left\{\Delta v^{* *} \cap\left(M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right)\right\}}{\operatorname{Pr}\left\{M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}}
$$

From algebraic properties of probabilities

$$
\begin{aligned}
& \begin{aligned}
\operatorname{Pr}\left\{\Delta v^{*} \mid \operatorname{Crash}\right\}+\operatorname{Pr}\left\{\Delta v^{*^{*}} \mid \operatorname{Crash}\right\} & =1 \therefore \frac{\operatorname{Pr}\left\{\Delta v^{*} \cap\left(M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right)\right\}}{\operatorname{Pr}\left\{M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}}+\frac{\operatorname{Pr}\left\{\Delta v^{*^{*}} \cap\left(M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right)\right\}}{\operatorname{Pr}\left\{M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}} \\
& =1 \operatorname{or}, \operatorname{Pr}\left\{\Delta v^{*} \cap\left(M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right)\right\}+\operatorname{Pr}\left\{\Delta v^{*^{*}} \cap\left(M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right)\right\} \\
& =\operatorname{Pr}\left\{M T T C^{*} \cup P S D^{*} \cup D R A C^{*}\right\}
\end{aligned} \\
& \text { or, } \operatorname{Pr}\{\text { SevereCrash }\}+\operatorname{Pr}\{\text { Non-severeCrash }\}=\operatorname{Pr}\{\text { Crash }\}
\end{aligned}
$$

Therefore, the unconditional probability for severe crashes can be defined as

$$
\operatorname{Pr}\{\text { SevereCrash }\}=\frac{\left(1-F_{\Delta v}(16)\right)+\left(1-C\left[F_{M T T C}(0), F_{P S D}(0), F_{D R A C}(8.5)\right]\right)-}{\left(1-C\left[F_{M T T C}(0), F_{P S D}(0), F_{D R A C}(8.5), F_{\Delta v}(16)\right]\right)}
$$

The formulas for all the other cases are given below:
Bivariate case $\left(S \Delta_{x, v}\right)$ :

$$
\begin{aligned}
& S_{x, \Delta v}=\operatorname{Pr}\left\{\Delta v^{*} \mid x^{*}\right\} \\
& \therefore S_{M T T C, \Delta v}=\operatorname{Pr}\left\{\Delta v^{*} \cap M T T C^{*}\right\}=F_{\Delta v}+F_{M T T C}-F_{M T T C, \Delta v} \\
& S_{P S D, \Delta v}=\operatorname{Pr}\left\{\Delta v^{*} \cap P S D^{*}\right\}=F_{\Delta v}+F_{P S D}-F_{P S D, \Delta v} \\
& S_{D R A C, \Delta v}=\operatorname{Pr}\left\{\Delta v^{*} \cap D R A C^{*}\right\}=F_{\Delta v}+F_{D R A C}-F_{D R A C, \Delta v}
\end{aligned}
$$

Trivariate case $\left(S_{x, y}, \Delta_{v}\right)$ :

$$
\begin{aligned}
& S_{x, y, \Delta v}=\operatorname{Pr}\left\{\Delta v^{*} \mid x^{*}, y^{*}\right\} \\
& \therefore S_{M T T C, \operatorname{PSD}, \Delta v}=\operatorname{Pr}\left\{\Delta v^{*} \cap\left(M T T C^{*} \cup P S D^{*}\right)\right\}=F_{\Delta v}+F_{M T T C, P S D}-F_{M T T C, P S D, \Delta v} \\
& S_{M T T C, \mathrm{DRAC}, \Delta v}=\operatorname{Pr}\left\{\Delta v^{*} \cap\left(M T T C^{*} \cup D R A C^{*}\right)\right\}=F_{\Delta v}+F_{M T T C, D R A C}-F_{M T T C, D R A C, \Delta v} \\
& S_{D R A C, \mathrm{PSD}, \Delta v}=\operatorname{Pr}\left\{\Delta v^{*} \cap\left(D R A C^{*} \cup P S D^{*}\right)\right\}=F_{\Delta v}+F_{D R A C, P S D}-F_{D R A C, P S D, \Delta v}
\end{aligned}
$$

## References

Aashto, 2018. Policy on geometric design of highways and streets, seventh ed. American Association of State Highway and Transportation Officials (AASHTO), Washington, DC.
Arun, A., Haque, M.M., Bhaskar, A., Washington, S., Sayed, T., 2021a. A bivariate extreme value model for estimating crash frequency by severity using traffic conflicts. Anal. Methods Accid. Res. 32, 100180.
Arun, A., Haque, M.M., Bhaskar, A., Washington, S., Sayed, T., 2021b. A systematic mapping review of surrogate safety assessment using traffic conflict techniques. Accid. Anal. Prev. 153, 106016.
Arun, A., Haque, M.M., Washington, S., Sayed, T., Mannering, F., 2021c. A systematic review of traffic conflict-based safety measures with a focus on application context. Anal. Methods Accid. Res. 32, 100185.
Asljung, D., Nilsson, J., Fredriksson, J., 2017. Using extreme value theory for vehicle level safety validation and implications for autonomous vehicles. IEEE Trans. Intell. Veh. 2, 288-297.
Bahouth, G., Graygo, J., Digges, K., Schulman, C., Baur, P., 2014. The benefits and tradeoffs for varied high-severity injury risk thresholds for advanced automatic crash notification systems. Traffic Inj. Prev. 15 (Suppl. 1), S134-S140.
Beirlant, J., Goegebeur, Y., Segers, J., Teugels, J.L., 2006. Statistics of extremes: Theory and applications. John Wiley \& Sons.
Bücher, A., Kojadinovic, I., 2015. An overview of nonparametric tests of extreme-value dependence and of some related statistical procedures. In: Dey, D.K., Yan, J. (Eds.), Extreme value modeling and risk analysis - methods and applications. Chapman and Hall/CRC, New York.
Cavadas, J., Azevedo, C.L., Farah, H., Ferreira, A., 2020. Road safety of passing maneuvers: A bivariate extreme value theory approach under non-stationary conditions. Accid. Anal. Prev. 134, 105315.
Coles, S., 2001. An introduction to statistical modeling of extreme values. UK, Springer-Verlag, London, London.
Essa, M., Sayed, T., 2020. Self-learning adaptive traffic signal control for real-time safety optimization. Accid. Anal. Prev. 146, 105713.
Farhadi, A., Redmon, J., 2018. Yolov3: An incremental improvement. Computer Vision and Pattern Recognition. Springer Berlin/Heidelberg, Germany, 1804-02.
Fazekas, A., Hennecke, F., Kalló, E., Oeser, M., 2017. A novel surrogate safety indicator based on constant initial acceleration and reaction time assumption. J. Adv. Transport. 2017, 1-9.
Fu, C., Sayed, T., 2021a. Comparison of threshold determination methods for the deceleration rate to avoid a crash (drac)-based crash estimation. Accid. Anal. Prev. 153, 106051.
Fu, C., Sayed, T., 2021b. Multivariate bayesian hierarchical gaussian copula modeling of the non-stationary traffic conflict extremes for crash estimation. Anal. Methods in Accid. Res. 29, 100154.
Fu, C., Sayed, T., Zheng, L., 2020. Multivariate bayesian hierarchical modeling of the non-stationary traffic conflict extremes for crash estimation. Anal. Methods Accid. Res. 28.
Fu, C., Sayed, T., Zheng, L., 2021. Multi-type bayesian hierarchical modeling of traffic conflict extremes for crash estimation. Accid. Anal. Prev. 160, 106309.
Gastaldi, M., Orsini, F., Gecchele, G., Rossi, R., 2020. Safety analysis of unsignalized intersections: a bivariate extreme value approach. Transport. Lett. 13, 209-218.

Guido, G., Saccomanno, F., Vitale, A., Astarita, V., Festa, D., 2011. Comparing safety performance measures obtained from video capture data. J. Transp. Eng. 137, 481-491.
He, Z., Qin, X., Liu, P., Sayed, M.A., 2018. Assessing surrogate safety measures using a safety pilot model deployment dataset. Transport. Res. Record: J. Transport. Res. Board 2672, 1-11.
Ismail, K., Sayed, T., Saunier, N., 2011. Methodologies for aggregating indicators of traffic conflict. Transport. Res. Record: J. Transport. Res. Board 2237, 10-19. Jeong, E., Oh, C., 2017. Evaluating the effectiveness of active vehicle safety systems. Accid. Anal. Prev. 100, 85-96.
Jin, W., Chowdhury, M., Salek, M.S., Khan, S. M., Gerard, P., 2021. Investigating hierarchical effects of adaptive signal control system on crash severity using random-parameter ordered regression models incorporating observed heterogeneity. Accident Analysis and Prevention, 150, 105895.
Kojadinovic, I., Yan, J., Holmes, M., 2011. Fast large-sample goodness-of-fit tests for copulas. Statistica Sinica 21, 841-871.
Kuang, Y., Qu, X., Weng, J., Etemad-Shahidi, A., 2015. How does the driver's perception reaction time affect the performances of crash surrogate measures? PLoS ONE 10, e0138617.
Laureshyn, A., De Ceunynck, T., Karlsson, C., Svensson, A., Daniels, S., 2017. In search of the severity dimension of traffic events: extended delta-v as a traffic conflict indicator. Accid. Anal. Prev. 98, 46-56.
Liu, H., Wei, H., Zuo, T., Li, Z., Yang, Y.J., 2017. Fine-tuning adas algorithm parameters for optimizing traffic safety and mobility in connected vehicle environment. Transp. Res. Part C Emerg. Technol. 76, 132-149.
Mannering, F., Maness, M., Pinjari, A., Zhang, Y., Balusu, S.K., Barbour, N., Menon, N., Sheela, P.V., Tahlyan, D., 2018. Investigation of the role of attitudinal factors on the adoption of emerging automated vehicle and safety technologies. US Department of Transportation University Transportation Center, Tampa, FL.
Mannering, F.L., Shankar, V., Bhat, C.R., 2016. Unobserved heterogeneity and the statistical analysis of highway accident data. Anal. Methods Accid. Res. 11, 1-16. Nelsen, R.B., 2007. An introduction to copulas. Springer Science \& Business Media, New York.
Ozbay, K., Yang, H., Bartin, B., Mudigonda, S., 2008. Derivation and validation of new simulation-based surrogate safety measure. Transport. Res. Record: J. Transport. Res. Board 2083, 105-113.
Shangguan, Q., Fu, T., Wang, J., Jiang, R., Fang, S.E., Guo, Y., 2021. Quantification of rear-end crash risk and analysis of its influencing factors based on a new surrogate safety measure. J. Adv. Transport. 2021, 1-15.
Shelby, S.G., 2011. Delta-v as a measure of traffic conflict severity. Transportation Research Board 90th Annual Meeting, 23-27 January 2011 Washington DC, USA.
Shi, X., Wong, Y.D., Li, M.Z.F., Chai, C., 2018. Key risk indicators for accident assessment conditioned on pre-crash vehicle trajectory. Accid. Anal. Prev. 117, 346-356.
Sklar, M., 1959. Fonctions de repartition a n dimensions et leurs marges. Publications de l'Institut Statistique de l'Université de Paris 8, 229-231.
Songchitruksa, P., Tarko, A.P., 2006. The extreme value theory approach to safety estimation. Accid. Anal. Prev. 38, 811-822.
Wojke, N., Bewley, A., Paulus, D., 2017. Simple online and real-time tracking with a deep association metric. In: 2017 IEEE International Conference on Image Processing (ICIP), 17-20 Sept. 2017 2017, pp. 3645-3649.
Wu, Y., Abdel-Aty, M., Park, J., Zhu, J., 2018. Effects of crash warning systems on rear-end crash avoidance behavior under fog conditions. Transport. Res. Part C: Emerging Technol. 95, 481-492.
Xie, K., Yang, D., Ozbay, K., Yang, H., 2019. Use of real-world connected vehicle data in identifying high-risk locations based on a new surrogate safety measure. Accid. Anal. Prev. 125, 311-319.
Zheng, L., Ismail, K., Sayed, T., Fatema, T., 2018. Bivariate extreme value modeling for road safety estimation. Accid. Anal. Prev. 120, 83-91.
Zheng, L., Sayed, T., 2019a. Bayesian hierarchical modeling of traffic conflict extremes for crash estimation: a non-stationary peak over threshold approach. Anal. Methods Accid. Res. 24, 100106.
Zheng, L., Sayed, T., 2019b. Comparison of traffic conflict indicators for crash estimation using peak over threshold approach. Transport. Res. Record: J. Transport. Res. Board 2673 (5), 493-502.
Zheng, L., Sayed, T., 2019c. From univariate to bivariate extreme value models: approaches to integrate traffic conflict indicators for crash estimation. Transport. Res. Part C: Emerging Technol. 103, 211-225.
Zheng, L., Sayed, T., 2020. A novel approach for real time crash prediction at signalized intersections. Transport. Res. Part C: Emerging Technol. 117.
Zheng, L., Sayed, T., Essa, M., 2019. Validating the bivariate extreme value modeling approach for road safety estimation with different traffic conflict indicators. Accid. Anal. Prev. 123, 314-323.
Zheng, L., Sayed, T., Mannering, F., 2021. Modeling traffic conflicts for use in road safety analysis: a review of analytic methods and future directions. Anal. Methods Accid. Res. 29, 100142.


[^0]:    * Corresponding author.
    E-mail addresses: ashutosh.arun@hdr.qut.edu.au (A. Arun), m1.haque@qut.edu.au (Md.M. Haque), simon@amagroup.io (S. Washington), tsayed@civil.ubc.ca (T. Sayed), flm@usf.edu (F. Mannering).

