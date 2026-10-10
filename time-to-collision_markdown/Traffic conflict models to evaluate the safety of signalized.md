# Traffic conflict models to evaluate the safety of signalized intersections at the cycle level 

Mohamed Essa, Tarek Sayed*<br>Department of Civil Engineering, University of British Columbia, 6250 Applied Science Lane, Vancouver, BC V6T 1Z4, Canada

## ARTICLE INFO

Keywords:
Automated traffic conflict analysis Safety of signalized intersections Effect of signal design on safety Safety performance functions


#### Abstract

The safety of signalized intersections has often been evaluated at an aggregate level relating collisions to annual traffic volume and the geometric characteristics of the intersection. However, for many safety issues, it is essential to understand how changes in traffic parameters and signal control affect safety at the signal cycle level. This paper develops conflict-based safety performance functions (SPFs) for signalized intersections at the signal cycle level. Traffic video-data was recorded for six signalized intersections located in two cities in Canada. A video analysis procedure is proposed to collect rear-end conflicts and various traffic variables at each signal cycle from the recorded videos. The traffic variables include: traffic volume, maximum queue length, shock wave characteristics (e.g. shock wave speed and shock wave area), and the platoon ratio. The SPFs are developed using the generalized linear models (GLM) approach. The results show that all models have good fit and almost all the explanatory variables are statistically significant leading to better prediction of conflict occurrence beyond what can be expected from the traffic volume only. Furthermore, space-time conflict heat maps are developed to investigate the distribution of the traffic conflicts. The heat maps illustrate graphically the association between rear-end conflicts and various traffic parameters. The developed models can give insight about how changes in the signal cycle design affect the safety of signalized intersections. The overall goal is to use the developed models for the real-time optimization of signalized intersection safety by changing the signal design.


## 1. Introduction

The safety of signalized intersections has often been evaluated at an aggregate level relating historical collision records to annual traffic volume and the geometric characteristics of the intersection. The collision-based safety evaluation is very useful in several applications such as identifying and ranking hazardous locations, and conducting before-and-after safety studies. However, collisions at signalized intersections can occur for several reasons including drivers' behavior in dilemma zones, approach queues and shock waves (Papaioannou, 2007; Machiani and Abbas, 2016). For intersection safety solutions that target these collisions, it is essential to understand how changes in traffic parameters and signal control affect safety at the signal cycle level. Unfortunately, modeling the safety of signalized intersections using collisions at the cycle level can be difficult for several reasons:

(1) The use of the historical collision data in safety analysis requires collisions to occur and be recorded over an adequately long period (e.g. years) in order to conduct a statistically sound safety diagnosis (Sayed and Zein, 1999; Chin and Quek, 1997).

[^0]

(2)The use of several years of collisions requires reliance on aggregate exposure measures such as the annual daily traffic (AADT) which does not explicitly account for the fact that not all vehicles are interacting unsafely (El-Basyouny and Sayed, 2013) and does not represent the variation of traffic flow between cycles.
(3)Collecting data on important traffic parameters such as delay, queue length, and traffic volume at each cycle is difficult and requires special sensing needs.
(4)Important cycle-related variables that can affect intersection safety such as the arrival type and the shock wave characteristics are difficult to collect and need special advanced algorithms.


This paper develops safety performance functions (SPFs) for signalized intersections at the signal cycle level. The models relate the rear-end conflicts occurring in each cycle to variables such as traffic volume, maximum queue length, shock wave characteristics (e.g. shock wave speed and shock wave area), and the platoon ratio. The developed models can give insight about how changes in the signal cycle design affect the safety of signalized intersections. The overall goal is to use the developed models for the real-time optimization of signalized intersection safety by changing the signal design. The approach presented in this paper provides several advantages as follows:

- The use of real traffic data, obtained by video recordings at six different intersections, which reflects actual driving behavior (i.e. the results are not based on microsimulation models).
- Proposing a video analysis procedure to collect data at the cycle level.
- The use of traffic conflicts as a measure of safety. Conflicts are extracted automatically and quantified using a conflict indicator (e.g. Time to collision). Also, the actual conflict location is determined.
- The proposed approach allows for the extraction of various traffic parameters including: the traffic volume, the maximum queue length, the shock wave characteristics, and the platoon ratio.
- The traffic conflict data and the various traffic parameters are measured directly from the video data and evaluated at a cycle level. As such, no hourly aggregation is needed.

## 2. Previous work

Safety performance functions (SPFs) of signalized intersections have been widely developed, investigated and calibrated in the literature. The highway safety manual (HSM) (AASHTO, 2010) provides SPFs that estimate the average crash frequency for signalized intersections on different road classes including rural two-lane roads, rural multi-lane roads, urban and suburban arterials. Also, several studies locally developed, adopted and calibrated SPFs for signalized intersections to local conditions of specific zones (Poch and Mannering, 1996; Miaou and Lord, 2003; Lyon et al., 2005; Wang et al., 2006; Wong et al., 2007; Wang and Abdel-Aty, 2008; Guo et al., 2010; Persaud et al., 2012; Abdel-Aty et al., 2014; Lee et al., 2017). The traffic exposure measure used in most of these studies is an aggregation of the traffic volume (e.g. AADT) and the predicted number of collisions is aggregated to several years.

There are several shortcomings with the reliance on crash data in safety analysis. A large number of crashes is needed to obtain statistical reliability which often requires a period of several years (Sayed and Zein, 1999; Ismail et al., 2010; Chin and Quek, 1997). As well, there are well-recognized availability and quality problems associated with crash data. The use of traffic conflicts for safety analysis is gaining acceptance as a proactive approach to study road safety from a broader perspective than relying only on collision data analysis (Sayed and Zein, 1999; Songchitruksa and Tarko, 2006). Traffic conflicts occur more frequently, can be clearly observed, and can provide insight into the failure mechanism that leads to collisions. Many researchers have shown that reducing traffic conflicts can lead to reducing the frequency of road collisions (Sacchi et al., 2013) as they further argued that the same failure mechanism in the driving process leads to the occurrence of both traffic conflicts and road collisions (Ismail et al., 2011). Therefore, the use of traffic conflicts for safety diagnosis has been recently gaining acceptance among road safety researchers as a surrogate or a complementary approach to the collision data analysis approach. A traffic conflict is defined as "an observable situation in which two or more road users approach each other in space and time to such an extent that there is a risk of collision if their movements remained unchanged" (Amundsen and Hydén, 1977). Recently, with the advances in computer vision techniques, the automated extraction of traffic conflicts from video recordings was demonstrated in several studies (Autey et al., 2012; Saunier and Sayed, 2008; Laureshyn et al., 2009; among others). The automated conflicts analysis approach overcomes many shortcomings in manual data collection and provides a more practical and efficient way to capture traffic conflicts. Previous studies have shown that SPFs for signalized intersections can be developed on the basis of field-observed traffic conflicts (Sayed and Zein, 1999; El-Basyouny and Sayed, 2013; Zhang et al., 2014; Sacchi and Sayed, 2016a, 2016b). In these studies, the exposure measure in the SPFs is represented by the average hourly traffic volume, and the traffic conflicts are aggregated to hours (i.e. number of conflicts/hour).

Conducting conflict-based safety evaluations using microsimulation models has also been proposed recently (Gettman et al., 2003). Microsimulation models have been widely calibrated and validated to evaluate the safety of signalized intersections using simulated traffic conflicts estimated by the SSAM tool (e.g. Gettman et al., 2008; Cunto and Saccomanno, 2008; Dijkstra et al., 2010; Huang et al., 2013; Shahdah et al., 2014; Essa and Sayed, in press, 2015, 2016). In most of these studies, the simulated results are usually aggregated into larger time periods such as hours. Other studies considered signalized intersection safety issues that related to dilemma zone (Papaioannou, 2007; Machiani and Abbas, 2016), or related to red-light running violations (Elmitiny et al., 2010; Jahangiri et al., 2016).

Although there are several studies developing SPFs for signalized intersections, to the best of the authors' knowledge, no studies have attempted to develop SPFs at the cycle level. This study aims to fill this research gap by relating the number of traffic conflicts

![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-03.jpg?height=1007&width=1533&top_left_y=185&top_left_x=177)
Fig. 1. Study locations in the City of Edmonton, Alberta.

during each signal cycle to various traffic parameters.

## 3. Study locations and data collection

Data from six signalized intersections in two cities were used in this study. Fig. 1 shows the study locations 1 and 2 in the City of Edmonton, Alberta. Fig. 2 shows study locations 3, 4, 5, and 6 in the City of Surrey, British Columbia. For all six sites, video cameras were installed to record video-data. The camera scenes mainly focused on the intersection approaches where most of the rear-end conflicts occur. To enable accurate rear-end conflicts and shock wave analysis, two issues were considered during the camera installation process. First, the camera scenes must cover a sufficient length of the intersection approaches upstream the stop line. Second, the stop line and the traffic signal indicators must be clearly captured in the video recordings.

Table 1 provides more details on the selected intersections that include: the location; the selected approaches; the number of lanes per approach; signal timing; the date of data collection; the Google-image; and the video scene.

## 4. Methodology

This section describes the methodological framework utilized in this paper to analyze video-data at the signal cycle level, and to develop various conflict-based SPFs incorporating different traffic characteristics and shock wave effect.

### 4.1. Shock waves at signalized intersections

Shock wave analysis is commonly undertaken at signalized intersections due to the concern of the length of queues formed upstream the intersection approaches. Shock waves at signalized intersections can be analyzed if the flow-density relationship is known for the approach and the flow state of the approaching traffic is specified (May, 1990). Fig. 3 shows a hypothetical space-time diagram for one lane approach at a signalized intersection. The vehicle trajectories are shown in dash lines, and the signal timing (i.e. green, yellow, and red) is overlaid on the stop line location. Typically, four traffic flow states (shown in cyan circles) and five shock waves are depicted in such space-time diagram.

From safety perspective, most of vehicle interactions occur around the triangle that surrounds the area where the traffic flow state is (II). The shock wave $\mathrm{S}_{12}$ separates two consecutive traffic flow states (I and II) that represent the maximum change or a sudden decrease in the traffic speeds. Theoretically, such a sudden decrease in the traffic speeds can result in higher risk in terms of rear-end conflict occurrence. Of the shock wave characteristics mentioned earlier, two characteristics were considered in the analysis: (1) the

![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-04.jpg?height=1257&width=1529&top_left_y=185&top_left_x=179)
Fig. 2. Study locations in the City of Surrey, British Columbia.

shock wave area where the traffic flow state is II (the triangle area); and (2) the speed of the backward-moving shock wave $\mathrm{S}_{12}$.

### 4.2. Video-data processing

The processing of video-data in this study is essential for estimating the number of traffic conflicts, as well as measuring values of different traffic parameters at each signal cycle using the recorded video data. The following sections describe the main steps of the video analysis procedure.

### 4.2.1. Signal timing detection

The first step of the video analysis procedure was to identify traffic signal cycles for each intersection. A MATLAB code was developed to extract the actual signal timing program for each video-hour. At each video frame, the code identifies the traffic signal indicator (e.g. green, red, or yellow) by detecting the RGB (red-greenblue) values of the signal head. Finally, the results were aggregated for all frames and the overall signal program was identified.

### 4.2.2. Vehicle trajectories and space-time diagram

The second step of the video analysis procedure was to extract vehicle trajectories and to plot the space-time diagram for each signal cycle. A computer code was developed to automate the process. First, the overall signal cycle program identified previously was used to determine the start frame and the end frame of each signal cycle. Second, within each cycle's frames, the RGB values of number of points (e.g. 50 or 100 points) located along the centerline of the studied lane were detected at each frame. The studied lane was selected to be a lane that has a through movement. Exclusive left-turn and right-turn lanes were not included. Third, a fivedimensional (5D) matrix was created. Each individual element of this matrix has the following values: (1) the point number along the centerline, (2) the frame number, and (3-5) the RGB values of this point at that frame. Subsequently, the 5D matrix was plotted as a two-dimensional image where the horizontal axis represents the point number and the vertical axis represents the frame number. This

Table 1
Description of the study locations (* protected-permissive left turns).
| Location \# | City (Province) | Intersected roads | Video-data was recorded in | Selected intersection approaches | Number of Lanes per approach | Traffic signal timing (seconds) | Google image | Video scene |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Edmonton (AB) | Stony Plain Rd \& 170 St | May 27th, 2015 June 2nd, 2015 | 170 St (Northbound) | 1 (Right)<br>1 (Left)<br>4 (Through)<br> | ( )<br> | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=152&width=173&top_left_y=784&top_left_x=392) | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=256&width=172&top_left_y=380&top_left_x=392) |
| 2 | Edmonton (AB) | Gateway Blvd \& 34 Ave | May 26th, 2015 | Gateway Blvd (Northbound) | 1 (Right)<br>1 (Left)<br>4 (Through)<br> | ( )<br> | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=151&width=173&top_left_y=785&top_left_x=598) | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=253&width=172&top_left_y=382&top_left_x=598) |
| 3 | Surrey (BC) | 72 Ave \& 128 St | March 28th, 2012 March 29th, 2012 | 72 Ave (Eastbound \& Westbound) | 1 (Left)<br>2 (Through)<br> | ( )<br> | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=256&width=90&top_left_y=680&top_left_x=805)![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=185&width=88&top_left_y=715&top_left_x=909) | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=203&width=139&top_left_y=432&top_left_x=806) |
| 4 | Surrey (BC) | 72 Ave \& 132 St | April 3rd, 2012 | 72 Ave (Westbound) | 1 (Left)<br>2 (Through)<br> | ( )<br> | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=279&width=126&top_left_y=655&top_left_x=1028) | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=253&width=172&top_left_y=382&top_left_x=1028) |
| 5 | Surrey (BC) | 64 Ave \& King George Blvd | June 10th, 2015 June 11th, 2015 | King George Blvd (Southbound) | 1 (Right)<br>1 (Left)<br>2 (Through)<br> | ( )<br> | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=118&width=170&top_left_y=818&top_left_x=1236) | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=255&width=170&top_left_y=380&top_left_x=1236) |
| 6 | Surrey (BC) | Fraser Highway \& 168 A St | June 10th, 2015 June 11th, 2015 | Fraser Highway (Southbound) | 1 (Bike lane)<br>1 (Left)<br>2 (Through)<br> | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=68&width=163&top_left_y=1124&top_left_x=1441) | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=165&width=173&top_left_y=769&top_left_x=1442) | ![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-05.jpg?height=255&width=173&top_left_y=380&top_left_x=1441) |


![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-06.jpg?height=1013&width=1285&top_left_y=185&top_left_x=302)
Fig. 3. Theory of shock wave at signalized intersections.

image represents the space-time diagram for the whole traffic cycle.
Fourth, for each column of pixels (at each x-value) in the space-time image, the pixels that represent a sudden change in the RGB values were detected and identified. These pixels represent arrival or departure of vehicles that passing through this point. Fifth, the identified pixels in the space-time image were grouped along consecutive columns in order to create vehicle trajectories. Pre-specified rules were followed during creating the trajectories. These rules consider the factual movement in terms of the maximum speed, the maximum acceleration, the minimum headway, and the maximum deceleration. Afterwards, the created trajectories were visual inspected to ensure that the created trajectories accurately represent the moving vehicles.

A further adjustment is needed in order to obtain the real-world positions of the vehicle trajectories. This adjustment was performed using a camera calibration process to identify a mapping between the three-dimensional real world and the two-dimensional image space (Ismail et al., 2013). Following the procedure presented in Ismail et al. (2013), a linear transformation was defined to convert 3D coordinates into 2D coordinates. The linear transformation was defined by a matrix, called the "homography matrix". The camera calibration is the process of determining the "homography matrix" (Ismail et al., 2013). The camera calibration process was performed at each intersection based on feature correspondences between the video image and the orthographic image of that intersection. Google Satellite image was used in this study as an orthographic image. Four types of annotations were used for camera calibration optimization: (1) corresponding points; (2) distances; (3) angels; and (4) global up directions. The calibration error was represented by the discrepancy between estimated and annotated segment lengths normalized by the length of each segment. The calibration error was very small and should have no impact on the accuracy of the estimated trajectories. More details about the camera calibration process can be found in Ismail et al. (2013).

Afterwards, the positions of the tracked trajectories were converted to the real-world coordinate system using the "homography matrix". As a final check, the trajectories were then overlaid on the original video and visually observed to ensure their accuracy. Also, during this visual observation of the video, vehicle lengths were observed and assigned to each trajectory in order to be considered in conflict analysis. Finally, the space-time diagram for the whole signal cycle was plotted using the final vehicle trajectories and the signal timing program. Fig. 4 illustrates, through examples, the performed procedure of extracting vehicle trajectories and obtaining the space-time diagram of signal cycles.

### 4.2.3. Shock wave analysis

After plotting the space-time diagram for each cycle, shock wave characteristics can be analyzed. As mentioned earlier, two shock wave characteristics were considered in the analysis: (1) the shock wave area where the traffic flow state is (II) (the triangle area shown in Fig. 3); and (2) the speed of the backward-moving shock wave $\mathrm{S}_{12}$. In reality, the shock wave area is not exactly a triangle as appeared in the shock wave theory; rather it might be a polygon. As well, the backward-moving shock wave speed is not a constant

![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-07.jpg?height=1106&width=1529&top_left_y=185&top_left_x=179)
Fig. 4. Platform of extract vehicle trajectories and plot space-time diagram using video data.

speed represented by one line from the first to the last vehicle in the queue; rather the shock wave speed varies between each couple of consecutive vehicles. A computer code was developed to compute the shock wave area and the speed using vehicle trajectories and signal timing plan. The program computes the shock wave speed between each couple of consecutive vehicles then average shock wave speed was calculated for the whole cycle. In addition, the maximum queue length of each cycle was measured and recorded.

### 4.2.4. Traffic conflicts

Traffic conflicts can be analyzed using vehicle trajectories. The conflict analysis involves the calculation of conflict indicators such as the Time-to-Collision (TTC) or Post-Encroachment-Time (PET). This study focuses only on the rear-end conflicts; therefore, the TTC was chosen as the primary conflict indicator. In the literature, the TTC is recognized as an appropriate conflict indicator for identifying the rear-end conflicts. The TTC is defined as "the time required for two vehicles to collide if they continue at their present speeds and on the same path" (Hayward, 1972). For each constitutive vehicle trajectories moving in the same lane, the TTC can be continuously estimated over time using the following equation.

$$
T T C_{t}=\frac{X_{j, t}-X_{j+1, t}-L_{j}}{V_{j+1, t}-V_{j, t}} ; \quad \forall\left(V_{j+1, t}-V_{j, t}\right)>0
$$

where
$t$ : The time interval;
$j$ : The leading vehicle;
$j+1$ : The following vehicle;
$X$ : The position of the vehicle;
$V$ : The speed of the vehicle;
$L$ : The length of the vehicle.
The minimum TTC can be extracted to represent the conflict severity. A critical value of a conflict indicator must be drawn from each interaction. Typically, the most severe value is used to represent the overall severity of a traffic event. Using the minimum TTC of each conflict, the number of rear-end conflicts was determined for each signal cycle at different TTC thresholds. Thresholds of TTC

![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-08.jpg?height=651&width=1535&top_left_y=185&top_left_x=177)
Fig. 5. Measurements (outputs) of video data analysis process.

ranged from 0.5 s to 3 s in 0.5 s increments. As well, rear-end conflict positions with reference to the stop line were determined using the coordinates of the critical event position (minimum TTC).

### 4.2.5. Platoon ratio

The quality of progression is a critical characteristic that must be quantified for the analysis of signalized intersections. The arrival type is a parameter that describes this characteristic for each lane group. According to Highway Capacity Manual (2000), six arrival types are defined to approximate the quality of progression. Although there are no definitive parameters to quantify arrival type, the platoon ratio is useful. The platoon ratio is defined as the proportion of all vehicles arriving during green multiplied by the ratio of the signal cycle length to the effective green time of the subject movement (Highway Capacity Manual, 2000). The platoon ratio and the arrival type can have a significant effect on the frequency of the rear-end conflicts at signalized intersections (Essa and Sayed, in press, 2015, 2016). Therefore, the platoon ratio was considered in this study for the safety assessment of signalized intersections at the cycle level. For each cycle, the platoon ratio was measured using the space-time diagram. The effective green time was considered to be the green time plus half of the yellow time. To determine the percentage of vehicles arriving during green time, vehicle trajectories were analyzed. If a vehicle did not stop, it was considered to be arrived on green. If a vehicle stopped, the first point of time of its stopping was compared to the signal timing to determine whether this vehicle arrived on red or green.

In summary, the outputs of the video-data analysis for each cycle are: (1) shock wave area (A); (2) traffic volume (vehicles/lane/ cycle) (V); (3) backward-moving shock wave speed $\left(\mathbf{S}_{12}\right)$; (4) platoon ratio (P); (5) maximum queue length (Q); (6) number of rearend conflicts that have TTC equals or less than different TTC thresholds (i.e. TTC $\leq 0.5,1,1.5,2,2.5$, or 3 s). Fig. 5 illustrates the outputs (measurements) of the video data analysis process.

### 4.3. Conflict-based SPFs at cycle level

After obtaining the aforementioned measurements (V, A, Q, $\mathrm{S}_{12}$, P, and the number of rear-end conflicts) for each traffic cycle using the proposed video analysis process, the next step was to develop conflict-based SPFs to investigate the impact of different traffic characteristics within a signal cycle on the number of rear-end conflicts that occurred at the same cycle. The SPFs are developed using the GLM approach.

The GLM approach has been widely used in literature for the development of collision and conflict prediction models (e.g. Sawalha and Sayed, 2001; El-Basyouny and Sayed, 2013; Persaud et al., 2010). Previous studies have shown that the number of potential traffic conflicts related to the number of vehicles arriving within a small time interval at a road site occurs by a Poisson process (Elvik et al., 2009). Assuming that traffic conflict data are non-negative, discrete, and rare events compared to the circulating traffic volume, mixed-Poisson distribution family might be used in this regard as with crash data (Sacchi and Sayed, 2016b). The GLM approach used to model traffic conflict occurrence assumes an error structure that is Poisson or Negative Binomial (Poisson-Gamma). Generally, the model must yield logical results. That is, it must not lead to a negative number of conflicts, as well as it must predict zero values of conflict frequency for zero values of exposure variable (i.e. traffic volume). A commonly used model form consists of an exposure measure(s) raised to some power and multiplied by an exponential function incorporating the remaining explanatory variables. Such a model form can be linearized by the logarithm link function (Sawalha and Sayed, 2006). The conflict prediction models used in this paper can be expressed mathematically as follows:

$$
E(Y)=V^{a_{1}} \exp \left[a_{0}+\sum_{j} b_{j} x_{j}\right]
$$

where
$E(Y)$ : The predicted number of rear-end conflicts per cycle;
$V$ : The traffic volume per lane per cycle (exposure);
$x_{j}$ : Any other explanatory variables (such as $\mathrm{A}, \mathrm{Q}, \mathrm{S}_{12}$, or P );
$a_{0}, a_{1}, b_{j}$ : The model parameters.
In order to decide whether the error structure follows Poisson or Negative Binomial distribution, the methodology presented by Sawalha and Sayed (2006) was applied. First, Poisson distribution was assumed and the model parameters were estimated. Then the dispersion parameter $\left(\sigma_{d}\right)$ was calculated using the following equation:

$$
\sigma_{d}=\frac{\text { Pearson } \chi^{2}}{n-p}
$$

where
$n$ : The number of observations;
$p$ : The number of model parameters.
Pearson $\chi^{2}$ is defined as follows:

$$
\text { Pearson } \chi^{2}=\sum_{i=1}^{n} \frac{\left[y_{i}-E\left(Y_{i}\right)\right]^{2}}{\operatorname{Var}\left(Y_{i}\right)}
$$

where
$y_{i}$ : The observed number of rear-end conflicts at cycle $(i)$;
$E\left(Y_{i}\right)$ : The predicted frequency of rear-end conflicts at cycle ( $i$ ) as obtained from the conflict prediction model;
$\operatorname{Var}\left(Y_{i}\right)$ : The variance of conflict frequency for the cycle ( $i$ ).
The dispersion parameter $\left(\sigma_{d}\right)$ is a useful statistic measure for assessing the amount of variation in the observed data. If the estimated value of $\left(\sigma_{d}\right)$ is significantly greater than 1.0, this means that the data have a greater dispersion than what can be explained by the Poisson distribution, and then the Negative Binomial distribution provides a better fit to the data (Sawalha and Sayed, 2006).

Various models were developed in this paper using different combinations of the explanatory variables (V, A, Q, $\mathrm{S}_{12}$, and P). The reason behind developing various models is to investigate the impact of adding different explanatory variables, as well as to make the proposed approach applicable in different situations where the availability of measuring or estimating some explanatory variables is limited. The procedure recommended by Sawalha and Sayed (2001) to add explanatory variables into the GLM model was utilized. The procedure is a forward procedure that seeks parsimonious models. In this procedure, the variables are added to a model one by one, and the decision on whether a variable is to be retained in the model is based on: (1) the significance of the estimated coefficient of this variable (t-ratio), and (2) the significance of the drop in the scaled deviance of the model caused by adding this variable. Also, variables that represent exposure (e.g. traffic volume) must be included first (Sawalha and Sayed, 2001, 2006).

The goodness of fit of the developed GLM models was assessed using two main statistical measurements: the scaled deviance (SD), and the Pearson chi-squared ( $\chi^{2}$ ). Generally, for a well-fitted model with a relatively large number of observations, the expected values of $\left(\chi^{2}\right)$ and SD will be approximately equal to the number of degrees of freedom (df) (Sawalha and Sayed, 2001). In addition to (SD) and ( $\chi^{2}$ ), different developed models were compared using Akiake's Information Criterion (AIC) which can be estimated as per Eq. (5).

$$
A I C=2 p-2\left(\log L i k_{\text {full }}\right)
$$

where
$p$ : The number of model parameters;
LogLik ${ }_{\text {full }}$ : Log-likelihood for the full model.
The free software environment for statistical computing "R" was used to develop the GLM models and to estimate different statistical measurements.

## 5. Results and discussion

### 5.1. Summary of data statistics

The data used for the analysis was obtained at the six study locations at signal cycle level using the video analysis procedure described earlier. Table 2 provides summary statistics of the measured data. It is noteworthy that the correlation values between V

Table 2
Summaries of data statistics.
| Variable | Description | Unit | Mean | SD | Min | Max |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| V | Volume per lane per cycle | - | 11.58 | 3.56 | 2 | 22 |
| A | Shock wave area | km.s | 1.05 | 0.96 | 0 | 3.93 |
| Q | Maximum queue length | meter | 40.42 | 24.54 | 0 | 97.46 |
| $\mathrm{S}_{12}$ | Backward-moving shock wave speed | meter/s | -2.07 | 2.65 | -27.2 | 0 |
| P | Platoon ratio | - | 1.26 | 0.40 | 0 | 2.27 |
| TTC0.5 | Number of rear-end conflicts ( TTC $\leq 0.5 \mathrm{~s}$ ) | - | 0.49 | 0.85 | 0 | 4 |
| TTC1.0 | Number of rear-end conflicts ( $\mathrm{TTC} \leq 1.0 \mathrm{~s}$ ) | - | 0.97 | 1.40 | 0 | 6 |
| TTC1.5 | Number of rear-end conflicts ( TTC $\leq 1.5 \mathrm{~s}$ ) | - | 1.88 | 1.88 | 0 | 7 |
| TTC2.0 | Number of rear-end conflicts ( $\mathrm{TTC} \leq 2.0 \mathrm{~s}$ ) | - | 2.97 | 2.30 | 0 | 11 |
| TTC2.5 | Number of rear-end conflicts ( TTC $\leq 2.5 \mathrm{~s}$ ) | - | 3.82 | 2.57 | 0 | 12 |
| TTC3.0 | Number of rear-end conflicts ( TTC $\leq 3.0 \mathrm{~s}$ ) | - | 4.25 | 2.73 | 0 | 13 |


and the number of rear-end conflict increase steadily with the TTC thresholds. For example, the correlation increases from 0.27 at TTC threshold of 0.5 s to 0.55 at TTC threshold of 3.0 s. That is, the higher the TTC threshold, the higher the dependency of the rearend conflicts on the exposure. This is confirming with the findings provided in previous studies (Essa and Sayed, in press, 2015, 2016). The covariates A, Q, $\mathrm{S}_{12}$, and P have good correlations with the number of rear-end conflicts, meaning that they can provide a better conflict prediction if they are incorporated in the conflict-based SPFs.

In addition, considering that the data are collected sequentially in time, the assumption that the error in the developed models is independent might not be appropriate if there is a serial correlation between the residuals. Therefore, the serial correlation between the conflicts in consecutive signal cycles at each location was estimated using the Durbin-Waston (DW) statistic. The results of the DW statistic showed that the serial correlation is not significant and should have no effect on the results.

### 5.2. Conflict-based SPFs at cycle level

Various models were developed in this paper using different combinations of the covariates (V, A, Q, $\mathrm{S}_{12}$, and P). For all models, the response ( $\boldsymbol{Y}$ ) denotes the number of rear-end conflicts per cycle that have TTC values equal or < 1.50 s. The TTC threshold of 1.50 s is commonly used by researchers to define rear-end conflicts (van der Horst and Hogema, 1993).

The results of the developed models are provided in Table 3. The first model represents the exposure only. In addition to the first model, the table shows four models that consider the exposure and one additional variable. Furthermore, the last model in the table considers the exposure and a combination of three additional explanatory variables. The significance of the explanatory variables, the goodness-of-fit statistics, and the error structure for all models are provided in the table.

Generally, the developed models show good fit and almost all the explanatory variables are statistically significant at the 95\% confidence level. Based on the estimated value of the dispersion parameter $\left(\sigma_{d}\right)$, the error structure was assumed to follow Negative Binomial distribution for four models, and Poisson distribution for two models. All the covariate coefficients have logical signs. In other words, higher conflict occurrence is expected during the signal cycles that have long queues and bigger shock waves. On the other hand, the higher platoon ratio means that more vehicles arrive during the green time, and subsequently, a better arrival type and lower chances of conflict occurrence during the cycle.

For the exposure-only model (model 1), the coefficient of V is statistically significant at 95\% confidence level. This model shows a good fit in terms of the (SD) value which is close to the degree of freedom (df). However, the model has a large value of the Pearson chi-squared ( $\chi^{2}$ ) compared to the (df). Also, the model has the largest value of AIC comparing to the other models. Thus, despite of

Table 3
Conflict-based SPFs at cycle level.
| Model\# $\boldsymbol{E}(\boldsymbol{Y})=$ | Variables | Error structure | K | SD | df | $\chi^{2}$ | AIC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| One variable (Exposure only): |  |  |  |  |  |  |  |
| Model 1: $V^{1.563} \exp (-3.231)$ (Exposure + One Variable): | $V$ | NB | 3.05 | 249 | 220 | 356 | 775 |
| Model 2: $V^{0.706} \exp (-1.797+0.501 A)$ | $V, A$ | NB | 14.9 | 244 | 219 | 241 | 702 |
| Model 3: $V^{0.65} \exp (-2.046+0.0122 Q)$ | $V, Q$ | NB | 8.73 | 243 | 219 | 253 | 716 |
| Model 4: $V^{1.637} \exp \left(-3.316+0.05 S_{12}\right)$ | $V, S_{12}$ | NB | 3.10 | 248 | 219 | 347 | 775 |
| Model 5: $V^{1.571} \exp (-1.768-1.266 P)$ Combined Model: | $V, P$ | Poisson | - | 276 | 219 | 281 | 706 |
| Model 6: $V^{1.239} \exp \left(-1.624+0.294 A-0.828 P+0.119 S_{12}\right)$ | $V, A, P, S_{12}$ | Poisson | - | 240 | 217 | 215 | 674 |


[^1]the significance of the exposure variable V, more explanatory variables are still needed to provide a better prediction of the conflict occurrence beyond what can be expected from the exposure only.

For the models that consider the exposure and one additional variable (models 2, 3, 4, and 5), all models are noted to have a better statistical fit comparing to model 1. Also, the additional explanatory variable is significant at 95\% confidence level. One exception of that is model 4 (volume and shock wave speed) whose additional variable $\left(\mathrm{S}_{12}\right)$ is statistically significant at 90\% confidence level. Model 2 (volume and shock wave area) represents the best model in this group in terms of AIC, ( $\chi^{2}$ ), and (SD) values. Model 3 (volume and maximum queue length) shows a good fit in terms of the $\left(\chi^{2}\right)$ and (SD) values. This model shows a value of AIC significantly lower than model 1 and slightly higher than model 2. Model 4 has a value of AIC similar to model 1; however, the value of $\left(\chi^{2}\right)$ is better than model 1. Model 5 has a value of AIC very close to model 2 and significantly better than model 1. Thus, the shock wave area, the maximum queue length, the shock wave speed, and the platoon ratio are shown to be important characteristics that affect the number of rear-end conflicts at the signal cycle. Incorporating one of these characteristics (A, Q, $\mathrm{S}_{12}$, or P), along with the traffic volume, in the conflict-based SPFs of signalized intersections is recommended to improve the model fit.

Finally, the last model in the table (model 6) combines the exposure measure (V) with three additional explanatory variables (A, $\left.\mathrm{P}, \mathrm{S}_{12}\right)$. The maximum queue length (Q) was excluded from this model due to the strong correlation between A and Q, or in other words, the multicollinearity effect. Model 6 shows the best fit comparing to all previous models. The model presents the minimum values of SD, $\left(\chi^{2}\right)$, and AIC. As well, all variables' coefficients are statistically significant in this model at 95\% confidence level. However, the main disadvantage of this model is the inclusion of many explanatory variables which may be difficult to obtain in some cases.

### 5.3. Space-time distribution of traffic conflicts

In addition to the developed model, a space-time conflict heat map diagram was developed from all observed signal cycles to investigate the distribution of traffic conflicts. To plot the conflict space-time distribution, two measurements were considered for each conflict. The first measurement is the time of the conflict with regard to the signal timing and represented as a percentage. The second measurement is the position of the conflict location ascribed to the stop line location and represented as a distance. Figs. 6 and 7 show heat maps that represent the space-time distribution of the rear-end conflicts at TTC thresholds of 1.5 s, and 3 s, respectively.

As shown in Figs. 6 and 7, during the red light, all conflicts occur upstream the stop line. At the beginning of the red light, when the queue length is very short, most of conflicts occur just behind the stop line. After that, the queue length increased gradually, and the most intensive location of conflicts moves backward away from the stop line. By the start of the green light, the cumulative queue starts to discharge and the hot spot of conflicts disappeared gradually with the progression of the green time. Also it can be noted that conflicts are distributed with time upstream and downstream the stop line during the green and yellow times. This is reasonable because, during these times, both of the conflicting vehicles are moving with a speed larger than zero which causes some conflicts to have a potential location downstream the stop line.

The heat maps illustrate graphically the association between the rear-end conflicts and the shock wave area. It can be noted that

![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-11.jpg?height=860&width=1531&top_left_y=1487&top_left_x=179)
Fig. 6. Space-time heat map for rear-end conflicts (TTC < 1.5 s) for all studied locations (6 intersections).

![](https://cdn.mathpix.com/cropped/49bb4c85-5040-4c1c-b66b-a7981251ddee-12.jpg?height=862&width=1531&top_left_y=185&top_left_x=179)
Fig. 7. Space-time Heat Map for Rear-end Conflicts (TTC < 3 s) for all studied locations (6 intersections).

the intensive conflict area in the heat map (red, yellow, and green spots) forms, approximately, a polygon that is similar to the hypothetical triangle of the shock wave area where the traffic flow state is II (shown in Fig. 3).

Also, it is noteworthy to mention that the heat maps show two areas with red spots (most intensive conflict areas). The first one occurs at the beginning of the red light, which most probably represents the dilemma zone where the traffic signal indication changes from green to yellow to red. The second one occurs during the start of the green time where the stopped flow starts to discharge gradually at low speed while other vehicles are arriving at higher speeds to the end of the queue. The heat maps show a relationship between the rear-end conflicts and the queue length. For example, the most intensive conflict area in the heat map is located upstream the stop line within a distance that approximately represents the 50th percentile of the maximum queue length. As well, most of the conflicts occur within a distance that approximately represents the 85th percentile of the maximum queue length.

6. Potential applications
Several potential implementations of the models can be summarized as follows:
(a) Safety evaluation using field-observed data:
The traffic parameters at each signal cycle can be observed in the field or by video camera and used in the models to estimate the predicted number of rear-end conflicts that is necessary for safety evaluation.
(b) The calibration of the microsimulation models for safety evaluation:
Generally, the use of microsimulation models in safety analysis has been criticized for two main reasons. First, vehicles in the simulation models follow specific rules which are aimed at avoiding collisions. Therefore, it is very difficult to represent unsafe vehicle interactions and near misses. Second, there are many parameters and several ways to model traffic in simulation models in microsimulation models. Therefore, the results can vary significantly depending on the input values of the model parameters and the approach used in modeling (Essa and Sayed, 2016). Furthermore, a rigorous calibration process is essential in order to avoid inaccurate results. Researchers have advocated the use of field measured conflicts in the calibration process but this data can be difficult to obtain (Essa and Sayed, 2016). The developed models in this paper can be used to facilitate the calibration process of the simulation models. The target of calibration process can be matching the actual and the simulated traffic parameters used in the developed SPFs (such as the queue length and the shock wave characteristics) instead of matching the actual and the simulated traffic conflicts.
(c) The real-time safety optimization of signalized intersections:
Real-time safety monitoring and evaluation gained interest among researchers as a proactive strategy to improve safety (Shi and Abdel-Aty, 2015; Oh et al., 2005; Hossain and Muromachi, 2012; among others). Real-time data of the approaching vehicles will be available in the connected-vehicles environment via vehicle-to-vehicle (V2V) and vehicle-to-infrastructure (V2I) communications (Harding et al., 2014). The connected-vehicles data can be used to obtain various traffic parameters and performing a real-time adaption of signal design by minimizing the total delays and the queue length (Feng et al., 2015). The models,

developed in this paper, can be used to predict the number of rear-end conflicts using the obtained traffic parameters in real-time. This can be useful in giving insight about how changes in the signal cycle design affects the safety of signalized intersections Thus, the real-time adaption of the signal design can consider both mobility and safety. This can be obtained by solving a multiobjective optimization process that seeks minimizing both the total delays and the total number of traffic conflicts for all the intersection approaches.

## 7. Summary and conclusions

The main objective of this paper is to develop conflict-based safety performance functions (SPFs) for signalized intersections at the signal cycle level. Traffic video-data was recorded for six signalized intersections located in two cities in Canada. A video analysis procedure was proposed to collect rear-end conflicts and various traffic variables at each signal cycle from the recorded videos. The TTC was used as a traffic conflict indicator. The traffic variables include: traffic volume, maximum queue length, shock wave speed and area, and the platoon ratio.

The SPFs were developed using the GLM approach, where the traffic volume per cycle represented the exposure measure. The error structure in the developed models was assumed to be Poisson or Negative Binomial (Poisson-Gamma). The goodness of fit of the developed GLM models was assessed using: scaled deviance (SD), Pearson chi-squared ( $\chi^{2}$ ), and AIC.

The results show that all the developed models have good fit and almost all the explanatory variables are statistically significant. All the covariate coefficients have logical signs. In other words, the number of traffic conflicts is expected to increase during the signal cycles that have long queues, bigger shock waves, and lower platoon ratios.

The shock wave area, the maximum queue length, the shock wave speed, and the platoon ratio are shown to be important characteristics that affect the number of rear-end conflicts at the signal cycle. Incorporating one of these characteristics or a combination of them, along with the traffic volume, in the conflict-based SPFs of signalized intersections is recommended to improve the model fit and provide a better prediction of the conflict occurrence beyond what can be expected from the traffic volume only.

Furthermore, space-time conflict heat maps were developed from all observed signal cycles to investigate the distribution of traffic conflicts. The heat maps illustrate graphically the association between the rear-end conflicts and both of shock wave area and the queue length. Also, the heat maps show that most of rear-end conflicts occur during: (1) the beginning of the red light which represents the dilemma zone where the traffic signal changes from green to yellow to red; (2) the start of the green time where the stopped flow starts to discharge gradually at low speed while other vehicles are arriving at higher speeds to the end of the queue.

The developed models in this paper can have potential applications including: facilitating safety evaluation of signalized intersections using field-observed data; simplifying the calibration process of the microsimulation models for safety evaluation; and realtime optimization of signalized intersection safety by changing the signal design. Future areas of research may include these applications.

Future areas of research are suggested to overcome several limitations of this paper. These includes: (1) validating the developed SPFs using additional datasets; (2) developing advanced models that account for the unobserved heterogeneity across different sites using other statistical approaches such as the Full Bayes approach; (3) incorporating other conflict indicators (such as the PET, collision probability, safe stopping distance, among others) and developing of a safety index that comprises several conflict indicators to better reflect conflict severity. Finally, more work is needed to investigate the relationship between collisions and conflicts.

## References

AASHTO, 2010. Highway Safety Manual. American Association of State Highway and Transportation Officials, Washington, DC.
Abdel-Aty, M.A., Kuo, P.F., Jiang, X., Lee, J., Al Amili, S., 2014. Two Level Approach to Safety Planning Incorporating the Highway Safety Manual (HSM) Network Screening.
Amundsen, F., Hydén, C., 1977. Proceedings of First Workshop on traffic Conflicts. Institute of Economics, Oslo, s.n.
Autey, J., Sayed, T., Zaki, M., 2012. Safety evaluation of right-turn smart channels using automated traffic conflict analysis. Accid. Anal. Prev. 45, 120-130.
Chin, Hoong-Chor, Quek, Ser-Tong, 1997. Measurement of traffic conflicts. Saf. Sci. 3 (26), 169-185.
Cunto, Flávio, Saccomanno, Frank F., 2008. Calibration and validation of simulated vehicle safety performance at signalized intersections. Accid. Anal. Prev. 3 (40), 1171-1179.
Dijkstra, Atze, Marchesini, Paula, Bijleveld, Frits, 2010. Do calculated conflicts in microsimulation model predict number of crashes? Transp. Res. Rec. 1 (2147), 105-112.
El-Basyouny, K., Sayed, Tarek, 2013. Safety performance functions using traffic conflicts. Saf. Sci. 51, 160-164.
Elmitiny, N., Yan, X., Radwan, E., Russo, C., Nashar, D., 2010. Classification analysis of driver's stop/go decision and red-light running violation. Accid. Anal. Prev. 42 (1), 101-111.
Elvik, Rune, Erke, Alena, Christensen, Peter, 2009. Elementary units of exposure. Transp. Res. Rec.: J. Transp. Res. Board 2103, 25-31.
Essa, Mohamed, Sayed, Tarek, 2016. A comparison between PARAMICS and VISSIM in estimating automated field-measured traffic conflicts at signalized intersections. J. Adv. Transp.
Essa, Mohamed, Sayed, Tarek, 2015. Simulated traffic conflicts: do they accurately represent field-measured conflicts? Transp. Res. Rec.: J. Transp. Res. Board 2514, 48-57.
Essa, Mohamed, Sayed, Tarek, 2015. Transferability of calibrated microsimulation model parameters for safety assessment using simulated conflicts. Accid. Anal. Prev. 84, 41-53.
Feng, Y., Head, K.L., Khoshmagham, S., Zamanipour, M., 2015. A real-time adaptive signal control in a connected vehicle environment. Transp. Res. Part C: Emerg. Technol. 55, 460-473.
Gettman, Douglas, Head, Larry, 2003. Surrogate safety measures from traffic simulation models. Transp. Res. Rec. 1840, 104-115.
Gettman, Douglas, Pu, Lili, Sayed, Tarek, Steven, 2008. Surrogate Safety Assessment Model and Validation: Final Report. FHWA-HRT-08-051.
Guo, F., Wang, X., Abdel-Aty, M.A., 2010. Modeling signalized intersection safety with corridor-level spatial correlations. Accid. Anal. Prev. 42 (1), 84-92.
Harding, J., et al., 2014. Vehicle-to-vehicle Communications: Readiness of V2V Technology for Application (Report No. DOT HS 812 014). United States Department of Transportation [U.S DOT], National Highway Traffic Safety Administration [NHTSA], Washington, DC.

Hayward, John C., 1972. Near-miss determination through use of a scale of danger. Highway Res. Rec. 384.
Highway Capacity Manual, 2000. Transportation Research Board, Washington, D.C..
Hossain, M., Muromachi, Y., 2012. A Bayesian network based framework for real-time crash prediction on the basic freeway segments of urban expressways. Accid. Anal. Prev. 373-381.
Huang, Fei, Liu, Pan, Hao, Yu., Wang, Wei, 2013. Identifying if VISSIM simulation model and SSAM provide reasonable estimates for field measured traffic conflicts at signalized intersections. Accid. Anal. Prev. 50, 1014-1024.
Ismail, K., Sayed, T., Saunier, N., 2013. A methodology for precise camera calibration for data collection applications in urban traffic scenes. Can. J. Civ. Eng. 1 (40), 57-67.
Ismail, K., Sayed, T., Saunier, N., 2010. Automated analysis of pedestrian-vehicle conflicts: a context for before-and-after studies. Transp. Res. Rec.: J. Transp. Res. Board 2198, 52-64.
Ismail, K., Sayed, T., Saunier, N., 2011. Methodologies for aggregating indicators of traffic conflict. Transp. Res. Rec.: J. Transp. Res. Board 2237, 10-19.
Jahangiri, A., Rakha, H., Dingus, T.A., 2016. Red-light running violation prediction using observational and simulator data. Accid. Anal. Prev. 96, 316-328.
Laureshyn, A., Ardö, H., Svensson, Å., Jonsson, T., 2009. Application of automated video analysis for behavioural studies: concept and experience. IET Intel. Transport Syst. 3 (3), 345-357.
Lee, J., Abdel-Aty, M., Cai, Q., 2017. Intersection crash prediction modeling with macro-level data from various geographic units. Accid. Anal. Prev. 102, 213-226.
Lyon, C., Haq, A., Persaud, B., Kodama, S., 2005. Safety performance functions for signalized intersections in large urban areas: development and application to evaluation of left-turn priority treatment. Transp. Res. Rec.: J. Transp. Res. Rec.: J. Transp. Res. Board 1908, 165-171.
Machiani, S.G., Abbas, M., 2016. Safety surrogate histograms (SSH): a novel real-time safety assessment of dilemma zone related conflicts at signalized intersections. Accid. Anal. Prev. 361-370.
May, Adolf D., 1990. Traffic Flow Fundamentals.
Miaou, S.P., Lord, D., 2003. Modeling traffic crash-flow relationships for intersections: dispersion parameter, functional form, and Bayes versus empirical Bayes methods. Transp. Res. Rec.: J. Transp. Res. Board 1840, 31-40.
Oh, J.S., Oh, C., Ritchie, S.G., Chang, M., 2005. Real-time estimation of accident likelihood for safety enhancement. J. Transp. Eng. 131 (5), 358-363.
Papaioannou, P., 2007. Driver behaviour, dilemma zone and safety effects at urban signalised intersections in Greece. Accid. Anal. Prev. 39 (1), 147-158.
Persaud, B., Saleem, T., Faisal, S., Lyon, C., Chen, Y., Sabbaghi, A., 2012. Adoption of highway safety manual predictive methodologies for canadian highways. Proceedings from the 2012 Conference of the Transportation Association of Canada, Fredericton, New Brunswick.
Persaud, Bhagwant, Lan, Bo, Lyon, Craig, Ravi, Bh., 2010. Comparison of empirical Bayes and full Bayes approaches for before-after road safety evaluations. Accid. Anal. Prev. 42 (1), 38-43.
Poch, M., Mannering, F., 1996. Negative binomial analysis of intersection-accident frequencies. J. Transp. Eng. 122 (2), 105-113.
Sacchi, E., Sayed, Tarek, DeLeur, P., 2013. A comparison of collision-based and conflict-based safety evaluations: the case of right-turn smart channels. Accid. Anal. Prev. 59, 260-266.
Sacchi, Emanuele, Sayed, Tarek, 2016b. Bayesian estimation of conflict-based safety performance functions. J. Transp. Saf. Secur. 8 (3), 266-279.
Sacchi, Emanuele, Sayed, Tarek, 2016a. Conflict-based safety performance functions for predicting traffic collisions by type. Transp. Res. Rec. J. Transp. Res. Board 2583, 50-55.
Saunier, N., Sayed, Tarek, 2008. Probabilistic framework for the automated analysis of the exposure to road collision. Transp. Res. Rec.: J. Transp. Res. Board 2083, 96-104.
Sawalha, Ziad, Sayed, Tarek, 2001. Evaluating safety of urban arterial roadways. J. Transp. Eng. 127 (2), 151-158.
Sawalha, Ziad, Sayed, Tarek, 2006. Traffic accident modeling: some statistical issues. Can. J. Civ. Eng. 33 (9), 1115-1124.
Sayed, T., Zein, S., 1999. Traffic conflict standards for intersections. Transp. Plann. Technol. (Transp. Plann. Technol.) (22), 309-323.
Shahdah, Usama, Saccomanno, Frank, Bhagwant, Persaud, 2014. Integrated traffic conflict model for estimating crash modification factors. Accid. Anal. Prev. 71, 228-235.
Shi, Q., Abdel-Aty, M., 2015. Big data applications in real-time traffic operation and safety monitoring and improvement on urban expressways. Transp. Res. Part C: Emerg. Technol. 58, 380-394.
Songchitruksa, Praprut, Tarko, Andrew P., 2006. The extreme value theory approach to safety estimation. Accid. Anal. Prev. 4 (38), 811-822.
van der Horst, Richard, Hogema, Jeroen, 1993. Time-to-collision and collision avoidance systems. Proceedings of the 6th ICTCT Workshop.
Wang, X., Abdel-Aty, M., Brady, P., 2006. Crash estimation at signalized intersections: significant factors and temporal effect. Transp. Res. Rec.: J. Transp. Res. Board 1953, 10-20.
Wang, Xuesong, Abdel-Aty, M., 2008. Modeling left-turn crash occurrence at signalized intersections by conflicting patterns. Accid. Anal. Prev. 40 (1), 76-88.
Wong, S.C., Sze, N.N., Li, Y.C., 2007. Contributory factors to traffic crashes at signalized intersections in Hong Kong. Accid. Anal. Prev. 39 (6), 1107-1113.
Zhang, Xin, Liu, Pan, Chen, Yuguang, Bai, Lu, Wang, Wei, 2014. Modeling the frequency of opposing left-turn conflicts at signalized intersections using generalized linear regression models. Traffic Injury Prevent. 15 (6), 645-651.


[^0]:    * Corresponding author.
    E-mail addresses: m.a.essa@civil.ubc.ca (M. Essa), tsayed@civil.ubc.ca (T. Sayed).

[^1]:    K: Dispersion parameter for Negative binomial family.
    All variables are significantly different from zero at 95\% confidence level.

    * Significantly different from zero at 90\% confidence level.

