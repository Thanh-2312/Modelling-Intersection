# Investigating impacts of various operational conditions on fuel consumption and stop penalty at signalized intersections 

Suhaib Alshayeb ${ }^{\mathrm{a}, *}$, Aleksandar Stevanovic ${ }^{\mathrm{a}}$, Justin R. Effinger ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}}$ Department of Civil and Environmental Engineering, University of Pittsburgh, Pittsburgh, PA, USA<br>${ }^{\mathrm{b}}$ NoTraffic: Palo Alto, CA 94306, USA

## ARTICLE INFO

Article history:
Received 12 January 2021
Received in revised form 12 August 2021
Accepted 28 September 2021
Available online 8 October 2021

Keywords:
Fuel consumption
Signalized intersections
Stops
Performance index
Stop penalty


#### Abstract

When optimizing signals relevant traffic agencies adopt policies to either improve mobility performance measures (e.g., delay and stops), environmental aspects, or safety of signalized intersections. One of such policies, mainly implemented through so-called Performance Index (PI), advocates that reduction of excess fuel consumption (FC) should be achieved by minimizing the PI - a linear combination of delays and stops. The key factor of such a PI is the stop penalty "K", which represents a weighting factor, or a stop equivalency measured in seconds of delay. In the contemporary signal optimization practice, this K is given a constant value (e.g., 10 seconds) and it is not recognized as a parameter that is dependent on various operational conditions. This study challenges that common view and presents a methodology to derive the K factor and investigate impacts of various operational conditions (e.g., cruising speed) on the K value. The study uses traffic simulation model coupled with a modal fuel consumption and emission model to investigate second-by-second FC during stopping events at a signalized intersection. The experiments are performed on a hypothetical, yet realistic, intersection under several operational scenarios. The findings show that the K varies significantly with all the investigated operational conditions. More importantly, results indicate that the K factor should be much larger than used by current signal timing practices. The implications of these findings may lead to significant changes in current polices for signal timing optimization. Future research shall validate these findings with second-by-second vehicle trajectory and FC data from the field.


© 2021 Tongji University and Tongji University Press. Publishing Services by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/ licenses/by-nc-nd/4.0/).

## 1. Introduction

Fuel consumption (FC) from the transportation sector accounts for about $30 \%$ of total US greenhouse emissions (EPA, 2019). Intersections along urban arterials contribute significantly to those 30\% because they entail queuing conditions and many stop-and-go events, making intersections one of the primary spots where excess fuel is consumed. The increase in FC also brings harmful impacts to the environment, contributing to climate change by increasing outputs of carbon dioxide ( $\mathrm{CO}_{2}$ ) in the Earth's atmosphere and to human health by increasing levels of particulate matter (PM) and other harmful pollutants (McMichael et al., 1996).

[^0]Multiple studies have confirmed that traffic signal optimization is one of the effective ways to increase the capacity of existing urban networks (Webster, 1958; Robertson, 1969; Sunkari, 2004). The prevailing method to optimize traffic signals (to achieve efficient traffic movements on urban arterials) is by minimizing delay and the number of stops. Prior research studies substantiate a belief that minimizing number of stops reduces FC, considering that most of the excess fuel is consumed during deceleration-acceleration phases of a stopping event (Rakha and Ding, 2003; El-Shawarby et al., 2005). However, while minimizing delay does not necessarily minimize number of stops, it does reduce FC of vehicles when their engines idle during the waiting time in a queue.

The oil crisis of the early '70 s attracted a few researchers to address how signalized intersections can be accommodated to minimize FC. Consequently, a few studies assessed the impact of cycle length on FC. Bauer, (1975), Courage and Parapar, (1975), and Hurley and Ball (1979) showed that the cycle length required to minimize FC is longer than the one needed to minimize delay. Hence a balance between delay and number of stops should be made not only to balance between mobility metrics (delay and stop), but also to reduce FC. In contrast, Cohen and Euler, (1978) concluded that delay, FC, and emissions are all minimized at the same cycle length value. Nevertheless, these research efforts were based on field measurements without identifying factors (e.g., speed, grade, driving behavior), which impact extra FC from stopping at signalized intersections (Claffey, 1971; Claffey, 1977).

Several studies (Kwak et al., 2012; Liao 2013; Zhao et al., 2018) proposed optimization models to find a right balance between delay and number of stops when optimizing traffic signal settings. However, the Performance Index [PI = Delay + K (number of stops)] developed by Robertson, 1969 is still one of the most popular objective functions, and heavily used in the contemporary traffic signal optimization practice (Husch and Albeck, 2006). One of the reasons for such a wide use of the PI is that it can be adjusted to achieve an optimal outcome for one of the three primary performance measures used in most of the traffic signal retiming policies: delay, number of stops, and FC. The PI enables policy makers to define how much weight (known as a $K$ factor or stop penalty) to give to each of these measures, to achieve the optimal traffic signal operations. A value of zero $K$ is used when only delay is supposed to be minimized. In contrast, positive values of $K$ add a penalty (measured as an equivalent delay) for each stop due to signal operations. For example, Robertson, 1969 used a $K$ factor of 8 seconds in his original study. However, he concluded that the $K$ value could be chosen to achieve any desired balance between delay and number of stops.

The utilization of the stop penalty ( $K$ ) to reduce FC was proposed by a few studies (Courage and Parapar, 1975; Robertson et al., 1980; Akcelik, 1981). In that case, the $K$ value represents a weighting factor of a number of seconds of delay equivalent to a stop from a fuel-consumption perspective. Courage and Parapar, (1975) and Akcelik, (1981) defined $K$ factor in a way that it depends on the fuel consumed during the deceleration, idling, and acceleration phases of a stop-and-go event (discussed later). Hence, one could conclude that factors impacting FC during the driving phases of a stop-and-go event (e.g., vehicle type, fleet distribution, and road gradient) also impact the $K$ value.

To the best of our knowledge, there have not been research efforts to address individual impact of various operational conditions (road and driving) on the $K$ value. Moreover, both studies (Courage and Parapar, 1975; Akcelik, 1981) that computed $K$ factor did not provide an exact analytical expression on how to calculate the $K$ value. Therefore, our study addresses these shortcomings by presenting a comprehensive methodology to derive the $K$ factor and by investigating the impact of various operational conditions factors on $K$ value. To test the proposed methodology, traffic simulation Vissim (PTV, 2020) was used to generate vehicles' trajectories from a set of scenarios with various operational conditions, which were then used to estimate FC from the Comprehensive Modal Emission Model (CMEM) (An et al., 1997). The results constitute a basis for further research, which aims to develop a new methodology to properly integrate various $K$ values into signal timing optimization practice to address environmentally driven signal retiming policies.

The rest of the paper is organized as follows: Section 2 describes the relevant literature. Section 3 presents the major operational conditions which impact vehicular FC and the K value. Section 4 presents the methodology. Section 5 discusses the experimental results, whereas Section 6 summarizes the study and provides conclusions.

## 2. Literature review

This section summarizes the most relevant studies addressing the computation and evaluation of the $K$ factor and gives an overview of a few other studies that proposed similar performance indices to the one developed by Robertson, 1969. It should be noted that none of the studies reviewed below have explicitly provided a mathematical expression to compute the $K$ factor. Therefore, all equations provided here are our interpretations of how they calculated the $K$ factor, based on the descriptions provided by those studies.

Courage and Parapar, (1975) used TRANSYT model and its PI objective function (Robertson, 1969) to investigate the impact of cycle length on two groups of PIs - those that reduce delay and those that reduce FC. The authors calculated the $K$ value by dividing the fuel consumed per one-stop (including FC during deceleration, idling, and acceleration phases) by the fuel consumed during one hour of idling converted to one second as shown in Equation (1).

$$
K=3600 \cdot\left(\frac{F C_{S}}{F C_{I}}\right)
$$

where: $K$ is stop penalty [seconds], $F C_{S}$ is fuel consumption per vehicle stop [gallon], $F C_{I}$ is fuel consumption per vehicle-hour idling [gallon/veh-hour], and 3600 is a conversion factor to obtain $K$ value equivalent to a number of seconds (instead of hours) of delay from FC perspective. Courage and Parapar, (1975) computed the stop penalty using fuel measurements collected in field by Claffey, (1971) for 30 -mph cruising speed and level terrain. As a result, a constant $K$ value of 60 seconds was derived and used to compute the PI. The same authors recognized the impact of various speeds on the $K$ factor, but they assumed that such impacts can be neglected. Their conclusion could be attributed to the fact that they did not possess high-resolution trajectory and FC data. In summary, their research showed an apparent trade-off between travel delay and FC in the signal optimization problem, which can be achieved by adjusting the $K$ value.

Robertson et al., (1980) investigated the impact of various $K$ values (0, 2, 5, 10, 20, 50, and 100 seconds) on the delay and FC on several coordinated signals in Glasgow. The authors found that FC can be reduced by 6-8\% when signals are optimized to reduce delay, exclusively $(K=0)$. They also recommended fuel consumption-driven $K$ of 20 seconds to make a proper trade-off between delay and stops and achieve an additional 3\% reduction in FC with no tangible increase in delay. This influential work set the stage for PI to become a standard performance measure not only when FC minimization is sought but in general when signal timings are optimized (Husch and Albeck, 2006; PTV, 2014; Shayeb et al., 2021). The main drawback of this research's conclusion is that it did not consider or mention the impact of other operational and driving factors on the $K$.

Akcelik, (1981) rederived the $K$ by dividing the FC during deceleration and acceleration phases by the idling fuel rate during the stopped delay time at the signal as shown in Equation (2). It should be noted that he subtracted excess fuel consumed due to delay contribution of the deceleration and acceleration phases of the stopping event. This approach seems slightly more accurate from the other efforts (e.g., by Courage and Parapar, 1975) because it made a better distinction between stops and delay through their equivalent FCs. This distinction was not 100\% accurate because Akcelik, (1981) combined FC associated with delay caused by the deceleration and acceleration and FC during idling (stopped delay). Deriving the $K$ factor in this way was mainly driven by the need to combine FCs from all delays to suit the FC model proposed in the same study. The $K$ value was derived for three fleet distributions (light vehicles, heavy vehicles, and composite fleet with 10\% of heavy vehicles) and a cruising speed of 60 km/h, which resulted in $K$ values of 54, 104, and 60 seconds, for the three respective fleet distributions.

$$
K=3600 \cdot\left(\frac{F C_{S}-\left(F C_{I} \cdot d_{s}\right)-\left(F C_{I} \cdot d_{h}\right)}{F C_{I}}\right)
$$

Where: $K$ is stop penalty [seconds], $F C_{S}$ is fuel consumption per vehicle stop [liter], $F C_{I}$ is fuel consumption per vehiclehour idling [liter/veh-hour], $d_{s}$ is stopped delay [hour], $d_{h}$ is deceleration-acceleration delay [hour], and 3600 is a conversion factor to obtain $K$ factor in seconds. Akcelik, (1981) used Equation (2) to calculate $K$ factor based on various field measurements of FC from different studies (Claffey, 1971; Claffey, 1977; Courage and Parapar, 1975; Dart and Mann, 1978; Robertson et al., 1980). He found that $K$ value varies from 26 to 228 seconds. Such a wide range can be explained by the fact that various elements that impact FC at a signalized intersection were included in various data sets but not recognized as such. For example, while the value of $K$ strongly depends on the vehicle type and vehicle engine, it is also a function of other factors (e.g., driving behavior/aggressiveness, road gradient, cruising speed).

In the past few decades, various performance indices (like the one developed by Robertson, (1969)) have been proposed. Reljic et al. (1992) proposed a PROMETHEE-based optimization procedure to optimize signal plans for various objective functions, including a fuel-consumption function as a linear combination of delays and stops, with a $K$ value equal to 20 seconds, as recommended by (Robertson et al., 1980). Oda et al. (2004) optimized signals to reduce $\mathrm{CO}_{2}$ using the same PI from Robertson (1969), but with weights applied both for delay and number of stops, instead of just one weight for the number of stops. Li et al. (2004) developed an optimization model to minimize a newly proposed performance index as a weighted sum of three objectives: delay, FC, and emissions. Although those last two studies (Oda et al., 2004; Li et al., 2004) extended the concept of weighting stops against delay, they did not derive or mention how much weight should be given to each stop in terms of FC or emissions.

To summarize, several studies considered this topic before but none of them made any comprehensive efforts to investigate what factors could have impact on the stop penalty and FC at signalized intersections. Moreover, various signal timing policies claim that reducing fuel consumption is one of the primary goals of traffic signal optimization (Gordon, 2010; Urbanik et al,2015). However, using a low and constant value of the $K$ factor, makes such policies unsubstantiated. To address these shortcomings in the body of existing knowledge, this paper addresses that matter by exploring the individual influences of various operational conditions (vehicle type, fleet distribution, driving behavior, road gradient, cruising speed, and wind effect) on the stop-related FC and $K$ factor.

## 3. Major factors impacting Stop-Related fuel consumption

Vehicular FC depends on numerous factors (Claffey, 1971; Redsell et al., 1993) which can be broadly classified in six categories: vehicle-related, traffic-related, travel-related, driver-related, roadway related, and weather-related factors (Ahn et al., 2002). In the recent years, few studies (Mock, 2012; Zhou et al. 2016) attempted to define further subcategories, summarized in Fig. 1, and their impact on FC. According to those impacts, the major factors affecting FC during a stop at a sig-

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-04.jpg?height=407&width=1386&top_left_y=185&top_left_x=250)
Fig. 1. Factors impacting vehicular fuel consumption.

nalized intersection considered in this study are summarized below. It should be noted that the list of factors selected is not inclusive and it presents factors with major impact on FC caused by stopping at signalized intersection.

1. Distribution of vehicular types and engines: vehicle mass, engine power, fuel used per engine's displacement, and the engine efficiency (to transfer the power to the wheels) are important factors affecting FC during acceleration (National Research Council, 2011). With all other factors being equal, higher vehicle masses and ability to achieve faster acceleration increase FC, which increases the value of $K$.
2. The proportion of heavy vehicles in fleet distribution: as the amount of fuel consumed depends on the vehicle type and engine, it is logical to expect that vehicular fleets composed of various proportions of light-duty vehicles (LDVs) and heavy-duty diesel vehicles (HDDVs) will result in different FCs, hence yielding to a variety of $K$ values (Alshayeb et al., 2021).
3. Driver's behavior: the amount of fuel consumed depends significantly on the individual driver's driving habits. Injection of an extra (fuel/gasoline) into the engine occurs when one applies a sudden momentary thrust with the acceleration pedal (Claffey, 1977). Such behavior will, therefore, cause higher FC during the acceleration phase, resulting in a higher $K$.
4. Road gradient: fuel generally increases when vehicles travel uphill and have to combat gravity. On the other hand, potential energy is added to the engine's kinematic energy when traveling downhill; thus, less fuel is required for downhilltravelling vehicles to achieve the cruising speed (Claffey, 1971), resulting in a lower $K$.
5. Cruising speed: additional fuel needed to accelerate to the original speed of travel depends principally on the original cruising speed, which is a factor of the speed limit. For a stopping event, a deceleration from a higher speed to zero, followed by acceleration again to the original cruising speed, yields to a higher excess FC (Rakha and Ding, 2003; Stevanovic et al., 2021) (resulting in a higher $K$ ) than when the original speed is lower.
6. Wind effect: wind also impacts effective speed of a moving vehicle, based on its direction (components of headwind and tailwind) and intensity. A vehicle accelerating upwind/downwind will consume more/less fuel than a vehicle accelerating without wind. This effect is most profound for trucks, whose FCs can vary remarkably in conditions with either headwind or tailwind (Heide and Mohazzabi, 2013). This study only considers the impact of wind on FC of heavy vehicles.

## 4. Methodology

When a vehicle stops at a signalized intersection, it must go through three driving phases. Firstly, the vehicle decelerates from its original cruising speed to zero (deceleration phase). Secondly, the vehicle waits for the signal to turn green, during which time the vehicle's engine idles (idling phase). Thirdly, once the signal turns green, the vehicle accelerates from zero to its cruising speed (acceleration phase). Those three phases form the concept of the "Cruising Speed Stop Profile" (CSSP), where cruising speed after acceleration is assumed to be the same as before the deceleration phase. Fig. 2c) shows three of such profiles for cruising speeds of 30, 40, and 45 mph. It can be stated that for a CSSP, the total amount of fuel consumed is:

$$
F C_{C S S P}=F C_{D}+F C_{I}+F C_{A}
$$

Where:
$\mathrm{FC}_{\text {CSSP }}$ - total fuel consumed during a CSSP [gallons, liters, or grams].
$\mathrm{FC}_{\mathrm{D}}$ - fuel consumed during the deceleration phase; [same unit as $\mathrm{FC}_{\text {CSSP }}$ ].
$\mathrm{FC}_{\mathrm{I}}$ - fuel consumed during the idling phase; [same unit as $\mathrm{FC}_{\text {CSSP }}$ ].
$\mathrm{FC}_{\mathrm{A}}$ - fuel consumed during the acceleration phase; [same unit as $\mathrm{FC}_{\text {CSSP }}$ ].

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-05.jpg?height=2146&width=1406&top_left_y=206&top_left_x=242)
Fig. 2. Dynamics and kinematics of vehicular stops at a 45-mph cruising speed.

Fig. 2 shows other relevant profiles of a vehicle making a stop at a signalized intersection. Fig. 2a) shows a vehicular trajectory in a time-distance domain. Fig. 2c) and 2e) show how speed and acceleration vary over time during a CSSP, respectively. Finally, Fig. 2g) depicts the most interesting relationship - how instantaneous FC changes over time during a CSSP. This part of Fig. 2 will be in our focus to explain how such a CSSP can be used to accurately compute the relevant $K$ factor. It should be noted that although Fig. 2a), 2c), 2e), and 2 g) represent trajectory and relevant data for a simulated vehicle, such data series are very similar to the actual field data as shown in Fig. 2b), 2d), 2f), and 2 h).

Fig. 2g) and 2 h) show that stopping at an intersection will also induce FC during the idling phase, but this part of the FC should be attributed to the concept of stopped delay, as it is important to separate 'delays' from 'stops', the two commonly used traffic performance measures for signalized intersections. Such a separation is needed because the delay during idling (or waiting time) in queue at traffic signal (referred to as stopped delay hereafter) can be extended over a long time depending on the red interval, and it is related to specific signal timing parameters (cycle length and split), which are different from those which are more impactful on the actual stops (consisting of only acceleration and deceleration, and associated delays). On the other hand, deceleration and acceleration are associated with the action of stopping (referred to as a stop hereafter), which is related to those signal timing parameters that mainly impact traffic progression (e.g., offset and phase sequence). Therefore, while developing a methodology to understand FC during the entire process of a CSSP, we separate extra FC attributed to the stop from that attributed to stopped delay. For this reason, it is vital to observe FC experienced under each CSSP regime, as shown by various areas under the FC rate curves shown in Fig. 2g) and 2 h). Based on Fig. 2g) and 2 h), one can conclude that a stop is equivalent to stopped delay, from FC perspective, only if:

$$
F C_{D}+F C_{A}=K_{e} \cdot F C_{I}
$$

Where: Ke is fuel-consumption equivalency factor between stops and delays. Then we get:

$$
K_{e}=\frac{F C_{D}+F C_{A}}{F C_{I}}
$$

The Ke from Equation (5) is a unitless number representing ratios of FCs (those associated with the stop and others associated with the stopped delay). The idling phase duration depends significantly on the red interval's length. Therefore, in order to assign a weight value that represents a number of seconds of stopped delay equivalent to a stop, from a fuelconsumption perspective, $F C_{I}$ is divided by the total idling time (seconds) $\left(T_{I}\right)$ to obtain a stop-penalty $K$ [sec]:

$$
K=\frac{F C_{D}+F C_{A}}{\frac{F C_{I}}{T_{I}}}
$$

To consider the fact that most of vehicular fleets consist of both LDVs and HDDVs, the stop penalty of a fleet $\left(K_{\text {fleet }}\right)$ can be expressed as shown in Equation (7) below, where $p$ is the percentage of HDDVs (\%) in the fleet:

$$
K_{\text {fleet }}=\frac{(1-p)\left(F C_{D}+F C_{A}\right)_{L D V s}+p\left(F C_{D}+F C_{A}\right)_{H D D V s}}{(1-p)\left(\frac{F C_{I}}{T_{I}}\right)_{L D V s}+p\left(\frac{F C_{I}}{T_{I}}\right)_{H D D V s}}
$$

Although $K_{\text {fleet }}$ value, as calculated by Equation (7), may include a minor error due to impact of accelerations and decelerations of mixed-fleet vehicles, such error is neglected at this point for two reasons: 1. The potential error is applied systematically across all intersection movements, thus making the relative importance of each movement's $K$ similar to their true values, 2. The magnitude of impact of such an errors on the $K$ is estimated to be much smaller than the error which is being addressed (e.g. in current practice, the adopted $K$ values are several times lower than the true value).

Fig. 2g) and 2 h) show instantaneous (second-by-second) fuel consumed during each of the three driving phases of a CSSP. The area under the FC rate curve, shown in Fig. 2g) and 2 h), represent the total fuel consumed during a CSSP for a particular vehicle under specific operational conditions (e.g., cruising speed, road gradient). Thus, Area 1, Area 2, and Area 3, shown in Fig. 2g) and 2 h), represent the FCs during the deceleration, idling, and acceleration phases, respectively. Areas 1-3 can be computed as the integration of the FC rate curve between any two time points $t_{1}$ and $t_{2}$ :

$$
F C=\int_{t 1}^{t 2} F R(t) \cdot d t
$$

This research focuses on modeling second-by-second FC measurements from CMEM, in which case the area under the curve can be approximated by using an appropriate discretization:

$$
F C=\sum_{i=1}^{n} F R(i) \cdot \Delta_{i}
$$

Where: $F C$ - total fuel consumed within $n$ elementary intervals of $\Delta i, F R(i)$ - fuel consumption rate (vary with $i$ ), $\Delta i$ - elementary time interval. The FR modeling in CMEM (An et al., 1997) reads as:

$$
F R(t)=\varnothing(t) \cdot\left(K(t) \cdot N(t) \cdot V+\frac{P(t)}{\mu}\right) \cdot \frac{1}{44}
$$

Where:
$\operatorname{FR}(t)$ - fuel rate [grams/second].
$\varnothing(t)$ - stoichiometric fuel/air equivalence ratio.
$K(t)$ is the engine friction factor.
$N(t)$ - engine speed [revolutions/seconds].
$V$ - engine displacement [liter].
$P(t)$ - engine power output [kW].
$\mu$ - a measure of indicated efficiency [default value is 0.4].
44 - the lower heating value of typical gasoline [kJ/gram].
For any given CSSP, $K$ value depends significantly on the FC during the acceleration and deceleration phases. One can observe from Fig. 2e), 2f), 2 g) and 2 h) that FC is the lowest during deceleration, followed by idling, whereas much higher FC is observed during acceleration. In summary, it can be stated that the main operational conditions that increase the extra FC due to a stop caused by a traffic signal are the ones that cause: (1) higher FC during the acceleration phase, and/or longer time required to make a complete stop. That is because the extra FC during the deceleration phase mainly depends on the duration of the stopping process, which depends on several factors, including the driver's behavior and the traffic dynamics in front of the stopping vehicle. Thus, regardless of how small the fuel consumption (per unit of time) during deceleration is, longer deceleration times consume more fuel. Therefore, our methodology to estimate the impact of various factors on $K$ value incorporates modelling scenarios, in Vissim and CMEM, which include various factors to determine different values of excess FC for various operational conditions.

### 4.1. Various variables of operational conditions impacting fuel consumption

When investigating the individual impact of a particular factor (e.g., vehicle type) on FC, all other factors (e.g., cruising speed, road gradient, fleet distribution, driver behavior, and wind speed) were kept constant, at their default values (discussed later). A total of 74 experiments were designed to cover a wide range of variables for each of the investigated operational condition factors. Table 1 shows a summary of the variables that were tested individually for each investigated factor.

1. While CMEM contains 28 LDV categories and 3 HDDV categories, only 12 LDVs and all three HDDV categories were included in the experiments. The rest of the LDVs were excluded due to their irrelevancy (age: 1983-1986 and predominantly driven outside of the US). The first two columns in Table 1 list how considered vehicles are categorized in CMEM as opposed to this study.
2. Eleven proportions of heavy vehicles in the fleet were considered to investigate the impact of various fleet distributions on FC and $K$, as shown in Table 1.
3. The impact of driver's behavior on FC is investigated by analyzing various acceleration-deceleration functions, where each function represents a single unique driving behavior. Previous studies (Stevanovic and Gundogan, 2012; Partners, 2019) have shown that Vissim's default acceleration-deceleration functions do not replicate actual driver's behavior in the field.

Table 1
Variables for various operational conditions impacting FC.
| Vehicle type |  | Fleet distribution | Driver behavior | Road gradient | Cruising speed | Wind effect |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| CMEM | Our study | LDV: HDDV | Acceleration functions | (\%) | (mph) | (mph-direction) |
| Category-4 | LDV1 | 100:0 | Func1 | -7 | 20 | 50 tailwinds |
| Category-5 | LDV2 | 99:1 | Func2 | -6 | 25 | 40 tailwinds |
| Category-6 | LDV3 | 98:2 | Func3 | -5 | 30 | 30 tailwinds |
| Category-7 | LDV4 | 97:3 | Func4 | -4 | 35 | 20 tailwinds |
| Category-8 | LDV5 | 96:4 | Func5 | -3 | 40 | 10 tailwinds |
| Category-9 | LDV6 | 95:5 | Func6 | -2 | 45 | No wind |
| Category-10 | LDV7 | 94:6 | Func7 | -1 | 50 | 10 headwinds |
| Category-11 | LDV8 | 93:7 | Func8 | 0 | 55 | 20 headwinds |
| Category-24 | LDV9 | 92:8 | Func9 | 1 | 60 | 30 headwinds |
| Category-25 | LDV10 | 91:9 | Func10 | 2 | 65 | 40 headwinds |
| Category-26 | LDV11 | 90:10 | Func11 | 3 | Not applicable | 50 headwinds |
| Category-27 | LDV12 | Not applicable | Func12 | 4 |  | Not applicable |
| Category-5 HDD | HDDV1 |  | Not applicable | 5 |  |  |
| Category-6 HDD | HDDV2 |  |  | 6 |  |  |
| Category-7 HDD | HDDV3 |  |  | 7 |  |  |


For that reason, stochastic acceleration-deceleration functions, which were calibrated and validated in a previous study (Stevanovic and Gundogan, 2012), were used as seed default functions in Vissim to generate 12 driving behaviors (discussed later) that were applied deterministically in all subsequent experiments.

4. A maximum grade for federally funded highways in the US is specified in design tables based on terrain and design speeds. Such grades go up to 6\% in mountainous and hilly urban areas with exceptions of up to 7\% grades on mountainous roads with speed limits below 60 mph (Hancock and Wright, 2013). Hence, to follow these general recommendations, we adopted, as shown in Table 1, a road gradient range between -7\% and + 7\% to investigate the impact of the road slope on FC and the value of $K$.
5. Speed limits of signalized corridors in the United States vary depending on number of geometrical and traffic conditions. They usually range from 20 mph on local residential streets (speeds can go as low as 10-15 mph within school zones) to 65 mph on some low-density multilane highways. We defined ten different cruising speeds, as shown in Table 1, to cover most of the possible speed limits that could impact FCs and $K$ factor.
6. A set of experiments representing various wind speeds and directions (headwind (HW) and tailwind (TW)) were performed to investigate the wind impact on fuel consumed by HDDVs during one-stop. The range of wind speed was limited to 50-mph because investigating the impact of higher (not normal) wind speeds is outside the scope of this study.

### 4.2. Traffic simulation program

PTV Vissim is a microscopic, time-step and behavior-based model developed to simulate urban traffic and public transport operations. Besides the fact that Vissim is a popular tool in the traffic community, it was selected in this study for the following reasons: 1. its ability to accurately model traffic signals and other operations (e.g., speed and acceleration) at a resolution of 0.1 seconds, 2. it provides several vehicle classes (e.g., cars and heavy vehicles) and allows users to identify the proportion of each class in the fleet, and 3 . Vissim outputs vehicle trajectory files (FZP) are well fitted to be used in CMEM to obtain a second-by-second FCs.

### 4.3. Model for estimation of fuel consumption

CMEM is a microscopic FC and emission model that estimates second-by-second FC and emissions based on different modal operations from in-use vehicle fleet. The required inputs for CMEM include vehicle activity (second-by-second speed trace, at a minimum) and fleet composition of traffic being modeled, where those inputs can be obtained from Vissim. In addition to that, CMEM was selected for this study for two reasons: 1. CMEM can estimate FC for various vehicle types, 2. it allows users to incorporate the impact of road gradient (for all vehicles) and wind effect (for heavy vehicles only) on FC estimates. FC estimates in this study were not validated against field data, for two reasons: 1. because the CMEM has already been calibrated and validated by using data from the National Cooperative Highway Research Program (An et al., 1997), and 2. proper validation is a project on its own, which goes beyond the scope of this study. Moreover, many studies have already validated estimates from CMEM, and they concluded that CMEM is generally accepted as a model that can generate verifiable FC estimates (Rakha et al., 2003; Barth et al., 2001).

### 4.4. Experimental setup

This section first describes the modelling of the test-bed intersection and then it explains how various operational conditions were modeled in Vissim and CMEM. Third, default values for the evaluated factors were identified to ensure consistent comparisons. Finally, procedures to estimate FC from CMEM, and compute $K$, are provided.

### 4.4.1. Modeling of a hypothetical intersection

To support development of the proposed methodology, a total of 74 experiments were simulated on a hypothetical 4-leg intersection with two through-traffic lanes at each approach. The Vissim traffic simulation software was used to model the testbed intersection, which run 1,100 seconds including 200 seconds of warmup time. Each of the simulation runs was long enough to gather relevant results for approximately 167 vehicles (performing stops at the intersection), which represents a good statistical sample size. The right and left turning vehicles were not included in the analysis for two reasons: 1. to reduce unnecessary noise in the results (e.g. those vehicles behave differently), and 2 . signals are mainly coordinated to reduce stops and FC for through movements while it is more acceptable that, if must, left- and right-turning vehicles may stop. Traffic volumes from a typical 4-leg intersection in Lake County, Chicago, IL were used to model realistic traffic flows. Fig. 3 shows directional volumes for this intersection. A two-phase fixed-time signal timing plan was operated on the simulated intersection. A desired cycle length of 180 seconds was applied as a result of a common method to calculate cycle length based on a volume to capacity ratio of 0.95, saturation flow headways of 2 sec, a lost time of 4 seconds per phase, and relevant critical volumes. The green splits for the two phases resulted in 137 seconds for the major road and 35 seconds for the minor street.

### 4.4.2. Modeling of various operational conditions

Various operational conditions were modeled in Vissim and CMEM to investigate their individual impacts on FC, and K. Two vehicle classes (light-duty vehicle 'LDV' and heavy-duty diesel vehicle 'HDDV') were modeled in Vissim, whereas 15

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-09.jpg?height=1346&width=1189&top_left_y=187&top_left_x=349)
Fig. 3. Layout, volumes, and splits of the hypothetical intersection.

vehicle types (12 LDVs and 3 HDDVs) were modeled in CMEM. Various proportions of heavy vehicles in the fleet distribution were modeled in Vissim by changing the relative flow percentage of each vehicle class in the vehicle compositions for each intersection approach. Also, multiple driver's behaviors were modeled in Vissim by adjusting the desired and maximum deceleration-accelerations functions. Road gradients were first modeled in Vissim by defining grades for each link starting from the stop line to the point where vehicles reach their original cruising speeds. Similarly, the same road gradients were specified in CMEM during the process of postprocessing Vissim trajectory data. In this way both Vissim and CMEM were able to consider impact of the road gradients on the FC - Vissim from kinematic perspective whereas CMEM from the perspective of increased engine loads.

Cruising speed, for each experiment, was modeled in Vissim by setting proper value in the desired speed distribution function. As mentioned previously, the Cruising Speed Stop Profile (CSSP) starts as a deceleration event from a particular cruising speed and ends when the vehicle reaches the same speed after the acceleration phase. For all of the experiments, the desired speed distribution was defined in Vissim to ensure that the vehicles satisfy these cruising speed conditions. This was done in a way to ensure that a complete CSSP was achieved for every cruising speed defined.

The effect of wind was included by adding information (in CMEM) on wind speed and direction for HDDVs only. The reason that LDVs were not included is because the CMEM does not support this functionality for small passenger cars. Fig. 4 shows the process of modeling traffic at the test-bed intersection, performing various experiments, post-processing data trajectories from Vissim, estimating FC (based on trajectories) in the CMEM, and post-processing FC estimates in Matlab to compute the value of $K$.

A controlled comparison of various experiments requires that FC estimations are based on an approximately equal number of stopped vehicles in each experiment. That is not easy to achieve when cruising speeds vary (in various experiments)
because vehicles need different times to travel to the modeled intersection's stop line. Such conditions may result in a situation where the same vehicle (same ID) stops at the intersection on a red signal in one scenario but goes through the green signal in another. This challenge was overcome by adjusting the start time of the relevant green interval to ensure a comparable number of stops under each experiment. As a result, 167 vehicles were consistently identified to have stopped at the signal in each experiment.

Additionally, the same vehicles (with the same IDs, from each simulation) were used to derive FCs and compare results. This approach was adopted to ensure that the results do not include 'noise' introduced by the stochastic nature of simulation-generated driving behavior (and other simulation parameters) for various individual vehicles in the traffic stream. That was especially important to ensure that the times needed to travel from the beginning of the links (at the four approaches) to the relevant stop lines are consistent.

### 4.4.3. Default variables for various operational conditions

A default value for each of the evaluated factors was identified, as a reference value used when comparing FC results, to ensure consistent comparisons. LDV1, HDDV3, no-heavy vehicles, 12 deterministic acceleration-deceleration functions, level

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-10.jpg?height=1527&width=1632&top_left_y=814&top_left_x=133)
Fig. 4. Vissim-Matlab-CMEM connection.

terrain, $45-\mathrm{mph}$, and no wind were selected as default values for LD vehicle type, HDD vehicle type, driving behavior, road gradient, cruising speed, and wind speed, respectively. Fig. 3 shows all those default values.

Acceleration and deceleration functions adopted from a previous study (Stevanovic and Gundogan, 2012) are stochastic, meaning that each stopped vehicle in the simulation can have a unique deceleration-acceleration function. The use of such stochastic functions results in uncontrollable experiments because the impacts of various deceleration-acceleration functions (driving behaviors) on the $K$ cannot be captured. To solve this issue, the Dynamic Time Warping (DTW) (Sakoe and Chiba, 1978) and k-means clustering (Hartigan and Wong, 1979) algorithms were used to classify the stochastic driving behaviors of all of the 167 stopped vehicles into 12 deterministic categories. Such deterministic categories are fully controllable during the experiments, which guarantees accurate quantifying of the impact of various driving behaviors during experimental scenarios as well as the impact of other factors (e.g., cruising speed) on the K factor.

To apply the DTW and k-means algorithms, results from a simulation run (with all of the previously mentioned default values (Fig. 3), except cruising speed which was set at 65-mph, were used to partition the 167 deceleration-acceleration functions into 12 distinctive clusters. The $65-\mathrm{mph}$ speed was used because it covers a wider range of decelerationacceleration rates compared to the rates of any of the lower speeds. It should be mentioned that in Vissim, driving behavior of a specific vehicle is not a function of cruising speed; thus, various levels of driver's aggressiveness (either on deceleration or acceleration side) can be observed through an entire set of cruising speeds. The clustering process was done in two stages. Firstly, we applied the DTW algorithm on all 167 behavior functions to find dissimilarity factors between the groups of deceleration-acceleration functions. Secondly, the resulting dissimilarity factors were entered into a k-means clustering algorithm (Hartigan and Wong, 1979) to cluster behavior functions into 12 distinctive groups.

The DTW is an algorithm used to measure the similarity between two sequences, which may vary in length (time) (Sakoe and Chiba, 1978). DTW algorithm was applied because it represents a way to apply a non-linear (elastic) alignment for distances between points in two data series. This elastic alignment (illustrated in the bottom part of Fig. 5a) produces a more intuitive way (e.g. more than one based on Euclidean distances) to align the $i$-th point from one time series with the $i$-th point from the other time series (as shown in the upper part of Fig. 5a) (Tsiporkova, 2020). This approach allows two similar shapes to be matched even if their time intervals (or whichever variable is on the × axis) are not of the same length, which is the case when dealing with deceleration-acceleration functions resulting from various vehicles and drivers. To find the best alignment between two arbitrary time series A and B (shown in Fig. 5b), one needs to find the path through the grid $p=p 1, \ldots, p s, \ldots, p k, p s=\left(i_{s}, j_{s}\right)$, which minimizes the total distance between them. Then the time-normalized distance between series A and B is computed as:

$$
D(A, B)=\frac{\sum_{S=1}^{K} D\left(P_{S}\right) \cdot W_{S}}{\sum_{S=1}^{K} W_{S}}
$$

$D(P s)$ is the distance between $i_{s}$ and $j_{s}$, and $W_{s}>0$ : weighting coefficient. Finally, the best alignment path between A and B is found as the minimum distance between A and B :

$$
P_{0}=\arg _{p} \min (D(A, B))
$$

The best alignments between all of the deceleration-acceleration functions from the 167 stopped vehicles were computed using a built-in Matlab function replicating Equations (11) and (12) (Sakoe and Chiba, 1978). Such alignments express how dissimilar deceleration-acceleration functions are to each other; thus, they can be called dissimilarity factors. Fig. 6a) shows a sample of dissimilarity factors from the resulted dissimilarity matrix of $167 \times 167$, where each cell of the matrix represents the dissimilarity between two deceleration-acceleration functions of two vehicles. A lower value indicates that the two deceleration-acceleration functions (representing trajectories of two vehicles) are more similar.

Then the factors from the dissimilarity matrix were fed into an unsupervised clustering k-means algorithm that aims to partition a given set of $n$ observations (data points) into $k$ clusters by minimizing the total Within-Cluster Sum of Squares (WCSS) (Hartigan and Wong, 1979):

$$
W C S S=\arg _{S} \min \sum_{i=1}^{m} \sum_{x=1}^{n}\left\|x-\mu_{i}\right\|^{2}
$$

Where $\mu_{i}$ is the mean point of the centroid of cluster $i(i=1,2, \ldots, m)$, and $n$ is the number of observations in each cluster $i$. The number of clusters is determined by using the 'elbow method', which is based on the rate of 'diminishing returns' (Hartigan and Wong, 1979). The elbow method (shown in Fig. 6b) uses a chart of the quality of clustering performance (as a function of the number of clusters)
to select a point at the elbow of the curve to indicate how many clusters to use. One can observe from the result of the Elbow method (shown in Fig. 6b) that 4-6 clusters are suggested. However, the authors decided to be more conservative and proceed with 12 distinctive deceleration-acceleration functions to cover a wider variety of potential driving behaviors. Fig. 6c) and 6d) show the 12 deceleration and the 12 acceleration functions, respectively, that came out of the clustering process. These 12 deceleration-acceleration combinations were then used as default and deterministic functions in Vissim. This meant that a vehicle deceleration-acceleration behavior in Vissim would not be a result of a stochastic process, but each vehicle would fall within one of the 12 deceleration-acceleration combinations, where each combination would cover approximately the same portion of vehicular fleet. In this way, it was ensured that by utilizing such deterministic functions,

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-12.jpg?height=1070&width=1394&top_left_y=183&top_left_x=246)
Fig. 5. Using Dynamic Time Warping algorithm with behavior functions.

the authors could completely control the experiments and exactly determine causes of the possible variations in estimated FC.

Although vehicles of each of the 12 distinctive deceleration-acceleration clusters behave similarly (from acceleration and deceleration perspective), the FCs are still computed for all of the 167 stopped vehicles in each experiment. This was done to account for the unique deceleration distance of each vehicle, considering that such distance is a function of cruising speed etc., and may not be the same for each approaching vehicle. The following steps explain how FC and $K$ are computed for each experiment:

1. Vissim outputs (FZP files), which include second-by-second speeds and accelerations (decelerations), is processed in Matlab to extract individual trajectories of all fully stopped vehicles.
2. Trajectories from step 1 are processed in Matlab to obtain CSSPs of fully stopped vehicles (e.g., decelerating from a cruising speed of 45-mph, reaching a zero-speed, and then accelerating to the original cruising speed of 45-mph).
3. CSSPs from step 2 are processed in CMEM to estimate FC by each stopped vehicle.
4. Given the second-by-second speeds and FC, Equation (6) is used to calculate the $K$ value of each CSSP.
5. Steps 1-3 were applied to all 167 stopped vehicles, for each experiment, with 12 different deterministic decelerationacceleration functions. The average FC and $K$ for all 167 stopped vehicles were calculated for each of the 12 Vissim simulations, representing various deceleration-acceleration functions. Then, the average FC and $K$ from 12 Vissim simulations were computed for each experiment. A software code was developed to interface Vissim, Matlab, and CMEM to speed up the computation process and produce outputs from all experiments in a consistent manner.

## 5. Results and discussion

The amount of consumed fuel (in grams) for a CSSP representing each of the various experiments, from Table 1, are presented in Table 2. Fig. 7 illustrates the FC results for three representative cases for each of the investigated variables: the default value and two extreme cases (e.g., lowest and highest). For each of the results from Table 2, values of K are illustrated (for each variable individually) as a function of a specific FC factor in Fig. 8. Each of the charts in Fig. 8 (except 8c)) includes 13 data series out of which 12 represent each of the 12 deterministic deceleration-acceleration functions investigated in the study, and the bolded line represents an average of those 12 data series. Fig. 8c) is an exception because it already shows the

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-13.jpg?height=1110&width=1410&top_left_y=179&top_left_x=238)
Fig. 6. Partitioning behavior functions of stopped vehicles into mutual clusters.

Table 2
Variables for various operational conditions impacting FC.
| Vehicle type |  | Fleet distribution |  | Driver behavior |  | Road gradient |  | Cruising speed |  | Wind effect |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Variable | FC (g) | Variable | FC (g) | Variable | FC (g) | Variable | FC (g) | Variable | FC (g) | Variable | FC (g) |
| LDV1 | 56.6 | 100:0 | 56.6 | Func1 | 45.7 | -7 | 34.8 | 20 | 16.1 | 50 tailwinds | 473.8* |
| LDV2 | 57.2 | 99:1 | 62.5 | Func2 | 47.2 | -6 | 37.6 | 25 | 21.8 | 40 tailwinds | 505.6 |
| LDV3 | 55.5 | 98:2 | 68.7 | Func3 | 49.5 | -5 | 40.8 | 30 | 27.2 | 30 tailwinds | 510.8 |
| LDV4 | 52.5 | 97:3 | 74.4 | Func4 | 51.9 | -4 | 43.5 | 35 | 36.7 | 20 tailwinds | 513.3 |
| LDV5 | 57.8 | 96:4 | 80.1 | Func5 | 53.2 | -3 | 46.3 | 40 | 46.4 | 10 tailwinds | 525.6 |
| LDV6 | 54.6 | 95:5 | 86.5 | Func6 | 55.4 | -2 | 49.6 | 45 | 56.6 | No wind | 549.0 |
| LDV7 | 55.5 | 94:6 | 92.3 | Func7 | 56.3 | -1 | 52.7 | 50 | 70.3 | 10 headwinds | 587.2 |
| LDV8 | 59 | 93:7 | 98.4 | Func8 | 58.4 | 0 | 56.6 | 55 | 85.5 | 20 headwinds | 628.5 |
| LDV9 | 58.7 | 92:8 | 104.1 | Func9 | 60.5 | 1 | 59.2 | 60 | 106.6 | 30 headwinds | 690.8 |
| LDV10 | 111.2 | 91:9 | 110.9 | Func10 | 62.2 | 2 | 63.7 | 65 | 135.3 | 40 headwinds | 835.4 |
| LDV11 | 56.8 | 90:10 | 117.6 | Func11 | 63.7 | 3 | 67.1 | Not applicable |  | 50 headwinds | 979.5 |
| LDV12 | 55.9 | Not applicable |  | Func12 | 65.4 | 4 | 71.1 |  |  | *Values are for HDDVs |  |
| HDDV1 | 816.5 |  |  | Not applicable |  | 5 | 75.0 |  |  |  |  |
| HDDV2 | 894.4 |  |  |  |  | 6 | 80.2 |  |  |  |  |
| HDDV3 | 549.0 |  |  |  |  | 7 | 85.6 |  |  |  |  |


impact of various driving behaviors on K value. We note here that Fig. 8a) was developed for all vehicle types tested in the study, Fig. 8b), 8c), 8d), and 8e) were produced for the default Light-duty vehicle type (LDV1), and Fig. 8f) and Fig. 9 were generated for default Heavy-duty diesel vehicle type (HDDV3).

Results of the experiments with various vehicle types (columns 1 and 2 in Table 2) show that each vehicle type consumes a different amount of fuel, which will result in various $K$ values, as shown in Fig. 8a). For light-duty vehicles, the results indicate that, if vehicles use the same fuel type, the FC is more sensitive to the vehicle's mass than the vehicle type (e.g., FC of LDV10 (Gross Vehicle Weight (GVW) > 8500 lbs) is much higher than that of LDV6 type (a normal sedan-like car)).

However, when compared to the default category (LDV1), FCs from all of the LDVs (except LDV 10) fall within a range of 0.35-4.24\% difference. The situation is much different for the HDDVs, where the absolute FCs are much higher than those of the LDVs; but also, the differences between older trucks (HDD1 and HDD2, representing HDDVs from '90 s) and the default

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-14.jpg?height=1997&width=1503&top_left_y=355&top_left_x=191)
Fig. 7. Impact of various operational conditions on excess FC caused by a single stop.

truck HDD3 are much higher 48.7-63\%. Such difference could be a result of recent improvements of the truck fuel economies, who seems to be higher than those of the LDVs. Based on these results, it would be fair to expect that even newer vehicles (e.g. those manufactured after 2010 ) would result in even lower FCs (and emissions footprints) at signalized intersections, which will reduce the value of $K$.

Going back to Fig. 7 parts a)-c), one can observe how FC changes for three selected vehicle types: LDV10, LDV11, and HDDV3. These results indicate that the FC of HDDV3 during acceleration mode is ~ 5-10 times higher than the relevant FC of LDV10 and LDV11. Similarly, Fig. 7c) shows that the fuel rate of a truck (e.g., HDDV3) is significantly higher during

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-15.jpg?height=1795&width=1594&top_left_y=554&top_left_x=147)
Fig. 8. Impact of various operational conditions on Stop penalty (K), where DB: Driver behavior.

![](https://cdn.mathpix.com/cropped/99fa2913-78bc-4c87-8454-d234ff125051-16.jpg?height=586&width=1491&top_left_y=181&top_left_x=197)
Fig. 9. Impact of road gradient and cruising speed on Stop penalty (K) of a representative HDDV.

the deceleration phase than the fuel rates of the other vehicles (e.g., LDV10 and LDV11). Such a characteristic of HDDVs is expected to result in a significant impact on the $K$ value, when a fleet contains a high HDDV percentage, as discussed next.

Table 2 (columns 3 and 4) also reveals that FC shows an approximately linear relationship with an increase in the percentage of HDDVs. For an HDDV proportion in the fleet of $0-10 \%$, each one percent of extra HDDVs adds, on average, 6 grams of consumed fuel at each intersection stop. Naturally, if more fuel is consumed a penalty of each stop of such a HDDVsignificant fleet will increase, as shown in Fig. 8b). The highest value for K is reached with the highest percentage of HDDVs in the fleet. Based on Fig. 8b), we can conclude that every increase of 1\% of HDDVs in the fleet costs around 11 seconds of extra waiting-idling time (based on the equivalent FC) for every additional stop at a traffic signal. In fact, the final K value for an intersection approach would be based on two factors: 1. Vehicle types constituting arriving (average) fleet (e.g., LDVs and HDDVs), and 2. Percentage of each of those vehicle types in the fleet.

Columns 5 and 6 in Table 2 show how FCs vary for the 12 deceleration-acceleration functions. There is no clearly recognizable pattern to correlate such FC variations with some intuitive expectations related to different driving behaviors, as such behaviors are usually based on unique mental and physical characteristics of the drivers. Nevertheless, FC variations can reach up to 40\% in difference (e.g., when function \#1 is compared to function \#12). Fig. 7 parts d)-f) show how FCs range for selected deceleration-acceleration functions. Although the differences in FCs from Fig. 7 parts d)-f) cannot be easily quantified by a naked eye, Fig. 8c) shows that the impact of those differences is significant on the $K$ value (ranging from 105 to 147 seconds for various deceleration-acceleration functions). Considering that those 12 functions were all generated from a single stochastic deceleration-acceleration combination, it is expected that the K could diversify even more with a higher degree of stochasticity in driving behavior.

Similar to the percentage of HDDVs in the fleet, it is observable from Table 2 (eighth column) that the FC increases linearly with an increase of the road gradient. Fig. 7 parts g)-i) show that the road gradient's impact is very significant, especially during the acceleration mode. For instance, a vehicle traveling on 7\% uphill terrain will consume as much as ~ 2.5 times more fuel than a vehicle traveling downhill on the same segment (with a gradient of -7\%). Furthermore, an interesting finding is that the extra fuel consumed on an uphill stop (e.g., 5.4 extra grams per CSSP for + 7\% compared to a CSSP with + 6\%) cannot be compensated by the savings gained by stopping on a downhill direction of the same road segment (e.g., 2.8 fewer grams per CSSP for -7\% when compared to a CSSP -6\%). These findings make the road gradient one of the most important factors to consider when defining K for an intersection approach.

The results of experiments with various cruising speeds are presented in Table 2 (tenth column). They show that the cruising speed (often correlated to the prevailing speed limit) substantially impacts the FC of a CSSP. In relation to the cruising speed, the $K$ factor growth seems to have an exponential shape, as shown in Fig. 8e). This is especially observable for cruising speeds higher than 45 mph. Fig. 7 parts j)-l) illustrate how the area under the FC curves increases significantly when the cruising speed increases. This finding can be interpreted as if stopping a vehicle at a higher cruising speed introduces a much more significant interruption than stopping a vehicle traveling at a lower speed. However, it should be noted that the fuel costs of stopping do not come from the stopping (decelerating) activity per se as much as they are a result of the acceleration process for the vehicle to regain its previous cruising speed. For example, as observable from Table 2, a stopped vehicle previously traveling at 45 mph will use twice as much of the excess fuel (to accelerate to the same speed) as a stopped vehicle traveling at 30 mph; thus, resulting in an approximately double value of $K$, as shown in Fig. 8e).

Results of the wind speed and direction have shown, as expected, that headwinds cause the HDDV to generate more energy (which requires more fuel) to overcome the energy of the wind blowing in the opposite direction. Similar to the impact of the road gradient, although tailwinds save FC, as shown in Table 2 and Fig. 7 parts m)-o), the amount of fuel savings gained from a tailwind of certain speed cannot recover the fuel increase caused by a headwind of the same speed magnitude.

Those results are reflected on the $K$ value as depicted in Fig. 8f); thus, they confirm the importance of including wind effect in K calculations, especially for fleets with a high percentage of HDDVs.

In summary, results suggest that $K$ factor should be significantly larger than the one used in the existing traffic signal optimization practice. Results also show that the $K$ value required to minimize FC varies with different operational conditions, hence $K$ factor cannot be a single value as it is widely used. Although most of the government agencies focus on the quantity of traffic arriving at a signalized intersection (when optimizing traffic signals), the results of this study indicate that dynamics of traffic should be also considered, if the objective is to minimize FC. For instance, some traffic streams may encompass a higher percentage of heavy vehicles than the other; or an approach could be situated on a slope thus causing certain traffic movements to create much larger negative environmental footprints than what the current practice would account for. However, these factors are not considered in the current signal retiming practices and that is why our signal retiming policies should be modified. The following subsection provides a step-by-step procedure that can be used to compute the K values under various operational conditions.

### 5.1. Computation of stop penalty

The stop penalty should be specified on the turning-movement level. However, it is not likely that many of the factors will have different values for various turning movements. Still, such flexibility should exist to ensure that a realistic stop penalty can be calculated for every turning movement at an intersection under special circumstances. This approach is important so that traffic signal engineers can have flexibility to decide which movements to include in the analysis. This section provides an approximation step-by-step procedure to compute the stop penalty based on the results presented in Fig. 8. Furthermore, a detailed example is given to show how the procedure should be applied.

The following procedure describes a logic that an engineer can follow when deciding which K factors (stop penalties) to apply for various intersection's movements. Once such K factors are defined, it is possible (with the use of relevant signal optimization software) to properly balance signal timings to optimally trade-off between delays for stops at various intersections, to reduce excessive fuel consumption. The procedure starts by determining the stop penalty based on vehicle type and driving behavior while all other factors assume their default values. Those default values are level-terrain (0\% grade), 45mph cruising speed, and no winds. Subsequently, the determined stop penalties are adjusted to consider the impact of potential deviations in grade, cruising speed, and wind. The proposed procedure should be applied for each vehicle type, separately.

1. Use Table 3 to determine the stop penalty for each vehicle type and its driving behavior at the movement (or approach) of interest.
    1.1. Your K is YYY
2. Apply specific Road gradient - Rgra
    2.1. Is your Rgra for this movement equal to default value (0\%)?
    2.1.1. Yes, $\mathrm{K}=\mathrm{YYY}$; move to the next factor, Step 3
    2.1.2. No, compute a correction factor $\left(\mathrm{C}_{\mathrm{fg}}\right)$ for K for your Rgra, and apply necessary \% changes for the road gradient.
$$
C_{f g}=\frac{K_{\text {actualgrade }}}{K_{0 \%}}
$$

Where: $K_{0 \%}$ is the stop penalty when road grade is $0 \%, K_{\text {actualgrade }}$ is the stop penalty for the actual grade on the movement of interest. $K_{0 \%}$ and $K_{\text {actualgrade }}$ are found from Fig. 8d) and 9a) for LDVs and HDDVs, respectively.

Note: when taking road gradient use always the exit side of the intersection for that specific movement as the road gradient has very significant impact when a vehicle accelerates, which always happens on the exit side of the intersection movement.


2.1.3. Multiply this correction factor with the current value of K
$$
K=Y Y Y \times C_{f g}
$$
3. Apply specific Cruising Speed - Cspe
    3.1. Is your Cspe for this movement equal to the default value (45-mph)?
    3.1.1. Yes, K is equal to the value from step 2.1.1 or 2.1.3; move to the next factor, Step 4
    3.1.2. No, compute a correction factor $\left(\mathrm{C}_{\mathrm{fs}}\right)$ for K for your Cspe, and apply necessary changes for the cruising speed.
$$
C_{f s}=\frac{K_{\text {actualspeed }}}{K_{45}}
$$

Where: $K_{45}$ is the stop penalty when cruising speed is 45-mph, $K_{\text {actualspeed }}$ is the stop penalty for the actual cruising speed on the movement of interest. $K_{45}$ and $K_{\text {actualspeed }}$ are found from Fig. 8e) and 9b) for LDVs and HDDVs, respectively.

Table 3
Stop penalties for various vehicle types and driving behaviors.
| Vehicle type | Driving behavior |  |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| LDV1 | 105.1 | 106.6 | 110.8 | 118.8 | 119.2 | 120.3 | 123.2 | 130.9 | 140.2 | 141.6 | 142.9 | 146.6 |
| LDV2 | 110.7 | 111.0 | 111.4 | 119.1 | 120.7 | 124.8 | 129.6 | 137.8 | 139.3 | 142.2 | 144.3 | 147.1 |
| LDV3 | 108.0 | 108.7 | 110.9 | 113.5 | 115.0 | 119.1 | 120.1 | 120.1 | 135.6 | 141.9 | 143.0 | 147.5 |
| LDV4 | 100.7 | 101.7 | 102.2 | 108.3 | 109.8 | 114.4 | 114.6 | 125.6 | 126.0 | 134.2 | 135.4 | 137.2 |
| LDV5 | 113.0 | 113.4 | 114.1 | 119.2 | 120.7 | 123.1 | 125.3 | 126.1 | 142.1 | 145.8 | 147.0 | 150.6 |
| LDV6 | 106.2 | 106.8 | 108.4 | 110.6 | 112.1 | 113.1 | 115.6 | 123.0 | 129.2 | 141.7 | 142.1 | 145.0 |
| LDV7 | 104.8 | 106.4 | 106.4 | 113.6 | 115.1 | 119.5 | 119.7 | 127.3 | 135.8 | 139.0 | 139.4 | 143.7 |
| LDV8 | 113.4 | 114.6 | 115.3 | 120.0 | 121.6 | 127.9 | 130.9 | 138.8 | 142.5 | 148.9 | 149.6 | 155.4 |
| LDV9 | 114.1 | 115.8 | 117.2 | 123.0 | 124.5 | 128.9 | 130.2 | 130.4 | 140.9 | 147.9 | 148.1 | 152.5 |
| LDV10 | 229.8 | 231.2 | 232.2 | 240.1 | 241.6 | 246.4 | 247.6 | 260.9 | 263.7 | 266.2 | 266.4 | 271.4 |
| LDV11 | 107.2 | 107.2 | 109.1 | 116.8 | 118.3 | 122.0 | 123.1 | 131.6 | 136.4 | 142.2 | 142.9 | 148.0 |
| LDV12 | 87.5 | 89.0 | 90.8 | 100.6 | 102.1 | 107.9 | 112.3 | 120.5 | 150.1 | 163.8 | 168.7 | 177.7 |
| HDDV1 | 1172.6 | 1239.6 | 1351.9 | 1521.7 | 1531.7 | 1533.2 | 1630.5 | 1747.3 | 2099.7 | 2387.3 | 2589.6 | 3232.8 |
| HDDV2 | 1252.9 | 1305.4 | 1394.2 | 1395.8 | 1437.0 | 1638.7 | 1756.1 | 1883.4 | 2301.6 | 2813.9 | 3425.2 | 3550.1 |
| HDDV3 | 891.6 | 896.0 | 923.8 | 955.1 | 984.6 | 986.1 | 1023.6 | 1370.2 | 1426.9 | 1596.3 | 1697.4 | 2092.4 |


3.1.3. Multiply this correction factor with the K value from step 2.1.1 or 2.1.3

$$
K=Y Y Y \times C_{f s}
$$

4. Is your vehicle type heavy-duty diesel?
4.1. Yes, move to the next factor, Step 5.
4.2. No, your final K is the outcome from steps 3.1.1 or 3.1.3.
5. Apply specific Wind effect - Weff
5.1. Is your Weff for this movement equal to the default value (no wind)?
5.1.1. Yes, your final K is equal to the value from step 3.1.1 or 3.1.3.
5.1.2. No, compute a correction factor $\left(\mathrm{C}_{\mathrm{fw}}\right)$ for K for your Weff, and apply necessary changes in wind effect.

$$
C_{f w}=\frac{K_{\text {actualwind }}}{K_{\text {nowind }}}
$$

Where: $K_{\text {nowind }}$ is a stop penalty when there is no wind, $K_{\text {actualwind }}$ is a stop penalty for the actual wind speed and direction on the movement of interest. $K_{\text {nowind }}$ and $K_{\text {actualwind }}$ are found from Fig. 8f), for HDDVs only.
5.1.3. Multiply outcomes from steps 3.1.1 or 3.1.3 with this correction factor.

$$
K=Y Y Y \times C_{f w}
$$

6. Use the following Equation to compute the final stop penalty for the entire fleet (on that movement).

$$
K_{m}=\sum_{i=1}^{n} p_{i} \cdot K
$$

Where: $K_{m}$ is the stop penalty for the movement of interest, p is the percentage of each vehicle type (i), $K$ is the stop penalty for vehicle type (i) at movement $m$, and $n$ is the number of all vehicles of types.
7. Go back to step 1 to apply the same procedure for other movements or vehicle types.

Example:. What is the stop penalty of an approach at a signalized intersection under the following conditions: vehicle types: 99\% is LDV1 and 1\% is HDDV1, driving behavior function = 1, road gradient = 3\%, cruising speed = 35-mph, Head wind (speed = 30mph)?

1- Using Table 3, we find the $K_{\text {LDV } 1}=105.1$ seconds and $K_{\text {HDDV } 1}=1172.6$ seconds.

2 - We adjust each of the above determined stop penalties for road gradient of $3 \%$.
$$
\begin{aligned}
& C_{f g L D V 1}=\frac{150}{126}=1.19, C_{f g H D D V 1}=\frac{1982.4}{1236.8}=1.60 \\
& K_{L D V 1}=1.19 \times 105.1=125.07 \text { seconds }, K_{H D D V 1}=1.60 \times 1172.6=1876.16 \text { seconds }
\end{aligned}
$$
3 - We adjust each of the above computed stop penalties for cruising speed of 35-mph.
$$
\begin{aligned}
& C_{f s L D V 1}=\frac{80}{126}=0.63, C_{f s H D D V 1}=\frac{756.2}{1236.8}=0.61 \\
& K_{L D V 1}=0.63 \times 125.07=78.79 \text { seconds, } K_{H D D V 1}=0.61 \times 1172.6=715.29 \text { seconds }
\end{aligned}
$$
4 - We adjust $K_{\text {HDDV } 1}$ for effect of a headwind of 30 mph
$$
\begin{aligned}
& C_{f w H D D V 1}=\frac{1552}{1237}=1.25 \\
& K_{H D D V 1}=1.25 \times 715.29=894.11 \text { seconds }
\end{aligned}
$$

5- We use equation (20) to account for the impact of vehicular distribution in the fleet. We finally get that the stop penalty for the entire approach is:

$$
K_{\text {approach }}=(0.99 \times 78.79)+(0.01 \times 894.11)=86.94 \text { seconds }
$$

## 6. Conclusions and Future research

We have argued that the stop penalty ( $K$ factor), used to balance between FC (or number of stops) and delay in one of the most popular objective functions in the signal retiming practice, is a function of multiple operational conditions and not a constant value as mistakenly recognized by our current signal retiming practice. This is certainly true when one seeks to reduce the FC as one of the primary objectives of many traffic signal retiming policies. Obviously, the $K$ factor dependency on several operational conditions suggests that the $K$ factor will most likely be different for various approaches at each signalized intersection. That is because each approach at a signalized intersection has unique operational conditions. Thus, having a better understanding of the factors that cause the major observed variations in the $K$ value will lead to better signal optimization practices. The following conclusions have been reached:

- Operational conditions during stop-and-go events at traffic signals significantly impact excess FC caused by such stops. The findings have shown that all of the six investigated factors significantly impact FC, which results in different $K$ values.
- Stop penalty for various LDVs ranges between 118-second to 132-second except for LDV with GVW > 8500lbs, which results in a stop penalty twice as high as those of other LDVs. This result may indicate that the FC is more sensitive to the vehicle's mass than the fuel/engine type. Such a conclusion may also be reached by observing the stop penalties of HDDVs, which resulted in ~ 9-15 times higher values than the average stop penalty from the LDVs.
- An increase of 1\% of HDDVs in the fleet distribution adds extra 11 seconds of equivalent delay from the FC perspective. Similarly, a 1\% uphill gradient adds up to ~ 11 seconds of FC-equivalent delay if a vehicle is stopped on uphill terrain.
- When accelerating from a stop-line at a signalized intersection, an aggressive driving behavior can increase the fuel consumption of a stopping vehicle by up to 42-seconds of equivalent waiting-idling time, when compared to a "normal" acceleration behavior.
- The increase of FC and the $K$ with an increase of cruising speed seems to follow an exponential trend. For the most common speed limits on urban arterials ( $35-45 \mathrm{mph}$ ), a stop-and-go event from-and-to a cruising speed of 45-mph (common for major arterials) costs 46 seconds more (of equivalent FC during idling) than a stop for a vehicle traveling at a cruising speed of $30-\mathrm{mph}$ (e.g., common for side-streets).
- Wind can significantly increase or decrease the stop penalty of HDDV. The findings show that the stop penalty for trucks facing significant headwinds could be increased by up to 970 seconds compared to a no-wind conditions. Thus, this should be seriously considered for signalized intersections of the roadways with frequent and heavy winds and a high percentage of HDDVs.

Although this study has confirmed the significance of individual impacts of major operational conditions on FC during a stop, further research is needed (possibly with field data) to validate the experimental findings. Also, more research is needed to investigate the compound effects of various operational conditions. Most importantly, further research should focus on applying the FC-driven stop penalties on coordinated signal corridors to test how such stop penalties impact various corridor signal performance measures.

CRediT authorship contribution statement
Suhaib Al Shayeb: Conceptualization, Methodology, Data curation, Writing - original draft, Visualization, Investigation, Writing - review \& editing. Aleksandar Stevanovic: Conceptualization, Methodology, Data curation, Writing - original draft, Visualization, Investigation, Writing - review \& editing. Justin R. Effinger: Data curation, Visualization, Investigation, Writing - review \& editing.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## References

Ahn, K., Rakha, H., Trani, A., Van Aerde, M., 2002. Estimating vehicle fuel consumption and emissions based on instantaneous speed and acceleration levels. J. Transp. Eng. 128 (2), 182-190. https://doi.org/10.1061/(ASCE)0733-947X(2002)128:2(182).
Akcelik, R., 1981. Fuel efficiency and other objectives in traffic system management. Traffic Eng, Control.
Alshayeb, S., Stevanovic, A., Dobrota, N., 2021. Impact of Various Operating Conditions on Simulated Emissions-Based Stop Penalty at Signalized Intersections. Sustainability 13 (18), 10037.
An, F., Barth, M., Norbeck, J., Ross, M., 1997. Development of comprehensive modal emissions model: Operating under hot-stabilized conditions. Transp. Res. Rec. 1587 (1), 52-62. https://doi.org/10.3141/1587-07.
Barth, M., Malcolm, C., Younglove, T., Hill, N., 2001. Recent validation efforts for a comprehensive modal emissions model, in: Transportation Research Record. 10.3141/1750-02.
Bauer, C.S., 1975. Some Energy Considerations in Traffic Signal Timing. Traffic Eng.
Claffey, P. J., 1977. Passenger car fuel conservation. Technical report, Federal Highway Administration. Report FHWA-PL-77009, Washington.
Claffey, P.J., 1971. Running costs of motor vehicles as affected by road design and traffic. Technical report, NCHRP, Report No. 111.
Cohen, S.L. and Euler, G., 1978. Signal cycle length and fuel consumption and emissions (No. HS-025 846).
Courage, K.G., Parapar, S.M., 1975. Delay and fuel consumption at traffic signals. Traffic Eng. 45 (11).
Partners, Crash Avoidance Measures. Traffic Optimization for Signalized Corridors (TOSCo) Phase 1 Project Report. 2019. Available online: https://prontocore-cdn.prontomarketing.com/2/wp-content/uploads/sites/2896/2020/02/TOSCo_Phase_\%201_Final_Report_-_CAMP_WEBSITE.pdf (accessed on 13 October 2021).
Dart, O.K., and L. Mann. Potential Energy Conservation in Louisiana's Cities Through Traffic Engineering Measures. In: Institute of Transportation Engineers, Annual Meeting. Institute of Transportation Engineers; 1978. p. 300-309.
El-Shawarby, I., Ahn, K., Rakha, H., 2005. Comparative field evaluation of vehicle cruise speed and acceleration level impacts on hot stabilized emissions. Transp. Res. Part D Transp. Environ. 10.1016/j.trd.2004.09.002
EPA, 2019, Us transportation sector greenhouse gas emissions 1990-2017 https://www.epa.gov/greenvehicles/fast-facts-transportation-greenhouse-gasemissions; (last visited 12/14/2020)
Gordon, R.L., 2010. Traffic signal retiming practices in the United States, Vol. 409. Transportation Research Board.
Hancock, M.W. and Wright, B., 2013. A policy on geometric design of highways and streets. American Association of State Highway and Transportation Officials: Washington, DC, USA.
Hartigan, J.A., Wong, M.A., 1979. Algorithm AS 136: A K-Means Clustering Algorithm. Appl. Stat. 28 (1), 100. https://doi.org/10.2307/2346830.
Heide, C.H., Mohazzabi, P., 2013. Fuel economy of a vehicle as a function of airspeed: The concept of parallel corridors. Int. J. Energy Environ. Eng. 10.1186/ 2251-6832-4-28
Hurley, J.W., Ball, R.P., 1979. Evaluation of Energy-Based Signal Settings for Traffic-Actuated Control. Model. Simulati. 10.
Husch, D., Albeck, J., 2006. Synchro Studio 7 User Guide. Trafficware. 522, p.
Kwak, J., Park, B., Lee, J., 2012. Evaluating the impacts of urban corridor traffic signal optimization on vehicle emissions and fuel consumption. Transp. Plan. Technol. 35 (2), 145-160. https://doi.org/10.1080/03081060.2011.651877.
Li, X., Li, G., Pang, S.S., Yang, X., Tian, J., 2004. Signal timing of intersections using integrated optimization of traffic quality, emissions and fuel consumption: A note. Transp. Res. Part D Transp. Environ. 10.1016/j.trd.2004.05.001
Liao, T.Y., 2013. A fuel-based signal optimization model. Transp. Res. Part D Transp. Environ. 10.1016/j.trd.2013.03.014
McMichael, A.J., Haines, J.A., Slooff, R., Sari Kovats, R. and World Health Organization, 1996. Climate change and human health: an assessment (No. WHO/ EHG/96.7). World Health Organization.
Mock, P., 2012. EU consumer organisations asking for more realistic vehicle testing. International Council on Clean Transportation.
National Research Council, 2011. Assessment of fuel economy technologies for light-duty vehicles. National Academies Press. 10.17226/12924.
Oda, T., Kuwahara, M., Niikura, S., 2004. Traffic signal control for reducing vehicle carbon dioxide emissions on an urban road network. In: Proc. 11th World Congr. ITS, pp. 1-8.
PTV, 2014. PTV VISTRO User Manual. PTV Group.
PTV, 2020. PTV Vissim 2020 User Manual, PTV Group.
Rakha, H., Ding, Y., 2003. Impact of stops on vehicle fuel consumption and emissions. J. Transp. Eng. 129 (1), 23-32. https://doi.org/10.1061/(ASCE)0733-947X(2003)129:1(23).
Rakha, H., Ahn, K., Trani, A., 2003. Comparison of MOBILE5a, MOBILE6, VT-MICRO, and CMEM models for estimating hot-stabilized light-duty gasoline vehicle emissions. Canadian Journal of Civil Engineering 30 (6), 1010-1021.
Redsell, M., Lucas, G.G., Ashford, N.J., 1993. Factors affecting car fuel consumption. Proc. Inst. Mech. Eng. Part D J. Automob. Eng. 10.1243/ PIME_PROC_1993_207_155_02
Reljic, S., Kamhi-Barna, M., Stojanovic, S., 1992. Multicriteria signal plan choice at an isolated intersection. In Mathematics in Transport Planning and Control (Institute of Mathematics \& its Applications Conference Series 38).
Robertson, D., 1969. TRANSYT: A Traffic Network Study Tool. Road Res Lab.

Robertson, D., Lucas, C., and Baker, R., 1980. Coordinating traffic signals to reduce fuel consumption. Technical report, Transport Research Laboratory, Crowthorne, Berkshire, United Kingdom, TRL Report LR934.
Sakoe, H., Chiba, S., 1978. Dynamic Programming Algorithm Optimization for Spoken Word Recognition. IEEE Trans. Acoust. 10.1109/TASSP.1978.1163055
Shayeb, S.A., Dobrota, N., Stevanovic, A., Mitrovic, N., 2021. Assessment of Arterial Signal Timings Based on Various Operational Policies and Optimization Tools. Transportation Research Record. https://doi.org/10.1177/03611981211011165.
Stevanovic, A., Shayeb, S.A., Patra, S.S., 2021. Fuel Consumption Intersection Control Performance Index. Transportation Research Record. 03611981211004181.
Stevanovic, A., Gundogan, F., 2012. Calibration of micro-simulation models for ITS applications, in: 19th Intelligent Transport Systems World Congress, ITS 2012.
Sunkari, S., 2004. The benefits of retiming traffic signals. ITE J. Institute Transp Eng.
Tsiporkova, E., 2020, Dynamic Time Warping Algorithm. http://www.mathcs.emory.edu/~lxiong/cs730_s13/share/slides/searching_sigkdd2012_DTW.pdf ; (last visited 12/14/2020)
Urbanik, T., Tanaka, A., Lozner, B., Lindstrom, E., Lee, K., Quayle, S., Beaird, S., Tsoi, S., Ryus, P., Gettman, D., Sunkari, S., 2015. Signal timing manual, Vol. 1. Transportation Research Board, Washington, DC.
Webster, F. V., 1958. Traffic signal settings. Road Res. Tech. Pap. No.39, Road Res. Lab. London.
Zhao, H., He, R., Su, J., 2018. Multi-objective optimization of traffic signal timing using non-dominated sorting artificial bee colony algorithm for unsaturated intersections. Arch. Transp. Doi: 10.5604/01.3001.0012.2109.
Zhou, M., Jin, H., Wang, W., 2016. A review of vehicle fuel consumption models to evaluate eco-driving and eco-routing. Transp. Res. Part D Transp. Environ. Doi: 10.1016/j.trd.2016.09.008.


[^0]:    Peer review under responsibility of Tongji University and Tongji University Press.

    * Corresponding author.
    E-mail address: sma115@pitt.edu (S. Alshayeb).

