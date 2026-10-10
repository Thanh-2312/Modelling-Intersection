Usama Shahdah ${ }^{\mathrm{a}, *}$, Frank Saccomanno ${ }^{\mathrm{b}, 1}$, Bhagwant Persaud ${ }^{\mathrm{c}, 2}$<br>${ }^{\mathrm{a}}$ Public Works Engineering Department, Mansoura University, Mansoura 35516, Egypt<br>${ }^{\mathrm{b}}$ Department of Civil and Environmental Engineering, University of Waterloo, 200 University Avenue West, Waterloo, Ontario N2L3G1, Canada<br>${ }^{\mathrm{c}}$ Department of Civil Engineering, Ryerson University, 350 Victoria Street Toronto, Ontario M5B 2K3, Canada

## ARTICLE INFO

Article history:
Received 1 November 2013
Received in revised form 23 April 2015
Accepted 1 June 2015

Keywords:
Crash modification factors
Safety performance
Traffic microsimulation
VISSIM
Conflicts
Surrogate measures


#### Abstract

The primary objective of this paper is to provide a statistical relationship between traffic conflicts estimated from microsimulation and observed crashes in order to evaluate safety performance, in particular the effect of countermeasures. A secondary objective is to assess the effect of conflict risk tolerance and number of simulation runs on the estimates of countermeasure effects so obtained. Conflicts were simulated for a sample of signalized intersections from Toronto, Canada, using VISSIM microscopic traffic simulation and several crash-conflict relationships were obtained. A separate sample of treated intersections from Toronto was used to compare countermeasure effects from the integrated crash-conflict expression to a conventional, but rigorous crash-based Empirical Bayes before-and-after analysis that was already done, with the results published, for the same sites and treatment. The countermeasure considered for this investigation involved changing the left turn signal operation for the treated intersection sample from permissive to protected-permissive. The results support the view that countermeasure effects can be estimated reliably from conflicts derived from microsimulation, and more so when a suitable number of simulation runs and conflict tolerance thresholds are used in the crash-conflict relationship.


© 2015 Published by Elsevier Ltd.

## 1. Introduction

The application of observational models based on reported crash history is the most common approach used to assess safety performance and to determine the effectiveness of road safety interventions or countermeasures. Recently, microscopic traffic simulation has been used to estimate surrogate measures of safety performance based on high-risk vehicle interactions (or conflicts) for different road and traffic conditions. Proponents of traffic conflict simulation argue that by taking into account these conflicts a better understanding is gained of potential safety problems than is possible from conventional crash prediction models. They provide inferences not only on where crashes are likely to occur, but also why they are occurring at these sites and how specific countermeasures act to reduce these crashes.

In crash prediction models, crashes are viewed as objective and verifiable failures in the transportation system, thereby providing an objective basis for assessing lack of safety. However, not all transportation system failures result in crashes. Reliance on reported crashes poses a number of problems for these types of observational prediction models, such as low

[^0]reporting rates for less severe crashes, and unreported near-misses (Nicholson, 1985; Farmer, 2003; Davis, 2004; Saunier and Sayed, 2007). For example, Hauer and Hakkert (1989) reported that $50 \%$ of cashes with injuries and $60 \%$ of property-damage-only crashes were not reported in police data. These low severity crashes and near-misses may contain essential information concerning lack of safety that is important for effective safety intervention.

It seems reasonable that the use of conflicts can help to resolve sample size issues that can plague before-and-after treatment evaluation based on observed crashes. This approach has been used traditionally to estimate countermeasure effects or, more specifically, crash modification factors (CMFs). Empirical Bayes (EB) before-and-after methodology is now widely used for the estimation of CMFs because it can address regression-to-the-mean (RTM) problems, as well as account for other changes in safety not related to the treatment (Hauer, 1997). However, the EB method requires a large sample of untreated reference sites from which to develop Safety Performance Functions (SPFs), and this can be both costly and impractical (Lan, 2010). Furthermore, in conducting EB before-and-after evaluations, countermeasure effects can only be estimated after implementing treatment, and then only if sufficient site-years of treatment data are available to ensure statistically meaningful results. Crash-based prediction models are subject to lack of specification in the crash data, and this can severely restrict their ability to explain how treatments act to reduce crashes at a given site. They function essentially as a kind of "treatment effect black box", and it seems reasonable to suggest that more behavioral approaches are needed for estimating meaningful CMFs for safety intervention.

Recently, researchers have used surrogate measures of safety performance based on predicted high-risk vehicle interactions. When these interactions exceed established risk tolerance thresholds, they are referred to as traffic conflicts. Safety studies using traffic conflicts were initially proposed by Perkins and Harris (1967) and researchers from the General Motors Laboratory. Traffic conflict analysis provides an alternative approach to observational crash-based studies, where crash data are limited or where there is a need to assess the potential safety effects of a treatment prior to their implementation.

Amundsen and Hyden (1977) defined traffic conflicts as "observable situations in which two or more road users or vehicles approach each other in space and time to such an extent that there is a risk of collision if their movement remains unchanged". The use of traffic conflicts in safety studies is based on the premise that conflicts occur more frequently than crashes, although the mechanism leading to both types of events can be quite comparable. As a consequence, conflicts can address some of the statistical issues linked to the rare random nature of crashes, especially those crashes with low severity that tend to be under-reported. Additionally, they consider the transportation failure mechanism from a somewhat broader "more mechanistic" perspective than can be inferred from observational crash data alone (Brown, 1994; Sayed et al., 1994; Van der Horst, 1990).

Traffic conflicts or higher vehicle interactions can be estimated either by monitoring the traffic stream with a view to extracting vehicle paths over time or, more practically, by simulation of specific traffic input scenarios. Gettman and Head (2003a) discuss how microscopic traffic microsimulation platforms, such as VISSIM (PTV, 2012) and AIMSUN (TSS, 2013), can be used to estimate safety performance based for individual vehicle tracks. Microsimulation also provides a way to investigate different traffic scenarios, when vehicle tracking data are not available for a given site.

However, the traffic conflict approach has been criticized for lacking a formal link to observational crashes, which are normally viewed as being the only "verifiable" measure of transportation system failure from a safety perspective. Establishing a link to observed crashes can address this criticism and provide an observational basis for using simulated traffic conflicts to identify sites with safety problems and evaluate countermeasures, especially if it can be determined that these result in differences in conflicts but not in the relationship between crashes and conflicts. The need to provide a link between simulated conflicts and crashes provides the motivation for the research discussed in this paper.

This research has three basic objectives: (1) provide a statistical link between simulated traffic conflicts and observed crashes so as to evaluate the safety implications of specific treatments, (2) compare the resultant countermeasure effects to those obtained from a conventional Empirical Bayesian (EB) before and after analysis for the same sites and treatment, and (3) assess the effect on model results of key microsimulation inputs and assumptions, such as conflict tolerance thresholds and number of simulation runs. The paper builds on recent research by Sachi et al. (2013) who used conflict-based analysis to evaluate a right turn treatment at signalized intersections and El-Basyouny and Sayed (2013) who investigated the relationship between crashes and conflicts and came to a conclusion that traffic conflicts could provide useful insights into the failure mechanism that leads to crashes.

A crash-conflict relationship is calibrated for a sample of untreated signalized intersections from Toronto. A separate sample of treated intersections from Toronto was used to compare countermeasure CMF estimates from the integrated crash-conflict approach to CMFs from a published crash-based EB before-and-after study that used the same sample. The countermeasure considered for this comparison involved changing the left turn signal operation for the treated intersection sample from permissive to protected-permissive. Traffic conflicts for left turn opposing (LTOPP) movements were simulated using VISSIM 5.40 (PTV, 2012). The inputs into the simulation were the observed intersection peak hour approach volumes and turning movements (through, left-turn and right-turn), as reported in the database.

## 2. Microsimulation of traffic conflicts

A sample of 53 signalized untreated intersections from the Toronto database was used to investigate the statistical relationship between crashes and simulated traffic conflicts, and between crashes and intersection approach volumes.

Table 1
Traffic volume and turning movements at untreated sites.
| Summary statistic | Volume (vph) in major | Volume (vph) in minor | \%RT major | \%RT minor | \%LT major | \%LT minor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mean | 1301.62 | 764.91 | 10.63 | 16.07 | 6.36 | 12.04 |
| St. deviation | 417.22 | 270.57 | 6.24 | 8.31 | 5.87 | 9.70 |
| Minimum | 663 | 48 | 0 | 0 | 0 | 0 |
| Maximum | 2246 | 1367 | 34 | 54 | 33 | 46 |


Table 2
Crash data at untreated sites (2001-2004).
| Summary statistic | LTOPP |
| :--- | :--- |
| Sum | 309 |
| Mean | 5.83 |
| St. deviation | 5.56 |
| Minimum | 0 |
| Maximum | 20 |


The compiled intersection database consists of major and minor approach volumes, mostly from 2002 and 2003, for the morning (AM) peak hour, including left, through and right turning movements for each approach. In addition, pedestrian counts and signal timings were available for the periods being analyzed.

The crash data used in this analysis were reported for the period 2001-2004. Data were available for all crashes for 24 h and the AM peak hour. Intersection geometries were obtained from the Toronto Traffic Control Centre, and in addition Google Earth software (Google 2012) was used to determine the lengths of the left-turn and right-turn exclusive lanes, utilizing the facility of this tool to access historical images. Traffic volume inputs (in vehicles per hour (vph)) for the simulation are summarized in Table 1 for the sample intersections, while the corresponding left-turn opposing (LTOPP) crash data are summarized in Table 2. Only the LTOPP crashes were used in this study in order to demonstrate how the number of simulation runs can affect the calibrated crash-conflict relationship and its subsequent crash modification factor (CMF). LTOPP refers to interactions between left turning vehicles in conflict with through vehicles entering the intersection from the opposing direction.

Traffic conflict measures were obtained as a function of 'vehicle-pair' speeds and spacing. Several expressions of safety performance have been introduced in the literature, for example, Gettman and Head (2003a), Archer (2005), Cunto (2008), and Cunto and Saccomanno (2008). In this paper, we use Time-to-Collision (TTC), where this measure is defined as the time separation between two vehicles before they collide, if both vehicles continue at their present speeds along their respective trajectories. This measure has been widely accepted due to its simplicity of computation and its ability to reflect crash potential (Gettman and Head, 2003a; Archer, 2005).

It is worth noting that the conflicts based on TTC were extracted using the Surrogate Safety Assessment Model (SSAM) (Pu and Joshi, 2008). A space-time diagram identifying TTC, for a conflict point event (i.e. LTOPP or crossing conflicts) is shown in Fig. 1. In this Figure, the trajectories of the crossing vehicle and the through vehicle are represented by curve "A" and curve "B", respectively. In such cases, TTC can be estimated as (Gettman and Head, 2003a,b):

$$
\text { TTC }=t_{4}-t_{3}
$$

where
$t_{3}=$ time when either corners of a crossing vehicle leave the encroachment point (or encroachment end time) and
$t_{4}=$ projected arrival time of the through-vehicle at the conflict point.
SSAM uses a unique algorithm to define conflict events and hence to obtain different parameters related to each conflict event, such as, times $t_{1}-t_{5}$, speed and acceleration/deceleration of vehicles in question. In this analysis, these parameters were estimated every $1 / 10 \mathrm{~s}$ to yield a simulation resolution of 10 simulation seconds for each second. For more information on how the computational algorithm works and how SSAM estimates different surrogate safety indicators and different conflict types, the reader is referred to Gettman and Head (2003b). Furthermore, more information on the nature of TTC can be found in Sayed and Zein (1999), Archer (2005), and Cunto (2008).

The 53 untreated signalized intersections were simulated using the VISSIM microscopic traffic simulation platform v5.40 (PTV, 2012) to extract vehicle trajectories over time. The Wiedemann-74 car-following model was selected due to its suitability for urban traffic conditions as suggested in the VISSIM manual. The VISSIM parameters were selected to reflect more realistic driving behavior and to ensure that the observed vehicles during the peak-hours can enter the simulation network within the specific simulation period; these are summarized in Table 3.

In our analysis, the AM peak hour was simulated to obtain all vehicle trajectories at the 53 untreated intersection sites. These serve as inputs into the estimation of traffic conflicts. For each intersection, 30 and 50 simulation runs with 30 and 50 random seeds, respectively were used to capture the randomness in traffic with 5-min warming-up period. Although only

![](https://cdn.mathpix.com/cropped/41486c50-0f37-4b4c-b0c0-0688ce62c968-4.jpg?height=840&width=1191&top_left_y=183&top_left_x=345)
Fig. 1. LTOPP time to collision (TTC) identified on conflict point diagram (modified from Gettman and Head, 2003a,b).

Table 3
Vissim parameters assumed.
| Behavioral parameter | Assumption |
| :--- | :--- |
| Driving behavior | Urban (motorized) |
| Car-following | Wiedemann 74 with $\begin{aligned} & \mathrm{ax}=2.00 \mathrm{~m}^{1} \\ & \mathrm{bx} \_ \text {add }=2.00^{2} \\ & \mathrm{bx} \_ \text {mult }=3.00^{3} \\ & \text { Smooth close-up } \end{aligned}$ |
| Lane change | Advanced merging <br> Cooperative lane change |
| Lateral parameters | Keep lateral distance to vehicles in on next lane(s) <br> Consider next turning decision |
| Signal control decision model | One decision |
| Conflict areas (left turn only) | Front gap $=0.00 \mathrm{~s}$ <br> Rear gap $=0.00 \mathrm{~s}$ <br> Avoid blocking = 0 for all cases and = 1 for 2 LT lanes |


[^1]one hour (typically the AM peak hour) was used in this analysis, a 2-h simulation time was used to ensure that all vehicles have entered the simulation network. Our assumption is that the ratio of peak-hour traffic to average daily traffic is approximately constant across sites and time and therefore that peak hour volumes and conflicts can reasonably be used as a "surrogate" for average daily traffic volumes and daily conflicts. This is a common assumption in expanding part day counts, which are typically obtained on different days, to average daily traffic that has been used successfully in calibrating crash-volume models.

For each simulation run, the Surrogate Safety Assessment Model (SSAM) (Pu and Joshi, 2008) was used to estimate the total number of conflicts from the trajectories of simulated vehicles, based on two time-to-collision thresholds: TTC $\leqslant 1.5 \mathrm{~s}$ and TTC $\leqslant 0.5$ s.

Table 4 summarizes the simulation results for LTOPP conflicts for the two TTC thresholds ( $\leqslant 1.5$ and $\leqslant 0.5 \mathrm{~s}$ ) for 30 and 50 simulation runs. Only LTOPP vehicle-to-vehicle conflicts are considered as they represent the dominant treatment effect measure in changing from permitted to protected-permissive left turn operation. The simulation assumes normal road and weather conditions in that the VISSIM parameters used in this simulation were calibrated for normal weather

Table 4
Simulated LTOPP conflicts for the 53 Untreated Sites.
| Summary statistic | $\mathrm{TTC} \leqslant 1.50 \mathrm{~s}$ |  | $\mathrm{TTC} \leqslant 0.50 \mathrm{~s}$ |  |
| :--- | :--- | :--- | :--- | :--- |
|  | 30 runs | 50 runs | 30 runs | 50 runs |
| Average (per run) over all sites | 30.37 | 29.78 | 3.20 | 8.62 |
| Mean per site (per run) | 0.57 | 0.56 | 0.06 | 0.16 |
| St. deviation | 0.46 | 0.44 | 0.07 | 0.17 |
| Minimum | 0.00 | 0.00 | 0.00 | 0.00 |
| Maximum | 1.73 | 1.82 | 0.30 | 0.90 |


conditions. Accordingly, the crash data used in the developing the crash-conflict relationships were filtered to apply to normal weather.

The results in Table 4 indicate that for the lower severity threshold (TTC < 1.50 s), the number of simulation runs (30 versus 50) has had little or no effect on the resulting number of conflicts. On the other hand, for the higher severity threshold (TTC < 0.50 s), the number of runs was found to have a significant effect on the resultant number of conflicts. This is reasonable since for the higher the threshold, fewer simulated conflicts would be expected, and more simulation runs would be required to obtain stable long-term pattern of simulated conflicts.

## 3. Calibration of the crash-conflict model

As noted above, 53 untreated signalized intersections were used to obtain a statistical relationship between observed LTOPP crashes and simulated LTOPP conflicts. To ensure that the geometric configuration of the intersection does not confound the relationship, only sites with no exclusive right turn or left turn lanes were used in the analysis. Only vehicle-to-vehicle crashes that took place during normal weather conditions were considered.

A Generalized Linear Negative Binomial (NB) model was fit to the crash-conflict data for the 53 untreated intersections in accordance with conventional practice in crash prediction modeling. The NB model parameters were estimated by maximum likelihood using the PSCL (Political Science Computational Laboratory) in the R-statistical software (2012). The model form of the crash-conflict SPF proposed in this study is as given in Eq. (2).

$$
L N\left(C R_{j}^{i}\right)=L N \alpha+\beta \times L N\left(C F_{j}^{i}\right)
$$

where
$C R_{j}^{i}=$ the expected number of crashes at site $i$ with type $j$,
$C F_{j}^{i}=$ the number of simulated conflicts at site I with type $j$,
$L N=$ the natural logarithm, and
$\alpha, \beta=$ the calibrated coefficients.
Table 5 summarizes the results of the LTOPP crash-conflict model calibration for TTC $\leqslant 1.50$ and $\leqslant 0.50 \mathrm{~s}$. For TTC $<1.50 \mathrm{~s}$, the AIC difference was found to be less than 5, which is small enough to indicate that there is no significant difference between the two models.

It should be noted that the value of the $\beta$ parameter associated with the prediction model differs significantly depending on whether 30 or 50 simulation runs were carried out. This is important, since it suggests that the number of simulation runs will have an effect on the crash-conflict model itself. Furthermore, this suggests that care should be taken in choosing the appropriate number of simulation runs prior to linking crashes to conflicts. For the higher severity threshold (TTC < 0.50 s) the results are seen to be similar in that, again, the value of $\beta$ in the crash-conflict expression was found to be sensitive to

Table 5
Parameter estimates for crash-conflict models.
| Parameter estimates | $\mathrm{TTC} \leqslant 1.50 \mathrm{~s}$ |  | $\mathrm{TTC} \leqslant 0.50 \mathrm{~s}$ |  |
| :--- | :--- | :--- | :--- | :--- |
|  | 30 runs | 50 runs | 30 runs | 50 runs |
| LN $\alpha$ [SE] | 2.0942 [0.144] | 2.1372 [0.1415] | 2.6937 [0.4100] | 2.8013 [0.3015] |
| $\beta$ [SE] | 0.4969 [0.120] | 0.5809 [0.1267] | 0.3439 [0.142] | 0.5556 [0.1431] |
| Dispersion parameter | 0.463 | 0.416 | 0.627 | 0.530 |
| Residual deviance | 59.46 | 59.51 | 59.34 | 58.76 |
| Degrees of freedom | 51 | 51 | 51 | 51 |
| Akaike's Information Criterion (AIC) | 289.04 | 285.55 | 300.01 | 293.16 |
| 2 log likelihood | -283.04 | -279.55 | -294.01 | -287.16 |


Table 6
Simulated LTOPP conflicts for treated sites (average per run over all sites).
| Conflict threshold | Parameter | Value |
| :--- | :--- | :--- |
| $\mathrm{TTC} \leqslant 1.50 \mathrm{~s}$ | Conflicts before [St. deviation] | 164.00 [11.77] |
|  | Conflicts after [St. deviation] | 118.70 [10.13] |
|  | $\rho$ [St. deviation] | 0.724 [0.105] |
| $\mathrm{TTC} \leqslant 0.50 \mathrm{~s}$ | Conflicts before [St. deviation] | 19.18 [4.49] |
|  | Conflicts after [St. deviation] | 16.28 [4.19] |
|  | $\rho$ [St. deviation] | 0.849 [0.332] |


Table 7
Crash modification factors from LTOPP conflicts at 47 treated intersections.
| Conflict threshold | Parameter | Number of simulation runs |  |
| :--- | :--- | :--- | :--- |
|  |  | 30 runs | 50 runs |
| $\mathrm{TTC} \leqslant 1.50 \mathrm{~s}$ | $\rho$ [St. deviation] | 0.724 [0.10542] | 0.724 [0.10542] |
|  | $B$ | 0.4969 | 0.5809 |
|  | $a_{1}$ | 0.5847 | 0.6652 |
|  | $a_{2}$ | -0.2032 | -0.1926 |
|  | CMF [SE] | 0.852 [0.0090] | 0.829 [0.0102] |
| Statistical significance with EB estimate at 5\% confidence level $\mathrm{TTC} \leqslant 0.50 \mathrm{~s}$ |  | Significantly different | Significantly different |
|  | $\rho$ [St. deviation] | 0.8488 [0.3321] | 0.8488 [0.3321] |
|  | $B$ | 0.3439 | 0.5556 |
|  | $a_{1}$ | 0.3830 | 0.5976 |
|  | $a_{2}$ | -0.1480 | -0.1564 |
|  | CMF [SE] | 0.94518 [0.0187] | 0.913 [0.0291] |
| Statistical significance with EB estimate at 5\% confidence level |  | No significant difference | No significant difference |


both the number of simulation runs as well as to the TTC threshold. It is worth noting that using more than 50 runs does not materially change the value of $\beta$. For example, for $\mathrm{TTC} \leqslant 1.50 \mathrm{~s}, 70$ simulation runs increases the value of $\beta$ by only 0.004 .

## 4. Estimating countermeasure effects

In this section of the paper, the estimation of countermeasure effects using VISSIM simulated conflicts and the crash-conflict model are compared with CMFs based on rigorous, conventional Empirical Bayes (EB) before-and-after crash analysis conducted by Srinivasan et al. $(2011,2012)$ for the same countermeasure and sample of treated Toronto intersections. The countermeasure under consideration is a change in left turn signal priority from permissive to protected-permissive on a single approach at 47 intersections. In our analysis, either of the AM or PM peak hours were simulated to obtain all vehicle trajectories at the 47 treated intersection sites depending on the time that the LT protected-permissive phase was used.

Table 6 shows the simulated conflicts before and after treatment for the two TTC thresholds ( $\leqslant 1.50 \mathrm{~s}$ and $\leqslant 0.50 \mathrm{~s}$ ) based on 50 simulation runs. Also shown is the ratio of simulated conflicts after treatment over those before $(\rho)$. These were found to be less than 1.0 for both TTC thresholds, suggesting that using only conflicts there is a safety improvement from the introduction of protected-permissive left turn signal operation. This would be the "end of story" on countermeasure safety effect, except that in this paper we wished to also provide a link to CMFs that are crash-based.

In this analysis it is assumed that the crash-conflict relationship parameters do not change with treatment. To obtain values for these parameters, an independent untreated data set was used to provide estimates of $\alpha$ and $\beta$. Using the relationship (Eq. (2)) introduced earlier between simulated conflicts and observed crashes, the Crash Modification Factor (CMF) can be expressed as a function of the conflict-based expressions [ratio $\rho$ in Eq. (3)].

CMF is expressed as the ratio of the expected number of crashes after treatment to that before, such that:

$$
C M F=\frac{\alpha \cdot\left(C F_{a}\right)^{\beta}}{\alpha \cdot\left(C F_{b}\right)^{\beta}},
$$

and this can be expressed as:

$$
C M F=\left(\frac{C F_{a}}{C F_{b}}\right)^{\beta}=(\rho)^{\beta}
$$

The variance of CMF can be estimated using the approach discussed in Shahdah et al. (2014) as:

$$
\operatorname{Var}[C M F]=a_{1}^{2} \cdot \operatorname{Var}(\rho)+a_{2}^{2} \cdot\left(3 \times(\operatorname{Var}(\rho))^{2}\right)
$$

Table 8
Results of the EB before-and-after (Srinivasan et al., 2011, 2012).
| Crash type | \# of sites | Expected crashes after | Observed crashes after | CMF | SE |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LTOPP | 47 | 341 | 314 | 0.919 | 0.069 |


The parameters $a_{1}$ and $a_{2}$ can be estimated as:

$$
\begin{aligned}
& a_{1}=\frac{(\rho)^{\beta} \cdot \beta}{\rho} \\
& a_{2}=\frac{(\rho)^{\beta} \cdot \beta^{2}-(\rho)^{\beta} \cdot \beta}{2(\rho)^{2}}
\end{aligned}
$$

Applying Eq. (4) to the treated intersection sample from Toronto, the results in Table 7 were obtained for the two levels of simulation runs and two TTC thresholds. It should be noted that increasing TTC severity (i.e. reducing the threshold from higher to lower values) reduces the effectiveness of the treatment. This was expected since the higher threshold (TTC < 1.50 s) picks up a larger number of conflicts. For a given threshold the resultant CMF does not appear to be affected significantly by the number of simulation runs.

To further assess the viability of the approach, the results from Table 7 were compared to the results from crash-based EB before-after analysis, as reported by Srinivasan et al. $(2011,2012)$ for the same Toronto intersection sample and treatment. The EB before-and-after results are summarized in Table 8. It should be noted that the CMF estimates for TTC $\leqslant 0.50 \mathrm{~s}$ are closer to those obtained by the EB before-and-after analysis than was observed for TTC $\leqslant 1.50 \mathrm{~s}$. The CMF estimates for TTC < 0.50 s with 30 and 50 runs were not found to be statistically different at the 5\% level from the CMF estimate from the EB before-and-after analysis. However, for 50 runs CMF estimates using simulation were found to be closer to those obtained from the EB analysis.

## 5. Further investigation of the effect of the number of simulation runs

Given the apparent sensitivity of the results to the number of simulation runs for estimating conflicts, a fundamental question that needs to be addressed is: What is the recommended number of runs required to yield the best estimates of the CMF? A possible answer can be found in the standard statistical inference expression, where for a given error tolerance the minimum required number of runs is (Johnson, 2000):

$$
N=\left(\frac{t_{\left(1-\frac{\alpha}{2}\right), N-1} \times \sigma}{E}\right)^{2}
$$

where
$N=$ required number of simulation runs,
$\sigma=$ the sample standard deviation of the number of simulated conflicts,
$t=$ student's $t$-statistic for two-sided error of $\alpha / 2$ (totals $\alpha$ percent) with $N-1$ degrees of freedom (for 10 runs, $t=2.3$ ), and
$E=$ allowed error range.
The allowed error range can be taken as a percentage of the mean, such that:

$$
E=\varepsilon \times \mu
$$

where
$\mu=$ the mean of the number of simulated conflicts based on the initial set of simulations runs and
$\varepsilon=$ the allowable error specified as a fraction of the mean $\mu$.
Table 9 summarizes the required number of simulation runs with respect to the acceptable error. For a low severity threshold, since more conflicts are obtained, fewer simulation runs would be required for a given tolerance. For TTC < 0.50 s

Table 9
Minimum required number of simulation runs.
| TTC threshold | Error ( $\varepsilon$ ) (\%) | Minimum required runs |
| :--- | :--- | :--- |
| TTC < 1.50 | 5 | 59 |
| TTC < 1.50 | 10 | 15 |
| TTC < 0.50 | 5 | 196 |
| TTC < 0.50 | 10 | 49 |


a total of 196 runs are recommended to obtain a tolerance of $5 \%$, as compared to only 59 runs for a lower severity threshold of TTC < 1.50 s. In summary, increasing the error tolerance suggests a corresponding increase in the recommended number of simulation runs.

It should be noted that from Table 4 for a lower threshold (TTC < 1.50 s) increasing the number of simulation runs from 30 to 50 has a negligible effect on the number of traffic conflicts. For this lower risk threshold, it is recommended that we choose the number of simulation runs to satisfy a given error tolerance expressed as a percentage of the mean.

From Table 9, for a TTC of <1.50 s 50 simulation runs will be sufficient for an error equal to 10\% of the mean number of conflicts. For the higher TTC threshold (TTC < 0.50 s), since the number of simulated conflicts is reduced a minimum of 50 simulation runs would be needed to obtain an error of 10\% of the mean. From this cursory analysis we would recommend a minimum of 50 runs for the higher conflict threshold. Some additional analysis based on 70 simulation runs was carried out for TTC < 0.50 s with negligible change in the coefficients in Table 5 as noted earlier.

## 6. Conclusion

The results have demonstrated that surrogate safety measures based on traffic conflicts estimated from microsimulation can be used to evaluate the effectiveness of countermeasures and yield crash modification factors that are consistent with those obtained from a rigorous, conventional EB before and after analysis. As the threshold for conflict definition is increased (e.g. lower time-to-collision), so too is the consistency of the results between conflict-based and crash-based evaluations. This is expected since increased thresholds reflect higher risk conflicts, and these presumably are the events that are more likely to result in crashes. The simulated traffic conflict approach has a decided advantage over the conventional observational crash-based approach in that countermeasure effects (i.e., CMFs) can be estimated even before treatments are introduced or when the crash sample is too small to obtain reliable CMFs from crash-based evaluations.

This paper has presented a statistical approach to link simulated conflicts with observed crashes. This link can provide an observational basis that reports simulation results in an equivalent CMF format. The number of simulation runs and TTC thresholds were found to have a significant effect on CMF estimates as obtained from the integrated crash-conflict model. Furthermore, although the 53 sites used for the research seem to give reasonable results, more work is needed to investigate the appropriate sample size of reference sites when calibrating the crash-conflict relationship.

## Acknowledgment

The authors would like to acknowledge Toronto Traffic Management Center (the Traffic Safety Unit) for providing the data required to complete this research. The research was supported by grants from the Natural Sciences and Engineering Research Council of Canada and Transport Canada.

## References

Amundsen, F., Hyden, C., 1977. In: Proceedings of the First Workshop on Traffic Conflicts. Institute of Transport Economics, Oslo.
Archer, J., 2005. Indicators for Traffic Safety Assessment and Prediction and their Application in Micro-Simulation Modelling: A Study of Urban and Suburban Intersections. PhD thesis, Royal Institute of Technology, Kungliga Tekniska Högskolan (KTH), SE-100 44 Stockholm, Sweden.
Brown, G.R., 1994. Traffic conflicts for road user safety studies. Canadian J. Civ. Eng. 21, 1-15.
Cunto, F., 2008. Assessing Safety Performance of Transportation Systems using Microscopic Simulation. PhD dissertation, University of Waterloo, Ontario, Canada.
Cunto, F., Saccomanno, F.F., 2008. Calibration and validation of simulated vehicle safety performance at signalized intersections. Accid. Anal. Prevent. 40, 1171-1179.
Davis, G., 2004. Possible aggregation biases in road safety research and a mechanism approach to accident modeling. Accid. Anal. Prevent. 36, 1119-1127.
El-Basyouny, K., Sayed, T., 2013. Safety performance functions using traffic conflicts. Safe. Sci. 51, 160-164.
Farmer, C.M., 2003. Reliability of police-reported information for determining accident and injury severity. Traffic Injury Prevent. 4, 38-44.
Gettman, D., Head, L., 2003a. Surrogate safety measures from traffic simulation models. In: Transportation Research Record: Journal of the Transportation Research Board, No. 1840. Transportation Research Board of the National Academies, Washington, DC, 2003, pp. 104-115.
Gettman, D., Head, L., 2003b. Surrogate Safety Measures from Traffic Simulation Models: Final Report. No. FHWA-RD-03-050, 2003.
Google Earth (Version 6.2.2.6613) [Software], 2012. <http://www.google.com/ earth/index.html>.
Hauer, E., Hakkert, A.S., 1989. The extent and implications of incomplete accident reporting. In: Transportation Research Record: Journal of the Transportation Research Board, vol. 1185, Transportation Research Board of the National Academies, Washington, DC, pp. 1-10.
Hauer, Ezra, 1997. Observational Before-After Studies in Road Safety: Estimating the Effect of Highway and Traffic Engineering Measures on Road Safety. Pergamon Press, Elsevier Science Ltd., Oxford, UK.
Johnson, A.Richard, 2000. Miller\& Freund's Probability \& Statistics For Engineers, sixth ed. Prentice-Hall.
Lan, Bo, 2010. Exploration of Theoretical and Application Issues in Using Fully Bayes Methods for Road Safety Analysis. PhD dissertation, Ryerson University, Ontario, Canada.
Nicholson, A.J., 1985. The variability of accident counts. Accid. Anal. Prevent. 17, 47-56.
Perkins, S.R., Harris, J.L., 1967. Traffic Conflict Characteristics, Accident Potential at Intersections. GeneralMotors Corporations, Warren, MI.
Pu, L., Rahul Joshi, 2008. Surrogate Safety Assessment Model (SSAM): Software User Manual. Publication FHWA-HRT-08-050. Federal Highway Administration, U.S. Department of Transportation. [http://www.fhwa.dot.gov/publications/research/safety/08050/08050.pdf](http://www.fhwa.dot.gov/publications/research/safety/08050/08050.pdf) (accessed 15.03.12).
R Development Core Team, 2012. R: A Language and Environment for Statistical Computing. R Foundation for Statistical Computing, Vienna, Austria. (ISBN 3-900051-07-0). [http://www.R-project.org](http://www.R-project.org) (accessed 15.03.12).
Sachi, E., Sayed, T., deLeur, P., 2013. A comparison of collision-based and conflict-based safety evaluations: the case of right turn smart channels. Accid. Anal. Prevent. 59, 260-266.
Saunier, N., Sayed, T., 2007. Automated road safety analysis using video data. In: Transportation Research Record: Journal of the Transportation Research Board, No. 2019. Transportation Research Board of the National Academies, Washington, DC, pp. 57-64.

Sayed, T., Zein, S., 1999. Traffic conflict standards for intersections. Transp. Plann. Technol. 22, 309-323.
Sayed, T., Brown, G., Navin, F., 1994. Simulation of traffic conflicts at unsignalized intersections with TSC-Sim. Accid. Anal. Prevent. 26, 593-607.
Shahdah, U., Saccomanno, F., Persaud, B., 2014. Integrated traffic conflict model for estimating crash modification factors. Accid. Anal. Prevent. 71, 228-235.
Srinivasan, R., Gross, F., Lyon, C., Persaud, B., Eccles, K., Hamidi, A., Baek, J., Smith, S., Lefler, N., Sundstrom, C., Carter, D., 2011. Evaluation of safety strategies at signalized intersections. NCHRP Rep. 705.
Srinivasan, R., Lyon, C., Persaud, B., Baek, J., Gross, F., Smith, S., Sundstorm, C., 2012. Crash Modification Factors for Changing Left Turn Phasing. TRB 2012 Paper No. 12-2521, TRB 2012 Annual Meeting Compendium.
Transport Simulation System (TSS), 2013. AIMSUN. [http://www.aimsun.com/wp/?page_id=21]](http://www.aimsun.com/wp/?page_id=21%5D) (accessed October, 2013).
Van der Horst, A.R.A., 1990. A Time-based Analysis of Road User Behaviour in Normal and Critical Encounters. PhD thesis, Delft University of Technology.
VISSIM 5.40 User Manual, 2012. Planung Transport Verkehr AG, Stumpfstraße 1, D-76131 Karlsruhe, Germany.


[^0]:    * Corresponding author. Tel.: +20 128798 1901; fax: +20 502244690.
    E-mail addresses: usama.shahdah@mans.edu.eg (U. Shahdah), saccoman@uwaterloo.ca (F. Saccomanno), bpersaud@ryerson.ca (B. Persaud).
    ${ }^{1}$ Tel.: +1 519888 4567×32631; fax: +1 5198884349.
    ${ }^{2}$ Tel.: +1 416979 5000x6464.

[^1]:    ${ }^{1}$ The average standstill distance with standard deviation of 0.30 m.
    ${ }^{2}$ The additive part of safety distance.
    ${ }^{3}$ The multiplicity part of safety distance.

