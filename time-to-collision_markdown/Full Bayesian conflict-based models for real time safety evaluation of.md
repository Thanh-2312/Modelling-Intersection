# Full Bayesian conflict-based models for real time safety evaluation of signalized intersections 

Mohamed Essa ${ }^{\mathrm{a}}$, Tarek Sayed ${ }^{\mathrm{b}, *}$<br>${ }^{\text {a }}$ Department of Civil Engineering, University of British Columbia, 6250 Applied Science Lane, Vancouver, BC, V6T 1Z4, Canada<br>${ }^{\mathrm{b}}$ Distinguished University Scholar, Department of Civil Engineering, University of British Columbia, 6250 Applied Science Lane, Vancouver, BC, V6T 1Z4, Canada

ARTICLE INFO

Keywords:
Automated conflict analysis
Effect of signal design on safety
Safety performance functions
Real time safety evaluation
Full Bayesian analysis


#### Abstract

Existing advanced traffic management and emerging connected vehicles (CVs) technology can generate considerable amount of data on vehicle positions and trajectories. This data can be used for real-time safety optimization of intersections. To achieve this, it is essential to first understand how changes in signal control affect safety in real-time. This paper develops conflict-based safety performance functions (SPFs) of signalized intersections at the cycle level using multiple traffic conflict indicators. The developed SPFs relate various dynamic traffic parameters to the number of rear-end conflicts at the signal cycle. The traffic parameters included: queue length, shock wave speed and area, and the platoon ratio. The Time-to-Collision, the Modified-Time-to-Collision, and the Deceleration Rate to Avoid the Crash were used as traffic conflict indicators. Traffic video-data collected from six signalized intersections was used in the analysis. The SPFs were developed using the Full Bayesian approach to address the unobserved heterogeneity and the variation among different sites. Overall, the results showed that all the developed SPFs have good fit with all explanatory variables being statistically significant. Also, the highest conflict frequency was noticed at the beginning of the green time, while the highest conflict severity was noticed at the beginning of the red time. Lastly, the results can be used most beneficially in real-time safety optimization of signalized intersection.


## 1. Introduction

In the existing practice, the management of traffic flow (aimed at improving the level of service of traffic facilities) and road safety (aimed at reducing crashes) have largely been considered independently despite the clear relationship between them. This can mainly be attributed to the availability of numerous traffic micro-simulation tools that can simulate traffic flow. However, most existing traffic flow models only focus on evaluating the level of service. They usually assume a crash-free environment and ignore violating road user behavior that can lead to crashes. As well, collecting data on important traffic control-related variables that can affect safety such as the shock wave characteristics at signalized intersections is difficult and need special advanced algorithms. Nevertheless, existing advanced traffic management and information systems now provide high-resolution traffic data and are capable to efficiently manage and analyze this data. Moreover, the emerging connected vehicles (CVs) technology that uses wireless communication between vehicles, infrastructure, and other road users will generate considerable amount of data on vehicle positions and trajectories (U.S. Department of Transportation, 2015). This data can be used for real-time safety and mobility optimization of traffic flow.

One of the promising applications of CVs is improving mobility at signalized intersections by minimizing the total delays. This application has been investigated in several studies ((Lee et al., 2013; Guler et al., 2014; Feng et al., 2015), among others). The main principle is that traffic signal controllers in the CVs environment can be adapted in realtime using vehicle-to-infrastructure (V2I) communications. The travel time of each phase can be estimated and updated repeatedly in a specific time interval (e.g. 5 s), and subsequently the green light can be given to the phase with the highest travel time. This could significantly decrease delays and improve mobility (Lee et al., 2013). One other potential application of CVs is the safety optimization of traffic signal control. However, the main question is how traffic signal controllers can be adapted in real-time to improve safety. Unlike vehicle delay and travel time, the safety of signalized intersections cannot be directly estimated in real-time from CVs data especially at low market penetration rates. Therefore, the main challenge becomes how safety of signalized intersections can be evaluated in real-time. Also, how realtime changes in the signal controller design can affect safety.

[^0]Traditionally, the safety of signalized intersections has often been evaluated at an aggregate level by relating historical collision records to the annual traffic volume and the geometric characteristics of the intersection. Relying on collision data in modelling real-time safety is very difficult for several reasons. First, the use of the historical collision data in safety analysis requires collisions to occur and be recorded over an adequately long period (usually years) in order to conduct a statistically sound safety diagnosis (Sayed and Zein, 1999; Chin and Quek, 1997). Second, the use of several years of collisions requires reliance on aggregate exposure measures such as the annual daily traffic (AADT) which does not explicitly account for the fact that not all vehicles are interacting unsafely (El-Basyouny and Sayed, 2013), and does not represent the variation of traffic flow within shorter periods. Third, important signal cycle-related variables that can affect intersection safety such as the arrival type and the shock wave characteristics are usually ignored due to the traffic data aggregation (Essa and Sayed, 2018).

A recent study (Essa and Sayed, 2018) developed SPFs for signalized intersections at the signal cycle level with the goal of using these models for real-time safety evaluation. The developed models relate rear-end conflicts occurring in each cycle to dynamic variables such as traffic volume, maximum queue length, shock wave characteristics, and platoon ratio. The developed SPFs were based on actual traffic data obtained by video recordings at six signalized intersections. Traffic conflicts were used as a surrogate measure of safety, since they are more frequent than collisions. The developed SPFs showed good fit with all explanatory variables being significant. The models used the Timeto-Collision (TTC) (Hayward, 1972) as the only traffic conflict indicator. In addition, the TTC threshold that distinguishes between conflict and non-conflict events was assumed to be 1.50 s. The conflict severity was not investigated. Furthermore, the SPFs were developed using the GLM approach without accounting for the unobserved heterogeneity and variation of traffic conditions across different sites.

Therefore, developing SPFs at the cycle level using other conflict indicators and considering different thresholds for each indicator is useful to reflect different severity levels. As well, another statistical approach that can account for the unobserved heterogeneity and site variation is required.

This paper aims to develop SPFs for signalized intersections at the signal cycle level using multiple conflict indicators including TTC (Hayward, 1972), Modified time to collision (MTTC) (Ozbay et al., 2008), and Deceleration Rate to Avoid the Crash (DRAC) (FHWA, 2003; Archer, 2005). Both the traffic video-data and the video analysis procedure provided in (Essa and Sayed, 2018) were utilized in the analysis. The model analysis uses the Full Bayesian (FB) approach to account for unobserved heterogeneity and the variation of traffic and environmental conditions across different sites. To account for different severity levels, the SPFs were developed by identifying conflicts at several thresholds of TTC, MTTC, and DRAC. In addition, conflict severity and temporal distributions were investigated. The Severity Index (SI) based on TTC (Saunier and Sayed, 2008), the extended time to collision measures (Time Exposed Time-to-collision (TET) and Time Integrated Time-to-collision (TIT) (Minderhoud and Bovy, 2001)) were investigated.

The developed models and the temporal severity distributions can give insights about how real-time changes in the traffic signal design can affect safety of signalized intersections. The results of this paper are considered as a first step towards real-time safety optimization of signalized intersection in the CVs environment.

## 2. Related work

### 2.1. Collision-based SPFs at signalized intersections

Safety performance functions (SPFs) of signalized intersections have been widely developed, investigated and calibrated in the literature. The highway safety manual (HSM, 2010) provides SPFs that estimate the average crash frequency for signalized intersections on different road classes including rural two-lane roads, rural multi-lane roads, urban and suburban arterials. Also, several studies locally developed, adopted and calibrated SPFs for signalized intersections to local conditions of specific zones (Poch and Mannering, 1996; Miaou and Lord, 2003; Lyon et al., 2005; Wang et al., 2006; Sawalha and Sayed, 2006b; Wong et al., 2007; Wang and Abdel-Aty, 2008; El-Basyouny and Sayed, 2012; Guo et al., 2010; Persaud et al., 2012; Lee et al., 2017). The traffic exposure measure used in most of these studies was an aggregation of the traffic volume (e.g. AADT) and the predicted number of collisions was aggregated to several years.

### 2.2. Conflict-based SPFs at signalized intersections

Relying on collision data in safety analysis has several limitations. First, collisions have to occur and be recorded for a long period (usually years) to obtain statistical reliability (Sayed and Zein, 1999; Ismail et al., 2010; Chin and Quek, 1997). Second, there are well-recognized availability and quality problems associated with collision data. To overcome these limitations, traffic conflict technique has been advocated as a proactive approach to study road safety from a broader perspective than relying only on collision data analysis (Sayed and Zein, 1999; Songchitruksa and Tarko, 2006). Traffic conflicts are more frequent than collisions, can be clearly observed, and can provide insight into the failure mechanism that leads to collisions. Previous research showed that reducing traffic conflicts can lead to reducing the frequency of road collisions (Ismail et al., 2011; Sacchi et al., 2013). The use of traffic conflicts for safety diagnosis has been recently gaining acceptance among road safety researchers as a surrogate or a complementary approach to the collision data analysis approach. A traffic conflict is defined as "an observable situation in which two or more road users approach each other in space and time to such an extent that there is a risk of collision if their movements remained unchanged" (Amundsen and Hydén, 1977). A number of traffic conflict indicators based on time and space proximity were developed in the literature. The most common indicators are: Time to collision (TTC) (Hayward, 1972), Modified time to collision (MTTC) (Ozbay et al., 2008), Post-encroachment time (PET) (Cooper, 1984), Deceleration to safety distance (DST) (Hupfer, 1997), Deceleration Rate to Avoid the Crash (DRAC) (FHWA, 2003; Archer, 2005), Time Exposed Time-to-collision (TET) (Minderhoud and Bovy, 2001), and Time Integrated Time-to-collision (TIT) (Minderhoud and Bovy, 2001).

Several studies demonstrated the automated extraction of traffic conflicts from video recordings using computer vision techniques ((Autey et al., 2012; Saunier and Sayed, 2008; Laureshyn et al., 2009), among others). The automated video analysis of traffic conflicts overcomes many shortcomings in manual data collection and provides a more practical and efficient way to capture and analyze traffic conflicts.

Previous studies attempted to develop SPFs for signalized intersections on the basis of field-observed traffic conflicts (Sayed and Zein, 1999; El-Basyouny and Sayed, 2013; Zhang et al., 2014; Sacchi and Sayed, 2016a,b). The exposure measure in theses SPFs is represented by the average hourly traffic volume, while the traffic conflicts are aggregated to hours (i.e. number of conflicts/hour).

### 2.3. Real-time crash prediction

Although a large number of previous studies has focused on freeways in terms of real-time crash risk analysis (Lee et al., 2003; Pande and Abdel-Aty, 2006; Hossain and Muromachi, 2012; Ahmed and Abdel-Aty, 2013; Xu et al., 2013; Shi and Abdel-Aty, 2015; Wu et al., 2017b), a few studies have considered signalized intersections and urban arterials. Theofilatos (2017) investigated accident likelihood and severity using real-time traffic and weather data collected from two urban arterials in Athens, Greece. However, the traffic data were aggregated to one-hour interval which might not capture the variations in
traffic parameters within shorter time periods (such as the traffic signal cycle). Yuan et al. (2018) and Yuan and Abdel-Aty (2018) investigated the relationship between crash occurrence on urban arterials and realtime traffic, signal phasing, and weather characteristics using Bluetooth data, weather data, and adaptive signal control datasets. Time interval of 5 min was considered (Yuan et al., 2018; Yuan and Abdel-Aty, 2018).

Several studies have investigated the safety evaluation, collision/ conflict prediction, and SPFs for signalized intersections. However, there is a need to develop safety models that can be used for real-time safety evaluation at signalized intersections. To the best of the authors' knowledge, no studies have attempted to develop conflict-based SPFs at the signal cycle level using multiple conflict indicators and different severity levels. This study aims to fill this research gap by relating the number of traffic conflicts (identified based on multiple conflict indicators and different severity levels) during each signal cycle to various traffic parameters.

## 3. Study locations and video data collection

The video-data described in detail in (Essa and Sayed, 2018) were used in this study. The data were recorded from six signalized intersections in two cities in Canada. Fig. 1a shows the study locations 1 and 2 in the City of Edmonton, Alberta. Fig. 1b shows the study locations 3-6 in the City of Surrey, British Columbia. For all six sites, video cameras were installed to record video-data. The video camera was fixed on an existing post located either downstream the stop line or upstream the functional area of the signalized intersection. The camera scenes were generally focused on the intersection approaches where most of the rear-end conflicts occur. The distance along the intersection approach that is covered by the video camera ranges from 110 to 130 m.

Table 1 provides more details on the selected intersections that include: the location; the selected approaches; the number of lanes per approach; and the date of data collection. The video data was analyzed to track vehicles and extract their trajectories. Detailed trajectories of more than 2500 vehicles were recorded. More details about the video analysis procedure will be provided later in this manuscript.

## 4. Conflict-based SPFs at the signal cycle level

### 4.1. Traffic characteristics

### 4.1.1. Traffic volume and queue length

The first explanatory variable in the developed SPFs is the exposure

![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-03.jpg?height=1479&width=1503&top_left_y=1055&top_left_x=282)
Fig. 1. Study Locations and Video Scenes.

Table 1
${ }^{\mathrm{a}}$ Description of the Study Locations. (For interpretation of the references to colour in this table legend, the reader is referred to the web version of this article.)
| Site \# | City (Province) | Intersected roads | Video-data was recorded in | Selected intersection approaches | Number of Lanes per approach | Traffic signal timing (seconds) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Edmonton (AB) | Stony Plain Rd \& 170 St | May $27{ }^{\text {th }}$,2015 <br> (2:00-3:00 pm) <br> June $2^{\text {nd }}$, 2015 <br> (2:00-3:00 pm) | 170 St <br> (Northbound) | 1 (Right) <br> 1 (Left) <br> 4 (Through) | ○ <br> 51 <br> 4 <br> 65 |
| 2 | Edmonton (AB) | Gateway Blvd \& 34 Ave | May $26^{\text {th }}$,2015 <br> (3:00-4:00 pm) | Gateway Blvd (Northbound) | 1 (Right) <br> 1 (Left) <br> 4 (Through) | ○ |
| 3 | Surrey (BC) | 72 Ave \& 128 St | March $28{ }^{\text {th }}$, 2012 <br> (10:00-11:00 am) <br> March $29{ }^{\text {th }}$, 2012 <br> (2:00-3:00 pm) | 72 Ave <br> (Eastbound \& <br> Westbound) | 1 (Left) <br> 1 (Through + Right) <br> 1 (Through) | ○ |
| 4 | Surrey (BC) | 72 Ave \& 132 St | April $3^{\text {rd }}$, 2012 <br> (9:00 - 10:00 am) | 72 Ave <br> (Westbound) | 1 (Left) <br> 1 (Through + Right) <br> 1 (Through) | ○ |
| 5 | Surrey (BC) | 64 Ave \& King George Blvd | June $10^{\text {th }}$, 2015 <br> (1:00-2:00 pm) <br> June $11^{\text {th }}$, 2015 <br> (1:00-2:00 pm) | King George <br> Blvd <br> (Southbound) | 1 (Right) <br> 1 (Left) <br> 2 (Through) | ○ |
| 6 | Surrey (BC) | Fraser <br> Highway \& 168 A St | June $10{ }^{\text {th }}$, 2015 <br> (9:00-10:00 am) <br> June $11^{\text {th }}$, 2015 <br> (9:00 - 10:00 am) | Fraser <br> Highway <br> (Southbound) | 1 (Bike lane) <br> 1 (Left) <br> 1 (Through + Right) <br> 1 (Through) | ○ |


${ }^{\mathrm{a}}$ Edited from the original table provided by (Essa and Sayed, 2018).
measure. The exposure was represented by the traffic volume (V) per cycle per lane. Another explanatory variable is the maximum queue length $(\mathbf{Q})$ at each cycle. For both the traffic volume and the maximum queue length, only through-lanes were considered in the analysis. Exclusive left-turn and right-turn lanes were excluded.

### 4.1.2. Shock wave characteristics

Shock waves commonly occur at signalized intersections due to the repeated stop-and-go situations. The relationship between shock waves and rear-end crashes has been proven in previous studies. Chatterjee and Davis (2016) investigated a condition for a shock wave to produce a rear-end crash using 41 shock waves including 5 resulted in rear-end crashes. Zheng et al. (2010) reported that traffic oscillation (stop-andgo driving) is significant factor that can affect the occurrence of rearend crashes on freeways. Machiani and Abbas (2016) developed a surrogate safety histogram for signalized intersections based on the relationship between rear-end conflicts and shock waves.

In this study, two shock wave characteristics were considered for developing the SPFs. The two characteristics were chosen based on their relation to rear-end conflicts. Considering the space-time diagram shown in Fig. 3, most of vehicle interactions occur around the triangle that surrounds the area where the traffic speed and flow are zeros (the shaded area). Therefore, the first shock wave characteristic considered in the analysis was the area of this triangle (A). Additionally, in the same diagram, the first backward-moving shock wave speed (shown in red color) that separates two different consecutive traffic flow states represents the maximum change or a sudden decrease in the traffic speeds. Such a sudden decrease in the speed can result in a higher risk of rear-end conflict. Therefore, the second shock wave characteristic considered in the analysis was the first backward-moving shock wave speed $\left(\mathbf{S}_{\mathbf{1 2}}\right)$. The selected shock wave area and speed were proven in a recent study to have a significant effect on the frequency of rear-end conflicts at signalized intersections (Essa and Sayed, 2018).

### 4.1.3. Platoon ratio

According to the Highway Capacity Manual (HCM, 2000), the platoon ratio is defined as the proportion of all vehicles arriving during green multiplied by the ratio of the signal cycle length to the effective green time of the subject movement. The platoon ratio (P) was considered in this study as an explanatory variable in the conflict-based SPFs. The platoon ratio and the arrival type were shown in previous studies to have a significant effect on the frequency of the rear-end conflicts at signalized intersections (Essa and Sayed, 2016, 2015a,b). For each cycle, the platoon ratio was measured assuming that the effective green time is the green time plus half of the yellow time. Afterwards, the percentage of vehicles arriving during green time was determined. If a vehicle had not stopped, it was considered to be arrived on green. If a vehicle had stopped, the first point of time of its stopping was compared to the signal timing to determine whether this vehicle arrived on red or green.

It should be noted that all the aforementioned traffic characteristics were measured only for cycles that are under-saturated. Over-saturated cycles, where a vehicle can stay in the same approach for more than one cycle, were neglected in this study. Future research is recommended to
consider over-saturated flow when evaluating safety at the cycle level.

### 4.2. Number of traffic conflicts per cycle (the model response)

This study focuses only on the rear-end conflicts at signalized intersections. Multiple rear-end conflict indicators were considered. The following sections explain more details about these indicators.

### 4.2.1. Time to collision (TTC)

TTC is generally recognized as the most frequently used indicator to identify rear-end conflicts. The TTC is defined as "the time required for two vehicles to collide if they continue at their present speeds and on the same path" (Hayward, 1972). For each constitutive vehicle trajectories moving in the same lane, the TTC can be continuously estimated over time using the following equation.

$$
T T C_{t}=\frac{X_{L, t}-X_{F, t}-D_{L}}{V_{F, t}-V_{L, t}} ; \quad \forall\left(V_{F, t}-V_{L, t}\right)>0
$$

Where:

$t$ : time interval
L: leading vehicle
$F$ : following vehicle
X: vehicle position
$V$ : vehicle speed
D: vehicle length

Using the minimum TTC of each conflict, the number of rear-end conflicts was determined for each signal cycle at different TTC thresholds. The main reason behind using different TTC thresholds is to provide multiple SPFs that can address different conflict-severity levels. Additionally, in the literature, there is a lack of agreement on the critical TTC threshold value that can be used to discriminate between conflict and non-conflict events. Hirst and Graham (1997) reported that a TTC of 4 s could be used to distinguish between dangerous and nondangerous situations. In a driving simulator experiment, Hogema and Janssen (1996) indicated that the critical TTC threshold is 3.5 and 2.6 s for non-supported and supported drivers, respectively (Hogema and Janssen, 1996; Minderhoud and Bovy, 2001). Also, the TTC threshold of 1.50 s is commonly used by researchers to define rear-end conflicts (van der Horst and Hogema, 1993). In this paper, the critical TTC thresholds range from 1 to 3 s with an interval of 0.5 s.

### 4.2.2. Modified time to collision (MTTC)

The definition of TTC is functional in defining conflicts only if the speed of the following vehicle is higher than the speed of the leading vehicle. However, this definition ignores many potential conflicts that can occur due to acceleration or deceleration discrepancies (Ozbay et al., 2008). Therefore, Ozbay et al. (2008) proposed another rear-end conflict indicator (Modified-TTC or MTTC) that considers relative positions, relative speeds, and relative accelerations of the conflicting vehicles. For each constitutive vehicle trajectories moving in the same lane, the MTTC can be continuously estimated over time using the following equation.

$$
M T T C_{t}=\frac{\Delta V_{t} \pm \sqrt{\Delta V_{t}^{2}+2 \Delta A_{t}\left(\Delta X_{t}-D_{L}\right)}}{\Delta A_{t}}
$$

Where:

$t$ : time interval
L: leading vehicle
$F$ : following vehicle

X: vehicle position

$V$ : vehicle speed
A: vehicle acceleration
D: vehicle length

$\Delta X=$ Relative position $=X_{L}-X_{F}$
$\Delta V=$ Relative speed $=V_{F}-V_{L}$
$\Delta A=$ Relative acceleration $=A_{F}-A_{L}$
Eq. (2) has two outcomes with regard to MTTC. If the two outcomes are positive, the minimum of them is considered to be the MTTC value. If one outcome is positive while the other one is negative, the positive outcome is considered to be the MTTC value. Like the TTC, the minimum MTTC value was used to determine the number of rear-end conflicts for each cycle at different thresholds (1 to 3 s with an interval of 0.5 s).

### 4.2.3. Deceleration rate to avoid crash (DRAC)

The DRAC can be defined as the rate at which a vehicle must decelerate to avoid the collision with other conflicting vehicle (FHWA, 2003; Archer, 2005). For each constitutive vehicle trajectories moving in the same lane, the DRAC can be continuously estimated over time using the following equation.

$$
\operatorname{DRAC}_{F, t}=\frac{\left(V_{F, t}-V_{L, t}\right)^{2}}{2\left[\left(X_{L, t}-X_{F, t}\right)-D_{L}\right]}
$$

Where:

$t$ : time interval
L: leading vehicle
$F$ : following vehicle
X: vehicle position
$V$ : vehicle speed
D: vehicle length

Using the maximum DRAC of each conflict, the number of rear-end conflicts was determined for each signal cycle at different DRAC thresholds. Four DRAC thresholds were chosen to address different severity levels (McDowell et al., 1983): $6 \mathrm{~m} / \mathrm{s}^{2}$ (the most severe), $4.5 \mathrm{~m} /$ $\mathrm{s}^{2}, 3 \mathrm{~m} / \mathrm{s}^{2}$, and $1.5 \mathrm{~m} / \mathrm{s}^{2}$.

It is also noteworthy to mention that the ability of DRAC to accurately reflect traffic conflicts and potential crash situation has been criticized by some researchers. Their main argument was that the DRAC does not consider the vehicle braking capability (e.g. a given DRAC value under wet pavement conditions is more critical to safety than the same value under dry pavement conditions). However, studies involving this safety measure that explores these aspects are not commonly found in the literature (Cunto and Saccomanno, 2008). Future research is recommended in order to consider these aspects.

### 4.3. Video analysis

The main objective of the video-data analysis was to extract traffic data from the video recordings. The video-analysis procedure is based on a set of MATLAB codes. The procedure started with identifying actual traffic signal timing and cycles for each intersection by detecting the changes in the signal colors from video scenes. Afterwards, moving vehicles in through lanes were tracked (exclusive left-turn and rightturn lanes were excluded), and the space-time diagram for each cycle was plotted. The whole video-analysis procedure is described in details in (Essa and Sayed, 2018). Fig. 2 shows samples of the space-time diagram results for 32 traffic signal cycles extracted from videos for one

![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-06.jpg?height=2086&width=1169&top_left_y=194&top_left_x=450)
Fig. 2. Samples of Space-Time Diagram Results (32 Traffic Signal Cycles).

of the study locations.
Using the space-time diagram, a computer code was developed to compute different traffic parameters and conflict indicators for each cycle. Thus, the outputs of the video-data analysis for each cycle were: 1) shock wave area (A); 2) traffic volume (vehicles/lane/cycle) (V); 3) backward-moving shock wave speed $\left(\mathbf{S}_{12}\right)$; 4) platoon ratio $(\mathbf{P})$; 5) maximum queue length (Q); 6) number of rear-end conflicts at different TTC thresholds; 7) number of rear-end conflicts at different MTTC thresholds; and 8) number of rear-end conflicts at different DRAC thresholds. Fig. 3 illustrates the outputs (measurements) of the video data analysis process.

With regard to the calculated TTC and MTTC, it should be noted

![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-07.jpg?height=857&width=1522&top_left_y=189&top_left_x=271)
Fig. 3. Measurements (Outputs) of Video Data Analysis Process.

that the values of the TTC and the MTTC estimated from Eqs. (1) and (2) are instantaneous values. The TTC and MTTC values were calculated in the analysis at each video frame (one second = 29.97 frames) providing adequate level of accuracy.

### 4.4. Summary of data statistics

The video analysis outputs described above were obtained for the six study locations. Table 2 provides summary statistics of the measured data. The covariates A, Q, $\mathbf{S}_{12}$, and P have good correlations with the number of rear-end conflicts, indicating that they can provide a better conflict prediction if they are incorporated in the conflict-based SPFs.

### 4.5. Full Bayesian analysis

After obtaining the aforementioned measurements, the next step was to develop conflict-based SPFs that relate different traffic characteristics of each cycle to the number of rear-end conflicts that occurred at the same cycle. The SPFs were developed using the FB approach to account for unmeasured or unobserved heterogeneity in the traffic conflict data. The FB approach has been widely used in literature for the development of collision/conflict prediction models (e.g. (Persaud et al., 2010; El-Basyouny and Sayed, 2012, 2009a; Sacchi et al., 2013)). The FB approach has a potential advantage of specifying very complex model forms, as well as the flexibility to accommodate various distributions such as the Poisson-Gamma distribution and the Poisson-LogNormal distribution (PLN). In addition, the FB approach has the ability of using prior information for any unknown parameters, and then it can provide more accurate measures of uncertainty on the posterior distributions of their estimates (Persaud et al., 2010; ElBasyouny and Sayed, 2009a,b; Sacchi et al., 2013).

Various models were developed using different combinations of the explanatory variables (V, A, Q, $\mathbf{S}_{\mathbf{1 2}}$, and P). The procedure recommended by (Sawalha and Sayed, 2001) to add explanatory variables into the model was utilized. The procedure is a forward procedure that seeks parsimonious models. In this procedure, the variables are

Table 2
Summaries of Data Statistics.
| Variable | Description | Unit | Mean | SD | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| V | Traffic Volume per lane per cycle | - | 11.58 | 3.56 | 2 | 22 |
| A | Shock wave area | km s | 1.05 | 0.96 | 0 | 3.93 |
| Q | Maximum queue length | m | 40.42 | 24.54 | 0 | 97.46 |
| $\mathrm{S}_{12}$ | Backward-moving shock wave speed | m/s | -2.07 | 2.65 | -27.2 | 0 |
| P | Platoon ratio | - | 1.26 | 0.40 | 0 | 2.27 |
| $\mathrm{TTC}_{1}$ | Number of rear-end conflicts ( $\mathrm{TTC} \leq 1.0 \mathrm{~s}$ ) | - | 0.97 | 1.40 | 0 | 6 |
| $\mathrm{TTC}_{1.5}$ | Number of rear-end conflicts (TTC $\leq 1.5 \mathrm{~s}$ ) | - | 1.88 | 1.88 | 0 | 7 |
| $\mathrm{TTC}_{2}$ | Number of rear-end conflicts ( $\mathrm{TTC} \leq 2.0 \mathrm{~s}$ ) | - | 2.97 | 2.30 | 0 | 11 |
| $\mathrm{TTC}_{2.5}$ | Number of rear-end conflicts ( $\mathrm{TTC} \leq 2.5 \mathrm{~s}$ ) | - | 3.82 | 2.57 | 0 | 12 |
| $\mathrm{TTC}_{3}$ | Number of rear-end conflicts ( $\mathrm{TTC} \leq 3.0 \mathrm{~s}$ ) | - | 4.25 | 2.73 | 0 | 13 |
| MTTC ${ }_{1}$ | Number of rear-end conflicts (MTTC $\leq 1.0 \mathrm{~s}$ ) | - | 2.60 | 2.35 | 0 | 13 |
| $\mathrm{MTTC}_{1.5}$ | Number of rear-end conflicts (MTTC $\leq 1.5$ s) | - | 4.61 | 3.12 | 0 | 17 |
| MTTC ${ }_{2}$ | Number of rear-end conflicts (MTTC $\leq 2.0 \mathrm{~s}$ ) | - | 5.38 | 3.37 | 0 | 18 |
| $\mathrm{MTTC}_{2.5}$ | Number of rear-end conflicts (MTTC $\leq 2.5 \mathrm{~s}$ ) | - | 5.88 | 3.53 | 0 | 18 |
| MTTC ${ }_{3}$ | Number of rear-end conflicts (MTTC $\leq 3.0 \mathrm{~s}$ ) | - | 6.02 | 3.64 | 0 | 19 |
| DRAC ${ }_{6}$ | Number of rear-end conflicts ( DRAC $\geq 6.0 \mathrm{~m} / \mathrm{s}^{2}$ ) | - | 0.41 | 0.77 | 0 | 3 |
| $\mathrm{DRAC}_{4.5}$ | Number of rear-end conflicts (DRAC $\geq 4.5 \mathrm{~m} / \mathrm{s}^{2}$ ) | - | 0.57 | 0.93 | 0 | 4 |
| $\mathrm{DRAC}_{3}$ | Number of rear-end conflicts ( DRAC $\geq 3.0 \mathrm{~m} / \mathrm{s}^{2}$ ) | - | 1.00 | 1.29 | 0 | 5 |
| $\mathrm{DRAC}_{1.5}$ | Number of rear-end conflicts ( DRAC $\geq 1.5 \mathrm{~m} / \mathrm{s}^{2}$ ) | - | 2.92 | 2.21 | 0 | 11 |


added to a model one by one, and the decision on whether a variable is to be retained in the model is based on: 1) the significance of the estimated coefficient of this variable (t-ratio), and 2) the improvement in the goodness of fit of the model caused by adding this variable. Also, variables that represent exposure (e.g. traffic volume (V)) must be included first (Sawalha and Sayed, 2001, 2006a).

### 4.5.1. PLN models

The PLN model is commonly used to address over-dispersion for unobserved heterogeneity. The PLN model was shown to be better than the Poisson-Gamma model when modeling traffic collisions with the presence of outliers (El-Basyouny and Sayed, 2009a). The main reason is that the tails of the PLN model are known to be heavier than those of the gamma distribution. The main limitation that makes the PLN model less popular is that the model requires more computational efforts. However, this is not an issue with the advanced computational capabilities of computer algorithms and the introduction of numerical methods in Bayesian statistics. This has allowed the application of the PLN model to analyze collision or conflict data with reasonable accuracy (Sacchi and Sayed, 2016b).

To account for over-dispersion for unobserved or unmeasured heterogeneity, FB PLN models were developed in this study following the FB procedure presented in (El-Basyouny and Sayed, 2009a). Let $Y_{i}$ denotes the number of conflicts at signal cycle $i(i=1,2 \ldots n)$. It was assumed that conflicts at the $n$ signal cycles are independent and that:

$$
Y_{i} \mid \theta_{i} \sim \operatorname{Poisson}\left(\theta_{i}\right)
$$

To address over-dispersion for unobserved or unmeasured heterogeneity, it was assumed that:

$$
\theta_{i}=\mu_{i} \exp \left(u_{i}\right)
$$

And:

$$
\ln \mu_{i}=\beta_{0}+\beta_{1} X_{i 1}+\ldots+\beta_{m} X_{i m}
$$

Where:
$X_{i 1}$ : The covariates representing the traffic characteristics (e.g. ln $\left.(\mathrm{V}), \mathrm{A}, \mathrm{Q}, \mathrm{P}, \mathrm{S}_{12}\right)$;
$\beta_{0}, \beta_{1}, \ldots, \beta_{m}$ : The model parameters;
$\exp \left(u_{i}\right)$ : A multiplicative random effect
The PLN regression model was obtained by the assumption:

$$
\exp \left(u_{i}\right) \sim \operatorname{Lognormal}\left(0, \sigma_{u}^{2}\right) \quad \text { or } u_{i} \sim N\left(0, \sigma_{u}^{2}\right)
$$

Where $\left(\sigma_{u}^{2}\right)$ denotes the extra Poisson variance that addressing unmeasured or unobserved heterogeneity.

### 4.5.2. PLN models with random intercept

Because the rear-end conflict data was measured at six different intersections, an additional variance component was added to the PLN models to account for the possibility that different sites can have different conflict risks due to the variation of traffic, geometric, driving behavior, and environmental conditions across sites. Hence, the PLN models were developed in such a way that the intercept can vary from site to site. Typically, the $n$ signal cycles belong to $k$ mutually exclusive sites. It was assumed that the $i$ th cycle belongs to site $s(i)$ where $(s(i) \in\{1,2, \ldots, k\})$, then the model can be expressed as follows:

$$
\ln \mu_{i}=\beta_{s(i), 0}+\beta_{1} X_{i 1}+\ldots+\beta_{m} X_{i m}
$$

Where:

$$
\beta_{s(i), 0}=\beta_{0}+w_{s(i)}
$$

And:

$$
w_{s(i)} \sim N\left(0, \sigma_{s}^{2}\right)
$$

Where: $\sigma_{s}^{2}$ represents the additional variance component that addressing the variation among different sites. This means that the model is equivalent to a PLN model with a random intercept that varies at each site.

### 4.5.3. Prior distributions

The formulation of FB models requires a prior distribution for each unknown parameter. A prior distribution reflects to some extent any prior knowledge about the parameter of interest. If such prior information is available before observing any data, it should be used to formulate the so-called informative priors; otherwise non-informative (vague) priors are usually used to reflect the lack of prior information (El-Basyouny and Sayed, 2009a). In this paper, prior distributions for all parameters $\left(\beta_{0}, \beta_{1}, \ldots, \beta_{m}\right)$ and all hyper-parameters $\left(\sigma_{u}^{2}, \sigma_{s}^{2}\right)$ were assumed as non-informative due to the lack of prior knowledge of their values. Following the most commonly used vague prior distributions, the prior distributions used in this paper were diffused normal distributions (with zero mean and large variance) for the regression parameters $\left(\beta_{0}, \beta_{1}, \ldots, \beta_{m}\right)$, and Gamma $(1, \varepsilon)$ for the hyper-parameters ( $\sigma_{u}^{2}, \sigma_{s}^{2}$ ), where $\varepsilon$ is a small number (e.g. 0.001) (El-Basyouny and Sayed, 2009a).

### 4.5.4. Full Bayes estimation

The posterior distributions of the model parameters needed in the FB approach can be obtained using Markov Chain Monte Carlo (MCMC) sampling techniques. MCMC techniques are used to repeatedly sample from the joint posterior distribution. The techniques generate chains of random points, whose distributions converge to the target posterior distributions. Usually, a sub-sample is used to monitor convergence and then discarded as a burn-in sample. The remaining iterations are used for parameter estimation, performance evaluation and inference. Monitoring convergence is essential because it ensures that the posterior distribution has been found in order to begin parameters sampling (El-Basyouny and Sayed, 2009a).

Therefore, in this study two independent Markov chains were used to run each model for 20,000 iterations that were discarded as burn in samples to reach convergence. Afterwards, the summary statistics of each chain were estimated, and the convergences of the developed models were checked. To check convergence, Brooks-Gelman-Rubin (BGR) statistic was used; where a value of the BGR statistic less than 1.2 indicates convergence. As well, the ratios of the Monte Carlo errors relative to the respective standard deviations of the estimates were estimated to ensure convergence. Generally, the convergence occurs if these ratios are around or less than (0.05). Moreover, the convergence was monitored throughout visual approaches such as observing trace plots of the estimated parameters (El-Basyouny and Sayed, 2009a; Osama and Sayed, 2016; Sacchi and Sayed, 2016b). Finally, after obtaining convergence, additional 20,000 iterations were performed for each chain and the significance of the parameter estimates was tested using the 95\% confidence intervals. The free statistical software (WinBUGS) (Lunn et al., 2000) was used in this study to perform MCMC sampling and to obtain estimates of the parameters for the developed FB models.

### 4.5.5. Model comparison and goodness-of-fit

The deviance information criterion (DIC) was used as a statistical goodness-of-fit measure to compare between the developed FB models. The DIC, proposed by Spiegelhalter et al. (2002), penalizes the model that has larger number of parameters (complexity of a model) as follows:

$$
\begin{aligned}
& D I C=\bar{D}+P D=\hat{D}+2^{*} P D \\
& \bar{D}=-2^{*} \log (\text { Likelihood }), \text { Liklihood is defiend as } P(y \mid \theta) \\
& \hat{D}=-2^{*} \log (\text { Likelihood }), \text { Liklihood is defiend as } P(y \mid \bar{\theta})
\end{aligned}
$$

Where:
$\bar{D}$ : The posterior mean of the unstandardized deviance of the model;
$\hat{D}$ : The point estimate of the deviance obtained by substituting the

Table 3
PLN Models for Different Conflict Indicators．（For interpretation of the references to colour in this table legend，the reader is referred to the web version of this article．）
| Model Format：$\quad \ln (Y)=\beta_{0}+\beta_{1} \ln (V)+\beta_{2} A+\beta_{3} P+\beta_{4} S_{12}+u_{i} ;$ where：$\quad u_{i} \sim N\left(0, \sigma_{u}{ }^{2}\right)$ |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Conflict Indicator | Y：Number of rear－end conflicts per cycle where | $\boldsymbol{\beta}_{\mathbf{0}}$ Estimate （2．5％，97．5％ Bayesian C．I） | $\boldsymbol{\beta}_{\mathbf{1}}$ Estimate （2．5％，97．5％ Bayesian C．I） | $\boldsymbol{\beta}_{\mathbf{2}}$ Estimate （2．5％，97．5％ Bayesian C．I） | $\boldsymbol{\beta}_{\mathbf{3}}$ Estimate （2．5％，97．5％ Bayesian C．I） | $\boldsymbol{\beta}_{\mathbf{4}}$ Estimate （2．5％，97．5％ Bayesian C．I） | $\sigma_{u}{ }^{2}$ Estimate＊＊ （2．5％，97．5％ Bayesian C．I） | DIC |
| TTC | $\mathbf{T T C} \leq \mathbf{1 . 0 ~ s e c}$ | －0．503 （－0．734，－0．302） | 1.503 （0．872，2．144） | 0.353 （0．168，0．541） | －1．145 （－1．636，－0．655） | 0.313 （0．183，0．455） | 0.030 （0．0003，0．270） | 521 |
|  | $\mathbf{T T C} \boldsymbol{\leq} \mathbf{1 . 5 ~ s e c}$ | 0.349 （0．224，0．469） | 1.250 （0．827，1．686） | 0.296 （0．166，0．422） | －0．83 （－1．182，－0．484） | 0.122 （0．055，0．197） | 0.003 （0．0003，0．019） | 674 |
|  | $\mathbf{T T C} \boldsymbol{\leq} \mathbf{2 . 0 ~ s e c}$ | 0.884 （0．790，0．975） | 1.178 （0．850，1．511） | 0.205 （0．101，0．307） | －0．765 （－1．038，－0．493） | 0.088 （0．040，0．141） | 0.002 （0．0003，0．008） | 770 |
|  | $\mathbf{T T C} \boldsymbol{\leq} \mathbf{2 . 5 ~ s e c}$ | 1.184 （1．105，1．261） | 0.993 （0．712，1．276） | 0.162 （0．070，0．253） | －0．749 （－0．989，－0．510） | 0.051 （0．014，0．091） | 0.002 （0．0003，＋0．0006） | 838 |
|  | $\mathbf{T T C} \boldsymbol{\leq} \mathbf{3 . 0 ~ s e c}$ | 1.302 （1．228，1．375） | 0.998 （0．737，1．266） | 0.150 （0．063，0．236） | －0．713 （－0．939，－0．489） | 0.040 （0．008，0．076） | 0.002 （0．0002，0．007） | 860 |
| MTTC | $\mathbf{M T T C} \boldsymbol{\leq} \mathbf{1 . 0 ~ s e c}$ | 0.722 （0．620，0．821） | 1.239 （0．900，1．583） | 0.220 （0．111，0．329） | －0．790 （－1．082，－0．498） | －－－＊ | 0.003 （0．0003，0．012） | 755 |
|  | $\mathbf{M T T C} \boldsymbol{\leq} \mathbf{1 . 5 ~ s e c}$ | 1.376 （1．305，1．447） | 1.073 （0．824，1．326） | 0.142 （0．059，0．225） | －0．677 （－0．891，－0．463） | －－－＊ | 0.002 （0．0003，0．007） | 907 |
|  | $\mathbf{M T T C} \boldsymbol{\leq} \mathbf{2 . 0 ~ s e c}$ | 1.559 （1．494，1．623） | 1.024 （0．792，1．257） | 0.128 （0．050，0．207） | －0．553 （－0．750，－0．354） | －－－＊ | 0.002 （0．0002，0．010） | 959 |
|  | $\mathbf{M T T C} \boldsymbol{\leq} \mathbf{2 . 5 ~ s e c}$ | 1.663 （1．602，1．722） | 0.975 （0．754，1．197） | 0.139 （0．062，0．213） | －0．413 （－0．601，－0．227） | －－－＊ | 0.002 （0．0003，0．012） | 1000 |
|  | $\mathbf{M T T C} \boldsymbol{\leq} \mathbf{3 . 0 ~ s e c}$ | 1.687 （1．627，1．746） | 0.984 （0．768，1．203） | 0.144 （0．070，0．218） | －0．366 （－0．552，－0．179） | －－－＊ | 0.002 （0．0003，0．013） | 1016 |
| DRAC | DVDIVDIDTICN | ——V． <br> 14．1 | DCownider <br> 1988 | Dealetate <br> ![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-09.jpg?height=22&width=60&top_left_y=1089&top_left_x=961) | TWOŚ）LOS <br> 11－00 | － <br> ![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-09.jpg?height=22&width=62&top_left_y=1089&top_left_x=1356) | Polomanus <br> 99 | wh |
|  | DNADIVADSN | ——十一日＇Sold <br> 十一七十一 | Andwwwws <br> Nu，10 | DGFOÓO <br> No | TÔUÓH <br> 十一十方 | DECTO <br> SIM | 20850019 <br> 99.003 | w |
|  | DNDTOSDEDN | －0 <br> ＋ | DC．10．17．75 <br> —3N | DALO <br> SUM | （I）www．w．ck <br> － 01 | DCMW．5． <br> －1 | 20850085 <br> 998 | UNN |
|  | DNDTIVEDS | 200．00．00 <br> ![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-09.jpg?height=22&width=62&top_left_y=1269&top_left_x=565) | DYANA）AIDGINA <br> 189 | 3．15．1318 <br> －1－6 | （1）Lucis <br> ＋ | a． 00000 <br> ●●●レャ | 318301901 <br> 99 | D゙ |


＊The explanatory variable $\mathrm{S}_{12}$ was removed from this model as its coefficient was not found to be significant at 95％confidence level．
${ }^{* *} \sigma_{u}^{2}$ is the extra Poisson variance that addressing unmeasured or unobserved heterogeneity in the Full Bayes models．
posterior means of the model＇s parameters in the unstandardized de－ viance；
$P D$ ：The effective number of parameters（the posterior mean of the deviance minus the deviance of the posterior means or（ $P D=\bar{D}-\hat{D}$ ）） （Spiegelhalter et al．，2003）．

When comparing different models，the best model is the one with the minimum DIC value．It is difficult to determine what would con－ stitute an important difference in DIC（Spiegelhalter et al．，2003）． However，it is roughly assumed that a difference of more than 10 in the value of DIC might rule out the model with higher DIC．Differences between 5 and 10 are substantial．Also，it could be misleading to report the model with the lowest DIC if the difference is less than 5 and the models make very different inferences（El－Basyouny and Sayed，2009a）．

## 4．6．Model estimates

Various SPFs were developed in this study considering different conflict indicators（TTC，MTT，and DRAC），various critical thresholds， different combinations of the covariates（ $\mathbf{A}, \mathbf{Q}, \mathbf{S}_{\mathbf{1 2}}$ ，and $\mathbf{P}$ ），and different cases of the model intercept（with or without a random intercept）．A total of 28 models were developed．Table 3 shows the PLN models that account for the heterogeneity，and Table 4 shows PLN models that account for both the heterogeneity and the site effect（models with random intercept）．The mathematical format，the estimates and the Bayesian confidence interval of all explanatory variables，the goodness－ of－fit statistic（DIC），and the variances that address the heterogeneity and／or the variation among sites $\left(\sigma_{u}^{2}, \sigma_{s}^{2}\right)$ for all models are provided in these tables．For all models，the response（ $\boldsymbol{Y}$ ）denotes the number of rear－end conflicts per traffic signal cycle．Also，it is noteworthy to mention that the maximum queue length $(\mathbf{Q})$ was excluded from the developed models due to the strong correlation between A and Q，or in other words，the multicollinearity effect．In addition，considering that the data were collected sequentially in time，the assumption that the error in the developed models is independent might not be appropriate． Therefore，the serial correlation between the observed conflicts in consecutive signal cycles at each location was estimated using the Durbin－Waston（DW）statistic．The results showed that the serial cor－ relation had low insignificant values and should have little impact on the results．

Overall，all the developed models provided in Tables 3 and 4 show good fit and all the explanatory variables are statistically significant according the Bayesian confidence interval at the 95％level．All the covariate coefficients have logical signs．In other words，higher conflict occurrence is expected during the signal cycles that have bigger shock waves．On the other hand，the higher platoon ratio means that more vehicles arrive during the green time leading to a better arrival type and lower chances of conflict occurrence during the cycle．

During the development of each model with a specific conflict in－ dicator and at a specific threshold，the explanatory variables were added to the model one by one．It was noted that the DIC value，the heterogeneity effect（ $\sigma_{u}^{2}$ ），and the site variation effect（ $\sigma_{s}^{2}$ ）steadily de－ creased when adding more explanatory variables to the model．This is reasonable as the additional variables improved the model fit and ex－ plained some of the unmeasured heterogeneity and unmeasured var－ iation across sites．This emphasizes the important effect of the selected variables（i．e．A，P，and $\mathbf{S}_{\mathbf{1 2}}$ ）in providing a better prediction of the conflict occurrence beyond what can be expected from the exposure only（i．e．V）．

As shown in Table 4，the models with the random intercept statis－ tically have better fit than their counterparts in Table 3 with a singular intercept．Considering the site variation effect $\left(\sigma_{s}^{2}\right)$ decreases the DIC value significantly and improves the model fit．For example，the DIC

Table 4
PLN Models with Random Intercept (Incorporating Site Effect) for Different Conflict Indicators. (For interpretation of the references to colour in this table legend, the reader is referred to the web version of this article.)
| Model Format: $\ln (Y)=\beta_{0}+\beta_{1} \ln (V)+\beta_{2} A+\beta_{3} P+\beta_{4} S_{12}+u_{i}+w_{s(i)}$; where: <br> $u_{i} \sim N\left(0, \sigma_{u}{ }^{2}\right)$ <br> \& $w_{s(i)} \sim N\left(0, \sigma_{s}{ }^{2}\right)$ |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Conflict Indicator | Y: Number of rear-end conflicts per cycle where | $\boldsymbol{\beta}_{\mathbf{0}}$ Estimate (2.5\%, 97.5\% Bayesian C.I) | $\boldsymbol{\beta}_{\mathbf{1}}$ Estimate (2.5\%, 97.5\% Bayesian C.I) | $\boldsymbol{\beta}_{\mathbf{2}}$ Estimate (2.5\%, 97.5\% Bayesian C.I) | $\boldsymbol{\beta}_{\mathbf{3}}$ Estimate (2.5\%, 97.5\% Bayesian C.I) | $\boldsymbol{\beta}_{\mathbf{4}}$ Estimate (2.5\%, 97.5\% Bayesian C.I) | $\sigma_{u}{ }^{2}$ Estimate** (2.5\%, 97.5\% Bayesian C.I) | $\sigma_{s}{ }^{2}$ Estimate*** (2.5\%, 97.5\% Bayesian C.I) | DIC |
| TTC | $\mathbf{T T C} \leq \mathbf{1 . 0 ~ s e c}$ | -0.484 (-1.135, 0.116) | 1.749 (1.063, 2.457) | 0.315 (0.101, 0.529) | -0.861 (-1.374, -0.343) | 0.180 (0.054, 0.325) | 0.005 (0.0003, 0.037) | 0.560 (0.128, 1.795) | 463 |
|  | $\mathbf{T T C} \leq \mathbf{1 . 5 ~ s e c}$ | 0.376 (0.076, 0.669) | 1.449 (0.981, 1.929) | 0.268 (0.121, 0.411) | -0.789 (-1.156, -0.424) | 0.072 (0.007, 0.145) | 0.003 (0.0003, 0.015) | 0.111 (0.020, 0.376) | 643 |
|  | $\mathbf{T T C} \boldsymbol{\leq} \mathbf{2 . 0 ~ s e c}$ | 0.886 (0.757, 1.013) | 1.227 (0.883, 1.579) | 0.190 (0.078, 0.298) | -0.760 (-1.044, -0.482) | 0.083 (0.033, 0.137) | 0.002 (0.0003, 0.007) | 0.011 (0.0004, 0.057) | 767 |
|  | $\mathbf{T T C} \boldsymbol{\leq} \mathbf{2 . 5 ~ s e c}$ | 1.175 (1.065, 1.276) | 1.022 (0.730, 1.316) | 0.150 (0.052, 0.244) | -0.744 (-0.990, -0.498) | 0.052 (0.015, 0.093) | 0.002 (0.0003, 0.007) | 0.006 (0.0003, 0.031) | 835 |
|  | $\mathbf{T T C} \boldsymbol{\leq} \mathbf{3 . 0 ~ s e c}$ | 1.291 (1.188, 1.386) | 1.032 (0.758, 1.319) | 0.136 (0.042, 0.226) | -0.716 (-0.951, -0.486) | 0.041 (0.007, 0.078) | 0.001 (0.0003, 0.006) | 0.006 (0.0004, 0.028) | 857 |
| MTTC | $\mathbf{M T T C} \leq \mathbf{1 . 0 ~ s e c}$ | 0.728 (0.567, 0.894) | 1.355 (0.974, 1.757) | 0.189 (0.066, 0.308) | -0.805 (-1.110, -0.502) | ---* | 0.0023 (0.0003, 0.011) | 0.023 (0.0005, 0.105) | 748 |
|  | $\mathbf{M T T C} \leq \mathbf{1 . 5 ~ s e c}$ | 1.331 (1.182, 1.456) | 1.126 (0.856, 1.401) | 0.111 (0.019, 0.202) | -0.698 (-0.933, -0.466) | ---* | 0.002 (0.0003, 0.009) | 0.018 (0.001, 0.069) | 893 |
|  | $\mathbf{M T T C} \boldsymbol{\leq} \mathbf{2 . 0 ~ s e c}$ | 1.484 (1.313, 1.636) | 1.093 (0.840, 1.350) | 0.091 (0.005, 0.176) | -0.603 (-0.824, -0.385) | ---* | 0.002 (0.0002, 0.007) | 0.032 (0.005, 0.112) | 931 |
|  | MTTC $\leq \mathbf{2 . 5 ~ s e c}^{\mathbf{2}}$ | 1.574 (1.384, 1.742) | 1.062 (0.819, 1.307) | 0.097 (0.014, 0.178) | -0.483 (-0.698, -0.274) | ---* | 0.002 (0.0002, 0.006) | 0.041 (0.007, 0.140) | 966 |
|  | MTTC $\leq \mathbf{3 . 0 ~ s e c}$ | 1.594 (1.399, 1.773) | 1.079 (0.840, 1.322) | 0.096 (0.016, 0.177) | -0.429 (-0.641, -0.220) | ---* | 0.002 (0.0003, 0.0065) | 0.047 (0.010, 0.156) | 974 |
| DRAC | DCHWOSING | (1):1)(1)101 <br> - 11 | DCANDCO <br> - SO | Dickniedem <br> Pol | TWANDSOS <br> 11411 | Ploclattler <br> Lisow | Piolicie Mu <br> 09 | 긍ه…f <br> ÖN | W. |
|  | DTDTOLAMSTA | (AL) ÀDŞ) <br> -1-0 | A. Go <br> No. | - 0000000 <br> Lut | ——G. <br> -Huć | ÖCO PONC <br> Lut | IBOO 201301 <br> ![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-10.jpg?height=19&width=55&top_left_y=1084&top_left_x=1414) | ÖCHAMEGE <br> 0 | மு |
|  | DEDROLOM | TÓCIDGOOO <br> + L W | Disoning <br> Lug | - 5 - <br> Sயு | (Lings. <br> +1 as | PBLO <br> UG | a8888383 <br> ![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-10.jpg?height=21&width=55&top_left_y=1137&top_left_x=1414) | ÖMENDSIN <br> ![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-10.jpg?height=21&width=55&top_left_y=1137&top_left_x=1597) | $\frac{4}{\infty}$ |
|  | DCHWCTINS | D/90-18 <br> 0 | (B) SCAL) <br> -10 | TOSTOS <br> - IMP | TIDASALA。 <br> ●⑧00 | BID BIDS <br> -0 | (B) <br> 00 | ![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-10.jpg?height=24&width=144&top_left_y=1217&top_left_x=1553) <br> ![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-10.jpg?height=21&width=55&top_left_y=1192&top_left_x=1597) | ●ق |


*The explanatory variable $\mathrm{S}_{12}$ was removed from this model as its coefficient was not found to be significant at 95\% confidence level.
${ }^{* *} \sigma_{\boldsymbol{u}}^{2}$ is the extra Poisson variance that addressing unmeasured or unobserved heterogeneity in the Full Bayes models.
${ }^{* * *} \sigma_{s}^{2}$ is the additional variance component that addressing the variation among different sites.
value of the first model (TTC $\leq 1 \mathrm{~s}$ ) decreased from 521 in Table 3 to 463 in Table 4. This is expected because the conflict data in this study was measured at six different intersections, and the random intercept (i.e. the additional variance component $\left(\sigma_{s}^{2}\right)$ ) accounts for the possibility that different sites can have different conflict risks due to the variation of traffic, geometric, driving behavior, and environmental conditions across sites.

For the TTC models shown in Table 4, it can be noted that the random term $\left(\sigma_{s}^{2}\right)$ at lower TTC thresholds is particularly stronger than that at higher TTC thresholds. This is mainly attributed to the strong effect of the site specificity on the occurrence of high severe conflicts.

## 5. Conflict frequency and severity

### 5.1. Conflict frequency distribution

The temporal distribution of rear-end conflicts presented in (Essa and Sayed, 2018) showed that most of conflicts occur usually during the yellow time (the start of the red time), the red time (the area of the shock wave), and the end of the red time (the start of releasing the traffic queue at the beginning of the green time). This study additionally considers various conflict indicators with multiple thresholds to address the severity of the conflicts. The conflict events obtained from all locations were divided into 21 bins based on the relation of the recorded conflict time to the signal time. To account for different signal timings (especially green and red durations) between cycles and sites, the conflict time was represented as a percentage with regard to the signal timing (e.g. a conflict occurs at 15\% of the red time). Both green and red times were divided into 10 bins (i.e. 0-10\%, 10-20\%... 90-100\%). The yellow time, which is 4 s for all locations, contained only one bin. Using the conflict time (as a percentage) and the TTC value, temporal distributions of conflict frequency were developed at different severity levels. Fig. 4 shows the conflict distribution based on different TTC thresholds.

As shown in Fig. 4, the maximum conflict frequency usually exists at the start of the green time. This is mainly attributed to the variation in speeds at the start of the traffic queue release. The stopped flow starts to discharge gradually at low speed while other vehicles are arriving at higher speeds to the end of the queue. However, most of these conflicts have a low severity (higher values of TTC). If a higher severity level is considered, another conflict frequency peak can be noticed at the first third of the red light duration. These conflicts can be attributed to the dilemma zone where the traffic signal indication changes from green to yellow to red.

In addition, it is noteworthy to mention that the MTTC identified higher frequencies of rear-end conflicts than the TTC. This can be attributed to inclusion of vehicle accelerations in MTTC calculation which may result in recognizing more conflicts than TTC. Basically, some situations that are not possible to produce TTC conflicts can produce possible MTTC conflicts. For example, when the speed of the leading vehicle is higher than the following vehicle, it is not possible to have a TTC conflict. However, in case of MTTC, there is a chance of having a conflict if the acceleration of the following vehicle is higher than the leading vehicle (Ozbay et al., 2008).

### 5.2 Conflict severity distribution

In addition to the frequency distribution, the severity distribution of the identified conflicts was also investigated. The Severity Index (SI) (Saunier and Sayed, 2008) based on the minimum TTC values was calculated following the formula provided in (Saunier and Sayed, 2008). Only through lanes were selected for analysis (i.e. exclusive right-turn and left-turn lanes were excluded). Therefore, the SI formula can be expressed as follows:

![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-11.jpg?height=708&width=1098&top_left_y=189&top_left_x=482)
Fig. 4. Conflict Frequencies (Based on Different TTC Thresholds) versus Traffic Signal Timing.

$$
S I=\operatorname{Exp}\left(\frac{-T T C_{\min }^{2}}{2 \sigma^{2}}\right) ; \quad \forall(T T C)>0
$$

Where:

SI: severity index
$T T C_{\text {min }}$ : minimum value of Time to Collision
$\sigma$ : normalizing constant
The normalizing constant $\sigma$ was chosen to be equal to an average age user reaction time (1.50 s) (Saunier and Sayed, 2008). Figs. 5 and 6 show the minimum TTC distribution and the SI distribution, respectively.

As shown in Figs. 5 and 6, the highest conflict severity (the lowest TTC values) exists at the first third of the red light duration. Again, this is attributed to the dilemma zone where the traffic signal indication changes from green to yellow to red. Also, although the beginning of the green time has the highest conflict frequency, it shows less conflict severity than the yellow and the red times.

### 5.3. Extended time to collision measures

Minderhoud and Bovy (2001) introduced two traffic conflict measures based on extensions of the TTC: Time Exposed Time-to-collision (TET) and Time Integrated Time-to-collision (TIT). These measures can take the full course of vehicles over space and time into account and can give a more comprehensive picture of the safety level on a specific section of road during a specific period of time (Minderhoud and Bovy, 2001). TET and TIT were estimated for each signal cycle. Also, the effects of the shock wave area and the platoon ratio on the TET and the TIT values at the signal cycle level were investigated. The following sections provide more detail about TET and TIT.
5.3.1. Time exposed to collision (TET)

The TET measure expresses the exposition time to safety-critical approach situations (in seconds). It is a summation of all moments (over the considered time period) that a driver approaches a front vehicle with a TTC-value below the critical TTC threshold that discriminates between conflict and non-conflict events. Thus, the lower the TET value, the more safe the situation (on average over the considered time period) (Minderhoud and Bovy, 2001). Based on the aforementioned definition, the TET value was calculated for each signal cycle as per the

![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-11.jpg?height=706&width=1098&top_left_y=1830&top_left_x=482)
Fig. 5. Minimum TTC Values versus Traffic Signal Timing.

![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-12.jpg?height=706&width=1098&top_left_y=189&top_left_x=482)
Fig. 6. Severity Index Values (Based on TTC) versus Traffic Signal Timing.

following formula (Minderhoud and Bovy, 2001).

$$
\begin{aligned}
& T E T^{*}=\sum_{i=1}^{N} T E T_{i}^{*} \\
& T E T_{i}^{*}=\sum_{t=0}^{T} \delta_{i}(t) \cdot \tau_{s c} \\
& \delta_{i}(t)=\left\{\begin{array}{cc}
0 & \text { else } \\
1 & \forall \\
0 & 0<T T C_{i}(t)<T T C^{*}
\end{array}\right.
\end{aligned}
$$

Where:

$$
\begin{aligned}
T E T^{*}= & T E T(\text { in seconds }) \text { for the signal cycle at a specific critical } T \\
& T C \text { threshold* }^{*}
\end{aligned}
$$

$N=$ Total number of vehicles at the signal cycle

$$
\begin{aligned}
& \tau_{s c}=\text { time step }=\text { video frame }=\frac{1}{29.97} \text { second } \\
& t=\text { time instants }=(0,1,2, \ldots T)
\end{aligned}
$$

$T=$ Number of video frames per cycle $=\frac{\text { total cycle length in seconds }}{\tau_{s c}}$
$T T C_{i}(t)=$ instantaneous Time to Collision (from Eq. (1))
After estimating the TET value for each cycle at different TTC thresholds, the relationship between the cycle parameters and the TET was investigated. Fig. 7 shows the TET relationships with the shock wave and the platoon ratio.

Fig. 7 indicates that the TET value is positively correlated with the shock wave area at all TTC thresholds. This conforms to the positive sign of the shock wave coefficient in the SPFS provided in Tables 3 and 4. On the other hand, the TET value is inversely correlated with the platoon ratio at all TTC thresholds. This is also conforming to the negative sign of the platoon ratio coefficient in the developed SPFs.

### 5.3.2. Integrated time to collision (TIT)

The TIT measure expresses the integral of the time-to-collision profile of drivers to express the level of safety (in $\mathrm{s}^{2}$ ) (Minderhoud and Bovy, 2001). Unlike the TET, the TIT measure takes into account the TTC-values during the critical events. Basically, the TIT integrates the difference between the TTC value and the critical TTC threshold over all time periods that the TTC is below this threshold. Thus, the lower the TIT value, the more safe the situation (on average over the considered time period). The TIT value for each signal cycle was estimated as per the following formula (Minderhoud and Bovy, 2001).

$$
\begin{aligned}
& T I T^{*}=\sum_{i=1}^{N} T I T_{i}^{*} \\
& T I T_{i}^{*}=\sum_{t=0}^{T}\left[T T C^{*}-T T C_{i}(t)\right] \cdot \tau_{s c} ; \quad \forall 0<T T C_{i}(t)<T T C^{*}
\end{aligned}
$$

Where:

$$
\begin{aligned}
\text { TIT } *= & \text { TIT }\left(\text { in s }^{2}\right) \text { for the signal cycle at a specific critical TTC } \\
& \text { threshold* }^{*}
\end{aligned}
$$

$N=$ Total number of vehicles at the signal cycle

$$
\begin{aligned}
& \tau_{s c}=\text { time step }=\text { video frame }=\frac{1}{29.97} \text { second } \\
& t=\text { time instants }=(0,1,2, \ldots T)
\end{aligned}
$$

$$
\begin{aligned}
T & =\text { Number of video frames per cycle } \\
& =\frac{\text { total cycle length in seconds }}{\tau_{s c}}
\end{aligned}
$$

$T T C_{i}(t)=$ instantaneous Time to Collision (from Eq.(1))
After estimating the TIT value for each cycle at different TTC thresholds, the relationship between the cycle parameters and the TIT was investigated. Fig. 8 shows the TIT relationships with the shock wave and the platoon ratio.

Like the TET, the TIT measure is shown in Fig. 8 to be positively correlated with the shock wave area and inversely correlated with the platoon ratio at all TTC thresholds. Again, this conforms to the signs of the shock wave and the platoon ratio coefficients in the SPFs developed earlier. This also emphasizes the importance of including these cycle parameters in real-time safety evaluation of signalized intersections.

## 6. Summary and conclusions

The paper develops Full Bayes SPFs of signalized intersections at the cycle level using multiple traffic conflict indicators. Traffic video-data collected from six signalized intersections was used in the analysis. The developed SPFs relate various dynamic traffic parameters to the number of rear-end conflicts at the signal cycle. The measured traffic parameters at each cycle were: traffic volume, maximum queue length, shock wave area, shock wave backward-moving speed, and platoon ratio. The TTC, the MTTC, and the DRAC were used as traffic conflict indicators. The SPFs were developed using the FB approach to address the unobserved heterogeneity and the variation among different sites. Two kinds of FB models were developed: 1) PLN models that account for heterogeneity; and 2) PLN models with random intercept that

![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-13.jpg?height=1365&width=1533&top_left_y=185&top_left_x=267)
Fig. 7. Time Exposed to Collision (TET) at the Signal Cycle versus the Shock Wave Area and the Platoon Ratio.

account for heterogeneity and site effect.
Overall, the results showed that all the developed models have good fit and all the explanatory variables are statistically significant. Also, all the covariate coefficients have logical signs. In other words, the number of traffic conflicts is expected to increase during the signal cycles that have bigger shock waves, and lower platoon ratios. The deviance information criterion (DIC) was used as a statistical goodness-of-fit measure to compare different models. It was noted that the DIC value, the heterogeneity effect ( $\sigma_{u}^{2}$ ), and the site variation effect ( $\sigma_{s}^{2}$ ) steadily decreased when adding more explanatory variables to the model. This is reasonable as the additional variables improved the model fit and explained some of the unmeasured heterogeneity and unmeasured variation across sites. This emphasizes the important effect of the selected traffic variables in providing a better prediction of the conflict occurrence beyond what can be expected from the exposure only. Moreover, the models with the random intercept are statistically better than their counterparts with a singular intercept. This is expected because the conflict data in this study was measured at six different intersections, and the random intercept accounts for the possibility that different sites can have different conflict risks due to the variation of traffic, geometric, driving behavior, and environmental conditions across sites.

Furthermore, the conflict frequency and severity distributions along the signal cycle were investigated. The results indicated that the highest conflict frequency exists at the beginning of the green time due to the variation in speeds at the start of the traffic queue release. On the other hand, the highest conflict severity exists at the beginning of the red time due to the dilemma zone where the traffic signal indication changes from green to yellow to red.

Lastly, two extended time to collision measures (TET and TIT) were investigated at the cycle level. The results showed that both TET and TIT are positively correlated with the shock wave area and inversely correlated with the platoon ratio at all TTC thresholds. This conforms to the signs of the shock wave and the platoon ratio coefficients in the developed SPFS. This also emphasizes the importance of including these cycle parameters in real-time safety evaluation of signalized intersections.

Of the SPFs developed in this paper, it was difficult to recommend a specific model to estimate traffic conflicts at the cycle level. This is due to the lack of agreement in the literature on the critical threshold value, for each conflict indicator, that can be used to discriminate between conflict and non-conflict events. Hence, estimating conflicts at different thresholds using multiple SPFs is recommended when comparing safety levels of different signal design alternatives.

The results of this paper can have a potential implementation in real-time safety optimization of signalized intersection in the CVs environment. Future areas of research may include developing a methodology for such an optimization process considering the predicted frequency and severity of rear-end conflicts. Also, a future study is required to investigate the transferability of these models using different datasets. Finally, future research may consider developing realtime SPFs that consider other types of conflicts (e.g. crossing and lane

![](https://cdn.mathpix.com/cropped/13ec74cd-6454-4377-9323-58a9a9dad526-14.jpg?height=1365&width=1529&top_left_y=185&top_left_x=269)
Fig. 8. Integrated Time to Collision (TIT) at the Signal Cycle versus the Shock Wave Area and the Platoon Ratio.

change conflicts), a combination of different conflict indicators, the extended conflict measures (TET and TIT), and other road facilities (e.g. other types of intersections and freeways).

It should be noted that this study has some limitations which can be summarized as follows:

1) The sample size of the trajectory data is limited. Only six signalized intersections were considered.
2) The developed SPFs are applicable only to under-saturated signal cycles. Over-saturated cycles were not considered in the analysis and should be considered in future work.
3) Only rear-end conflicts at the intersection approaches were considered. Other types of traffic conflict within the intersection area such as right angle conflicts were not considered.
4) The effect of signal coordination on the results was not investigated.
5) In the FB analysis, non-informative prior distribution was assumed for each unknown parameter. The informative priors were recommended in the literature to improve the FB models goodness of fit (Yu and Abdel-Aty, 2013; Wang et al., 2018). Using informative priors to develop SPFs at the cycle level is recommended as a future area of research.

## Acknowledgement

The authors gratefully acknowledge the contributions of the Insurance Corporation of British Columbia (ICBC) for its financial and resource commitment to this project.

## References

Ahmed, M., Abdel-Aty, M., 2013. A data fusion framework for real-time risk assessment on freeways. Transp. Res. Part C: Emerg. Technol. 26, 203-213.
Amundsen, F., Hydén, C., 1977. Proceedings of First Workshop on Traffic Conflicts. Institute of Economics, Oslo.
Archer, J., 2005. Indicators for Traffic Safety Assessment and Prediction and Their Application in Micro-simulation Modelling: a Study of Urban and Suburban Intersections. s.l.: Doctoral Dissertation. Royal Institute of Technology.
Autey, J., Sayed, T., Zaki, M., 2012. Safety evaluation of right-turn smart channels using automated traffic conflict analysis. Accid. Anal. Prev. 45, 120-130.
Chatterjee, I., Davis, G., 2016. Analysis of rear-end events on congested freeways by using video-recorded shock waves. Transp. Res. Rec.: J. Transp. Res. Board 2583, 110-118.
Chin, Hoong-Chor, Quek, Ser-Tong, 1997. Measurement of traffic conflicts. Saf. Sci. 3 (26), 169-185.
Cooper, P.J., 1984. Experience With Traffic Conflicts in Canada With Emphasis on "Post Encroachment Time" Techniques. Springer, pp. 75-96 Berlin Heidelberg.
Cunto, Flávio, Saccomanno, Frank F., 2008. Calibration and validation of simulated vehicle safety performance at signalized intersections. Accid. Anal. Prev. 40 (3), 1171-1179.
El-Basyouny, K., Sayed, T., 2009a. Accident prediction models with random corridor parameters. Accid. Anal. Prev. 41 (5), 1118-1123.
El-Basyouny, K., Sayed, T., 2009b. Urban arterial accident prediction models with spatial effects. Transp. Res. Rec.: J. Transp. Res. Board 2102, 27-33.
El-Basyouny, K., Sayed, T., 2012. Measuring safety treatment effects using full Bayes nonlinear safety performance intervention functions. Accid. Anal. Prev. 45, 152-163.
El-Basyouny, K., Sayed, T., 2013. Safety performance functions using traffic conflicts. Saf. Sci. 51 (1), 160-164.
Essa, M., Sayed, T., 2015a. Simulated traffic conflicts: do they accurately represent fieldmeasured conflicts? Transp. Res. Rec.: J. Transp. Res. Board 2514, 48-57.

Essa, M., Sayed, T., 2015b. Transferability of calibrated microsimulation model parameters for safety assessment using simulated conflicts. Accid. Anal. Prev. 84, 41-53.
Essa, M., Sayed, T., 2016. A comparison between PARAMICS and VISSIM in estimating automated field-measured traffic conflicts at signalized intersections. J. Adv. Transp. 50, 897-917.
Essa, M., Sayed, T., 2018. Traffic conflict models to evaluate the safety of signalized intersections at the cycle level. Transp. Res. Part C: Emerg. Technol. 89, 289-302.
Feng, Y., Head, K., Khoshmagham, S., Zamanipour, M., 2015. A real-time adaptive signal control in a connected vehicle environment. Transp. Res. Part C: Emerg. Technol. 55, 460-473.
FHWA, 2003. Surrogate Safety Measures From Traffic Simulation Models. Federal Highway Administration Report FHWA-RD-03-050, McLean, VA.
Guler, S., Menendez, M., Meier, L., 2014. Using connected vehicle technology to improve the efficiency of intersections. Transp. Res. Part C: Emerg. Technol. 46, 121-131.
Guo, F., Wang, X., Abdel-Aty, M., 2010. Modeling signalized intersection safety with corridor-level spatial correlations. Accid. Anal. Prev. 42 (1), 84-92.
Hayward, J.C., 1972. Near-miss determination through use of a scale of danger. Highway Res. Rec Issue 384.
HCM, 2000. Highway Capacity Manual. Transportation Research Board, Washington, D.C.
Hirst, S., Graham, R., 1997. The format and presentation of collision warnings. Ergon. Saf. Intell. Driv. Interfaces 203-219.
Hogema, J., Janssen, W., 1996. Effect of Intelligent Cruise Control on Driving Behaviour. TNO Human Factors, Soesterberg, The Netherlands.
Hossain, M., Muromachi, Y., 2012. A Bayesian network based framework for real-time crash prediction on the basic freeway segments of urban expressways. Accid. Anal. Prev. 373-381.
HSM, 2010. Highway Safety Manual. American Association of State Highway and Transportation Officials, Washington, DC.
Hupfer, C., 1997. Computer Aided Image Processing to Modify Traffic Conflicts Technique, s.l. Transportation Department, University of Kaiserslautern, Germany.
Ismail, K., Sayed, T., Saunier, N., 2010. Automated analysis of pedestrian-vehicle conflicts: a context for before-and-after studies. Transp. Res. Rec.: J. Transp. Res. Board 2198, 52-64.
Ismail, K., Sayed, T., Saunier, N., 2011. Methodologies for aggregating indicators of traffic conflict. Transp. Res. Rec.: J. Transp. Res. Board 2237, 10-19.
Laureshyn, A., Ardö, H., Svensson, Å., Jonsson, T., 2009. Application of automated video analysis for behavioural studies: concept and experience. IET Intell. Transp. Syst. 3 (3), 345-357.
Lee, C., Hellinga, B., Saccomanno, F., 2003. Real-time crash prediction model for application to crash prevention in freeway traffic. Transp. Res. Rec.: J. Transp. Res. Board 1840, 67-77.
Lee, J., Park, B., Yun, I., 2013. Cumulative travel-time responsive real-time intersection control algorithm in the connected vehicle environment. J. Transp. Eng. 139 (10), 1020-1029.
Lee, J., Abdel-Aty, M., Cai, Q., 2017. Intersection crash prediction modeling with macrolevel data from various geographic units. Accid. Anal. Prev. 102, 213-226.
Lunn, D., Thomas, A., Best, N., Spiegelhalter, D., 2000. WinBUGS-a Bayesian modelling framework: concepts, structure, and extensibility. Stat. Comput. 10 (4), 325-337.
Lyon, C., Haq, A., Persaud, B., Kodama, S., 2005. Safety performance functions for signalized intersections in large urban areas: development and application to evaluation of left-turn priority treatment. Transp. Res. Rec.: J. Transp. Res. Board 1908, 165-171.
Machiani, S., Abbas, M., 2016. Safety surrogate histograms (SSH): a novel real-time safety assessment of dilemma zone related conflicts at signalized intersections. Accid. Anal. Prev. 96, 361-370.
McDowell, M., Wennell, J., Storr, P., Darzentas, J., 1983. Gap Acceptance and Traffic Conflict Simulation As a Measure of Risk. Technical Report, Supplementary Report 776. Transportation and Road Research Laboratory.
Miaou, S., Lord, D., 2003. Modeling traffic crash-flow relationships for intersections: dispersion parameter, functional form, and Bayes versus empirical Bayes methods. Transp. Res. Rec.: J. Transp. Res. Board 1840, 31-40.
Minderhoud, M.M., Bovy, P.H., 2001. Extended time-to-collision measures for road traffic safety assessment. Accid. Anal. Prev. 33 (1), 89-97.
Osama, A., Sayed, T., 2016. Evaluating the impact of bike network indicators on cyclist safety using macro-level collision prediction models. Accid. Anal. Prev. 97, 28-37.
Ozbay, K., Yang, H., Bartin, B., Mudigonda, S., 2008. Derivation and validation of new simulation-based surrogate safety measure. Transp. Res. Rec.: J. Transp. Res. Board 2083, 105-113.
Pande, A., Abdel-Aty, M., 2006. Comprehensive analysis of the relationship between real- time traffic surveillance data and rear-end crashes on freeways. Transp. Res. Rec.: J. Transp. Res. Board 1953, 31-40.
Persaud, B., Lan, B., Lyon, C., Bh, R., 2010. Comparison of empirical Bayes and full Bayes approaches for before-after road safety evaluations. Accid. Anal. Prev. 42 (1), 38-43.
Persaud, B., et al., 2012. Adoption of Highway Safety Manual Predictive Methodologies for Canadian Highways. s.l., s.n.Adoption of Highway Safety Manual Predictive Methodologies for Canadian Highways. s.l., s.n.
Poch, M., Mannering, F., 1996. Negative binomial analysis of intersection-accident frequencies. J. Transp. Eng. 122 (2), 105-113.
Sacchi, E., Sayed, T., 2016a. Conflict-based safety performance functions for predicting traffic collisions by type. Transp. Res. Rec.: J. Transp. Res. Board 2583, 50-55.
Sacchi, E., Sayed, T., 2016b. Bayesian estimation of conflict-based safety performance functions. J. Transp. Saf. Secur. 8 (3), 266-279.
Sacchi, E., Sayed, T., DeLeur, P., 2013. A comparison of collision-based and conflict-based safety evaluations: the case of right-turn smart channels. Accid. Anal. Prev. 59, 260-266.
Saunier, N., Sayed, T., 2008. Probabilistic framework for the automated analysis of the exposure to road collision. Transp. Res. Rec.: J. Transp. Res. Board 2083, 96-104.
Sawalha, Z., Sayed, T., 2001. Evaluating safety of urban arterial roadways. J. Transp. Eng. 127 (2), 151-158.
Sawalha, Z., Sayed, T., 2006a. Traffic accident modeling: some statistical issues. Can. J. Civ. Eng. 33 (9), 1115-1124.
Sawlaha, Z., Sayed, T., 2006b. Transferability of accident prediction models. Saf. Sci. 44 (3), 209-219.
Sayed, T., Zein, S., 1999. Traffic conflict standards for intersections. Transp. Plan. Technol. 22 (4), 309-323.
Shi, Q., Abdel-Aty, M., 2015. Big data applications in real-time traffic operation and safety monitoring and improvement on urban expressways. Transp. Res. Part C: Emerg. Technol. 58, 380-394.
Songchitruksa, P., Tarko, A.P., 2006. The extreme value theory approach to safety estimation. Accid. Anal. Prev. 38 (4), 811-822.
Spiegelhalter, D.J., Best, N.G., Carlin, B.P., Van Der Linde, A., 2002. Bayesian measures of model complexity and fit. J. R. Stat. Soc. Ser. B: Stat. Methodol. 64 (4), 583-639.
Spiegelhalter, D., Thomas, A., Best, N., Lunn, D., 2003. WinBUGS User Manual, s.l.: s.n.WinBUGS User Manual, s.l.: s.n.
Theofilatos, A., 2017. Incorporating real-time traffic and weather data to explore road accident likelihood and severity in urban arterials. J. Saf. Res. 61, 9-21.
U.S. Department of Transportation, 2015. ITS Research 2015-2019: Connected Vehicle (Connected Vehicles: Benefits, Roles, Outcomes). [Online]Available at:. [Accessed 12 May 2017]. https://www.its.dot.gov/research_areas/WhitePaper_connected_ vehicle.htm.
van der Horst, Hogema, J., 1993. Time-to-Collision and Collision Avoidance Systems. s.l., s.n.Time-to-Collision and Collision Avoidance Systems. s.l., s.n.
Wang, X., Abdel-Aty, M., 2008. Modeling left-turn crash occurrence at signalized intersections by conflicting patterns. Accid. Anal. Prev. 40 (1), 76-88.
Wang, X., Abdel-Aty, M., Brady, P., 2006. Crash estimation at signalized intersections: significant factors and temporal effect. Transp. Res. Rec.: J. Transp. Res. Board 1953, 10-20.
Wang, X., Yuan, J., Schultz, G., Fang, S., 2018. Investigating the safety impact of roadway network features of suburban arterials in Shanghai. Accid. Anal. Prev. 113, 137-148.
Wong, S.C., Sze, N.N., Li, Y.C., 2007. Contributory factors to traffic crashes at signalized intersections in Hong Kong. Accid. Anal. Prev. 39 (6), 1107-1113.
Wu, Y., Abdel-Aty, M., Lee, J., 2017b. Crash risk analysis during fog conditions using realtime traffic data. Accid. Anal. Prev. 114, 4-11.
Xu, C., Tarko, A., Wang, W., Liu, P., 2013. Predicting crash likelihood and severity on freeways with real-time loop detector data. Accid. Anal. Prev. 57, 30-39.
Yu, R., Abdel-Aty, M., 2013. Investigating different approaches to develop informative priors in hierarchical Bayesian safety performance functions. Accid. Anal. Prev. 56, 51-58.
Yuan, J., Abdel-Aty, M., 2018. Approach-level real-time crash risk analysis for signalized intersections. Accid. Anal. Prev. 119, 274-289.
Yuan, J., et al., 2018. Real-Time Crash Risk Analysis of Urban Arterials Incorporating Bluetooth, Weather, and Adaptive Signal Control Data. In: Proceedings of the Transportation Research Board 97th Annual Meeting Transportation Research Board. Washington, D.C..
Zhang, X., et al., 2014. Modeling the frequency of opposing left-turn conflicts at signalized intersections using generalized linear regression models. Traffic Inj. Prev. 15 (6), 645-651.
Zheng, Z., Ahn, S., Monsere, C., 2010. Impact of traffic oscillations on freeway crash occurrences. Accid. Anal. Prev. 42 (2), 626-636.


[^0]:    * Corresponding author.
    E-mail addresses: m.a.essa@civil.ubc.ca (M. Essa), tsayed@civil.ubc.ca (T. Sayed).

