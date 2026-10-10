# Traffic queue modeling using arena simulation software (a case study of Mergan 4-Way intersection in Malang City) 

Dani Yuniawan ${ }^{1, *}$, Aang Fajar P. $\mathrm{P}^{1}$, Samsudin Hariyanto ${ }^{1}$, and Romi Setiawan ${ }^{1}$<br>${ }^{1}$ Industrial Engineering Department, Engineering Faculty, University of Merdeka Malang, 65146 Malang, Indonesia


#### Abstract

Currently Mergan 4-way intersection is one of intersection that have most traffic dense in Malang City, East Java - Indonesia. This research implement simulation method in order to give several solution option to manage the traffic queue in Mergan 4-way intersection. Simulation method is conducted with several phase, from problem identification up to verification and validation also scenario simulation. Arena Simulation software v. 14 is chosen as the tool to modeling the traffic queue line. The research outcome give several solution through Traffic Light 2 simulation scenario. With this simulation scenario, the traffic flow system simulation can be run with fewer queues of vehicles.


## 1 Introduction

In the INRIX 2017 Survey [1], the congestion rate in Malang beats Surabaya as the capital of East Java (INRIX is a software SaaS and DaaS company which provides of Internet services and mobile applications related to road traffic and driver services in 38 countries). The second largest city in East Java is even sitting as the third city with the worst congestion level in Indonesia. The rider must spend 45 hours a year on a standstill with an overall percentage of 23 percent. During peak hours, congestion rose to 27 percent compared to outside peak hours of 24 percent. According to [2], long queues result in congestion that can interfere with other activities. Traffic congestion leads to loss of time, cost and air pollution. Therefore, it is necessary to control the optimal traffic (more precisely it called the queue) to create a comfortable city environment to live in. Basically, a queue is a common phenomenon that occurs when the need for a service exceeds the capacity available to carry out the service. In other words, the formation of the queue is if the consumer (goods or persons) who come to a service facility is not immediately served by the existing facilities [3]. The number of traffic accidents at the signaled intersection was 0.43 crashes / million vehicles compared with 0.60 at the non-signal intersection and 0.30 on the roundabout [4]. In overcoming these problems, this research employing simulation tools, because of the decision-making process will take more efficient time compare to

[^0]other analytic method. Based on these problems, this research intends to find the optimal solution by comparing the queue level of the vehicle without using traffic lights or by using traffic lights for Mergan 4-way intersection at Malang, with the help of Arena simulation software v.14.

## 2 Literature Review

Previous research that underlies this research includes, first; [5], conducted a study entitled "Traffic Lights Duration Analysis Using Simulation Method". Objects studied namely ITN Crossroad (National Institute of Technology of Malang), which is access for two-or fourwheel riders passing around the road. This research uses simulation approach with ARENA simulation software to determine best scenario to overcome congestion at ITN intersection. Secondly, [6] conducted a study entitled "Determining Optimal Time on Traffic Controller Using Simulation Method". Case Study at Jl. Soekarno Hatta Buah Batu. Simulation in this research is done by using Promodel 6.0 simulation software. Thirdly, [7] conducted a study entitled "Simulation of Traffic Light Motor Vehicle Queue at Crossroads with Round Robin Method". In this research, Pristiwanto used the Round Robin Application, with the aim of enabling the use of linguistic variables and inexact traffic light to be manipulated in the design of signal timing plans.

## 3 Research Methodology

Research was done through several stages (Figure 1). The first stage are field study, literature study, and problem identification which is include the research objectives are at the second stage.

![](https://cdn.mathpix.com/cropped/a83fa663-8099-4d5f-be70-94ca020b4fc8-2.jpg?height=389&width=705&top_left_y=1361&top_left_x=484)
Fig.1. Research flow diagram.

In this stage the place or object of direct observation (data collection) is the Mergan 4-way intersection, Kec. Klojen, Malang City, East Java 65146. The object studied is the access road connecting to the centre City, Market, Factory, Mall, and public area. The third stage is the collection of data needed to implement the simulation modeling. The data taken is number of vehicles passing through the observed streets during morning, afternoon, and evening, each for workday and weekend. The four stage are include the distribution fitting, build the simulation model, verification and validation model, where it refers to how to build a model system with precise and accurate, to build a model that is able to meet the objectives of the research. The simulation model within the software should be an image that corresponds to the model of the system in the real world of observation. Verification phase is expected to answer the question whether the model has been implemented correctly in the computer. And for validation phase, it is associated with how the model is
performed, to determine whether the conditions in the field can be accurately described by the simulation model that has been built. Validation is done by entering the experimental data obtained from the observation stage and comparing it to the situation in the field. In this case the validation test is done by using T-distribution or T-test to know the validation of the data, after that build the scenario simulation for traffic queue in the model. After that, then scenario simulation can be performed. The fifth stage are include data analysis and scenario analysis, which is will be discussed in last part of this research in order to observe which scenario is the optimal solution. This research using assumption that all driver obey the traffic rules.

## 4 Data Collection \& Model Development

### 4.1 Data Collection

Input Analyzer is a facility within Arena simulation software with the aim is to do the distribution fitting before enter the data that was obtained at the time of field observation into the simulation model. The data obtained at the time of observation is being fitted first for it's statistically distribution in order to be included in the simulation model. The following is example of distribution fitting data generated using Input Analyzer (Figure 2).

![](https://cdn.mathpix.com/cropped/a83fa663-8099-4d5f-be70-94ca020b4fc8-3.jpg?height=419&width=597&top_left_y=1095&top_left_x=539)
Fig.2. Example of input analyzer result for distribution fit test.

### 4.2 Traffic Simulation Model Development

The simulation model was made after observation to the field in order to see the real condition before finally made simulation model. This model is designed to facilitate a simulation model in Arena 14. This simulation model is employed for each section in 4-way intersection is shown in Figure 3.
![](https://cdn.mathpix.com/cropped/a83fa663-8099-4d5f-be70-94ca020b4fc8-3.jpg?height=288&width=1118&top_left_y=1968&top_left_x=277)

Fig.3. Example of a section of 4-way intersection Simulation Model in Arena Software Simulation.

From the Figure 3 above, each section which is modeled and implemented to 4 parts of 4-way intersection. Jalan Jupri, Jalan Langsep, Jalan Ir. Rais, and Jalan Mergan Lori (Figure 4). The simulation model created based on real conditions in the field. It's applies equally for each road segment which is being modeled.

### 4.2.1 Model Verification

Verification model is a phase that aims to ensure the model has been made based on actual events during observation and each element within the model functioning properly [8]. Here are the animations that have been made in the traffic queue simulation model.

![](https://cdn.mathpix.com/cropped/a83fa663-8099-4d5f-be70-94ca020b4fc8-4.jpg?height=449&width=816&top_left_y=808&top_left_x=425)
Fig.4. Capture of Animation traffic queue model while running the simulation.

### 4.2.2 Model Validation

Model Validation aims to ensure that the simulation result in the Arena software is valid based on data obtained at the time of observation [9]. To ensure the validation of the data, it is based on a simulation model that has the same characteristics as the observations made. In this case to know the data used is valid that is using T test. T test is used to test the difference of mean of 2 variables from different sample. This research employ Microsoft excel add on analysis pack for T test model validation [10]. The hypothesis taken are: $\mathrm{H}_{0}=\mathrm{A}<\mathrm{B}$ (there is no significant difference compare to data simulation result); $\mathrm{H}_{1}=\mathrm{A}>\mathrm{B}$ (there is significant difference compare to data simulation result) Where: A = Original Data (Observation); B = Data of Simulation Result (Arena)

Table 1. T Test Example - Mergan Lori Street.
| Mean | 7,564613 | 8,29126 |
| :--- | :--- | :--- |
| Variance | 161,9012 | 731,7269 |
| Observations | 2159 | 85271 |
| Pooled Variance | 717,6618 |  |
| Hypothesized Mean Difference | 8 |  |
| df | 87428 |  |
| t Stat | -14,948 |  |
| $\mathrm{P}(\mathrm{T}<=\mathrm{t})$ one-tail | 9,26E-51 |  |
| t Critical one-tail | 1,644871 |  |
| $\mathrm{P}(\mathrm{T}<=\mathrm{t})$ two-tail | $1,85 \mathrm{E}-50$ |  |
| t Critical two-tail | 1,959991 |  |


Acceptance Criteria Hypothesis Test:

1. $\mathrm{H}_{0}$ is accepted, if T Count is smaller than T table ( $\mathrm{H}_{1}$ is rejected)
2. $\mathrm{H}_{0}$ is rejected, if T Count is greater than T table ( $\mathrm{H}_{1}$ accepted)

From T test result, it can be seen that T Stat (T Count) with value (-14,948) and T Critical one-tail (T table) with value (1.64487). In this case T Count <T Table means $\mathrm{H}_{0}$ accepted. Therefore, it can be seen that the data produced there is no significant difference between data A (Original Data) and data B (Data Simulation Results). Related to the resulting T test that can be concluded between the original data and simulation result data no significant difference (Table 1). It means in this case, data result from validation (T-test) that included into the simulation software is valid or the data is true. This procedure is implemented to all section models in simulation software and all result are valid.

## 5 Result and Discussion

The 4-way intersection of mergans has four streets, namely Jupri Street, Jalan Raya Langsep, Jalan Ir. Rais, and Jalan Mergan Lori. Of the four road segments have different road width and geometric point. Starting from the width of the road is too narrow and geometric way up and down. This greatly affects the flow of the road. In addition, the 4-way intersection access on mergan become very busy / crowded to be passed by vehicles because it can connect to public places or tours in the city of Malang. Observations made are divided into 3 parts, namely Morning, Day, and Afternoon. To see specifically the amount of vehicle (cars and motorcycles) volume per unit time can be seen in Figure 5.

![](https://cdn.mathpix.com/cropped/a83fa663-8099-4d5f-be70-94ca020b4fc8-5.jpg?height=298&width=1241&top_left_y=1276&top_left_x=219)
Fig.5. Graph comparison between each way section.

From the above graph (Figure 5), it can be seen the dominance of the vehicle at the time of Morning, afternoon, and evening is on the Raya Langsep Street. From the simulation data result, it will be analyzed and become several alternatives to the problem. The simulation model of "Traffic Light" is divided into 4 streets (Jl Jupri, Jl Raya Langsep, IR Rais and Jl Mergan Lori) and is divided into 2 categories of vehicles (Cars and Motorcycles) as entities that cross Mergan 4-way intersection. In this case the resulting data is queue which shows the level of queue in each direction of the road (Straight, Turn Right, and Left Turn). In this case the simulation model is divided into 2 types, namely "Traffic Light 1" and "Traffic Light 2". Traffic Light 1 illustrates traffic lights with an alternate one traffic flow movement. This alternative takes the picture of a traffic system such as the Four Dieng Intersection, i.e with one by one the movement per road section. As for Traffic Light 2 describes in accordance with the problems at the Mergan 4-way intersection. This alternative corresponds to two simultaneous traffic flow movements. So in the "Traffic Light" simulation model there are 2 alternatives as an option in analyzing the problem with
the aim of providing solutions. The following data generated with the simulation model "Traffic Light 1" and "Traffic Light 2".

From the graph (Figure 6) shows that of the three alternative models that have been made, then the total lowest queue is by using the model or system Traffic Light 2. In this case known total queues for the straight current 833 units per time interval, and for the right turning current 627 units per time interval. Hence, in this alternative solution taken the modeling system using traffic lights with 2 variations. For this alternative model is expected to minimize the queue or the level of congestion that occurred at the Mergan 4-way intersection. The Turn left data shows zero result due to in this observation, vehicle that no condition on waiting in queue not listed as a queue. Decisions on the selection of traffic lights based on vehicle category and volume.

Total Queue
![](https://cdn.mathpix.com/cropped/a83fa663-8099-4d5f-be70-94ca020b4fc8-6.jpg?height=251&width=1219&top_left_y=782&top_left_x=209)

Fig.6. Total queue for each scenario.

## Conclusion

With the alternative model of Traffic Light 2-scenario simulation (the lowest queue result), the traffic flow system can be run and implemented in the real traffic line. This scenario simulation is become one of proposal solution in order to improve the smoothness of traffic in Mergan 4-way intersection. For future work, there is possibilities to do more detail in experiment design with simulation in order to obtain more optimal result.

## References

1. INRIX, the INRIX 2017 Global Traffic Scorecard, Los Angeles: INRIX (2017)
2. Amri, M. \& Malasy, T. S., Malikussaleh Industrial Eng. J., 2 (2013)
3. Benyamin Indra Prawira, Simulasi dan Pemodelan Lalu Lintas Pada Simpang Bersinyal Untuk Mengurangi Kerugian Antrian (2017)
4. Directorate General of Highways, Manual Road Capacity. Jakarta: Office of Highways (1997)
5. Tama, I. P. et al, J. of Eng. Man. in Industrial System, 4 (2016)
6. Yani, I., (2014)
7. Pristiwanto, Simulasi Traffic Light Antrian Kendaraan Bermotor pada Persimpangan dengan Metode Round Robin, Majalah Ilmiah INTI - P3M STMIK Budi Darma Medan, (2013)
8. Yuniawan, D. et al, Int. J. of Internet Manufacturing and Services, 3 (2014)
9. Yuniawan, D. et al, Concurrent Engineering Research and Application J., 21 (2013)
10. Supranto, J., Statistic - Theory and Application, 2 (2016)

[^0]:    * Corresponding author: dani.yuniawan@unmer.ac.id

