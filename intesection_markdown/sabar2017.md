# A memetic algorithm for real world multi-intersection traffic signal optimisation problems 

Nasser R. Sabar ${ }^{\mathrm{a}, *}$, Le Minh Kieu ${ }^{\mathrm{a}}$, Edward Chung ${ }^{\mathrm{a}}$, Takahiro Tsubota ${ }^{\mathrm{b}}$, Paulo Eduardo Maciel de Almeida ${ }^{\text {c }}$<br>${ }^{\mathrm{a}}$ Smart Transport Research Centre, Queensland University of Technology, QLD 4001 Brisbane, Australia<br>${ }^{\mathrm{b}}$ Department of Civil and Environmental Engineering, Faculty of Engineering, Ehime University, 3 Bunko-cho Matsuyama, Ehime 790-8577, Japan<br>${ }^{\mathrm{c}}$ Federal Center for Technological Education of Minas Gerais State, Av. Amazonas, 7675, Belo Horizonte 30510-000, Brazil

## ARTICLE INFO

Article history:
Received 16 September 2016
Received in revised form
19 April 2017
Accepted 25 April 2017

Keywords:
Traffic signal optimisation
Dynamic optimisation
Meta-heuristics
Traffic control


#### Abstract

Traffic signals play a significant role in the urban transportation system. They control the movement of traffic on urban streets by determining the appropriate signal timing settings. Due to the stochastic nature of the traffic flow, deciding on the best signal timing settings is a computationally complex problem, with the result that traditional analytical methods have been found to be inadequate in dealing with real world scenarios. This issue has already been tackled using computational intelligence algorithms such as the genetic algorithm (GA). However, despite good results, GA may experience slow convergence, especially when dealing with constrained optimisation problems. To address this issue, we propose an adaptive memetic algorithm (MA) for optimising signal timings in real world urban road networks using traffic volumes derived from induction loop detectors. The proposed MA combines the strengths of GA with the exploitation power of a local search algorithm, in an adaptive manner, so as to accelerate the search process and generate high quality solutions. In this work, we propose two important techniques for improving the performance of a traditional MA. First, we use a systematic neighbourhood based simple descent algorithm as a local search to effectively exploit the search space around GA solutions. Second, to achieve a proper balance between the exploration of GA and the local search algorithm, we propose an indicator scheme to control the local search application based on the diversity and the quality of the search process. The proposed MA was tested in two different case studies for the cities of Brisbane, Australia, and Plock, Poland, using the well-known microscopic traffic simulator, AIMSUN. Results demonstrate that our MA is better than GA and traditional fixed-time traffic signal settings.


Crown Copyright © 2017 Published by Elsevier Ltd. All rights reserved.

## 1. Introduction

The efficient operation of traffic signals is essential to the urban transportation system (Hunt et al., 1982). Traffic signals govern the movement of traffic on urban streets by manipulating the signal timing settings. Good timing settings increase traffic capacity and reduce delays and travel times, which in turn affect fuel usage and emissions (Akcelik, 1981). In practice, good settings deliver less congestion and smoother movements of traffic, whereas poor settings can result in a congested network. Thus, decisions driving the selection of signal timing settings will have a significant impact on the urban transportation system. As the volume of traffic

[^0]in cities continues to grow, traffic signal timing settings become more and more challenging, and less able to cope with future demand. Indeed, it is very difficult, if not impossible, to design a precise model for generating signal timing settings that can capture all situations and/or uncertainties at urban intersections. Consequently, the urban transportation system needs to find an effective and efficient solution methodology to meet the ever increasing demand from traffic (Zhao et al., 2012).

Traffic control systems have been well-studied in the literature and various types were developed (Zhao et al., 2012). Existing systems have been categorised into two types: pre-timed (or fixed-time) and adaptive (Zhao et al., 2012). In fixed-time systems, the signal timing settings are determined based on historical traffic data and remain constant over pre-specified time periods. Although they are easy to implement and produce satisfactory results for a predictable traffic pattern, they do not capture the uncertainties of traffic demand, and they require regular updates to avoid loss of capacity (Bell, 1992). Adaptive systems, on the
other hand, generate signal timing settings in a real time based on prevailing traffic conditions, and continuously adapt to the realtime traffic flow. These are more practical than fixed-time systems and can more efficiently cope with escalating demand (Zhao et al., 2012).

In this work, we consider the development of an adaptive, signal timing settings system, featuring multi-intersection traffic signal optimisation, which we test on two real world problems. The proposed algorithm uses traffic volumes derived from induction loop detectors to generate the signal timing settings in an online manner. Traffic signal optimisation is a computationally complex problem that needs an effective and efficient solution methodology (Zhao et al., 2012). In addition, owing to the stochastic nature and the uncertainties of traffic flow, traditional analytical methods have proven to be inadequate to the task of tackling real-world scenarios. Researchers and practitioners have therefore resorted to computational intelligence algorithms that can return good quality signal timing settings within an acceptable amount of time (Zhao et al., 2012).

Population based computational intelligence algorithms (Araghi et al., 2015) such as the genetic algorithm (Ceylan and Bell, 2004; Chin et al., 2011), harmony search algorithm (Ceylan and Ceylan, 2012), cross entropy algorithm (Maher et al., 2013) and particle swarm optimisation (Garcia-Nieto et al., 2013) have been widely used to generate the signal timing settings, with different levels of adaptability. Reinforcement learning (Khamis and Gomaa, 2014) has also been used. Reviews for the application of computational intelligence algorithms for traffic signal optimisation are available in Araghi et al. (2015) and Zhao et al. (2012).

The population based algorithms mentioned above presented improvements when compared to traditional analytical methods (Zhao et al., 2012; Araghi et al., 2015). However, despite these good results, most were developed to tackle only a single intersection involving a small number decision variables. In addition, it is well known in the scientific literature that population based algorithms often experience slow convergence especially when dealing with constrained optimisation problems (Moscato, 1989; Ong and Keane, 2004; Ong et al., 2006; Neri and Cotta, 2012). The work described here improves on the existing methodologies by considering multi-intersection traffic signal optimisation and proposes a hybrid optimisation scheme, called an adaptive memetic algorithm, to effectively solve the multi-intersection traffic signal optimisation in an on-line manner. More precisely, our work has the following features, which differentiate it from the work of other researchers:

1. We consider two real world traffic signal optimisation problems with very different characteristics: one in Brisbane, Australia, and the other in Plock, Poland. Both cases involve multiple intersections with various constraints and decision variables.
2. We propose an effective adaptive memetic algorithm (MA) to generate various traffic signal timing settings according to prevailing traffic flow conditions. The proposed MA combines the strengths of GA with a local search algorithm in order to accelerate the search convergence process and generate high quality solutions. Given the dynamic nature of the traffic flow, it is important that the developed algorithm should be able to adaptively explore and exploit the search space in order to accommodate changes in the problem. In our MA, GA is used to effectively explore the search space, while leaving the local search algorithm to fine-tune the generated solutions.
3. To effectively exploit the area around the given solution, we propose two important techniques to improve the performance of a traditional MA. First, we use a systematic neighbourhood based simple descent algorithm as a local search to effectively exploit the search space around GA solutions. Second, we

To evaluate the effectiveness of the proposed MA, we coded it into the commercial microscopic simulator, AIMSUN, and tested it on two case studies for Brisbane and Plock. The computational results demonstrated that the proposed MA is better than GA and the traditional fixed-time signal settings.

## 2. Case studies

This section briefly outlines the case studies and introduces the problem formulation.

### 2.1. Brisbane

The Brisbane study area is located north of the Brisbane central business district (CBD) on one of this city's busiest urban corridors: the Bowen Bridge Road. The coded network is 673 m long, crossing two other busy roads: O'Connel Terrace and Gregory Terrace. For the purpose of implementing the proposed signal optimisation, stop-line detectors were installed to detect the passage of vehicles in all lanes approaching the intersections. Fig. 1 illustrates the Brisbane case study.

### 2.2. Plock

The Plock study area is a major signalised corridor, Wyszogrodzka Route 62, which traverses the CBD area from east to west. The coded network is a 1100 m section consisting of three key intersections and crossing roads near a shopping centre. Similarly to the Brisbane case, stop-line detectors were also installed. Fig. 2 illustrates the detector and lane configurations for the coded intersections.

### 2.3. Problem formulation

The case studies under consideration each have a network of signalised intersections. The set of signal timings to be optimised is referred as a solution $x=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$, representing $n$ green times of each phase at each intersection. The fitness function $D[\pi]$ is defined to evaluate each solution $x$ in the set $X$ of all possible solutions. Here $D[\pi]$ measures the traffic delay per vehicle exiting the study site, which is the difference between the estimated travel time to exit the study corridor and the free-flow travel time. $D[\pi]$ depends on a vector $\pi$ of traffic-related variables from the loop detectors located under each lane at intersections. $D[\pi]$ is therefore estimated by a time-dependent form of Davidson's function, derived using the coordinate transformation technique in Akcelik (1981) and calculated as follows:

$$
\min D=0.25 \times T_{f} \times\left(z+\left(z^{2}+8 \times J_{D} \times S /\left(Q \times T_{f}\right)\right) \times 0.5\right)
$$

where
$D=$ average traffic delay per unit distance (seconds per km).
$T_{f}=$ flow period constant (seconds), equals 7200 s in this study.

![](https://cdn.mathpix.com/cropped/edd81836-6006-45c1-87c7-b1c15c6f220c-3.jpg?height=1163&width=872&top_left_y=198&top_left_x=149)
Fig. 1. The Brisbane case study.

$$
z=S-1
$$

$S=$ degree of saturation, equal to the ratio of volume to capacity (both vehicles per hour).
$Q=$ capacity constant (vehicles per hour).
$J_{D}=$ delay parameter, dependent on road conditions.
subject to:

$$
\sum_{i=1}^{m} x_{i}=\chi
$$

$$
x_{\min } \leq x_{i} \leq x_{\max } \quad \forall i \in(1 \ldots m)
$$

The first constraint, Eq. (2), ensures that the sum of green times at $m$ phases within an intersection equals the cycle time, $\chi$. The second constraint, Eq. (3), defines the minimum and maximum times that an adaptive signal phase may be held green.

## 3. Methodology

The body of research into traffic signal optimisation has demonstrated that population based algorithms are the state of the art, in that they outperform other traditional analytical methods in many different scenarios. Notwithstanding this remarkable success, most population based algorithms exhibit slow convergence, especially when dealing with constrained optimisation problems, and this hinders their applicability in real time scenarios (Moscato, 1989; Ong and Keane, 2004; Ong et al., 2006; Neri and Cotta, 2012). To mitigate the slow convergence issue, memetic algorithms (MAs) were introduced. MA is a hybrid computational intelligence algorithm that merges the strengths of population based algorithms with local search algorithms to accelerate the search convergence (Moscato, 1989; Sabar and Aleti, 2017; Sabar et al., 2016b, 2015c; Turky et al., 2016, 2017). However, the development of an effective MA depends greatly on how the search can achieve a proper balance between exploration and exploitation (Sabar et al., 2016a, 2017, 2015a, 2015b, 2013).

To address this issue, we propose an adaptive memetic algorithm (MA) for the traffic signal optimisation problem. The proposed MA integrates the exploration power of GA with the exploitation capability of a local search in an adaptive manner. We use a systematic neighbourhood based simple descent algorithm as a local search to effectively exploit the search space around GA solutions. The decision whether of not to activate this local search is driven by a newly developed indicator scheme based on the search diversity and quality. The flowchart of the proposed MA is presented in Fig. 3. It has three parts: GA (Section 3.1), the indicator scheme (Section 3.2) and the local search algorithm (Section 3.3). The GA is responsible for exploring new areas in the search space of solutions. The quality indicator scheme determines whether the local search should be applied or not. The local search algorithm is used to accelerate the search convergence. The main parts of the proposed MA are described in the following subsections.

### 3.1. Genetic algorithm

The proposed MA uses GA to explore the search space of solutions. GA is a nature inspired computational intelligence method that simulates the process of natural selection (Holland, 1975). It begins with a population of solutions and then applies evolutionary operators (selection, crossover, mutation and update) to evolve a new population of solutions within which improved solutions may exist.

In this work, each GA solution represents a set of traffic signal timing settings in the form of a one-dimensional array, as shown in Fig. 4. The number of cells represents the total number of phases at all intersections in the study area. The value in each cell indicates the green time of a particular phase at the associated intersection. For example, the first intersection (intersection \#1) has 5 phases and the green time of the first is 11 s, the second is 2 s, the third is 8 s and so on.

The flowchart of the GA is shown in Fig. 5. It begins by setting the parameter values, generating a population of solutions and then calculating the fitness value of each solution in the population. Next, the main loop is executed for a predefined number of generations (iterations). At each generation, GA evolutionary operators (selection, crossover and mutation) are applied to generate a new population of solutions. If the specified stopping condition has been satisfied, the GA will stop and return the best solution. Otherwise, it calculates the fitness value of the new population, calls the population update mechanism and commences a new generation cycle.

The main steps of the GA are described in further detail below:

- Step 1: Set parameters. In this step, the main GA parameters are initialised. These include:
1. Maximum number of generations $(\operatorname{MaxG})$-indicating the number of generations before termination of the GA search process..
2. Population size (PS)-representing the number of solutions to be created.
3. Crossover rate(Cr)-specifying the proportion of solutions subjected to the crossover operator.
4. Mutation rate (Mr)-denoting the probability that an element of a given solution will be altered to a different value.
- Step 2: Initial population of solutions. A set of solutions, PS, is randomly created. We assign to each cell of a given solution a

![](https://cdn.mathpix.com/cropped/edd81836-6006-45c1-87c7-b1c15c6f220c-4.jpg?height=797&width=1516&top_left_y=196&top_left_x=258)

![](https://cdn.mathpix.com/cropped/edd81836-6006-45c1-87c7-b1c15c6f220c-4.jpg?height=510&width=1124&top_left_y=1044&top_left_x=454)
Fig. 2. The Plock case study.

![](https://cdn.mathpix.com/cropped/edd81836-6006-45c1-87c7-b1c15c6f220c-4.jpg?height=777&width=760&top_left_y=1727&top_left_x=170)
Fig. 3. The overall flowchart of the proposed MA.

uniformly distributed random value between upper and lower bounds as follows:

$$
x_{i, j}=x_{i, j}^{L B}+\operatorname{Rand}[0,1] *\left(x_{i, j}^{U B}-x_{i, j}^{L B}\right)
$$

where $i$ is the index of solution, $j$ represents the current decision variable of the $i$ th solution and $\operatorname{Rand}[0,1]$ returns a random number between 0 and $1 . L B$ and $U B$ are, respectively, the lower and upper bounds for the $j$ th decision variable.

- Step 3: Fitness calculation. In this step, we assign a fitness value to each solution in the population. The fitness value represents the quality of a solution relative to others in the same population. We use the delay from Eq. (1) to calculate fitness values.
- Step 4: Selection. The selection mechanism picks out two solutions from the population for the crossover (or reproduction) step. We adopted the traditional tournament selection mechanism. The tournament size is set to 3, indicating that each tournament has three solutions competing with each other. At each tournament call, three different solutions from the current population are randomly selected and the one with highest fitness value will be added to the reproduction pool.
- Step 5: Crossover. Crossover is responsible for generating a new population of solutions. It takes two or more solutions from the reproduction pool and then mixes their genetic materials to

![](https://cdn.mathpix.com/cropped/edd81836-6006-45c1-87c7-b1c15c6f220c-5.jpg?height=151&width=1344&top_left_y=198&top_left_x=379)
Fig. 4. An example of GA solution representation.

![](https://cdn.mathpix.com/cropped/edd81836-6006-45c1-87c7-b1c15c6f220c-5.jpg?height=1046&width=512&top_left_y=491&top_left_x=327)
Fig. 5. The flowchart of GA.

produce new offsprings. We have used the uniform crossover operator (or reproduction operator), which generates two offsprings by mixing the materials of two different solutions. That is, an offspring is created by randomly copying materials from both solutions in fixed proportions.

- Step 6: Mutation. The mutation operator alters a part of the generated offsprings based on Mr. It attempts to improve the search diversity so as to escape locally optimal points. We adopted the uniform point mutation operator which iterates through all cells of a given offspring and then, based on the Mr, replaces their values with random numbers uniformly distributed between specified upper and lower bounds.
- Step 7: Stopping condition. This step is responsible for terminating the search process. It checks whether MaxG has been reached and, if so, halts the GA search process and returns the best found solution. If, on the other hand, $\operatorname{MaxG}$ is not reached, it calls the following steps:

1. Perform fitness calculation: calculates the fitness values of the generated new solutions.
2. Update the population: replaces new solutions with old ones if the new ones are better in terms of the fitness value.
3. Return to Step 4.

3.2. Indicator scheme

It is important in the design of an effective MA to achieve a good trade-off between the exploration power of GA and the exploitation capability of the local search algorithm. Obviously, calling the local search algorithm at every GA generation will be computationally expensive and the search will be exploitative more than explorative. To avoid this issue, we propose an indicator scheme to determine when the local search algorithm should be applied. The proposed indicator scheme uses the quality and diversity of the search process to either add the generated solution into the population, without local search improvement, or to call the local search to improve it. In this work, the quality is calculated using Eq. (1) and the diversity is quantified as the average similarity between the generated solution and current population (using Euclidean distance). A local search algorithm is applied if the solution is no better than the worst one in the population and, at the same time, sufficiently diverse from the current population of solutions. The main idea is to call the local search algorithm only when the generated solution is not better than any other in the population and it can also promote some diversity. In this way, the local search algorithm will only be executed during certain generations. This will not only save computational time but will also improve the search process.

The proposed indicator scheme works in the following way. It begins by calculating the quality and diversity of the solution generated by GA. If this solution is better than the worst one in the population, the latter is discarded and the generated solution added into the population. Otherwise, the average diversity between the generated solution and the current population of solutions is calculated. If the generated solution is better in terms of diversity (i.e. highly dissimilar), then the local search algorithm (Section 3.3) is called to improve it, and the worst one in the population is replaced with the final solution.

### 3.3. Local search algorithm

The local search algorithm is a particularly important component in the proposed MA. Its main role is to improve the convergence process of the GA in order to attain higher quality solutions (Moscato, 1989). For the work described in this paper, the utilised local search algorithm follows the general rules of the simple descent method. It takes a given solution as an input and iteratively modifies it, seeking out improvements until it reaches a specified termination condition. That is, at each iteration of the local search process, we modify the current solution to produce a new one. To effectively exploit the area around the given solution, we use a systematic neighbourhood operator to modify the current solution. This operator scans the cells of a given solution, one by one, carrying out the following actions. First, the value of the cell is temporarily changed to a uniformly distributed random number between upper and lower bounds. Then, if the new value leads to a better solution in terms of the fitness function, it replaces the old one; otherwise, the new value is rejected and the search moves to the next cell. The local search process is terminated after a predefined number of consecutive non-improving iterations (in this work we settled on 10 iterations based on a preliminary experiment, see Section 4). The pseudocode of the local search algorithm is shown in Algorithm 1.

Algorithm 1. Local search algorithm

```
\(S=S_{0} / *\) Given an initial solution \(S_{0}{ }^{*} /\);
Set Max \(_{i t e r}\), Iter \(=0\);
while Iter \(<M a x_{i t e r}\) do
    \(N=S\);
    for \(i=1\) to \(|S| \mathbf{d o}\)
        \(N_{i}=S_{i}^{L B}+\operatorname{Rand}[0,1] *\left(S_{i}^{U B}-S_{i}^{L B}\right) ;\)
        if \(N\) is better than \(S\) then
            \(S=N\)
        end
    end
    Iter = Iter + 1;
end
Output final solution, \(S\);
```


## 4. Experimental settings

This section presents the settings used in the simulator (AIMSUN) and the parameter values used in the proposed MA.

### 4.1 Simulation settings

To simulate the actual working environment of the proposed MA in a practical implementation, this study utilised the wellknown stochastic microscopic traffic simulator, AIMSUN (Barceló and Casas, 2005). It should be noted, however, that the method proposed here is generic to any microscopic or macroscopic traffic simulators. Fig. 6 illustrates the simulation flowchart.

The traffic volumes were collected by the Brisbane City Council (for the Brisbane case) and by the Polish Road and Bridge Research Institute (IBDIM) (for the Plock case) on a weekday during morning peak hours between 6:30 am and 8:30 am. The signal phase sequence and cycle times were coded in AIMSUN, similarly to the observed values. Traffic volumes, recorded by the stop-line detectors modelled in AIMSUN, provide the variable input to the optimisation algorithm which produces a new set of traffic signal timings. AIMSUN takes these new signal timings and proceeds to the next time step. The AIMSUN simulation was run 30 times using different random seeds to achieve an accurate estimate of the objective function $D[\pi]$. Table 1 summarizes parameters used at the Brisbane and Plock study sites.

### 4.2. MA parameter settings

The proposed MA requires a few parameters to be set by the user. To this end, a preliminary experimental test was conducted to identify appropriate parameter values (Kendall et al., 2016). For each parameter, we tested various values and selected the one that produced the best trade-off between computational time and

![](https://cdn.mathpix.com/cropped/edd81836-6006-45c1-87c7-b1c15c6f220c-6.jpg?height=476&width=637&top_left_y=2071&top_left_x=230)
Fig. 6. Simulation flowchart.

Table 1
Signal phase sequence, cycle time and study period.
| Case | Intersection Id | Number of phases | Total cycle time (s) | Study period |
| :--- | :--- | :--- | :--- | :--- |
| Brisbane | 1 | 2 | 90 | 6:30-8:30 AM |
|  | 2 | 3 |  |  |
|  | 3 | 2 |  |  |
|  | 4 | 3 |  |  |
| Plock | 1 | 12 | 120 | 6:30-8:30 AM |
|  | 2 | 13 |  |  |


Table 2
The parameter settings of MA.
| Parameter | Tested range | Suggested value |
| :--- | :--- | :--- |
| Maximum number of generations, MaxG | 5-100 | 40 fitness evaluations |
| Population size, PS | 5-30 | 20 |
| Crossover rate, Cr | 0.1-0.9 | 0.4 |
| Mutation rate, Mr | 0.1-0.9 | 0.2 |
| Maximum number of non-improving iterations for local search | 5-20 | 10 |


solution quality. The final parameter values, along with tested ranges, are presented in Table 2.

## 5. Experimental results

This section is divided into two subsections. The first examines the performance of the proposed MA using the standard benchmark test functions. The second presents the computational results of the tested algorithms (MA, GA and fixed) for the traffic signal optimisation case studies.

### 5.1. The computational results of the test functions

The effectiveness of the proposed MA was verified using the standard benchmark test functions. The benchmark consists of 6 continuous minimisation functions that have various characteristics and have been widely used in the literature (Suganthan et al., 2005; Lim and Isa, 2013). The formulations, feasible search ranges and the dimensions (D) of all functions are presented in Table 3 (Suganthan et al., 2005).

The results of our MA are compared against the following stateof-the-art algorithms:

- SaDE: Differential evolution algorithm with strategy adaptation (Qin et al., 2009).
- ABC: Artificial bee colony algorithm (Gao et al., 2013).
- CMA: Covariance matrix adaptation evolution strategy (Hansen and Ostermeier, 2001).
- PSO: Particle swarm optimisation with increasing topology connectivity (Lim and Isa, 2014)

To ensure a fair comparison, we used the maximum number of fitness evaluations as our termination condition - fixed at 300,000 fitness evaluations. In line with standard practice, our MA was tested 30 independent runs on all functions. The computational results (mean and standard deviation (SD)) of MA and the compared algorithms (SaDE, ABC, CMA and PSO) are presented in Table 4. In the table, best results are indicated in bold font. As can be seen, the proposed MA obtained the best results for all tested functions. Specifically, for five of the six tested functions, MA reached the global optimal 30 times as indicated by the standard

Table 3
The parameter settings of MA.
| No. | Name | Formulae | Range | D |
| :--- | :--- | :--- | :--- | :--- |
| F1 | Sphere | $F_{1}(X)=\sum_{i=1}^{D} X_{i}^{2}$ | [ - 100, 100] ${ }^{D}$ | 30 |
| F2 | Schwefel | $F_{2}(X)=\sum_{i=1}^{D}\left(\sum_{j=1}^{i} X_{j}\right)^{2}$ | [ - 100, 100] ${ }^{D}$ | 30 |
| F3 | Rosenbrock | $F_{3}(X)=\sum_{i=1}^{D-1}\left(100\left(X_{i}^{2}-X_{i+1}\right)^{2}+\left(X_{i}-1\right)^{2}\right)$ | $[-2.048,2.048]^{D}$ | 30 |
| F4 | Rastrigin | $F_{4}(X)=\sum_{i=1}^{D}\left(X_{i}^{2}-10 \cos \left(2 \pi X_{i}\right)+10\right)$ | [ - 5.12, 5.12] ${ }^{D}$ | 30 |
| F5 | Griewank | $F_{5}(X)=\sum_{i=1}^{D} X_{i}^{2} / 4000-\prod_{i=1}^{D} \cos \left(X_{i} / \sqrt{i}\right)+1$ | $[-600,600]^{D}$ | 30 |
| F6 | Ackley | $F_{6}(X)=-20 \exp \left(-0.2 \sqrt{\sum_{i=1}^{D} X_{i}^{2} / D}\right)-\exp \left(\sum_{i=1}^{D} \cos \left(2 \pi X_{i}\right) / D\right)+20+e$ | $[-32,32]^{D}$ | 30 |


Table 4
The results of MA compared to the state-of-the art algorithms.
| Function |  | MA | SaDE | ABC | CMA | PSO |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sphere | Mean | 0.00E+00 | $3.28 \mathrm{E}-20$ | 4.32E-43 | $6.09 \mathrm{E}-29$ | 0.00E+00 |
|  | SD | 0.00E+00 | $3.63 \mathrm{E}-20$ | 8.16E-43 | $1.55 \mathrm{E}-29$ | 0.00E+00 |
| Schwefel | Mean | 0.00E+00 | NA | NA | $1.51 \mathrm{E}-26$ | 0.00E+00 |
|  | SD | 0.00E+00 | NA | NA | $3.64 \mathrm{E}-27$ | 0.00E+00 |
| Rosenbrock | Mean | 5.00E-01 | 2.10E+01 | 7.89E-01 | $5.58 \mathrm{E}-01$ | 2.55E + 01 |
|  | SD | 1.28E+00 | 7.80E + 00 | $6.27 \mathrm{E}-01$ | 1.39E+00 | 1.35E+00 |
| Rastrigin | Mean | 0.00E+00 | $2.43 \mathrm{E}+00$ | 0.00E+00 | 4.95E + 01 | 0.00E+00 |
|  | SD | 0.00E+00 | 1.60E+00 | 0.00E+00 | $1.23 \mathrm{E}+01$ | 0.00E+00 |
| Ackley | Mean | 0.00E+00 | $3.81 \mathrm{E}-06$ | 5.32E-15 | 4.61E+00 | 0.00E+00 |
|  | SD | 0.00E+00 | 8.26E-07 | $1.82 \mathrm{E}-15$ | 8.73E+00 | 0.00E+00 |
| Grienwank | Mean | 0.00E+00 | 2.52E-09 | 0.00E+00 | $7.40 \mathrm{E}-04$ | 0.00E+00 |
|  | SD | 0.00E+00 | $1.24 \mathrm{E}-08$ | 0.00E+00 | 2.39E-03 | 0.00E+00 |


deviation $(\mathrm{SD}=0)$. For one test function, the obtained result is very close to the optimal value. The average computational times of the proposed MA is between 120 and 140 s. It should be noted that the compared algorithms did not reported the computational times. Overall, the results demonstrate that the proposed MA offers an effective method for solving continuous minimisation test functions.

### 5.2. The computational results of the traffic signal problems

In this section, we present the computational results for both case studies: Brisbane and Plock. Three different algorithms were tested and compared. These are:

- Memetic algorithm (MA): the new approach being proposed;
- Genetic algorithm (GA): the forerunner and foundation of MA-the GA was tested in both case studies, using the same parameter settings and computational resources as used in MA, so as to assess the impact of the integrated local search on search performance; and,
- Fixed time (FT): the traditional fixed-time approach as implemented in AIMSUN.

The result comparisons of MA, GA and FT over both case studies are presented in Table 5. For both case studies, we executed 30 independent runs of MA and GA using different random seeds. The results are presented in terms of the best overall average delay per vehicle in the network, where lower delay represents better performance. Bold font indicates the best result obtained. In the table, column \#GAMA represents the percentage improvement of MA

Table 5
The computational results of FT, GA and MA for Brisbane and Plock.
| Case | FT | GA | MA | \#GAMA | \#FTMA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Brisbane | 71.71 | 70.24 | 65.08 | 7.92\% | 10.18\% |
| Plock | 317.51 | 288.15 | 278.95 | 3.29\% | 13.82\% |


over GA, and \#FTMA is the percentage improvement of MA over FT. As can be seen from Table 5, the proposed MA outperforms FT and GA on both case studies. The percentage improvement of MA compared to FT is 10.18\% for Brisbane and 13.82\% for Plock. Compared to GA, MA is significantly better with $7.92 \%$ for Brisbane and 3.29\% for Plock.

In Table 6, we present further measures of the overall average vehicle delay (worst, average, standard deviation (Std)), together with the average computational time, for MA and GA, over 30 replications. As can be seen from the table, MA performs better than GA in both case studies. In particular, the lower average and standard deviation results of MA, in both case studies, indicates that MA is more stable and can effectively handle the search landscape changes. The results obtained show the positive impact on search performance achieved by integrating the local search algorithm.

To further verify the result, a Wilcoxon statistical test was conducted with a significance level of 0.05 . The $p$-value of MA versus GA for Brisbane is 4.00E-05 ( $p$-value < 0.05) and for Plock is 2.83E-04 ( $p$-value < 0.05), indicating that MA is statistically better than GA. To examine the search behaviour of MA and GA, we show in Fig. 7 an example of one replication of the progression of the search for both case studies. As can be seen from the figure, MA does not just produce better results, but it is also the more stable algorithm. MA did not generate many spikes during the whole search process, and it remained lower than GA. It should be noted

Table 6
The worst, average, standard deviation and time (seconds) of MA and GA for both case studies.
| Cases | GA |  |  |  | MA |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Worst | Average | Std | Time | Worst | Average | Std | Time |
| Brisbane | 82.44 | 76.53 | 3.57 | 70 | 69.22 | 67.65 | 1.22 | 56 |
| Plock | 315.14 | 302.19 | 7.34 | 95 | 298.24 | 283.85 | 2.26 | 73 |


The search behaviour of MA and GA for Brisbane case study

![](https://cdn.mathpix.com/cropped/edd81836-6006-45c1-87c7-b1c15c6f220c-8.jpg?height=1178&width=1150&top_left_y=252&top_left_x=439)
Fig. 7. Comparing MA and GA search behaviour.

that we have given both algorithms (MA and GA) the same number of fitness evaluations, meaning that the computational time consumed by both algorithms was the same, yet MA converged faster than GA. This positive result again demonstrates the benefit of integrating the local search algorithm with GA. Indeed, the use of the local search algorithm can effectively enhance the performance of GA to obtain very good results for both cases.

## 6. Conclusion

This paper presented an adaptive traffic signal optimisation algorithm for real world multi-intersection traffic signal optimisation problems. The proposed algorithm is based on the so-called memetic algorithm that combines the strengths of the genetic algorithm and local search in an adaptive manner. It uses two important techniques for improving the performance of traditional memetic algorithms. First, a systematic neighbourhood based simple descent algorithm was employed as a local search to effectively exploit the search space. Second, an indicator scheme was proposed to control the local search application based on the quality and diversity of the search process. The proposed indicator scheme tries to avoid losing diversity, and directs the search towards promising regions. The proposed algorithm was coded in the commercial microscopic traffic simulator, AIMSUN, and tested on two difference real world case studies in Brisbane, Australia, and Plock, Poland. The results demonstrate that the proposed algorithm is better than genetic algorithms and fixed-time settings, indicating that the proposed algorithm is an effective solution method for traffic signal optimisation problems.

## References

Akcelik, R., 1981. Traffic Signals: Capacity and Timing Analysis.
Araghi, S., Khosravi, A., Creighton, D., 2015. A review on computational intelligence methods for controlling traffic signal timing. Expert Syst. Appl. 42 (3), 1538-1550.
Barceló, J., Casas, J., 2005. Dynamic network simulation with aimsun. In: Simulation approaches in transportation analysis, Springer, pp. 57-98.
Bell, M.G., 1992. Future directions in traffic signal control. Transp. Res. A: Policy Pract. 26 (4), 303-313.
Ceylan, H., Bell, M.G., 2004. Traffic signal timing optimisation based on genetic algorithm approach, including drivers routing. Transp. Res. B: Methodol. 38 (4), 329-342.
Ceylan, H., Ceylan, H., 2012. A hybrid harmony search and transyt hill climbing algorithm for signalized stochastic equilibrium transportation networks. Transp. Res. C: Emerg. Technol. 25, 152-167.
Chin, Y.K., Yong, K., Bolong, N., Yang, S.S., Teo, K.T.K. 2011. Multiple intersections traffic signal timing optimization with genetic algorithm. In: Control System, Computing and Engineering (ICCSCE), 2011 IEEE International Conference on, IEEE, pp. 454-459.
Gao, W.-f., Liu, S.-y., Huang, L.-l., 2013. A novel artificial bee colony algorithm based on modified search equation and orthogonal learning. IEEE Trans. Cybern. 43 (3), 1011-1024.
Garcia-Nieto, J., Olivera, A.C., Alba, E., 2013. Optimal cycle program of traffic lights with particle swarm optimization. IEEE Trans. Evolut. Comput. 17 (6), 823-839.
Hansen, N., Ostermeier, A., 2001. Completely derandomized self-adaptation in evolution strategies. Evolut. Comput. 9 (2), 159-195.
Holland, J.H., 1975. Adaptation in Natural and Artificial Systems: An Introductory Analysis with Applications to Biology, Control, and Artificial Intelligence. U Michigan Press.
Hunt, P., Robertson, D., Bretherton, R., Royle, M.C., 1982. The scoot on-line traffic signal optimisation technique. Traffic Eng. Control 23 (4).
Kendall, G., Bai, R., Błazewicz, J., De Causmaecker, P., Gendreau, M., John, R., Li, J., McCollum, B., Pesch, E., Qu, R., et al., 2016. Good laboratory practice for optimization research. J. Oper. Res. Soc. 67 (4), 676-689.
Khamis, M.A., Gomaa, W., 2014. Adaptive multi-objective reinforcement learning with hybrid exploration for traffic signal control based on cooperative multiagent framework. Eng. Appl. Artif. Intell. 29, 134-151.

Lim, W.H., Isa, N.A.M., 2013. Two-layer particle swarm optimization with intelligent division of labor. Eng. Appl. Artif. Intell. 26 (10), 2327-2348.
Lim, W.H., Isa, N.A.M., 2014. Particle swarm optimization with increasing topology connectivity. Eng. Appl. Artif. Intell. 27, 80-102.
Maher, M., Liu, R., Ngoduy, D., 2013. Signal optimisation using the cross entropy method. Transp. Res. C: Emerg. Technol. 27, 76-88.
Moscato, P., 1989. On evolution, search, optimization, genetic algorithms and martial arts - towards memetic algorithms. Caltech Concurrent Computation Program, C3P Report, 826: pp. 1-67.
Neri, F., Cotta, C., 2012. Memetic algorithms and memetic computing optimization: a literature review. Swarm Evolut. Comput. 2, 1-14.
Ong, Y.S., Keane, A.J., 2004. Meta-lamarckian learning in memetic algorithms. IEEE Trans. Evolut. Comput. 8 (2), 99-110.
Ong, Y.-S., Lim, M.-H., Zhu, N., Wong, K.-W., 2006. Classification of adaptive memetic algorithms: a comparative study. IEEE Trans. Syst. Man Cybern. B: Cybern. 36 (1), 141-152.
Qin, A.K., Huang, V.L., Suganthan, P.N., 2009. Differential evolution algorithm with strategy adaptation for global numerical optimization. IEEE Trans. Evolut. Comput. 13 (2), 398-417.
Sabar, N.R., Ayob, M., Kendall, G., Qu, R., 2013. Grammatical evolution hyperheuristic for combinatorial optimization problems. IEEE Trans. Evolut. Comput. 17 (December (6)), 840-861. http://dx.doi.org/10.1109/TEVC.2013.2281527 (ISSN 1089-778X).
Sabar, N.R., Ayob, M., Kendall, G., Qu, R., 2015a. Automatic design of a hyperheuristic framework with gene expression programming for combinatorial optimization problems. IEEE Trans. Evolut. Comput. 19 (3), 309-325. http://dx. doi.org/10.1109/TEVC.2014.2319051 (ISSN 1089-778X).
Sabar, N.R., Ayob, M., Kendall, G., Qu, R., 2015b. A dynamic multiarmed bandit-gene expression programming hyper-heuristic for combinatorial optimization problems. IEEE Trans. Cybern. 45 (2), 217-228. http://dx.doi.org/10.1109/ TCYB.2014.2323936 (ISSN 2168-2267).
Sabar, N.R., Abawajy, J., Yearwood, J., 2017. Heterogeneous cooperative co-evolution memetic differential evolution algorithm for big data optimization problems. IEEE Trans. Evolut. Comput. 21 (2), 315-327. http://dx.doi.org/10.1109/ TEVC.2016.2602860 (ISSN 1089-778X).
Sabar, N.R., Aleti, A., 2017. An adaptive memetic algorithm for the architecture optimisation problem. In: Australasian Conference on Artificial Life and Computational Intelligence, Springer, pp. 254-265.
Sabar, N.R., Song, A., Tari, Z., Yi, X., Zomaya, A., 2015c. A memetic algorithm for dynamic shortest path routing on mobile ad-hoc networks. In: Parallel and Distributed Systems (ICPADS), 2015 IEEE. In: Proceedings of the 21st International Conference on, IEEE, pp. 60-67.
Sabar, N.R., Song, A., Zhang, M., 2016a. A variable local search based memetic algorithm for the load balancing problem in cloud computing. In: European Conference on the Applications of Evolutionary Computation, Springer, pp. 267-282.
Sabar, N.R., Turky, A., Song, A., 2016b. A multi-memory multi-population memetic algorithm for dynamic shortest path routing in mobile ad-hoc networks. In: Pacific Rim International Conference on Artificial Intelligence, Springer, pp. 406-418.
Suganthan, P.N., Hansen, N., Liang, J.J., Deb, K., Chen, Y.-P., Auger, A., Tiwari, S., 2005. Problem definitions and evaluation criteria for the cec 2005 special session on real-parameter optimization. Technical report.
Turky, A., Sabar, N.R., Song, A., 2016. A multi-population memetic algorithm for dynamic shortest path routing in mobile ad-hoc networks. In: Evolutionary Computation (CEC), 2016 IEEE Congress on, pp. 4119-4126. IEEE.
Turky, A., Sabar, N.R., Song, A., 2017. An evolutionary simulating annealing algorithm for google machine reassignment problem. In: Intelligent and Evolutionary Systems. In: Proceedings of the 20th Asia Pacific Symposium, IES 2016, Canberra, Australia, November 2016, Proceedings, Springer, pp. 431-442.
Zhao, D., Dai, Y., Zhang, Z., 2012. Computational intelligence in urban traffic signal control: a survey. IEEE Trans. Syst. Man Cybern. C: Appl. Rev. 42 (4), 485-494.


[^0]:    * Corresponding author.
    E-mail addresses: nasser.sabar@qut.edu.au (N.R. Sabar), leminh.kieu@qut.edu.au (L.M. Kieu), edward.chung@qut.edu.au (E. Chung), t.tsubota@cee.ehime-u.ac.jp (T. Tsubota),
    pema@lsi.cefetmg.br (P.E. Maciel de Almeida).

