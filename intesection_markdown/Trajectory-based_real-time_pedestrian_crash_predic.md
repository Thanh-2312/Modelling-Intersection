# Trajectory-based real-time pedestrian crash prediction at intersections: A novel non-linear link function for block maxima led Bayesian GEV framework addressing heterogeneous traffic condition 

Parvez Anowar ${ }^{\mathrm{a}}$, Nazmul Haque ${ }^{\mathrm{b}}$, Md Asif Raihan ${ }^{\mathrm{c} *}$ and Md Hadiuzzaman ${ }^{\mathrm{d}}$

${ }^{\mathrm{a}}$ Department of Civil, Environmental and Construction Engineering, University of Central Florida, 12800 Pegasus Drive, Orlando, FL 32816, USA; Email: pa545735@ucf.edu
${ }^{\mathrm{b}}$ Accident Research Institute, Bangladesh University of Engineering and Technology, Dhaka 1000, Bangladesh; Email: nhaque@ari.buet.ac.bd
${ }^{\mathrm{c}}$ Accident Research Institute, Bangladesh University of Engineering and Technology, Dhaka 1000, Bangladesh; Email: raihan@ari.buet.ac.bd
${ }^{\mathrm{d}}$ Department of Civil Engineering, Bangladesh University of Engineering and Technology, Dhaka 1000, Bangladesh; Email: mhadiuzzaman@ce.buet.ac.bd
*Corresponding author:
Md Asif Raihan
Email: raihan@ari.buet.ac.bd

## Highlights

- Real-time crash prediction model for mixed and non-lane-based intersections
- Bayesian GEV model integrates linear and non-linear link function comparison
- Modified crash risk metric adjusts for habitual pedestrian risk-taking behavior
- Non-linear link functions enhance accuracy in heterogeneous traffic conditions

Note: This manuscript is a preprint and has not yet been peer-reviewed. It is currently being considered for submission to a peer-reviewed journal.

# Trajectory-based real-time pedestrian crash prediction at intersections: A novel non-linear link function for block maxima led Bayesian GEV framework addressing heterogeneous traffic condition 


#### Abstract

This study develops a real-time framework for estimating pedestrian crash risk at signalized intersections under heterogeneous, non-lane-based traffic. Existing approaches often assume linear relationships between covariates and parameters, oversimplifying the complex, nonmonotonic interactions among different road users. To overcome this, the framework introduces a non-linear link function within a Bayesian generalized extreme value (GEV) structure to capture traffic variability more accurately. The framework applies extreme value theory through the block maxima approach using post-encroachment time as a surrogate safety measure. A hierarchical Bayesian model incorporating both linear and non-linear link functions into GEV parameters is estimated using Markov Chain Monte Carlo simulation. It also introduces a behavior-normalized Modified Crash Risk (MRC) formula to account for pedestrians' habitual risk-taking behavior. Seven Bayesian hierarchical models were developed and compared using deviance information criterion. Models employing non-linear link functions for the location and scale parameters significantly outperformed their linear counterparts. The results revealed that pedestrian speed has a negative relationship with crash risk, while flow and speed of motorized vehicles, pedestrian flow, and non-motorized vehicles conflicting speed contribute positively. The MRC formulation reduced overestimation and provided crash predictions with 93\% confidence. The integration of non-linear link functions enhances model flexibility, capturing the non-linear nature of traffic extremes. The proposed MRC metric aligns crash risk estimates with real-world pedestrian behavior in mixed-traffic environments. This framework offers a practical analytical tool for traffic engineers and planners to design adaptive signal control and pedestrian safety interventions before crashes occur.


Keywords: pedestrian safety; extreme value theory; post-encroachment time; non-lane-based traffic; behavior-normalized crash risk; trajectory

## 1. Introduction

Proactive road safety assessment methodologies incorporating surrogate safety measures have gained momentum to overcome the limitations of historical crash data and to address the crash risks associated with emerging technologies such as connected and automated vehicles (CAV) (Arun et al., 2021). Extreme Value Theory (EVT) (Songchitruksa and Tarko, 2006), probabilistic frameworks (Saunier and Sayed, 2008), and causal models (Davis et al., 2011) have been employed to estimate crash risks from traffic conflicts. EVT, in particular, has seen increasing application due to its unique capability for estimating crash risk based on observable events, such as traffic conflicts, leading to rare or unobservable crash events. It provides an alternative to traditional methods that rely solely on police-reported crash data and offers a unified measure of traffic conflict severity, aligning well with established safety frameworks like Hydén's pyramid (Hydén, 1987) and avoiding assumptions about fixed crash-to-surrogate
ratios (Zheng et al., 2014; Laureshyn et al., 2010; Svensson and Hydén, 2006). Thus, EVT has been extensively utilized in developing crash risk models, particularly focusing on vehicle-tovehicle crashes.

EVT's application in real-time pedestrian crash risk assessment has recently gained attention (Ali et al., 2023a; Fu \& Sayed, 2023; Tahir and Haque, 2024; Ankunda et al., 2024). However, most studies have been limited to homogeneous traffic settings, with little consideration for mixed conditions where motorized vehicles (MVs) and non-motorized vehicles (NMVs) share the same carriageway. This gap can be attributed to study locations lacking significant NMV presence or having designated lanes. In heterogeneous conditions, differences in vehicle speeds, maneuverability, and pedestrian interactions produce varying levels of crash severity, influencing overall crash risk (Lee et al., 2015).

Furthermore, prior researches assume linear link functions for Generalized Extreme Value (GEV) parameters such as location and scale, which oversimplifies the complex nature of the traffic scenarios. The theoretical foundation for employing non-linear link functions in extreme value models has been well-established across various disciplines. In road safety, Lao et al. (2013) developed generalized non-linear models (GNM) for rear-end crash risk analysis using Poisson formulations and showed that generalized linear models (GLM) are a special case of GNMs. By employing logarithmic and polynomial link functions, their results demonstrated that non-linear, non-monotonic relationships better capture real-world crash dynamics. Similarly, Carrodano (2024) used a Bayesian network approach to identify non-linear factor interactions in crash risk, emphasizing that human, vehicle, and environmental factors jointly influence accident likelihood through interconnected, non-linear dependencies.

Beyond traffic, non-linear link functions have been extensively applied in hydrology, environmental science, oceanography, and climate science. For instance, nonstationary GEV models in hydrology and climate research have shown that non-linear functional forms, such as quadratic, exponential, or spline-based relationships, can more accurately describe changes in extremes compared to traditional linear specifications (Panagoulia et al., 2013; Um et al., 2017; Adlouni et al., 2007; Robin \& Ribes, 2020; and Song et al., 2018). Li et al. (2024) further advanced this framework through Bayesian hierarchical modeling for surface-level ozone extremes, demonstrating that the dependence of upper tail distributions on multiple covariates is highly nonlinear. In oceanographic applications, Mackay and Jonathan (2020) illustrated how non-stationary extreme value models with non-linear covariate relationships significantly improve return value estimates for observed storm peak behavior compared to linear approaches. The evgam framework (Youngman, 2022) consolidated these developments by providing a flexible generalized additive modeling (GAM) structure for GEV and GPD parameters, where non-linear smooth functions define covariate effects and linear forms emerge as special cases. These applications demonstrate the versatility and effectiveness of non-linear approaches in capturing complex relationships between extreme value parameters and covariates.

Despite these successful applications across multiple disciplines, the use of non-linear link functions remains largely unexplored in the estimation of crash risk using block maxima in GEV methods. This study addresses this gap by providing a detailed comparison of how models with linear link functions and non-linear link functions behave in the context of vehiclepedestrian crash risk estimation. Through the development of seven Bayesian hierarchical
models incorporating different link function specifications, this research systematically evaluates the performance improvements achieved through non-linear approaches.

Additionally, many studies have focused on locations that have relatively low numbers of conflicts, where crashes are less likely to occur leaving locations with high numbers of conflicts unaddressed, where conventional crash risk models fail to adequately account for pedestrians' inherent risk-taking behaviour. This simplification often leads to an overestimation of predicted crashes compared to actual occurrences.

To address the overestimation of crash risk caused by habitual risk-taking in Dhaka's mixed, non-lane-based traffic, this study introduces a behavior-normalized Modified Crash Risk (MRC) metric. In such congested conditions, pedestrians often cross through traffic, accept minimal time gaps, and cross through conflict zones instead of using designated facilities (Zafri, 2023; Sadeek et al., 2025; Fattah et al., 2021; Tahmid et al., 2024; Noman et al., 2024). These actions, reinforced by inadequate infrastructure and inconvenient overpasses, have normalized risk-taking in daily travel (Debnath et al., 2021; Sakib et al., 2023). Based on Risk Homeostasis Theory (Wilde, 1982; Evans, 1986), pedestrians adjust their behavior to maintain a personal comfort level of risk, meaning that conventional crash risk estimates remain high even under typical conditions. The proposed MRC incorporates behavioral calibration, enabling more realistic and targeted safety assessments in Bangladesh's urban traffic conditions.

The overall contributions of this study are as follows:

(1) It develops a real-time vehicle-pedestrian crash risk framework for signalized intersections that considers both MVs and NMVs within the same traffic stream, applying a hierarchical Bayesian model using Block Maxima (BM) and GEV distribution.
(2) It incorporates both linear and non-linear link functions for GEV parameters and forms seven hierarchical models, comparing them through DIC values to evaluate the performance of non-linear structures.
(3) It introduces a modified crash risk metric that accounts for behavioral adaptation, addressing the overestimation commonly observed in conventional crash risk formulations under mixed traffic conditions.

## 2. Relevant studies on extreme value models

EVT enables researchers to extrapolate from frequent traffic conflicts to rare crash events, offering a powerful analytical framework to identify high-risk areas. Existing EVT-based studies on pedestrian safety have focused on key methodological aspects such as sampling strategy, conflict indicators, traffic stream characteristics, link functions, and covariate inclusion. These factors are critical for model accuracy, as they determine how conflicts are quantified and how variable interactions influence crash risk. In particular, the inclusion of covariates allows models to capture the effects of traffic flow, speed, and behavioral variations on pedestrian safety, thereby providing actionable insights for proactive risk management.

Many studies have employed EVT using the BM or peak-over-threshold (POT) approaches to analyze vehicle-pedestrian interactions. Fu and Sayed (2023) and Zheng and Sayed (2020) applied the BM approach with modified time-to-collision (MTTC) to examine how traffic flow
and shock wave area affect pedestrian safety, highlighting the relationship between traffic dynamics and conflict severity. Similarly, Ali et al. (2022) and Guo et al. (2020) analyzed homogeneous traffic conditions using POT with Gap Time and Post Encroachment Time (PET), incorporating factors such as driver demographics and violation behaviors. Studies such as Alozi and Hussein (2022) and Zhang and Abdel-Aty (2022) further utilized PET and Timeto-Collision (TTC) in homogeneous streams, emphasizing the influence of pedestrian signal phases, cycle length, and vehicle count. Although these studies demonstrated the value of integrating signal-related and behavioral variables, they lacked the complexity of heterogeneous traffic interactions.

Tahir and Haque (2024) extended EVT applications to signalized intersections using BM, with PET and Delta-V as conflict indicators. They modeled the location and scale parameters using linear and log-linear link functions, respectively, and included variables such as vehicle and pedestrian counts, speed, and the number of conflicts per cycle. Similarly, Ali et al. (2023a, and 2023b) developed BM-based frameworks using PET, Gap Time, and minimum Time-to-Collision (mTTC) as indicators but maintained linear link assumptions for GEV parameters. While these studies contributed to methodological consistency, they did not adequately capture the complexity of heterogeneous, non-lane-based traffic. Ankunda et al. (2024) made one of the few attempts to extend EVT to such conditions by combining BM and POT approaches with PET and Gap Time, incorporating elements like group pedestrian crossings and twowheelers. Although this study provided a more realistic understanding of mixed-traffic environments, it remained confined to moderate-conflict locations and still relied on linear link functions for covariates.

Despite these advancements, significant research gaps remain. Most studies rely on linear assumptions for GEV parameters, which oversimplify the non-linear and interdependent dynamics of mixed-traffic interactions. Moreover, high-conflict intersections, where diverse vehicle types, speed variations, and pedestrian risk-taking behaviors interact, remain underrepresented in the literature. As a result, current models often fail to accurately reflect the complex risk structure of heterogeneous urban environments.

In summary, EVT applications in pedestrian safety have yet to fully address the challenges posed by heterogeneous, non-lane-based traffic. The prevailing reliance on linear link functions limits the models' ability to capture non-monotonic relationships between covariates and crash risk. These gaps underscore the need for advanced modeling frameworks that incorporate vehicle heterogeneity, high-conflict conditions, and non-linear link functions. Addressing these limitations forms the central motivation of the present study, which employs a Bayesian hierarchical GEV framework with both linear and non-linear link structures to provide a more realistic representation of vehicle-pedestrian crash risk in mixed traffic conditions.

## 3. Methodology

Figure 1 depicts the novel real-time crash risk estimation framework for vehicle-pedestrian interactions at signalized intersections introduced in this study. The following sub-sections describe different segments of this framework.

### 3.1.Road user detection, classification, and trajectory extraction considering local peculiarity

This study employed the advanced DEEGITS (Islam et al., 2024) framework for vehicle detection, classification, and tracking using video sensors. The system harnessed cutting-edge convolutional neural network (CNN) techniques to efficiently and accurately detect vehicles and pedestrians, even in complex conditions such as congestion and occlusion. Calibration was performed using the enriched 'DhakaPersons' training dataset, which utilized a data fusion approach for simultaneous detection of both vehicles and pedestrians. To enhance dataset quality and diversity, image pre-processing and augmentation techniques were applied. Transfer learning was implemented with the YOLOv8 pre-trained model to improve detection accuracy across various vehicle types. Optimal hyperparameters were identified using the Grid Search algorithm, while the Stochastic Gradient Descent (SGD) optimizer delivered superior performance. Rigorous experiments validated the framework's high detection accuracy. For tracking, the DeepSORT multi-object tracking algorithm was integrated, and the framework was successfully tested under heterogeneous traffic conditions to evaluate mixed traffic states. The tracked points are aggregated into corresponding vehicle trajectories and these trajectories are calibrated for camera perspective error using Equation (1) adopted from Hadiuzzaman et al. (2017).

$$
R=\theta(r, \rho(x, X))
$$

Where, $\rho(x, X)$ corrects the distorted distances $(r)$ due to decrease in length $X$ when a vehicle moves away at a distance x from the camera (also known as error due to perspective view) and $\theta$ converts the pictorial distance into field distance. The function $\rho$ can have any functional form. However, this study considers $\rho$ a 2nd-degree polynomial function to have the corrected distance $R$.

### 3.2.Identification of conflict points and measuring surrogate safety

Intersections between the paths of pedestrians and vehicles are identified as potential conflict points where their trajectories intersect. This process involves representing the paths of pedestrians as polylines. If an intersecting point is found, the algorithm extracts the coordinates $\left(x_{\text {int }}, y_{\text {int }}\right)$ of the intersection point and stores the relevant information, including the IDs and time stamp ( $t_{p}$ and $t_{v}$ ) of the involved pedestrian and vehicle tracks respectively, in a structured data frame. The PET was then calculated based on these timestamps. Specifically, if a pedestrian arrived at the conflict point before the vehicle ( $t_{p}<t_{v}$ ), the PET was calculated as the difference between the vehicle's arrival time and the pedestrian's departure time and vice versa, as shown in Equation (2).

$$
\text { PET }=f(x)= \begin{cases}t_{v}-t_{p}, & t_{p}<t_{v} \\ t_{p}-t_{v}, & t_{v}<t_{p} \\ 0 & t_{v}=t_{p}\end{cases}
$$

Subsequently, PET values are aggregated over time intervals $\Delta t$ to analyse temporal variations. Specifically, the average PET and standard deviation are computed for each time interval $t_{i}$ (i.e. signal cycle) to match the co-variates mention in the next subsection.

![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-07.jpg?height=1958&width=1571&top_left_y=471&top_left_x=243)
Figure 1. Real-time crash risk estimation framework for vehicle-pedestrian interactions

### 3.3.Block maxima approach of extreme value theory and incorporating covariates

The proposed framework employs the BM approach of EVT to estimate crash risk from traffic conflicts. EVT is particularly well-suited for this purpose due to its ability to extrapolate from frequent traffic conflicts to rare crashes (Songchitruksa and Tarko, 2006). This enables a proactive safety assessment framework that identifies potential crash precursors before actual collisions occur. The signal cycle is used as the time interval for analysis for two main reasons. First, it provides a meaningful temporal unit to capture the dynamic interactions and risks associated with multiple road users at signalized intersections (Ali et al., 2021). Second, using the signal cycle as a block aligns naturally with the BM approach, corresponding to a GEV distribution, which allows the statistical modeling of extreme conflicts occurring within each cycle.

In the BM approach, the highest value within each block of observations is considered an extreme value (Coles, 2001). Mathematically, it involves a sequence of random and independent variables $\left(p_{1}, p_{2}, p, \ldots \ldots, p_{n}\right)$, each following a common distribution function, and $M_{n}=\max \left(p_{1}, p_{2}, p_{3}, \ldots \ldots, p_{n}\right)$ denoting the block maximum of these values. Within this framework, $p_{i}$ represents a traffic conflict indicator such as PET measured during signal cycle $i$. Assuming that the maximum conflict values follow a GEV distribution as $n$ approaches infinity (Fisher and Tippett, 1928), the GEV distribution function can be expressed mathematically as Equation (3).

$$
G(z)=\exp \left(-\left[1+\xi\left(\frac{z-\mu}{\sigma}\right)\right]^{-\frac{1}{\xi}}\right)
$$

Here, $z$ represents the observed or possible extreme value of the conflict indicator, $-\infty<$ $\mu<\infty$ represents the location parameter, $\sigma>0$ indicates the scale parameter and $-\infty<\xi<$ $\infty$ represents the shape parameter. Equation (3) is used to describe traffic extremes (near-crash situations) while ensuring that the scale parameter remains strictly positive. It is parameterized as $\operatorname{GEV}(\mu, \phi, \xi)$, where $\phi=\log \sigma$. Let, $p_{i j}$ be the $i^{\text {th }}$ cycle maximum for site $j$, where $j=$ $1,2,3, \ldots \ldots, s$ and $i=1,2,3, \ldots \ldots, n_{j}$. That means $p_{i j}$ represents the maximum value for cycle $i$ and site $j$ and the GEV distribution, which is site-dependent, can be expressed as Equation (4):

$$
G\left(z_{i j}<z \mid \mu_{i j}, \phi_{i j}, \xi_{i j}\right)=\exp \left(-\left[1+\xi_{i j}\left(\frac{p-\mu_{i j}}{\exp \left(\phi_{i j}\right)}\right)\right]^{-\frac{1}{\xi_{i j}}}\right)
$$

To address the fluctuating nature of traffic extremes over time and describe changing crash risk, relevant covariates are incorporated into the parameters of the GEV distribution using an identity link function. However, accurately estimating the shape parameter can be challenging due to the varied distribution of conflict extremes and the absence of covariates (Coles et al., 2001). When GEV parameters are related to covariates, it is termed a non-stationary process; otherwise, it is referred to as a stationary process $\left(\alpha_{\mu 1}=\alpha_{\phi 1}=0\right)$. The non-stationary process is represented by Equation (5) as follows:

$$
\left(\begin{array}{c}
\mu_{i j}=\alpha_{\mu 0}+\alpha_{\mu 1} \mathrm{X}^{\theta_{\mu}}+\varepsilon_{\mu j} \\
\phi_{i j}=\alpha_{\phi 0}+\alpha_{\phi 1} \mathrm{Y}^{\theta} \phi+\varepsilon_{\phi j} \\
\xi_{i j}=\alpha_{\xi 0}+\varepsilon_{\xi j}
\end{array}\right)
$$

In the equation above, $\alpha_{\mu 0}, \alpha_{\phi 0}$, and $\alpha_{\xi 0}$ represent intercept terms for three model parameters and $\alpha_{\mu 1}$ and $\alpha_{\phi 1}$ denote parameter estimates for the covariate vectors X and Y. $\varepsilon_{\mu j}$, $\varepsilon_{\phi j}$, and $\varepsilon_{\xi j}$ stand for random error terms. $\theta_{\mu}$ and $\theta_{\phi}$ represent the exponent of the covariates of the location parameter and scale parameter respectively. It is worth noting that the random terms in Equation (5) signify variances between sites, which remain constant for extremes at the same site but vary across different sites. When $\theta_{\mu}=\theta_{\phi}=1, \mu_{i j}$ and $\phi_{i j}$ will indicate linear relationship among the covariates. Previous studies (Fu and Sayed, 2023; Ali et al., 2023a; Tahir and Haque, 2024; Ankunda et al., 2024) primarily adopted such linear forms, which tend to oversimplify the link functions and fail to reflect the non-monotonic nature of real-world traffic dynamics.

In contrast, incorporating non-linear link functions by introducing the exponent term $\theta$ provides greater flexibility in modeling complex, non-additive relationships between predictors and crash risk. This approach allows the effects of covariates to vary depending on the level or interaction of other variables, capturing the non-linear influence of traffic flow, pedestrian movement, and vehicle heterogeneity. Non-linear link functions also enhance model interpretability and predictive performance by representing thresholds and saturation effects that are typical in heterogeneous, non-lane-based traffic. Additionally, non-linear models can improve predictive performance by fitting the data more closely, particularly in scenarios where linear assumptions are insufficient to capture underlying patterns in the data (Haque et al., 2020). In the linear relationship, the models can only be explained by the sign of the coefficients. It requires additional statistical tests to find the influence of the covariate. However, in Equation (5) the exponent term $\theta$ can be independently interpreted the influence of the covariate terms without the assistance of further statistical tests. This flexibility makes the non-linear GEV formulation a more powerful and realistic tool for representing complex, mixed-traffic interactions in urban safety analysis.

### 3.4. Bayesian approach for model estimation

To estimate the model described in Equation (4) and Equation (5), a Bayesian approach is employed, offering flexibility through the estimation of posterior distributions and characterization of the underlying process by specifying priors for model parameters. The model is structured by assigning priors to seven fundamental parameters $\left(\alpha_{\mu 0}, \alpha_{\phi 0}, \alpha_{\xi 0}, \alpha_{\mu 1}\right.$, $\alpha_{\phi 1}, \theta_{\mu}$, and $\theta_{\phi}$ ). The first five parameters are assumed to have uninformative priors, modeled with a normal distribution having a mean of zero and a variance of $10^{6}\left(\mathrm{~N}\left(0,10^{6}\right)\right)$ suggested by Ntzoufras (2011). The last two parameters, $\theta_{\mu}$ and $\theta_{\phi}$, are considered to follow a uniform distribution within the range of (-2.0, 2.0) to avoid unwanted simulation environment (i.e. logarithm of negative value). However, accurately estimating the shape parameter of the GEV distribution can present convergence challenges if priors are not properly defined (Zheng et al., 2014). To address this issue, the shape parameter is constrained within a uniform distribution
range of (-5.0 to 5.0) which is slightly larger than the previous studies (Zheng et al., 2014; Songchitruksa and Tarko, 2006). The estimation of posterior distributions for the model parameters is carried out using Markov Chain Monte Carlo (MCMC) simulation, with Gibbs sampling employed for the estimation process.

### 3.5. Measure of performance

In Bayesian analysis, the DIC is often utilized for model comparison, offering a common goodness-of-fit measure (Spiegelhalter et al., 2002). DIC can be considered as a broadened version of Akaike's information criterion (El-Basyouny and Sayed, 2009). According to Spiegelhalter et al. (2002), DIC is expressed as in Equation (6).

$$
D I C=\bar{D}+p_{D}
$$

Here, $\bar{D}$ represents the posterior mean deviance, which evaluates how well the model fits the data, while $p_{D}$ indicates the effective number of parameters in the model. Generally, a lower DIC value suggests a better fit for the model. When considering multiple covariates, various models are created and compared, and the model with the lowest DIC value is selected as the best fit.

### 3.6. Crash risk estimation

The risk of crash for each signal cycle was estimated using the fitted GEV distribution, which captures the probability of extreme vehicle-pedestrian conflicts leading to a crashequivalent condition. The risk of crash is expressed as in Equation (7).

$$
=\left(\begin{array}{c}
R C_{i}=\operatorname{Pr}\left(z_{i}>0\right)=1-G_{i}(0) \\
1-\exp \left(-\left[1-\xi_{i} \frac{\mu_{i}}{\sigma_{i}}\right]^{-\frac{1}{\xi}}\right), \text { for } \xi \neq 0 \\
1-\exp \left[-\exp \left(\frac{\mu_{i}}{\sigma_{i}}\right)\right], \text { for } \xi=0
\end{array}\right)
$$

Here, $R C_{i}$ represents the crash risk in signal cycle $i$, where a value of zero indicates a safe cycle and a positive value indicates a potential crash occurrence within that cycle. This measure quantifies the likelihood that a vehicle-pedestrian interaction becomes critical.

### 3.7. Modified Crash Risk Formulation

Equation (7) has been widely adopted to model the tails of conflict severity distributions and infer crash probability from observable traffic conflicts (Ali et al., 2023a; Fu \& Sayed, 2023; Tahir and Haque, 2024).

However, this direct estimation assumes that all risk-taking events are equally hazardous. In highly heterogeneous and congested traffic environments such as Dhaka, this assumption is unrealistic. Numerous studies have shown that risk-taking behavior is deeply embedded in everyday pedestrian movement, making high-risk interactions a common and often necessary practice rather than an exception.

Pedestrians in Dhaka frequently accept very short time gaps ( $\leq 2 \mathrm{~s}$ ), run while crossing, and use mid-block or conflict-zone crossings rather than marked facilities (Zafri, 2023). These behaviors are strongly associated with male and younger pedestrians, uncontrolled intersections, narrow ( $\leq 1.5 \mathrm{~m}$ ) or discontinuous medians, and high traffic volumes, all of which are prevalent throughout the city (Zafri, 2023). The preference for informal crossings is further reinforced by inaccessible or inconvenient formal facilities, such as overpasses and footbridges, which are often avoided due to time inefficiency, steep stairs, and perceived insecurity (Sadeek et al., 2025). Additionally, $85 \%$ of pedestrians randomly cross roads with flexible medians rather than using designated crossing points, with pedestrians citing time savings and avoidance of long walks as primary motivations (Fattah et al., 2021). Consequently, the majority of pedestrians in Dhaka cross at grade, even when vehicle speeds and flows are high.

Risk Homeostasis Theory (Wilde, 1982; Evans, 1986) suggests that individuals maintain a target level of perceived risk by adjusting their behavior. These behavioral and infrastructural realities create a persistently elevated baseline of risk, where pedestrians continuously engage in actions that would be considered unsafe in more regulated environments. The Perceptual Cycle Model analysis demonstrates that environmental factors such as blocked footpaths, poor pavement conditions, and obstructed crosswalks compel pedestrians to engage in risky behaviors, making these actions feel necessary rather than voluntary (Debnath et al., 2021). Furthermore, unsuitable crosswalk location placement, absence of guard rails on medians, and inadequate lighting are the most important factors discouraging proper crosswalk use (Sakib et al., 2023). As a result, the conventional crash risk $\left(R C_{i}\right)$ remains high in most signal cycles, failing to distinguish abnormally dangerous conditions from the background of routine risktaking.

To overcome this limitation, this study introduces a Modified Crash Risk (MRC) measure that adjusts the raw crash risk relative to the prevailing local baseline. The MRC isolates signal cycles where the observed risk meaningfully exceeds the habitual, accepted level of risk-taking in Dhaka's traffic context, as defined in Equation (8).

$$
M R C_{i}=\left\{\begin{aligned}
R C_{i}-\overline{R C}-Z_{c r} * \sigma_{R C}, & \overline{R C} \gg 0: \\
R C_{i}, & \text { otherwise }
\end{aligned}\right.
$$

Here, $M R C_{i}$ is the non-negative (i.e. $\forall i: M R C_{i}>0$ ) modified crash risk in signal cycle $i$. $\overline{R C}$ and $\sigma_{R C}$ denote the average and standard deviation of the crash risk for each cycle, respectively. $Z_{c r}$ indicates the z-critical value for a particular confidence interval. This formulation ensures that $M R C_{i}$ is non-negative $\left(M R C_{i} \geq 0\right)$ and emphasizes only those cycles where the risk level significantly exceeds the site's normal exposure conditions.

Theoretically, this modification extends the exceedance-over-threshold principle to a behavioral setting, where the baseline ( $\overline{R C}+Z_{c r} * \sigma_{R C}$ ) represents the community's habitual risk tolerance rather than purely statistical variation. By adjusting for this behavioral normalization, MRC captures abnormally high-risk cycles that indicate temporary breakdowns in pedestrian-vehicle interactions such as chaotic crossings, sudden surges in pedestrian flow.

The proposed MRC metric therefore provides a context-sensitive and realistic measure of crash risk, capable of differentiating genuine safety-critical cycles from those reflecting the city's inherently risky yet socially normalized crossing behavior.

## 4. Data collection and pre-processing

### 4.1. Data collection

The selection of intersections was informed by historical crash data from 2016 to 2020, sourced from the Accident Research Institute's (ARI) police-reported crash database. To ensure a representative sample of intersections within Dhaka city, nine locations were selected, comprising four 3-legged tee intersections (Abul Hotel, Bonolota Market, Mirpur 1 Bus Stop, and Shishu Mela) and five 4-legged cross intersections (Motsho Bhaban, Paltan, Shahbagh, Bijoy Sarani, and Banglamotor). The signal of these intersections does not have any dedicated pedestrian phase. Pedestrians naturally cross the road individually when the traffic flow is low; however, they accumulate and form groups before crossing if the flow is higher. Conflict data were collected through continuous video monitoring, with two cameras installed at a height of 6 to 10 meters at each site to capture the entire traffic flow for two hours during peak periods on regular weekdays under favourable weather conditions as illustrated in Table A1 (see Appendix). Figure A2 (see Appendix) shows the approximate coverage area of each camera, with careful selection of positions and fields of view to ensure a comprehensive capture of all potential conflicting movements.

The video analysis platform detected conflicts by identifying instances where predicted vehicle paths overlapped, signalling a potential for collisions. A PET value approaching zero signifies that a collision was narrowly avoided (Allen et al., 1978). Various studies have employed different PET thresholds to define vehicle-pedestrian conflicts. For example, Tahir and Haque (2024) and Ali et al. (2023a) considered interactions with PET $\leq 6$ seconds as conflicts, whereas Zheng and Sayed (2019) and Fu and Sayed (2021) used a more stringent threshold of $\mathrm{PET} \leq 4$ seconds to focus on extreme events. The latter threshold captures more critical interactions while reducing unnecessary data processing. Additionally, Zheng et al. (2019b) demonstrated that the choice of predetermined event selection values has minimal effect on model estimation results, provided they remain sufficiently distant from the threshold that defines extreme events. This study classified vehicle-pedestrian interactions as conflicts when the PET was less than 5 seconds. PET quantifies the time interval between the moment the offending road user clears the potential collision area and when the conflicted road user reaches that same point (Allen et al., 1978). In shared road spaces with complex and intersecting movement patterns where vehicle-pedestrian interactions occur, PET serves as an effective indicator for evaluating traffic conflicts and safety margins.

### 4.2. Signal cycle level covariates

An automated covariate extraction algorithm is used in this research to overcome the complexity due to the involvement of multiple dimensions in data processing at the signal level. The algorithm starts by synchronizing datasets based on timestamps and assigns each trajectory and conflict to the corresponding signal cycle, while incorporating additional details such as signal phases. It identifies signal cycles involving pedestrian conflicts with various vehicle types and extracts key covariates, such as the flow and speed of all road users, along with their conflicting flow and speed. While this research focuses on vehicle-pedestrian interactions, the
algorithm is flexible enough to be adapted for analysing other types of crashes, such as rearend collisions.

The process began by counting different road users during each cycle interval at all intersections. Given the mixed traffic conditions, vehicle counts were converted to Passenger Car Unit (PCU) values using guidelines from the Revised Strategic Transport Plan (RSTP) for Dhaka (DTCA, 2015). Subsequently, road users were classified into three categories: pedestrians, MVs, and NMVs. MVs and NMVs were categorized separately because their differing speeds and protective features result in varying severities of accidents involving pedestrians, leading to distinct impacts on crash risk (Lee et al., 2015; Hoque et al., 2025; Xie et al., 2009). The conflicting flow was defined as the flow of road users involved in conflicting events. A substantial number of road users were found to participate in these conflicting events, largely due to the heterogeneity of vehicles and the insufficient enforcement of traffic regulations.

The determination of speed involved collecting object coordinates and timestamps, followed by camera calibration to convert pixel coordinates to real-world measurements. Space mean speeds were then calculated based on the distance travelled within cycle intervals. Before incorporating the covariates into the extreme value model, a comprehensive correlation analysis was performed to assess their interrelationships. From the initial set of variables, only those with significant correlations were retained for modelling as illustrated in Figure A1 (see Appendix). The selected covariates include the flow of motorized vehicles, flow of pedestrians, speed of motorized vehicles, speed of pedestrians, conflicting flow of motorized vehicles, conflicting speed of motorized vehicles, and conflicting speed of non-motorized vehicles. These covariates exhibited a range of weak to moderate correlations with one another, justifying their inclusion without multicollinearity concerns.

Highly correlated variables are systematically managed during the modelling process, with a focus on retaining only those that demonstrate statistical significance. Variables with high correlation are flow of non-motorized vehicles, speed of non-motorized vehicles, conflicting flow of non-motorized vehicles, conflicting flow of pedestrians, conflicting speed of pedestrians. The methodology employed for this analysis aligns with the approaches outlined by Ali et al. (2023a) and Ankunda et al. (2024), ensuring consistency in variable selection.

Crash data were gathered to benchmark the proposed framework, as shown in Table 1. This dataset includes the count of cycles, crashes, and various covariates for each intersection. The framework was specifically applied to vehicle-pedestrian crashes estimated from traffic conflicts extracted from daytime videos, focusing solely on daytime crashes to assess model performance. Based on these criteria, the selected intersections reported thirty-six crashes between 2016 and 2020.

Table 1. Summary of traffic flow, speed metrics, conflict incidents, and crash data
| Parameter |  | $\mathbf{F}_{\mathrm{MV}}$ (PCU) | $\mathbf{F}_{\mathbf{P}}$ | $\mathbf{S}_{\text {MV }}$ (m/s per PCU) | $\mathbf{S}_{\mathbf{P}}$ (m/s) | $\mathbf{C F}_{\text {MV }}$ (PCU) | $\mathbf{C S}_{\text {MV }}$ (m/s per PCU) | $\mathbf{C S}_{\text {nMv }}$ (m/s per PCU) | PET (s) | Cycle timings (min) | Number of cycles | Total conflicts | Crash records (2016-20) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Abul Hotel | Mean | 824.79 | 1477.61 | 1.91 | 0.70 | 337.08 | 2.21 | 0.67 | 2.39 | 6.67 | 18 | 29744 | 4 |
|  | S. D. | 50.53 | 145.87 | 0.16 | 0.03 | 35.37 | 0.17 | 0.06 | 0.07 |  |  |  |  |
|  | Max | 901.75 | 1737 | 2.29 | 0.75 | 397.75 | 2.45 | 0.77 | 2.49 |  |  |  |  |
|  | Min | 748.75 | 1279 | 1.66 | 0.62 | 279.75 | 1.89 | 0.59 | 2.20 |  |  |  |  |
| Bonolota Market | Mean | 503.08 | 199.22 | 4.01 | 1.87 | 123.01 | 4.10 | 1.99 | 2.22 | 3.33 | 36 | 8750 | 3 |
|  | S. D. | 33.18 | 33.73 | 0.58 | 0.24 | 27.93 | 0.63 | 0.47 | 0.15 |  |  |  |  |
|  | Max | 568.50 | 251 | 5.34 | 2.25 | 179.75 | 5.63 | 3.07 | 2.57 |  |  |  |  |
|  | Min | 430.75 | 104 | 2.43 | 1.02 | 64.00 | 2.75 | 1.25 | 1.92 |  |  |  |  |
| Mirpur 1 Bus Stand | Mean | 343.69 | 1165.92 | 3.09 | 1.70 | 90.40 | 4.63 | 1.50 | 2.39 | 5.00 | 24 | 27568 | 4 |
|  | S. D. | 59.08 | 106.08 | 0.74 | 0.30 | 16.89 | 1.30 | 0.26 | 0.06 |  |  |  |  |
|  | Max | 456.25 | 1365 | 4.95 | 2.21 | 127 | 7.42 | 2.01 | 2.50 |  |  |  |  |
|  | Min | 221.50 | 996 | 2.05 | 0.98 | 61.75 | 2.69 | 1.07 | 2.18 |  |  |  |  |
| Shishu Mela | Mean | 909.58 | 450 | 3.53 | 1.65 | 139.15 | 5.31 | 1.83 | 2.37 | 5.00 | 24 | 7599 | 2 |
|  | S. D. | 86.89 | 179.25 | 0.61 | 0.74 | 23.56 | 1.26 | 0.74 | 0.12 |  |  |  |  |
|  | Max | 1043.75 | 1102 | 5.27 | 2.32 | 197 | 8.05 | 3.53 | 2.59 |  |  |  |  |
|  | Min | 699.50 | 265 | 2.63 | 0.85 | 100 | 3.50 | 0.63 | 2.15 |  |  |  |  |


Abbreviations: $\mathrm{F}_{\mathrm{MV}}=$ Flow of motorized vehicles; $\mathrm{F}_{\mathrm{P}}=$ Flow of pedestrians; $\mathrm{S}_{\mathrm{MV}}=$ Speed of motorized vehicles; $\mathrm{S}_{\mathrm{P}}=$ Speed of pedestrians; $\mathrm{CF}_{\mathrm{MV}}=\mathrm{Conflicting} \mathrm{flow} \mathrm{of}$ motorized vehicles; $\mathrm{CS}_{\mathrm{MV}}=$ Conflicting speed of motorized vehicles; $\mathrm{CS}_{\mathrm{NMV}}=$ Conflicting speed of non-motorized vehicles; PCU = Passenger Car Unit; S.D. = Standard deviation.

| Parameter |  | $\mathbf{F}_{\mathrm{mv}}$ (PCU) | $\mathbf{F}_{\boldsymbol{P}}$ | $\mathbf{S}_{\text {MV }}$ (m/s per PCU) | $\mathbf{S}_{\mathbf{P}}$ (m/s) | $\mathbf{C F}_{\text {MV }}$ (PCU) | $\mathbf{C S}_{\text {MV }}$ (m/s per PCU) | $\mathbf{C S}_{\text {nMv }}$ (m/s per PCU) | PET (s) | Cycle timings (min) | Number of cycles | Total conflicts | Crash records (2016-20) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Motsho Bhaban | Mean | 1639.33 | 248.95 | 3.59 | 1.73 | 187.99 | 4.41 | 2.00 | 2.36 | 6.00 | 20 | 8662 | 8 |
|  | S. D. | 133.88 | 50.52 | 0.33 | 0.24 | 33.66 | 0.44 | 0.30 | 0.11 |  |  |  |  |
|  | Max | 1818.25 | 350 | 4.09 | 2.26 | 245.50 | 5.14 | 3.04 | 2.61 |  |  |  |  |
|  | Min | 1238.25 | 143 | 2.98 | 1.30 | 136.50 | 3.75 | 1.61 | 2.19 |  |  |  |  |
| Paltan | Mean | 915.84 | 198.29 | 6.61 | 1.96 | 107.39 | 8.56 | 3.26 | 2.47 | 5.00 | 24 | 16229 | 4 |
|  | S. D. | 144.78 | 30.05 | 1.17 | 0.55 | 19.50 | 1.58 | 0.58 | 0.06 |  |  |  |  |
|  | Max | 1190 | 261 | 8.57 | 2.35 | 151.75 | 10.60 | 4.31 | 2.63 |  |  |  |  |
|  | Min | 685 | 134 | 5.01 | 1.32 | 68 | 6.58 | 1.94 | 2.38 |  |  |  |  |
| Shahbagh | Mean | 553.70 | 192.93 | 5.17 | 1.82 | 95.34 | 7.37 | 2.03 | 2.53 | 4.00 | 30 | 11342 | 3 |
|  | S. D. | 120 | 37.74 | 1.10 | 0.89 | 39.24 | 1.23 | 0.95 | 0.08 |  |  |  |  |
|  | Max | 855.25 | 317 | 7.80 | 2.22 | 198 | 9.57 | 3.11 | 2.71 |  |  |  |  |
|  | Min | 339.75 | 142 | 4.31 | 1.05 | 43 | 5.90 | 1.37 | 2.35 |  |  |  |  |
| Bijoy Sarani | Mean | 923.49 | 181.13 | 6 | 1.91 | 109.78 | 8.06 | 2.14 | 2.22 | 4.00 | 30 | 5865 | 4 |
|  | S. D. | 112.25 | 40.01 | 0.93 | 0.45 | 36.98 | 1.17 | 0.63 | 0.25 |  |  |  |  |
|  | Max | 1163.50 | 281 | 7.21 | 2.39 | 173 | 9.96 | 3.12 | 2.82 |  |  |  |  |
|  | Min | 698.75 | 104 | 4.44 | 1.18 | 46 | 5.81 | 1.55 | 1.76 |  |  |  |  |
| Bangla Motor | Mean | 590.52 | 182.94 | 4.94 | 1.79 | 175.54 | 6.81 | 2.35 | 2.41 | 3.75 | 32 | 25223 | 4 |
|  | S. D. | 178.77 | 46.58 | 1.23 | 0.74 | 23.61 | 1.27 | 0.81 | 0.06 |  |  |  |  |
|  | Max | 891.50 | 284 | 6.18 | 2.48 | 228 | 9.10 | 4.04 | 2.54 |  |  |  |  |
|  | Min | 361.75 | 122 | 3.98 | 1.15 | 138.50 | 5.12 | 1.39 | 2.28 |  |  |  |  |

Abbreviations: FMV = Flow of motorized vehicles; FP = Flow of pedestrians; SMV = Speed of motorized vehicles; SP = Speed of pedestrians; CFMV = Conflicting flow of motorized vehicles; CSMV = Conflicting speed of motorized vehicles; CSNMV = Conflicting speed of non-motorized vehicles; DIC=Deviance Information Criterion; S.D. = Standard deviation.

Table 2. Summary of the model estimation results
| Model | Model 1 |  |  |  | Model 2(a) |  |  |  | Model 2(b) |  |  |  |  | Model 2(c) |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Parameter |  | Mean | S. D. | 2.5\% | 97.5\% | Mean | S. D. | 2.5\% | 97.5\% | Mean | S. D. | 2.5\% | 97.5\% | Mean | S. D. | 2.5\% | 97.5\% |
| Location | $\mu_{0}$ | 2.319 | 0.011 | 2.295 | 2.34 | 2.385 | 0.029 | 2.328 | 2.423 | 2.099 | 0.0003 | 2.098 | 2.099 | 2.153 | 0.058 | 2.007 | 2.244 |
|  | $\mu_{\text {FMV }}$ | - | - | - | - | -0.0004 | 0.0002 | -0.001 | -0.0001 | - | - | - | - | 0.0002 | 0.0002 | -0.001 | 0.001 |
|  | $\mu_{\mathrm{FP}}$ | - | - | - | - | -0.0001 | 0.0001 | -0.0003 | 0.0002 | - | - | - | - | 0.0004 | 0.0004 | -0.001 | 0.001 |
|  | $\mu_{\text {smv }}$ | - | - | - | - | -0.034 | 0.006 | -0.044 | -0.021 | - | - | - | - | -0.009 | 0.008 | -0.025 | 0.004 |
|  | $\mu_{\text {SP }}$ | - | - | - | - | 0.012 | 0.004 | 0.005 | 0.02 | - | - | - | - | 0.013 | 0.005 | 0.002 | 0.022 |
|  | $\mu_{\text {CFMV }}$ | - | - | - | - | 0.001 | 0.001 | -0.001 | 0.003 | - | - | - | - | 0.0004 | 0.002 | -0.006 | 0.003 |
|  | $\mu_{\text {CSMV }}$ | - | - | - | - | 0.009 | 0.003 | 0.002 | 0.015 | - | - | - | - | 0.003 | 0.004 | -0.003 | 0.011 |
|  | $\mu_{\text {CSNMV }}$ | - | - | - | - | 0.01 | 0.003 | 0.002 | 0.016 | - | - | - | - | 0.005 | 0.005 | -0.003 | 0.015 |
| Scale | $\sigma_{0}$ | 1.36 | 0.002 | 1.355 | 1.364 | 1.359 | 0.007 | 1.347 | 1.364 | 12.01 | 0.0004 | 12.01 | 12.01 | 2.389 | 2.67 | 1.337 | 9.736 |
|  | $\sigma_{\text {FMV }}$ | - | - | - | - | - | - | - | - | -0.003 | 0.0002 | -0.004 | -0.003 | -0.004 | 0.01 | -0.031 | 0.0003 |
|  | $\sigma_{\mathrm{FP}}$ | - | - | - | - | - | - | - | - | -0.011 | 0.0002 | -0.011 | -0.011 | -0.005 | 0.013 | -0.048 | 0.001 |
|  | $\sigma_{\text {SMV }}$ | - | - | - | - | - | - | - | - | 0.00001 | 0.0003 | -0.0002 | 0.0004 | -0.006 | 0.018 | -0.055 | 0.004 |
|  | $\sigma_{\mathrm{SP}}$ | - | - | - | - | - | - | - | - | -0.007 | 0.0004 | -0.008 | -0.007 | -0.003 | 0.01 | -0.033 | 0.004 |
|  | $\sigma_{\text {CFMV }}$ | - | - | - | - | - | - | - | - | -0.018 | 0.0003 | -0.018 | -0.017 | -0.005 | 0.01 | -0.033 | -0.0001 |
|  | $\sigma_{\text {CSMV }}$ | - | - | - | - | - | - | - | - | -0.005 | 0.0003 | -0.006 | -0.005 | -0.006 | 0.013 | -0.047 | 0.001 |
|  | $\sigma_{\text {CSNMV }}$ | - | - | - | - | - | - | - | - | -0.005 | 0.0001 | -0.005 | -0.005 | -0.001 | 0.004 | -0.013 | 0.001 |
| Shape | $\xi_{0}$ | -0.41 | 0.013 | -0.433 | -0.381 | -0.413 | 0.013 | -0.437 | -0.385 | -3.87 | 0.004 | -3.874 | -3.864 | -0.553 | 0.398 | -1.747 | -0.379 |
| DIC |  | 7164 |  |  |  | 7125 |  |  |  |  | 16720 |  |  |  | 7087 |  |  |


Abbreviations: FMV = Flow of motorized vehicles; FP = Flow of pedestrians; SMV = Speed of motorized vehicles; SP = Speed of pedestrians; CFMV = Conflicting flow of motorized vehicles; CSMV = Conflicting speed of motorized vehicles; CSNMV = Conflicting speed of non-motorized vehicles; DIC=Deviance Information Criterion; S.D. = Standard deviation.

| Model | Model 3(a) |  |  |  |  |  | Model 3(b) |  |  |  |  | Model 4 |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Parameter |  | Mean | S. D. | 2.5\% | 97.5\% | $\theta$ | Mean | S. D. | 2.5\% | 97.5\% | $\theta$ | Mean | S. D. | 2.5\% | 97.5\% | $\theta$ |
| Location | $\mu_{0}$ | 1.759 | 0.705 | 0.044 | 2.831 | - | 2.057 | 0.406 | 1.165 | 3.002 | - | 1.952 | 0.044 | 1.871 | 2.046 | - |
|  | $\mu_{\text {FMV }}$ | 0.513 | 0.835 | -0.793 | 2.141 | -0.591 | -28.81 | 77.65 | -247.3 | 86.11 | -1.011 | -4.66 | 6.515 | -14.44 | 0.816 | -0.099 |
|  | $\mu_{\mathrm{FP}}$ | 0.165 | 0.281 | -0.537 | 0.812 | -0.698 | -3.491 | 6.18 | -16.34 | -0.29 | -0.782 | -9.901 | 8.145 | -19.36 | 0.412 | -0.908 |
|  | $\mu_{\text {SMV }}$ | 0.261 | 0.447 | -0.707 | 1.126 | -0.185 | 0.074 | 0.34 | -0.297 | 1.065 | 0.3 | -0.064 | 0.076 | -0.185 | 0.008 | -0.35 |
|  | $\mu_{\mathrm{SP}}$ | -0.12 | 0.473 | -1.063 | 0.561 | -1.027 | 0.333 | 0.498 | 0.003 | 1.808 | -0.448 | -0.084 | 0.047 | -0.168 | -0.017 | -0.157 |
|  | $\mu_{\text {CFMV }}$ | -0.449 | 0.404 | -1.198 | 0.496 | 0.145 | -1.025 | 1.844 | -4.517 | 3.698 | -0.622 | -0.84 | 0.85 | -1.832 | -0.006 | -1.253 |
|  | $\mu_{\text {CSMV }}$ | -0.14 | 0.396 | -1.227 | 0.545 | -0.97 | -0.078 | 0.363 | -0.617 | 0.679 | -0.964 | -0.764 | 0.605 | -1.605 | -0.152 | -0.078 |
|  | $\mu_{\text {CSNMV }}$ | 0.381 | 0.597 | -0.132 | 1.978 | 0.14 | 0.28 | 0.438 | -0.025 | 1.545 | 0.909 | 0.008 | 0.003 | 0.0009 | 0.015 | 0.005 |
| Scale | $\sigma_{0}$ | 1.359 | 0.003 | 1.355 | 1.364 | - | 4.892 | 3.418 | 1.339 | 8.336 | - | 10.67 | 0.747 | 9.93 | 11.77 | - |
|  | $\sigma_{\text {FMV }}$ | - | - | - | - | - | 0.00001 | 0.002 | -0.0002 | 0.0005 | 0.0003 | -0.039 | 0.01 | -0.049 | -0.026 | 0.932 |
|  | $\sigma_{\mathrm{FP}}$ | - | - | - | - | - | -0.009 | 0.01 | -0.019 | 0.0006 | 0.0014 | -0.025 | 0.015 | -0.042 | -0.01 | 0.736 |
|  | $\sigma_{\text {SMV }}$ | - | - | - | - | - | -0.008 | 0.01 | -0.018 | 0.003 | -0.003 | -0.099 | 0.058 | -0.167 | -0.027 | -0.637 |
|  | $\sigma_{\mathrm{SP}}$ | - | - | - | - | - | -0.012 | 0.013 | -0.03 | 0.003 | 0.0004 | -0.037 | 0.012 | -0.059 | -0.024 | 0.633 |
|  | $\sigma_{\text {CFMV }}$ | - | - | - | - | - | -0.009 | 0.009 | -0.017 | -0.0009 | -0.0008 | -0.03 | 0.019 | -0.056 | -0.009 | 0.951 |
|  | $\sigma_{\text {CSMV }}$ | - | - | - | - | - | -0.01 | 0.009 | -0.022 | 0.0006 | 0.001 | -0.032 | 0.019 | -0.06 | -0.011 | 0.49 |
|  | $\sigma_{\text {CSNMV }}$ | - | - | - | - | - | -0.001 | 0.002 | -0.007 | 0.0003 | 0.0011 | -0.046 | 0.064 | -0.206 | -0.007 | 0.817 |
| Shape | $\xi_{0}$ | -0.41 | 0.013 | -0.434 | -0.384 | - | -1.215 | 0.790 | -2.071 | -0.387 | - | -2.28 | 0.477 | -2.784 | -1.781 | - |
| DIC |  |  |  | 7062 |  |  |  |  | 7064 |  |  |  |  | 15470 |  |  |

Abbreviations: FMV = Flow of motorized vehicles; FP = Flow of pedestrians; SMV = Speed of motorized vehicles; SP = Speed of pedestrians; CFMV = Conflicting flow of motorized vehicles; CSMV = Conflicting speed of motorized vehicles; CSNMV = Conflicting speed of non-motorized vehicles; DIC = Deviance Information Criterion; S.D. = Standard deviation; $\theta=$ exponent of the covariates of location or scale parameter.

## 5. Results and discussion

### 5.1. Model development

This study estimated four types of Bayesian extreme value models, incorporating covariates into the GEV distribution parameters through both linear (Model 1 and Model 2)) and nonlinear (Model 3 and Model 4) link functions. Model 1 serves as the baseline stationary model $\left(\alpha_{\mu 1}=\alpha_{\phi 1}=0\right)$, where no covariates are added to the location or scale parameters. In contrast, Model 2 applies a linear link function to the location and log-linear link function scale parameters, resulting in three sub-models: Model 2(a) includes covariates only in the location parameter, Model 2(b) incorporates covariates solely in the scale parameter, and Model 2(c) adds covariates to both parameters.

Model 3 introduces non-linear link functions for the location parameter while maintaining log-linear link functions for the scale parameter. Under this framework, two sub-models were estimated: Model 3(a), which includes covariates only in the location parameter, and Model 3(b), where covariates are incorporated into both the location and scale parameters. Model 4 represents the most complex scenario, with non-linear link functions for both the location and scale parameters, exploring the non-stationary nature of these relationships. The goal was to examine the impact of incorporating covariates into both parameters (i.e. location and scale), thus gaining deeper insights into the influence of covariates on model sensitivity under varying conditions.

Additional configurations, such as incorporating non-linear link functions for the scale parameter while retaining linear functions for the location parameter, and those adding covariates exclusively to either the scale or location parameters in Models 3 and 4, were tested but did not converge. The shape parameter was not parameterized due to convergence difficulties and estimation imprecision (Coles, 2001). A range of covariate combinations were evaluated, and the best-performing model was selected based on goodness-of-fit metrics.

Table 2 presents the DIC values used to compare the performance of all seven sub-models. The results indicate that Models 1, 2(a), and 2(c) perform well, whereas Model 2(b) is the least effective; it indicates that the scale parameter does not align properly with the covariates and the Model 2(b) has the highest intercept value of 12.01 . Model 4, with a DIC value of 15,470 , suggests that incorporating non-linear link functions for both the location and scale parameters does not lead to optimal model convergence. In contrast, Model 3 stands out with the lowest DIC value among the three types of models, indicating that the approach of assigning nonlinear relationships among covariates of the location parameter while maintaining log-linear relationships for the scale parameter is more effective. Although Models 3(a) and 3(b) have very close DIC values, Model 3(a) emerges as the best model overall due to its lowest DIC value along with the lowest intercept value in both location and scale parameters.

The dependent variable, PET, was used as the key traffic conflict indicator for each cycle in all models. Each of the seven sub-models was estimated using two separate MCMC chains initialized with different values. A total of 76,000 iterations were performed, with the first 26,000 discarded as burn-in samples to ensure convergence. Posterior estimates were derived from the remaining 50,000 iterations. Model convergence was confirmed through two diagnostic methods: first, a visual inspection of trace plots showed well-mixed chains,
indicating no sensitivity to initial values; second, the Gelman-Rubin statistic was calculated for each parameter, with most values below the threshold of 1.1, further confirming convergence (Ali et al., 2023a). Figures A4 and Figure A5 (see Appendix) illustrate the trace plots and Gelman-Rubin statistics (BGR diagrams) for Model 3(a), where covariates were added only to the location parameter.

Since the speeds of vehicles and pedestrians are used to calculate post-encroachment time, directly considering them in the extreme value model could introduce endogeneity issues. To circumvent this problem, instead of using the instantaneous speeds of vehicles and pedestrians, the aggregated space mean speed of each block was used as a covariate in the model.

### 5.2. Model interpretation

Model 3(a) reveals significant relationships between various covariates and crash risk, providing an in-depth understanding of the factors influencing pedestrian safety at intersections. The coefficient terms in the location parameter indicate the direction and strength of each covariate's association with crash risk, with positive values suggesting an increase and negative values a decrease in risk. The exponent terms quantify the sensitivity of crash risk to these covariates, with larger absolute values reflecting greater impact. An exponent of zero signifies no influence on crash risk. This model underscores the critical factors driving pedestrian crashes at intersections, offering insights into how changes in these variables can affect risk, thus guiding the development of targeted safety interventions. Table 2 shows that pedestrian speed is the most influencing variable in predicting pedestrian crash risk having a coefficient value of -0.12 and exponent -1.027. Table 3 provides a concise summary of these relationships, highlighting the direction of each covariate's influence, and the interpretation of the exponents derived from the data. The table shows that flow covariates for motorized vehicles and pedestrians contribute positively to the crash risk. On the other hand, although motorized vehicle speed contributes to the crash risk, the crash risk reduces with increasing pedestrian speed. Motorized vehicles' conflicting volume and speed contribute negatively to the crash risk, whereas the conflicting speed of non-motorized vehicles contributes positively to the crash risk. Further explanations are illustrated in Table 3.

### 5.3.Model evaluation and comparison

The estimated Bayesian extreme value model undergoes evaluation before its use in realtime crash risk assessment, with the evaluation comparing the crashes predicted by the model to the actual crashes observed over a defined period. To facilitate this comparison, the mean number of estimated crashes over T years is calculated using the formula proposed by Zheng et al. (2019a), as shown in Equation (9):

$$
N=\frac{T}{t} * \sum_{i=1}^{m} M R C_{i}
$$

Here, $N$ represents the expected number of crashes during the duration T, where t refers to the video recording duration, MRC denotes the modified crash risk (considering only positive MRC values), and m is the total number of cycles. MRC values are computed as per

Equation (8). For instance, if $T=5$ years, then $N$ provides an estimate of the expected number of crashes over those five years. In Equation (8), the parameter $Z_{c r}$ is assigned a value of 1.45, representing a 93\% confidence level, which was carefully chosen to balance confidence and precision, ensuring reliability while avoiding overfitting. Researchers applying this model to different locations, traffic conditions, or datasets are advised to calibrate the confidence level according to their specific circumstances. Sensitivity analyses are recommended to identify the optimal confidence level for various scenarios, with the 93\% level serving as a guideline rather than a fixed standard.

Table 3. Summary of covariates influencing pedestrian crash risk at intersections
| Covariate | Relationship with crash risk | Exponent interpretation |
| :--- | :--- | :--- |
| Flow of motorized vehicles | Positive: Raises crash risk due to higher pedestrianvehicle interactions. | Large negative exponent: Effect diminishes significantly at high volumes as congestion slows vehicles, creating stop-and-go conditions. |
| Flow of pedestrians | Positive: Increase exposure to potential crashes. | High negative exponent: Marginal risk increase diminishes at higher volumes as drivers become more cautious, and slower vehicle speeds. |
| Speed of motorized vehicles | Positive: Higher speeds significantly increase crash risk. | Relatively low negative exponent: Marginal effect of increasing speed diminishes at higher velocities as drivers adopt more cautious behaviors. |
| Speed of pedestrians | Negative: Initially reduces crash risk by minimizing time in conflict areas. | High exponent: Risk reduction diminishes at higher pedestrian speeds as focus on maintaining pace may reduce awareness. |
| Conflicting flow of motorized vehicles | Negative: Reduces crash risk due to slower speeds and cautious driving. | Smaller positive exponent: Risk reduction becomes less significant as conflicting flow increases. |
| Conflicting speed of motorized vehicles | Negative: Initially reduce crash risk as drivers become more vigilant. | Strongly negative exponent: At very high speeds, reduced reaction time and longer stopping distances increase risk. |
| Conflicting speed of non-motorized vehicles | Positive: Increase crash risk due to potential driver misjudgments and less protective structures. | Small positive exponent: While risk rises with speed, the rate of increase diminishes at higher speeds. |


From 2016 to 2020, a total of 36 crashes were observed across the nine studied locations. In comparison, the mean estimated crashes for Models 1, 2(a), 2(b), 2(c), 3(a), 3(b), and 4 are 0, 137.47, 26.34, 697.64, 40.57, 566.25, and 78.81, respectively. Among these, Model 3(a) provides the closest mean estimate to the observed crashes.

It is worth noting that adding a non-linear link function for the location parameter significantly improves the model's ability to explain the crash risk mechanism, resulting in more precise estimates. This improvement ensures a closer alignment between the estimates provided by Model 3(a) and the observed crashes, which used the MRC formula for crash risk assessment. In contrast, when the generic crash risk equation was applied, Model 3(a) estimated
an implausible figure of 388,392 crashes under heterogeneous traffic conditions. This substantial deviation highlights the superiority of the MRC method in providing a more reliable estimation of crash risks within the complexities of non-lane-based, heterogeneous traffic environments.

### 5.4. Real-time crash risk assessment

For each signal cycle, distinct GEV distributions are generated for Model 3(a), incorporating the specific covariates for that cycle. To illustrate this concept, Figure A3 (see Appendix) presents a set of three randomly selected cycles from each intersection, indicating cycle numbers within each subfigure, with areas of positive crash risk highlighted in red.

The shape of the estimated GEV distribution is crucial for real-time vehicle-pedestrian crash risk assessment, as it reveals crash-prone conditions. A positive crash risk is indicated when the tail of the GEV distribution extends before the PET reaches zero. As shown in Figure A3 (see Appendix), all signal cycles at the studied intersections exhibit a positive crash risk, with their distributions extending before the PET reaches zero. Data for this analysis were collected from various intersections in Dhaka, a densely populated city characterized by heterogeneous traffic conditions. The lack of lane discipline and the high-risk crossing behaviour of pedestrians at these intersections contribute to the presence of positive crash risks across all cycles.

Identifying high-risk cycles enables road authorities to take real-time actions to mitigate pedestrian crash risk. Practical interventions include dedicating green time for pedestrians, restricting permissive right/left turns by giving pedestrian priority, and anticipating crash risks in upcoming cycles using this framework can significantly improve pedestrian safety in environments with heterogeneous traffic.

## 6. Conclusions and practical applications

This study develops a novel framework for real-time estimation of vehicle-pedestrian crash risk at signalized intersections, explicitly accounting for vehicle heterogeneity in mixed, nonlane-based traffic environments. By integrating both motorized vehicles (MVs) and nonmotorized vehicles (NMVs) within a unified modeling framework, the approach provides a more comprehensive and realistic assessment of pedestrian crash risk in Dhaka's complex urban traffic. The proposed framework employs the Block Maxima (BM) approach of Extreme Value Theory (EVT), corresponding to a Generalized Extreme Value (GEV) distribution, to identify extreme traffic conflicts derived from Post-Encroachment Time (PET) values at the signal-cycle level. A hierarchical Bayesian modeling structure was utilized to estimate timevarying crash risks across four tee and five cross intersections. This framework underscores the significance of incorporating traffic heterogeneity in pedestrian safety research and demonstrates the potential of EVT-based methods for proactive safety assessment under mixed-traffic conditions.

A major contribution of this research lies in the introduction and evaluation of multiple Bayesian GEV models incorporating both linear and non-linear link functions. By allowing the GEV parameters to vary with relevant covariates, the study captures the non-stationary and
non-linear dynamics of traffic extremes more effectively. Model 3 introduced a non-linear link function to the location parameter and a log-linear link function to the scale parameter, with Model 3(a) which added covariates only to the location parameter emerging as the bestperforming model, evidenced by its lowest DIC value. The findings confirm that non-linear link functions improve the model's flexibility in representing complex, non-monotonic relationships between traffic variables and crash risk.

Another key contribution of this study is the introduction of a behavior-normalized Modified Crash Risk (MRC) metric that corrects the overestimation tendency of conventional models by accounting for pedestrians' habitual risk-taking behavior in congested, mixed-traffic conditions. In such environments, the frequent risk-taking behaviour of pedestrians leads to a higher occurrence of conflict events. Pedestrian speed is found to be the most influencing variable in predicting pedestrian crash risk and contributes negatively. The flow and speed of MVs, flow of pedestrians, and the conflicting speed of NMVs contribute positively to the crash risk.

The findings from this research offer important implications for both policy and methodological advancements. First, they demonstrate that EVT-based crash risk modeling, when extended with non-linear link functions, provides a theoretically sound and practically robust framework for real-time safety analysis. Second, incorporating behavioral normalization through the MRC metric ensures that model outcomes align more closely with observed risktaking behaviors in developing urban contexts such as Dhaka. In the future, integrating sociodemographic variables such as pedestrian age and gender could further enhance the model by capturing behavioral heterogeneity in pedestrian crash risk estimation.

## CRediT Authorship Contribution Statement

Parvez Anowar: Writing - original draft, Writing - review \& editing, Visualization, Validation, Software, Methodology, Investigation, Data curation, Conceptualization. Nazmul Haque: Writing - review \& editing, Visualization, Validation, Supervision, Software, Methodology, Conceptualization. Md Asif Raihan: Writing - review \& editing, Visualization, Validation, Supervision, Conceptualization. Md Hadiuzzaman: Writing - review \& editing, Validation, Supervision, Project administration, Conceptualization.

## Acknowledgement

This work is funded by Research Expenses (Regular) Fund (Docket No.: 1718, Sector No.: 3257103(A)), by the Department of Civil Engineering, Bangladesh University of Engineering and Technology (BUET), Bangladesh.

## Disclosure statement

The authors report that they do not have any competing interests to declare.

## Data availability statement

The data used in this study are available from the corresponding author upon reasonable request.

## ORCID

Parvez Anowar: https://orcid.org/0009-0000-3656-237X
Nazmul Haque: https://orcid.org/0009-0006-4698-3366
Md Asif Raihan: https://orcid.org/0009-0005-1762-8528
Md Hadiuzzaman: https://orcid.org/0000-0002-5690-3351

## References

Adlouni, S. E., Ouarda, T. B. M. J., Zhang, X., Roy, R., \& Bobée, B. (2007). Generalized maximum likelihood estimators for the nonstationary generalized extreme value model. Water Resources Research, 43(3). https://doi.org/10.1029/2005wr004545
Ali, Y., Haque, M. M., \& Mannering, F. (2023a). A Bayesian generalised extreme value model to estimate real-time pedestrian crash risks at signalised intersections using artificial intelligence-based video analytics. Analytic Methods in Accident Research, 38, 100264. https://doi.org/10.1016/j.amar.2022.100264
Ali, Y., Haque, M. M., \& Zheng, Z. (2022). An Extreme Value Theory approach to estimate crash risk during mandatory lane-changing in a connected environment. Analytic Methods in Accident Research, 33, 100193. https://doi.org/10.1016/j.amar.2021.100193
Ali, Y., Washington, S., \& Haque, M. M. (2023b). Estimating real-time crash risk at signalized intersections: A Bayesian Generalized Extreme Value approach. Safety Science, 164, 106181. https://doi.org/10.1016/j.ssci.2023.106181
Ali, Y., Zheng, Z., Haque, M. M., Yildirimoglu, M., \& Washington, S. (2021). CLACD: A complete LAne-Changing decision modeling framework for the connected and traditional environments. Transportation Research Part C Emerging Technologies, 128, 103162. https://doi.org/10.1016/j.trc.2021.103162
Allen, B. L., Shin, B. T., \& Cooper, P. J. (1978). Analysis of traffic conflicts and collisions. Transportation Research Record Journal of the Transportation Research Board, 667. https://trid.trb.org/view.aspx?id=85806
Alozi, A. R., \& Hussein, M. (2022). Evaluating the safety of autonomous vehicle-pedestrian interactions: An extreme value theory approach. Analytic Methods in Accident Research, 35, 100230. https://doi.org/10.1016/j.amar.2022.100230
Ankunda, A., Ali, Y., \& Mohanty, M. (2024). Pedestrian crash risk analysis using extreme value models: New insights and evidence. Accident Analysis \& Prevention, 203, 107633. https://doi.org/10.1016/j.aap.2024.107633
Arun, A., Haque, M. M., Bhaskar, A., Washington, S., \& Sayed, T. (2021). A systematic mapping review of surrogate safety assessment using traffic conflict techniques. Accident Analysis \& Prevention, 153, 106016. https://doi.org/10.1016/j.aap.2021.106016

Carrodano, C. (2024). Data-driven risk analysis of nonlinear factor interactions in road safety using Bayesian networks. Scientific Reports, 14(1). https://doi.org/10.1038/s41598-024-69740-6
Coles, S. (2001). An introduction to statistical modeling of extreme values. In Springer series in statistics. https://doi.org/10.1007/978-1-4471-3675-0
Davis, G. A., Hourdos, J., Xiong, H., \& Chatterjee, I. (2011). Outline for a causal model of traffic conflicts and crashes. Accident Analysis and Prevention, 43(6), 1907-1919. https://doi.org/10.1016/j.aap.2011.05.001
Debnath, M., Hasanat-E-Rabbi, S., Hamim, O. F., Hoque, M. S., McIlroy, R. C., Plant, K. L., \& Stanton, N. A. (2021). An investigation of urban pedestrian behaviour in Bangladesh using the Perceptual Cycle Model. Safety Science, 138, 105214. https://doi.org/10.1016/j.ssci.2021.105214
DTCA, J., 2015. The Project on the Revision and Updating of the Strategic Transport Plan for Dhaka. Dhaka Transport Coordination Authority (DTCA).
El-Basyouny, K., \& Sayed, T. (2009). Urban Arterial Accident Prediction Models with Spatial Effects. Transportation Research Record Journal of the Transportation Research Board, 2102(1), 27-33. https://doi.org/10.3141/2102-04
Fattah, M. A., Morshed, S. R., Morshed, S. Y., Hoque, M. M., \& Haque, M. N. (2021). The impact of urban street median in pedestrian behavior and traffic flow: Experience from a growing city Khulna, Bangladesh. Transportation Engineering, 6, 100090. https://doi.org/10.1016/j.treng.2021.100090
Fisher, R. A., \& Tippett, L. H. C. (1928). Limiting forms of the frequency distribution of the largest or smallest member of a sample. Mathematical Proceedings of the Cambridge Philosophical Society, 24(2), 180-190. https://doi.org/10.1017/s0305004100015681
Fu, C., \& Sayed, T. (2021). Multivariate Bayesian hierarchical Gaussian copula modeling of the non-stationary traffic conflict extremes for crash estimation. Analytic methods in accident research, 29, 100154.
Fu, C., \& Sayed, T. (2023). Identification of adequate sample size for conflict-based crash risk evaluation: An investigation using Bayesian hierarchical extreme value theory models. Analytic Methods in Accident Research, 39, 100281. https://doi.org/10.1016/j.amar.2023.100281
Guo, Y., Sayed, T., \& Zheng, L. (2020). A hierarchical bayesian peak over threshold approach for conflict-based before-after safety evaluation of leading pedestrian intervals. Accident Analysis and Prevention, 147, 105772. https://doi.org/10.1016/j.aap.2020.105772
Hadiuzzaman, M., Haque, N., Rahman, F., Hossain, S., Siam, M.R.K. and Qiu, T.Z., 2017. Pixel-based heterogeneous traffic measurement considering shadow and illumination variation. Signal, Image and Video Processing, 11, pp.1245-1252. https://doi.org/10.1007/s11760-017-1081-z
Haque, N., Hadiuzzaman, M., Rahman, F. and Siam, M.R.K., 2020. Real-time motion trajectory based head-on crash probability estimation on two-lane undivided highway. Journal of Transportation Safety \& Security, 12(10), pp.1312-1337. https://doi.org/10.1080/19439962.2019.1597001
Hoque, I., Ananda, T. N., Anowar, P., Naz, A., \& Murshed, M. N. (2025). Machine Learning Approach in Calibrating VISSIM Microsimulation Model for Mixed Traffic

Conditions. Journal of Engineering Science, 16(1), 21-30. https://doi.org/10.3329/jes.v16i1.82663
Hyden, C. (1987). The development of a method for traffic safety evaluation: the swedish traffic conflicts technique. Bulletin Lund Institute of Technology, Department, (70). https://trid.trb.org/view/239059
Islam, M., Haque, N., \& Hadiuzzaman, M. (2024). DEEGITS: Deep Learning based Framework for Measuring Heterogenous Traffic State in Challenging Traffic Scenarios. In 103rd Annual Meeting of Transportation Research BoardAt: Washington, D.C.
Lao, Y., Zhang, G., Wang, Y., \& Milton, J. (2013). Generalized nonlinear models for rear-end crash risk analysis. Accident Analysis \& Prevention, 62, 9-16. https://doi.org/10.1016/j.aap.2013.09.004
Laureshyn, A., Svensson, Å., \& Hydén, C. (2010). Evaluation of traffic safety, based on microlevel behavioural data: Theoretical framework and first implementation. Accident Analysis \& Prevention, 42(6), 1637-1646. https://doi.org/10.1016/j.aap.2010.03.021
Lee, J., Abdel-Aty, M., \& Jiang, X. (2015). Multivariate crash modeling for motor vehicle and non-motorized modes at the macroscopic level. Accident Analysis and Prevention, 78, 146-154. https://doi.org/10.1016/j.aap.2015.03.003
Li, J., Russell, B. T., Huang, W. K., \& Porter, W. C. (2024). Modeling nonstationary surfacelevel ozone extremes through the lens of US air quality standards: A Bayesian hierarchical approach. Environmetrics. https://doi.org/10.1002/env. 2882
Mackay, E., \& Jonathan, P. (2020). Assessment of return value estimates from stationary and non-stationary extreme value models. Ocean Engineering, 207, 107406. https://doi.org/10.1016/j.oceaneng.2020.107406
Noman, G. A., Tahmid, M. M., Raihan, M. A., \& Hoque, M. S. (2023, July). Artificial Intelligence-based Perceived Motorcycle Risk Prediction in Bangladesh's Urban Driving Environment. In International Conference on Advances in Civil Infrastructure and Construction Materials (pp. 379-388). Cham: Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-63280-8_39
Ntzoufras, I., 2011. Bayesian modeling using WinBUGS. John Wiley \& Sons.
Panagoulia, D., Economou, P., \& Caroni, C. (2013). Stationary and nonstationary generalized extreme value modelling of extreme precipitation over a mountainous area under climate change. Environmetrics, 25(1), 29-43. https://doi.org/10.1002/env. 2252
Robin, Y., \& Ribes, A. (2020). Nonstationary extreme value analysis for event attribution combining climate models and observations. Advances in Statistical Climatology, Meteorology and Oceanography, 6(2), 205-221. https://doi.org/10.5194/ascmo-6-205-2020
Sadeek, S. N., Rahman, M. H., \& Rifaat, S. M. (2025). Understanding pedestrian bridge usage considering perception and socio-demographic characteristics of the road users in Dhaka city. Transportation Research Interdisciplinary Perspectives, 31, 101384. https://doi.org/10.1016/j.trip.2025.101384
Sakib, N., Paul, T., Ahmed, M. T., Momin, K. A., \& Barua, S. (2023). Investigating factors influencing pedestrian crosswalk usage behavior in Dhaka city using supervised machine learning techniques. Multimodal Transportation, 3(1), 100108. https://doi.org/10.1016/j.multra.2023.100108

Saunier, N., \& Sayed, T. (2008). Probabilistic Framework for Automated analysis of exposure to road collisions. Transportation Research Record, 2083(1), 96-104. https://doi.org/10.3141/2083-11
Song, X., Lu, F., Wang, H., Xiao, W., \& Zhu, K. (2018). Penalized maximum likelihood estimators for the nonstationary Pearson type 3 distribution. Journal of Hydrology, 567, 579-589. https://doi.org/10.1016/j.jhydrol.2018.10.035
Songchitruksa, P., \& Tarko, A. P. (2006). The extreme value theory approach to safety estimation. Accident Analysis and Prevention, 38(4), 811-822. https://doi.org/10.1016/j.aap.2006.02.003
Spiegelhalter, D. J., Best, N. G., Carlin, B. P., \& Van Der Linde, A. (2002). Bayesian measures of model complexity and fit. Journal of the Royal Statistical Society. Series B, Statistical Methodology, 64(4), 583-639. https://doi.org/10.1111/1467-9868.00353
Svensson, Å., \& Hydén, C. (2006). Estimating the severity of safety related behaviour. Accident Analysis \& Prevention, 38(2), 379-385. https://doi.org/10.1016/j.aap.2005.10.009
Tahir, H. B., \& Haque, M. M. (2024). A non-stationary bivariate extreme value model to estimate real-time pedestrian crash risk by severity at signalized intersections using artificial intelligence-based video analytics. Analytic Methods in Accident Research, 43, 100339. https://doi.org/10.1016/j.amar.2024.100339
Tahmid, M. M., Raihan, M. A., Salam, S., Muktadir, M. A., \& Hoque, M. S. (2024). Analysis of heterogeneous motorcycle risk perception and crash exposure in a developing country's urban driving environment: Precursors and policy implications using structural equation modeling (Paper No. TRBAM-24-02246). Paper presented at the 103rd Annual Meeting of the Transportation Research Board, Washington, D.C. https://doi.org/10.13140/RG.2.2.12192.65280
Um, M., Kim, Y., Markus, M., \& Wuebbles, D. J. (2017). Modeling nonstationary extreme value distributions with nonlinear functions: An application using multiple precipitation projections for U.S. cities. Journal of Hydrology, 552, 396-406. https://doi.org/10.1016/j.jhydrol.2017.07.007
Xie, D., Gao, Z., Zhao, X., \& Li, K. (2009). Characteristics of mixed traffic flow with nonmotorized vehicles and motorized vehicles at an unsignalized intersection. Physica a Statistical Mechanics and Its Applications, 388(10), 2041-2050. https://doi.org/10.1016/j.physa.2009.01.033
Youngman, B. D. (2022). evgam: An R Package for Generalized Additive Extreme Value Models. Journal of Statistical Software, 103(3). https://doi.org/10.18637/jss.v103.i03
Zafri, N. M. (2023). Walk or run? An observational study to explore pedestrian crossing decision-making at intersections in Dhaka, Bangladesh applying rules mining technique. Transportation Research Part F Traffic Psychology and Behaviour, 94, 83-98. https://doi.org/10.1016/j.trf.2023.02.003
Zhang, S., \& Abdel-Aty, M. (2022). Real-Time Pedestrian conflict prediction model at the signal cycle level using machine learning models. IEEE Open Journal of Intelligent Transportation Systems, 3, 176-186. https://doi.org/10.1109/ojits.2022.3155126

Zheng L, Ismail K, Meng X. 2014. Freeway safety estimation using extreme value theory approaches: A comparative study. Accid Anal Prev. 62:32-41. doi:10.1016/j.aap.2013.09.006.
Zheng, L., Ismail, K., \& Meng, X. (2014). Freeway safety estimation using extreme value theory approaches: A comparative study. Accident Analysis and Prevention, 62, 32-41. https://doi.org/10.1016/j.aap.2013.09.006
Zheng, L., \& Sayed, T. (2019). From univariate to bivariate extreme value models: Approaches to integrate traffic conflict indicators for crash estimation. Transportation research part C: emerging technologies, 103, 211-225.
Zheng, L., \& Sayed, T. (2020). A novel approach for real time crash prediction at signalized intersections. Transportation Research. Part C, Emerging Technologies, 117, 102683. https://doi.org/10.1016/j.trc.2020.102683
Zheng, L., Sayed, T., \& Essa, M. (2019a). Bayesian hierarchical modeling of the non-stationary traffic conflict extremes for crash estimation. Analytic Methods in Accident Research, 23, 100100. https://doi.org/10.1016/j.amar.2019.100100
Zheng, L., Sayed, T., \& Essa, M. (2019b). Validating the bivariate extreme value modeling approach for road safety estimation with different traffic conflict indicators. Accident Analysis \& Prevention, 123, 314-323

## Appendix

Table A1. Timetable for data collection at study sites
| Intersection name | No. of camera | Date | Time | Duration |
| :--- | :--- | :--- | :--- | :--- |
| Abul Hotel | 2 | 11/12/2023 | $4 \mathrm{pm}-6 \mathrm{pm}$ | 2 h |
| Bonolota Market | 2 | 12/12/2023 | $4 \mathrm{pm}-6 \mathrm{pm}$ | 2 h |
| Mirpur 1 Bus Stop | 2 | 14/12/2023 | 4:30 pm-6:30 pm | 2 h |
| Shishu Mela | 2 | 17/12/2023 | $4 \mathrm{pm}-6 \mathrm{pm}$ | 2 h |
| Motsho Bhaban | 2 | 18/12/2023 | $4 \mathrm{pm}-6 \mathrm{pm}$ | 2 h |
| Paltan | 2 | 20/12/2023 | $4 \mathrm{pm}-6 \mathrm{pm}$ | 2 h |
| Shahbagh | 2 | 21/12/2023 | $4 \mathrm{pm}-6 \mathrm{pm}$ | 2 h |
| Bijoy Sarani | 2 | 27/12/2023 | 4:30 pm-6:30 pm | 2 h |
| Banglamotor | 2 | 28/12/2023 | 4:30 pm-6:30 pm | 2 h |


| $\mathrm{F}_{\mathrm{MV}}(\mathrm{PCU})$ | 1.00 | 1.00 |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\mathrm{F}_{\mathrm{P}}$ | -0.01 |  |  |  |  |  |  |
| $\mathrm{S}_{\mathrm{MV}}(\mathrm{m} / \mathrm{s}$ per PCU) | -0.30 | -0.71 | 1.00 |  |  |  |  |
| $\mathrm{S}_{\mathrm{P}}(\mathrm{m} / \mathrm{s})$ | 0.12 | -0.46 | 0.41 | 1.00 |  |  |  |
| $\mathrm{CF}_{\mathrm{MV}}(\mathrm{PCU})$ | 0.54 | 0.55 | -0.59 | -0.62 | 1.00 |  |  |
| $\mathrm{CS}_{\mathrm{MV}}(\mathrm{m} / \mathrm{s}$ per PCU) | -0.11 | -0.38 | 0.67 | 0.67 | -0.62 | 1.00 |  |
| $\mathrm{CS}_{\mathrm{NMV}}$ (m/s per PCU) | -0.19 | -0.67 | 0.57 | 0.53 | -0.60 | 0.54 | 1.00 |
|  | $\mathrm{F}_{\mathrm{MV}}(\mathrm{PCU})$ | H | Ệu SOT SOTED | (B) | Se er | Çâ一c Sucture | çãruncn SOTIO |

Abbreviations: $\mathrm{F}_{\mathrm{MV}}=$ Flow of motorized vehicles; $\mathrm{F}_{\mathrm{P}}=$ Flow of pedestrians; $\mathrm{S}_{\mathrm{MV}}=$ Speed of motorized vehicles; $\mathrm{S}_{\mathrm{P}}=$ Speed of pedestrians; $\mathrm{CF}_{\mathrm{MV}}=$ Conflicting flow of motorized vehicles; $\mathrm{CS}_{\mathrm{MV}}=$ Conflicting speed of motorized vehicles; $\mathrm{CS}_{\mathrm{NMV}}=$ Conflicting speed of non-motorized vehicles; PCU = Passenger Car Unit

Figure A1. Correlation heatmap among covariates

![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-29.jpg?height=1470&width=2278&top_left_y=236&top_left_x=310)
Figure A2. Real-time camera positions at the study sites

| Abul Hotel Intersection | Bonolota Market Intersection | Mirpur 1 Bus Stop Intersection |  | Shishu Mela Intersection | Motsho Bhaban Intersection |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-30.jpg?height=680&width=1695&top_left_y=296&top_left_x=304) |  |  |  |  | ![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-30.jpg?height=678&width=340&top_left_y=298&top_left_x=2109) |
| ![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-30.jpg?height=719&width=342&top_left_y=985&top_left_x=528) | ![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-30.jpg?height=679&width=343&top_left_y=1025&top_left_x=979) | ![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-30.jpg?height=679&width=344&top_left_y=1025&top_left_x=1429) |  | ![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-30.jpg?height=677&width=344&top_left_y=1027&top_left_x=1880) |  |

Figure A3. Estimated generalized extreme value distributions for sample cycles at each intersection using Model 3(a)

![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-31.jpg?height=2062&width=1530&top_left_y=290&top_left_x=281)
Figure A4. Trace plots of covariates of Model 3(a)

![](https://cdn.mathpix.com/cropped/24424e72-6f41-4941-8bd2-3cc369e2c2c3-32.jpg?height=2006&width=1547&top_left_y=245&top_left_x=277)
Figure A5. BGR diagrams of covariates of Model 3(a)

