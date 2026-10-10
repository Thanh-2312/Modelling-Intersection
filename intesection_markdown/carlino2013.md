# Auction-based autonomous intersection management 

Dustin Carlino<br>Department of Computer Science<br>The University of Texas at Austin<br>Austin, TX 78712<br>dcarlino@cs.utexas.edu

Stephen D. Boyles<br>Department of Civil, Architectural<br>\& Environmental Engineering<br>The University of Texas at Austin<br>Austin, TX 78712<br>sboyles@mail.utexas.edu

Peter Stone<br>Department of Computer Science<br>The University of Texas at Austin<br>Austin, TX 78712<br>pstone@cs.utexas.edu


#### Abstract

Autonomous vehicles present new opportunities for addressing traffic congestion through flexible traffic control schemes. This paper explores the possibility that auctions could be run at each intersection to determine the order in which drivers perform conflicting movements. While such a scheme would be infeasible for human drivers, autonomous vehicles are capable of quickly and seamlessly bidding on behalf of human passengers. Specifically, this paper investigates applying autonomous vehicle auctions at traditional intersections using stop signs and traffic signals, as well as to autonomous reservation protocols. This paper also addresses the issue of fairness by having a benevolent system agent bid to maintain a reasonable travel time for drivers with low budgets. An implementation of the mechanism in a microscopic simulator is presented, and experiments on city-scale maps are performed.


## I. INTRODUCTION

Autonomous vehicles (AVs) have tremendous potential for reducing traffic congestion and its consequences, including 5.5 billion wasted hours, 2.9 billion gallons of wasted fuel, and 56 billion pounds of carbon emissions in the United States alone [1]. This potential comes not only from increased safety and decreased following distance, but also because they admit innovative traffic control schemes. In particular, intersections are the major source of delay on arterial streets. Existing intersection control schemes, such as traffic signals or stop signs, must conform to human behavioral limitations and are highly inefficient. By contrast, AVs communicating with reservation-based intersection managers can make much better use of available roadway capacity, reducing delay by up to two orders of magnitude at highly congested intersections [2].

The management scheme proposed in [2] assigns reservations on a first-come, first-served basis. This paper improves on this basic management scheme by reflecting differences in priority among trips. For instance, travelers late for a flight presumably find intersection delay far more onerous than do travelers on a routine shopping trip, and an ideal reservation system should be able to accommodate this difference. We propose that a market-based pricing mechanism can allow travelers to self-organize in a way that prioritizes higher-valued trips, and that AVs provide an ideal platform for introducing this mechanism without unduly burdening drivers. Specifically, we propose a decentralized auctionbased autonomous intersection management scheme. Each driver has a "wallet agent," which automatically bids money or credits on behalf of the driver, to permit the driver to cross the intersection sooner or laster, depending on their value of time.

The primary contribution of this paper is this auctionbased autonomous intersection management scheme reflecting variation in travelers' value of time, and a corresponding "wallet" system for automatic bidding based on trip characteristics, driver-specified budget, and remaining distance to the destination. Using several representative city networks as test locations, we evaluate the performance of this scheme in simulation. In several cases, substantial time savings are observed relative to current schemes. A key feature of the proposed framework are "system bids," which subsidize bids beneficial to the overall traffic stream, and which partially address equity considerations.

The remainder of this paper is organized as follows. Related work is first surveyed in Section II. The mechanics of auctions are presented in Section III, then data demonstrating how auctions affect trip times in a microsimulation are shown in Section IV. We then discuss social equity issues brought about by auctions in Section V and conclude in Section VI.

## II. RELATED WORK

The notion that market forces can be harnessed to address congestion externalities can be traced to Pigou [3] and Beckmann et al. [4], who proposed that network-wide marginal-cost tolls can coordinate drivers to choose routes minimizing total travel time. These early works required a number of strong assumptions that later research has relaxed: more sophisticated pricing models can address reliability and uncertainty [5], [6], variations in value of time across the population [7], [8], real-time travel information [9], [10], and adaptive, dynamic pricing [11], [12]. The work presented here is distinctive in its focus on applying market forces at intersections, rather than roadway segments. This reflects the nature of delay on arterial street networks, which is the focus of our study, as opposed to freeways where tolls are traditionally collected.

A similar approach to our work was conducted by Vasirani and Ossowski, who extended the AIM reservation protocol [2] to use auctions at individual intersections as well. To handle an entire network, they introduce competitive traffic

![](https://cdn.mathpix.com/cropped/56860d5a-4d6e-46b8-be43-dc735bcd0906-2.jpg?height=1003&width=881&top_left_y=183&top_left_x=183)
Fig. 1: The amount each driver bids (in units of cents) is shown below or beside their name, and the total bid for each choice is circled. Assume for simplicity that all drivers wish to cross straight across the intersection.

assignment [13], which has intersections update reserve prices in real-time in response to the current demand. Drivers choose routes based on their own preferences between time and cost, participating in intersections auctions as long as they are willing to meet the reserve price. Although our work bears similarity to this approach, there are several key distinctions. First, our system does not restrict drivers to routes based on pricing. Instead, we use pricing to control the order in which drivers proceed through intersections. Second, we explicitly address the issue of equity with system bids. Third, we generalize the notion of auctions to work at traditional intersection policies as well as with autonomous reservations. Finally, we show that the idea of intersection auctions is compatible with the realism of a microscopic simulator running on maps from OpenStreetMap, and make our implementation available under an open source license.

## III. INTERSECTION AUCTIONS

We first present an example of how intersection auctions work in general, then formalize the general procedure and describe details of how they apply at stop signs, traffic signals, and autonomous reservation intersections. An explanation of automatic bidding and system regulation follows.

## A. Example

As an example to illustrate how our proposed intersection auctions work, consider Figure 1, in which driver $A$ is about to leave the intersection. Assume that only one driver can move through the intersection at a time. As soon as $A$ finishes crossing, the intersection must pick the next driver to admit. In the traditional setting, this ordering is determined by which driver reached the intersection first, but here, an auction is run instead. Only $B, C, D$, and $E$ are candidates, since the other drivers are behind one of these four. Each driver bids for the driver at the front of its lane, since each is self-interested. Note that the drivers behind $C$ do not bid anything, while the driver behind $E$ is actually helping $E$, to get the indirect benefit of moving up in their queue of cars sooner.

The winners will split the cost of the second highest bid with proportional payment, a method inspired by the Clarke-Groves tax mechanism [14], [15]. The total bids are shown for each of the candidate drivers. $B$ wins with $50 ¢$, and the runner-up is $E$ with $40 ¢$. The winners - $B$, who bid $30 \not c$, and $G$, who bid $20 \not \subset$, must together pay the total of the runnerup's bid: $40 ¢$. Since $B$ comprised $60 \%$ of the winning bid and $G$ made up the other 40\%, $B$ pays 60\% of the 40¢ and $G$ pays the remaining $16 ¢$. After $B$ crosses the intersection, a new auction is run, and $G$ is now a candidate. Note that $G$ must bid again; the fact that it contributed to the winner of the previous auction does not affect the next auction. In fact, there is a risk that new drivers, not shown, could appear behind $C$ and $D$ and repeatedly outbid $G$. The effect is that $G$ wastes its money paying for $B$ to move earlier.

## B. General procedure

Now the general process for running an intersection auction is outlined. The following definitions are used.

C (the list of candidate items for a particular auction) and losers (the drivers who experience delay due to the outcome of an auction) are defined per intersection policy
participants are all drivers traveling on a lane that leads to the intersection
$\mathbf{R}$ (item) is a rate by which an item's total bid is multiplied, described in Section III-E
bids $:=\{$ ask_bid $(a, C) \mid a \in$ participants $\}$
where each bid is a tuple ( $a$, item $\in C$, amount)
sum(bids) $:=\sum_{b \in \text { bids }}$ amount $_{b}$
winner $:=\operatorname{argmax}_{\text {item } \in C}\left(R(i t e m) * \operatorname{sum}\left(\right.\right.$ bids $\left.\left._{i t e m}\right)\right)$ where bids $_{\text {item }}:=\left\{b \in\right.$ bids $\mid$ item $_{b}=$ item $\left._{\text {® }}\right\}$
runner_up $:=\operatorname{argmax}_{i \in C}\left(R(i) * \operatorname{sum}\left(L_{i}\right)\right)$
where $L_{i}:=\left\{b \in\right.$ bids $\mid$ item $_{b}=i \wedge$ driver $_{i} \in$ losers $\}$
second_price $:=R($ runner_up $) *$ sum $($ losing_bids $)$ where losing_bids := \{b € bids | item ${ }_{b}=$ runner_up $\wedge$ item $_{a} \in$ losers $\}$

The procedure to choose a winning item - a single driver or a phase of a traffic signal - is as follows:

1) Form a list of candidate items $C$
2) Ask all participating drivers to bid on an item, collecting bids
3) Determine winner and second_price

4) Collect payment from each driver who bid for the winning item. If a contributed amount to winner, which won with total $:=\operatorname{sum}\left(b i d s_{\text {winner }}\right)$, then $a$ pays: $\frac{\text { amount }}{\text { total }} * \frac{\text { second_price }}{R(\text { winner })}$

The auction format is that of a $2^{n d}$ price, sealed bid auction. Ties are broken arbitrarily (but deterministically). Empirically, ties do not occur often. The winners split the second_price cost proportionally to what they originally bid. This cost comes from the item with the second-highest total, except that drivers who are not delayed due to the winner are not counted towards this cost. The multiplier $R$ (winner), which comes from system bids described in Section III-E, adjusts for the boost that the system gave to the winner, so that an driver never spends more than it bids.

## C. Types of intersection policies

In this section, we specify how auctions can be incorporated in three different types of intersection control policies: stop signs, traffic signals, and autonomous reservations.

Stop signs are the simplest policy, illustrated in the example above. The candidates that drivers can bid on include all drivers who are stopped at the front of their respective lane. The losers are all drivers who did not bid for the winner.

Traffic signals are another common policy. They cycle through pre-determined "phases," which allow drivers to perform some set of non-conflicting movements for some duration. In this case, the candidates are phases, not individual drivers. Since many drivers could cross the intersection before a phase ends, more have incentive to participate in the auction. The set of losers is all drivers whose desired movement is not in the winning phase. Note that an extension to this scheme could let drivers also bid to extend or shorten the duration of phases, but in our implementation, all phases operate for a fixed duration. This time can be extended by multiples of the duration by simply bidding for the same phase sequentially.

Finally, the reservation policy is a flexible intersection policy for managing autonomous vehicles, pioneered by Dresner with Autonomous Intersection Management [2]. Auctions are run repeatedly, choosing one driver each round. Drivers are approved to move in the order determined by the auctions, and individuals must wait if their movement conflicts with that of a driver with higher precedence.

In our implementation, all drivers in lanes leading to an intersection can participate in the auctions there, even if they are far away. The candidates only include drivers ready to enter the intersection, preventing drivers from winning the auction and then waiting behind another driver not yet approved for entry. ${ }^{1}$ The losers are drivers whose movements conflict with that of the winner. For example, if $B$ wins the first auction in figure 1, then $E$, whose path

[^0]![](https://cdn.mathpix.com/cropped/56860d5a-4d6e-46b8-be43-dc735bcd0906-3.jpg?height=694&width=722&top_left_y=183&top_left_x=1152)
Fig. 2: $A$ wants to go straight across the intersection, and $B$ and $C$ want to turn left. On the left road, $B$ should get precedence, since $A$ must wait for the cars ahead of it to move. On the right, $C$ may wait indefinitely if a steady stream of drivers with more money flows past.

does not cross that of $B$, could win the second auction and experience no delay. Thus, $E \notin$ losers in this case.

## D. Automatic bidding: wallets

Rather than requiring humans to constantly assess the value of passing through a particular intersection more quickly, an automated wallet agent can bid on behalf of each driver. Ideally, humans input their preferences to the wallet in the form of constraints such as a total budget, a limit on cost per time gained, and a deadline for arrival. However, the time gained by crossing one intersection sooner does not have a obvious relation to the change in net trip time, since traffic jams in the future could make saving time now negligible later.

Instead, we propose three simple wallets. The free-rider wallet never bids anything. In contrast, the static wallet always bids some fixed amount and has an effectively infinite budget. This can be used to model emergency vehicles, for instance, by making the amount that they bid sufficiently high.

Finally, we have implemented one wallet intended for general use: the fair wallet. The fair wallet begins with an initial budget for the trip and divides the funds remaining at any time among the intersections left to cross, as determined by the current route. The route only changes when it must - for instance, when the driver is unable to change lanes on a busy road to make a certain turn and follow the prescribed path. At each intersection, the fair wallet bids $\frac{\text { funds }}{\text { total }}$, where total is the number of intersections remaining along the currently planned route and funds is the amount of money remaining from the original budget. The fair wallet does not pay for anybody ahead of its driver; as a simple heuristic, it avoids the risk of spending money without direct benefit.

## E. Regulating fairness with reserve prices

Two problems remain with having drivers express their preferences. First, consider a steady stream of wealthier drivers competing against a small group without much funds, as in the right panel of Figure 2. Although the greater demand should get priority, the smaller group's progress should not be stalled indefinitely. Second, suppose two groups compete at an autonomous reservation intersection. Each driver bids similarly, causing the winner to alternate between the two groups, effectively reducing the intersection to a stop sign. Enforcing some degree of throughput would improve every-body's trip.

These issues motivate the participation of a benevolent system wallet, who intervenes to maintain various fairness properties. This regulation may always be overcome by a high enough driver bid, meaning the system wallet effectively imposes a reserve price on the auctions. After the bids for some item are summed, the system wallet multiplies the total by some rate, denoted $R$ in Section III-B. Multiplying existing bids is more desirable than adding another bid due to different scales of currency. If drivers are bidding between $5 ¢$ and $10 ¢$, the system bids will modify the results the same as if drivers were spending $50 ¢$ to $100 ¢$. Since multiplying any total of $0 ¢$ is useless, the system wallet will first add $1 ¢$ to any item it boosts before multiplying.

In the specification of system bids below, a queue refers to the sequence of drivers in a lane. Queues are defined per lane, not per road. Below, when a system bid "rewards" a driver, it multiplies the total for the candidate items beneficial to that driver by some rate. Recall that in the case of stop signs and autonomous reservations, the items are individual drivers, while the candidates for traffic signals are phases.

Some system bids apply to all auctions:

- To prevent drivers from being perpetually stuck, reward drivers for being stalled for waiting_time seconds by multiplying by wait_rate $*$ waiting_time.
- A driver has no need to quickly enter a queue already filled nearly to its capacity, since they will just wait there for the drivers ahead to clear out. Reward all drivers destined for emptier queues that have some minimum percent of capacity available by a single rate, capacity_rate. This is demonstrated in the left panel of Figure 2.
- When severe traffic jams form, "queue spillback" occurs as nearby queues fill to capacity, due to one full queue not moving. Reward drivers trying to leave a full queue by dependency_rate * net_demand, where net_demand is the number of total drivers that depend on the driver freeing space in that queue.

Other bids specifically regulate the autonomous reservation policy.

- Multiply by thruput_rate to increase throughput, by preferring drivers whose movements are compatible with those of already accepted drivers. Throughput is not applicable to stop signs and is naturally achieved by traffic signals with fixed durations.
- Stop signs only admit drivers at the front of a queue, and traffic signals cut off drivers too far away to possibly cross before the phase ends. To prevent drivers far away on incoming queues from blocking other conflicting turns from happening, reward drivers for being ready to begin their movement by ready_rate. For the first driver in a queue, this means being close to the end of the queue. For all others, it means following the leading driver at something near the following distance.

These system bids deliberately conflict. For instance, the throughput bid for reservations, if unrestricted, would accept an entire queue of cars, even if some were far away and would prevent others from crossing while they approach the intersection. Currently, the rates described are manually tuned: wait_rate = 1, capacity_rate = 5, dependency_rate = 2, thruput_rate = 7, and ready_rate $=5$. In the future, they will be adjusted by automated offline optimization.

## IV. EXPERIMENTAL RESULTS

To quantify how auctions affect trip times, we implemented auctions in a micro-simulator called AORTA, which is described in Section IV-A. Our strategy for evaluating intersection auctions is then presented in Section IV-B. The results and discussion of the experiments follow in Section IV-C.

All code for AORTA and intersection auctions is open-source and available at http://code.google.com/p/road-rage, and the instructions for reproducing these results are available ${ }^{2}$.

## A. Simulator overview

AORTA [16], the Approximately Orchestrated Routing and Transportation Analyzer, is an open source, agent-based microscopic simulator, written in Scala. The simulator, auction implementation, and experimentation framework total merely 9,500 lines of code. The simulation is continuous in space (meaning roads are not divided into tiles) and discrete in time (meaning simulation proceeds in increments of some fixed time-step). Simulations in any city can be set up in minutes by importing maps from OpenStreetMap, and AORTA is resilient to issues arising from using automatically converted, untuned maps. The map model includes roads with multiple lanes, one-way streets, and intersections with turns leading from an incoming lane to an outgoing lane. (When a driver crosses straight through an intersection, this is still considered a turn.) Two turns conflict if they cross at any point, meaning a driver must wait for others to completely clear conflicting turns. An appropriate policy controls each intersection, based on OpenStreetMap metadata. Stop signs manage intersections between minor roads, traffic signals are placed at crossings of major roads, and autonomous reservations control intersections with a mixture of minor and major roads.

[^1]TABLE I: Trip times using 7 orderings, repeated with 3 trials (units are seconds per driver)
| Metric | FIFO | Equal | Auction | Fixed | Equal with sys | Auction with sys | Fixed with sys |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Austin | $4,846 \pm 92$ |  |  |  |  |  |  |
| weighted | $4,853 \pm 96$ | $4,812 \pm 32$ | $4,428 \pm 84$ | $4,666 \pm 117$ | $4,698 \pm 187$ | $4,240 \pm 48$ | $4,566 \pm 152$ |
| BR |  |  |  |  |  |  |  |
| unweighted | $1,599 \pm 47$ | $1,752 \pm 233$ | $1,821 \pm 77$ | $1,652 \pm 110$ | $1,240 \pm 8$ | $1,236 \pm 16$ | $1,262 \pm 8$ |
| weighted | $1,608 \pm 52$ | $1,758 \pm 236$ | $1,799 \pm 69$ | $1,631 \pm 114$ | $1,246 \pm 11$ | $1,235 \pm 19$ | $1,261 \pm 13$ |
| Seattle |  |  |  |  |  |  |  |
| unweighted | $4,713 \pm 62$ | $2,926 \pm 33$ | $2,666 \pm 52$ | $2,876 \pm 36$ | $3,599 \pm 9$ | $3,488 \pm 53$ | $3,537 \pm 24$ |
| weighted | $4,700 \pm 66$ | $2,933 \pm 24$ | $2,497 \pm 55$ | $2,823 \pm 44$ | $3,596 \pm 10$ | $3,397 \pm 39$ | $3,514 \pm 38$ |
| SF |  |  |  |  |  |  |  |
| unweighted | $1,883 \pm 31$ | $1,878 \pm 5$ | $1,596 \pm 9$ | $1,843 \pm 16$ | $1,593 \pm 58$ | $1,573 \pm 20$ | $1,546 \pm 29$ |
| weighted | $1,884 \pm 34$ | $1,877 \pm 4$ | $1,552 \pm 10$ | $1,825 \pm 18$ | $1,588 \pm 57$ | $1,564 \pm 24$ | $1,537 \pm 26$ |


![](https://cdn.mathpix.com/cropped/56860d5a-4d6e-46b8-be43-dc735bcd0906-5.jpg?height=636&width=1693&top_left_y=688&top_left_x=211)

Every time-step, each driver analyses upcoming roads to determine what cars and intersections constrain its speed, and decides whether it should change lanes. Drivers follow the shortest-distance route to their destination until they encounter a road already at its full capacity. Then they re-route, strictly preferring roads that are not at full capacity. This naturally diminishes the effects of congestion and gridlock.

## B. Experimental setup

An AORTA scenario is a complete encoding of a deterministic simulation, capturing aspects of traffic demand (the source, destination, departure time, and budget of every driver), intersections (whether auctions are performed or not), and simulation parameters (the following distance for cars, physical constraints of acceleration, and such). When comparing various metrics per city, the same scenario is simulated, with only intersection ordering modified.

In each experiment, 10,000 drivers begin their trip per hour for 3 hours, with a source and destination uniformly chosen from the entire city. Their budgets are uniformly distributed between $0 ¢$ (free-riders) and $500 ¢$. Simulations are run until all 30, 000 drivers finish their trip.

## C. Results

4 urban cities - Austin, Baton Rouge (BR), San Francisco (SF), and Seattle - were tested with various approaches for intersection ordering.

1) FIFO admits drivers in the order of their request, and cycles through phases in a fixed order for traffic signals. This mimics the status quo.
2) Equal treats each driver the same, picking the winner based on unweighted demand. This is equivalent to every driver always bidding 1 wkith the static wallet.
3) In Auctions, drivers bid using the fair wallet.
4) In Fixed, drivers always bid their priority, using the static wallet. Presumably, drivers could place their one bid up-front and receive that priority throughout their trip.

Every ordering except for FIFO can have the help of system bids or not, as described in section III-E. Each set of experiments per city was repeated with 3 different scenarios of 30,000 drivers.

The mean and standard deviation of several metrics for each run are given in Table I. Unweighted trip time is the sum of every driver's trip time. Weighted trip time is a weighted sum of every driver's trip time, where the driver's weight is equal to the initial budget they had available, plus $1 ¢$ to incorporate free-riders' times. Weighted times are normalized to match the scale of unweighted times.

As expected, FIFO, as the status quo, is generally a baseline. The exception is in Baton Rouge, where all orderings without system bids performed worse than FIFO. The contribution of system bids is unclear: in Baton Rouge, they appear to significantly help, but in Seattle, they hurt. Everywhere except in Austin, the results for Equal, Auction, and Fixed
with system bids have little differences, meaning they aided drivers with lower bids until they were nearly indistinguishable from drivers with higher bids. While the reduced times particularly in Baton Rouge suggest that orderings based on auctions can regulate traffic more effectively, further tests with tuned system bidding parameters and more trials are required to draw stronger conclusions.

In a true market, agents would express different risk preferences and attempt to strategize. Using just one strategy - the fair wallet - with different budgets does not yet introduce an appropriate level of diversity. In addition, the fair wallet has a caveat - it offers to pay some amount in each auction, but if other agents collaborate, then it pays less than its bid. Towards the end of the trip, the fair wallet has more funds remaining to distribute among fewer intersections, meaning it will bid higher.

## V. DISCUSSION OF SOCIAL EQUITY

In this section, we briefly discuss whether the proposed scheme prefers wealthy drivers. The concern about the distribution of benefits and costs among different demographic groups is both a political question [17], [18], and a legal one - in the United States, Executive Order 12898 (Federal Actions to Address Environmental Justice in Minority Populations and Low-Income Populations) requires transportation planning agencies to avoid "disproportionately high and adverse" effects on disadvantaged groups.

As Section III-E explains, we directly regulate this issue by setting reserve prices to protect drivers from waiting indefinitely. Another way to balance drivers with uneven budgets is to grant all drivers a fixed number of "credits" to use instead of money. These credits would be renewed per week or month, and drivers could spend them however they see fit - all at once for one fast trip, or spread out carefully. To be fair, credits should be tracked per driver, not per car, since wealthy drivers could afford multiple cars to get more credits.

## VI. CONCLUSIONS

This paper has introduced intersection auctions in a microsimulator framework for enabling drivers to express their preferences of time and cost. Rather than let an unequal distribution of wealth jeopardize social equity without limit, we regulate auctions using a benevolent system agent. In the future, our work will focus on three directions. First, we will increase the expressive power of agents by developing more powerful wallets. Second, we will explore more flexible routing algorithms to divide traffic among available paths in a way that respects a driver's budget. Finally, we will investigate the marginal costs of a single driver making different choices in routing or bidding, to enable wallets to predict the effects of their decisions.

## ACKNOWLEDGMENTS

This work has taken place in the Learning Agents Research Group (LARG) at the Artificial Intelligence Laboratory, The University of Texas at Austin. LARG research is supported in part by grants from the National Science Foundation (IIS-0917122), ONR (N00014-09-1-0658), and the Federal Highway Administration (DTFH61-07-H-00030).

The authors would like to thank Mandy Gabriel for useful discussions about game theory and for "rubber duck" debugging.

## References

[1] D. Schrank, B. Eisele, and T. Lomax, "2012 urban mobility report," Texas Transportation Institute, Tech. Rep., 2012.
[2] K. Dresner and P. Stone, "A multiagent approach to autonomous intersection management," Journal of Artificial Intelligence Research, vol. 31, pp. 591-656, March 2008.
[3] A. C. Pigou, The Economics of Welfare. London: Macmillan and Co., 1920.
[4] M. J. Beckmann, C. B. McGuire, and C. B. Winston, Studies in the Economics of Transportation. Connecticut: Yale University Press, 1956.
[5] S. D. Boyles, K. M. Kockelman, and S. T. waller, "Congestion pricing under operational, supply-side uncertainty," Transportation Research Part C, pp. 519-535, 2010.
[6] L. Gardner, S. D. Boyles, and S. T. Waller, "Quantifying the benefit of responsive pricing and travel information in the stochastic congestion pricing problem," Transportation Research Part A, vol. 45, pp. 204-218, 2011.
[7] R. B. Dial, "Network-optimized road pricing: Part I: a parable and a model," Operations Research, vol. 47, no. 1, pp. 54-64, 1999.
[8] -, "Network-optimized road pricing: Part II: algorithms and examples," Operations Research, vol. 47, no. 2, pp. 327-336, 1999.
[9] A. de Palma and R. Lindsey, "Information and usage of congestible facilities under different pricing regimes," Canadian Journal of Economics, vol. 31, no. 3, pp. 666-692, 1998.
[10] H. Yang, "Evaluating the benefits of a combined route guidance and road pricing system in a traffic network with recurrent congestion," Transportation, vol. 26, pp. 299-322, 1999.
[11] Y. Lou, Y. Yin, and J. Laval, "Optimal dynamic pricing strategies for high-occupancy/toll lanes," Transportation Research Part C, vol. 19, no. 1, pp. 64-74, 2011.
[12] K. Ozbay, E. F. Morgul, S. Ukkusuri, S. Iyer, and W. F. Yushimoto, "Mesoscopic simulation evaluation of dynamic congestion pricing strategies for New York City crossings," 2011, presented at the 90th Annual Meeting of the Transportation Research Board, Washington, DC.
[13] M. Vasirani and S. Ossowski, "A market-inspired approach for intersection management in urban road traffic networks," J. Artif. Intell. Res. (JAIR), pp. 621-659, 2012.
[14] E. H. Clarke, "Multipart pricing of public goods," Public Choice, vol. 11, no. 1, September 1971.
[15] T. Groves, "Incentives in teams," Econometrica, vol. 41, no. 4, pp. 617-31, July 1973.
[16] D. Carlino, M. Depinet, P. Khandelwal, and P. Stone, "Approximately orchestrated routing and transportation analyzer: Large-scale traffic simulation for autonomous vehicles," in Proceedings of the 15th IEEE Intelligent Transportation Systems Conference (ITSC 2012), September 2012.
[17] D. J. Forkenbrock and L. A. Schweitzer, "Environmental justice in transportation planning," Journal of the American Planning Association, vol. 65, pp. 96-111, 1999.
[18] J. Duthie, K. Cervenka, and S. T. Waller, "Environmental justice analysis: challenges for metropolitan transportation planning," Transportation Research Record, vol. 2013, pp. 8-12, 2007.

[^0]:    ${ }^{1}$ This is enforced with an invariant stating that if a driver has been accepted to an intersection, all drivers in front of them on the same queue have also been accepted. A queue of cars is defined per lane, so on roads with multiple lanes, drivers cannot change lanes if it would cause them to violate this invariant.

[^1]:    ${ }^{2}$ See http://code.google.com/p/road-rage/source/ browse/docs/itsc_2013_instructions.txt

