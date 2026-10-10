# A general formulation for time-to-collision safety indicator 

1 Mahmoud Saffarzadeh
Professor, Faculty of Civil and Environmental Engineering, Tarbiat Modares University, Tehran, Iran
2 Navid Nadimi
Research Assistant, Faculty of Civil and Environmental Engineering, Tarbiat Modares University, Tehran, Iran
3 Saber Naseralavi
Assistant Professor, Faculty of Engineering, Shahid Bahonar University, Kerman, Iran
4 Amir Reza Mamdoohi
Assistant Professor, Faculty of Civil and Environmental Engineering, Tarbiat Modares University, Tehran, Iran

![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-01.jpg?height=224&width=226&top_left_y=959&top_left_x=206)
![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-01.jpg?height=222&width=222&top_left_y=959&top_left_x=521)
![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-01.jpg?height=222&width=222&top_left_y=959&top_left_x=832)
![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-01.jpg?height=219&width=217&top_left_y=959&top_left_x=1144)

Time to collision is an important time-based safety indicator for detecting rear-end conflicts in traffic safety evaluations. A major weakness of the time to collision notion is the assumption of constant velocities during the course of an accident. In this paper we utilise equations of motion to develop a generalised formulation for time to collision by relaxing the assumption of constant velocity, constant acceleration and so on. This paper also illustrates how this concept can be applied to real-world data, and detailed data gathered in the NGISM project are used. Then time to collision is calculated based on the assumption of constant speed, constant acceleration and linear acceleration for leading and following vehicles. Results indicate that in the third case (linear acceleration), the average duration of exposure to critical time to collision values is greater than the others. So, applying time to collision based on the assumption of linear acceleration in collision avoidance systems would decrease driver errors more than other cases.

Notation
| $D$ | inter-vehicle clearance |
| :--- | :--- |
| $f$ | time to collision for a following vehicle |
| $l$ | leading vehicle |
| $l_{\mathrm{F}}$ | following vehicle length |
| $l_{\mathrm{L}}$ | leading vehicle length |
| $t$ | collision at time $t$ |
| $X$ | position of vehicle |
| $\dot{X}, \ddot{X}$ | derivatives of $X$ with respect to time |
| $\dot{X}_{\mathrm{F}}$ | following vehicle speed |
| $X_{\mathrm{L}}$ | leading vehicle speed |
| $X_{\mathrm{F}}$ | following vehicle acceleration |
| $X_{\mathrm{L}}$ | leading vehicle acceleration |
| $\delta$ | switching variable |
| $\tau_{\mathrm{SC}}$ | small time interval |
| $\forall$ | following vehicle |


not a suitable criterion for traffic safety evaluation. First, the number of crashes is generally too small for in-depth analysis. On the other hand, gathering enough crash data needs a long period of time (at least 3 years) during which several external factors might change. Another problem is the effect of reduction to the mean phenomenon, which may mislead the observer about the impact of a countermeasure in crash reduction, soon after its implementation (Gousios and Garber, 2009). So, traffic conflict technique (TCT) as a promising method for evaluating traffic safety is introduced here. Conflicts can be defined as recognisable circumstances in which two or more vehicles move toward each other in time and space to such an extent that there is a risk of collision if their movement remains unchanged (Hyd'en, 1977). The most effective method to measure traffic conflicts is to use safety indicators.

Also, there are two different approaches to improving traffic safety, which are passive and active countermeasures. Passive countermeasures usually refer to devices which are designed to reduce the consequence of accidents, such as seat belts, deformable roadside equipment and so on. However, along with the development of intelligent transportation systems (ITS), attention is turning towards active safety countermeasures, which are developed to reduce driver errors and thereby the number of accidents (Lundgren and Tapani, 2006). One important type of
active safety measure is advanced driver assistance systems (ADAS), which is a field of ITS. An example of ADAS, for longitudinal support of drivers in car-following situations, is collision avoidance systems (CAS). The parameters which are generally used to activate such systems and specifying longitudinal driving behaviours are safety indicators.

Time to collision (TTC) is the most well-known time-based safety indicator. TTC refers to the time remaining before the rear-end accident if the course and speed of vehicles are maintained. TTC has proven to be an effective measure for discriminating critical from normal behaviours in car-following situations. The major shortcoming of TTC is the assumption of constant vehicle velocities, during collision course. Also, according to Vogel (2003), TTC indicates the actual occurrences of dangerous situations and cannot capture potentially dangerous situations. Therefore, the enhancement of TTC is indispensable.

In this paper a generalised formulation for TTC is proposed based on the equations of motion and relaxing the assumption of constant velocities. Then, the paper illustrates how the concept can be applied to real-world data. For this, car-following situations are selected and for more simplicity, TTC is calculated in just three cases, based on the assumption of constant velocities, constant acceleration and linear acceleration. Lastly, results are compared in different lanes and applying each kind of TTC, in CAS, is discussed.

## 2. Literature review

Time to collision, as perceived from its name, refers to the duration of time before two (or more) objects collide with initial certain conditions. Use of TTC in the field of transportation started after its introduction by Hayward in 1971 as the time span left before two vehicles collide, if no evasive action is taken (Hayward, 1971). TTC is a main criterion in traffic conflict techniques and plays a significant role in car-following processes, especially when confronted with the questions of when and how a driver accelerates (or decelerates) (Wang et al., 2008). TTC is a core parameter in designing collision avoidance systems (van der Horst and Hogema, 1993) which can also be used for highway traffic management (Balas and Balas, 2008). Furthermore, safety evaluation in many cases has been accomplished by means of TTC-based surrogate safety measures (Lundgren and Tapani, 2006; Ozbay et al., 2008). TTC has been considered as an effective indicator in evaluating traffic safety in the field of traffic conflict studies (Minderhoud and Bovy, 2001; Oh et al., 2006; Vogel, 2003).

Rear-end collisions occur in car-following processes. Traffic conflict techniques with the help of safety indicators are promising tools for traffic safety evaluation and detection of risky carfollowing situations. To date, several safety indicators have been developed in the scientific literature to assess the risk with carfollowing manoeuvres. Time to collision (TTC) is the most wellknown indicator, and is applied in different studies for evaluating rear-end collision risk. TTC value at an instant $t$ is defined as the time for two vehicles to collide if they continue at their present speed and on the same path. So, the higher a TTC value, the safer a situation. The TTC for a following vehicle $(f)$ at instant $t$ with respect to a leading vehicle $l$ can be calculated with Equation 1
1.

$$
\begin{aligned}
T T C_{\mathrm{F}}(t) & =\frac{X_{\mathrm{L}}(t)-X_{\mathrm{F}}(t)-l_{\mathrm{L}}}{\dot{X}_{\mathrm{F}}(t)-\dot{X}_{\mathrm{L}}(t)} \\
\forall \dot{X}_{\mathrm{F}}(t) & >\dot{X}_{\mathrm{L}}(t)
\end{aligned}
$$

where $X$ denotes the position, $\dot{X}$ denotes the derivative of $X$ with respect to time or the speed, and $l_{\mathrm{L}}$ denotes the leading vehicle length; L and F as subscripts refer to leading and following vehicles in a car-following process. Note that TTC is only valid when the speed of the following vehicle is higher than the leading vehicle.

Thus TTC is based on the assumption that the following and leading vehicles continue with constant speeds till collision occurrs, thus ignoring the actual acceleration or deceleration of both vehicles in this interval. Such an assumption would ignore many potential conflicts due to deceleration and acceleration discrepancies. So, it is probable that some dangerous events would not be considered in traffic safety evaluations, and safety systems like CAS would be insensitive to such situations.

Ozbay et al. (2008) proposed Table 1 to indicate possible reasonable situations where potential conflicts might occur that conventional TTC cannot capture. In Table $1, \ddot{X}_{\mathrm{F}}$ and $\ddot{X}_{\mathrm{L}}$ are the time

| $\dot{X}$ |  | $\dot{X}_{F}>\dot{X}_{L}$ |  |  | $\dot{X}_{F} \leqslant \dot{X}_{L}$ |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\ddot{X}$ | $\ddot{X}_{L}>0$ | $\ddot{X}_{L}<0$ | $\ddot{X}_{\mathrm{L}}=0$ | $\ddot{X}_{L}>0$ | $\ddot{X}_{L}<0$ | $\ddot{X}_{L}=0$ |
| $\ddot{X}_{F}>0$ | $P$ | C | C | $P$ | C | $P$ |
| $\ddot{X}_{F}<0$ | $P$ | $P$ | $P$ | 1 | $P$ | 1 |
| $\ddot{X}_{\mathrm{F}}=0$ | $P$ | $C$ | $C$ | 1 | C | 1 |
| $C=$ conflict occurs; $P=$ possible conflict; $I=$ conflict impossible |  |  |  |  |  |  |

Table 1. Possible situations for a pair of vehicles in a carfollowing process (Ozbay et al., 2008)

derivatives of $\dot{X}$ or the acceleration of the following and leading vehicles, respectively. Then, based on the equations of motion and constant acceleration assumption, they developed a new TTC, named as $\mathrm{TTC}_{2}$ in this paper.

Determination of whether a conflict would occur is based on the consideration of the trajectory parameters of leading and following vehicles, including the relative distance, relative velocity and relative acceleration. So, $\mathrm{TTC}_{2}$ would be calculated as Equation 2
2. $\dot{X}_{\mathrm{F}} t+\frac{1}{2} \ddot{X}_{\mathrm{F}} t^{2}=D+\dot{X}_{\mathrm{L}} t+\frac{1}{2} \ddot{X}_{\mathrm{L}} t^{2}$

Equation 2 can be rewritten as
3. $\frac{1}{2} \Delta \ddot{X} t^{2}+\Delta \dot{X} t-D=0$
where $\Delta \dot{X}$ is relative speed, $\left(\dot{X}_{\mathrm{F}}-\dot{X}_{\mathrm{L}}\right), \Delta \ddot{X}$ is relative acceleration, $\left(\ddot{X}_{\mathrm{F}}-\ddot{X}_{\mathrm{L}}\right)$ and $D$ is inter-vehicle clearance.
$\mathrm{TTC}_{2}$ is the real and non-negative solution of Equation 3, which is presented below. Figure 1 illustrates an algorithm to choose $\mathrm{TTC}_{2}$, from $t_{1}$ and $t_{2}$.

$$
\begin{aligned}
& \text { If }(\Delta \ddot{X} \neq 0) \\
& \left\{t_{1}=\frac{-\Delta \dot{X}-\sqrt{\Delta \dot{X}^{2}+2 \Delta \ddot{X} D}}{\Delta \ddot{X}}\right. \\
& t_{2}=\frac{-\Delta \dot{X}+\sqrt{\Delta \dot{X}^{2}+2 \Delta \ddot{X} D}}{\Delta a}
\end{aligned}
$$

Minderhoud and Bovy (2001) derived time-exposed time-tocollision (TET*) as a new safety measure. TET* is the duration of exposure to safety-critical TTC values over specified time duration $h$. It is the summation of all moments (over the considered time period) that a driver approaches a front vehicle with a TTC value below the threshold value TTC*. TTC* is the boundary between safe and unsafe car-following situations. Different values are reported as TTC* in the literature. Hirst and Graham (1997) reported that a TTC measure of 4 s could be used to discriminate between cases where drivers unintentionally find themselves in a dangerous situation from cases where they remain in control. The study further describes a laboratory experiment of the design of a collision warning system. The results showed that a TTC warning criterion of 4 or 5 s results in too many false alarms. The study shows that a TTC value of 3 s produced the least number of alarms although in some cases critical situations were observed. Hogema and Janssen (1996) studied driver behaviour at an approach to a queue among non-supported and supported drivers in a driving simulator experiment. They found a minimum TTC value of 3 ⋅ 5 s for the non-supported drivers, and

![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-03.jpg?height=884&width=1629&top_left_y=1782&top_left_x=254)
Figure 1. Algorithm of selecting $\mathrm{TTC}_{2}$ from $t_{1}$ and $t_{2}$

2.6 s for supported drivers. The 2.6 s value is regarded as a safety concern. van der Horst and Hogema (1993) reports even lower critical TTC values, based on approaches at intersections. So, there is no definite value for TTC* for different drivers in different car-following situations.

To calculate the TET* indicator, the trajectory of all vehicles entering and leaving a specified road section, over time period of $h$, must be established. From these trajectories, a TTC diagram over $h$ would be drawn such as in Figure 2. Since data are mostly collected in discrete time, the TTC values will also be determined at discrete time moments (time intervals as $\tau_{\mathrm{SC}}$ ). For calculation purposes, it is assumed that the measured TTC values, at an instant $t$, would not change, during a small time interval $\tau_{\mathrm{SC}}$ (e.g. $0.1 \mathrm{~s})$. For the considered time period $h$, there are $T=H / \tau_{\mathrm{SC}}$ time instants $t$, taken into account in the calculation $(t=0 \ldots t)$.

So from Figure 2, it can be concluded that the TET* indicator for a subject vehicle $i$, can be calculated by
4.

$$
\mathrm{TET}^{*}=\sum_{t=0}^{T} \delta_{i}(t) \tau
$$

$$
\delta_{i}(t)=\left\{\begin{array}{lc}
1, & 0 \leqslant T T C_{i}(t) \leqslant T T C^{*} \\
0, & \text { ow }
\end{array}\right.
$$

in which $\delta$ is a switching variable and $o w$ is otherwise. Its value is 1 , when an instant of car-following TTC value is between 0 and the critical threshold TTC*, and 0 in other cases.

In Figure 2, at instant $t=0$, the driver approaches a slower moving vehicle, so TTC values decreases with time. Then the driver decides to make a lane-change at moment $t_{1}$. Now the driver is confronted with a new leader at a smaller gap distance.

![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-04.jpg?height=493&width=825&top_left_y=2127&top_left_x=144)
Figure 2. Time extended time to collision concept (Minderhoud and Bovy, 2001)

The TTC values are now smaller and below TTC*. The driver adapts his speed to increase the gap distance and reduce the speed differential. Between $t_{2}$ and $t_{3}$ there is no positive TTC value. The lead vehicle is thus driving at a higher speed. At $t_{3}$, the subject approaches another lead vehicle, and this process would be continued in car-following situations, and TTC would switch from negative to positive values to maintain a minimum desired gap distance (Minderhoud and Bovy, 2001). To calculate TET*, the duration of time with TTC values less than TTC* must be calculated. So in Figure 2, $t_{1}$ plus $t_{2}$ is TET*.

Minderhoud and Bovy (2001) also proposed an indicator based on TET*, to calculate the percentage of time that a random driver drives with TTC values below the threshold TTC*. This indicator is calculated by Equation 5
5. $\mathrm{TETP}^{*}=100 \times \frac{\mathrm{TET}^{*}}{H}$

## 3. A generalised formulation for TTC

In Equation 3, proposed by Ozbay et al., it is assumed that the acceleration of leading and following vehicles is constant (Ozbay et al., 2008), so ignoring their fluctuations. Four impossible scenarios shown in Table 1 are also based on this assumption (constant acceleration for both leading and following vehicles). However, conflicts may occur in these (impossible) scenarios, if jerk value (acceleration time derivative) for the following vehicle is more than that of the leading vehicle. For instance, assume that $\dot{X}_{\mathrm{F}} \leqslant \dot{X}_{\mathrm{L}}, \ddot{X}_{\mathrm{L}}>0$ and $\ddot{X}_{\mathrm{F}}<0$, then the occurrence of a rear-end collision is impossible. However, in this scenario, there is a possibility of rear-end collision if considering acceleration fluctuations for both vehicles. Thus $\mathrm{TTC}_{3}$ (with assumption of linear acceleration (or constant jerk) for both vehicles during collision course) unlike $\mathrm{TTC}_{2}$ proposed by Ozbay et al. can capture some potentially risky situations.

Equation 6 is the necessary and sufficient condition for rear-end collision
6. $X_{\mathrm{F}}-X_{\mathrm{L}}+l_{\mathrm{L}}=0 \Leftrightarrow$ rear-end collision

If the current locations of assumed leading and following vehicles are $X_{0 \mathrm{~L}}$ and $X_{0 \mathrm{~F}}$ respectively, and with assumption of constant speed (acceleration or jerk), it is possible to compute the new location of a pair of vehicles ( $X_{\mathrm{L}}$ and $X_{\mathrm{F}}$ ) in $t$ subsequent seconds using equations of motion. Then, by placing $X_{\mathrm{L}}$ and $X_{\mathrm{F}}$ in Equation 6, TTC is achievable as the moment when the front of the following vehicle collides with the back of the leading one. Table 2 illustrates the equations whose solution leads to different TTCs based on the assumption of constant speed $\left(\mathrm{TTC}_{1}\right)$, constant acceleration $\left(\mathrm{TTC}_{2}\right)$ and linear acceleration $\left(\mathrm{TTC}_{3}\right)$ for both leading and following vehicles during the collision course.

|  |  |  |
| :--- | :--- | :--- |
| TTC type | Assumptions | Equations |
| $\mathrm{TTC}_{1}$ | $\begin{aligned} & \dot{X}_{L}=\text { cte } \\ & \dot{X}_{F}=\text { cte } \\ & \ddot{X}_{L}=\ddot{X}_{F}=0 \end{aligned}$ | $\begin{aligned} & X_{F}=X_{O F}+\dot{X}_{F} t \\ & X_{L}=X_{O L}+\dot{X}_{L} t \\ & \left(\dot{X}_{F}-\dot{X}_{L}\right) T T C-\left(X_{L}-X_{F}-I_{L}\right)=0 \end{aligned}$ |
| $\mathrm{TT} \mathrm{C}_{2}$ | $\begin{aligned} & \ddot{X}_{L}=\text { cte } \\ & \ddot{X}_{F}=\text { cte } \\ & \ddot{X}_{L}=\dddot{X}_{F}=0 \end{aligned}$ | $\begin{aligned} & X_{F}=X_{O F}+\dot{X}_{F} t+\frac{1}{2} \ddot{X}_{F} t^{2} \\ & X_{L}=X_{O L}+\dot{X}_{L} t+\frac{1}{2} \ddot{X}_{L} t^{2} \\ & \frac{1}{2}\left(\ddot{X}_{F}-\ddot{X}_{L}\right) T T C^{2}+\left(\dot{X}_{F}-\dot{X}_{L}\right) T T C-\left(X_{L}-X_{F}-I_{L}\right)=0 \end{aligned}$ |
| $\mathrm{TTC}_{3}$ | $\begin{aligned} & \ddot{X}_{L}=\text { cte } \\ & \ddot{X}_{F}=\text { cte } \end{aligned}$ | $\begin{aligned} & X_{\mathrm{F}}=X_{\mathrm{OF}}+\dot{X}_{\mathrm{F}} t+\frac{1}{2} \ddot{X}_{\mathrm{t}} t^{2}+\frac{1}{6} \ddot{X}_{\mathrm{X}} t^{3} \\ & X_{\mathrm{L}}=X_{\mathrm{OL}}+\dot{X}_{\mathrm{L}} t+\frac{1}{2} \ddot{X}_{\mathrm{L}} t^{2}+\frac{1}{6} \ddot{X}_{\mathrm{L}} t^{3} \\ & \frac{1}{6}\left(\ddot{X}_{\mathrm{F}}-\ddot{X}_{\mathrm{L}}\right) T T C^{3}+\frac{1}{2}\left(\ddot{X}_{\mathrm{F}}-\ddot{X}_{\mathrm{L}}\right) T T C^{2} \\ & +\left(\dot{X}_{\mathrm{F}}-\dot{X}_{\mathrm{L}}\right) T T C-\left(X_{\mathrm{L}}-X_{\mathrm{F}}-I_{\mathrm{L}}\right)=0 \end{aligned}$ |

Table 2. Description of three different cases for TTC calculations

As shown in Table 2, $\mathrm{TTC}_{1}, \mathrm{TTC}_{2}$ and $\mathrm{TTC}_{3}$ can be obtained from linear, quadratic and cubic polynomial equations, respectively.

The three cases in Table 2 lead to developing the generalised formulation for TTC. At first, location of leading and following vehicles after $t$ seconds, for calculation of $\mathrm{TTC}_{k}$ with the assumption of the $(k-1)$ th derivative of speed being constant, can be computed as follows

$$
\left\{\begin{array}{l}
X_{\mathrm{F}}=X_{0 \mathrm{~F}}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times \frac{\partial^{n} X_{\mathrm{F}}}{\partial t^{n}} \times t^{n}\right) \\
\quad k=1,2,3, \ldots n \\
X_{\mathrm{L}}=X_{0 \mathrm{~L}}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times \frac{\partial^{n} X_{\mathrm{L}}}{\partial t^{n}} \times t^{n}\right)
\end{array}\right.
$$

where $\partial^{n} X / \partial t^{n}$ is the $n$th derivative of $X$, for instance $\partial^{3} X_{\mathrm{F}} / \partial t^{3}=\ddot{X}_{\mathrm{F}}$. Replacing $X_{\mathrm{L}}$ and $X_{\mathrm{F}}$ into Equation 6 results in the $k$ th degree polynomial Equation 7 whose solution is $\mathrm{TTC}_{k}$

$$
X_{0 \mathrm{~F}}-X_{0 \mathrm{~L}}+L_{\mathrm{L}}+\sum_{n=1}^{k}\left[\frac{1}{n!} \times\left(\frac{\partial^{n} X_{\mathrm{F}}}{\partial t^{n}}-\frac{\partial^{n} X_{\mathrm{L}}}{\partial t^{n}}\right) \times t^{n}\right]
$$

7. 
8. 

$$
=0
$$

$\mathrm{TTC}_{k}$ is the minimum, non-zero and real (non-complex) solution (for $t$ ) of Equation 7.

With solution of Equation 7, the $t$ would be reported as $\mathrm{TTC}_{k}$. This equation can consider different instantaneous characteristics (speed, acceleration, jerk and so on) of the leading and following vehicles and is hence a generalised form of earlier TTC defined by Equation 3. The definitions of TTC such as TTC ${ }_{1}$ proposed by Hayward (1971) and $\mathrm{TTC}_{2}$ proposed by Ozbay et al. (2008) are special cases of Equation 7, for $k=1$ and $k=2$, respectively. Although, $\mathrm{TTC}_{1}$ is in many cases more useful and simpler than the others, Equation 7 can be valuable in unstable car-following situations and can also theoretically fill the gap in the literature.

## 4. Data collection and respective calculations

The aim of this section is to illustrate the applicability of the proposed concept to real-world data and to present some comparative analysis. So first the data collection process is described and then there is a description of other calculations.

The data used to calculate each TTC are part of a comprehensive dataset obtained from the Next Generation Simulation (NGSIM) website (NGSIM, 2009). NGSIM is a Federal Highway Administration-supported project with a goal of developing a core of open behavioural algorithms mainly in support of microscopic traffic simulation. Datasets prepared in this project can be used for validation and verification of traffic models within the traffic engineering community. NGSIM data are very detailed, openly distributed, and freely available for use in transportation and traffic research. These data are of extreme value for calculation of each TTC in this research. The NGSIM project maintains some datasets from freeways and arterials gathered using highresolution cameras that are able to record vehicle position every $0 \cdot 1$ s. Vehicle trajectory data collected in the afternoon peak hour on Wednesday 13 April 2005 from 4:00 pm to 4:15 pm on a segment of Interstate 80 in Emeryville, San Francisco is used in this research (Figure 3).

There are three types of vehicles (motorcycles, passenger cars, and heavy vehicles) in this freeway, which has six lanes, where lane 1 is the left-most lane and an HOV (high-occupancy vehicle) lane. Also, as seen in Figure 3, lanes 5 and 6 being the right-most lanes are influenced by an on-ramp and an off-ramp.

![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-06.jpg?height=717&width=1480&top_left_y=477&top_left_x=260)
Figure 3. Interstate 80 six-lane section under study and its characteristics

In order to use these trajectory data for the proposed analysis, appropriate pairs of adjacent cars must be selected. Three selection criteria were used.

(a) Both leading and following vehicles are passenger cars.
(b) The two cars had to be adjacent during the whole period that they were both observed through the 1600 ft study segment; for example, neither of the vehicles changes its lane in this segment and no third vehicle places between the two vehicles.
(c) The period during which both cars were observed should have a length of at least 30 s (at least 300 observations).

Under the abovementioned conditions, 491 car-following time series are achieved. The numbers of car-following processes are 67, 193, 75, 71, 45 and 40 for lane 1 from 6, respectively.

The smoothing of vehicles' longitudinal coordinates as a solution to the problem of discontinuity in coordinates of the NGSIM data is undertaken by the technique of kernel moving average. Kernel smoothing is a powerful smoothing algorithm which belongs to the class of weighted moving averages. All points in the timeseries are weighted using the computations of kernel function. Every kernel function has several properties: all kernel values are positive or zero, the kernel functions are normally symmetric, and kernel function values decrease to zero from a central (maximum) value. After smoothing the data, speed, acceleration and jerk of vehicles are obtained from smoothed variation of the vehicles' longitudinal coordinates.
$\mathrm{TTC}_{1}, \mathrm{TTC}_{2}$ and $\mathrm{TTC}_{3}$ are then calculated for each instant of car-following process employing the equations of motion presented in the previous section, in Equation 7, for $k=1,2$ and 3. It should be noted that for the calculation of $\mathrm{TTC}_{k}$ designed for $k>1$, the speed of leading and following vehicles could never be negative, so in equations of motion when speed reaches zero the calculation must be finished and thereafter all instantaneous dynamic characteristics such as speed, acceleration, jerk and so on are set to zero.

As mentioned in the literature review, because drivers' behaviour is not constant in different situations, there is no definite value for TTC threshold (TTC*) to discriminate between safe and unsafe car-following situations. So in this paper, a wide range of values from $0 \cdot 5$ to 10 s with $0 \cdot 5$ s intervals is selected as TTC*. TET*s are calculated based on this range of TTC* for TTC ${ }_{1}$, $\mathrm{TTC}_{2}$ and $\mathrm{TTC}_{3}$. Thereafter, TETP* is determined and averaged per lane.

Since there is no definite value for TTC* for a fixed TTC (e.g. $\mathrm{TTC}_{1}$ ) in all situations, computing TET* with a wide range of TTC* values helps in comparative analysis and reduces bias, in comparison with the condition of applying just a fixed TTC* in all cases. So as a conclusion, this process helps to find the most appropriate TTC*, which would be useful for further applications in CAS, and also traffic safety evaluations based on the notion of generalised TTC.

## 5. Results and discussion

Based on three safety indicators $\mathrm{TTC}_{1}, \mathrm{TTC}_{2}, \mathrm{TTC}_{3}$ and different TTC* values, TET* and then TETP* are computed for each carfollowing situation. So now, for each car-following process, the duration of the time one car drives below the critical value of TTC (TTC*) is determined and the percentage of time driving in a dangerous condition is calculated (TETP*).

For comparative analysis, the box plot of TETP* for TTC ${ }_{1}$
$\left(\mathrm{TETP}_{1}\right), \mathrm{TTC}_{2}\left(\mathrm{TETP}_{2}\right)$ and $\mathrm{TTC}_{3}\left(\mathrm{TETP}_{3}\right)$ for all carfollowing processes in the freeway is shown in Figure 4. In these plots the tops and bottoms of each 'box' are the 25th and 75th percentiles of the samples, respectively. The distances between the tops and bottoms are the interquartile ranges. The line in the middle of each box is the sample median. If the median is not centred in the box, it shows sample skewness. The whiskers are lines extending above and below each box. Whiskers are drawn from the ends of the interquartile ranges to the furthest observations within the whisker length (the adjacent values). Observations beyond the whisker length are marked as outliers. By default, an outlier is a value that is more than 1.5 times the interquartile range away from the top or bottom of the box, but this value can be adjusted with additional input arguments. Outliers are displayed with a red + sign.

The box plots indicate the percentage range of car-following situations which are dangerous, based on the value of TTC*s. But these plots would not show the overall safety condition of the freeway, so in Figure 5 the mean values for the box plots of Figure 4, which are the mean values of TETP* for $\mathrm{TTC}_{1}, \mathrm{TTC}_{2}$ and $\mathrm{TTC}_{3}$, are shown. For a wide range of TTC*s, TTC capability in detecting safety-critical situations increases from TTC ${ }_{1}$ to $\mathrm{TTC}_{3}$. It seems initially that $\mathrm{TTC}_{3}$ is the most appropriate indicator in safety evaluation analysis because of more detection of rear-end conflicts, as shown in Figure 5. But it should be considered that for a random car-following situation in a freeway, following in constant velocity is more probable than constant acceleration, and following in constant acceleration would be more probable than constant jerk. Figure 6 indicates this claim well. These diagrams show velocity, acceleration and jerk variations for a random car-following situation for a duration of about 10 s. As the diagrams show, it is more probable that velocity remains constant than the other parameters. So although values of average duration of exposure to safety-critical time to collision for $\mathrm{TTC}_{2}$ and $\mathrm{TTC}_{3}$ are greater than values computed based on

![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-07.jpg?height=1307&width=1711&top_left_y=1284&top_left_x=208)
Figure 4. Box plot of TETP*s as a function of the critical threshold for: $\mathrm{TETP}_{1}$ * (upper left); $\mathrm{TETP}_{2}{ }^{*}$ (upper right); $\mathrm{TETP}_{3}{ }^{*}$ (bottom)

![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-08.jpg?height=601&width=816&top_left_y=477&top_left_x=146)
Figure 5. Variations of mean TETP* as a function of the critical threshold

$\mathrm{TTC}_{1}$, it should on the other hand be considered that acceleration and jerk might change a few seconds later, and therefore the $\mathrm{TTC}_{2}$ and $\mathrm{TTC}_{3}$ are not trustworthy in a relatively high critical threshold and nor are TETP*s.

Figure 7 shows a comparative analysis of safety in different lanes of the freeway, based on $\mathrm{TTC}_{1}, \mathrm{TTC}_{2}$ and $\mathrm{TTC}_{3}$. According to Figure 7, lane-based comparative analysis with $\mathrm{TTC}_{1}$ is more straightforward than the others. So, a multiple t-test on means of TETP*s (TETP* ${ }_{1}, \mathrm{TETP}^{*}{ }_{2}$ and TETP* ${ }_{3}$ ) for each lane with three thresholds of 2, 3 and 4 s, and with a significance level of $0 \cdot 05$, is used in order to test whether there is a statistical difference between the safety of any two of the six lanes at each threshold level. The results of groups of pairs with a statistically significant difference are presented only for those cases that are statistically significant in Table 3 (TETP* ${ }_{1}$ ) and Table 4 (TETP* ${ }_{2}$ and TETP* ${ }_{3}$ ) with the sign of the difference. As shown in Tables 3 and 4, for any critical threshold level, the safety of lane 1 based on TETP* ${ }_{1}$ is significantly different from the others. The mean TETP* ${ }_{1}$ of lane 1 is significantly smaller than the means for the other five lanes of freeway at almost all critical thresholds except for the critical threshold equal to 2, at which the mean TETP* ${ }_{1}$ of lane 1 and lane 2 is not significantly different. For TETP* ${ }_{2}$, the mean TETP* ${ }_{2}$ of lane 1 is smaller than the others for thresholds equal to 3 and 4, but the same was not observed for TETP* ${ }_{3}$ at any threshold. According to this result, based on the analysis of the means of the TETP*, it is concluded that among safety indicators, one is good if show distinction between alternatives. So, as shown in Table 4, $\mathrm{TTC}_{1}$ is more suitable than $\mathrm{TTC}_{2}$ and $\mathrm{TTC}_{3}$ for distinguishing which lane is safer than others.

In reality, any instantaneous dynamic of vehicles such as speed, acceleration and even jerk do not discretely vary, and therefore the variations of these characteristics are continuous over time. This claim is more perceptible with more detailed data. It should also be mentioned that in a balanced car-following process, especially for high-speed freeways, there is little change in acceleration, so this case may appear non-practical. But on the other hand, there are some risky traffic flow situations that conventional TTC cannot capture. Furthermore, there is a need for a generalised formulation which fills the gap in the literature

![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-08.jpg?height=911&width=1288&top_left_y=1773&top_left_x=361)
Figure 6. Random car-following situation for 10 s

![](https://cdn.mathpix.com/cropped/6fabb045-05f8-40c9-bb3a-1b0d9c0ee79e-09.jpg?height=1302&width=1720&top_left_y=471&top_left_x=203)
Figure 7. TETP* based on 6 lanes as a function of the critical threshold for: $\mathrm{TETP}_{1}$ * (upper left); $\mathrm{TETP}_{2}{ }^{*}$ (upper right); $\mathrm{TETP}_{3}{ }^{*}$ (bottom)

and provides the theoretical background and formulation necessary when detailed and precise estimation and prediction of reality is needed. It should be noted that for a normal carfollowing situation and also normal driver behaviour, it is not practical to compute TTC in situations with jerk variations, which leads to computational complexity and needs detailed data. So, it is only reasonable to consider acceleration variations for TTC computation.

## 6. Conclusion

This paper fills a gap in the literature by proposing a robust framework and by presenting a generalised formulation for TTC. In the conventional definition of TTC, the speed of two vehicles is considered constant, restricting it to special, limited and simple cases. This paper proposes a generalised formulation for TTC using equations of motion which can be employed depending on data availability and the level of precision required. In this formulation, inspired by the work of Hayward (1971) and Ozbay et al. (2008), the acceleration (and also its time derivatives) can be considered to be variable, leading to non-linear speed (acceleration and also jerk). Equations of motion were used as the basis for developing the more general formulation in the form of mathematical equations. For the applicability of the proposed concept to real-world data, comprehensive and detailed data gathered in the NGSIM project on the I-80 freeway are used. TTC is computed for each car-following process per lane in three cases, with the assumption of constant speed, constant acceleration and linear acceleration for leading and following vehicles during the collision course, respectively. As drivers' behaviour is not constant in different situations, there is no definite value for TTC threshold (TTC*) to enable discrimination between safe and unsafe car-following situations. So, in this paper a wide range of values from 0.5 to 10 s are selected as TTC*. Then, the average time duration of exposure to safety-critical TTC values in each case is determined. Results indicate that average time taken to a safety-critical level in the third case (linear acceleration) is greater than in the others.

|  | Case 1 | Case 2 | Case 1 minus Case 2 |
| :--- | :--- | :--- | :--- |
| Threshold $=2 \mathrm{~s}$ | Lane 1 | Lane 2 | - |
|  |  | Lane 4 | - |
|  |  | Lane 5 | - |
|  |  | Lane 6 | - |
|  | Lane 3 | Lane 4 | - |
| Threshold $=3 \mathrm{~s}$ | Lane 1 | Lane 2 | - |
|  |  | Lane 3 | - |
|  |  | Lane 4 | - |
|  |  | Lane 5 | - |
|  |  | Lane 6 | - |
|  | Lane 3 | Lane 2 | - |
|  |  | Lane 4 | - |
| Threshold $=4 \mathrm{~s}$ | Lane 1 | Lane 2 | - |
|  |  | Lane 3 | - |
|  |  | Lane 4 | - |
|  |  | Lane 5 | - |
|  |  | Lane 6 | - |
|  | Lane 3 | Lane 2 | - |
|  |  | Lane 4 | - |

Table 3. Results of $t$-test for difference in lane safety based on TETP* ${ }_{1}$

In all, applying $\mathrm{TTC}_{3}$ in collision avoidance systems (CAS) would increase the precision of the system because most of the dangerous car-following instances would be detected. But on the other hand, because of variability in acceleration in car-following situations, probably giving rise to many false alarms, the reliability of CAS might decrease in comparison with the condition in which TTC ${ }_{1}$ is applied as the safety indicator. Also in traffic safety evaluations, $\mathrm{TTC}_{3}$ (and also other time derivatives of the generalised formulation) shows the safety status of car-following situations is more critical than the conditions in which $\mathrm{TTC}_{1}$ and $\mathrm{TTC}_{2}$ are applied. So $\mathrm{TTC}_{3}$ (and other time derivatives of the generalised formulation) evaluates freeway safety from a meticulous point of view, whereas $\mathrm{TTC}_{1}$ accepts a level of risk in safety evaluations. As a conclusion, for detailed and precise estimation and prediction of reality, $\mathrm{TTC}_{3}$ (and other time derivatives of the generalised formulation) is more suitable than other TTCs.

Further research is recommended regarding assessment from the viewpoint of TTC of the instantaneous safety condition for two vehicles, one following another, and comparisons between $\mathrm{TTC}_{1}$, $\mathrm{TTC}_{2}$ and in particular $\mathrm{TTC}_{3}$ for rear-end conflict detection.

REFERENCES
Balas VE and Balas MM (2008) Constant time to collision platoons. International Journal of Computers Communications \& Control 3: 33-39.
Gousios S and Garber NJ (2009) Relationship between time to collision conflicts and crashes on interstate highways subjected to truck lane restrictions. Proceedings of the 88th Annual Meeting of the Transportation Research Board, TRB, Washington, DC, USA.
Hayward J (1971) Near Misses as a Measure of Safety at Urban Intersections. PhD thesis, Department of Civil Engineering, Pennsylvania State University, University Park, PA, USA.
Hirst S and Graham R (1997) The format and presentation of collision warnings. In Ergonomics and Safety of Intelligent Driver Interfaces (Noy YI (ed.). Lawrence, New Jersey, USA.
Hogema JH and Janssen WH (1996) Effects of Intelligent Cruise Control on Driving Behaviour. Report tm-1996-c-12. TNO Human Factors, Soesterberg, the Netherlands.

| TETP* |  | Case 1 | Case 2 | Case 1 minus Case 2 |
| :--- | :--- | :--- | :--- | :--- |
| $\mathrm{TETP}_{2}$ * | Threshold $=2 \mathrm{~s}$ | Lane 1 | Lane 2 | - |
|  | Threshold $=3 \mathrm{~s}$ | Lane 1 | Lane 2 | - |
|  |  |  | Lane 3 | - |
|  |  |  | Lane 4 | - |
|  |  |  | Lane 5 | - |
|  |  |  | Lane 6 | - |
|  |  | Lane 3 | Lane 4 | - |
|  | Threshold $=4 \mathrm{~s}$ | Lane 1 | Lane 2 | - |
|  |  |  | Lane 3 | - |
|  |  |  | Lane 4 | - |
|  |  |  | Lane 5 | - |
|  |  |  | Lane 6 | - |
|  |  | Lane 3 | Lane 4 | - |
| $\mathrm{TETP}_{3}$ * | Threshold $=3 \mathrm{~s}$ | Lane 1 | Lane 4 | - |

Table 4. Results of $t$-test for difference in lane safety based on TETP* ${ }_{2}$ and TETP* ${ }_{3}$

Hyd'en C (1977) A Traffic Conflicts Technique for Determining Risk. PhD thesis, Lund Institute of Technology, Lund, Sweden.
Lundgren J and Tapani A (2006) Evaluation of safety effects of driver assistance systems through traffic simulation. Transportation Research Record 1953: 81-88.
Minderhoud M and Bovy P (2001) Extended time-to-collision measures for road traffic safety assessment. Accident Analysis and Prevention 33: 89-97.
NGSIM (2009) Next generation simulation http:// ngsim.fhwa.dot.gov (accessed 5 June 2009).
Oh C, Park S and Ritchie SG (2006) A method for identifying rear-end collision risks using inductive loop detectors. Accident Analysis and Prevention 38: 295-301.
Ozbay K, Yang H, Bartin B and Mudigonda S (2008) Derivation and validation of new simulation-based surrogate safety measure. Transportation Research Record 2083: 105-113.
Park B, Chen Y and Hourdos J (2010) Opportunities to prevent rear-end vehicle crashes: findings from analyzing actual crash data. Proceedings of the 89th Annual Meeting of the Transportation Research Board, Washington, DC, USA.
van der Horst R and Hogema J (1993) Time-to-collision and collision avoidance systems. Proceedings of the 6th ICTCT Workshop: Safety Evaluation of Traffic Systems: Traffic Conflicts and Other Measures, Salzburg, Austria.
Vogel K (2003) A comparison of headway and time to collision as safety indicators. Accident Analysis and Prevention 35: 427-433.
Wang LJ, Zhang H, Meng HD and Wang XQ (2008) A model based on TTC to describe how drivers control their vehicles. European Physical Journal B66: 149-153.

## WHAT DO YOU THINK?

To discuss this paper, please email up to 500 words to the editor at journals@ice.org.uk. Your contribution will be forwarded to the author(s) for a reply and, if considered appropriate by the editorial panel, will be published as a discussion in a future issue of the journal.

Proceedings journals rely entirely on contributions sent in by civil engineering professionals, academics and students. Papers should be 2000-5000 words long (briefing papers should be 1000-2000 words long), with adequate illustrations and references. You can submit your paper online via www.icevirtuallibrary.com/content/journals, where you will also find detailed author guidelines.

