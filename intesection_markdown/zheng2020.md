Lai Zheng*, Tarek Sayed<br>Department of Civil Engineering, The University of British Columbia, Canada

ARTICLE INFO

Keywords:
Real time crash prediction
Signalized intersection
Extreme value theory
Bayesian hierarchical model


#### Abstract

This study proposes a novel approach to predict real time crash risk at signalized intersections at the signal cycle level. The approach uses traffic conflicts extracted from informative vehicle trajectories as an intermediate for crash prediction and develops generalized extreme value (GEV) models based on conflict extremes. Moreover, a Bayesian hierarchical structure is developed for the GEV model to combine conflict extremes of different intersections, and the aim is to further improve safety estimates through borrowing strength from different intersections and accounting for non-stationarity and unobserved heterogeneity in conflict extremes. The proposed approach was applied to four signalized intersections in City of Surrey, British Columbia. Traffic conflicts measured by modified time to collision and three cycle-level traffic parameters (traffic volume, shock wave area, and platoon ratio) were extracted from collected video data using computer vision techniques, and a best fitted model was then developed. Two safety indices, risk of crash (RC) and return level of a cycle (RLC), were derived from the GEV model to quantitatively measure the safety cycle-by-cycle. The results show that the non-negative RC can directly point out cycles with crash prone traffic conditions with RC > 0, and RLC is a more flexible safety index which can differentiate between safety levels even for "safe" cycles with $\mathrm{RC}=0$. The real time crash prediction results are validated at an aggregate level by comparing to observed crashes.


## 1. Introduction

There is considerable interest in developing approaches to predict crash risk in real time with the aim at managing road safety proactively. The general objective of real time crash prediction is to assess the crash proneness of traffic conditions within a very short time window, and the hypothesis is that the probability of a crash occurring on a specified road facility in a short term can be predicted using the instantaneous traffic dynamics of that period (Lee et al., 2003).

Considerable research efforts have been conducted on real time crash prediction during the past decades (Lee et al., 2003; Abdel-Aty and Abdalla, 2004; Oh et al., 2005; Hourdos et al., 2006; Ahmed and Abdel-Aty, 2012, 2013; Hossain and Muromachi, 2012; Xu et al., 2013a, b, 2015, 2016; Yu and Abdel-Aty, 2013; Fang et al., 2016; Roy et al., 2016; Sun and Sun, 2015; Katrakazas et al., 2017; Wang et al., 2017; Yang et al., 2018; Chen et al., 2018; Basso et al., 2018; Essa and Sayed, 2018; Chen and Qin, 2019; Wang et al., 2019; Essa and Sayed, 2019). A recent literature review study by Hossain et al. (2019) identified 78 studies from 2003 to 2018 that were related to this topic. They summarized that most of these studies used loop detectors to collect dynamic traffic data, applied a matched case-control approach for compiling the data in non-crash and crash conditions, and modeled the compiled data with

[^0]Logistic regression, Bayesian, or artificial intelligence approaches. The used case-control approach and modeling approaches have shown the capability of identifying crash prone traffic conditions, but the problem is that they can only differentiate crash occurrence (i.e., yes or no) and are not able to show how "risky" the crash prone traffic condition actually is (Roshandel et al., 2015; Yasmin et al., 2018). Another problem is that traffic characteristics derived from loop detectors and other types of sensor data are not informative, and important behavior factors such as braking, swerving and other evasive actions of drivers that have significant influence on crash occurrence are usually omitted (Roshandel et al., 2015).

Furthermore, the majority of previous studies focused on real time crash prediction for freeway/expressway segments, probably because they are well equipped with different types of sensors (e.g., loop detectors) and the corresponding data are more accessible. In contrast, intersections that are widely recognized as hazardous locations have been rarely investigated in the context of real time safety analysis. Crash statistics show that in United States about 22\% of traffic related fatalities and 45\% of traffic related injuries occurred at intersections (FHWA, 2009). In Canada, more than 30\% of deaths and 40\% of the serious injuries on the roads occurred at intersections (Barua et al., 2010) and most of injuries in urban areas occurred at signalized intersections (Fernandes, 2013). Sig-nalized intersections are usually of greater safety concern because of the larger traffic volume, more frequent stop-and-go traffic, and more complex conflicting movements (Yuan and Abdel-Aty, 2018).

Machiani and Abbas (2016) proposed a real time safety measure called safety surrogate histogram (SSH) to evaluate the safety of dilemma zone at signalized intersections. The SSH was developed based on real-time radar data to capture the degree and frequency of traffic conflicts. Their study showed that the traffic conflict based measure SSH was efficient for real time safety evaluation at signalized intersections, but the measure is not useful for crash risk prediction. Mussone et al. (2017) analyzed the factors affecting the severity of crashes at urban road intersections with traffic data of 5 min interval. They found that the real-time traffic flow characteristics played a role in predicting crash severity. However, the study did not estimate crash risk at the intersections. Yuan and Abdel-Aty (2018) developed an approach-level real time crash prediction model for signalized intersections using the matched case-control approach and Bayesian logistic models. They investigated the relationship between crash occurrence and dynamic traffic characteristics within 5 min interval, and found that the average speed, average green time, average waiting time for the left turn phase, green ratio for the through phase, and adaptability for the through phase had negative effect on the odds of intersection entrance crash occurrence, while the average queue length on through lanes had a positive effect.

In summary, there are certain limitations in the area of real time crash prediction from the perspectives of research object, data, and methodology. These limitations include: the limited research on intersections despite their considerable contribution to collision occurrence on road networks; relying on input data sources that are generally not adequately informative to account for road user behavior factors; and the developed models not being able to show how "risky" the crash prone traffic condition is.

To bridge these gaps, this study proposes a novel approach for real time crash prediction at signalized intersections. The approach uses traffic conflicts that are extracted from informative vehicle trajectories and consider dynamic traffic parameters as an intermediate for crash risk prediction. Moreover, the proposed approach is developed within the extreme value theory (EVT) framework. With the EVT model risk of crash and other safety indices are developed to quantitatively show the safety level of dynamic traffic conditions cycle-by-cycle. In addition, the proposed approach that takes vehicle trajectories as the main inputs is also promising with the emergence of connected and automated vehicles (CAVs). CAV techniques that use wireless communication between vehicles, infrastructure, and other road users will generate large amount of real time data on vehicle trajectories, which can be used to optimize the safety of traffic signal control, enhance in-vehicle technologies, and improve autonomous vehicle algorithms (Essa and Sayed, 2019).

Applying the EVT for road safety estimation has drawn increasing research interest in recent years, but to the best of authors' knowledge, there have been no studies that apply the EVT for real time crash prediction. The EVT was mainly applied to establish the relationship between traffic conflicts and crashes and accordingly show the validity of traffic conflict techniques (Farah and Azevdo, 2017; Songchitruksa and Tarko, 2006; Tarko, 2012, 2018; Wang et al., 2018; Zheng et al., 2014, 2018, 2019a, 2019b, Zheng and Sayed, 2019a, 2019b). It has also been applied to develop parametric safety continuum models (Zheng et al., 2014b; Zheng and Ismail, 2017), conduct before-after safety analysis (Zheng et al., 2018a; Zheng and Sayed, 2019c), and validate the safety of autonomous vehicles (Åsljung et al., 2017). In most of these studies, EVT models were developed for individual sites separately, which affects models' accuracy and result in large uncertainty. The reason is that extreme conflicts are "rare" in nature, so that there may not be many data values corresponding to each site. This study applies the Bayesian hierarchical modeling approach proposed in Zheng et al. (2019b) to combine conflict extremes of different intersections for crash risk estimation, so that the problem will be overcome by using more data and sharing information from different intersections.

The remainder of the study is organized as follows. Section 2 presents the research framework and the rational of applying EVT models for real time safety prediction. Section 3 provides details of model development, including the Bayesian hierarchal structure, model inference, and model choice. The data for model application is described in Section 4, and the model estimation and real time safety analysis results are also discussed in Section 4. Conclusions are presented in Section 5.

## 2. Research framework and rationale

The real time crash prediction at signalized intersections is conducted at the signal cycle level. The schematic diagram of the research framework is shown in Fig. 1. Real time traffic data of a signalized intersection can be collected using some "Real Time Intersection Data Collection System", which usually includes video sensors, storage devices, and remote processing computers. The rapid development of video sensors and computer vision techniques allows effective and accurate data extraction from video footages. Video data processing is to extract vehicle trajectories and to plot the space-time diagram for each signal cycle, from which

![](https://cdn.mathpix.com/cropped/b11ed932-193c-43ea-884f-d848621bb0f7-03.jpg?height=862&width=1374&top_left_y=185&top_left_x=258)
Fig. 1. Schematic diagram of the research framework.

individual vehicle related parameters (e.g., location, length, speed, acceleration) and cycle level traffic parameters (e.g., traffic volume, shock wave, platoon ratio) are extracted. These parameters are used to identify traffic conflicts, which are the intermediate used to estimate safety indices. The extrapolation from traffic conflicts to crashes is realized by using the EVT approach, and safety indices are obtained though the extreme value distribution of traffic conflicts and related to corresponding cycle level traffic parameters. Therefore, the safety indices (SI) that fluctuate with the change of cycle level traffic parameters can reflect the real time safety level of the signalized intersection. Moreover, the influence of cycle level traffic parameters on SI would be sent back to the signal control system to dynamically improve the traffic safety.

A key component of the framework is to use traffic conflict as the intermediate for real time crash risk prediction. A traffic conflict is "an observable situation in which two or more road users approach each other in space and time to such an extent that there is a risk of collision if their movements remain unchanged" (Amundsen and Hydén, 1977). This definition implies that traffic conflicts and crashes share similar process except for the presence and the success of evasive actions (Zheng et al., 2014c). This natural connection lays the foundation for extrapolating crashes from traffic conflicts. Moreover, it also means that vehicle and driver behavior factors, which are often omitted in previous studies, are incorporated into the real time crash prediction model by using traffic conflicts. The incorporation of certain vehicle and driver behavior factors is more explicit from the perspective of traffic conflict indicators that are used to measure the severity of traffic conflicts. For instance, the modified time to collision (MTTC) indicator that measures the temporal proximity of two consecutive vehicles is defined as (Ozbay et al., 2008):

$$
M T T C=\frac{\Delta v \pm \sqrt{\Delta v^{2}+2 \Delta a\left(S_{1}-L_{1}\right)}}{\Delta a}
$$

Where, $\Delta v=v_{2}-v_{1}$ is the relative speed, $\Delta a=a_{2}-a_{1}$ is the relative acceleration, $S_{1}$ is the space headway and $L_{1}$ is the length of the leading vehicle. There are two outcomes to MTTC. If both of them are positive, the smaller one is considered to be the MTTC value; if one outcome is positive while the other is negative, the positive outcome is considered to be the MTTC value.

In general, a smaller MTTC value indicates a more severe traffic conflict, and a crash occurs when the MTTC is equal to or less than 0. In contrast to crashes that rarely occur, traffic conflicts are more observable, especially at signalized intersections where vehicles following each other closely in a stop-and-go traffic. Therefore, using traffic conflicts to predict crashes means the extrapolation from observable levels to unobservable levels, and the EVT readily meet the need (Zheng et al., 2018a). More interestingly, the EVT is capable of sampling extremes at a block level and then estimating a corresponding generalized extreme value (GEV) distribution for each block. Apparently, the signal cycle is a "natural" block for the EVT and traffic conflict extremes of different cycles can be used to develop the GEV model. Mathematically, let $X_{1}, X_{2}, \ldots, X_{n}$ is a sequence of independent random variables having a common distribution and $M_{n}=\max \left\{X_{1}, X_{2} \ldots, X_{n}\right\}$ corresponds to a block maximum of $n$ values. In this application, $X_{i}$ represents negated MTTC values measured during a cycle so that $M_{n}$ represents the cycle maxima. If there exists sequences of constants $\left\{a_{n}>0\right\}$ and $\left\{b_{n}\right\}$ such that $\operatorname{Pr}\left\{\left(M_{n}-b_{n}\right) / a_{n} \leq \mathrm{z}\right\} \rightarrow G(z)$ as $n \rightarrow \infty$, where $G$ is a non-degenerate distribution function $G$, then $G$ is a member of GEV family:

$$
G(z)=\exp \left\{-\left[1+\xi\left(\frac{z-\mu}{\sigma}\right)\right]^{-1 / \xi}\right\}
$$

defined on $\{z: 1+\xi(z-\mu) / \sigma>0\}$, where $-\infty<\mu<\infty$ corresponding to the constant $b_{n}$ is the location parameter, $\sigma>0$ corresponding to the constant $a_{n}$ is the scale parameter, and $-\infty<\xi<\infty$ is the shape parameter.

If a GEV distribution of negated MTTC is developed for a signalized intersection, several safety indices can be obtained, and two important quantitative measures are the risk of crash (RC) and return level of a cycle (RLC). RC at signal cycle level can be calculated as:

$$
R C_{i}=\operatorname{Pr}\left\{z_{i} \geq 0\right\}=1-G_{i}(0)= \begin{cases}1-\exp \left\{-\left[1-\xi_{i} \frac{\mu_{i}}{\sigma_{i}}\right]^{-\frac{1}{\xi_{i}}}\right\}, & \text { for } \xi \neq 0 \\ 1-\exp \left[-\exp \left(\frac{\mu_{i}}{\sigma_{i}}\right)\right], & \text { for } \xi=0\end{cases}
$$

Where, $R C_{i}$ is the risk of crash of cycle $i, z_{i}$ is the maximum negated MTTC in cycle $i$, and $G_{i}(\cdot)$ is the fitted GEV distribution. RC is nonnegative. A $R C$ value of zero means no risk of crash for a cycle, while a $R C$ value greater than zero indicates a crash prone cycle because of positive risk of crash.

In addition to RC, the other safety index can also be developed from the fitted GEV distribution, which is the return level of a cycle (RLC). The return level is a standard prediction in extreme value analysis, and RLC can be obtained by inverting Equation (2):

$$
R L C_{p i}=\left\{\begin{array}{l}
\mu_{i}-\frac{\sigma_{i}}{\xi_{i}}\left[1-\{-\log (1-p)\}^{-\xi_{i}}\right], \quad \text { for } \quad \xi \neq 0 \\
\mu_{i}-\log \{-\log (1-p)\}, \quad \text { for } \quad \xi=0
\end{array}\right.
$$

where $R L C_{p i}$ is the return level of cycle $i$ associated with the return period $1 / p$ giving $G\left(R L C_{p i}\right)=1-p$. In this study, the return level corresponds to the maximum value of negated MTTC that could be expected during the return period. Therefore, $R L C_{p i} \geq 0$ implies that positive crash risk is expected during cycle $i$ while $R L C_{p i}<0$ implies that zero crash risk is expected (Songchitruksa, 2004; Zheng et al., 2014b).

## 3. Model development

Combining traffic conflicts and EVT provides a theoretically feasible framework for real time crash prediction. However, there are two important practical problems. Firstly, although traffic conflicts are more observable, extreme conflicts are "rare" in nature, so that there are not many data values corresponding to an intersection. Therefore, the real time safety estimation based on the data of an individual intersection is usually subject to limited accuracy and large uncertainty. Secondly, to realize the assumption of predicting crash using the dynamic traffic parameters of the cycle, the GEV distribution should be directly related to these traffic parameters. Moreover, the unobserved heterogeneity associated with an intersection, which has been found to significantly influence crash prediction (Lord and Mannering, 2010; Mannering and Bhat, 2014; Buddhavarapu et al., 2016; Guo et al., 2018), should also be properly considered. To overcome these problems, a Bayesian hierarchical structure for the GEV model is developed.

### 3.1. Bayesian hierarchical structure

The Bayesian hierarchical structure has three layers (Cooley et al., 2006; Zheng et al., 2019b; Zheng and Sayed, 2019d). The first layer models data with the GEV distribution, the second layer models the latent process that drives the traffic conflict extremes, and the third layer consists of prior distributions of the parameters that control the latent process.

### 3.1.1. Data layer

A GEV given by Equation (2) is used to model the data at the first layer of hierarchy. To ensure a positive scale parameter, the GEV is reparameterized as $\operatorname{GEV}(\mu, \phi, \xi)$, where $\phi=\log \sigma$. Let $z_{i j}$ be the $i$ th recorded cycle maximum at site $j$, with $j=1, \ldots, s$ and $i=1, \ldots$, $n_{j}$. Given that $z_{i j}$ corresponds to the cycle maximum, it can be described by the GEV distribution whose parameters are dependent on the site. Letting $\mu_{i j}, \phi_{i j}, \xi_{i j}$ represent the parameters of site $j$ yields

$$
G\left(z_{i j}<z \mid \mu_{i j}, \phi_{i j}, \xi_{i j}\right)=\exp \left\{-\left[1+\xi_{i j}\left(\frac{z-\mu_{i j}}{\exp \phi_{i j}}\right)\right]^{-1 / \xi_{i j}}\right\}
$$

### 3.1.2. Process layer

In the process layer, a latent Gaussian process underlying extremes is characterized by using identity link function that relates the parameters of the data layer to certain covariates. It is noted that this is also the common way to deal with the non-stationary problem (i.e., extremes are not identically distributed and may relate to other variables). Since the shape parameter $\xi_{i j}$ of the GEV is difficult to estimate with precision, it is unrealistic to model $\xi_{i j}$ as a smooth function of covariates. In usual, it is assumed to be unknown but not affected by covariates during the process (Coles, 2001; Cooley et al., 2006). As such, the parameters in the data layer can be written as

$$
\left\{\begin{array}{c}
\mu_{i j}=\alpha_{\mu 0}+\alpha_{\mu} X \\
\phi_{i j}=\alpha_{\phi 0}+\alpha_{\phi} X \\
\xi_{i j}=\alpha_{\xi 0}
\end{array}\right.
$$

where, $\alpha_{\mu 0}, \alpha_{\phi 0}$ and $\alpha_{\xi 0}$ are intercept terms corresponding to the three model parameters; X is the covariate vector, and $\alpha_{\mu}$ and $\alpha_{\phi}$ are the vectors of regression parameters. In practice, there appears to be additional heterogeneity that is not directly addressed by covariates. To capture the additional heterogeneity, random error terms are introduced as

$$
\left\{\begin{array}{c}
\mu_{i j}=\alpha_{\mu 0}+\alpha_{\mu} X+\varepsilon_{\mu j} \\
\phi_{i j}=\alpha_{\phi 0}+\alpha_{\phi} X+\varepsilon_{\phi j} \\
\xi_{i j}=\alpha_{\xi 0}+\varepsilon_{\xi j}
\end{array}\right.
$$

where, $\varepsilon_{\mu j}, \varepsilon_{\phi j}$ and $\varepsilon_{\xi j}$ are random error terms accounting for additional heterogeneity that is not directly addressed by the covariates. It is noted that the random terms represent between-site variances, which are consistent for extremes in the same site but vary between different sites. Therefore, the process described in Equation (7) can also be written as a random intercept model as follows:

$$
\left\{\begin{array}{c}
\mu_{i j}=\alpha_{\mu j}+\alpha_{\mu} X \\
\phi_{i j}=\alpha_{\phi j}+\alpha_{\phi} X \\
\xi_{i j}=\alpha_{\xi j}
\end{array}\right.
$$

### 3.1.3. Prior layer

In this layer, priors to parameters $\alpha_{\mu j}, \alpha_{\phi j}, \alpha_{\xi j}, \alpha_{\mu}$ and $\alpha_{\phi}$ are assigned to characterize the latent process, and it is assumed that each parameter in this layer is independent to the others.

Since no prior information on how the GEV parameters are related to covariates, the uninformative priors for the regression parameters $\alpha_{\mu j}, \alpha_{\phi j}, \alpha_{\mu}$ and $\alpha_{\phi}$ are adopted. They are assumed to follow a normal distribution with zero mean and large variance, i.e., $\mathrm{N}\left(0,10^{6}\right)$. Since the GEV model is sensitive to its shape parameter and an improper defined prior would cause convergence problems during the model estimation, information from previous studies as Songchitruksa and Tarko (2006) and Zheng et al. (2014b) is referred. In these studies, it can be found that the estimated shape parameters are in general within the range of (-1.0, 1.0). Therefore, the prior for shape parameter is set as $\alpha_{\xi j} \sim \operatorname{Unif}(-1.0,1.0)$.

### 3.2. Model inference and choice

### 3.2.1. Model inference

Using the Bayes theorem, under the three-layer hierarchical model, the inference for the model parameters $\boldsymbol{\theta}$ given the data $\mathbf{Z}$ is

$$
\begin{aligned}
& p(\theta \mid \mathbf{Z}) \propto p_{1}\left(\underset{\text { Data }}{\left(\mathbf{Z} \mid \theta_{1}\right)}\right) p_{2}(\underbrace{\left(\theta_{1} \mid \theta_{2}\right)}_{\text {Process }}) \underbrace{\left(\theta_{2}\right)}_{\text {Prior }} \\
& \propto \prod_{i=1}^{n_{i}} \prod_{j=1}^{s} \operatorname{GEV}\left(z_{i j} \mid \mu_{j}, \phi_{j}, \xi_{j}\right) \times p\left(\mu_{j} \mid \mathrm{X}, \alpha_{\mu j}, \alpha_{\mu}\right) \times p\left(\phi_{j} \mid \mathrm{X}, \alpha_{\phi j}, \alpha_{\phi}\right) \times p\left(\xi_{j} \mid \alpha_{\xi j}\right) \times p_{\alpha_{\mu j}}\left(\alpha_{\mu j}\right) \times p_{\alpha_{\mu}}\left(\alpha_{\mu}\right) \times p_{\alpha_{\phi j}}\left(\alpha_{\phi j}\right) \times p_{\alpha_{\phi}}\left(\alpha_{\phi}\right) \times p_{\xi j}\left(\alpha_{\xi j}\right)
\end{aligned}
$$

where $p_{j}$ is the density associated with level $j$ of the hierarchical model. In the Bayesian hierarchical models, the likelihood functions are built from the probability distributions defined in the data layer and process layer and then the prior distributions assigned in the prior layer. Based on Equation (9), the posterior distributions of model parameters can be obtained. The inference of the posterior distributions is carried out by means of Markov chain Monte Carlo (MCMC) simulation using Gibbs Sampling.

### 3.2.2. Model choice

Bayesian hierarchical models are developed with considering combinations of GEV parameters as functions of several covariates, and thus there will be a large catalogue of models to choose from. In the Bayesian framework, Deviance Information Criterion (DIC) is the most widely used model comparison criterion. The basic principle of DIC is parsimony, obtaining the simplest model that explains as much of the variation in the data as possible (Spiegelhalter, et al., 2002). The DIC is calculated as follows:

$$
D I C=\bar{D}+p_{D}
$$

where $\bar{D}$ is the posterior mean deviance that measures the model fitting and $p_{D}$ is the effective number of parameters in the model. Generally, a smaller DIC value indicates a better model. It is also suggested that a difference greater than 10 can definitely rule out the model with the higher DIC value, the differences ranging from 5 to 10 are considered substantial, and a difference less than 5 make the models competitive (El-Basyouny and Sayed, 2012a,b).

![](https://cdn.mathpix.com/cropped/b11ed932-193c-43ea-884f-d848621bb0f7-06.jpg?height=566&width=1132&top_left_y=187&top_left_x=371)
Fig. 2. Study locations and characteristics of studied intersection approaches.

## 4. Model application

### 4.1. Data description

The proposed approach is applied for real time rear-end crash prediction at the signal cycle level. A detailed dataset was prepared based on video data collected from four signalized intersections in the city of Surrey, British Columbia, Canada. The intersections are 72 Ave \& 128 St, 72 Ave \& 132 St, 64 Ave \& King George Blvd, and Fraser Hwy \& 168 St. To collect the video data, a video camera was installed for each intersection with its scene focused on an intersection approach where most of rear-end conflicts occur. All the studied approaches have three lanes as shown in Fig. 2, including a left-turn lane, a through lane, and a right-turn or right-turn and through lane, and only vehicles on the middle through lane were the target. A total of 13 h video data were collected during clear daytime, including four, three, two and four hours for 72 Ave \& 128 St, 72 Ave \& 132 St, 64 Ave \& King George Blvd, and Fraser Hwy \& 168 St, respectively.

A platform was developed to extract the needed information from the video footages. Readers can refer to Essa and Sayed (2018) for the details of the platform, and the main purpose of the platform is to detect the signal timing, extract vehicle trajectories, and generate space-time diagram of vehicles. From the space-time diagram, three traffic parameters at the signal cycle level and the conflict indicator (i.e., MTTC) were obtained. It is noted that MTTC is employed as the indicator because it outperforms other indicators such as time to collision (TTC), post encroachment time (PET) and deceleration rate to avoid a crash (DRAC) in crash estimation for the current dataset (Zheng and Sayed, 2019b). The three traffic parameters are as follows: traffic volume (V) is the number of vehicles per cycle on the studied lane. The minimum of V is 2 vehicles per cycle and the maximum is 28 vehicles per cycle; Shock wave area (A) is a triangle area where the traffic flow state is II in terms of four traffic flow states theory (May 1990), as shown in Fig. 3. The minimum of A is 0 and the maximum is 5.66 km⋅s; Platoon ratio (P) is defined as the proportion of all vehicles arriving during green multiplied by the ratio of the signal cycle length to the effective green time of the subject movement (Highway Capacity Manual, 2000). The minimum of P is 0 and the maximum is 2.27. For the traffic conflicts measured by MTTC, a total of 2,128 conflicts were obtained from 372 signal cycles, which is on average 6 events per cycle. The minimum of MTTC value is 0.03 s while the maximum is 3.82 s.

In addition to the video data, crash data of three years (2013-2015) were collected from the Insurance Corporation of British

![](https://cdn.mathpix.com/cropped/b11ed932-193c-43ea-884f-d848621bb0f7-06.jpg?height=465&width=731&top_left_y=1874&top_left_x=582)
Fig. 3. Four different traffic flow states at signalized intersections.

Table 1
Summary statistics of the collected data.
|  |  | 72 Ave \& 128 St | 72 Ave \& 132 St | 64 Ave \& King George Blvd | Fraser Hwy \& 168 St |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Video was recorded in |  | March 28, 2012 (10:00-12:00; 14:00-16:00) | April 3, 2012 (09:00-12:00) | June 10, 2015 (13:00-15:00) | June 10, 2015 (09:00-13:00) |
| Number of cycles |  | 133 | 79 | 44 | 116 |
|  | Mean | 13.45 | 13.43 | 10.43 | 13.61 |
|  | Std. Dev. | 4.99 | 3.52 | 2.53 | 3.94 |
|  | Min | 2 | 7 | 6 | 3 |
|  | Max | 28 | 25 | 14 | 23 |
| A (km⋅s) | Mean | 1.37 | 0.96 | 0.61 | 1.08 |
|  | Std. Dev. | 1.23 | 0.72 | 0.42 | 0.89 |
|  | Min | 0 | 0 | 0 | 0 |
|  | Max | 4.45 | 2.90 | 1.80 | 5.66 |
| P | Mean | 1.10 | 1.07 | 1.57 | 1.13 |
|  | Std. Dev. | 0.32 | 0.35 | 0.35 | 0.27 |
|  | Min | 0 | 0.14 | 0.55 | 0.32 |
|  | Max | 1.88 | 1.72 | 2.27 | 1.75 |
| MTTC value (s) | Mean | 1.83 | 1.63 | 1.75 | 1.61 |
|  | Std. Dev. | 0.72 | 0.72 | 0.64 | 0.82 |
|  | Min | 0.13 | 0.15 | 0.12 | 0.03 |
|  | Max | 3.82 | 3.75 | 3.66 | 3.74 |
| Observed crash count | 2013 | 8 | 0 | 9 | 4 |
|  | 2014 | 3 | 1 | 7 | 3 |
|  | 2015 | 3 | 0 | 2 | 3 |


Note: the table is revised from Zheng et al. (2019b).
Columbia for the four intersections. The data contained information such as location, date, time, crash type, and a brief description on the direction of travel of incident vehicles, the lane that the incident vehicle occupied, and the total number of involved vehicles. In order to relate the crashes better to the rear-end conflicts observed on the studied lanes during daytime periods, only rear-end crashes that occurred at the specific lanes of the target approaches were selected, and these rear-end crashes were further reduced to the daytime only. At last, a total of 43 crashes remained.

The summary statistics of the collected data is shown in Table 1.

### 4.2 Model estimation

Three Bayesian hierarchical models were developed to fit the block maxima of negated MTTC, considering the three covariates added to location parameter, scale parameter, and both location and scale parameters, respectively. These three models are denoted as BHM_GEV(1,0,0), BHM_GEV(0,1,0) and BHM_GEV(1,1,0) in order. The models were estimated using the WINBUGS tool. Two separate chains for each model parameter with diverse initial values were set to run 50,000 iterations and the first 20,000 iterations were discarded as burn-in samples. The posterior estimates were obtained from the remaining 30,000 iterations. The model convergence was checked by calculating the Gelman-Rubin statistic of two chains for each parameter as well as visually inspecting the trace plots of parameter chains (El-Basyouny and Sayed, 2009). The model estimation results are shown in Table 2. It is noted only significant covariates in the model are reported.

It can be seen from the table that BHM_GEV(1,1,0) is the best model in terms of DIC. The DIC value differences between it and BHM_GEV(1,0,0) and BHM_GEV(0,1,0) are 9.0 and 137.3 respectively, which indicates that BHM_GEV(1,1,0) substantially outperform the other two models. The superior fit of BHM_GEV(1,1,0) also implies that introducing covariates to both location and scale parameters of GEV model explains a substantial amount of variation in the observed data.

### 4.3. Real time safety analysis

### 4.3.1. Real time safety index calculation

With the best fitted BHM_GEV(1,1,0) model and the corresponding traffic parameters (i.e., V, A, and P), each cycle will have its own GEV distribution. An example of GEV distributions of individual cycles for 64 Ave \& King George Blvd, which have 44 signal cycles (from Cycle 213 to 256), is shown in Fig. 4. The distributions, which show where most of extreme events are located and how far the distribution away from the risk of crash area (i.e., negated MTTC = 0), have certain safety implications (Zheng et al., 2018b). Moreover, whenever the right-hand tail ends after the point of negated MTTC = 0, the corresponding cycle has a crash prone traffic condition because positive risk of crash is expected. As shown in Fig. 4, it can be found that cycle 226, 233, 247, and 253 have their distributions crossed the point of negated MTTC $=0$.

The cycle-by-cycle safety level change can also be quantitatively measured by the proposed safety indices, RC and RLC. From the GEV distribution of each cycle, RC and RLC can be calculated using Equations (3) and (4), respectively. For the calculation of RLC, the $p$ in Equation (4) is selected as $1 /(365$ days $* 12 \mathrm{~h} * 60 \mathrm{~min} / 2 \mathrm{~min}) \approx 0.000007$, where 2 min is the average cycle length of the

Table 2
Model estimation results.
| Node |  | BHM_GEV(1,0,0) |  |  |  | BHM_GEV(0,1,0) |  |  |  | BHM_GEV(1,1,0) |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | mean | s.d. | 2.50\% | 97.50\% | mean | s.d. | 2.50\% | 97.50\% | mean | s.d. | 2.50\% | 97.50\% |
|  | $\alpha_{\mu[1]}$ | -1.4840 | 0.0979 | -1.6730 | -1.2850 | -1.2290 | 0.0494 | -1.3270 | -1.1310 | -1.4330 | 0.1090 | -1.6490 | -1.2240 |
|  | $\alpha_{\mu \text { [2] }}$ | -1.8040 | 0.1027 | -2.0070 | -1.6020 | -1.5580 | 0.0734 | -1.7110 | -1.4220 | -1.7440 | 0.1079 | -1.9550 | -1.5300 |
|  | $\alpha_{\mu[3]}$ | -1.4600 | 0.1413 | -1.7310 | -1.1840 | -1.4770 | 0.1089 | -1.7040 | -1.2760 | -1.3430 | 0.1492 | -1.6330 | -1.0480 |
|  | $\alpha_{\mu[4]}$ | -1.5270 | 0.0970 | -1.7100 | -1.3260 | -1.2960 | 0.0588 | -1.4170 | -1.1880 | -1.4610 | 0.1062 | -1.6690 | -1.2540 |
|  | $\alpha_{\mu}(V)$ | 0.0350 | 0.0052 | 0.0253 | 0.0455 | - | - | - | - | 0.0390 | 0.0062 | 0.0278 | 0.0513 |
|  | $\alpha_{\mu}(A)$ | 0.1268 | 0.0257 | 0.0753 | 0.1762 | - | - | - | - | 0.1086 | 0.0260 | 0.0589 | 0.1605 |
|  | $\alpha_{\mu}(P)$ | -0.2807 | 0.0698 | -0.4188 | -0.1548 | - | - |  | - | -0.3623 | 0.0839 | -0.5250 | -0.1945 |
|  | $\alpha_{\phi[1]}$ | -1.1080 | 0.0671 | -1.2330 | -0.9700 | -1.1980 | 0.1044 | -1.3900 | -0.9863 | -0.8953 | 0.1082 | -1.0970 | -0.6730 |
|  | $\alpha_{\phi[2]}$ | -0.7181 | 0.0973 | -0.8950 | -0.5118 | -0.9716 | 0.1326 | -1.2240 | -0.7039 | -0.6276 | 0.0996 | -0.8135 | -0.4254 |
|  | $\alpha_{\phi[3]}$ | -0.6180 | 0.1286 | -0.8452 | -0.3271 | -0.7665 | 0.1473 | -1.0340 | -0.4543 | -0.5663 | 0.1228 | -0.7807 | -0.2941 |
|  | $\alpha_{\phi[4]}$ | -0.8623 | 0.0812 | -1.0110 | -0.6915 | -0.9340 | 0.1184 | -1.1560 | -0.7044 | -0.7582 | 0.0846 | -0.9195 | -0.5857 |
|  | $\alpha_{\phi}(V)$ | - | - | - | - | 0.0253 | 0.0070 | 0.0112 | 0.0391 | - | - | - | - |
|  | $\alpha_{\phi}(A)$ | - | - | - | - | 0.0691 | 0.0370 | 0.0018 | 0.1493 | -0.1438 | 0.0485 | -0.2355 | -0.0470 |
|  | $\alpha_{\Phi}(P)$ | - | - | - | - | - | - | - | - | - | - | - | - |
| $\xi$ | $\alpha_{\xi[1]}$ | -0.3185 | 0.0441 | -0.4004 | -0.2271 | -0.4693 | 0.0503 | -0.5735 | -0.3749 | -0.3850 | 0.0535 | -0.4896 | -0.2792 |
|  | $\alpha_{\xi[2]}$ | -0.4628 | 0.0762 | -0.6115 | -0.3104 | -0.4737 | 0.0791 | -0.6334 | -0.3204 | -0.3589 | 0.0785 | -0.5116 | -0.1982 |
|  | $\alpha_{\xi[3]}$ | -0.4552 | 0.0986 | -0.6581 | -0.2648 | -0.5611 | 0.0992 | -0.7633 | -0.3703 | -0.3928 | 0.0967 | -0.5636 | -0.1766 |
|  | $\alpha_{\xi[4]}$ | -0.5270 | 0.0733 | -0.6782 | -0.3915 | -0.7076 | 0.0744 | -0.8571 | -0.5635 | -0.4345 | 0.0776 | -0.5934 | -0.2886 |
| $\bar{D}$ |  | 80300.0 |  |  |  | 80430.0 |  |  |  | 80290.0 |  |  |  |
| $p_{D}$ |  | 13.5 |  |  |  | 11.8 |  |  |  | 14.5 |  |  |  |
| DIC |  | 80313.5 |  |  |  | 80441.8 |  |  |  | 80304.5 |  |  |  |


Note: "-" indicates the covariate is not considered or insignificant.
studied intersections. With this given $p$ value, the calculated RLC equivalents to the expected return level (i.e., maximum negated MTTC value) during a year assuming that all the signal cycles of that year have identical traffic parameters. The RC and RLC calculation results along with traffic parameters of each cycle for the combined four signalized intersections are shown in Fig. 5.

As seen in Fig. 5, the safety indices fluctuate among cycles with the change of traffic parameters, especially for RLC. RC is assigned to be a non-negative value, and whenever the RC is greater than 0, it indicates a cycle with the crash prone traffic condition because there is a positive risk of crash, otherwise the cycle is considered to be "safe". It can be found that most of cycles are "safe" in terms of RC. However, even for the "safe" cycles, the safety margins are different, as shown in the fluctuation of RLC. The different safety margins can also be shown in Fig. 4, where the closeness of GEV distributions to the point of negated MTTC = 0 are different for these cycles with zero risk of crash. In summary, RC is a straightforward safety index which can directly point out the cycles with crash prone traffic conditions. The understanding of RLC's safety meaning is not straightforward, but RLC is a more flexible safety index which can differentiate the safety levels even for "safe" cycles. Moreover, it can be found that a positive RC is always corresponding to a positive RLC, and the positive correlation between RC and RLC would make the safety interpretation of RLC much easier.

### 4.3.2. Crash prone traffic conditions

The traffic conditions of a cycle are represented by three variables, traffic volume, shock wave area, and platoon ratio. The parameters of the three covariates seem to have logical signs in the best fitted model. The positive sign of traffic volume means that the more vehicles within a cycle, the closer the GEV distribution to the risk of crash area is, which indicates a more crash prone traffic condition. The negative sign of platoon ratio means a higher platoon ratio will lead to a smaller location parameter and accordingly a lower risk of crash. This is intuitive since the higher platoon ratio means that more vehicles arrive during the green time, and subsequently, a better arrival type and lower chances of crash occurrence during the cycle. The shock wave area has significant influence on both the location parameter and scale parameter, but the sign for location parameter is positive while that for scale parameter is negative. It means a greater shock wave area yields a greater location parameter (i.e., higher risk of crash) but a smaller scale parameter (i.e., lower risk of crash). To show the overall impact of shock wave area, the RC is calculated while the other two variables are fixed, and the results show that a higher shock wave area leads to a higher RC.

With the integrated impact of the three traffic parameters, a total of 10 cycles with crash prone traffic conditions were identified, and there were four cycles from intersection of 72 Ave \& 128 St, four cycles from 64 Ave \& King George Blvd, and two cycles from Fraser Hwy \& 168 St. The identified cycles with crash prone traffic conditions are shown in Table 3. It can be seen that a crash prone traffic condition usually occurs when the cycle has extremely high volume (i.e., about 50\% larger than the mean) and meanwhile has medium shock wave area and platoon ratio. Examples of this kind including cycle 106, 109, 127, 226, 247, 253 and 346. In addition, a cycle with very large shock wave area together with either large traffic volume (i.e., cycle 94) or small platoon ratio (i.e., cycle 347) is also crash prone. The extremely small platoon ratio will also lead to crash prone traffic condition even when the other two parameters are around their average level (i.e., cycle 233).

![](https://cdn.mathpix.com/cropped/b11ed932-193c-43ea-884f-d848621bb0f7-09.jpg?height=1481&width=1545&top_left_y=183&top_left_x=171)
Fig. 4. Estimated GEV distributions of individual cycles for 64 Ave \& King George Blvd.

### 4.3.3. Results validation

Since the $R C_{i}$ is non-negative, it can be considered as the expected number of crashes during cycle $i$ of an intersection, and thus the summation of $R C_{i}$ over an observation period $t$ is equivalent to the expected number of crashes during period $t$, which is $C_{t}=\sum_{i=1}^{N_{t}} R C_{i}$, where $N_{t}$ is the number of cycles during period $t$. If the observation period $t$ is assumed to be representative to a longer time $T$, say $T=1$ year, then the estimated annual number of crashes for the intersection can be calculated as $C_{T}=\frac{N_{T}}{N_{t}} C_{t}$, where $N_{T}$ is the number of cycles during period $T$. As such, the safety estimates from the model can be validated at the aggregate level by comparing the estimated crashes to observed crashes. However, it should be noted that such a validation method is a compromise to the short conflict observation time. It can only show whether there is an agreement between the aggregated crash risks of signal cycles and observed crashes but provide little support to claim the safety of different signal cycles.

The estimated annual numbers of crashes are calculated to be 5.5, 0, 9.7, and 3.7 for intersections of 72 Ave \& 128 St, 72 Ave \& 132 St, 64 Ave \& King George Blvd, and Fraser Hwy \& 168 St, respectively. The comparison between the estimated crashes and observed crashes are shown in Fig. 6. In the figure, the 95\% confidence intervals (95\% C.I.) of observed crashes are obtained by assuming the observed crash counts follow the Poisson distribution (Songchitruksa and Tarko, 2006). The 95\% Poisson interval for observed mean annual crash occurrences $\lambda$ could be obtained as $\left\{\lambda: \frac{1}{2 n} \chi_{2 y_{0}, 0.975}^{2} \leq \lambda \leq \frac{1}{2 n} \chi_{2\left(y_{0}+1\right), 0.025}^{2}\right\}$, where $n=3$ is the number of years for observed crashes, and $y_{0}$ is the total number of crashes in the 3-year period for an intersection. It is noted that observed crash data were screened based on crash type, lane occupation, and occurrence time to match them better to the observed traffic conflicts in this study.

![](https://cdn.mathpix.com/cropped/b11ed932-193c-43ea-884f-d848621bb0f7-10.jpg?height=1396&width=1384&top_left_y=187&top_left_x=252)
Fig. 5. Safety indices (RC and RLC) and covariates (V, A, and P) fluctuation among cycles.

Table 3
Identified cycles with crash prone traffic conditions.
| Intersection | Cycle ID | V | A | P | RC | RLC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 72 Ave \& 128 St | 94 | 22 | 3.808 | 0.955 | 1.677E - 05 | 0.0021 |
|  | 106 | 28 | 2.872 | 1.366 | 3.684E-03 | 0.1899 |
|  | 109 | 25 | 2.598 | 1.145 | $6.253 \mathrm{E}-04$ | 0.0387 |
|  | 127 | 24 | 2.300 | 1.027 | $6.825 \mathrm{E}-04$ | 0.0376 |
| 64 Ave \& King George Blvd | 226 | 16 | 0.858 | 1.159 | 3.664E-03 | 0.0483 |
|  | 233 | 9 | 0.807 | 0.548 | $1.254 \mathrm{E}-03$ | 0.0013 |
|  | 247 | 16 | 1.220 | 1.222 | $1.443 \mathrm{E}-03$ | 0.0095 |
|  | 253 | 14 | 0.870 | 1.204 | 2.566E - 04 | 0.0047 |
| Fraser Hwy \& 168 St | 346 | 23 | 1.027 | 0.946 | $6.298 \mathrm{E}-04$ | 0.0350 |
|  | 347 | 18 | 5.664 | 0.551 | $2.755 \mathrm{E}-03$ | 0.1193 |


Note: values in bold are about 50\% larger (for V and A) or smaller (for P) than the mean.
It can be seen from the figure that the estimated crashes are in general close to the observed ones, and most of the estimated crashes are within the 95\% C.I. of observed crashes. This confirms the validation of the proposed model from an aggregation perspective. However, there is also an intersection with estimated crashes outside the $95 \%$ C.I. of observed crashes. A possible reason is that the short observation time of traffic conflicts cannot fully represent the traffic of a year because of daily/weekly/seasonal variations.

![](https://cdn.mathpix.com/cropped/b11ed932-193c-43ea-884f-d848621bb0f7-11.jpg?height=447&width=741&top_left_y=187&top_left_x=576)
Fig. 6. Comparison between estimated crashes and observed crashes.

## 5. Conclusions

This study proposed an approach for crash risk prediction at signalized intersections within the EVT framework. To be specific, each signal cycle was considered as a block, and the maximum value of a traffic conflict indicator (i.e., negated MTTC) in each block was considered as the extreme and used to fit the GEV model. Furthermore, a Bayesian hierarchical structure that can combine traffic conflict extremes of different sites, incorporate the influence of dynamic traffic parameters, and account for unobserved heterogeneity, was developed for the GEV model. Based on the GEV model, two important safety indices (i.e., RC and RLC) were proposed to measure the safety of intersection at the signal cycle level.

The proposed approach was applied to video data of 13 h collected from four signalized intersections. Vehicle trajectories, traffic parameters (V, A, and P) at the signal cycle level, and the traffic conflict indicator (MTTC) were extracted from the video data using computer vision techniques. Three Bayesian hierarchical models were developed, including BHM_GEV(1,0,0) that added covariates to the location parameter, BHM_GEV(0,1,0) that added covariates to the scale parameter, and BHM_GEV(1,1,0) that added covariates to both the location and scale parameters. The modeling results show that the BHM_GEV(1,1,0) is the best fitted model. With the best fitted model, GEV distributions were generated for individual cycles of an intersection, and two safety indices RC and RLC were derived from the GEV distributions. RC is non-negative and could directly point out cycles with crash prone traffic conditions with RC > 0, and RLC was a more flexible safety index which could differentiate the safety levels even for "safe" cycles with RC = 0. With the help of these two safety indices, a total of 10 cycles with crash prone traffic conditions were identified. Moreover, the cycleby-cycle crash risk prediction results were also validated at an aggregate level by comparing predicted crashes to observed crashes.

The proposed approach is novel from the following three aspects: $i$ ) the crash risk prediction within a short time window is realized through the EVT model instead of conventional Logistic regression model, and the modeling results are not only to answer "yes" or "no" to the question of whether the traffic condition is crash prone, but also to quantitatively show how "risky" the traffic condition actually is. ii) the proposed approach uses traffic conflicts as the intermediate for crash prediction. Most of traffic conflict indicators are extracted from vehicle trajectories, through which behavioral factors (such as accelerating and braking) are incorporated into the real time crash prediction. iii) a Bayesian hierarchical structure is developed for the GEV model which has advantages in borrowing strength from different sites and accounting for non-stationarity as well as unobserved heterogeneity. These aspects make the proposed model substantially different from the real time crash prediction models for freeways and promising for real time crash prediction at signalized intersections. However, compared to those freeway models that have been studied extensively and have shown positive impact on both safety and operation of freeways (Roshandel et al., 2015; Yasmin et al., 2018; Hossain et al., 2019), the impact of the proposed model on the operation of signalized intersections needs further validation. Future research is needed to investigate the performance of the proposed model at a larger scale (e.g., a corridor with coordinated signal control system or an urban road network) from both the safety and operational point of view.

There are also several limitations needed to be addressed in future research. More data with a longer time period and from a larger number of intersections are needed. Collecting data with a longer time period could help to validate the proposed model at the disaggregate level, and to fully validate the model traffic parameter data from signal cycles with actual crashes are needed. As well, with a larger number of intersections, the various road geometric and environmental conditions could be incorporated in the model to further improve the model performance, and the transferability of the real time crash prediction model could also be investigated. Besides, although this study focused on the rear-end conflicts at signalized intersections, the proposed framework can also be applied to other types of conflicts with proper conflict indicators. However, if different types of conflicts are considered simultaneously, more advanced models might be needed to account for the correlation between different types of conflicts.

## CRediT authorship contribution statement

Lai Zheng: Conceptualization, Data curation, Methodology, Validation, Writing - original draft. Tarek Sayed: Conceptualization, Methodology, Writing - review \& editing.

## Appendix A. Supplementary material

Supplementary data to this article can be found online at https://doi.org/10.1016/j.trc.2020.102683.

## References

Abdel-Aty, M., Abdalla, M.F., 2004. Linking roadway geometrics and real-time traffic characteristics to model daytime freeway crashes. Transport. Res. Record: J. Transport. Res. Board 1897, 106-115.
Ahmed, M., Abdel-Aty, M.A., 2012. The viability of using automatic vehicle identification data for real-time crash prediction. IEEE Trans. Intell. Transp. Syst. 13 (2), 459-468.
Ahmed, M., Abdel-Aty, M., 2013. A data fusion framework for real-time risk assessment on freeways. Transp. Res. Part C 26, 203-213.
Amundsen, F.H., Hydén, C. (editors), 1977. Proceedings of the 1st Workshop on Traffic Conflicts, Oslo, Norway.
Åsljung, D., Nilsson, J., Fredriksson, J., 2017. Using extreme value theory for vehicle level safety validation and implications for autonomous vehicles. IEEE Trans. Intell. Veh. 2 (4), 288-297.
Barua, U., Azad, A., Tay, R., 2010. Fatality risks of intersection crashes in rural undivided highways of Alberta, Canada. Transport. Res. Record: J. Transport. Res. Board 2148, 107-115.
Basso, F., Basso, L.J., Bravo, F., Pezoa, R., 2018. Real-time crash prediction in an urban expressway using disaggregated data. Transp. Res. Part C 86, 202-219.
Buddhavarapu, P., Scott, J.G., Prozzi, J.A., 2016. Modeling unobserved heterogeneity using finite mixture random parameters for spatially correlated discrete count data. Transp. Res. Part B 91, 492-510.
Chen, F., Chen, S., Ma, X., 2018. Analysis of hourly crash likelihood using unbalanced panel data mixed logit model and real-time driving environmental big data. J. Saf. Res. 65, 153-159.
Chen, Z., Qin, X., 2019. A novel method for imminent crash prediction and prevention. Accid. Anal. Prev. 125, 320-329.
Coles, S., 2001. An introduction to statistical modeling of extreme values. Springer-Verlag, London, UK.
Cooley, D., Naveau, P., Jomelli, V., Rabatel, A., Grancher, D., 2006. A Bayesian hierarchical extreme value model for lichenometry. Environmetrics 17, 555-574.
El-Basyouny, K., Sayed, T., 2009. Urban arterial accident prediction models with spatial effects. Transport. Res. Record: J. Transport. Res. Board 2102, 27-33.
El-Basyouny, K., Sayed, T., 2012a. Measuring direct and indirect treatment effects using safety performance intervention functions. Saf. Sci. 50, 1125-1132.
El-Basyouny, K., Sayed, T., 2012b. Measuring safety treatment effects using full Bayes non-Linear safety performance intervention functions. Accid. Anal. Prev. 45, 152-163.
Essa, M., Sayed, T., 2018. Traffic conflict models to evaluate the safety of signalized intersections at the cycle level. Transp. Res. Part C 89, 289-302.
Essa, M., Sayed, T., 2019. Full Bayesian conflict-based models for real time safety evaluation of signalized intersections. Accid. Anal. Prev. 129, 367-381.
Farah, H., Azevdo, C.L., 2017. Safety analysis of passing maneuvers using extreme value theory. IATSS Res. 41 (1), 12-21.
Fang, S., Xie, W., Wang, J., Ragland, D.R., 2016. Utilizing the eigenvectors of freeway loop data spatiotemporal schematic for real time crash prediction. Accid. Anal. Prev. 59-64.
Fernandes, D., 2013. Vehicle-pedestrian accidents at signalized intersections in Montreal. Montreal. McGill University.
FHWA, 2009. The National Intersection Safety Problem. Intersection Safety Issue Brief 2. Publication FHWA-SA-10-005. Department of Transportation, Washington, D.C.
Guo, Y., Osama, A., Sayed, T., 2018. A cross-comparison of different techniques for modeling macro-level cyclist crashes. Accid. Anal. Prev. 113, 38-46.
Highway Capacity Manual, 2000. Transportation Research Board, Washington, D.C.
Hossain, M., Muromachi, Y., 2012. A Bayesian network based framework for real-time crash prediction on the basic freeway segments of urban expressways. Accid. Anal. Prev. 45, 373-381.
Hossain, M., Abdel-Aty, M., Quddus, M.A., Muromachi, Y., Sadeek, S.N., 2019. Real-time crash prediction models: State-of-the-art, design pathways and ubiquitous requirements. Accid. Anal. Prev. 124, 66-84.
Hourdos, J.N., Garg, V., Michalopoulos, P.G., Davis, G.A., 2006. Real-time detection of crash-prone conditions at freeway high-crash locations. Transport. Res. Record: J. Transport. Res. Board 1968, 83-91.
Katrakazas, C., Quddus, M.A., Chen, W.H., 2017. A simulation study of predicting conflict-prone traffic conditions in real-time. Presented at the Transportation Research Board 96th Annual Meeting, Washington D.C.
Lee, C., Hellinga, B., Saccomanno, F., 2003. Real-time crash prediction model for the application to crash prevention in freeway traffic. Transport. Res. Record: J. Transport. Res. Board 1840, 67-77.
Lord, D., Mannering, F., 2010. The statistical analysis of crash-frequency data: A review and assessment of methodological alternatives. Transp. Res. Part A 44 (5), 291-305.
Machiani, S.G., Abbas, M., 2016. Safety surrogate histograms (SSH): A novel real-time safety assessment of dilemma zone related conflicts at signalized intersections. Accid. Anal. Prev. 96, 361-370.
Mannering, F., Bhat, C., 2014. Analytic methods in accident research: Methodological frontier and future directions. Analytic Methods Accident Res. 1, 1-22.
May, Adolf D., 1990. Traffic Flow Fundamentals.
Mussone, L., Bassani, M., Masci, P., 2017. Analysis of factors affecting the severity of crashes in urban road intersections. Accid. Anal. Prev. 103, 112-122.
Oh, C., Oh, J., Ritchie, S.G., 2005. Real-time hazardous traffic condition warning system: framework and evaluation. IEEE Trans. Intell. Transp. Syst. 6 (3), 265-272.
Ozbay, K., Yang, H., Bartin, B., Mudigonda, S., 2008. Derivation and validation of new simulation-based surrogate safety measure. Transport. Res. Record: J. Transport. Res. Board 2083, 105-113.
Roshandel, S., Zheng, Z., Washington, S., 2015. Impact of real-time traffic characteristics on freeway crash occurrence: Systematic review and meta-analysis. Accid. Anal. Prev. 79, 198-211.
Roy, A., Kobayshi, R., Hossain, M., Muromachi, Y., 2016. Real time crash prediction model for urban expressway using Dynamic Bayesian Network. J. Jpn. Soc. Civ. Eng., Ser. D3 72 (5), 1331-1338.
Songchitruksa, P., 2004. Innovative non-crash-based safety estimation: an extreme value theory approach. PhD dissertation, Purdue University, West Lafayette, Indiana.
Songchitruksa, P., Tarko, A.P., 2006. The extreme value theory approach to safety estimation. Accid. Anal. Prev. 38, 811-822.
Spiegelhalter, D.J., Best, N.G., Carlin, B.P., Van der Linde, A., 2002. Bayesian measures of model complexity and fit. J. Roy. Statist. Soc. B 64, 1-34.
Sun, J., Sun, J., 2015. A Dynamic Bayesian Network model for real-time crash prediction using traffic speed conditions data. Transp. Res. Part C 54, 176-186.
Tarko, A.P., 2012. Use of crash surrogates and exceedance statistics to estimate road safety. Analy. Prevent. 45, 230-240.
Tarko, A.P., 2018. Estimating the expected number of crashes with traffic conflicts and the Lomax Distribution - A theoretical and numerical exploration. Accid. Anal. Prev. 113, 63-73.
Wang, C., Xu, C., Xia, J., Qian, Z., Lu, L., 2018. A combined use of microscopic traffic simulation and extreme value methods for traffic safety evaluation. Transp. Res. Part C 90, 281-291.
Wang, L., Abdel-Aty, M., Lee, J., 2017. Safety analytics for integrating crash frequency and real-time risk modeling for expressways. Accid. Anal. Prev. 104, 58-64.
Wang, L., Abdel-Aty, M., Lee, J., Shi, Q., 2019. Analysis of real-time crash risk for expressway ramps using traffic, geometric, trip generation, and socio-demographic predictors. Accid. Anal. Prev. 122, 378-384.
Xu, C., Tarko, A.P., Wang, W., Liu, P., 2013a. Predicting crash likelihood and severity on freeways with real-time loop detector data. Accid. Anal. Prev. 57, 30-39.
Xu, C., Wang, W., Liu, P., 2013b. A genetic programming model for real-time crash prediction on freeways. Trans. Intell. Transport. Syst. 14 (2), 574-586.

Xu, C., Wang, W., Liu, P., Li, Z., 2015. Calibration of crash risk models on freeways with limited real-time traffic data using Bayesian meta-analysis and Bayesian inference approach. Accid. Anal. Prev. 85, 207-218.
Xu, C., Liu, P., Wang, W., 2016. Real-time estimation of secondary crash likelihood on freeways using high-resolution loop detector data. Transp. Res. Part C 71, 406-418.
Yang, K., Wang, X., Yu, R., 2018. A Bayesian dynamic updating approach for urban expressway real-time crash risk evaluation. Transp. Res. Part C 96, 192-207.
Yasmin, S., Eluru, N., Wang, L., Abdel-Aty, M.A., 2018. A joint framework for static and real-time crash risk analysis. Analy. Methods Acc. Res. 18, 45-56.
Yu, R., Abdel-Aty, M., 2013. Utilizing support vector machine in real-time crash risk evaluation. Accid. Anal. Prev. 51, 252-259.
Yuan, J., Abdel-Aty, M., 2018. Approach-level real-time crash risk analysis for signalized intersections. Accid. Anal. Prev. 119, 274-289.
Zheng, L., Ismail, K., Meng, X., 2014a. Freeway safety estimation using extreme value theory approaches: A comparative study. Accid. Anal. Prev. 62, 32-41.
Zheng, L., Ismail, K., Meng, X., 2014b. Shifted Gamma-Generalized Pareto Distribution model to map the safety continuum and estimate crashes. Saf. Sci. 64, 155-162.
Zheng, L., Ismail, K., Meng, X., 2014c. Traffic conflict techniques for road safety analysis: Open questions and some insights. Can. J. Civ. Eng. 41, 633-641.
Zheng, L., Ismail, K., 2017. A generalized exponential link function to map a conflict indicator into severity index within safety continuum framework. Accid. Anal. Prev. 102, 23-30.
Zheng, L., Sayed, T., Tageldin, A., 2018a. Before-after safety analysis using extreme value theory: A case of left-turn bay extension. Accid. Anal. Prev. 121, 258-267.
Zheng, L., Ismail, K., Sayed, T., Fatema, T., 2018b. Bivariate extreme value modeling for road safety estimation. Accid. Anal. Prev. 120, 83-91.
Zheng, L., Sayed, T., Essa, M., 2019a. Validating the bivariate extreme value modeling approach for road safety estimation with different traffic conflict indicators. Accid. Anal. Prev. 123, 314-323.
Zheng, L., Sayed, T., Essa, M., 2019b. Bayesian hierarchical modeling the non-stationary traffic conflict extremes for crash estimation. Analy. Methods Acc. Res. 23, 100100.
Zheng, L., Sayed, T., 2019a. From univariate to bivariate extreme value models: Approaches to integrate traffic conflict indicators for crash estimation. Transport. Res. Part C: Emerg. Technol. 103, 211-225.
Zheng, L., Sayed, T., 2019b. A comparison of traffic conflict indicators for crash estimation using peak over threshold approach. Transport. Res. Record: J. Transport. Res. Board 2673 (5), 493-502.
Zheng, L., Sayed, T., 2019c. Application of extreme value theory for before-after road safety analysis. Transport. Res. Record: J. Transport. Res. Board 2673 (4), 1001-1010.
Zheng, L., Sayed, T., 2019d. Bayesian hierarchical modeling traffic conflict extremes for crash estimation: A non-stationary peak over threshold approach. Analy. Methods Acc. Res. 24, 100106.


[^0]:    *Corresponding author.
    E-mail address: zhenglai@hit.edu.cn (L. Zheng).

