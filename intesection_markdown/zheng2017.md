Jianfeng Zheng ${ }^{\mathrm{a}}$, Henry X. Liu ${ }^{\mathrm{a}, \mathrm{b}, *}$<br>${ }^{\mathrm{a}}$ Department of Civil and Environmental Engineering, University of Michigan, United States<br>${ }^{\mathrm{b}}$ University of Michigan Transportation Research Institute, United States

## ARTICLE INFO

Article history:
Received 5 November 2016
Received in revised form 10 February 2017
Accepted 13 March 2017

Keywords:
Connected vehicle
Mobile data
GPS trajectory
Traffic signal
Vehicle-to-infrastructure communication
Traffic volume estimation
Safety Pilot Model Deployment (SPMD) project


#### Abstract

Recently connected vehicle (CV) technology has received significant attention thanks to active pilot deployments supported by the US Department of Transportation (USDOT). At signalized intersections, CVs may serve as mobile sensors, providing opportunities of reducing dependencies on conventional vehicle detectors for signal operation. However, most of the existing studies mainly focus on scenarios that penetration rates of CVs reach certain level, e.g., 25\%, which may not be feasible in the near future. How to utilize data from a small number of CVs to improve traffic signal operation remains an open question. In this work, we develop an approach to estimate traffic volume, a key input to many signal optimization algorithms, using GPS trajectory data from CV or navigation devices under low market penetration rates. To estimate traffic volumes, we model vehicle arrivals at signalized intersections as a time-dependent Poisson process, which can account for signal coordination. The estimation problem is formulated as a maximum likelihood problem given multiple observed trajectories from CVs approaching to the intersection. An expectation maximization (EM) procedure is derived to solve the estimation problem. Two case studies were conducted to validate our estimation algorithm. One uses the CV data from the Safety Pilot Model Deployment (SPMD) project, in which around 2800 CVs were deployed in the City of Ann Arbor, MI. The other uses vehicle trajectory data from users of a commercial navigation service in China. Mean absolute percentage error (MAPE) of the estimation is found to be 9-12\%, based on benchmark data manually collected and data from loop detectors. Considering the existing scale of CV deployments, the proposed approach could be of significant help to traffic management agencies for evaluating and operating traffic signals, paving the way of using CVs for detector-free signal operation in the future.


© 2017 Elsevier Ltd. All rights reserved.

## 1. Introduction

Signalized intersections are indispensable parts of urban traffic networks. Currently, over 300,000 traffic signals exist in the U.S., accounting for $\$ 82.7$ billion public investments (NTOC, 2012). With two-thirds of urban vehicle miles traveled on signal controlled roads (McCracken, 1996), signalized intersections have often become hot-spots of traffic congestion, causing 295 million vehicle-hours of delay annually. ${ }^{1}$ Considering the amount of traffic signals and their impact to the traffic

[^0]network, it is critical to operate traffic signals efficiently. However, the majority of signals in the U.S. are only re-timed once every 2-5 years, despite of a high benefit-cost ratio for signal re-timing (Sunkari, 2004). This is primarily due to the labor costs for the retiming process. With tightening budgets and resources nowadays, maintaining efficient signal operation has become a challenging task for many traffic management agencies.

Recent advent of connected vehicle (CV) introduces great opportunities of reforming the conventional traffic signal operation. Currently, many traffic signals in the U.S. are still fixed-time signals, which are not responsive to fluctuated traffic demands. For traffic signals to accommodate varying demands, vehicle detectors, e.g., inductance loop detectors or video detectors, need to be installed and maintained properly. This inevitably incurs significant cost for the public agencies. With the vehicle-to-infrastructure (V2I) communication, CVs can continuously report their status to roadside equipment (RSE) at intersections, working as mobile sensors. Therefore, CVs hold great potential to reduce or even eliminate the needs for fixedlocation detectors in the existing signal systems. When penetration rates are low, the CV data could be used to generate performance measures for fine-tuning traffic signals periodically. When penetration rates are high, it becomes viable to operate adaptive signal control that solely depends on CV input.

Considering these potentials, deploying V2I systems at signalized intersections has been an important part of CV pilot deployment, exemplified by the installation of RSEs at intersections in the Safety Pilot Model Deployment (SPMD) project (Gay and Kniss, 2015), the upcoming CV pilot deployment (Masters, 2016), as well as in the Smart City development supported by the US Department of Transportation (USDOT). Along with the deployment efforts, a number of CV-based signal control algorithms have also been proposed. However, the signal control algorithms proposed in the previous studies mainly focus on scenarios that penetration rates of CVs reach certain levels, e.g., 25\%, which may not be feasible in the near future. In addition, most of the existing studies rely on simulated data which may not capture real-world characteristics of CVs, e.g. communication performance or GPS accuracy. Therefore, the proposed algorithms may not be transferable to the practice. How to utilize real-world CV data under low penetration rate environment to improve traffic signal operation remains as an open question.

Aiming to answer this question, this work develops an innovative approach that uses data from CVs to estimate traffic volumes at signalized intersections, particularly under low penetration rate environment. It has been well known that traffic volumes are the very key inputs to designing and optimizing traffic signal operation. In conventional signal systems, vehicle arrival information can only be obtained from detectors at fixed locations. Different from the detector data, CV data provide detailed trajectories, albeit from a small percentage of vehicles. The comparison is illustrated in Fig. 1. The challenge here is to estimate overall arrival information using limited CV trajectories. (For example, about 3-12\% traffic in the City of Ann Arbor, MI, are CVs because of the SPMD Project.)

In this work, the above challenge will be addressed through leveraging historical CV data and the repetitive patterns of vehicle arrivals at signalized intersections. In the proposed algorithm, vehicle arrivals at intersections are modeled as a timedependent Poisson process with a time dependent factor characterizing arrival types. For volume estimation, an expectation maximization (EM) procedure is derived that can incorporate different types of CV trajectories. To evaluate the performance of the proposed algorithm, two case studies were conducted: the first case study utilized real-world CV data received by a RSE in the SPMD project; the second case study utilized vehicle trajectory data from users of a route navigation service. To the best of our knowledge, this research is the first attempt of exploring real-world CV or GPS trajectory data under low penetration rate environment for volume estimation at signalized intersections. Our ultimate goal is to use CV data to develop a detector-free signal control system in the future.

The rest of this paper is organized as follows. Section 2 presents a review of relevant work for traffic signal control with CVs, as well as traffic state estimation at intersections with probe vehicle. Section 3 briefly introduces the SPMD project and CV data. Section 4 describes the methodology for estimating traffic arrivals. Section 5 presents the two case studies using vehicle trajectory data. Conclusions and future research are discussed in Section 6.

## 2. Relevant work

Traffic signal control with CVs has captured substantial attention in the past several years. Many existing studies focus on developing real-time traffic signal control with CVs, through either extending signal actuation mechanism or minimizing vehicle delay based on a traffic model (Agbolosu-Amison et al., 2008; Milanés et al., 2012; He et al., 2012, 2014; Lee et al., 2013b,a; Guler et al., 2014; Feng et al., 2015; Goodall et al., 2016). However, most of the proposed adaptive signal control algorithms require high penetration rates of CVs, e.g., 25\%. Such high penetration rates may not be achievable in the near future. A notable exception is Day and Bullock (2016) which conducted a proof-of-concept study using CV data in a low penetration rate environment for optimizing signal coordination. However, the data used in Day and Bullock (2016) were sampled from fixed location vehicle detectors so vehicle trajectories were not used in their study. The problem of estimating traffic volume from vehicle trajectories, which is a fundamental input for signal operation, is also not tackled.

On the other hand, with increasing availability of GPS data from cell phones and navigation units, substantial efforts have been carried out for traffic state estimation using vehicle trajectory data. Exemplified by the Mobile Century project (Hoh et al., 2008; Work et al., 2008; Herrera et al., 2010), a large group of existing studies used GPS data to estimate traffic speed and travel time (Turner and Holdener, 1995; Chen and Chien, 2001; Long Cheu et al., 2002; Hellinga and Fu, 2002; Nanthawichit et al., 2003; Bhaskar et al., 2011; Jenelius and Koutsopoulos, 2013; Zheng and Van Zuylen, 2013).

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-03.jpg?height=633&width=1096&top_left_y=183&top_left_x=389)
Fig. 1. Illustration of CV data versus detector data.

Recently, several studies have also been conducted for real-time queue length estimation at signalized intersections. These approaches can be grouped into two main categories, one based on a probabilistic approach and the other using shockwave theory. Comert and his colleague derived analytical expressions of conditional probability of queue length based on the probability of observing probe vehicles in a queue (Comert and Cetin, 2009; Comert, 2013, 2016). Hao et al. proposed a Bayesian Network based model for estimating the probability of probe vehicle positions in vehicle arrivals (Hao et al., 2013, 2014). Another category focuses on applying the shock-wave theory by Lighthill and Whitham (1955) and Richards (1956) for queue length estimation with vehicle trajectory data. Ban et al., proposed to estimate traffic delay using travel time sampled from mobile sensors (Ban et al., 2009). The methodology was later extended for real-time estimation of queue length in Ban et al. (2011) and Hao et al. (2015). Cetin proposed a procedure for queue length estimation with over-saturated traffic conditions by identifying critical points of traffic shockwave (Cetin, 2012). Christofa et al. proposed a procedure to detect queue spillback using trajectory data with signal status information at both subject and upstream intersections (Christofa et al., 2013). Li et al. proposed a data fusion procedure for queue length estimation, leveraging data from both probe vehicles and loop detectors (Li et al., 2013). Sun \& Ban applied the variation formulation of traffic flow model by Daganzo (2005) for reconstructing all vehicle trajectories based on probe vehicle data (Sun and Ban, 2013). Their key idea was to obtain flow information based on probe vehicle speeds, assuming that arrivals between two probe vehicles were uniform.

In the aforementioned studies, the primary focus is on estimating real-time performance measures at isolated intersections. However, estimating traffic volumes, which are critical for offline optimization of signal operation, has yet been studied. A notable exception is Ban and Gruteser (2010), which proposed an estimator for volume estimation using sampled travel time and delay pattern estimated from Ban et al. (2009). However, the algorithm relies on accurate delay estimation, which requires a relatively high penetration rate (>20\%) as reported in Ban et al. (2009). This, however, would be difficult in a near future. In this work, we aim to fill in the gap for volume estimation using CV data with low penetration rates. We believe that the proposed methodology would be an important building block of utilizing CV or vehicle trajectory data for traffic signal re-timing, and eventually achieving detector-free signal operation in the future.

## 3. Data from the Safety Pilot Model Deployment (SPMD) project

In this paper, we use CV trajectory and signal status data collected in the SPMD project. The SPMD project was conducted by the University of Michigan Transportation Research Institute (UMTRI) for evaluating operation applicability of CV technology in a real-world concentrated environment, and also for quantifying the benefits of CV safety applications and user acceptance. ${ }^{2}$ In the project, since August 2012, UMTRI has equipped about 2800 vehicles with dedicated short range communication (DSRC) devices and deployed RSEs at 27 locations including 19 intersections. An illustration of RSE deployment in the project is shown in Fig. 2. The basic safety messages (BSM) received by the RSEs have been continuously collected and archived in the UMTRI database. Sample data from the SPMD project are also available at the Research Data Exchange. ${ }^{3}$

[^1]![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-04.jpg?height=1191&width=1191&top_left_y=185&top_left_x=357)
Fig. 2. Deployments of RSEs in the SPMD project (Source: http://safetypilot.umtri.umich.edu/).

BSM data from RSEs
A sample of processed BSM data received by a RSE is shown in Fig. 3. Only a subset of data fields are used in our investigation, including device ID of a RSE (RxDevice), device ID of a CV sending the BSMs (TxDevice), GPS position and speed of the CV, and timestamp when the BSM was received by a RSE.

Signal status data from SPaT messages
The SPaT (signal phase and timing) data broadcast by the RSEs have also been collected at deployed intersections. The SPaT data contain information of signal status that can be used as the input for "signal aware" CV applications, e.g., red light violation warning or eco-approach/departure assistance. Here, only a portion of the data fields in the SPaT are used, including: timestamp when a message was generated, signal phase ID and signal status. A sample of SPaT data is shown in Fig. 4.

Data processing
The GPS information from BSM and signal status data are processed in the following manner. We first select an interested movement, its associated signal phase, and an interested time period, e.g., 8AM-9AM, for investigation. We then select GPS data associated with the movement and time period, based on direction of CV trajectories, and also prepare corresponding signal status data. Then, based on road geometry, we calculate CVs' longitudinal position along the road from GPS positions, and generate time-space trajectories. We also map GPS time into signal clock time. This is done by finding the green start when a CV passes the stop bar, and subtracting the green start time from CV trajectory time, so that we have signal clock time for the CV trajectory, i.e., time using green start as zero. With the time in signal clock, we can aggregate trajectories to calculate the time dependent factor, similar to the cyclic profile generated from vehicle detectors (Abbas et al., 2001;

| RSE ID | CV ID | Gentime (second) | Latitude | Longitude | Speed (m/s) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 18013 | 35 | 281203941.949 | 42.30465 | -83.70778 | 4.78 |
| 18013 | 35 | 281203942.249 | 42.30465 | -83.70776 | 4.7 |
| 18013 | 35 | 281203942.349 | 42.30465 | -83.70776 | 4.66 |
| 18013 | 35 | 281203942.449 | 42.30465 | -83.70775 | 4.68 |
| 18013 | 35 | 281203942.549 | 42.30465 | -83.70774 | 4.68 |

Fig. 3. Sample BSM data received by RSEs.

| Time Stamp | Phase ID | Phase Status |
| :--- | :--- | :--- |
| 2015-9-1,0:6:48.837 | 2 | Red |
| 2015-9-1,0:6:48.837 | 2 | Red |
| 2015-9-1,0:6:48.837 | 1 | Green |
| 2015-9-1,0:6:48.837 | 1 | Green |

Fig. 4. Sample signal status data from SPaT messages broadcast by RSEs.

Zheng et al., 2014; Day and Bullock, 2016). The time dependent factor is then used with CV trajectories to estimate traffic volumes, the details of which is presented in the next section.

## 4. Methodology

In order to estimate traffic volume, our basic idea is to take advantage of vehicle arrival information in vehicle trajectories. The arrival information can be reflected from the status whether a vehicle stopped or not. An example is shown in Fig. 5. In the figure, CV1 passed the intersection with a stop and CV2 without a stop. Then, based on CV1's stopping position or departure time, we can calculate number of vehicles queuing in front of it. Based on the trajectory of CV2 without a stop, we know that if vehicle queue existed, the queue would not be long enough to impact CV2. In other words, the upper bound of possible vehicle arrivals between CV1 and CV2 can be calculated based on the trajectory of CV2. By combining these arrival information from vehicle trajectories, volume of overall vehicle arrivals can be estimated.

The inputs to our estimation algorithm include vehicle trajectories approaching to an intersection as well as traffic signal status. For a CV trajectory, the information being utilized includes its projected arrival time with free flow speed at the stop bar $t_{f, i}$, its departure time at the stop bar $t_{d, i}$, the type of event indicating whether a CV stopped or not $s_{i}$, and the subscript $i$ as the index of the event. For each CV trajectory, we can retrieve the following vector $X_{i}$, for the key information of trajectories. Then, the estimation only needs to use the information within the vector, instead of the raw trajectory data.

$$
X_{i}=\left(t_{f, i}, t_{d, i}, s_{i}\right)^{T}
$$

For CV without a stop, the projected arrival time at stop bar is equal to the departure time, as: $t_{f, i}=t_{d, i}$. For a CV with a stop, we can estimate its projected arrival time $t_{f, i}$ as:

$$
t_{f, i}=t_{s, i}+\frac{l_{i}}{v_{f}}
$$

where $t_{s, i}$ is time when the CV came to a stop, $l_{i}$ is the distance of its stopping position to the stop bar, and $v_{f}$ is the free flow speed.

To incorporate signal information, we also treat the red signals as a type of events. Here, we assume that no residual queue exists at the start of red signal. With this assumption, we only focus on estimation with non-saturated traffic conditions, leaving estimation with over-saturated traffic conditions in our future research. For each red signal, we can also prepare the trajectory information vector as:

$$
X_{j}=\left(t_{f, j}, t_{d, j}, s_{j}\right)^{T}, \text { with } t_{f, j}=t_{r, j}, t_{d, j}=t_{g, j}
$$

where $t_{r, j}$ is the time of red start for cycle $j$, and $t_{g, j}$ for green start. Here, $s_{j}$ is set as -1, indicating that this event is corresponding to a red signal. Denoting red signal as an event is for the ease of data processing so that we can calculate inter arrival period between arrivals of CVs and starting time of red signals easily.

These two vectors are the main input to the estimation process in the next section.

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-06.jpg?height=482&width=1076&top_left_y=183&top_left_x=413)
Fig. 5. Illustration of vehicle arrival information in trajectories.

### 4.1. Modeling traffic arrivals as a time-dependent Poisson process

During a selected Time of Day (TOD) period, we assume that traffic arrivals follow a time-dependent Poisson process with an arrival rate of $\lambda p\left(t^{(c)}\right)$. Here, $t^{(c)}$ indicates time within a signal cycle, the superscript $(c)$ indicates that the time is measured using a signal clock, $\lambda$ denotes the mean arrival rate, and $p\left(t^{(c)}\right)$ is the time dependent factor proportional to the arrival rate at $t^{(c)}$, i.e., the fraction of total arrivals at $t^{(c)}$ over the entire signal cycle. In traffic engineering literature, Poisson process is a common choice to model traffic arrivals at intersections. The additional assumption that arrival rates are dependent on the time in a signal cycle is to account for impacts from signal coordination. With the signal coordination, traffic departures at the upstream intersection would be grouped as platoons, leading to nonhomogeneous arrivals at subject intersection. The time-dependent Poisson process is used to characterize the non-homogeneous arrivals.

Defining $N\left(t_{1}, t_{2}\right)$ as the accumulative number of arrivals from time $t_{1}$ to $t_{2}$, we have:

$$
N\left(t_{1}, t_{2}\right) \sim \operatorname{Poisson}\left(\Lambda\left(t_{1}, t_{2}\right)\right)
$$

where $\Lambda\left(t_{1}, t_{2}\right)=\int_{t_{1}}^{t_{2}} \lambda p(C(t)) d t=\lambda \int_{t_{1}}^{t_{2}} p(C(t)) d t$, indicating arrival rate between $t_{1}$ and $t_{2}$, and also for simplifying notations. $C: t \rightarrow t^{(c)}$, maps the time of a day, $t$, to time in signal cycle clock, $t^{(c)} . \lambda$ is the mean arrival rate across the investigation period.

By aggregating CV trajectories, we can calculate the time dependent factor $p\left(t^{(c)}\right)$ based on the following equation:

$$
p\left(t^{(c)}\right)=\frac{1}{N} \sum_{i=1}^{N} I\left\{C\left(t_{f, i}\right)=t^{(c)}\right\}
$$

where $I\left\{C\left(t_{f, i}\right)=t^{(c)}\right\}$ is an indicator equal to 1 if the projected arrival time is in $t^{(c)}$ interval, and 0 otherwise, and $N$ is the total number of CV trajectories. For the ease of data processing, we discretize time with 1-s interval.

Here, the equation essentially calculates fraction of CV arrivals during $t^{(c)}$ interval from total CV arrivals during a cycle. We use the fraction of CV arrivals as the estimate of the fraction of traffic, including both CV and non-CV. Essentially, this assumes that CVs are homogeneously distributed in cycle arrivals for a particular movement during the investigation period. However, across different movements, we allow the penetration rates to be different, which are observed in cases studies in the later sections.

Given the Poisson arrival process, the likelihood function for observing all valid CV trajectories can be formulated by taking advantage of the inter-arrival time and the corresponding number of non-CV arrivals between two consecutive CV trajectories received at RSE. As mentioned earlier, two types of CV trajectories are considered: 1. CV trajectory with a stop at an intersection, and 2. CV trajectory that traverses the intersection without a stop. Between the projected arrival times of two stopped CVs, or between the projected arrival time of one stopped CV and the start of a red signal, the number of non-CV arrivals can be calculated based on the CVs' departure time. If a CV without a stop is observed, then queues at intersection, if exist, are not long enough to affect the non-stopped CV. Thus, the maximum number of vehicle arrivals before the CV can be calculated. Illustrations of the two types of CVs are shown in Fig. 6, along with notations for calculation later on.

For each CV trajectory, we can calculate the probability of occurrence according to the following cases:
Case 1. If $s_{i}=1, s_{i-1}=-1$ or 1, indicating a CV trajectory with a stop is observed after red start or after the arrival of another stopped CV, we have:

$$
N\left(t_{f, i-1}, t_{f, i}\right)=n_{y, i}, N\left(t_{f, i-1}, t_{f, i}\right) \sim \operatorname{Poisson}\left(\lambda P_{y, i}\right)
$$

where $n_{y, i}=\left\lfloor\frac{G\left(t_{d, i-1}, t_{d, i}\right)}{h_{s}}\right\rfloor$, denoting the number of departures during the inter-arrival period $\left[t_{f, i-1}, t_{f, i}\right]$. $h_{s}$ is the saturated headway, and $P_{y, i}=\frac{\Lambda\left(t_{f, i-1}, t_{f, i}\right)}{\lambda}=\int_{t_{f, i}}^{t_{f, i-1}} p(C(t)) d t$, for simplifying notations. $G\left(t_{d, i-1}, t_{d, i}\right)$ is the effective green time from time $t_{d, i-1}$, to $t_{d, i}$. The subscript $y$ denotes that the observations are for stopped CVs. The illustration is also shown in Fig. 6a.

Case 2. If $s_{i}=2, s_{i-1}=-1$ or 1, indicating a CV trajectory without a stop is observed after red start or after a stopped CV. Accordingly, we have:

$$
N\left(t_{f, i-1}, t_{f, i}\right) \leqslant n_{z, i}, N\left(t_{f, i-1}, t_{f, i}\right) \sim \operatorname{Poisson}\left(\lambda P_{z, i}\right)
$$

where $n_{z, i}=\left\lfloor\frac{G\left(t_{d, i-1}, t_{d, i}\right.}{h_{s}}\right\rfloor, P_{z, i}=\frac{\Lambda\left(t_{f, i-1}, t_{f, i}\right)}{\lambda}=\int_{t_{f, i}}^{t_{f, i-1}} p(C(t)) d t$. The subscript $z$ denotes that the observations are for non-stopped CVs. The illustration is also shown in Fig. 6b.

Besides these two cases, two other cases of trajectories also exist: 1. stopped CV arriving after a non-stopped CV in the same cycle, and 2. non-stopped CV arriving after another non-stopped CV, also in the same cycle. For the first case, the stop of the CV would not be caused by queues or red signal, but likely by other factors, e.g., mid-block entry of other vehicles. For the second case, after the arrival of a non-stopped CV, we know that the queues must have been cleared and the rest of CVs in the same cycle would travel with free-flow speed. The trajectory therefore does not provide useful information for volume estimation. Accordingly, both cases are considered as invalid or trivial observations, and are not used in the estimation.

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-07.jpg?height=1435&width=913&top_left_y=913&top_left_x=478)
Fig. 6. Illustrations of two different types of CV trajectories.

Based on the discussion, the likelihood of observing all valid CV trajectories can be calculated with the following equation, with Y as the collection of observations for all stopped CVs, and Z for all non-stopped CVs.

$$
L(Y, Z \mid \lambda)=\prod_{i=1}^{n}\left\{\frac{\left(\lambda P_{y, i}\right)^{n_{y, i}} e^{-\left(\lambda P_{y, i}\right)}}{n_{y, i}!}\right\} \prod_{j=1}^{m}\left\{\sum_{k=0}^{n_{z, j}} \frac{\left(\lambda P_{z, j}\right)^{k} e^{-\left(\lambda P_{z, j}\right)}}{k!}\right\}
$$

Now, we can estimate $\lambda$ for the traffic volume using maximum likelihood estimator (MLE). However, due to the summation inside the product operation in Eq. (3), it is difficult to obtain a closed form of the MLE. Instead of seeking for a closed form, we use the Expectation Maximization (EM) algorithm for the estimation.

### 4.2. Estimating parameter using Expectation Maximization (EM)

The Expectation Maximization (EM) algorithm is an iterative procedure to find the MLE mostly suitable when unobserved or partially observed variables exist. The EM algorithm consists of two main steps: the E-step and the M-step. The E-step calculates the conditional expectation of unobserved or partially observed variables based on initialized parameters, and the conditional expectation of the likelihood. Then, the M-step searches for an optimal update of the parameters through maximizing the likelihood. The two steps are iterated until updates converge. For the details of the EM algorithm, interested readers are referred to Bilmes (1998). In our case, CV trajectories with stop provide direct information of number of arrivals, while trajectories without a stop only provide information of upper bounds of the number of arrivals, i.e., partial information. Considering this, the EM algorithm would be a proper choice for our estimation.

For the E-Step, denoting $\hat{n}_{z, i}$ as the true value of accumulated number of arrivals by time $t_{z, i}$ corresponding to a CV trajectory without a stop, we have the log-likelihood for the complete data sequence as:

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-08.jpg?height=1193&width=1189&top_left_y=1080&top_left_x=359)
Fig. 7. Illustration of investigated intersections.

$$
\begin{aligned}
L L^{c}= & \sum_{i=1}^{n} \ln p\left(n_{y, i} \mid \lambda P_{y, i}\right)+\sum_{i=1}^{m} \ln p\left(\hat{n}_{z, i} \mid \lambda P_{z, i}\right) \\
= & \sum_{i=1}^{n}\left[\ln \frac{\left(\lambda P_{y, i}\right)^{n_{y, i}} e^{-\lambda P_{y, i}}}{n_{y, i}!}\right]+\sum_{i=1}^{m}\left[\ln \frac{\left(\lambda P_{z, i}\right)^{\hat{n}_{z, i}} e^{-\lambda P_{z, i}}}{\hat{n}_{z, i}!}\right] \\
= & \sum_{i=1}^{n}\left[n_{y, i}\left(\ln \lambda+\ln P_{y, i}\right)-\lambda P_{y, i}-\ln n_{y, i}!\right] \\
& +\sum_{i=1}^{m}\left[\hat{n}_{z, i}\left(\ln \lambda+\ln P_{z, i}\right)-\lambda P_{z, i}-\ln \hat{n}_{z, i}!\right]
\end{aligned}
$$

Then, the expectation of the log-likelihood can be expressed as:

$$
Q\left(\lambda \mid \lambda^{(s)}\right)=E\left(L L^{c} \mid \lambda^{(s)}\right)=C+\sum_{i=1}^{n}\left[n_{y, i} \ln \lambda-\lambda P_{y, i}\right]+\sum_{i=1}^{m}\left[\hat{n}_{z, i} \ln \lambda-\lambda P_{z, i}\right]
$$

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-09.jpg?height=1564&width=1543&top_left_y=784&top_left_x=169)
Fig. 8. Illustration of CV trajectories (a) and time dependent factor (b) for EB through movement.

We will use the conditional mean as the estimate of the unobserved $\hat{n}_{z, i}$, given $n_{z, i}$. We have:

$$
\hat{n}_{z, i} \mid n_{z, i}, \lambda^{(s)}=\sum_{k=0}^{n_{z, i}} k \operatorname{Pr}\left(\hat{n}_{z, i}=k \mid \hat{n}_{z, i} \leqslant n_{z, i}, \lambda^{(s)}\right)=\sum_{k=0}^{n_{z, i}} k \frac{\frac{\left(\lambda^{(s)} p_{z, i}\right)^{k}}{k!}}{\sum_{l=0}^{n_{z, i}} \frac{\left(\lambda^{(s)} p_{z, i}\right)^{l}}{l!}}
$$

Finally, in the M-step, by setting the derivative of $Q\left(\lambda \mid \lambda^{(s)}\right)$ with respect to $\lambda$ as zero, we have an equation for updating $\lambda$, as:

$$
\lambda^{(s+1)}=\frac{\sum_{i=1}^{n} n_{y, i}+\sum_{i=1}^{m} \hat{n}_{z, i}}{\sum_{i=1}^{n} P_{y, i}+\sum_{i=1}^{m} P_{z, i}}
$$

The Eqs. (6), (7) complete the EM iteration for the estimation.

## 5. Case studies

To evaluate the proposed estimation algorithm, two case studies were conducted. The first case study utilized CV data received by a RSE in the SPMD project. The second case study utilized GPS data from users of a navigation service. These two types of data essentially contain similar information. However, the studied intersection in the first study was controlled by the SCOOT adaptive signal system, while in the second case study, the intersections were controlled by fixed-time signals.

### 5.1. Case study 1: Using CV data from a RSE

In the first case study, we analyzed data from Intersection of Plymouth Rd. \& Green Rd., one of the deployed intersections in the SPMD project. CV data used were collected from 04/25/16 to 05/13/16. An illustration of the intersection geometry is shown in Fig. 7, together with the ring-and-barrier diagram for traffic signal in operation. Here, our investigation focused only on EB through, WB through, as well as SB through and left-turn traffic, corresponding to phase 1, 2 and 4. The NB approach is a single-lane road adjacent to the parking lot of a shopping plaza. At the NB approach, traffic from the driveways and parking lots frequently affected vehicles traveling at the NB approach, resulting in additional queues and vehicle-stops not caused by the traffic signal. Since the stop and queuing information play key roles in our estimation, we exclude the analysis for the NB traffic, considering the noises caused by the traffic from the parking lot.

For each interested approach, trajectories of CVs were first processed as time-space plots with time as the horizontal axis and distance to the stop bar as the vertical axis. The trajectories are shown in Fig. 8. With the SCOOT adaptive signal system, at this intersection, the cycle length, red and green duration all varied from cycle to cycle. To select a common reference point in a signal cycle, we use the start of green as time 0 in the plot for simplicity. The stop bar position is used as 0 origin along the $y$-axis. The distance increases upstream along $y$-axis. That is, vehicles travel from locations of positive distances to negative distances.

The CV trajectories were aggregated according to different TOD periods with 1-h intervals across different days, to first calculate time-dependent factors $p(t)$. For different TOD periods, substantially different $p(t)$ were observed with two examples shown in Fig. 8b. The differences in $p(t)$ are likely due to differences in both traffic patterns and signal settings in the two different TOD periods. Then, the EM procedure was implemented for the estimation.

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-10.jpg?height=604&width=1193&top_left_y=1741&top_left_x=359)
Fig. 9. CV penetration rates over time of day.

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-11.jpg?height=1304&width=1555&top_left_y=179&top_left_x=161)
Fig. 10. Comparison between observed volume with estimated volume for case 1.

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-11.jpg?height=661&width=903&top_left_y=1624&top_left_x=486)
Fig. 11. Trajectories of converted trajectory data from navigation users.

For validation purpose, hourly volumes were also manually collected for two days, i.e., 04/25/16 and 04/26/16, from 11:00 AM to 7:00 PM. Using the measured volumes, we calculated the penetration rates of CVs, shown in Fig. 9. Overall, the penetration rates ranged from 3\% to 12\%, varying over the selected periods. The rates also varied substantially at different approaches, with lower CV penetration rates at the EB and WB approach, i.e., the main approaches, and higher rates at the SB approach, a minor approach. This variation could be due to that the SB approach connects to residential areas close to the University of Michigan, that would have larger population of participants of the SPMD project.

The observed volumes were then used for comparing with the estimated volumes, with results shown in Fig. 10. The three cases are shown in three sub-figures, respectively. In the figure, the yellow bars show the estimated volume, and the blue bars show the observed volumes, both in units of vehicle per hour per lane (vphpl). Substantial different traffic patterns exists in the three cases. For example, clear afternoon peak existed in both EB and SB cases, but not in WB case. Regarding the estimation, the estimated volumes are generally closed to the observed volumes for all the three cases. To further quantify the accuracy, we calculated the Mean Absolute Percentage Error (MAPE) for the estimation based on the following formula, indicated as well in the figure.

$$
M A P E=\frac{1}{N} \sum_{i=1}^{N} \frac{\left|V o l_{0, i}-V o l_{e, i}\right|}{V o l_{0, i}}
$$

where $\operatorname{Vol}_{o, i}$ is the observed volume, and $\operatorname{Vol}_{e, i}$ is the estimated volume, during i-th interval.

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-12.jpg?height=643&width=1199&top_left_y=846&top_left_x=353)
Fig. 12. Penetration rates of the navigation users over time of day.

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-12.jpg?height=748&width=1296&top_left_y=1596&top_left_x=302)
Fig. 13. Comparison between observed volume with estimated volume for case 2.

The MAPEs are 11.2\%, 10.1\% and 12.3\% for EB, WB and SB approach, respectively, indicating reasonable accuracy of the proposed procedure. Among the 3 approaches, however, the estimation for the SB approach performs the worst among all three phases, despite the largest CV penetration rates. This is likely due to that the arrival patterns are more stable at the EB and WB approaches with signal coordination, than that at the SB approach, i.e., a minor approach. Additionally, with the lowest traffic volumes at the SB approach, the total number of observed CV trajectories at the SB approach is similar to that at the EB and WB approach, which could imply that the sample size also play an important role rather than the penetration rate alone. Nonetheless, the results show encouraging estimation accuracy using CV data with overall low penetration rates in the investigated cases.

### 5.2. Case study 2: Using data from a route navigation service

In the second case study, we utilized data collected from drivers using a navigation service in China. The data were collected on workdays for two weeks from an signalized arterial with 5 intersections. We first selected an intersection in the

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-13.jpg?height=1614&width=1511&top_left_y=733&top_left_x=185)
Fig. 14. Comparison between observation and estimation for $30-\mathrm{min}$ volume (sub-Figure a) and $10-\mathrm{min}$ volume (sub-Figure b).

arterial for volume estimation. The volume estimation was validated using data from loop detectors for the interested approach.

At the selected intersection, a sample set of the GPS trajectories between the adjacent upstream and downstream intersections for the through movement is shown in Fig. 11. The time of each GPS data point was also converted to time within a signal cycle.

For validation purposes, volume data were also obtained for the selected approach from loop detectors on 07/12/2016. Based on the detector data, we calculated the penetration rates of the navigation users for the through movement. The results are shown in Fig. 12. In general, the penetration rates were between 0.5\% to 2\%. The penetration rates also varied substantially across different time of day, with the peak penetration rates occurring around 11AM and 3 PM.

The volume estimation results are shown in Fig. 13. In this case, we did not observe clear morning peak and afternoon peak, and the traffic volumes are rather similar throughout a day, in the range between 200 vphpl and 500 vphpl. Regarding the estimation accuracy, the estimated volumes are generally close to the observed volumes. The MAPE of the estimation is 9.2\% for the selected approach. The overall trend of estimation is similar to that in Case Study 1. However, the estimation errors in Case Study 2 are slightly smaller than those in Case Study 1, despite lower penetration rates. This is most likely because that the traffic signal in Case Study 2 was in a fixed-timed mode, while the signal in Case Study 1 was controlled by the SCOOT adaptive control system. Therefore, the time-dependent factors or the cyclical profiles in Case Study 2 are more consistent from cycle to cycle, than those in Case Study 1, hence yielding better estimation results.

In addition to hourly volume estimation, we further estimate the $30-\mathrm{min}$ volume and $10-\mathrm{min}$ volume, to test the performance of the proposed method for different estimation intervals. The estimation results are summarized in Fig. 14. The upper figure shows results for 30 -min volume estimation, and lower figure shows results for 10 -min volume estimation. For 30 -min volumes, the estimations are closed to the observed volumes with a MAPE of 11.5\%, showing reasonable estimation accuracy for the 30-min volumes. For 10-min volumes, although we can observe that the main trend of estimated volumes follows the observation, with a MAPE of 18.7\%. However, the estimation performance is less consistent with the largest estimation errors around 40\% to 50\%. (Note that, estimation at 2PM yields an error over 100\%. However, this is likely caused by the abnormally low detector volume due to a detector error.) Overall, the inconsistency would be likely due to the low number of CV trajectories within the 10 -min windows for estimation input.

To illustrate the use of the estimated volume data for assisting signal operation, we estimate the hourly-volume for four other intersections along the interested road and generated a time-space diagram (TS-Diagram) based on the estimated volumes and the time dependent factors. The TS-Diagram is a convenient and popular tool for traffic engineers to evaluate performance of signal coordination, and to fine-tune signal settings if necessary. The procedure to construct TS-Diagram is based on Zheng et al. (2015), and the result is shown in Fig. 15 for the selected corridor with the 5 intersections for time period 8 AM-9 AM.

From Fig. 15, it can be seen that, in general, the signals were coordinated well with traffic traveling in free-flow speed for the most of the time. However, for Int. 1 and Int. 3 of the selected road, vehicle delay exist and could potentially be reduced by adjusting offsets at these two intersections, indicating improvement opportunities.

![](https://cdn.mathpix.com/cropped/aafc5fb2-9322-4113-a862-c114d6e90f64-14.jpg?height=822&width=1189&top_left_y=1523&top_left_x=359)
Fig. 15. Time-Space diagram for the tested segment.

## 6. Conclusion and future research

With the rapid development of CV technology, paradigm shift may be brought to the traffic signal systems. The data from CVs provide invaluable opportunities to reduce or even eliminate the needs for conventional traffic detectors. In the near future with low penetration rates, data from CVs could be particularly useful to generate offline performance measure for traffic signal systems and adjust signal operation periodically, e.g., two weeks or a month. This potential is especially beneficial for improving fixed time signal operation.

In this paper, we developed a method to estimate traffic volumes using trajectories data from CVs or trajectories data from navigation devices. For traffic signals, traffic volumes are the key inputs to signal optimization, as well as to many other traffic engineering practices. Considering that CV deployments are still in their early stages, the focus of the proposed approach is to accommodate low CV penetration rates, for instance, below 10\% in the City of Ann Arbor, MI. In the proposed approach, we modeled the traffic arrivals as a time dependent Poisson process and derived an EM procedure for the estimation. Based on the time-dependent Poisson process, the method can accommodate coordinated intersections, as well as isolated intersections, for traffic volume estimation. We tested the estimation procedure with two case studies using real-world CV data from the SPMD project and vehicle trajectory data from navigation service users, respectively. Comparing with volume data collected manually and data from loop detectors, reasonable accuracy of the estimations was found, with MAPE in range of 9-12\%, for volume of intervals in 30 min and 1 h, and MAPE of 19\% for volume of 10-min interval. We believe that the proposed methodology would be an important building block of utilizing CV data for adjusting or re-timing traffic signals.

This research is but the first step of exploring trajectories data from CV or navigation devices for assisting traffic signal operation, and it can be extended in several directions. One of the directions is to improve the algorithm for volume estimation with short intervals, e.g., cycle-by-cycle estimation, through data fusion of both historical data and real-time data. Such real-time volume estimation is critical for adaptive signal control, and will be one of the focuses of our future work. In addition, the proposed estimation is sensitive to interrupted traffic from adjacent parking lots or driveways which introduce significant noises to the vehicle trajectories. Thus, the proposed algorithm is mostly suitable for estimation at signalized intersections where no sink/source exists nearby the stop bar. Also, due to the assumption that no residual queue exists at start of signal cycles, the proposed approach is not suitable for estimation with over-saturated traffic conditions. We intend to address these limitations in our future work. Lastly, while the current focus is on estimating traffic arrival information, developing systematic approaches for traffic signal re-timing, regarding offsets, green splits, and cycle lengths as well as time-of-day schedules, will be another focus of our future work.

## Acknowledgment

Partial funding for this research was provided by the Department of Energy under Award No. DE-EE0007212. The views expressed in this paper are those of the authors alone.

## References

Abbas, M., Bullock, D., Head, L., 2001. Real-time offset transitioning algorithm for coordinating traffic signals. Transport. Res. Rec.: J. Transport. Res. Board (1748), 26-39.
Agbolosu-Amison, S.J., Park, B., Center, M.-A.U.T., 2008. Performance evaluation of dynamic gap-out feature using stochastic optimization method and software in the loop simulation. Technical report, Mid-Atlantic Universities Transportation Center.
Ban, X., Gruteser, M., 2010. Mobile sensors as traffic probes: addressing transportation modeling and privacy protection in an integrated framework. In: Traffic and Transportation Studies 2010, pp. 750-767.
Ban, X., Herring, R., Hao, P., Bayen, A., 2009. Delay pattern estimation for signalized intersections using sampled travel times. Transport. Res. Rec.: J. Transport. Res. Board (2130), 109-119.
Ban, X.J., Hao, P., Sun, Z., 2011. Real time queue length estimation for signalized intersections using travel times from mobile sensors. Transport. Res. Part C: Emerging Technol. 19 (6), 1133-1156.
Bhaskar, A., Chung, E., Dumont, A.-G., 2011. Fusing loop detector and probe vehicle data to estimate travel time statistics on signalized urban networks. Comput.-Aid. Civil Infrastruct. Eng. 26 (6), 433-450.
Bilmes, J.A. et al, 1998. A gentle tutorial of the em algorithm and its application to parameter estimation for gaussian mixture and hidden markov models. Int. Comput. Sci. Inst. 4 (510), 126.
Cetin, M., 2012. Estimating queue dynamics at signalized intersections from probe vehicle data: Methodology based on kinematic wave model. Transport. Res. Rec.: J. Transport. Res. Board (2315), 164-172.
Chen, M., Chien, S., 2001. Dynamic freeway travel-time prediction with probe vehicle data: link based versus path based. Transport. Res. Rec.: J. Transport. Res. Board (1768), 157-161.
Christofa, E., Argote, J., Skabardonis, A., 2013. Arterial queue spillback detection and signal control based on connected vehicle technology. Transport. Res. Rec.: J. Transport. Res. Board (2356), 61-70.
Comert, G., 2013. Simple analytical models for estimating the queue lengths from probe vehicles at traffic signals. Transport. Res. Part B: Methodol. 55, 59-74.
Comert, G., 2016. Queue length estimation from probe vehicles at isolated intersections: estimators for primary parameters. Eur. J. Oper. Res. 252 (2), 502-521.
Comert, G., Cetin, M., 2009. Queue length estimation from probe vehicle location and the impacts of sample size. Eur. J. Oper. Res. 197 (1), 196-202. Daganzo, C.F., 2005. A variational formulation of kinematic waves: basic theory and complex boundary conditions. Transport. Res. Part B: Methodol. 39 (2), 187-196.
Day, C.M., Bullock, D.M., 2016. Opportunities for detector-free signal offset optimization with limited connected vehicle market penetration: a proof-of-concept study. Transport. Res. Rec.

Feng, Y., Head, K.L., Khoshmagham, S., Zamanipour, M., 2015. A real-time adaptive signal control in a connected vehicle environment. Transport. Res. Part C: Emerging Technol. 55, 460-473.
Gay, K., Kniss, V., 2015. Safety pilot model deployment lessons learned and recommendations for future connected vehicle activities. Technical report, USDOT FHWA-JPO-16-363.
Goodall, N.J., Smith, B.L., Park, B., 2016. Microscopic estimation of freeway vehicle positions from the behavior of connected vehicles. J. Intell. Transport. Syst. 20 (1), 45-54.
Guler, S.I., Menendez, M., Meier, L., 2014. Using connected vehicle technology to improve the efficiency of intersections. Transport. Res. Part C: Emerging Technol. 46, 121-131.
Hao, P., Ban, X., Whon Yu, J., 2015. Kinematic equation-based vehicle queue location estimation method for signalized intersections using mobile sensor data. J. Intell. Transport. Syst. 19 (3), 256-272.
Hao, P., Ban, X.J., Guo, D., Ji, Q., 2014. Cycle-by-cycle intersection queue length distribution estimation using sample travel times. Transport. Res. Part B: Methodol. 68, 185-204.
Hao, P., Sun, Z., Ban, X.J., Guo, D., Ji, Q., 2013. Vehicle index estimation for signalized intersections using sample travel times. Transport. Res. Part C: Emerging Technol. 36, 513-529.
He, Q., Head, K.L., Ding, J., 2012. Pamscod: Platoon-based arterial multi-modal signal control with online data. Transport. Res. Part C: Emerging Technol. 20 (1), 164-184.
He, Q., Head, K.L., Ding, J., 2014. Multi-modal traffic signal control with priority, signal actuation and coordination. Transport. Res. Part C: Emerging Technol. 46, 65-82.
Hellinga, B.R., Fu, L., 2002. Reducing bias in probe-based arterial link travel time estimates. Transport. Res. Part C: Emerging Technol. 10 (4), 257-273.
Herrera, J.C., Work, D.B., Herring, R., Ban, X.J., Jacobson, Q., Bayen, A.M., 2010. Evaluation of traffic data obtained via gps-enabled mobile phones: the mobile century field experiment. Transport. Res. Part C: Emerging Technol. 18 (4), 568-583.
Hoh, B., Gruteser, M., Herring, R., Ban, J., Work, D., Herrera, J.-C., Bayen, A.M., Annavaram, M., Jacobson, Q., 2008. Virtual trip lines for distributed privacy-preserving traffic monitoring. In: Proceedings of the 6th International Conference on Mobile Systems, Applications, and Services. ACM, pp. 15-28.
Jenelius, E., Koutsopoulos, H.N., 2013. Travel time estimation for urban road networks using low frequency probe vehicle data. Transport. Res. Part B: Methodol. 53, 64-81.
Lee, J., Park, B., Yun, I., 2013a. Cumulative travel-time responsive real-time intersection control algorithm in the connected vehicle environment. J. Transport. Eng. 139 (10), 1020-1029.
Lee, J., Park, B.B., Malakorn, K., So, J.J., 2013b. Sustainability assessments of cooperative vehicle intersection control at an urban corridor. Transport. Res. Part C: Emerging Technol. 32, 193-206.
Li, J.-Q., Zhou, K., Shladover, S., Skabardonis, A., 2013. Estimating queue length under connected vehicle technology: using probe vehicle, loop detector, and fused data. Transport. Res. Rec.: J. Transport. Res. Board (2356), 17-22.
Lighthill, M.J., Whitham, G.B., 1955. On kinematic waves. ii. A theory of traffic flow on long crowded roads. Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences, vol. 229. The Royal Society, pp. 317-345.
Long Cheu, R., Xie, C., Lee, D.-H., 2002. Probe vehicle population and sample size for arterial speed estimation. Comput.-Aid. Civil Infrastruct. Eng. 17 (1), 53-60.
Masters, J., 2016. Making the right connections. ITS Int., 9-11
McCracken, J., 1996. Demonstration project 93-making the most of today's technology. Public Roads 59 (3).
Milanés, V., Villagra, J., Godoy, J., Simó, J., Pérez, J., Onieva, E., 2012. An intelligent v2i-based traffic management system. IEEE Trans. Intell. Transport. Syst. 13 (1), 49-58.
Nanthawichit, C., Nakatsuji, T., Suzuki, H., 2003. Application of probe-vehicle data for real-time traffic-state estimation and short-term travel-time prediction on a freeway. Transport. Res. Rec.: J. Transport. Res. Board (1855), 49-59.
NTOC, 2012. 2012 National traffic signal report card.
Richards, P.I., 1956. Shock waves on the highway. Oper. Res. 4 (1), 42-51.
Sun, Z., Ban, X.J., 2013. Vehicle trajectory reconstruction for signalized intersections using mobile traffic sensors. Transport. Res. Part C: Emerging Technol. 36, 268-283.
Sunkari, S., 2004. The benefits of retiming traffic signals. Inst. Transport. Eng. ITE J. 74 (4), 26.
Turner, S.M., Holdener, D.J., 1995. Probe vehicle sample sizes for real-time information: the houston experience. In: Vehicle Navigation and Information Systems Conference, 1995. Proceedings. In conjunction with the Pacific Rim TransTech Conference. 6th International VNIS.'A Ride into the Future'. IEEE, pp. 3-10.
Work, D.B., Tossavainen, O.-P., Blandin, S., Bayen, A.M., Iwuchukwu, T., Tracton, K., 2008. An ensemble kalman filtering approach to highway traffic estimation using gps enabled mobile devices. In: 47th IEEE Conference on Decision and Control, 2008 (CDC 2008). IEEE, pp. 5062-5068.
Zheng, F., Van Zuylen, H., 2013. Urban link travel time estimation based on sparse probe vehicle data. Transport. Res. Part C: Emerging Technol. 31, 145-157.
Zheng, J., Liu, H., Misgen, S., 2015. Fine-tuning time-of-day transitions for arterial traffic signals. Transport. Res. Rec.: J. Transport. Res. Board (2488), 32-40.
Zheng, J., Liu, H., Misgen, S., Schwartz, K., Green, B., Anderson, M., 2014. Use of event-based traffic data in generating time-space diagrams for evaluation of signal coordination. Transport. Res. Rec.: J. Transport. Res. Board (2439), 94-104.


[^0]:    * Corresponding author at: Department of Civil and Environmental Engineering, University of Michigan, United States.
    E-mail address: henryliu@umich.edu (H.X. Liu).
    ${ }^{1}$ Congestion Reduction Toolbox. U.S. DOT FHWA. http://www.fhwa.dot.gov/congestion/toolbox.

[^1]:    ${ }^{2}$ SPMD Project http://safetypilot.umtri.umich.edu/.
    ${ }^{3}$ FHWA Research Data Exchange: www.its-rde.net.

