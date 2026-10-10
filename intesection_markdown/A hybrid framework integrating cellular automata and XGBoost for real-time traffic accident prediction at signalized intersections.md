# A hybrid framework integrating cellular automata and XGBoost for real-time traffic accident prediction at signalized intersections 

A. Ángeles Robles ${ }^{\mathrm{a}}{ }^{\text {® }}$, J. Águila León ${ }^{\mathrm{b}}$ (iD), G.A. Mejía-Pérez ${ }^{\mathrm{c}}$ (bit), B. Castillo-Téllez ${ }^{\mathrm{b}}$ (b), O. Bamaarouf ${ }^{\text {d }}$ ®, O. Oubram ${ }^{\text {a }}$, R. Marzoug ${ }^{\text {e,* }}$ ®<br>${ }^{\mathrm{a}}$ Facultad de Ciencias Químicas e Ingeniería, Universidad Autónoma del Estado de Morelos, Av. Universidad 1001, Col. Chamilpa, Cuernavaca, Morelos, 62209, Mexico<br>${ }^{\mathrm{b}}$ Centro Universitario de Tonalá, Universidad de Guadalajara, Tonalá, Jalisco, Mexico<br>${ }^{\mathrm{c}}$ Centro Universitario de Tlaquepaque, Universidad de Guadalajara, Tlaquepaque, Jalisco, Mexico<br>${ }^{\mathrm{d}}$ Interdisciplinary Applied Research Laboratory, International University of Agadir- Universiapolis, Agadir, 80000, Morocco<br>${ }^{\mathrm{e}}$ Centro Universitario del Norte, Universidad de Guadalajara, Colotlán, Jalisco, Mexico

## ARTICLE INFO

Keywords:
Urban road safety
Red-light running
Ensemble learning
Nonlinear dynamic
Predictive safety systems
Intelligent transportation systems


#### Abstract

Traffic accidents at signalized intersections constitute a major public safety concern, representing a significant proportion of urban road fatalities worldwide. Machine learning methods have been applied to accident prediction; however, most existing approaches depend on large-scale real-world datasets, focus on freeway segments rather than intersections, and operate at spatial and temporal resolutions that constrain their applicability for real-time event-level prediction. This paper presents a novel framework integrating a Cellular Automata (CA) traffic simulation model with an XGBoost (eXtreme Gradient Boosting) binary classifier for individual-event accident prediction at signalized intersections. The CA model enables the controlled generation of feature-rich data including heterogeneous vehicular dynamics and red-light running. The framework employs a sliding temporal window to extract features from simulation data for a 30-s prediction horizon. The proposed model achieves an accuracy of 0.86, a recall of 0.966, and an AUC of 0.91 on the test set, outperforming baseline models such as K-Nearest Neighbors and Long Short-Term Memory networks. The high recall is particularly important in safety-critical applications, as it minimizes undetected accident events. The results show that integrating simulation-based traffic modeling with machine learning enables efficient accident prediction at intersections and offers a viable alternative to sensor-based approaches for intelligent traffic management systems.


## 1. Introduction

Road traffic accidents represent a major public safety concern worldwide. According to the Global Status Report on Road Safety 2023, approximately 1.19 million fatalities occur each year due to road traffic crashes, with injuries remaining the leading cause of death among children and young people aged 5 to 29 years [1]. Beyond the human toll, traffic accidents impose substantial economic burdens on health systems and transportation infrastructure, underscoring the need for tools that support early risk detection and preventive intervention. Accident analysis and prediction have been the focus of extensive research over recent decades [2,3]. Models for traffic accident prediction are broadly classified into two categories: statistical methods and machine learning models. Statistical approaches, including logistic regression and logit models, provide interpretable frameworks but exhibit limitations in handling complex nonlinear interactions between variables, capturing temporal dynamics, and satisfying the distributional assumptions required for valid inference [4]. These constraints have motivated the adoption of machine learning techniques, which offer greater flexibility in modeling the high-dimensional, nonlinear relationships inherent in traffic data [5,6].

Beyond accident prediction, machine learning and deep learning techniques have been applied across a broad spectrum of traffic problems, including congestion forecasting [7-9], traffic signal optimization at signalized intersections [10], and neural network optimization [11], while complementary reviews have systematically surveyed machine learning algorithms for crash injury severity prediction [12].

A broad range of machine learning architectures has been applied to accident prediction with varying degrees of success. Alkheder et al. [13] applied an artificial neural network (ANN) to predict injury severity in

[^0]Abu Dhabi, achieving an accuracy of 74.6\% compared to 59.5\% for an ordered probit model. Similarly, Chong et al. [14] combined ANNs and decision trees to model injury severity from accident records, while Masood et al. [15] employed a convolutional neural network (CNN) specifically, to detect distracted driving from in-vehicle camera images. Regarding infrastructure, Mussone et al. [16] applied ANNs to intersection-related accidents in Milan, identifying nighttime non-signalized intersections as the highest-risk configuration for pedestrian collisions.

Recent studies have increasingly shifted toward real-time applications. Formosa et al. [17] used a deep learning model to forecast traffic conflicts on the M1 motorway, achieving 94\% accuracy by incorporating time-to-collision, traffic density, and speed as inputs. In terms of sequential modeling, Yuan et al. [18] implemented an LSTM model for real-time crash risk prediction, reporting a sensitivity of 60.67\%, outperforming conditional logistic regression. To address spatial complexity, Moosavi et al. [19] developed a deep neural network integrating recurrent, fully connected, and embedding layers for large-scale urban accident prediction, while Bao et al. [20] proposed a spatiotemporal convolutional LSTM network for citywide crash frequency prediction that incorporates taxi trip data, road network features, and land use patterns. More recently, hybrid approaches have gained prominence; Kashifi et al. [21] combined CNN, LSTM, and DNN into a deep hybrid network for spatiotemporal crash prediction at 1 km grid resolution across Chicago, achieving an accuracy of 0.72. Jin and Noh [22] introduced a CNN-DNN model with an accident risk index, attaining accuracy above 80\%. Li et al. [23] developed a real-time crash risk model for urban arterials based on an LSTM-CNN architecture, reporting an outstanding AUC of 0.93.

A distinct strand of real-time research focuses specifically on signalized intersections and adopts extreme value theory to quantify crash risk at the signal-cycle level. Zheng and Sayed [24] estimated real-time crash risk at signalized intersections from the extremes of traffic conflicts using generalized extreme value models, and Ali et al. [25] proposed a Bayesian generalized extreme value formulation that derives rear-end crash risk in real time from conflict indicators, incorporating traffic volume as a covariate and accounting for unobserved heterogeneity. Building on this line, Hussain et al. [26] developed a bilevel framework that couples a non-stationary Bayesian generalized extreme value model with a recurrent neural network to forecast risk for subsequent signal cycles. These approaches share the intersection setting addressed here, but they quantify aggregated crash risk from surrogate conflicts at the cycle level rather than classifying the occurrence of individual crash events, and they rely on trajectory and conflict data collected in the field. In parallel, studies on crash outcome modeling in other vehicular safety domains have emphasized the strong class imbalance of real-world records; for instance, in the context of autonomous vehicle safety, Channamallu et al. [27] compared ensemble methods with class-weighting strategies and found that random forests balance sensitivity and specificity to limit missed events.

Despite these advances, several limitations persist in the literature. First, most real-time crash risk prediction studies focus predominantly on freeway segments [28-30], with comparatively few addressing signalized intersections, where crossing traffic flows create distinct and complex conflict patterns [31]. Second, spatial prediction at grid-cell resolution (e.g., $1 \mathrm{~km}^{2}, 5 \mathrm{~km}^{2}$ ) [32-34] provides only aggregate risk estimates over large areas, thereby hindering the identification of precise accident locations. Furthermore, studies operating at a daily temporal resolution lack the necessary granularity for real-time traffic management applications [19,21,22,32]. Approaches focused on arterial roads [23] and statistical intersection models [33] share analogous limitations in both temporal granularity and individual-event resolution.

A further challenge is the inherent scarcity of labeled accident data. Traffic accidents are inherently rare events, and detailed sensor-level records-including individual vehicle speed, acceleration, and lane- change behavior-are rarely available in conjunction with crash logs [34,35]. Large-scale traffic databases are often subject to confidentiality constraints, contain outdated records, or lack contextual variables required for intersection-level risk assessment. Furthermore, most sensors capture macroscopic aggregates, such as flow and average speed, rather than the microscopic state variables underlying individual accident events. Traffic simulation therefore provides a compelling and tractable alternative: it enables the controlled generation of both accident and non-accident events under diverse traffic conditions, producing the feature-rich datasets essential for individual-event prediction.

Since the 1990s, cellular automata (CA) models have been widely employed to simulate vehicular traffic dynamics due to their ability to reproduce emergent macroscopic behavior from simple local update rules [36,37]. The pioneering Nagel-Schreckenberg (NaSch) model [38-40] established the foundational framework for one-dimensional traffic CA, with subsequent extensions addressing multi-lane dynamics, heterogeneous vehicle populations, and adverse environmental conditions. Within this framework, Boccara et al. [41] derived conditions for rear-end collisions in the deterministic NaSch model, a study further extended by Huang and Tseng [42] extended this analysis using a mean-field approach. Similarly, Pang et al. investigated accident dynamics under low-visibility and rainy conditions on both three-lane [43] and two-lane [44] freeways. Others CA studies have examined the modulation of accident probability by a localized roadway defect [45], and accident dynamics between adjacent signalized intersections in the presence of bus stops with left-turn lanes [46].

Regarding signalized intersections, Chang and Xiang [47] demonstrated that collisions in these environments are typically more severe than midblock crashes, while Wang and Abdel-Aty [48] identified red-light running as a primary cause of right-angle crashes. More recently, Marzoug et al. [31] proposed a two-lane CA model specifically designed to investigate the relationship between traffic parameters and accident likelihood at signalized intersections.

The integration of CA with machine learning has been explored in diverse domains. Li and Yeh [49,50] and Almeida et al. [51] applied neural networks to CA-based urban growth simulation, while Liu and Shi [52] incorporated a backpropagation network into a CA traffic flow model to predict lane changes with high accuracy. Furthermore, Kim and Kim [53] demonstrated that a CA-ANN collaborative model produces reliable predictions of traffic congestion. Cellular automata have also been employed directly as pattern classifiers, as in the cellular-automata-based classifier with a variance decision table proposed by Wanna and Wongthanavasu [54].

To the best of the authors' knowledge, no prior study has combined CA-based intersection modeling with machine learning for individualevent accident prediction at signalized intersections.

Two recent developments in the literature further motivate the proposed framework. First, boosted tree ensembles have become increasingly popular in traffic safety research, and hybrid formulations have emerged in which metaheuristic optimization techniques are used to tune XGBoost classifiers for crash severity prediction, as reported by Chen et al. [55]. Second, recent studies have explored the generation of training data through traffic simulation rather than field sensors. For example, Qu et al. [56] proposed a digital-twin framework that reproduces expressway traffic in a microsimulation environment and trains boosted tree models using simulated crash scenarios. However, these studies focus on crash severity assessment or post-event detection on freeways and expressways rather than short-horizon prediction of individual crash occurrence at signalized intersections from simulation-generated data.

This paper presents a framework that integrates a CA traffic simulation model with an XGBoost binary classifier for short-horizon accident risk prediction at signalized intersections. The primary contributions of this work are as follows:

- A two-lane CA intersection model that simulates heterogeneous vehicular dynamics-including lane-changing behavior, traffic signal control, and red-light running-under open boundary conditions.
- A sliding temporal window procedure that extracts 18 traffic features from simulation data over a 30-s observation window to characterize pre-accident traffic states.
- A labeled dataset of 13,504 balanced samples generated across 147 simulated scenarios covering free flow, congested, and jammed traffic phases.
- An XGBoost classifier trained on the generated dataset and evaluated against K-Nearest Neighbors and LSTM baselines, achieving an accuracy of 0.86, a recall of 0.966, and an AUC of 0.91 on the test set.

The remainder of this paper is organized as follows. Section 2 describes the methodology, including the CA model, the feature extraction procedure, the XGBoost classifier, and the simulation parameters and dataset. Section 3 presents the results and discussion, while section 4 outlines the conclusions and future work.

## 2. Materials and methods

In the present study, the prediction of vehicular accidents at intersections is addressed through a novel framework that integrates Cellular Automata (CA) simulation with Machine Learning (ML). The proposed methodology captures the stochastic and non-linear complexities of vehicular behavior at road intersections, enabling a datadriven approach to accident prevention at signalized intersections. Fig. 1 illustrates the general architectural workflow of this work and its constituent stages.

Fig. 1 summarizes the three-stage architecture of the proposed framework. Stage 1 encompasses the CA intersection model, the vehicle dynamics rules, and the simulation scenarios designed to generate the raw traffic data. Stage 2 covers the sliding temporal window procedure, the correlation-based feature selection, and the construction of the balanced dataset. Finally, stage 3 presents the XGBoost classifier, the baseline models, and the evaluation protocol. The following subsections detail each stage according to the proposed workflow.

### 2.1. Cellular automata traffic model

The CA traffic model constitutes the first stage of the proposed framework. Its primary objective is to simulate microscopic vehicular dynamics at a signalized intersection under heterogeneous traffic conditions, thereby generating the accident and non-accident events required to construct the feature dataset. The model is characterized by a specific intersection geometry, a set of vehicle update rules based on the NaSch formulation, lane-changing logic, and a traffic signal control mechanism that explicitly incorporates red-light running behaviors. Each of these components is detailed in the following subsections.

### 2.1.1. Intersection geometry and traffic dynamic

The intersection comprises two perpendicular two-lane roads of equal length L, crossing at the center as shown in Fig. 2. Traffic on road $\mathrm{R}_{1}$ flows from north to south, while on road $\mathrm{R}_{2}$, it moves from west to east, both subsystems operate under open boundary conditions. Vehicles enter roads $\mathrm{R}_{1}$ and $\mathrm{R}_{2}$ with injection rates $\alpha_{1}$ and $\alpha_{2}$, respectively, and exit with an extraction rate $\beta$.

Each lane on both roads is divided into identical cells of equal size. The intersection conflict area can accommodate up to four vehicles simultaneously. Vehicles can move at discrete speed values, from 0 to a maximum speed $v_{\text {max }}$ t each time step, the speed $v_{i}(t)$ and position $x_{i}(t)$ of the i-th vehicle are updated. The available space (headway) in front of the i-th vehicle is defined as $d_{i}=\left(x_{i+1}(t)-x_{i(t)}\right)-1$ This headway definition follows the cellular automaton model of Nagel and Schreckenberg [40,57]. Furthermore, the distance to the intersection entry point for vehicles on roads $\mathrm{R}_{1}$ and $\mathrm{R}_{2}$ is denoted as $\mathrm{g}_{1}$ and $\mathrm{g}_{2}$, respectively, as shown in Fig. 2.

Vehicle dynamics - NaSch update rules.
The vehicle position at time $t+1$ is updated according to the following steps from the NaSch model applied in parallel [38-40,57]:

Step1: Acceleration: If $v_{i}^{\prime}=\min \left(v_{i}(t)+1, v_{\text {max }}\right)$

The vehicle's speed increases by 1 unit, limited by the maximum speed.

Step 2: Deceleration (collision avoidance):

![](https://cdn.mathpix.com/cropped/4a4d610a-c6f6-4d67-b0d9-9a92cb6a133b-03.jpg?height=792&width=1496&top_left_y=1690&top_left_x=282)
Fig. 1. The general architectural workflow of this work.

![](https://cdn.mathpix.com/cropped/4a4d610a-c6f6-4d67-b0d9-9a92cb6a133b-04.jpg?height=1098&width=1199&top_left_y=189&top_left_x=433)
Fig. 2. The scheme of the signalized intersection.

If $v_{i}^{\prime}>d_{i}: v_{i}^{\prime \prime}=\min \left(d_{i}, v_{i}^{\prime}\right)$.
$d_{i}$ represents the gap between the current vehicle and the one ahead. The vehicle adjusts its speed to avoid collisions by decelerating when necessary.

Step 3: Randomization (Stochastic braking):
If $v_{i}^{\prime \prime}>0$ so: $v_{i}(t+1)=v_{i}^{\prime \prime}-1$, with a braking probability $P_{b}$, or $v_{i}(t+1)=v_{i}^{\prime \prime}$ with a probability $1-P_{b}$.

Step 4: Position Update:

Finally, the position of the vehicle is updated according to its new speed:

$$
x_{i}(t+1)=x_{i}(t)+v_{i}(t+1)
$$

At the road's end, if $v_{i}(t+1)-x_{i}(t)>L$, the vehicle can exit the system with probability $\beta$, otherwise, it slows down and its speed becomes $v_{i}(t+1)=L-x_{i}(t)$, with the probability $1-\beta$.
2.1.2. Heterogeneous traffic and lane-changing rules

In this study, traffic is modeled as heterogeneous by incorporating two types of vehicles, differentiated by their maximum speeds: slow vehicles $\left(v_{\text {smax }}\right)$ and fast vehicles $\left(v_{\text {fmax }}\right)$. The proportion of fast and slow vehicles is represented by $P_{f}$ and $P_{s}$, respectively, where $P_{f}=1-P_{s}$.

Drivers switch lanes to either maintain the highest possible speed or to avoid obstacles or incidents. Lane-changing rules can generally be classified as symmetric or asymmetric, depending on the vehicles or the lanes involved. Symmetric rules treat both lanes and all vehicles equivalently. In contrast, asymmetric rules account for differences based on lane (e.g., left or right) and vehicle type (e.g., cars or trucks). Additionally, lane changes are permitted only when certain safety criteria are met.

The system evolution follows a two-stage update process. In the first sub-step, vehicles adjust their speed according to the NaSch model. In the second sub-step, they are allowed to change lanes if the lanechanging rules are satisfied. Both processes are applied simultaneously to all vehicles. Lane changes are governed by the following rules [58]:

Symmetric rules (applicable to both vehicle types and lanes):

1) The gap ahead in the current lane $\left(g_{c}\right)$ is smaller than $v_{i}+1$,
2) The gap ahead in the adjacent lane ( $g_{o}$ ) is greater than that in the current lane ( $g_{c}$ ),
3) The adjacent position in the other lane is empty, and
4) The maximum speed of the vehicle behind in the adjacent lane is less than the gap between the two vehicles $\left(g_{b}\right)$.

In the asymmetric model, the lane-changing rules depend on both the vehicle type (slow or fast) and the current lane occupancy (right or left). A vehicle initiates a lane-change maneuver when all the following conditions are met:

1) The gap ahead in the current lane is smaller than $v_{i}+1$, or, if the vehicle is fast and finds a slower vehicle within a distance shorter than $v_{\text {max }}$ ).
2) The gap in the left lane is larger than the gap in the right lane,
3) The adjacent position in the left lane is unoccupied, and
4) The maximum speed of the vehicle behind in the left lane is less than the available gap between the two vehicles.

2.1.3. Traffic signal control and accident definition

The intersection is controlled by traffic lights that alternate priority between roads $R_{1}$ and $R_{2}$. Specifically, $R_{1}$ is assigned priority (green light) for a duration $T_{g 1}$, during which $R_{2}$ faces a red light. Subsequently,
$R_{1}$ receives the red light (and $R_{2}$ the green light) for a duration $T_{g 2}$. During the red phase, vehicles are required to stop, adjusting their speed to $v_{i}=\min \left(v_{i}, g_{i}\right)$, where $g_{i}$ denotes the distance to the intersection's stop line. Additionally, during yellow phase, vehicles undergo stochastic deceleration and stop at the intersection with a probability $P_{y}$.

In practice, red-light running (RLR) is a prevalent violation [59,60], particularly during the yellow-to-red transition. In this model, we explicitly incorporate RLR behavior: drivers may encroach upon the intersection when the opposing road is in its yellow phase with a probability $P_{\text {RLR }}$, thereby introducing the risk of right-angle (side-impact) collisions. This behavior models the tendency of some drivers to start moving before their light turns green or to clear the intersection late.

An accident is formally defined as a spatio-temporal conflict where vehicles from conflicting roads simultaneously occupy the same intersection cell. This is represented by the condition $t_{1}=t_{2}$, where $t_{1,2}=$ $g_{1,2} / v_{1,2}$, is the Time-to-Reach-Intersection (TRI) for vehicles on $\mathrm{R}_{1}$ and $\mathrm{R}_{2}$ respectively. This criterion is equivalent to a Time-To-Collision (TTC) of zero, which corresponds to the most severe endpoint of the surrogate safety measures (SSMs) conflict severity spectrum [61,62]. Although continuous-domain SSMs such as TET and TIT offer richer conflict quantification, the discrete CA lattice does not support sub-cell resolution; the binary TRI condition therefore represents the most rigorous conflict criterion achievable within this framework, consistent with prior CA accident studies. Moreover, accidents can occur at any of the four sites of the intersection.

### 2.2. Feature extraction

The second stage of the framework is dedicated to extracting features from the raw simulation output generated by the CA model. A sliding temporal window procedure is applied to the time series of traffic states, segmenting the data into fixed-length observation intervals. Subsequently, a binary label is assigned to each interval based on whether an accident occurs within a defined prediction horizon. This approach transforms the continuous simulation output into a structured tabular dataset suitable for supervised binary classification. The mathematical formulation of the window and the dimensionality of extracted features are described in the following subsections.

### 2.2.1. Sliding window formulation

We implemented a sliding temporal window technique to segment the multivariate time series, allowing for the extraction of local features representative of the dynamic traffic process, in line with real-time crash risk studies that derive traffic features over temporal observation windows [4,18]. This approach captures the temporal evolution of the traffic states, enabling the identification of pre-accident risk patterns through sequential observations.

Let $F_{t}^{(s)}$ denote the feature vector describing the traffic characteristics at time $t$ of simulation $s$, where $s \epsilon\{1,2, \ldots, S\}$. $S$ represents the total number of simulated scenarios, and $t \in\{1,2, \ldots, T\}$ denotes the discrete time steps within a simulation of total duration $T$.

For each simulation $s$, a time series of system states is defined as:

$$
F^{(s)}=\left\{F_{1}^{(s)}, F_{2}^{(s)}, \ldots, F_{T}^{(s)}\right\}
$$

Each time window $W_{t}$ is characterized by three fundamental parameters:

- Observation window $\left(T_{\text {obs }}\right)$ : The time period during which data from the system is collected.
- Prediction horizon $\left(T_{\text {hor }}\right)$ : The future time interval used to assess accident occurrence.
- Sliding step $(\Delta t)$ : The time offset between consecutive windows (set to 1 s in this study).

Formally, the window $W_{t}$ at time $t_{k}$ is represented as the sequence of feature vectors:

$$
W_{t}=\left\{F_{t-T_{o b s}+1}^{(s)}, \ldots, F_{t}^{(s)}\right\}
$$

Each time window $W_{t}$ is assigned a binary label $y_{t} \in\{0,1\}$ denoting the accident status within the prediction horizon:
$y_{t}=1$ : if an accident occurs in the time interval $\left[t, t+T_{\text {hor }}\right]$
$y_{t}=0$ : if no accident occurs within this specific interval.
Consequently, for each time step $t$ within simulation $s$ :

1. Observations are extracted from the interval $\left[t_{k}, t_{k}+T_{\text {obs }}\right]$.
2. Aggregate features are computed over this window to form the vector $F_{t}^{(s)}$.
3. Accident occurrence is verified within the future interval $\left[t, t+T_{\text {hor }}\right]$.
4. The corresponding label is assigned ( $y_{t}=0$ or $y_{t}=1$ ).

### 2.2.2. Extracted feature set

For each window $W_{t}$, the following 18 traffic-related features are extracted:
$\mu_{v_{1}}, \mu_{v_{2}}$ : Mean speed in the 70 sites upstream of the intersection in $R_{1}$ and $R_{2}$.
$\sigma_{v_{1}}, \sigma_{v_{2}}$ : Standard deviation of speed in the 70 sites upstream of the intersection in $R_{1}$ and $R_{2}$.
$\mu_{h_{1}}, \mu_{h_{2}}$ : Space headway between vehicles in the 70 sites upstream of the intersection in $R_{1}$ and $R_{2}$.
$\sigma_{h_{1}}, \sigma_{h_{2}}$ : Standard deviation of space headway $h_{1,2}$ in the 70 sites upstream of the intersection in $R_{1}$ and $R_{2}$.
$N_{11}$ : Number of vehicles in the 70 sites upstream of the intersection in $R_{1}$.
$N_{12}$ : Number of vehicles in the 70 sites downstream of the intersection in $R_{1}$.
$N_{21}$ : Number of vehicles in the 70 sites upstream of the intersection in $R_{2}$.
$N_{22}$ : Number of vehicles in the 70 sites downstream of the intersection in $R_{2}$.
$\alpha_{1}, \alpha_{2}$ : Vehicle inflow (injection) probability in $R_{1}$ and $R_{2}$.
$\mu_{c h g_{1}}, \mu_{c h g_{2}}$ : Mean number of lane changes in the 70 sites upstream of the intersection in $R_{1}$ and $R_{2}$.
$\sigma_{\text {chg }_{1}}, \sigma_{\text {chg }_{2}}$ : Standard deviation of the number of lane changes in the 70 sites upstream of the intersection in $R_{1}$ and $R_{2}$.

A 70-cell observation window was established to encompass the intersection's functional area of influence, ensuring that the input features reflect the spatial evolution of traffic states rather than localized stochastic noise.

### 2.3. XGBoost classifier

This section details the design and implementation of the Extreme Gradient Boosting (XGBoost) classifier integrated into the framework to predict vehicular accidents. The model leverages gradient-boosted decision trees to capture the complex, high-dimensional, and nonlinear relationships inherent in the traffic data generated by the CA simulations. Fig. 3 illustrates the hierarchical architecture of the XGBoost learning process.

XGBoost was selected as the primary classifier due to its ability to model complex nonlinear relationships, its strong performance on structured tabular datasets, and its built-in regularization mechanisms that help prevent overfitting. In addition, XGBoost provides interpretable feature importance measures, facilitating the identification of traffic variables associated with accident occurrence. These characteristics, together with its low computational cost and successful application in previous traffic safety studies, make it well suited for the proposed accident prediction framework.

![](https://cdn.mathpix.com/cropped/4a4d610a-c6f6-4d67-b0d9-9a92cb6a133b-06.jpg?height=420&width=1376&top_left_y=194&top_left_x=355)
Fig. 3. Integrated XGBoost Classifier Model Architecture. The model receives a vector of 18 traffic features (generated by the Cellular Automata model).

### 2.3.1. Model formulation

The input layer receives a feature vector $\mathrm{X} \in \mathrm{R}^{\mathrm{n}}$, where $\mathrm{n}=18$ represents the total number of traffic parameters derived from the CA model. The input feature space comprises the variables described above, calculated for both roads $\mathrm{R}_{1}$ and $\mathrm{R}_{1}$ :

- Velocity profiles: $\left\{\mu_{v_{1}}, \mu_{v_{2}}, \sigma_{v_{1}}, \sigma_{v_{2}}\right\}$
- Spatial gaps: $\left\{\mu_{h_{1}}, \mu_{h_{2}}, \sigma_{h_{1}}, \sigma_{h_{2}}\right\}$
- Inflow dynamics: $\left\{\alpha_{1}, \alpha_{2}\right\}$
- Traffic density: $\left\{N_{11}, N_{12}, N_{21}, N_{22}\right\}$
- Lane-changing behavior: $\left\{\mu_{c h g_{1}}, \mu_{c h g_{2}}, \sigma_{c h g_{1}}, \sigma_{c h g_{2}}\right\}$

In total, the input layer consists of 18 features, and the model outputs a single binary value representing the predicted occurrence or nonoccurrence of a vehicular accident within the subsequent 30-s prediction horizon.

The prediction is executed using the XGBoost (eXtreme Gradient Boosting) classifier. This model utilizes an additive ensemble technique that sequentially constructs a series of $K$ decision trees $f_{k}(\boldsymbol{x})$. Each successive tree is fitted to minimize the residual errors of the preceding ensemble, thereby progressively improving the model's predictive performance [63].

The final prediction of the model, $\widehat{y}$, is obtained as a weighted sum of the outputs from all individual trees:

$$
\widehat{y}_{i}=\sum_{k=1}^{K} \eta f_{k}\left(F_{i}\right)
$$

Where $\eta$ is the learning rate (set to 0.1), which scales the contribution of each tree to mitigate overfitting. The model architecture is configured with $K=30$ estimators, a learning rate $\eta=0.1$, and a maximum tree depth of 3.

During training, the model minimizes a regularized objective function based on the binary log-likelihood loss. The final raw output is processed using the logistic (sigmoid) function to generate a probability $P\left(y_{i}=1 \mid F_{i}\right)$, which is crucial for evaluating the model's discriminative capability.

### 2.3.2. Hyperparameter selection and justification

The XGBoost classifier was configured with three primary hyperparameters: $K=30$, learning rate $\eta=0.1$, and $\max _{\text {depth }}=3$. The selection of these values reflects a deliberate balance between model expressiveness and the risk of overfitting on a moderately sized dataset of 13,504 samples.

The number of estimators ( $K$ ) determines the total number of decision trees constructed sequentially. A small ensemble reduces the probability that later trees overfit residuals that arise from noise rather than from genuine signal in the feature space. The dataset generated here, while balanced and preprocessed, derives from a simulation model with a fixed set of stochastic parameters; an excessively large ensemble would risk memorizing simulation-specific patterns that do not generalize to alternative parameterizations. A value of 30 was found sufficient to achieve stable validation performance without requiring regularization-driven early stopping.

The learning rate $\eta=0.1$ scales the contribution of each tree to the ensemble prediction, controlling the gradient descent step size in the function space. Lower values of $\eta$ require more estimators to achieve equivalent training loss but produce smoother loss surfaces and reduce sensitivity to individual trees that fit noise. The combination $\eta=0.1$ and $K=30$ is consistent with the conservative regime recommended for small-to-medium datasets, where the priority is generalization rather than training loss minimization [63].

The maximum tree depth $\left(\right.$ max $\left._{\text {depth }}=3\right)$ limits the number of consecutive binary splits in each tree, thereby constraining the complexity of the interactions that any individual tree can capture. A depth of 3 permits up to eight leaf nodes, which is sufficient to model high order interactions among the 18 input features while preventing the construction of trees that partition the training set into excessively sparse regions. Furthermore, shallow trees improve model interpretability, ensuring that feature importance scores remain physically meaningful.

These 18 features constitute the initial extraction set. A subsequent feature selection procedure, described in Section 3.2, reduces this set to the 9 most discriminative predictors used as the final input to all classifiers.

The hyperparameters were selected through a grid search procedure over a validation set (10\% of the total dataset, approx. 1350 samples). Table 1 lists the candidate values evaluated for each hyperparameter.

### 2.4. Simulation scenarios and dataset

This subsection describes the simulation protocol used to generate the dataset, the structure of the collected data, and the preprocessing steps applied prior to classification. The parameter space was designed to cover the full range of traffic phases, from unrestricted free flow to saturated jam conditions.

### 2.4.1. Simulation scenarios

The simulation environment is defined by a road segment of length $L=500$ cells. To model diverse driving dynamics, maximum velocities are set at $v_{\text {fmax }}=3$ and $v_{\text {smax }}=2$ for fast and slow vehicles, respectively. Vehicle heterogeneity is explicitly captured by a population proportion of $P_{f}=0.8$ for fast vehicles. Furthermore, driver behavior is characterized by a lane-changing probability $P_{c h g}=0.8$, reflecting the aggressive

Table 1
Candidate values evaluated during hyperparameter grid search.
| Hyperparameter | Candidates evaluated | Selected value |
| :--- | :--- | :--- |
| $K$ | 20, 30, 50, 100 | 30 |
| $\eta$ | 0.01, 0.05, 0.1, 0.2 | 0.1 |
| $\max _{\text {depth }}$ | 2, 3, 4, 5 | 3 |


maneuvers typical of congested urban environments. To account for stochastic deceleration and driver variability, a braking probability of $P_{b}=0.1$ is integrated into the movement rules.

A primary challenge in accident prediction is the inherent scarcity of accident events. In real-world settings, collecting sufficient accident data alongside high-resolution traffic flow information requires extensive time and significant hardware resources. To overcome this data sparsity, we utilized the CA model to generate a comprehensive dataset of accident and non-accident events under controlled conditions.

To capture the entire spectrum of traffic dynamics, the injection rates $\alpha_{1}$ and $\alpha_{2}$, were systematically varied to reflect different traffic phases, including free flow, congested and jammed states. Furthermore, inflow asymmetry was incorporated, where $\alpha_{1}$ and $\alpha_{2}$ are not necessarily identical. The specific values evaluated for the injection rates were: \{0.05, 0.1, 0.3, 0.5, 0.7, 0.9, 1\}.

Furthermore, the impact of traffic light cycles was analyzed under both symmetric $\left(T_{g 1}=T_{g 2}\right)$ and asymmetric $\left(T_{g 1} \neq T_{g 2}\right)$ timing regimes. Three timing combinations were analyzed: $T_{g 1}=T_{g 2}=20 s, T_{g 1}=$ $T_{g 2}=40 s$, and $T_{g 1}=40 s$ with $T_{g 2}=20 s . T_{r 1,2}=T_{g 2,1}+T_{y 2,1}$, where $T_{r 1,2}$ and $T_{y 1,2}=3 s$ represent the red light and yellow light durations for roads $\mathrm{R}_{1}$ and $\mathrm{R}_{2}$, respectively. Moreover, the probability of red-light running (RLR) was fixed at $P_{R L R}=0.01(1 \%)$ to induce a realistic yet controlled frequency of conflict events.

For each combination of $\alpha_{1}, \alpha_{2}$, and signal timing, the simulation was executed for 100,000 iterations. To ensure the system reached a steady state and to eliminate transient effects, the initial 20,000 iterations were discarded as burn-in period. The subsequent 80,000 iterations were used for analysis, providing a robust and statistically stable dataset for each traffic scenario. This approach ensures that the captured patterns reflect the long-term behavior of the system across diverse parameterizations.

### 2.4.2. Data description

Traffic features are aggregated over a 30-s observation window $\left(T_{\text {obs }}\right)$, providing the input for the model to predict the occurrence of an accident within the subsequent 30-s prediction horizon $\left(T_{\text {hor }}\right)$. The detection system produces a binary output ( $y \epsilon\{0,1\}$ ), where 0 signifies a safe state and 1 indicates an imminent collision. For each labeled instance, a comprehensive suite of traffic descriptors is recorded, including vehicular inflow, mean speed, speed dispersion, vehicle density (within a ±70-cell radius of the intersection), and the mean and standard deviation of the space headway.

The observation window $T_{\text {obs }}=30 s$ was selected to encompass between half and one complete signal cycle ( $T_{g}=20-40 s$ ), ensuring that the extracted features capture the full behavioral sequence preceding a potential red-light running event. At the maximum vehicle speed ( $v_{\text {max }}=$ 3 cells/step), this window allows vehicles to traverse the complete 70cell observation zone. Moreover, the prediction horizon $T_{\text {hor }}=30 \mathrm{~s}$ was selected to provide sufficient lead time for potential traffic management interventions, such as adaptive signal timing adjustments or warning generation, while maintaining a relatively high temporal resolution for accident prediction. Shorter horizons may not allow effective preventive actions, whereas longer horizons reduce the temporal precision of the predicted event.

Due to the stochastic nature of the CA model, the raw simulation output is characterized by a significant class imbalance, where nonaccident states vastly outnumber accident events. To address this, we implemented a random under-sampling strategy. We retained the entire population of accident events and randomly extracted an equivalent number of non-accident instances from the majority pool, maintaining a fixed 1:1 ratio throughout the analysis.

This approach is supported by literature; as noted by Ref. [64], a ratio of non-accident to accident events $(n)$ between 1:1 and 5:1 is typically effective for traffic safety modeling. Furthermore, previous research [65] has demonstrated that variations within this range do not significantly alter model performance. Consequently, the 1:1 balanced distribution adopted in this study ensures that the XGBoost classifier can effectively learn the discriminative patterns of the minority class (accidents) without being biased toward the majority class.

### 2.4.3. Data preprocessing and feature selection

The dataset comprises 18 input features and a single binary target variable. Following data collection, a rigorous preprocessing pipeline was implemented. First, any instances containing missing values (NaN) in any of the 18 parameters were pruned. This filtering process resulted in a perfectly balanced dataset of 13,504 samples, consisting of 6752 accident events and 6752 non-accident instances. A Min-Max normalization was applied to scale all feature values into a consistent range [0, 1]. This transformation accelerates gradient convergence during training and prevents features with larger numerical scales from dominating the model's weight updates [66]. Subsequently, the samples were subjected to a random shuffling procedure to eliminate any bias associated with the original temporal or scenario-based arrangement of the simulation output.

To enhance model parsimony and mitigate the impact of noise, feature selection was performed. We retained the 9 most significant predictors, which collectively accounted for 90\% of the cumulative feature importance. This reduction in dimensionality focuses the model on the most discriminative variables while preventing overfitting.

The processed dataset was partitioned into training (80\%), testing (10\%), and validation (10\%) sets. Furthermore, to guarantee the robustness of the hyperparameter tuning, a 10-fold cross-validation approach was implemented within the training set, ensuring that the model's performance is stable across different subsets of the data.

### 2.5. Performance metrics for model evaluation

The predictive performance of the XGBoost classifier was evaluated using the following metrics derived from the confusion matrix, which categorizes predictions into True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives $(F N)$. These metrics constitute a standard set of confusion-matrix measures for classification tasks [67], and are formally defined as follows:

Accuracy:
Accuracy represents the overall proportion of correct classifications (both positive and negative) relative to the total number of cases. While intuitive, it is primarily effective for balanced datasets.

$$
\text { Accuracy }=\frac{T P+T N}{T P+T N+F P+F N}
$$

Precision:
Also known as Positive Predictive Value (PPV), quantifies the model's ability to avoid type I errors (labeling a safe state as an accident).

$$
\text { Precision }=\frac{T P}{T P+F P}
$$

It is critical for minimizing false alarms, which can lead to "cry-wolf" effects in real-world traffic management systems.

Recall (Sensitivity):
It measures the model's ability to identify all relevant positive instances (accidents).

$$
\text { Recall }=\frac{T P}{T P+F N}
$$

In safety-critical applications, maximizing Recall is the highest priority, as failing to predict an accident (type II error) has far more severe consequences than a false alarm.

F1-Score:
The F1-score is the harmonic mean of Precision and Recall. It provides a balanced assessment of the model's performance, especially
when there is an uneven class distribution.

$$
F 1-\text { score }=2 \times \frac{\text { Precision } \text { × } \text { Recall }}{\text { Precision }+ \text { Recall }}
$$

Area Under the ROC Curve (AUC-ROC):
The AUC measures the entire two-dimensional area underneath the Receiver Operating Characteristic (ROC) curve. It provides an aggregate measure of performance across all possible classification thresholds, reflecting the model's capability to discriminate between accident and non-accident classes [68].

## 3. Results and discussion

This section presents the results derived from the simulationgenerated dataset, the feature selection analysis, and the classification performance of the proposed XGBoost-CA framework. We provide a detailed comparison with baseline methods, reporting numerical outcomes and their physical interpretation within the context of traffic dynamics.

### 3.1. Hyperparameter tuning and model optimization

To identify the optimal architecture for accident prediction, a comprehensive grid search was performed across the hyperparameter space defined in the methodology. The performance metrics for the most prominent configurations are summarized in Table 2.

Given the safety-critical nature of traffic accident prediction, the selection criteria prioritized the Recall metric to minimize false negatives (missed accidents). The configuration consisting of $K=30, \eta=$ 0.1, $\max _{\text {depth }}=3$ yielded the highest recall on the validation set. This choice aligns with the risk-aversion strategy essential for real-world traffic management systems.

Analysis of Table 2 reveals that the evaluated hyperparameter configurations yield consistently high performance, with recall values remaining above 0.95 across all cases, reinforcing the robustness of the model in detecting positive events.

While the configuration with $K=30, \eta=0.1$, and $\max _{\text {depth }}=3$ achieves the highest recall, the differences among the top configurations are relatively small, indicating low sensitivity to moderate hyperparameter variations. Notably, increasing $\max _{\text {depth }}$ or the number of estimators does not lead to substantial improvements, suggesting that the model achieves an adequate balance between complexity and generalization at relatively low depths and ensemble sizes. Additionally, configurations with higher learning rates $(\eta=0.2)$ or lower ones $\eta=$ 0.05) do not significantly outperform the baseline, further confirming the stability of the training process. From an application standpoint, these results support the selection of simpler configurations that maintain high recall while avoiding unnecessary computational cost, which is particularly relevant in safety-critical traffic scenarios where minimizing false negatives is a primary objective.

### 3.2. Feature importance analysis

Fig. 4 presents the feature importance of the proposed model. A Pareto analysis is subsequently applied to establish a threshold for distinguishing the most relevant from the least relevant predictors. The results indicate that the first nine variables account for 90\% of the cumulative explanatory power, proving sufficient to maintain high model performance while reducing dimensionality.

A clear predominance of vehicle speed variables is observed, as they exhibit the highest discriminative power. These are followed by headway-related measures and vehicle counts. In contrast, variables associated with the global system load-such as vehicular inflow probabilities ( $\alpha_{1}$ and $\alpha_{2}$ ), along with lane-changing frequency-show minimal influence, ranking at the lower end of the importance scale.

From the perspective of complex systems physics and traffic dynamics, this distribution of importance suggests that accidents are emergent phenomena governed primarily by local kinematic conditions rather than by the global state of the network. The dominant role of speed highlights that collisions are intrinsically linked to kinetic energy and reduced reaction times within the conflict zone. Furthermore, the relevance of headway supports the idea that the spatial structure of traffic and the formation of platoons determine the available maneuvering margin to avoid an impact. The low contribution of the $\alpha$ parameters reinforces the conclusion that crash risk is not a direct consequence of long-term inflow volume. Instead, it arises from specific configurations of transient instability and disorder in the cells near the intersection. This provides the model with a solid physical basis, consistent with the non-linear nature of real-world traffic accidents.

In addition, a statistical test was used to compare the original 18feature representation with the reduced 9-feature set. Each configuration was run 30 times, and a Student's t-test was applied. Statistical analysis indicated that the observed differences were not significant $(p>0.05)$ across all evaluated metrics: recall $(p=0.81)$, accuracy $(p=$ $0.71)$, precision $(p=0.61)$, F1-score $(p=0.40)$, and AUC $(p=0.82)$. This demonstrates that the reduced feature set preserves the predictive information contained in the original representation.

To optimize the model's parsimony and predictive stability, parameters with low importance were removed from the feature set, reducing the dimensionality from 18 to 9 input variables, which are: $\mu_{v_{1}}, \mu_{v_{2}}, N_{12}$, $\sigma_{v_{1}}, N_{21}, \sigma_{h_{1}}, N_{11}, \mu_{h_{2}}$ and $N_{21}$. This pruning minimizes the risk of incorporating noise that could destabilize the gradient boosting process without contributing to accuracy. The nine retained features formed the input vector for all three classifiers evaluated in this study.

### 3.3. Model performance

For comparative purposes, two additional classifiers were considered. KNN was selected as a representative distance-based, non-parametric learning algorithm, while LSTM was chosen as a representative deep learning architecture capable of modeling temporal dependencies. Together with XGBoost, these models represent three distinct machine learning paradigms, enabling a broader evaluation of the proposed framework without restricting the comparison to variants of a single learning strategy.

Table 3 reports the classification metrics obtained by XGBoost, KNN, and LSTM on the held-out test set of 1351 samples. Results are evaluated across five metrics: accuracy, precision, recall, F1 score, and AUC, to

Table 2
Validation-set performance for selected hyperparameter combinations.
| $K$ | $\eta$ | max $_{\text {depth }}$ | Accuracy | Precision | Recall | F1 | AUC |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 30 | 0.1 | 3 | 0.8741 | 0.8170 | 0.9677 | 0.8860 | 0.9160 |
| 30 | 0.1 | 4 | 0.8793 | 0.8250 | 0.9663 | 0.8900 | 0.9209 |
| 30 | 0.1 | 2 | 0.8570 | 0.7951 | 0.9663 | 0.8724 | 0.9087 |
| 30 | 0.2 | 3 | 0.8826 | 0.8300 | 0.9655 | 0.8927 | 0.9190 |
| 50 | 0.1 | 3 | 0.8796 | 0.8263 | 0.9648 | 0.8902 | 0.9179 |
| 20 | 0.1 | 3 | 0.8704 | 0.8139 | 0.9641 | 0.8827 | 0.9149 |
| 30 | 0.05 | 3 | 0.8633 | 0.8048 | 0.9633 | 0.8770 | 0.9132 |
| 100 | 0.1 | 3 | 0.8830 | 0.8352 | 0.9575 | 0.8922 | 0.9202 |


![](https://cdn.mathpix.com/cropped/4a4d610a-c6f6-4d67-b0d9-9a92cb6a133b-09.jpg?height=956&width=1589&top_left_y=189&top_left_x=237)
Fig. 4. Pareto analysis of feature importance for the proposed model. The bar chart shows the relative importance of each predictor, while the red line represents the cumulative importance. The dashed line indicates the 90\% threshold used to identify the most relevant variables.

Table 3
Comparative performance metrics (mean ± standard deviation over 30 runs) of the XGBoost model and alternative approaches (KNN and LSTM) on the test dataset.
| Model | Accuracy | Precision | Recall | F1 Score | AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| XGBOOST | $0.8636 \pm 0.0077$ | $0.8013 \pm 0.0096$ | $0.9665 \pm 0.0054$ | $0.8762 \pm 0.0067$ | $0.9116 \pm 0.0055$ |
| KNN | $0.8579 \pm 0.0068$ | $0.7981 \pm 0.0086$ | $0.9577 \pm 0.0060$ | $0.8706 \pm 0.0059$ | $0.9044 \pm 0.0063$ |
| LSTM | $0.8514 \pm 0.0103$ | $0.7900 \pm 0.0171$ | $0.9581 \pm 0.0209$ | $0.8655 \pm 0.0081$ | $0.9007 \pm 0.0070$ |


provide a comprehensive characterization of each classifier's performance at the selected operating threshold.

The XGBoost classifier achieved an accuracy of 0.86 and a recall of 0.966, the highest values among the evaluated models. In the context of traffic safety, Recall is the critical metric as it quantifies the proportion of actual accidents correctly identified. A Recall of 0.966 indicates that only 4\% of accident events were misclassified as safe states (False Negatives). Given that undetected accidents in a real-time warning system represent missed life-saving interventions, this high sensitivity carries significantly greater practical weight than precision.

KNN achieved a precision of 0.798 , marginally slower than XGBoost (0.80), indicating a slightly higher false positive rate. However, its recall (0.957) and accuracy (0.857) are both below those of XGBoost. Both models reached the same F1 score (0.87), and their AUC values (0.911 for XGBoost, 0.904 for KNN) are closely comparable, reflecting similar overall discriminative performance despite the differences at the selected operating threshold.

The LSTM classifier produced the lowest values across all metrics, with an accuracy of 0.85, a recall of 0.958, an F1-score of 0.865, and an AUC of 0.9. Although recurrent architectures such as LSTM are designed to capture sequential dependencies, the feature extraction procedure used here aggregates traffic state information over 30-s windows into scalar statistics (means, standard deviations, counts). This aggregation reduces the temporal granularity available to the LSTM, limiting the advantage of its sequence-modeling capacity. The boosted tree (XGBoost) and distance-based (KNN) approaches operate directly on these aggregate features and do not depend on sequential structure, which accounts for their comparatively higher performance on this dataset.

To evaluate the statistical significance of the differences among the classifiers, each model (XGBoost, KNN, and LSTM) was trained and evaluated over 30 repetitions, using a different random seed in each repetition but sharing the same seed across the three models within that repetition. Since the resulting measurements are paired, a Friedman test was performed. The analysis revealed statistically significant differences among the evaluated classifiers $\left(\chi^{2}(2)=18.97, p=7.613 \times 10^{-5}<\right.$ 0.05), in terms of Recall. A post-hoc multiple-comparison analysis further showed that XGBoost significantly outperformed both KNN and LSTM in terms of Recall, whereas no statistically significant difference was observed between KNN and LSTM.

It is noted that the LSTM baseline evaluated here operates on the same aggregated feature vector as XGBoost and KNN, rather than on raw per-second temporal sequences. This design ensures a controlled comparison under identical input conditions consistent with the proposed deployment pipeline, but constrains the LSTM from fully exploiting its sequence-modeling capacity. A configuration receiving raw sequential inputs would likely yield higher LSTM performance and is proposed as a direction for future comparative analysis.

Moreover, a comparative ROC Curve, which evaluates the performance of the three binary classification algorithms: LSTM, XGBoost, and KNN, is presented in Fig. 5. This type of graph is crucial in machine learning for understanding a model's discrimination capability across all possible decision thresholds. The area under the curve (AUC) summarizes discriminative capability across all thresholds as the probability

![](https://cdn.mathpix.com/cropped/4a4d610a-c6f6-4d67-b0d9-9a92cb6a133b-10.jpg?height=695&width=1189&top_left_y=192&top_left_x=435)
Fig. 5. Comparative ROC Curve, visualizing the classification performance of the LSTM, XGBoost, and KNN models.

that the model assigns a higher score to a randomly drawn positive example than to a randomly drawn negative example. The obtained AUC values of 0.911 for XGBoost, 0.904 for KNN, and 0.9 for LSTM, confirm that all three classifiers substantially exceed random discrimination. While these reported AUC values reflect a robust global performance consistent with the results in Table 3, minor differences between the plotted curve areas and the tabulated metrics arise from the specific probability threshold at which the point-estimates are evaluated.

Although XGBoost (AUC $=0.911$ ) and KNN (AUC = 0.904) show closely comparable overall discrimination, they differ in the highsensitivity region. XGBoost achieves a true positive rate (TPR) of 0.966 at its operating threshold, corresponding to a point in the upperleft portion of the ROC space. For accident prediction applications, where the cost of a false negative (an undetected accident) outweighs the cost of a false alarm, the high-TPR operating point of XGBoost is the more suitable choice. KNN reaches a comparable region of the curve but at a slightly lower TPR (0.957), consistent with the threshold-specific metrics in Table 3.

### 3.4. Comparison with existing methods

Table 4 summarizes the proposed framework alongside representative machine learning models from the recent literature on accident and conflict prediction. The comparison includes method, spatial scope, target, data and performance metrics.

Among the studies whose target coincides with that of the present work, namely crash occurrence prediction, tree-based ensemble models trained on real-world data have achieved high recall and AUC, primarily on freeways. Ma et al. [69] report a recall of 0.86 and an AUC of 0.907 with XGBoost on a freeway, using a balanced 1:1. On urban arterials, sequential models trained on instrumented data report partial recall and AUC values: Yuan et al. [18] obtain a sensitivity of 0.61 with an LSTM-RNN, and Li et al. [23] an AUC of 0.93 with a recall of 0.868 using an LSTM-CNN. The closest precedent in both spatial scope and target, the prediction of crash occurrence at a signalized intersection from real data, is Yuan and Abdel-Aty [33]. They predicted crash occurrence at entrance, exit, and within signalized intersections using Bayesian conditional logistic regression and reported an AUC of approximately 0.76 without reporting event-level sensitivity. In contrast, the proposed framework focuses specifically on Red Light Running (RLR)-related collisions, thereby capturing the traffic dynamics and behavioral patterns that precede this particular crash mechanism. This distinction is important because different crash types are associated with different causal processes and risk factors. Consequently, the proposed

Table 4
Comparison of the proposed framework with selected machine learning models for traffic accident and conflict prediction.
| Study | Method | Scope | Target | Reported performance |
| :--- | :--- | :--- | :--- | :--- |
| Ma et al. (2023) [69] | XGBoost | Freeway | Crash occurrence (binary) | Recall $=0.86$; AUC = 0.907 (1:1) |
| Yuan et al. (2019) [18] | LSTM | Arterial segment | Crash occurrence (binary) | Sensitivity = 0.61 |
| Li et al. (2020) [23] | LSTMCNN | Arterial segment | Crash occurrence (binary) | Recall $=0.868$; $\mathrm{AUC}=0.93$ |
| Yuan \& AbdelAty (2018) [33] | Bayesian logistic regression | Signalized intersection | Crash occurrence (binary) | $\mathrm{AUC}=0.76$ |
| Formosa et al. (2020) [17] | R-CNN + DNN | Freeway segment | Traffic conflict (surrogate) | Accuracy $=0.94$ |
| Zhang \& AbdelAty (2022) [70] | XGBoost | Signalized intersection | Pedestrianvehicle conflict (surrogate) | Recall = 0.739; $\mathrm{AUC}=0.841$ |
| Kashifi et al. (2022) [21] | CNN + LSTM +DNN | $1 \mathrm{~km}^{2}$ grid | Crash frequency (areal) | Accuracy $=0.72$ |
| Chen et al. (2025) [55] | MSCPOXGBoost | National records | Crash severity (3 classes) | Accuracy $=0.84$; Recall $=0.85$; AUC = 0.93 |
| Proposed | XGBoost + CA | Signalized intersection | Crash occurrence (binary; right-angle/ RLR) | Accuracy=0.863; Recall=0.966; AUC=0.911 |


framework advances beyond generalized crash occurrence prediction by providing high-resolution, event-level prediction of a specific and safety-critical collision mechanism, achieving both high recall (0.96) and strong discriminative capability (AUC $=0.911$ ).

Two further ensemble-based studies complement this picture. On urban expressways, Peng et al. [71] addressed binary crash occurrence in real time with an ensemble that combines random under-sampling
with boosting, reporting a sensitivity of 0.842 and an AUC of 0.892 at a class ratio of 1 to 20, which confirms that boosted ensembles can attain competitive recall and discrimination for crash occurrence, although again on controlled-access facilities rather than at intersections. From a different angle, Qu et al. [56] trained boosted tree models for crash detection on an expressway and reported a detection rate of 0.939 with XGBoost, with the crash instances generated by simulation within a digital twin; this task concerns the detection of crashes already in progress rather than their prediction, and its discrimination is reported only as a relative ranking of models without explicit AUC values. Taken together, these cases extend the same pattern: boosted ensembles deliver competitive recall or detection for crash occurrence on freeways and expressways, whether trained on field or simulated data, but not for individual crash events at a signalized intersection.

The studies with the highest reported metrics pursue targets different from the one addressed here. Formosa et al. [17] reach an accuracy of 0.94, but on conflict detection over a freeway segment that depends on continuous camera coverage. Zhang and Abdel-Aty [70], although located at a signalized intersection, predict surrogate pedestrian-vehicle conflicts based on PET and TTC rather than recorded crashes, with a recall of 0.739 and an AUC of 0.841. Kashifi et al. [21] predict crash frequency at $1 \mathrm{~km}^{2}$ grid resolution, a target too aggregated for event-level intervention, while Chen et al. [55] address multiclass crash severity, with a recall of 0.85 and an AUC of 0.93 . None of these targets corresponds to the prediction of individual crash events at a signalized intersection.

The distinguishing factor of the present work is not an isolated metric value but the combination of spatial scope, prediction target, and data independence. It is the first model to predict individual crash events risk at a signalized intersection with a 30-s horizon, using data generated through cellular automata simulation and without any dependence on field sensor infrastructure. This combination makes the framework applicable to intersection geometries and traffic conditions for which no real labeled datasets exist. The high sensitivity achieved by the model, with a recall of 0.966, highlights its potential for integration into Intelligent Transportation Systems (ITS) as a predictive decision-support tool. When integrated with field sensors or cameras, the framework can issue early warnings of impending crashes and enable preventive strategies such as adaptive traffic signal control.

## 4. Conclusion

This study presented a robust framework for traffic accident prediction at signalized intersections by integrating a Cellular Automata simulation model with an XGBoost binary classifier. This approach effectively addresses two critical gaps in current literature: the scarcity of granular, labeled accident data at the intersection level and the lack of models capable of predicting individual collision events within a shorttime horizon.

Feature importance and Pareto analysis revealed that local kinematic variables, specifically mean speeds, vehicle counts, and headway measures, constitute the primary predictors of accident occurrence, accounting for over 90\% of the model's predictive power. On the held-out test set, the optimized XGBoost classifier achieved an accuracy of 0.863, a recall of 0.966, a precision of 0.803, an F1-score of 0.876, and an AUC of 0.911. Notably, the recall of 0.966 demonstrates the framework's high sensitivity, successfully identifying 96\% of accident events and minimizing the risk of undetected collisions in safety-critical scenarios. Moreover, statistical analysis showed that XGBoost significantly outperformed both KNN and LSTM in terms of Recall.

This model can be integrated with sensors and cameras and applied within Intelligent Transportation Systems as an early warning mechanism to predict potential accident occurrences. When a high-risk situation is detected, adaptive traffic control strategies, such as adjusting traffic light timings, can be implemented to mitigate hazardous conditions and reduce the likelihood of accidents.

Despite its strong predictive performance, the framework has been evaluated exclusively on simulation-generated data, reflecting the fundamental challenge of collecting real-world accident data at the microscopic resolution required by the model, where events are rare and continuous long-duration monitoring is necessary. Future work will focus on real-world validation at instrumented intersections using fixed high-resolution cameras with vehicle tracking pipelines, assessing the generalization of the pre-trained XGBoost model through transfer learning approaches. Additionally, the accident definition will be extended to incorporate explicit SSM thresholds to capture near-miss events, and the simulation will be enhanced with more heterogeneous traffic scenarios to broaden the training distribution and improve crossdomain robustness.

## Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work the authors used Gemini in order to generate Fig. 3. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.

## Funding sources

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## CRediT authorship contribution statement

A. Ángeles Robles: Data curation, Formal analysis, Software, Validation, Visualization. J. Águila León: Conceptualization, Methodology, Software, Validation, Writing - original draft. G.A. Mejía-Pérez: Conceptualization, Formal analysis, Investigation, Project administration, Resources, Validation. B. Castillo-Téllez: Conceptualization, Data curation, Investigation, Visualization. O. Bamaarouf: Conceptualization, Formal analysis, Visualization, Writing - original draft. O. Oubram: Conceptualization, Data curation, Formal analysis, Supervision. R. Marzoug: Conceptualization, Data curation, Formal analysis, Investigation, Methodology, Project administration, Software, Supervision, Validation, Visualization, Writing - original draft, Writing - review \& editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## References

[1] World Health Organization. Global status report on road safety 2023:country and territory profiles. World Health Organization; 2024.
[2] Eisenberg D. The mixed effects of precipitation on traffic crashes. Accid Anal Prev 2004;36(4):637-47. https://doi.org/10.1016/S0001-4575(03)00085-X.
[3] Ma S, Mei G, Cuomo. An analytic framework using deep learning for prediction of traffic accident injury severity based on contributing factors. Accid Anal Prev 2021; 160:106322. https://doi.org/10.1016/j.aap.2021.106322.
[4] Wang L, Abdel-aty M, Shi Q, Park J. Real-time crash prediction for expressway weaving segments. Transport Res C Emerg Technol 2015;61:1-10. https://doi.org/ 10.1016/j.trc.2015.10.008.
[5] Yu M, Abdel-Aty. Utilizing support vector machine in real-time crash risk evaluation. Accid Anal Prev 2013;51:252-9. https://doi.org/10.1016/j. aap.2012.11.027.

[6] Lin L, Wang Q, Sadek AW. A novel variable selection method based on frequent pattern tree for real-time traffic accident risk prediction. Transp Res Part C 2015; 55:444-59. https://doi.org/10.1016/j.trc.2015.03.015.
[7] Najafabadi MM, Villanustre F, Khoshgoftaar TM, Seliya N, Wald R, Muharemagic E. Deep learning applications and challenges in big data analytics. J Big Data 2015;2 (1):1-21. https://doi.org/10.1186/s40537-014-0007-7.
[8] Moridpour S. A review of traffic congestion prediction using. J Adv Transp 2021; 2021(1):8878011. https://doi.org/10.1155/2021/8878011.
[9] Kothai G, et al. A new hybrid deep learning algorithm for prediction of wide traffic congestion in smart cities. Wireless Commun Mobile Comput 2021;2021(1): 5583874. https://doi.org/10.1155/2021/5583874.
[10] Al-Turki SM, Kashifi MT, Ratrout NT, Rahman. Traffic signal optimization framework using interpretable machine learning technique under heterogeneousautonomy traffic environment. Neural Comput Appl 2024;36(22):13761-81. https://doi.org/10.1007/s00521-024-09694-y.
[11] Abdolrasol A, Hussain SS, Ustun TS, Sarker MR, Hannan MA, Mohamed R, Ali Abdel, Mekhilef S, Milad. Artificial neural networks based optimization techniques: a review. Electron 2021;10(21):2689. https://doi.org/10.3390/electronics10212689.
[12] Santos K, Dias JP, Amado C. A literature review of machine learning algorithms for crash injury severity prediction. J Saf Res 2022;80:254-69. https://doi.org/10.1016/j.jsr.2021.12.007.
[13] Alkheder S, Taamneh M, Taamneh S. Severity prediction of traffic accident using an artificial neural network. J Forecast 2017;36(1):100-8.
[14] Chong MM, Abraham A, Paprzycki M. Traffic accident analysis using decision trees and neural networks. Proc. IADIS Int. Conf. Appl. Comput. 2004;2:39-42.
[15] Masood S, Rai A, Aggarwal A, Doja MN, Ahmad M. Detecting distraction of drivers using convolutional neural network. Pattern Recognit Lett 2020;139(2018):79-85. https://doi.org/10.1016/j.patrec.2017.12.023.
[16] Mussone L, Ferrari A, Oneta M. An analysis of urban collisions using an artificial intelligence model. Accid Anal Prev 1999;31(6):705-18. https://doi.org/10.1016/S0001-4575(99)00031-7.
[17] Formosa N, Quddus M, Ison S, Abdel-Aty M, Yuan J. Predicting real-time traffic conflicts using deep learning. Accid Anal Prev 2020;136. https://doi.org/10.1016/j.aap.2019.105429. 0-45.
[18] Yuan J, Abdel-Aty M, Gong Y, Cai Q. Real-time crash risk prediction using long short-term memory recurrent neural network. Transp Res Rec 2019;2673(4): 314-26. https://doi.org/10.1177/0361198119840611.
[19] Moosavi S, Samavatian MH, Parthasarathy S, Teodorescu R, Ramnath R. Accident risk prediction based on heterogeneous sparse data: new dataset and insights. GIS Proc ACM Int Symp Adv Geogr Inf Syst 2019:33-42. https://doi.org/10.1145/3347146.3359078.
[20] Bao J, Liu P, Ukkusuri SV. A spatiotemporal deep learning approach for citywide short-term crash risk prediction with multi-source data. Accid Anal Prev 2019;122: 239-54. https://doi.org/10.1016/j.aap.2018.10.015.
[21] Kashifi MT, Al-Sghan IY, Rahman SM, Al-Ahmadi HM. Spatiotemporal grid-based crash prediction-application of a transparent deep hybrid modeling framework. Neural Comput Appl 2022;34(23):20655-69. https://doi.org/10.1007/s00521-022-07511-y.
[22] Jin Z, Noh B, , From Prediction to Prevention: Leveraging Deep Learning in Traffic AccidenJin, Z., Noh B. From prediction to prevention: leveraging deep learning in traffic accident prediction systems. Electronics (Switzerland) 2023;12(20):1-17.
[23] Li P, Abdel-Aty M, Yuan J. Real-time crash risk prediction on arterials based on LSTM-CNN. Accid Anal Prev 2020;135(November 2019):105371. https://doi.org/10.1016/j.aap.2019.105371.
[24] Zheng L, Sayed T. A novel approach for real time crash prediction at signalized intersections. Transport Res C Emerg Technol 2020;117(December 2019):102683. https://doi.org/10.1016/j.trc.2020.102683.
[25] Ali Y, Washington S, Haque MM. Estimating real-time crash risk at signalized intersections: a Bayesian generalized extreme value approach. Saf Sci 2023;164 (March):106181. https://doi.org/10.1016/j.ssci.2023.106181.
[26] Hussain F, Ali Y, Li Y, Haque MM. A bi-level framework for real-time crash risk forecasting using artificial intelligence-based video analytics. Sci Rep 2024;14(1): 1-16. https://doi.org/10.1038/s41598-024-54391-4.
[27] Channamallu SS, Almaskati D, Kermanshachi S, Pamidimukkala A. Predictive analytics in autonomous vehicles safety: crash outcome modeling. Urban, Plan Transp Res 2024;12(1). https://doi.org/10.1080/21650020.2024.2409676.
[28] Yu R, Abdel-Aty M. Analyzing crash injury severity for a mountainous freeway incorporating real-time traffic and weather data. Saf Sci 2014;63:50-6. https://doi. org/10.1016/j.ssci.2013.10.012.
[29] Ahmed M, Abdel-Aty M, Yu R. Assessment of interaction of crash occurrence, mountainous freeway geometry, real-time weather, and traffic data. Transp Res Rec 2012;(2280):51-9. https://doi.org/10.3141/2280-06.
[30] Oh JS, Oh C, Ritchie SG, Chang M. Real-time estimation of accident likelihood for safety enhancement. J Transport Eng 2005;131(5):358-63. https://doi.org/10.1061/(ASCE)0733-947X(2005)131:5(358).
[31] Marzoug R, Lakouari N, Ez-Zahraouy H, Castillo Téllez B, Castillo Téllez M, Cisneros Villalobos L. Modeling and simulation of car accidents at a signalized intersection using cellular automata. Phys A Stat Mech its Appl 2022;589:126599. https://doi.org/10.1016/j.physa.2021.126599.
[32] Yuan Z, Zhou X, Yang T. Hetero-convlstm: a deep learning approach to traffic accident prediction on heterogeneous spatio-temporal data. In: In proceedings of the 24th ACM SIGKDD international conference on knowledge discovery \& data mining; 2018. p. 984-92. https://doi.org/10.1145/3219819.3219922.
[33] Yuan J, Abdel-Aty M. Approach-level real-time crash risk analysis for signalized intersections. Accid Anal Prev 2018;119:274-89. https://doi.org/10.1016/j.aap.2018.07.031.
[34] Wang K, Qin X. Exploring driver error at intersections: key contributors and solutions. Transp Res Rec 2015;2514:1-9. https://doi.org/10.3141/2514-01.
[35] Yang CYD, Najm WG. Examining driver behavior using data gathered from red light photo enforcement cameras. J Saf Res 2007;38(3):311-21. https://doi.org/10.1016/j.jsr.2007.01.008.
[36] Chopard B. Cellular automata modeling of physical systems. New York, NY: Springer; 2009.
[37] Toffoli T, Margolus N. Cellular automata machines: a new environment for modeling. Cell Autom Mach 1987;1:967-93. https://doi.org/10.7551/mitpress/1763.001.0001.
[38] Nagel K, Paczuski M. Emergent traffic jams. Phys Rev E 1995;51(4):2909-18. https://doi.org/10.1103/PhysRevE.51.2909.
[39] Biham O, Middleton AA, Levine D. Self-organization and a dynamical transition in traffic-flow models. Phys Rev A 1992;46(10):6124-7. https://doi.org/10.1103/PhysRevA.46.R6124.
[40] Nagel K, Schreckenberg M. A cellular automaton model for freeway traffic. J Phys I 1992;2(12):2221-9. https://doi.org/10.1051/jp1:1992277.
[41] Boccara N, Fukś H, Zeng Q. Car accidents and number of stopped cars due to road blockage on a one-lane highway. J Phys Math Gen 1997;30(10):3329-32. https://doi.org/10.1088/0305-4470/30/10/012.
[42] wei Huang D, chung Tseng W. Mean-field theory for car accidents. Phys Rev E 2001;64(5):4. https://doi.org/10.1103/PhysRevE.64.057106.
[43] Pang MB, Zheng SS, Cai ZH. Simulation of three lanes one-way freeway in low visibility weather by possible traffic accidents. Phys A Stat Mech its Appl 2015;433 (xxxx):161-70. https://doi.org/10.1016/j.physa.2015.03.066.
[44] Pang MB, Ren BN. Effects of rainy weather on traffic accidents of a freeway using cellular automata model. Chin Phys B 2017;26(10). https://doi.org/10.1088/1674-1056/26/10/108901.
[45] Yang XQ, Zhang W, Qiu K, Zhao YM. Effects of a type of quenched randomness on car accidents in a cellular automaton model. Phys Rev E - Stat Nonlinear Soft Matter Phys 2006;73(1):1-7. https://doi.org/10.1103/PhysRevE.73.016126.
[46] Pang MB, Ye LH, Pei YN. Influence of bus stop with left-turn lines between two adjacent signalized intersections. Chin Phys B 2016;25(8):1-11. https://doi.org/10.1088/1674-1056/25/8/088901.
[47] Chang GL, Xiang H. The relationship between congestion levels and accidents. State Highw Adiministration July, 2003 [Online]. Available: http://roads.maryla nd.gov/OPR_Research/MD-03-SP308B46-Congestion-Vs-Accidents-Report.pdf.
[48] Wang X, Abdel-Aty M. Right-angle crash occurrence at signalized intersections. Transp Res Rec 2007;2019:156-68. https://doi.org/10.3141/2019-19.
[49] Li X, Yeh AGO. Modelling sustainable urban development by the integration of constrained cellular automata and GIS. Int J Geogr Inf Sci 2000;14(2):131-52. https://doi.org/10.1080/136588100240886.
[50] Li X, Yeh AG. Calibration of cellular automata by using neural networks for the simulation of complex urban systems. Environ Plann 2001;33(8):1445-62. https://doi.org/10.1068/a33210.
[51] Almeida CM, Gleriani JM, Castejon EF, Soares-Filho BS. Using neural networks and cellular automata for modelling intra-urban land-use dynamics. Int J Geogr Inf Sci 2008;22(9):943-63. https://doi.org/10.1080/13658810701731168.
[52] Liu M, Shi J. A cellular automata traffic flow model combined with a BP neural network based microscopic Lane changing decision model. J Intell Transport Syst Technol Plann Oper 2019;23(4):309-18. https://doi.org/10.1080/15472450.2018 .1462176.
[53] Kim BS, Kim TG. Modeling and simulation using artificial neural network-embedded cellular automata. IEEE Access 2020;8:24056-61. https://doi.org/10.1109/ACCESS.2020.2970547.
[54] Wanna P, Wongthanavasu S. An efficient cellular automata-based classifier with variance decision table. Appl Sci 2023;13(7). https://doi.org/10.3390/app13074346.
[55] Chen F, et al. Traffic accident severity prediction based on an enhanced MSCPO-XGBoost hybrid model. Sci Rep 2025;15(1):1-18. https://doi.org/10.1038/s41598-025-00797-7.
[56] Qu Q, Shen Y, Yang M, Zhang R. Towards efficient traffic crash detection based on macro and micro data fusion on expressways: a digital twin framework. IET Intell Transp Syst 2024;18(12):2725-43. https://doi.org/10.1049/itr2.12498.
[57] Chowdhury D, Santen L. Statistical physics of vehicular traffic and some related systems. Phys Rep 2000;329(4):199-329. https://doi.org/10.1016/S0370-1573(99)00117-9.
[58] Chowdhury D, Wolf DE, Schreckenberg M. Particle hopping models for two-lane traffic with two kinds of vehicles: effects of lane-changing rules. Phys A Stat Mech its Appl 1997;235(3-4):417-39. https://doi.org/10.1016/S0378-4371(96)00314-7.
[59] Porter BE, England KJ. Predicting red-light running behavior: a traffic safety study in three urban settings. J Saf Res 2000;31(1):1-8. https://doi.org/10.1016/S0022-4375(99)00024-9.
[60] Elmitiny N, Yan X, Radwan E, Russo C, Nashar D. Classification analysis of driver's stop/go decision and red-light running violation. Accid Anal Prev 2010;42(1): 101-11. https://doi.org/10.1016/j.aap.2009.07.007.
[61] Hayward JC. Near miss determination through use of a scale of danger. In: 51st annual meeting of the highway research board; 1972. p. 24-34.
[62] Allen BL, Shin BT. Analysis of traffic conflicts and collisions. Anal traffic conflicts collisions 1978:67-74.

[63] Chen C, Guestrin. XGBoost: a scalable tree boosting system. In: In proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining; 2016. p. 785-94.
[64] Hosmer R, Lemeshow S, Sturdivant. Applied logistic regression. John Wiley \& Sons.; 2013.
[65] Abdel-Aty M, Uddin N, Pande A, Abdalla MF, Hsia L. Predicting freeway crashes from loop detector data by matched case-control logistic regression. Transp Res Rec 2004;(1897):88-95. https://doi.org/10.3141/1897-12.
[66] Huang L, Qin J, Zhou Y, Zhu F, Liu L, Shao L. Normalization techniques in training DNNs: methodology, analysis and application. IEEE Trans Pattern Anal Mach Intell 2023;45(8):10173-96. https://doi.org/10.1109/TPAMI.2023.3250241.
[67] Sokolova M, Lapalme G. A systematic analysis of performance measures for classification tasks. Inf Process Manag 2009;45(4):427-37. https://doi.org/10.1016/j.ipm.2009.03.002.
[68] Fawcett T. An introduction to ROC analysis. Pattern Recognit Lett 2006;27(8): 861-74. https://doi.org/10.1016/j.patrec.2005.10.010.
[69] Ma Y, Zhang J, Lu J, Chen S, Xing G, Feng R. Prediction and analysis of likelihood of freeway crash occurrence considering risky driving behavior. Accid Anal Prev 2023;192(July):107244. https://doi.org/10.1016/j.aap.2023.107244.
[70] Zhang S, Abdel-Aty M. Real-time pedestrian conflict prediction model at the signal cycle level using machine learning models. IEEE Open J Intell Transp Syst 2022;3 (March):176-86. https://doi.org/10.1109/OJITS.2022.3155126.
[71] Peng Y, Li C, Wang K, Gao Z, Yu R. Examining imbalanced classification algorithms in predicting real-time traffic crash risk. Accid Anal Prev 2020;144(March). https://doi.org/10.1016/j.aap.2020.105610.

[^0]:    * Corresponding author.
    E-mail address: rachid.marzoug@academicos.udg.mx (R. Marzoug).

