# Comparing Safety at Signalized Intersections and Roundabouts Using Simulated Rear-End Conflicts 

Frank F. Saccomanno, Flávio Cunto, Giuseppe Guido, and Alessandro Vitale

The safety implications of adopting roundabouts in place of conventional signalized intersections have not been adequately assessed. A microscopic simulation model was used to compare the pattern of traffic conflicts at roundabouts with conflicts for signalized intersections. Three indicators of safety performance were defined: (a) time to collision (TTC), (b) deceleration rate to avoid the crash (DRAC), and (c) crash potential index (CPI). For each indicator, traffic conflict profiles were obtained in terms of number of vehicles in conflict and number of conflicts per vehicle for selected directional maneuvers. The exposure time to conflict for each maneuver and vehicle was also determined. Twelve combinations of geometric and traffic attributes (traffic scenarios) were simulated over a $\mathbf{1 5}-\mathbf{m i n}$ period. The results suggested that roundabouts yield reduced exposure times to rear-end conflicts compared with signalized intersections. On average, signalized intersections also reflected increased number of vehicles in conflict and percentage of vehicles in conflict compared with roundabouts. This relationship was found to be independent of input volumes and pavement surface condition and applied consistently to all safety indicator measures (TTC, DRAC, and CPI).

Roundabouts are receiving increasing attention as an effective means of traffic management and control. The safety implications of roundabouts compared with conventional signal controlled intersections are not well understood. Proponents of roundabouts have claimed that they yield safety dividends comparable to those potentially obtained from signalized intersections. Those in support of more roundabouts have argued that they can significantly improve safety by reducing the potential for rear-end crashes over conventional signalized intersections.

The scientific evidence in support of these arguments has been limited primarily to empirical observational studies for different jurisdictions and traffic conditions (1, 2). As noted by Wang et al. (3) and Davis (4), these types of studies fail to reflect the complex relationships that could lead to crashes at intersections and roundabouts for different traffic conditions. This failure has undercut the scientific basis of various inferences drawn from the literature regarding the safety benefits of roundabouts.

[^0]The purpose of this study was to apply microscopic simulation to compare the pattern of traffic conflicts that can lead to crashes at roundabouts to those obtained for signalized intersections. In a practical sense, this paper attempts to provide scientific evidence concerning safety implications of using roundabouts in place of signalized intersections on the basis of individual vehicle interactions in real time.

## INTERSECTION AND ROUNDABOUT GEOMETRIC AND TRAFFIC FEATURES

Figure 1 illustrates the roundabout design features used to assess safety implications. This roundabout connects traffic on two roads (major and minor approaches) intersecting at right angles. The traffic ring and entrance and exit ramps consist of two lanes (3.5-m width) with no special acceleration or deceleration lanes. Vehicles entering the roundabout from all entry points must yield to vehicles on the outer and inner rings before entering.

The intersection considered in this paper is a conventional, signalcontrolled intersection with minor and major roads intersecting at right angles. Signals are assumed to operate independent of timings at other adjacent intersections with semiactuated phases optimized using Synchro 7. Different cycle times (45-, 55-, and 65-s cycles) were determined for three levels of volume. For this analysis, right turns on red were prohibited, with permissive left turn maneuvers.

As summarized in Table 1, three volumes were assumed for both roundabout and intersection designs: high (2,500 vph), medium (2,000 vph) and low (1,500 vph). This volume was apportioned in terms of 10\% left turns and 10\% right turns. The directional split is one-third minor (N-S) and two-thirds major (E-W). The volumes used in this analysis are representative of volumes observed for roundabout and intersection traffic flows in a midsized Italian city.

## SAFETY PERFORMANCE INDICATORS FOR TRAFFIC CONFLICTS

Safety performance indicators represent real-time traffic interactions between any two vehicles in a traffic stream. When these indicators attain certain critical values, there is a potential for crashes to occur. Amundsen and Hydén defined traffic conflict as "an observable situation in which two or more vehicles approach each other in space and time to such an extent that there is a risk of collision if their movements remain unchanged" [as quoted in Sayed and Zein (5, p. 310)]. Logically, we would expect the higher the number of traffic conflicts and their increased level of severity are, the higher is the time individual vehicles are exposed to these conflicts will be, and the greater their potential for crashes will be.

![](https://cdn.mathpix.com/cropped/d51ec0a2-67a8-40b8-acdf-07d9ba882a7e-2.jpg?height=924&width=1195&top_left_y=211&top_left_x=464)
FIGURE 1 Roundabout geometric features.

Recent research has argued that traffic conflicts provide a more meaningful measure for lack of safety than the expected or historical number of crashes at a given location. Saunier and Sayed (6) noted that there are well-recognized availability and quality problems associated with collision data, and the use of collision records for safety analysis is reactive and a significant number of collisions must be recorded before action is taken. Furthermore, the focus on traffic conflicts permits consideration of the full spectrum of incidents that reflect high-risk situations, including those that result in crashes. The combined effect of crashes and near misses provides a more complete appreciation of factors that compromise safety at a given location.

As noted previously, the focus of this study is the reduced number of rear-end conflicts expected from the introduction of a roundabout compared with conventional intersection signalization. One of the concerns of signalization is that a reduction in angled crashes comes at the expense of an increase in the potential for rear-end crashes. This aspect was verified by Cunto and Saccomanno (7) in their study on the impact of signalization on the potential for crash occurrences using microscopic simulation. A similar result was obtained by Persaud et al. (1) using before and after observational analysis.

In this paper, safety performance is expressed in terms of three indicators: (a) time to collision (TTC) experienced by a vehicle as it progresses through the intersection or roundabout, (b) deceleration rate to avoid the crash (DRAC), and (c) crash potential index (CPI). Many current microscopic simulation packages provide the output needed to calculate TTC, DRAC, and CPI for short increments of time (0.1 s).

TTC can be defined as expected time for two vehicles to reach a common position on the road assuming their speed and trajectory remain the same and can be calculated using an expression of the form

$$
\operatorname{TTC}_{i, t}=\frac{\left(X_{i-1, t}-X_{i, t}\right)-L_{i-1, t}}{V_{i, t}-V_{i-1, t}} \quad V_{i, t}>V_{i-1, t}
$$

where

$$
\begin{aligned}
t= & \text { time interval, } \\
X= & \text { position of the vehicles ( } i=\text { following vehicle, } i-1=\text { lead } \\
& \text { vehicle), } \\
L= & \text { vehicle length, and } \\
V= & \text { velocity. }
\end{aligned}
$$

van der Horst (8) noted that the likelihood of crashes becomes a concern when TTC for a given vehicle is less than 1.5 s. This result

TABLE 1 Traffic Input Scenarios
| Volume Level | Volume (vph) |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- |
|  | Northbound (minor) | Southbound (minor) | Eastbound (major) | Westbound (major) | Total |
| Low | 250 | 250 | 500 | 500 | 1,500 |
| Medium | 334 | 334 | 666 | 666 | 2,000 |
| High | 417 | 417 | 833 | 833 | 2,500 |


was obtained from an experiment involving the application of a driver simulator to a closed course road.

The use of TTC can be limited in scope when identifying crash risk behavior, because it fails to reflect deceleration requirements for individual vehicles and vehicle pairs (lead and following vehicles). Hence, two vehicles approaching each other at high speeds at greater distances are treated in a similar fashion to slower-moving vehicles approaching each other at a shorter distance. We would expect that these scenarios have different crash risks and hence should be modeled differently.

A better indicator of safety performance was recognized by the Gettman and Head (9) and Archer (10), on the basis of earlier work by Darzentas et al. (11). This indicator intrinsically considered the role of speed differentials and decelerations in crash occurrence. The deceleration rate to avoid the crash or DRAC can be defined using time and space relationships applied to a given vehicle pair as the deceleration required by the following vehicle to come to a timely stop or attain a matching lead vehicle speed to avoid a rear-end crash. This can be expressed as follows:

$$
\operatorname{DRAC}_{i, t+1}=\frac{\left(V_{i, t}-V_{i-1, t}\right)^{2}}{2\left[\left(X_{i-1, t}-X_{i, t}\right)-L_{i-1, t}\right]}
$$

Hydén (12) noted that crash risk becomes problematic when values of DRAC exceed some predetermined braking comfort threshold. Archer (10) established a relationship between speed and required braking rate for two conflict levels: serious and nonserious (Figure 2). From this figure, a DRAC value exceeding $3.35 \mathrm{~m} / \mathrm{s}^{2}$ appears to reflect unsafe conditions.

Recently, researchers have argued that the conventional DRAC measure fails to accurately reflect traffic conflicts and identify potential crash situations, because it does not consider the available vehicle braking capability at specific points in time. For example, as a result of reduced friction, we would expect that a given value of DRAC under wet conditions is more critical to safety than the same value under dry conditions.

In their investigation of crash risk at intersections, Cunto and Saccomanno (7) proposed a CPI that accounts for the maximum available deceleration for an individual vehicle, on the basis of prevailing road vehicle and traffic conditions. This is referred to as maximum available deceleration rate (MADR). Because MADR takes into account differences in vehicle braking and road conditions, separate values need to be specified for each vehicle in the traffic

![](https://cdn.mathpix.com/cropped/d51ec0a2-67a8-40b8-acdf-07d9ba882a7e-3.jpg?height=565&width=838&top_left_y=1916&top_left_x=187)
FIGURE 2 Braking rates for different speeds (10).

stream. A CPI index can be obtained using an expression of the following form:

$$
\mathrm{CPI}_{i}=\frac{\sum_{t=t_{i}}^{t_{i}} P\left(\mathrm{DRAC}_{i, t}>\mathrm{MADR}_{i, t}\right) \times \Delta t \times b}{T_{i}}
$$

where

$$
\begin{aligned}
P= & \text { probability, } \\
\mathrm{CPI}_{i}= & \text { crash potential index for vehicle } i, \\
t i_{i}= & \text { initial time interval for vehicle } i, \\
t f_{i}= & \text { final time interval for vehicle } i, \\
\mathrm{DRAC}_{i, t}= & \text { deceleration rate to avoid the crash }\left(\mathrm{m} / \mathrm{s}^{2}\right) \text { for vehicle } \\
& i \text { in time } t, \\
\mathrm{MADR}_{i, t}= & \text { maximum available deceleration rate }\left(\mathrm{m} / \mathrm{s}^{2}\right) \text { for vehi- } \\
& \text { cle } i, \\
\Delta t= & \text { observation time interval }(\mathrm{s}), \\
T_{i}= & \text { total simulated time for vehicle } i(\mathrm{~s}), \text { and } \\
b= & \text { a binary state variable, } 1 \text { if } \mathrm{DRAC}_{i, t}>0 \text { and } 0 \text { other- } \\
& \text { wise. }
\end{aligned}
$$

This suggests that a conflict can occur only when the following vehicle is approaching the lead vehicle. The previously mentioned CPI expression is computationally sound because it reflects a probability that unsafe conditions present themselves to any given driver as he or she progresses along the road.

Using CPI, a conflict can be ascribed to each vehicle and observation interval when DRAC exceeds MADR. In this paper, unique MADR values were assigned to each vehicle assuming a truncated normal distribution for the parameters given in Table 2. The average value assumed for dry pavement was obtained from field tests for different cars with initial speeds from 80 to 100 km/h coming to a full stop. Upper and lower limits were estimated as ±50\% of the average DRAC for both wet and dry pavements. The average MADR for wet pavement was assumed to be 75\% of the MADR for dry pavement.

In the next section of the paper, we highlight potential traffic conflict situations for individual vehicles on the basis of the previously mentioned three indicators: TTC, DRAC, and CPI. A comparison of the results for roundabouts and intersections provided a sound measure of high crash risk behavior, both for individual vehicles and for the entire traffic stream on the basis of an assumed traffic scenario. In this way, the safety implications of roundabouts compared with signalized intersections can be assessed.

One of the important aspects of traffic conflict analysis is the duration of time any given vehicle is exposed to a conflict while undertaking a given maneuver. Exposure time to conflict was estimated for each vehicle in the traffic stream. As expected, the higher the level of conflict (i.e., the closer to a crash situation) is the shorter the exposure time will be. Drivers may be distracted for a brief moment and cross the threshold to conflict, but as the level of risk

TABLE 2 Assumed Truncated Normal Distribution Parameters for MADR
| MADR Distribution Parameter | Dry | Wet |
| :--- | :--- | :--- |
| Average $\left(\mathrm{m} / \mathrm{s}^{2}\right)$ | 8.45 | 6.34 |
| Standard deviation $\left(\mathrm{m} / \mathrm{s}^{2}\right)$ | 1.40 | 1.40 |
| Upper limit ( $\mathrm{m} / \mathrm{s}^{2}$ ) | 12.68 | 9.51 |
| Lower limit ( $\mathrm{m} / \mathrm{s}^{2}$ ) | 4.23 | 3.17 |


increases corrective responses are normally taken to avoid the crash. This clearly demonstrates why so many near misses fail to develop into actual crashes. It also underscores the importance of considering exposure time to conflict as opposed to only considering the number of vehicle in conflict.

Traffic conflicts are estimated for each vehicle in the traffic stream (input flow) for every 0.1 s of simulation time. For each safety indicator (TTC, DRAC, and CPI), traffic conflict profiles were obtained for each simulated scenario and vehicle maneuver in terms of three output measures: ( $a$ ) number of vehicles in conflict (at least once), $(b)$ percentage of vehicles in conflict, and $(c)$ exposure time to conflict.

## MICROSCOPIC SIMULATION ENVIRONMENT

A comparison of safety performance at roundabouts with conventional signalized intersections was carried out using microscopic simulation software VISSIM ${ }^{\text {® }}$ version 4.2, distributed by PTV America. Car-following situations in VISSIM are modeled through a psychophysical or action-point based algorithm. The basic assumption underlying VISSIM is that following vehicle drivers are able to ascertain whether they are approaching a lead vehicle by changes in its "apparent size" and by a perception of the relative speed through changes in its visual angle (13).

Simulations were performed using the default values of the model parameters (CC0 to CC9) for the VISSIM car-following algorithm. The parameter values for lane change and gap acceptance used in the simulation are summarized in Table 3.

Some preliminary analysis of vehicle tracking data at intersections suggested that VISSIM estimates of traffic conflicts were sensitive to two basic behavioral inputs: desired deceleration rate distribution and number of lead vehicles considered by the car-following driver. The authors suggested input values of $1.8 \mathrm{~m} / \mathrm{s}^{2}$ for desired deceleration and three observed vehicles ahead in car following. In this study an 18-min simulation time period was adopted, including 3 min warm-up time.

For roundabouts, five desired speed distributions were considered for each curvilinear and tangent segment. The desired speeds were obtained using the following expressions:

$$
V=\sqrt{127 \times R_{1 \min } \times(e+f)}
$$

and

$$
V=\sqrt{127 \times R_{1 \max } \times(e+f)}
$$

where

$$
\begin{aligned}
& V=\text { design speed }(\mathrm{km} / \mathrm{h}), \\
& e=\text { superelevation }(\mathrm{m} / \mathrm{m}), \\
& f=\text { side friction factor, and }
\end{aligned}
$$

TABLE 3 Simulations Parameters
|  | Dry | Wet |
| :--- | :--- | :--- |
| Lane change |  |  |
| Maximum acceptable deceleration ( $\mathrm{m} / \mathrm{s}^{2}$ ) | 4.50 | 4.00 |
| Minimum acceptable deceleration $\left(\mathrm{m} / \mathrm{s}^{2}\right)$ | 1.00 | 0.20 |
| Gap acceptance |  |  |
| Minimum gap time (s) | 2.60 | 2.60 |
| Minimum headway (m) | 5.00 | 5.00 |
| Maximum speed (km/h) | 35.44 | 31.27 |


TABLE 4 Speed Distribution Parameters
|  | Dry | Wet |
| :--- | :--- | :--- |
| Average of ring speed ${ }^{a}$ (km/h) | 24.33 | 20.36 |
| Standard deviation (km/h) | 6.00 | 6.00 |
| Crossing grade (\%) | 0.00 | 0.00 |
| Friction coefficient | 0.20 | 0.14 |


${ }^{a}$ Considering two lanes on ring.
$R_{1 \text { min }}$ and $R_{1 \text { max }}=$ minimum and maximum value of entrance radii.
To simulate the wet pavement conditions, a 30\% reduction in the coefficient of friction was applied. Table 4 summarizes the speed distribution parameters used for dry and wet pavement conditions. For the gap acceptance algorithm at the roundabout in VISSIM two cases were considered:

1. If the gap is greater than or equal to some critical value $(T c)$, an entrance speed greater than zero is assumed (gap accepted). The entrance vehicle arrives at the stop or yield line with an initial speed $V_{0}(14)$.
2. If the gap is less than $T c$ an initial speed of zero was assumed (gap not accepted). The vehicle comes to a full stop before entering the roundabout and an acceptable gap appears to accelerate into the outer circle (15).

A vehicle is assumed to enter the simulation at a point 100 m upstream of the roundabout or intersection and to exit from the simulation at a point 100 m downstream.

## RESULTS AND CONCLUSIONS

The results of the simulation were reported in terms of 12 combinations of geometric and traffic attributes or test scenarios. Table 5 provides a summary of traffic conflicts for TTC, DRAC, and CPI in terms of the number of vehicles in conflict, their percentages and their average exposure time. For CPI its 85th percentile values (CPI85th) also have been reported. Table 6 summarizes the change in the percentage of vehicles in conflict and CPI85th for different safety measures for roundabouts and signalized intersections.

On average, signalized intersections yield an increase in the number of vehicles in conflict from 60\% to 100\%, depending on volume and pavement surface condition. This finding is independent of how we measure safety performance (TTC, DRAC, CPI). The increase in number of vehicles in rear-end conflicts appears to be especially pronounced for dry pavement conditions. This result is intuitively reasonable because we would expect vehicles on dry pavement to be approaching the intersection stop line at a higher approach speed, increasing the crash risk.

Tables 7, 8, and 9 summarize the three-way analysis of variance (ANOVA) results with respect to the percentage vehicles in conflict, time exposure to conflict and CPI85th percentile, respectively. The ANOVA considers three main effects (geometry, weather, and volume) and three second-order interactions, as per categories given in Table 5. The significance of these relationships is established at the 5\% level.

Several important findings and conclusions can be drawn from this analysis:

TABLE 5 Simulated Test Scenarios
| Test | Geometry | Pavement Surface Condition | Vol. (vph) | \#Veh. | TTC |  |  | DRAC |  |  | CPI |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  | No. of Veh. in Conf. | \% of Veh. in Conf. | Avg. Exposure (veh/s) | No. of Veh. in Conf. | \% of Veh. in Conf. | Avg. Exposure (veh/s) | No. of Veh. in Conf. | \% of Veh. in Conf. | Avg. Exposure (veh/s) | CPI85th |
| 1 | Roundabout | Dry | 1,500 | 392 | 11 | 2.72 | 0.50 | 3 | 0.73 | 0.24 | 1 | 0.27 | 0.15 | $1.06 \mathrm{E}-09$ |
| 2 | Roundabout | Dry | 2,000 | 522 | 18 | 3.44 | 0.55 | 4 | 0.80 | 0.29 | 3 | 0.52 | 0.14 | $1.72 \mathrm{E}-09$ |
| 3 | Roundabout | Dry | 2,500 | 657 | 32 | 4.81 | 0.56 | 7 | 1.04 | 0.32 | 4 | 0.59 | 0.18 | $3.83 \mathrm{E}-09$ |
| 4 | Roundabout | Wet | 1,500 | 395 | 13 | 3.41 | 0.59 | 4 | 1.01 | 0.36 | 3 | 0.76 | 0.24 | $3.36 \mathrm{E}-06$ |
| 5 | Roundabout | Wet | 2,000 | 527 | 30 | 5.73 | 0.60 | 8 | 1.45 | 0.37 | 6 | 1.18 | 0.23 | $5.14 \mathrm{E}-06$ |
| 6 | Roundabout | Wet | 2,500 | 664 | 57 | 8.59 | 0.59 | 14 | 2.08 | 0.36 | 10 | 1.55 | 0.23 | $7.24 \mathrm{E}-06$ |
| 7 | Intersection | Dry | 1,500 | 386 | 27 | 7.03 | 0.60 | 4 | 1.02 | 0.40 | 3 | 0.66 | 0.25 | $1.69 \mathrm{E}-08$ |
| 8 | Intersection | Dry | 2,000 | 519 | 51 | 9.83 | 0.60 | 10 | 1.89 | 0.40 | 7 | 1.44 | 0.27 | $1.91 \mathrm{E}-08$ |
| 9 | Intersection | Dry | 2,500 | 653 | 101 | 15.45 | 0.55 | 15 | 2.25 | 0.42 | 11 | 1.62 | 0.22 | $1.28 \mathrm{E}-08$ |
| 10 | Intersection | Wet | 1,500 | 393 | 28 | 7.01 | 0.58 | 5 | 1.29 | 0.34 | 4 | 0.97 | 0.19 | $1.39 \mathrm{E}-05$ |
| 11 | Intersection | Wet | 2,000 | 525 | 50 | 9.60 | 0.57 | 10 | 1.90 | 0.41 | 8 | 1.47 | 0.22 | $1.52 \mathrm{E}-05$ |
| 12 | Intersection | Wet | 2,500 | 656 | 99 | 15.16 | 0.50 | 18 | 2.77 | 0.40 | 13 | 2.02 | 0.20 | $1.05 \mathrm{E}-05$ |


1. For rear-end conflicts, the percentage of vehicles in conflict increases significantly for signalized intersection compared with roundabouts. This finding confirms the primary assertion that introducing a roundabout lowers the potential for rear-end conflicts compared with signalization at conventional intersections.

TABLE 6 Change in the Percentage of Vehicles in Conflict and CPI85th-Roundabouts Versus Signalized Intersections
|  | TTC | DRAC | CPI | CPI85th |
| :--- | :--- | :--- | :--- | :--- |
| Dry |  |  |  |  |
| Low | 0.89 | 0.33 | 0.83 | 1.76 |
| Medium | 0.96 | 0.80 | 0.93 | 1.67 |
| High | 1.05 | 0.73 | 0.93 | 1.08 |
| Wet |  |  |  |  |
| Low | 0.69 | 0.24 | 0.25 | 1.22 |
| Medium | 0.50 | 0.27 | 0.22 | 0.99 |
| High | 0.55 | 0.29 | 0.26 | 0.37 |


TABLE 7 Three-Way ANOVA for Percentage Vehicles in Conflict
| Source | Type III Sum of Squares | df | Mean Square | $F$ | Sig. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Geometry | 13.71 | 1 | 13.71 | 70.70 | 0.00 |
| Weather | 10.23 | 1 | 10.23 | 52.77 | 0.00 |
| Volume | 18.72 | 2 | 9.36 | 48.27 | 0.00 |
| Geometry * weather | 2.27 | 1 | 2.27 | 11.71 | 0.00 |
| Geometry * volume | 1.59 | 2 | 0.79 | 4.09 | 0.02 |
| Weather * volume | 0.99 | 2 | 0.50 | 2.56 | 0.08 |
| Geometry * weather * volume | 0.45 | 2 | 0.22 | 1.16 | 0.32 |


2. An increase in volume results in an increase in the percentage of vehicles in conflict. This finding applies to both roundabouts and signalized intersections.
3. As expected, adverse weather conditions (wet pavement) have a negative effect on the number of vehicles in conflicts, a result that appears to be especially pronounced for roundabouts.
4. Conflict exposure time is affected by geometry. Roundabouts produce significantly lower exposure time to conflict compared with intersections. Exposure time is affected by the second order interaction between geometry and volume. All other interaction terms were found to be insignificant.
5. Conflict exposure time is not affected by pavement surface condition (wet and dry) or volume, either alone or in combination.
6. The 85th percentile CPI measure reflects a more sensitive weather-related effect on conflicts, because it explicitly accounts for restricted braking capabilities under adverse pavement surface conditions. We note that for intersections, the CPI85th percentile initially increases with volume to an upper threshold value and then begins to drop as the volume approaches capacity. This finding appears to be reasonable because we would expect that at higher volumes driver freedom of movement becomes more restrictive.

TABLE 8 Three-Way ANOVA for Time Exposure to Conflict
| Source | Type III Sum of Squares | df | Mean Square | $F$ | Sig. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Geometry | 0.04 | 1 | 0.04 | 12.41 | . 00 |
| Weather | 0.01 | 1 | 0.01 | 2.95 | . 09 |
| Volume | 0.00 | 2 | 0.00 | . 36 | . 70 |
| Geometry * weather | 0.15 | 1 | 0.15 | 47.23 | . 00 |
| Geometry * volume | 0.02 | 2 | 0.01 | 3.48 | . 03 |
| Weather * volume | 0.00 | 2 | 0.00 | . 00 | 1.00 |
| Geometry * weather * volume | 0.01 | 2 | 0.01 | 1.84 | 0.16 |


TABLE 9 Three-Way ANOVA for CPI85th
| Source | Type III Sum of Squares (E+11) | df | Mean Square (E+11) | $F$ | Sig. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Geometry | 0.71 | 1 | 0.71 | 410.90 | 0.00 |
| Weather | 3.82 | 1 | 3.82 | 2199.38 | 0.00 |
| Volume | 0.02 | 2 | 0.10 | 5.71 | 0.00 |
| Geometry * weather | 0.71 | 1 | 0.71 | 408.01 | 0.00 |
| Geometry * volume | 0.12 | 2 | 0.06 | 35.63 | 0.00 |
| Weather * volume | 0.02 | 2 | 0.01 | 5.69 | 0.00 |
| Geometry * weather * volume | 0.12 | 2 | 0.06 | 60.84 | 0.00 |


Roundabouts have the potential for traffic management with minimum disruption to traffic flow compared with conventional intersections. The safety implications of adopting roundabouts have not been adequately addressed in the literature, and these implications can be significant in terms of cost and personal injuries. This paper confirmed that roundabouts result in a reduced exposure to rear-end traffic compared with signalized traffic control at intersections. This finding is valid for different traffic scenarios such as volume and environmental conditions.

## REFERENCES

1. Persaud, B. N., R. A. Retting, P. Garder, and D. Lord. Safety Effect of Roundabout Conversions in the United States: Empirical Bayes Observational Before-After Study. In Transportation Research Record: Journal of the Transportation Research Board, No. 1751, TRB, National Research Council, Washington, D.C., 2001, pp. 1-8.
2. Nambisan, S. S., and V. Parimi. A Comparative Evaluation of Safety Performance of Roundabouts and Traditional Intersection Controls. ITE Journal, Vol. 77, No. 3, 2007, pp. 18-25.
3. Wang, Y., H. Ieda, and F. Mannering. Estimating Rear-End Accident Probabilities at Signalized Intersections: Occurrence-Mechanism Approach. Journal of Transportation Engineering, Vol. 129, No. 4, 2003, pp. 377-384.
4. Davis, G. A. Possible Aggregation Biases in Road Safety Research and a Mechanism Approach to Accident Modeling. Accident Analysis and Prevention, Vol. 36, 2004, pp. 1119-1127.
5. Sayed, T., and S. Zein. Traffic Conflict Standards for Intersections. Transportation Planning and Technology, Vol. 22, 1999, pp 309-323.
6. Saunier, N., and T. Sayed. Automated Analysis of Road Safety with Video Data. Presented at 86th Annual Meeting of the Transportation Research Board, Washington, D.C., 2007.
7. Cunto, F., and F. Saccomanno. Micro-Level Traffic Simulation Method for Assessing Crash Potential at Intersections. Presented at 86th Annual Meeting of the Transportation Research Board, Washington, D.C., 2007.
8. van der Horst, A. R. A. Time-to-Collision as a Cue for Decision-Making in Braking. In Vision in Vehicles (I. D. Brown, C. M. Haselgrave, I. Moorhead, and S. Taylor, eds.), Vol. 3, 1991, pp. 19-26.
9. Gettman, D., and L. Head. Surrogate Safety Measures from Traffic Simulation Models: Final Report. Publication FHWA-RD-03-050. FHWA, U.S. Office of Safety Research and Development, 2003.
10. Archer, J. Methods for the Assessment and Prediction of Traffic Safety at Urban Intersection and Their Application in Micro-Simulation Modelling. PhD dissertation, Department of Infrastructure, Royal Institute of Technology, Stockholm, Sweden, 2005.
11. Darzentas, J., D. F. Cooper, P. A. Storr, and M. R. C. McDowell. Simulation of Road Traffic Conflicts at T-junctions. Simulation, 1980, pp. 155-164.
12. Hydén, C. The Development of a Method for Traffic Safety Evaluation: The Swedish Traffic Conflict Technique. Bulletin 70. Department of Planning and Engineering, Lund University, Lund, Sweden, 1987.
13. Brackstone, M., and M. McDonald. Car-Following: A Historical Review. In Transportation Research Part F: Traffic Psychology and Behavior, Vol. 2. TRB, National Research Council, Washington, D.C., 1999, pp. 181-196.
14. Astarita, V., G. Guido, and A. Vitale. Verifica Della Applicabilità Di Rotatorie Di Forma Non Circolare Tramite Simulazione Microscopica Del Deflusso Veicolare. In Manutenzione e Adeguamento Delle Strade Esistenti-Sessione: Adeguamento. Centro Editoriale e Librario, Università della Calabria, Rende, Italy, 2006, pp. 271-285.
15. Guido, G., and A. Vitale. Analysis of Users' Behaviour in Roundabout under Car-Following Conditions. Urban Transport 2006 (12-14 luglio, Praga), Transactions on the Built Environment, Vol. 89. WIT Press, Southampton, United Kingdom, 2006, pp. 317-326.

The Roundabouts Task Force sponsored publication of this paper.


[^0]:    F. F. Saccomanno and F. Cunto, Department of Civil Engineering, University of Waterloo, 200 University Street West, Waterloo, Ontario N2L 6P6, Canada. G. Guido and A. Vitale, Dipartimento di Pianificazione Territoriale Università della Calabria, Via P. Bucci, cubo 46/B 87030 Arcavacata di Rende (CS), Italy. Corresponding author: F. Cunto, fjccunto@uwaterloo.ca.

    Transportation Research Record: Journal of the Transportation Research Board, No. 2078, Transportation Research Board of the National Academies, Washington, D.C., 2008, pp. 90-95.
    DOI: 10.3141/2078-12

