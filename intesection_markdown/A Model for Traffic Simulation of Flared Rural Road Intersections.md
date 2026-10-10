4th International Symposium of Transport Simulation-ISTS'14, 1-4 June 2014, Corsica, France A model for traffic simulation of flared rural road intersections

Per Strömgren ${ }^{\mathrm{a} *}$, Johan Olstam ${ }^{\mathrm{b}, \mathrm{c}}$, Andreas Tapani ${ }^{\mathrm{b}, \mathrm{c}}$<br>${ }^{\text {a }}$ Royal Institute of Technology (KTH), Department of Transportation and Logistics (ToL), SE-100 44 Stockholm ${ }^{b}$ Swedish<br>National Road and Transport Research Institute (VTI), SE-58195 Linköping, Sweden<br>${ }^{c}$ Linköping University, Department of Science and Technology (ITN), SE-60174 Norrköping, Sweden


#### Abstract

This paper presents a micro-simulation model that takes flared design of rural intersections into consideration. The intersection model is designed with input parameters that describe the geometric conditions of the flare. The behavior model includes both a traditional gap-acceptance sub-model and a passage model for modelling of vehicles' possibility to pass other vehicles using the flare. The intersection model developed has been implemented in the traffic micro simulation model RuTSim. The gap-acceptance part of the model has been calibrated using data for stop and yield 3-way intersections. The validation was performed by using video recordings to calculate delay for the yield regulated intersection and time in queue and service time for the stop regulated intersection. The results from the validation simulations correspond well with the empirical validation data. The effect of the flare on delay has been studied by using 3 different intersection lay-outs and different levels of minor and major flow. The result shows that the delay is decreasing with increasing intersection radius.


© 2015 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).
Selection and/or peer-review under responsibility of the Organizing Committee of ISTS' 14
Keywords: micro simulation; intersection; non-discrete; flare; gap-acceptance; rural

[^0]
## 1. Introduction

The road mileage is in many countries dominated by rural highways. This type of road has specific properties that limit the capacity for the road facility. Examples of limits are, limited overtaking possibilities, limited sight distances, different type of connecting intersections etc. As for urban intersections also rural intersection design affects the capacity and accessibility. Rural intersections are commonly designed with a flare which makes it possible for right and left turning vehicles to simultaneously approach the stop/yield line even if there are no marked turning bays, see Trafikverket (2012a), Trafikverket (2012b), Vejdirektoratet (2012) and the example in Fig. 1. The reason for this is the accessibility for trucks with trailer. Swedish intersection design is made so that the curve follows the swept path for semi-trailer. Since micro simulation models for urban environments and motorway facilities do not incorporate this geometric element they are not developed, calibrated and validated for rural intersections.

The traffic situation for the right and left turning vehicles on the secondary road thus depend on driver behavior. In the left case driver number 3 has not accepted the space and thus not passed the vehicle in front, which also prevents vehicle number 4 from passing. In the second case, driver number 3 has accepted the space, thereby vehicle number 3 does not prevent vehicle number 4 from queuing in the flared area.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-02.jpg?height=542&width=1487&top_left_y=897&top_left_x=133)
Fig. 1. Illustration of non-discrete lane use at a flared approach.

Flared intersections have been shown to result in increased capacity compared to corresponding one lane intersections Kyte et al. (1996) and Wu (1997). The increase in capacity depends on the length of flare and if it is a left flare, mixed flare or right flare. Wu (1997) estimated the capacity increase to between $6 \%$ and $60 \%$, depending of the flare design.

According to the Swedish Road Design Guidelines Trafikverket (2012a) and Manual for Performance Effect Calculations Trafikverket (2012b), intersections for rural conditions should be designed with a flare.

Hence, there is a need for rural road traffic simulation models capable of assessing the performance of such road environments. Modelling the overtaking process has been the main focus in rural road traffic simulation Brodin et al. (1986), Farah et al. (2009), McLean (1989) and Washburn (2005) while the interactions at rural intersections have been given less attention.

However, the state-of-the art rural road simulation models do not incorporate modelling of intersections with flare. For example, the present Swedish rural road micro simulation model RuTSim Tapani $(2005,2008)$ includes a simple intersection model that do not considered flared intersection designs. RuTSim deals with vehicles and intersections by "only" adding or removing vehicles at one point on the link.

The aim of this paper is to present a driver behavior model that takes geometric design of flared rural intersections into considerations. The intersection model developed has been implemented in RuTSim Tapani (2005) and is calibrated and validated using real world data.

The paper is organized as follows: a literature review is given in Chapter 2, the present RuTSim intersection model is presented in Chapter 3; Chapter 4 gives a description of the new intersection model and the implementation into the RuTSim model; Calibration and simulation results is presented in Chapter 5; Chapter 6 ends the paper with concluding remarks and suggestions for further research.

## 2. Literature Review

The Swedish Road Design Guideline Trafikverket (2012a) suggests that for rural conditions, a flared intersection design should be used. Rural intersection design is in general influenced of flare design. The exact design differs dependent on vehicle geometry, connecting road link angle to the major road and major and minor road width Trafikverket (2012a), Trafikverket (2012b), Vejdirektoratet (201)2, Statens Vegvesen (2013), Vägverket (2004).

Hence, traffic simulation models applied for rural roads in Sweden should be able to model non signalized intersections with flare. However, the state-of-the art rural road simulation models do not incorporate modelling of intersections with flare.

The need for estimation of rural road impacts has led to the development of microscopic traffic simulation models for rural roads including TRAffic on Rural Roads TRARR Hoban et al. (1991), TWO-lane PASsing TWOPAS Leiman et al. (1996), TWOSIM Kim (2006), VTISim Brodin et al. (1986) which has been further developed into RuTSim Tapani (2005), and CORSIM Li et al. (2011).

TRARR is designed for two-lane rural highway links, with intermittent passing-lane sections. TWOPAS McLean (1989) was developed to improve the methodology for two-lane, two-way road links in HCM 2000 Transport Research Board (2000). TWOSIM Kim (2006) was developed in three steps. In step one only a straight tangent level road without opposing traffic and no additional traffic entering or exiting via step two that includes overtaking behavior to step three with a geometric representation of curvature and truck traffic. The current RuTSim model has no geometric intersection model. The present model instead uses virtual queues of vehicles. Nothing is graphically exposed as an intersection and vehicles just starts at the origin point and ends at the destination point without any impact of the geometric design of the intersection. Li et al. (2011) developed a passing model and linked segments to traffic signalized intersections for CORSIM. However, the CORSIM intersection model does not include modelling of flared non signalized intersections.

Many commonly used commercial simulation tools are impossible to calibrate for two-lane rural road conditions. The reason for this is the non-existing feature of overtaking using the opposite lane. It is possible to design an intersection with flare, but it is difficult and even more difficult to calibrate. The method is to go from one lane via a connector connected to the middle lane of the three lane section. From the left lane a connector for the left turning movement is used and from the right lane a connector for the right turning movement. The middle lane should be wide and the right and left lanes narrow. In the middle lane a conflict zone is defined, this makes the two vehicles interacting. The conclusion is that models for rural conditions have limited support for intersections, especially for design with flare. With VISSIM it is possible to design an intersection with flare, but it is not straight forward and the model is not designed for rural road conditions including overtaking using the oncoming lane.

## 3. The New Intersection Model

### 3.1. Geometric description of the intersection

The model is designed with input parameters that describe the geometric conditions of the intersection including the flare. The input parameters are used to calculate an intersection curve, with one center radius and two clothoids connecting the center radius with the road edge for the major and the minor roads. To simplify the geometric translation to the RuTSim road description the two clothoids are replaced with two circle arcs. The intersection curve is described by eight different width dimensions, $\mathrm{s}_{1}-\mathrm{s}_{4}, \mathrm{t}_{1}-\mathrm{t}_{4}$ and the lane width of major road, $l w_{m a}$, and the lane width of minor road, $l w_{m i}$, as illustrated in Fig. 2.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-04.jpg?height=822&width=1422&top_left_y=214&top_left_x=218)
Fig. 2. Structure of the coordinate system and the parameters describing the channel width and the intersection curve of intersection.

Through these ten parameter values an approximate intersection curve can be calculated. For each possible turning movement a common car track is calculated according to the OpenDrive Dupuis et al. (2010) road specification. The car tracks are illustrated in Fig. 3. Vehicles can then move related to these tracks, where the left edge describes a center-line. Thus, the simulated vehicles do not necessary need to drive within the lateral limits of the track but each vehicle is coupled to a track and its movements are related to the track center line.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-04.jpg?height=681&width=1396&top_left_y=1429&top_left_x=236)
Fig. 3. In a 3-way intersection there will be 6 different OpenDRIVE Paths in the intersection area.

### 3.2. Geometric description of the intersection

A model for drivers' speed adaptation with respect to intersection curve radius was generated by using empirical data from speed measurement in roundabouts, intersections and chicanes in combination with a theoretical model.

The model calculates the speed V (equation 1), at which a vehicle can drive through a transition curve arc specified by the clothoid parameter A (equation 3), and the friction f (equation 2). To obtain A , also the lateral acceleration k (equation 4) must be calculated. This implies that an iterative procedure must be used to calculate the speed V and the clothoid parameter A.

$$
V=(R \cdot g \cdot f)^{0.5}
$$

Nomenclature

| V | Speed (m/s) |
| :--- | :--- |
| R | Radius arc (m) |
| g | Gravity acceleration ( $\mathrm{m} / \mathrm{s}^{2}$ ) |
| f | Coefficient of friction |

$$
f=A \cdot e^{-B \cdot V}
$$

Nomenclature

| A | Clothoid parameter |
| :--- | :--- |
| B | Coefficient |
| V | Speed (m/s) |
| f | Coefficient of friction |

$$
A=\left|\frac{(3.6)}{r}\right|
$$

| Nomenclature |  |
| :--- | :--- |
| A | Clothoid parameter |
| V | Speed (m/s) |
| k | Lateral acceleration $\left(\mathrm{m} / \mathrm{s}^{2}\right)$ |

$$
k=e^{-0,000015 * v^{3}}+0.45
$$

Nomenclature

| v | Speed (km/h) |
| :--- | :--- |
| k | Lateral acceleration $\left(\mathrm{m} / \mathrm{s}^{2}\right)$ |

The model described by equation 1-4 has been calibrated with data for radius between 8 and 100 m . However, iterative methods are undesirable from a traffic simulation implementation point of view. Instead of directly implementing equation 1-4 in the simulation model, the equations were utilized to calculate the curve speed for a large set of different curve radius. A second order polynomial was then fitted to the created data set, which resulted in equation 5.

$$
V=0.001 \cdot R^{2}+0.4829 \cdot R+15.211
$$

Nomenclature

| V | Speed (m/s) |
| :--- | :--- |
| R | Radius arc (m) |

The radius R is approximated by taking the center radius of the intersection curve and adding half the vehicle width and a marginal to the road edge of 0.5 m. The speed adaptation for vehicle turning movements are adjusted according to the calculated radius for the intersection curve and the deceleration is set to reach the calculated speed at the start of the intersection curve. The model is used for yield regulated right turns from minor to major roads, right turns from major to minor roads, yield regulated left turns from minor to major roads and left turns from major to minor roads.

### 3.3. Queue passage model

The RuTSim. 2 queue passage model compares the distance between a left-turning vehicle and the road-way edge, or right-turning vehicles and the center line with an individual assigned critical pass through width, W_c, see an example in Fig. 4.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-06.jpg?height=590&width=1100&top_left_y=1576&top_left_x=191)
Fig. 4. Illustration of critical pass through width for a right turning vehicle, $W_{c}$.

The critical pass through width is assumed to be normal distributed with a mean value of 1 ( 1.8 m is added for the vehicle width as a minimum critical passage width) and a standard deviation of 0.3 , i.e. the critical passage width is N(1,0.3). The critical passage width is not estimated based upon empirical values, due to lack of resources. Instead the standard width of parking lots (2.5 m) has been used as an estimate, which together with the standard deviation of 0.3 gives a total width of 2.8 m . This width is 1 meter more than the width of the average car in Sweden (1.8 m).

The queue passage model is schematic described in Fig. 5. The left turning case is described in the left part of the figure and right turning case to the right. In each simulation time step a queuing driver checks the current passage width and decides to either accept it (and pass on the right/left) or to continue queuing behind the front vehicle.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-07.jpg?height=778&width=1501&top_left_y=584&top_left_x=191)
Fig. 5: Illustration of the logical decisions that are made in queue model regarding to the critical width.

### 3.4. Gap acceptance model

The arrival at the intersection area and the logical choices done by drivers in RuTSim. 2 are described in the flow chart in Fig. 6.
![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-08.jpg?height=1950&width=1164&top_left_y=213&top_left_x=479)

Fig. 6. Illustration of the logical decisions that are made in the intersection area.

The driver checks in the first step an intersection is approaching, if not the link sub-models are applied. In the second step the driver deduce if the intersection is a mandatory stop or yield intersection. The driver starts to adapt its speed either in order to stop at a stop line or to pass safely through the intersection curve (in the case of a yield regulated intersection). The driver search for eventual vehicles in front and if any the available passage width is compared to the driver's critical passage width. If the passage width is larger than the critical passage width the search for a gap in the major traffic stream begins. If not, the car-following model is applied until a width gap that is large enough occurs. If the vehicle is free and within L_s meter from the yield line, gap searching among the gaps on the primary road begins for the yield regulated intersection. For stop regulated intersections the gap searching starts at the stop line, see the description in Fig. 7. $\mathrm{L}_{\mathrm{s}}$ represent the length where an approaching vehicle is able to estimate a first time gap at intersections that are regulated with a yield sign. Normally the distance is 20 m before the driver reach the yield line in accordance to sight distance requirement in the Swedish road design guideline Vägverket (2004).

| Model for left turn stop | Model for right turn stop | Model for left turn yield | Model for right turn yield |
| :--- | :--- | :--- | :--- |
| ![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-10.jpg?height=1058&width=310&top_left_y=359&top_left_x=163) | ![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-10.jpg?height=724&width=318&top_left_y=361&top_left_x=515) | ![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-10.jpg?height=1591&width=326&top_left_y=361&top_left_x=885) | ![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-10.jpg?height=1269&width=338&top_left_y=361&top_left_x=1255) |

Fig. 7. Illustration of the logical decisions that are made in the intersection area.

The RuTSim. 2 gap acceptance model is divided into four different cases, left and right turn with mandatory stop or yielding. The difference between yield and stop regulated intersections is that the gap search starts 20 m before
the yielding line when yielding. The driver does not need to stop and can therefore keep the speed through the whole intersection movement as determined by equation 5 .

### 3.5. Steering model for trucks

Trucks and trucks with trailer need larger turn radius then cars when going through intersections. To correctly model their impact on the queue discharge both their wider turns and trailer trajectories need to be taken into account. For the steering of vehicles and trailers a PI-regulator in combination with a simple bike dynamics model is utilized in RuTSim.2. In normal cases all vehicles use the middle of the track as the reference point for the steering. However trucks, buses and trucks with trailer delay the start of their turn until they are approximately 10-15 meters from the stop/yield line. Then they start to steer towards the middle of their outgoing target lane.

## 4. Model calibration and validation

The new intersection model described in chapter 3 was implemented in RuTSim. The calibration and validation was performed with empirical data from recorded observations with camera in ten rural T-intersections. The calibration data included data from six intersections and the validation data from two of the remaining four intersections.

### 4.1. Method including calibration and validation data

Calibration of RuTSim. 2 has been done according to empirical values of critical time gap and standard deviation Strömgren (2002). Different distributions from studied intersections in Sweden have been used to calculate an average value for the critical gap, see tab. 1 Olstam (2014).

Tab. 1. Basic values of the critical time gap.
| Traffic stream | Posted speed limit on major road |  |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Direction | $50 k p h$ |  | 60 kph |  | 70 kph |  | 80 kph |  | 90 kph |  |
| Major road |  | Yield | Stop | Yield | Stop | Yield | Stop | Yield | Stop | Yield | Stop |
|  | Left turn | 4.8 | 4.8 | 5.3 | 5.3 | 5.7 | 5.7 | 6.2 | 6.2 | 6.7 | 6.7 |
|  | Left turn | 5.3 | 6.0 | 5.8 | 6.5 | 6.2 | 6.9 | 7.2 | 7.4 | 7.2 | 7.8 |
| Minor road | Right turn | 5.0 | 5.7 | 5.5 | 6.2 | 5.9 | 6.6 | 6.4 | 7.1 | 6.9 | 7.5 |


From the distributions the standard deviation has been calculated, and has been set to 0.2 seconds in RuTSim.2. The individual vehicle/driver unit has then been assigned a critical gap time according to a Log-normal distribution.

### 4.2 Computational results

A visual inspection of the sites was performed before starting the survey, to see if there was enough space to set up facilities, and if the road's geometry allowed a measurement of the selected intersection, i.e. if sight length was enough.

The main study area is from the intersection and about 50 meters out on the primary road and secondary road. The equipment used was a 15 meter high mast mounted remote camera. To register time gaps between vehicles and speeds on the primary road, tubing detectors was used, see Fig. 8.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-12.jpg?height=1009&width=1594&top_left_y=224&top_left_x=145)
Fig. 8. The Configuration of the equipment for field measurement. The Camera was mounted on a 15 m high mast.

The empirical data are used to determine the delay for vehicles traveling from the minor road to the major road.
The selection of intersections was made, primary among the ones not used for the critical gap estimation and where the camera view was optimal for the calculation. During the field measurement it was concluded that data for two of the four intersections could not be utilized due to too small minor traffic flows.

The remaining intersections were Grästorp for left turn validation and Sjuntorp for right turn validation. Both intersections are of the same type with a traffic island on the minor road. The following time sequences were chosen, see tab. 2.

Tab. 2. Basic data for the intersections in the validation data set. The proportion of Lb (truck without trailer) and Lps (truck with trailer) in the Table is related to the major flow.
| Place | Time sequence | Speed limit1 | Speed limit2 | Speed limit3 | Major flow 1 | Major flow 2 | Minor flow | Lb \% | Lps \% |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sjuntorp | 06:00-06:15 | 70 | 70 | 70 | 248 | - | 132 | 1.4 | 5.2 |
|  | 06:15-06:30 |  |  |  | 388 | - | 208 | 1.6 | 5.0 |
|  | 06:30-06:45 |  |  |  | 384 | - | 284 | 1.1 | 5.1 |
|  | 06:45-07:00 |  |  |  | 444 | - | 284 | 1.3 | 5.3 |
|  | 07:00-07:15 |  |  |  | 396 | - | 140 | 1.4 | 5.1 |
|  | 07:15-07:30 |  |  |  | 444 | - | 204 | 1.3 | 5.0 |
|  | 07:30-07:45 |  |  |  | 516 | - | 144 | 0.9 | 4.7 |
|  | 07:45-08:00 |  |  |  | 596 | - | 156 | 0.8 | 4.9 |
|  | 08:00-08:15 |  |  |  | 408 | - | 96 | 1.5 | 5.3 |


| Grästorp | 08:15-08:30 |  |  |  | 428 | - | 96 | 1.5 | 5.5 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  |  |  |  | 392 | - | 88 | 1.7 | 5.2 |
|  | 08:45-09:00 |  |  |  | 452 | - | 112 | 1.3 | 4.9 |
|  | 09:00-09:15 |  |  |  | 404 | - | 52 | 1.5 | 5.4 |
|  | 06:45-07:00 | 90 | 70 | 90 | 212 | 172 | 48 | 1.5 | 5.8 |
|  | 07:00-07:15 |  |  |  | 220 | 248 | 84 | 1.7 | 6.0 |
|  | 07:15-07:30 |  |  |  | 256 | 200 | 76 | 0.8 | 9.6 |
|  | 07:30-07:45 |  |  |  | 272 | 172 | 60 | 2.7 | 5.4 |
|  | 08:15-08:30 |  |  |  | 200 | 204 | 72 | 7.9 | 8.9 |

Major flow 1 is the flow from left hand in Fig. 8 and major flow 2 is the flow from right hand in Fig. 8. Speed limit 1 is the speed limit on the major road for traffic coming from left and speed limit 2 is the speed limit on the minor road and speed limit 3 is the speed limit on the major road for traffic coming from right. For the intersection at Sjuntorp, at which only the right turn delay is considered, the major flow 2 is of no interest for the evaluation. The judgement if a specific vehicle can be considered free and unconstrained have been visual assessed.

The analyses of the Sjuntorp intersection field data were done by measure the travel time from a specific start point to a stop point for each vehicle in the specific direction. Each time slot was set to 15 minutes, to have a consistent flow on the major road. For each 15 minutes interval an average delay was calculated for two groups of free vehicles and bound vehicles, also the standard deviation was calculated, see tab. 3.

Tab. 1. Average travel time and delay for free and bounded vehicles at the Sjuntorp intersection.
| Time sequence | Avg. TT Bound flow | Avg. TT Free flow | Std. TT Bound flow | Std. TT Free flow | Delay |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 06:00-06:15 | 26.3 | 20.1 | 4.5 | 1.7 | 6.2 |
| 06:15-06:30 | 32.6 | 20.3 | 15.5 | 11.3 | 12.4 |
| 06:30-06:45 | 30.5 | 20.0 | 5.2 | 8.6 | 10.5 |
| 06:45-07:00 | 31.2 | 20.7 | 5.6 | 2.1 | 10.5 |
| 07:00-07:15 | 29.9 | 21.0 | 3.9 | 2.4 | 8.9 |
| 07:15-07:30 | 31.8 | 20.1 | 6.5 | 2.1 | 11.8 |
| 07:30-07:45 | 33.5 | 20.5 | 11.7 | 1.4 | 13.0 |
| 07:45-08:00 | 32.5 | 20.1 | 9.4 | 7.2 | 12.4 |
| 08:00-08:15 | 32.2 | 19.9 | 9.6 | 1.4 | 12.3 |
| 08:15-08:30 | 27.3 | 19.8 | 5.4 | 1.6 | 7.5 |
| 08:30-08:45 | 29.3 | 21.0 | 4.5 | 6.0 | 8.4 |
| 08:45-09:00 | 27.4 | 20.7 | 4.6 | 5.3 | 6.7 |
| 09:00-09:15 | 29.3 | 22.0 | 10.1 | 3.1 | 7.3 |


The estimated delay for the empirical flow interval shows an almost linear trend up to a major flow of 600 (v/h) and a minor flow up to 300 (v/h), see Fig. 9. Higher flow values will give a delay that increases asymptotic to infinity.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-14.jpg?height=957&width=1386&top_left_y=218&top_left_x=195)
Fig. 9. Delay as a function of minor flow and major flow.

The analyses of the Grästorp intersection field data were done by measure the time in queue and the service time for each vehicle in the each direction. Each time slot was set to 15 minutes, to have a consistent flow on the major road. For each 15 minutes interval an average time in queue and service time was calculated, also the standard deviation was calculated, see tab. 4. There could be a bias for those drivers/vehicles that have a higher desired speed.

Tab. 2. Estimated service time from field survey at left turn movement for the intersection in Grästorp.
| Time sequence | Time in queue | Service time | Std. Time in queue | Std. Service time |
| :--- | :--- | :--- | :--- | :--- |
| 06:45-07:00 | 0.2 | 7.4 | 0.8 | 5.5 |
| 07:00-07:15 | 3.9 | 5.1 | 8.4 | 6.2 |
| 07:15-07:30 | 0.5 | 8.7 | 1.5 | 5.6 |
| 07:30-07:45 | 0.2 | 7.9 | 0.4 | 7.4 |
| 08:15-08:30 | 4.1 | 6.1 | 9.3 | 5.7 |


Prediction intervals gives an estimate on in which interval one can expect the next data point sampled. Assume that the data really are randomly sampled from a Gaussian distribution. Collect a sample of data and calculate a prediction interval (see equation 6). Then sample one more value from the population. If you do this many times, you'd expect that next value to lie within that prediction interval. The key point is that the prediction interval tells you about the distribution of values, not the uncertainty in determining the population mean.

Prediction intervals must account for both the uncertainty in knowing the value of the population mean, plus data scatter. A prediction interval is always wider than a confidence interval.

$$
P_{i}=\bar{x} \pm t_{\frac{\alpha}{2}, n-1} \sqrt{\frac{n+1}{n}} s
$$

Nomenclature

| $\bar{x}$ | Average value |
| :--- | :--- |
| $t_{\frac{\alpha}{2}, n-1}$ | The value of the t -statistic for the confidence level $\alpha$ and $n-1$ degrees of freedom |
| $s$ | Standard deviation of average replication value |

Tab. 5 and 6 shows the result of the comparison between empirical data and simulated data. For the right turn movement case, tab. 5, the empirical and simulated data correlates in 12 of 13 cases.

Tab. 3. Estimated average delay and corresponding prediction intervals from simulations of right turn movements for the intersection in Sjuntorp. Pi(-) are lower value and Pi (+) the higher value of the prediction interval.
| Time sequence | Delay Empiric data | Avg. Delay simulation | Std. avg Delay | Pi(-) | Pi(+) | Empirical data within interval |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 06:00-06:15 | 6.2 | 4.5 | 0.9 | 2.5 | 6.5 | Y |
| 06:15-06:30 | 12.4 | 9.6 | 2.0 | 4.9 | 14.3 | Y |
| 06:30-06:45 | 10.5 | 12.4 | 2.5 | 6.5 | 18.3 | Y |
| 06:45-07:00 | 10.5 | 14.9 | 1.9 | 10.3 | 19.5 | Y |
| 07:00-07:15 | 8.9 | 7.5 | 1.0 | 5.2 | 9.7 | Y |
| 07:15-07:30 | 11.8 | 11.1 | 1.8 | 6.9 | 15.4 | Y |
| 07:30-07:45 | 13.0 | 10.5 | 1.7 | 6.5 | 14.4 | Y |
| 07:45-08:00 | 12.4 | 14.5 | 3.1 | 7.2 | 21.9 | Y |
| 08:00-08:15 | 12.3 | 6.7 | 1.2 | 3.9 | 9.5 | N |
| 08:15-08:30 | 7.5 | 7.5 | 1.2 | 4.7 | 10.2 | Y |
| 08:30-08:45 | 8.4 | 6.8 | 1.8 | 2.6 | 11.1 | Y |
| 08:45-09:00 | 6.7 | 8.5 | 1.5 | 4.9 | 12.0 | Y |
| 09:00-09:15 | 7.3 | 5.8 | 0.9 | 3.6 | 7.9 | Y |


The result for left turn movement case, tab. 6, shows that the empirical and simulated data correlates in 4 of 5 cases. In the fifth case the queue estimate didn't correlate but the service time results correlates.

Tab. 4. Estimated average service time and corresponding prediction intervals from simulation of left turn movements for the intersection in Grästorp. Pi(-) are lower value and Pi (+) the higher value of the prediction interval.
| Time sequence | Avg. Time in queue empiric data | Avg. Time in queue Simulation | Std. time in queue | Pi(-) | Pi(+) | Corr | Avg. Serv. time empiric data | Avg. Serv. time simulation | Std. Serv. time | Pi(-) | Pi(+) | Corr |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 06:45-07:00 | 0.2 | 1.9 | 1.7 | -2.0 | 5.9 | Y | 7.4 | 4.6 | 1.4 | 1.4 | 7.8 | Y |
| 07:00-07:15 | 3.9 | 4.6 | 1.3 | 1.5 | 7.7 | Y | 5.1 | 6.4 | 1.2 | 3.6 | 9.2 | Y |
| 07:15-07:30 | 0.5 | 4.3 | 0.8 | 2.3 | 6.3 | N | 8.7 | 6.7 | 1.2 | 3.7 | 9.6 | Y |
| 07:30-07:45 | 0.2 | 2.5 | 1.4 | -0.9 | 5.8 | Y | 7.9 | 5.5 | 1.2 | 2.8 | 8.3 | Y |
| 08:15-08:30 | 4.1 | 2.7 | 0.8 | 0.8 | 4.5 | Y | 6.1 | 4.7 | 0.8 | 2.8 | 6.5 | Y |


## 5. Effects of intersection flare on traffic performance

### 5.1. Experimental setup

In order to investigate the effect of flare a simulation experiment with different flare designs has been conducted. Three different intersection lay-outs one with a small intersection radius of 5 m and one medium of 12 m and one large of 20 m have been studied, see fig. 10. This gives a flare that has different length and width for the three cases which causes three different levels of queue storage in the flare, from 1 private car in the case of intersection radius 5 m , two private cars in the case of intersection radius 12 m and three private cars in the case of intersection radius 20 m. These three intersection designs also gives different speed through the intersection when yielding regulation, 17 (kph) for 5 m radius, 21 (kph) for 12 m radius and 25 (kph) for 20 m radius.

The delay is computed from a distance 1000 m before the intersection to 1000 m after the intersection with 10 minutes of warm up period and 60 minutes of measuring time.

| Intersection |  |
| :--- | :--- |
| with radius |  |
| 5 m. |  |


| Intersection with radius 12 m. | ![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-17.jpg?height=778&width=1390&top_left_y=238&top_left_x=360) |
| :--- | :--- |
| Intersection with radius 20 m. | ![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-17.jpg?height=873&width=1390&top_left_y=1065&top_left_x=360) |

Fig. 11: Delay as a function of intersection radius for minor road flow 300 (vph) (50 \% right turn and 50 \% left turn) and major flow (Qm) 330 (vph) respectively 730 (vph).

### 5.2. Computational results

The results show that the delay increases with decreasing intersection radius, see fig. 12 and fig. 13. fig. 14 show the effect of the flare on delay for two different major flow levels.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-18.jpg?height=782&width=1304&top_left_y=228&top_left_x=155)
Fig. 15: Delay as a function of intersection radius for minor road flow 300 (vph) (50 \% right turn and 50 \% left turn) and major flow (Qm) 330 (vph) respectively 730 (vph).

The more extreme increase in delay due to larger major flow for the intersection with radius 5 m is due to that the design gives in principle only one lane at the yielding line, dependant on the driver critical width. The intersection design with radius 20 m gives on the other hand approximately two lanes that could handle two private cars at the same time and queue additional two right turning vehicles in the flare. With a low major flow, 330 (vph), there are not so many cases where a queue occurs, witch explain why the smaller difference between the three different intersection radii. At the case with high major flow, 730 (vph), there are many occasions with a queue on the minor road. Since the intersection with intersection radius 5 m doesn't have the ability to serve more than one vehicle at a time, there will be substantial queues with large delays for this design.

Fig. 12 shows the effect of the flare on delay for two different minor flow levels. In this experiment the flow on the major road is constant, 730 (vph), and the minor flow is varied. The intersection with a radius of 5 m gives less increase in delay for increasing minor flow than the two designs with larger radius. The explanation is that in the first case the intersection has already reach a significant level of queues at the lower flow due to the locking between right turning and left turning vehicles. For the intersection with 12 m radius this occur later which gives a larger increase in the case with a minor flow of 500 (vph). The intersection with 20 m radius has a larger increase than the intersection with 5 m radius and less increase then the one with 12 m radius.

![](https://cdn.mathpix.com/cropped/fb0b22b9-9f25-48ee-8047-403b0d56394d-19.jpg?height=800&width=1437&top_left_y=224&top_left_x=165)
Fig. 12: Delay as a function of intersection radius for minor road flow 300 (vph) and 500 (vph) (50 \% right turn and 50 \% left turn) and major flow (Qm) 730 (vph).

## 6. Conclusions and further research

This paper describes a traffic simulation model for T-intersections with flare at rural two-lane roads. Flared intersections give the possibility for simultaneous discharge of left and right turning vehicles if the flare is wide enough. This is modelled by a queue passage model that compares individual assigned critical passage widths with the available passage width. A gap-acceptance model is used to model drivers' gap search in the major traffic stream. The model also includes a sub-model for drivers' speed adaptation with respect to the intersection curve radius.

The validation result shows that the geometric intersection model with flare correlates well with empirical delay data, empirical time in queue and service time. In 16 of 18 cases the simulated data corresponds with the empirical data when compared in a prediction interval analysis.

The simulation model developed has been utilized to investigate the effect of the flare on the delay for vehicles on the minor road. The simulation results show a logical relation between the intersection radius and delay, i.e. increased delay with decreasing intersection radius. The explanation is that small radii (here 5 m ) gives in principle only one lane at the yielding line. Large radii (here 20 m) gives on the other hand approximately two lanes that could handle two private cars at the same time and queue additional two right turning vehicles in the flare. At low major flow levels, 330 (vph), the results show no large differentials between the three different intersection radii. At the case with a high major flow, 730 (vph), the intersection with radius 5, don't have the capacity and the effect is substantial queues with large delays. The two intersections with larger intersection radius still have the ability to discharge the approaching vehicles and show smaller delays.

Future research includes further calibration and validation of the intersection model and further development in order to handle 4-way intersections and roundabouts. The model could also be extended with modelling of the "push" effect, i.e. when drivers on the minor road starts to accept smaller time gaps due to few acceptable time gaps in the major stream, due to low speeds and high flows on the major road.

## References

Brodin, A., and Carlsson A. 1986. The VTI Traffic Simulation Model. Swedish National Road and Transport Research Institute, Linköping.
Dupuis, M., et al. 2010. OpenDRIVE® Format Specification, Rev. 1.3D, VIRES Simulationstechnologie GmbH, Rosenheim, Germany.
Farah, H., Bekhor, S., Polus, A., and Toledo T. 2009. A passing gap acceptance model for two-lane rural highways. Transportmetrica 5 (3), 159-72.
Hoban, C. J., Shepherd, R. J., Fawcett, . G. J. and Robinson, G. K. 1991. A model for simulating traffic on two-lane rural roads: User guide 30 BIBLIOGRAPHY and manual for TRARR version 3.2. Technical manual ATM 10B, Australian Road Research Board.
Kim, J. 2006. A Capacity Estimation Methods for Two-lane Two-way Highways Using Simulation Modeling. Ph.D. dissertation of The Pennsylvania State University.
Kyte, M., Tian, Z., Mir, Z., Harneedmansoor, W., Kittelson, M., Vandehey, Robinson, B., Brilon, W., Bondzio, L., Wu, N., Troutbeck, R. 1996. Capacity and Level of Service at Unsignalized Intersections, Final Report: Volume I- Two-Way Stop-Controlled Intersections. National Cooperative Highway Research Program, Project 3-46.
Leiman, L., Archilla, A. R., and May, A. D. 1998. Twopas Model Improvements. University of California, Berkeley California.
Li, J., and Washburn, S. 2011. Implementing Two-lane Highway Simulation Modeling into CORSIM1, 6th International Symposium on Highway Capacity and Quality of Service Stockholm, Sweden June 28 - July 1, 2011, Department of Civil and Coastal Engineering, University of Florida, Gainesville, FL 32611, USA.
McLean, John R. (1989), Two-Lane Highway Traffic Operations - Theory and Practice. Gordon and Breach Science Publishers, New York.
Olstam, J. 2014. Kapitel 5 Ej signalreglerade korsningar: Metodbeskrivning för beräkning av kapacitet och framkomlighetseffekter i vägtrafikanläggningar (TRV 2013:64343ed.). In: Freddie Westman (Ed.), TRVMB Kapacitet och framkomlighetseffekter: Trafikverkets metodbeskrivning för beräkning av kapacitet och framkomlighetseffekter i vägtrafikanläggningar. Borlänge: Trafikverket.
Olstam, J., and Tapani, A. 2010a. "Enhancements to the Intelligent Driver Model", in Proceedings of the 89th annual meeting of the Transportation Research Board, Washington, USA.
Olstam, J., Hagring, O. and Allström, A. 2010b. Beräkningsmanual CAPCAL 3.3, 2010-04-06.
PTV. 2005. VISSIM 5.10 User Manual, PTV, Planung Transport Verkehr AG, Stumpfstraße 1, D-76131 Karlsruhe, Germany.
Statens Vegvesen 2013. Veg- og gateutforming, Håndbok 017, Vegdirektoratet.
Strömgren, P. 2002. Mikrosimulering av trafik i vägkorsning. Kungliga Tekniska Högskolan (KTH), Kompetenscentrum för Trafiksimulering (CTR) i Stockholm.
Tapani, A. 2008. Traffic Simulation Modelling of Rural Roads and Driver Assistance Systems. Linköpings University Institute of Technology.
Tapani, A. 2005. Versatile model for simulation of rural road traffic, Transportation Research Record 1934, pp. 169-178.
Transport Research Board 2010. Highway Capacity Manual HCM 2010, Transport Research Board, National Research Council, Washington, D.C.
Transport Research Board 2000. Highway Capacity Manual HCM 2000, Transport Research Board, National Research Council, Washington, D.C.
Trafikverket 2012a. Krav för Vägars och gators utformning, Publ. 2012:179. Vägar och gators utformning VGU, Publikation 2004:080.
Trafikverket 2012b. Effektsamband för vägtransportsystemet, Bygga om eller bygga nytt, Kapitel 4 Tillgänglighet, 2012-08-31.
Vejdirektoratet 2012. Handbog, Grundlag for udformning af trafikarealer, Anlaeg og planlaegning. Januar 2012, Høringsutgave.
Vägverket 2004. Vägar och gators utformning, VV Publikation 2004:80, Vägverket och Svenska Kommunförbundet, 2004-05.
Washburn, Scott S. (2005), Improvement of Planning Level Analysis Procedures for Two-Lane Highways. Final Report. Florida Department of Transportation. Tallahassee, FL. 375 pages.
Wu, N. 1997. Capacity of Shared-Short Lanes at Unsignalised Intersections, Proceedings of the Third International Symposium on Intersections Without Traffic Signals. Portland, Oregen, July 1997, Institute for Transportation Ruhr-University Bochum, Germany.


[^0]:    * Corresponding author. Tel.: +46(0)70-6653876; fax: +46(0)8-212899.
    E-mail address: perstro@kth.se

