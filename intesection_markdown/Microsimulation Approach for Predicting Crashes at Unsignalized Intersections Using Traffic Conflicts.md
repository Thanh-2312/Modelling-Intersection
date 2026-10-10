# Microsimulation Approach for Predicting Crashes at Unsignalized Intersections Using Traffic Conflicts 

Ciro Caliendo ${ }^{1}$ and Maurizio Guida ${ }^{2}$


#### Abstract

A microsimulation approach is presented for assessing safety at unsignalized intersections using critical traffic conflicts computed in simulation models as a surrogate safety measure. The proposed approach was applied to a crash data set, collated over a 5-year monitoring period, corresponding to urban unsignalized intersections of the city of Salerno, Italy. Given that over 45\% of accidents recorded at these intersections occurred more especially in six 1-h time periods during the day and that these hourly periods corresponded to the peak traffic volumes, it was considered worthwhile to investigate each of these 1-h concentrated time intervals. Traffic flows were computed by using video cameras placed at each intersection and expressed as peak-hour volumes in the analysis. A process of microsimulation model calibration and validation was carried out, and a good level of conformity between the traffic simulated in the peak hours and the corresponding one measured in the field was obtained. Subsequently, a form of software, which is compatible with the applied microsimulation software, was used for identifying the number of critical conflicts at the intersections investigated. For this aim, a collision was assumed to be very probable when conflicts are characterized by a time to collision (TTC) and post-encroachment time (PET) below the threshold values of 1.5 and 5 s, respectively. The relationship between critical conflicts computed in microsimulation models and actual crashes was found to be statistically significant. A crash-prediction regression model was then developed for the investigated intersections, which allows predicting crashes in the field on the basis of the critical conflicts computed in simulation. The proposed model was found to fit the accident data slightly better than the traffic volume-based regression model. DOI: 10.1061/(ASCE)TE.1943-5436.0000473. © 2012 American Society of Civil Engineers.


CE Database subject headings: Simulation; Intersections; Traffic signals; Traffic safety; Predictions.
Author keywords: Microsimulation; Unsignalized intersections; Traffic; Crashes; Critical conflicts; Surrogate safety measures.

## Introduction

Traffic simulation models have been used mainly as a method for studying transport-planning and traffic-engineering situations. More recently there has been a growing interest in developing traffic simulation models for investigating the impact of traffic on both air pollution and road safety. Currently, although some existing microsimulation forms of software also allow an evaluation of vehicle emissions, safety assessment still continues to be a prevalent question. The lack of direct measures for evaluating safety has hitherto been considered to be a shortcoming of the microsimulation approach.

Road safety analyses have traditionally been carried out by statistical models on the basis of the number and the localization of accidents. Over the years, however, numerous problems associated with accident data have been discussed, and the topics that follow have been considered especially relevant: (1) accidents are rare events, which may cause serious difficulties in safety analyses owing to the fact that an insufficient number of accidents might be available for analysis; (2) not all accidents are reported, thus making it difficult to understand the seriousness of the accident and

[^0]types of road users involved when accident reports are incomplete; (3) a long observation time is required for ensuring an adequate sample of crash data for estimating statistical models; (4) information on the user's behavior (acceleration, deceleration, braking, and steering) before an accident occurs is often not available (unless a naturalistic approach is used on the basis of instrumented vehicles that allows viewing the preaccident driver behavior); (5) safety analyses are conducted from a reactive viewpoint, being based on actual crashes that have already taken place (unless new methods and/or technologies, e.g., ITS, are used that allow the conducting of safety analysis from a proactive viewpoint not based on historical accident data).

Nowadays there is a need to develop safety indicators that could allow a preventive safety analysis without having to wait for a crash to occur and that would give the following advantages: (1) evaluating road safety more efficiently and more quickly; (2) having a better understanding of the relationships between the user's behavior and crash risk and gaining knowledge about the influence of the design elements; (3) characterizing more clearly the process of crash risk in both normal and/or peak-hour traffic conditions. In this respect, the use of surrogate safety measures, which are not based on the observation of actual crashes but on crash likelihood, is proving to be ever more interesting. The aim of singling out appropriate surrogate safety measures is expected to be achieved, among other ways, also by means of the microsimulation approach.

The literature features several surrogate safety measures, with certain ones being generally compatible with microsimulation possibilities. In microsimulation, one of the most common surrogate safety measures is known as a conflict. The term conflict is generally defined as an observed situation in which two or more road users approach each other on a collision course, and where an
accident is imminent if neither of them takes evasive action (Amundsen and Hyden 1977). Conflict analysis assumes that traffic conflicts can be a close representation of actual accidents, so that by observing the former, one may predict the latter with less time and effort (Paddock 1974). Several safety indicators for identifying conflicts exist in the literature. Traditionally, the most widely used safety indicators are the following: time to collision, post-encroachment time, time gap, time headway, and initial deceleration rate. According to the classical definition made by Hayward (1971), time to collision (TTC) is defined as the expected time for two vehicles to collide if they remain at their present speed and on the same trajectory. Post-encroachment time (PET) is usually defined as the time between when the first vehicle last occupied a position and the time when the second vehicle subsequently arrived at the same position (Hallen et al. 1978). The time gap is conventionally described as the time interval between the passing of one vehicle and the arrival of the next vehicle; technically it is measured from the back bumper of the front vehicle to the front bumper of the next vehicle [Federal Highway Administration (FHWA 1976)]. Time headway (H) is generally defined as the time elapsing between the front of the lead vehicle passing a point on the roadway and the front of the following vehicle passing the same point (Evans 1991); it differs from the gap because it is measured from the front bumper of the front vehicle to the front bumper of the next vehicle. Because deceleration is considered as the action taken by the subject vehicle to avoid the collision, the initial deceleration rate (DR) may also be an indicator of a potential conflict (Cooper and Ferguson 1976; Darzentas et al. 1980).

By using microsimulation, researchers have hitherto focused above all on the potentiality of different safety indicators for defining conflicts, which, however, is still a subject of controversy. In addition, only few research projects have compared simulated conflicts with real accidents. Conflicts attributable to vehicle trajectories have a strong impact on frequency and the severity of real accidents, especially at road intersections where numerous turning maneuvers and different collision angles take place. Previous research has paid little attention to urban areas and in particular to unsignalized intersections (Sayed et al. 1994). Moreover, these studies have been carried out prevalently in countries in which traffic characteristics, driver behavior, and geometry of intersections differ from those in Italy. In this respect, it is to be noted that according to the Italian National Institute of Statistics over 70\% of reported road crashes in Italy take place in urban areas, and over 50\% of these accidents occur at intersections. Among types of intersection, unsignalized urban intersections are recognized to be more dangerous for both property-damage-only accidents and injury accidents than signalized intersections (Elvik and Vaa 2004).

As a result of the considerations made above, there are at least four main reasons for justifying this paper. The first is motivated by the need to test the potentiality of microsimulation for assessing safety at urban unsignalized intersections by using conflicts as a surrogate safety measure. In fact, there is an a priori reason for believing that a higher number of conflicts may indicate a greater number of crashes. The second reason, given that several parameters exist for identifying conflicts, is for suggesting certain indicators and their threshold values that appear to be more appropriate for a safety analysis at unsignalized intersections. A third reason, given that the results of microsimulation can help a road designer and/or traffic operator to make preventive decisions on safety, is for strongly recommending the use of this tool. Finally, given that accidents are rare events and therefore with a random variation in a small number, researchers need alternative approaches as the simulation tool for evaluating safety at sites for which an insufficient number of crashes has been observed.

This then, is the context wherein the present work is set. The paper sets out to study traffic conflicts and crash data occurring in Italy at unsignalized urban intersections. The objective is to identify a relationship between the simulated conflicts and recorded crashes and to test whether crashes at unsignalized intersections correlate better with conflicts than with traffic flow. The tool used for this analysis is based on the microsimulation approach. For this purpose, a monitoring period regarding crashes occurring at unsignalized urban intersections of the city of Salerno, Italy was considered. Given that the accident reports showed that the number of crashes was greater when the peak hours of traffic occurred, traffic flow in terms of peak hourly volume at the time of crashes was chosen in the paper to be more appropriate than average daily traffic amounts for explaining crashes. Digital video cameras placed at the intersections were used for computing the values of peak hourly volumes. The AIMSUN (2010) traffic simulation software was used to model traffic flow during peak hours at the preselected unsignalized intersections. A calibration process of the parameters of microsimulation model was made to reproduce traffic conditions accurately. Subsequently, another software named the Surrogate Safety Assessment Model (SSAM), which is compatible with AIMSUN, was used (Gettman et al. 2008) for calculating and classifying conflicts. Safety indicators for identifying conflicts, such as TTC and PET, were more used, and two different threshold values were applied, respectively, to TTC and PET that were chosen for defining when vehicle-vehicle interactions had to be classified as critical conflicts. A collision became very probable when TTC and PET were below these values. A statistical analysis was then performed to assess the relationship between the number of critical conflicts and actual crashes. A statistical correlation between actual crashes and peak hourly traffic volumes was also examined. Finally, a prediction model that allows estimating crashes in the field on the basis of critical conflicts computed in simulation was proposed.

In light of the previous considerations, the present paper is organized as follows: "Literature Review" concerns the safety indicators that have been more frequently used in a microsimulation approach; "Microsimulation Modeling" deals with the calibration process developed for implementing AIMSUN software; "Critical Conflicts" discusses how the results of traffic microsimulation are used for exporting vehicle trajectories and consequently by the SSAM software for computing critical conflicts; "Statistical Analysis" presents analysis of critical conflicts and correlations with recorded crashes and between these latter ones and peak hourly traffic volumes. Finally, the conclusions and directions for future research are reported.

## Literature Review

As far as the writers are aware, the idea of using the potential of microsimulation modeling for road safety assessment appears to be attributable initially to Archer (2000). Despite progress in modeling techniques and increased computer power, some problems are discussed in that paper and the lessons learned are presented. The author recommended caution in using microsimulation and stated that the key to the success of this tool for assessing safety lies in the ability to model road user behavior at a sufficiently detailed level. Archer also considers that the safety indicators, which can be used for comparing the real situations and corresponding representations in simulation, are useful for safety purposes.

Minderhould and Bovy (2001) introduced two new safety indicators that are based on extensions of the time to collision (TTC). In contrast to the classical TTC safety indicator, these
extensions take into account the full course of vehicles over space and time. These two new indicators are named time exposed time to collision (TET) and time integrated time to collision (TIT), respectively. The TET indicator expresses the exposure time to safety-critical situations, whereas the TIT takes into account the TTC values encountered during these safety-critical approaches. According to Minderhould and Bovy these two new indicators can be used in microscopic simulation studies for assessing impacts on safety attributable to driver support systems, such as autonomous intelligent cruise control.

Vogel (2003) compared two classical indicators, namely headway (H) and time to collision (TTC) with respect to their usefulness in determining the safety of different traffic situations at junctions. It was found that H and TTC are independent of each other for following vehicles. Although a short headway can also be interpreted as a potential danger, which is attributable to the fact that only vehicles travelling with short H values have the possibility of producing small TTC values that represent actual danger, these two indicators are recognized to be suitable for different purposes because they provide different information. In that paper it was recommended that the authorities use headway as a criterion to check whether a vehicle drives too closely behind another vehicle, whereas TTC should be used for evaluating safety as it is more appropriate for indicating the occurrence of dangerous situations.

Barcelo et al. (2003) using AIMSUN software, presented a safety indicator named un-safety parameter for determining the level of un-safety in the relationship between consecutive vehicles. This parameter is expressed as a function of the speed of the follower vehicle, the speed difference between two vehicles at the time of collision, the ratio between the deceleration of the leader vehicle, and its maximum deceleration capacity. The value of this un-safety parameter is zero when the hypothetical crash does not occur or the leader vehicle is not braking. This safety indicator appears to be limited to the linear collision probability (rear-end crashes) so that it does not give information on crossing conflicts as at intersections.

Gettman and Head (2003) investigated the potential for deriving surrogate measures of safety from existing traffic simulation models. In their work, the safety indicators that are considered to be the best are time to collision, post-encroachment time, deceleration rate, maximum speed, and speed differential. The results of this report showed that the review of the existing simulation models did not indicate a clear superiority of any particular model for predicting surrogate measures. However, even if surrogate measures of safety from simulation approach were considered to be promising for the use in the evaluation of safety at intersections, Gettman and Head recommended caution because the driver behavior assumed in the simulation models could limit their applicability.

Kiefer et al. (2005) use the inverse time to collision term, defined as the difference in speed between the lead and following vehicles divided by the range between these two vehicles. They assume that the driver deceleration response in response to a crash alert, in a car safety technology that assists drivers in avoiding rearend crashes, is based on an inverse TTC threshold that decreases linearly with driver speed.

Cunto and Saccomanno (2008) argue that the deceleration rate for avoiding the crash (DRAC) does not take into consideration the vehicle's braking capability over time for the prevailing road and traffic conditions. It is expected, for example, that a given value of DRAC when subject to wet pavement conditions is more critical than the same value under dry conditions because the pavement friction coefficient is reduced. In this respect Cunto and Saccomanno introduce a crash potential index (CPI) as a safety measure that expresses the probability that the DRAC of a vehicle is higher than its braking capacity or maximum available deceleration rate (MADR). The procedure suggested in the paper, which is based on the above-mentioned CPI parameter, has been used for estimating safety performance regarding rear-end crashes at signalized intersections.

Gettman et al. (2008) made another important step forward in showing the potentials of surrogate safety measures at intersections. Their report contains the findings of the development of software for deriving surrogate measures from data output through traffic simulation models. This software is known as the Surrogate Safety Assessment Model (SSAM). The surrogate measures developed are on the basis of the identification, classification, and evaluation of traffic conflicts. For identifying these conflicts TTC and PET are prevalently used. A vehicle trajectory data format has also been designed, and this format is added as an output option by some traffic simulation models. Finally, statistical validation tests are performed to compare the processed conflict results with the crash records or to contrast simulated design alternatives. In this report it was found that a wide range in the total number of conflicts can be obtained from applying existing simulation models that are compatible with SSAM. In general, intersections modeled in certain commercially available simulation software exhibited the lowest or the highest number of conflicts, whereas other simulation software showed a number of conflicts contained between these extremes. However, all simulation models produced some inaccuracies that led SSAM to identify conflicts also when the TTC was to be zero. Given that in none of the microsimulation models can there be crashes because the vehicles avoid each other during the simulation process, the events in SSAM with TTC = 0 have to be excluded from the traffic conflicts analysis.

Archer and Young (2010) used a microsimulation approach to investigate the traffic safety of five alternative signal treatments at a metropolitan highway intersection. Archer and Young noted that further work was required to improve the use of simulation models in replicating accidents. However, their work is relevant for the purposes of this paper and, above all, for their using the GEH statistic in the calibration process of microsimulation model.

Yang et al. (2010), in contrast, proposed a safety indicator that is a modified version of TTC for rear-end crashes. This new timebased indicator named modified time to collision (MTTC), in contrast with the classical TTC, which is on the basis of the assumption that the consecutive vehicles maintain constant speeds until the collision occurs so that only if the speed of the following vehicle is greater than that of the leading vehicle will a longitudinal collision result, takes any acceleration difference into account between the following and the leading vehicle. The performance of MTTC is tested by making a comparison between simulation results and real accident records on two real highway sections. According to the Yang et al. it appears difficult for the MTTC to identify potential conflicts when traffic volume is low.

In their study, Pirdavani et al. (2010) chose one of the most common safety indicators such as PET for evaluating the safety situation of unsignalized intersections. This indicator is used for evaluating situations in which two road users that are on a collision course pass over a common spatial point with a time difference that is below a predetermined threshold. They found that PET is useful for evaluating the safety level of unsignalized intersections under different traffic volume and speed limits. According to Pirdavani et al. because the use of the PET is only for investigating transverse collisions, other safety indicators such as TTC and/or its derived subindicators are also necessary for analyzing other types of collisions, such as rear-end and converging collisions.

Dijkstra et al. (2010) investigated the relationships between the detected conflicts at junctions using a microsimulation model and the crashes recorded at the same locations. By using the bestknown safety indicator, TTC, they found a quantitative relationship between the number of calculated conflicts at priority junctions and the number of crashes observed.

Laureshyn et al. (2010) discuss safety indicators proposed in the literature for reflecting two aspects of a collision, namely collision risk and collision consequences. According to Laureshyn et al. the existing indicators on the basis of time, such as TTC, time gap, and time advantage, all of which may be seen as an extension of PET, appeared to be inadequate for describing collision severity. To achieve this aim, these indicators need to be completed with a set of supplementary indicators such as the speed of both the leading vehicle and the following vehicle and the time of the latter vehicle in arriving at the potential collision point.

Bachmann et al. (2011) also provided a revised definition of TTC for simulating traffic conflicts. The calculation of the revised TTC in contrast with the classical definition involves the distance between the vehicles and speed of both vehicles. According to Bachmann et al. the revised definition is for identifying conflict lines so that it is suitable for freeway studies, where, attributable to lane changing and/or merging maneuvers, conflict lines are expected. By using this revised definition of TTC, Bachmann et al. found that on the adding of a separate lane for trucks, the conflicts related to trucks diminished in number, whereas the number of lane-change conflicts of passenger cars increased attributable to their increased freedom for maneuver.

Guido et al. (2011) investigated five safety performance measures as maximum deceleration rate to avoid a crash (DRAC), time to collision (TTC), proportion of stopping distance (PSD), time integrated time to collision (TIT), and crash potential index (CPI). This paper describes a comparison of the aforementioned safety performance measures that had been obtained experimentally from videotaped vehicle tracking data. Differences in safety performance are discussed, and it is shown that safety performance is highly sensitive to the way it is measured.

The previously cited literature review proves that studies have concentrated more especially on investigating and proposing different safety indicators for defining conflicts, which actually is still a subject of discussion. The present paper, in contrast, based on two safety indicators that have been successfully applied for many years (TTC and PET), uses a microsimulation approach for focusing on the quantitative relationships between conflicts at urban unsignalized intersections and observed crashes. The work also relates crashes to traffic expressed in terms of peak-hour volume at the time of the crashes; as a consequence an investigation is also made to show whether crashes can be explained better by conflicts or by traffic, and a prediction model is also proposed. "Data Description" describes the data set used and the procedure of preparing it for microsimulation analysis.

## Data Description

A 5-year monitoring period extending from 2003 to 2007 was evaluated at the urban unsignalized intersections of the city of Salerno. During this period, crash data, which were extracted from the official reports of the urban police, were collated. For each accident, a variety of details was recorded, including date, hour, and location of accident type and accident severity; number of vehicles and persons involved; and a short description of the accident dynamics.

The number of total accidents (including both property-damageonly accidents and injury and fatal accidents) was considered in conflict analysis. This was attributable to the fact that too few injury and fatal accidents were available for making an analysis only on the basis of the severity of crashes. Additionally, it is also to be said that if there were a sufficient number of serious accidents it would not be possible to take into account the severity of the crashes in conflict analysis. Traffic conflicts are a close representation of actual accidents and are generally identified by safety indicators that in this paper are classical TTC and PET. Lower TTC and PET certainly indicate a higher probability of accidents, but they cannot yet be linked directly to the severity of the resulting accidents because the speed values of vehicles and the speed difference between conflicting vehicles have not yet been considered in these safety indicators.

Among the unsignalized intersections investigated, only those with a total number of crashes greater than 10 in the 5-year monitoring period were preselected for subsequent analysis. In this respect, it is to be mentioned that an intersection is a specific place where in general a high concentration of accidents is observed, so that it is often defined as a black spot. Nevertheless, no universally accepted definition of black spot is given in the literature. This paper assumes a black spot is an intersection in which more than 10 total accidents with at least five injury and fatal accidents have been reported to the police during the 5-year monitoring period (i.e., intersections in which the frequency of total accidents is greater than 2 per year and with at least one injury and fatal accident per year). Intersections in which accidents were below the aforementioned thresholds or having zero observed accidents were not considered in the analysis. The number of the unsignalized intersections having the previously quoted frequency of accidents was found to be nine.

The geometry of these intersections, priority of maneuvers, and speed limits were obtained by observation during site visits. Seven of the nine intersections were of the T-type, whereas the remaining two were of the four-arm type as reported in Table 1. All intersections had a major and a minor road. Each road consisted of two, three, or four lanes, with an average width of 3.75 m and a negligible longitudinal grade. The number of lanes contained in Table 1 refers to road sections entering the intersection and involves both directions. The average width of lanes corresponds to the normal width of such roads in Italy, and the capacity of a single lane was assumed to be 800 vehicles/h. The ratio between the peak hourly volume per lane and the capacity per lane is contained in the ranges 0.2-1.2 on major roads and 0.1-0.6 on minor roads. The imposed speed limit is 50 km/h.

Some 219 accidents were reported at the nine aforementioned unsignalized intersections, 138 of which were severe crashes (i.e., including injuries and fatal crashes). In total, 420 motor vehicles were involved (cars, heavy vehicles, and two wheelers) in the 219 crashes. The database does not include pedestrian, bicycle, and bus accidents because these were found to be too few to be worth considering in the analysis. Table 1 gives accident count data observed during the 5-year monitoring period for each of the unsignalized intersections investigated (labeled from 1 to 9).

A more detailed analysis of the accident reports showed that the crashes occurred at specific periods during the day. In particular, a great number of accidents was found to have occurred at three 2-h time periods during the day. These time periods were between 7:00 a.m. and 9:00 a.m., between 12:00 a.m. and 2:00 p.m., and finally between 6:00 p.m. and 8:00 p.m. The corresponding total number of accidents was found to be 100 total crashes (i.e., over 45\% of the total number of accidents at the nine intersections investigated). The reason for this was attributed to higher traffic volumes than those at other hours of the day. As a direct consequence,

Table 1. Accident Count Data Observed during the 5-Year Monitoring Period
| Unsignalized intersection | Type of intersection | Major road Number of lanes | Minor road Number of lanes | Number of total accidents (5 years) | Number of motor vehicles involved | Injury and fatal accidents |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Four arm | 3 | 3 | 94 | 171 | 58 |
| 2 | Three arm | 3 | 3 | 16 | 37 | 11 |
| 3 | Four arm | 3 | 3 | 14 | 26 | 12 |
| 4 | Three arm | 3 | 2 | 21 | 40 | 10 |
| 5 | Three arm | 2 | 2 | 15 | 30 | 5 |
| 6 | Three arm | 4 | 2 | 17 | 35 | 15 |
| 7 | Three arm | 4 | 4 | 14 | 22 | 6 |
| 8 | Three arm | 4 | 4 | 14 | 31 | 11 |
| 9 | Three arm | 3 | 2 | 14 | 28 | 10 |
| Total |  |  |  | 219 | 420 | 138 |


this result was considered to be worthy of special investigation in the present paper. Because only total accidents are investigated in this study, it is not surprising that these crashes increase with an increase in traffic volume so that more total accidents are observed during peak hours attributable essentially to higher traffic volumes. The reason for this is the increasing level of exposure attributable to a rise in the amount of traffic conflicts compared with those of lower traffic volumes. However, it is also to be stated that when traffic volume increases, a reduction in speeds is expected (vehicles can move more slowly) and as a consequence less severe accidents might occur (in contrast with lower traffic volumes vehicles that can move freely with higher speeds and a greater severity of accidents might be expected). Unfortunately, as has been mentioned before, it does not yet appear that the aspect of severity of accidents can be investigated by the traditional safety indicators (TTC and PET) that are, however, still the most widely used.

Because official reports on accidents did not contain information regarding traffic volumes, measurements of traffic in the field were made. Traffic flows were computed by using video cameras placed at each intersection. The video camera was placed on a tripod at a suitable vantage point near each intersection to record turning movements (right turn, left turn, and straight on). Data were recorded for 15 min during all three aforementioned 2-h time periods, thus corresponding to hours in which a higher number of crashes was observed during the day at these intersections. The videotape was played in the laboratory several times to record the entering and turning traffic volume count and to divide the traffic volume into three vehicle categories: cars, heavy vehicles, and two-wheelers. However, to shorten the length of the paper, only the traffic in terms of hourly volume (sum of traffic measured at four 15-min intervals) at the nine intersections and at the time of crashes (6 h mentioned previously) has been reported. Table 2 gives, for each unsignalized intersection, accident count data observed in the previously mentioned six 1-h time periods during the day and the corresponding peak hourly traffic volume expressed in terms of total volume entering each intersection $\mathrm{VHP}_{e, i}(i=1, \ldots, 9)$.

Total traffic entering each intersection was observed to vary from 1,122 to 3,188 vehicles per hour during videotaping. The turning traffic volumes (right turn, left turn, and straight on) and the composition of the traffic (cars, heavy vehicles, two-wheelers) entering each of the nine intersections in the previously mentioned peak hours are given in Tables 3 and 4, respectively.

Table 2. Accident Count in Peak Hours and Corresponding Total Traffic Entering Each Intersection Expressed as Peak Hourly Volume $\left(\mathrm{VHP}_{e, i}\right)$
| Unsignalized intersection | Accident count data and $\mathrm{VHP}_{e, i}$ for each intersection | Time |  |  |  |  |  | Total number of accidents |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 7:00-8:00 a.m. | 8:00-9:00 a.m. | 12:00 a.m.1:00 p.m. | 1:00-2:00 p.m. | 6:00-7:00 p.m. | 7:00-8:00 p.m. |  |
| 1 | No. of accidents | 0 | 7 | 19 | 11 | 3 | 3 | 43 |
|  | $\mathrm{VHP}_{e, 1}$ (vehicles/h) | 1,902 | 2,688 | 2,660 | 2,692 | 2,164 | 2,158 |  |
| 2 | No. of accidents | 1 | 0 | 3 | 1 | 1 | 0 | 6 |
|  | $\mathrm{VHP}_{e, 2}$ (vehicles/h) | 1,515 | 2,285 | 2,346 | 2,408 | 2,050 | 1,940 |  |
| 3 | No. of accidents | 0 | 1 | 3 | 1 | 1 | 1 | 7 |
|  | $\mathrm{VHP}_{e, 3}$ (vehicles/h) | 1,122 | 1,786 | 1,722 | 1,720 | 1,664 | 1,800 |  |
| 4 | No. of accidents | 0 | 0 | 0 | 2 | 3 | 2 | 7 |
|  | $\mathrm{VHP}_{e, 4}$ (vehicles/h) | 2,859 | 3,188 | 2,617 | 3,075 | 3,079 | 2,909 |  |
| 5 | No. of accidents | 1 | 1 | 2 | 0 | 0 | 1 | 5 |
|  | $\mathrm{VHP}_{e, 5}$ (vehicles/h) | 2,458 | 2,714 | 2,048 | 2,075 | 2,431 | 2,073 |  |
| 6 | No. of accidents | 0 | 1 | 2 | 0 | 3 | 3 | 9 |
|  | $\mathrm{VHP}_{e, 6}$ (vehicles/h) | 1,696 | 2,381 | 1,704 | 1,451 | 1,821 | 1,651 |  |
| 7 | No. of accidents | 0 | 0 | 0 | 3 | 2 | 1 | 6 |
|  | $\mathrm{VHP}_{e, 7}$ (vehicles/h) | 1,617 | 2,300 | 1,656 | 1,376 | 1,759 | 1,566 |  |
| 8 | No. of accidents | 1 | 3 | 1 | 1 | 0 | 1 | 7 |
|  | $\mathrm{VHP}_{e, 8}$ (vehicles/h) | 1,661 | 2,343 | 1,888 | 1,734 | 2,003 | 1,739 |  |
| 9 | No. of accidents | 0 | 4 | 0 | 3 | 2 | 1 | 10 |
|  | $\mathrm{VHP}_{e, 9}$ (vehicles/h) | 1,310 | 2,358 | 1,998 | 2,085 | 2,046 | 1,940 |  |
|  | Total number of accidents in 5 years |  |  |  |  |  |  | 100 |


Table 3. Volume of Turning Traffic at Each Intersection during Peak Hours
| Unsignalized intersection | Turning traffic volume | Time |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 7:008:00 a.m. | 8:009:00 a.m. | 12:00 a.m.1:00 p.m. | 1:002:00 p.m. | 6:007:00 p.m. | 7:008:00 p.m. |
| 1 <br> 2 | Right turn (vehicles/h) | 575 | 694 | 604 | 694 | 551 | 543 |
|  | Left turn (vehicles/h) | 55 | 108 | 152 | 164 | 95 | 121 |
|  | Straight on (vehicles/h) | 1,272 | 1,886 | 1,904 | 1,834 | 1,518 | 1,494 |
|  | Total traffic $\mathrm{VHP}_{e, 1}$ (vehicles/h) | 1,902 | 2,688 | 2,660 | 2,692 | 2,164 | 2,158 |
|  | Right turn (vehicles/h) | - | - | - | - | - | - |
|  | Left turn (vehicles/h) | 273 | 444 | 576 | 612 | 518 | 551 |
|  | Straight on (vehicles/h) | 1,242 | 1,841 | 1,770 | 1,796 | 1,532 | 1,389 |
|  | Total traffic $\mathrm{VHP}_{e, 2}$ (vehicles/h) | 1,515 | 2,285 | 2,346 | 2,408 | 2,050 | 1,940 |
| 3 | Right turn (vehicles/h) | 123 | 309 | 245 | 195 | 245 | 293 |
|  | Left turn (vehicles/h) | 62 | 93 | 103 | 97 | 76 | 97 |
|  | Straight on (vehicles/h) | 937 | 1,384 | 1,374 | 1,428 | 1,343 | 1,410 |
|  | Total traffic $\mathrm{VHP}_{e, 3}$ (vehicles/h) | 1,122 | 1,786 | 1,722 | 1,720 | 1,664 | 1,800 |
| 4 | Right turn (vehicles/h) | 393 | 471 | 604 | 996 | 661 | 839 |
|  | Left turn (vehicles/h) | 96 | 98 | 65 | 103 | 92 | 85 |
|  | Straight on (vehicles/h) | 2,370 | 2,619 | 1,948 | 1,976 | 2,326 | 1,985 |
|  | Total traffic $\mathrm{VHP}_{e, 4}$ (vehicles/h) | 2,859 | 3,188 | 2,617 | 3,075 | 3,079 | 2,909 |
| 5 | Right turn (vehicles/h) | 52 | 60 | 66 | 44 | 58 | 45 |
|  | Left turn (vehicles/h) | 1,036 | 1,199 | 1,314 | 884 | 1,165 | 894 |
|  | Straight on (vehicles/h) | 1,370 | 1,455 | 668 | 1,147 | 1,208 | 1,134 |
|  | Total traffic $\mathrm{VHP}_{e, 5}$ (vehicles/h) | 2,458 | 2,714 | 2,048 | 2,075 | 2,431 | 2,073 |
| 6 | Right turn (vehicles/h) | 9 | 18 | 40 | 37 | 42 | 49 |
|  | Left turn (vehicles/h) | 125 | 164 | 122 | 137 | 144 | 180 |
|  | Straight on (vehicles/h) | 1,562 | 2,199 | 1,542 | 1,277 | 1,635 | 1,422 |
|  | Total traffic $\mathrm{VHP}_{e, 6}$ (vehicles/h) | 1,696 | 2,381 | 1,704 | 1,451 | 1,821 | 1,651 |
| 7 | Right turn (vehicles/h) | 47 | 105 | 169 | 118 | 78 | 127 |
|  | Left turn (vehicles/h) | 205 | 215 | 88 | 59 | 208 | 215 |
|  | Straight on (vehicles/h) | 1,365 | 1,980 | 1,399 | 1,199 | 1,473 | 1,224 |
|  | Total traffic $\mathrm{VHP}_{e, 7}$ (vehicles/h) | 1,617 | 2,300 | 1,656 | 1,376 | 1,759 | 1,566 |
| 8 | Right turn (vehicles/h) | 142 | 251 | 308 | 271 | 367 | 320 |
|  | Left turn (vehicles/h) | 440 | 581 | 662 | 706 | 570 | 515 |
|  | Straight on (vehicles/h) | 1,079 | 1,511 | 918 | 757 | 1,066 | 904 |
|  | Total traffic $\mathrm{VHP}_{e, 8}$ (vehicles/h) | 1,661 | 2,343 | 1,888 | 1,734 | 2,003 | 1,739 |
| 9 | Right turn (vehicles/h) | 31 | 56 | 36 | 37 | 38 | 50 |
|  | Left turn (vehicles/h) | 144 | 295 | 226 | 256 | 249 | 272 |
|  | Straight on (vehicles/h) | 1,135 | 2,007 | 1,736 | 1,792 | 1,759 | 1,618 |
|  | Total traffic $\mathrm{VHP}_{e, 9}$ (vehicles/h) | 1,310 | 2,358 | 1,998 | 2,085 | 2,046 | 1,940 |


The straight-on maneuvers were observed to be prevalent compared with those of right and left turn maneuvers, and the number of cars was recorded to be much higher than that of heavy vehicles and motorcycles by processing the videos.

## Microsimulation Modeling

## Assumptions

In keeping with the literature, none of the existing simulation models is clearly superior to any other as a specific model for predicting surrogate safety measures. In the group of simulation software, which are compatible with SSAM, there also features AIMSUN, which was found to exhibit average values of the total number of conflicts at intersections compared with other software (Gettman et al. 2008). In light of these considerations and because the objective of this paper is not to compare the capabilities of several forms of simulation software in predicting conflicts but to make a contribution for a more consolidated verification of the potentiality of a microsimulation approach in assessing safety at intersections using conflicts as a surrogate safety measure, it appeared reasonable to use the microsimulation software AIMSUN. Because microsimulation software is constantly evolving, the upgraded version of the AIMSUN (Version 6.1.2) that was commercially available at the time of developing this research was used.

The decision was made to keep the AIMSUN default values of driver behavior to avoid the risk of generating unrealistic maneuvers in simulation. This decision also allows comparing AIMSUN with other software with default values of the driver's behavior in future studies.

Because AIMSUN and other software may produce some inaccuracies that lead SSAM to identify conflicts also when TTC is zero (Gettman et al. 2008), it was decided to exclude from the computing of conflicts those events in SSAM characterized by TTC = 0. Furthermore, events with $\mathrm{PET}=0$ were also excluded from the conflict analysis.

## Performing Process

The main steps in the process of activating the AIMSUN microsimulation software were, more specifically (1) identifying the intersection geometry; (2) defining the driver's behavior; and (3) assigning traffic and turning movements. A graphic interface, which is contained in AIMSUN, was used for importing the geometric background of the intersection and showing it on the computer screen. This graphic interface is compatible with the

Table 4. Traffic Composition at Each Intersection during Peak Hours
| Unsignalized intersection | Traffic composition | Time |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 7:008:00 a.m. | 8:009:00 a.m. | 12:00 a.m.1:00 p.m. | 1:002:00 p.m. | 6:007:00 p.m. | 7:008:00 p.m. |
| 1 <br> 2 | Cars (vehicles/h) | 1,438 | 1,848 | 1,560 | 1,552 | 1,476 | 1,484 |
|  | Heavy vehicles (vehicles/h) | 183 | 180 | 114 | 142 | 99 | 62 |
|  | Two-wheelers (vehicles/h) | 281 | 660 | 986 | 998 | 589 | 612 |
|  | Total traffic $\mathrm{VHP}_{e, 1}$ (vehicles/h) | 1,902 | 2,688 | 2,660 | 2,692 | 2,164 | 2,158 |
|  | Cars (vehicles/h) | 1,237 | 1,746 | 1,495 | 1,505 | 1,382 | 1,260 |
|  | Heavy vehicles (vehicles/h) | 104 | 102 | 104 | 100 | 62 | 49 |
|  | Two-wheelers (vehicles/h) | 174 | 437 | 747 | 803 | 606 | 631 |
|  | Total traffic $\mathrm{VHP}_{e, 2}($ vehicles $/ \mathrm{h})$ | 1,515 | 2,285 | 2,346 | 2,408 | 2,050 | 1,940 |
| 3 | Cars (vehicles/h) | 875 | 1,275 | 1,076 | 1,111 | 1,079 | 1,191 |
|  | Heavy vehicles (vehicles/h) | 105 | 112 | 84 | 103 | 68 | 44 |
|  | Two-wheelers (vehicles/h) | 142 | 399 | 562 | 506 | 517 | 565 |
|  | Total traffic $\mathrm{VHP}_{e, 3}$ (vehicles/h) | 1,122 | 1,786 | 1,722 | 1,720 | 1,664 | 1,800 |
| 4 | Cars (vehicles/h) | 2,442 | 2,666 | 2,116 | 2,500 | 2,784 | 2,635 |
|  | Heavy vehicles (vehicles/h) | 256 | 293 | 231 | 206 | 97 | 46 |
|  | Two-wheelers (vehicles/h) | 161 | 229 | 270 | 369 | 198 | 228 |
|  | Total traffic $\mathrm{VHP}_{e, 4}$ (vehicles/h) | 2,859 | 3,188 | 2,617 | 3,075 | 3,079 | 2,909 |
| 5 | Cars (vehicles/h) | 2,087 | 2,251 | 1,660 | 1,717 | 2,216 | 1,921 |
|  | Heavy vehicles (vehicles/h) | 218 | 264 | 204 | 175 | 84 | 42 |
|  | Two-wheelers (vehicles/h) | 153 | 199 | 184 | 183 | 131 | 110 |
|  | Total traffic $\mathrm{VHP}_{e, 5}$ (vehicles/h) | 2,458 | 2,714 | 2,048 | 2,075 | 2,431 | 2,073 |
| 6 | Cars (vehicles/h) | 1,500 | 2,131 | 1,430 | 1,203 | 1,661 | 1,529 |
|  | Heavy vehicles (vehicles/h) | 102 | 109 | 124 | 116 | 62 | 28 |
|  | Two-wheelers (vehicles/h) | 94 | 141 | 150 | 132 | 98 | 94 |
|  | Total traffic $\mathrm{VHP}_{e, 6}$ (vehicles/h) | 1,696 | 2,381 | 1,704 | 1,451 | 1,821 | 1,651 |
| 7 | Cars (vehicles/h) | 1,433 | 2,061 | 1,395 | 1,135 | 1,611 | 1,468 |
|  | Heavy vehicles (vehicles/h) | 101 | 109 | 123 | 119 | 62 | 34 |
|  | Two-wheelers (vehicles/h) | 83 | 130 | 138 | 122 | 86 | 64 |
|  | Total traffic $\mathrm{VHP}_{e, 7}$ (vehicles/ h ) | 1,617 | 2,300 | 1,656 | 1,376 | 1,759 | 1,566 |
| 8 | Cars (vehicles/h) | 1,439 | 2,084 | 1,583 | 1,410 | 1,850 | 1,662 |
|  | Heavy vehicles (vehicles/h) | 152 | 151 | 184 | 210 | 77 | 38 |
|  | Two-wheelers (vehicles/h) | 70 | 108 | 121 | 114 | 76 | 39 |
|  | Total traffic $\mathrm{VHP}_{e, 8}$ (vehicles/h) | 1,661 | 2,343 | 1,888 | 1,734 | 2,003 | 1,739 |
| 9 | Cars (vehicles/h) | 1,078 | 1,820 | 1,408 | 1,431 | 1,566 | 1,521 |
|  | Heavy vehicles (vehicles/h) | 77 | 109 | 99 | 109 | 54 | 34 |
|  | Two-wheelers (vehicles/h) | 155 | 429 | 491 | 545 | 426 | 385 |
|  | Total traffic $\mathrm{VHP}_{e, 9}$ (vehicles/h) | 1,310 | 2,358 | 1,998 | 2,085 | 2,046 | 1,940 |


Autodesk Inc. AutoCAD 2000 software, which contained aerial surveys of the urban area investigated. Intersections were modeled on the basis of their geometric characteristics (e.g., number of lanes, width of lanes, grades) and priority rules (e.g., stop or give way on minor roads). Driver behavior was simulated by employing car-following and lane-changing models. The way in which the car-following model was implemented in AIMSUN also took the additional constraints into account on the braking capabilities of vehicles that are imposed on the classic safe-to-stop distance. The lane-changing process was modeled as a decision-making process that emulates the driver's behavior when considering changing lane. However, at intersections when motor vehicles are queuing up waiting to go straight on and/or to turn, no lane changing is allowed in simulation. Lane splitting at intersections, e.g., by motorcycles, even if generally tolerated in the field, is considered violation in Italy. These violations, just as other illegal forms of behavior (e.g., stop and/or give way violations and the use of cell phone), in general cannot yet be modeled in simulation, so they are not considered in the analysis. The traffic was modeled on the basis of vehicle type (car, heavy vehicle, and two-wheelers) and assigning both the paths of each vehicle type from its origin to its destination (turning movements) and the corresponding number of vehicles on the basis of 15-min intervals (same time intervals of traffic measurements in the field) to represent traffic demand.

The microsimulation model under consideration was subsequently resolved, and the results in the postprocessing phase were shown. Typically predictions of traffic, speed, density, queue, delay time, travel time, etc., were computed. An animated 2D output of the simulation runs was also shown.

## Calibration

The calibration operation involved the capability of the representation of geometric and traffic characteristics. The calibration was related to the testing of model accuracy by comparing traffic values in simulation to those measured in the field. In this respect it is to be said that in some single intersections that had been simulated as being isolated, it was found that the computed traffic was not a reasonable approximation of the traffic in the field. This was attributable to the short distance in the field between the adjacent intersections (less than 150 m), which influenced the traffic flow entering the downstream intersection. When a single intersection was assumed as isolated in simulation, this did not reflect the actual situation where the traffic entering this intersection was conditioned by the close presence of the upstream intersection, as a result differences between the simulated and measured traffic were found. For this reason larger-scale intersections rather than single intersections were modeled. Wider geometric configurations, containing one or more adjacent single intersections, which were consistent with the

Table 5. Intersection Scenarios and Corresponding Total Accident Data and Total Traffic Volume ( $\sum \mathrm{VHP}_{e, i}$ ) during Peak Hours
| Intersection scenario | Accident data and traffic volume for each scenario | Time |  |  |  |  |  | Total number of accidents |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 7:008:00 a.m. | 8:009:00 a.m. | 12:00 a.m.1:00 p.m. | 1:002:00 p.m. | 6:007:00 p.m. | 7:008:00 p.m. |  |
| I (Intersection | Total number of accidents for each scenario | 1 | 8 | 25 | 13 | 5 | 4 | 56 |
| $i=1,2$, and 3) | $\sum \mathrm{VHP}_{e, i}$ (vehicles/h) | 4,539 | 6,759 | 6,728 | 6,820 | 5,878 | 5,898 |  |
| II (Intersection | Total number of accidents for each scenario | 1 | 1 | 2 | 2 | 3 | 3 | 12 |
| $i=4$ and 5) | $\sum \mathrm{VHP}_{e, i}($ vehicles $/ \mathrm{h})$ | 5,317 | 5,902 | 4,665 | 5,150 | 5,510 | 4,982 |  |
| III (Intersection | Total number of accidents for each scenario | 1 | 4 | 3 | 4 | 5 | 5 | 22 |
| $i=6,7$, and 8) | $\sum \mathrm{VHP}_{e, i}$ (vehicles/h) | 4,974 | 7,024 | 5,248 | 4,561 | 5,583 | 4,956 |  |
| IV (Intersection | Total number of accidents for each scenario | 0 | 4 | 0 | 3 | 2 | 1 | 10 |
| $i=9$ ) | $\sum \mathrm{VHP}_{e, i}$ (vehicles/h) | 1,310 | 2,358 | 1,998 | 2,085 | 2,046 | 1,940 |  |
|  | Total number of accidents of 4 scenarios |  |  |  |  |  |  | 100 |


physical size of the scenario area, were defined. In particular four intersection scenarios, named from I to IV, were identified to be considered as isolated in simulation (i.e., not affected by upstream or downstream intersections). Each intersection scenario contained one or more of the previously mentioned single intersections as listed below: I (Intersection 1, 2, and 3), II (Intersection 4 and 5), III (Intersection 6, 7, and 8), IV (only Intersection 9). In Table 5 are reported these four intersection scenarios and, during the peak hours, the total corresponding accident data (sum of accident data of each intersection $i$ contained in the scenario) and total traffic volume $\sum \mathrm{VHP}_{e, i}$ (sum of traffic volumes entering each intersection $i$ of scenario).

Once having identified these intersection scenarios as isolated and having considered driver behavior as previously mentioned (i.e., drivers do not change lane at intersections, maintain at least a minimum headway, and have knowledge of the priority of movements), the calibration process referred to vehicle characteristics (length, width, maximum speed desired, maximum acceleration and deceleration, etc.), traffic volume of all turning maneuvers (right turn, left turn, and straight on), and traffic composition (cars, heavy vehicles, and two-wheelers). The measured traffic volume is one of the most important forms of simulation input. However, the simulation results are said not to provide the real traffic because the simulation model incorporates several parameters that often require calibrating. In general, the calibration involves the comparison of the simulation output with the input value of each parameter used. For example, if the headway generated by simulation is less than the minimum allowable headway, this parameter has to be set to the minimum and a new simulation run is necessary. For the purpose of this study, the calibration process was interrupted when no other adjustment of parameters involved in the simulation model appeared to be further necessary, and by comparing the traffic volumes measured in the field with the traffic volumes generated in simulation, the corresponding differences were within predefined

![](https://cdn.mathpix.com/cropped/729e77a9-37c3-4b4c-bfce-c67c9aa44e74-08.jpg?height=1076&width=1571&top_left_y=1422&top_left_x=277)
Fig. 1. Comparison of measured and simulated morning peak-hour volume

statistical tolerance levels. In this respect, the GEH statistic was used for validating the calibration process:

$$
\mathrm{GEH}=\sqrt{\frac{2(M-C)^{2}}{M+C}}
$$

where $M=$ simulated hourly traffic volume; and $C=$ hourly traffic volume measured in the field. In all the six cited peak hours the recommended GEH value less than 5 was observed, thus demonstrating that a good level of conformity between the simulated peak hourly volumes and those measured in the field was obtained. In Figs. 1, 2, and 3 the results of simulation runs, along with measured traffic volumes are presented. The visual comparisons also confirms close agreement between simulated and actual traffic volumes.

Therefore, the writers are confident that microsimulation modeling, which has been performed in this paper, reflects actual traffic conditions accurately. In this paper, only the findings of the validation process are reported but not everything the writers did to achieve this objective. This was done to focus the reader's attention more especially on the main topic of this paper that concerns the potential of simulation with associated conflicts to analyze sites for which an insufficient number of accidents is observed and to shorten the length of the paper.

## Critical Conflicts

## Computing Procedure

Although microsimulation approach offers an excellent approximation of actual traffic flows, it does not yet permit extracting potential collision situations directly. In a microsimulation model, vehicles follow a certain path and react to other vehicles in a programmed manner in such a way that they do not collide. But when vehicles approach each other in time and/or space they could crash if no action is taken. However, this situation, which may be identified as a conflict, cannot yet be simulated directly in a microsimulation model. Thus for the purpose of this paper, an interesting point was to identify a procedure on the basis of the results of simulation for predicting conflict points. Because trajectories of vehicles at intersections attributable to turning movements (right turn, left turn, and straight on) are recognized to be particularly dangerous, a trajectory file (named TRJ file) was generated from AIMSUN after traffic simulation had been completed. Subsequently, the software named Surrogate Safety Assessment (SSAM), which is compatible with AIMSUN, was used for calculating and classifying conflicts attributable to trajectories of vehicles from the aforementioned TRJ file. SAAM was also used for computing a set of safety indicators such TTC and PET and their threshold values to identify the time when conflicts had to be classified as critical conflicts. For this aim, TTC and PET threshold values of 1.5 and 5 s, respectively, were used in this paper, as reported in Gettman et al. (2008). A collision becomes very probable when TTC and PET are below these values. Given that SSAM also includes a filter tool, this permitted excluding conflicts having TTC > 1.5 s and PET > 5 s. Moreover, conflicts with TTC = 0 and/or PET $=0$ were also excluded, so that only the events with $0<\mathrm{TTC} \leq 1.5 \mathrm{~s}$ and $0<\mathrm{PET} \leq 5 \mathrm{~s}$ were considered in the conflict analysis.

SSAM also provided the number of critical conflict types (crossing, rear-end, lane change) for each simulation. Because no universally accepted classification of the aforementioned conflict types on the basis of the conflict angle (angle of hypothetical

![](https://cdn.mathpix.com/cropped/729e77a9-37c3-4b4c-bfce-c67c9aa44e74-09.jpg?height=1074&width=1577&top_left_y=1427&top_left_x=275)
Fig. 2. Comparison of measured and simulated afternoon peak-hour volume

![](https://cdn.mathpix.com/cropped/729e77a9-37c3-4b4c-bfce-c67c9aa44e74-10.jpg?height=1089&width=1566&top_left_y=105&top_left_x=281)
Fig. 3. Comparison of measured and simulated evening peak-hour volume

collision between conflicting vehicles) is reported in the literature, this paper assumes in simulation with reference to the absolute value of the conflict angle that the conflict type is classified as a rear-end conflict if |conflict angle| < 30°, a crossing conflict if |conflict angle| $>85^{\circ}$, or otherwise a lane-changing conflict, as is reported in Gettman et al. (2008). Obviously a different choice of the absolute value of the conflict angle influences the classification of the conflict type. It should also be noted that at intersections the number of different conflict types depends on the traffic volume of a minor road that crosses the traffic volume of a major road. If the former is much less than the latter, crossing conflicts might also be found at unsignalized intersections to be much fewer than rear-end conflicts that are, instead, generated by the number of stops within the traffic streams of both the major and minor road. Thereby it might not be surprising that the number of crossing conflicts computed in a simulation at unsignalized intersections may be greater than that of rear-end conflicts. However, making a safety analysis at intersections on the basis of different conflict types, albeit interesting, still appears to be difficult in fact, because it is affected by the way followed for classifying conflicts and by several variables involved (e.g., traffic volume of turning movements and/or intersection geometry that could obstruct the view of maneuvers) and by the number of observed crashes for each type.

In this paper, because information in the field regarding the type of crash was sometimes unavailable from the official urban police reports and dividing crashes by type in many cases would have resulted in too small a number for each type, it was decided to make an analysis only on the basis of the total number of critical conflicts (which obviously includes all conflict types).

## Counting of Critical Conflicts

In this section critical conflicts (0< TTC $\leq 1.5 \mathrm{~s}$ and $0<$ $\mathrm{PET} \leq 5.0 \mathrm{~s}$ ) computed for each intersection scenario during peak hours, according to the simulation procedure previously described, are presented and discussed. Table 6 contains the total number of critical conflicts calculated, along with the number of different conflict types. It results that a very high total number of critical conflicts characterizes Intersection Scenario I in the afternoon peak hours 12:00 a.m.-1:00 p.m. (757 critical conflicts) and 1:00-2:00 p.m. (862 critical conflicts). This appears to be in keeping with the number of accidents recorded during these peak hours (25 and 13 crashes, respectively). The total number of critical conflicts was found, in contrast, to be very low for Intersection Scenario IV in the peak hours 7:00-8:00 a.m. (32 critical conflicts) and 12:00 a.m.-1:00 p.m. (57 critical conflicts), in which no accident was observed in the field. This seems to suggest that a high (low) number of critical conflicts can indicate more (or fewer) crashes.

It is worth noting that such a high number of crashes at Intersection Scenario I in the afternoon peak hours might be attributable to both high hourly traffic volumes and to different types of drivers compared with those driving in the morning peak hours. The intersections of Scenario I are prevalently located in a commercial area with the presence of many shops that are open between 12:00 a.m. and 1:00 p.m. and between 1:00 p.m. and 2:00 p.m. in contrast with the previously mentioned morning peak hours. This implies that the intersections of Scenario I, even if having similar hourly traffic volumes, are crossed during the afternoon peak hours by both commuter and noncommuter drivers in contrast with morning peak hours in which are prevalently commuters. Noncommuter drivers do not display the same driving behavior as do regular commuters.

Table 6. Critical Conflicts ( $0<$ TTC $\leq 1.5 \mathrm{~s}$ and $0<$ PET $\leq 5$ s ) and Corresponding Conflict Types for Each Intersection Scenario during Peak Hours
| Intersection scenario | Number of critical conflict types | Time |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 7:008:00 a.m. | 8:009:00 a.m. | 12:00 a.m.1:00 p.m. | 1:002:00 p.m. | 6:007:00 p.m. | 7:008:00 p.m. |
| I (Intersection | Number of crossing conflicts | 4 | 20 | 18 | 21 | 8 | 13 |
| 1, 2, and 3) | Number of rear-end conflicts | 267 | 530 | 634 | 686 | 417 | 464 |
|  | Number of lane-changing conflicts | 44 | 123 | 105 | 155 | 54 | 77 |
|  | Total number of critical conflicts | 315 | 673 | 757 | 862 | 479 | 554 |
| II (Intersection 4 and 5) | Number of crossing conflicts | 0 | 0 | 3 | 0 | 0 | 0 |
|  | Number of rear-end conflicts | 129 | 76 | 58 | 201 | 99 | 231 |
|  | Number of lane-changing conflicts | 13 | 14 | 3 | 18 | 8 | 7 |
|  | Total number of critical conflicts | 142 | 90 | 64 | 219 | 107 | 238 |
| III (Intersection 6, 7 and 8) | Number of crossing conflicts | 8 | 13 | 7 | 5 | 15 | 7 |
|  | Number of crossing conflicts | 159 | 550 | 355 | 278 | 228 | 86 |
|  | Number of lane-changing conflicts | 12 | 28 | 12 | 12 | 9 | 2 |
|  | Total number of critical conflicts | 179 | 591 | 374 | 295 | 252 | 95 |
| IV (Intersection 9) | Number of crossing conflicts | 0 | 0 | 1 | 1 | 0 | 0 |
|  | Number of rear-end conflicts | 29 | 69 | 49 | 92 | 68 | 62 |
|  | Number of lane-changing conflicts | 3 | 8 | 7 | 8 | 9 | 5 |
|  | Total number of critical conflicts | 32 | 77 | 57 | 101 | 77 | 67 |


Table 7. Hourly Critical Conflicts $(0<\mathrm{TTC} \leq 1.5 \mathrm{~s}, 0<\mathrm{PET} \leq 5 \mathrm{~s})$ Computed in Simulation and Corresponding Hourly Traffic Volumes (Measured in the Field) that Enter Each Intersection Scenario from the Major $\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)$ and Minor Roads $\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)$, Respectively
| Intersection scenario | Total critical conflicts and traffic volumes | Time |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 7:008:00 a.m. | 8:009:00 a.m. | 12:00 a.m.1:00 p.m. | 1:002:00 p.m. | 6:007:00 p.m. | 7:008:00 p.m. |
| I (Intersection | Hourly critical conflicts | 315 | 673 | 757 | 862 | 479 | 554 |
| 1, 2, and 3) | $\mathrm{VHP}_{e, \mathrm{Ma}}$ (vehicles/h) | 3,418 | 5,213 | 4,882 | 4,994 | 4,359 | 4,360 |
|  | VHP ${ }_{e, \mathrm{Mi}}$ (vehicles/h) | 1,121 | 1,546 | 1,846 | 1,826 | 1,519 | 1,538 |
| II (Intersection | Hourly critical conflicts | 142 | 90 | 64 | 219 | 107 | 238 |
| 4 and 5) | $\mathrm{VHP}_{e, \mathrm{Ma}}$ (vehicles/h) | 4,159 | 4,568 | 3,232 | 4,168 | 4,232 | 3,987 |
|  | VHP ${ }_{e, \mathrm{Mi}}$ (vehicles/h) | 1158 | 1,334 | 1,433 | 982 | 1,278 | 995 |
| III (Intersection | Hourly critical conflicts | 179 | 591 | 374 | 295 | 252 | 95 |
| 6, 7, and 8) | VHP ${ }_{e, \mathrm{Ma}}$ (vehicles/h) | 4,760 | 6,692 | 4,703 | 3,980 | 5,187 | 4,430 |
|  | $\mathrm{VHP}_{e, \mathrm{Mi}}($ vehicles $/ \mathrm{h})$ | 214 | 332 | 545 | 581 | 396 | 526 |
| IV (Intersection 9) | Hourly critical conflicts | 32 | 77 | 57 | 101 | 77 | 67 |
|  | $\mathrm{VHP}_{e, \mathrm{Ma}}$ (vehicles/h) | 1,135 | 2,007 | 1,736 | 1,792 | 1,759 | 1,618 |
|  | $\mathrm{VHP}_{e, \mathrm{Mi}}($ vehicles $/ \mathrm{h})$ | 175 | 351 | 262 | 293 | 287 | 322 |


Drivers who do not usually travel into the city, not being familiar with the perception of the accident risk at these intersections, do not adopt sufficient safety margins, so that more accidents may occur.

Table 6 also shows that, for the intersections investigated in the present paper, rear-end conflicts are found to be more frequent than crossing conflicts or lane-changing conflicts.

Table 7 contains, in contrast, the number of hourly critical conflicts computed in simulation and the corresponding traffic expressed in terms of hourly traffic volume (measured in the field) that enters each Intersection Scenario from the major $\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)$ and minor roads $\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)$, respectively.

This table was used for the subsequent statistical modeling.

## Statistical Modeling

The objective of statistical modeling in the present section is to estimate the expected number of accidents in the field on a given intersection scenario during peak hours as a function of critical conflicts computed in the simulation model. Thus, a conflict-based crash-prediction model was developed, and goodness-of-fit tests were used to determine the strength of this relationship. In addition, a traditional traffic volume-based crash-prediction model was also developed. This has allowed assessing the crash-prediction capabilities of the conflicts-based model compared with the traffic volume-based model.

Generalized linear regression models (GLM) were used to estimate the expected crash frequency at each intersection scenario. In particular, it was assumed that accident counts $Y_{i}$ occurring at the $i$-th peak hour time of the investigated intersection scenarios, during the observation time interval of 5 years, are negative binomial (NB) random variables with $E\left\{Y_{i}\right\}=\lambda_{i}$ and $\operatorname{Var}\left\{Y_{i}\right\}=$ $\lambda_{i}\left(1+\lambda_{i} / \varphi\right)$, where $\varphi=$ overdispersion parameter, and

$$
\lambda_{i}=\exp \left(\mathbf{x}_{i}^{T} \boldsymbol{\beta}\right)
$$

where $\mathbf{x}_{i}=$ vector of $k$ covariates; and $\boldsymbol{\beta}=$ vector of $k$ (unknown) parameters [see Caliendo et al. (2007), for an in-depth discussion].

To obtain estimates, $\hat{\beta}$ and $\hat{\varphi}$ say, of the unknown parameters $\boldsymbol{\beta}$ and $\varphi$, the log-likelihood function under the governing model is maximized. In light of the invariance property of maximum likelihood (ML) estimation, $\hat{\lambda}_{i}=\exp \left(\mathbf{x}_{i}^{T} \hat{\boldsymbol{\beta}}\right)$ is the ML estimate of the expected number of accidents at the $i$-th peak hour time. For this purpose, a FORTRAN code was implemented that maximizes the log-likelihood function by using the double precision routine DBCONF of the IMSL MATH/LIBRARY (1989).

Table 8. Regression Model for Crashes as a Function of Traffic Volumes and Total Conflicts
| Parameter | $e^{\beta_{0}+\beta_{1} D u} \cdot\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)^{\beta_{2}} \cdot\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)^{\beta_{3}}$ | $e^{\beta_{0}+\beta_{1} D u} \cdot(C f)^{\beta_{2}}$ | $e^{\beta_{0}+\beta_{1} D u} \cdot(C f)^{\beta_{2}} \cdot\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)^{\beta_{3}} \cdot\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)^{\beta_{4}}$ |
| :--- | :--- | :--- | :--- |
| Constant | -6.60600 | -1.61360 | -3.90831 |
| Dummy | 1.55216 (4.31E-06) | 1.20095 (4.31E-06) | 1.23308 (4.31E-06) |
| Conflicts |  | 0.50193 (1.83E-03) | 0.36884 (1.83E-03) |
| Major traffic volume | 0.84446 (6.27E-03) |  | 0.31508 (5.06E-01) |
| Minor traffic volume | 0.10877 (5.98E-01) |  | 0.06296 (7.62E-01) |
| Overdispersion $\varphi$ | 34.89516 | 42.25238 | 47.20177 |
| Log-likelihood | 80.66 | 81.64 | 81.91 |
| Scaled deviance | 24.4 | 22.8 | 22.5 |
| Pearson chi-squared | 22.4 | 21.2 | 21.0 |
| Segrees of freedom $\nu$ | 19 | 20 | 18 |
| $\chi_{0.10 ; \nu}^{2}$ | 27.2 | 28.4 | 26.0 |
| Miaou R-squared | 0.961 | 0.967 | 0.971 |


Note: P-values in parentheses.

Three measures of goodness-of-fit of regression models are provided. The scaled deviance measure (i.e., twice the difference between the log-likelihood of the data under the saturated model and the log-likelihood under the current model), which is computed as follows:

$$
\mathrm{SD}=2 \sum_{i=1}^{n}\left[y_{i} \log \left(\frac{y_{i}}{\hat{\lambda}_{i}}\right)-\left(y_{i}+\hat{\varphi}\right) \log \left(\frac{y_{i}+\hat{\varphi}}{\hat{\lambda}_{i}+\hat{\varphi}}\right)\right]
$$

the Pearson chi-squared statistic given by

$$
X=\sum_{i=1}^{n} \frac{\left(y_{i}-\hat{\lambda}_{i}\right)^{2}}{\hat{\lambda}_{i}\left(1+\hat{\lambda}_{i} / \hat{\varphi}\right)}
$$

and the adjusted R-squared measure defined by Miaou (1996), which is computed as

$$
R^{2}=1-\frac{\hat{\varphi}_{0}}{\hat{\varphi}} \frac{n-1}{n-k}
$$

where $y_{i}=$ number of observed crashes at the $i$-th peak hour time; $\hat{\lambda}_{i}=$ estimated number of crashes at the $i$-th peak hour time; $\hat{\varphi}=$ overdispersion parameter estimated in the current NB model; $\hat{\varphi}_{0}=$ overdispersion parameter estimated in the NB model with only the constant term; $n=$ total number of observations in the sample, and $k=$ total number of parameters in the model.

In addition, the likelihood ratio test (LRT) was used to assess the significance of the covariates entering the regression model.

The following variables are considered as potential covariates in the regression model: actual total number of vehicles per hour entering each intersection scenario from the major roads $\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)$; actual total number of vehicles per hour entering each intersection scenario from the minor roads $\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)$; total number of conflicts per hour $(C f)$ generated by the simulation model on the basis of actual traffic volumes. Furthermore, the writers also considered a dummy variable $(D u)$ that takes value 1 for the time intervals between 12:00 a.m. and 1:00 p.m. and between 1:00 p.m. and 2:00 p.m. of Intersection Scenario I and 0 elsewhere. This was done to take into account the occurrence of a much higher number of crashes at Intersection Scenario I in the afternoon peak hours compared with the observed crash frequency at other peak hours of the investigated scenarios with similar traffic volumes and conflicts.

In Table 8 estimates of the parameters of the three following regression models are presented:

$$
\text { Crashes }=e^{\beta_{0}+\beta_{1} D u} \times\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)^{\beta_{2}} \times\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)^{\beta_{3}}
$$

$$
\text { Crashes }=e^{\beta_{0}+\beta_{1} D u} \times(C f)^{\beta_{2}}
$$

$$
\text { Crashes }=e^{\beta_{0}+\beta_{1} D u} \times(C f)^{\beta_{2}} \times\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)^{\beta_{3}} \times\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)^{\beta_{4}}
$$

along with goodness-of-fit measures and covariate significance measures in terms of P-values of the LRT statistic. Model (6) establishes a relationship between crashes and traffic volumes only, model (7) estimates crashes at each peak hour time as a function of conflicts only, and finally model (8) uses both traffic volumes and conflicts for predicting crashes. The scaled deviance values and the Pearson values for all the models are not significant at the 90\% level, thus indicating goodness of fit. The likelihood ratio test (LRT) showed that the covariates $D_{u}$ and $\mathrm{VHP}_{e, \mathrm{Ma}}$ in Model (6) and $D_{u}$ and $C_{f}$ in Model (7) are significant. The R-squared value was recorded to be 0.961 for the crash prediction model on the basis of traffic volumes, as opposed to 0.967 for the regression model on the basis of total conflicts. Moreover, for the Intersection Scenarios I, II, III, and IV, one estimates by Model (7) 55.9, 14.1, 20.1, and 9.9 total crashes in 5 years, respectively, compared with 52.1, 19.6, 20.4, and 7.9 predicted by the Model (6), in which the actual crashes recorded in the field are 56, 12, 22, and 10. This shows that, in the present study, the conflict-based Model (7) fits accident data slightly better than the volume-based Model (6).

Traffic volumes in Model (8), in contrast were not found to be significant, as can be seen by looking at their corresponding P-values in Table 8. This can be explained by the fact that conflicts and traffic volumes are closely correlated variables (see Table 9), so that entering traffic volume in the regression model when conflicts

Table 9. Regression Model for Total Conflicts as a Function of Traffic Volumes
| Parameter | $e^{\beta_{0}} \cdot\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)^{\beta_{1}} \cdot\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)^{\beta_{2}}$ |
| :--- | :--- |
| Constant | -7.65574 |
| Major traffic volume | 1.33443 (1.17E-06) |
| Minor traffic volume | 0.32939 (7.19E-02) |
| Overdispersion $\varphi$ | 3.76755 |
| Log-likelihood | 3,3273.4 |
| Scaled deviance | 24.8 |
| Pearson chi-squared | 17.2 |
| Degrees of freedom $\nu$ | 20 |
| $\chi_{0.10 ; \nu}^{2}$ | 28.4 |
| Miaou R-squared | 0.625 |


Note: P-values in parentheses.
are already present does not significantly contribute to reducing unexplained variability.

Table 9 shows the estimates of the parameters for predicting total conflicts as a function of traffic volumes along with the corresponding P-values:

$$
\text { Conflicts }=e^{\beta_{0}} \times\left(\mathrm{VHP}_{e, \mathrm{Ma}}\right)^{\beta_{1}} \times\left(\mathrm{VHP}_{e, \mathrm{Mi}}\right)^{\beta_{2}}
$$

All parameters were found to be significant by LRT. This table also shows that the scaled deviance and the Pearson chi-squared values are not significant at the 90\% level, thus indicating a good fit. The R-squared value was 0.625, indicating significant correlation between conflicts and traffic volumes.

More especially Model (6) shows that the total number of crashes increases with an increase in traffic volumes of major and/or minor roads, which was also found by Layfield et al. (1996). Model (7) shows that the number of total crashes increases with an increase in the number of total conflicts, thus a finding in keeping with the study made by Paddock (1974). Finally, in Model (9) the number of total conflicts is shown to become greater with an increase in traffic volumes, which is also supported by Sayed et al. (1994).

The fact that critical conflicts fit actual crashes slightly better than traffic may not come as a surprise. There is an a priori reason for believing that when critical conflicts in the unit time increase, the number of crashes also generally increases (likewise if the number of conflicts diminishes, the number of crashes is expected to fall), whereas with an increase in the hourly traffic volume a greater number of crashes is not always expected. This depends on whether we are in free-flowing or almost congested flow-traffic conditions. In free-flow conditions with an increasing volume of traffic drivers still enjoy a great amount of freedom for turning movements at intersections, a fact that might be associated with an increase in crash risk; whereas in almost congested conditions when traffic increases, the driver's freedom of maneuver starts to become ever more restricted and consequently it might be associated with a decrease in crash risk. Although it is too early to be sure that in crash-prediction models at unsignalized intersections between the two explanatory candidate variables (critical conflicts and traffic) the latter might not be taken into account, the results of this study show that at least the conflict-based model represents a valid alternative to the traffic volume-based model.

## Recommendations for Future Investigations

The writers of this paper are confident that by carrying out a suitable analysis they have correctly calibrated and implemented microsimulation models for an accurate evaluation of traffic conflicts at urban unsignalized intersections and have shown that a significant statistical relationship exists between recorded crashes and simulated conflicts. However, there still remain some points of interest that are worth investigating.

First of all, field measures of vehicle trajectories should be made for a more consolidated verification of conflicts computed in simulation. The focus of discussion is not whether the simulated conflicts can be replicated in a field study, but rather whether the simulated conflicts correlate with the actual crashes at intersections. Because this correlation has been found here, it is now of interest to investigate whether experimental measures of conflicts produce the simulated conflicts. Costs and time necessary for these future tests are now also much more justifiable.

The writers also know that the severity of accidents is important in safety analysis. However, conflicts cannot yet be directly linked to the severity of accidents. At the present, conflicts are a close representation of actual accidents and are identified by safety indicators that do not yet take into account the speed values of vehicles and the speed difference of conflicting vehicles and the vulnerability of vehicles and drivers. Therefore, it is recommended that further developments of conflict analysis should make this additional progress possible.

Also the process of producing more advanced simulation software should be made. Such software ought to give the possibility of evaluating conflicts directly without using other tools interfacing with them. Moreover the types of conflicts (crossing, rear-end, lane change) should be investigated more thoroughly, in addition to considering conflicts with buses, cyclists, and pedestrians.

However, it is to be stressed here that observed accidents are rare events with a random variation in a small-sized sample. Therefore researchers require alternative or complementary approaches as the simulation tool for evaluating safety at sites for which an insufficient number of crashes has been observed for making appropriate statistical analyses. Even if it is too early to say that observed crashes can be substituted by simulated conflicts, the findings of this paper encourage the development of a new area of research into road safety based on conflicts.

## Summary and Conclusions

This research was motivated by the need to prove the potentiality of microsimulation models for assessing safety at urban unsignalized intersections using critical conflicts computed in simulation as a surrogate safety measure. A further point of interest was to identify a crash-prediction model at unsignalized intersections on the basis of critical conflicts and traffic.

To achieve the paper's goal, a 5-year monitoring period between 2003 and 2007 was studied at the unsignalized urban intersections of the city of Salerno. Among the unsignalized intersections investigated, only those showing a total number of crashes greater than 10 in the 5 years of monitoring were preselected for analysis. These intersections were found to be nine in number. Accident reports, which were obtained from official documents of the local urban police, showed that the number of crashes at these intersections was greater during traffic peak hours (between 7:00 a.m. and 9:00 a.m.; between 12:00 a.m. and 2:00 p.m., and between 6:00 p.m. and 8:00 p.m.). As a result, accidents occurring during these peak hours were considered to be worthy of special investigation in the paper. Traffic flows in terms of hourly volume in the peak hours at the time of crashes were measured by video cameras placed at the intersections investigated. Microsimulation models were performed for the investigated intersections and the AIMSUN traffic simulation software was used to model traffic flow during the six aforementioned peak hours. During the calibration process of microsimulation models four different intersection scenarios containing one or more of the previously mentioned nine intersections were identified to be considered as isolated in simulation. The validation of these four microsimulation models was made by the GEH statistic. Subsequently, another software named the Surrogate Safety Assessment Model (SSAM), which is compatible with AIMSUN, was used for identifying the number of critical conflicts (0< TTC $\leq 1.5$ s and $0<\mathrm{PET} \leq 5 \mathrm{~s}$ ) for each intersection scenario. A collision was assumed to be highly probable when conflicts were characterized for having TTC and PET values falling within the aforementioned range. On the basis of this study the conclusions given below may be drawn.

A good level of conformity between the simulated traffic volumes during peak hours and those corresponding measured in field was obtained.

A significant correlation between recorded crashes and critical conflicts computed in microsimulation models was observed.

The conflict-based model for predicting crashes was found to fit accident data slightly better than the volume-based model.

For the model containing both conflicts and traffic volumes, it was found that traffic was not significant. This was attributable to the fact that conflicts and traffic volumes are closely correlated variables, so that if traffic enters the regression model when conflicts are already present it does not significantly contribute toward reducing unexplained variability.

Therefore the proposed model, which permits predicting crashes in the field on the basis of critical conflicts computed in simulation, was found to be a valid alternative to the traffic volume-based model.

The microsimulation approach has been verified to allow a preventive safety analysis at intersections without waiting for a crash to occur. This may offer great assistance to road designers and/or traffic operators in making preventive decisions based on (1) comparing different design alternatives by considering both traffic demand and safety in a shorter time; (2) designing an intersection by taking into account functionality and crash risk at the same time; (3) ranking the safety level of existing intersection types and evaluating the priority of countermeasures to reduce accidents; and (4) understanding how to modify the existing intersections in such a way that a good compromise may be obtained between mobility and safety before adjustments in the field are made.

One of the limitations of this study is that illegal forms of driver behavior are not considered in the analysis. More specifically traffic filtering by motorcycles, even if it represents a frequent way of riding at intersections, has not been taken into account in the simulation model. In addition, this paper is based on total accident number only so that the severity of accidents has not been investigated.

Although this paper represents a more consolidated verification of the microsimulation approach for assessing safety at intersections using critical conflicts as a surrogate safety measure, it is too early to make a generalization that observed crashes may be substituted by simulated conflicts. However the findings of this paper open the door to a new scenario of research on the basis of conflicts that is worth investigating. In this respect, field measures should be made for a more consolidated verification of simulated conflicts. Conflicts should also be linked to the severity of accidents. Further developments of simulation software should be made to give users the possibility of directly evaluating conflicts without using other tools. Conflict types (crossing, rear-end, lane change) should also be studied more carefully in simulation models, in addition to considering conflicts with buses, cyclists, and pedestrians. Thus, research requires further development to make such additional progress possible.

## Acknowledgments

The authors would like to thank the two anonymous referees whose comments proved to be invaluable.

## References

AIMSUN [Computer software]. (2010). Version 6.1.2. TSS-Transport Simulation System, Barcelona. Amundsen, F., and Hyden, C. (1977). Proc., 1st Workshop on Traffic Conflicts, Institute of Transport Economics, Oslo, Norway.
Archer, J. (2000). "Developing the potential of micro-simulation modelling for traffic safety assessment." ICTCT, Corfu, Greece.
Archer, J., and Young, W. (2010). "Signal treatments to reduce the likelihood of heavy vehicle crashes at intersections: Microsimulation modelling approach." J. Transp. Eng., 136(7), 632-639.
Autodesk Inc. Autocad. [Computer software]. (2000) Autodesk, United States.
Bachmann, C., Roorda, M. J., and Abdulhai, B. (2011). "Simulating traffic conflicts on truck-only infrastructure using an improved time-tocollision definition." 90th Transportation Research Board Annual Meeting (CD-ROM), Transportation Research Board, Washington, DC.
Barcelo, J., Dumont, A. G., Montero, L., Perarnau, J., and Torday, A. (2003). "Safety indicators for micro-simulation based assessments." 82nd Transportation Research Board Annual Meeting (CD-ROM), Transportation Research Board, Washington, DC.
Caliendo, C., Guida, M., and Parisi, A. (2007). "A crash-prediction model for multilane roads." Accid. Anal. Prev., 39, 657-670.
Cooper, D., and Ferguson, N. (1976). "A conflict simulation model." Traffic Eng. Control, 17, 306-309.
Cunto, F., and Saccomanno, F. F. (2008). "Calibration and validation of simulated vehicle performance at signalized intersections." Accid. Anal. Prev., 40, 1171-1179.
Darzentas, J., McDowell, M. R. C., and Cooper, D. (1980). "Minimum acceptance gaps and conflict involvement in a single crossing maneuver." Traffic Eng. Control, 21, 58-62.
Dijkstra, A., Marchesini, P., Bijleveld, F., Kars, V., Drolenga, H., and van Maarseveen, M. (2010). "Do calculated conflicts in microsimulation model predict number of crashes?" Transportation Research Record, Transportation Research Board, Washington, DC, 105-112.
Elvik, R., and Vaa, T. (2004). The handbook of road safety measures, Elsevier.
Evans, L. (1991). Traffic safety and the drive, Van Nostrand Reinhold, Amsterdam.
FHWA. (1976). Traffic control system handbook, implementation package 76-10, US Dept. of Transportation Federal Highway Administration Office of Development Implementation Division, Washington, DC.
Gettman, D., and Head, L. (2003). "Surrogate safety measures from traffic simulation models." Report No: FHWA-RD-03-050, US Dept. of Transportation, Federal Highway Administration, Washington, DC.
Gettman, D., Pu, L., Sayed, T., and Shelby, S. (2008). "Surrogate safety assessment model and validation: Final report."Report No: FHWA-HRT-08-051, US Dept. of Transportation, Federal Highway Administration, Washington, DC.
Guido, G., Saccomano, F., Vitale, A., Astarita, V., and Festa, D. (2011). "Comparing safety performance measures obtained from video capture data." J. Transp. Eng., 137(7), 481-491.
Hallen, B. L., Shin, B. T., and Cooper, P. J. (1978). "Analysis of traffic conflict collisions." Transportation Research Record, Washington, DC, 67-74.
Hayward, J. C. (1971). "Near misses as a measure of safety at urban intersections." Doctoral thesis, The Pennsylvania State Univ., Dept. of Civil Engineering, Penn State.
IMSLMATH/LIBRARY. (1989). Fortran subroutines for mathematical applications, IMSL, United States.
Kiefer, R. J., Le Blanc, D. J., and Flannagan, C. A. (2005). "Developing an inverse time-to-collision crash alert timing approach based on drives' last-second braking and steering judgments." Accid. Anal. Prev., 37, 295-303.
Laureshyn, A., Svensson, A., and Hyden, C. (2010). "Evaluation of traffic safety, based on micro-level behaviour data: Theoretical framework and first implementation." Accid. Anal. Prev., 42, 1637-1646.
Layfield, R. L., Summersgill, I., Hall, R. D., and Chatterjee, K. (1996). "Accidents at urban priority crossroads and staggered junctions."

TRL Report 185, Transportation Research Laboratory, ISSN 0968-4107, Crowthorne, England.
Miaou, S. P. (1996). "Measuring the goodness-of-fit of accident prediction models." Report No: FHWA-RD-96-040, US Dept. of Transportation, Federal Highway Administration, Washington, DC.
Minderhould, M. M., and Bovy, P. H. L. (2001). "Extended time-tocollision measures for road traffic safety assessment." Accid. Anal. Prev., 33, 89-97.
Paddock, R. (1974). The traffic conflict technique: An accident prediction method, Dept. of Transportation, Division of Highway Bureau of Traffic Control, Ohio.
Pirdavani, A., Brijs, T., Bellemans, T., and Wets, G. (2010). "Evaluation of traffic safety at un-signalized intersections using microsimulation: A utilization of proximal safety indicators." Adv. Transp. Studies, 22, 43-50.
Sayed, T., Brown, G., and Navin, F. (1994). "Simulation of traffic conflicts at unsignalized intersections with TSC-Sim." Acc. Anal. Prev., 26, 593-607.
Vogel, K. (2003). "A comparison of headway and time to collision as safety indicators." Acc. Anal. Prev., 35, 427-473.
Yang, H., Ozbay, K., and Bartin, B. (2010). "Application of simulation based traffic conflict analysis for highway safety evaluation." Proc., 1098 12th WCTR, Jul. 11-15, Lisbon.


[^0]:    ${ }^{1}$ Dept. of Civil Engineering, Univ. of Salerno, 84084 Fisciano (SA), Italy (corresponding author). E-mail: ccaliendo@unisa.it
    ${ }^{2}$ Dept. of Electronic and Computer Engineering, Univ. of Salerno, 84084 Fisciano (SA), Italy.
    Note. This manuscript was submitted on January 24, 2012; approved on June 13, 2012; published online on August 22, 2012. Discussion period open until May 1, 2013; separate discussions must be submitted for individual papers. This paper is part of the Journal of Transportation Engineering, Vol. 138, No. 12, December 1, 2012. © ASCE, ISSN 0733-947X/ 2012/12-1453-1467/\$25.00.

