# Max pressure control of a network of signalized intersections 

Pravin Varaiya*<br>Department of Electrical Engineering and Computer Sciences, University of California, Berkeley, CA 94720-1770, United States

ARTICLE INFO

Article history:
Received 18 June 2013
Received in revised form 27 August 2013
Accepted 28 August 2013

Keywords:
Max pressure
Local control
Traffic responsive
Adaptive signal control
Bounded queues
Store-and-forward model
Queueing network
Network stability


#### Abstract

The control of a network of signalized intersections is considered. Vehicles arrive in iid (independent, identically distributed) streams at entry links, independently make turns at intersections with fixed probabilities or turn ratios, and leave the network upon reaching an exit link. There is a separate queue for each turn movement at each intersection. These are point queues with no limit on storage capacity. At each time the control selects a 'stage', which actuates a set of simultaneous vehicle movements at given iid saturation flow rates. Network evolution is modeled as a controlled store-and-forward (SF) queuing network. The control can be a function of the state, which is the vector of all the queue lengths. A set of demands is said to be feasible if there is a control that stabilizes the queues, that is the timeaverage of every mean queue length is bounded. The set of feasible demands $D$ is a convex set defined by a collection of linear inequalities involving only the mean values of the demands, turn ratios and saturation rates. If the demands are in the interior $D^{o}$ of $D$, there is a fixed-time control that stabilizes the queues. The max pressure (MP) control is introduced. At each intersection, MP selects a stage that depends only on the queues adjacent to the intersection. The MP control does not require knowledge of the mean demands. MP stabilizes the network if the demand is in $D^{o}$. Thus MP maximizes network throughput. MP does require knowledge of mean turn ratios and saturation rates, but an adaptive version of MP will have the same performance, if turn movements and saturation rates can be measured. The advantage of MP over other SF network control formulations is that it (1) only requires local information at each intersection and (2) provably maximizes throughput. Examples show that other local controllers, including priority service and fully actuated control, may not be stabilizing. Several modifications of MP are offered including one that guarantees minimum green for each approach and another that considers weighted queues; also discussed is the effect of finite storage capacity.


© 2013 Elsevier Ltd. All rights reserved.

## 1. Introduction

The evolution of traffic in a signalized road network is modeled in this paper as a network of queues. The state of this network is the vector of all queue lengths at all intersections. The signal control at any time permits certain simultaneous turn movements at each intersection at pre-specified saturation rates. Miller (1963) studies the queue for one approach at a single intersection modeled by the equation

$$
x(t+1)=x(t)-c(t) \wedge x(t)+d(t) .
$$

[^0]Here $x(t)$ is the queue length at the beginning of period $t, c(t)$ is the number of vehicles that can potentially depart in period $t$ when the signal is actuated, and $d(t)$ is the demand in period $t . c(t)$ and $d(t)$ are iid (independent, identically distributed) random variables with mean $c$ and $d$ vehicles per period, respectively. $y \wedge z=\min \{y, z\}$. The system (1) is said to be stable if the mean queue length is bounded. This system is stable if $d<c$, that is, the mean demand is smaller than the service rate. Under this condition, Miller (1963) estimates the mean and variance of the queue length in equilibrium.

The single-queue model (1) extends to a network of signalized intersections. In such a model for every approach $k$ at an intersection the queue length $x_{k}(t)$ evolves according to

$$
x_{k}(t+1)=x_{k}(t)-C_{k}(t+1) S_{k}(t) \wedge x_{k}(t)+\sum_{l} a_{k, l}(t)+d_{k}(t+1)
$$

Here $S_{k}(t)=1$ or 0, accordingly as the intersection signal control permits or forbids movement of vehicles from queue $x_{k}(t)$, $C_{k}(t+1)$ is the random number of vehicles that could depart in period $t$ if $S_{k}(t)=1, \sum_{l} a_{k, l}(t)$ is the sum over all arrivals from other intersections in the network, and $d_{k}(t+1)$ is the sum of all arrivals from outside the network.

The network model (2) has not been analyzed in the literature, even for a fixed-time control. (A noteworthy exception is the approximate equilibrium analysis of the network model in Osorio and Bierlaire (2009).) In particular, it seems not to be known whether, with stochastic arrivals and service, a particular fixed-time control will stabilize the network, i.e., all queues have bounded mean. That question is settled by Theorem 3 which states that a fixed-time control stabilizes the network if and only if for each queue the mean total arrival rate is smaller that the mean service rate.

Instead of an analysis of the statistical properties of (2) published work has focused on the design of feedback or trafficresponsive controls in which the intersection signals are selected as a function of the current state, the vector of all queue lengths in the network. This large literature is not summarized here in detail, since there are good reviews in Mirchandani and Head (2001), Papageorgiou et al. (2003), Osorio and Bierlaire (2008), and Xie et al. (2012). Here we discuss some major differences between this literature and the contributions of the present paper. A more critical comparison between this literature and max pressure or MP control is available in Varaiya (2013).

The calculation of signal control in systems such as OPAC (Gartner et al., 2001), RHODES (Mirchandani and Head, 2001), and in the widely deployed SCOOT Robertson and Bretherton (1991) is distributed i.e., the control of each intersection is set independently, with the objective of minimizing some measure of upstream queues over some horizon. OPAC uses upstream flow measurements to predict the flow over a rolling horizon (usually one cycle). RHODES uses a 'dynamic network model' to estimate link flows which are used to adjust the control at each intersection based on prediction of vehicle arrivals. The network model includes demands, turn probabilities and saturation flow rates as parameters. SCOOT measures upstream flows at each intersection to update a queue model. None of these models considers the impact of signal control on downstream queues. The counter-examples in Section 5 suggest that such controls may therefore be destabilizing. (It is not possible to provide precise counter-examples to these control schemes since they are not mathematically described in the published literature.)

On the other hand, TUC (Diakaki et al., 2003; Aboudolas et al., 2009b) prescribes a centralized control, which may require significant communication infrastructure. By contrast, the calculations in MP are local: the evaluation of MP at each intersection at any time requires knowledge only of the queues at adjacent links at that time. According to Lindley (2012), traffic-responsive and adaptive control achieve large benefits but fewer than 10\% of intersections in the US use adaptive signals, because of the deployment cost of detection and communication and uncertainty about benefits.

Second, these signal control systems attempt to minimize the cost over an infinite or finite rolling horizon. Calculation of this future cost requires prediction of future demands and turn ratios, and if the prediction is biased, the control strategy will not be optimal, see Varaiya (2013). By contrast, MP requires no knowledge of the demand, although it does require knowledge of turn ratios. However, the adaptive version of MP, AMP, can estimate these turn ratios.

The third difference is theoretical. None of these systems comes with a guarantee that the resulting closed loop system will be stable. Theorem 2 shows that MP is a stabilizing control if there exists any stabilizing control. Thus MP maximizes throughput.

The paper is organized as follows. Section 2 formulates a static flow problem, with mean (average) demands, turn ratios and saturation rates. In this formulation, the set $D$ of feasible demands is characterized by a set of linear inequalities and each $d \in D^{o}$ can be supported by a fixed-time controller. Section 3 describes the basic MP control, and shows that it maximizes throughput. Section 4 considers several variations of the basic MP including adaptive MP, and the use of weighted queues. Section 5 is devoted to three examples: a fully actuated control of a two-intersection network, a utilization-maximizing and a priority-based control for a single intersection, all of which are de-stabilizing even though in each case there exists a stabilizing fixed-time control. Section 6 summarizes the conclusions, briefly discusses the limitations of the present formulation and directions for further work. Most of the technical proofs are collected in Appendix A.

A note on max pressure: The max pressure algorithm was first presented in Tassiulas and Ephremides (1992), which considers the routing and scheduling of packet transmission in a wireless network. In that context, packets may not be simultaneously transmitted over two interfering links. (In the traffic context of this paper, vehicles may not make simultaneous movements if these can cause collisions.) In packet networks, the term backpressure policy has been adopted. The name max pressure may have been coined by Dai and Lin (2005), and it seems to be the preferred term in scheduling and routing in flexible manufacturing networks. There is a large literature on max pressure or backpressure algorithms.

The max pressure traffic signal control was presented in June 2010 at the NSF Workshop on Dynamic Route Guidance and Traffic Control (Varaiya, 2013). That version uses a network calculus model of uncertainty in demand, turn ratio, and saturation flow rate, rather than a stochastic model as in the present paper, which was presented at the LATSIS Symposium, EPFL, September 2012. The max pressure control for traffic signals was independently proposed in Wongpiromsarn et al. (2012); however the network model and the notion of stability in that work are significantly different from those formulated here.

## 2. Deterministic flows and fixed-time control

The control problem is formulated at two levels. The first level deals with deterministic vehicle flows subject to routing and conservation constraints described in Section 2.1, and constraints on simultaneous turn movements and saturation flows at intersections described in Section 2.2. This deterministic formulation leads to a simple linear programming characterization of feasible demands, the fixed-time control with minimum cycle length that accommodate feasible demands, and the network reserve capacity. This characterization is known. The second level formulation considers the movement of individual vehicles and traffic-responsive or feedback signal control. It is discussed in Section 3.

### 2.1. Routing and flow conservation

Fig. 1 illustrates the concepts and variables in the flow model. The network is a collection of directed links, $l \in \mathcal{L}_{\text {all }}$, and nodes or intersections, $n \in \mathcal{N}$. There are three types of links: an internal link ( $l \in \mathcal{L}$ ) goes from its start node to its end node; an entry link ( $l \in \mathcal{L}_{\text {entry }}$ ) has no start node; and an exit link ( $l \in \mathcal{L}_{\text {exit }}$ ) has no end node. Link $l$ is input to link $m$ if $l$ has an end node $n$ and $m$ has start node $n$. We also say that link $m$ is output from link $l$.

The following notation is used:

$$
\begin{aligned}
& \mathcal{L}_{\text {all }}=\text { set of all links, elements } l, m, k \\
& \mathcal{L}\left[\mathcal{L}_{\text {entry, }} \mathcal{L}_{\text {exit }}\right]=\text { set of internal [entry, exit] links } \\
& \text { In } n_{l} \subset \mathcal{L} \cup \mathcal{L}_{\text {entry }} \text {, set of links input to } l \in \mathcal{L} \cup \mathcal{L}_{\text {exit }} \\
& \text { Out } t_{l} \subset \mathcal{L} \cup \mathcal{L}_{\text {exit }} \text {, set of links output from } l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }} \\
& f_{l}=\text { flow of vehicles in link } l \text {, vehicles per period } \\
& d_{l}=\text { exogenous flow of vehicles in link } l \in \mathcal{L}_{\text {entry }} \text {, vehicles per period } \\
& r(l, m)=\text { proportion of vehicles leaving } l \text { and entering } m \\
& c(l, m)=\text { saturation flow of phase }(l, m) \text {, vehicles per period } \\
& \mathcal{N}=\text { set of nodes or intersections, elements } n \\
& I(n) \subset \mathcal{L} \cup \mathcal{L}_{\text {entry, set of links entering } n} \\
& O(n) \subset \mathcal{L} \cup \mathcal{L}_{\text {exit }} \text {, set of links leaving } n
\end{aligned}
$$

By definition $m \in$ Out $_{l}$ implies $l \in I n_{m}$. The pre-specified routing proportions $\{r(l, m)\}$ satisfy

$$
\begin{aligned}
& r(l, m)=0, l \in \mathcal{L}_{\text {exit }}, m \in \mathcal{L}_{\text {all }} \\
& r(l, m)=0, l \in \mathcal{L}_{\text {all }}, m \in \mathcal{L}_{\text {entry }} \\
& r(l, m)=0, l \in \mathcal{L}_{\text {all }}, m \notin \text { Out }_{l} \\
& \sum_{m} r(l, m)=1, l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }} .
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-03.jpg?height=367&width=901&top_left_y=1973&top_left_x=486)
Fig. 1. Network links are denoted by arrows, and nodes or intersections by dark circles.

Routing and flow conservation together impose these constraints:

$$
\begin{aligned}
& f_{l}=d_{l}, l \in \mathcal{L}_{\text {entry }} \\
& f_{m}=\sum_{l} f_{l} r(l, m), m \in \mathcal{L} \cup \mathcal{L}_{\text {exit }}
\end{aligned}
$$

Flows on entry links are specified by exogenous demands (7); flows on other links are determined by the routing proportions and flow conservation at nodes (8).

An exit path from link $l$ is a sequence of links $l=l_{1}, \ldots, l_{n}$ with $r\left(l_{i}, l_{i+1}\right)>0$ and $l_{n} \in \mathcal{L}_{\text {exit }}$. It is assumed that every link $l$ belongs to an exit path, so every vehicle will eventually exit.

Let $f=\left\{f_{l}, l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}\right\}$ denote the row vector of flows in the internal and entry links and let $d=\left\{d_{l}, l \in \mathcal{L}_{\text {entry }}\right\}$ denote the row vector of demands on entry links. The next result uses elementary linear algebra.

Proposition 1. For every demand vector $d=\left\{d_{l}, l \in \mathcal{L}_{\text {entry }}\right\}$ there is a unique flow $f=\left\{f_{l}, l \in \mathcal{L}_{\text {all }}\right\}$ satisfying (7) and (8). Hence there is a matrix $P$, which depends only on the routing proportions, such that $f=d P$.

### 2.2. Phases and control matrices

In addition to the routing and conservation constraints (7) and (8) there are two intersection constraints: only certain simultaneous turn movements are permitted, and permitted movements are subject to a capacity or saturation flow limit. These constraints are formulated next.

Time is discrete, $t=1,2, \ldots$. The fixed duration of each period is $\tau$ sec. A phase or movement $(l, m)$ is a pair of links with $m \in \operatorname{Out}_{l}$ (or $l \in \operatorname{In}_{m}$ ), $l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}$. (There is no phase ( $l, m$ ) if $l \in \mathcal{L}_{\text {exit }}$ or $m \in \mathcal{L}_{\text {entry }}$, see Fig. 1). The set of phases at intersection $n$ is $\{(l, m) \in I(n) \times O(n)\}$. Certain subsets of phases at intersection $n$ may be simultaneously actuated. Each such subset is represented by an intersection control matrix matrix $S_{n}=\left\{S_{n}(l, m), l \in I(n), m \in O(n)\right\}$ with entries $S_{n}(t)(l, m)=1$ or 0 accordingly as the phase $(l, m)$ is or is not actuated. The set of all such matrices at $n$ is denoted $\mathcal{S}_{n}$.

A collection of intersection control matrices $\left\{S_{n}\right\}$, one for each intersection, can be combined into the single network control matrix $S$ of dimension $\left|\mathcal{L} \cup \mathcal{L}_{\text {entry }}\right| \times\left|\mathcal{L} \cup \mathcal{L}_{\text {exit }}\right|$, with $S(l, m)=1$ if for some intersection $n, l \in I(n), m \in O(n)$ and $S_{n}(l, m)=1$; otherwise $S(l, m)=0$. (Notation: $|A|$ is the number of elements in set $A$.) $S$ can be put in block-diagonal form with the intersection matrices $S_{n}$ along the diagonal and all other entries zero, like in Fig. 2. The set of all network control matrices is denoted by $\mathcal{S} . \mathcal{S}$ is a finite set of 0,1 matrices.

If phase ( $l, m$ ) is actuated in period $t$ up to $c(l, m)$ vehicles can move from $l$ to $m$ in period $t . c(l, m)$ is the (known) saturation flow for phase $(l, m)$. An unactuated phase serves zero movements. $c(l, m)$ is a deterministic service rate for now, but in Section 3 it is the mean rate of a stochastic service. If movement $(l, m)$ is never permitted, $c(l, m)=0$.

Terminology In this paper a phase ( $l, m$ ) corresponds to a single turn movement or stream in European usage. In the US 'phase' is sometimes used to denote simultaneous compatible turn movements. An 'intersection control matrix' $S_{n} \in S_{n}$ in this paper corresponds to a 'stage' in European usage.

Example 1 (Standard intersection). Fig. 3 depicts the standard intersection with phases denoted by $\phi_{i}$ instead of by the pair $(l, m)$ of input-output links. It has eight stages, each corresponding to a pair of phases:

$$
\left(\phi_{1}, \phi_{5}\right),\left(\phi_{1}, \phi_{6}\right),\left(\phi_{2}, \phi_{5}\right),\left(\phi_{2}, \phi_{6}\right),\left(\phi_{3}, \phi_{7}\right),\left(\phi_{3}, \phi_{8}\right),\left(\phi_{4}, \phi_{7}\right),\left(\phi_{4}, \phi_{8}\right) .
$$

The control matrix for $\left(\phi_{1}, \phi_{5}\right)$ is shown on the right.
An infinite network control sequence $S=\{S(1), S(2), \ldots, S(t), \ldots\}$ is admissible if $S(t) \in S$ for each $t$. For admissible $S$, define the matrix $\Sigma_{S}$ with entries

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-04.jpg?height=427&width=564&top_left_y=1914&top_left_x=669)
Fig. 2. A network control matrix $S$ is a block-diagonal matrix with intersection control matrices $S_{n}, S_{m}$ along the diagonal.

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-05.jpg?height=476&width=1013&top_left_y=183&top_left_x=427)
Fig. 3. The eight phases of a standard intersection and the control matrix $S$ corresponding to $\left(\phi_{1}, \phi_{5}\right)$.

$$
\Sigma_{S}(l, m)=\liminf _{T} \frac{1}{T} \sum_{t=1}^{T} S(t)(l, m), \quad l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, \quad m \in \mathcal{L} \cup \mathcal{L}_{\text {exit }} .
$$

Let $f=\left\{f_{l}, l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}\right\}$ be the flow vector corresponding to the demand vector $d ; f=d P$ according to Proposition 1.
Definition 1. The admissible network control sequence $S=\{S(t)\}$ accommodates $f$ (or equivalently $d$ is a feasible demand) if

$$
c(l, m) \Sigma_{S}(l, m)>f_{l} r(l, m) \text { for every phase }(l, m) .
$$

The justification for the definition is this. By (9) the phase actuations of the control sequence $S$ can serve $c(l, m) \Sigma_{S}(l, m)$ turn movements per period on average. On the other hand, the flow vector $f$ generates $(l, m)$ turn movements at a rate of $f_{l} r(l, m)$ per period. By (9) and (10), there exist $T<\infty$ and $\epsilon>0$ such that

$$
\sum_{t=1}^{T} c(l, m) S(t)(l, m)-f_{l} r(l, m) T>\epsilon T, \quad T>\bar{T}
$$

Hence the number of vehicles in link $l$ waiting to turn into link $m$ will forever be bounded. (Theorem 3 below states that under (10), with stochastic arrivals with mean rate $d$ and stochastic service with mean rates $c(l, m)$ all queue lengths in the network will have finite means.)

Denote by

$$
\operatorname{co}(\mathcal{S})=\left\{\sum_{S \in \mathcal{S}} \lambda_{S} S \mid \lambda_{S} \geqslant 0, \sum \lambda_{S}=1\right\}
$$

the convex hull of the set $\mathcal{S}$ of all network control matrices. Since $\mathcal{S}$ is finite, $\operatorname{co}(\mathcal{S})$ is a closed, bounded polytope. The next result is straightforward.

Proposition 2. $\Sigma \in \operatorname{co}(\mathcal{S})$ if and only if there is an admissible control sequence $\{S(t)\}$ such that for all ( $l, m$ )

$$
\lim \frac{1}{T} \sum_{t=1}^{T} S(t)(l, m)=\Sigma(l, m) .
$$

It will be convenient to assume that if $S_{n} \in S_{n}$ and $S_{n}^{\prime}$ is obtained from $S_{n}$ by setting more of its entries to zero, then $S_{n}^{\prime} \in S_{n}$ as well, i.e., it is always permissible not to actuate a phase. Consequently $\Sigma^{\prime} \in \mathcal{S}$ if $\Sigma \in \mathcal{S}$ and $0 \leqslant \Sigma^{\prime} \leqslant \Sigma$.

Let $D$ be the set of demand vectors $d$ such that for $f=d P$ there exists

$$
\Sigma \in \operatorname{co}(\mathcal{S}) \text { with } f_{l} r(l, m) \leqslant c(l, m) \Sigma(l, m) \text { for all }(l, m) .
$$

Let $D^{o}$ denote the interior of $D$. From (12) it follows that $D^{o}$ is the set of demands $d$ such that for $f=d P$ there exists

$$
\Sigma \in \operatorname{co}(\mathcal{S}) \text { with } f_{l} r(l, m)<c(l, m) \Sigma(l, m) \text { for all }(l, m) .
$$

Thus $D^{o}$ is the set of feasible demands. The next fact is elementary.
Proposition 3. $0 \in D$. $D$ is a convex, compact polytope. If $d \in D, 0 \leqslant d^{\prime} \leqslant d$ (coordinate wise), then $d^{\prime} \in D$.
2.3. Fixed-time control

We find the fixed-time control with minimal cycle time for each $d \in D^{o}$.

Definition 2. A fixed-time network control with cycle length $T$ periods (or $T \tau \mathrm{sec}$ ) is a collection of network control matrices $S^{1}, \ldots, S^{k}$, corresponding durations $\lambda_{1}, \ldots, \lambda_{k}$, expressed in fractions of the cycle length, such that $T=\left(\sum \lambda_{i}\right) T+L$ and $L$ is the pre-specified lost time in periods per cycle.
$L$ is the lost time in each cycle during which vehicles cannot use the intersection. A fixed-time control defines a periodic admissible network control sequence which repeats the pattern: actuate $S^{i}$ for duration $\lambda_{i} T, i=1, \ldots, k, S^{k+1}=0$ for duration $L$. In this formulation the $\lambda_{i} T$ are 'effective' durations (with no lost time) and the total lost time is lumped into $S^{k+1}=0$ for duration $L$. ( $k$ is the number of stages in each cycle.) $\lambda_{i} T$ plus an appropriate portion of the lost time $L$ is called the split.

Fix demand $d$ and let $f=d P$ be the corresponding flow vector. Consider the linear program

$$
\begin{array}{ll}
\min & \sum_{S \in \mathcal{S}} \lambda_{S} \\
\text { s.t. } & \sum_{S \in \mathcal{S}} \lambda_{S} c(l, m) S(l, m) \geqslant f_{l} r(l, m), \text { all }(l, m) \\
& \lambda_{S} \geqslant 0 \text { all } S \in \mathcal{S} .
\end{array}
$$

This is an obvious extension of the linear program for a single intersection proposed by Allsop (1972). A version of (14) is implicit in the formulation of Wong and Yang (1997).

Let $\left\{\lambda_{S}^{*}\right\}$ be an optimum solution and let $\lambda^{*}=\sum \lambda_{S}^{*}$ be the minimum value of (14). ( $\lambda^{*}$ is the 'network' degree of saturation.)
Theorem 1. (a) $d \in D^{o}$ if and only if $\lambda^{*}<1$. (b) The fixed-time control given by the durations $\left\{\lambda_{S}^{*}+\epsilon, S \in \mathcal{S}\right\}$ ( $\epsilon>0$ arbitrary) accommodates $d$ with a cycle time arbitrarily close to the minimum cycle time

$$
T=\frac{L}{1-\lambda^{*}} \times \tau \sec
$$

(c) If $0 \leqslant \hat{d} \notin D$, no admissible control sequence can accommodate $\hat{d}$.

Proof. (a) follows from (13) and (14). (b) Consider any fixed-time control given by durations $\mu_{S}, S \in \mathcal{S}$, that accommodates $d$. If its cycle time is smaller than $T,\left(1-\sum_{S} \mu_{S}\right) T>L$ and hence $\sum_{S} \mu_{S}<\lambda^{*}$, but $\lambda^{*}$ is the minimum value. (c) Suppose the sequence $S=\{S(t)\}$ accommodates $\hat{f}=\hat{d} P$, i.e., $\Sigma_{S}(l, m)>\hat{f}_{l} r(l, m)$ for all $(l, m)$. By Proposition 2, $\Sigma_{S} \in \operatorname{co}(\mathcal{S})$. But then by (12), $\hat{d} \in D . \quad \square$

Remark 1. Theorem 1 states that $d \in D^{o}$ can be accommodated by a fixed-time control. But construction of this control requires knowledge of the demand vector $d$ and the turn ratios or routing proportions $r(l, m)$. The feedback control $u^{*}$ defined in Section 3 accommodates any $d \in D^{o}$ without requiring knowledge of $d$.

Suppose the cycle time $T$ is fixed and $\lambda^{*}$ is the minimum value of (14). The demand $d$ will be accommodated by the fixedtime control of Definition 2 provided

$$
T>\frac{L \tau}{1-\lambda^{*}} \text { or } \lambda^{*}<1-\frac{L \tau}{T} .
$$

Moreover if $\mu^{*}>1$ is defined by

$$
\lambda^{*} \mu^{*}=1-\frac{L \tau}{T},
$$

then ( $\mu^{*}-1$ ) is the network reserve capacity since the demand $\mu \mathrm{d}$ is accommodated by scaling the durations to $\mu \lambda_{s}^{*}$ within the same cycle time $T$, provided $\mu<\mu^{*}$. This network analog of the intersection reserve capacity in Allsop (1972) was formulated in Wong and Yang (1997).

The linear program (14) is particularly easy because it decomposes into small linear programs, one per intersection. We study these for standard intersections.

Example 2. Consider a network of standard intersections illustrated in Fig. 3. Suppose the demand vector $d$ is known and the flows $f=d P$ are calculated. At each intersection, $f$ gives eight turn movements of the form $f_{l} r(l, m)$, arranged as a row vector $\vartheta=\left(\vartheta_{1}, \ldots, \vartheta_{8}\right)$ corresponding to the phases $\phi_{1}, \ldots, \phi_{8}$, respectively. Any one of eight phase-pairs can be actuated at a time: $\left(\phi_{1}, \phi_{5}\right),\left(\phi_{1}, \phi_{6}\right), \ldots$. Each pair can be written as a row vector of dimension 8, with $C_{i}$ in the $i$ th position if phase $\phi_{i}$ is actuated and 0 otherwise. ( $C_{i}$ is the saturation flow per period for phase $\phi_{i}$.) Call these vectors $\varphi_{1,5}, \varphi_{1,6}$, etc. Solve the linear program

$$
\min \left\{\sum \lambda_{i, j} \mid \lambda_{1,5} \varphi_{1,5}+\lambda_{1,6} \varphi_{1,6}+\cdots \geqslant \vartheta\right\} .
$$

Suppose the minimum value of (17) for intersection $n$ is $\lambda^{*}(n)$. If the same cycle length is required for the entire network, let $\lambda^{*}=\max \left\{\lambda^{*}(n) \mid n \in \mathcal{N}\right\}$. The minimum network-wide cycle length is given by (15). The linear program (17) was formulated by Allsop (1972).

If $\lambda^{*}=\lambda^{*}(n)$, it is appropriate to call $n$ the critical intersection.

## 3. Queues and feedback signal control

We recall the store-and-forward queueing network model of the movement of individual vehicles from one link to another, and define what it means for a feedback control to be stabilizing. We then introduce the max pressure (MP) control and show that MP is stabilizing and maximizes throughput.

### 3.1. Store-and-forward model

See Fig. 4. Associate a distinct queue with each $\operatorname{link} l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}$ and each $m \in$ Out $_{l}$, and let $x(l, m)(t)$ be the length of this queue at the beginning of period $t$. Let $X(t)=\{x(l, m)(t)\}$ be the array of all the queue lengths. $X(t)$ is the state of the queueing network. $\mathcal{X}=\{x(l, m) \geqslant 0\}$ is the state space.

At the end of each period $t$ a network control matrix $S(t)=\{S(l, m)(t)\} \in \mathcal{S}$ must be selected as a function of $X(t)$ for use in period $(t+1)$, see bottom of Fig. 4. Thus $S(t)=u(X(t))$ is given by the feedback control policy or function $u: \mathcal{X} \rightarrow \mathcal{S} . u$ is a stationary or time-invariant policy, since it does not explicitly depend on $t$.

## Random demand, turns, saturation flow

For each $l$ and $t$, the $R(l)(t)$ are iid random variables with $R(l)(t)=m$ with probability $r(l, m)$. Define $R(l, m)(t)=1$ or 0 accordingly as $R(l)(t)=m$ or $\neq m$.

For each $(l, m)$ and $t$, the $C(l, m)(t)$ are non-negative bounded iid random variables with mean value equal to the service or saturation flow rate $c(l, m)$. For each entry link $l$ the $d(l, m)(t+1)$ are non-negative bounded iid random variables with mean $d_{l} r(l, m)$. The $\{R(l)(t), C(l, m)(t), d(l, m)(t+1)\}$ are all independent.

We now develop the equations of evolution of the state $X(t)$. (See the bottom of Fig. 4.) First consider an internal link $l \in \mathcal{L}$. Suppose $S(l, m)(t)=1$, that is phase $(l, m)$ is actuated. Suppose the random number $C(l, m)(t+1)$ is realized. Then up to $C(l, m)(t+1)$ vehicles will leave queue $(l, m)$ and they will be routed to queue $(m, p)$ if $R(m, p)(t+1)=1$. So at the beginning of period $(t+1), x(l, m)$ will decrease by up to $C(l, m)(t+1)$ and $x(m, p)$ will increase by the same number. These changes are captured in the queue update equation:

$$
\begin{aligned}
x(l, m)(t+1)= & x(l, m)(t)-[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)] \\
& +\sum_{k}[C(k, l)(t+1) S(k, l)(t) \wedge x(k, l)(t)] R(l, m)(t+1), \quad l \in \mathcal{L}, \quad m \in \text { Out }_{l}
\end{aligned}
$$

(As before $z \wedge y=\min \{z, y\}$.) The second term on the right in (18) indicates that the queue length $x(l, m)(t)$ decreases by up to $C(l, m)(t+1)$ vehicles if $S(l, m)(t)=1$; the third term indicates that up to $C(k, l)(t+1)$ vehicles will move from queue $(k, l)$ if $S(k, l)(t)=1$ and they will join queue $(l, m)$ if $R(l, m)(t+1)=1$.

The queue update equation for an entry link $l \in \mathcal{L}_{\text {entry }}$ is a bit different since it has exogenous arrivals and no input links (Fig. 1):

$$
x(l, m)(t+1)=x(l, m)(t)-[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)]+d(l, m)(t+1), l \in \mathcal{L}_{\text {entry }}, \quad m \in \text { Out }_{l} .
$$

Thus the queue length $x(l, m)$ decreases as in (18), but it increases from exogenous demands with expected rate $d_{l} r(l, m)$ vehicles per period.

Suppose the initial state $X(1)=\{x(l, m)(1)\}$ is a non-negative bounded random variable. Since $S(t)=u(X(t))$ is a function of the current state $X(t)$, and since the service rates $C(l, m)(t+1)$, turn movements $R(l, m)(t+1)$, and demands $d(l, m)(t+1)$ in (18) and (19) are independent of $X(1), \ldots, X(t)$, the process $X(t), t=1,2, \ldots$ is a Markov chain. The transition probabilities and hence the statistics of the chain $X(t)$, depend on the feedback policy $u$.

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-07.jpg?height=443&width=1098&top_left_y=1900&top_left_x=385)
Fig. 4. The queueing network (top). Sequence of events in each period (bottom).

Definition 3. The queue length process $X(t)=\{x(l, m)(t)\}$ is stable in the mean (and $u$ is a stabilizing control policy) if for some $K<\infty$

$$
\frac{1}{T} \sum_{t=1}^{T} \sum_{l, m} E x(l, m)(t)<K, \quad \text { for all } T .
$$

Stability in the mean implies that the chain is positive recurrent and has a unique steady-state probability distribution. In (20), $E$ denotes expectation.

### 3.2. Max pressure

The max pressure (MP) signal control policy $u^{*}: \mathcal{X} \rightarrow \mathcal{S}$ specified below does not require knowledge of the average demands $d=\left\{d_{l}\right\}$. Moreover under MP $X$ is stable whenever $d \in D^{o}$ (see Theorem 2), so MP maximizes throughput. We now specify $u^{*}$.

For $X \in \mathcal{X}$ assign the weight of each phase ( $l, m$ )

$$
w(l, m)(X)=x(l, m)-\sum_{p \in \text { Out }_{m}} r(m, p) x(m, p),
$$

and assign the pressure of each network signal control matrix $S \in \mathcal{S}$

$$
\gamma(S)(X)=\sum_{l, m} c(l, m) w(l, m)(X) S(l, m)=\sum_{l, m: S(l, m)=1} c(l, m) w(l, m)(X) .
$$

$\left(\operatorname{In}(21) x(m, p)=0\right.$ for $m \in \mathcal{L}_{\text {exit }}$.) The MP policy $u^{*}$ is

$$
u^{*}(X)=\arg \max \{\gamma(S)(X) \mid S \in \mathcal{S}\} .
$$

Thus MP selects the network signal control matrix with the maximum pressure at every state $X$. The pressure of a signal control matrix $S$ is the sum of the saturation flows multiplied by the weights of all the phases that $S$ actuates simultaneously. The weight of a phase $(l, m)$ is the queue length $x(l, m)$ at the input link $l$ minus the average queue length $\sum_{p} r(m, p) x(m, p)$ at the output link $m$. If we regard $x(l, m)^{\text {down }}=\sum_{p} r(m, p) x(, p)$ as the (average) downstream queue length and $x(l, m)$ as the upstream queue length, $w(l, m)$ is simply the difference between the upstream and downstream queue lengths.

Note At an isolated intersection each output link is an exit, so the weight in (21) is simply $x(l, m)$; hence the pressure (22) is simply the sum of queue lengths multiplied by their corresponding saturation rates.

Theorem 2. The MP control $u^{*}$ is stabilizing whenever the average demand vector $d=\left\{d_{l}\right\} \in D^{o}$. There is no stabilizing control when $d \notin D$.

Proof. The second statement of the theorem is implied by Theorem 1. To prove the first statement, let $S(t)=u^{*}(X(t))$ be the network control matrix selected by the policy (23). The resulting Markov chain is given by (18) and (19). For any state $X \in \mathcal{X}$, let $|X|^{2}=\sum_{l, m}[x(l, m)]^{2}$ be the sum of squares of all the queue lengths. We will show that there exist $k<\infty$ and $\epsilon>0$ such that under $u^{*}$

$$
E\left\{|X(t+1)|^{2}-|X(t)|^{2} \mid X(t)\right\} \leqslant k-\epsilon|X(t)|, \quad t=1,2, \ldots
$$

Suppose (24) holds. Taking (unconditional) expectations and summing over $t=1, \ldots, T$ gives

$$
E|X(T+1)|^{2}-E|X(1)|^{2} \leqslant k T-\epsilon \sum_{t=1}^{T} E|X(t)|,
$$

and so

$$
\epsilon \frac{1}{T} \sum_{t=1}^{T} E|X(t)| \leqslant k+\frac{1}{T} E|X(1)|^{2}-\frac{1}{T} E|X(T+1)|^{2} \leqslant k+\frac{1}{T} E|X(1)|^{2},
$$

which immediately implies the stability condition (20). Inequality (24) is proved in Appendix A. □

Remark 2. From (A.5) in Appendix A we see that $\epsilon$ in (24) is proportional to the reserve capacity ( $\mu^{*}-1$ ) defined in (16) with $L=0$. From (25), the sum of the mean queue lengths is bounded in equilibrium by

$$
E|X(t)| \leqslant \frac{k}{\epsilon} .
$$

From (A.9) $k=M\left(K_{2}+K^{2}\right)$ in which $M$ is the total number of queues in the network and $K_{2}, K$ are constants that depend only on the maximum values of the demands and saturation flows, but not on the network. Thus the mean length of any individual queue in equilibrium is bounded by

$$
\frac{1}{M} E|X(t)| \leqslant \epsilon^{-1}\left(K_{2}+K^{2}\right) .
$$

The dependence of the queue length on the inverse of the reserve capacity is similar to well-known queuing formulas. For example, in an M/M/1 system the mean queue length is $(1-\rho)^{-1} \rho$, in which $\rho$ is the ratio of the mean arrival rate to the mean service rate, so that ( $1-\rho$ ) plays the same role as $\epsilon$. (Note, however, that the queues in the traffic network are not M/M/1.)

Remark 3. Calculation of the MP control $u^{*}$ divides into local calculations, one for each intersection or node. Partition array $X$ into the set of arrays $\{X(n), n \in \mathcal{N}\}$, with $X(n)=\{x(l, m) \mid l \in I(n), m \in O(n)\}$ denoting the array of queues on links adjacent to node $n$. Express the network control matrix $S$ as the array of intersection control matrices $\left\{S_{n}, n \in \mathcal{N}\right\}$. Observe that

$$
\gamma(S)(X)=\sum_{n \in \mathcal{N}} \gamma_{n}\left(S_{n}\right)\left(X_{n}\right) ; \gamma_{n}\left(S_{n}\right)\left(X_{n}\right)=\sum_{l \in I(n), m \in O(n)} c(l, m) w(l, m)\left(X_{n}\right) S_{n}(l, m) .
$$

It follows from (23) that $u^{*}(X)=\left\{u_{n}^{*}\left(X_{n}\right), n \in \mathcal{N}\right\}$ with

$$
u_{n}^{*}\left(X_{n}\right)=\arg \max \left\{\gamma_{n}\left(S_{n}\right)\left(X_{n}\right) \mid S_{n} \in \mathcal{S}_{n}\right\} .
$$

So for each intersection $n$ and in each period $t$, the procedure in Table 1 implements $u^{*}$ in real time. The calculations in Table 1 are much simpler than those required by OPAC, RHODES and SCOOT.

Theorem 3 is a stochastic version of Theorem 1. It seems not to be in the literature. It can be proved in the same way as Theorem 2.

Theorem 3. Suppose $d \in D^{o}$ and let $\{S(t)\}$ be a fixed-time periodic control sequence that accommodates $d$. The resulting queue length process is stable in the mean.

## 4. Variations of MP

Several variations of MP are considered in this section.

### 4.1. Adaptive MP

The MP controller (21)-(23) requires two parameter sets: turn ratios $\{r(m, p)\}$ and saturation flow rates $\{c(l, m)\}$. If these parameters are not known one may use estimated parameters in (23). More precisely, the estimates $\hat{r}(m, p)$ and $\hat{c}(l, m)$ are used to estimate pressure $\hat{\gamma}(S)(X)$ from (22), and the AMP control $\hat{u}$ by

$$
\hat{u}(X)=\arg \max \{\hat{\gamma}(S)(X) S \mid S \in \mathcal{S}\} .
$$

A modification the proof of Theorem 2 yields the next result.
Theorem 4. Suppose the estimates $\{\hat{r}(m, p)(t)\}$ and $\{\hat{c}(l, m)(t)\}$ converge to the true parameters $\{r(m, p)\}$ and $\{c(l, m)\}$. The AMP control $\hat{u}$ is stabilizing whenever the average demand vector $d \in D^{o}$.

The estimates can be obtained if vehicle turns and discharge rates at intersections are measured. In principle the exogenous demand vector $d$ can also be estimated. But this is difficult, since there are entry links for residences, offices, shopping centers, etc. As these demands vary significantly over time, one needs to instrument these entry links for continuous measurement.

The key to stability of MP (in fact of any feedback controller) is the inequality (see (A.6))

$$
\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m}\left[f_{l} r(l, m)-S^{*}(l, m)(t) c(l, m)\right] w(l, m)(t)=\epsilon<0 .
$$

Table 1
Procedure to implement $u^{*}$.

The larger is $\epsilon$, the looser can be the estimates of turn probabilities, saturation flow rates and queues used to calculate pressure. Thus $\epsilon$ provides a rough estimate of the robustness of MP to parameter misspecification.

### 4.2. Weighted queues

Inequality (24) suggests, and its proof in Appendix A confirms, that under the MP control $u^{*},|X(t)|^{2}$ serves as a stochastic quadratic Lyapunov function of the Markov chain $\{X(t)\}$. More significantly, at any current state $X(t)$, the control $S^{*}(t)=u^{*}(-$ $X(t)$ ) moves the state in a direction that (approximately) minimizes the expected 'gradient' $E\left\{|X(t+1)|^{2}-|X(t)|^{2} \mid X(t)\right\}$ and hence it also minimizes $E\left\{|X(t+1)|^{2} \mid X(t)\right\}$ (see (A.6)). Thus one can regard $u^{*}$ as a one-step quadratic cost minimizing strategy.

Reference to Lyapunov function suggests consideration of the more general quadratic function,

$$
|Q X|^{2}=\sum_{l, m}[Q(l, m) x(l, m)]^{2},
$$

in which $Q=\{Q(l, m)\}$ is any positive array and $Q X$ denotes the array $\{q(l, m) x(l, m)\}$. It turns out that this is also a Lyapunov function. Define the Q-weight

$$
w_{Q}(l, m)=[Q(l, m)]^{2} x(l, m)-\sum_{p \in \text { Out }_{m}} r(m, p)[Q(m, p)]^{2} x(m, p),
$$

and to each $S \in \mathcal{S}$ assign the $Q$-pressure

$$
\gamma_{Q}(S)(X)=\sum_{l, m} c(l, m) w_{Q}(l, m)(X) S(l, m)=\sum_{l, m: S(l, m)=1} c(l, m) w_{Q}(l, m)(X) .
$$

Define the policy $u_{Q}^{*}$ by

$$
u_{Q}^{*}(X)=\arg \max \left\{\gamma_{Q}(X) \mid S \in \mathcal{S}\right\} .
$$

Theorem 5. $u_{Q}^{*}$ is a stabilizing control whenever the average demand vector $d=\left\{d_{l}\right\} \in D^{o}$. There is no stabilizing control when $d \notin D$.

Proof. It is sufficient simply to repeat the proof of Theorem 2, replacing the crucial inequality (24) by

$$
E\left\{|Q X(t+1)|^{2}-|Q X(t)|^{2} \mid X(t)\right\} \leqslant k_{Q}-\epsilon_{Q}|Q X(t)|, \quad t=1,2, \ldots
$$

which is proved in Appendix B. □
We illustrate how the more general Lyapunov function (28) can be put to good use, keeping in mind the intuition that the control $u_{Q}^{*}(X(t))$ approximately minimizes the one-step 'cost' $\sum_{l, m}[Q(l, m) x(l, m)(t+1)]^{2}$. The first idea follows Aboudolas et al. (2009b, eq (13)) and sets

$$
[Q(l, m) x(l, m)]^{2}=\frac{x(l, m)^{2}}{x_{\max }(l, m)}
$$

in which $x_{\text {max }}(l, m)$ is the maximum permissible queue length. As a result, $u_{Q}^{*}$ gives preferences to queues on links with small storage capacity.

Another suggestion may be useful in the case that certain movements $(l, m) \in B$ are restricted to buses (say), which are to be given signal priority over other vehicles. If a large value of $Q(l, m)$ is chosen for $(l, m) \in B, u_{Q}^{*}$ will favor movement of these vehicles. The magnitude of the ratios $Q(l, m) / Q\left(l^{\prime}, m^{\prime}\right)$ for $\left(l^{\prime}, m^{\prime}\right) \notin B$, trades off bus movements vs. movements of other vehicles. If these ratios are large, $u_{Q}^{*}$ will preempt normal signal operation in favor of the bus, whenever one arrives.

Remark 4. Theorem 5 offers a theoretical comment on the signal control $u_{\rho}$ proposed in Lin and Lo (2008) for an isolated intersection with only two movements (e.g. two one-way streets with no turns). The feedback control is a function of the two queue lengths $x(1)$ and $x(2)$. The objective of the control $u_{\rho}$ is to maintain the queue length ratio $x(1)(t) / x(2)(t)$ near a pre-specified value $\rho$. Accordingly, $u_{\rho}$ serves queue $x(1)$ when $x(1)>\rho x(2)$ and serves queue $x(2)$ when $x(1)<\rho x(2)$. Consider now the strategy $u_{Q}^{*}$ that maximizes the pressure $x(1) c(1) S(1)+\hat{\rho} x(2) c(2) S(2)$, with $S(1)+S(2)=1, c(1), c(2)$ being the saturation flows for the two movements. If $\hat{\rho}=[c(1) / c(2)] \rho, u_{Q}^{*}$ is the same as $u_{\rho}$. If the demand can be accommodated, Theorem 5 guarantees that $u_{\rho}$ is a stabilizing feedback control, and the queue lengths $(x(1)(t), x(2)(t))$ have a steady-state distribution. Consequently, the ratio $x(1)(t) / x(2)(t)$ also has a steady-state distribution. This distribution gives the precise sense in which this ratio is close to the desired ratio $\rho$.

### 4.3. Invoking MP once per cycle

The basic MP control (23) is changed at the beginning of each period, which may be small. For example, SCOOT, OPAC, RHODES and Xie et al. (2012) decide every second or so whether to continue a stage or to switch to another stage. Note that the MP calculation requires only a tiny computational effort compared with these other schemes. From an implementation point of view it may be desirable to take the period as the cycle so that the MP signal control is changed only once each cycle. Since the period has been unspecified, the results above continue to hold.

However, invoking MP only once per cycle can lead to undesirable behavior. For example, consider an isolated intersection in which demands are very unequal. Suppose also that each stage actuates a single phase and all the saturation rates are equal. Then over any cycle, MP will actuate the phase with the largest queue length, which frequently will be the phase with the largest demand. The phase with the least demand will be actuated only when its queue length becomes the largest. Consequently, vehicles in this queue will wait for several cycles, which may be undesirable. One way of relieving this condition is to insist that the MP actuates every stage $S$ for a minimum duration $\lambda_{S}^{\text {min }}$. With this restriction, the MP control for the next cycle selects durations $\lambda_{S}^{*}$ given by

$$
u^{\min , *}(X)=\arg \max _{\left\{\lambda_{S}\right\}}\left\{\sum_{S} \lambda_{S} \gamma(S)(X) \mid \lambda_{S} \geqslant \lambda_{S}^{\min }, \sum \lambda_{S}=1\right\},
$$

which can be compared with (23).
Define $D^{\text {min }}$ to be the set of demand vectors such that for $f=d P$ there exists $\left\{\lambda_{S} \geqslant \lambda_{S}^{\text {min }}\right\}$ with $f_{l} r(l, m) \leqslant \sum_{s} c(l, m) \lambda_{s} S(l, m)$ for all $(l, m)$. Let $D^{\text {min,o }}$ be the interior of $D^{\text {min }}$. The next result is proved in the same way as Theorem 2.

Theorem 6. The MP control $u^{\text {min,* }}$ is stabilizing whenever $d \in D^{\text {min,o }}$.
While this result mitigates the negative impact of invoking MP once per cycle, neverthless a sub-cycle invocation of MP is much more beneficial.

### 4.4. Long links

In the model, the actuation of phase $(l, m)$ permits a vehicle to move from queue $(l, m)$ to a queue $(m, p)$ in one period. This is clearly unrealistic if, say, the link $l$ or $m$ is very long compared to another link. That is, the model ignores the link travel time. This limitation is easily overcome by replacing a long link by several links. in Fig. 5. The long link $l$ in the top of Fig. 5 is replaced by a sequence of short links $\left\{l_{i}\right\}$ shown in the bottom of the figure. These links are connected by virtual intersections, with only one phase, namely $\left(l_{i}, l_{i+1}\right)$ with a single admissible signal control matrix, $S\left(l_{i}, l_{i+1}\right)(t) \equiv 1$. The stabilizing control policy at the original intersections remains unchanged.

### 4.5. Saturated links

The queues in Fig. 4 are 'vertical' with unlimited capacity, as in many store-and-forward queue models. Therefore the model does not permit saturation of a downstream link that blocks the movement of vehicles from an upstream link. This is a limitation. It is straightforward to model blocking in the update Eq. (18). The first term in the right of (18) $\Delta=-C(l \cdot m)(t+1) S(l, m)(t) \wedge(x(l, m))(t)$ implies that $x(l, m)$ is decremented if the phase $(l, m)$ is actuated, regardless of the congestion in the downstream link $m$. If link $m$ has a queue capacity of $L(m)$ and the total queue length is $x(m)=\sum_{p} x(m, p)$, one could replace $\Delta$ in (18) by $\Delta \times \mathbf{1}(x(m) \geqslant L(m))$, so that movement $(l, m)$ is blocked whenever link $m$ is saturated.

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-11.jpg?height=401&width=999&top_left_y=1942&top_left_x=437)
Fig. 5. The long link $l$ is replaced by a sequence of short links $\left\{l_{i}\right\}$ connected by virtual intersections (open circles).

This observation suggests a variation of the MP policy (23) defined by

$$
u^{s a t, *}(X)=\arg \max \{\gamma(S)(X) \mid S \in \mathcal{S}, S(l, m)=0 \quad \text { if } x(m) \geqslant L(m)\} .
$$

Under $u^{\text {sat,* }}$, movement into a saturated link is not permitted. However, Example 3 shows that stability under $u^{\text {sat,* }}$ is not guaranteed.

Example 3. In the two networks of Fig. 6, consider the initial condition $x(2,3)=0, x(2,4)=L(2)$ and $x(4,2)=x(4,5)=L(4)$, so links 2 and 4 are initially saturated in both networks. As a consequence for the left network, under $u^{\text {sat,* }}$ all movements are blocked, and there is a gridlock. Thus $u^{\text {sat,* }}$ performs poorly. In the right network, however, $u^{\text {sat,* }}$ will actuate movement (4,5) and the initial gridlock will not persist. Indeed one can show that for the right network, $u^{\text {sat,* }}$ maximizes throughput. $u^{\text {sat,* }}$ is suggested by the study of max pressure policies for networks with bounded queues in Giaccone et al. (2005).

### 4.6. Coordinated intersections

The discussion in this paper is limited to the determination of splits, that is the duration of each stage within a cycle. The cycle time itself and the offset must be determined by other means. For a discussion see Aboudolas et al. (2009a).

## 5. Counter-examples

We present examples of reasonable control strategies, which, however, are de-stabilizing.

### 5.1. Full actuation

Consider a 'fully-actuated' control in which at any intersection each stage actuates only one movement, hence serves one queue at its specified saturation rate. Also specified is a 'max gap' as a lower bound $f_{\min }$ on the flow. (The flow is inversely proportional to the headway or gap between successive vehicles.) The control operates as follows. If a particular stage is selected at some time it continues to be selected so long as the flow along the actuated phase exceeds $f_{\text {min }}$. When the flow drops below this minimum value a new stage is selected. The new stage is the one with the maximum product of queue length and saturation rate.

Example 4. Fig. 7 depicts the network. It has five links: link 1 is the entry link, link 5 is the exit link. The four possible phases are (1,2), (2,3), (3,4), (4,5), with corresponding saturation rates $c(1,2)=c(3,4)=4 \mathrm{vpp}, c(2,3)=c(4,5)=3 / 2 \mathrm{vpp}$. No turns are allowed. The network is deterministic. Vehicles enter link 1 at the rate 1 vehicle per period (vpp). The minimum flow is $f \mathrm{~min}=1.1$. The queues $x_{i}$ and their departures $d_{i}$ are labeled as in Fig. 7. The initial queues are

$$
x_{1}(0)=K, x_{2}(0)=x_{3}(0)=x_{4}(0)=0 .
$$

Fig. 8 displays the plots of the queues and departures. Starting at time 0 the queue $x_{1}$ decreases at rate 3 , since it is served at saturation rate $c(1,2)=4$ and the arrival rate is $a(t)=1$. At time $K / 3, x_{1}(K / 3)=0$, but movement $(1,2)$ continues to be served at rate $d_{1}(t)=1$ until time $2 K$, because queue $x_{4}(t)=0, t \in[0,2 K]$. During [0,2K], queue $x_{2}$ builds up until time $K / 3$ and it then decreases until it becomes empty at $t=2 K$. Since $d_{2}(t)=3 / 2>f_{\text {min }}=1.1$ for $t \in[0,2 K]$, the actuated control does not serve queue $x_{3}$ during this interval $[0,2 K]$. So $x_{3}(t)$ increases until $x_{3}(2 K)=3 K$; it then decreases at rate $d_{3}(t)=4$ until it is empty at $x_{3}(2 K+3 / 4)=0$. Thus $d_{3}(t)$ is as shown in the figure. Finally, $x_{4}(t)$ increases until time $2 K+3 / 4$ and it then decreases at its saturation rate $c(4,5)=3 / 2$. The departure $d_{4}(t)=3 / 2>1.1$ until time $t=4 K$, at which time $x_{4}(4 K)=0$. Hence queue $x_{1}$ is not served until time $t=4 K$. Finally at time $4 K$ the queues are

$$
x_{1}(4 K)=2 K, \quad x_{2}(2 K)=x_{3}(2 K)=x_{4}(2 K)=0,
$$

which is the same as (31), except that the queues have doubled in length. Hence,

$$
x_{1}(0)=K, x_{1}(4 K)=2 K, x_{1}(8 K)=4 K, x_{1}(16 K)=8 K, \cdots,
$$

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-12.jpg?height=300&width=848&top_left_y=2047&top_left_x=522)
Fig. 6. Under $u^{\text {sat,* }}$ the network on the left can exhibit gridlock, but the network on the right will function well.

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-13.jpg?height=413&width=854&top_left_y=183&top_left_x=504)
Fig. 7. The deterministic network with five links and two intersections of Example 4.

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-13.jpg?height=538&width=1493&top_left_y=703&top_left_x=185)
Fig. 8. Trajectories of queues and departures in network of Example 4.

so that the network is unstable under this fully-actuated control. On the other hand, the fixed-time control that actuates phases $(1,2)$ and $(3,4)$ for a fraction $(1 / 4+\epsilon)$ and phases $(2,3)$ and $(4,5)$ for a fraction $(2 / 3+\epsilon)$ of a cycle is stabilizing, according to Theorem 1.

Remark 5. The control in this example appears to be identical to the Schedule-driven Intersection Control (SchIC) studied in Xie et al. (2012). The instability of this fully-actuated control is related to the fact that the amount of time phase 1 (or 2,3,4) is actuated keeps growing without bound. Thus the instability can be eliminated by imposing a 'max green' - the maximum time that a phase can be continuously actuated when another phase has a non-zero queue. In practice, one always has a max green. However, a more detailed study of this example reveals that the maximum queue length will grow as the max green is increased. This example indicates that fully actuated control can lead to large delays if the network has 'loops' like in Fig. 7.

### 5.2. Isolated intersection

An isolated intersection has phases ( $l, m$ ) for entry links $l \in \mathcal{L}_{\text {entry }}$ and exit links $m \in \mathcal{L}_{\text {exit }}$. There are no internal links. The state equations are

$$
x(l, m)(t+1)=x(l, m)(t)-[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)]+d(l, m)(t+1), l \in \mathcal{L}_{\text {entry }}, m \in \mathcal{L}_{\text {exit. }}
$$

The weight of a phase ( $l, m$ ) is $\chi(l, m)$ so the pressure of an admissible intersection control matrix $S$ is $\gamma(S)=\sum_{m} c(l, m) x(l, m) S(l, m)$-the sum of the queue lengths multiplied by their saturation flows at the input links of the activated phases. The MP control $u^{*}$ maximizes this sum.

By way of contrast, consider the feedback control $u^{\dagger}$ which at each time maximizes the instantaneous intersection $u t i l i$ zation, i.e., the number of vehicles that cross the intersection. If the weight of a phase is defined as

$$
w^{\dagger}(l, m)=\mathbf{1}(x(l, m)),
$$

and the score of an admissible $S$ as

$$
\gamma^{\dagger}(S)=\sum_{m} \mathbf{1}(x(l, m)) S(l, m),
$$

![](https://cdn.mathpix.com/cropped/e25c0d85-78ec-4165-b5ad-b20a76ca4c1f-14.jpg?height=330&width=796&top_left_y=187&top_left_x=552)
Fig. 9. The intersection of Example 5 has two entry and two exit links.

then $u^{\dagger}(X)=\arg \max \left\{\gamma^{\dagger}(S)\right\}$ is the utilization-maximizing signal control. If more than one $S$ maximizes $\gamma^{\dagger}(S)$, the tie is broken randomly. Above $\mathbf{1}(x(l, m))=1$ or 0 accordingly as $x(l, m)>0$ or $=0$. Note that the presence detector for movement $(l, m)$ measures $\mathbf{1}(x(l, m))$, so $u^{\dagger}$ is easy to implement.

From (33) the expected sum of the queue lengths in period $(t+1)$ conditioned on the state $X(t)$ is

$$
E\left\{\sum_{l, m} x(l, m)(t+1) \mid X(t)\right\}=\sum_{l, m} x(l, m)(t)-\sum_{l, m} S(l, m)(t) \mathbf{1}(x(l, m)(t))+\sum_{l, m} d_{l} r(l, m) .
$$

It is minimized by $u^{\dagger}$ (which minimizes the second term on the right above) and not by $u^{*}$. It may be surprising that $u^{\dagger}$ is not stabilizing in Example 5 below, adapted from McKeown et al. (1999).

Example 5. The intersection has two entry links, 1 and 2, and two exit links, $a$ and $b$, see Fig. 9. There are three permitted phase-pairs: $\{(1, a),(2, b)\},\{(1, b),(2, a)\}$ and $\{(2, a),(2, b)\}$. The saturated rates for each of the four movements $(1, a),(1, b),(2, a)$, $(2, b)$ equals 1 vehicle per period. The cycle time is $T$ periods and the lost time $L=0$. The demands $d(1, a)(t), d(1, b)(t), d(2, a)(t)$, $d(2, b)(t)$ are all iid 0-1 random variables with mean (0.5 - $\delta$ ). Clearly this demand vector $d \in D^{o}$ for every $\delta>0$, so MP control $u^{*}$ is stabilizing. (The fixed-time control that actuates phase-pairs $\{(1, a),(2, b)\}$ and $\{(1, b),(2, a)\}$ each for duration $0.5 T$ is also stabilizing.) We now show that for some values of $\delta>0, u^{\dagger}$ is not stabilizing. Define the event $A=\{d(2, a)(t)=d(2, b)(t)=1\}$ and observe from (33) or Fig. 9 that

$$
P\{x(2, a)(t+1)>0, x(2, b)(t+1)>0 \mid A\}=1 .
$$

Then conditional on $A, u^{\dagger}$ selects one of the phase-pairs $\{(2, a),(2, b)\}$, or $\{(2, a),(1, b)\}$ if $x(1, b)(t+1)>0$, or $\{(2, b),(1, a)\}$ if $x(1, a)(t+1)>0$. Hence

$$
P\{S(1, a)(t+1)+S(1, b)(t+1)=1 \mid A\} \leqslant \frac{2}{3}
$$

Now $P(A)=P(d(2, a)(t)=1) \times P(d(2, b)(t)=1)=(0.5-\delta)^{2}$. Hence

$$
\begin{aligned}
P(S(1, a)(t+1)+S(1, b)(t+1)=1) & \leqslant P\{S(1, a)(t+1)+S(1, b)(t+1)=1 \mid A\} \times P(A)+(1-P(A)) \\
& \leqslant \frac{2}{3}(0.5-\delta)^{2}+\left[1-(0.5-\delta)^{2}\right]=1-\frac{1}{3}(0.5-\delta)^{2} .
\end{aligned}
$$

On the other hand, the mean value of $d(1, a)(t)+d(1, b)(t)$ is $(1-2 \delta)$. Hence $u^{\dagger}$ is not stabilizing if

$$
1-\frac{1}{3}(0.5-\delta)^{2}<(1-2 \delta),
$$

which is the case for $\delta<0.358$. With $\delta=0.3$, each demand is only 0.2 vehicles per period, well below capacity of 0.5 , and yet the utilization-maximizing control is unstable.

Example 6. The network, demands, and saturation flow rates are the same as in Example 3. Consider the signal control $u^{p}$ which gives priority to movement $(1, a)$, so that the phase pair $\{(1, a),(2, b)\}$ is actuated whenever $x(1, a)>0$. Let $A=\{d(1, a)(t)=1\}$. Then

$$
P\{x(1, a)(t+1)>0 \mid A\}=1, P\{S(1, a)(t+1)=1, S(2, b)(t+1)=1, S(2, a)(t+1)=0, S(1, b)=0 \mid A\}=1 .
$$

Hence

$$
P\{S(2, a)(t+1)+S(1, b)(t+1)=1\} \leqslant 1-P(A)=0.5+\delta .
$$

On the other hand $d(2, a)+d(1, b)=2(0.5-\delta)=1-2 \delta$. So if $1-2 \delta>0.5+\delta$ or $3 \delta<0.5$, the priority signal control is unstable.

The controllers in Examples 5 and 6 are work-conserving, i.e., there is no 'wasted' green so long as some queue is nonempty. Varaiya (2013) shows that if a stage actuates only one phase every work-conserving controller for an isolated intersection are stabilizing.

## 6. Discussion

The paper presented the max pressure (MP) control of a signalized network. It has three advantages. First, MP is local: the control at an intersection depends only on the queue lengths on adjacent links. Consequently, MP communication requirements are low, and intersections can be added with no change in the control of other intersections. Second, MP adaptively adjusts splits or phase durations to changes in demand without predicting or estimating those demands. MP does require knowledge of turn ratios and saturation flow rates, but adaptive MP can be employed effectively if those parameters can be estimated.

The main contribution of the paper is theoretical. It is proved that MP is stabilizes the network, i.e., maintains bounded queue lengths, if the network can be stabilized by any control. Such a stability guarantee is not available for published adaptive controllers such as SCOOT or ACS-Lite. An instructive theoretical contribution is provided in examples of seemingly reasonable adaptive controllers that are de-stabilizing even when there exist stable fixed-time controllers. These examples underscore the importance of delimiting the range of application within which a proposed adaptive controller can guarantee stability.

While its results are theoretically appealing, the study's limitations also need emphasis, if only because they may point to directions for further work. A common objection to the point-queue model is that unlike queues on real roads, the point queue uses no space. However, the space occupied by a queue can be straightforwardly approximated by the queue length multiplied by the average length of a vehicle, as explained in Section 4.5. This leads to the biggest limitation of the model: its assumption of infinite storage capacity in each link. If a link can only accommodate finite queues, some movements may be blocked even when that movement is actuated - sometimes called 'de facto red'.

Blocking may occur when a link becomes saturated because of stochastic demand fluctuations even though (14) has a solution with $\sum \lambda_{S}<1$, so that with unbounded storage all queues would remain finite in accordance with Theorems 2, 3. The two examples in Section 4.5 show that such blocking may or may not lead to a (permanent) reduction in the throughput. So an important question is to determine when blocking does not lead to throughput reduction. Fig. 6 suggests the looselyworded conjecture that a network with a loop like in the left of the figure can always be subject to gridlock no matter how large the links are.

Saturation of links and blocking can occur for an entirely different reason. A FT controller whose timing plan does not meet the inequalities (10) will lead to unbounded queues, even if a correctly timed FT controller will stabilize the network. Of course, MP will stabilize the network in this case. Note that it is not possible to conclude that a link is saturated as a consequence of oversaturated traffic conditions, i.e. 'demand exceeding capacity', unless demand is measured in the entire network, see Wu et al. (2010), where measurements are used to determine over-saturation in a simple linear network.

Saturation of links will always occur if demand is excessive, i.e., if (12) has no solution. In this case, one may wish to prevent saturation within some protected area using a control strategy that keeps the excess demand outside of this area. Such a 'gating strategy' is studied in Ekbatani et al. (2012), Aboudolas and Geroliminis (2013). A gating strategy may be non-local since saturation in one link calls for throttling demand in an entrance link that does not share an intersection with the saturated link. MP does not directly permit such a non-local gating strategy. However, in Ekbatani et al. (2012), Aboudolas and Geroliminis (2013), the protected area is itself represented by a single link modeled by a so-called network fundamental diagram (NFD), so the entrance link becomes adjacent to this link and, in principle, one can use MP. This is another direction that is worthy of investigation. The MP strategy in Giaccone et al. (2005) is precisely such a non-local gating strategy.

Blocking may occur without saturation in case a lane has shared movements, e.g., a through movement and a permissive left turn. In this case, a left-turning movement may block the next vehicle that wants to make a through movement. The effect is to reduce the saturation flow rate for such movements. Such 'head-of-line' blocking is not permitted by the assumption in this study of a separate queue for each movement. The reduction in the saturation flow rate from head-of-line blocking can be evaluated as in the study of "input-buffered switches" (McKeown et al., 1993).

The paper provides only an introduction to MP, and further work needs to be done. We are exploring three directions. First, we want to study the performance of MP in terms of standard metrics such as delay, utilization, and number of stops. To this end we are developing a discrete-event simulator which will be available for use in modeling and evaluating the performance of standard controllers as well as MP. Second, there are variants of MP that for wireless networks provide delay guarantees (Neely et al., 2005) and maximize throughput even when queue lengths are constrained (Giaccone et al., 2005). These variants merit investigation in the context of signal control. Third, we need practical schemes to estimate queue lengths and to explore the performance of MP when queues are estimated instead of being measured as, for example, in Sanchez et al. (2011).

## Acknowledgements

This research supported by National Science Foundation Award CMMI-0941326 and California Department of Transportation. I am grateful to Nikolas Geroliminis, Gabriel Gomes, Roberto Horowitz, Tasos Kouvelas, Alex Kurzhanskiy, Jennie Lioris, Ajith Muralidharan, Kaan Ozbay, and Markos Papageorgiou for discussions, criticisms and suggestions.

## Appendix A. Proof of (24)

We prove (24) through a sequence of steps. Let $S(t)=u(X(t))$ be any feedback policy. Recall that $X(t+1)$ is given by (18) and (19):

$$
\begin{aligned}
& x(l, m)(t+1)=x(l, m)(t)-[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)]+\sum_{k}[C(k, l)(t+1) S(k, l)(t) \wedge x(k, l)(t)] R(l, m)(t+1), \\
& l \in \mathcal{L}, m \in \text { Out }_{l}, x(l, m)(t+1)=\left[x(l, m)(t)-[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)]+d(l, m)(t+1), l \in \mathcal{L}_{\text {entry }}, m \in \text { Out }_{l} .\right.
\end{aligned}
$$

Define the array $\delta=\{\delta(l, m)\}$ by $\delta=X(t+1)-X(t)$, so

$$
\begin{aligned}
& \delta(l, m)=-[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)]+\sum_{k}[C(k, l)(t+1) S(k, l)(t) \wedge x(k, l)(t)] R(l, m)(t+1), l \in \mathcal{L}, m \in \text { Out }_{l}, \\
& \delta(l, m)=-[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)]+d(l, m)(t+1), l \in \mathcal{L}_{\text {entry }}, m \in \text { Out }_{l} .
\end{aligned}
$$

For any two arrays $Y=\{y(l, m)\}$ and $Z=\{z(l, m)\}$ let $Y^{T} Z=\sum_{l, m} Y(l, m) Z(l, m)$. So $|X(t+1)|^{2}=X(t+1)^{T} X(t+1)$. Hence

$$
|X(t+1)|^{2}-|X(t)|^{2}=|X(t)+\delta|^{2}-|X(t)|^{2}=2 X(t)^{T} \delta+|\delta|^{2}=2 \alpha+\beta, \text { say. }
$$

We separately upperbound $2 \alpha$ and $\beta$.
A.1. Bound on $\alpha$

We have

$$
\begin{aligned}
\alpha= & X(t)^{T} \delta=-\sum_{l \in \mathcal{L}} \sum_{m} x(l, m)(t)[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)] \\
& +\sum_{k} \sum_{l \in \mathcal{L}} \sum_{m} x(l, m)(t)[C(k, l)(t+1) S(k, l)(t) \wedge x(k, l)(t)] R(l, m)(t+1) \\
& +\sum_{l \in \mathcal{L}_{\text {entry }}} \sum_{m} x(l, m)(t)\{-[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)]+d(l, m)(t+1)\} \\
= & \sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}} \sum_{m}[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)]\left\{-x(l, m)(t)+\sum_{p} R(m, p)(t+1) x(m, p)(t)\right\} \\
& +\sum_{l \in \mathcal{L}_{\text {entry }}} \sum_{m} d(l, m)(t+1) x(l, m)(t)
\end{aligned}
$$

Since $R(m \cdot p)(t+1)$ is independent of $\{C(l, m)(t+1), X(t)\}$,

$$
\begin{aligned}
& E\{[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)] R(m, p)(t+1) x(m, p)(t) \mid X(t)\} \\
& =E\{E\{[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)] R(m, p)(t+1) x(m, p)(t) \mid C(l, m)(t+1), X(t)\} \mid X(t)\} \\
& =E\{[C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t)] \mid X(t)\} r(m, p) x(m, p)(t)
\end{aligned}
$$

and by (21), $x(l, m)(t)-\sum_{p} r(m, p) x(m, p)(t)=w(l, m)(t)=w(l, m)(X(t))$, so

$$
E\{\alpha \mid X(t)\}=-\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} E\{C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t) \mid X(t)\} w(l, m)(t)+\sum_{l \in \mathcal{L}_{\text {entry }}, m} d_{l} r(l, m) x(l, m)(t) .
$$

Next, using (7) and (8), and writing $x(l, m)=x(l, m)(t), w(l, m)=w(l, m)(t)$,

$$
\begin{aligned}
& \sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} f_{l} r(l, m) w(l, m)=\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} f_{l} r(l, m)\left[x(l, m)-\sum_{p} r(m, p) x(m, p)\right] \\
& \left.\quad=\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} f_{l} r(l, m) x(l, m)-\sum_{m}\left[\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}} f_{l} r(l, m)\right] \sum_{p} r(m, p) x(m, p)\right] \\
& \quad=\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} f_{l} r(l, m) x(l, m)-\sum_{m \in \mathcal{L}, p} f_{m} r(m, p) x(m, p) \\
& \quad=\sum_{l \in \mathcal{L}_{\text {entry }}, m} d_{l} r(l, m) x(l, m)
\end{aligned}
$$

Substitution in (A.4) gives

$$
E\{\alpha \mid X(t)\}=\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m}\left[f_{l} r(l, m)-E\{C(l, m)(t+1) S(l, m)(t) \wedge x(l, m)(t) \mid X(t)\}\right] w(l, m)(t)=\alpha_{1}+\alpha_{2},
$$

with

$$
\begin{aligned}
& \alpha_{1}=\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m}\left[f_{l} r(l, m)-c(l, m) S(l, m)(t)\right] w(l, m)(t) \\
& \alpha_{2}=\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m}[c(l, m)-E\{C(l, m)(t+1) \wedge x(l, m)(t) \mid X(t)\}] S(l, m)(t) w(l, m)(t)
\end{aligned}
$$

Lemma 1. For all $l, m$ and $t$,

$$
\alpha_{2} \leqslant \sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} c(l, m) \bar{C}(l, m),
$$

in which $\bar{C}(l, m)$ is the maximum value of the random service rate $C(l, m)(t)$.

Proof. The function $c \mapsto c \wedge x$ is concave in $c$. Hence by Jensen's inequality

$$
E\{C(l, m)(t+1) \wedge x(l, m)(t) \mid X(t)\} \leqslant E\{C(l, m)(t+1) \mid X(t)\} \wedge x(l, m)(t)=c(l, m) \wedge x(l, m)(t) \leqslant c(l, m),
$$

and since $w(l, m)(t) \leqslant x(l, m)(t)$ and $S(l, m)(t)$ is a 0-1 function of $X(t)$,

$$
\alpha_{2} \leqslant \sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m}[c(l, m)-E\{C(l, m)(t+1) \wedge x(l, m)(t) \mid X(t)\}] S(l, m)(t) x(l, m)(t) .
$$

Now

$$
\begin{aligned}
0 & \leqslant c(l, m)-E\{C(l, m)(t+1) \wedge x(l, m)(t) \mid X(t)\} \\
& =\left\{\begin{array}{ll}
c(l, m)-E\{C(l, m)(t+1) \wedge x(l, m)(t) \mid X(t)\} & \text { if } x(l, m)(t) \leqslant \bar{C}(l, m) \\
0 & \text { if } x(l, m)(t)>\bar{C}(l, m)
\end{array} .\right.
\end{aligned}
$$

It follows that

$$
[c(l, m)-E\{C(l, m)(t+1) \wedge x(l, m)(t) \mid X(t)\}] S(l, m)(t) x(l, m) \leqslant c(l, m) \bar{C}(l, m),
$$

which proves the lemma. $\square$

Lemma 2. If the control policy $u^{*}$ is used and $d \in D^{o}$ there exists $\epsilon>0$ such that

$$
\alpha_{1} \leqslant-\epsilon|X(t)| .
$$

Proof. Let $S^{*}(t)=u^{*}(X(t))$ and $w(l, m)(t)=w(l, m)(X(t))$. By (23)

$$
\sum_{l, m} S^{*}(l, m)(t) c(l, m) w(l, m)(t)=\max _{s \in \mathcal{S}} \sum_{l, m} S(l, m) c(l, m) w(l, m)(t)=\max _{\Sigma \in c(S)} \sum_{l, m} \Sigma(l, m) c(l, m) w(l, m)(t) .
$$

Let $\left\{f_{l}\right\}$ be the flows given by (7) and (8).
By (13), since $d$ is in the interior of $D$, there exist $\epsilon>0$ and $\Sigma^{+} \in \operatorname{co}(\mathcal{S})$ such that $c(l, m) \Sigma^{+}(l, m)>f_{l} r(l, m)+\epsilon$ for all $(l, m)$. Recall that $\Sigma \in \operatorname{co}(\mathcal{S})$ if $0 \leqslant \Sigma \leqslant \Sigma^{+}$. Hence for fixed $t$, there exists $\Sigma \in \operatorname{co}(\mathcal{S})$ such that

$$
\Sigma(l, m) c(l, m)=\left\{\begin{array}{ll}
f_{l} r(l, m)+\epsilon, & \text { if } w(l, m)(t)>0 \\
0, & \text { if } w(l, m)(t) \leqslant 0
\end{array} .\right.
$$

Then

$$
\begin{aligned}
\alpha_{1} & =\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m}\left[f_{l} r(l, m)-S^{*}(l, m)(t) c(l, m)\right] w(l, m)(t) \\
& \leqslant \sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m}\left[f_{l} r(l, m)-\Sigma(l, m) c(l, m)\right] w(l, m)(t) \\
& \left.=-\epsilon \sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} w^{+}(l, m)(t)+\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} f_{l} r(l, m) w^{-}(l, m)(t)\right] \\
& \leqslant-\epsilon|w(l, m)(t)|
\end{aligned}
$$

Above $w^{+}=\max \{w, 0\}$ and $w^{-}=\max \{-w, 0\}$. It is assumed that $f_{l} r(l, m)>\epsilon$, because if $r(l, m)=0$, we simply omit the movement $(l, m)$.

Next, the array $\left\{w(l, m)=x(l, m)-\sum_{p} r(m, p) x(m, p)\right\}$ is a linear function of the array $X=\{x(l, m)\}$. One can show that this function is $1: 1$ using the properties (3)-(6) of the routing probabilities $\{r(l, m)\}$. Hence there exists $\eta>0$ such that

$$
\sum_{l, m}|w(l, m)| \geqslant \eta|X(t)|,
$$

which, together with (A.6) gives

$$
\alpha_{1} \leqslant-\epsilon \eta|X(t)|,
$$

completing the proof of Lemma 2. □
Combining Lemmas 1 and 2 gives the upper bound

$$
E\{\alpha \mid X(t)\} \leqslant-\epsilon|X(t)|+\sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} c(l, m) \bar{C}(l, m) .
$$

A.2. Bound on $\beta$

From (A.1) and (A.2) we have the bounds

$$
|\delta(l, m)| \leqslant \max \left\{\bar{C}(l, m), \sum_{k} \bar{C}(k, l)\right\}, l \in \mathcal{L}, m \in \text { Out }_{l}|\delta(l, m)| \leqslant \max \{\bar{C}(l, m), \bar{d}(l, m)\}, l \in \mathcal{L}_{\text {entry }}, m \in \text { Out }_{l}
$$

in which $\bar{d}(l, m)$ is the maximum value of the random demand $d(l, m)(t+1)$. Let $K$ be the maximum value of all these bounds. Then

$$
\beta=|\delta|^{2} \leqslant M K^{2},
$$

in which $M$ is the total number of queues (or number of movements) in the network.
Lastly, from (A.3), (A.7), and (A.8)

$$
E\left\{\left.X(t+1)\right|^{2}-|X(t)|^{2} \mid X(t)\right\}=E\{2 \alpha+\beta \mid X(t)\} \leqslant-2 \epsilon|X(t)|+M\left(K_{2}+K^{2}\right),
$$

in which $K_{2}$ is defined so that

$$
2 \sum_{l \in \mathcal{L} \cup \mathcal{L}_{\text {entry }}, m} c(l, m) \bar{C}(l, m)=M K_{2} .
$$

This proves (24). $\square$

## Appendix B. Proof of (29)

One simply mimics the proof of (24) in Appendix A with $X(t+1), X(t), \delta$ replaced by $Q X(t+1), Q X(t), Q \delta$ and then $w(l, m)$ will be replaced by $w_{Q}(l, m)$. $\square$

## References

Aboudolas, K., Geroliminis, N., 2013. Perimeter and boundary flow control in multi-reservoir heterogeneous networks. Transportation Research, Part B 55, 265-281.
Aboudolas, K., Papageorgiou, M., Kosmatopoulos, E., 2009a. Store-and-forward based methods for the signal control problem in large-scale congested urban road networks. Transportation Research, Part C 17, 163-174.
Aboudolas, K., Papageorgiou, M., Kouvelas, A., Kosmatopoulos, E., 2009b. A rolling-horizon quadratic-programming approach to the signal control problem in large-scale congested urban road networks. Transportation Research, Part C 17, 680-694.
Allsop, R.E., 1972. Estimating the traffic capacity of a signalized road junction. Transportation Research 6, 245-255.
Dai, J.G., Lin, W., 2005. Maximum pressure policies in stochastic processing networks. Operations Research 53 (2), 197-218.
Diakaki, C., Dinopoulou, V., Aboudolas, K., Papageorgiou, M., Ben-Shabat, E., Seider, E., Leibov, A., 2003. Extensions and new applications of the trafficresponsive urban control strategy. Transportation Research Record 1856, 202-211.
Ekbatani, M.K., Kouvelas, A., Papamichail, I., Papageorgiou, M., 2012. Congestion control in urban networks via feedback gating. Transportation Research, Part B 46, 1393-1403.
Gartner, N.H., Pooran, F.J., Andrews, C.M., 2001. Implementation of the OPAC adaptive control strategy in a traffic signal network. In: IEEE intelligent Transportation Systems Conference Proceedings. Oakland, CA, pp. 195-200.
Giaccone, P., Leonardi, E., Shah. D., 2005. On the maximal throughput of networks with finite buffers and its application to buffered crossbars. In: Proceedings IEEE INFOCOM, vol. 2, pp. 971-980 (March).
Lin, W.H., Lo, H.K., 2008. A robust quasi-dynamic traffic signal control scheme for queue management. In: Proceedings of the 13th International Conference of Hong Kong Society for Transportation Studies. Hong Kong, pp. 37-46.
Lindley, J.A., 2012. Applying systems engineering to implementation of adaptive signal control technology. In: ITS World Congress.
McKeown, N., Varaiya, P., Walrand, J., 1993. Scheduling cells in an input-buffered switch. Electronic Letters 29 (25), 2174-2175.

McKeown, N., Mekkittikul, A., Anantharam, V., Walrand, J., 1999. Achieving 100 percent throughput in an input-queued switch. IEEE Transactions on Communications 47 (8), 1260-1267.
Miller, A.J., 1963. Settings for fixed-cycle traffic signals. Operations Research 14 (4), 373-386.
Mirchandani, P., Head, L., 2001. A real-time traffic signal control system: architecture, algorithms, and analysis. Transportation Research, Part C 9, 415-432.
Neely, M.J., Modiano, E., Rohrs, C.E., 2005. Dynamic power allocation and routing for time-varying wireless networks. IEEE Journal on Selected Areas in Communications 23 (1), 89-103.
Osorio, C., Bierlaire, M., 2008. A multiple model approach for traffic signal optimization in the city of Lausanne. In: Swiss Transport Research Conference [http://www.strc.ch/conferences/2008/2008_Osorio_Bierlaire_TrafficSignalOptimization.pdf](http://www.strc.ch/conferences/2008/2008_Osorio_Bierlaire_TrafficSignalOptimization.pdf) (accessed 15.08.09).
Osorio, C., Bierlaire, M., 2009. An analytic finite capacity queueing network model capturing the propagation of congestion and blocking. European Journal of Operational Research 196, 996-1007.
Papageorgiou, M., Diakaki, C., Dinopoulou, V., Kotsialos, A., Wang, Y., 2003. Review of road traffic control strategies. Proceedings of the IEEE 91 (12), 2043-2067.
Robertson, D.I., Bretherton, R.D., 1991a. Optimizing networks of traffic signals in real time-the SCOOT method. IEEE Transactions on Vehicular Technology 40 (1), 11-15.
Robertson, D.I., Bretherton, R.D., 1991b. Optimizing networks of traffic signals in real time-the SCOOT method. IEEE Transactions on Vehicular Technology 40 (1), 11-15.
Robertson, D.I., Bretherton, R.D., 1991c. Optimizing networks of traffic signals in real time-the SCOOT method. IEEE Transactions on Vehicular Technology 40 (1), 11-15.
Sanchez, R.O., Horowitz, R., Varaiya, P., 2011. Analysis of queue estimation methods using wireless magnetic sensors. Transportation Research Record 2229, 34-45.
Tassiulas, L., Ephremides, A., 1992. Stability properties of constrained queuing systems and scheduling policies for maximum throughput in multihop radio networks. IEEE Transactions on Automatic Control 37 (12), 1936-1948.
Varaiya, P., 2013. The max-pressure controller for arbitrary networks of signalized intersections. In: Ukkusuri, S.V., Ozbay, K. (Eds.), Advances in Dynamic Network Modeling in Complex Transportation Systems, Complex Networks and Dynamic Systems, vol. 2. Springer.
Wong, S.C., Yang, H., 1997. Reserve capacity of a signal-controlled road network. Transportation Research B 31 (5), 397-402.
Wongpiromsarn, T., Uthaicharoenpong, T., Wang, Y., Frazzoli, E., Wang, D., 2012. Distributed traffic signal control for maximum network throughput, May [http://arxiv.org/abs/1205.5938](http://arxiv.org/abs/1205.5938).
Wu, X., Liu, H.X., Gettman, D., 2010. Identification of oversaturated intersections using high-resolution traffic signal data. Transportation Research, Part C 18, 626-638.
Xie, X.-F., Smith, S.F., Lu, L., Barlow, G.J., 2012. Schedule-driven intersection control. Transportation Research, Part C, 168-189.


[^0]:    * Tel.: +1 5106425270.
    E-mail address: varaiya@berkeley.edu

