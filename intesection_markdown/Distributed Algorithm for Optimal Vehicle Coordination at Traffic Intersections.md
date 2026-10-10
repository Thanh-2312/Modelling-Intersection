# Distributed Algorithm for Optimal Vehicle Coordination at Traffic Intersections 

Yuning Jiang* Mario Zanon ** Robert Hult ** Boris Houska *<br>* School of Information Science and Technology, ShanghaiTech University, Shanghai, China (jiangyn, borish@shanghaitech.edu.cn)<br>** Department of Signals and Systems, Chalmers University of Technology, Göteborg, Sweden (mzanon, robert.hult@chalmers.se)


#### Abstract

Automated vehicle coordination can be used to control vehicles across traffic intersections safely and efficiently. This paper proposes a novel parallelizable algorithm, which solves the coordination problem at traffic intersections under a given precedence order by using a tailored variant of the augmented Lagrangian based alternating direction inexact Newton method (ALADIN). Here, each vehicle solves its own optimal control problem and exchanges information about arrivial and departure times at the intersection with its neighbors such that collisions are avoided. We illustrate the performance of ALADIN by analyzing two scenarios, one during rush hour and one at low-traffic conditions.


Keywords: Autonomous Vehicles, Traffic Control, Optimal Control, Distributed Optimization

## 1. INTRODUCTION

Traffic jams are a persistent problem in cities around the world as they account for up to 40\% of the total accidents and 20\% of the fatalities (Chen et al. (2016)). Automated coordination of vehicles at traffic intersection is a technology that aims at regulating the traffic in order to reduce traffic jams (Azimi et al. (2011); Dresner et al. (2004); Steinmetz et al. (2014); Campos et al. (2013); Lee et al. (2012)). Moreover, the coordination of automated vehicles has the potential to dramatically reduce the number of accidents, and improve both energy efficiency and infrastructure utilization. For these reasons, a large research effort has recently been devoted to intersection management and an excellent survey on the state of the art can be found in Chen et al. (2016). In this paper, we focus on fully automated intersections in a distributed framework. For the sake of simplicity, we consider the deterministic case, in which all agents communicate and cooperate with each other. Extensions of our approach to account for e.g. pedestrians with uncertain behaviour are left for future research.

By introducing communication between automated vehicles at an intersection, one obtains a cooperative multiagent system where each vehicle is an agent, which can communicate with its neighbors. The overall coordination problem can be separated into two interdependent problems (Hult et al. (2016)). First, the precedence problem consists in deciding the order in which the vehicles should cross the intersection. Second, an optimal control problem is solved to compute the control actions guaranteeing that all vehicles cross the intersection optimally in the prescribed order and without collision. In this paper, we focus on the second problem assuming that the precedence order is given. The problem is then reduced to a structured optimal control problem. For solving this structured control problem, in practice, a fast and efficient distributed nonlinear programming (NLP) solver is needed. Here, one way to construct such an NLP solver starts by using a sequential quadratic programming (SQP) (Nocedal et al. (2006)) solver. Most of the operations of an SQP method can be parallalized such as the function and derivative evaluation. The QPs are however coupled. In Hult et al. (2016) it is suggested to formulate a bilevel problem comprising decoupled finite horizon optimal control problem with linear dynamics in the lower level, as well as a nonconvex upper level coordination problem. The upper level problem is then solved by using an SQP method. This framework has the advantage that the vehicles only communicate via the upper level, whose optimization variables are parameterizing the time schedule for passing the intersection. A technical disadvantage of this approach, however, is that the lower-level constrained optimization problems have non-differentiable objective values with respect to the upper-level parameters-a general problem in bilevel optimization. Of course, one could try to apply heuristics or systematic methods from the field of bilevel optimization or mathematical programming with equilibrium constraints (Bard (1999); Facchinei (1999)), which can deal with this issue. However, an empirical observation with such heuristics is that they are hard to tune often leading to quite non-reliable solvers. Another path, which is followed in the current paper, is to avoid bilevel structures completely by developing tailored distributed optimization solvers. More precisely, this paper uses a variant of the alternating direction augmented Lagrangian based inexact Newton method (ALADIN), which has originally been proposed in Houska et al. (2016). In contrast to Dual Decomposition (Necoara et al. (2008)) and ADMM (Boyd et al. (2011)), which can deal with convex optimization problems only, ALADIN can be applied to nonconvex optimization problems, too. Initial
attempts to apply ALADIN in the context of nonlinear optimal control can be found in Kouzoupis et al. (2016).

This paper is structured as follows. Section 2 discusses how to formulate and discretize optimal traffic control problems. The main contribution of this paper is presented in Section 3, which proposes a tailored ALADIN algorithm for solving this control problem in a distributed way. Similar to the approach by Hult et al. (2016) the vehicles communicate their time schedules only, but the proposed algorithm avoids bilevel problems and, more importantly, reduces the communication overhead. Section 4 illustrates the performance of the proposed method for two scenarios one during rush hour the other during low-traffic conditions. Section 5 concludes the paper.

Notation: The notation $\mathbb{Z}_{z_{1}}^{z_{2}}=\left\{z \in \mathbb{Z} \mid z_{1} \leq z \leq z_{2}\right\}$ is used to denoted integer ranges.

## 2. OPTIMAL TRAFFIC CONTROL

This section discusses how to model and control the traffic at intersection by using distributed optimization.

![](https://cdn.mathpix.com/cropped/a5a85b4d-8a77-4082-9233-da48ac6c3a37-2.jpg?height=633&width=882&top_left_y=1147&top_left_x=137)
Fig. 1. Illustration of the intersection problem. The central square area corresponds to the zone where collisions may occur.

### 2.1 Continuous-time model

One of the simplest possible differential equations for modeling vehicles is a linear system of the form

$$
\dot{x}_{i}(t)=A x_{i}(t)+B u_{i}(t), A=\left(\begin{array}{ll}
0 & 1 \\
0 & 0
\end{array}\right), B=\binom{0}{1},
$$

where $x_{i}(t)=\left(p_{i}(t), v_{i}(t)\right)^{\top}$ denotes the position and velocity of the $i$-th vehicle and $u_{i}(t)$ a control input at time $t$. Let $t_{i}^{\text {in }}$ denote the time at which vehicle $i$ enters the intersection and $t_{i}^{\text {out }}$ the time when it leaves the intersection. A simple collision avoidance strategy can be implemented by enforcing constraints of the form

$$
p_{i}\left(t_{i}^{\text {in }}\right)=d_{i}^{\text {in }}, p_{i}\left(t_{i}^{\text {out }}\right)=d_{i}^{\text {out }}, t_{i}^{\text {out }} \leq t_{i+1}^{\text {in }} .
$$

Here, as shown in Figure 1, $\left[d_{i}^{\text {in }}, d_{i}^{\text {out }}\right] \subseteq \mathbb{R}$ denotes the intersection interval. Note that this constraint structure is based on the assumption that the precedence order of the vehicles is pre-determined, i.e., vehicle $i$ has to pass the intersection before vehicle $i+1$. The traffic control problem of our interest can now be written in the form

$$
\begin{aligned}
& \min _{x, u, T} \sum_{i=1}^{M} \frac{1}{t_{i}^{\text {out }}} \int_{0}^{t_{i}^{\text {out }}}\left\|x_{i}(t)-x_{i}^{\text {ref }}\right\|_{Q_{i}}^{2}+\left\|u_{i}(t)\right\|_{R_{i}}^{2} \mathrm{~d} t \\
& \text { s.t. }\left\{\begin{array}{l}
\forall i \in \mathbb{Z}_{1}^{M}, \forall t \in\left[0, t_{i}^{\text {out }}\right], \\
\dot{x}_{i}(t)=A x_{i}(t)+B u_{i}(t), \\
C_{i} x_{i}(t)+D_{i} u_{i}(t)+b_{i} \leq 0, \\
x_{i}(0)=\hat{x}_{i}, \\
{\left[x_{i}\left(t_{i}^{\text {in }}\right)\right]_{1}=d_{i}^{\text {in }},\left[x_{i}\left(t_{i}^{\text {out }}\right)\right]_{1}=d_{i}^{\text {out }},} \\
t_{i}^{\text {out }} \leq t_{i+1}^{\text {in }} .
\end{array}\right.
\end{aligned}
$$

Here, the time points $T=\left(T_{1}, \ldots, T_{M}\right), T_{i}=\left(t_{i}^{\text {in }}, t_{i}^{\text {out }}\right)$, at which the vehicles enter or leave the intersection are free optimization variables. Moreover, throughout this paper, we consider quadratic tracking objectives with given weighting matrices $Q_{i} \in \mathbb{R}_{+}^{2 \times 2}$ and $R_{i} \in \mathbb{R}_{+}$and reference $x_{i}^{\text {ref }}$. Notice that the objective contribution of all vehicles is scaled by $t_{i}^{\text {out }}$ such that the vehicles have no incentive to speed-up in order to reduce their contribution to the overall objective value. As an alternative, one could also augment the problem formulation (2) with quadratic end-cost terms in order to take an approximation of the infinite-horizon cost into account. The initial positions and velocities of all vehicles, denoted by $\hat{x}_{i}$, are assumed to be given, too. The matrices $C_{i} \in \mathbb{R}^{n \times 2}$ and vectors $D_{i}, b_{i} \in \mathbb{R}^{n}$ can be used to model position, velocity, and acceleration constraints.

Notice that at larger intersections, especially during rush hours, there may be hundreds of automated vehicles passing in a relatively short time window. In such scenarios $M$ is large and the collision avoidance constraints of the form $t_{i}^{\text {out }} \leq t_{i+1}^{\text {in }}$ introduce a coupling. This constraint requires communication and coordination between the vehicles. In this context, another principal challenge is that in a practical scenario there is an inflow of new vehicles entering the neighborhood of the intersection while other vehicles are leaving this region again. However, it would be unnatural to pick one selected vehicle to act as a central unit, since this vehicle might leave the neighborhood of the intersection soon afterwards. Consequently, the focus of this paper is on solving (2) in a distributed way, where each vehicle optimizes its own trajectory and communicates with its neighbors only.

### 2.2 Discretization

In order to discretize (2) a direct single shooting method with piecewise constant control discretization is applied (Sargent et al. (1978)). Here, we denote by

$$
h_{k}\left(T_{i}\right)= \begin{cases}\frac{t_{i}^{\mathrm{in}}}{N_{i}^{1}}, & \text { if } k<N_{i}^{1} \\ \frac{t_{i}^{\text {out }}-t_{i}^{\text {in }}}{N_{i}-N_{i}^{1}}, & \text { otherwise }\end{cases}
$$

the length of the shooting intervals with the number of discretization intervals $N_{i}^{1}$ and $N_{i}-N_{i}^{1}$. Notice that the differential equations for the vehicles can be solved explicitly, i.e., no numerical integration is needed. The
solution of differential equation (1) at the shooting nodes is given by the explicit expression

$$
\xi_{i, k}\left(a_{i}, T_{i}\right)=\mathcal{G}_{k, 0}\left(T_{i}\right) \hat{x}_{i}+\sum_{j=1}^{k} \mathcal{G}_{k, j}\left(T_{i}\right) \mathcal{B}_{j}\left(t_{i}\right) a_{i, j},
$$

where $a_{i, k}$ denotes the control discretization parameters,

$$
\mathcal{G}_{k+1, j}\left(T_{i}\right)=\left(\begin{array}{cc}
1 & h_{k}\left(T_{i}\right) \\
0 & 1
\end{array}\right) \mathcal{G}_{k, j}\left(T_{i}\right) \quad \text { with } \quad \mathcal{G}_{j, j}\left(T_{i}\right)=I
$$

for all indices $k, j, k \geq j$, and

$$
\mathcal{B}_{j}\left(T_{i}\right)=\binom{0.5 h_{j}\left(T_{i}\right)^{2}}{h_{j}\left(T_{i}\right)^{2}} .
$$

A discrete-time approximation of (2) is now given by

$$
\begin{array}{ll}
\min _{a, t} & \sum_{i=1}^{M} \frac{1}{t_{i}^{\text {out }}}\left\{\sum_{k=0}^{N_{i}-1} \ell_{i, k}\left(a_{i}, T_{i}\right)\right\} \\
\text { s.t. } & \left\{\begin{array}{l}
\forall k \in \mathbb{Z}_{0}^{N_{i}}, \forall i \in \mathbb{Z}_{1}^{M}, \\
C_{i} \xi_{i, k}\left(a_{i}, T_{i}\right)+D_{i} a_{i, k}+b_{i} \leq 0, \\
{\left[\xi_{i, N_{i}^{1}}\left(a_{i}, T_{i}\right)\right]_{1}=d_{i}^{\text {in }},} \\
{\left[\xi_{i, N_{i}}\left(a_{i}, T_{i}\right)\right]_{1}=d_{i}^{\text {out }},} \\
t_{i}^{\text {out }} \leq t_{i+1}^{\text {in }},
\end{array}\right.
\end{array}
$$

where $\left[\xi_{i, k}\left(a_{i}, T_{i}\right)\right]_{1}$ denotes the first component of the vector $\xi_{i, k}\left(a_{i}, T_{i}\right)$ corresponding to the discrete-time position of the $i$-th vehicle. Here, the objective function can be found by by working out an explicit expression for the integrals in the objective of (2). They are given by

$$
\begin{aligned}
\ell_{i, k}\left(a_{i}, T_{i}\right)= & \left(\begin{array}{c}
\xi_{i, k}\left(a_{i}, T_{i}\right) \\
a_{i, k} \\
1
\end{array}\right)^{\top}\left(\begin{array}{lll}
\mathcal{Q}_{k}\left(T_{i}\right) & \mathcal{S}_{k}\left(T_{i}\right) & q_{k}\left(T_{i}\right) \\
\mathcal{S}_{k}\left(T_{i}\right)^{\top} & \mathcal{R}_{k}\left(T_{i}\right) & r_{k}\left(T_{i}\right) \\
q_{k}\left(T_{i}\right)^{\top} & r_{k}\left(T_{i}\right)^{\top} & 0
\end{array}\right) \\
& *\left(\begin{array}{c}
\xi_{i, k}\left(a_{i}, T_{i}\right) \\
a_{i, k} \\
1
\end{array}\right),
\end{aligned}
$$

with shorthands

$$
\begin{aligned}
\mathcal{Q}_{k}\left(T_{i}\right)= & \frac{h_{k}\left(T_{i}\right)^{3}}{3} A^{\top} Q_{i} A+\frac{h_{k}\left(T_{i}\right)^{2}}{2}\left(A^{\top} Q_{i}+Q_{i} A\right) \\
& +h_{k}\left(T_{i}\right) Q_{i}
\end{aligned}
$$

$$
\mathcal{R}_{k}\left(T_{i}\right)=\frac{h_{k}\left(T_{i}\right)^{5}}{20} B^{\top} A^{\top} Q_{i} A B+\frac{h_{k}\left(T_{i}\right)^{4}}{8} B^{\top} A^{\top} Q_{i} B
$$

$$
\begin{aligned}
\mathcal{S}_{k}\left(T_{i}\right)= & \frac{h_{k}\left(T_{i}\right)^{4}}{8} A^{\top} Q_{i} A B+\frac{h_{k}\left(T_{i}\right)^{3}}{6} Q_{i} A B \\
& +\frac{h_{k}\left(T_{i}\right)^{3}}{3} A^{\top} Q_{i} B+\frac{h_{k}\left(T_{i}\right)^{2}}{2} Q_{i} B .
\end{aligned}
$$

and

$$
\begin{aligned}
& q_{k}\left(T_{i}\right)=-\frac{h_{k}\left(T_{i}\right)^{2}}{2} A^{\top} Q_{i} x_{i}^{\mathrm{ref}}-h_{k}\left(T_{i}\right) Q_{i} x_{i}^{\mathrm{ref}}, \\
& r_{k}\left(T_{i}\right)=-\frac{h_{k}\left(T_{i}\right)^{3}}{6} B^{\top} A^{\top} Q_{i} x_{i}^{\mathrm{ref}}-\frac{h_{k}\left(T_{i}\right)^{2}}{2} B^{\top} Q_{i} x_{i}^{\mathrm{ref}},
\end{aligned}
$$

Remark 1. The discrete-time mixed state-control constraint in (4) only enforces approximate feasibility of the original continuous-time optimal control problem in the sense that the trajectory $x_{i}(t)$ might violate the constraint between the shooting nodes. However, the constraint violation converges to 0 if $N_{i}^{1} \rightarrow \infty$ and $N_{i}-N_{i}^{1} \rightarrow \infty$. Moreover, even if we use a broad discretization, we know that $x_{i}(t)$ is for our control discretization a piecewise quadratic function for which an explicit expression can be found. Thus, in principle, it is possible to simply redefine the constraint vectors $b_{i}$ by adding a small margin that depends on $N_{i}^{1}$ and $N_{i}-N_{i}^{1}$ such that feasibility of the continuous-time trajectory can be guaranteed in a mathematically rigorous way.

### 2.3 Reformulation as a Distributed Problem

In order to solve (4) by a distributed optimization algorithm, the auxiliary variables $t_{i}^{\mathrm{c}}$ are introduced such that

$$
t_{i}^{\mathrm{c}}=t_{i+1}^{\mathrm{in}}, \forall i \in \mathbb{Z}_{1}^{M-1} .
$$

The coupled time constraints can be then be written in the form

$$
t_{i}^{\mathrm{c}}=t_{i+1}^{\text {in }}, t_{i}^{\text {out }} \leq t_{i}^{\mathrm{c}}, \forall i \in \mathbb{Z}_{1}^{M-1} .
$$

In the following, we introduce new stacked time variables $\tau_{i}=\left(t_{i}^{\text {in }}, t_{i}^{\text {out }}, t_{i}^{\mathrm{c}}\right)$. Next, we introduce the shorthands

$$
\begin{aligned}
& L_{i}\left(a_{i}, \tau_{i}\right)=\frac{1}{t_{i}^{\text {out }}} \sum_{k=0}^{N_{i}-1} \ell_{i, k}\left(a_{i},\left(t_{i}^{\text {in }}, t_{i}^{\text {out }}\right)\right) \\
& G_{i}\left(a_{i}, \tau_{i}\right)=\left\{\begin{array}{l}
\forall k \in \mathbb{Z}_{0}^{N_{i}-1}, \\
C_{i} \xi_{i, k}\left(a_{i},\left(t_{i}^{\text {in }}, t_{i}^{\text {out }}\right)\right)+D_{i} a_{i, k}+b_{i}, \\
u_{\min }-a_{i, k}, k \in \mathbb{Z}_{0}^{N_{i}-1}, \\
a_{i, k}-u_{\max }, k \in \mathbb{Z}_{0}^{N_{i}-1}, \\
t_{i}^{\text {out }}-t_{i}^{\mathrm{c}},
\end{array}\right. \\
& F_{i}\left(a_{i}, \tau_{i}\right)=\left\{\begin{array}{l}
{\left[\xi_{i, N_{i}^{1}}\left(a_{i},\left(t_{i}^{\text {in }}, t_{i}^{\text {out }}\right)\right)\right]_{1}-d_{i}^{\text {in }},} \\
{\left[\xi_{i, N_{i}}\left(a_{i},\left(t_{i}^{\text {in }}, t_{i}^{\text {out }}\right)\right)\right]_{1}-d_{i}^{\text {out }} .}
\end{array}\right.
\end{aligned}
$$

as well as

$$
\Phi_{i}\left(\tau_{i}\right)=\min _{a_{i}} L_{i}\left(a_{i}, \tau_{i}\right) \quad \text { s.t. } \quad\left\{\begin{array}{l}
F_{i}\left(a_{i}, \tau_{i}\right)=0 \\
G_{i}\left(a_{i}, \tau_{i}\right) \leq 0
\end{array} .\right.
$$

Here, an extended value notation is used; that is, $\Phi_{i}$ takes the value $+\infty$ if the constraints in the above minimization problem are infeasible. By using this notation NLP (4) can be written in the equivalent form

$$
\begin{aligned}
\min _{\tau} & \sum_{i=1}^{M} \Phi_{i}\left(\tau_{i}\right) \\
\text { s.t. } & t_{i}^{\mathrm{c}}=t_{i+1}^{\mathrm{in}} \quad \mid \lambda_{i} \quad, i \in \mathbb{Z}_{1}^{M-1} .
\end{aligned}
$$

Here, $\lambda_{i} \in \mathbb{R}$ denotes the multiplier of the $i$-th coupling constraint. Note that the above problem is written in the
form of a bilevel optimization problem, since the separable objective functions $\Phi_{i}$ can only be evaluated by solving (decoupled) optimization problems.

## 3. DISTRIBUTED TRAFFIC CONTROL ALGORITHM

This section proposes a distributed traffic control algorithm based on a variant of ALADIN (Houska et al. (2016)). Algorithm 1 outlines the main steps for solving problem (13). Notice that the main primal and dual iterates are denoted by $\left(z_{i}, a_{i}\right)$ and $\lambda_{i}$. In practice, we initialize $\lambda$ with 0 while the initialization of $z$ is based on an initial estimate of the time schedule. Notice that Step 1 and 2 are completely parallelizable, but Step 3 requires communication. However, fortunately, the QP in Step 3 can be solved by communicating between neighboring vehicles only as explained further below.

Algorithm 1 Distributed Traffic Control Algorithm
Input: Initial guess $z$ and $\lambda$, tuning parameter $\rho$.
Repeat:
(1) Each vehicle solves
$$
\begin{aligned}
\min _{a_{i}, \tau_{i}} & L_{i}\left(a_{i}, \tau_{i}\right)-\lambda_{i-1} t_{i}^{\mathrm{in}}+\lambda_{i} t_{i}^{\mathrm{c}}+\frac{\rho}{2}\left\|\tau_{i}-z_{i}\right\|^{2} \\
\text { s.t. } & G_{i}\left(a_{i}, \tau_{i}\right) \leq 0 \quad \text { and } \quad F_{i}\left(a_{i}, \tau_{i}\right)=0 .
\end{aligned}
$$
(2) Each vehicle chooses $H_{i} \succ 0$ and computes
$$
g_{i}=\rho\left(z_{i}-\tau_{i}\right)+\left(\lambda_{i-1}, 0,-\lambda_{i}\right)^{\top} .
$$
(3) All vehicles solve the equality constrained QP
$$
\min _{\Delta \tau} \sum_{i=1}^{M} \frac{1}{2} \Delta \tau_{i}^{\top} H_{i} \Delta \tau_{i}+g_{i}^{\top} \Delta \tau_{i}
$$
$$
\begin{array}{ll}
\text { s.t. } & t_{i}^{\mathrm{c}}+\Delta t_{i}^{\mathrm{c}}=t_{i+1}^{\mathrm{in}}+\Delta t_{i+1}^{\mathrm{in}} \mid \lambda_{i}^{\mathrm{QP}}, i \in \mathbb{Z}_{1}^{M-1} \\
& t_{i}^{\text {out }}+\Delta t_{i}^{\text {out }}=t_{i}^{\mathrm{c}}+\Delta t_{i}^{\mathrm{c}}, i \in \mathbb{A}
\end{array}
$$
together by communicating with each other.
(4) Each vehicle updates $z_{i} \leftarrow \tau_{i}+\Delta \tau_{i}$ and $\lambda_{i} \leftarrow \lambda_{i}^{\mathrm{QP}}$.

### 3.1 Decoupled Optimal Control Problems

In Step 1 of Algorithm 1 the decoupled discrete-time optimal control problems

$$
\begin{aligned}
\min _{a_{i}, \tau_{i}} & L_{i}\left(a_{i}, \tau_{i}\right)-\lambda_{i-1} t_{i}^{\text {in }}+\lambda_{i} t_{i}^{\mathrm{c}}+\frac{\rho}{2}\left\|\tau_{i}-z_{i}\right\|^{2} \\
\text { s.t. } & G_{i}\left(a_{i}, \tau_{i}\right) \leq 0 \quad \text { and } \quad F_{i}\left(a_{i}, \tau_{i}\right)=0 .
\end{aligned}
$$

have to be solved, which can be done separately onboard each vehicle and in parallel by using any suitable NLP solver, e.g., an SQP method.

Notice that if (for a given vehicle $i$ ) the function $\Phi_{i}$ is differentiable at the solution $\tau_{i}$ of the above decoupled NLP, then the vector $g_{i}$ in Step 2 is such that $g_{i}=$ $\nabla \Phi_{i}\left(\tau_{i}\right)$, which can be proven by working out the first order KKT optimality condition of the above optimization problem. Thus, Algorithm 1 coincides with the original ALADIN algorithm from Houska et al. (2016) applied to (13). However, notice that the function $\Phi_{i}$ is not differentiable in general and, consequently, the above derivative-free ALADIN variant is preferable in such scenarios. In addition, if $\Phi_{i}$ is twice differentiable at $\tau_{i}$, we may choose a positive definite $H_{i}$ such that $H_{i} \approx$ $\nabla^{2} \Phi_{i}\left(\tau_{i}\right)$ in order to improve the local convergence rate. However, also other scaling matrices can be used. The tuning parameter $\rho$ should be sufficiently large as discussed in more detail in Houska et al. (2016).

The local convergence proof from Houska et al. (2016) can be applied one-to-one in order to establish local convergence of Algorithm 1 under the assumption that the mininizer is regular KKT point. On the other hand, Algorithm 1 might not converge, if it is initialized far away from a locally optimal solution, but in this case ALADIN can be augmented with line search routines that guarantee convergence to local minimizers from any starting point for sufficiently large $\rho$ as discussed in Houska et al. (2016), too.

### 3.2 Communication Step

The arguably most critical step of Algorithm 1 is Step 3, where a coupled QP of the form

$$
\begin{array}{ll}
\min _{\Delta \tau} & \sum_{i=1}^{M} \frac{1}{2} \Delta \tau_{i}^{\top} H_{i} \Delta \tau_{i}+g_{i}^{\top} \Delta \tau_{i} \\
\text { s.t. } & t_{i}^{\mathrm{c}}+\Delta t_{i}^{\mathrm{c}}=t_{i+1}^{\text {in }}+\Delta t_{i+1}^{\text {in }} \quad \mid \lambda_{i}^{\mathrm{QP}}, i \in \mathbb{Z}_{1}^{M-1} \\
& t_{i}^{\text {out }}+\Delta t_{i}^{\text {out }}=t_{i}^{\mathrm{c}}+\Delta t_{i}^{\mathrm{c}}, i \in \mathbb{A}
\end{array}
$$

has to be solved. Here, $\mathbb{A}$ denotes the set of indices for which the constraint $t_{i}^{\text {out }} \leq t_{i}^{c}$ is strictly active at the optimal solution of the decoupled optimal control problems.

Notice that the above QP is always feasible and bandstructured, i.e., the solution of this QP can be found by a dynamic programming recursion (Bertsekas (2012)) starting with last vehicle $i=N$ and passing a quadratic cost-to-go function backwards, from vehicle $i$ to vehicle $i-1$ until the first vehicle is reached. Next, the first vehicle knows the solution and passes it to second vehicle, and so on, until all vehicles know the solution of the above QP. By working out the dynamic programming recursion in detail, it turns our that in total only 2 floating point numbers need to be passed from vehicle $i$ to vehicle $i-1$ and another single floating point number is passed back from vehicle $i-1$ to vehicle $i$. Thus, the communication overhead compared to centralized methods such as SQP is reduced significantly.

### 3.3 Termination

Algorithm 1 should be terminated as soon as all vehicles agree on a collision-free and locally optimal time schedule. Here, a suitable termination criterion is given by

$$
\max _{i}\left|t_{i}^{\mathrm{c}}-t_{i+1}^{\mathrm{in}}\right| \leq \epsilon \quad \text { and } \quad\|\tau-z\|_{\infty} \leq \epsilon
$$

for a user-specified tolerance $\epsilon$, see Houska et al. (2016). Checking this condition requires additional communication between the vehicles, however, as they need to agree on when to stop iterating.

![](https://cdn.mathpix.com/cropped/a5a85b4d-8a77-4082-9233-da48ac6c3a37-5.jpg?height=585&width=806&top_left_y=279&top_left_x=146)
Fig. 2. Scenario 1: optimal positions of all vehicles in dependence on time. The intersection area, where the collision avoidance constraints have to be satisfied, is highlighted by the black dashed lines.

## 4. NUMERICAL RESULT

In this section, we illustrate the performance of Algorithm 1 for two scenarios, one during rush hour and one at low-traffic conditions. Actually, the proposed algorithm can solve traffic coordination problems within milliseconds and scales up easily to hundreds of vehicles, as it is fully distributed. However, for illustration purposes, we show in the current paper scenarios that involve 10 vehicles only, such that we can reasonably plot the solution. In both scenarios, the intersection is defined by $d_{i}^{\mathrm{in}}=0 \mathrm{~m}$ and $d_{i}^{\text {out }}=10 \mathrm{~m}$. Control constraints of the form $-2.0 \frac{\mathrm{~m}}{\mathrm{~s}^{2}} \leq$ $u(t) \leq 2.0 \frac{\mathrm{~m}}{\mathrm{~s}^{2}}$ are enforced. The weighting matrices are set to

$$
Q_{i}=\left(\begin{array}{cc}
0 \frac{1}{\mathrm{~m}^{2}} & 0 \frac{\mathrm{~s}}{\mathrm{~m}^{2}} \\
0 \frac{\mathrm{~s}}{\mathrm{~m}^{2}} & 1 \frac{\mathrm{~s}^{2}}{\mathrm{~m}^{2}}
\end{array}\right), R_{i}=1 \frac{\mathrm{~s}^{4}}{\mathrm{~m}^{2}},
$$

such that there are no position references needed, as the corresponding entries in the $Q_{i}$ s are set to 0. The reference for the velocities of the vehicles is set to

$$
v^{\mathrm{ref}}=(80,80,65,70,70,60,70,75,80,85)^{\top} \mathrm{km} / \mathrm{h}
$$

during Scenario 1 and to

$$
v^{\mathrm{ref}}=(80,80,75,70,70,75,80,75,75,75)^{\top} \mathrm{km} / \mathrm{h}
$$

during Scenario 2. Additionally, we set $N_{i}^{1}=20$ and $N_{i}=25$ for all vehicles. The termination tolerance is set to $\epsilon=10^{-8}$ and we use $\rho=250$ for Scenario 1 (rush hour) and $\rho=1$ for Scenario 2 (lower traffic conditions). The algorithm is implemented in Julia-0.4.6. The primal iterates are initialized with the decoupled optimal solution that is obtained without any communication by not enforcing the collision avoidance constraints.

### 4.1 Optimal trajectories

Figure 2 and Figure 3 show the numerical results for the position trajectories for Scenario 1 and 2, respectively. For the rush hour scenario (Scenario 1) the initial states are

![](https://cdn.mathpix.com/cropped/a5a85b4d-8a77-4082-9233-da48ac6c3a37-5.jpg?height=583&width=806&top_left_y=281&top_left_x=1067)
Fig. 3. Scenario 2: same as Scenario 1 but with different initial vehicle positions.

![](https://cdn.mathpix.com/cropped/a5a85b4d-8a77-4082-9233-da48ac6c3a37-5.jpg?height=628&width=825&top_left_y=1005&top_left_x=1085)
Fig. 4. Convergence of the residuals of the coupling constraints, the difference between the local primal solution and primal iterates, as well as the $\infty$-norm of the KKT residuals. First row: Scenario 1 (rush hour); second row: Scenario 2 (low-traffic conditions).

set in such a way that all vehicles would collide in the intersection area if collision avoidance constraints would not be enforced. In Scenario 2 the situation is somewhat more relaxed and only a few of the collision constraints are active in the optimal solution.

### 4.2 Convergence

The upper left part of Figure 4 shows the progress of the residuals of the coupling constraints, $\max \left|t_{i}^{\text {in }}-t_{i+1}^{\text {out }}\right|$, and the difference between the local solution and the primal iterates $\|\tau-z\|_{\infty}$, versus the iteration index of the main loop of Algorithm 1 for Scenario 1. The upper right part of Figure 4 shows the $\infty$-norm of the violation of the first order necessary KKT optimilaty conditions of problem (13), denoted by $\|r\|_{\infty}$. The lower left and the lower right parts of Figure 4 show the same but for Scenario 2. Notice that Algorithm 1 needs more iterations during rush hour (Scenario 1) as the collision avoidance constraints are much more difficult to satisfy. However, in both case the proposed algorithm converges
reliably to a locally optimal solution. Also notice that a locally quadraric convergence rate can be observed for all scenarios, as exact Hessian approximations were used. Notice that for accuracies less than $10^{-10}$ the algorithm iterates on rounding errors that are due to the finite precision arithmetic.

4.3 Comparison versus SQP
![](https://cdn.mathpix.com/cropped/a5a85b4d-8a77-4082-9233-da48ac6c3a37-6.jpg?height=302&width=841&top_left_y=585&top_left_x=146)

Fig. 5. Convergence of the difference between the primal iterates and optimal solutions: SQP versus Algorithm 1. Left: Scenario 1; Right: Scenario 2.
Figure 5 compares the convergence of $\left\|z-\tau^{*}\right\|_{\infty}$ of Algorithm 1 with a standard SQP algorithm indicating that the proposed method needs fewer iterations to converge. However, the main advantage of Algorithm 1 compared to SQP is that it is fully distributed and that the communication overhead is reduced significantly.

## 5. CONCLUSIONS

This paper has presented a distributed optimization algorithm for solving traffic coordination problems at intersections under the assumption that the precedence order is given. The algorithm is based on a variant of ALADIN that has been tailored for traffic coordination problems, which are non-convex with respect to the parameterization of the time schedule. The performance of the method has been illustrated by applying it to a problem with 10 vehicles for different scenarios finding that the proposed algorithm converges reliably. Generally, in more strongly coupled scenarios, e.g., during rush hour, many collision avoidance constraints may become active and the optimization problem is more challenging to solve. Future work will investigate the robustness of the method with respect to communication failures as well as extensions of the proposed algorithm for real-time model predictive control scenarios.

## ACKNOWLEDGEMENTS

The work of Yuning Jiang and Boris Houska was supported by the National Science Foundation China (NSFC), Nr. 61473185, as well as ShanghaiTech University, Grant-Nr. F-0203-14-012. The work of Mario Zanon and Robert Hult was supported by the Swedish Research Council (VR) under grant number 2012-4038 and the European Commission Seventh Framework under the AdaptIVe, grant agreement number 610428.

## REFERENCES

S.R. Azimi, G. Bhatia, R. Rajkumar, and P. Mudalige. Vehicular networks for collision avoidance at intersections. SAE International Journal of Passenger Cars -Mechanical Systems, 4(1):406-416, 2011. J.F. Bard. Practical Bilevel Optimization: Algorithms and Applications. Kluwer Academic Publishers, Boston MA, 1999.
D. Bertsekas. Dynamic Programming and Optimal Control. Athena Scientific Dynamic Programming and Optimal Control, 2012.
S. Boyd, N. Parikh, E. Chu, B. Peleato, J. Eckstein. Distributed optimization and statistical learning via the alternating direction method of multipliers. Foundations and Trends in Machine Learning, 3(1):1-122, 2011.
G. R. de Campos, P. Falcone, and J. Sjoberg. Autonomous cooperative driving: A velocity-based negotiation approach for intersection crossing. In Intelligent Transportation Systems - (ITSC), 2013 16th International IEEE Conference on, pages 1456-1461, 2013.
L. Chen and C. Englund. Cooperative Intersection Management: A Survey. In IEEE Transactions on Intelligent Transportation Systems, pages 570-586, Feb 2016.
K. Dresner and P. Stone. Multiagent traffic management: A reservation-based intersection control mechanism. In The Third International Joint Conference on Autonomous Agents and Multiagent Systems, pages 530-537, July 2004.
F. Facchinei, H. Jiang, L. Qi. A smoothing method for mathematical programs with equilibrium constraints. Mathematical Programming, 85(1):107-134, 1999.
R. Hult, M. Zanon, S. Gros, and P. Falcone. Primal Decomposition of the Optimal Coordination of Vehicles at Traffic Intersections. In Proceedings of the 55th IEEE Conference on Decision and Control, 2016.
B. Houska, J. Frasch, M. Diehl. An Augmented Lagrangian Based Algorithm for Distributed Non-Convex Optimization. SIAM Journal on Optimization, Volume 26(2), pages 1101-1127, 2016.
D. Kouzoupis, R. Quirynen, B. Houska, M. Diehl. A block based ALADIN scheme for highly parallelizable direct optimal control. In Proceedings of the 2016 American Control Conference, Boston, USA, 2016.
J. Lee and B. Park. Development and evaluation of a cooperative vehicle intersection control algorithm under the connected vehicles environment. IEEE Transactions on Intelligent Transportation Systems, 13(1):81-90, 2012.
I. Necoara, J.A.K. Suykens. Application of a smoothing technique to decomposition in convex optimization. IEEE Transactions on Automatic Control, 53(11):2674-2679, 2008.
J. Nocedal and S. J. Wright. Numerical Optimization. Springer, 2nd edition, 2006.
E. Steinmetz, R. Hult, G. Rodrigues de Campos, M. Wildemeersch, P. Falcone, and H. Wymeersch. Communication analysis for centralized intersection crossing coordination. In Wireless Communications Systems (ISWCS), 2014 11th International Symposium on, pages 813-818, Aug 2014.
R.W.H. Sargent and G.R. Sullivan. The development of an efficient optimal control package. In J. Stoer, editor, Proceedings of the 8th IFIP Conference on Optimization Techniques (1977), Part 2, Heidelberg, 1978. Springer

