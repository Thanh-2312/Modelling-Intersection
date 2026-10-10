# Disaggregate Exposure Measures and Injury Frequency Models of Cyclist Safety at Signalized Intersections 

Luis F. Miranda-Moreno, Jillian Strauss, and Patrick Morency

This paper proposes a new approach to represent cyclist risk exposure. This approach considers disaggregate motor vehicle and cyclist flows and develops cyclist injury frequency models. Three definitions of risk exposure were used in this research, including aggregated flows, motor vehicle flows aggregated by movement type, and potential conflicts between motor vehicles and cyclists. As an application environment, a large sample of signalized intersections on the island of Montreal, Quebec, Canada, was used, along with data that comprised disaggregate motor vehicle and cyclist flows. Several negative binomial models were fitted to the data. This study showed that cyclist collisions were sensitive to changes in both cyclist and motor vehicle flows. A 10\% increase in bicycle flow was associated with a 4.4\% increase in the frequency of cyclist injuries. A 10\% increase in the total number of motor vehicles that passed through the intersection would result in a $\mathbf{3 . 4} \boldsymbol{\%}$ increase in cyclist injury occurrence. When motor vehicle flows were considered on the basis of movement type, right-turn movements had a great effect on injury occurrence. Similar results, which identified right turns as having the greatest effect on cyclist injuries, were produced when the impact of potential conflicts was determined. The number of bus stops in the proximity of the intersection increased cyclist injury occurrence. Some geometric design factors, such as the presence of a median, parking entrance, and the number of intersection legs, were tested. The effect, however, was found to be statistically nonsignificant.

Within the current context of climate change, energy, and health issues, the need is urgent to adapt to greener transportation systems, and push toward a higher mode share of active forms of transportation, specifically cycling. It is well recognized in the literature that cycling can reduce noise, air pollution, and greenhouse gases associated with travel while at the same time help integrate physical activity into daily life and consequently improve fitness and diminish obesity (1). Despite these recognized benefits, cyclists in North American cities in general, and in Montreal, Quebec, Canada, in particular, incur a higher risk of injuries that require hospitalization than do motor vehicle occupants (2, 3). When a motor vehicle and a

[^0]cyclist are involved, 100 out of 1,000 accidents require the hospitalization of the cyclist, and 10 out of 1,000 accidents result in a fatality. If a motor vehicle is not involved, 50 out of 1,000 accidents require hospitalization and less than one out of 1,000 results in a fatality (2). Over a 5-year period, from 1999 to 2003, 4,751 cyclists were injured on the island of Montreal, an average of 950 cyclists per year, and almost 60\% of their accidents occurred at an intersection (2). Montreal has experienced increases in both cyclist infrastructure and ridership in recent years (4). In response, local governments and transportation agencies have identified cyclist safety as a high priority toward the development of sustainable transportation.

Despite the substantial body of research, to date, many cyclist safety studies have focused on investigating the effect of specific factors on different levels of injury severity. These studies include the work of Attewell et al. (5), Kim et al. (6), and Eluru et al. (7). All of these studies have helped to identify severity factors, which include the influence of alcohol, bicycle helmet usage, cyclist and vehicle characteristics, speed limit, and collision types, among others. Few studies have looked at accident rates associated with the type of bicycle facility. In addition, these studies have mostly been confined to European countries [Reynolds et al. (1) and Elvik and Vaa (8)], with some exceptions in Canada [Aultman-Hall and Hall (9) and the recent work of Lusk et al. (10)]. Other studies have looked at the safety effects of certain treatments and roundabout designs (11-13).

An important issue that has yet to attract much attention is cyclist collision occurrence at signalized intersections. Among the few studies of the issue are those of Brüde and Larsson (14), Garder et al. (11), Jensen (12), Wang and Nihan (15), Turner et al. (16), Ma et al., (17), and Oh et al. (18). Similarly, the occurrences of cyclist injuries at intersections and their link to motor vehicle and bicycle flows is a relationship that has yet to receive the attention that it requires. Thus far, investigations have been limited to European and Asian cities. Studies on signalized intersections and cyclist safety are rare in North America. Few studies have taken into account full measures of risk exposure, including disaggregate cyclist and motor vehicle traffic flows and the interactions among the different movements. Most of the studies reported in the literature have been performed on relatively old data with relatively small samples of intersections. Finally, few recent studies have looked at the geometric design and built environment attributes at intersections.

The objectives of this paper are twofold: (a) to contribute to the small body of research literature that examines the link between cyclist injury counts and both motor vehicle and bicycle flows at signalized intersections and (b) to propose and evaluate the effect of different risk exposure measures, with controls for some geometric design and built environment characteristics. To achieve this goal,
different injury count regression models were developed by using alternative specifications of risk exposure measures.

To contribute to the important but limited body of literature on cyclist safety, this study responded to the current need to improve collision risk exposure measures, injury modeling methodologies, and data collection methods. Such methods are needed to identify the most appropriate road and bicycle facility designs and suitable countermeasures for improving bicycle safety at signalized intersections. This study focused on a sample of 753 signalized intersections on the island of Montreal. This research used injury count data from ambulance services, which had fewer underreporting and misallocation problems associated with them than did the police report data usually used in cyclist safety research. The number of cyclist injuries reported by the police was lower than it was in the ambulance data. The misallocation problem of the police reports resulted in part because of the use of the link-node method in which injury location was identified by using the distance from an intersection (3).

This paper is divided into several sections. The second section offers a review of the literature on bicycle safety, with particular focus on bicycle safety analysis at intersections. The third section describes the site selection and procedure followed to build the empirical application used in this research. The fourth section presents the conceptual framework and model formulation to analyze cyclist safety at signalized intersections. The fifth section shows the results (injury frequency models) and their implications. The sixth section provides a discussion of the results as well as the limitations of this study. The final section presents conclusions and directions for future work.

## LITERATURE REVIEW

In the transportation safety literature, various studies have been published on different issues related to cyclist safety. Most of these studies, however, have focused on the effectiveness of cyclist helmet use and other factors associated with the level of injury severity, such as vehicle, individual, weather, and environmental characteristics. Another important issue that has attracted less attention is the safety effectiveness of physically separated paths, such as those used in the Netherlands, Denmark, and more recently in Canada. These studies have attempted to evaluate the effectiveness of separated cycle tracks or other specific treatments in built paths (10). For a general literature review on the impact of transportation infrastructure on cyclist injuries and crashes, see Reynolds et al. (1). For a literature review on helmet effectiveness, see Attewell et al. (5). For cyclist and vehicle attributes, as well as weather and environmental factors associated with injury severity levels, see Kim et al. (6) and Eluru et al. (7).

Despite the importance of the issue, only a few studies have dealt with cyclist safety at intersections in an urban environment. They include Brüde and Larsson (14), Garder et al. (11), Jensen (12), Wang and Nihan (15), Turner et al. (16), Ma et al. (17), and Oh et al. (18). These studies were carried out in European or Asian countries. No studies of this type in North American cities have been reported in the literature. Other cyclist safety studies have used aggregated data at the level of cities, towns, or countries [Elvik (19) and Jacobsen (20)].

Brüde and Larsson collected police report data on accidents that occurred at a junction and involved a cyclist in 30 Swedish cities from 1983 to 1988 (14). The researchers expressed the cyclist accident rate as a function of the average, annual daily motor vehicle and cyclist flows. The exponents attributed to these variables in the equation reflected the different relationships that motor vehicle and bicycle flows had on accident rates. With a 10\% increase in traffic flow, the frequency of accidents increased by 5\%. Brüde and Larsson used this finding to explain that the presence of more motor vehicles increased the potential conflicts between vehicles and cyclists and therefore increased the occurrence of an accident (14). With a 10\% increase in bicycle flow, the frequency of accidents increased by $6.5 \%$. The probability that a cyclist would be involved in an accident decreased, however, which therefore created a safety in numbers effect (20).

Garder et al. carried out another study in Sweden that also focused on bicycle safety at junctions (11). They used a before-after analysis on a compilation of police report data and hospital accident data collected from January 1988 to September 1996 from Gothenburg, the second largest city in Sweden, to evaluate the safety effects of raised bicycle crossings. Different methods were employed, and the results were then combined by using a Bayesian approach. These methods included cyclist surveys, expert opinions, interactions between motor vehicles and cyclists, as well as a quantitative model on the basis of expert knowledge. In the study, 44 T-intersections received this treatment, and a sample of four intersections was used in the analysis. The raised bicycle crossing caused a decrease in motor vehicle speed, which reduced the number of accidents that occurred between motor vehicles and cyclists. The experts, however, emphasized that accident risk was more sensitive to bicycle speeds than to motor vehicle speeds, which were found to increase after the implementation of the raised crossing. From the videos processed in relation to conflicts, safety benefits were perceived for all modes. Cyclist safety was the least improved, compared with pedestrian and motor vehicle safety. Garder et al. suggested that any bicycle crossing could be made safer if it was both raised and painted in bright colors. Ten years later, Jensen performed a before-after analysis, which looked at the effects that intersection crossings that were painted blue had on cyclist safety (12). Jensen used a stepwise method on a sample of 65 signalized junctions in Copenhagen, Denmark, to analyze the safety effects as a function of the number of painted crossings. A case in which all four crossings were painted blue resulted in an increase in rear-end collisions as well as right-angle collisions between motor vehicles, because drivers had focused on the crossings and not on the traffic signals. Jensen suggested that only one crossing should be marked, namely, the one that had witnessed the most accidents and, furthermore, in cases in which there was more than one painted crossing, the paint should be removed from all but one.

In one of the most recent studies, Wang and Nihan estimated the risk of accidents that occurred between motor vehicles and bicycles at 115 four-legged, signalized intersections in Tokyo from 1992 to 1995 (15). In this study, the accidents were aggregated at an intersection approach level, as opposed to an intersection level. In other words, for four-legged intersections, accidents were recorded on the basis of the three types of movements: through movements, rightturn movements, and left-turn movements. The collision risk was evaluated separately for each movement, and consideration was given to the actual motor vehicle and bicycle flows that traveled through each approach. By using a statistical modeling approach, three negative binomial (NB) models were calibrated. In their modeling, Wang and Nihan adjusted for average daily bicycle and motor vehicle volumes, intersection location (with respect to downtown), speed limit, visual noise, as well as the width of the entering approach. Among their main findings was that an increase in bicycle volume was associated with a lower collision risk with turning vehicles, whereas a higher number of turning lanes and the presence of a wide
median significantly increased the risk of a collision when the vehicle was turning.

These previous studies consistently showed that cyclist crash risk depended on cyclist and motor vehicle flows with a nonlinear relationship. In other words, the risk faced by each cyclist declined as the number of cyclists increased. This phenomenon has been referred to as the safety-in-numbers effect (20), and Elvik reviewed recent studies that found a safety-in-numbers effect for both pedestrians and cyclists (19). Although these studies are useful, they suffer from several shortcomings such as the following:

- Most studies on cyclist collision occurrence modeling have taken into account total cyclist volumes as well as total motor vehicle traffic flows as a measure of risk exposure. In other words, models have been developed on the basis of aggregated flows: daily averages. Although aggregate measures are useful, they do not allow a complete observation of the impact of different movement types. More important, they do not fully represent the interactions (potential conflicts) for each approach and time.
- Few studies on bicycle safety have considered the geometric design and built environment attributes related to the layout of intersections (e.g., presence of bus stops, medians, number of approaches, presence of bicycle facilities). Most studies have looked at the effect of aggregate traffic and bicycle volumes on vehicle collision frequency, but few have incorporated geometric design and built environment characteristics.
- Most studies, in Europe and Asia, were not up-to-date or were done on the basis of data sets that included relatively small sample sizes.

As far as it is known, no studies of cyclist collision occurrence at signalized intersections have been published in North America. This paper thus attempts to address some of the above-mentioned research gaps by developing a methodology that includes the combination of different sources of data and the development of alternative exposure measures.

## SITE SELECTION AND DATA

The island of Montreal, Quebec, Canada, was used as the application environment. For this research, data were obtained from such local agencies as the Montreal Department of Public Health and the Montreal Department of Transportation. The steps required to achieve the objectives of this study included: (a) site selection and data inventory, (b) definition of risk exposure measures, and (c) development of collision occurrence models.

## Site Selection

For this research a detailed inventory was built for a sample of 753 intersections, which included information on motor vehicle flows per movement as well as bicycle flows per approach. Most of these intersections were located in the central neighborhoods of the city of Montreal. Their location and the magnitude of their flows are schematically presented in Figure 1. The bicycle flows in this figure are the aggregated flows from the 8-h count period for each particular intersection. The sum therefore captures all bicycle flows that passed through the intersection during the morning peak, noon period, and evening peak. The intersections involved in this study met the following two conditions: (a) recent cyclist and traffic counts were available, and $(b)$ counts had been taken between April 1 and November 30, when seasonal cycle tracks were open.

## Injury, Counts, and Geometric Data

## Bicycle Injury Data

For the intersections under analysis, data were included on all injured cyclists for whom an ambulance was dispatched after the occurrence of an accident on the island of Montreal over 9 years (from 2000 to 2008). Some summary statistics on the number of cyclist injuries are provided in Table 1. Urgences-Santé (Montreal's ambulance service) was a source of data and had a monopoly in the territory covered. For every call made to 911 in Montreal, the caller's address was automatically sent to Urgences-Santé, and the location of the cyclist's injury was validated over the phone. This location was instantly mapped in a geographic information system to dispatch and guide the ambulance. Collisions located within a 15-m radius around an intersection were labeled as intersection accidents. Ambulance service data appeared to have fewer underreporting and misallocation problems than the police report data usually used in published cyclist safety research. Police reports in the province of Quebec provided the street names as they were written by police officers at the accident scenes, and these names underwent an extensive validation process. If an accident involved two cyclists, it was counted as two injuries. In other words, the analysis was performed at the level of the individual and not that of the accident. The percentage of accidents that involved two cyclists was marginal, however. Although this data set was characterized by a low mean value of 1.0, the analysis involved a relatively large sample size (21).

## Cyclist and Motor Vehicle Traffic Flow Data

For all of the intersections studied, cyclist and traffic volumes were collected manually by the city of Montreal between 2008 and 2009. These volumes were obtained over three periods: ( $a$ ) morning peak (6 to 9 a.m.), (b) noon period (11 a.m. to 1 p.m.), and (c) evening peak (3:30 to 6:30 p.m.). Cyclist and motor vehicle movements were disaggregated for every 15-min interval and for each approach. The volumes for each movement could then be obtained over the 8-h period. The data at each intersection were collected on a weekday during the cycling season. Some summary statistics of the flows (left, right, and through-movement volumes) at the studied intersections are presented in Table 1.

## Geometric Design and Built Environment Characteristics

Data for some geometric design and built environment features were generated by using a geographic information system. These variables were generated for each intersection through the use of various sources (Table 1). These variables included the following:

- Number of approaches per intersection,
- Presence of a median in one or all intersection approaches,
- Presence of bus stops in the vicinity of the intersection (to account for the impact of buffer dimensions, different buffer sizes including 15 and 50 m were tested), and

![](https://cdn.mathpix.com/cropped/1b48d3b6-41ba-47c4-a8a8-10a32cabf663-4.jpg?height=1371&width=1764&top_left_y=213&top_left_x=183)
FIGURE 1 Intersections and their respective bicycle flows.

TABLE 1 Summary Statistics
| Variable | Mean ${ }^{a}$ | SD | Min. | Max. |
| :--- | :--- | :--- | :--- | :--- |
| Bicycle injury count ${ }^{b}$ | 1.0452 | 1.9895 | 0 | 30 |
| Total bike flows | 195.04 | 442.05 | 0 | 8,543 |
| Total traffic flows | 12,892.80 | 6,223.54 | 1,937 | 42,478 |
| Total left traffic | 1,367.85 | 1,368.67 | 0 | 12,195 |
| Total right traffic | 1,378.16 | 1,389.71 | 0 | 11,796 |
| Total through traffic | 10,146.79 | 5,526.00 | 980 | 38,521 |
| Presence of median (dummy 0/1) | 0.46 | 0.50 | 0 | 1 |
| Parking entrance (dummy 0/1) | 0.16 | 0.36 | 0 | 1 |
| Three legs (dummy 0/1) | 0.23 | 0.42 | 0 | 1 |
| Number of bus stops in 50-m buffer | 1.59 | 1.35 | 0 | 7 |


[^1]- Presence of a parking entrance in the proximity of an intersection (in the 15-m buffer).


## METHODOLOGY

As suggested in the literature, the individual risk faced by cyclists has been found to be nonlinear and often is referred to as the safetyin-numbers effect (19, 20). This effect implies that, as the number of cyclists increases and the traffic flow remains constant, the individual risk faced by each cyclist goes down. The absolute number of collisions increases, however, as cyclist, motor vehicle flow, or both, goes up in the absence of countermeasures. Most previous studies used aggregate crash risk exposure measures, such as the total number of motor vehicles or cyclists that were entering at an intersection (14, 19). These aggregate measures ignored the time variations and interactions among cyclist and motor vehicle flows across intersections. The effect of particular traffic movements on cyclist safety could not be estimated with measures such as total traffic and bicycle flows. Consequently, in the current study, the impact of different exposure measures was explored, including motor vehicle flows disaggregated by movement type and by the
number of potential opportunities for cyclist-vehicle crashes to occur at an intersection.

## Modeling Approach

To model cyclist injury occurrence, the standard Poisson-gamma or NB model was used. The number of injury counts $\left(Y_{i}\right)$ at intersection $i$ was Poisson distributed; injury occurrence generally was assumed to be governed by a random process (22). The standard NB or Poisson-gamma model for $Y_{i}$ can be represented in Equation 1 as

$$
Y_{i} \mid \theta_{i} \sim \operatorname{Poi}\left(\theta_{i}\right) \quad \text { with } \theta_{i}=\lambda_{i} \exp \left(\beta \tilde{x}_{i}+\epsilon_{i}\right)
$$

where $\theta_{i}$ stands for the mean injury count and $\exp \left(\boldsymbol{\epsilon}_{i}\right)$ stands for a multiplicative random effect of the model. (This error term represented all unobserved heterogeneities and is assumed to be independent.) The model is assumed to follow a gamma distribution, with both parameters equal to $1 / \kappa$,
where

$$
\begin{aligned}
\kappa= & \text { dispersion parameter; } \\
\lambda_{i}= & \text { measure of risk exposure, as defined in Equa- } \\
& \text { tions } 2 \text { to } 4 ; \\
\tilde{x}_{i}= & \text { geometric or built environment, site-specific } \\
& \text { attributes; and } \\
\beta=\left(\beta_{0}, \ldots, \beta_{k}\right)^{\prime}= & \text { vector of regression parameters estimated from } \\
& \text { the data. }
\end{aligned}
$$

## Definition of Risk Exposure Measures

To capture the specific contribution of the movement types (left, right, and through movements) on the mean number of cyclist injuries, alternative risk exposure measures were proposed. To explain these exposure measures, a graphical representation of the different movements in a typical four-leg intersection is shown in Figure 2. The traditional aggregate and proposed disaggregate exposure measures are defined in the following subsections.

## Total Cyclist and Vehicle Flows

This classical measure of risk exposure usually is represented by the following (19, 23):

$$
\lambda_{i}=\alpha_{0} B_{i}^{\alpha_{1}} V_{i}^{\alpha_{2}}
$$

where, as defined in Table 2, $B_{i}$ and $V_{i}$ are the total bicycle and motor vehicle flows observed during a period (in this case 8 h) at intersection $i(i=1, \ldots, n)$, and $\alpha_{0}, \alpha_{1}$, and $\alpha_{2}$ are model parameters to be estimated from the data.

## Disaggregate Flows by Movement Type

The aim of this measure is to observe the impact of each particular movement. As discussed in previous studies, the safety effect of right turns versus left turns is expected to be different. In the form of an equation, this exposure measure is represented as

$$
\lambda_{i}=\beta_{0} B_{i}^{\beta_{1}} V_{\mathrm{li}}^{\beta_{2}} V_{\mathrm{ri}}^{\beta_{3}} V_{\mathrm{ti}}^{\beta_{4}}
$$

where, again, $B_{i}$ is the total bicycle flow, and traffic flow is disaggregated by the movement types (left, right, and through flows) denoted by $V_{\mathrm{li}}, V_{\mathrm{ri}}$, and $V_{\mathrm{ti}}$, respectively. For more details, refer to Table 2. In addition, $\beta_{1}, \ldots, \beta_{4}$ are model parameters that measure the effect of each movement on the mean number of injury counts.

## Disaggregate Cyclist-Vehicle Potential Conflicts by Movement Type

This measure is expressed by the following equation:

$$
\lambda_{i}=\gamma_{0} C_{\mathrm{li}}^{\gamma_{1}} C_{\mathrm{ri}}^{\gamma_{2}} C_{\mathrm{ti}}^{\gamma_{3}}
$$

![](https://cdn.mathpix.com/cropped/1b48d3b6-41ba-47c4-a8a8-10a32cabf663-5.jpg?height=748&width=1242&top_left_y=1727&top_left_x=443)
FIGURE 2 Typical four-leg intersection and movements associated with it.

TABLE 2 Risk Exposure Measures for Typical Four-Leg Intersection
| Risk Exposure Definition | Notation | Definition | Movements ${ }^{a}$ |
| :--- | :--- | :--- | :--- |
| 1, 2 | $B_{i}$ | Total bicycle flow observed during 8-h period at intersection $i(i=1, \ldots, n)$ | $1+5+9+13$ |
| 1 | $V_{i}$ | Total motor vehicle flow during the 8-hour period | $\begin{gathered} 2+3+4+6+7+8+10+ \\ 11+12+14+15+16 \end{gathered}$ |
| 2 | $V_{\mathrm{li}}$ | Total motor vehicle left turns per intersection | $4+8+12+16$ |
| 2 | $V_{\text {ri }}$ | Total motor vehicle right turns per intersection | 2 + 6 + 10 + 14 |
| 2 | $V_{\mathrm{ti}}$ | Total motor vehicle through flows per intersection | 3 + 7 + 11 + 15 |
| 3 | $V_{\text {lip }} \times B_{\text {lip }}$ | $V_{\text {lip }}=$ motor vehicle left turns in each $15-\min$ interval $p$, and $p=1, \ldots, 32$ intervals of 15 min <br> $B_{\text {lip }}=$ bicycle flow in the same 15 min; potentially conflicts with motor vehicle left turns | $\begin{aligned} & (4 \times 5)+(8 \times 9)+(12 \times 13)+ \\ & (16 \times 1) \end{aligned}$ |
| 3 | $V_{\text {rip }} \times B_{\text {rip }}$ | $V_{\text {rip }}=$ motor vehicle right turns in each $15-\mathrm{min}$ interval $p$, and $p=1, \ldots, 32$ intervals of 15 min <br> $B_{\text {rip }}=$ bicycle flow in the same 15 min ; potentially conflicts with motor vehicle right turns | $\begin{aligned} & (6 \times 1)+(10 \times 5)+(14 \times 9)+ \\ & (2 \times 13) \end{aligned}$ |
| 3 | $V_{\text {tip }} \times B_{\text {tip }}$ | $V_{\text {tip }}=$ motor vehicle through movements in each $15-\min$ interval $p$, and $p=1, \ldots, 32$ intervals of 15 min <br> $B_{\text {tip }}=$ bicycle movements in the same 15 min ; potentially conflicts with motor vehicle through movements | $\begin{aligned} & (3+11) \times(1+9)+(7+5) \times \\ & (5+13) \end{aligned}$ |


${ }^{a}$ See Figure 2.
where $C_{\mathrm{li}}, C_{\mathrm{ri}}$, and $C_{\mathrm{ti}}$ stand for cyclist-vehicle left, right, and through potential conflicts during 8 h, respectively. These values are obtained by adding up the potential conflicts per movement type:

$$
\begin{aligned}
& C_{\mathrm{li}}=\sum_{p=1}^{P} B_{\mathrm{lip}} * V_{\mathrm{lip}} \\
& C_{\mathrm{ri}}=\sum_{p=1}^{P} B_{\mathrm{rip}} * V_{\mathrm{rip}}
\end{aligned}
$$

and

$$
C_{\mathrm{ti}}=\sum_{p=1}^{P} B_{\mathrm{tip}} * V_{\mathrm{tip}}
$$

where, as defined in Table 2,

$$
\begin{aligned}
V_{\text {lip }}, V_{\text {rip }}, \text { and } V_{\text {tip }}= & \text { motor vehicle left turn, right turn, and through } \\
& \text { flows in each } 15-\text { min interval; } \\
B_{\text {lip }}, B_{\text {rip }}, \text { and } B_{\text {tip }}= & \text { conflicting bicycle flows in the same } 15-\mathrm{min} \\
& \text { interval, respectively; and } \\
\gamma_{1}, \ldots, \gamma_{3}= & \text { model parameters that measure the effect of } \\
& \text { each potential conflict. }
\end{aligned}
$$

Perpendicular bicycle flows in principal should not conflict with motor vehicle through traffic. Driver and cyclist violations do exist, however.

## RESULTS

According to the modeling approach and measures of exposure previously defined, different NB models were fitted to the data under analysis. The results of four models with different measures of exposure, geometric design, and built environment variables are presented in Table 3. The estimated coefficients and corresponding $p$-values are presented in this table for each model. In Table 4, to evaluate the goodness of fit of each model, Akaike information criterion was used, defined as $-2 \log (L)+2 k$, where $k$ is the number of model parameters, and $L$ is the maximized value of the model likelihood function. From the results presented in those tables, the following observations can be made about the models:

Model 1. In this model, risk exposure was represented in the traditional manner by using the total flows as defined in Equation 2. In this case, the total bicycle and motor vehicle flows were the counts observed during 8 h. The results showed that bicycle flow was a significant determinant, with a coefficient of 0.44. This value was consistent with those obtained in previous studies and documented by Elvik (19). This finding implies that a $10 \%$ increase in bicycle flow will increase cyclist injuries by 4.4\%. Total motor vehicle flows were also significant, with a coefficient of 0.34 . From the estimated value and the $p$-value of the dispersion parameter, overdispersion in the data also was confirmed.

Model 2. In this model, as defined in Equation 3, the impact of traffic exposure on collision frequency was decomposed into the three main movements: total left turn, total right turn, and total through motor vehicle flows. The results demonstrated important differences between the movement types. Total motor vehicle left and right turns had statistically significant effects on cyclist safety at intersections. For motor vehicle right turns, the estimated parameter was 0.28, which meant that a 10\% increase in right turns would cause a $2.8 \%$ increase in the expected number of injuries. A 10 \% increase in motor vehicle left turns would result in a 1.2\% increase in cyclist injury occurrence. With regard to bicycle flows, the impact remained stable, with a parameter of 0.44. In terms of goodness of fit, this model fit the data better than Model 1.

Model 3. In this model, the effect of some geometric and built environment variables was explored, including the presence of a median, the number of approaches, the presence of a parking entrance, and bus stops in a 50-m buffer. The presence of a median in one or both approaches related negatively to cyclist injury risk. Its effect, however, was not statistically significant. The effect of bus stops was positive, with a small $p$-value. The model provided a better fit to the data than did Model 2; see the values for Akaike information criterion in Table 4.

TABLE 3 Multivariate Results
| Variable | Model 1 |  | Model 2 |  | Model 3 |  | Model 4 |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | Coeff. | $p$-Value | Coeff. | $p$-Value | Coeff. | $p$-Value | Coeff. | $p$-Value |
| Lane total bike flows | 0.441 | . 000 | 0.436 | . 000 | 0.438 | . 000 | na | na |
| Lane total traffic flows | 0.338 | . 002 | na | na | na | na | na | na |
| Lane total left-turn traffic | na | na | 0.122 | . 012 | 0.122 | . 014 | na | na |
| Lane total right-turn traffic | na | na | 0.280 | . 000 | 0.246 | . 000 | na | na |
| Lane total through traffic | na | na | 0.062 | . 512 | 0.027 | . 797 | na | na |
| Total left-turn conflicts | na | na | na | na | na | na | 0.101 | . 002 |
| Total right-turn conflicts | na | na | na | na | na | na | 0.165 | . 000 |
| Total through conflicts | na | na | na | na | na | na | 0.124 | . 001 |
| Geometric or built environment |  |  |  |  |  |  |  |  |
| Three legs | na | na | na | na | 0.051 | . 712 | 0.113 | . 421 |
| Parking entrance | na | na | na | na | -0.081 | . 644 | -0.089 | . 606 |
| Presence of median | na | na | na | na | -0.054 | . 667 | -0.069 | . 535 |
| Number of bus stops in 50-m buffer | na | na | na | na | 0.138 | . 001 | 0.103 | . 010 |
| Constant | -5.229 | . 000 | -5.366 | . 000 | -5.040 | . 000 | -3.005 | . 000 |


Note: Coeff. = coefficient; na = not applicable.

Model 4. In this model, defined by Equation 5, the three types of potentially conflicting movements were statistically significant. This model confirmed the greater effect of right-turn potential conflicts (with a parameter of 0.165) than left-turn and through potential conflicts. Results similar to those for Model 3 were obtained for the geometric and built environment characteristics. The fit of the model was not as good as it was for Model 3, but it was much better than for Model 1. The individual impact of each variable was tested by using univariate models and a correlation matrix. These results were consistent with those across all models (Models 1 to 4).

## DISCUSSION OF RESULTS

The results of this study suggest that bicycle safety at signalized intersections is significantly affected by cyclist volumes and traffic flows, in particular the magnitude of the right-turn motor vehicle movements or of right-turn potential conflicts. This work suggests that particular attention be paid to right turns, which should be reduced or treated with specific countermeasures, while other important functioning characteristics of the intersection are maintained.

This study suggests that some intersection environments, such as ones with bus stops, are associated with higher injury risk, which accords with the recent work of Ma et al. (17). The link between some geometric design characteristics and cyclist injury count was investigated, but its effects were not statistically significant. These

TABLE 4 Model Goodness-of-Fit Statistics
| Statistic | Model 1 | Model 2 | Model 3 | Model 4 |
| :--- | :--- | :--- | :--- | :--- |
| Akaike information criterion | 1,977.8 | 1,935.4 | 1,931.7 | 1,941.7 |
| Dispersion parameter | 1.11 | 0.95 | 0.92 | 0.92 |


results, however, should be seen as preliminary. More research is needed on the basis of more data, and other study designs, such as before-after observation or a control-group comparison approach.

These current results do suggest that the treatment of total traffic, right- or left-turn traffic flows, and conflicts can significantly improve cyclist safety. Potential countermeasures could include the reduction of turning radii that force slower vehicle speeds, use of an exclusive bicycle and pedestrian signal phase, and a separate left-turn phase, along with a pedestrian signal. The prohibition of left and right movements, a common practice in Montreal, could simply move the problem to another location. Employment of this countermeasure could have a negative impact on network connectivity, travel times, and delays. It could, however, be justified in situations with heavy pedestrian or cyclist volumes. Despite recent developments, little guidance is available on safety designs and countermeasures for cyclists at signalized intersections in North America. More research is urgently needed to identify effective safety treatments.

In the development of guidance, international experience should be considered. Some intersection treatments and priority traffic signals used in Western Europe (e.g., in Dutch, Danish, British, and German cities) could be evaluated for use at urban intersections in North America, such as (a) advanced green lights for cyclists, (b) colored bicycle lanes through intersections, (c) bicycle-specific signals and signal phases, ( $d$ ) advanced stop line for cyclists, ( $e$ ) synchronization of traffic signals at cyclist speeds to ensure consecutive green lights for cyclists, ( $f$ ) light-emitting diode lane lights to reduce the risk of right-turn collisions, and $(g)$ speed management strategies. When a separated bicycle path runs parallel alongside a road, a recommended design is to bend the cycle track toward the main road, so that both the cyclist and the driver travel at an angle at which they have a better view of one another as they approach the intersection. Garder et al. also proposed that separated bicycle paths be cut some short distance before the intersection, which not only would improve visibility but also cause cyclists to feel less safe and therefore would influence them to pay more attention at the intersection (24). Further research on these alternative treatments and
designs is required, however, to determine the best practices for North American cities.

This study has some limitations. The traffic and bicycle counts were taken at the end of the period of analysis and were not available for each year of the study period. This limitation may have introduced some bias, because risk exposure may have evolved differently across intersections over time. Some unmeasured factors might have affected the observed effect of right turns, if, for example, intersections with more motor vehicle right turns had an added right-turn lane or an increased turning radius. Other geometric and built environment variables should be tested to verify this potential issue.

More than 700 intersections were included in this study, but they were not randomly selected. Other appropriate study designs should be used (e.g., observational before-after analysis) to evaluate the effect of some geometric design and built environment characteristics. Risk exposure measures included potential conflicting movements, but no actual conflicts were included as a measure. Data were not available on red light violations for either cyclists or motor vehicles. These data could be collected by using video sensors and used to validate these results. Finally, flows were collected during different months and in the presence of different weather conditions. Correction factors therefore should be developed to standardize flows, particularly cyclist volumes, which are sensitive to temporal and weather variations (4).

## CONCLUSIONS AND FUTURE WORK

Intersections present serious safety concerns for cyclists. To encourage current motorized road users to make the switch to cycling, or even to keep cyclists on the road, intersection cyclist safety must be addressed. To date, however, not many studies have been carried out in North America in which the main research focus has been on intersections. This current study proposed the use of disaggregate risk exposure measures to study cyclist injury occurrence at signalized intersections. For this purpose, various risk exposure and collision occurrence models were developed with combined data sources. The primary conclusions of this study were the following:

1. The number of cyclist collisions was sensitive to changes in cyclist and motor vehicle flows. Injury numbers increased about half as fast as cyclist numbers, which was consistent with previous work (19).
2. After traffic flows were separated into three constituent movements, the right-turn movement was found to have the greatest effect on the number of cyclist collisions. In a consideration of potential conflicts as a measure of risk exposure, right-turn potential conflicts with cyclists were found to be more significant than the other conflicts.
3. Built environment attributes, such as the presence of bus stops, presented safety issues for cyclists. Other geometric characteristics, such as the effect of a median and parking entrance, were tested. Their effects were not statistically significant, however.

As a part of future work, a larger sample of intersections will be used to investigate the impact of specific geometric design and built environment characteristics, such as the presence of left-turn lanes, road width, and traffic controls. To determine the link between cyclist injury occurrence and conflicts, video analysis should be used to obtain actual conflicts. Automatic count data that come from several permanent stations (with bicycle and motor vehicle loop detectors) will be used to generate expansion factors to scale up to annual average daily flows and correct for weather. For the research reported in this paper, crash movement data and turning volumes for bicycle movements were not available. Data also will be collected to look at the effect of turning cyclist flows. It will then be important to relate various turning movement flows to bicycle injury collisions per approach, rather than to all collisions. Further studies are also required to determine the safety effectiveness of bicycle facilities at intersections. Observational before-after or control-case studies are therefore recommended. It would be interesting to compare crashes reported through the police with ambulance data. More research is also needed to look closer at the different types of intersections, including nonsignalized intersections. This research agenda is expected to contribute to the identification of effective safety countermeasures to protect cyclists at intersections.

## ACKNOWLEDGMENTS

The financial support of the Natural Sciences and Engineering Research Council of Canada is acknowledged. The authors thank the City of Montreal Department of Transportation for providing the count data.

## REFERENCES

1. Reynolds, C. C. O., M. A. Harris, K. Teschke, P. A. Cripton, and M. Winters. The Impact of Transportation Infrastructure on Bicycling Injuries and Crashes: A Review of the Literature. Environmental Health, Vol. 8, No. 47, 2009, pp. 1-19.
2. Vélo Québec, 2005. L'Etat du vélo au Québec en 2005. Quebec, Canada, 2005.
3. Morency, P., and M.-S. Cloutier. Distribution Géographique des Blessés de la Route sur L'île de Montréal (1999-2003). Report. Direction de santé publique de Montréal, Agence de développement de réseaux locaux de services de santé et de services sociaux. Montréal, Quebec, Canada, 2005.
4. Miranda-Moreno, L., and T. Nosal. A Look at Weather's Impact on Physically Separated Cycling Facilities and Temporal Trends in an Urban Environment. Presented at 90th Annual Meeting of the Transportation Research Board, Washington D.C., 2011.
5. Attewell, R. G., K. Glase, and M. McFadden. Bicycle Helmet Efficacy: A Meta-Analysis. Accident Analysis and Prevention, Vol. 33, 2001, pp. 345-352.
6. Kim, J. K., S. Kim, G. F. Ulfarsson, and L. A. Porrello. Cyclist Injury Severities in Bicycle-Motor Vehicle Accidents. Accident Analysis and Prevention, Vol. 39, 2007, pp. 238-251.
7. Eluru, N., C. R. Bhat, and D. A. Hensher. A Mixed Generalized Ordered Response Model for Examining Pedestrian and Cyclist Injury Severity Level in Traffic Crashes. Accident Analysis and Prevention, Vol. 40, 2008, pp. 1033-1054.
8. Elvik, R., and T. Vaa. The Handbook of Road Safety Measures. Elsevier, New York, 2004.
9. Aultman-Hall, L., and F. L. Hall. Ottawa-Carleton Commuter Cyclist On- and Off-Road Incident Rates. Accident Analysis and Prevention, Vol. 30, 1998, pp. 29-43.
10. Lusk, A. C., P. G. Furth, P. Morency, L. F. Miranda-Moreno, W. C. Willett, and J. T. Dennerlein. Risk of Injury for Bicycling on Cycle Tracks Versus in the Street. Injury Prevention, 2011.
11. Garder, P., L. Leden, and U. Pulkkinen. Measuring the Safety Effect of Raised Bicycle Crossings Using a New Research Methodology. In Transportation Research Record 1636, TRB, National Research Council, Washington D.C., 1998, pp. 64-70.
12. Jensen, S. U. Safety Effects of Blue Crossings: A Before-After Study. Accident Analysis and Prevention, Vol. 40, 2008, pp. 742-750.

13. Hels, T., and I. Orozova-Bekkevold. The Effect of Roundabout Design Features on Cyclist Accident Rate. Accident Analysis and Prevention, Vol. 39, 2007, pp. 300-307.
14. Brüde, U., and J. Larsson. Models for Predicting Accidents at Junctions Where Pedestrians and Cyclists Are Involved. How Well Do They Fit? Accident Analysis and Prevention, Vol. 25, 1993, pp. 499-509.
15. Wang, Y., and N. L. Nihan. Estimating the Risk of Collisions Between Bicycles and Motor Vehicles at Signalized Intersections. Accident Analysis and Prevention, Vol. 36, 2004, pp. 313-321.
16. Turner, S., S. Binder, and A. Roozenburg. Cycle Safety: Reducing the Crash Risk. Research Report 389. New Zealand Transport Agency, Wellington, New Zealand 2008.
17. Ma, M., X. Yan, M. Abdel-Aty, H. Huang, and X. Wang. Safety Analysis of Urban Arterials Under Mixed-Traffic Patterns in Beijing, China. In Transportation Research Record: Journal of the Transportation Research Board, No. 2193, Transportation Research Board of the National Academies, Washington, D.C., 2010, pp. 105-115.
18. Oh, J., J. Jun, E. Kim, and M. Kim. Assessing Critical Factors Associated with Bicycle Collisions at Urban Signalized Intersections. Presented at 87th Annual Meeting of the Transportation Research Board, Washington, D.C., 2008.
19. Elvik, R. The Non-Linearity of Risk and the Promotion of Environmentally Sustainable Transport. Accident Analysis and Prevention, Vol. 41, 2009, pp. 849-855.
20. Jacobsen, P. L. Safety in Numbers: More Walkers and Bicyclists, Safer Walking and Cycling. Injury Prevention, Vol. 9, 2003, pp. 205-209.
21. Lord, D. Modeling Motor-Vehicle Crashes Using Poisson-Gamma Models: Examining the Effects of Low Sample Mean Values and Small Sample Size on the Estimation of the Fixed Dispersion Parameter. Accident Analysis and Prevention, Vol. 38, No. 4, 2006, pp. 751-766.
22. Lord, D., S. P. Washington, and J. N. Ivan. Poisson, Poisson-Gamma and Zero Inflated Regression Models of Motor-Vehicle Crashes: Balancing Statistical Fit and Theory. Accident Analysis and Prevention, Vol. 37, No. 1, 2005, pp. 35-46.
23. Miaou, S.-P., and D. Lord. Modeling Traffic Crash-Flow Relationships for Intersections: Dispersion Parameter, Functional Form, and Bayes Versus Empirical Bayes Methods. In Transportation Research Record: Journal of the Transportation Research Board, No. 1840, Transportation Research Board of the National Academies, Washington, D.C., 2003, pp. 31-40.
24. Garder, P., L. Leden, and T. Thedeen. Safety Implications of Bicycle Paths at Signalized Intersections. Accident Analysis and Prevention, Vol. 26, 1994, pp. 429-439.

All errors and the views expressed in this research paper are those of the authors.

The Safety Data, Analysis, and Evaluation Committee peer-reviewed this paper.


[^0]:    L. F. Miranda-Moreno and J. Strauss, Department of Civil Engineering and Applied Mechanics, McGill University, Macdonald Engineering Building, 817 Sherbrooke Street West, Montreal, Quebec H3A 2K6, Canada. P. Morency, Montreal Department of Public Health, Montreal Health and Social Services Agency, 1301 Sherbrooke Street East, Montreal, Quebec H2L 1M3, Canada. Corresponding author: L. F. Miranda-Moreno, luis.miranda-moreno@mcgill.ca.

    Transportation Research Record: Journal of the Transportation Research Board, No. 2236, Transportation Research Board of the National Academies, Washington, D.C., 2011, pp. 74-82.
    DOI: 10.3141/2236-09

[^1]:    Note: SD = standard deviation; min = minimum; max = maximum.
    ${ }^{a}$ For dummy variables "mean" represents the proportions.
    ${ }^{b}$ For period of analysis, approximately 58\% of intersections had zero accidents, 21\% had one accident, 11\% had two accidents, and the remaining 10\% had three or more accidents.

