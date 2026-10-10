# Modeling Driver Behavior Within a Signalized Intersection Approach Decision-Dilemma Zone 

Hesham Rakha, Ahmed Amer, and Ihab El-Shawarby

This study uses data gathered in a field test on 60 test participants to develop models that characterize driver brake perception-reaction times (PRTs), brake times, and stop-go decisions at the onset of a yellow indication at a high-speed signalized intersection approach. The study demonstrates that driver PRTs are influenced only by the driver's time to intersection (TTI) at the onset of the yellow indication. The driver PRT is found to increase linearly with TTI and is not affected by the vehicle speed (in the range of 54 to 88 km/h), driver gender, or driver age. In the case of stop-go behavior, the older driver ( $\boldsymbol{\geq} \mathbf{6 5}$ years of age) dilemma zone is wider, ranging from a TTI of 4.81 to 1.66 s versus 4.90 to 2.87 s for the younger age group. Female drivers are more likely to stop than male drivers and tend to have a dilemma zone that is closer to the intersection. Finally, the study demonstrates that dilemma zone control systems should consider a dilemma zone from 5.0 to 1.5 s instead of the current state of practice of 5.5 to 2.5 s to capture all potential driver age and gender groups.

High-speed signalized intersections are typically associated with vehicle crashes resulting from decision-dilemma zone problems. Dilemma zones are defined in either time or space, as zones where some drivers may decide to proceed through an intersection while others may decide to stop at the onset of a yellow indication. Incorrect driver decisions can lead to rear-end crashes if a driver decides to stop when he or she should have proceeded and right-angle crashes with side-street traffic when a driver proceeds when he or she should have stopped. Driver decision within a dilemma zone may vary as a function of the driver's perception-reaction time (PRT), driver's acceptable deceleration rate, driver's age, driver's gender, and driver's time to intersection (TTI) at the instant when the yellow indication is introduced.

Several research efforts have attempted to address the dilemma zone problem using various intelligent transportation system (ITS) strategies. These strategies include basic green-extension systems, enhanced green-extension systems, and green-termination systems (1-4). More recently, researchers developed the detection-control system (D-CS), which uses two loop detectors in a speed trap configuration installed about 300 m upstream of the intersection on the main approach to detect the presence and measure the speed of indi-

[^0]vidual vehicles (5, 6). Speed information is then used to predict vehicle arrivals in the dilemma zone, and ultimately at the intersection, assuming vehicles travel at a constant speed over the 300 m distance. The system assumes a constant dilemma zone, defined by TTIs ranging between 5.5 and 2.5 s. The D-CS implements a two-step gap-out (maximum gap size between consecutive vehicles) strategy to reduce the probability of max-out (reaching the maximum green time) and thus reduce the probability of trapping vehicles in the dilemma zone. During the first step, the D-CS holds the green indication until the dilemma zone is clear of any vehicles. If the dilemma zone is not cleared after a certain time, the D-CS applies a second-step relaxed criterion that allows the green to end when there is only one car in the dilemma zone (but not a truck). This two-stage operation mimics the operation of the LHOVRA and SOS systems, developed in Sweden (1, 2).

The current dilemma zone mitigation systems assume that the driver dilemma zone is fixed (ranges between 5.5 to 2.5 s from the intersection) considering a 1.0 s PRT. However, it is not clear how driver PRTs and corresponding dilemma zones vary as a function of drivers' characteristics and their TTI. A number of studies have demonstrated that brake PRTs may be much longer than 1.0 s and that the 85th percentile PRT is more in the range of 1.5 to 1.9 s (7). These studies have also demonstrated that PRTs on high-speed intersection approaches (greater than 64 km/h) are lower, with 85th percentile PRTs in the range of 1.1 to 1.3 s. All studies, however, have measured the PRT as the time difference between the onset of the yellow phase and the activation of the vehicle's brake lights; thus, the PRT estimates include the time lag from the instant the driver presses the brake pedal until the brake lights are displayed.

The objectives of this paper are fourfold. First, the paper develops models for estimating driver perception, reaction, and PRT times considering the vehicle's instantaneous speed and TTI at the onset of the yellow interval. Second, it compares the controlled field study driver behavior to naturalistic field driver behavior. Third, it develops data transformation procedures to adjust controlled field study data to reflect naturalistic field driver behavior. Fourth, the paper evaluates gender and age impacts on driver PRTs and stop-go decisions. It is anticipated that the models developed in this paper can be incorporated within microscopic traffic simulation software to enhance the modeling of driver behavior at the onset of a yellow interval.

A background of the problem is presented followed by a brief description of the data gathering procedures. Subsequently, driver perception, reaction, and PRTs are characterized. Next, driver stop-go decisions and dilemma zone boundaries are studied. Finally, conclusions of the paper are presented.

## BACKGROUND

A review of fundamental concepts associated with reaction times provides a better understanding of factors related to PRT and driver behavior within a dilemma zone. When a driver responds to a sensory input, such as the onset of a yellow light at a traffic signal, the total reaction time can be split into a mental processing time (time required for the driver to perceive the sensory input and to decide on a response) and a movement time (time used to perform the programmed movement, such as lifting the foot from the accelerator and touching the brake). Because the mental processing time is an internal quantity that cannot be measured directly and objectively without a physical response, it is usually measured jointly with the movement time (8).

In the case of a driver arriving at a signalized intersection when the indication changes from green to yellow, the time interval from the onset of the yellow light to the instant when the brake pedal is pressed is called the perception-reaction time $(9,10)$ perception response time (11), brake reaction time (8, 12), perception-braking response time (13), yellow response time (14), or brake-response time (15). This paper refers to the interval as the perception-reaction time (PRT).

Taoka stressed that PRTs measured under anticipatory conditions, when drivers are aware that their PRTs are recorded, are shorter than the expected values under normal driving conditions (7). In a comprehensive survey that summarized PRT results from most studies published until 2000, Green classified PRT studies into three basic types: simulator studies, controlled road studies, and naturalistic observation (8). Controlled road studies and naturalistic observation are both field approaches but differ in the sense that, in the latter, the driver is unaware of the data collection effort. Each type of study has limitations to the degree in which results can be generalized to normal driving conditions. PRT measurements from driving simulators are typically shorter than those measured in vehicles because simulators typically have simplified visuals, smaller fields of view, no depth, no nonvisual cues, and small cognitive loads. Some may argue that the cognitive load is higher in simulators. Controlled-road studies may also produce shorter PRT measurements because drivers may be more alert than in normal driving conditions. Both simulator and controlled-road studies create practice effects owing to the many trials used to gather data for each driver. Alternatively, naturalistic studies have the highest validity, but they are also limited because it is not possible to test effects of independent variables, place drivers in emergency or even urgent situations, measure perception and movement times separately, or control driver demographics to avoid sample bias.

PRTs at traffic signals also include some lag time because the onset of the yellow does not always require immediate braking reaction unless the driver is close to the intersection. In a study by Chang et al., seven intersections were observed, and driver PRTs (defined as "the time elapsed from the onset of the yellow until the brake light is observed") were recorded (14). This lag should be small or nonexistent on high-speed signalized approaches because the high speed requires immediate reactions to avoid excessive deceleration or even collisions with other vehicles. The study focused on the effect of distance from the intersection at the onset of a yellow indication because, according to those authors, drivers tend to react faster as vehicles move closer to the intersection; when vehicles are farther away, the PRT might be longer because the urgency to make a decision is not as great. Accordingly, the study produced curves demonstrating significant variability in driver PRT as a function of the vehicle speed (different lines represent speeds in km/h) and distance to intersection at the instant the traffic signal turned yellow, as illustrated in Figure 1. It is demonstrated that if the $x$-axis were replaced with TTI instead of distance from intersection, the lines approach one another. Consequently, it seems that TTI would be a better explanatory variable because it combines two explanatory variables, as will be

![](https://cdn.mathpix.com/cropped/7cb6d512-512f-4b65-802b-0b4e1bf298b2-02.jpg?height=904&width=1738&top_left_y=1551&top_left_x=196)
FIGURE 1 Variation in (a) and (b) driver PRT and (c) and (d) deceleration rate as a function of distance and time to intersection and approach speed [based on Chang et al. (14)].

demonstrated later. Similar behavior is observed for vehicle decelerations, as demonstrated in Figure 1. However, in the case of vehicle deceleration levels, the effect of speed still appears to be significant. The results of the Chang et al. study suggest that speed effectively influences the median PRT, which converges to 0.9 s at speeds equal to or greater than 72 km/h (45 mph) (14). Other research efforts have also considered the use of TTI as an explanatory variable (16, 17).

A study that used a driving simulator to analyze the behavior of 77 drivers approaching signalized intersections at 70 km/h made similar conclusions (18). The study concluded that the TTI significantly affected the PRT, whereas age did not. The PRT grand mean was 0.96 s, ranging from 0.86 s for drivers closest to the intersection stop line to 1.03 s for drivers farthest from it.

To overcome the effect of the distance from the intersection on the PRT at the yellow indication onset, Wong and Goh used a transitional or dilemma zone, defined as the zone in which drivers are required to make a decision quickly or be forced to cross (13). Drivers before the dilemma zone must stop at the intersection (because they cannot legally cross); drivers after the dilemma zone must cross the intersection. The dilemma zone was defined in regard to the TTI, measured as the actual travel time for those vehicles that crossed the intersection and as the projected travel time for those that stopped. For the three intersections analyzed in Singapore, the dilemma zone was defined as lying between 4.2 and 2.3 s from the intersection stop bar. PRT was defined as the time elapsed from the yellow indication onset until the brake lights became visible. PRT values found for the transitional zone were 0.84 s (median), 0.86 s (mean), 0.64 s (15th percentile), and 1.08 s (85th percentile), following a log-normal distribution; this finding is consistent with those of other studies (7). In another paper, Goh and Wong reported shorter reaction times at intersections with red light surveillance cameras: 0.80 s for the median and mean and 1.00 s for the 85th percentile (11).

A recent study by Gates et al. evaluated the behavior of vehicles trapped in the dilemma zone, defined by the authors to be between 2.0 and 5.5 s (15). The study can be classified as a naturalistic observation study that recorded vehicle's behavior at six signalized intersections in the Madison, Wisconsin, area consisting of 463 first-to-go and 538 last-to-go records. The analysis included brake-response time and deceleration rate for first-to-stop vehicles, and probability of vehicle stopping and nonstopping. The 15th, 50th, and 85th percentile brake-response times were 0.7, 1.0, and 1.6 s, respectively. In regard to the vehicle stopping and nonstopping probability, the TTI was found to be by far the strongest variable affecting the stop-go decision among all other factors. Drivers were found to be more likely to stop rather than to go with greater TTI. A comparison between the calibrated model by Gates et al. [University of Wisconsin (UWn) model (15)] and the calibrated model [Virginia Tech (VT) model] are presented later in this paper.

## DATA DESCRIPTION

The experiment involved having each test participant drive an instrumented vehicle along a $2.6-\mathrm{km}$ private highway at approximately 72 km/h. After a practice run that allowed the participant to get acquainted with the vehicle, the participant approached a signalized intersection a number of times. Driver behavior was observed as the signal phases changed, and data on the participant's responses included vehicle speed, signal indication, and measurements of the pressing of the accelerator (throttle value) and brake (brake value) pedals. Worth mentioning is that the latter two measurements, throttle and brake values, are used to determine the perception and reaction times, as will be explained later. The experiment could then be classified as a controlled-road study, according to Green's classification scheme (8). While the drivers were not informed of the specific objectives of the study, they might have inferred these objectives as a result of the multiple runs they made at the signalized intersection.

This section describes the instrumented vehicle, test track, test participants, and how the data were collected.

## Instrumented Vehicle and Signal Controller Box

A real-time DAS was installed in a 2004 Chevrolet Impala, concealed from the driver's view, in the car trunk. This DAS was developed and built by the Center for Technology Development at the Virginia Tech Transportation Institute (VTTI) for collecting data for experiments such as this one. A notebook computer connected to the DAS controlled the sequence of test runs.

Signal phase data was also recorded in the data stream using a communications link between the DAS and the signal controller box installed at the intersection. The signal controller box, which was also developed at VTTI, was used to trigger the yellow phase when the front of the vehicle reached predetermined distances from the intersections. Phase changes were controlled from the instrumented car using a differential Global Positioning System to determine the distance from the intersection and a wireless communications link to trigger the phase changes.

## Intersection and Intersection Approaches

The test bed used for data collection was a signalized intersection at the Virginia Department of Transportation's Smart Road facility, located at VTTI. It is a state-of-the-art facility built for full-scale research and evaluation of pavement and intelligent transportation systems, technologies, and products. The Smart Road is a 3.5-km private highway limited to test vehicles. The section of the Smart Road used for the data collection includes a four-way signalized intersection, high-speed banked turnaround, and low-speed turnaround. The horizontal alignment is fairly straight, and the vertical profile of this segment is a 3\% slope. Thus, half of the trials run by each participant were on a 3\% upgrade and the other half on a 3\% downgrade. The uphill approach to the intersection was nearly 1.6 km long starting from the low-speed turnaround; the downhill approach was 0.5 km long starting from the high-speed turnaround. To the test participants, the appearance of the traffic signal and of the intersection was no different than normal signalized intersections on roads with a similar layout in southwest Virginia.

## Test Participants

The test participants for the study were recruited using posters, word of mouth, local newspaper ads, and the VTTI volunteer database. Participants were paid \$20/h. Interested drivers were screened to verify that they were licensed drivers and to determine if they had any health problems that could exclude them from participating in the study. Sixty drivers were recruited, 30 in each gender; 32 drivers were younger than 65 years, equally divided by gender; and 28 were 65 years or older, also equally divided by gender. The age structure was designed to allow the possible effects of slower response times
among older drivers to be more evident. The younger group had ages ranging from 20 to 64 years, with a mean age of 40 years; the older group had a mean age of 71 years, and ages ranged from 65 to 82 years.

## Procedure

Participants were tested individually under good conditions (daylight, good weather, dry pavement, etc.). On arrival at VTTI, participants were submitted to a visual acuity and color vision test. All participants selected had a minimum of 20/40 vision, passed the color vision test, and were screened by a medical questionnaire for drug and alcohol use and for any medical conditions that might impair driving. Participants were then escorted to the test vehicle and asked to familiarize themselves with the car, adjusting seat, mirrors, seat belts, and so on, and then to drive to the Smart Road, about 0.5 km away. Two experimenters rode in the car with the participant. During the drive to the Smart Road, one of the experimenters instructed the participant and answered questions while the other, in the back seat, used the onboard computer to control the trial conditions and the DAS. During the initial practice run, participants were asked to brake the car to a full stop from 40 km/h, 55 km/h, and 70 km/h to become familiar with handling of the car under hard braking.

In the experiment, participants were instructed to drive the car at 72 km/h (45 mph) except in the turnarounds or when stopping at the intersection. Participants were told about the objectives of the study. Not counting the initial practice run, participants drove along the entire test course (2.1 km downhill, low-speed turnaround, 2.1 km uphill, high-speed turnaround) 12 times, passing through the traffic lights 24 times (12 times uphill, 12 times downhill), composing 24 trials. At the beginning of each trial run, the signal displayed a green light. As the car approached the intersection, the onboard computer decided whether or not to trigger the yellow and, if so, at what distance from the stop bar.

The yellow duration was 4 s and was initiated when the front of the car was at the following distances from the stop bar: 32 m (105 ft), 55 m (180 ft), 66 m (215 ft), 88 m (290 ft), or 111 m (365 ft). Considering an approach speed of 72 km/h (45 mph) speed, these distances correspond to TTIs of 1.60 s, 2.75 s, 3.30 s, 4.40 s, and 5.55 s, respectively. Each participant faced phase changes from green to yellow four times for each distance. These 24 trial conditions (20 yellow lights and 4 green lights) ran in a predetermined, randomized sequence, with a different order for each participant. This implies that the number of times a participant encountered a yellow light at a given TTI on a given grade (up or down) varied between one and three times. In other words, the experimental design ensured that a driver had at least one of the four yellow light encounters on each of the two approaches.

## ANALYSIS OF DRIVER PERCEPTION-REACTION TIME

Before describing results of the analysis, the various parameters that were measured and a description of how they were measured are presented. Three response parameters were recorded; they included the perception time, reaction time, and brake time. Worth mentioning is that this analysis is conducted only on the stopping drivers at the onset of yellow. Identification of the start and the end of the different response parameters is not feasible in the case of nonstopping drivers, given that there is no tangible action to be measured. Accordingly, the perception time was defined as the time required by the driver to perceive the yellow indication and make his or her decision, either to stop or to go. It was measured from the time of yellow indication onset to the instant in time at which the driver lifted his or her foot from the gas pedal (throttle value $\leq 6 \%$ ). Alternatively, the reaction time was defined as the duration of time required by the driver to react after his or her perception of the yellow indication. It started from the instant the driver lifted his or her foot from the gas pedal (throttle value $\leq 6 \%$ ) until he or she pressed the brake pedal (brake value $\geq 1.67 \%$ ). Finally, the braking time was defined as the duration of time required by the vehicle to come to a complete stop starting from the moment the brake pedal was pressed (brake value $\geq 1.67 \%$ ) until the vehicle came to a complete stop (speed < 0.1 km/h). The perception reaction time was computed as the sum of both the perception and reaction times, whereas the stop time was computed as the sum of the three parameters: perception, reaction, and brake times. A total of 745 data records were available for analysis ranging from a minimum TTI of 1.34 s to a maximum of 6.19 s . The PRT ranged from 0.139 s to 2.400 s, while the brake time ranged from 2.9 to 14.4 s.

Although drivers were instructed to drive at a speed of 72 km/h (45 mph), the approach speeds at the yellow interval onset varied considerably from 54 to 88 km/h (34 to 52 mph), as illustrated in Figure 2b. Consequently, an initial model considering the TTI and approach speed at the yellow interval onset $(u)$ was formulated as

$$
t=b_{0}+b_{1} \mathrm{TTI}+b_{2} u
$$

where $b_{0}, b_{1}$, and $b_{2}$ are model constants. A robust linear regression was applied to the data to derive the model parameters. The robust linear regression fit uses an iteratively reweighted least squares algorithm, with the weights at each iteration calculated by applying the bisquare function to the residuals from the previous iteration. This MATLAB algorithm gives lower weight to points that seem to be outliers. Data that should be disregarded are given a weight of zero. Consequently, the regression model is less sensitive to outliers in the data as compared with ordinary least squares regression.

The speed coefficient was found to be insignificant in the case of the PRT, brake, and total stop time, with $t$-statistic probabilities ( $p$-values) of .37, .76, and .48, respectively. Given that speed was not found to be a statistically significant explanatory variable, the analysis did not consider the approach speed any further.

Having identified the critical independent variables, the next step in the analysis was to fit a single linear model and test for normality of the residual error. Unfortunately, a Kolmogorov-Smirnov (K-S) test revealed that there was insufficient evidence to conclude the data were normal $(p<.05)$, as is evident in Figure $2 a$. Different data transformations were considered including logarithmic and square root transformations; however, these did not result in normal PRT data. Finally, the data were sorted and aggregated based on their TTI into equal sized bins (equal number of observations) and the average parameter for each bin was computed. Using a bin size of 3 observations or greater the PRT, brake, and stop residual errors passed the K-S normality test with $p$-values of .73, .12, and .15, respectively. An illustration of the PRT and initial speed distribution following the data aggregation is also presented in Figure 2c and Figure $2 d$, considering a bin size of three observations. Again a robust linear regression was applied to the data to derive the model parameters (only a single observation was excluded from the analysis using the robust regression). The estimated model parameters and root-mean-square error (RMSE) for each of the response variables

![](https://cdn.mathpix.com/cropped/7cb6d512-512f-4b65-802b-0b4e1bf298b2-05.jpg?height=1311&width=1779&top_left_y=206&top_left_x=172)
FIGURE 2 Distribution of raw data for ( $a$ ) PRT and ( $b$ ) speed; distribution of aggregated data for ( $c$ ) PRT and ( $d$ ) speed.

are summarized in Table 1. All models and variables were statistically significant, demonstrating that the PRT, deceleration (brake) time, and total stop time increase linearly as the TTI increases.

The model predictions seem to be consistent with the field data, as illustrated in Figure $3 a$ through $3 c$. The model is valid for a TTI range of 1.5 to 6.0 s and should not be used outside this range.

The slope of the PRT is significantly less than the slope of brake and total stop times, demonstrating that the PRT is less sensitive to the TTI in the 1.5 to 6.0 s range. Furthermore, summation of the PRT and brake time coefficients approximately equals the stop time coefficients, as expected, given that the stop time equals to the summation of both times. Interestingly, an earlier field study by Chang et al. (14) found that the PRT was more sensitive to the TTI, as illustrated in Figure $4 a$ and $4 b$.

Results presented here are identical to those of the Chang et al. (14) study at a TTI of 2.77 s (the lowest TTI considered in the Chang et al. study). It seems that in the controlled field study (Smart Road study), given that drivers encountered more yellows than greens, they were more alert and thus less sensitive to the TTI. A correction factor for the PRTs was computed in which coefficients of the correction factor (CF) equal the difference in model coefficients, as illustrated in Figure 4. In this case, the PRT correction factor equals the following:

$$
\mathrm{CF}_{\text {PRT }}=-0.6049+0.2189 \times \mathrm{TTI}
$$

A sensitivity analysis considering different data aggregation levels was conducted. Results demonstrate that overall the model

TABLE 1 Summary of Model Parameters
| Measure | K-S Prob. | RMSE | $b_{0}$ | $b_{1}$ |
| :--- | :--- | :--- | :--- | :--- |
| PRT (s) | 0.73 | 0.0886 | 0.4784 (<.0005) | 0.0577 (<.0005) |
| Brake time (s) | 0.12 | 0.5156 | 0.2008 (<.033) | 1.8297 (<.0005) |
| Stop time (s) | 0.15 | 0.4606 | 0.6022 (<.0005) | 1.8845 (<.0005) |


$p$-values in parentheses.

![](https://cdn.mathpix.com/cropped/7cb6d512-512f-4b65-802b-0b4e1bf298b2-06.jpg?height=1405&width=1755&top_left_y=322&top_left_x=183)
FIGURE 3 Parameter variation as a function of TTI: (a) PRT, (b) brake time, and (c) stop time.

![](https://cdn.mathpix.com/cropped/7cb6d512-512f-4b65-802b-0b4e1bf298b2-06.jpg?height=507&width=1775&top_left_y=1865&top_left_x=176)
FIGURE 4 Model comparison of results by Chang et al. (14): (a) PRT and (b) difference.

coefficients are marginally affected by the level of aggregation considered in the model development (differences in the third decimal place).

In an attempt to quantify potential differences in driver behavior as a function of driver age and gender, data were divided into two age groups (Group 1: <65 years of age and Group 2: $\geq 65$ years of age). A full model for the PRT of the form was as follows:

$$
t=b_{0}+b_{1} \mathrm{TTI}+b_{2} z+b_{3} z \text { TTI }
$$

The model was fit to the data where $z$ is a binary variable that is equal to 1 for Group 1 and 0 for Group 2. A statistical comparison of the full model to the partial model of form

$$
t=b_{0}+b_{1} \mathrm{TTI}
$$

revealed no statistical difference using an $F$-test [ $p \ll .0005$ for $F(2,727)$ ]. Similarly, no statistical differences were found in PRTs associated with driver gender. Consequently, the results revealed no statistical differences in PRTs associated with driver age and gender. Similarly, gender and age were found to have no impact on the brake (deceleration) time ( $p \ll .0005$ ). These findings are consistent with those of an earlier study conducted using distance to intersection as opposed to TTI (19).

## MODELING DRIVER STOP-GO BEHAVIOR

A total of 1,186 stop-go decisions were available for analysis. Data included driver age, gender, TTI, vehicle speed at the onset of yellow, and a binary (0 or 1) driver stop decision variable to indicate whether a driver stopped or proceeded through the intersection. By using the data, a generalized linear model of the logistic type was fit to the data considering a binomial distribution of the form

$$
\ln \left(\frac{P_{r}}{P_{s}}\right)=\ln \left(\frac{1-P_{s}}{P_{s}}\right)=c_{0}+c_{1} \mathrm{TTI}
$$

where

$$
\begin{aligned}
& P_{r}=\text { probability of running, } \\
& P_{s}=\text { probability of stopping, and } \\
& c_{1}=\text { model constants. }
\end{aligned}
$$

The model calibrated parameters were 4.486 and -1.806 for parameters $c_{0}$ and $c_{1}$, respectively ( $p \ll .0005$ ). The model produced a 13.66\% prediction error (a total of 162 wrong decisions out of the 1,186 trials). The field observed data and model fit are illustrated graphically in Figure 5. To illustrate the field data graphically, the probability of stopping $\left(P_{s}\right)$ was computed considering a bin size of 20 observations sorted by TTI ( $P_{s}$ was computed as the number of

![](https://cdn.mathpix.com/cropped/7cb6d512-512f-4b65-802b-0b4e1bf298b2-07.jpg?height=1268&width=1742&top_left_y=1225&top_left_x=191)
FIGURE 5 Smart Road field data and model predictions of probability of stopping: ( $a$ ) actual data and ( $b$ ) log-transformed data.

stopped trials divided by the 20 total trials within the bin). The field data, as is the case with previous field studies, clearly demonstrates a decrease in the probability of stopping as the TTI decreases. The figure also demonstrates a good match between the VT model estimates and field observations with some outlier field observations at the 5.5 and 6.1 TTIs.

Because drivers experienced more yellow than green indications (20 yellows versus four greens), it appeared that drivers were more willing to stop at shorter TTIs when compared with uncontrolled field test results reported in the literature, as illustrated in Figure 5 (comparing the controlled smart road VT Model with uncontrolled field test UWn Model). As mentioned earlier, a study conducted by the University of Wisconsin reported a model with $c_{0}$ and $c_{1}$ coefficient values of 6.34 and -1.69, respectively (15). Consequently, a data transformation of the Smart Road TTI observations was applied to adjust for the higher propensity for vehicle stopping in the controlled field test versus uncontrolled field test; while maintaining the advantage of tracking the subject driver in the controlled test versus an uncontrolled field test. Computation of the data transformation parameters can be derived considering the adjusted TTI (TTI') as

$$
\mathrm{TTI}^{\prime}=\alpha_{0}+\left(1+\alpha_{1}\right) \mathrm{TTI}
$$

A data transformation from the VT model to the UWn model parameters can be computed considering that

$$
c_{0}+c_{1} \mathrm{TTI}^{\prime}=c_{0}^{\prime}+c_{1}^{\prime} \mathrm{TTI}
$$

where $\mathrm{c}_{0}^{\prime}$ and $\mathrm{c}_{1}^{\prime}$ are the desired model parameters (6.34 and -1.69, respectively). Solving Equation 7, the TTI adjustment factors $\alpha_{0}$ and $\alpha_{1}$ can be computed as

$$
\alpha_{0}=\frac{c_{0}^{\prime}-c_{0}}{c_{1}}
$$

and

$$
\alpha_{1}=\frac{c_{1}^{\prime}-c_{1}}{c_{1}}
$$

After deriving the data transformation parameters, the Smart Road field data were transformed and the logistic model was fit to the transformed data to produce a model similar to the UWn model, as illustrated in Figure 6a and 6b. The optimized model parameters are estimated at 5.82 and -1.62 $(p \ll .0005)$ with a prediction error rate of $12.8 \%$ and a dispersion parameter of 1.01 . This model is

![](https://cdn.mathpix.com/cropped/7cb6d512-512f-4b65-802b-0b4e1bf298b2-08.jpg?height=1283&width=1764&top_left_y=1199&top_left_x=172)
FIGURE 6 Transformed Smart Road field data and model predictions of probability of stopping: ( $a$ ) actual data and ( $b$ ) log-transformed data.

TABLE 2 Summary Results of Dilemma Zone Boundaries
|  | Raw |  | Transformed |  | Raw |  | Transformed |  | All |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | <65 | $\geq 65$ | <65 | $\geq 65$ | Male | Female | Male | Female | Raw | Transformed |
| $a$ | 5.198 | 3.988 | 8.381 | 4.511 | 4.783 | 4.208 | 5.877 | 5.796 | 4.486 | 5.816 |
| $b$ | -1.930 | -1.781 | -2.157 | -1.396 | -1.861 | -1.759 | -1.589 | -1.666 | -1.806 | -1.620 |
| $P(.10)$ | 1.55 | 1.01 | 2.87 | 1.66 | 1.39 | 1.14 | 2.32 | 2.16 | 1.27 | 2.23 |
| $P(.90)$ | 3.83 | 3.47 | 4.90 | 4.81 | 3.75 | 3.64 | 5.08 | 4.80 | 3.70 | 4.95 |
| Width | 2.28 | 2.47 | 2.04 | 3.15 | 2.36 | 2.50 | 2.77 | 2.64 | 2.43 | 2.71 |
| $E$ | 13.27\% | 13.20\% | 13.27\% | 13.20\% | 14.53\% | 13.30\% | 13.35\% | 11.95\% | 13.66\% | 12.82\% |


$a$ and $b=$ model parameters, $p(.10)=10$ th percentile, $p(.90)=90$ th percentile, $E=$ prediction error rate.
statistically equivalent to the UWn model, given that the parameter standard errors are 0.41 and 0.10 , respectively.

The next step in the analysis was to consider potential differences in driver behavior associated with driver gender or age. In the case of age impacts, the data were grouped into two groups: ages <65 and ages $\geq 65$. A full model of the form

$$
\ln \left(\frac{P_{r}}{P_{s}}\right)=\ln \left(\frac{1-P_{s}}{P_{s}}\right)=c_{0}+c_{1} \mathrm{TTI}+c_{2} \mathrm{z}+c_{3} \mathrm{z} \mathrm{TTI}
$$

was fit to the data, where $z$ is a flag indicating the driver age group ( 0 for < 65 and 1 for $\geq 65$ ). The error for the full model and the partial model were then compared to identify differences in driver behavior associated with age. The computed $F$-statistic $\left(F_{c}\right)$ was estimated as

$$
F_{c}=\frac{\frac{\left(\mathrm{SSE}_{r}-\mathrm{SSE}_{f}\right)}{\mathrm{DF}_{1}}}{\frac{\mathrm{SSE}_{f}}{\mathrm{DF}_{2}}}
$$

where

$$
\begin{aligned}
\mathrm{SSE}_{r}= & \text { sum-of-squared error for the reduced model (all ages), } \\
\mathrm{SSE}_{f}= & \text { sum of squared error for the full model (considering two } \\
& \text { age groups), } \\
\mathrm{DF}_{1}= & \text { number of parameters being tested (in this case 2), and } \\
\mathrm{DF}_{2}= & \text { degrees of freedom for the full model (in this case } n-4= \\
& 1,182) \text {. }
\end{aligned}
$$

Given that the computed $F$-statistic (32.1866) exceeds the tabulated 95th-percentile $F$-statistic $[F(2,1182)=3.0033]$, it is concluded that the difference between the two age groups is statistically significant. In the case of gender, the $F$-statistic is 3.31, which is slightly greater than 95th-percentile $F$-statistic (3.00). Consequently, one can conclude that the gender difference is statistically significant.

The results demonstrate that the dilemma zone for older drivers ( $\geq 65$ years of age) is larger (ranges from a TTI of 4.81 to 1.66 s) than that for the younger driver population (ranges from 4.90 to 2.87 s), as summarized in Table 2. Female drivers tend to delay their stop-go decision compared with male drivers (i.e., dilemma zone is closer to the intersection). In regard to the design of dilemma control systems, the study demonstrates that the dilemma zone should be expanded and shifted from the current range of 2.5 to 5.5 s range to 1.5 to 5.0 s.

## CONCLUSIONS

In regard to driver perception-reaction, brake, and stop times, the following two conclusions are drawn. Driver PRTs are influenced only by the driver's TTI at the onset of the yellow indication. Also, the driver PRT is found to increase linearly with TTI and is not influenced by the vehicle speed (in the range of 54 to 88 km/h), driver gender, or driver age.

Furthermore, pertaining to driver stop-go decisions, the study demonstrated the following:

1. The use of a controlled field testbed is suitable for gathering driver behavior within the traffic signal dilemma zone. Data transformations may be required to replicate naturalistic field data; however, these transformations are simple. Specifically, the paper develops mathematical formulations for such transformations.
2. Drivers in the $\geq 65$ years of age group tend to have a wider width for the dilemma zone in comparison with the younger age group (3.15 versus 2.03 s).
3. Drivers in the $\geq 65$ years of age group have a dilemma zone that is closer to the intersection (ranges from a TTI of 4.81 to 1.66 s) versus 4.90 to 2.87 s for the younger age group.
4. Female drivers are more likely to stop when compared with male drivers and tend to have a dilemma zone that is closer to the intersection.
5. Dilemma control systems should consider a dilemma zone from 1.5 to 5.0 s instead of the current state of practice of 2.5 to 5.5 s.

## ACKNOWLEDGMENTS

The authors acknowledge the financial support from the Mid-Atlantic University Transportation Center, FHWA, and the Virginia Department of Transportation. In addition, the authors acknowledge the support of Mohamadreza Farzaneh, Huanyu Yue, and Wang Zhang for running the tests and thank Vaughan Inman and Gregory Davis for providing valuable comments throughout the research effort.

## REFERENCES

1. Kronborg, P. MOVA and LHOVRA: Traffic Signal Control for Isolated Intersections. Traffic Engineering and Control, Vol. 34, No. 4, 1993, pp. 195-200.
2. Kronborg, P., F. Davidsson, and J. Edholm. SOS-Self-Optimising Signal Control: Development and Field Trials of the SOS Algorithm for Self-Optimising Signal Control at Isolated Intersections. Transport Research Institute, Stockholm, Sweden, 1997.

3. Pant, P. D., and Y. Cheng. Dilemma Zone Protection and Signal Coordination at Closely Spaced High-Speed Intersections, FHWA 2001.
4. Peterson, A., T. Bergh, and K. Steen. LHOVRA: A New Traffic Signal Control Strategy for Isolated Junctions. Traffic Engineering and Control, Vol. 27, No. 7-8, 1986, pp. 388-389.
5. Zimmerman, K. H., and J. A. Bonneson. In-Service Evaluation of a Detection-Control System for High-Speed Signalized Intersections. FHWA/TX-05/5-4022-01-1. Texas Transportation Institute, Texas A\&M University, College Station, 2005.
6. Bonneson, J. A., D. R. Middleton, K. H. Zimmerman, H. A. Charara, and M. M. Abbas. Intelligent Detection-Control System for Rural Signalized Intersections. FHWA/TX-03/4022-2. Texas Transportation Institute, Texas A\&M University, College Station, 2002.
7. Taoka, G. T. Brake Reaction Times of Unalerted Drivers. ITE Journal, Vol. 59, No. 3, 1989, pp. 19-21.
8. Green, M. How Long Does It Take to Stop? Methodological Analysis of Driver Perception-Brake Times. Transportation Human Factors, Vol. 2, No. 3, 2000, pp. 195-216.
9. Bates, J. T. Perception-Reaction Time. ITE Journal, Vol. 65, No. 2, 1995, pp. 35-36.
10. Dimitropoulos, I., and G. Kanellaidis. Transportation Research Circular E-C003: Highway Geometric Design: The Issue of Driving Behavior Variability. TRB, National Research Council, Washington, D.C., 1998, pp. 1-7.
11. Goh, P.-K., and Y.-D. Wong. Driver Perception Response Time During the Signal Change Interval. Applied Health Economics and Health Policy, Vol. 3, No. 1, 2004, pp. 9-15.
12. Summala, H. Brake Reaction Times and Driver Behavior Analysis. Human Factors, Vol. 2, No. 3, 2000, pp. 217-226.
13. Wong, Y.-D., and P.-K. Goh. Perception-Braking Response Time of Unalerted Drivers at Signalized Intersections. ITE Journal, Vol. 71, No. 6, 2001, pp. 73-76.
14. Chang, M.-S., C. J. Messer, and A. J. Santiago. Timing Traffic Signal Change Intervals Based on Driver Behavior. In Transportation Research Record 1027, TRB, National Research Council, Washington, D.C., 1985, pp. 20-30.
15. Gates, T. J., D. A. Noyce, L. Laracuente, and E. V. Nordheim. Analysis of Driver Behavior in Dilemma Zones at Signalized Intersections. In Transportation Research Record: Journal of the Transportation Research Board, No. 2030, Transportation Research Board of the National Academies, Washington D.C., 2007, pp. 29-39.
16. Williams, W. L. Driver Behavior During the Yellow Interval (Abridgment). In Transportation Research Record 644, TRB, National Research Council, Washington, D.C., 1977, pp. 75-78.
17. van der Horst, R., and A. Wilmink. Drivers' Decision Making at Signalised Intersections: An Optimisation of the Yellow Timing. Traffic Engineering and Control, Vol. 27, No. 12, 1986, pp. 615-617.
18. Caird, J. K. Effect of Amber Light Onset Time on Older and Younger Drivers' Perception Response Time and Intersection Behavior. Presented at 84th Annual Meeting of the Transportation Research Board, Washington, D.C., 2005.
19. Setti, J. R., H. Rakha, and I. El-Shawarby. Analysis of Brake PerceptionReaction Times on High-Speed Signalized Intersection Approaches. Proc., IEEE Intelligent Transportation Systems Conference. Toronto, Ontario, Canada, Sept. 17-20, 2006.

The Vehicle User Characteristics Committee sponsored publication of this paper.


[^0]:    Center for Sustainable Mobility, Virginia Tech Transportation Institute, 3500 Transportation Research Plaza, Blacksburg, VA 24061. Corresponding author: H. Rakha, hrakha@vt.edu.

    Transportation Research Record: Journal of the Transportation Research Board, No. 2069, Transportation Research Board of the National Academies, Washington, D.C., 2008, pp. 16-25.
    DOI: 10.3141/2069-03

