$21^{\text {st }}$ EURO Working Group on Transportation Meeting, EWGT 2018, $17^{\text {th }}-19^{\text {th }}$ September 2018, Braunschweig, Germany

# Surrogate Safety Measures from Traffic Simulation Models a Comparison of different Models for Intersection Safety Evaluation 

Vittorio Astarita ${ }^{\text {a* }}$, Demetrio Carmine Festa ${ }^{\text {a }}$, Vincenzo Pasquale Giofrè ${ }^{\text {a }}$ and Giuseppe Guido ${ }^{\mathrm{a}}$<br>${ }^{a}$ Univesità della Calabria, Via Ponte Bucci, Rende 87036, Italy


#### Abstract

This paper offers an assessment of intersection safety evaluation through the use of different traffic micro-simulators. The aim of the paper is to evaluate the applicability of traffic simulation in the safety evaluation of typical intersections. The considered scenarios are three real cases: a roundabout, a traffic light regulated intersection and an unregulated intersection. All cases were chosen in urban areas, where statistically the number of car interactions that could potentially turn into collisions is greater. All scenarios were assessed with three different microscopic traffic simulation models that were coupled with the FHWA tool SSAM.


© 2019 The Authors. Published by Elsevier Ltd.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0/)
Selection and peer-review under responsibility of the scientific committee of the $21{ }^{\text {st }}$ EURO Working Group on Transportation Meeting, EWGT 2018, $17^{\text {th }}-19^{\text {th }}$ September 2018, Braunschweig, Germany.

Keywords: Traffic simulation models; Surrogate safety measures; Urban traffic safety

## 1. Introduction

This paper intends to offer a useful assessment of the application of surrogate safety measures in the design and traffic planning of urban areas as well as verifying that the performances of different micro-simulation models are comparable in the evaluation of typical intersection scenarios, thus showing that traffic simulation is a viable and consistent method to perform safety evaluation on different intersection designs.

There are still ongoing research efforts devoted to assessing the range of applicability of surrogate safety measures evaluated with traffic simulation. This paper presents three real cases assessing results of three different traffic simulation models and offering useful results that can be easily replicated.

[^0]The considered scenarios are: a roundabout, a traffic light regulated intersection and an unregulated intersection. All the cases were chosen in urban areas and all the scenarios were assessed with microscopic traffic simulation models that were coupled with the FHWA tool SSAM by Gettman et al. (2008).

The first applications of microscopic simulation to the evaluation of traffic safety performances were introduced by Cooper and Ferguson (1976) and Darzentas et al. (1980). For the first time the concept was presented that road safety can be compromised by recurring cases where trajectories of vehicles almost overlap.

Microsimulation allows an observer to reproduce in detail traffic and the trajectories of vehicles thus establishing potential conflicts. The applicability of this approach is based on a detailed simulation reproduction of trajectories and the assumption that simulated data are comparable with observed data.

Cunto and Saccomanno (2008) affirm that the major steps in applying simulation is to ensure that important model inputs have been determined based on observational data and they ensure calibration of the used traffic simulation model on traffic safety performance values obtained from real trajectories extracted from video.

Calibration in micro-simulation applications is, in fact, important to guarantee the quality of any traffic measure evaluation and in the case of traffic safety measure this is even more delicate since results are obtained from the microscopic interactions among simulated vehicles.

Many papers have been published on micro-simulation model calibration also, in some cases, with specific focus on traffic safety performance measures (among others Guido et al., 2011;Hourdakis et al., 2003), this paper, instead, intends to focalize on the practical application of commonly used traffic simulation models to traffic safety performance evaluation in a real urban setting. The paper aims to be useful in evidencing procedures and results that can be reproduced in intersection safety evaluation.

Results that are presented in the following show that surrogate safety measures must be used with great caution in assessing how real intersection layouts can affect the safety level. Presented results, in fact, are in contradiction with well-known established road safety facts. Roundabouts are well known for being safer than other kinds of intersection. This knowledge is based on accident statistical data by Persaud et al. (2001) and also on the empirical fact that vehicles have necessarily to slow down when entering potential conflict areas. Instead this paper shows for the first time, using different traffic simulation models and car-following rules, with easy to reproduce results, that, no matter what traffic micro-simulation model a practitioner is going to use, traditional SSAM surrogate safety measures will show that a roundabout is less safe than other kind of intersections.

Results of this paper on the roundabout case and other presented cases confirm the intuitions of other authors Chen et al. (2011) that traditional surrogate safety measures are not the best way to assess real safety at intersections and in general in urban areas. More research on different surrogate safety measures that take into account also the speed and relative speed of vehicles must be dedicated to establish better and different safety measures from what is commonly used.

## 2. Methodology

The surrogate safety measures that are analyzed in this paper are all common and widely used: TTC, PET, Maximum speed and DR.

TTC (Time To Collision) by Sayed et al. (1994) and by Hayward (1972) is the time that a vehicle would take to collide with another vehicle if the current relative velocity at a given point was maintained. When a potential conflict is in progress, the TTC value varies over time, and the critical measure of conflict severity becomes the minimum TTC value in the couple of vehicles interacting. A standard safety limit has been proposed in 1.50 seconds by Van der Horst (1991). TTC formulation is as follows:

$$
T T C_{f}=\frac{d}{V_{f}-V_{l}}
$$

Where $V_{f}$ is the speed of the vehicle under examination (following), $V_{l}$ is that of the vehicle in front (leader) and $d$ the distance between the two vehicles.

PET (Post Encroachment Time) by Hydén (1987) is defined as the time period from the time the first road user is leaving a conflict zone until the second user reaches it.

The results obtained by the simulators, for each scenario, are the result of the average of 20 simulations, in order to guarantee greater mathematical precision. The three different simulation models have been calibrated on the three given scenarios obtaining common traffic simulation results. The evaluation of traffic safety measures intends to establish whether the three simulation models, that are able to reproduce consistently general traffic conditions, are able with the same settings to reproduce also similar results (among them) for the evaluation of traffic safety measures.

The proposed methodology does not calibrate the three simulation models on real measured traffic safety performances since this would obviously bring similar results from the point of view of traffic safety performance, instead the objective is that of showing the applicability and reliability of the simulation models in assessing traffic safety in a common situation with a common parameter calibration.

## 3. Case studies

In all three cases (Fig. 1) traffic surveys were carried out throughout the day, focusing mainly on peak times, where traffic is heavier, from 8.30 to 9.30, from 12.30 to 13.30 and from 17.00 to 19.00. These three cases represent a sample of the most common scenarios in cities and are: 1 a roundabout, 2 a signalized intersection and 3 a complex unsignalized intersection.

![](https://cdn.mathpix.com/cropped/bf4ae99f-f402-4ee6-8044-da21b1878da4-3.jpg?height=478&width=1634&top_left_y=951&top_left_x=127)
Fig. 1. Studied cases.

These three cases represent the most common scenarios in cities. From the point of view of security, scenario 1 is commonly considered the safest since speeds are lower and scenario 3, is considered the most dangerous, because of its complexity, the number of conflicts and visibility issues that would suggest an increased risk of accidents.

## 4. Microsimulation models

It is expected that different simulation models commonly used in professional applications and cited in research papers would bring similar results in the simulation of typical urban intersections and there are many research paper that showed reliability of traffic flow statistical results of applied micro-simulation. This paper instead presents results on the ability of such models to reproduce reliable and reproducible surrogate safety measures.

The traffic micro-simulation models that have been applied are Aimsun, VISSIM and Tritone. Aimsun is a microscopic traffic simulator developed at the Department of Statistics and Operations Research of the Politècnica de Catalunya University by Barceló and Casas (2002), Spain. Aimsun is based on the car-following model devised by Gipps in 1981 and then modified by TSS (Gipps, 1981, 1986; TSS-Transport Simulation Systems, 2002). In Aimsun vehicles accelerate by hoping to reach the desired speed and slow down when they have to avoid a collision. Speed is influenced by vehicle characteristics and limitations imposed by the leader vehicle, as shown in the following equation.

$$
V_{n}(t+T)=-b T+\sqrt{b^{2} T^{2}+b\left\{2 d-V_{n}(t) T+\frac{V_{n-1}(t)^{2}}{b^{\prime}}\right\}}
$$

Where b is the maximum deceleration of the considered vehicle in $\mathrm{m} / \mathrm{s} 2, \mathrm{~b}$ is an estimate of the desired deceleration of the leading vehicle in $\mathrm{m} / \mathrm{s} 2, \mathrm{~d}$ is distance between the vehicles, T is the reaction time of the driver of the follower vehicle.

VISSIM instead was developed in Germany by PTV. It is based entirely on the car-following models devised by Wiedemann in 1974 and 1991. These are psycho-physical models, behaviour changes from one model to another (braking, following, approaching, free driving) based on predetermined perceptual threshold levels, which form the basis of psychophysical models. These thresholds are defined as a combination of the difference in speed and position on the road.

Finally, Tritone (Astarita et. al., 2012a, 2017) based on an experience of over 7 years in the field of micro-simulation of traffic networks and the resolution of problems related to road safety, at the Department of Civil Engineering of the University of Calabria, Italy. Unlike previous ones, it incorporates 21 car-following models (Giofrè et al., 2013), including Gipps and Wiedemann 74/99, and multiple calibration methods (Astarita et al., 2012b). Tritone was developed with different car-following models since each different model can lead to similar but slightly different results that turn out a different measure of effectiveness especially in the case of traffic surrogate safety measures. For this reason, Tritone leaves to the user the task to evaluate which car-following model is most appropriate to the case study.

It must be noted that many commercial traffic simulation models do not reproduce explicitly traffic safety measures and the safety evaluations must be carried out by extracting trajectories of single vehicles and post-elaborating them. A common tool used to perform this task is the SSAM software.

The SSAM software developed by FHWA in 2008 was created for the evaluation of surrogate safety measures. Through analysis of the trajectories of the simulated vehicles, it allows the evaluation of some safety indexes such as TTC, PET and potential collisions.

SSAM software practical applicability and results are investigated in this paper, in the three investigated scenarios, as opposed to a direct calculation of surrogate safety measures obtained using trajectories directly extracted from the micro-simulation models.

The first two listed simulators, Aimsun and VISSIM, both have one module that allows the extraction of the vehicular trajectories to be opened later with the SSAM software, while Tritone implements within itself the SSAM APIs, obtaining the results dynamically in an automatic process.

This article did not analyze other microsimulators, because currently only these three and Paramics (Cameron and Gordon, 1996), support the output for the analysis with SSAM.

Paramics has been extensively compared with VISSIM, in safety performance estimation, leading to similar results (Saleem et al., 2014, Essa and Sayed, 2016).

## 5. Data and preliminary results

In the three studied simulators, actual traffic demand and supply was modeled according to surveys. For the unsignalized intersection, 2470 veh/h were detected, for the signalized intersection 1457 veh/h and for the roundabout 2912 veh/h.

The geometries and the boundary conditions were modeled in order to reproduce the three scenarios faithfully. For each of these scenarios, 20 simulations were carried out. For the Aimsun and VISSIM microsimulators, the only basic car-following models (Gipps and Wiedemann 99) were used, as well as the related lane-changing and gap-acceptance models, while for Tritone 5 different models of car-following (Gipps, Wiedemann 99, Gazis and Herman, IDM 2000, Fritzsche) were used and replicated in different sets of 20 simulations. Table 1 shows a comparison between different models based on the average results of 20 simulations for the entire road network.

Table 1．Summary of simulations output．
| Micro simulator software（model） | Speed［km／h］ | Travel Time［s］ | Vehicles | Travel | Speed［km／h］ | Travel Time［s］ | Vehicles | Travel | Speed［km／h］ | Travel Time［s］ | Vehicles | Travel |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Aimsun（Gipps） | 38.3 | 125.1 | 2465 | 23.0 | 32.9 | 56.5 | 1441 | 9.7 | 33.6 | 183.4 | 2823 | 44.3 |
| Tritone（Gipps） | 41.4 | 111.2 | 2394 | 22.2 | 42.1 | 93.2 | 1424 | 9.8 | 24.1 | 157.0 | 2809 | 43.2 |
| VISSIM（Wiedemann 99） | 37.3 | 119.6 | 2466 | 16.2 | 11.8 | 67.1 | 1440 | 4.7 | 16.9 | 148.4 | 2655 | 32.8 |
| Tritone（Wiedemann 99） | 36.7 | 167.8 | 2266 | 18.2 | 37.9 | 77.4 | 1422 | 6.0 | 25.3 | 173.6 | 2827 | 31.6 |
| Tritone（Gazis and Herman） | 42.1 | 96.2 | 2391 | 16.6 | 38.9 | 85.6 | 1422 | 5.5 | 24.4 | 167.8 | 2836 | 41.0 |
| Tritone（IDM 2000） | 41.7 | 96.1 | 2380 | 16.3 | 38.3 | 80.9 | 1424 | 5.7 | 22.3 | 68.3 | 2844 | 21.7 |
| Tritone（Fritzsche） | 40.9 | 114.9 | 2371 | 18.9 | 38.3 | 82.3 | 1424 | 5.8 | 22.0 | 133.5 | 2823 | 30.5 |
|  | Unregulated intersection |  |  |  | Traffic light regulated intersection |  |  |  | Roundabout |  |  |  |


All models reach similar results of average speed on the network，average driving time of the single driver and of all drivers，as well as the number of vehicles that the network managed to dispose of during one hour of simulation．

For each model／software used，a calibration process was performed based on the number of vehicles leaving the sections in each scenario，in order to reduce the discrepancies with reality．Subsequently，the vehicle trajectories， obtained from each simulated scenario（20 different repetitions），were analyzed with the SSAM algorithm，in order to evaluate the surrogate safety measures．

It is possible to observe that the results are similar（for different microsimulation models）also with regard to traffic safety measures．On average，by evaluating the TTC indicator the SSAM analysis shows a greater danger in the scenario with the roundabout（TTC＝0．64 s）and lower danger in that with the non－signalized traffic light intersection $(\mathrm{TTC}=0.77 \mathrm{~s})$ and traffic light $(\mathrm{TTC}=0.80 \mathrm{~s})$ ．

Table 2．Percentage conflict．
| Micro simulator software（model） | Sero． | Ö「 $\stackrel{\text {（1）}}{\text { itempan }}$ | Daِّک0 50 | Sieron ${ }$ | Pagethed「 $\stackrel{\text {（1）}}{\text { itempan }}$ | Date 50 | ． $\sqrt{0}$ | ![](https://cdn.mathpix.com/cropped/bf4ae99f-f402-4ee6-8044-da21b1878da4-5.jpg?height=161&width=28&top_left_y=1507&top_left_x=1525)「000 | Unided 50 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Aimsun（Gipps） | 20.89 | 7.98 | 92.02 | 5.06 | 4.95 | 95.05 | 74.06 | 41.33 | 58.67 |
| Tritone（Gipps） | 19.05 | 34.44 | 65.56 | 17.16 | 2.17 | 97.83 | 63.79 | 42.11 | 57.89 |
| VISSIM（Wiedemann 99） | 9.74 | 18.46 | 81.54 | 2.91 | 13.48 | 86.52 | 87.35 | 13.47 | 86.53 |
| Tritone（Wiedemann 99） | 24.63 | 25.68 | 74.32 | 11.79 | 13.41 | 86.59 | 63.59 | 14.56 | 85.44 |
| Tritone（Gazis and Herman） | 11.56 | 52.24 | 47.76 | 26.39 | 9.46 | 90.54 | 62.05 | 29.96 | 70.04 |
| Tritone（IDM 2000） | 9.02 | 64.40 | 35.60 | 16.23 | 16.30 | 83.70 | 74.76 | 48.75 | 51.25 |
| Tritone（Fritzsche） | 15.76 | 34.45 | 65.55 | 10.08 | 15.74 | 84.26 | 74.16 | 18.64 | 81.36 |
|  | Unregulated intersection |  |  | Traffic light regulated intersection |  |  | Roundabout |  |  |


Preliminary results show similar results，in most cases，between the three different micro－simulation models． Analyzing in detail the trajectories of the single vehicles，through the SSAM algorithm，it is noted that even if the average values of the surrogate safety measures are comparable in the three scenarios，the frequencies with which they occur are not．In fact，observing Figure 2，it is possible to notice how all the models indicate that many more potential
conflicts/collisions occur in the roundabout, currently considered one of the safest intersections, than in the signal regulated and in the unregulated intersections.

In Table 2 analytical data of Figure 2 are shown with the detail of the percentage of these that are due to potential collisions/conflicts of the crossing/lane changing type (the vehicle under test is in conflict with another vehicle with an angle from 30 ° to 180 °) or rear end (the vehicle under test is in a conflict with leading vehicle at an angle from 0 ${ }^{\circ}$ to $30^{\circ}$ ).

These data show that most of the potential collisions/conflicts occur between the vehicle under examination and the vehicle that precedes it with a maximum angle of $30^{\circ}$. Slight differences can be noticed in the scenario of the roundabout, but this may be due to its geometric conformation and to a greater diversity of points of conflict.

This research confirms how different simulators and models reach very similar conclusions. In fact, it is noted that Aimsun and Vissim and Tritone all show how a signal regulated intersection is much safer than a roundabout and of course also safer than the unregulated intersection.

Results are specific to the simulated intersections with specific different traffic flows and so no general observations can be inferred. For this reason additional simulations where carried out with the same traffic flows on different intersection layouts.

![](https://cdn.mathpix.com/cropped/bf4ae99f-f402-4ee6-8044-da21b1878da4-6.jpg?height=397&width=1271&top_left_y=913&top_left_x=310)
Fig. 2. Percentage conflict in scenarios.

## 6. Additional results

From the considerations made on the results presented in the previous section, a second experiment was carried out. On the geometry of the real roundabout of the preceding sections three sub-cases have been studied (visible in Fig. 3). Based on the same geometric dimensions and the same vehicle flows present in the above described roundabout case two other scenarios have been created of a signalized and an unsignalized intersection.

![](https://cdn.mathpix.com/cropped/bf4ae99f-f402-4ee6-8044-da21b1878da4-6.jpg?height=478&width=1634&top_left_y=1725&top_left_x=129)
Fig. 3. Additional studied cases.

The result of these additional simulations is that all software and car-following models return similar values. These results are, however, different from the previous case studies. In fact, it is noted (Figure 4) that while the number of conflicts remains almost constant for the unsignalized intersection, for the case of the signalized intersection, instead, there is an increase, and a reduction for the roundabout.

![](https://cdn.mathpix.com/cropped/bf4ae99f-f402-4ee6-8044-da21b1878da4-7.jpg?height=413&width=1271&top_left_y=445&top_left_x=308)
Fig. 4. Percentage conflict in additional scenarios.

The main result of the previous simulations is, though, confirmed: the roundabout layout solution maintains a greater percentage of conflicts than the other two cases studied.

## 7. Conclusions

The purpose of this article is to evaluate the goodness of the results obtained by the simulators for the analysis of surrogate safety measures, in order to use these tools in research in the field of road safety. We have seen how different models return similar results and information that can classify a scenario as "potentially" at risk.

This research has shown that in an analysis of intersection planning it is possible to use the SSAM methodology to minimize the points of conflict and find better solutions. Micro-simulation models are able to evaluate numerically the safety level of every planning solution. In fact, by coupling microsimulation to SSAM, one has the opportunity to study, as in this article, different scenarios from the point of view of road safety, and quickly evaluate possible solutions. Naturally, in order to achieve a generic optimal solution, a good modeling and calibration phase of the network and its models is always necessary.

This paper shows that the numerical analysis conducted with different simulation models is reliable in confronting the same kind of intersection layouts.

## References

Astarita, V., Giofré, V.P., Guido, G., \& Vitale, A., 2012a. Calibration of a new microsimulation package for the evaluation of traffic safety performances. 15th meeting of the EURO Working Group on Transportation, Procedia-Social and Behavioral Sciences, 54, 1019-1026.
Astarita, V., Guido, G., Vitale, A., \& Giofré, V.P., 2012b. A new microsimulation model for the evaluation of traffic safety performances. European Transport, Paper № 1, ISSN 1825-3997, pp 1-16, 2012.
Astarita, V., Giofrè, V. P., Guido, G., Vitale, A., Festa, D., Vaiana, R., Iuele, T., Mongelli, D., Rogano, D. \& Gallelli, V., 2017. New features of Tritone for the evaluation of traffic safety performances. In Aiit International Congress on Transport Infrastructure and Systems (Tis 2017), Rome, Italy, 10-12 April, pp. 625-632.
Barceló, J., and Casas, J., 2002. "Dynamic Network Simulation with AIMSUN." International Symposium on Transport Simulation, Yokohama.
Cameron, G. D., \& Duncan, G. I., 1996. PARAMICS-Parallel microscopic simulation of road traffic. The Journal of Supercomputing, 10(1), 25-53.
Chen, Y., Persaud, B., \& Lyon, C., 2011. Effect of Speed on Roundabout Safety Performance: Implications for Use of Speed as Surrogate Measure (No. 11-2846).
Cooper, D. F., \& Ferguson, N., 1976. Traffic studies at T-Junctions. 2. A conflict simulation Record. Traffic Engineering \& Control, 17(Analytic).
Cunto, F., \& Saccomanno, F. F., 2008. Calibration and validation of simulated vehicle safety performance at signalized intersections. Accident analysis \& prevention, 40(3), 1171-1179.

Darzentas, J., Cooper, D. F., Storr, P. A., \& McDowell, M. R. C., 1980. Simulation of road traffic conflicts at T-junctions. Simulation, 34(5), 155-164.
Essa, M., \& Sayed, T., 2016. A comparison between PARAMICS and VISSIM in estimating automated field-measured traffic conflicts at signalized intersections. Journal of advanced transportation, 50(5), 897-917.
FHWA, 2008. Surrogate Safety Assessment Model and Validation: Final Report, FHWA-HRT-08-051, June 2008
Gettman, D., Pu, L., Sayed, T., \& Shelby, S. G., 2008. Surrogate safety assessment model and validation (No. FHWA-HRT-08-051), Federal Highway Administration, Washington, DC, USA.
Giofrè, V. P., Maciejewski, M., Merkisz-Guranowska, A., Piątkowski, B., \& Astarita, V., 2013. Real road network application of a new microsimulation tool: TRITONE. Archives of Transport, 01/2013, Vol. 27-28 n.3-4, pp 111-121.
Gipps, P. G., 1981. A behavioural car-following model for computer simulation. Transportation Research Part B: Methodological, 15(2), 105-111.
Gipps, P. G., 1986. Multsim: a model for simulating vehicular traffic on multi-lane arterial roads. Mathematics and Computers in Simulation, 28(4), 291-295.
Guido, G., Astarita, V., Giofré, V.P., \& Vitale, A., 2011. Safety performance measures: a comparison between microsimulation and observational data. Procedia-Social and Behavioral Sciences, 20, 217-225.
Hayward, J. C., 1972. Near miss determination through use of a scale of danger.
Horst, R. V. D., 1991. Time-to-collision as a cue for decision-making in braking. Vision in Vehicles--III.
Hourdakis, J., Michalopoulos, P., \& Kottommannil, J., 2003. Practical procedure for calibrating microscopic traffic simulation models. Transportation Research Record: Journal of the Transportation Research Board, (1852), 130-139.
Hydén, C., 1987. The development of a method for traffic safety evaluation: The Swedish Traffic Conflicts Technique. Bulletin Lund Institute of Technology, Department, (70).
Persaud, B., Retting, R., Garder, P., \& Lord, D., 2001. Safety effect of roundabout conversions in the united states: Empirical bayes observational before-after study. Transportation Research Record: Journal of the Transportation Research Board, (1751), 1-8.
Saleem, T., Persaud, B., Shalaby, A., \& Ariza, A., 2014. Can microsimulation be used to estimate intersection safety? Case studies using VISSIM and Paramics. Transportation Research Record: Journal of the Transportation Research Board, (2432), 142-148.
Sayed, T., Brown, G., \& Navin, F., 1994. Simulation of traffic conflicts at unsignalized intersections with TSC-Sim. Accident Analysis \& Prevention, 26(5), 593-607.
TSS-Transport_Simulation_Systems, 2002. "GETRAM/AIMSUN version 4.1 User's Manuals."
Wiedemann, R., 1974. Simulation des Straßenverkehrsflusses", Schriftenreihe des Instituts für Verkehrswesen der Universitä Karlsruhe, Heft 8.
Wiedemann, R., 1991. Modelling of RTI-Elements on multi-lane roads. In Drive Conference (1991: Brussels, Belgium) (Vol. 2).


[^0]:    * Corresponding author. Tel.: +39-0984-496780; fax: +0-000-000-0000 .
    E-mail address: vittorio.astarita@unical.it

