![](https://cdn.mathpix.com/cropped/13b8b760-0483-4a1b-bc48-97b7b7c5c8f4-01.jpg?height=339&width=323&top_left_y=165&top_left_x=77)

# An evaluation of time-to-collision as a surrogate safety measure and a proposal of a new method for its application in safety analysis 

Navid Nadimi, David R Ragland \& Amir Mohammadian Amiri

To cite this article: Navid Nadimi, David R Ragland \& Amir Mohammadian Amiri (2019): An evaluation of time-to-collision as a surrogate safety measure and a proposal of a new method for its application in safety analysis, Transportation Letters, DOI: 10.1080/19427867.2019.1650430

To link to this article: https://doi.org/10.1080/19427867.2019.1650430

Published online: 03 Aug 2019.

Submit your article to this journal

Article views: 10

View Crossmark data

# An evaluation of time-to-collision as a surrogate safety measure and a proposal of a new method for its application in safety analysis 

Navid Nadimi ${ }^{\mathrm{a}}$, David R Ragland ${ }^{\mathrm{b}}$ and Amir Mohammadian Amiri ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}}$ Faculty of Engineering, Shahid Bahonar University, Kerman, Iran; ${ }^{\mathrm{b}}$ Safe Transportation Research \& Education Centre, University of California, Berkeley, CA, USA


#### Abstract

Various surrogate safety measures have been introduced, of which Time-to-Collision (TTC) is the most wellknown and commonly applied indicator. TTC first was defined as the time remaining prior to a collision if the path and speed of vehicles are maintained as a constant. Various modifications have been applied to this indicator to increase the efficiency of TTC. However, there is still no specific platform that shows how all of these modifications can be applied simultaneously. Thus, this paper first reviews the modifications that have been made to TTC; subsequently, a comprehensive framework is proposed for the application of this indicator for different types of conflicts, while considering all previous modifications. The framework is then applied for microscopic traffic data collected in Tehran. Results indicate that there is a great difference between the results of different versions of TTC for collision probability prediction. However, the proposed procedure might be beneficial in increasing the precision and accuracy of detecting dangerous encounters.


KEYWORDS
Safety; time-to-collision; indicator; conflict; collision

## Introduction

Over 1.35 million people die each year in traffic crashes, and about 50 million are injured (Global Status Report on Road Safety (WHO) 2018). Various factors are involved in the occurrence of road collisions, of which human factors are considered the most significant (Sagberg 2018). Human factors - human capabilities, limitations, physical conditions, and/or psychological states - play a significant role in transportation accidents (Sundfør, Sagberg, and Høye 2019; Parsa et al. 2019; Charly and Mathew 2019). To reduce their effects in road crashes in hazardous situations, various technologies have been developed and subsequently used in advanced technology vehicles. The In-vehicle Collision Avoidance Warning System (IVCAWS) is one of these technologies and can assist in the avoidance of rear-end collisions. IVCAWS must detect collision warning signs early enough to alert the driver to take immediate action to avoid a crash. Because this could be a nuisance for drivers, system errors must be as limited as possible. Thus, a proper warning strategy must be defined to improve the performance of IVCAWS (Ben Yaakov, Maltz, and Shinar 2002; Behbahani et al. 2019)

To address this goal, the use of surrogate safety measures (SSM) as evasive maneuvers can be beneficial. If SSM are properly defined, they can be effective tools in identifying dangerous situations because they have been developed based on the motion characteristics of vehicles (Van Der Horst and Hogema 1993; Barcelo et al. 2003; Archer 2005; Gettmann and Head 2003; Craveiro 2008; Gousios and Garber 2009; Sobhani et al. 2013; Young et al. 2014; Reddy et al. 2019; Babu and Vedagiri 2018).

Up until the present, different safety indicators have been developed, such as Time-to-Collision (TTC), Post-Encroachment Time (PET), Unsafe Density (UD), Deceleration Rate to Avoid the Collision (DRAC), Proportion of Stopping Distance (PSD), Gap Time (GT), Comprehensive Time-based Measure (CTM), Rear-end collision probability (RECP), Crash Potential Index (CPI), Cyclist Deceleration Rate, Evasive action-based indicators like Deceleration Rate, Jerk Profile and Yaw rate for pedestrians and cyclists conflicts, among others (Hayward 1971; Van Der Horst and Hogema 1993; Barcelo et al. 2003; Gettmann and Head 2003; Cooper 1983; Brian, Shin, and Cooper 1978; Behbahani et al. 2014; Behbahani, Nadimi, and Naseralavi 2014; Zhao and Lee 2018; Strauss et al. 2018; Tageldin and Sayed 2015).

TTC is the most well-known and most commonly applied measure in detecting dangerous situations. Nevertheless, there are some limitations associated with using TTC for this objective. To enhance the efficiency of TTC, various modifications have been applied to this indicator. However, there is still no consensus on how these modifications can be implemented simultaneously. Accordingly, a solution to this problem could result in TTC becoming the most powerful indicator for application in IVCAWS. Accordingly, this paper seeks to review the most important improvements made to TTC. Subsequently, a framework is proposed to calculate TTC based on all the improvements simultaneously.

It is noteworthy that to increase the capabilities of IVCAWS, it is important to have a comprehensive and accurate measure. This measure must be available in order to select a proper reaction to various types of possible collisions, and must also consider the motion characteristics of vehicles potentially involved in a collision.

In the following section, a brief overview of the most wellknown improvements made to TTC is discussed, followed by an explanation of the general procedure for calculating TTC. The aforementioned procedure of TTC calculation is applied in simulated scenarios and results are compared to previous versions of TTC. This is followed by the conclusion.

For the aim of abbreviation, a nomenclature is presented which would be applied throughout the paper.

Nomenclature

| $X_{i}$ | Position of the vehicle i in horizontal direction |
| :--- | :--- |
| $\dot{X}_{i}$ | Speed of the vehicle i in horizontal direction |
| $X_{i}$ | Acceleration/Deceleration of the vehicle i in horizontal direction |
| $l_{i}$ | Length of the vehicle i |
| $t$ | Time |
| $X_{O i}$ | Initial position of the vehicle i in horizontal direction |
| $\frac{\partial^{n} X}{\partial t^{n}}$ | is the $n_{\text {th }}$ derivative of $X$, for instance $\frac{\partial^{3} X_{F}}{\partial t^{3}}=\dddot{X}_{F}$ |
| $\tau$ | Length of time instants |
| $H$ | Duration of car-following, |
| $\left(T=\frac{H}{\tau}\right)$ | Number of time instants |
| $(x, y)$ | Coordinates of a point |
| $X_{\mathrm{ln}}$ | Speed of a line in horizontal direction |
| $Y_{\text {ln }}$ | Speed of a line in vertical direction |
| $Y_{i}$ | Position of the vehicle i in vertical direction |
| $Y_{i}$ | Speed of the vehicle i in vertical direction |
| $\ddot{Y}_{i}$ | Acceleration/Deceleration of the vehicle i in vertical direction |
| $Y_{O i}$ | Initial position of the vehicle i in vertical direction |
| $\frac{\partial^{n} Y}{\partial t^{n}}$ | is the $n_{\text {th }}$ derivative of $Y$, for instance $\frac{\partial^{3} Y_{F}}{\partial t^{3}}=\dddot{Y}_{F}$ |
| L | The leading vehicle |
| F | The following vehicle |
| S | The subject vehicle |
| C | The colliding vehicle |

## TTC improvements

In this section, the modifications made to TTC are reviewed to evaluate the performance of each.

## Time-to-collision (TTC)

TTC was introduced in 1971 by Hayward and applied in different studies to evaluate the likelihood of rear-end collision. TTC value at instant t represents the time for two vehicles to collide if they continue at their present speed and on the same path (Hayward 1971). TTC for the following vehicle (F) at instant t with respect to a leading vehicle L can be calculated with Equation 1:

$$
T T C_{F}(t)=\frac{X_{L}(t)-X_{F}(t)-l_{L}}{\dot{X}_{F}(t)-\dot{X}_{L}(t)} \quad \forall \dot{X}_{F}(t)>\dot{X}_{L}(t)
$$

Note that TTC is only valid when the speed of the following vehicle is higher than the leading vehicle.

## Modified TTC (MTTC)

To consider the motion variations during collision course, Ozbay et al. (2008), proposed a model in which the leading and the following vehicles' speeds are considered constant. The authors proposed the definition presented in Table 1 to indicate possible reasonable situations in which conflicts might occur that conventional TTC is unable to capture. Then, based on the equations of motion and constant acceleration assumption, the authors developed a new TTC, referred to as MTTC (Ozbay et al. 2008).

Determination of whether a conflict would occur is based on consideration of the trajectory parameters of the leading and following vehicles, including the relative distance, relative velocity, and relative acceleration. Thus, MTTC would be calculated as Equation 2:

$$
\dot{X}_{F} t+\frac{1}{2} \ddot{X}_{F} t^{2}=\left(X_{L}-X_{F}-l_{L}\right)+\dot{X}_{L} t+\frac{1}{2} \ddot{X}_{L} t^{2}
$$

Equation 2 can be rewritten as:

$$
\frac{1}{2}\left(\ddot{X}_{F}-\ddot{X}_{L}\right) t^{2}+\left(\dot{X}_{F}-\dot{X}_{L}\right) t-\left(X_{L}-X_{F}-l_{L}\right)=0
$$

MTTC is the real and non-negative solution of Equation 3.

## General formulation for TTC (GTTC)

In developing MTTC, it is assumed that acceleration (or deceleration) of the leading and following vehicles is constant. Saffarzadeh et al. (2013), considered this parameter in the TTC calculation process. Based on this new assumption, even cases that are identified as impossible conflicts in Table 1, would be considered rearend collisions. The authors suggested a theoretical formulation for TTC calculation if the $(\mathrm{k}-1)_{\mathrm{th}}$ derivative of speed is assumed to be constant, as shown in Equation 4 (Saffarzadeh et al. 2013):

$$
\left\{\begin{array}{l}
X_{F}=X_{0 F}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times \frac{\partial^{n} X_{F}}{\partial t^{n}} \times t^{n}\right) \\
X_{L}=X_{0 L}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times \frac{\partial^{n} X_{L}}{\partial t^{n}} \times t^{n}\right)
\end{array} \quad k=1,2,3, \ldots\right.
$$

Equation 5 is the necessary and sufficient condition for rear-end collision:

$$
X_{F}-X_{L}+l_{L}=0 \Leftrightarrow \text { Rear-end collision }
$$

Placing Equation 4 into Equation 5 results in $\mathrm{k}_{\text {th }}$ degree polynomial whose solution is $\mathrm{TTC}_{\mathrm{k}}$ :

$$
X_{0 F}-X_{0 L}+L_{L}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times\left[\frac{\partial^{n} X_{F}}{\partial t^{n}}-\frac{\partial^{n} X_{L}}{\partial t^{n}}\right] \times t^{n}\right)=0
$$

$\mathrm{TTC}_{\mathrm{k}}$ is the minimum, non-zero and real (non-complex) solution of Equation 6, (for t).

## Time exposed TTC (TET) and time integrated TTC (TIT)

Minderhoud and Bovy (2001), introduced two new extended indicators, Time Exposed Time-to-collision (TET) and Time Integrated Time-to-collision (TIT). These indicators are derived using trajectories and TTC profiles of all vehicles, over a specific length of a road and during a specific time period. If TTC* is considered to be the boundary between safe and unsafe situations,

Table 1. Possible Outcomes for a Pair of Vehicles in Car-following Process (Ozbay et al., 2008)
| $\dot{X}$ | $\dot{X}_{F}>\dot{X}_{L}$ |  |  | $\dot{X}_{F} \leq \dot{X}_{L}$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\ddot{X}$ | $\ddot{X}_{L}>0$ | $\ddot{X}_{L}<0$ | $\ddot{X}_{L}=0$ | $\ddot{X}_{L}>0$ | $\ddot{X}_{L}<0$ | $\ddot{X}_{L}=0$ |
| $\ddot{X}_{F}>0$ | $P$ | $C$ | $C$ | $P$ | $C$ | $P$ |
| $\ddot{X}_{F}<0$ | $P$ | $P$ | $P$ | 1 | $P$ | $l$ |
| $\ddot{X}_{F}=0$ | $P$ | $C$ | $C$ | 1 | $C$ | 1 |


Note: C=Conflict occurs; P=Possible Conflict; I=Impossible conflict with each other.
then the procedure to calculate each indicator is described as shown in the following subsections.

TET represents the duration of the exposition of safety-critical TTC values over a specified time duration. Thus, all of the instants in which the driver is following the leading vehicle, which $0<T T C<T T C^{*}$ must be summed. For a subject vehicle i, it is assumed that the measured TTC-values at an instant t do not change during a small time step $\tau_{S C}$ (e.g. 0.1 s). For the considered time period H, there are $T=H / \tau_{S C}$ time instants. Therefore, TET for vehicle i is computed as follows (Minderhoud and Bovy 2001):

$$
T E T_{i}=\sum_{t=0}^{T} \delta_{i}(t) \cdot \tau_{S C} \delta_{i}(t)=\left\{\begin{array}{cc}
1, & 0 \leq T T C_{i}(t) \leq T T C^{*} \\
0, & \text { otherwise }
\end{array}\right.
$$

In which $\delta$ is a switching variable and its value is 1 , when during an instant of following, TTC-value is between 0 and TTC*, and 0 in other cases.

Since TET does not consider the value of TTC below the critical threshold, TIT is introduced as an alternative measure. TIT uses the integral of TTC profile, so the value of TTC below TTC* is also considered in the calculation process. Equation 8 presents the estimation formula for TIT (Minderhoud and Bovy 2001):

$$
T I T_{i}=\sum_{t=0}^{T}\left[T T C^{*}-T T C_{i}(t)\right] \cdot \tau_{S C} \quad \forall 0 \leq T T C_{i}(t) \leq T T C^{*}
$$

Different TTC* values within the range of 2 to 5 s have been proposed to varying driving scenarios including out of control vehicles, vehicles under control, non-supported drivers, and supported drivers, among others (Hirst and Graham 1997; Hogema and Janssen 1996).

Minderhoud and Bovy also proposed Equations 9 and 10 to calculate the collision probability based on TET and TIT during a car-following situation of H seconds.

$$
\begin{gathered}
T E T P_{i}^{*}=\frac{T E T}{H} \\
T I T P_{i}^{*}=\frac{T I T_{i}}{H \cdot T T C^{*}}
\end{gathered}
$$

## Comprehensive time-based measure (CTM)

Behbahani et al. (2015), noticed that considering the rate of changes in the TTC profile for each vehicle can also be an effective parameter, which has not been included in either TET or TIT. The authors proposed a new indicator called Comprehensive timebased measure (CTM) as shown in Equation 11. This model has both the characteristics of TET and TIT and considers the rate of variation in TTC value (Behbahani, Nadimi, and Naseralavi 2014).

$$
\begin{aligned}
& \operatorname{CTM}_{i}(H)=\frac{\sum_{t=1}^{T} \frac{1}{3}\left(\left(\delta_{i}(t) \times \frac{\frac{\partial T T C_{i}(t)}{\partial t}}{70}\right)+\delta_{j}(t)\left(\frac{T I T(t)}{\tau \times T T C^{*}}+\frac{T E T_{i}(t)}{\tau}\right)\right)}{T} \\
& \delta_{i}(t)=\left\{\begin{array}{ll}
0 & \text { else } \\
1 & \forall \frac{\partial T T C(t)}{\partial t}<0
\end{array} \quad \delta_{j}(t)= \begin{cases}0 & \text { else } \\
1 & \forall 0<T T C_{i}(t)<T T C^{*}\end{cases} \right.
\end{aligned}
$$

## TTC for a moving line section and a point

Laureshyn, Svensson, and Hyden. (2010), suggested calculating TTC between two vehicles at any angle at which they could collide. The authors stated that in any possible collision, a corner of one of the vehicles touches one side of the other vehicle. Thus, a new concept for TTC is developed, which calculates TTC between a moving line section and a point. The procedure is presented below (Laureshyn, Svensson, and Hyden. 2010).

Consider the line with $\left(x_{1}, y_{1}\right)$ and $\left(x_{2}, y_{2}\right)$ as the coordinates of its endpoints and a point with current coordinates $\left(x_{p}, y_{p}\right)$. Based on equations of motion, the position of the specified point at an instant t will be as shown in Equation 12.

$$
\left\{\begin{array}{l}
x(t)=x_{p}+\dot{X}_{p} t \\
y(t)=y_{p}+\dot{Y}_{p} t
\end{array}\right.
$$

As in Equation 13, the coordinates of the line section ending after t seconds based on a constant speed motion are:

$$
\left\{\begin{array} { l } 
{ x _ { 1 } ( t ) = x _ { 1 } + X _ { \mathrm { ln } } \cdot t } \\
{ y _ { 1 } ( t ) = y _ { 1 } + Y _ { \mathrm { ln } } \cdot t }
\end{array} \text { and } \left\{\begin{array}{l}
x_{2}(t)=x_{2}+X_{\mathrm{ln}} \cdot t \\
y_{2}(t)=y_{2}+Y_{\mathrm{ln}} \cdot t
\end{array}\right.\right.
$$

The line Equation in canonical form with k as line slop is:

$$
x-x_{1}=\frac{y-y_{1}}{k}
$$

Assuming that the line moves parallel to itself, then k is constant and based on the initial coordinates of its endpoints:

$$
k=\frac{y_{2}-y_{1}}{x_{2}-x_{1}}
$$

TTC is calculated if replacing point coordinates (Equation 16) inline equation:

$$
T T C=\frac{\left(y_{p}\right)-k\left(x_{p}-x_{1}\right)}{\left(\dot{Y}_{p}-\dot{Y}_{\mathrm{ln}}\right)-k\left(\dot{X}_{p}-\dot{X}_{\mathrm{ln}}\right)}
$$

## Enhanced TTC (ETTC)

Kiefer, Leblanc, and Flannagan (2005), in a study on driver deceleration response to a crash alert, introduced a new definition for TTC called Enhanced Time-to-Collision (ETTC). ETTC assumes that leading and following vehicles do not change their respective courses until collision occurrence, but in this case, the leading vehicle continues to decelerate at the prevailing deceleration value until it stops. In addition, the following vehicle's acceleration at the moment of brake onset is assumed to be zero. Thus, the main difference between ETTC and conventional TTC is consideration of the deceleration behavior of the leading vehicle in the calculation process.

## Time to collision with disturbance (TTCD)

TTCD tries to determine the risk of rear-end collision, when a hypothetical disturbance is imposed on the leading vehicles. TTCD can be calculated in the scenarios where the speed of the following vehicles is not higher than the leading vehicle. In order to calculate TTCD, first, the deceleration rate imposed by the disturbance (d) and the critical deceleration $\left(\mathrm{d}^{\star}\right)$ must be calculated and compared. The procedure for calculating TTCD is as Equations 17 and 18 (Xie et al. (2018)).

$$
d^{*}=\frac{2 \dot{X}_{L} . \dot{X}_{F}-\dot{X}_{L}}{2\left(X_{L}-X_{F}-l_{L}\right)}
$$

$$
\left\{\begin{array}{l}
d \leq d^{*} \rightarrow \text { TTCD }=\frac{\left(\dot{X}_{L}-\dot{X}_{F}\right)+\sqrt{\left(\dot{X}_{L}-X_{F}\right)^{2}+2 d\left(X_{L}-X_{F}-l_{L}\right)}}{d} \\
d>d^{*} \rightarrow \text { TTCD }=\frac{2 d\left(X_{L}-X_{F}-l_{L}\right)+\dot{X}_{L}^{2}}{2 d \dot{X}_{F}}
\end{array}\right.
$$

Summary of review
Table 2 presents an overview of previous researches on modification of TTC.

TTC, MTTC, GTTC, TTCD, ETTC and TTC for a moving line and an object, units are second and all of them indicate the remaining time to a collision. TETP* and TITP* are between 0 and 1 and whatever the value is greater the collision probability is also more. CTM comprises TET and TIT characteristics and also is in the range of 0 to 1. In fact, CTM calculates the collision probability based on TTC. So, first, it must be determined which form of TTC is more appropriate and then we can apply CTM to determine the collision probability.

TTC, MTTC, and GTTC try to show the imminent danger of collision. Namely, when based on TTC, MTTC and GTTC the collision probability is high it means that we can expect a collision based on the present condition. But, when TTCD or ETTC indicates that a situation is critical it means that if a change would occur in motion characteristics of the involved vehicles then a collision might be expected.

Here we will just deal with the indicators which show the imminent danger of collision, so ETTC and TTCD would not be considered.

## Methodology

As mentioned earlier, there are various versions of TTC. However, due to the diversity found in the literature, it is difficult to decide how to use TTC in safety evaluations. Therefore, a framework is proposed for the application of TTC in detecting dangerous situations properly. In this framework, conflicts are divided into two categories: rear-end and angular. Rear-end conflicts often occur in car-following scenarios. Since in this category both vehicles have the same path and there are infinite potential collision points, these conflicts are excluded from angular conflicts. However, in angular conflicts, it should first be determined whether two vehicles have a common collision point, at which point TTC can be calculated.

To determine the type of the collision, the angle between the paths of two vehicles' movement must be established. The movement is considered as a vector in which the start and end of the vector are the coordinates of the vehicle in a previous time instant and the present, respectively. Table 3 shows the procedure for calculating the angle of each vehicle's movement with a horizontal axis.

When two vehicles are in the same lane, then the collision may be of the rear-end type. Otherwise, the collision might be angular and the angle of movement for each vehicle must be determined. The collision angle would be the absolute difference between angles of motion of two vehicles.

Consequently, the procedure for calculating TTC for rear-end and angular conflicts can be demonstrated.

## TTC for rear-end conflicts

When the angle of a potential collision is between -10 and +10 degrees and both vehicles are in the same lane, the conflict is considered to be rear-ended. In order to calculate TTC, the general framework proposed by Saffarzadeh et al. (2013), would be applied. However, the precise formulation (e.g. constant speed, constant deceleration) is applied based on motion characteristics of the previous moments. Then, TTC can be calculated as was shown in Equations 4 to 6.

## TTC for angular conflicts

Figure 1 shows a scenario in which an angular collision might occur. In these types of conflicts, it must be first determined

Table 2. Summary of previous researches on TTC modifications.
| TTC category | Methodological approach | Advantages | Disadvantages | Previous research |
| :--- | :--- | :--- | :--- | :--- |
| TTC | Introducing TTC based on constant speed for rear-end conflicts | Simple and comprehensible indicator | Ignoring changes in motion characteristics of vehicles during collision course | Hayward (1971) |
| MTTC | Considering acceleration in TTC calculation for rear-end conflicts (MTTC) | Considering the acceleration of vehicles during collision course | Ignoring other changes in motion characteristics of vehicles during collision course | Ozbay et al. (2008) |
| GTTC | Presenting a general formulation for TTC considering all possible variations in motion for rear-end conflicts (GTTC) | Considering all of the possible changes in motion characteristics of vehicles during collision course | Complicated for application | Saffarzadeh et al. (2013) |
| TET\&TIT | Considering duration and extent that a vehicle drives with dangerous TTCs for rear-end conflicts (TET\&TIT) | Appropriate for safety evaluations based on TTC for a time interval | Ignoring rate of changes occurred in TTC during car-following | Minderhoud and Bovy (2001) |
| CTM | Considering duration, extent and rate of changes of dangerous TTCs (CTM) | Appropriate for safety evaluations based on TTC for a time interval with more precision than TET\&TIT | The procedure for normalizing each part of the formulation is unknown | Behbahani et al. (2015) |
| TTC for a moving line and an object | Trying to develop a framework to calculate TTC for conflicts of different angles at constant speed | Appropriate for calculating collision probability based on TTC for sideswipe conflicts | Ignoring changes in motion characteristics of vehicles during collision course | Laureshyn, Svensson, and Hyden. (2010) |
| ETTC | Considering the deceleration behaviour of leading vehicle in the calculation process (ETTC) | Considering a more critical scenario than conventional TTC | Ignoring the real changes in motion characteristics of vehicles during collision course | Kiefer, Leblanc, and Flannagan (2005) |
| TTCD | Calculating TTC for car-followings where the following vehicle's speed is less than the leading vehicle. Also, considering a hypothetical disturbance for the leading vehicle. | Introducing an indicator for the cases in which a sudden reaction would be exerted by leading vehicle | It is not clear where TTCD must be applied | Xie et al. (2018) |


Table 3. Procedure for calculating the angle of motion for each vehicle.
| Coordinates of start of the vector | Coordinates of end of the vector | Condition | Angle |
| :--- | :--- | :--- | :--- |
| $\left(x_{1}, y_{1}\right)$ | $\left(x_{2}, y_{2}\right)$ | $\begin{aligned} & x_{2}>x_{1} \\ & y_{2}>y_{1} \\ & x_{2}<x_{1} \\ & y_{2}>y_{1} \\ & x_{2}<x_{1} \\ & y_{2}<y_{1} \\ & x_{2}>x_{1} \\ & y_{2}<y_{1} \end{aligned}$ | $\begin{gathered} \operatorname{arctg}\left\|\frac{y_{2}-y_{1}}{x_{2}-x_{1}}\right\| \\ \pi-\operatorname{arctg}\left\|\frac{y_{2}-y_{1}}{x_{2}-x_{1}}\right\| \\ \pi+\operatorname{arctg}\left\|\frac{y_{2}-y_{1}}{x_{2}-x_{1}}\right\| \\ 2 \pi-\operatorname{arctg}\left\|\frac{y_{2}-y_{1}}{x_{2}-x_{1}}\right\| \end{gathered}$ |


whether there is a collision point between vehicles. For this purpose, the type of motion for each vehicle is determined based on previous moments for each time step in x and y directions. This results in two sets of Equations:

$$
\begin{aligned}
& \left\{\begin{array}{l}
X_{S}=X_{0 S}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times \frac{\partial^{n} X_{S}}{\partial t^{n}} \times t^{n}\right) \\
Y_{S}=Y_{0 S}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times \frac{\partial^{n} Y_{S}}{\partial t^{n}} \times t^{n}\right)
\end{array} \quad k=1,2,3, \ldots\right. \\
& \left\{\begin{array}{l}
X_{C}=X_{0 C}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times \frac{\partial^{n} X_{C}}{\partial t^{n}} \times t^{n}\right) \\
Y_{C}=Y_{0 C}+\sum_{n=1}^{k}\left(\frac{1}{n!} \times \frac{\partial^{n} Y_{C}}{\partial t^{n}} \times t^{n}\right)
\end{array} \quad k=1,2,3, \ldots\right.
\end{aligned}
$$

To specify the collision point, the procedure shown in Figure 2 is applied.

If there is a common collision point between two vehicles, TTC for the subject vehicle is calculated as shown in Figure 3.

Now, there would be a complete framework in which almost all previous modifications on TTC are considered. All types of conflicts are considered based on the angle of collision which would be calculated automatically. Motion characteristics of vehicles would be involved in the calculation procedure. After calculating TTC, then CTM can be applied to calculate the risk of driving at each moment and also in a time interval based on a specific TTC*.

In order to compare the results, Analysis of Variances (ANOVA) is applied. Mean differences for CTMs calculated based on TTC, DTTC, and GTTC are compared by ANOVA in car-following scenarios. Also, t-test is applied to compare the results of CTM

![](https://cdn.mathpix.com/cropped/13b8b760-0483-4a1b-bc48-97b7b7c5c8f4-06.jpg?height=655&width=833&top_left_y=1912&top_left_x=174)
Figure 1. Schematic of an angular collision.

calculated by TTC proposed in this paper and what has been proposed by Laureshyn, Svensson, and Hyden. (2010).

## Application of the proposed methodology

In this section, the application of the new methodology for calculating TTC is demonstrated for two scenarios: car-following and lane-changing. The procedure is evaluated using real-world data for a group of vehicles.

To collect microscopic traffic data, a vantage point is required for video recording. For this purpose, Tabiat Bridge in Tehran was selected for the present study. Tabiat Bridge in the Abbas Abad region of Tehran is a three-level bridge designed for pedestrians. The bridge passes through Modares highway and connects two parks: Taleghani in the east and Ab'o 'Atash in the west. The bridge height to the surface of the highway is approximately 40 m (131 feet). Figure 4 displays the site in which the study has been conducted.

Data collection was conducted between 9:00 and 11:00 in April 2015. Finally, for a length of approximately 400 m, the trajectory of each vehicle (including longitudinal and transverse coordinates) is provided in 0.1 s frames using TRAZER software developed by Kritikal Solution. Accordingly, other relevant information including speed, time headway, and TTC among other factors is calculated. In Table 4 a summary is presented about data collection.

As we want to compare TTC calculated based on different approaches, car-following, and lane-changing scenarios are first specified and extracted from these data. Lane-changings and carfollowing situations are susceptible to angular and rear-end conflicts, respectively.

## Car-following scenarios

In these scenarios, two vehicles follow each other for at least 10 s in the same lane. Each time instant is 0.1 s. In each time step, the motion characteristics are known based on the coordinates of the two vehicles. To compare TTC, MTT, GTTC different types of motion have been selected in the collected data as shown in Table 5.

TTC, MTTC, and GTTC are calculated during the carfollowing process. Since the conflict is rear-ended, the new procedure is the same as GTTC (Equations 4 to 6).

In addition, CTM is calculated for the car-following scenarios based on TTC, MTTC, and GTTC. Now ANOVA is applied to compare the results of CTM calculated based on different TTCs. The results are demonstrated in Table 5.

As can be deduced from Table 6, the null hypothesis can be rejected by 95\% confidence. Therefore, we conclude that there is a great difference between the CTM calculated by GTTC, MTTC, and TTC. This difference will affect the accuracy and efficiency of IVCAW, which might be dangerous.

## Lane-changing scenarios

To calculate TTC based on the new proposed methodology, first, angles for each vehicle must be calculated based on the information presented in Table 3.

Based on the flowcharts shown in Figures 2 and 3, the projected collision point and TTC for angular conflict can be determined. In addition, CTM for the lane-changing vehicles is calculated based on $\mathrm{TTC}^{\star}=2$. The lateral acceleration and steering are ignored during the angular collision and CTM is calculated by equation 11. However, angular TTCs calculated by Figure 3 would be applied.

![](https://cdn.mathpix.com/cropped/13b8b760-0483-4a1b-bc48-97b7b7c5c8f4-07.jpg?height=2009&width=1264&top_left_y=179&top_left_x=426)
Figure 2. Flowchart to determine the projected collision point for two vehicles.

Now t-test is conducted to compare CTM results calculated by TTCs obtained based on the methodology proposed in this paper and what has been illustrated in section 2.6 by Laureshyn, Svensson, and Hyden. (2010). Again by 95\% confidence, the null hypothesis would be rejected. Therefore, it can be deduced that there is a great difference between the CTM results obtained by these two methods. Namely, considering motion characteristics of each vehicle to calculate TTC can be important to obtain more precise values.

Time-to-collision (TTC) is one of the most important SSMs and different modifications have been done on this indicator. Now it is relatively hard to decide about the suitable version of TTC for safety evaluations. This paper tries to have a thorough review of TTC and its changes. It can be declared that ETTC

![](https://cdn.mathpix.com/cropped/13b8b760-0483-4a1b-bc48-97b7b7c5c8f4-08.jpg?height=2379&width=934&top_left_y=179&top_left_x=590)
Figure 3. Calculation of TTC for angular conflicts.

![](https://cdn.mathpix.com/cropped/13b8b760-0483-4a1b-bc48-97b7b7c5c8f4-09.jpg?height=1587&width=1268&top_left_y=181&top_left_x=424)
Figure 4. Overview of the site for data collection.

Table 4. Descriptive analysis of data.
| Volume (veh/hr) |  |  | Analysis period (hr) | Length of study (m) | Average speed (km/ hr) | Number of lanes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Passenger car | Motorcycle | Truck | 2 | 400 | 73.8 | 4 |
| 4536 | 2568 | 642 |  |  |  |  |


Table 5. Motion characteristics of car-following scenarios.
| Following vehicle | Leading vehicle |
| :--- | :--- |
| Constant speed | Constant speed |
| Constant jerk | Constant jerk |
| Constant acceleration | Constant acceleration |
| Constant deceleration | Constant deceleration |


and TTCD are suitable to consider the worst-case scenarios during car-following for safety evaluations. GTTC can consider the variations in the motion characteristics of vehicles. Therefore, the results of GTTC are more realistic than the

Table 6. ANOVA outputs to compare CTM means in car-following scenarios.
|  | Sum of squares | df | Mean square | F | Sig. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Between groups | 0.005 | 2 | 0.002 | 39.931 | 0.000 |
| Within groups | 0.009 | 147 | 0.000 |  |  |
| Total | 0.013 | 149 | 0.000 |  |  |


conventional definition of TTC and MTTC. A framework is also proposed to determine the angular conflicts and then calculating TTC. In this framework again the motion characteristics of vehicles are considered to have more realistic results. In all, it can be declared that the proposed method might improve the workability of IVCAWS.

The main limitation of this study relates to testing all versions of TTC for IVCAWS activation in the real world for instrumented vehicles. This procedure might help to obtain more profound results about the application of each type of TTC and the role of each TTC for safety evaluations.

## Conclusion

In the near future, self-driving vehicles will be a common term in automotive literature. However, the main challenge facing the safe operation of these vehicles is the detection and prevention of collisions with objects or other vehicles in a traffic stream. Invehicle collision avoidance warning systems (IVCAWS) could help reduce the risk of collision. To activate such systems a warning strategy must first be defined. Time-to-Collision is a time-based indicator which can be useful as a surrogate safety measure. Up until now, various changes have been made to this indicator to improve its reliability in collision prediction. As a result, a confusion has arisen regarding which version of TTC is most suitable for application in collision probability perdition. For this paper, first, a review on TTC improvements was conducted. Next, a general framework was proposed to calculate TTC. Using this framework, based on the coordinates of each vehicle, its angle with the horizontal axis is determined. Then, if the angles of the involved vehicles are not too dissimilar, the conflict would be rearended, otherwise, it would be angular. The type of motion for each vehicle at each time instant is then determined (e.g., constant speed, constant acceleration, constant jerk and among others). Using dynamics laws at each time step, and based on the type of collision and motion, TTC can be calculated. The procedure was evaluated for car-following and lane-changing scenarios and compared with previous versions of TTC. Based on the results, application of the new procedure to calculate TTC is shown to be helpful, in particular for IVCAWS, since using just the coordinates of the involved vehicles, TTC can be dynamically and automatically calculated at each time-step. In addition, this framework might increase the capabilities of IVCAWS in detecting collision risk, since it determines the type of conflict and motion automatically and then applies relating formulations to calculate potential risk.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## References

Archer, J. 2005. "Indicators for Traffic Safety Assessment and Prediction and Their Application in Micro-simulation Modeling: A Study of Urban and Suburban Intersections." Ph.D. thesis.,Royal Institute of Technology.
Babu, S. S., and P. Vedagiri. 2018. "Proactive Safety Evaluation of a Multilane Unsignalized Intersection Using Surrogate Measures." Transportation Letters: the International Journal of Transportation Research 10 (2): 104-112. doi:10.1080/19427867.2016.1230172.
Barcelo, J., L. Montero, J. Perarnau, and A. Torday. 2003. "Safety Indicators for Micro-simulation Based Assessments." In: 82nd Annual meeting of the Transportation Research Board, Washington, D.C, USA.
Behbahani, H., A. Mohammadian Amiri, N. Nadimi, and D. R. Ragland. 2019. "Increasing the Efficiency of Vehicle Ad-hoc Network to Enhance the Safety Status of Highways by Artificial Neural Network and Fuzzy Inference System". Journal of Transportation Safety\&Security Published online..
Behbahani, H., N. Nadimi, H. Alenoori, and M. Sayadi. 2014. "Developing a New Surrogate Safety Indicator Based on Motion Equations." Promet Traffic \& Transportation 26 (5): 371-381. doi: 10.7307/ptt.v26i5.1388.
Behbahani, H., N. Nadimi, and S. Naseralavi. 2014. "New Time-based Surrogate Safety Measure to Assess Crash Risk in Car-following Scenarios." Transportation Letters: the International Journal of Transportation Research 7 (4): 229-239. doi:10.1179/ 1942787514Y.0000000051.
Ben Yaakov, A., M. Maltz, and D. Shinar. 2002. "Effects of an In-Vehicle Collision Avoidance Warning System on Short- and Long-Term Driving Performance." Human Factors 44 (2): 335-342. doi:10.1518/ 0018720024497925.
Brian, L., T. Shin, and P. J. Cooper. 1978. "Analysis of Traffic Conflicts and Collisions." Transportation Research Record: Journal of the Transportation Research Board 667: 67-74.
Charly, A., and T. V. Mathew. 2019. "Evaluation of Driving Performance in Relation to Safety on an Expressway Using Field Driving Data." Transportation Letters: the International Journal of Transportation Research Published online. doi:10.1080/19427867.2019.1591075.
Cooper, P. J. 1983. "Experience with Traffic Conflicts in Canada with Emphasis on "post Encroachment Time" Techniques." In Proceedings of the NATO Advanced Research Workshop on International Calibration Study of Traffic Conflict Technique.
Craveiro, C. F. J. 2008. "Assessing Safety Performance of Transportation Systems Using Microscopic Simulation." Ph.D. thesis.,Department of Civil Engineering, Waterloo, Canada.
Gettmann, D., and L. Head. 2003. "Surrogate Safety Measures from Traffic Simulation Models." Technical report, Federal Highway Administration - FHWA.
Global Status Report on Road Safety (WHO). 2018. Switzerland: Department of Violence \& Injury Prevention \& Diability, World Health Organization, Department of Violence Injury Prevention Disability (VIP). www.WHO.int/ violence_injury_prevention
Gousios, S., and N. J. Garber. 2009. "Relationship between Time to Collision Conflicts and Crashes on Interstate Highways Subjected to Truck Lane Restrictions." 88th Annual Meeting of the Transportation Research Board, Washington, D.C.
Hayward, J. 1971. "Near Misses as a Measure of Safety at Urban Intersections." Ph.D. thesis.,Department of Civil Engineering, The Pennsylvania State University, University Park, PA.
Hirst, S., and R. Graham. 1997. "The Format and Presentation of Collision Warnings." In Ergonomics and Safety of Intelligent Driver Interfaces, edited by Y. I. Noy. New Jersey: Lawrence, Y.I. Noy (Ed.).
Hogema, J. H., and W. H. Janssen. 1996. "Effects of Intelligent Cruise Control on Driving Behavior." Report TM-1996-C-12, Soesterberg, the Netherlands: TNO Human Factors.
Kiefer, R. J., D. J. Leblanc, and C. A. Flannagan. 2005. "Developing an Inverse Time-to Collision Crash Alert Timing Approach Based on Drivers' Lastsecond Braking and Steering Judgments." Accident Analysis and Prevention 37: 295-303. doi:10.1016/j.aap.2004.09.003.
Laureshyn, A., A. Svensson, and Hyden. 2010. "Evaluation of Traffic Safety, Based on Micro-level Behavioral Data: Theoretical Framework and First Implementation." Accident Analysis and Prevention 42 (6): 1637-1646. doi:10.1016/j.aap.2010.03.021.
Minderhoud, M. M., and P. H. L. Bovy. 2001. "Extended Time-to-collision Measures for Road Traffic Safety Assessment." Accident Analysis and Prevention 33: 89-97.
Ozbay, K., H. Yang, B. Bartin, and S. Mudigond. 2008. Derivation and Validation of New Simulation-Based Surrogate Safety Measure, 105-113. Transportation Research Record.
Parsa, A. B., H. Taghipour, S. Derrible, and A. K. Mohammadian. 2019. "Realtime Accident Detection: Coping with Imbalanced Data." Accident Analysis \& Prevention 129: 202-210. doi:10.1016/j.aap.2019.05.014.
Reddy, K. A., S. Chepuri, A. S. Arkatkar, and G. Joshi. 2019. "Developing proximal safety indicators for assessment of un-signalized intersectiona case study in Surat city." Transportation Letters: The international journal of transportation research published online.
Saffarzadeh, M., N. Nadimi, S. Naseralavi, and A. Mamdoohi. 2013. "A General Formulation for Time-to-Collision Safety Indicator." Proceedings of the Institution of Civil Engineers Journal-Transport (5): 294-304.
Sagberg, F. 2018. "Characteristics of Fatal Road Crashes Involving Unlicensed Drivers or Riders: Implications for Countermeasures." Accident Analysis \& Prevention 117: 270-275. doi:10.1016/j.aap.2018.04.025.
Sobhani, A., W. Young, M. Sarvi, and S. Bahrololoom. 2013. "Calculating Time-To-Collision for Analyzing Right Turning Behavior at Signalized Intersections." Road and Transport Research 22 (3): 49-61.
Strauss, J., S. Zangenehpour, L. F. Miranda-Moreno, and N. Saunier. 2018. "Cyclist Deceleration Rate as Surrogate Safety Measure in Montreal Using Smartphone GPS Data." Accident Analysis and Prevention 99: 287-296. doi:10.1016/j.aap.2016.11.019.
Sundfør, H. B., F. Sagberg, and A. Høye. 2019. "Inattention and Distraction in Fatal Road crashes-Results from In-depth Crash Investigations in Norway." Accident Analysis \& Prevention 125: 152-157. doi:10.1016/j.aap.2019.02.004.
Tageldin, A., and T. Sayed. 2015. "Can Time Proximity Measures Be Used as Safety Indicators in All Driving Cultures?" A Case Study of Motorcycle Safety in China 2520: 165-174.
Van Der Horst, R., and J. Hogema. 1993. "Time-to-Collision and Collision Avoidance Systems." Proceedings of the 6th ICTCT Workshop: Safety

Evaluation of Traffic Systems: Traffic Conflicts and Other Measures, Salzburg: Austria.
Xie, K., D. Yang, K. Ozbay, and H. Yang. 2018. "Use of Real-world Connected Vehicle Data in Identifying High-risk Locations Based on a New Surrogate Safety Measure". Accident Analysis and Prevention Article in Press.
Young, W., A. Sobhani, M. Lenne', and M. Sarvi. 2014. "Simulation of Safety: A Review of the State of the Art in Road Safety Simulation Modelling." Accident Analysis and Prevention 66: 89-103. doi:10.1016/j.aap.2014.01.008.
Zhao, P., and C. Lee. 2018. "Assessing Rear-end Collision Risk of Cars and Heavy Vehicles on Freeways Using a Surrogate Safety Measure." 113: 149-158.

