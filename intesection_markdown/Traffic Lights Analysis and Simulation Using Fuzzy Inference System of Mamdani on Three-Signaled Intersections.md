5th International Conference on Computer Science and Computational Intelligence 2020

# Traffic Lights Analysis and Simulation Using Fuzzy Inference System of Mamdani on Three-Signaled Intersections. 

Siti Komsiyah ${ }^{\mathrm{a}, *}$, Evelyn Desvania ${ }^{\mathrm{a}}$<br>${ }^{a}$ Mathematics Department, School of Computer Science, Bina Nusantara University, Jakarta, Indonesia 11480


#### Abstract

As one of the main characters at road intersections, traffic lights have lost its limelight and functions as of late. The unbalanced timing on its green light/green time duration settings with less to no regard to actual traffic in each lane becomes one of its main problems. Therefore in this paper, the author will formulate a more dynamic green time setting system by using Fuzzy Inference System type Mamdani. To help with the analyzing process, a desktop-based application is designed to simulate the green light duration setting for the traffic light based on the previously conducted analysis. The green light/green time output obtained during the implementation of this application will be further compared to the data obtained from transportation office of DKI Jakarta (Dinas Perhubungan Provinsi DKI Jakarta). From this comparison, it can be deduced that the output results from the implementation of this methods show a more dynamic value.


© 2021 The Authors. Published by Elsevier B.V.
This is an open access article under the CC BY-NC-ND license (https://creativecommons.org/licenses/by-nc-nd/4.0)
Peer-review under responsibility of the scientific committee of the 5th International Conference on Computer Science and Computational Intelligence 2020

Keywords: Fuzzy Inference System ; Mamdan ; traffic lights simulation; green time.

## 1. Introduction

A traffic setting done by using traffic lights, especially at an intersection is meant to control the vehicle movements from each direction in order to keep it in order and avoid potential traffic jams or even accidents. However, most traffic lights setting in Indonesia didn't work fluidly. The same duration settings of the green light for all intersection lane became one of the biggest reason traffic jam happens.

[^0]Based on the previously mentioned problem, this paper is conducted to analyze and plan a more dynamic traffic light system. In this paper, the author refers to several journal references. The journals relating to traffic light analysis are first the paper by Prasetiyo et al (2015) ${ }^{(1)}$, the concept of dynamic traffic lights control is explained by using fuzzy logic control type Sugeno. According to Zachariah et al (2017) ${ }^{(2)}$,the paper seeks to optimize the allocation of rightof way to road users (moving vehicles) using fuzzy logic tools interfaced with a DPSTLS system. The paper by Salehi et al (2014) ${ }^{(3)}$, this paper describes a fuzzy logic signal controller for a four-way intersection suitable for mixed traffic, including a high proportion of motorcycles. The paper by Mohit J and Shailia S $(2014)^{(4)}$, fuzzy logic traffic controller for isolated intersections with emergency vehicle priority system using matlab simulation. Then paper by Krzysztof M and Stanisław I (2019) ${ }^{(5)}$, present the analysis of the impact of various driver behaviours on the traffic flow in the city and the analysis of the countdown timers mounted at traffic lights and their positive influence on traffic light. Then the paper by Madalin D.P (2018), ${ }^{(6)}$ the purpose of this paper is to present an approach of optimization tool using in order to decrease the traffic congestion and the crossing time of a road network. And then by Thuniga, T (2019) ${ }^{(7)}$, the paper presents a comparison of optimized fixed-time signals and responsive signals in the application. The following journals related to the Fuzzy Inference System of Mamdani are first by Zulfikar W.B et al (2018) ${ }^{(8)}$, This paper reported a classification employee based on their eligibility for promotion where the degree of membership was decided using Mamdani Fuzzy based on determinant factors of the performance of employees. Then the paper by Segismundo, S I, and Luis R I (2018) ${ }^{(9)}$, this paper studies the potential use of Mamdani systems to explore the logical consequences of a model based on IF-THEN rules via simulation. And then the paper by Khan, M.A et all (2018) ${ }^{(10)}$ , the objective of this paper is to analysis key issues and the solutions about traffic congestion in a smart city in the light of critical inducing aspects.

In this paper, Fuzzy Inference System (FIS) type Mamdani is used because according to Kusumadewi.S and Purnomo.H (2004) ${ }^{(11)}$, FIS of Mamdani is a method easy to be implemented and has been widely used in various fields like decision support systems, artificial intelligence, and there are a lot of problems that, one of them is the traffic lights setting. The method based on this fuzzy logic is chosen because it is considered more practical to use because of its simplicity, easy to understand and flexible. In this paper, the sample used is Batu Sari intersection in Jakarta Barat. Furthermore, an application will be designed to simulate the result of the analysis that has been formulated by using the Java programming language. The solution achieved by this paper will be compared to the data obtained from Transportation Office of DKI Jakarta.

The limitation in this paper are the mathematical modeling used Fuzzy Inference System type of Mamdani, case studies are only conducted at the intersection of Jalan Batu Sari, West Jakarta, the characteristics of intersections are three-signaled intersections, and case studies only takes into account four-wheeled vehicles.

## 2. Literature Review and Methods

### 2.1. Traffic Lights

A traffic light is a controlling device using lamps/lights installed at the intersection as a means to control the traffic flows. Traffic flows setting at the intersection is basically used to regulate the vehicular movements for each flows so the vehicles can move orderly and without causing much disturbance by conflicting with the other traffic flows. There are various types of control devices available, however, the decision of choosing one over the other is strictly pure by the field conditions, such as volumes, intersection geometrics and others.

Geometrical conditions and traffics will affect the traffic capacity and performance of an intersection. Therefore, a planner needs to be able to specifically design the traffic in order to properly distribute the duration of the lights to each vehicular movement in order to achieve its optimal performance. Traffic lighting system that uses the lamp/lights movements are; Green Light, in which the vehicles affected by the light needs to move forward; Amber Light, in which the affected vehicles need to anticipate their next movement based on the order of following lights color, and; Red Light, in which the vehicles affected by this light has to stop moving forward before the stop line.

### 2.2. Signalized Intersection

Signalized Intersection is an intersection consisting of a number of arms and equipped with traffic lights signal settings. Based on Indonesian Road Manual Capacity (MKJI) of $1997{ }^{(12)}$, to count the time cycle (c) and green
duration $\left(\mathrm{g}_{\mathrm{i}}\right)$, following equations of (1) and (2) can be used :

$$
\begin{gathered}
c=\frac{(1,5 \times L T I+5)}{1-\Sigma I F R_{c r i t}} \\
g_{i}=\left(c_{u}-L T I\right) \times P R i
\end{gathered}
$$

In which (LTI) is the value of all periods between green in a cycle by using seconds. Intersection flow ratio (IFR) is the value of the highest critical flow for all signal phases in sequential order within a cycle. Phase ratio (PR) is a critical ratio divided by the intersection flows ratio.

### 2.3. Mamdani Methods

Mamdani method is often known as the Max-Min method, introduced by Embrahim Mamdani as found by Zadeh L.A (1965) ${ }^{(13)}$. This fuzzy inference system consists of 4 phases :
1). The formation of a Fuzzy set : The formation of a fuzzy set is a process to change the crisp format of an input variable into a fuzzy set of linguistic variables each with its own affiliated functions.
2). The application of implication function : In Mamdani method, the implication function used is min. The result of this fuzzy implication for each rule will then be combined to obtain the fuzzy inference output using (3).

$$
\mu_{(A \cap B)}(x)=\min \left[\mu_{A}(x), \mu_{B}(x)\right]
$$

3). Rules composition : If a system consists of a number of rules, the inference will then be obtained from the sets and correlation between rules. The method used during a fuzzy inference system is Max Method. Max (Maximum) Method takes the solution of fuzzy formation by taking the rule's maximum value, and then using it to modify the fuzzy area, and applying it to the output by using OR operator (union). If all propositions have been evaluated, the output will consist of a fuzzy formation that reflects the contribution of each proportion. In general, it can be written this way :

$$
\mu_{s f}\left[x_{i}\right]=\max \left(\mu_{s f}\left[x_{i}\right], \mu_{k f}\left[x_{i}\right]\right)
$$

with:
$\mu_{\mathrm{sf}}\left[\mathrm{x}_{\mathrm{i}}\right]=$ affiliation value of fuzzy solution up to the -i rules
$\mu_{\mathrm{kf}}\left[\mathrm{x}_{\mathrm{i}}\right]=$ affiliation value of fuzzy consequence up to the -i rules .
4). Confirmation (Defuzzification) : The input of the defuzzification process is a fuzzy formation obtained from various fuzzy rules composition, while the output obtained is a number in that specific fuzzy formation domain. The method used here is Centroid Method. In centroid method, the crisp solution is obtained by taking the center point of the fuzzy area. In general, the equation can be written as follows:

$$
Z^{*}=\frac{\int z \cdot \mu_{c}(z) d z}{\int \mu_{c}(z)}
$$

## 3. Simulation Result and Discussion

The author gathered the data used in this paper by using two procedures which are done by conducting a survey to Transportation Office of DKI Jakarta and by doing a direct paper to Batu Sari intersection at Jakarta Barat. Geometric illustration of the intersection of Batusari, West Jakarta can be seen in Fig 1 where each crossing arm is given a code of approach to the wind direction, namely South, West and North.

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-04.jpg?height=431&width=923&top_left_y=252&top_left_x=538)
Fig. 1. Geometric illustration of the intersection of Batu Sari, West Jakarta

The data gathered consists of intersection geometric, the traffic light duration data and the traffic duration data. The data in table 1. contains data for input simulation example, the authors take one sample group of data, that is vehicle queue (passenger car unit), vehicle flows (passenger car unit/hour), gross flow (passenger car unit/green hour), and total time loss (seconds), it's taken during the 6 p.m.-7 p.m. observation of the $9^{\text {th }}$ cycle because that time is peak time where the most dense vehicle flow and vehicle queue also the most.

Table 1. Input Data Calculated Using FIS Type Mamdani Method
| Input Variables | Units | Approacher |  |  |
| :--- | :--- | :--- | :--- | :--- |
|  |  | South | West | North |
| Queue | Smp (passenger car unit) | 49 | 23 | 43 |
| Vehicle Flows | Smp (passenger car unit)/hour | 1444 | 1291 | 1465 |
| Gross Flows | Smp (passenger car unit)/green hour | 1500 | 1200 | 1500 |
| Total Time Loss | seconds | 12 |  |  |


### 3.1. Application of Fuzzy Inference System type Mamdani

Fuzzy Inference System type Mamdani application steps in the dynamic traffic lights expansion as follows :
1). The formation of fuzzy set

Table 2. Fuzzy Set Formation
| Function | Variable | Fuzzy Set | Domain |
| :--- | :--- | :--- | :--- |
| Input | South lane vehicle queue (NQ) | Short | [0,25] |
|  |  | Medium | [10,40] |
|  |  | Long | [25,50] |
|  | West lane vehicle queue (NQ) | Short | [0,25] |
|  |  | Medium | [10,40] |
|  |  | Long | [25,50] |
|  | North lane vehicle queue (NQ) | Short | [0,25] |
|  |  | Medium | [10,40] |
|  |  | long | [25,50] |
|  | Time cycle | Quick | [50,75] |
|  |  | Normal | [60,90] |
|  |  | Slow | [75,100] |


Table 2 contains the first step in applying the Fuzzy Inference System (FIS) of Mamdani method, which is to create a fuzzy set of each variable. In this paper, the input system consists of three variables, namely the queue of the southern lane vehicle, the queue of the west lane vehicle and the queue of the lane north lane, with each have Fuzzy set are a short, medium and long. While the output is cycle time duration with Fuzzy set are fast, medium, and long.
2). The declaration of affiliation function

The following is the affiliation function for the south lane, west lane and north lane queue:

$$
\begin{aligned}
& \mu_{\text {short }}(x)=\left\{\begin{array}{c}
0, \quad x \geq 25 \\
\frac{25-x}{25}, \quad 0 \leq x \leq 25
\end{array}\right. \\
& \mu_{\text {medium }}(x)=\left\{\begin{array}{cc}
0, & x<10 \text { or } x \geq 40 \\
\frac{x-10}{15}, & 10 \leq x \leq 25 \\
\frac{40-x}{15}, & 25<x<40
\end{array}\right. \\
& \mu_{\text {long }}(x)=\left\{\begin{array}{cl}
0, & x \leq 25 \\
\frac{x-25}{25}, & 25 \leq x \leq 50 \\
1, & x \geq 50
\end{array}\right.
\end{aligned}
$$

a. The Affiliation Function of South Lane Vehicles Queue (NQ)
The affiliation function graphic for the southern lane queue can be seen in Fig. 2 below

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-05.jpg?height=409&width=790&top_left_y=1265&top_left_x=560)
Fig. 2. Affiliation Function of South Lane Queue

b. The Affiliation Function of West Lane Vehicles Queue (NQ)
The affiliation function graphic for the western lane queue can be seen in Fig. 3. below

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-05.jpg?height=401&width=794&top_left_y=1854&top_left_x=592)
Fig. 3 Affiliation Function of West Lane Queue

c. The Affiliation Function of North Lane Vehicles Queue (NQ)
The affiliation function graphic for the northern lane queue can be seen in Fig. 4. below
\begin{figure}
![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-06.jpg?height=383&width=782&top_left_y=377&top_left_x=604)
\end{figure}d.The Affiliation Function of Time Cycle
The following is the affiliation function for time cycle:

$$
\begin{aligned}
& \mu_{\text {quick }}(x)=\left\{\begin{aligned}
0, & x \geq 75 \\
\frac{75-x}{75}, & 50 \leq x \leq 75
\end{aligned}\right. \\
& \mu_{\text {normal }}(x)=\left\{\begin{aligned}
0, & x<60 \text { or } x \geq 90 \\
\frac{x-60}{15}, & 60 \leq x \leq 75 \\
\frac{90-x}{15}, & 75<x<90
\end{aligned}\right. \\
& \mu_{\text {slow }}(x)=\left\{\begin{aligned}
\frac{x-75}{25}, & x \leq 75 \\
1, & x \geq 100
\end{aligned}\right.
\end{aligned}
$$

The affiliation function graphic of the Time Cycle can be seen in Fig 5 below

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-06.jpg?height=373&width=822&top_left_y=1600&top_left_x=540)
Fig. 5. Affiliation Function of Time Cycle
3) . The basic rules of fuzzy

Fuzzy basic rules are a set of implications that apply as rules in the system. The basic rules are indicated by the existence of a set of linguistic statements or called fuzzy propositions. Fuzzy propositions or rules are determined in advance so that the fuzzy control system is in accordance with the circumstances. Until now there are no binding rules in determining the basis of this rule. So the determination is based on expert knowledge or operator experience. A FAM (Fuzzy Associative Memory) will be provided in table 3 to help shape the rules that will be used. The form of this rule is IF (antecedent 1) AND (antecedent 2) THEN (consequent).

Table 3. Fuzzy Associative Memory (FAM)
|  | West | Short |  |  | Medium |  |  | Long |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | North | Short | Med | Long | Short | med | Long | Short | Med | Long |
| South | Short | Quick | Quick | Normal | Quick | Normal | Normal | Normal | Normal | Normal |
|  | Medium | Quick | Normal | Normal | Normal | Normal | Normal | Normal | Normal | Slow |
|  | Long | Normal | Normal | Normal | Normal | Normal | Slow | Normal | Slow | Slow |


Example for rule 1 (R1):

[R1] If south lane vehicle queue is short AND west lane vehicle queue is short and north lane vehicle queue is short THEN time cycle is quick

4). Fuzzification

During the fuzzification process, the crisp (numerical) value will be mapped into the fuzzy set to define its degree of affiliation.

a. Southern Lane Vehicles Queue
$$
\begin{aligned}
& \mu_{\text {short }}(49)=0 \\
& \mu_{\text {medium }}(49)=0 \\
& \mu_{\text {long }}(49)=0,96
\end{aligned}
$$
b. Western Lane Vehicles Queue
$$
\begin{aligned}
& \mu_{\text {short }}(23)=0,08 \\
& \mu_{\text {medium }}(23)=0,867 \\
& \mu_{\text {long }}(23)=0
\end{aligned}
$$
c. Northern Lane Vehicles Queue
$$
\begin{aligned}
& \mu_{\text {short }}(43)=0 \\
& \mu_{\text {medium }}(43)=0 \\
& \mu_{\text {long }}(43)=0,72
\end{aligned}
$$

The degree of membership value can be further seen in table 4. below:

Table 4. Degree Of Membership Value
| Input (Number of Vehicles Queue) | Short | Medium | Long |
| :--- | :--- | :--- | :--- |
| South Lane $=49$ | 0 | 0 | 0,96 |
| West Lane = 23 | 0,08 | 0,867 | 0 |
| North Lane = 43 | 0 | 0 | 0,72 |


5). Rules evaluation

The $\alpha$-predicate calculation can be done by applying the implication function to each rule by using the MIN function. The examples are as follows:

[R1] IF south lane vehicle queue is short AND west lane vehicle queue is short and north lane vehicle queue is short THEN time cycle is quick.
$$
\alpha \text { predicate }{ }_{1}=\min (0 ; 0,08 ; 0)=0
$$

6). Rules composition

Furthermore, the MAX function is used to compose between every rule.

- For [R21] IF the south lane vehicle queue = 49 long AND the west lane vehicle queue = 23 short AND the north lane vehicle queue $=43$ long THEN the time cycle is medium with a minimum value of 0,08 .
- For [R24] IF the south lane vehicle queue = 49 long AND the west lane vehicle queue = 23 medium AND the north lane vehicle queue $=43$ long THEN the time cycle is medium with a minimum value of 0,72 .

So, it can be concluded that the affiliation function of the rules composition can be stated like the following equation

$$
\mu_{\text {quick and normal }}(x)=\left\{\begin{array}{cl}
\frac{x-60}{15}, & 60<x<61,2 \\
0,08, & 61,2<x<77 \\
\frac{x-75}{25}, & 77<x<93 \\
0,72, & 93<x<100
\end{array}\right.
$$

Calculating Momentum

$$
\begin{aligned}
\mathrm{M}_{1} & =\int_{60}^{61,2}\left(\frac{z-60}{15}\right) z d z=2,918 \\
\mathrm{M}_{2} & =\int_{61,2}^{77}(0,08) z d z=87,342 \\
\mathrm{M}_{3} & =\int_{77}^{93}\left(\frac{z-75}{25}\right) z d z=557,653 \\
\mathrm{M}_{4} & =\int_{93}^{100}(0,72) z d z=486,36
\end{aligned}
$$

Calculating Area

$$
\begin{aligned}
& A_{1}=\frac{1,2 \times 0,08}{2}=0,048 \\
& A_{2}=15,8 \times 0,08=1,264 \\
& A_{3}=\frac{(0,08+0,72)}{2} \times 16=6,4 \\
& A_{4}=7 \times 0,72=5,04
\end{aligned}
$$

Counting focus point at z (centroid method)

$$
\begin{aligned}
Z & =\frac{\mathrm{M}_{1}+\mathrm{M}_{2}+\mathrm{M}_{3}+\mathrm{M}_{4}}{\mathrm{~A}_{1}+\mathrm{A}_{2}+\mathrm{A}_{3}+\mathrm{A}_{4}}=\frac{2,918+87,342+557,653+486,36}{0,048+1,264+6,4+5,04} \\
& =88,949
\end{aligned}
$$

So, the resulting output of the time cycle done by using manual calculation is 88,949 seconds and is rounded off to 89 seconds.

The following are the steps to find the green time duration of each approacher. Deciding the flow ratio (FR) for each approacher.

1) . Flow ratio is obtained by dividing gross flows with vehicle flows.
    a) South
$$
F R_{\text {South }}=\frac{1444}{1500}=0,963
$$


b) West
$$
F R_{\text {West }}=\frac{1291}{1400}=1,076
$$
c) North
$$
F R_{\text {North }}=\frac{1465}{1500}=0,977
$$
2) . Determining Intersection Flow Ratio (IFR) : The intersection flow ratio is obtained by adding a critical flow ratio (=highest) for all consecutive signal phases within one cycle.
$$
I F R=0,963+1,076+0,977=3,016
$$
3) . Determining Phase Ratio (PR) of approacher
Phase ratio is obtained by dividing Intersection Flow Ratio with its Flow Ratio

    - South
$$
P R_{\text {South }}=\frac{0,963}{3,016}=0,319
$$
    - West
$$
P R_{\text {West }}=\frac{1,076}{3,016}=0,357
$$
    - North
$$
P R_{\text {North }}=\frac{0,977}{3,016}=0,324
$$
4) . Dividing the green time of each approacher
    a) South
$$
g_{\text {South }}=(89-12) \times 0,319=24,563 \approx 25 \text { seconds }
$$
    b) West
$$
g_{\text {West }}=(89-12) \times 0,357=27,489 \approx 28 \text { seconds }
$$
    c) North
$$
g_{\text {North }}=(89-12) \times 0,324=24,948 \approx 25 \text { seconds }
$$

The following is a display application example for the simulation. The result of the green time output will be mapped to the simulation panel which is in each traffic light. For the South lane, the green time output is 25 seconds, therefore when the simulation takes place, the South lane traffic light will show the green time of 25 seconds. The result for the South lane's green time simulation can be seen in Fig. 6 below

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-09.jpg?height=542&width=945&top_left_y=1769&top_left_x=469)
Fig. 6. Simulation Result of South lane's Green Time

### 3.2. Comparing the Observed Data Results and the Department of Transportation (DISHUB) Data

## 1) Time Cycle Comparison

Comparison of time cycle which is thobserved data from 06 p.m. - 07 p.m shown in table 5 at Batu Sari intersection using Fuzzy Inference System (FIS) of Mamdani is more dynamic compared to the data obtained from the Department of Transportation (DISHUB) DKI Jakarta. This Fuzzy Inference System (FIS) type Mamdani is more dynamic because it considers each approaching vehicle queue.

Table 5. Table of Comparison of Cycle Times 06 p.m - 07 p.m
| Observation hour | Cycle | Vehicle queue (passenger car unit) |  |  | Cycle time (second) |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | south | west | north | Department of Transportation (DISHUB) DKI Jakarta | Research result |
|  | 1 | 43 | 30 | 25 | 112 | 77 |
|  | 2 | 42 | 23 | 29 | 112 | 76 |
|  | 3 | 40 | 28 | 36 | 112 | 85 |
|  | 4 | 45 | 29 | 32 | 112 | 78 |
|  | 5 | 35 | 27 | 30 | 112 | 78 |
| $06 \mathrm{pm}-07 \mathrm{pm}$ | 6 | 46 | 25 | 30 | 112 | 77 |
|  | 7 | 47 | 26 | 32 | 112 | 78 |
|  | 8 | 50 | 24 | 29 | 112 | 76 |
|  | 9 | 49 | 23 | 43 | 112 | 91 |
|  | 10 | 35 | 19 | 27 | 112 | 76 |


The comparison graphic can be seen at Fig 7 below

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-10.jpg?height=480&width=899&top_left_y=1427&top_left_x=496)
Fig. 7. Time Cycle Comparison Graphic for 6 p.m. - 7 p.m.

## 2) Green Time Comparison

Comparison the green time of South Lane, West Lane and North Lane observed data from 6 p.m. - 7 p.m can be seen in table 6 below. It is shown that the green time output from 6 p.m. - 7 p.m. in Batu Sari intersection using the Fuzzy Inference System (FIS) of Mamdani method is more dynamic in comparison to the data obtained from the Department of Transportation (DISHUB) DKI Jakarta. This Fuzzy Inference System (FIS) type Mamdani resulted in a more dynamic green time output because it considers the vehicular queue, vehicle flows and gross flows in its approacher.

Table 6. Table of Comparison of Green Times 06 pm - 07 pm
| Observation Hour | Cycle | Green time of South Lane (second) |  | Green time of West Lane (second) |  | Green time of North Lane (second) |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  |  | Department of Transportation (DISHUB) DKI Jakarta | Research result | Department of Transportation (DISHUB) DKI Jakarta | Research result | Department of Transportation (DISHUB) DKI Jakarta | Research result |
| $06 \mathrm{pm}-07 \mathrm{pm}$ | 1 | 40 | 21 | 30 | 23 | 30 | 21 |
|  | 2 | 40 | 21 | 30 | 23 | 30 | 21 |
|  | 3 | 40 | 23 | 30 | 26 | 30 | 24 |
|  | 4 | 40 | 21 | 30 | 24 | 30 | 21 |
|  | 5 | 40 | 21 | 30 | 23 | 30 | 21 |
|  | 6 | 40 | 21 | 30 | 23 | 30 | 21 |
|  | 7 | 40 | 21 | 30 | 24 | 30 | 21 |
|  | 8 | 40 | 20 | 30 | 23 | 30 | 21 |
|  | 9 | 40 | 25 | 30 | 28 | 30 | 26 |
|  | 10 | 40 | 20 | 30 | 23 | 30 | 21 |


The comparison graphic can be seen at Fig 8, Fig 9 and Fig 10 below

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-11.jpg?height=528&width=1098&top_left_y=1068&top_left_x=385)
Fig. 8. Comparison Graphic for South Lane Green Time at 6 p.m. - 7 p.m.

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-11.jpg?height=558&width=1094&top_left_y=1721&top_left_x=389)
Fig. 9. Comparison Graphic for West Lane Green Time at 6 p.m. - 7 p.m.

![](https://cdn.mathpix.com/cropped/14750c50-885a-42e5-9165-8250a62ecfef-12.jpg?height=598&width=1080&top_left_y=234&top_left_x=409)
Fig. 10. Comparison Graphic for North Lane Green Time at 6 p.m. - 7 p.m.

## 4. Conclusion

Based on the analysis and discussion results, the Fuzzy Inference System (FIS) type Mamdani can be applied in an analysis of a traffic light settings system at Batu Sari intersection, Jakarta Barat, in which the calculation and analysis shows the time cycle duration of 89 seconds with the green time distribution for the South lane is at 25 seconds, West lane for 28 seconds and the North lane for 25 seconds. The simulation application made for the traffic lights at Batu Sari Intersection helps calculating the Fuzzy inference System (FIS) analysis method type Mamdani better because the green time can be directly presented in the simulation. From the solution comparison between calculation analysis and Transportation Ofiice of DKI Jakarta (DISHUB DKI Jakarta), it can be deduced that by applying the Fuzzy inference System (FIS) type Mamdani method, the green time duration obtained is considered to be more dynamic.

## Acknowledgements

We thank to Bina Nusantara University was supported this research and who provided insight and expertise that greatly assisted this paper, and reviewer for comments that greatly improved the manuscript.

## References

1. Prasetiyo EE, Wahyunggoro O, Sulistyo S. "Design and Simulation of Adaptif Traffic Light Controller Using Fuzzy Logic Control Sugeno Method". International Journal of Scientific and Research Publications. 2015; 5(4).
2. Zachariah B, Ayuba P, Damuut LP. "Optimization of Traffic Light Control System of an Intersection Using Fuzzy Inference System". Science World Journal. 2017; 12(4).
3. Salehi M, Sepahvand I, Yarahmadi M. "TLCSBFL : A Traffic Light Control System Based on Fuzzy Logic". International Journal of u- and e-Service, Science and Technology. 2014; 7(3).
4. Mohit J, Shailia S. "Design of Fuzzy Logic Traffic Controller For Isolated Intersection With Emergency Vehicle Priority System Using MATLAB Simulation". Control Instrumentations System Conference. 2014 May.
5. Krzysztof M, Stanislaw I. Modeling traffic flow on two-lane roads with traffic lights and countdown timer. Transportation Research Procedia. 2019; 39.
6. Madalin DP. Traffic light management using optimization tool. Procedia- Social and Behavioral Sciences. 2018; 238.
7. Thuniga T, Schefflerb R, Strehlerb M, Nagela K. Optimization and simulation of fixed time traffic signal control in real word application. Procedia Computer Science. 2019; 151.
8. Zulfikar WB, Jumadi , Prasetyo PK, Ramdhani MA. Implementation of Mamdani Fuzzy method in employee promotion system. IOP Conf.Series: Materials Science and Engineering. 2018; 288.
9. Segismundo SI, Luis RI. Mamdani Fuzzy Systems for Modelling and Simulation : A critical Assessment. Journal of Artificial Societies and

Social Simulation. 2018; 21(3).

10. Khan MA, Hazan Z, Abbas S, Fatima A. Intelligent Transportation System for Smart-Cities using Mamdani Fuzzy Inference System. International Journal of Advanced Computer Science and Applications. 2018; 9(2).
11. Kusumadewi S. Fuzzy Multi-Attribute Decision Making (FUZZY MADM) Yogyakarta: Graha Ilmu; 2006.
12. Marga DJB. Manual Kapasitas Jalan Indonesia (MKJI). Jakarta:, Departemen Pekerjaan Umum; 1997.
13. Zadeh LA. "Fuzzy Sets". Information and Control. 1965; 8(3).

[^0]:    * Corresponding author. Tel.: +62 81282829430; fax: +62 215300244
    E-mail address: citie_math@binus.ac.id

