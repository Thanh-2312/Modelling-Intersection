# A Hierarchical Control Framework for Coordination of Intersection Signal Timings in All Traffic Regimes 

Goof Sterk van de Weg ${ }^{\text {® }}$, Hai L. Vu ${ }^{\text {® }}$, Senior Member, IEEE, Andreas Hegyi ${ }^{\text {® }}$, Member, IEEE, and Serge Paul Hoogendoorn


#### Abstract

In this paper, we develop a hierarchical approach to optimize the signal timings in an urban traffic network taking into account the different dynamics in all traffic regimes. The proposed hierarchical control framework consists of two layers. The first layer-the network coordination layer-uses a model predictive control strategy based on a simplified traffic flow model to provide reference outflow trajectories. These reference outflow trajectories represent average desired link outflows over time. These are then mapped to green-red switching signals which can be applied to traffic lights. To this end, the second layer-the individual intersection control layer-then selects at every intersection the signal timing stage that realizes an outflow which has the smallest error with respect to the reference outflow trajectory. The proposed framework is tested using both macroscopic and microscopic simulations. It is shown that the control framework can outperform a greedy control policy that maximizes the individual intersection outflows, and the control framework can distribute the queues over the network in a way that the network outflow is improved. Simulations using a macroscopic model allow the direct application of the reference outflows computed by the network coordination layer, and the results indicate that the mapping of the reference outflows to the detailed signal timings by the individual intersection control layer only introduces a small performance loss.


Index Terms-Model predictive control, urban traffic network control, link transmission model, signal timings, intersection coordination.

## I. Introduction

COORDINATION of the signal timings of intersections to improve the performance of urban traffic networks is a complex problem. One of the main reasons for this is that coordination requires accounting for the impact of the signal timings on the propagation of traffic over the network. This introduces several issues as discussed below.

Manuscript received April 13, 2017; revised October 27, 2017 and February 23, 2018; accepted April 18, 2018. This work was supported in part by the Australian Research Council Future Fellowships under Grant FT120100723, in part by the Discovery Project under Grant DP130100156, and in part by the Netherlands Organization for Scientific Research through Application of Operations Research in Urban Transport Program. The Associate Editor for this paper was I. Papamichail. (Corresponding author: Goof Sterk van de Weg.)
G. S. van de Weg, A. Hegyi, and S. P. Hoogendoorn are with the Transport and Planning Department, TU Delft, 2628CN Delft, The Netherlands (e-mail: g.s.vandeWeg@tudelft.nl).
H. L. Vu is with the Department of Civil Engineering, Faculty of Engineering, Institute of Transport Studies, Monash University, Clayton, VIC 3800, Australia (e-mail: hai.vu@monash.edu).
Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TITS.2018.2837162

One of the main issues of controlling signal timings plans is that they have a switching structure, meaning that a stage - i.e., a set of streams that can be active simultaneously - can either be green or red. This introduces interruptions (or discontinuities) in the traffic flows at intersections. Due to these discontinuities, optimizing the signal timing plans results in a mixed integer optimization problem that is difficult to solve. This is problematic, since only a limited amount of computation time is available for the real-time application of traffic control strategies. Additionally, other properties of the signal timing plan such as clearance times, offsets, (predetermined) stage sequences, and cycle times, add to the complexity.

Apart from that, the direction of the interaction between intersections changes when the traffic regime changes as discussed in [1]. More specifically, in the under-saturated regime - i.e., when queues are completely emptied during a green time period - an increase in the outflow of an upstream intersection can lead to a change in the outflow at a downstream intersection. This relation is typically used in green-wave approaches that allow vehicles to pass multiple intersections without stopping. In the saturated regime - i.e., when queues neither become empty, nor will spill back to upstream intersections - there is no such strong coupling. Finally, in the over-saturated regime - i.e., when queues spill back to upstream intersections - a change in the outflow at a downstream intersection leads to a change in the outflow of an upstream intersection at a later time instant. All these effects have to be taken into account when optimizing the timing of a signal controller.

The aim of this paper is to design a control strategy for the coordination of signal timings of multiple intersections. The control strategy has to account for all the traffic regimes. It also has to be real-time feasible, meaning that it can compute the control actions within the controller sampling time. The controller sampling time is the time period between updates of the control signal, which is typically in the range of one to several minutes.

## A. Literature

This section discusses approaches to the urban traffic network control problem. We examine for what traffic regimes the different strategies are designed, whether they are real-time feasible, and in what way signal timings are considered. First,
various well-known or recent control strategies are discussed. After that, the review focuses on model-based predictive control strategies.

1) Approaches to the Urban Traffic Network Control Problem: The first approaches to the coordination of intersections focused on performance improvement in the undersaturated traffic regime. A well-known example is the MAXBAND approach proposed by Little [2] for the creation of greenwaves between intersections. MAXBAND computes the signal timings off-line in such a way that traffic can pass multiple intersection without stopping. A disadvantage of off-line control is that it cannot adapt to changes in the traffic demand. SCOOT [3] and SCATS [4] are examples of widely used control strategies for under-saturated traffic regimes that can dynamically adjust to changes in the traffic situation. The performance of SCOOT may deteriorate in saturated and over-saturated regimes according to Papageorgiou et al. [5]. Recently, Lämmer and Helbing [6] proposed a decentralized algorithm that decides at each time instant which stage to actuate in order to reduce the delay at every intersection in the undersaturated regime.

Diakaki et al. [7] proposed the TUC algorithm, which is specifically designed to improve the urban traffic network throughput in the saturated regime. TUC has a feedback structure, and adjusts the green times at an intersection based on the queue lengths in the network. Various extensions to TUC have been proposed, such as the inclusion of green-waves [8]. Recently, the max-pressure (or back-pressure) algorithm was proposed to address the coordination problem in the saturated regime [9], [10]. The max-pressure algorithm decides at every time instant which stage to actuate. This decision is made using information on the queues located directly upstream and downstream of the intersection, so that no centralized communication structure is required.

The performance of the aformentioned control strategies may deteriorate in the over-saturated regime, since the impact of spill back and the corresponding shock wave dynamics are not considered in the controller design. In that regime, congestion may propagate through the network causing a loss of efficiency at intersections and potentially leading to gridlock [11]. One way to address this issue is by perimeter control based on the network fundamental diagram (NFD) [12]. The aim of this strategy is to keep the number of vehicles in the network below or at the critical density of the network fundamental diagram so that congestion is prevented. An issue with this approach is that the shape of the NFD may be affected by the intersection control strategies.

In conclusion, all these approaches are designed to improve the performance in only one or two of the three traffic regimes. A promising approach to include all the traffic regimes is the application of a predictive control strategy. However, this is a challenging task, as discussed in the next section.
2) Model-Based Predictive Control Approaches: Model predictive control (MPC) is a popular method to determine a control action that accounts for the long-term impact of a control signal on the system's performance. It is typically used to determine a control signal over a period of time called the control horizon, that optimizes the performance over a period of time called the prediction horizon [13], [14]. MPC is a procedure in which the impact - expressed using an objective function - of a candidate control signal on the propagation of traffic over the network is predicted using a prediction model. At every controller sampling time instant, the control signal that optimizes the objective function is recomputed using the most recent traffic state measurements. This is commonly referred to as the receding horizon principle.

Lo [15] and Van den Berg et al. [16] have proposed MPC approaches for the optimization of signal timings. Lo [15] used the Cell-Transmission Model (CTM) to predict the traffic dynamics, and modeled the signal timings using binary variables - i.e., a stream can receive either green (1) or red (0). This resulted in a mixed-integer linear programming problem (MILP). Van den Berg et al. [16] used the horizontal queuing model of Kashani and Saridis [17] to model all the traffic regimes, resulting in a non-linear optimization problem. Lin et al. [18] used the S-model, which is a simplification of the model of Van den Berg et al. [16], to formulate another MILP optimization problem. Despite the ability to explicitly consider signal timings and all traffic regimes, all of the resulting non-linear and MILP optimization problems are cumbersome to solve. Due to this, these methods are not realtime feasible when applied to medium to large-scale networks of several (tens of) intersections.

The scalability problem can be mitigated by aggregating the traffic dynamics to (several) tens of seconds and replacing the binary signal timings with average outflows so that continous or linear optimization problems can be formulated [1], [19], [20]. Aboudolas et al. [19] proposed a linear MPC approach based on the store-and-forward model for the saturated regime which resulted in a drastic reduction of the computation time. Le et al. [20] proposed an MPC approach based on a modified version of the CTM for under-saturated and saturated regimes. Recently, van de Weg et al. [1] proposed the use of the Link Transmission Model (LTM) in a linear MPC framework. This approach is capable of reproducing all traffic regimes and is realtime feasible. However, non of these methods consider signal timings, so they are not directly applicable to a real traffic network.

## B. Research Approach and Contributions

This paper develops a real-time feasible, hierarchical control framework for the control of signal timings in order to improve the urban network throughput in all traffic regimes. The main contribution of the research is the design of a real-time feasible framework for the control of signal timings that can optimize the distribution of traffic over a network while taking into account the upstream propagating waves caused by spillback.

The hierarchical control framework consists of two layers. The top layer - called the network coordination layer - consists of the linear MPC strategy for urban traffic networks (LML-U) of van de Weg et al. [1] that optimizes the aggregated traffic dynamics. The LML-U strategy distributes the traffic over the network so that the average throughput is maximized over the prediction horizon. In this
paper, the optimized control signal is translated to nearfuture reference outflow trajectories for the entire prediction horizon of the links in the network. These reference outflow trajectories represent average desired link outflows over time which cannot be directly applied to the network since they represent average traffic flows while traffic lights require a green-red switching signal. Hence, the bottom layer - called the individual intersection layer - which consists of the local intersection controllers maps the reference outflow trajectories to a green-red switching signal. The goal of these controllers is to select the stage at every time step that minimizes the error with the reference outflow trajectories. The framework is designed in such a way that control strategies other than the one implemented in this paper may be used in both the top and bottom layers.The proposed framework is evaluated using simulation experiments.

The second contribution of the paper is to show that compared to locally optimizing the intersection outflows, the resulting control strategy can improve the throughput by distributing traffic over the network in spillback conditions. This is shown quantitatively by comparing the proposed strategy to a strategy that optimizes the local intersection outflows, and qualitatively by studying the realized traffic states.

The third contribution of the paper is to provide insight into the controller performance when varying the controller sampling times and when applied to different process models. The reason why this is studied is that an important issue of MPC strategies is that the mismatch between the prediction and process model may negatively affect the controller performance. One way to limit the impact of this mismatch is by reducing the sampling time of the controller, so that the possible prediction errors can be corrected more frequently by using new measurements. In the proposed framework, the sampling times of the two layers can be varied, both of which may affect the controller performance. Reducing the sampling time of the individual intersection layer allows more frequent switching, leading to a better tracking of the reference outflow trajectories; reducing the sampling time of the network coordination layer allows for a more frequent correction of prediction errors. Qualitative analyses are carried out in which the sampling times of the different layers are varied. In addition, simulations are carried out with two different process models, namely, the LTM and the microscopic model Vissim that has a larger mismatch with the prediction model.

## C. Design Considerations

Several factors were considered when designing the control strategy in order to simplify the problem or to emphasize the most important control features.

As stated before, an intersection control program is rather complex. To simplify this, we assume that there is no fixed stage sequence. Also, no minimum green times, and no fixed cycle times are used. Clearance times - i.e., the time used to clear the intersection between two conflicting stages - are included in the approach.

The control strategy has to be real-time feasible. This means that the time it takes to compute the control signal is shorter

![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-03.jpg?height=926&width=877&top_left_y=200&top_left_x=1083)
Fig. 1. Schematic overview of the control strategy.

than the controller sampling time, which is typically in the range of one to several minutes. A longer controller sampling time is beneficial, since it allows more time to optimize the control signal. However, the controller sampling time should be kept short so that the controller can quickly respond to traffic changes and unexpected events.

The aim of the controller is to improve the throughput. In practice, other performance indicators might also be included, such as equity, pollution, and reliability. Their inclusion, however, is beyond the scope of this paper.

Finally, the paper focuses on networks used solely by motorized traffic. The extension to networks used by heterogenous traffic - e.g. cars, trucks, public transport, and bicycles - is left for further research.

## II. Controller Design

In order to bridge the gap between the high computation time required by optimization based control strategies and the low computation time, but lower expected performance, of feedback-based control strategies, a hierarchical control framework is proposed in this paper. The framework is presented in Figure 1 and consists of two layers:

1) The top layer uses an aggregated prediction model to optimize the network throughput every $T^{\text {ref }}$ seconds, where $T^{\text {ref }}$ is in the range of one to several minutes. The control signal consists of the fractions of green time that every stream in the network has to realize, but which are not directly applicable by the traffic signal controllers. Nevertheless, the desired behavior of the traffic system - for instance, a prediction of link outflows - can be derived from this signal. Hence, reference outflow trajectories can be derived from the optimized

![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-04.jpg?height=438&width=1766&top_left_y=202&top_left_x=176)
Fig. 2. Schematic overview of the timing used. In this example, the sampling time $T$ is 1 second, the intersection controller sampling time $T^{\text {local }}$ is 5 seconds, the prediction model sampling time $T^{c}$ is 10 seconds, the coordination layer sampling time $T^{\text {ref }}$ is 60 seconds, and the prediction horizon $N^{p}$ is 30 steps.

signal, such as the reference cumulative outflow of a link, or a reference number of vehicles that has to be present in the link.
2) The bottom layer consists of the local intersection controllers. The task of the local intersection controllers is to track the reference outflows. This is realized by selecting every $T^{\text {local }}$ seconds - in the range of 5 to 10 seconds - the stage that is expected to lead to the smallest reference tracking error in the next $T^{\text {local }}$ seconds. The local intersection controllers may not be able to track the reference outflows exactly, because they were determined using a simplified traffic flow model. However, it is expected that the average behavior of the local intersection controllers will lead to improved network performance when the tracking error remains small.

The advantage of this framework is that the signal timings are determined in a decentralized way; i.e., every intersection requires only measurements of the direct upstream and downstream links. However, due to the tracking of the reference outflows, the individual intersection controllers are capable of realizing network-wide performance improvements.

The idea behind the proposed framework is that different control algorithms can be applied to the different layers. In this way, the framework can be adapted to different traffic networks, situations, and desired controller properties. As a proof-of-concept, Section II-B details the implementation of a linear MPC strategy - called LML-U - based on the link transmission model in the coordination layer, and Section II-C presents a greedy reference tracking (GRT) strategy for the individual intersection controller layer. Hence, the proposed strategy is called LML-U + GRT. In Section III, simulation results of this implementation are presented.

## A. Timing

Discrete timing is considered in this paper. The time step $k(-)$ and sampling time $T(\mathrm{~s})$ refer to the period $t \in$ $[T k, T(k+1))(\mathrm{s})$. It is assumed that the sampling time of the measurements is equal to $T$. The prediction model has a sampling time step $k^{\mathrm{c}}(-)$ and sampling time $T^{c}(\mathrm{~s})$. It holds that $T^{\mathrm{c}}=\epsilon^{\mathrm{c}} T$ with the factor $\epsilon^{\mathrm{c}} \in \mathcal{Z}^{+}$- i.e., it is a strictly positive integer. The intersection controllers select a new stage to actuate every controller sampling time step $k^{\text {local }}(-)$ with controller sampling time step $T^{\text {local }}(\mathrm{s})$ for which it holds that $T^{\text {local }}=\epsilon^{\text {local }} T$, with the factor $\epsilon^{\text {local }} \in \mathcal{Z}^{+}$. The reference outflow trajectory is updated every time step $k^{\text {ref }}(-)$ with the sampling time step $T^{\text {ref }}=\epsilon^{\text {ref }} T$ seconds, with $\epsilon^{\text {ref }} \in \mathcal{Z}^{+}$. It also holds that $T^{\text {ref }}=\epsilon^{\text {c,ref }} T^{\mathrm{c}}$, with $\epsilon^{\text {c,ref }} \in \mathcal{Z}^{+}$. It follows that $k=\left(k^{\text {local }}-1\right) \epsilon^{\text {local }}+1=\left(k^{\mathrm{c}}-1\right) \epsilon^{\mathrm{c}}+1=\left(k^{\text {ref }}-1\right) \epsilon^{\text {ref }}+1$, and that $k^{\mathrm{c}}=\left(k^{\text {ref }}-1\right) \epsilon^{\text {c } \text {,ref }}+1$. Figure 2 provides an overview of the timing used in this paper.

It must be noted that a measurement that is available at time step $k$ reflects the traffic state at the beginning of the time period $k$. It is thus not possible to change the control action at time step $k$. Hence, at time step $k$ the control signal for the next time step $k+1$ will be determined. So, in this paper the control action at time step $k^{\text {local }}$ is determined based on the data available at time step $\left(k^{\text {local }}-1\right) \epsilon^{\text {local }}=k$.

## B. Network Coordination Layer: LML-U Approach

The task of the network coordination layer - i.e., the top layer of the proposed framework - is to determine the reference outflows that optimize the network throughput. Recall that the coordination layer sampling time $T^{\text {ref }}($ s $)$ is in the range of one to several minutes. Hence, in order to satisfy real-time feasibility, the coordination layer has to be able to compute the reference outflow trajectories within one to several minutes.

To this end, the recently developed linear model predictive control strategy using the link transmission model for urban traffic networks (LML-U) is chosen in the coordination layer [1]. This approach has the advantage that it considers all relevant first-order traffic dynamics - i.e., upstream and downstream propagating waves - using only two traffic states. Compared to segment-based models, such as the CTM, this is more efficient from a computational point of view. The approach requires a prediction of the traffic demand, turnfractions, and maximum network outflows. Its output consists of the optimized fractions of green time used by the traffic streams in the network. The remainder of this section first discusses the prediction model used in more detail, next the optimization problem is introduced, and finally the approach to compute the reference outflow trajectories from the optimization output is presented.

1) The Prediction Model: The prediction model used in the LML-U control strategy is the LTM. The main elements used

$$
\begin{aligned}
N_{i^{\mathrm{L}}}^{\mathrm{in}}\left(k^{\mathrm{c}}+1\right) & =N_{i^{\mathrm{L}}}^{\mathrm{in}}\left(k^{\mathrm{c}}\right)+\sum_{j^{\mathrm{L}} \in \mathcal{I}_{i^{\mathrm{L}}}^{\mathrm{L}, \text { us }}}\left(\eta_{j^{\mathrm{L}}, i^{\mathrm{L}}}\left(k^{\mathrm{c}}\right) b_{i^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right) q_{i^{\mathrm{L}}}^{\text {sat }} T^{\mathrm{c}}\right)+\sum_{i^{\mathrm{O}} \in \mathcal{I}_{i^{\mathrm{L}}}^{\mathrm{O}, \text { us }}}\left(\eta_{i^{\mathrm{O}}, i^{\mathrm{L}}}\left(k^{\mathrm{c}}\right) b_{i^{\mathrm{O}}}^{\text {eff, } \mathrm{O}}\left(k^{\mathrm{c}}\right) q_{i^{\mathrm{O}}}^{\text {cap }} T^{\mathrm{c}}\right), \\
N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}+1\right) \leq & \gamma_{i^{\mathrm{L}}}^{\text {c,free }} N_{i^{\mathrm{L}}}^{\text {in }}\left(k^{\mathrm{c}}-k_{i^{\mathrm{L}}}^{\mathrm{c}, \text { free }}+2\right)+\left(1-\gamma_{i^{\mathrm{L}}}^{\mathrm{c}, \text { free }}\right) N_{i^{\mathrm{L}}}^{\text {in }}\left(k^{\mathrm{c}}-k_{i^{\mathrm{L}}}^{\mathrm{c}, \text { free }}+1\right), \\
N_{i^{\mathrm{L}}}^{\text {in }}\left(k^{\mathrm{c}}+1\right) \leq & \gamma_{i^{\mathrm{L}}}^{\text {c,shock }} N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}-k_{i^{\mathrm{L}}}^{\mathrm{c}, \text { shock }}+2\right)+\left(1-\gamma_{i^{\mathrm{L}}}^{\mathrm{c}, \text { shock }}\right) N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}-k_{i^{\mathrm{L}}}^{\mathrm{c}, \text { shock }}+1\right)+n_{i^{\mathrm{L}}}^{\text {max }}, \\
J^{\mathrm{TTS}} & \left.=\sum_{k^{\mathrm{c}}=\left(k^{\text {ref }}-1\right) \epsilon^{\mathrm{c}, \text { ref }}+1} T^{\mathrm{c}}\left\{\sum_{i^{\mathrm{L}} \in \mathcal{I}^{\mathrm{L}}}\left(N_{i^{\mathrm{L}}}^{\text {in }}\left(k^{\mathrm{c}}\right)-N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}\right)\right)+\sum_{i^{\mathrm{O}}, \text { ref }}\left(k^{\mathrm{c}}\right)-N_{i^{\mathrm{O}}}^{\mathrm{O}, \text { out }}\left(k^{\mathrm{c}}\right)\right)\right\},
\end{aligned}
$$

here are links - indicated with index $i^{\mathrm{L}}(-)-$ and origins - indicated with index $i^{\mathrm{O}}(-)$. The traffic dynamics of origins and links are updated using two traffic states; the cumulative link inflow $N_{i^{\mathrm{L}}}^{\text {in }}\left(k^{\mathrm{c}}\right)$ (veh) and outflow $N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}\right)$ (veh), and the cumulative origin inflow $N_{i}^{\mathrm{O}, \text { in }}\left(k^{\mathrm{c}}\right)$ (veh) origin outflow $N_{i \mathrm{O}}^{\mathrm{O}, \mathrm{in}}\left(k^{\mathrm{c}}\right)$ (veh). Every outflow is controlled using a control parameter $b_{i^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right)$ for links and $b_{i^{\mathrm{O}}}^{\text {eff }, \mathrm{O}}\left(k^{\mathrm{c}}\right)$ for origins that expresses the effective fraction of green time used during the time step $k^{\mathrm{c}}$. Note that this optimization approach is presented in more detail in [1]. The interested reader is referred to [21] for a more detailed description of the LTM.

The cumulative link outflow is updated using the following equation:

$$
N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}+1\right)=N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}\right)+q_{i^{\mathrm{L}}}^{\text {sat }} T^{\mathrm{c}} b_{i^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right),
$$

where $q_{i}^{\text {sat }}(\mathrm{veh} / \mathrm{h})$ is the saturation rate. The cumulative link inflow is modeled as the sum of the outflows of upstream links $j^{\mathrm{L}} \in \mathcal{I}_{i^{\mathrm{L}}}^{\mathrm{L}, \text { us }}$ and origins $i^{\mathrm{O}} \in \mathcal{I}_{i^{\mathrm{L}}}^{\mathrm{O}, \text { us }}$ multiplied by the turn-fractions $\eta_{j}{ }^{\mathrm{L}},{ }_{i} \mathrm{~L}(k)$ as given in (2), as shown at the top of this page, where the set $\mathcal{I}_{i}^{\mathrm{L}}$, us is the set of links directly upstream of link $i^{\mathrm{L}}$, and the set $\mathcal{I}_{i^{\mathrm{L}}}^{\mathrm{O}, \mathrm{us}}$ is the set of origins directly upstream of link $i^{\mathrm{L}}$. The fraction $\eta_{j}{ }^{\mathrm{L}},{ }_{i} \mathrm{~L}\left(k^{\mathrm{c}}\right)$ indicates the turn-fraction from link $j^{\mathrm{L}}$ to link $i^{\mathrm{L}}$, and the fraction $\eta_{i}{ }^{\mathrm{O}, i^{\mathrm{L}}}\left(k^{\mathrm{c}}\right)(-)$ indicates the turn-fraction from origin $i^{\mathrm{O}}$ to link $i^{\mathrm{L}}$.

In order to model free-flow dynamics, the cumulative link outflow is bound from above, so that vehicles cannot travel through the link faster than the free flow travel time $t_{i^{\mathrm{L}}}^{\text {free }}(\mathrm{s})$. This can be written as a constraint on the cumulative outflow as given in (3), as shown at the top of this page. In (3) the number of time steps $k_{i^{\mathrm{L}}}^{\mathrm{c}, \text { free }}=\left\lceil t_{i^{\mathrm{L}}}^{\text {free }} / T^{\mathrm{c}}\right\rceil(-)$, and the fraction $\gamma_{i \mathrm{~L}}^{\mathrm{c} \text {, free }}=k_{i \mathrm{~L}}^{\mathrm{c} \text {, free }}-t_{i \mathrm{~L}}^{\text {free }} / T^{\mathrm{c}}(-)$ are used to linearly interpolate the cumulative curve, as detailed in [1]. The mathematical operator $\lceil\cdot\rceil$ rounds the argument of the function to the nearest integer that is higher than the argument of the function. In order to satisfy CFL conditions, it should hold that $k_{i \mathrm{~L}}^{\mathrm{c}, \text { free }} \geq 2$.

Similarly, upstream propagating waves caused by spillback are included by bounding the cumulative link inflow from above so that a vehicle can only enter a link $t_{i^{\mathrm{L}}}^{\text {shock }}(\mathrm{s})$ seconds after the vehicle $n_{i \mathrm{~L}}^{\text {max }}$ (veh) has exited the link, as given in (4), as shown at the top of this page, with the number of time steps $k_{i}^{\mathrm{c} \text {, shock }}=\left\lceil t_{i \mathrm{~L}}^{\text {shock }} / T^{\mathrm{c}}\right\rceil(-)$, and the fraction $\gamma_{i \mathrm{~L}}^{\mathrm{c} \text {,shock }}=$ $k_{i^{\mathrm{L}}}^{\mathrm{c} \text {,shock }}-t_{i^{\mathrm{L}}}^{\text {shock }} / T^{\mathrm{c}}(-)$. It should hold that $k_{i^{\mathrm{L}}}^{\mathrm{c}, \text { shock }} \geq 2$ in order to guarantee CFL conditions.

Outflow limitations at the network are modeled as external disturbances - i.e., inputs that cannot be affected by the control signal. So, when a link is at an exit of the network, an extra constraint is added:

$$
N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}+1\right) \leq N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}\right)+q_{i^{\mathrm{L}}}^{\text {out, } \max }\left(k^{\mathrm{c}}\right) T^{\mathrm{c}},
$$

where $q_{i}^{\text {out, max }}\left(k^{\mathrm{c}}\right)($ veh $/ \mathrm{h})$ is the maximum outflow that can exit the link at time step $k^{\mathrm{c}}$.

Origins are modeled as vertical queues via the following state update equations and constraints:

$$
\begin{aligned}
N_{i^{\mathrm{O}}}^{\mathrm{O}, \text { in }}\left(k^{\mathrm{c}}+1\right) & =N_{i^{\mathrm{O}}}^{\mathrm{O}, \text { in }}\left(k^{\mathrm{c}}\right)+d_{i^{\mathrm{O}}}^{\text {in }}\left(k^{\mathrm{c}}\right) T^{\mathrm{c}}, \\
N_{i^{\mathrm{O}}}^{\mathrm{O}, \text { out }}\left(k^{\mathrm{c}}+1\right) & =N_{i^{\mathrm{O}}}^{\mathrm{O}, \text { out }}\left(k^{\mathrm{c}}\right)+q_{i^{\mathrm{O}}}^{\text {cap }} T^{\mathrm{c}} b_{i^{\mathrm{O}}}^{\text {eff, } \mathrm{O}}\left(k^{\mathrm{c}}\right), \\
N_{i^{\mathrm{O}}}^{\mathrm{O}, \text { out }}\left(k^{\mathrm{c}}+1\right) & \leq N_{i^{\mathrm{O}}}^{\mathrm{O}, \text { in }}\left(k^{\mathrm{c}}+1\right) .
\end{aligned}
$$

with $q_{i}^{\text {cap }}($ veh $/ \mathrm{h})$ the origin capacity.
The final constraints concern the effective fractions $b_{i^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right)$ and $b_{i^{\mathrm{O}}}^{\text {eff, } \mathrm{O}}\left(k^{\mathrm{c}}\right)$ of green-time which should be between 0 and 1. Additionally, if there is a conflict $i^{\text {con }}$ between links at an intersection - i.e., $\left\{j^{\mathrm{L}}, i^{\mathrm{L}}\right\} \in \mathcal{I}_{i^{\text {con }}}^{\text {conflict }}$ - the sum of the effective green fractions $b_{i^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right)+b_{j^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right)$ should be less than $1-\theta_{i^{\text {con }}}$. The tuning parameter $\theta_{i}$ con (-) is used to prevent infeasible reference outflows that can occur when a clearance time has to be respected when switching link $i^{\mathrm{L}}$ to $j^{\mathrm{L}}$. This results in the following constraints:

$$
\begin{aligned}
& 0 \leq b_{i^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right) \leq 1, \\
& 0 \leq b_{i^{\mathrm{e}}}^{\text {eff }, \mathrm{O}}\left(k^{\mathrm{c}}\right) \leq 1, \\
& 0 \leq b_{i^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right)+b_{j^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right) \leq 1-\theta_{i^{\text {con }}} .
\end{aligned}
$$

2) The Optimization Problem: The objective of the linear optimization problem is to minimize the total time spent (TTS) $J^{\text {TTS }}$ (veh ⋅ h) used by all the vehicles in the network over a prediction horizon $N^{p}(-)$ subject to the linear model and constraints presented in the previous section. The TTS can be expressed as the total number of vehicles in the network at every time step $k^{\mathrm{c}}$ mutiplied by the sampling time $T^{c}$ and summed over the time steps $k^{\mathrm{c}}=\left(k^{\text {ref }}-1\right) \epsilon^{\text {c,ref }}+$ $1, \ldots,\left(k^{\text {ref }}-1\right) \epsilon^{\text {c,ref }}+N^{\mathrm{p}}+1$, as given in (12), as shown at the top of this page. There, $\mathcal{I}^{\mathrm{L}}(-)$ represents the set of all links and $\mathcal{I}^{\mathrm{O}}(-)$ represents the set of all origins.

As in [1], minimizing the TTS can be written as the following linear optimization problem:

$$
\begin{aligned}
& \min _{\bar{u}\left(k^{\mathrm{ref}}\right)} Z \tilde{B} \bar{u}\left(k^{\mathrm{ref}}\right)+Z\left(\tilde{A} x\left(k^{\mathrm{ref}}\right)+\tilde{C} \bar{d}\left(k^{\mathrm{ref}}\right)\right), \\
& \text { Subject to } M^{\text {ineq }} \bar{u}\left(k^{\mathrm{ref}}\right) \leq V^{\text {ineq }},
\end{aligned}
$$

$$
\begin{aligned}
u\left(k^{\mathrm{c}}\right) & =\left[\begin{array}{lllll}
b_{1}^{\text {eff }}\left(k^{\mathrm{c}}\right) & \ldots & b_{n^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right) & b_{1}^{\text {eff, } \mathrm{O}}\left(k^{\mathrm{c}}\right) & \ldots \\
d\left(k^{\mathrm{c}}\right) & =\left[\begin{array}{llll}
d_{1}^{\text {in }}\left(k^{\mathrm{c}}\right) & \ldots & d_{n^{\mathrm{o}}}^{\text {in } \mathrm{o}}\left(k^{\mathrm{c}}\right)
\end{array}\right]^{\top}, \\
\bar{x} & =\left[\begin{array}{llll}
x\left(\left(k^{\mathrm{ref}}-1\right) \epsilon^{\mathrm{c}, \text { ref }}+2\right) & \ldots & x\left(\left(k^{\text {ref }}-1\right) \epsilon^{\mathrm{c}, \text { ref }}+N^{\mathrm{p}}+1\right)
\end{array}\right]^{\top} . \\
x_{i^{\mathrm{L}}}^{\mathrm{L}}\left(k^{\mathrm{c}}\right) & =\left[\begin{array}{llll}
N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}\right) & \ldots & N_{i^{\mathrm{L}}}^{\text {out }}\left(k^{\mathrm{c}}-k^{\mathrm{c}, \text { shock }}\right) & N_{i^{\mathrm{L}}}^{\text {in }}\left(k^{\mathrm{c}}\right) \\
\ldots & \ldots & N_{i^{\mathrm{L}}}^{\text {in }}\left(k^{\mathrm{c}}-k^{\mathrm{c}, \text { free }}\right)
\end{array}\right]^{\top} . \\
x_{i^{\mathrm{o}}}^{\mathrm{O}}\left(k^{\mathrm{c}}\right) & =\left[\begin{array}{llll}
N_{i^{\mathrm{o}}}^{\mathrm{O}, \text { out }}\left(k^{\mathrm{c}}\right) & N_{i^{\mathrm{o}}}^{\mathrm{O}, \text { in }}\left(k^{\mathrm{c}}\right)
\end{array}\right]^{\top} . \\
N_{i^{\mathrm{L}}}^{\text {out,ref }}\left(k^{\text {ref }}\right) & =\left[\begin{array}{llll}
N_{i^{\mathrm{L}}}^{\text {out }}\left(\left(k^{\text {ref }}-1\right) \epsilon^{\mathrm{c}, \text { ref }}+1\right. & N_{i^{\mathrm{L}}}^{\text {out }}\left(\left(k^{\text {ref }}-1\right) \epsilon^{\mathrm{c}, \text { ref }}+2\right. & \ldots & N_{i^{\mathrm{L}}}^{\text {out }}\left(\left(k^{\text {ref }}-1\right) \epsilon^{\mathrm{c}, \text { ref }}+N^{\mathrm{p}}+1\right)
\end{array}\right]^{\top} . \\
\hat{N}_{i^{\mathrm{L}}}^{\text {out,ref }}(\hat{k}) & =\left(\begin{array}{ll}
\left.1-\gamma^{\text {ref }}(\hat{k})\right) N_{i^{\mathrm{L}}}^{\text {out,ref }}\left(\hat{k}^{\mathrm{c}}(\hat{k})\right)+\gamma^{\text {ref }}\left(\hat{k} N_{i^{\mathrm{L}}}^{\text {out,ref }}\left(\hat{k}^{\mathrm{c}}(\hat{k})+1\right)\right.
\end{array} .\right.
\end{array} .\right.
\end{aligned}
$$

Here, the matrices $\tilde{A}, \tilde{B}$, and $\tilde{C}$ as detailed in [1] describe the traffic dynamics, so that a prediction of the traffic state $\bar{x}\left(k^{\text {ref }}\right)$, as defined by equations 1, 2, 6, and 7, can be computed by multiplication of the control vector $\bar{u}\left(k^{\text {ref }}\right)$ by $\tilde{B}$, the initial traffic state $x\left(k^{\text {ref }}\right)$ by $\tilde{A}$, and a prediction of the disturbances $\bar{d}\left(k^{\text {ref }}\right)-$ i.e., inputs that cannot be controlled - by $\tilde{C}$. The matrix $M^{\text {ineq }}$ and vector $V^{\text {ineq }}$ as detailed in [1] contain the inequality constraints of equations 3, 4, 5, 8, 9, 10, and 11. Multiplication of the vector $Z$ by the predicted state gives the TTS.

The vector $\bar{u}\left(k^{\text {ref }}\right)$ contains the effective fractions of green time $b_{i^{\mathrm{L}}}^{\text {eff }}\left(k^{\mathrm{c}}\right)$ and $b_{i^{\mathrm{O}}}^{\text {eff }}\left(k^{\mathrm{c}}\right)$ used by the links and origins in the network at the time steps $k^{\mathrm{c}}=\left(k^{\text {ref }}-1\right) \epsilon^{\text {c,ref }}+1, \ldots,\left(k^{\text {ref }}-1\right)$ $\epsilon^{\mathrm{c}, \text { ref }}+N^{\mathrm{p}}$ :

$$
\bar{u}\left(k^{\mathrm{ref}}\right)=\left[\begin{array}{c}
u\left(\left(k^{\mathrm{ref}}-1\right) \epsilon^{\mathrm{c}, \mathrm{ref}}+1\right) \\
\vdots \\
u\left(\left(k^{\mathrm{ref}}-1\right) \epsilon^{\mathrm{c}, \mathrm{ref}}+N^{\mathrm{p}}\right)
\end{array}\right],
$$

The disturbance vector $\bar{d}\left(k^{\text {ref }}\right)$ contains the traffic demands $d\left(k^{\mathrm{c}}\right)$ at time steps $k^{\mathrm{c}}=\left(k^{\text {ref }}-1\right) \epsilon^{\text {c,ref }}+1, \ldots,\left(k^{\text {ref }}-1\right)$ $\epsilon^{\mathrm{c}, \text { ref }}+N^{\mathrm{p}}$ :

$$
\bar{d}\left(k^{\mathrm{ref}}\right)=\left[\begin{array}{c}
d\left(\left(k^{\mathrm{ref}}-1\right) \epsilon^{\mathrm{c}, \mathrm{ref}}+1\right) \\
\vdots \\
d\left(\left(k^{\mathrm{ref}}-1\right) \epsilon^{\mathrm{c}, \mathrm{ref}}+N^{\mathrm{p}}\right)
\end{array}\right],
$$

The control vector $u\left(k^{\mathrm{c}}\right)$ and disturbance vector $d\left(k^{\mathrm{c}}\right)$ at a time step $k^{\mathrm{c}}$ are given in (16) and (17), as shown at the top of this page, respectively, where $n^{\mathrm{L}}(-)$ indicates the number of links and $n^{\mathrm{O}}(-)$ the number of origins.
3) The Reference Outflow Trajectory: The outcome of the optimization problem (13) is the vector $\bar{u}^{*}\left(k^{\text {ref }}\right)$ ( - ). As noted before, this signal cannot be directly applied to the local intersection controllers due to the aggregated nature of the traffic flow model that is used to formulate the linear optimization problem. Instead, a reference outflow trajectory is derived from the optimized signal $\bar{u}^{*}\left(k^{\text {ref }}\right)$.

A prediction of the traffic states $\bar{x}\left(k^{\text {ref }}\right)$ can be obtained as follows:

$$
\bar{x}\left(k^{\mathrm{ref}}\right)=\tilde{A} x\left(k^{\mathrm{ref}}\right)+\tilde{B} \bar{u}^{*}\left(k^{\mathrm{ref}}\right)+\tilde{C} \bar{d}\left(k^{\mathrm{ref}}\right) .
$$

The prediction of the state $\bar{x}\left(k^{\text {ref }}\right)$ consists of the traffic states $x\left(k^{\mathrm{c}}\right)$ at time steps $k^{\mathrm{c}}=\left(k^{\text {ref }}-1\right) \epsilon^{\text {c, ref }}+2, \ldots,\left(k^{\text {ref }}-\right.$ $1) \epsilon^{\mathrm{c}, \text { ref }}+N^{\mathrm{p}}$, as given in (19), as shown at the top of this page. In its turn, the state $x\left(k^{\mathrm{c}}\right)$ consists of the states of the links $x_{i^{\mathrm{L}}}^{\mathrm{L}}\left(k^{\mathrm{c}}\right)$ and origins $x_{i^{\mathrm{O}}}^{\mathrm{L}}\left(k^{\mathrm{c}}\right)$ at time step $k^{\mathrm{c}}$ :

$$
x\left(k^{\mathrm{c}}\right)=\left[x_{1}^{\mathrm{L}}\left(k^{\mathrm{c}}\right) \ldots x_{n^{\mathrm{L}}}^{\mathrm{L}}\left(k^{\mathrm{c}}\right) x_{1}^{\mathrm{O}}\left(k^{\mathrm{c}}\right) \ldots x_{n^{\mathrm{o}}}^{\mathrm{O}}\left(k^{\mathrm{c}}\right)\right]^{\top} .
$$

The states of link $x_{i^{\mathrm{L}}}^{\mathrm{L}}\left(k^{\mathrm{c}}\right)$ and origin $x_{i^{\mathrm{O}}}^{\mathrm{O}}\left(k^{\mathrm{c}}\right)$ at time step $k^{\mathrm{c}}$ are given in (21) and (22), as shown at the top of this page.

Now, a reference cumulative outflow trajectory $N_{i^{\mathrm{L}}}^{\text {out,ref }}\left(k^{\mathrm{c}}\right)$ as given in (23), as shown at the top of this page, can be derived from $\bar{x}\left(k^{\mathrm{c}}\right)$ for every link $i^{\mathrm{L}} \in \mathcal{I}^{\text {controlled }}$ for all the time steps $k^{\mathrm{c}}=\left(k^{\text {ref }}-1\right) \epsilon^{\mathrm{c}, \text { ref }}+1, \ldots,\left(k^{\text {ref }}-1\right) \epsilon^{\mathrm{c}, \text { ref }}+N^{\mathrm{p}}$.

Since the sampling time of the prediction model is a multiple of the measurements sampling time - i.e $T^{\mathrm{c}}=\epsilon^{\mathrm{c}} T-$, the signal $N_{i^{\mathrm{L}}}^{\text {out,ref }}$ ( $k^{\text {ref }}$ ) has to be resampled. Equation (24), as shown at the top of this page, shows how the reference outflow $\hat{N}_{i \mathrm{~L}}^{\text {out }, \text { ref }}(\hat{k})$ at an arbitrary time step $\hat{k} \in\left(k^{\text {ref }}-1\right) \epsilon^{\text {ref }}+$ $1, \ldots,\left(k^{\text {ref }}+N^{\mathrm{p}} \epsilon^{\text {c } \text {,ref }}\right) \epsilon^{\text {ref }}+1$ can be obtained. Here, the time step $\hat{k}^{\mathrm{c}}(\hat{k})$ is given as:

$$
\hat{k}^{\mathrm{c}}(\hat{k})=\left\lfloor\hat{k} / T^{\mathrm{c}}\right\rfloor,
$$

and the fraction $\gamma^{\text {ref }}(\hat{k})$ is the residual of a time step that $\hat{k}$ exceeds $\hat{k}^{\mathrm{c}}(\hat{k})$ :

$$
\gamma^{\mathrm{ref}}(\hat{k})=\frac{\hat{k}-\hat{k}^{\mathrm{c}}(\hat{k})}{T^{\mathrm{c}}} .
$$

## C. Local Intersection Layer: Greedy Reference Tracking

The task of the local intersection layer is to actuate at every time step $k^{\text {local }}$ and at every intersection the stage that leads to the smallest reference tracking error. The reference tracking error of a stage is defined as a measure of the error between the reference outflow trajectories and the potential outflows of the different streams at an intersection when actuating that stage.

The stage selection is done in a decentralized way, which is possible because the time step $T^{\text {local }}$ is chosen to be short - i.e., in the range of several seconds -, and no fixed stage sequence is assumed. The tracking strategy is called greedy, since it selects the stage that minimizes the reference tracking error for a short time horizon $T^{\text {local }}$. An alternative would be to implement a strategy that minimizes the tracking error over a longer time horizon. However, this would require predicting the outflow of many different stage sequences,

$$
\begin{aligned}
& N_{i^{\mathrm{L}}}^{\text {out, } \mathrm{p}}\left(\hat{k}+1 \mid k, p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)=\min \left\{N_{i^{\mathrm{L}}}^{\text {out, } \mathrm{p}}\left(\hat{k} \mid k, p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)+q_{i^{\mathrm{L}}}^{\text {sat }} T b_{i^{\mathrm{L}}}(\hat{k}), \ldots\right. \\
& \left.\times N_{i^{\mathrm{L}}}^{\text {out }, \text { free }}(\hat{k}+1), N_{i^{\mathrm{L}}}^{\text {out,sp }}(\hat{k}+1)\right\} \quad \forall i^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{US}} . \\
& N_{i^{\mathrm{L}}}^{\text {out,free }}(k+1)=\gamma_{i^{\mathrm{L}}}^{\text {free }} N_{i^{\mathrm{L}}}^{\text {in }}\left(k-k_{i^{\mathrm{L}}}^{\text {free }}+2\right)+\left(1-\gamma_{i^{\mathrm{L}}}^{\text {free }}\right) N_{i^{\mathrm{L}}}^{\text {in }}\left(k-k_{i^{\mathrm{L}}}^{\text {free }}+1\right) \text {. } \\
& N_{i^{\mathrm{L}}}^{\text {out }, \text { sp }}(k+1)=N_{i^{\mathrm{L}}}^{\text {out, } \mathrm{p}}(k)+\gamma_{j \mathrm{~L}}^{\text {shock }} N_{j \mathrm{~L}}^{\text {out }}\left(k-k_{j \mathrm{~L}}^{\text {shock }}+2\right)+\left(1-\gamma_{j \mathrm{~L}}^{\text {shock }}\right) N_{j \mathrm{~L}}^{\text {out }}\left(k-k_{j \mathrm{~L}}^{\text {shock }}+1\right)+n_{j \mathrm{~L}}^{\text {max }}-N_{j \mathrm{~L}}^{\text {in,p }}(k) \text {. } \\
& N_{i^{\mathrm{L}}}^{\mathrm{in}, \mathrm{p}}\left(\hat{k}+1 \mid k, p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)=\sum_{j^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{US}}} \eta_{j^{\mathrm{L}}, i^{\mathrm{L}}}(\hat{k})\left(N_{i^{\mathrm{L}}}^{\text {out, } \mathrm{p}}\left(\hat{k}+1 \mid k, p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)-\ldots\right. \\
& \left.N_{i^{\mathrm{L}}}^{\text {out, } \mathrm{p}}\left(\hat{k} \mid k, p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)\right) \quad \forall i^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{DS}} . \\
& \bar{e}_{i \text { inter }}\left(p_{i \text { inter }}\left(k^{\text {local }}\right)\right)=\gamma^{\mathrm{e}} \hat{e}_{i}^{\mathrm{a}} i_{\text {inter }}\left(p_{i \text { inter }}\left(k^{\text {local }}\right)\right)+\left(1-\gamma^{\mathrm{e}}\right) \hat{e}_{i \text { inter }}^{\mathrm{b}}\left(p_{i \text { inter }}\left(k^{\text {local }}\right)\right) \text {. } \\
& \hat{e}_{i^{\text {inter }}}^{\mathrm{a}}\left(p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)=\sum_{\hat{k}=k+2}^{k+\epsilon^{\text {local }}+1} \sum_{i^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{US}}}\left(\hat{N}_{i^{\mathrm{L}}}^{\text {out,ref }}(\hat{k})-N_{i^{\mathrm{L}}}^{\text {out,p }}(\hat{k})\right)^{2} . \\
& \hat{e}_{i^{\text {inter }}}^{\mathrm{b}}\left(p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)=\sum_{\hat{k}=k+2}^{k+\epsilon^{\text {local }}+1}\left|\left(\sum_{i^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{US}}} \hat{N}_{i^{\mathrm{L}}}^{\text {out,ref }}(\hat{k})-\sum_{i^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{US}}} N_{i^{\mathrm{L}}}^{\text {out, } \mathrm{p}}(\hat{k})\right)\right| .
\end{aligned}
$$

and it would require taking into account the impact of the selected stage sequences of upstream and downstream intersections as well, leading to a complex optimization problem.

The greedy policy is computed for every intersection separately by carrying out the following steps:

1) predict for every stage the potential cumulative outflow of every link in the intersection when actuating the stage (see Section II-C1);
2) compute for every stage the resulting reference tracking error (see Section II-C2);
3) actuate the stage that is expected to realize the smallest reference tracking error (see Section II-C3).
1) Potential Cumulative Outflow Prediction: The first step is to predict, for every intersection $i^{\text {inter }}$ and stage $p_{i}{ }^{\text {inter }}\left(k^{\text {local }}\right) \in$ $\mathcal{P}_{i^{\text {inter }}}^{\text {stages }}$, with $\mathcal{P}_{i^{\text {inter }}}^{\text {stages }}$ the set of stages at the intersection, the potential cumulative outflows $N_{i^{\mathrm{L}}}^{\text {out }, \mathrm{p}}\left(\hat{k} \mid k, p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)$ (veh) of the links $i^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{US}}$ directly upstream of the intersection using (27), as shown at the top of this page, for the time steps $\hat{k}=k+1, \ldots, k+\epsilon^{\text {local }}+1$. In this equation, the maximum link outflow $N_{i^{\mathrm{L}}}^{\text {out,free }}(k+1)$ (veh) in freeflow conditions is computed using (28), as shown at the top of this page. It is assumed that $T^{\text {local }}<t_{i^{\mathrm{L}}}^{\text {free }} \forall i^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{US}}$, so that the outflow $N_{i^{\mathrm{L}}}^{\text {out, free }}(k)$ depends on historical control decisions at the upstream intersections only. The maximum possible cumulative outflow under spillback from a downstream link $j^{\mathrm{L}} \in \mathcal{I}_{i^{\mathrm{L}}}^{\mathrm{DS}}$ is computed using (29), as shown at the top of this page. It is assumed that $T^{\text {local }}<t_{i^{\mathrm{L}}}^{\text {shock }} \forall i^{\mathrm{L}} \in \mathcal{I}_{i^{\text {inter }}}^{\mathrm{DS}}$, so that the maximum outflow $N_{i \mathrm{~L}}^{\text {out, sp }}(k)$ depends on historical control decisions at the downstream intersections only.
The cumulative link inflows $N_{i^{\mathrm{L}}}^{\mathrm{in}, \mathrm{p}}\left(\hat{k} \mid k, p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)$ (veh) of the links $\mathcal{I}_{i^{\text {inter }}}^{\mathrm{DS}}$ directly downstream of the intersection when actuating the stage $p_{i}$ inter $^{\text {(local }}$ ) for the time steps

When clearance times have to be respected when switching from stage $p_{i \text { inter }}\left(k^{\text {local }}-1\right)$ to stage $p_{i}$ inter $\left(k^{\text {local }}\right)$, the corresponding values of $b_{i} \mathrm{~L}(\hat{k})$ in (27) are set to 0 for the first $T_{i^{\mathrm{L}}}^{\text {clear }}$ seconds.
2) Reference Tracking Error: Now that the predictions of the link outflows are available when actuating the different stages, the expected reference tracking error $\bar{e}_{i \text { inter }}\left(p_{i \text { inter }}\left(k^{\text {local }}\right)\right)$ can be computed using (31), as shown at the top of this page. It is defined as the weighted average of the error $\hat{e}_{i^{\text {inter }}}^{\mathrm{a}}\left(p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)-$ which is the square of the area between the reference outflow and the predicted outflow computed using (32), as shown at the top of this page, - and of the error $\hat{e}_{i^{\text {inter }}}^{\mathrm{b}}\left(p_{i^{\text {inter }}}\left(k^{\text {local }}\right)\right)-$ which is the error between the total intersection reference outflow and total predicted intersection outflow $\hat{e}_{i \text { inter }}^{\mathrm{b}}\left(p_{i \text { inter }}\left(k^{\text {local }}\right)\right)$ computed using (33), as shown at the top of this page. The parameter $\gamma^{\mathrm{e}}$ is introduced to balance the current reference tracking costs and the final reference tracking costs.
3) Stage Actuation: The final step is the actuation of the stage $p_{i}^{*}$ inter $\left(k^{\text {local }}\right)$ that leads to the smallest expected reference tracking error of all the streams that use the intersection using:

$$
p_{i^{\text {inter }}}^{*}\left(k^{\text {local }}\right)=\arg \min _{p_{i} \text { inter } \in \mathcal{P}_{i^{\text {stages }}}} \bar{e}_{i \text { inter }}\left(p_{i}^{\text {inter }}\left(k^{\text {local }}\right)\right) .
$$

4) Numerical Example: To clarify the reference tracking approach we have included the following simple numerical example. Assume that we have a network consisting of two conflicting links that can realize a flow equal to the saturation rate of 1000 veh/h when given green. It is also assumed that $T^{\text {local }}=5 \mathrm{~s}$, and that the reference outflows for time step 1 to 12 are computed by the network coordination layer as

![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-08.jpg?height=746&width=715&top_left_y=202&top_left_x=245)
Fig. 3. Small example of reference outflows and realized outflows.

600 and 300 veh/h respectively, as shown in Figure 3. The inter-stage clearance time when switching from stage 1 to 2 and vice versa is assumed to be 2 seconds. Assume that at every time step we can choose between actuating stage 1 - i.e., giving green to link 1 and red to link 2 - or actuating stage 2 - i.e., giving red to link 1 and green to link 2.

At time step $k=1$ the error is determined over time steps $k=3$ to $k=7$. For stage 1 , the total error computed using (31) is 0.85 while the error for stage 2 is 1.82 given that $\gamma^{\mathrm{e}}=0.3$. Because the error of stage 1 is smaller it will be activated. Next, at time step $k=6$, the error when actuating stage 1 is 2.28 while the error for actuating stage 2 is 1.82 . Hence, stage 2 will be activated. Note that in the error calculation the inter-stage clearance time between stage 1 and stage 2 is also accounted for.

## III. Simulation Experiments

Simulation experiments are carried out to show that the use of the individual intersection layer does not lead to significant performance degradation, and that the proposed framework is able to efficiently distribute the queues over the network in the presence of spillback. Additionally, the impact of the mismatch between the prediction and the process model is studied which is influenced by the selected process model and the chosen controller sampling times.

First simulations are carried out with the LTM as the process model, so that the mismatch between the process and prediction model is small. A comparison is made - in terms of TTS reduction and realized traffic states - with a controller that directly applies the reference outflows of the coordination layer to the model - which is only possible when using a macroscopic process model - giving the lowest possible TTS. This shows the TTS increase caused by the individual intersection layer. Next, the performance is compared with a greedy feedback policy that optimizes the signal timings of the local intersections. This provides insight into the ability of the

![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-08.jpg?height=565&width=862&top_left_y=202&top_left_x=1089)
Fig. 4. Schematic overview of the simulation set-up.

proposed framework to distribute queues more efficiently over the network in the presence of spillback. Next, the microscopic model Vissim 5.30 is used as the process model, which introduces a larger mismatch.

In both simulations, the controller sampling times $T^{\text {local }}$ and $T^{\text {ref }}$ are varied and the impact on the TTS and reference tracking error is analyzed. It is expected that a smaller sampling time $T^{\text {local }}$ leads to a lower TTS and a lower reference tracking error, because it allows more frequent switching of the stages. Similarly, it is expected that choosing a smaller sampling time $T^{\text {ref }}$ reduces the reference tracking error but does not necessarily reduce the TTS.

## A. Simulation Set-Up

The simulation set-up is shown in Figure 4. Every second, measurements are obtained from the process model - i.e., the LTM in Section III-B, and Vissim in Section III-C. The local control layer is updated every $T^{\text {local }}$ seconds, and the network coordination layer updates the reference outflow trajectories every $T^{\text {ref }}$ seconds. Figure 5 shows the network used in the simulations. It consists of three intersections; (1) top left, (2) top right, and (3) bottom right. The link lengths are indicated in the figure, where it must be noted that link 16 is 800 meters. It can also be seen that a bottleneck is located at the downstream end of link 7. This bottleneck is used to mimic a situation where downstream congestion is spilling back towards the controlled network. Alternatively, the bottleneck can represent a situation where the controlled network outflow is limited by a perimeter control strategy. A simulation period of 2500 seconds is considered. The demand pattern that is applied to the network consists of a high demand for the first 1800 seconds of respectively 900, 1100, and 1800 veh/h at links 1, 8, and 12. From time 1800 to 2500 seconds the demand is decreased to respectively 300, 250, and 200 veh/h at links 1, 8, and 12. This implies that in the high demand situation 600 veh/h want to go from links 5 to 7 and links 17 to 18, 500 veh/h from link 6 to link 19, and 600 veh/h from link 18 to link 19. The bottleneck at link 7 is activated from time 100 seconds with a capacity of 600 veh/h.

It is assumed that no measurement noise is present and that there is no uncertainty in the disturbance predictions. In this

![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-09.jpg?height=735&width=866&top_left_y=200&top_left_x=172)
Fig. 5. Schematic overview of the network used for the simulations, including the link lengths, location of the bottlenecks, and the turn-fractions.

way, controlled experiments can be carried out that allow studying the controller behavior in detail. It must be noted that there is a mismatch between the process model and the prediction model caused by the difference in the local control signals and the MPC output.
B. Simulation Set 1: Macroscopic Simulation Using the LTM

The first set of evaluations is carried out using the LTM as the process model. These evaluations are carried out in order to gain insight into the quantitative controller performance. The LTM allows a direct implementation of the reference outflows obtained from the network coordination layer and thus enables studying the reference tracking error incurred in the individual intersection control layer. The mean reference tracking error is defined as the average of the absolute difference between the reference outflows computed with the network coordination layer and the realized outflows.

1) Simulation Set 1: Set-Up: The LTM is implemented as the process model with a sampling time step of 1 second. Clearance times are not considered in this simulation set, and the tuning parameters $\theta_{i}$ con are set to 0 . This implies that the control strategies can actuate any stage at any time step $T^{\text {local }}$.

Three different control strategies are compared:

1) LML-U + GRT: this is the control strategy proposed in this paper.
2) LML-U: this is the LML-U strategy of the top layer with the optimized green-fractions directly applied to the network. Note that this implementation is not deployable, since these green-fractions can be simultaneously nonzero for conflicting traffic movements in a time interval. Comparing with this control policy gives an idea of the best possible TTS that can be obtained.
3) GCP: this is a greedy control policy (GCP) that tries to actuate the stage at every time step $T^{\text {local }}$ that will maximize the throughput of every individual intersection. This is realized by predicting for every stage

In the various simulations, the local control strategy sampling time $T^{\text {local }}$ is varied from 1 to 15 seconds. The coordination layer sampling time $T^{\text {ref }}$ is varied from 10 to 590 seconds. In this way the impact of the controller parameters on the controller performance can be studied. The prediction model used in the coordination layer uses a sampling time step of 10 seconds and a prediction horizon of 600 seconds. The factor $\gamma^{\mathrm{e}}$ is set to 0.3.
2) Simulation Set 1: Results: Several simulations were carried out with the different control strategies. The quantitative results are presented in the left two columns of Figure 6. First, the impact of changing the controller timings $T^{\text {ref }}$ and $T^{\text {local }}$ on the different controllers is discussed. After that, the performance of the different controllers is compared.

Figure 6 (a) and (e) show the impact of $T^{\text {ref }}$ on the TTS and on the mean reference tracking error. For every sampling time $T^{\text {ref }}$ there are multiple results, since the simulations were repeated for different values of $T^{\text {local }}$. Figure (a) shows the impact of the coordination layer sampling time on the TTS. It can be observed from this figure that for low sampling times the TTS fluctuates considerably. When $T^{\text {ref }}$ increases the fluctuations decrease, and for higher values of $T^{\text {ref }}$ the TTS starts increasing again, which is mainly caused by the time $T^{\text {ref }}$ being close to the prediction horizon of 600 seconds. Figure 6 (e) shows the impact of the sampling time $T^{\text {ref }}$ on the mean reference tracking error. This plot shows a slight increase in the reference tracking error when increasing the time $T^{\text {ref }}$, although this result does not seem to be significant.

Figure 6 (b) and (f) show the impact of $T^{\text {local }}$ on the TTS and on the mean reference tracking error. Figure 6 (b) shows that an increase in $T^{\text {local }}$ results in an increase in the TTS. Similarly, Figure 6 (f) shows that an increase in $T^{\text {local }}$ results in an increase in the reference tracking error. These results are best explained by the fact that a smaller sampling time $T^{\text {local }}$ results in the possibility of more rapid stage switching, which allows for better tracking of the reference outflow trajectories.

Figure 6 (a) and (b) also show the realized TTS of the LML-U and GCP strategies. Figure 6 (a) shows that the LML-U strategy can realize the lowest TTS. It also shows that it is not sensitive to changes in the time $T^{\text {ref }}$ until approximately 400 seconds. After that, the TTS increases due to the time $T^{\text {ref }}$ getting close to the prediction horizon. The lowest TTS realized with the LML-U strategy is 234.33 veh ⋅ h. Figure 6 (b) shows that the TTS increases when increasing the sampling time $T^{\text {local }}$. The best performance realized by the LML-U + GRT strategy is 234.56 veh ⋅ h for $T^{\text {local }}$ being 1 second. When setting $T^{\text {local }}$ to a more realistic value of 5 seconds, the lowest TTS is 235.45 veh ⋅ h. In the case of the GCP, the lowest TTS realized is 238.16 veh ⋅ h.

These evaluations show that a sampling time $T^{\text {ref }}$ in the range of 300 to 400 seconds is preferred for the performance. However, ideally $T^{\text {ref }}$ is chosen small, so that the control

![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-10.jpg?height=1203&width=1794&top_left_y=193&top_left_x=165)
Fig. 6. Simulation results for different set-ups. The two left columns represent the results obtained with the LTM, the two right columns represent results obtained with Vissim. The first row shows the impact of the controller sampling times $T^{\text {ref }}$ and $T^{\text {local }}$ on the TTS. The second row shows the impact of the sampling times on the mean reference tracking error. Plot (l) shows the impact of the sampling time $T^{\text {local }}$ on the mean local prediction error. This result is not shown for the LTM because the prediction error is negligible, since the process and prediction models are identical. The max, mean, and min lines indicate the maximum, mean, and minimum realized TTS of the non-shown parameter (e.g. $T^{\text {local }}$ in plot (a)).

strategy can quickly respond to disturbances. In order to reduce the sampling time $T^{\text {ref }}$, it is suggested to study the use of an observer in future research. The evaluations also show that the performance loss incurred by the switching of the stages is limited when the mismatch between the process and prediction model is small. Additionally, it is shown that a smaller local sampling time $T^{\text {local }}$ results in better performance due to the ability to track the reference outflows more accurately.

## C. Simulation Set 2: Microscopic Simulation Using Vissim

The second set of simulations is carried out with a microscopic simulation model. This allows us to study the performance when applied to a more complex process model. The quantitative performance is studied by comparing the control strategy to two other control strategies and studying the impact of changes in the controller parameters. Additionally, the qualitative performance is studied.

1) Simulation Set 2: Set-Up: In this simulation set, Vissim 5.30 is used as the traffic flow model, with a sampling time step of 0.2 seconds. Measurements are gathered and sent to Matlab R2016a every second. The rest of the set-up is similar to that discussed in Section III-B1.

The same network model as in Figure 5 is used. However, the parameters used in the prediction model are different than those discussed in Section III-B1. The link parameters are shown in Table I and are obtained by fitting the simulation data obtained with the LTM to an identification data set from a Vissim simulation. The origin capacities are estimated as $q_{1}^{\text {cap }}=2000 \mathrm{veh} / \mathrm{h}, q_{8}^{\text {cap }}=2000 \mathrm{veh} / \mathrm{h}, q_{12}^{\text {cap }}=2000 \mathrm{veh} / \mathrm{h}$.

In the various simulations, the local control strategy sampling time $T^{\text {local }}$ was varied from 5 to 12 seconds. The coordination layer sampling time $T^{\text {ref }}$ was given values of 30, 60, 90, 120, 180, 240, 300, 360, 420, 480, 540, and 590 seconds. In this way, the impact of the controller parameters on the controller performance can be studied. The prediction model used in the coordination layer uses a sampling time step of 10 seconds and a prediction horizon of 600 seconds. The factor $\gamma^{\mathrm{e}}$ was set to 0.3 . The clearance time between two conflicting links was set to 2 seconds, and the parameters $\theta_{i}$ con were set to $4.4 \cdot 10^{-2}$.
2) Simulation Set 2: Quantitative Results: The quantitative results are presented in the right two columns of Figure 6. First, the impact of the controller sampling times $T^{\text {ref }}$ and $T^{\text {local }}$ is discussed. After that the performance is compared to the GCP.

TABLE I
Link Parameters Used in the Prediction Model
| Link | $t^{\text {free }}(\mathrm{s})$ | $t^{\text {shock }}(\mathrm{s})$ | $n^{\text {max }}$ (veh) | $q^{\text {sat }}(\mathrm{veh} / \mathrm{h})$ | Link | $t^{\text {free }}(\mathrm{s})$ | $t^{\text {shock }}(\mathrm{s})$ | $n^{\text {max }}$ (veh) | $q^{\text {sat }}($ veh $/ \mathrm{h})$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 21.0 | 60.0 | 45 | 1961.9 | 11 | 21.0 | 58.0 | 46 | 2048.3 |
| 2 | 14.0 | 60.0 | 30 | 1916.1 | 12 | 21.0 | 56.4 | 44 | 1994.4 |
| 3 | 14.0 | 46.6 | 30 | 2000.0 | 13 | 14.0 | 61.0 | 31 | 1979.2 |
| 4 | 21.0 | 68.0 | 45 | 2369.8 | 14 | 14.0 | 70.0 | 30 | 1998.3 |
| 5 | 14.0 | 70.0 | 30 | 2369.8 | 15 | 21.0 | 58.0 | 46 | 1935.3 |
| 6 | 14.0 | 39.0 | 30 | 1848.5 | 16 | 57.0 | 205.0 | 119 | 1914.9 |
| 7 | 21.0 | 92.0 | 46 | 2023.0 | 17 | 14.0 | 60.0 | 30 | 2262.5 |
| 8 | 21.0 | 63.2 | 45 | 2150.9 | 18 | 14.0 | 48.3 | 31 | 2195.1 |
| 9 | 14.0 | 60.0 | 30 | 2000.0 | 19 | 21.0 | 53.4 | 47 | 1937.3 |
| 10 | 14.0 | 55.0 | 30 | 2000.0 |  |  |  |  |  |


Figure 6 (c) shows the impact of $T^{\text {ref }}$ on the TTS. It can be observed that the TTS is lowest for sampling times $T^{\text {ref }}$ in the range of 200 to 300 seconds. This is in accordance with the results obtained with the LTM. The reason is that the reference outflows are determined for average dynamics. When using small values of $T^{\text {ref }}$, the frequent updates of the MPC signal do not allow a good representation of the average dynamics. For high sampling times $T^{\text {ref }}$, the impact of the mismatch between the process and prediction model becomes larger, as is also shown in Figure 6 (g).

Figure 6 (d) shows the impact of $T^{\text {local }}$ on the TTS. It can be observed that there is no clear connection between the sampling time $T^{\text {local }}$ and the TTS. When studying Figure 6 (h), it is also clear that there is no strong connection between the sampling time $T^{\text {local }}$ and the reference tracking error. This is best explained by the mismatch between the LTM and Vissim when predicting the intersection outflows with a time horizon in the range of 10 seconds. Figure 6 (1) shows the impact of $T^{\text {local }}$ on the prediction error of the bottom layer.

When examining the realized TTS in Figure 6 (d), it can be seen that the LML-U + GRT strategy can realize a TTS of 270.17 veh ⋅ h while the GCP can realize a TTS of 279.35 veh ⋅ h. The reason for this, as discussed in the next subsection, is that the approach proposed in this paper distributes the queues over the network better. Also, when studying Figure 6 (1) it can be observed that the mean local prediction error of the GCP is consistently higher. The reason for this is that the predictions in the intersection layer are especially off when queues spill back to upstream intersections. This affects the GCP more, because that strategy causes much more spillback.
3) Simulation Set 2: Qualitative Results: Figure 7 shows the number of vehicles over time in several links for the two different control strategies - i.e., the LML-U + GRT in the left column, and the GCP in the right column. Figure 8 shows the outflows of the network exits over time. The simulation results with $T^{\text {local }}=9$ seconds and $T^{\text {ref }}=300$ are used for the comparison. The vertical lines are used to indicate the time instants 300, 460, 650, and 1800 seconds respectively. Below, the behavior is discussed using these figures.

- Figure 7 (a) and (b) show that from time 80 to 300 the flow into the bottleneck exceeds the bottleneck capacity and a queue starts building up in link 7. This occurs when using either of the two policies.
- Figure 7 (c) and (d) show that at time 300 (indicated with the first vertical line) the spillback reaches links 5 and 17

- Around time 460 (indicated with the second vertical line) spillback cannot be avoided any more. The LML-U + GRT controller reduces the outflow of link 5 so that queues built up in links 5, 4, 2, and 9. In contrast to that, the GCP controller gives green to both links 5 and 17. This causes spillback towards links 4 and 16, which causes blocking of links 6 and 18.
- Next, around time 650 (indicated with the third vertical line) the LML-U + GRT blocks the outflow from link 17 in order to prevent spillback to links 8 and 1. As shown in Figure 7 (c), the number of vehicles in link 5 decreases while the number of vehicles in link 17 increases. It is interesting to see that links 2 and 9 do not seem that full around time 650. This is due to the shock wave dynamics that cause a delay in the time when an outflow increase at link 5 leads to increased outflows at upstream links 2 and 9. Hence, only around time 800 seconds do the queues in links 2 and 9 become more or less stationary. The GCP controller does not have such a global view of the network, so the queue on link 2 grows, resulting in spillback to link 1 and an outflow reduction at link 11, as can be observed in Figure 8 (c).
- At time 1800 (indicated with the righter most vertical line) the demands decrease. Due to this, the outflow of link 5 can be reduced without triggering spillback to links 1 and 8 so that the queues on link 12, 14, 16, and 17 can be reduced.

## IV. Discussion

Several assumptions were made to simplify the problem addressed in this paper. This allowed us to combine optimization of the traffic flows at the network level with local signal controllers. This section discusses the implication of these assumptions and suggestions for relaxing them. It also discusses the scalability of the framework.

It was assumed that no minimum and maximum green times, no maximum or fixed cycle time, no off-set, and no fixed stage sequences had to be considered. Including these properties may affect the control performance, since, it reduces the control freedom. In order to correctly take these properties into account, the network coordination layer may need to be adjusted to reflect the impact of the different signal controller properties on the link outflows. Also, the logic of the local intersection control layer may need to be adopted to ensure that

![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-12.jpg?height=1186&width=788&top_left_y=206&top_left_x=198)
Fig. 7. Number of vehicles in the links 7, 5, 17, 9, and 2 over time for the LML-U + GRT strategy in the left column and the GCP strategy in the right column. The vertical lines indicate the time instants 300, 460, 650, and 1800 seconds.

maximum green times, cycle times, and fixed stage sequences are realized. Depending on the problem type, this may be achieved by using heuristic approaches or optimizationbased strategies. Hence, relaxing these assumptions may require some theoretical extensions and additional numerical evaluations which is beyond the scope of the present paper.

Apart from that, an idealized set-up was assumed with no noise or uncertainties, and in which only normal vehicular traffic is present. The impact of uncertainties on the controller performance requires further investigation and, when needed, robust control strategies should be developed (e.g., see [22], [23]). Different traffic types may be included by using a multi-modal LTM, and including public transport priority as constraints within the optimization problem.

The approach was designed for sub-networks consisting of (several) tens of intersections at maximum, and was tested on a small network consisting of three intersections. When applying the framework to larger networks, the computation time required by the network coordination layer increases. The size of the optimization vector is given as $\left(n^{\mathrm{L}}+n^{\mathrm{O}}\right) N^{\mathrm{p}}(-)$ and number of constraints is given as

![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-12.jpg?height=799&width=816&top_left_y=198&top_left_x=1109)
Fig. 8. Outflow of links 7, 11, 15, and 19 over time for the LML-U + GRT strategy and the GCP strategy. The vertical lines indicate the time instants 300, 460, 650, and 1800 seconds.

$\left(4 n^{\mathrm{L}}+3 n^{\mathrm{O}}+n^{\mathrm{E}}+n^{\text {con }}\right) N^{\mathrm{p}}(-)$, with $n^{\mathrm{E}}(-)$ the number of exits, and $n^{\text {con }}(-)$ the number of conflicts between links.

## V. Conclusions and Recommendations

This paper proposes a hierarchical control framework for coordinated intersection control. The top layer - the network coordination layer - uses an efficient, linear MPC strategy for the optimization of network throughput. The output of the network coordination layer consists of reference outflow trajectories for the controlled links at intersections. The bottom layer consists of the individual intersection controllers that actuate the stage that minimizes the current reference tracking error. Simulations were carried out to test the impact of the controller timings and to compare the performance for the different timings. Simulations using the LTM as the process model indicated that the best performance can be obtained when using a moderate (around 200 to 300 seconds) sampling time for the network coordination layer. It was also shown that a smaller sampling time of the bottom layer leads to improved performance. It was found that the policy proposed in this paper can realize a TTS that is only 0.5\% worse than the best possible performance when directly applying the signal of the network coordination layer. It was also shown that the controller can outperform a greedy control policy that tries to maximize the individual intersection throughput. Simulations using microscopic simulation revealed that the control strategy is capable of efficiently distributing the traffic over the network in spillback conditions, even when a large mismatch between the prediction and process model is present.

Further research can investigate the application of the framework to an intersection signal program where fixed stage sequences and minimum green times are included. Additionally, the application to a network that consists of heterogeneous
vehicle types - e.g. vehicles, public transport, and bicycles - may be studied. Finally, further research can be carried out into the design of an observer so that the sampling time of the network coordination layer can be reduced.

## References

[1] G. van de Weg, M. Keyvan-Ekbatani, A. Hegyi, and S. Hoogendoorn, "Urban network throughput optimization via model predictive control using the link transmission model," in Proc. 95th Annu. Meeting Transp. Res. Board, Washington, DC, USA, 2016.
[2] J. D. C. Little, "The synchronization of traffic signals by mixed-integer linear programming," Oper. Res., vol. 14, no. 4, pp. 568-594, 1966.
[3] P. Hunt, D. Robertson, R. Bretherton, and M. Royle, "The SCOOT online traffic signal optimisation technique," Traffic Eng. Control, vol. 23, no. 4, pp. 190-199, 1982.
[4] J. Luk, A. Sims, and P. Lowrie, "SCATS-Application and field comparison with a transyt optimised fixed time system," in Proc. Int. Conf. Road Traffic Signalling, London, U.K., 1982, pp. 71-74. [Online]. Available: https://trid.trb.org/view/1188852
[5] M. Papageorgiou, C. Diakaki, V. Dinopoulou, A. Kotsialos, and Y. Wang, "Review of road traffic control strategies," Proc. IEEE, vol. 91, no. 12, pp. 2043-2067, Dec. 2003.
[6] S. Lämmer and D. Helbing, "Self-control of traffic lights and vehicle flows in urban road networks," J. Stat. Mech., Theory Experim., vol. 2008, no. 4, p. P04019, 2008.
[7] C. Diakaki et al., "Extensions and new applications of the trafficresponsive urban control strategy: Coordinated signal control for urban networks," Transp. Res. Rec., J. Transp. Res. Board, vol. 1856, pp. 202-211, Jan. 2003.
[8] W. Kraus, Jr., et al., "Cost effective real-time traffic signal control using the TUC strategy," IEEE Intell. Transp. Syst. Mag., vol. 2, no. 4, pp. 6-17, Winter 2010. [Online]. Available: https://ieeexplore. ieee.org/document/5681212/
[9] P. Varaiya, "Max pressure control of a network of signalized intersections," Transp. Res. C, Emerg. Technol., vol. 36, pp. 177-195, Nov. 2013.
[10] T. Le, P. Kovács, N. Walton, H. Vu, L. H. Andrew, and S. P. Hoogendoorn, "Decentralized signal control for urban road networks," Transp. Res. C, Emerg. Technol., vol. 58, pp. 431-450, Sep. 2015.
[11] C. F. Daganzo, "Urban gridlock: Macroscopic modeling and mitigation approaches," Transp. Res. B, Methodol., vol. 41, no. 1, pp. 49-62, 2007.
[12] M. Keyvan-Ekbatani, A. Kouvelas, I. Papamichail, and M. Papageorgiou, "Exploiting the fundamental diagram of urban networks for feedbackbased gating," Transp. Res. B, Methodol., vol. 46, no. 10, pp. 1393-1403, Dec. 2012.
[13] C. E. Garcia, D. M. Prett, and M. Morari, "Model predictive control: Theory and practice-A survey," Automatica, vol. 25, no. 3, pp. 335-348, 1989.
[14] D. Mayne, J. Rawlings, C. Rao, and P. Scokaert, "Constrained model predictive control: Stability and optimality," Automatica, vol. 36, no. 6, pp. 789-814, 2000.
[15] H. K. Lo, "A novel traffic signal control formulation," Transp. Res. A, Policy Pract., vol. 33, no. 6, pp. 433-448, 1999.
[16] M. van den Berg, A. Hegyi, B. D. Schutter, and J. Hellendoorn, "Integrated traffic control for mixed urban and freeway networks: A model predictive control approach," Eur. J. Transp. Infrastruct. Res., vol. 7, no. 3, pp. 223-250, Sep. 2007.
[17] H. Kashani and G. Saridis, "Intelligent control for urban traffic systems," Automatica, vol. 19, no. 2, pp. 191-197, 1983.
[18] S. Lin, B. De Schutter, Y. Xi, and H. Hellendoorn, "Fast model predictive control for urban road networks via MILP," IEEE Trans. Intell. Transp. Syst., vol. 12, no. 3, pp. 846-856, Sep. 2011.
[19] K. Aboudolas, M. Papageorgiou, A. Kouvelas, and E. Kosmatopoulos, "A rolling-horizon quadratic-programming approach to the signal control problem in large-scale congested urban road networks," Transp. Res. C, Emerg. Technol., vol. 18, no. 5, pp. 680-694, Oct. 2010.
[20] T. Le, H. Vu, Y. Nazarathy, Q. Vo, and S. Hoogendoorn, "Linearquadratic model predictive control for urban traffic networks," Transp. Res. C, Emerg. Technol., vol. 36, pp. 498-512, Nov. 2013.
[21] I. Yperman, "The link transmission model for dynamic network loading," Ph.D. dissertation, KU Leuven, Leuven, Belgium, 2007.
[22] T. Tettamanti, T. Luspay, B. Kulcsár, T. Péni, and I. Varga, "Robust control for urban road traffic networks," IEEE Trans. Intell. Transp. Syst., vol. 15, no. 1, pp. 385-398, Feb. 2014.
[23] S. V. Ukkusuri, G. Ramadurai, and G. Patil, "A robust transportation signal control problem accounting for traffic dynamics," Comput. Oper. Res., vol. 37, no. 5, pp. 869-879, May 2010.
![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-13.jpg?height=320&width=256&top_left_y=423&top_left_x=1081)

Goof Sterk van de Weg received the M.Sc. degree in systems and control and the Ph.D. degree from the Delft University of Technology, The Netherlands, in 2013 and 2016, respectively. His main research interests are the design of control algorithms for cooperative systems, traffic lights, variable speed limits, ramp metering, and route guidance to improve the performance of road traffic networks.
![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-13.jpg?height=318&width=254&top_left_y=851&top_left_x=1081)

Hai L. Vu (S'97-M'98-SM'06) received the B.Sc./M.Sc. and Ph.D. degrees in electrical engineering from the Technical University of Budapest, Hungary, in 1994 and 1999, respectively. He was with The University of Melbourne for 5 years and with the Swinburne University of Technology for 11 years. In 2016, he joined the Engineering Faculty, Monash University, Melbourne, Australia, where he is currently a Professor of intelligent transport systems. He has authored or co-authored over 150 scientific journals and conference papers. His research interests include modeling, performance analysis and design of complex networks, and stochastic optimization and control with applications to connected autonomous vehicles and intelligent transport. In 2012, he was a recipient of the prestigious research award, the Australian Research Council Future Fellowship in the Intelligent Transport Systems Research.
![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-13.jpg?height=320&width=254&top_left_y=1465&top_left_x=1083)

Andreas Hegyi (M'12) received the M.Sc. degree in electrical engineering and the Ph.D. degree from the Delft University of Technology (TU Delft), The Netherlands, in 1998 and 2004, respectively. From 2004 to 2007, he was a Post-Doctoral Researcher with TU Delft and also with Ghent University. He is currently an Assistant Professor with TU Delft. He has authored or co-authored over 100 papers. His research interests are in the areas of traffic flow modeling and control, connected and cooperative vehicles, traffic state estimation, and traffic data analysis. He is a member of the IEEE-ITSS and IFAC-CTS. He is a member of the Editorial Board of the Transportation Research Part C. He has served as an IPC Member for various other conferences, the Program Chair for the IEEE-ITSC 2013 Conference, and the General Chair for the IXth TRISTAN Symposium 2016. He is an Associate Editor of the IEEE Transactions on Intelligent Transportation Systems.
![](https://cdn.mathpix.com/cropped/fa3d9f8c-5cab-4299-b689-8d3848d61a9f-13.jpg?height=320&width=254&top_left_y=2114&top_left_x=1083)

Serge Paul Hoogendoorn received the M.Sc. degree in applied mathematics from Delft University of Technology in 1995 and the Ph.D. degree in civil engineering from Delft University of Technology in 1999. He is currently a Full Professor with the Delft University of Technology, where he holds a chair position in traffic operations and management and is a Distinguished Professor of smart urban mobility. He has authored or co-authored over 280 papers. His research interests cover a variety of topics, including traffic flow theory, traffic management, ITS, and active mode mobility. He is an IAC Member of the ISTTT. He is a member of the TRB Traffic Flow Theory Committee. He was a recipient of the ERC Advanced Grant in 2014. He is the Chair of the TRB Crowd Modeling and Management Subcommittee. He is an Editor of the Journal of Advanced Transportation, EJTL, and EJTIR.

