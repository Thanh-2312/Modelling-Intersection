# New time-based surrogate safety measure to assess crash risk in car-following scenarios 

H. Behbahani ${ }^{\mathbf{1}}$, N. Nadimi ${ }^{\boldsymbol{*} \mathbf{1}}$ and S.S. Naseralavi ${ }^{\mathbf{2}}$

Surrogate safety measures have been employed as road safety indicators for decades; numerous measures have been developed to replicate the volume and relative severity of adverse incidents in various regions. "Time-to-collision" (TTC) is one of the most frequently used time-based surrogate safety measures. In the current study, a new application of "TTC" has been developed for the enhancement of road safety assessment. Values for both the rate of "TTC" variation and the level of hazard associated with "TTC" have been amalgamated as an approximate safety indicator. A microsimulation model is used to validate the newly developed measure with respect to the assessment of the level of safety associated with a freeway (Interstate-80). Results suggest that the developed measure more accurately considers driver car-following behavior; consequently, detection of potentially hazardous collisions is significantly improved. The proposed technique for collision prediction is shown to provide a more accurate level of risk assessment with respect to car-following scenarios; thus, it may present an opportunity for increasing the precision associated with in-vehicle collision avoidance warning systems (IVCAWS).

Keywords: Collision avoidance, Safety, Surrogate measures, Time-to-collision

## Introduction

Surrogate safety measures are beneficial tools for road safety assessment in the absence of actual crash data (Barcelo, Montero, Perarnau, and Torday 2003; Archer 2005; Gettman and Head 2003; Cunto 2008; Gousios and Garber 2009; Sobhani, Young, Sarvi, and Bahrololoom 2013; Young, Sobhani, Lenne, and Sarvi 2014). These measures have been applied in intelligent transportation system operations, including in-vehicle collision avoidance warning systems (IVCAWS), as a preemptive strategy for the reduction of crash risks associated with road networks (Van der Horst and Hogema 1993). Several road safety indicators have been developed for uncovering the probability and relative severity of traffic conflicts. One of these indicators is "time-to-collision" (TTC), a well-developed and frequently employed time-based measure. Time-to-collision was first introduced by Hayward (1971) and defined as "the time remaining to a collision if the course and speed of colliding objects remain constant during a car-following scenario." In recent years, other definitions have been propounded for TTC, which

[^0]consider collisions occurring at varying angles and trajectories (Van der Horst 1990; Minderhoud and Bovy 2001; Ozbay, Yang, Bartin, and Mudigond 2008; Saffarzadeh, Nadimi, Nasealavi, and Mamdoohi 2013; Sobhani, Young, Sarvi, and Bahrololoom 2013). Regardless of the employed method of TTC calculation, in order to appropriately and accurately indicate the potential severity of a collision occurring within specific conditions, a threshold value must be selected to distinguish between categorically safe and unsafe vehicle encounters with respect to a specific time or space. This is also true when TTC is employed as an early warning strategy within IVCAWSs. Minderhoud and Bovy (2001) have previously introduced extended TTC measures for the assessment of road traffic safety pertaining to a specific time interval. These proximal safety indicators have been shown to enhance crash risk estimation capabilities in the absence of actual crash data. However, to date, no time-based surrogate safety measures capable of concurrently considering both TTC severity and TTC variation have been presented. Accordingly, the current study sought to develop a novel indicator, in order to append a measure of TTC variation to TTC in its current format. It was considered that successful development would lead to a measure that would effectively provide increased levels of detail pertaining to drivers' risky behavior during carfollowing scenarios.
![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-02.jpg?height=597&width=799&top_left_y=176&top_left_x=208)


1Schematic outlining post-encroachment time (PET) on a highway


## Surrogate safety measures for rear-end collisions

Several measures have been introduced for the detection of rear-end vehicle collisions, the most frequently employed of which are TTC, post-encroachment time (PET), deceleration rate to avoid collision (DRAC), and proportion of stopping distance (PSD). These are now outlined.

## Time-to-collision

Various improvements on TTC notion have been proposed, among which are the introduction of modified TTC (MTTC) (Ozbay, Yang, Bartin, and Mudigond 2008), a generalized formulation of TTC (Saffarzadeh, Nadimi, Nasealavi, and Mamdoohi 2013), development of an inverse TTC (Kiefer, Leblanc, and Flannagan 2005), and TTC with respect to a moving line section and a point (Laureshyn et al. 2010). For the purpose of simplicity, the current study has employed the conventional definition of TTC for rear-end collisions throughout as follows

$$
\operatorname{TTC}_{\mathrm{F}}(t)=\frac{X_{\mathrm{L}}(t)-X_{\mathrm{F}}(t)-l_{\mathrm{L}}}{\dot{X}_{\mathrm{F}}(t)-\dot{X}_{\mathrm{L}}(t)} \quad \forall \dot{X}_{\mathrm{F}}(t)>\dot{X}_{\mathrm{L}}(t)
$$

where $X$ represents the position of front of vehicles at time $t, \dot{X}$ represents the derivative of $X$ with respect to time or velocity, $l_{\mathrm{L}}$ is the lead vehicle length, and L and F are indices referring to the lead and following vehicles in a carfollowing situation.

## Post-encroachment time

Post-encroachment time (PET) is the time difference between lead vehicle entry to a collision point and the arrival of a following vehicle to the same point (Cooper 1983) (Fig. 1). In this figure, the leading vehicle arrives to the red line at $t_{1}$ but the following vehicle reaches at $t_{2}$, therefore $\mathrm{PET}=t_{2}-t_{1}$. A decreasing PET typically results in an increasing likelihood of collision (Vogel 2003).

## Encroachment time

This is the time that the leading vehicle occupies the conflict area. This indicator is suitable for sideswipe conflicts in intersections (Craveiro 2008).

## Initially attempted post-encroachment time

Initially attempted post-encroachment time (IAPT) is similar to PET, however, it applies the projected arrival time for the following vehicle to conflict area (Craveiro 2008).

## Gap time

Gap time (GT) is the projected time arrival of the following vehicle to the conflict area minus the time required for the leading vehicle to clear the conflict area (Craveiro 2008).

## Deceleration rate to avoid collision

Deceleration rate to avoid collision is the minimum rate at which a vehicle must decelerate to avoid a probable collision and is considered an appropriate measure for the detection of dangerous driving maneuvers. For vehicles traveling on the same path, DRAC is quantified as follows (Archer 2005)

$$
\text { DRAC }_{\mathrm{i}}=\frac{\left(\dot{X}_{\mathrm{F}}(t)-\dot{X}_{\mathrm{L}}(\mathrm{t})\right)^{2}}{2\left[\left(X_{\mathrm{L}}(t)-X_{\mathrm{F}}(\mathrm{t})\right)-l_{\mathrm{L}}\right]}
$$

## Proportion of stopping distance

Proportion of stopping distance is defined as the ratio of available distance between two vehicles and distance required for collision avoidance with respect to the maximum available deceleration rate (MADR) (Brian, Allen, Shin, and Cooper 1978)

$$
\operatorname{PSD}=\frac{\left(X_{\mathrm{L}}(t)-X_{\mathrm{F}}(\mathrm{t})\right)-l_{\mathrm{L}}}{\left(\dot{X}_{\mathrm{F}}^{2}(t) / 2 \mathrm{MADR}\right)}
$$

## Extended TTC measures

In order to assess road traffic safety in a time period, Minderhoud and Bovy (2001) previously introduced two extended indicators, namely, "time exposed time-tocollision" (TET) ("Time exposed TTC" section) and "time integrated time-to-collision" (TIT) ("Time integrated TTC" section). Both indicators are derived via the use of all vehicle trajectories and TTC profiles, over a specified section length and during a specified period. A typical TTC profile pertaining to a hypothetical vehicle is presented in Fig. 2.

## Time exposed TTC

Time exposed TTC is the duration of exposure to safetycritical TTC values (TTC*) with respect to a specified time period; this is the sum of all instances during which a secondary vehicle is following the leading vehicle with $0<\mathrm{TTC}<\mathrm{TTC}^{*}$. For vehicle $i$, it is assumed that measured TTC values at time $t$ do not fluctuate during small time-steps $\tau$ (e.g. $0 \cdot 1 \mathrm{~s}$ ). During time period $H$, $T=[H / \tau]$; thus, TET for vehicle $i$ is calculated as follows (Minderhoud and Bovy 2001). $\delta_{\mathrm{i}}(t)$ is 1 if $0 \leq \mathrm{TTC}_{\mathrm{i}}(t) \leq$ TTC* and 0 if $\mathrm{TTC}_{\mathrm{i}}>\mathrm{TTC}^{*}$
![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-03.jpg?height=443&width=1169&top_left_y=163&top_left_x=490)

2 Typical time-to-collision (TTC) profile for a hypothetical following vehicle

$$
\mathrm{TET}_{\mathrm{i}}=\sum_{\mathrm{t}=1}^{\mathrm{T}} \delta_{\mathrm{i}}(t) \cdot \tau
$$

where $\delta$ is a switching variable with a value of 1 during which the TTC value lies between 0 and TTC*, and 0 in all other cases. Time exposed time-to-collision for $N$ vehicles, passing a road section during time interval $H$ is equal to

$$
\mathrm{TET}_{\text {total }}=\sum_{\mathrm{i}=1}^{\mathrm{N}} \mathrm{TET}_{\mathrm{i}}
$$

The mean of ${ }_{\text {TET }}$ during $H$ seconds for $N$ vehicles is calculated as (6)

$$
\overline{\mathrm{TET}}=\frac{\mathrm{TET}_{\text {total }}}{N \cdot H}
$$

## Time integrated TTC

Time exposed time-to-collision does not take into consideration TTC values below the critical threshold; accordingly, TIT has been introduced as an alternative measure. Time integrated TTC uses the integral of the TTC profile, in order that values of TTC below TTC* are also considered in the calculation procedure as follows (Minderhoud and Bovy 2001)

$$
\mathrm{TIT}_{\mathrm{i}}=\sum_{\mathrm{t}=1}^{\mathrm{T}}\left[\mathrm{TTC}^{*}-\mathrm{TTC}_{\mathrm{i}}(t)\right] \cdot \tau \quad \forall 0 \leq \mathrm{TTC}_{\mathrm{i}}(t) \leq \mathrm{TTC}^{*}
$$

Thus, TIT for $N$ vehicles passing a road section is given by the following equation

$$
\mathrm{TIT}_{\text {total }}=\sum_{\mathrm{i}=1}^{\mathrm{N}} \mathrm{TIT}_{\mathrm{i}}
$$

Accordingly, the mean TIT during $H$ seconds for $N$ vehicles is given by the following equation

$$
\overline{\mathrm{TIT}}=\frac{\mathrm{TIT}_{\text {total }}}{N \cdot H \cdot \mathrm{TTC}^{*}}
$$

The calculation procedures for TET and TIT using equations (4)-(9) are presented in Fig. 3. As shown, sum of the magnitude of the shaded areas $\left(S_{1}+S_{2}+S_{3}\right)$ below the critical threshold (TTC*) represent the magnitude of TIT and sum of all moments below the TTC* threshold $\left(T_{1}+T_{2}\right)$, thus, approximating to the magnitude of TET. Different TTC* values within the range $2-5 \mathrm{~s}$ have been propounded to varying driving scenarios including out of control vehicles, vehicles under control, non-supported drivers and supported drivers, among others (Hirst and
![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-03.jpg?height=589&width=1167&top_left_y=1809&top_left_x=488)

3 Calculation procedures for time exposed time-to-collision (TET) and time integrated time-to-collision (TIT) pertaining to a hypothetical time-to-collision (TTC) profile

![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-04.jpg?height=657&width=1171&top_left_y=172&top_left_x=462)

## 4 Theoretical profile for time-to-collision (TTC)

Graham 1997; Hogema and Janssen 1996; Van der Horst 1990).

Time exposed time-to-collision and TIT have been shown to be beneficial indicators for use in road safety analyses and driver warning systems during car-following situations; however, neither measure is accurate. It is considered that the additional consideration of driverassociated behavioral information would serve to enhance both TET and TIT. A theoretical profile for TTC of a hypothetical vehicle is presented in Fig. 4. As shown (Fig. 4), the TTC profile is divided into 17 identical timesteps from $t_{1}$ to $t_{18}$, with each time-step representing $0 \cdot 1 \mathrm{~s}$. Time exposed TTC and TIT have been calculated for two different sections of this profile: $\left[t_{2}, t_{9}\right]$ and $\left[t_{9}, t_{17}\right]$ (Table 1).

As shown (Fig. 4), TTC is less than TTC* with respect to both time intervals, however, $\left[t_{2}, t_{9}\right]$ exhibits a decreasing rate while $\left[t_{9}, t_{17}\right]$ exhibits an increasing rate.

Based upon calculated values for TET and TIT (Table 1), time interval $\left[t_{9}, t_{17}\right]$ represents a greater level of collision danger than interval $\left[t_{2}, t_{9}\right]$. However, as shown (Fig. 4), TTC exhibits a decreasing pattern within the first interval, indicating an increasing likelihood of a rear-end collision in a car-following situation. In $\left[t_{9}, t_{17}\right]$, the inverse is displayed, whereby the likelihood of a rear-end collision is decreasing. Accordingly, the rate of change with respect to TTC is a necessary factor for accurate TET or TIT calculation. During consideration of TTC, the first interval presents a more significant hazard than that exhibited in the second interval. Thus, in the application of TET or TIT as a preemptive warning strategy with

Table 1 Time exposed time-to-collision (TET) and time integrated time-to-collision (TIT) for $\left[\mathbf{t}_{\mathbf{2}}, \mathbf{t}_{\mathbf{9}}\right]$ and [ $\mathbf{t}_{\mathbf{9}}, \mathbf{t}_{\mathbf{1 5}}$ ] time intervals
| Interval | TET | TIT |
| :--- | :--- | :--- |
| $\left[t_{2}, t_{9}\right]$ | 0.7 | 1.26 |
| $\left[t_{9}, t_{17}\right]$ | 0.8 | 1.44 |


IVCAWSs, consideration of the rate of TTC variation will aid in the prevention of rear-end collisions.

## Methodology

As previously outlined, the rate of change associated with the magnitude of TTC affects safety in car-following scenarios; however, to date, this rate of change has not been included in either TET or TIT calculation procedures. This points to the need for development of an enhanced TTC-based safety indicator, considering both TTC magnitude and rate of change. The first derivative of a hypothetical TTC profile (Fig. 4) with respect to a time variable is presented in Fig. 5, while the status of each time interval based on TTC value and $\mathrm{TTC}^{\prime}=\mathrm{d}$ TTC/d $t$ is outlined in Table 2.

When TTC < TTC* a collision risk is indicated, while TTC' <0 indicates a decreasing rate of TTC, in concurrence with an increasing probability of collision. Thus, time intervals $\left[t_{1}, t_{2}\right],\left[t_{2}, t_{9}\right]$, and $\left[t_{9}, t_{17}\right]$ all represent an inherent level of danger, while $\left[t_{2}, t_{9}\right]$ is shown to be the most likely time interval during which a collision may occur. In order to effectively quantify the comparative levels of risk associated with each time period, a comprehensive time-based measure (CTM) is needed, to permit the inclusion of TTC variation rates during carfollowing scenarios

Comprehensive time-based measure must include TET, TIT, and TTC' but determining the effect of TET, TIT, and TTC' in CTM is difficult. One way is applying regression models with the help of previous surrogate safety measures. However, then there is a question if the other indicators are accurate enough that we use a regression, then why one use CTM? Here the effect of each indicator has been considered the same and just we have presented a method to normalize indicators in a range between [0,1] to be analogous.

In order to normalize TTC', TET, and TIT, first the maximum value of each indicator at each time step must be calculated. The maximum variation rate for TTC can be obtained based on TTC' of real car-following scenarios
![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-05.jpg?height=634&width=1171&top_left_y=200&top_left_x=486)

## 5 First derivative of hypothetical time-to-collision (TTC) profile with respect to time

during $\tau$ second time steps. Max TTC' would be considered as the most dangerous rate of variation for TTC and TTC'/max TTC' gives a good measure in the range of $[0,1]$ to normalize TTC'. The maximum TET and TIT during a $\tau$ second period would be $\tau$ and ( $\tau \times \mathrm{TTC}^{*}$ ), respectively. Again $\operatorname{TET}(\tau) / \tau$ and $\operatorname{TIT}(\tau) /\left(\mathrm{TTC}^{*} \cdot \tau\right)$ give two measures in the range of [0,1] to normalize TET and TIT values at each time step, respectively. Figures 6-8 display these procedures schematically.

Therefore, at each time step three values in the range of [0,1] can be calculated. For a car-following scenario that is $H \mathrm{~s}$ there are $T=H / \tau$ time steps and CTM can be calculated as follows
$\operatorname{TET}(t, t-1)$ TET at each time step $\delta_{\mathrm{i}}$ and $\delta_{\mathrm{j}}$ switching variables

## Data

Freeway traffic data were required for effective calibration and validation of the developed safety indicator. Microscopic level variables were employed for the evaluation of CTM accuracy. Accordingly, next generation simulation (NGSIM) data for I-80 freeway in Emeryville San Francisco were used for evaluation. Next generation simulation is a Federal Highway Administration (FHWA) supported project for the development of a core of open

$$
\begin{aligned}
\operatorname{CTM}_{\mathrm{i}}(H) & =\sum_{\mathrm{t}=1}^{\mathrm{T}}\left(\left(\delta_{\mathrm{i}} \times \frac{\mathrm{TTC}^{\prime}(t)}{\max \mathrm{TTC}^{\prime}}\right)\right. \\
& \left.+\delta_{\mathrm{j}}\left(\frac{0 \cdot 5 \times \tau \times\left(\left(\mathrm{TTC}^{*}-\mathrm{TTC}_{\mathrm{i}}(t)\right)+\left(\mathrm{TTC}^{*}-\mathrm{TTC}_{\mathrm{i}}(t+1)\right)\right)}{\tau \times \mathrm{TTC}^{*}}+\frac{\mathrm{TET}_{\mathrm{i}}(t, t-1)}{\tau}\right)\right) \\
\delta_{\mathrm{i}} & =\left\{\begin{array}{ll}
0 & \text { else } \\
1 & \forall \mathrm{TTC}_{\mathrm{i}}(t)<0
\end{array} \quad \delta_{j}= \begin{cases}0 & \text { else } \\
1 & \forall 0<\mathrm{TTC}_{\mathrm{i}}(t)<\mathrm{TTC}^{*}\end{cases} \right.
\end{aligned}
$$

Here
$\mathrm{CTM}_{\mathrm{i}}(t)$ comprehensive measure based on TTC for vehicle $i$
$\mathrm{TTC}_{\mathrm{i}}(t)$ time-to-collision for vehicle $i$ at time $t$
$\mathrm{TTC}^{\prime}(t)$ time derivative of TTC for vehicle $i$ at time $t$

Table 2 Comparison of varying time intervals based on values of TTC and TTC'
| Interval | TTC*-TTC | TTC' |
| :--- | :--- | :--- |
| $\left[t_{1}, t_{2}\right]$ | - | - |
| $\left[t_{2}, t_{9}\right]$ | + | - |
| [ $t_{9}, t_{17}$ ] | + | + |
| $\left[t_{17}, t_{18}\right]$ | - | + |


TTC: time integrated time-to-collision.
behavioral algorithms for microscopic traffic simulation. Datasets were collated using high-resolution cameras, capable of capturing vehicle position at $0 \cdot 1$ s increments. Employed I-80 vehicle trajectory data relate an afternoon traffic peak (from 4:00 p.m. to 4:15 p.m.) on Wednesday, April 13, 2005. Three vehicle categories (motorcycles, passenger cars, and heavy vehicles) were encountered along the six-lane study section. Lane 1 represents the left-most lane (a high occupancy vehicle-HOV lane), while lanes 5 and 6 are the right-most lanes, both of which are directly influenced by adjacent on- and offramps (Fig. 9).

In order to accurately classify and extract car-following situations and study driver behaviors during car-following scenarios, three criteria are used, as follows:
![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-06.jpg?height=862&width=1169&top_left_y=168&top_left_x=464)

6 Procedure of normalizing TTC' at each time step
![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-06.jpg?height=720&width=1003&top_left_y=1143&top_left_x=548)
7 Procedure of normalizing time exposed time-to-collision (TET) at each time step

- Both leading and following vehicles must be passenger cars.

- Both vehicles must associate with a car-following scenario for the entirety of the observation period along the 500 m study segment (i.e. neither vehicle may

- The observation period should be $\geq 90$ s (car-following period must permit observation of all variations in driver behavior).

Table 3 Maximum rate of variations for time-to-collision (TTC) in car-following scenarios
| Car-following | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Max(TTC') | $24 \cdot 5$ | 69.8 | 23.8 | $34 \cdot 7$ | 35.2 | 38 | 23.9 | $32 \cdot 7$ | 29.7 | $31 \cdot 4$ |
| Car-following | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| Max(TTC') | $22 \cdot 4$ | 34.8 | 24.3 | $31 \cdot 1$ | $31 \cdot 5$ | $30 \cdot 9$ | 41.7 | $62 \cdot 6$ | 39.1 | 25.3 |


$$
\frac{\operatorname{TIT}\left(\mathrm{t}_{2}, t_{1}\right)}{\max (\operatorname{TIT}(\tau))}=\frac{0.5 \times \tau \times\left(\left(T T C^{*}-T T C\left(t_{1}\right)\right)+\left(\operatorname{TTC}^{*}-T T C\left(t_{2}\right)\right)\right)}{\tau \times T T C^{*}}
$$

![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-07.jpg?height=522&width=1169&top_left_y=314&top_left_x=490)

## 8 Procedure of normalizing time integrated time-to-collision (TIT) values at each time step

Based on these criteria, 20 car-following scenario timeseries were selected, equating to approximately 19000 rows of data.

## Results

For each car-following scenario, TTC was calculated based on the aforementioned conventional definition (1). Subsequently, for $\mathrm{TTC}^{*}=2,3,4,5,6,7,8 \mathrm{~s}$ (a rational range for TTC ${ }^{*}$ for sensitivity analyses) CTM can be calculated.

Here, $\tau=0.1 \mathrm{~s}$ and $\operatorname{Max}\left(\mathrm{TTC}^{\prime}\right)$ for 20 car-following scenarios are in Table 3. At last, 70 is selected as Max(TTC') for car-following scenarios.

Comprehensive time-based measure is calculated using equation (10) and compared with TIT for each carfollowing scenario. Results are summarized in Fig. 10. Further examination of CTM and TIT variations at each time-point for four selected car-following situations are presented in Fig. 11, just for $\mathrm{TTC}^{*}=5 \mathrm{~s}$.

The following findings have been garnered from these supplementary investigations (Fig. 8):

- CTM>TIT at each time-point because of the inclusion of the varying TTC value in the CTM. Moreover, CTMendeavors to offset the effect of TTC value, which represents the primary parameter in TIT determination.
- In some instances, TIT equals zero, while CTM does not exhibit a zero value; conversely, the reverse does not occur. This occurs because of the inclusion of rate variations of TTC. When CTM equals zero, there is no probability of the occurrence of rear-end collisions.
- Variations of CTM are greater than those associated with TIT; the TIT profile displays a relatively smooth trend, while CTM is shown to oscillate abruptly, because of the inherent driver behaviors during carfollowing scenarios.
- Typically, the overall form of CTM and TIT profiles are somewhat similar; notwithstanding zero points within the TIT profile, peak points generally coincide with each other.
- Instances may occur that are characterized by an abrupt peak in the CTM profile, in concurrence with a low or zero-value TIT. This finding suggests that rate of TTC variation is elevated in concurrence with a sudden TTC decrease, although its value may remain above the critical threshold. These represent sudden and potentially hazardous changes in driver behavior.

![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-07.jpg?height=509&width=999&top_left_y=1929&top_left_x=574)

![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-08.jpg?height=1482&width=1650&top_left_y=170&top_left_x=223)
10 Comprehensive time-based measure (CTM) and $\overline{\text { TIT }}$ for each car-following situation

Based on these points, it may be concluded that CTM is a more precise indicator than TIT. As CTM considers TTC variation in addition to its absolute magnitude, a part of variations in the car-following process because of factors including driver behavior and environmental conditions might be accounted for by CTM. Based on this inherent attribute, CTM may also be extremely useful for application as a preemptive warning within IVCAWSs; even lowlevel risks during car-following scenarios are noted and considered. Furthermore, although CTM is a new indicator, results to date are typically coincident with TIT; at no time were potential collisions detected via TIT and not concurrently detected by CTM.

## Conclusion

Surrogate safety measures are beneficial and potentially life-saving tools for road safety assessments, while also having significant applications as a preemptive warning process in vehicle collision avoidance systems. In the current study, one of the most frequently employed safety indicators, namely TTC, has been evaluated. In order to accurately assess time interval based safety, two extended measures (TET and TIT) have been developed. Results indicate that TIT is a more complete measure and considers the duration of time associated with unsafe TTCs and overall TTC magnitude during car-following scenarios. However, TIT does not consider the rate of change associated with TTC values, thus representing an operational disadvantage; the rate of TTC variation is reflective of changes in driver behavior during car-following scenarios, and is therefore an extremely important factor with respect to collision prediction and road safety assessment. Accordingly, a novel indicator has been developed. This new indicator CTM simultaneously considers both TTC magnitude and the rate of TTC variation. Comparative analyses show that CTM is a more accurate measure because of the inclusion of increased levels of data

![](https://cdn.mathpix.com/cropped/c3c9e5cc-c25c-4015-82a8-881678eed4ca-09.jpg?height=1994&width=1629&top_left_y=170&top_left_x=251)
11 Comprehensive time-based measure (CTM) and TIT variations for four car-following scenarios

pertaining to driver behavior. Road safety is an undoubtedly complicated issue, with collisions typically occurring in parallel with numerous disparate factors. Thus, variation in one of these factors may result in the decreased likelihood or complete avoidance of a collision; as CTM considers a higher number of potentially causative parameters, it may have wide-reaching applications as an early warning strategy in IVCAWS, thus reducing the instance of rearend collisions, in addition to increasing the precision with which safety evaluations are currently undertaken.

## References

Archer, J. 2005. Indicators for traffic safety assessment and prediction and their application in micro-simulation modeling: a study of urban and suburban intersections. Unpublished PhD thesis. Royal Institute of Technology, Stockholm, Sweden.
Barcelo, J., Montero, L., Perarnau, J. and Torday, A. 2003. Safety indicators for micro-simulation based assessments. In: 82nd Annual Meeting of the Transportation Research Board. Washington, DC, USA.
Brian, L., Allen, B., Shin, T. and Cooper, P. J. 1978. Analysis of traffic conflicts and collisions. Transportation Research Record: Journal of the Transportation Research Board, 667, pp.67-74.
Cooper, P. J. 1983. Experience with traffic conflicts in Canada with emphasis on 'post encroachment time' techniques. In: Proceedings of the NATO Advanced Research Workshop on International Calibration Study of Traffic Conflict Technique. Copenhagen, Denmark, 25-27 May 1983.
Cunto, F. J. C. 2008. Assessing safety performance of transportation systems using microscopic simulation, Unpublished PhD thesis. Department of Civil Engineering, Waterloo, Canada
Gettman, D. and Head, L. 2003. Surrogate safety measures from traffic simulation models. Technical Report, Federal Highway Administration - FHWA-RD-03-050.
Gousios, S. and Garber, N. J. 2009. Relationship between time to collision conflicts and crashes on interstate highways subjected to truck lane restrictions. In: 88th Annual Meeting of the Transportation Research Board. Washington, DC, 11 January 2009-15 January 2009.
Hayward, J. 1971. Near misses as a measure of safety at urban intersections. Unpublished PhD thesis, Department of Civil Engineering, The Pennsylvania State University, University Park, PA.
Hirst, S. and Graham, R. 1997. The format and presentation of collision warnings. In: Y. I. Noy, ed. Ergonomics and safety of intelligent driver interfaces. Mahwah, NJ: Lawrence Erlbaum Associates, Inc, 432p.
Hogema, J. H. and Janssen, W. H. 1996. Effects of intelligent cruise control on driving behavior. Report TM-1996-C-12. Soesterberg, the Netherlands: TNO Human Factors.
Laureshyn, A., Svensson, A. and Hyden, Ch. 2010. Evaluation of traffic safety, based on micro-level behavioral data: Theoretical framework and first implementation, Accident analysis\&prevention. Volume, 42, issue 6, pp.1637-1646.
Kiefer, R. J., Leblanc, D. J. and Flannagan, C. A. 2005. Developing an inverse time-to collision crash alert timing approach based on drivers' last-second braking and steering judgments. Accident Analysis and Prevention, 37, pp.295-303.
Minderhoud, M. M. and Bovy, P. H. L. 2001. Extended time-to-collision measures for road traffic safety assessment. Accident Analysis and Prevention, 33, pp.89-97.
NGSIM, June 5, 2009. Next generation simulation. Available: http://http:/ /ngsim-community.org/
Ozbay, K., Yang, H., Bartin, B. and Mudigond, S. 2008. Derivation and validation of new simulation-based surrogate safety measure. Transportation Research Record, Journal of the Transportation Research Board No. 2083, pp.105-13.
Saffarzadeh, M., Nadimi, N., Nasealavi, S. and Mamdoohi, A. R. 2013. A general formulation for time to collision. In: Proceedings of the ICE Transport, Volume 166, pp.294-304, London: Institution of Civil Engineers.
Sobhani, A., Young, W., Sarvi, M. and Bahrololoom, S. 2013. Calculating time-to-collision for analyzing right turning behavior at signalized intersections. Road and Transport Research, 22(3), pp.49-61.
Van der Horst, A. 1990. A time-based analysis of road user behavior in normal and critical encounters. TNO Institute for Perception, Soesterberg, Netherlands.
Van der Horst, R. and Hogema, J. 1993. Time-to-collision and collision avoidance systems. In: Proceedings of the 6th ICTCT Workshop: Safety Evaluation of Traffic Systems: Traffic Conflicts and Other Measures. Salzburg, Austria.
Vogel, K. 2003. A comparison of headway and time to collision as safety indicators. Accident Analysis and Prevention, 35, pp.427-33.
Young, W., Sobhani, A., Lenne, M. and Sarvi, M. 2014. Simulation of safety: a review of the state of the art in road safety simulation modeling. Accident Analysis and Prevention, 66, pp.89-103.


[^0]:    ${ }^{1}$ Department of Civil Engineering, Iran University of Science and Technology, P.O. Box 13114-16846, Tehran, Iran
    ${ }^{2}$ Faculty of Engineering, Shahid Bahonar University, Kerman, Iran
    *Corresponding author, email navidnadimi@yahoo.com

