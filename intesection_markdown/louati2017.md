# An immune memory inspired case-based reasoning system to control interrupted flow at a signalized intersection 

Ali Louati ${ }^{\mathbf{1 , 3}}$ • Sabeur Elkosantini ${ }^{\mathbf{2 , 3}}$ • Saber Darmoul ${ }^{\mathbf{2}}$ • Lamjed Ben Said ${ }^{\text {3 }}$

© Springer Science+Business Media B.V., part of Springer Nature 2017


#### Abstract

To monitor and control traffic at signalized intersections, several traffic signal control systems (TSCSs) were developed based on optimization and artificial intelligence techniques. Unfortunately, existing approaches put little emphasis on providing concepts and mechanisms that are generic enough to deal with a variety of disturbances while maintaining traffic fluidity. Moreover, only a few works have investigated case-based reasoning (CBR) to control traffic at signalized intersections. Existing works usually state that the case-base is created using experts' knowledge but do not specify how this knowledge is acquired and how the case-base is built. The contribution of this study is threefold. First, a new TSCS is designed to monitor and control traffic at a signalized intersection using innovative concepts and mechanisms borrowed from the biological immune memory and secondary immune response. Immune memory provides the concepts to represent cases to deal with disturbances in a more generic way, and immune secondary response mechanisms guide the design of a CBR system to monitor traffic and control disturbances. Second, a new learning algorithm for the creation of the case-base combining simulation-optimisation, condensed nearest neighbour algorithm and a rule-based system are developed. Third, the performance of the suggested TSCS is assessed by benchmarking it against two standard


[^0]control strategies from the literature, namely fixed-time traffic signal control and the longest queue first-maximal weight matching algorithm. The suggested TSCS is implemented in Python and applied on an intersection simulated using VISSIM, a state-of-the-art traffic simulation software. The results show that the suggested TSCS is able to handle different traffic scenarios with competitive performance, and that it is recommended for extreme situations involving blocked approaches and high traffic flow.

Keywords Traffic signal control systems • Artificial immune system • Case-based reasoning • Longest queue first maximal weight matching algorithm • Condensed nearest neighbour algorithm • Fixed-time controller

## 1 Introduction

With the sustained pace of urbanisation and growing mobility requirements, the monitoring and control of traffic flow on urban roads became a major concern for local transportation authorities. Ineffective or inefficient traffic control lead to congestion and accidents, with human casualties and severe damage to equipment and infrastructure (Bellemans et al. 2002). Transportation authorities have to improve traffic flow management and to ensure user safety, especially when disturbances occur. Such disturbances include dealing with congestion and bottlenecks, managing accidents and adverse weather conditions (i.e., heavy rain, fog, smoke, dust, etc.), handling major events (international meetings, conferences, sport events, shows, etc.), and clearing the way for high priority vehicles, such as ambulances, firefighters, army, or police vehicles. In such situations, intersections (also called junctions), which are areas of exchange between several roads that allow vehicles to move from one area to another (Robertson and Bretherton 1991), may become bottlenecks of the urban road network and the major source of traffic congestion.

Although construction of new infrastructure may be a solution to such traffic problems, it requires considerable time to achieve the project, and availability of both geographical space and high financial investment to conduct the construction project. Unfortunately, these conditions are very often hardly met simultaneously. Consequently, transportation authorities have invested in Traffic Signal Control Systems (TSCS) in order to control the traffic at signalized intersections. TSCS coordinate individual traffic signals to improve traffic fluidity, avoid conflicting movements and deadlock situations, and therefore achieve network-wide traffic operation objectives (Traffic Signal Control Systems 1997). TSCSs determine decisions to be sent to traffic signals in order to better control the traffic flow. These decisions are related to the duration of phases (i.e. cycle times or duration of green and red signal times) and to the sequence that governs phase transitions. Several TSCSs were developed to control traffic flow at signalized intersections. They can be classified into two classes: pre-timed and actuated systems.

Pre-timed controllers include systems such as TRANSYT (Robertson 1969) and MAXBAND (Little et al. 1981). These systems are based on a fixed time strategy: the duration and sequence of all phases remain fixed and do not take into account or adapt to the dynamic state of the traffic at each approach of the intersection. The signal timing-plan is selected according to a fixed schedule from a set of predetermined plans. These plans are developed off-line on the basis of historical traffic data and using statistical analysis and mathematical optimization methods (Angulo et al. 2011). Various theories and methods were applied to enhance the timing efficiency of traffic signals (Li 2011; Wong and Woon 2008; Yin 2008).

Yin (2008) indicated that pre-timed (fixed) traffic signals are widely used in the developing countries due to the high costs of implementation and maintenance of real-time adaptive signal control systems. The author particularly pointed out that further improvements of the performance of TSCS is still needed, for example to improve their ability to detect and to react to changes in traffic conditions.

Actuated controllers, which are adaptive traffic control systems, include systems such as SCATS (Luk 1984), SCOOT (Robertson and Bretherton 1991), PRODYN (Henry et al. 1984), TRANSYT-7F (Wallace et al. 1984), PASSER II (Chang et al. 1988), CRONOS (Boillot et al. 1992), and RHODES (Mirchandani and Head 2001). Actuated systems are based on adaptive time strategies: the timing of traffic signals is adjusted in order to optimize either a single objective (e.g. minimize the total waiting time or delay of vehicles in queues at intersections), or multiple objectives (e.g. minimize total waiting time and maximize average speed). This adjustment is made based on the length of the traffic queue at each approach of the intersection. This detection is achieved using traffic detectors, which provide information on the presence or absence of vehicles at intersections.

### 1.1 Disturbance management capabilities of TSCS

In the scientific literature, a few references have addressed urban traffic disturbance management, including disturbance modeling and the development of reactive approaches. For example, TRANSYT-7F (Wallace et al. 1984) has restricted ability to consider different types of disturbances. SCOOT (Robertson and Bretherton 1991) is able to detect disturbances related only to traffic congestion and bus priority. Kosonen (2003) presented a TSCS that only uses vehicle queue lengths to detect disturbances. The developed TSCS is based on a set of fuzzy rules to decide about the extension of an active green time. The author relies on a human expert to construct the rule base. However, there is no specification about how knowledge is captured. Wen (2008) detects congestions using data about the vehicle flow, inter-arrival time between vehicles, and average vehicle speed. The TSCS uses a knowledge base containing a set of rules to select and activate the appropriate phase. However, the author does not detail how the knowledge base is designed.

Despite the help that TSCS provide, and in spite of their successful implementation and widespread use in many cities (Stevanovic 2010), existing TSCS still offer limited support to deal with disturbances. Limitations stem from the lack of explicit models for the representation of knowledge related to disturbances. Limitations are also related to the development of generic mechanisms, and integrated functions that provide support to issues such as how to detect disturbances, and how to determine/adapt decisions to disturbances, not only in terms of signal timing and sequence, but also in terms of coordination between several intersections. Existing systems suffer limitations to suggest appropriate reaction strategies in a way that is generic enough so that no, or at least little, customization is required when a new type of disturbance is considered.

### 1.2 Case-based reasoning approaches to traffic signal control

In the scientific literature, many TSCS were developed based on artificial intelligence paradigms (Araghi et al. 2015; Tahilyani et al. 2013). However, only a limited number of works investigated the use of case-based reasoning (CBR) for traffic control as a problemsolving paradigm that relies on earlier experiences to solve new problems.

De Schutter et al. (2003) developed a decision support system (DSS) that combines a multi-agent system and CBR to select and evaluate possible control decisions to control traf-
fic in highways via variable message signs. Decisions include setting speed limits, showing dynamic route guidance, and opening shoulder lanes. Instead of simulating all possible decisions, the system selects the most similar cases from the case-base using a similarity measure based on fuzzy membership functions. The system simulates these selected cases and ranks them according to a specified performance indicator. The human operator can then choose one decision among the evaluated list.

Karim and Adeli (2003) developed a DSS to control the traffic and improve safety in work zones. Different types of control decisions are evaluated according to the type of work and traffic to guide drivers through the work zone with adequate protection for the workers. Cases were created from information obtained from the Ohio Department of Transportation.

Sadek et al. (2001) developed a CBR system to solve the problem of freeway traffic routing. The system monitors the traffic flow on several roadway segments of a highway network. The information received through various devices, such as sensors and closed circuit television, is used to detect disturbances. When an incident is detected, the system develops a routing strategy that optimizes the utilization of network capacity and helps drivers to avoid the disturbed roads.

Elkosantini et al. (2011a,b) developed a bimodal traffic controller for signposted roadrail intersections. The main objective was to manage the existing infrastructure to relieve congestion, react to disturbances, and insure a safer and more convenient travel for people. Authors developed a CBR system, coupled with fuzzy set theory, where each case is associated to a situation (traffic status) and its regulation decision (timing schedules).

In this limited number of works, authors usually state that the case-base is created using experts' knowledge. However, they do not specify how this knowledge is acquired and how the case-base is built. A famous technique called the Condensed Nearest Neighbour (CNN) algorithm was widely used in other CBR application domains to build and optimize the size of case-bases (Murty and Devi 2011; Smyth and McKenna 1999). However, to the best knowledge of the authors, this technique has not yet been applied to traffic signal control problems.

### 1.3 Problem statement

In this article, we consider the control of a single signalized intersection, with only one type of vehicles, i.e. without differentiating between cars and other vehicles, such as buses or trucks. Accordingly, this article intends neither to coordinate traffic across several intersections, nor to deal with all possible kinds of disturbances. Instead, it intends to provide pertinent concepts and mechanisms, relevant to the traffic signal control problem, and to show that these concepts and mechanisms provide decision-support, with competitive performance, to deal with disturbances. More particularly, we are interested in:

- Designing a new CBR based TSCS to monitor and control traffic at a single signalized intersection in case of disturbances. The design should allow describing features (indicators, symptoms, etc.) and attributes (causes, context, etc.) of disturbances, and allow this description to be extended to integrate other features and attributes when/as needed, and without questioning the downstream decision/reaction mechanisms. To provide concepts and mechanisms that are more explicit and generic than existing approaches, we adopt biological immunity as a design guideline;
- Developing a new learning algorithm to build the case-base and optimize its size to deal with relevant traffic disturbances. We suggest combining simulation-optimisation, condensed nearest neighbour (CNN) algorithm and a rule-based system. This learning

algorithm fills the gap in the literature concerning how to obtain a case-base in CBR approaches for traffic control;
- Assessing the performance of the suggested TSCS by benchmarking it against two standard control strategies from the literature, namely fixed-time traffic signal control and the longest queue first-maximal weight matching (LQF-MWM) algorithm.

Therefore, the remainder of this paper is organized as follows. Section 2 introduces the main features of biological immunity and reviews artificial immune system applications in traffic control. Section 3 introduces our design, implementation and developed system. Section 4 details the experimentation framework used to assess our system. Section 5 assesses the performance of the suggested system and discusses the obtained results. We conclude the article by discussing our contributions and opening further research directions.

## 2 Biological immunity and artificial immune systems: an overview

Biological immunity is a natural system that relies on a limited but efficient and effective number of concepts and mechanisms to deal with a great variety of disease causing elements disturbing its normal behaviour. The following sections provide a general description of the main biological immune concepts and mechanisms, and an overview on existing works that adapt those concepts and mechanisms to solve transportation and traffic engineering problems.

### 2.1 Biological immunity

The biological immune system (BIS) reacts to adverse environmental changes, and to internal and/or external stimuli to the organism by discovering and eliminating disease causing elements called "antigens", such as viruses, bacteria, and other parasites. The BIS initiates an immune response to neutralize the detected antigens. Figure 1 shows the main mechanisms involved in an immune response. When an antigen enters into the body, it stimulates a subset of immune cells, called "lymphocytes", to produce special molecules, called "antibodies". Antibodies bind to antigens, block them and thereby lead to their elimination. The mechanism of affinity allows measuring the intensity of this binding. The higher the affinity, the better the immune system recognizes and eliminates the antigen. During the immune response, lymphocytes differentiate into two main types of cells: effector (plasma) cells and memory cells (Hofmeyr 2001; Perelson and Weisbuch 1997). Effector (plasma) cells have a short lifetime and are created for the immediate defense of the organism. Memory cells are long-lived cells that circulate through the host organism. This concept is called the immunological memory. When confronted with the presence of an antigen that was previously recognized, memory cells are able to launch a rapid and effective secondary immune response. Usually, artificial immune systems (AIS) often use the idea of memory cells to retain good solutions to the problem under consideration. In our case, we rely on immune memory, and on the mechanism of affinity to control traffic at a signalized intersection.

### 2.2 Artificial immune systems for transportation and traffic engineering

Recently, very few works have investigated adaptations of biological immune concepts and mechanisms to solve transportation and traffic engineering problems. In public transportation engineering, Darmoul and Elkosantini (2014) identified new concepts and mechanisms and introduced a knowledge-based decision support approach to monitor and control public bus

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-06.jpg?height=622&width=1199&top_left_y=185&top_left_x=164)
Fig. 1 Selection, proliferation and differentiation of immune cells. Reproduced with permission from De Castro and Von Zuben (1999)

transportation systems. More closely related to traffic signal control, a few recent research works investigated AIS to develop TSCS (Moalla et al. 2013; Negi 2006; Trabelsi et al. 2012). For example, Negi (2006) proposed an AIS that is able to detect simple abnormal conditions affecting the traffic flow, such as congestions. Trabelsi et al. (2012) proposed an algorithm based on the clonal selection theory to control traffic at a single signalized intersection. The algorithm aimed to increase the flow of vehicles by minimizing the length of the queues in different approaches of an intersection. Moalla et al. (2013) presented an algorithm based on the immune network theory to monitor traffic at a single signalized intersection, and to determine regulation decisions as soon as a disturbance is detected. It is worth noting that these works are "proofs of concepts", aimed at introducing new analogies and at showing how these analogies contribute to solve traffic control problems. They lack in-depth analysis and assessment of their performance compared to other state of the art algorithms. Our article provides a novel analogy and innovative technological implementation choices, as well as a detailed comparative analysis with a state-of-the-art traffic control algorithm (cf. Sect. 4.3).

## 3 An immune memory based CBR

The BIS maintains the integrity of the body in the presence of disease causing elements (i.e. antigens). Similarly, a TSCS should maintain traffic fluidity at acceptable levels in case of disturbances. Antigens disturb the body organs, tissues and functions. Consequently, the body develops an immune response to generate the suitable antibodies that can eliminate antigen. In traffic management, disturbances can be detected based on symptoms, such as queue lengths and waiting times at one or more approaches of the intersection. When a disturbance is detected, the TSCS has to determine the most appropriate control decisions to deal with it. After reaction, the BIS memorizes both the antigen and the antibody that eliminated the antigen in order to reuse it (during a secondary immune response) when a similar antigen is detected. Similarly, the TSCS should store the determined control decision in a database

Table 1 Analogy between the Biological Immune System and TSCS
| Biology | Analogy |
| :--- | :--- |
| Body | A signalized intersection |
| Biological immune system | Traffic signal control system |
| Antigen | Disturbance detected at the intersection |
| Antibody | A case, i.e. a disturbance and its associated control decision (phase sequencing and duration) |
| Affinity | Measure of similarity between control decision and disturbance |
| Immune memory | Storage of cases (disturbances and control decisions) in a case-base. The immune memory corresponds to the case-base of disturbances and control decisions |
| Secondary immune response | Retrieval of cases from the case-base to use them to control disturbances |


(case-base) to reuse it when similar traffic conditions are detected. Table 1 synthesizes the analogies between biological immunity and traffic control.

### 3.1 Antigen structure

An antigen, denoted $A g$, is a disturbance associated with the whole intersection. A disturbance is an event (such as an accident, a jam or bad weather conditions) that affects the fluidity of the traffic. A disturbance can be represented as a vector of three attributes:

$$
\boldsymbol{A} \boldsymbol{g}=\left\langle\left\{\left(Q L_{i}, Q D_{i}\right)_{i}=1 \ldots n\right\} ; P\right\rangle
$$

where

- $Q L_{i}$ is the length (number of vehicles) of the vehicle queue at approach $i$, and $n$ is the number of approaches of the intersection. Approach notation and labelling are compliant with the National Electrical Manufacturers Association (NEMA) convention;
- $Q D_{i}$ is the average queue delay of vehicles at approach $i$. It represents the average amount of time, expressed in seconds, spent by vehicles waiting in the queue before leaving the intersection;
- $P$ is the period of the day in which the disturbance occurred (1 = rush hour; 0 = off-peak hour).

For example, consider the following antigen corresponding to an intersection with four approaches:

$$
\boldsymbol{A} \boldsymbol{g}=\left\langle\left\{(10,65)_{1},(8,170)_{2},(6,200)_{3},(7,60)_{4}\right\} ; 0\right\rangle
$$

This representation means that:

- Approach 1 has a queue length of 10 vehicles and an average queue delay of 65 s;
- Approach 2 has a queue length of 8 vehicles and an average queue delay of 170 s;
- Approach 3 has a queue length of 6 vehicles and an average queue delay of 200 s;
- Approach 4 has a queue length of 7 vehicles and an average queue delay of 60 s;
- The disturbance occurred in an off-peak hour.

The suggested antigen structure captures knowledge related to both space occupancy (represented by the queue length) and time occupancy of the disturbance (represented by the average queue delay and the period of the day). It is worth noting that antigens can be extended with other indicators related to other features that describe more exhaustively the state of each approach of an intersection. Antigens can be extended with other attributes to describe causes and context of occurrence of disturbances. Extensions can be made without questioning the downstream decision and control mechanisms, which contributes to ensure increased genericity.

### 3.2 Antibody structure

An antibody, denoted $A b$, represents a case with two parts: the pre-condition and the decision. The pre-condition has the same structure as the antigen and is used to activate the antibody. The decision is described by two attributes for each approach: the phase sequencing and the duration of each phase at each approach. The representation of an antibody is given by Eq. 3.

$$
\boldsymbol{A} \boldsymbol{b}=\left\langle\left\{\left(Q L_{i}, Q D_{i}\right)_{i=1 \ldots n}\right\} ;\left\{P ;\left\{\left(P h_{i}, D_{i}\right)_{i=1 \ldots n}\right\}\right\}\right\rangle
$$

where:

- $Q L_{i}, Q D_{i}$, and $P$ are the same attributes of an antigen characterizing a disturbance;
- $P h_{i}$ is the phase number (within the cycle) associated to approach $i$;
- $D_{i}$ is the duration (in seconds) of each phase of the cycle.

If the antibody associated to the antigen of Eq. 4 is represented by:

$$
\begin{aligned}
\boldsymbol{A} \boldsymbol{b}= & \left\{\left\{(10,65)_{1},(8,170)_{2},(6,200)_{3},(7,60)_{4}\right\} ; 0\right. \\
& \left.\left\{(3,30)_{1},(2,25)_{2},(1,15)_{3},(4,15)_{4}\right\}\right\rangle
\end{aligned}
$$

Then this representation means that:

- Approach 1 is assigned phase 3 with duration 30 s;
- Approach 2 is assigned phase 2 with duration 25 s;
- Approach 3 is assigned phase 1 with duration 15 s;
- Approach 4 is assigned phase 4 with duration 15 s.

This means that the adopted cycle has the following sequencing: phase $3 \rightarrow$ phase $2 \rightarrow$ phase $1 \rightarrow$ phase 4 with a total cycle duration of 85 s. It is worth noting that, in this article, we do not consider cycles with a fixed phase order. Both phase sequence and duration may be different from one situation to another.

### 3.3 Affinity between antibodies and antigens

The affinity between an antigen (detected disturbance) and an antibody (control decision) corresponds to the Manhattan distance (De Castro and Timmis 2002) (cf. Eq. 5). The Manhattan distance has demonstrated a better performance in presence of noisy data, which is often the case in transportation systems. This distance is expressed as the weighted sum of absolute values of differences between the values of the attributes of the detected disturbance and control decisions. To calculate this affinity, several weights (denoted $\alpha_{1}, \alpha_{2}$ and $\alpha_{3}$ ) are respectively associated with the queue length, average queue delay and the period of the day.

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-09.jpg?height=472&width=1191&top_left_y=190&top_left_x=167)
Fig. 2 The developed learning algorithm

$$
\begin{aligned}
& \text { Affinity }\left(\boldsymbol{A} \boldsymbol{b}_{\boldsymbol{i}}, \boldsymbol{A g}\right) \\
& \qquad=\alpha_{1} \cdot \sum_{i=0}^{n}\left(\left|Q L_{i}^{A b}-Q L_{i}^{A g}\right|\right)+\alpha_{2} \cdot \sum_{i=0}^{n}\left|Q D_{i}^{A b}-Q D_{i}^{A g}\right|+\alpha_{3} \cdot\left|P^{A b}-P^{A g}\right|
\end{aligned}
$$

where

- $\boldsymbol{Q} \boldsymbol{L}_{i}^{\boldsymbol{A} \boldsymbol{g}}$ is the length of the vehicle queue at approach $i$ for the detected antigen Ag
- $\boldsymbol{Q} \boldsymbol{L}_{\boldsymbol{i}}^{\boldsymbol{A} \boldsymbol{b}}$ is the length of the vehicle queue at approach $i$ of the stored antibody $A b$
- $\boldsymbol{Q} \boldsymbol{D}_{i}^{\boldsymbol{A} \boldsymbol{g}}$ is the average queue delay of vehicles at approach $i$ for the detected antigen Ag
- $\boldsymbol{Q} \boldsymbol{D}_{i}^{\boldsymbol{A} \boldsymbol{b}}$ is the average queue delay of vehicles at approach $i$ of the stored antibody $A b$
- $\boldsymbol{P}^{A g}$ is the period of the day at the intersection for the detected antigen Ag
- $\boldsymbol{P}^{\boldsymbol{A} \boldsymbol{b}}$ is the period of the day of the stored antibody $A b$

The weights used in Eq. 5 are determined using the choquet integral (Labreuche 2003; Marichal 2004; Diala et al. 2012) based on a quadratic program developped in (Bouhana et al. 2013) and implemented using Cplex, a powerful linear programming solver. The aim of this program is to minimize the distance between a new antigen and all other antigens.

### 3.4 A new learning mechanism for the creation of the immune memory

In this article, the immune memory corresponds to a database (case-base) with a set of antibodies that can neutralize abnormal traffic situations. To create such an immune memory, we developed a new learning algorithm including four steps (initialization, editing, refinement and evaluation) and combining different techniques, namely simulation-optimisation, Condensed Nearest Neighbour (CNN) algorithm and a rule-based system. Figure 2 illustrates the different steps of the algorithm, which are detailed in the next subsections.

### 3.4.1 Initialisation of the immune memory

Initially, the immune memory is empty. The objective of this step is to identify the most relevant abnormal traffic situations using simulation. Therefore, for each time slot $t$, the algorithm monitors the traffic status, denoted $T S_{i}$, by reading the traffic indicators (average queue length and average queue delay) from the simulation tool (cf. Sect. 4.1). The traffic situation is then evaluated using the function of Eq. 6.

```
Train ← the initial immune memory
Condensed ← ø
Reduced ← ø
Repeat
    Select the first antibody from the Train and add it to Condensed
    Reduced = Train - Condensed
    Repeat
        Select an antibody from Reduced
        Find the antibody representing the nearest neighbour in Condensed
        If the antibody of the nearest neighbour <> selected antibody (the affinity between the two anti-
        bodies < predefined threshold (th2)) then
            Add the selected antibody to Condensed
            Delete the selected antibody from Reduced
    Until Reduced is empty
    Reduced \(\boldsymbol{=}\) Train \(\boldsymbol{-}\) Condensed
Until there is no change in Condensed or Reduced during two successive iterations
```

Fig. 3 CNN algorithm

```
\(\boldsymbol{T} \boldsymbol{S}_{\boldsymbol{i}}=\left(w_{1} Q L_{i}+w_{2} Q D_{i}\right) ; \quad(i=1, \ldots, 4)\)
```

where

- $\boldsymbol{Q} \boldsymbol{L}_{\boldsymbol{i}}$ is the length of the queue of vehicles at approach $i$;
- $\boldsymbol{Q} \boldsymbol{D}_{\boldsymbol{i}}$ is the average queue delay at approach $i$;
- $\boldsymbol{w}_{\mathbf{1}}$ and $\boldsymbol{w}_{\mathbf{2}}$ are weights associated respectively to the vehicle queue length and the average queue delay at approach $i$. These weights are determined using Choquet integral as discussed in Sect. 3.3;
- $\boldsymbol{T} \boldsymbol{S}_{\boldsymbol{i}}$ is the traffic status attribute at approach $i$.

If the value of the function $\boldsymbol{T} \boldsymbol{S}_{\boldsymbol{i}}$ is greater than a predefined threshold (Th1), then, the situation is considered as abnormal. In this case, a new antibody is created, collected data are assigned to attributes of the antigen part of the created antibody (cf. Sect. 3.2), and the created antibody is added to the case-base. The threshold Th1 is determined using both trial and error and simulation optimization. At the end of simulation, we obtain $m$ antibodies, which have their antigen part filled and the control decisions empty.

### 3.4.2 Memory editing

The output of the previous step is an initial immune memory, which contains a big number of antibodies and some of them are similar. This step aims at editing the immune memory in order to delete redundant/similar antibodies, reduce its size and keep only representative antibodies. We adopted the condensed nearest neighbour (CNN) algorithm (cf. Fig. 3). The CNN is a technique that allows the pruning of a set of training examples to produce a compact edited set (Murty and Devi 2011; Smyth and McKenna 1999). It is widely used for pattern recognition and machine learning. In general, CNN is used in classification problems, regression tasks and case retrieval (Smyth and McKenna 1999). The performance of CNN was widely studied, and many works show that CNN produces an edited set of examples that is consistent with the original unedited training data (Coomans and Massart 1982; Guo et al. 2003). It is worth noting that to the best knowledge of the authors, this technique has not yet been applied to traffic signal control problems.

Through CNN, a single antibody is first put in a set named the condensed set. Then the memory is searched and the nearest neighbour in the condensed set is determined. The
most similar antibody from the condensed base (i.e. having a similarity of the antigen part exceeding a predefined threshold (th2) and the same control decision) will be deleted from the condensed base. Otherwise, the antibody is considered as representative and added to the condensed set. This step is repeated in an incremental way, by classifying each antibody from the initial immune memory using the condensed base. These iterations are carried out until no more antibodies are added to the condensed base.

### 3.4.3 Memory refinement

Two main objectives are considered in this step: assignment and improvement of control decisions. First, we assign control decisions to the set of antigens obtained after memory editing. This is achieved using a simulation-optimization technique and according to the linear program defined by Eqs. 7-10 below. For each antigen in the edited case base, the linear program finds a good combination $\left\{P h_{i}, D_{i}\right\}$ that minimizes the objective function of Eq. 7 under the constraints presented in Eqs. 8, 9 and 10.

$$
\operatorname{Min}\left(W_{T D} A v g T D+W_{Q L} A v g Q L+W_{V S} A v g V S\right)
$$

Such that

$$
\begin{aligned}
& D_{i} \in \mathrm{D} ; \\
& D^{\operatorname{Min}} \leq \sum_{i=0}^{n} D_{i} \leq D^{\operatorname{Max}} \\
& P h_{i} \in P h ;
\end{aligned}
$$

where

- $\boldsymbol{D}$ is the set of possible durations of different phases
- $\boldsymbol{D}^{\text {Min }}$ is the minimum cycle time and $\boldsymbol{D}^{\text {Max }}$ is the maximum cycle time
- Ph is the set of possible phase sequences
- $\boldsymbol{W}_{\text {TD }}$ is the weight associated to the average total delay per vehicle;
- $\boldsymbol{W}_{\boldsymbol{Q} \boldsymbol{L}}$ is the weight associated to the average queue length for the intersection;
- $\boldsymbol{W}_{\boldsymbol{V} \boldsymbol{S}}$ is the weight associated to the average number of stops per vehicle;

The objective function of Eq. 7 is an aggregation of the average total delay per vehicle (AvgTD) for the intersection, the average queue length for the intersection $(A v g Q L)$ and the average number of vehicle stops (AvgVS) for the intersection. The constraint given by Eq. 8 defines a set $D$ of possible values of phase durations $D_{i}$. The constraint given by Eq. 9 specifies the maximum and minimum possible cycle times. The constraint given by Eq. 10 defines a set $P h$ of possible phase sequences. This formulation has the advantage to comply with local regulations, where transportation authorities usually have an established organization and prevailing management policy for signalized intersections in the considered urban areas. Such a policy usually includes a set of possible phase sequences and durations that should be respected to have a homogeneous control strategy over the controlled urban areas. In our particular case, phase sequences, durations, and cycle times will be fixed in section 4.4 based on expert recommendations and in compliance with local regulation. The problem is implemented and solved using Cplex, a powerful solver for linear programming problems.

The second objective of memory refinement is to refine the obtained decisions. As depicted in Fig. 4, this step uses a rule-based system to update the control decisions. The system takes as input the edited memory and complementary information about the traffic, such as fluctuations (changes) of traffic volumes.

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-12.jpg?height=301&width=795&top_left_y=190&top_left_x=367)
Fig. 4 The rule based system for the memory refinement

A set of IF...THEN rules is used to apply some basic and elementary actions on the duration $D_{i}$ or the phase sequencing $P h_{i}$ of each antibody stored in the memory. These elementary actions can be:

- Increase phase duration by $s$ seconds;
- Decrease the phase duration by $s$ seconds;
- Switch phases (phase $i$, phase $j$ ).

The rules used for the refinement step have the following structure:
IF an approach has high traffic density
THEN increase phase duration by s second
IF an approach is blocked by an accident for a short duration
THEN switch phases by given this approach the priority

The output of this system is a refined memory.

### 3.4.4 Memory evaluation

The objective of this step is to evaluate the efficiency of the memory and compare it to the performance of the reference algorithm, which is the LQF-MWM (Wunderlich et al. 2007, 2008) (cf. Sect. 4.3). We considered the average total delay as performance indicator. We used the simulation model developed in step 1. If the LQF-MWM performs better than the suggested Immune Memory based Algorithm (IMA), then we loop back to memory refinement. Otherwise, the obtained immune memory is considered as final.

### 3.5 Immune memory based traffic control algorithm and architecture

The suggested Immune Memory based Algorithm (IMA) works according to the following steps:

- Step 1 Data collection: the control algorithm performs data acquisition from the controlled intersection. A simulation software is used to simulate an intersection and collect data (cf. Sect. 4). Collected data are related to both the average delay and queue length of vehicles in each approach.
- Step 2 Data analysis: the algorithm analyzes collected data in order to detect possible disturbances. The system evaluates the traffic situation with respect to the evaluation function $T S_{i}$ of the Eq. 6. Two possible sub-steps are considered. The first one is related to the activation of the fixed time control or the activation of the suitable control decision:
```
Ag ← ø
Initialisation: load the immune memory, th1
Repeat
    For each T time
        For each approach
            Measure the traffic status ( \(L_{i}, Q D_{i}, P\) )
            Calculate \(T S_{i}\) using Equation 6
            If \(T S_{i}>t h 1\) then
                \(\boldsymbol{A} \boldsymbol{g} \leftarrow\) new antigen object
                Evaluate the new antigen with respect to the antibodies stored in the
                    immune memory using Equation 5
                Select the antibody representing the highest degree of affinity
                Apply the control decision given by the selected antibody ( \(P h_{i}, D_{i}\) )
            Else
            Activate the fixed-time controller
            EndIf
        EndFor
    EndFor
Until (end of the simulation)
```

Fig. 5 IMA algorithm

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-13.jpg?height=285&width=1189&top_left_y=919&top_left_x=167)
Fig. 6 Control architecture


- Step 2.1 this step is activated if the value $T S_{i}$ is less than th1. In this case, no disturbances are detected. Consequently, the algorithm activates the fixed time controller with 60 s cycle time, 15 s for each phase and phase sequencing $p h_{1} \rightarrow p h_{2} \rightarrow$ $p h_{3} \rightarrow p h_{4}$. Then, go to step 1 for data acquisition.
- Step 2.2 this step is activated if the value $T S_{i}$ is greater than th1. The algorithm detects a disturbance and creates an antigen object (Eq. 1) with collected data. Then, go to step 3 to select the appropriate control decision.
- Step 3 Selection of the appropriate control decision: the algorithm selects from the memory the most appropriate antibody (control decision) that can deal with the disturbance (antigen). For that, the algorithm determines the affinity between the detected disturbance (antigen) and all control decisions (antibodies) from the database (cf. Sect. 3.3). The algorithm selects the control decision with the highest value of affinity.
- Step 4 The selected control decision is applied to the controlled intersection. Go to step 1 for data acquisition.

Steps 1-4 are repeated each T (sampling period) seconds.
Figure 5 presents the structure of the suggested algorithm.
The suggested Immune Memory based Algorithm (IMA) will be used within the control architecture of Fig. 6.

In this article, it is worth noting that (cf. Sect. 4.1 for more details):

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-14.jpg?height=672&width=799&top_left_y=190&top_left_x=365)
Fig. 7 The simulated intersection

- The controlled intersection is a simulated one;
- Data acquisition is performed using an application-programming interface (API) associated with the traffic simulation software we use;
- Data acquisition is performed in the beginning of a sampling period, while the determined control decision is applied at the beginning of next sampling period.

## 4 Experimentation framework

In this section, we describe the experimentation settings, the two algorithms against which our suggested IMA algorithm will be compared (namely a fixed time controller and the LQF-MWM algorithm) and the obtained immune memory after the application of the suggested learning mechanism.

### 4.1 Intersection configuration, implementation and performance indicators

We have applied the algorithms on a single signalized intersection with four phases (cf. Fig. 7). Vehicles in each approach can cross the intersection based on the related green time and direction of the phases. The intersection contains four approaches, each one is 400 meters long (Wunderlich et al. 2007, 2008). Each approach has two lanes, one for turning right and the other one is a shared lane for straight and turning left movements. The intersection is simulated using PTV VISSIM 7 (Fellendorf and Vortisch 2010; PTV 2015). The suggested algorithm and the LQF-MWM algorithm are implemented using Python 2.7.9. Data is collected from PTV VISSIM 7 each 3 s.

The performance of the three controllers was assessed under the following four different scenarios:

1. Scenario 1 with 4800 generated vehicles during off-peak hour $(\mathrm{P}=0)$. The aim of this scenario is to assess performance under "normal" traffic conditions and low traffic density.

2. Scenario 2 with 7200 generated vehicles during rush hour $(\mathrm{P}=1)$. The aim of this scenario is to assess performance with a high-density traffic flow.
3. Scenario 3 with 4800 generated vehicles during off-peak hour $(\mathrm{P}=0)$. In this scenario, we simulated an accident in one approach of the intersection, which blocked the traffic during the first 200 simulation seconds.
4. Scenario 4 with 7200 generated vehicles during rush hour $(\mathrm{P}=1)$ and three blocked approaches, due to accidents during the first 20 min of simulation.

Each scenario has a duration of 40 min. It is important to note that the scenarios used for the assessment of the suggested system are different from the scenarios used in the learning phase (cf. Sect. 3.4). To evaluate the performance of the three algorithms, a set of performance indicators are considered as follows:

1. The total delay in the intersection: represents the total time spent by all vehicles in the intersection. Such time includes the average queue delay of vehicles and time taken by vehicles to leave the intersection. Such criteria provide an overview of the global performance of the controllers in the different scenarios.
2. The average total delay per vehicle for each approach: refers to the mean delay of a vehicle to cross the intersection. Since the performance of IMA and LQF-MWM are very close to each other, we decided to use Log(delay[sec]) in order to better distinguish the performance of each algorithm.
3. The average queue length.
4. The average vehicle stops.

It should be noted that the two indicators vehicle stops and queue length play an important role as they represent a direct measure of the level of service at the intersection, and an indirect measure of sustainability criteria, such as the fuel consumption and air pollution.

Moreover, the different thresholds, weights, and the obtained immune memory used are as follows:

- $\alpha_{1}=0.5$;
- $\alpha_{2}=0.3$;
- $\alpha_{3}=0.2$;
- $w_{1}=0.5$
- $w_{2}=0.3$
- $W_{T D}=0.3$;
- $W_{Q L}=0.5$;
- $W_{V S}=0.2$;
- $T h_{1}=12$;
- $T h_{2}=200$;

### 4.2 Fixed-time controller

In a fixed-time controller, the same sequence of phases is repeated with a fixed duration, always arranged in the same order, to have a fixed cycle. In this work, we used the "Optimized Stage-Based Fixed-Time controller", a tool of PTV VISSIM that allows the determination of the optimal duration of different phases of a cycle. As input, this tool requires only the desired cycle time. In this paper, we have considered two different cycle times. The first cycle time is 120 s, which is used in (Chen et al. 2013), and the second cycle time is 240 s, which is used in (Araghi et al. 2015). Both, Chen et al. (2013) and Araghi et al. (2015) used an isolated intersection with four approaching links for the assessment task. As output, VISSIM
suggests an optimized phase duration for each approach. The obtained phase durations by VISSIM are as follows:

- The fixed time controller with a total cycle time of 120 s: 25 s for each phase with 5 s of inter-green;
- The fixed time controller with a total cycle time of 240 s: 55 s for each phase with 5 s of inter-green.

### 4.3 LQF-MWM algorithm

For a comparative assessment of the performance of the developed IMA system, we considered the longest queue first-maximal weight matching (LQF-MWM) algorithm as a reference algorithm (Wunderlich et al. 2007, 2008). LQF-MWM dynamically adapts the duration of each phase based on the traffic status. The algorithm favours approaches with the longest vehicle queues. It allocates green light to the phase with the longest waiting time. According to Wunderlich et al. (2007), the queue length at each lane of an isolated intersection is directly proportional to the delay experienced by the vehicles in the lane. Thus, to minimize the vehicle delays, the authors focused on minimizing the queue lengths. The suggested algorithm collects data from the network each k-time slots, where k is defined by human controllers. The authors consider only a single type of vehicle, and all vehicles are treated uniformly (no priority of a type of vehicles, e.g. trucks, over another type, e.g. cars). In Wunderlich et al. (2008), the authors noted that LQF-MWM provides better results than a fixed time controller on two tested scenarios. The authors did not compare their algorithm to another adaptive controller. Ahmad et al. (2014) stated that the LQF-MWM is an adaptive traffic control algorithm that tends to reduce the average delay of vehicles through isolated intersections by making all queues stable. Wu et al. (2011) noticed that LQF-MWM shows good performance compared to other approaches like the Ant Colony System (ACS), or the First Come First Serve policy (FCFS). It is worth noting that the LQF-MWM algorithm is increasingly used for benchmarking purposes by a number of recent references (Ahmad et al. 2014; Chen et al. 2013; Wu et al. 2011), and that is why we are referring to it for a comparative assessment of the performance of the developed IMA system.

There are fundamental differences between our suggested IMA algorithm and LQF-MWM. The first relates to the criteria considered for the detection of disturbances. LQF-MWM uses only the queue length while our algorithm uses both the queue length and average queue delay for the detection of disturbances. The second relates to the control decisions. LQF-MWM acts only on phase sequencing, while our algorithm acts on both phase sequencing and duration. Finally, unlike the LQF-MWM algorithm, we introduced a disturbance and control decision models and a case-base to facilitate the capture and reuse of knowledge related to disturbances.

### 4.4 Creation of the immune memory

To instantiate our linear program presented in Sect. 3.4, we consider the following settings:

- Minimum cycle time $D^{\text {Min }}=60 \mathrm{~s}$;
- Maximum cycle time $D^{\text {Max }}=380 \mathrm{~s}$;
- The set of possible phase durations is $D=\{12,15,20,30,45,60,120\} s$.
- Only 6 sequences of phases are considered
- $P h=\{\{1,2,3,4\} ;\{1,3,4,2\} ;\{2,1,4,3\} ;\{3,2,4,1\} ;\{4,1,3,2\} ;\{4,3,2,1\}\}$

Phase durations, sequences and cycle times were fixed based on recommendations of experts in traffic engineering from local transportation authorities, and based on local regulations that tend to standardize durations in all signalized intersections of the controlled urban area. Considering these regulation restrictions, we checked these recommendations using simulation and were able to confirm that they provide satisfactory results for the considered intersection.

To create the immune memory, a scenario with total duration of 120 min is designed, made of four sub-scenarios, each one has a duration of 30 min . The first sub-scenario simulates a low traffic density with different volumes starting from 500 vehicles/approach to 1000 vehicles/approach. In the second sub-scenario, the traffic density is increased to reach 2000 vehicles/approach. In the third sub-scenario, some approaches are blocked during a short period with low density. Finally, in the fourth sub-scenario, some approaches are blocked during long periods and with a high density. The obtained immune memory includes 16 antibodies that are presented in Fig. 8.

The result of the first step of the suggested learning algorithm presented in Sect. 3.4 includes 25,601 antigens represented in Fig. 9 by blue points. These antigens are the set of all detected antigens. After editing and reducing the size of the immune memory using the step 2, we obtained 16 representative antibodies highlited by different colored points. From Fig. 9, we note that the antibodies are well distributed and cover the densiest regions of the antigen space. However, it is important to emphasize that a larger simulation and an additional indepth statistical analysis (e.g. Design of Experiment) are required to assess the coverage and representativity of the obtained antibodies, and to obtain an immune memory with optimal size and coverage, which is out of the scope of this article.

## 5 Experimental results

In this section, the obtained results for the four scenarios are discussed and compared based on the four performance indicators. Figure 10 and Table 2 show the average total delay per vehicle (expressed in seconds) for all scenarios and for all control algorithms. We notice that IMA has better performance than both fixed time and LQF-MWM controllers with respect to the average total delay in all scenarios.

- For scenario 1, IMA reduced the average total delay by 16.6\%, 24.8 and 29.5\% compared to LQF-MWM and the two Fixed-Time controllers (120 and 240 s), respectively.
- In the second scenario (characterized by a high density but without accidents), the performance of the two algorithms (IMA and LQF-MWM) are similar. IMA reduced the average total delay by 8.86\%. It was reduced by 18.7 and 21.6\% compared to Fixed-Time controllers, 120 and 240 s respectively. This result shows that IMA gives better results, with respect to the average total delay per vehicle, in both normal and disturbed situations. Fixed-time strategy gives always the highest delays due to its static and fixed time duration and phase sequencing.
- In scenario 3, IMA reduced the average total delay by 31.8, 40.2 and 41.7\% compared to LQF-MWM and the two Fixed-Time controllers (120 and 240 s), respectively.
- Finally in scenario 4, IMA reduced the average total delay by 5.07, 16.4 and 17.9\% compared to LQF-MWM and the two Fixed-Time controllers (120 and 240 s), respectively.

In the following subsections, we will discuss the performance of the algorithms for each scenario with respect to different performance indicators.

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-18.jpg?height=1675&width=1195&top_left_y=186&top_left_x=166)
Fig. 8 Final immune memory

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-19.jpg?height=540&width=1194&top_left_y=188&top_left_x=164)
Fig. 8 continued

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-19.jpg?height=721&width=1193&top_left_y=820&top_left_x=166)
Fig. 9 Obtained immune memory coverage

### 5.1 Scenario 1

In this scenario, we simulate a low flow of vehicles without considering any type of disturbance. Figure 11 illustrates the total delay of vehicles at the intersection. It can be noted that the fixed-time control provides better results at the beginning of the simulation, during which there is a very low density of vehicles. LQF-MWM and IMA have a similar performance. However, after 10 min, the performance of IMA is clearly better.

According to Fig. 12, it can be noticed that the performance of both algorithms is similar regarding the average queue length for each approach. Indeed, in approach 1 and 4, IMA is better but in the two other approaches, LQF-MWM is the best. This can be explained by the fact that our algorithm gives priority to approaches with the longer queue and/or higher average queues delays while LQF-MWM gives priority only to longer queue.

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-20.jpg?height=609&width=992&top_left_y=192&top_left_x=266)
Fig. 10 Average total delay per vehicle for 40 min simulation

Table 2 Performance of algorithms
| Method | Scenario 1 | Rank | Scenario 2 | Rank | Scenario 3 | Rank | Scenario 4 | Rank |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Suggested algorithm | 223.003 | 1 | 267.747 | 1 | 188.3 | 1 | 495.889 | 1 |
| LQF-MWM | 267.665 | 2 | 293.805 | 2 | 276.107 | 2 | 552.4 | 2 |
| Fixed-time (120s) | 297.712 | 3 | 329.682 | 3 | 315.1 | 3 | 593.403 | 3 |
| Fixed-time (240 s) | 316.437 | 4 | 341.937 | 4 | 323.171 | 4 | 604.506 | 4 |


![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-20.jpg?height=694&width=1185&top_left_y=1250&top_left_x=170)
Fig. 11 Total delay for the intersection for the scenario 1

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-21.jpg?height=595&width=992&top_left_y=192&top_left_x=266)
Fig. 12 Average queue lengths for the scenario 1

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-21.jpg?height=643&width=997&top_left_y=947&top_left_x=264)
Fig. 13 Average stops per vehicle for scenario 1

The last studied performance deals with the vehicle stops. Figure 13 presents the average vehicle stops per vehicle. In this scenario, a vehicle has to stop around 3 times to cross the intersection with the optimal fixed time with a total cycle time of 240s, while vehicles have to stop around 5 times with the second optimal cycle time (120 s). Vehicles has to stop between 2 and 6 times with the suggested algorithm. Finally, LQF-MWM performs better regarding this performance indicator as vehicles have to stop two times or less to leave the intersection.

Regarding this analysis, we can conclude that both LQF-MWM and the optimal fixed time strategy with a total cycle time of 240 s have comparable performance in low traffic density. Both can be used for the control of the traffic in such situation.

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-22.jpg?height=690&width=1194&top_left_y=188&top_left_x=164)
Fig. 14 Total delay for the intersection for the scenario 2

### 5.2 Scenario 2

In this scenario, we increase the traffic density to simulate traffic congestion and test the ability of the three control methods to maintain the fluidity of the traffic. The number of generated vehicles is 7200 and every approach has 1800 generated vehicles. The obtained results are illustrated in Figs. 14, 15 and 16. The optimal fixed time strategy with the total cycle time of 120 s has not shown good performance compared to the other control strategies. With respect to the total delay (Fig. 14), IMA performs slightly better than LQF-MWM as it takes the average queue delay into consideration when determining the appropriate phases duration and sequencing. The LQF-MWM gives priority only to approaches with a greater number of waiting vehicles

With the increase in traffic volume, we observe an increase in queue sizes for the three controllers (cf. Fig. 15). Despite this increase, IMA and LQF-MWM have comparable performances as the average queue length is lower in approaches 1 and 4 with the developed algorithm and while it is lower with LQF-MWM in approaches 2 and 3. Both fixed time strategies have bad performance with regards to the average queue length.

Regarding the average vehicle stops, Fig. 16 illustrates that LQF-MWM and the optimal fixed time with the cycle time of 240s have similar performance as the average of vehicle stops is less or equal than 3 times while it is more than 7 in some approaches with IMA and the second fixed time control. This can be explained by the fact that LQF-MWM continues increasing the duration of the phase associated to the approach with the longer vehicle queue until the queue length becomes lower than a fixed threshold or another approach will have longer queue length.

### 5.3 Scenario 3

In this scenario, we simulate three blocked approaches of the intersections (1, 3 and 4) during 200 s due to, for example, an accident. During the occurrence of the accident, the number

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-23.jpg?height=647&width=999&top_left_y=186&top_left_x=262)
Fig. 15 Average queue lengths for scenario 2

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-23.jpg?height=641&width=996&top_left_y=932&top_left_x=264)
Fig. 16 Average stops per vehicle for scenario 2

of the generated vehicles is 1200 for approach 1 and 500 generated vehicles for the other approaches. After this period, the traffic volume becomes 1200 vehicles for each approach. Regarding the total delay, Fig. 17 reveals that the developed algorithm performs better than other control strategies. During the disturbance, fixed-time and LQF-MWM have comparable performance as approaches 1, 3 and 4 are blocked and no vehicles can across the intersection during 200 s . After 200 s, disturbed approaches have a greater congestion as vehicles were blocked. In such situations, IMA performs better than the other strategies.

IMA performs better than LQF-MWM regarding the queue length as illustrated in Fig. 18. Despite the accident and the congestion in approaches 1, 3 and 4, the developed algorithm has the ability to maintain the queue length at acceptable level. The four algorithms had comparable performces in the non disurbed approach (approach 2).

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-24.jpg?height=698&width=1187&top_left_y=192&top_left_x=168)
Fig. 17 Total delay for the intersection for scenario 3

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-24.jpg?height=647&width=997&top_left_y=979&top_left_x=264)
Fig. 18 Average queue lengths for scenario 3

Finally, Fig. 19 illustrates that the two algorithms (IMA and LQF-MWM) have the same performance as LQF-MWM is better in approaches 2 and 3 while IMA is better in the two other approaches. It is also clear that the fixed time strategy, especially the one with a total cycle time of 120s, is not able to deal with abnormal situations as the average vehicle stops is more than 4 times.

### 5.4 Scenario 4

In this scenario, we simulate an extreme disturbed situation in which three approaches (approaches 1,3 and 4) are blocked during 20 min, for example due to an accident. The

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-25.jpg?height=643&width=997&top_left_y=186&top_left_x=264)
Fig. 19 Average stops per vehicle for scenario 3

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-25.jpg?height=473&width=813&top_left_y=918&top_left_x=354)
Fig. 20 Total delay for the intersection for scenario 4

number of generated vehicles in these approaches is also high as it was 1800 vehicles. The number of generated vehicles in the non-disturbed approach (approach 2 ) is 500 vehicles. The number of generated vehicles in intersection during the simulation is 7200 vehicles. According to the Fig. 20, the performance of the two fixed time strategies was better than the two other algorithms during the first period of the disturbance (during the first 10 min) due to the low number of generated vehicles during this period. However, the developed algorithm shows better performance during the remainder of the simulation regarding the total delay.

IMA performs better also with respect to the two other performance indicators: the average queues length (Fig. 21) and the average vehicle stops (Fig. 22). Indeed, the average queue length as well as the average vehicle stops of the four approaches is lower with IMA than fixed-time strategy and LQF-MWM.

### 5.5 Discussion of results

Table 3 summaries the obtained results for the studied scenarios. It can be noticed that both IMA and LQF-MWM can be used for the management of traffic at low or medium

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-26.jpg?height=640&width=997&top_left_y=186&top_left_x=264)
Fig. 21 Average queue lengths for scenario 4

![](https://cdn.mathpix.com/cropped/4b9ce602-8e00-4cf9-8bc9-8680fed13713-26.jpg?height=643&width=996&top_left_y=947&top_left_x=266)
Fig. 22 Average stops per vehicle for scenario 4

traffic densities. IMA should be considered if transportation authorities are more interested in reducing delays. In addition, in more complex situations, such as accidents with an acceptable level of fluidity, IMA performs better than fixed time and LQF-MWM regarding delays and queue lengths. In such situations, LQF-MWM has better performance with respect to the number of vehicle stops. Finally, IMA is recommended for extreme situations, such as blocked approaches and in cases of high traffic flows.

However, IMA does not perform better than the other algorithms with respect to vehicle stops. This can be explained by the fact that the detection of disturbances does not explicitly include vehicle stops. Moreover, we can notice that the performance of IMA is better in approaches 1 and 4 than in approaches 2 and 3. This can be explained by the fact that

Table 3 Comparative analysis
| Performance indicator | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 |
| :--- | :--- | :--- | :--- | :--- |
| Delay | IMA | IMA | IMA | IMA |
| Queue length | IMA/LQF-MWM | IMA/LQF-MWM | IMA | IMA |
| Vehicle stops | LQF-MWM/fixedtime (240s) | LQF-MWM/fixedtime (240 s) | LQF-MWM/fixedtime (240 s) | IMA |
| Recommended | IMA/LQF-MWM | IMA/LQF-MWM | IMA | IMA |


antibodies resulting from the CNN based memory editing give more priority to vehicles coming from approaches 1 and 4 in terms of both phase order and duration.

In addition to the in-depth analysis of the performance of algorithms, this paper demonstrated that it is very important to consider many performance indicators for assessing the performance of control strategies. Indeed, a majority of published research papers (Wunderlich et al. 2007) limit their assessment to the queue length considering that other indicators will be evaluated in the same way, which is not always true.

## 6 Discussion

The main contribution of this article is to develop new concepts and mechanisms borrowed from the biological immune memory and secondary immune response to control traffic at a single signalized intersection. Immune concepts and mechanisms were matched with representation and coding analogies, case based reasoning, and CNN based learning. Several important research directions can be drawn from this research in order to enhance what we can do to control traffic at signalized intersections based on artificial immunity:

- The suggested approach is based on two separate phases, a learning phase to create the case base and a control phase that uses those cases to control traffic. The main advantages of this design choice are that the learning phase contributes to an intelligent sampling of the disturbance and the control decision spaces. The learning phase allows creating a concise case base that is compliant with the technological limitations of realworld signalized intersections, which are usually controlled using programmable logic controllers (PLCs) with limited storage and computing capabilities. However, this design choice has some coverage limitations, mainly due to the fact that not all disturbance cases are stored. As a consequence, the distance between a detected disturbance and retrieved cases may be important. One way to consider this limitation consists in developing a continuous learning approach, able to detect and adapt cases to new situations without any separation between learning and control phases. Continuous learning enables continuous creation, replacement, and removal of antibodies based on their performance. However, continuous learning requires more investigation, and exploration of additional immune mechanisms, such as the clonal selection theory (Ulutaş and Kulturel-Konak 2011), and the immune network theory (Raza and Fernandez 2015), to insure the scalability of the case-base and its compatibility with real-world implementation constraints and requirements.

- As a corollary of the previous remark, the separation into two different stages raises questions about the coverage of the suggested case-base. Although several references in the literature emphasize the ability of the CNN algorithm to obtain case-bases with good coverage (Althoff et al. 1999; Leake and Wilson 2000), an in-depth statistical analysis of the obtained immune memory is required to insure its coverage. Moreover, other classification algorithms, such as the k-NN, can be used for the memory editing;
- The detection of disturbances was based on average queue lengths and average queue delays. More indicators can be considered to detect disturbances without loss of genericity. The detection of disturbances can also be enhanced by integrating other artificial intelligence techniques, such as data mining, clustering and classification. Fuzzy set theory can also be considered to cope with uncertainties.
- The suggested immune memory based algorithm (IMA) uses a similiarity measure to retrieve antibodies. The similarity measure is based on the Manhattan distance, which has demonstrated a good performance in presence of noisy data as discussed in Sect. 3.3. However, other operators can be used, such as the generalized ordered weighted averaging (GOWA, Yager 2004) operator. GOWA is an aggregation method for aggregating criterias. It provides a parameterized family of operators that includes the maximum, the minimum and the average criteria.In future works, the performance of the algorithm using the manhattan distance and GOWA operator can be compared.

## 7 Conclusion

Controlling traffic at signalized intersections, especially in the presence of disturbances, is a complex and open-ended problem, for which several intelligent and adaptive control systems were developed. However, there is still a lack of approaches that provide concepts and mechanisms that are generic enough to deal with a variety of disturbances while maintaining traffic fluidity. This article provides an intelligent and adaptive traffic signal control system (TSCS) that adapts traffic signals (both phase sequencing and duration) to traffic disturbances at a single signalized intersection. The suggested approach and developed system contribute both to artificial immune systems (AIS) and to case-based reasoning (CBR).

With respect to AIS, our article provides a novel analogy, based on the immune memory and secondary response, innovative implementation choices and techniques, as well as a detailed comparative analysis of performance against two control strategies, namely a fixed time control strategy, and LQF-MWM algorithm. Immune memory provides the concepts to represent cases to deal with disturbances in a more generic way, and immune secondary response mechanisms guide the design of a CBR system to monitor traffic and control disturbances.

With respect to CBR, our article described a hybrid methodology to create the case-base using simulation-optimisation, Condensed Nearest Neighbour algorithm (CNN) and a rulebased system. It is worth noting that despite the widespread use of CNN in other CBR domain applications, the suggested approach is among the first to apply it in a traffic signal control problem.

The suggested approach and developed system implement biological immunity inspired concepts, and rely on explicit and direct representation and mechanisms that allow more generic disturbance handling. In fact, the representation used allows integrating more indicators to enrich the description of disturbances with more features, and allows integrating more attributes that add complementary knowledge about disturbances (such as causes or
context of occurrence of disturbances), without questioning the downstream decision and reaction mechanisms. The suggested TSCS was tested on different traffic situations and disturbed scenarios. Different Key Performance Indicators (KPIs) were considered and used in the analysis. The comparative assessment results show that for normal or slightly disturbed traffic, the suggested TSCS and LQF-MWM have comparable performance. However, in case of extreme situations, the suggested TSCS outperforms the other two control strategies.

The suggested TSCS can be extended in several ways in future works. For example, a more formal classification of disturbances can be considered through clustering and data mining techniques. The system can be coupled to an ontology to handle this classification. Reasoners and inferencing can be used to enhance decision-making. In addition, the system can be extended using other concepts and mechanisms inspired by biological immunity. For example, the immune network theory can inspire mechanisms for multi-criteria decision-making to select a case among several candidate cases. The clonal selection theory provides optimization mechanisms that can improve the performance of antibodies and their sensitivity to abnormal traffic situations and disturbances. Finally, the concepts and mechanisms provided can be extended to cover a network of several signalized intersections.

Acknowledgements This project was funded by the Deanship of Scientific Research at King Saud University through research Group No. (RG-1438-056).

## References

Ahmad A, Arshad R, Mahmud SA, Khan GM, Al-Raweshidy HS (2014) Earliest-deadline-based scheduling to reduce urban traffic congestion. IEEE Trans Intell Transp Syst 15(4):1510-1526. https://doi.org/10. 1109/TITS.2014.2300693
Althoff K-D, Branting L, Bergmann R (1999) Case-based reasoning research and development. Springer, Berlin, London
Angulo E, Romero FP, García R, Serrano-Guerrero J, Olivas JA (2011) An adaptive approach to enhanced traffic signal optimization by using soft-computing techniques. Expert Syst Appl 38(3):2235-2247. https://doi. org/10.1016/j.eswa.2010.08.011
Araghi S, Khosravi A, Creighton D (2015) A review on computational intelligence methods for controlling traffic signal timing. Expert Syst Appl 42(3):1538-1550. https://doi.org/10.1016/j.eswa.2014.09.003
Bellemans T, Schutter B, De Moor B (2002) Model predictive control with repeated model fitting for ramp metering. In: Proceedings of the IEEE 5th international conference on intelligent transportation systems, vol 19, pp 236-241. https://doi.org/10.1109/ITSC.2002.1041221
Boillot F, Blosseville JM, Lesort JB, Motyka V, Papageorgiou M, Sellam S (1992) Optimal signal control of urban traffic networks. In: 6th IEE international conference on road traffic monitoring and control, IET. http://ieeexplore.ieee.org/articleDetails.jsp?arnumber=363749
Bouhana A, Fekih A, Abed M, Chabchoub H (2013) An integrated case-based reasoning approach for personalized itinerary search in multimodal transportation systems. Transp Res C Emerg Technol 31:30-50. https://doi.org/10.1016/j.trc.2013.02.014
Chang ECP, Lei JCK, Messer CJ (1988) Arterial signal timing optimization using PASSER-II-87. ITE J 467:27-31
Chen L-W, Sharma P, Tseng Y-C (2013) Dynamic traffic control with fairness and throughput optimization using vehicular communications. IEEE J Sel Areas Commun 31(9):504-512. https://doi.org/10.1109/ JSAC.2013.SUP. 0513045
Coomans D, Massart DL (1982) Alternative k-nearest neighbour rules in supervised pattern recognition. Anal Chim Acta 138:167-176. https://doi.org/10.1016/S0003-2670(01)85299-5
Darmoul S, Elkosantini S (2014) Artificial immunity to control disturbances in public transportation systems: concepts, mechanisms and a prototype implementation of a knowledge based decision support system. Knowl Based Syst. https://doi.org/10.1016/j.knosys.2014.02.022
De Castro LN, Von Zuben FJ (1999) Artificial immune systems: part 1-basic theory and applications, vol 19. Springer. http://eva.evannai.inf.uc3m.es/docencia/doctorado/cib/documentacion/OverviewIS.pdf

De Castro LN, Timmis J (2002) Artificial immune systems: a new computational intelligence approach. Springer, London
De Schutter B, Hoogendoorn SP, Schuurman H, Stramigioli S (2003) A multi-agent case-based traffic control scenario evaluation system. In: Proceedings of the 2003 IEEE international conference on intelligent transportation systems, vol 1. IEEE, pp 678-683. https://doi.org/10.1109/ITSC.2003.1252037
Diala D, Sid-Ali A, Abderrahman EM, Habib C (2012) A dynamic multi-criteria aid for process driving using case-based reasoning. J Decis Syst 18:459-484
Elkosantini S, Mnif S, Chabchoub H (2011a) A system for the traffic control in signposted junctions. In: Proceedings of the 2011 IEEE symposium on computational intelligence in vehicles and transportation systems (CIVTS). IEEE, pp 52-58. https://doi.org/10.1109/CIVTS.2011.5949528
Elkosantini S, Mnif S, Chabchoub H (2011b) An urban traffic controller for signposted road-rail intersections. In: 2011 4th international conference on logistics. IEEE, pp 13-18. https://doi.org/10.1109/LOGISTIQUA. 2011.5939396
Fellendorf M, Vortisch P (2010) Microscopic traffic flow simulator VISSIM. In: Barceló J (ed) Fundamentals of traffic simulation. Springer, New York, pp 63-93. https://doi.org/10.1007/978-1-4419-6142-6
Guo G, Wang H, Bell D, Bi Y, Greer K (2003) KNN model-based approach in classification. In: Meersman R, Tari Z, Schmidt DC (eds) On the move to meaningful internet systems 2003: CoopIS, DOA, and ODBASE. Springer, Berlin, pp 986-996. https://doi.org/10.1007/978-3-540-39964-3_62
Henry JJ, Farges J-L, Tuffal J (1984) The PRODYN real time traffic algorithm. In: IFAC/IFIP/IFORS conference on control in transportation systems. Baden-Baden, Germany, pp 305-310. http://trid.trb.org/view. aspx?id=339694
Hofmeyr SA (2001) An interpretative introduction to the immune system. In: Segel LA, Cohen IR (eds) Design principles for the immune system and other distributed autonomous systems. Oxford University Press, New York, pp 3-28
Karim A, Adeli H (2003) CBR model for freeway work zone traffic management. J Transp Eng. https://doi. org/10.1061/(ASCE)0733-947X(2003)129:2(134)
Kosonen I (2003) Multi-agent fuzzy signal control based on real-time simulation. Transp Res C Emerg Technol 11(5):389-403. https://doi.org/10.1016/S0968-090X(03)00032-9
Labreuche C (2003) The Choquet integral for the aggregation of interval scales in multicriteria decision making. Fuzzy Sets Syst 137(1):11-26. https://doi.org/10.1016/S0165-0114(02)00429-3
Leake DB, Wilson DC (2000) Remembering why to remember: performance-guided case-base maintenance (pp. 161-172). Springer, Berlin, Heidelberg. https://doi.org/10.1007/3-540-44527-7_15
Li J-Q (2011) Discretization modeling, integer programming formulations and dynamic programming algorithms for robust traffic signal timing. Transp Res C Emerg Technol 19(4):708-719. https://doi.org/10. 1016/j.trc.2010.12.009
Little JDC, Kelson MD, Gartner NM (1981) MAXBAND: a program for setting signals on arteries and triangular networks. In: 60th annual meeting of the transportation research board, pp 40-46. Washington District of Columbia, United States: Transportation Research Board. http://trid.trb.org/view.aspx?id=172891
Luk JYK (1984). Two traffic-responsive area traffic control methods: scat and scoot. Traffic Eng Control 25(1). http://trid.trb.org/view.aspx?id=203568
Marichal J-L (2004) Tolerant or intolerant character of interacting criteria in aggregation by the Choquet integral. Eur J Oper Res 155(3):771-791. https://doi.org/10.1016/S0377-2217(02)00885-8
Mirchandani P, Head L (2001) A real-time traffic signal control system: architecture, algorithms, and analysis. Transp Res C Emerg Technol 9(6):415-432. https://doi.org/10.1016/S0968-090X(00)00047-4
Moalla D, Elkosantini S, Darmoul S (2013) An artificial immune network to control traffic at a single intersection. In: Proceedings of the fifth international conference on industrial engineering and systems management, IESM 2013
Murty MN, Devi VS (eds) (2011) Nearest neighbour based classifiers. In: Pattern recognition. Springer, London, pp 48-85. https://doi.org/10.1007/978-0-85729-495-1
Negi P (2006) Artificial immune system based urban traffic control. Texas A\&M University. http://oaktrust. library.tamu.edu/bitstream/handle/1969.1/5764/etd-tamu-2006A-MEEN-Negi.pdf
Perelson A, Weisbuch G (1997) Immunology for physicists. Rev Mod Phys 69(4):1219-1268. https://doi.org/10.1103/RevModPhys.69.1219
PTV G (2015) VISSIM simulation software. Retrieved 28 Sept 2015. http://vision-traffic.ptvgroup.com/enuk/home/
Raza A, Fernandez BR (2015) Immuno-inspired robotic applications: a review. Appl Soft Comput 37:490-505. https://doi.org/10.1016/j.asoc.2015.08.050
Robertson DI (1969) "TRANSYT" method for area traffic control. Traffic Eng Control 11(6):276-281. http://trid.trb.org/view.aspx?id=116630

Robertson DI, Bretherton RD (1991) Optimizing networks of traffic signals in real time-the SCOOT method. IEEE Trans Veh Technol 40(1):11-15. https://doi.org/10.1109/25.69966
Sadek AW, Smith BL, Demetsky MJ (2001) A prototype case-based reasoning system for real-time freeway traffic routing. Transp Res C Emerg Technol 9(5):353-380. https://doi.org/10.1016/S0968-090X(00)00046-2
Smyth B, McKenna E (1999) Building compact competent case-bases. In: Althoff K-D, Bergmann R, Branting LK (eds) Case-based reasoning research and development, vol 1650. Springer, Berlin, pp 329-342. https://doi.org/10.1007/3-540-48508-2
Stevanovic A (2010) Adaptive traffic control systems: domestic and foreign state of practice. Transportation research Board. http://trid.trb.org/view.aspx?id=916104
Tahilyani S, Darbari M, Shukla PK (2013) Soft computing approaches in traffic control systems: a review. AASRI Procedia 4:206-211. https://doi.org/10.1016/j.aasri.2013.10.032
Trabelsi B, Elkosantini S, Darmoul S (2012) Traffic control at intersections using artificial immune system approach. In: 9th international conference of modeling, optimization and simulation-MOSIM'12. Bordeaux, France
Traffic Signal Control Systems (1997) In: Advanced transportation management technologies. United States Department of Transportation, National Transportation Library, pp 1-28. http://ntl.bts.gov/lib/jpodocs/edldocs1/13480/ch3.pdf
Ulutaş BH, Kulturel-Konak S (2011) A review of clonal selection algorithm and its applications. Artif Intell Rev 36(2):117-138. https://doi.org/10.1007/s10462-011-9206-1
Wallace CE, Courage KG, Reaves DP, Schoene GW, Euler GW (1984) TRANSYT-7F user's manual. http://trid.trb.org/view.aspx?id=213009
Wen W (2008) A dynamic and automatic traffic light control expert system for solving the road congestion problem. Expert Syst Appl 34(4):2370-2381. https://doi.org/10.1016/j.eswa.2007.03.007
Wong Y, Woon W (2008) An iterative approach to enhanced traffic signal optimization. Expert Syst Appl 34(4):2885-2890. https://doi.org/10.1016/j.eswa.2007.05.007
Wu J, Abbas-Turki A, El Moudni A (2011) Cooperative driving: an ant colony system for autonomous intersection management. Appl Intell 37(2):207-222. https://doi.org/10.1007/s10489-011-0322-z
Wunderlich R, Elhanany I, Urbanik T (2008) A novel signal-scheduling algorithm with quality-of-service provisioning for an isolated intersection. IEEE Trans Intell Transp Syst 9(3):536-547. https://doi.org/10.1109/TITS.2008.928266
Wunderlich R, Elhanany I, Urbanik T (2007) A stable longest queue first signal scheduling algorithm for an isolated intersection. In: 2007 IEEE international conference on vehicular electronics and safety. IEEE, pp 1-6. https://doi.org/10.1109/ICVES.2007.4456393
Yager RR (2004) Generalized OWA aggregation operators. Fuzzy Optim Decis Mak 3(1):93-107. https://doi. org/10.1023/B:FODM.0000013074.68765.97
Yin Y (2008) Robust optimal traffic signal timing. Transp Res B Methodol 42(10):911-924. https://doi.org/10.1016/j.trb.2008.03.005


[^0]:    - Sabeur Elkosantini
    selkosantini@ksu.edu.sa;
    ssabeur.elkosantini@yahoo.fr
    Ali Louati
    alouati@ksu.edu.sa
    Saber Darmoul
    sdarmoul@ksu.edu.sa
    Lamjed Ben Said
    lamjed.bensaid@isg.rnu.tn
    ${ }^{1}$ Raytheon Chair for Systems Engineering, Advanced Manufacturing Institute, King Saud University, P.O. Box 800, Riyadh 11421, Kingdom of Saudi Arabia
    ${ }^{2}$ Industrial Engineering Department, King Saud University, P.O. Box 800, Riyadh 11421, Kingdom of Saudi Arabia
    3 SMART Laboratory, High Institute of Management of Tunis, University of Tunis, Tunis, Tunisia

