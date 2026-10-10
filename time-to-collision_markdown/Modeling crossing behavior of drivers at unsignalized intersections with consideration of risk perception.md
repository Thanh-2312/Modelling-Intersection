# Modeling crossing behavior of drivers at unsignalized intersections with consideration of risk perception 

Miaomiao Liu ${ }^{\mathrm{a}, *}$, Yongsheng Chen ${ }^{\mathrm{a}}$, Guangquan Lu ${ }^{\mathrm{b}}$, Yunpeng Wang ${ }^{\mathrm{b}}$<br>${ }^{\mathrm{a}}$ Research Institute of Highway, Ministry of Transport, 8 Xitucheng Road, Haidian District, Beijing 100088, China<br>${ }^{\mathrm{b}}$ Beijing Key Laboratory for Cooperative Vehicle Infrastructure Systems and Safety Control, School of Transportation Science and Engineering, Beihang University, 37 Xueyuan Road, Haidian District, Beijing 100191, China

## ARTICLE INFO

Article history:
Received 30 March 2016
Received in revised form 23 August 2016
Accepted 28 November 2016

Keywords:
Unsignalized intersection
Traffic safety
Risk perception
Crossing behavior
Game theory


#### Abstract

Studying driver awareness of information, particularly risk perception, is vital to understanding driving behavior and improving traffic safety. In the dynamic interaction of a driver-vehicle-environment system, risk perception of drivers changes dynamically. In this study, we focused on drivers' risk perception at unsignalized intersections in China and analyzed their crossing behavior with consideration of risk perception. Based on cognitive psychology theory and an adaptive neuro-fuzzy inference system, quantitative models of drivers' risk perception were established for the crossing processes between two straight-moving vehicles from the orthogonal direction. Drivers' acceptable risk perception levels were identified using a self-developed data analysis method. On the basis of game theory, the relationship among the quantitative value of drivers' risk perception, acceptable risk perception level, and vehicle motion state was analyzed, then the crossing behavior models of drivers were established. Finally, the behavior models were validated using data collected from real-world vehicle movements and driver decisions. The results showed that the developed behavior models had both high accuracy and good applicability. This study would provide theoretical and algorithmic references for the microscopic simulation and active safety control system of vehicles.


© 2016 Elsevier Ltd. All rights reserved.

## 1. Introduction

Traffic safety in intersections has attracted increasing attention. According to the National Highway Traffic Safety Administration (National Highway Traffic Safety Administration, 2015), approximately $47 \%$ of the total $10,064,000$ crashes in the United States in 2013 occurred at intersections and nearby areas. The American Institute of Transportation Engineers have declared that road intersection safety was an important subject that required careful solutions (Elmitiny, Yan, Radwan, Russo, \& Nashar, 2010). Moreover, previous researches showed that drivers' behavior at intersections could significantly affect the capacity and safety of intersections (Sharma, Bullock, \& Peeta, 2011; Xiao, Ran, Yang, \& Wang, 2011). Thus, conducting research on drivers' behavior at intersections is necessary.

Unlike signalized intersections, unsignalized intersections have no positive indication to inform drivers when it is appropriate to enter the intersection. Drivers' behavior at unsignalized intersections is more complex than that at signalized intersections. Each driver makes decisions about when, where and how to complete a required maneuver based on the elements

[^0]of a decision context, including his/her perceptions of distance, velocity, and the performance of his/her vehicle (TRB., 1997). Accordingly, the number of vehicular conflicts and accidents at unsignalized intersections is higher than that at other intersections. According to National Highway Traffic Safety Administration (2015) statistical data, approximately 46\% of intersection crashes in the United States in 2013 occurred at unsignalized intersections. In China, crashes also occurred at unsignalized intersections in 2013, accounting for approximately 60\% of total intersection crashes (Statistical yearbook of China, 2014). Therefore, we mainly focused on drivers' behavior at unsignalized intersections and established drivers' behavior models in this study.

The information analysis of drivers, particularly risk perception, is notably a key problem in understanding driving behavior and improving traffic safety (McKenna, Horswill, \& Alexander, 2006). The level of drivers' risk perception changes dynamically in the dynamic interaction of a driver-vehicle-environment system. Once a perceived risk is out of an accepted region (i.e., an acceptable risk perception level), a driver will accordingly speed up or slow down to adjust his/her perceived risk. That is, drivers' risk perception significantly influences driving behavior. Thus, establishing drivers' risk perception models and determining acceptable risk perception levels are important to analyze drivers' behavior at unsignalized intersections.

In addition, the lack of stop signs and roundabouts at unsignalized intersections in China causes difficulty in controlling or guiding traffic. In most cases, when one vehicle encounters another vehicle at an unsignalized intersection in China, neither of the drivers will completely stop their vehicle. Instead, one driver will gradually approach the intersection and adjust his/ her driving behavior by gaming with the other vehicle. That is, the encounter between the two vehicles is actually a game process between the two drivers, and thus, can be analyzed using game theory.

In this study, we selected typical crossing cases at unsignalized intersections in China (in each case, one straight-moving vehicle encountered another straight-moving vehicle from the orthogonal direction) and developed drivers' behavior models based on risk perception and game theory. The models were expected to possibly reflect drivers' psychological characteristics and describe drivers' behavior at unsignalized intersections with improved accuracy.

## 2. Literature review

### 2.1. Drivers' risk perception

Drivers' risk perception has been defined as the ability to anticipate dangerous situations on the road ahead (Wilde, 1982; McKenna et al., 2006). It is one skill which has been found to be associated with crash risk (Darby, Murray, \& Raeside, 2009). In recent years, many researchers have focused on drivers' risk perception and conducted numerous studies, which included analyzing the differences of risk perception in various situations and counties, identifying the risk perception ability of drivers, and finding the relationship between drivers' risk perception and road traffic safety, etc. For example, Whelan, Groeger, Senserrick, and Triggs (2002) recorded the response times of drivers to hazards or potential hazards appearing in photographed traffic scenes by using a laptop-based mouse-driven computer program; then, they analyzed the risk perception abilities of novice and experienced drivers. Pradhan et al. (2005) collected drivers' eye movement characteristics in an advanced driving simulator, and then analyzed drivers' scanning behavior and their deficits to perceive potential risks. In addition, many studies have highlighted the importance of risk perception in safe driving, as well as the feasibility of using hazard perception tests to evaluate the risk perception of drivers (Darby et al., 2009; McKenna et al., 2006; Pollatsek, Fisher, \& Pradhan, 2006; Queensland Department of Transport, 2010).

Although previous studies have comprehensively analyzed drivers' perception characteristics and risk perception ability, and have made considerable achievements, research on quantifying drivers' risk perception and identifying the relationship between risk perception and drivers' decision behavior remains lacking. Drivers' risk perception exhibits nonlinear characteristics because of the effects of various factors. Thus, describing the risk perception of drivers using one particular formula is difficult. Previous studies have demonstrated the general use of neural networks in nonlinear mapping, reasoning, and prediction (Pao, 1989). However, a neural network has one disadvantage, that is, we cannot effectively obtain the implicit rules in a network structure. For a fuzzy logic system, it can be used to model human perception in an uncertain and imprecise environment. However, the fuzzy logic system is more complex; thus, it is difficult for the human brain to understand the causality existing in such system (Xiao, Sun, \& Ran, 2004). According to recent literature (Sangole \& Patil, 2014), an adaptive neuro-fuzzy inference system (ANFIS) is a combination of neural network and fuzzy logic approaches; hence, it inherently has the advantages of both, such as having a good learning mechanism and reasoning capability. Accordingly, we adopted ANFIS to model drivers' risk perception at unsignalized intersections in China in this study.

### 2.2. Drivers' behavior models at unsignalized intersections

Many researchers have conducted studies on divers' behavior at unsignalized intersections; most of these studies have focused on drivers' gap acceptance. For example, Madanat, Cassidy, and Wang (1994) developed gap acceptance functions at a stop-controlled intersection and evaluated the capacity of this intersection on the basis of logit-modeling techniques and stochastic queuing theory. Considering the risk evaluation results associated with accepting or denying small gaps, Pollatschek, Polus, and Livneh (2002) presented a model of driver gap-acceptance behavior when waiting at an unsignalized intersection. In addition, traffic conflict analyses and cellular automaton models have been applied to model driver behavior
at unsignalized intersections (Brilon \& Wu, 2002; Freund \& Pöschel, 1995). However, the lack of control measures for rightof-way at unsignalized intersections in China makes gap-forcing behavior common. The aforementioned studies and models may not be applicable in China. Moreover, they cannot explicitly consider the dynamic interactions among drivers and cognitive decision features. To address such shortcomings, an approach based on game theory inspired by the early works of Kita (1999) was adopted to model drivers' behavior in the present study.

### 2.3. Game theory in modeling drivers' behavior

Game theory can accurately provide the foundation to capture the dynamic interactions among drivers and describe the spatiotemporal characteristics of driving behavior. According to previous studies, game theory has mainly been used to model driver give-way behavior and route choice behavior. For example, Kita (1999) modeled merging and give-way behavior in a merging section under a new framework that explicitly considered two-directional game and interaction. Li (2003) investigated the route choice behavior of drivers under guide information based on an evolutionary game model. Wu and Li (2006) analyzed drivers' behavior under the traffic congestion phenomenon using another evolutionary game approach. However, only a few studies have been conducted to model drivers' crossing behavior at unsignalized intersections in China using game theory. Therefore, in this study, we aimed to establish drivers' dynamic behavior models based on game theory and describe the interaction process between two straight-moving vehicles under crossing condition at unsignalized intersections.

## 3. Quantifying risk perception of drivers

### 3.1. Data collection and processing

A typical unsignalized intersection, shown in Fig. 1(a) and (b), where pedestrians as well as non-motor and motor vehicles traveled together, was selected for this study.

![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-03.jpg?height=1195&width=1346&top_left_y=1148&top_left_x=270)
Fig. 1. The observation site.

We chose a tall building on the southwest corner of the intersection and used a video-based system to record traffic conditions. Then, we selected 150 typical crossing cases, including two straight-moving vehicles from the orthogonal direction, as shown in Fig. 1(c). To avoid interference from other vehicles to drivers' crossing behavior, we selected only the simplest crossing cases. In each case, one straight-moving vehicle encountered another straight-moving vehicle and no other object. Furthermore, the vehicle from the right side was labeled as "right vehicle," that is, $C_{R}$ in Fig. 1(c) in this study, whereas the vehicle from the left side was labeled as "left vehicle," that is, $C_{L}$ in Fig. 1(c). Point $C$ in Fig. 1(c) indicates the crossing point of the trajectories of the two vehicles.

Using OpenCV and its built-in algorithms, we developed a program to detect and track moving vehicles, as described in our previous papers (Liu, Lu, Wang, \& Zhang, 2014a; Liu, Lu, Wang, \& Zhang, 2014b; Liu, Wang, Lu, \& Zhang, 2014c). This program can extract and save the reliable motion parameters of vehicles, such as position, velocity, and acceleration (Lu, Liu, Xia, \& Deng, 2010).

### 3.2. Risk perception parameters

In our previous study (Liu et al., 2014b), we identified the main factors influencing the decision of straight-moving drivers when they encountered another vehicle moving at unsignalized intersections in China. For right vehicle drivers, SPEED_DIF-FERENCE (i.e., the relative speed between the right vehicle and the left vehicle), DISTANCE_DIFFERENCE (i.e., the relative distance between the right vehicle to the crossing point and the left vehicle to the crossing point), and SPEED_L (i.e., the speed of the left vehicle) were main factors affecting drivers' risk perception and their yielding/preemptive decisions. For left vehicle drivers, the main factors influencing their risk perception and decisions were SPEED_DIFFERENCE, CROSS_TIME_R (i.e., the travel time of the right vehicle to the crossing point), CROSS_DISTANCE_R (i.e., the distance between the right vehicle and the crossing point). In this study, we used these parameters to model drivers' risk perception in driving processes.

### 3.3. Quantitative method

As mentioned in Section 2.1, in this paper, we chose ANFIS to model drivers' risk perception at unsignalized intersections in China. In general, ANFIS has a six-layer feedforward neural network structure. Fig. 2 shows the ANFIS structure for a model with n inputs: $x_{1}, x_{2}, \ldots, x_{n}$ and one output: $P$. Explanation of each layer is as follows:

Layer 1 is the input layer. In this layer, neurons pass the input signals to next layer. Layer 2 is called the fuzzification layer. This layer can make the input variables to be divided into linguistic variables. Layer 3 is the rule layer. Each neuron corresponds to a Sugeno-type fuzzy rule in this layer. In layer 4, called the normalization layer, each neuron receives inputs from all neurons in the rule layer, and calculates the normalized firing strength- the ratio of the firing strength of a given rule to the sum of firing strengths of all rules- of a given rule. Layer 5 is the defuzzification layer. Defuzzification is the process in which the weighted consequent value is determined for a given rule. Layer 6 is the output layer having single neuron. In this layer, overall output P is determined by summing all the outputs from layer 5. For detailed structure of ANFIS, see Jang, Sun, and Mizutani (1997).

According to our previous study (Liu et al., 2014b), both right and left vehicle drivers completed their yielding/preemptive decisions at 0.9 s before reaching the crossing point. To understand and model drivers' risk perception conveniently, we used the values of the input and output variables at the drivers' decision moment to train ANFIS of drivers' risk perception in this study. All the input variables were fuzzy variables, which should be described and measured using linguistic rather than precise numerical values (Sangole \& Patil, 2014). In this study, each input variable was divided into the following linguistic variables: negative big (NB), negative small (NS), zero (ZO), positive small (PS), and positive big (PB). The membership functions

![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-04.jpg?height=558&width=1044&top_left_y=1779&top_left_x=415)
Fig. 2. Structure of ANFIS.

of all the input variables were initially supplied exogenously. The output variable was the quantitative value of drivers' risk perception. For two drivers in a crossing process, if one driver decelerates or stops the vehicle before reaching the crossing point and makes a yielding decision, then this condition generally represents a more serious perceived risk of this driver than the other driver. Under this condition, we considered the risk perception value of this driver as "1." By contrast, if one driver makes a preemptive decision, then the risk perception value of this driver is smaller than that of the other driver. We considered the risk perception value of this driver as "0."

The fuzzy logic toolbox in MATLAB was used to develop and test the drivers' risk perception models. The specific steps were described as follows:

Step 1: Generating and inputting training and testing data. We chose 100 crossing cases as training samples and extracted the training data for this study. The parameter data obtained from the other 50 cases were used as testing data.
Step 2: Identifying the type of membership functions. In this study, a Gaussian membership function was selected to fuzzify all the input variables.
Step 3: Using the "genfis1" function to generate the original fuzzy inference structure (FIS).
Step 4: Setting the training parameters of ANFIS.
Step 5: Using the "anfis" function to train ANFIS.
Step 6: Using the "evalfis" function to test the obtained performance of FIS.

### 3.4. Model results

Drivers' risk perception models can be obtained using the quantitative method described earlier. Fig. 3 shows the inputoutput risk perception values of drivers.

From Fig. 3, it was known that the model result could possibly reflect the changes in drivers' risk perception within a small model error, which indicated that the model could satisfy practical requirements.

### 3.5. Model test

Table 1 shows the comparison between parts of the observed and predicted values for drivers' risk perception.
As seen in Table 1, the mean absolute error of the predicted risk perception for right and left vehicle drivers is small, 0.09 and 0.13 , respectively. It also could be known from Table 1 that, through the training of lots of samples, the predicted risk perception value of the right vehicle drivers decreased with the increase of SPEED_DIFFERENCE (i.e., the relative speed between the right vehicle and the left vehicle). However, the predicted risk perception value of the left vehicle drivers

![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-05.jpg?height=905&width=1408&top_left_y=1439&top_left_x=252)
Fig. 3. Input-output risk perception values of drivers.

increased with the increase in SPEED_DIFFERENCE. That is, the higher the right vehicle speed, the smaller the predicted risk perception value of the right vehicle driver and the greater the predicted risk perception value of the left vehicle driver. By contrast, the higher the left vehicle speed, the greater the predicted risk perception value of the right vehicle driver and the smaller the predicted risk perception value of the left vehicle driver. These results agreed well with the reality and the observed values, which indicated that the structure and algorithm of both models were reasonable.

## 4. Indentifying acceptable risk perception level

### 4.1. Defining the acceptable level of drivers' risk perception

Previous studies have indicated that the risk perception abilities of drivers varied under different characteristics of drivers during the actual driving process (Siren \& Kjær, 2011). However, each driver has a fixed level of acceptable risk perception that can guide his/her behavior. According to risk compensation theory (RCT), individuals tend to adjust their behavior in response to perceived changes in risk. After training, drivers should have a similar acceptable risk level in similar driving situations (Lu, Cheng, Lin, \& Wang, 2012). In this study, we considered this level as a "range," which was assumed as $[\alpha$, $\beta$ ]. According to risk homeostasis theory (RHT), drivers would adjust their driving procedures based on this range to maintain a stable and constant condition. When the perceived risk level of drivers was less than $\alpha$, they would speed up to achieve their driving purpose. During this time, these drivers generally made preemptive decisions in the crossing process at unsignalized intersections. If the risk perception value was larger than $\beta$, then drivers would slow down and make yielding decisions to ensure safety. If the risk perception value of drivers was within the range of $[\alpha, \beta]$, then they would make either yielding or preemptive decisions when encountering another vehicle.

### 4.2 Determination method

The acceptable risk perception level is related to the risk perception abilities of drivers and their driving operation. Thus, identifying the acceptable risk perception level is critical in this study. According to the established quantitative method, we can obtain the ranges of drivers' risk perception under preemptive and yielding conditions. Then, the acceptable risk level can be determined according to these two ranges. As shown in Fig. 4, assuming the overlapping region of both ranges is [A, B]. When the perceived risk value is within [A, B], drivers may make either yielding or preemptive decisions. Thus, [A, B] can be considered as the acceptable risk level $[\alpha, \beta]$ in this study.

### 4.3. Result of the acceptable level

### 4.3.1. For right vehicle drivers

By using the quantitative method, we determined that the range of risk perception of right vehicle drivers under preemptive conditions was [-0.31, 0.64] (as shown in Fig. 5(a)). However, the range of risk perception under yielding conditions was [0.59, 1.18] (as shown in Fig. 5(b)). Thus, the overlapping range was [0.59, 0.64]. That is, the acceptable risk perception level of right vehicle drivers was [0.59, 0.64].

### 4.3.2. For left vehicle drivers

Similarly, for left vehicle drivers, the ranges of risk perception under preemptive and yielding conditions were [-0.26, 0.61 ] and [0.44,1.17], respectively (as shown in Fig. 6). Thus, the overlapping range [0.44, 0.61] was the acceptable risk perception level of left vehicle drivers.

Table 1
The comparison between parts of the observed and predicted values for drivers' risk perception.
|  | Parameters | Denote | Data |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| For right vehicle drivers | SPEED_DIFFERENCE (m/s) | $x_{1 R}$ | -7.22 | -4.98 | -0.14 | 0.69 | 1.96 |
|  | DISTANCE_DIFFERENCE (m) | $x_{2 R}$ | 6.42 | -2.90 | 2.41 | 3.26 | 4.69 |
|  | SPEED_L (m/s) | $x_{3 R}$ | 8.93 | 5.21 | 4.03 | 2.09 | 2.73 |
|  | The observed risk perception value | $Y_{R}$ | 1 | 1 | 1 | 0 | 0 |
|  | The predicted risk perception value | $P_{R}$ | 1.14 | 1.09 | 1.01 | 0.16 | 0.05 |
|  | Mean absolute error of risk perception | $E_{R}$ | 0.09 |  |  |  |  |
| For left vehicle drivers | SPEED_DIFFERENCE (m/s) | $x_{1 L}$ | -7.22 | -4.98 | -0.14 | 0.69 | 1.96 |
|  | CROSS_TIME_R (s) | $x_{2 L}$ | 6.60 | 5.33 | 1.54 | 1.91 | 1.30 |
|  | CROSS_DISTANCE _R (m) | $x_{3 L}$ | 11.26 | 2.65 | 5.98 | 5.31 | 6.11 |
|  | The observed risk perception value | $Y_{L}$ | 0 | 0 | 0 | 1 | 1 |
|  | The predicted risk perception value | $P_{L}$ | 0.02 | 0.10 | 0.28 | 0.89 | 1.16 |
|  | Mean absolute error of risk perception | $E_{L}$ | 0.13 |  |  |  |  |


![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-07.jpg?height=260&width=723&top_left_y=185&top_left_x=588)
Fig. 4. The sketch of drivers' acceptable risk perception level.

## 5. Modeling drivers' crossing behavior

### 5.1. Modeling method

In general, various factors have influence on drivers' crossing behavior. Among them, the velocity change of vehicles can effectively reflect the change in drivers' risk perception and their decision behavior. To simplify the model, in this study, we analyzed the game process of drivers and established game behavior models based on the following factors: vehicle speed and drivers' risk perception. According to Kita (1999), the interaction process between right and left drivers could be considered a zero-sum non-cooperative game under complete information. This type of game indicated that crossing decisions were made when drivers were certain about the decisions of other drivers. Moreover, the payoffs of the drivers were obtained by choosing different strategies and depended on the preferences and characteristics of other drivers.

According to game theory, the player set for the crossing process in this study was $C=\left\{C_{R}, C_{L}\right\}$, as shown in Fig. 1(c). $C_{R}$ and $C_{L}$ might take different measures, such as acceleration, deceleration, or uniform motion, according to perceived risk. Thus, the strategy set for drivers could be considered $S=\left\{S_{1}, S_{2}, S_{3}\right\}$, where $S_{1}, S_{2}$, and $S_{3}$ denoted acceleration, uniform motion, and deceleration, respectively.

To study the game process between $C_{R}$ and $C_{L}$, we assumed that the payoffs of $C_{R}$ and $C_{L}$ were $B_{R}\left(S_{1}, S_{2}, S_{3}\right)$ and $B_{L}\left(S_{1}, S_{2}, S_{3}\right)$, respectively. Assuming that $C_{R}$ and $C_{L}$ drivers began their game decision at moment $T_{A}$ and completed it at moment $T_{E}$; then, we divided period $\left[T_{A}, T_{E}\right]$ into $N$ time steps.

Assuming that the velocity of $C_{R}$ and $C_{L}$ at the beginning of time step i were $V_{R}^{i}$ and $V_{L}^{i}$, their acceleration (or deceleration) were $a_{R}^{i}$ and $a_{L}^{i}$, and the distance from both vehicles to the crossing point were $L_{R}^{i}$ and $L_{L}^{i}$, respectively. Assuming that the risk perception values of $C_{R}$ and $C_{L}$ drivers at time step $i$ were $P_{R}^{i}$ and $P_{L}^{i}$, respectively. As mentioned earlier, SPEED_DIFFERENCE (i.e., $V_{R}^{i}-V_{L}^{i}$ ), DISTANCE_DIFFERENCE (i.e., $L_{R}^{i}-L_{L}^{i}$ ), and SPEED_L (i.e., $V_{L}^{i}$ ) were the main factors that affected the risk perception of right vehicle drivers. Meanwhile, the main factors that affected the risk perception of left vehicle drivers were SPEED_DIFFERENCE, CROSS_TIME_R (i.e., $T_{R}^{i}$ ), and CROSS_DISTANCE_R (i.e., $L_{R}^{i}$ ). We assumed that all drivers would continue driving with the same acceleration at time step $i$ to reach the crossing point. Thus, $T_{R}^{i}$ can be calculated using Eq. (1):

![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-07.jpg?height=731&width=1427&top_left_y=1618&top_left_x=238)
Fig. 5. The distribution of risk perception value for right vehicle drivers.

![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-08.jpg?height=737&width=1431&top_left_y=179&top_left_x=222)
Fig. 6. The distribution of risk perception value for left vehicle drivers.

$$
T_{R}^{i}=\sqrt{\left(V_{R}^{i} / a_{R}^{i}\right)^{2}+2 L_{R}^{i} / a_{R}^{i}}-\left(V_{R}^{i} / a_{R}^{i}\right)
$$

Then, $P_{R}^{i}$ and $P_{L}^{i}$ could be obtained according to the established risk perception models.
For time step $i+1$, the velocity of $C_{R}$ and $C_{L}$ at the beginning $\left(V_{R}^{i+1}\right.$ and $\left.V_{L}^{i+1}\right)$, the distance from both vehicles to the crossing point ( $L_{R}^{i+1}$ and $L_{L}^{i+1}$ ), and the velocity change of both vehicles ( $\Delta V_{R}^{i+1}$ and $\Delta V_{L}^{i+1}$ ) could be estimated as follows:

$$
\left\{\begin{array}{l}
V_{j}^{i+1}=V_{j}^{i}+a_{j}^{i} \Delta t^{i} \\
\mathrm{~L}_{j}^{i+1}=L_{j}^{i}-V_{j}^{i} \Delta t^{i}-a_{j}^{i}\left(\Delta t^{i}\right)^{2} / 2 \\
\Delta V_{j}^{i+1}=V_{j}^{i+1}-V_{j}^{i}=a_{j}^{i} \Delta t^{i}
\end{array}\right.
$$

where $j=R, L ; \mathrm{i}=1,2, \ldots, N-1 . \Delta t^{i}$ was the time length at time step $i$.
The risk perception value of $C_{R}$ driver at time step $i+1\left(P_{R}^{i+1}\right)$ could be analyzed by considering the parameters $\left(V_{R}^{i+1}-V_{L}^{i+1}, L_{R}^{i+1}-L_{L}^{i+1}\right.$, and $\left.V_{L}^{i+1}\right)$ in the established risk perception model of right vehicle drivers. Where,

$$
\left\{\begin{array}{l}
V_{R}^{i+1}-V_{L}^{i+1}=V_{R}^{i}+a_{R}^{i} \Delta t^{i}-V_{L}^{i}-a_{L}^{i} \Delta t^{i} \\
L_{R}^{i+1}-L_{L}^{i+1}=L_{R}^{i}-V_{R}^{i} \Delta t^{i}-a_{R}^{i}\left(\Delta t^{i}\right)^{2} / 2-L_{L}^{i+1}+V_{L}^{i} \Delta t^{i}+a_{L}^{i}\left(\Delta t^{i}\right)^{2} / 2 \\
V_{L}^{i+1}=V_{L}^{i}+a_{L}^{i} \Delta t^{i}
\end{array}\right.
$$

At time step $i+1$, the risk perception value of $C_{L}$ driver $\left(P_{L}^{i+1}\right)$ could be determined by considering parameters $\left(V_{R}^{i+1}-V_{L}^{i+1}, T_{R}^{i+1}\right.$, and $\left.L_{R}^{i+1}\right)$ in the risk perception model of left vehicle drivers. Where,

$$
\left\{\begin{array}{l}
V_{R}^{i+1}-V_{L}^{i+1}=V_{R}^{i}+a_{R}^{i} \Delta t^{i}-V_{L}^{i}-a_{L}^{i} \Delta t^{i} \\
T_{R}^{i+1}=T_{R}^{i}-\Delta t^{i} \\
L_{R}^{i+1}=L_{R}^{i}-V_{R}^{i} \Delta t^{i}-a_{R}^{i}\left(\Delta t^{i}\right)^{2} / 2
\end{array}\right.
$$

Similarly, the risk perception values of both drivers at time steps $i+2, i+3$ to $N$ could be calculated.
For both drivers, when the increase in velocity change was high and the risk perception value was low, the payoff of the drivers was high. Thus, we defined the payoff function of the drivers as follows:

$$
F_{j}^{i}=m_{j}^{i} F\left(\Delta V_{j}^{i}\right)+n_{j}^{i} G\left(1-P_{j}^{i}\right)
$$

where $j=R, L ; i=1,2, \ldots, N . F\left(\Delta V_{j}^{i}\right)$ and $G\left(1-P_{j}^{i}\right)$ denoted the normalization for $\Delta V_{j}^{i}$ and $\left(1-P_{j}^{i}\right)$, respectively. $m_{j}^{i}$ and $n_{j}^{i}$ represented the expectation coefficients of the drivers to vehicle speed and risk perception, and $m_{j}^{i} \geqslant 0, n_{j}^{i} \geqslant 0, m_{j}^{i}+n_{j}^{i}=1$.

In actual driving processes, the speed and risk perception factors had different influences on drivers' payoff. If the risk perception value of a driver was lower than his/her acceptable risk perception level, then he/she would focus on improving
vehicle speed. If the perceived risk value of a driver was higher than his/her acceptable risk perception level, then he/she would focus on changing risk perception. However, if the risk perception value of a driver was within the range of the acceptable risk level, then we could conclude that the speed and risk perception factors were equally important to the driver's payoff. Therefore, based on the acceptable risk perception level of drivers $\left[\alpha_{j}, \beta_{j}\right]$, the speed coefficient $m_{j}^{i}$ can be defined as follows:

$$
m_{j}^{i}= \begin{cases}1-0.5 P_{j}^{i} / \alpha_{j}, & P_{j}^{i}<\alpha_{j} \\ 0.5, & \alpha_{j} \leqslant P_{j}^{i} \leqslant \beta_{j} \\ 0.5\left(1-P_{j}^{i}\right) /\left(1-\beta_{j}\right), & P_{j}^{i}>\beta_{j}\end{cases}
$$

The sketch map of $m_{j}^{i}$ is shown in Fig. 7:
To analyze the game behavior between $C_{R}$ and $C_{L}$ drivers, solving the game model at each time step was necessary. The method for this process was as follows:

Step 1: According to the established motion state and risk perception model, the velocity changes of the two drivers and their risk perception values at the first time step (i.e., $\Delta V_{R}^{1}, \Delta V_{L}^{1}, P_{R}^{1}$, and $P_{L}^{1}$ ) under different strategy combinations, such as $\left\{S_{1}, S_{1}\right\},\left\{S_{1}, S_{2}\right\},\left\{S_{1}, S_{3}\right\},\left\{S_{2}, S_{1}\right\},\left\{S_{2}, S_{2}\right\},\left\{S_{2}, S_{3}\right\},\left\{S_{3}, S_{1}\right\},\left\{S_{3}, S_{2}\right\}$, and $\left\{S_{3}, S_{3}\right\}$, were calculated.
Step 2: The payoff values of the two drivers under different strategy combinations were evaluated based on Eq. (5).
Step 3: The Nash equilibrium strategy (the Nash equilibrium is a game solution in which no player can gain anything by unilaterally changing his/her own strategy) at the first time step was obtained according to the payoff value, and consequently, the behavior strategies of the two drivers were determined. Then, the motion information of the two vehicles at the beginning of the second time step was calculated based on the determined behavior strategies.
Step 4: According to the motion state and the established risk perception models, the velocity changes of the two drivers and their risk perception values at the second time step under different strategy combinations were calculated. By repeating steps 2 and 3, the behavior strategies of the two drivers at the second time step and the motion state of the two vehicles at the beginning of the third time step were obtained.
Step 5: Similarly, the behavior strategies of the two drivers at time steps 3 to $N$ were calculated.

### 5.2. Model results

To facilitate understanding, we analyzed the game behavior of the drivers within a certain period $\left[T_{A}, T_{E}\right]$ (as mentioned in Section 5.1). $\left[T_{A}, T_{E}\right]$ represented 2 s before the preemptive driver reached the crossing point. Then, we divided this period into 10 time steps and each time step was 0.2 s. According to related literature, we assumed that if $C_{\mathrm{R}}$ and $C_{\mathrm{L}}$ drivers chose acceleration strategy $\left(\mathrm{S}_{1}\right)$, then acceleration was considered $1.0 \mathrm{~m} / \mathrm{s}^{2}$ (i.e., $a_{R}=1.0 \mathrm{~m} / \mathrm{s}^{2}, a_{L}=1.0 \mathrm{~m} / \mathrm{s}^{2}$ ). If the two drivers adopted deceleration strategy $\left(S_{3}\right)$, then deceleration was determined as $1.5 \mathrm{~m} / \mathrm{s}^{2}$ (i.e., $a_{R}=-1.5 \mathrm{~m} / \mathrm{s}^{2}, a_{L}=-1.5 \mathrm{~m} / \mathrm{s}^{2}$ ). If the drivers chose uniform motion $\left(S_{2}\right)$, then $a_{R}=a_{L}=0$.

For a crossing case shown in Fig. 8 ( $C_{R}$ passed the crossing point first), the motion state at the beginning of the first time step was $L_{R}^{1}=9.0 \mathrm{~m}, L_{L}^{1}=12.3 \mathrm{~m}, V_{R}^{1}=4.8 \mathrm{~m} / \mathrm{s}, V_{L}^{1}=5.0 \mathrm{~m} / \mathrm{s}, a_{R}^{1}=0, a_{L}^{1}=0$.

As described earlier, the acceptable risk perception level of the right vehicle driver was [ $0.59,0.64$ ]; thus, $\alpha_{R}=0.59$, $\beta_{R}=0.64$. The acceptable risk perception level of the left vehicle driver was [0.44, 0.61]; that is, $\alpha_{L}=0.44, \beta_{L}=0.61$.

![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-09.jpg?height=528&width=737&top_left_y=1811&top_left_x=584)
Fig. 7. The sketch map of $m_{j}^{i}$.

![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-10.jpg?height=365&width=1461&top_left_y=183&top_left_x=199)
Fig. 8. A crossing case of the two straight-moving drivers.

Based on Eq. (5), the payoff values of the two drivers under different strategy combinations at the first time step was shown in Table 2.

The result showed that at the first time step, the Nash equilibrium strategy was: both $C_{R}$ and $C_{L}$ chose $\mathrm{S}_{3}$ (deceleration strategy) when the payoffs of $C_{R}$ and $C_{L}$ drivers were the largest, 0.47 and 0.54, respectively. Then, we could determine the motion information of the two vehicles at the beginning of the second time step according to the estimated strategies: $L_{R}^{2}=11.27 \mathrm{~m}, L_{L}^{2}=7.97 \mathrm{~m}, V_{R}^{2}=4.5 \mathrm{~m} / \mathrm{s}$, and $V_{L}^{2}=4.7 \mathrm{~m} / \mathrm{s}$. Similarly, the Nash equilibrium at the second time step could be inferred, when both $C_{R}$ and $C_{L}$ also decelerated. Based on this analogy, the Nash equilibrium strategy at each time step could be determined. Table 3 shows the estimated drivers' strategies when reach each Nash equilibrium.

### 5.3. Model test

As shown in Table 3, both $C_{R}$ and $C_{L}$ drivers decelerated at the beginning of the crossing game, and then $C_{L}$ continued to decelerate; however, $C_{R}$ chose to accelerate. According to the estimated strategies, vehicle speed and distance to the crossing point at the beginning of each time step could be calculated. Fig. 9 shows the comparison between the estimated and the actual results.

Fig. 9(a) showed the constant deceleration of $\mathrm{C}_{\mathrm{L}}$ driver in actual driving. Meanwhile, $\mathrm{C}_{\mathrm{R}}$ driver first decelerated and then accelerated. Also, the result in Fig. 9(a) indicated that the estimated speed of the two vehicles was almost consistent with the actual speed. Based on the estimated strategies in Table 3 and Eq. (2), the distance from both vehicles to the crossing point at the beginning of each time step could be estimated. It could be known from Fig. 9(b), the estimated distance from the two vehicles to the crossing point could accurately reflect the actual distance. In addition, which vehicle reached the crossing point first could be identified according to the distance from the vehicles to the crossing point at the last time step. The one who was closer to the crossing point at the last time step would reach the crossing point first. As seen in Fig. 9(b), $\mathrm{C}_{\mathrm{R}}$ was estimated to be closer to the crossing point than $\mathrm{C}_{\mathrm{L}}$ at the last time step. That was, $\mathrm{C}_{\mathrm{R}}$ driver would make a preemptive decision and pass the crossing point first. This result was consistent with the observed data.

In this study, we also established the game models for another 50 crossing cases, and then calculated the game strategies of the drivers. As seen in Fig. 9, we also estimated vehicles' speed, distance from the vehicles to the crossing point, and final preemptive or yielding decisions of the drivers in each case. Table 4 shows the error of the estimated speed and distance for all the cases we chose.

As shown in Table 4, the error between the estimated and the actual results was minimal. It indicated the established models could efficiently describe drivers' behavior. By comparing the estimated and the actual preemptive/yielding decision in all 50 cases, 48 of them were estimated accurately. The accuracy reached to 96\%.

To verify the applicability of the established game models in this study, we chose another typical unsignalized intersection in Kunming City (i.e., the test intersection, shown in Fig. 10) to extract information on crossing cases.

We collected 10 crossing cases and analyzed drivers' game behavior. It was also showed that the estimated results were consistent with the actual results. The preemptive/yielding decisions of the drivers in all the 10 cases were inferred accurately. Table 5 shows the estimated error at test intersection.

Table 2
The payoff of the two drivers under different strategy combinations.
| Game strategy |  | $\boldsymbol{C}_{\boldsymbol{L}}$ |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  |  | $\mathrm{S}_{1}$ | $\mathrm{S}_{2}$ | $\mathrm{S}_{3}$ |
| $C_{R}$ | $\mathrm{S}_{1}$ | (0.32, 0.31) | (0.42, 0.35) | (0.45, 0.39) |
|  | $\mathrm{S}_{2}$ | (0.36, 0.49) | (0.40, 0.48) | (0.46, 0.40) |
|  | $\mathrm{S}_{3}$ | (0.39, 0.51) | (0.47, 0.53) | (0.47, 0.54) |


Table 3
The estimated strategies when reach each Nash equilibrium point.
| Parameters |  | Time step |  |  |  |  |  |  |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Game strategy | $C_{R}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{1}$ | $\mathrm{S}_{1}$ | $\mathrm{S}_{1}$ | $\mathrm{S}_{1}$ | $\mathrm{S}_{1}$ | $\mathrm{S}_{1}$ | $\mathrm{S}_{1}$ |
|  | $C_{L}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ | $\mathrm{S}_{3}$ |


![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-11.jpg?height=937&width=727&top_left_y=488&top_left_x=590)
Fig. 9. The comparison between the estimated and the actual results.

Table 5 indicated that the estimated error at the test intersection was minimal, and the established game models exhibited good applicability. In summary, we considered the practicality of studying driver crossing behavior based on game theory.

## 6. Discussion and conclusion

In this study, we focused on typical crossing cases at unsignalized intersections. In each case, one straight-moving vehicle encountered another straight-moving vehicle. Based on one of our previous studies on typical crossing cases, the main parameters that affected the risk perception of right and left vehicle drivers were determined. Then, we used these parameters to establish the quantitative models of drivers' risk perception based on ANFIS. By comparing the actual data and the model prediction results, we verified the practicality of the proposed quantitative risk perception models.

Based on stimulus response, traffic psychology, and risk analysis theories, we defined the acceptable risk perception level. Moreover, the relationship among the quantitative value of risk perception, the acceptable risk perception level, and the

Table 4
The error of the estimated speed and distance.
| Parameters | Error |  |
| :--- | :--- | :--- |
|  | Mean error | Standard error |
| Right vehicle speed (m/s) | 0.164 | 0.236 |
| Left vehicle speed (m/s) | 0.165 | 0.254 |
| Distance from the right vehicle to the crossing point (m) | 0.450 | 0.674 |
| Distance from the left vehicle to the crossing point (m) | 0.420 | 0.573 |


![](https://cdn.mathpix.com/cropped/8327701e-bcbe-4b9e-867b-aa04dc804b64-12.jpg?height=486&width=1257&top_left_y=179&top_left_x=304)
Fig. 10. Another typical unsignalized intersection.

Table 5
The estimated error at test intersection.
| Parameters | Error |  |
| :--- | :--- | :--- |
|  | Mean error | Standard error |
| Speed (m/s) | 0.193 | 0.267 |
| Distance from the vehicles to the crossing point (m) | 0.516 | 0.806 |


decision-making ability of drivers was analyzed. Then, according to a data analysis method that we developed, the acceptable risk perception levels for right and left vehicle drivers were identified.

In the light of game theory, the relationship among the quantitative value of risk perception, the acceptable risk perception level, and vehicle motion state was analyzed. Moreover, the payoff function of drivers was determined. Then, we provided the method that could be used to estimate drivers' game behavior under crossing conditions. By analyzing the Nash equilibrium strategy, the acceleration/deceleration strategies of the drivers at each time step could be identified. Then, we could calculate vehicle speed and the distance from a vehicle to the crossing point at the beginning of each time step. It was shown that the estimated results were consistent with the fact. By analyzing a test intersection, the established game models were proven to have good applicability.

In summary, this study could promote the development of risk analysis theory from qualitative analysis to quantitative calculation, as well as expand the application of this theory to traffic safety. Moreover, we considered drivers' risk perception factor and used game theory to model their behavior. Such efforts made the model accurate and reasonable. Furthermore, the results of this study could provide a good theory and algorithm for the microscopic simulation and active safety control system of vehicles.

Nevertheless, this study exhibited several limitations. Only the simplest crossing cases, in which one straight-moving vehicle encountered another straight-moving vehicle, were selected for analysis. We did not study the crossing behavior when one straight-moving vehicle encountered two or more vehicles from different directions. Furthermore, the effects of geometric design, intersection capacity, and the personal characteristics of drivers were not considered in modeling crossing behavior. In our future research, we will examine more unsignalized intersections to analyze the effects of complex traffic situations and factors (e.g., geometric design, intersection capacity, etc.) on drivers' crossing behavior.

## Acknowledgements

This work was supported by the Opening Project of Key Laboratory of Road Safety Technologies, Ministry of Transport, China (2015) and the Fundamental Research Funds for the National-level Research Institutes (Z2060302150009038) and the National Natural Science Foundation of China (51308263).

## References

Brilon, W., \& Wu, N. (2002). Unsignalized intersections - a third method for analysis. In Proceedings of the 15th International Symposium on Transportation and Traffic Theory, Adelaide, pp. 1-19.
Darby, P., Murray, W., \& Raeside, R. (2009). Applying online fleet driver assessment to help identify, target and reduce occupational road safety risks. Safety Science, 47, 436-442.
Elmitiny, N., Yan, X., Radwan, E., Russo, C., \& Nashar, D. (2010). Classification analysis of driver's stop/go decision and red-light running violation. Accident Analysis and Prevention, 42, 101-111.
Freund, J., \& Pöschel, T. (1995). A statistical approach to vehicular traffic. Physical A: Statistical Mechanics and Its Application, 219(1), 95.
Jang, J. S. R., Sun, C. T., \& Mizutani, E. (1997). Neuro-fuzzy and soft computing-a computational approach to learning and machine intelligence. NJ: Prentice Hall. Kita, H. (1999). A merging-giveway interaction model of cars in a merging section: A game theoretic analysis. Transportation Research Part A, 33, 305-312.

Li, Z. (2003). A study of route choice behavior of drivers based on the evolutionary game under the condition of traffic flow guidance. Journal of Transportation System Engineering and Information Technology, 3(2), 23-27.
Liu, M., Lu, G., Wang, Y., \& Zhang, Z. (2014a). Preempt or yield? An analysis of driver's dynamic decision making at unsignalized intersections. Safety Science, 65(2014), 36-44.
Liu, M., Lu, G., Wang, Y., \& Zhang, Z. (2014b). Analyzing drivers' crossing decisions at unsignalized intersections in China. Transportation Research Part F, 24 (2014), 244-255.
Liu, M., Wang, Y., Lu, G., \& Zhang, Z. (2014c). Logit-based merging behavior model for uncontrolled intersections in China. Journal of Transportation Engineering, 140(12), 1-8.
Lu, G., Cheng, B., Lin, Q., \& Wang, Y. (2012). Quantitative indicator of homeostatic risk perception in car following. Safety Science, 50(9), 1898-1905.
Lu, G., Liu, M., Xia, S., Deng, C. (2010). Vehicles' motion parameters detection in intersection based on videos of low view angles. 2010 International Conference on Optoelectronics and Image Processing, Haiko, China, pp. 718-721.
Madanat, S., Cassidy, M., \& Wang, M. (1994). Probabilistic delay model at stop controlled intersection. Journal of Transportation Engineering, 120(1), 21-36.
McKenna, F. P., Horswill, M. S., \& Alexander, J. L. (2006). Does anticipation training affect drivers' risk taking? Journal of Experiment Psychological Application, 12, 1-10.
National Highway Traffic Safety Administration, NHTSA. (2015). Traffic safety facts 2013. Washington, DC.
Pao, Y. (1989). Adaptive pattern recognition and neural networks. New Jersey: Addison-Wesley Pub.
Pollatschek, M. A., Polus, A., \& Livneh, M. (2002). A decision model for gap acceptance and capacity at intersections. Transportation Research Part B, 36(7), 649-663.
Pollatsek, A., Fisher, D., \& Pradhan, A. (2006). Identifying and remedying failures of selective attention in younger drivers. Current Directions in Psychological Science, 15, 255-259.
Pradhan, A. K., Hammel, K. R., DeRamus, R., Pollatsek, A., Noyce, D. A., \& Fisher, D. L. (2005). Using eye movements to evaluate effects of driver age on risk perception in a driving simulator. Human Factors, 47(4), 840-852.
Queensland Department of Transport and Main Roads. (2010). Everything you needed to know about the Hazard Perception Test. Available at [http://www.transport.qld.gov.au/hpt](http://www.transport.qld.gov.au/hpt) on February 17, 2010.
Sangole, J. P., \& Patil, G. R. (2014). Adaptive neuro-fuzzy interface system for gap acceptance behavior of right-turning vehicles at partially controlled T-intersections. Journal of Modern Transportation, 22(4), 235-243.
Sharma, A., Bullock, D., \& Peeta, S. (2011). Estimating dilemma zone hazard function at high speed isolated intersection. Transportation Research Part C, 19(3), 400-412.
Siren, A., \& Kjær, M. R. (2011). How is the older road users' perception of risk constructed? Transportation Research Part F, 14, 222-228.
Statistical yearbook of China (2014). Beijing: National Bureau of Statistics of China Available at http://www.stats.gov.cn/.
TRB. (1997). Review of international practices used to evaluate unsignalized intersections. Transportation Research Circular 468.TRB, National Research Council, Washington, DC.
Whelan, M. I., Groeger, J. A., Senserrick, T. M., \& Triggs, T. J. (2002). Alternative methods of measuring hazard perception: Sensitivity to driving experience. UK: Guildford.
Wilde, G. J. S. (1982). The theory of risk homeostasis: Implications for safety and health. Risk Analysis, 2, 209-225.
Wu, B., \& Li, L. (2006). Evolutionary dynamic analysis of traffic congestion. China Journal of Highway and Transport, 19(3), 106-110.
Xiao, Y., Ran, Q., Yang, J., \& Wang, Z. (2011). Analysis and modeling of crossing behavior at urban intersections in China. Journal of Transportation Engineering, 137(2), 121-127.
Xiao, H., Sun, H., \& Ran, B. (2004). Special factor adjustment model using fuzzy-neural network in traffic prediction. Transportation Research Record, 1879(1), 17.


[^0]:    * Corresponding author.
    E-mail address: liumiao-0605@163.com (M. Liu).

