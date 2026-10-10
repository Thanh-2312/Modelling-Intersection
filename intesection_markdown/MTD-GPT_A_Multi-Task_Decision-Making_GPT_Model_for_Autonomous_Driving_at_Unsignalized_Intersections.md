# MTD-GPT: A Multi-Task Decision-Making GPT Model for Autonomous Driving at Unsignalized Intersections 

Jiaqi Liu, Peng Hang, Member, IEEE, Xiao Qi , Jianqiang Wang, and Jian Sun


#### Abstract

Autonomous driving technology is poised to transform transportation systems. However, achieving safe and accurate multi-task decision-making in complex scenarios, such as unsignalized intersections, remains a challenge for autonomous vehicles. This paper presents a novel approach to this issue with the development of a Multi-Task Decision-Making Generative Pre-trained Transformer (MTD-GPT) model. Leveraging the inherent strengths of reinforcement learning (RL) and the sophisticated sequence modeling capabilities of the Generative Pre-trained Transformer (GPT), the MTD-GPT model is designed to simultaneously manage multiple driving tasks, such as left turns, straight-ahead driving, and right turns at unsignalized intersections. We initially train a single-task RL expert model, sample expert data in the environment, and subsequently utilize a mixed multi-task dataset for offline GPT training. This approach abstracts the multi-task decisionmaking problem in autonomous driving as a sequence modeling task. The MTD-GPT model is trained and evaluated across several decision-making tasks, demonstrating performance that is either superior or comparable to that of state-of-the-art single-task decision-making models.


## I. INTRODUCTION

Autonomous driving technology promises to bring revolutionary changes to transportation systems [1], [2], yet ensuring safe and accurate decision-making in complex scenarios remains a significant challenge for autonomous vehicles (AVs) [3]. Intersections represent one of the most challenging driving scenarios, where decision-making typically encompasses tasks such as making left turns, proceeding straight, and making right turns. Extensive research has investigated decision-making and interaction issues for autonomous vehicles in intersection scenarios [1]. In these studies, rule-based methods (such as PET [4]) often struggle to handle decision-making in complex scenarios, and game theory-based methods typically require the setting of strong assumptions and pose challenges in terms of computational efficiency [5], [6].

Reinforcement learning (RL), due to its exceptional learning capabilities and computational efficiency, has been widely applied in the design of decision-making algorithms

[^0]for AV [7]-[9]. However, these methods mostly use a single model to handle different tasks, and utilizing a single model to cope with multiple autonomous driving decision-making scenarios and tasks remains a significant challenge for RL [8].

To enhance the generalization capabilities and performance of RL, researchers have recently revisited and reformulated RL using Transformer models, achieving promising results [10]. Inspired by these works, we treat the autonomous driving multi-task decision-making problem as a sequence modeling and prediction problem, using the Generative Pre-trained Transformer (GPT) model to learn driving data and generate action decisions.

Concurrently, we introduce a pipeline for training GPT in multi-task decision-making, with guidance from RL experts: initially, we train an expert model for a single decisionmaking task using RL algorithms, followed by sampling expert data in the environment; ultimately, we utilize a mixed multi-task dataset for offline GPT training. Based on the training pipeline and GPT-2 [11], we propose a Multi-Task Decision-Making GPT (MTD-GPT) model for the multitask decision-making of autonomous driving at unsignalized intersections, which is capable of simultaneously executing the decision-making tasks of turning left, going straight, and turning right at unsignalized intersections.

We train multiple MTD-GPT models with different parameter scales and evaluate them in several decision-making tasks at intersections through simulations. We find that the performance of MTD-GPT across various tasks is superior to or on par with state-of-the-art (SOTA) single-task decisionmaking experts.

Our contributions can be summarized as follows:

- We abstract the autonomous driving multi-task decisionmaking problem as a sequence modeling problem and propose a Multi-Task Decision-Making GPT (MTDGPT) model based on GPT-2.
- We design a pipeline for training MTD-GPT, utilizing RL algorithms to train single-task decision-making experts and providing guidance for MTD-GPT learning using expert data.
- We assess MTD-GPT's performance on various decision-making tasks at unsignalized intersections, finding that our model's performance is either superior or comparable to that of outstanding single-task decision-making RL models.

## II. Related Works

## A. Decision-making of AV at Intersection

In recent years, considerable research has been devoted to the problems of decision-making and interaction of AV in intersection scenarios. These studies have employed various approaches, including ruled-based methods [12], gametheoretic methods [5], [13], and data-driven techniques [8], [9], [14], in which RL is recognized as a flexible, efficient, and potent method. However, its widespread implementation is hindered by several obstacles, one of which is training a RL model that can effectively manage a range of driving situations and decision-making tasks [8]. Kai et al. [8] formulated multitask objectives as a four-dimensional vector and devised a vectorized reward function to tackle multi-task decision-making issues at intersections. Liu et al. [15] introduced a multi-task safe reinforcement learning framework, resulting in more secure intersection decisionmaking for autonomous driving.

Nonetheless, these approaches are heavily dependent on the intricate design of state spaces and model components, posing difficulties when extending their application to broader and more complex scenarios. In this study, we utilize the GPT model for multi-task decision-making, which circumvents the need to create specific structures and components for individual subtasks, potentially improving the model's adaptability and generalization abilities.

## B. Transformer in Reinforcement Learning

The remarkable accomplishments of Transformer models in domains such as natural language processing (NLP) [16] and computer vision (CV) [17] in recent years have generated considerable interest. Consequently, numerous researchers have attempted to apply Transformers to the RL domain, achieving remarkable results [18]-[20]. A notable approach entails converting RL problems into sequence modeling tasks and directly employing Transformer architectures for learning, which showcase exceptional performance and generalization properties [10], [20], [21].

In this study, we recast the autonomous driving decisionmaking problem as a sequence modeling task and employ a Transformer architecture identical to that of GPT-2 to learn from the data, aiming to achieve multi-task decision-making at unsignalized intersections.

## III. Problem Formulation

## A. Scenario Description

The problem of multi-task decision-making for AV at unsignalized intersections is considered. Specifically, we define a single-lane cross-shaped unsignalized intersection. A couple of human-driven vehicles (HVs) with different driving styles and intentions appear randomly from different directions and positions. After interacting with the HVs, the AV needs to complete the tasks of turning left, going straight, or turning right. The scenario we study is shown in Fig. 1

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-2.jpg?height=763&width=786&top_left_y=174&top_left_x=1115)
Fig. 1: The intersection scenario for multi-task decisionmaking in our research.

## B. Vehicle Kinematics

In our problem, AV actions determined by the RL expert and MTD-GPT model are converted to low-level steering and acceleration signals via a closed-loop PID controller. Vehicle position and heading are controlled by Eq. (1) and Eq. (2), respectively:

$$
\begin{aligned}
v_{\text {lat }, r} & =-K_{p, \text { lat }} \Delta_{\text {lat }}, \\
\Delta \psi_{r} & =\arcsin \left(\frac{v_{\text {lat }, r}}{v}\right)
\end{aligned}
$$

where $\Delta_{\text {lat }}$ is the lateral position of the vehicle with respect to the lane center-line, $v_{\text {lat }, r}$ is the lateral velocity command, $\Delta \psi_{r}$ is a heading variation to apply the lateral velocity command.

$$
\begin{aligned}
\psi_{r} & =\psi_{L}+\Delta \psi_{r} \\
\dot{\psi}_{r} & =K_{p, \psi}\left(\psi_{r}-\psi\right) \\
\delta & =\arcsin \left(\frac{1}{2} \frac{l}{v} \dot{\psi}_{r}\right)
\end{aligned}
$$

where $\psi_{L}$ is the lane heading, $\psi_{r}$ is the target heading to follow the lane heading and position, $\dot{\psi}_{r}$ is the yaw rate command, $\delta$ is the front wheels angle control, $K_{p, \text { lat }}$ and $K_{p, \psi}$ are the position and heading control gains.

Vehicle motion is determined by a Kinematic Bicycle Model [22]:

$$
\begin{aligned}
\dot{x} & =v \cos (\psi+\beta) \\
\dot{y} & =v \sin (\psi+\beta) \\
\dot{v} & =a \\
\dot{\psi} & =\frac{v}{l} \sin \beta \\
\beta & =\tan ^{-1}(1 / 2 \tan \delta)
\end{aligned}
$$

where $(x, y)$ is the vehicle position, $v$ is forward speed, $\psi$ is heading, $a$ is the acceleration command, $\beta$ is the slip angle
at the center of gravity, $\delta$ is the front wheel angle used as a steering command.
C. Multi-Task Partially Observable Markov Decision Process

We describe the multi-task decision-making process of AV in the traffic environment as a multi-task partially observable Markov Decision Process (POMDP), which can be formulated by $M=\left(\mathcal{S}, \mathcal{A}, \mathcal{O}, \mathscr{P},\left\{r_{i}\right\}_{i=1}^{N}\right)$, where $\mathcal{S}$ is the state space; $\mathcal{A}$ is the action space; $\mathcal{O}$ is the observation space; $\mathscr{P}$ : $\mathcal{S} \times \mathcal{A} \rightarrow \mathbb{R}$ is the transition function; $\left\{r_{i}\right\}_{i=1}^{N}$ is a finite set of reward functions with different tasks, $r_{i}$ denotes the reward function of task $i$. The goal of the offline GPT model is to find a policy $\pi_{\text {gpt }}(a \mid s)$ that maximizes expected return over all the tasks:

$$
\pi_{g p t}^{*}(a \mid s)=\arg \max _{\pi} \mathbb{E}_{i \sim[N]} \mathbb{E}_{\pi}\left[\sum_{t=1}^{T} r_{i}\left(s_{t}, a_{t}\right)\right]
$$

The observation space and action space of AV in our works are defined as follows:

1) Observation Space: The set of all observable HVs within the perception range of AV $i$ is denoted as $\mathscr{H}_{i}$. The observation matrix for expert $i$, denoted as $\mathcal{O}_{i}$, is a matrix of dimensions $\left|\mathscr{H}_{i}\right| \times|\mathcal{F}|$, where $\left|\mathscr{H}_{i}\right|$ represents the total number of observable vehicles for expert $i$, and $|\mathcal{F}|$ signifies the number of features used to describe a vehicle's state. The feature vector for vehicle $k$ is expressed as:

$$
\mathscr{F}_{k}=\left[x_{k}, y_{k}, v_{k}^{x}, v_{k}^{y}\right]
$$

where $x_{k}, y_{k}, v_{k}^{x}, v_{k}^{y}$ correspond to the longitudinal position, lateral position, longitudinal speed, and lateral speed, respectively.
2) Action Space: We focus primarily on the high-level decision-making actions of AV. As the AV navigates through an intersection, we predefine the driving route, requiring the AV to determine acceleration and deceleration actions to reach its destination. Consequently, we define the action space $\mathcal{A}$ for the AV as a set of high-level control decisions, encompassing \{slow down, cruising, speed up\}. Both acceleration and deceleration actions have absolute values of $1 \mathrm{~m} / \mathrm{s}^{2}$.

## IV. Methodology

In this section, the training pipeline used to train MTD-GPT is first introduced, then the process of expert data collection is described. Finally, detailed information on our MTD-GPT model is introduced.

## A. Overview of the Training Pipeline for MTD-GPT

As shown in Fig. 2, MTD-GPT's training pipeline is composed of three key components: Expert Data Collection, GPT Training, and GPT Evaluation. During the Expert Data Collection phase, multiple expert models are trained using the proximal policy optimization (PPO) algorithm with the attention mechanism to achieve excellent performance on single-task decision-making. Subsequently, in a simulated environment, the expert's actions are recorded, generating a multi-task expert demonstration dataset.

In the GPT Training phase, the multi-task expert dataset serves as a guide for GPT learning. First, the problem of multi-task decision-making for autonomous driving is abstracted as a sequence modeling and prediction task. Then we transform the "state-action-reward" tuples from expert data into a token format similar to Natural Language Processing (NLP) task to match the input format of the GPT model [10].

In the GPT Evaluation phase, the trained MTD-GPT is assessed in various task scenarios, considering the decisionmaking data of GPT as quasi-expert data for future training of GPT.

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-3.jpg?height=563&width=784&top_left_y=765&top_left_x=1121)
Fig. 2: The Training Pipeline for our MTD-GPT.

## B. Expert Data Collection

The entire process of expert data collection is illustrated in Fig. 3. Initially, three distinct autonomous vehicle decisionmaking tasks - turning left, proceeding straight, and turning right - are defined. Subsequently, three RL experts are trained using the PPO-Attention algorithm. Ultimately, the action and reward data are recorded and compiled into an offline multi-task dataset through simulating the actions of each expert within a designated simulation environment.

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-3.jpg?height=273&width=795&top_left_y=1916&top_left_x=1115)
Fig. 3: The process of the data sample for offline training.

1) RL Experts Training: First, we train a couple of RLbased experts $i(i \in 1,2, \ldots, N)$ who is good at single decision-making task. Every RL expert consists of a policy network $\pi_{\theta}$ parameterized by $\theta$ and a value network $V_{\phi}$ parameterized by $\phi$. The policy network maps the observation $\mathcal{O}$ to a distribution of actions $a$. And taking the same inputs
as the policy network, the value network will estimate a scalar value $v$.
- Policy Network. To better the performance of the RL Expert, the attention mechanism [23] is integrated into the policy network. The policy network with attention module is shown in Fig.4. For each RL expert $i$, the corresponding observation $\mathcal{O}_{i}$ and states $\mathcal{F}_{i}$ are initially embedded via a Multilayer Perceptron (MLP) encoder. Following this initial transformation, the embedded data undergoes further processing within an attention layer, serving to prioritize and capture salient features. Finally, the attention-focused data is decoded by an MLP decoder, converting the processed information into an actionable output.

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-4.jpg?height=327&width=795&top_left_y=821&top_left_x=215)
Fig. 4: The policy network with attention layer.
- Policy Optimization. The Clipped PPO [24] is used to train the policy network $\pi_{\theta}$ and the value network $V_{\phi}$, whose main idea is the clipping surrogate objective:
$$
\begin{gathered}
L^{\mathrm{PPO}}(\theta)=E_{t}\left[\operatorname { m i n } \left(r_{t}(\theta) \hat{A}_{t}\right.\right. \\
\left.\left.\operatorname{clip}\left(r_{t}(\theta), 1-\epsilon, 1+\epsilon\right) \hat{A}_{t}\right)\right]
\end{gathered}
$$
where $r(\theta)=\frac{\pi_{\theta}(a \mid s)}{\pi_{\theta^{\prime}(a \mid s)}}$ denotes the ratio of the new policy $\pi_{\theta}(a \mid s)$ to the old policy $\pi_{\theta^{\prime}(a \mid s)}$, $\hat{A}_{t}$ signifies the advantage function and $\epsilon$ is the clipping range.
- Reward Function. To pass the intersection in a safe and efficient way, the reward function of expert $i$ is defined as:
$$
r_{i}=w_{c} r_{c}+w_{e} r_{e}+w_{a} r_{a}
$$
where $w_{c}, w_{e}$, and $w_{a}$ are the weight coefficients of collision reward $r_{c}$, efficiency reward $r_{e}$, and arrival reward $r_{a}$, respectively.
2) Data Sample: Upon completing the RL training, we deploy all expert models within the intersection simulation environment to collect a combined expert dataset $\mathscr{D}=\cup_{i=1}^{N} \mathscr{D}_{i}$. In each episode, the data sampling from experts is transformed into a sequential representation: $\tau=$ $\left(s_{1}, a_{1}, r_{1}, s_{2}, a_{2}, r_{2}, \ldots, s_{T}, a_{T}, r_{T}\right)$, where $s_{t}, a_{t}, r_{t}$ are the state, action and reward of the expert at timestep t, respectively.

\section*{C. Offline Training GPT}
Following [10], the GPT's training process is considered as the sequence modeling problem and will be trained in an autoregressive way.

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-4.jpg?height=892&width=780&top_left_y=180&top_left_x=1119)
Fig. 5: The GPT model streamlines AV decision-making by sampling expert trajectories, tokenizing them, mapping tokens via MLP and positional encoding, masking irrelevant information with self-attention, and predicting actions through a linear layer.

1) Input Representation: Let $\tau(\tau \in \mathscr{D})$ denote a trajectory of AV and let $|\tau|$ denote its length. The return-to-go (RTG) of the trajectory $\tau$ is defined as: $g_{t}=\sum_{t^{\prime}=t}^{T} r_{t^{\prime}}$, which represents the sum of future AV 's rewards from timestep $t$. Let $s=\left(s_{1}, \ldots, s_{|\tau|}\right), a=\left(a_{1}, \ldots, a_{|\tau|}\right)$ and $g=\left(g_{1}, \ldots, g_{|\tau|}\right)$ denote the sequence of state, action and RTG of $\tau$, respectively. Consequently, the representation of a trajectory sent to GPT is :

$$
\tau^{\prime}=\left(s_{1}, a_{1}, g_{1}, s_{2}, a_{2}, g_{2}, \ldots, s_{T}, a_{T}, g_{T}\right)
$$

The initial RTG $g_{1}$ is equal to the return of the trajectory.
2) Architecture: As shown in Fig.5, the MTD-GPT model utilizes an approach similar to Natural Language Processing (NLP) techniques for modeling and predicting decisionmaking tasks in autonomous driving.

Initially, expert trajectories $\tau^{\prime}$ are randomly sampled from the data pool $\mathscr{D}$ for various subtasks, and these trajectories are then transformed into tokens suitable for the model's processing, where $\left\langle s_{t}, a_{t}, g_{t}\right\rangle$ is defined as one token $x_{t}$ at timestep $t$.

Next, a MLP is utilized to map tokens to a continuous vector space and positional encodings (PE) [23] are then added to the embeddings to maintain the order of the input sequence:

$$
\begin{gathered}
x_{t}^{\prime}=\operatorname{MLP}\left(x_{t}\right) \\
e_{t}=x_{t}^{\prime}+\text { Positional_Encoding }\left(x_{t}\right)
\end{gathered}
$$

Then the embedding results are passed through the Transformer's layers to acquire hidden states $h_{t}$ :

$$
h_{t}=\operatorname{TransformerLayer}\left(e_{t}\right)
$$

As shown in Fig.6, we use GPT-2 [11] as our transformer model, which has the decoder-only architecture. To mask irrelevant information, the self-attention mechanism [23] is applied, which computes the attention scores using query $Q$, key $K$, and value $V$ matrices:

$$
\operatorname{Attention}(Q, K, V)=\operatorname{softmax}\left(\frac{Q K^{T}}{\sqrt{d_{k}}}+M\right) V
$$

where $M$ is the matrix that ensures the input trajectory at the timestep $t$ can only correlate with the input from $\langle 1, \cdots, t-$ $1\rangle$.

Finally, a linear prediction layer is used to generate predicted action $a_{t+1}$ based on the hidden states:

$$
a_{t+1}^{\prime}=\operatorname{Linear}\left(h_{t}\right)
$$

By following this process, at timestep $t$, MTD-GPT generates the action $a_{t+1}^{\prime}$ conditioned on the tokens from the latest $K$ timesteps, where $K$ is a hyperparameter and is also referred to as the context length for the GPT. Specifically, the policy of MTD-GPT is represented as $\pi_{\text {gpt }}\left(a_{t} \mid s_{-K, t}, g_{-K, t}\right)$, where $s_{-K, t}$ is shorthand for the sequence of $K$ past states $s_{\max (1, t-K+1): t}$ and similarly for $g_{-K, t}$. The whole training procedure of MTD-GPT is summarized in Algorithm 1

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-5.jpg?height=477&width=788&top_left_y=1354&top_left_x=217)
Fig. 6: The original structure of GPT-2.

3) Training: All tokens from dataset $\mathscr{D}$ are fed into MTD-GPT, of which left-turn, straight-through, and right-turn tasks each account for one-third. The policy $\pi_{g p t}$ is trained by the Cross-entropy (CE) loss:

$$
\mathcal{L}_{C E}=\frac{1}{K} \sum_{t=1}^{K} P\left(a_{t}\right) \log \left(\pi_{g p t}\left(s_{-K, t}, g_{-K, t}\right)\right)
$$

## D. GPT Evaluation

After training, MTD-GPT will be evaluated in different driving tasks at intersections. For task $i$, we specify the desired performance $g_{1}^{i}$ and an initial state $s_{1}^{i}$ of AV. The MTD-GPT generates the action $a_{1}^{i}=\pi_{g p t}\left(s_{1}^{i}, g_{1}^{i}\right)$. Then the action $a_{1}^{i}$ will be executed by AV. The next state $s_{t+1}^{i} \sim$ $P\left(\cdot \mid s_{t}^{i}, a_{t}^{i}\right)$ and a reward $r_{t}^{i}=R\left(s_{t}^{i}, a_{t}^{i}\right)$ will be obtained, which gives us the next RTG as $g_{t+1}^{i}=g_{t}^{i}-r_{t}^{i}$. And GPT generates the action $a_{2}^{i}$ based on $s_{1}^{i}, s_{2}^{i}$ and $g_{1}^{i}, g_{2}^{i}$. The whole decision-making process is repeated until the episode terminates. Then the decision success rate of the AV on each task will be tallied and calculated.

```
Algorithm 1: Multi-Task Decision-Making GPT
    Inputs : Offline Dataset \(\mathscr{D}\)
    Outputs: \(\pi_{\text {gpt }}(a \mid s, g)\)
    Initialize GPT model with random weights \(\theta\);
    for Epoch \(=1\) to \(M\) do
        repeat
            Sample a batch of trajectories \(\tau\) of task \(i\)
                from \(\mathscr{D}\);
            Compute RTG \(g\) for each trajectory \(\tau\);
            Get tokens \(x\) : Tokenize \((\tau)\);
            Embed input tokens : \(e=M L P(x)+P E_{t}\);
            Acquire hidden states \(h\) by
            TransformerLayer \((e)\);
            Get predicted action \(a\) by LinearLayer \((h)\);
            Compute CE loss \(L_{C E}(\theta)\);
            Update \(\theta\) using gradient descent on \(L_{C E}(\theta)\);
        until \(\mathscr{D}\) is empty;
    end
```


## V. Simulation and Performance Evaluation

A. Simulation Environment

Our simulation platform is built based on an OpenAI Gym environment [25]. The longitude and lateral decisions of HVs are controlled by the IDM [26] and MOBIL [27] models, respectively. All HVs in our simulator are set with the constant-speed motion prediction and collision avoidance functions.
B. Implementation Details

For the RL expert, the Encoder and Decoder of the attention-based policy network both are MLP, which has two linear layers and the layer size is $64 \times 64$. The Attention Layer contains 2 attention heads and the feature size is 128. We use Deep Q-learning (DQN) and Proximal Policy Optimization (PPO) as our single-task baselines. The total training steps are all $20 K$. The $w_{c}, w_{e}$ and $w_{a}$ in Eq.(7) are all set as 1. The parameters of MTD-GPT are shown in Table I.

All experiments are conducted in a computation platform with Intel Xeon Silver 4214R CPU, NVIDIA GeForce RTX 3090 GPU×2, and 128G Memory.
C. Performance Evaluation

1) RL Expert: Fig. 7 presents a comparative analysis of the RL Expert algorithm, PPO-Attention, which we develop, juxtaposed with several baseline algorithms including DQN and PPO. Assessing both the speed of convergence and the average reward, it becomes discernible that PPO-Attention exhibits superior overall performance across all decisionmaking tasks. This indicates the robustness of our RL expert

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-6.jpg?height=423&width=1669&top_left_y=174&top_left_x=226)
Fig. 7: The performance comparison between RL Experts (PPO-Attention) and other baselines:(a) turning left task, (b) going straight task, (c) turning right task.

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-6.jpg?height=406&width=1650&top_left_y=735&top_left_x=228)
Fig. 8: The performance of GPT with different parameter counts: (a) training loss, (b) training action error, (c) the success rate on different testing tasks.

TABLE I: The hyperparameter of the MTD-GPT model
| Symbol | Definition | Value |
| :--- | :--- | :--- |
| $M$ | Training Epoch | 100 |
| $N_{s}$ | Steps for Each Epoch | $10^{4}$ |
| $K$ | Training Context Length | 30 |
| $D$ | Dropout | 0.1 |
| $N_{h}$ | Number of Attention Heads | 4 |
| $N_{l}$ | Number of Layers | 3/6/12 |
| $E_{d}$ | Embedding Dimension | 128/ 256/ 1024 |
| $B_{s}$ | Batch Size | 64 |


when faced with singular decision-making tasks, thereby supplying high-quality action data for GPT model.
2) MTD-GPT Performance Analysis: We train different models with varying parameter counts (approx. $600 K, 1.2 M, 2.4 M, 38 M, 75 M$ ) by adjusting the number of decoder layers and embedding dimensions. The training losses, action errors, and success rates on test tasks during the training process for GPT models with different parameter scales are depicted in Fig. 8 (a), Fig. 8 (b), and Fig.8(c), respectively.

As the model's parameter count increases, convergence is achieved faster during the training process. The two models with $38 M$ and $75 M$ parameters exhibit the best convergence and learning outcomes during training. However, we find that larger models do not necessarily guarantee better decisionmaking performance. We test these models on three decision tasks at intersections. MTD-GPT (600K) achieves decision success rates of 66\%, 75\%, and 94\% for left-turn, straight- ahead, and right-turn tasks, respectively. When the model's parameter count increases to 1.2M, the decision success rates increase by 4\%, 8\%, and 1\%, respectively. Nevertheless, when the model's parameter scale further increases, the decision success rates actually decline.

We posit that models with larger parameter counts are more prone to overfitting on fixed offline data, leading to suboptimal performance in test tasks. Therefore, devising training strategies to prevent overfitting and exploring other methods to enhance model generalization capabilities will be our next area of focus.

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-6.jpg?height=370&width=765&top_left_y=1813&top_left_x=1121)
Fig. 9: The performance comparison between GPT and RL Experts.

3) MTD-GPT vs. RL Expert: As illustrated in Fig.9, we compare the single-subtask success rates of MTD-GPT (1.2M) and RL Expert. RL Expert achieves decision success rates of 49\%, 81\%, and 92\% for left-turn, rightturn, and straight-ahead tasks, respectively, while MTD-GPT

![](https://cdn.mathpix.com/cropped/1d568846-a762-4ab6-b8ca-15894ba29631-7.jpg?height=978&width=1654&top_left_y=174&top_left_x=228)
Fig. 10: Three cases of turning left task from different models: (a) Case 1 from GPT with $600 K$ parameters, (b) Case 2 from GPT with $1.2 M$ parameters, (c) Case 3 from GPT with $75 M$ parameters.

(1.2M) achieves 70\%, 83\%, and 95\%. These results show improvement compared to the single-task RL Expert, and even GPT models with other parameter scales can achieve performance comparable to RL Expert in these subtasks. This demonstrates the promising impact and significant potential of the MTD-GPT model in multi-task decision-making.

## D. Case Analysis

Given the complexity involved in executing left turns at unsignalized intersections, we evaluate the performance of our model in such scenarios. We conduct an analysis on three distinct cases, each corresponding to a GPT model of different parameter scales $(600 K, 1.2 M$, and $75 M)$. Animations demonstrating these cases and more demos can be accessed at the site. ${ }^{1}$

Our analysis reveals that, even when confronted with identical decision-making tasks, models with varying parameter scales demonstrate divergent decision-making styles. As depicted in Fig. 10(a), for Case 1, the AV hardly reduces its speed after entering the intersection $($ Step $=3)$ and navigates its way through just before an oncoming vehicle traveling straight arrives at the intersection $($ Step $=5)$. This approach enables the AV to accomplish the task in less time, but the aggressive decision-making style heightens safety risks, indicating that it is not an optimal strategy.

Conversely, in Case 2, the AV adopts a more conservative behavior, as illustrated in Fig. 10(b). Upon entering the

[^1] intersection, the AV opts to halt and observe (Step = 12), only advancing into the intersection when the risk is deemed low or when there is an absence of interaction conflict (i.e., after the oncoming vehicle has passed) (Step = 18), thereby ensuring a safe departure from the intersection.

Furthermore, in the model with $75 M$ parameters, we notice a further amplification of this conservative decisionmaking inclination. As demonstrated in Fig. 10(c) for Case 3, the AV pauses before entering the intersection $($ Step = 8). However, the adoption of an overly cautious strategy culminates in an extended waiting period (Step $=8-37$ ), subsequently leading to congestion in its lane and a decrease in the overall traffic system efficiency.

## VI. CONCLUSIONS

Developing a multi-task decision-making model for autonomous driving constitutes a remarkably challenging goal in the field of research. In this work, we propose the MTD-GPT model for multi-task decision-making of AV at unsignalized intersections. Moreover, we design a pipeline that leverages RL algorithms to train single-task decisionmaking experts and utilize expert data to provide guidance for MTD-GPT learning. Our experimental results demonstrate that the MTD-GPT model outperforms or matches the performance of exceptional single-task decision-making RL models in different decision-making tasks.

In future work, we aim to further expand the generalization capabilities of the MTD-GPT model, enabling exceptional performance in tasks such as merging onto ramps, navi-
gating roundabouts, and changing lanes or overtaking on urban roads. Additionally, we plan to employ a hybrid dataset comprising natural driving and simulation data for GPT training. Furthermore, we will investigate incorporating Reinforcement Learning with Human Feedback (RLHF) methods into the GPT model's training regimen, promoting the generation of more human-like, secure, and interpretable decision-making behaviors.

## References

[1] S. Aradi, "Survey of deep reinforcement learning for motion planning of autonomous vehicles," IEEE Transactions on Intelligent Transportation Systems, vol. 23, no. 2, pp. 740-759, 2020.
[2] N. M. Negash and J. Yang, "Anticipation-based autonomous platoon control strategy with minimum parameter learning adaptive radial basis function neural network sliding mode control," SAE International Journal of Vehicle Dynamics, Stability, and NVH, vol. 6, no. 10-06-03-0017, pp. 247-265, 2022.
[3] R. Chandra, "Towards autonomous driving in dense, heterogeneous, and unstructured traffic," Ph.D. dissertation, University of Maryland, College Park, 2022.
[4] P. De Beaucorps, T. Streubel, A. Verroust-Blondet, F. Nashashibi, B. Bradai, and P. Resende, "Decision-making for automated vehicles at intersections adapting human-like behavior," in 2017 IEEE Intelligent Vehicles Symposium (IV). IEEE, 2017, pp. 212-217.
[5] P. Hang, C. Lv, Y. Xing, C. Huang, and Z. Hu, "Human-like decision making for autonomous driving: A noncooperative game theoretic approach," IEEE Transactions on Intelligent Transportation Systems, vol. 22, no. 4, pp. 2076-2087, 2020.
[6] X. Zhao, Y. Tian, and J. Sun, "Yield or rush? social-preferenceaware driving interaction modeling using game-theoretic framework," in 2021 IEEE International Intelligent Transportation Systems Conference (ITSC). IEEE, 2021, pp. 453-459.
[7] Q. Liu, X. Li, Z. Li, J. Wu, G. Du, X. Gao, F. Yang, and S. Yuan, "Graph reinforcement learning application to co-operative decisionmaking in mixed autonomy traffic: Framework, survey, and challenges," arXiv preprint arXiv:2211.03005, 2022.
[8] S. Kai, B. Wang, D. Chen, J. Hao, H. Zhang, and W. Liu, "A multi-task reinforcement learning approach for navigating unsignalized intersections," in 2020 IEEE Intelligent Vehicles Symposium (IV). IEEE, 2020, pp. 1583-1588.
[9] H. Seong, C. Jung, S. Lee, and D. H. Shim, "Learning to drive at unsignalized intersections using attention-based deep reinforcement learning," in 2021 IEEE International Intelligent Transportation Systems Conference (ITSC). IEEE, 2021, pp. 559-566.
[10] L. Chen, K. Lu, A. Rajeswaran, K. Lee, A. Grover, M. Laskin, P. Abbeel, A. Srinivas, and I. Mordatch, "Decision transformer: Reinforcement learning via sequence modeling," Advances in neural information processing systems, vol. 34, pp. 15084-15 097, 2021.
[11] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, I. Sutskever et al., "Language models are unsupervised multitask learners," OpenAI blog, vol. 1, no. 8, p. 9, 2019.
[12] M. Zhang, N. Li, A. Girard, and I. Kolmanovsky, "A finite state machine based automated driving controller and its stochastic optimization," in Dynamic Systems and Control Conference, vol. 58288. American Society of Mechanical Engineers, 2017, p. V002T07A002.
[13] J. Cai, P. Hang, and C. Lv, "Game theoretic modeling and decision making for connected vehicle interactions at urban intersections," in 2021 6th IEEE International Conference on Advanced Robotics and Mechatronics (ICARM). IEEE, 2021, pp. 874-880.
[14] H. Shu, T. Liu, X. Mu, and D. Cao, "Driving tasks transfer using deep reinforcement learning for decision-making of autonomous vehicles in unsignalized intersection," IEEE Transactions on Vehicular Technology, vol. 71, no. 1, pp. 41-52, 2021.
[15] Y. Liu, Y. Gao, Q. Zhang, D. Ding, and D. Zhao, "Multi-task safe reinforcement learning for navigating intersections in dense traffic," Journal of the Franklin Institute, 2022.
[16] S. Casola, I. Lauriola, and A. Lavelli, "Pre-trained transformers: An empirical comparison," Machine Learning with Applications, vol. 9, p. 100334, 2022.
[17] S. Khan, M. Naseer, M. Hayat, S. W. Zamir, F. S. Khan, and M. Shah, "Transformers in vision: A survey," ACM computing surveys (CSUR), vol. 54, no. 10s, pp. 1-41, 2022.
[18] W. Yuan, J. Chen, S. Chen, L. Lu, Z. Hu, P. Li, D. Feng, F. Liu, and J. Chen, "Transformer in reinforcement learning for decision-making: A survey," 2023.
[19] Q. Zheng, A. Zhang, and A. Grover, "Online decision transformer," in International Conference on Machine Learning. PMLR, 2022, pp. 27 042-27 059.
[20] Q. Lin, H. Liu, and B. Sengupta, "Switch trajectory transformer with distributional value approximation for multi-task reinforcement learning," arXiv preprint arXiv:2203.07413, 2022.
[21] M. Janner, Q. Li, and S. Levine, "Offline reinforcement learning as one big sequence modeling problem," Advances in neural information processing systems, vol. 34, pp. 1273-1286, 2021.
[22] P. Polack, F. Altché, B. d'Andréa Novel, and A. de La Fortelle, "The kinematic bicycle model: A consistent model for planning feasible trajectories for autonomous vehicles?" in 2017 IEEE intelligent vehicles symposium (IV). IEEE, 2017, pp. 812-818.
[23] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, "Attention is all you need," Advances in neural information processing systems, vol. 30, 2017.
[24] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, "Proximal policy optimization algorithms," arXiv preprint arXiv:1707.06347, 2017.
[25] E. Leurent, "An environment for autonomous driving decisionmaking," https://github.com/eleurent/highway-env, 2018.
[26] A. Kesting, M. Treiber, and D. Helbing, "Enhanced intelligent driver model to access the impact of driving strategies on traffic capacity," Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, vol. 368, no. 1928, pp. 4585-4605, 2010.
[27] -, "General lane-changing model mobil for car-following models," Transportation Research Record, vol. 1999, no. 1, pp. 86-94, 2007.


[^0]:    This work was supported in part by the Natural Science Foundation of China (52232015 and 52125208), the Young Elite Scientists Sponsorship Program by CAST (2022QNRC001) and the Fundamental Research Fund for the Central Universities.

    Jiaqi Liu, Peng Hang, Xiao Qi and Jian Sun are with the Department of Traffic Engineering and Key Laboratory of Road and Traffic Engineering, Ministry of Education, Tongji University, Shanghai 201804, China. (e-mail: \{liujiaqi13, hangpeng, qixiao, sunjian\}@tongji.edu.cn)

    Jianqiang Wang is with State Key Laboratory of Automotive Safety and Energy School of Vehicle and Mobility, Tsinghua University, Beijing 100084, China.(e-mail: wjqlws@tsinghua.edu.cn)

    Corresponding author: Peng Hang

[^1]:    ${ }^{1}$ See https://shorturl.at/eMNS4

