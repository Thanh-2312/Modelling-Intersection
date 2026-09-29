# **MÃ´ phá»ng vi mÃ´ nÃºt giao thÃ´ng há»—n há»£p 2D** 

2D Continuous Mixed-Traffic Intersection Simulation 

ThÃ nh Táº¥t 

September 2026 

DÆ°á»›i Ä‘Ã¢y lÃ  báº£n phÃ¢n tÃ­ch toÃ n diá»‡n vÃ  chi tiáº¿t vá»nguyÃªn lÃ½ hoáº¡t Ä‘á»™ng, cáº¥u trÃºc mÃ£ nguá»“n vÃ  cÃ¡c thuáº­t toÃ¡n trong dá»±Ã¡n **MÃ´ phá»ng vi mÃ´ nÃºt giao thÃ´ng há»—n há»£p 2D** , bao quÃ¡t toÃ n bá»™cÃ¡c file trong mÃ£ nguá»“n. 

## **1 CÃC THÃ”NG Sá»CÆ  Báº¢N** 

### **1.1 ThÃ´ng sá»‘hÃ¬nh há»c nÃºt giao & háº¡táº§ng** 

_Quy Ä‘á»‹nh táº¡i_ `geometry.py` , `control.py` , `main.py` . 

- **Quy mÃ´ nÃºt giao:** NgÃ£ tÆ° 4 nhÃ¡nh tiáº¿p cáº­n: Báº¯c ( `North` ), Nam ( `South` ), ÄÃ´ng ( `East` ), TÃ¢y ( `West` ). 

- **Chiá»u rá»™ng máº·t cáº¯t ngang má»—i nhÃ¡nh** _W_ **:** 

_W_ = 21 _._ 0 m 

gá»“m 6 lÃ n xe: 3 lÃ n vÃ o vÃ  3 lÃ n ra, má»—i lÃ n rá»™ng 3 _._ 5 m. 

- **Ná»­a chiá»u rá»™ng Ä‘Æ°á»ng:** 

_W_ half = 10 _._ 5 m 

tÃ­nh tá»«tim Ä‘Æ°á»ng Ä‘áº¿n mÃ©p vá»‰a hÃ¨. 

- **Vá»‹trÃ­ tÃ¢m cá»§a 3 lÃ n vÃ o** theo tá»a Ä‘á»™lá»‡ch ngang Frenet _d_ so vá»›i tim Ä‘Æ°á»ng: 

   - **LÃ n 1 lÃ n trong cÃ¹ng, sÃ¡t tim Ä‘Æ°á»ng:** 

_d_ = _âˆ’_ 1 _._ 75 m 

chuyÃªn ráº½trÃ¡i hoáº·c há»—n há»£p. 

**â€“ LÃ n 2 lÃ n giá»¯a:** 



lÃ n há»—n há»£p: Ä‘i tháº³ng, ráº½trÃ¡i, ráº½pháº£i. 

- **LÃ n 3 lÃ n ngoÃ i cÃ¹ng, sÃ¡t lá»pháº£i:** 



chuyÃªn ráº½pháº£i hoáº·c há»—n há»£p. 

1 

- **Váº¡ch dá»«ng xe:** 

_s_ stop = _âˆ’_ 10 _._ 5 m 

- **VÃ¹ng xung Ä‘á»™t:** 

#### 21 m _Ã—_ 21 m 

vá»›i tá»a Ä‘á»™tá»« _âˆ’_ 10 _._ 5 m Ä‘áº¿n +10 _._ 5 m trÃªn cáº£hai trá»¥c _X_ vÃ  _Y_ . 

- **Khoáº£ng cÃ¡ch sinh xe:** 

60 _._ 0 m 

tÃ­nh tá»«tÃ¢m nÃºt giao. 

- **Pháº¡m vi hiá»ƒn thá»‹Ä‘á»“há»a:** 



### **1.2 ThÃ´ng sá»‘Ä‘áº·c tÃ­nh phÆ°Æ¡ng tiá»‡n** 

_Quy Ä‘á»‹nh táº¡i_ `vehicle.py` . 

Báº£ng 1: Báº£ng thÃ´ng sá»‘Ä‘áº·c tÃ­nh phÆ°Æ¡ng tiá»‡n 

|**ThÃ´ng sá»‘**|**Ã” tÃ´**|**Xe mÃ¡y**|
|---|---|---|
|Chiá»u dÃ i _L_|4_._5 m|1_._8 m|
|Chiá»u rá»™ng _W_|1_._8 m|0_._8 m|
|Váº­n tá»‘c tá»‘i Ä‘a _v_max|50 km_/_h_â‰ˆ_13_._89 m_/_s|40 km_/_h_â‰ˆ_11_._11 m_/_s|
|Gia tá»‘c tÄƒng tá»‘c cá»±c Ä‘áº¡i _a_max|+2_._5 m_/_s<sup>2</sup>|+2_._5 m_/_s<sup>2</sup>|
|Gia tá»‘c phanh thoáº£i mÃ¡i _a_comf|_âˆ’_3_._0 m_/_s<sup>2</sup>|_âˆ’_3_._0 m_/_s<sup>2</sup>|
|Gia tá»‘c phanh kháº©n cáº¥p _a_min|_âˆ’_5_._0 m_/_s<sup>2</sup>|_âˆ’_5_._0 m_/_s<sup>2</sup>|



### **1.3 ThÃ´ng sá»‘phÃ¡t sinh dÃ²ng giao thÃ´ng** 

- **CÆ°á»ng Ä‘á»™dÃ²ng xe Ä‘áº¿n trung bÃ¬nh (** `LAMBDA_RATE` **):** 



- **Khoáº£ng thá»i gian giÃ£n cÃ¡ch tá»‘i thiá»ƒu:** 



- **Tá»·lá»‡thÃ nh pháº§n dÃ²ng xe:** 

      - 67% xe mÃ¡y _,_ 33% Ã´ tÃ´ 

- **Tá»·lá»‡phÃ¢n luá»“ng theo hÆ°á»›ng Ä‘i:** 

   - 70% Ä‘i tháº³ng _,_ 10% ráº½trÃ¡i _,_ 20% ráº½pháº£i 

_Hiá»‡n táº¡i Ä‘á»ƒthá»­nghiá»‡m nÃªn tá»‰lá»‡50/30/20_ 

2 

### **1.4 ThÃ´ng sá»‘Ä‘Ã¨n tÃ­n hiá»‡u giao thÃ´ng** 

- **Chu ká»³Ä‘Ã¨n tá»•ng:** 

_C_ = 80 _._ 0 s 

Äiá»u khiá»ƒn theo mÃ´ hÃ¬nh 2 pha cá»‘Ä‘á»‹nh. 

- **Pha 1 trá»¥c Báº¯c - Nam:** 

37 s xanh _â†’_ 3 s vÃ ng _â†’_ 40 s Ä‘á» 

- **Pha 2 trá»¥c ÄÃ´ng - TÃ¢y:** 



### **1.5 ThÃ´ng sá»‘mÃ´ hÃ¬nh bÃ¡m Ä‘uÃ´i & Ä‘iá»u khiá»ƒn** 

- **Thá»i gian bÃ¡m Ä‘uÃ´i an toÃ n:** _T_ = 1 _._ 5 s 

- **Khoáº£ng cÃ¡ch dá»«ng tÄ©nh tá»‘i thiá»ƒu:** _s_ 0 = 2 _._ 0 m 

- **Sá»‘mÅ© gia tá»‘c:** _Î´_ = 4 _._ 0 

- **Há»‡sá»‘bÃ¡m lÃ n P-Controller:** _Kp_ = 0 _._ 2 GÃ³c báº»lÃ¡i giá»›i háº¡n: 



- **Váº­n tá»‘c khá»‘ng cháº¿an toÃ n trong ngÃ£ tÆ°:** 

**â€“ Ráº½trÃ¡i:** 

**â€“ Ráº½pháº£i: â€“ Äi tháº³ng:** 





- **BÆ°á»›c thá»i gian mÃ´ phá»ng (** `DT` **):** 



## **2 CÃC LUáº¬T MÃ” PHá»ŽNG CÆ  Báº¢N** 

### **2.1 Quy táº¯c luáº­t giao thÃ´ng Viá»‡t Nam (Äi bÃªn pháº£i)** 

Má»i xe di chuyá»ƒn theo quy táº¯c Ä‘i bÃªn pháº£i tim Ä‘Æ°á»ng theo chiá»u tiáº¿n. Tá»a Ä‘á»™Ä‘Æ°á»£c quy Ä‘á»•i linh hoáº¡t sang **há»‡tá»a Ä‘á»™Frenet** ( _s, d_ ): 

- _s_ : vá»‹trÃ­ dá»c theo trá»¥c nhÃ¡nh Ä‘Æ°á»ng. TÃ¢m ngÃ£ tÆ° lÃ  má»‘c _s_ = 0. TrÆ°á»›c khi vÃ o ngÃ£ tÆ°: _s <_ 0. Sau khi ráº½hoáº·c thoÃ¡t ngÃ£ tÆ°: _s >_ 0. 

- _d_ : khoáº£ng cÃ¡ch lá»‡ch ngang so vá»›i tim Ä‘Æ°á»ng ( _d_ = 0). Pháº§n Ä‘Æ°á»ng bÃªn pháº£i há»£p lá»‡ thá»a mÃ£n: _âˆ’_ 10 _._ 5 _â‰¤ d <_ 0. 

3 

### **2.2 PhÃ¢n lÃ n vÃ  hÃ nh vi láº¥n lÃ n vá»›i xe mÃ¡y** 

- **GÃ¡n lÃ n Ä‘Æ°á»ng má»¥c tiÃªu:** 

   - Xe ráº½trÃ¡i chá»n ngáº«u nhiÃªn giá»¯a lÃ n trong ( _|d|_ = 1 _._ 75 m) hoáº·c lÃ n giá»¯a ( _|d|_ = 5 _._ 25 m). 

   - Xe Ä‘i tháº³ng Ä‘i á»ŸlÃ n giá»¯a ( _|d|_ = 5 _._ 25 m). 

   - Xe ráº½pháº£i chá»n giá»¯a lÃ n ngoÃ i ( _|d|_ = 8 _._ 75 m) hoáº·c lÃ n giá»¯a ( _|d|_ = 5 _._ 25 m). 

- **Äáº·c tÃ­nh dÃ²ng xe mÃ¡y:** KhÃ¡c vá»›i Ã´ tÃ´ luÃ´n bÃ¡m tÃ¢m lÃ n nghiÃªm ngáº·t, xe mÃ¡y Ä‘Æ°á»£c gÃ¡n má»™t Ä‘á»™lá»‡ch ngáº«u nhiÃªn: 



Äiá»u nÃ y mÃ´ phá»ng dÃ²ng giao thÃ´ng há»—n há»£p: xe mÃ¡y cháº¡y dÃ n hÃ ng ngang, táº­n dá»¥ng khoáº£ng trá»‘ng vÃ  Ä‘i sÃ¡t lá»hoáº·c mÃ©p Ã´ tÃ´. 

### **2.3 Quy táº¯c phÃ¡t sinh vÃ  giáº£i phÃ³ng phÆ°Æ¡ng tiá»‡n** 

**PhÃ¡t sinh dÃ²ng xe:** Khoáº£ng cÃ¡ch thá»i gian giá»¯a hai xe káº¿tiáº¿p _h_ tuÃ¢n theo phÃ¢n phá»‘i mÅ© bá»‹cháº·n dÆ°á»›i: 



**Kiá»ƒm tra an toÃ n khi xuáº¥t hiá»‡n:** Xe má»›i chá»‰Ä‘Æ°á»£c Ä‘Æ°a vÃ o mÃ´ phá»ng náº¿u: 

   - PhÃ­a trÆ°á»›c khÃ´ng cÃ³ xe; hoáº·c 

   - Xe trÆ°á»›c Ä‘ang cháº¡y bÃ¬nh thÆ°á»ng ( _v >_ 4 _._ 0 m _/_ s) vÃ  khoáº£ng cÃ¡ch Ä‘uÃ´i xe _d_ gap _>_ 15 _._ 0 m; hoáº·c 

- Xe trÆ°á»›c Ä‘ang dá»«ng/cháº¡y cháº­m ( _v â‰¤_ 4 _._ 0 m _/_ s) vÃ  khoáº£ng cÃ¡ch trá»‘ng _d_ gap _>_ 4 _._ 0 m. 

- Náº¿u khÃ´ng Ä‘á»§Ä‘iá»u kiá»‡n, xe Ä‘Æ°á»£c giá»¯láº¡i trong hÃ ng Ä‘á»£i ( `pending_queue` ) cá»§a nhÃ¡nh Ä‘Ã³. 

**Giáº£i phÃ³ng bá»™nhá»›:** Khi xe di chuyá»ƒn vÆ°á»£t khá»i khung nhÃ¬n: 

_|x| >_ 75 m hoáº·c _|y| >_ 75 m 

Ä‘á»‘i tÆ°á»£ng Ä‘á»“há»a vÃ  dá»¯liá»‡u xe sáº½Ä‘Æ°á»£c há»§y bá». 

## **3 CÃC THUáº¬T TOÃN ÄIá»€U KHIá»‚N XE** 

### **3.1 Cáº­p nháº­t Ä‘á»™ng há»c phÆ°Æ¡ng tiá»‡n** 

Má»—i chu ká»³ âˆ† _t_ = 0 _._ 1 s, phÆ°Æ¡ng tiá»‡n cáº­p nháº­t váº­n tá»‘c vÃ  tá»a Ä‘á»™theo phÆ°Æ¡ng phÃ¡p tÃ­ch phÃ¢n sá»­dá»¥ng váº­n tá»‘c trung bÃ¬nh: 

_v_ next = max (0 _,_ min ( _v_ + _a_ âˆ† _t, v_ max)) 



Xe khÃ´ng bá»‹giáº­t lÃ¹i ( _v â‰¥_ 0) vÃ  luÃ´n chá»‹u gia tá»‘c trong giá»›i háº¡n: _a_ min _â‰¤ a â‰¤ a_ max. 

4 

### **3.2 MÃ´ hÃ¬nh bÃ¡m Ä‘uÃ´i IDM-Intelligent Driver Model** 

IDM cÃ¢n báº±ng giá»¯a xu hÆ°á»›ng tÄƒng tá»‘c Ä‘áº¡t _v_ 0 vÃ  nhu cáº§u phanh giáº£m tá»‘c dá»±a trÃªn chÃªnh lá»‡ch váº­n tá»‘c âˆ† _v_ = _v_ ego _âˆ’ v_ lead cÃ¹ng khoáº£ng cÃ¡ch thá»±c táº¿ _s_ gap: 



Trong Ä‘Ã³ khoáº£ng cÃ¡ch mong muá»‘n tá»©c thá»i: 



### **3.3 Dummy Vehicle - Xe áº£o** 

Má»i chÆ°á»›ng ngáº¡i váº­t dá»«ng Ä‘á»—(váº¡ch dá»«ng Ä‘Ã¨n Ä‘á», Ä‘iá»ƒm dá»«ng nhÆ°á»ng Ä‘Æ°á»ng ráº½trÃ¡i, ranh giá»›i xung Ä‘á»™t) Ä‘á»u Ä‘Æ°á»£c Ä‘Ã³ng gÃ³i thÃ nh: 

`DummyVehicle` ( _s, d, v_ = 0) 

Nhá»Ä‘Ã³, bá»™Ä‘iá»u khiá»ƒn IDM chá»‰coi váº­t cáº£n lÃ  má»™t xe Ä‘á»©ng yÃªn phÃ­a trÆ°á»›c vÃ  tá»±Ä‘á»™ng phanh mÆ°á»£t mÃ . 

### **3.4 Thuáº­t toÃ¡n láº¥n lÃ n** 

- **Xe mÃ¡y lÃ¡ch qua Ã´ tÃ´ cháº­m/dá»«ng:** Khi gáº·p Ã´ tÃ´ phÃ­a trÆ°á»›c ( _s_ gap _â‰¤_ 30 m), xe mÃ¡y tÃ­nh khoáº£ng trá»‘ng trÃ¡i/pháº£i ( `gap_left` , `gap_right` ). Náº¿u _gap â‰¥ W_ moto +0 _._ 4 m, xe mÃ¡y sáº½chá»n bÃªn rá»™ng hÆ¡n Ä‘á»ƒlÃ¡ch qua. 

- **Xe Ä‘i tháº³ng lÃ¡ch qua xe ráº½trÃ¡i:** Xe Ä‘i tháº³ng phÃ­a sau lÃ¡ch qua sÆ°á»n pháº£i cá»§a xe ráº½trÃ¡i Ä‘ang chá»giá»¯a giao lá»™. 

- **VÃ¹ng cáº¥m lÃ¡ch:** Trong pháº¡m vi _s âˆˆ_ [ _âˆ’_ 15 _._ 0 _,_ +5 _._ 0] m quanh váº¡ch dá»«ng, xe mÃ¡y **bá»‹ cáº¥m lÃ¡ch qua Ã´ tÃ´** Ä‘á»ƒtrÃ¡nh Ä‘Ã¢m xuyÃªn ngang hÃ´ng Ã´ tÃ´ khi dá»«ng chá»Ä‘Ã¨n. 

- **Äiá»u kiá»‡n thoÃ¡t lÃ¡ch:** Khi thÃ¢n xe thá»±c táº¿Ä‘Ã£ lá»‡ch háº³n khá»i hÃ¬nh chiáº¿u ngang cá»§a xe trÆ°á»›c (lateral_clearance _â‰¥_ 0 _._ 15 m), xe trÆ°á»›c má»›i Ä‘Æ°á»£c giáº£i phÃ³ng khá»i biáº¿n `lead_veh` . 

### **3.5 Äiá»u hÆ°á»›ng ráº½báº±ng Ä‘Æ°á»ng cong BÃ©zier báº­c 2 - Quadratic BÃ©zier Curves** 

Quá»¹Ä‘áº¡o ráº½Ä‘Æ°á»£c mÃ´ táº£báº±ng 3 Ä‘iá»ƒm kiá»ƒm soÃ¡t: 

- _P_ 0: Ä‘iá»ƒm báº¯t Ä‘áº§u táº¡i váº¡ch dá»«ng cá»§a lÃ n vÃ o. 

- _P_ 1: giao Ä‘iá»ƒm tiáº¿p tuyáº¿n hÃ¬nh há»c cá»§a hai nhÃ¡nh. 

- _P_ 2: Ä‘iá»ƒm káº¿t thÃºc táº¡i lÃ n ra má»¥c tiÃªu. 

PhÆ°Æ¡ng trÃ¬nh Ä‘Æ°á»ng cong vá»›i _t âˆˆ_ [0 _,_ 1]: 

_B_ ( _t_ ) = (1 _âˆ’ t_ )<sup>2</sup> _P_ 0 + 2(1 _âˆ’ t_ ) _tP_ 1 + _t_<sup>2</sup> _P_ 2 

Tham sá»‘ _t_ tÄƒng dáº§n theo quÃ£ng Ä‘Æ°á»ng: âˆ† _t_ =<sup>_<u>v</u>_</sup> _L_<sup>âˆ†</sup> curve<sup>_<u>t</u>_</sup><sup><u>sim</u>.XeliÃªntá»¥cbÃ¡mtheoÄ‘iá»ƒmmá»¥ctiÃªu</sup> phÃ­a trÆ°á»›c _t_ ahead = _t_ + _L_ curve2 _<u>.</u>_ <u>0</u><sup>vÃ Ä‘iá»uchá»‰nhgÃ³clÃ¡ivá»›igiá»›iháº¡n</sup><sup>_|Î´_steering</sup><sup>_| â‰¤_15</sup><sup>_â—¦_.</sup> 

5 

## **4 CÃC THUáº¬T TOÃN ÄIá»€U KHIá»‚N Táº I NGÃƒ TÆ¯** 

### **4.1 Tráº¡ng thÃ¡i cáº£u phÆ°Æ¡ng tiá»‡n** 

Má»—i xe chuyá»ƒn qua 4 tráº¡ng thÃ¡i ná»‘i tiáº¿p: 

`approaching` _âˆ’â†’_ `in_intersection` _âˆ’â†’_ `leaving` _âˆ’â†’_ `departed` 

### **4.2 Xá»­lÃ½ Ä‘Ã¨n tÃ­n hiá»‡u & VÃ¹ng lÆ°á»¡ng lá»±(Dilemma Zone Model)** 

Táº¡i váº¡ch dá»«ng _s_ stop = _âˆ’_ 10 _._ 5 m: 

- **ÄÃ¨n Ä‘á»:** KÃ­ch hoáº¡t `DummyVehicle` táº¡i _s_ = _âˆ’_ 10 _._ 5 m ( _v_ = 0). 

_d_ to_stop â€¢ **ÄÃ¨n vÃ ng:** TÃ­nh thá»i gian tá»›i váº¡ch dá»«ng TTI = _v_ . 

- TTI _>_ 5 _._ 0 s: Quyáº¿t Ä‘á»‹nh **Dá»«ng** . 

- TTI _<_ 1 _._ 5 s: Quyáº¿t Ä‘á»‹nh **Äi tiáº¿p** . 

**â€“** 1 _._ 5 _â‰¤_ TTI _â‰¤_ 5 _._ 0 s: TÃ­nh xÃ¡c suáº¥t dá»«ng theo mÃ´ hÃ¬nh há»“i quy Logistic: 



### **4.3 Thuáº­t toÃ¡n ráº½trÃ¡i nhÆ°á»ng Ä‘Æ°á»ng** 

Xe ráº½trÃ¡i pháº£i nhÆ°á»ng cho luá»“ng Ä‘i tháº³ng Ä‘á»‘i diá»‡n dá»±a trÃªn khoáº£ng thá»i gian an toÃ n gap =<sup>_d_opposite</sup> _v_ opposite<sup>.</sup> 

- Khoáº£ng trá»‘ng tá»›i háº¡n: crit_gapcar = 3 _._ 5 s, crit_gapmotorcycle = 3 _._ 0 s. 

- **HÃ nh vi nhÃ­ch chá»(Creeping):** Náº¿u min(gap) _<_ crit_gap, xe khÃ´ng dá»«ng cháº¿t táº¡i váº¡ch dá»«ng mÃ  nhÃ­ch tá»«tá»«( _v_ creep _â‰ˆ_ 1 _._ 0 _âˆ’_ 1 _._ 5 m _/_ s) vÃ o gáº§n tÃ¢m nÃºt ( _s_ = _âˆ’_ 1 _._ 0 m) chá»khoáº£ng trá»‘ng Ä‘á»ƒbá»©t tá»‘c. 

### **4.4 PhÃ¢n Ä‘á»‹nh quyá»n Æ°u tiÃªn & TrÃ¡nh xung Ä‘á»™t cáº¯t ngang** 

HÃ m `get_conflict_vehicle` giáº£i quyáº¿t va cháº¡m theo cÃ¡c má»©c: 

1. **Lá»c quá»¹Ä‘áº¡o:** Bá»qua cÃ¡c luá»“ng khÃ´ng giao cáº¯t váº­t lÃ½. 

2. **Quy táº¯c giáº£i phÃ³ng nÃºt giao:** Xe Ä‘Ã£ trong ngÃ£ tÆ° luÃ´n Ä‘Æ°á»£c Æ°u tiÃªn hÆ¡n xe Ä‘ang tiáº¿p cáº­n . 

3. **KhÃ´ng nhÆ°á»ng xe bá»‹Ä‘Ã¨n Ä‘á»cháº·n.** 

4. **Cháº¥m Ä‘iá»ƒm Æ°u tiÃªn theo TTI:** 

Score = _âˆ’_ 1 _._ 0 TTI + 1 _._ 5 _I_ straight + 0 _._ 5 _I_ right + 2 _._ 0 _I_ intersection 

Xe cÃ³ Ä‘iá»ƒm sá»‘tháº¥p hÆ¡n sáº½pháº£i nhÆ°á»ng. 

6 

### **4.5 Phanh phÃ²ng thá»§2D dá»±a trÃªn TTC khÃ´ngâ€“thá»i gian** 

#### **4.5.1 CÆ¡ sá»ŸlÃ½ thuyáº¿t** 

Thuáº­t toÃ¡n duyá»‡t qua tá»«ng phÆ°Æ¡ng tiá»‡n Ä‘á»‘i tÃ¡c _v_ xung quanh xe theo 5 bÆ°á»›c: 

**BÆ°á»›c 1: Chuyá»ƒn Ä‘á»•i sang há»‡quy chiáº¿u cá»¥c bá»™cá»§a xe tá»±hÃ nh** Gá»i tá»a Ä‘á»™vÃ  gÃ³c hÆ°á»›ng cá»§a xe tá»±hÃ nh lÃ  ( _x_ 0 _, y_ 0 _, Î¸_ 0) vÃ  cá»§a xe Ä‘á»‘i tÃ¡c _v_ lÃ  ( _xv, yv, Î¸v_ ). VectÆ¡ Ä‘á»™lá»‡ch vá»‹trÃ­ trong há»‡tá»a Ä‘á»™toÃ n cá»¥c: 



Chiáº¿u sang tá»a Ä‘á»™tÆ°Æ¡ng Ä‘á»‘i theo phÆ°Æ¡ng dá»c ( _s_ rel â€“ Forward) vÃ  phÆ°Æ¡ng ngang ( _d_ rel â€“ Lateral): 





Äá»™lá»‡ch gÃ³c hÆ°á»›ng giá»¯a hai xe: 



**BÆ°á»›c 2: Chiáº¿u kÃ­ch thÆ°á»›c hÃ¬nh há»™p vÃ  bÃ¹ gÃ³c ráº½** KÃ­ch thÆ°á»›c váº­t lÃ½ thá»±c cá»§a xe _v_ lÃ  chiá»u dÃ i _Lv_ vÃ  chiá»u rá»™ng _Wv_ . Khi nhÃ¬n tá»«há»‡quy chiáº¿u cá»§a Ego, kÃ­ch thÆ°á»›c bao ngoÃ i hÃ¬nh chiáº¿u cá»§a xe _v_ lÃ : 



_CÆ¡ cháº¿bÃ¹ gÃ³c ráº½:_ Khi xe _v_ Ä‘ang trong quÃ¡ trÃ¬nh quay vÃ²ng giá»¯a ngÃ£ tÆ° vÃ  ráº½trÃ¡i/pháº£i, thÃ¢n xe sáº½quÃ©t má»™t diá»‡n tÃ­ch ngang lá»›n hÆ¡n khi vÄƒng Ä‘uÃ´i: 



**BÆ°á»›c 3: XÃ¡c Ä‘á»‹nh hÃ nh lang va cháº¡m ngang** BÃ¡n kÃ­nh ná»­a hÃ nh lang an toÃ n Ä‘á»ƒ hai xe khÃ´ng quáº¹t ngang vÃ o nhau: 



Trong Ä‘Ã³ há»‡sá»‘bÃ¹ lá»an toÃ n: 

- Ego lÃ  **Xe mÃ¡y (** `Motorcycle` **):** margin = _âˆ’_ 0 _._ 2 m (cho phÃ©p xe mÃ¡y táº­n dá»¥ng khe há»Ÿháº¹p Ä‘á»ƒlÃ¡ch qua thÃ¢n Ã´ tÃ´). 

- Ego lÃ  **Ã” tÃ´ (** `Car` **):** margin = 0 _._ 0 m. 

7 

**BÆ°á»›c 4: Váº­n tá»‘c tÆ°Æ¡ng Ä‘á»‘i vÃ  xÃ¡c Ä‘á»‹nh cá»­a sá»•thá»i gian giao cáº¯t** [ _t_ start _, t_ end] Váº­n tá»‘c tÆ°Æ¡ng Ä‘á»‘i cá»§a xe _v_ Ä‘á»‘i vá»›i xe: 



Vá»›i chÃ¢n trá»i dá»±bÃ¡o tá»‘i Ä‘a _T_ horizon = 3 _._ 0 s, vá»‹trÃ­ ngang tÆ°Æ¡ng Ä‘á»‘i theo thá»i gian _t_ lÃ : 



Xe _v_ xÃ¢m pháº¡m hÃ nh lang an toÃ n ngang khi: 



â€¢ **TrÆ°á»ng há»£p chuyá»ƒn Ä‘á»™ng song song ngang (** _|v_ rel _,d| <_ 10<sup>_âˆ’_3</sup> **):** 



â€¢ **TrÆ°á»ng há»£p cÃ³ váº­n tá»‘c cáº¯t ngang (** _|v_ rel _,d| â‰¥_ 10<sup>_âˆ’_3</sup> **):** Thá»i Ä‘iá»ƒm báº¯t Ä‘áº§u cháº¡m vÃ  rá»i khá»i hÃ nh lang: 



Cá»­a sá»•thá»i gian giao cáº¯t thá»±c táº¿trong chÃ¢n trá»i dá»±Ä‘oÃ¡n lÃ : 



**BÆ°á»›c 5: ÄÃ¡nh giÃ¡ va cháº¡m theo khoáº£ng cÃ¡ch dá»c** Náº¿u _t_ start _â‰¤ t_ end, xe _v_ cháº¯c cháº¯n sáº½cáº¯t ngang máº·t Ego trong khoáº£ng [ _t_ start _, t_ end]. LÃºc nÃ y há»‡thá»‘ng tÃ­nh khoáº£ng cÃ¡ch Ä‘áº§uâ€“Ä‘uÃ´i giá»¯a 2 xe dá»c theo trá»¥c tiáº¿n: 



Äiá»u kiá»‡n xÃ¡c Ä‘á»‹nh **nguy cÆ¡ va cháº¡m** : 



Trong Ä‘Ã³ _R_ scan lÃ  bÃ¡n kÃ­nh quÃ©t Ä‘á»™ng tÆ°Æ¡ng á»©ng vá»›i quÃ£ng Ä‘Æ°á»ng phanh: 



Náº¿u thá»a mÃ£n Ä‘iá»u kiá»‡n va cháº¡m trÃªn vÃ  Ä‘á»‘i tÆ°á»£ng náº±m á»ŸphÃ­a trÆ°á»›c mÅ©i xe ( _s_ rel _>_ 0 _._ 2 m), xe _v_ chÃ­nh lÃ  Ä‘á»‘i tÆ°á»£ng cáº§n phanh kháº©n cáº¥p phÃ²ng thá»§. 

8 

#### **4.5.2 CÆ¡ cháº¿tÃ­ch há»£p vÃ o kiáº¿n trÃºc Ä‘iá»u khiá»ƒn tá»•ng thá»ƒ** 

Thuáº­t toÃ¡n TTC khÃ´ng tÃ¡c Ä‘á»™ng lá»±c phanh ngáº¯t quÃ£ng mÃ  tÃ­ch há»£p mÆ°á»£t mÃ  vÃ o luá»“ng Ä‘iá»u khiá»ƒn: 

1. **Sinh chÆ°á»›ng ngáº¡i váº­t áº£o (** `DummyVehicle` **):** Khi phÃ¡t hiá»‡n xe _v_ nguy hiá»ƒm qua TTC, bá»™Ä‘iá»u khiá»ƒn táº¡o má»™t xe áº£o náº±m trÃªn trá»¥c Frenet cá»§a Ego: 

_s_ dummy = _s_ ego + _s_ rel _v_ dummy = max(0 _._ 0 _, vv_ cos âˆ† _Î¸_ ) 

GÃ¡n cÃ¡c thuá»™c tÃ­nh kÃ­ch thÆ°á»›c hÃ¬nh chiáº¿u _Lv,_ proj, hÆ°á»›ng ráº½vÃ  tráº¡ng thÃ¡i hÃ nh trÃ¬nh cá»§a _v_ vÃ o váº­t thá»ƒáº£o nÃ y. 

2. **TÃ­ch há»£p vÃ o mÃ´ hÃ¬nh IDM:** Trong hÃ m cáº­p nháº­t `step()` , náº¿u `defensive_dummy` cÃ³ vá»‹trÃ­ gáº§n hÆ¡n xe Ä‘i trÆ°á»›c thÃ´ng thÆ°á»ng, nÃ³ sáº½Ä‘Æ°á»£c gÃ¡n lÃ m `lead_veh` . HÃ m `compute_idm()` sáº½tá»±Ä‘á»™ng tÃ­nh gia tá»‘c giáº£m tá»‘c _a_ target Ãªm Ã¡i, Ä‘áº£m báº£o xe dá»«ng trÆ°á»›c Ä‘iá»ƒm giao cáº¯t. 

3. **Phá»‘i há»£p vá»›i cÆ¡ cháº¿lÃ¡ch lÃ n :** Náº¿u váº­t cáº£n gÃ¢y nguy cÆ¡ TTC lÃ  má»™t xe ráº½trÃ¡i Ä‘ang dá»«ng nhÃ­ch chá»giá»¯a ngÃ£ tÆ°, xe Ä‘i tháº³ng phÃ­a sau nháº­n diá»‡n váº­t thá»ƒáº£o nÃ y vÃ  kÃ­ch hoáº¡t hÃ nh vi lÃ¡ch qua sÆ°á»n pháº£i cá»§a xe ráº½trÃ¡i thay vÃ¬ dá»«ng cháº¿t, ngÄƒn ngá»«a hiá»‡n tÆ°á»£ng ngháº½n máº¡ng giao thÃ´ng (Deadlock). 

#### **4.5.3 PhÃ¢n biá»‡t TTC vá»›i cÃ¡c Ä‘áº¡i lÆ°á»£ng thá»i gian trong mÃ´ hÃ¬nh** 

Báº£ng 2: So sÃ¡nh cÃ¡c chá»‰sá»‘thá»i gian dÃ¹ng trong cÃ¡c bÃ i toÃ¡n Ä‘iá»u khiá»ƒn 

|**KhÃ¡i niá»‡m**|**CÃ´ng**<br>**thá»©c**<br>**cá»‘t lÃµi**|**Má»¥c Ä‘Ã­ch sá»­dá»¥ng**|
|---|---|---|
|**TTC 2D**|_t_<br>=<br>_Â±W_corridor_âˆ’d_rel<br>_v_rel_,d_<br>káº¿t há»£p gap(_t_)|Phanh kháº©n cáº¥p phÃ²ng thá»§2D (AEB), chá»‘ng va cháº¡m<br>Ä‘Ã¢m ngang thÃ¢n/cáº¯t Ä‘áº§u xe.|
|**TTI (Conflict)**|TTI = <sup>_d_to_center</sup><br>_v_eff|XÃ¡c Ä‘á»‹nh thá»©tá»±Æ°u tiÃªn nhÆ°á»ng Ä‘Æ°á»ng theo luáº­t giá»¯a<br>cÃ¡c nhÃ¡nh tiáº¿p cáº­n ngÃ£ tÆ°.|
|**TTI (Dilemma)**|TTI = <sup>_d_to_stop</sup><br>_v_ego|TÃ­nh xÃ¡c suáº¥t Dá»«ng hay Äi (_P_stop) khi chuyá»ƒn Ä‘Ã¨n<br>vÃ ng.|
|**Critical Gap**|Gap =<br>_d_opposite<br>_v_opp<br>(3_._5 s Car, 3_._0 s<br>Moto)|ÄÃ¡nh giÃ¡ khe há»Ÿan toÃ n cá»§a dÃ²ng xe Ä‘á»‘i diá»‡n khi xe<br>ráº½trÃ¡i cáº¯t qua.|



### **4.6 Kiá»ƒm soÃ¡t tá»‘c Ä‘á»™an toÃ n khi qua nÃºt giao** 

Trong pháº¡m vi quÃ£ng Ä‘Æ°á»ng hÃ£m phanh _D_ decel trÆ°á»›c váº¡ch dá»«ng, tráº§n váº­n tá»‘c Ä‘Æ°á»£c háº¡ xuá»‘ng: 

_v_ des _,_ left _â‰ˆ_ 4 _._ 95 m _/_ s _, v_ des _,_ right _â‰ˆ_ 2 _._ 45 m _/_ s _, v_ des _,_ straight = 5 _._ 0 m _/_ s 

9 

## **TÃ“M Táº®T Cáº¤U TRÃšC THUáº¬T TOÃN** 

ToÃ n bá»™mÃ´ phá»ng cÃ³ thá»ƒÄ‘Æ°á»£c biá»ƒu diá»…n theo chuá»—i xá»­lÃ½ khÃ©p kÃ­n: 

Traffic Generation _â†’_ Vehicle Dynamics _â†’_ IDM _â†’_ Intersection Control _â†’_ Conflict Resolution _â†’_ 2D 

Trong Ä‘Ã³ tráº¡ng thÃ¡i xe táº¡i má»—i chu ká»³ âˆ† _t_ = 0 _._ 1 s lÃ : 

Vehicle State = [ _x, y, v, Î¸, s, d,_ route _,_ state] vÃ  toÃ n bá»™phÆ°Æ¡ng tiá»‡n tÆ°Æ¡ng tÃ¡c phi tuyáº¿n thÃ´ng qua cÆ¡ cháº¿tá»•ng há»£p: IDM + Dummy Vehicle + Gap Acceptance + Conflict Resolution + 2D TTC + Lateral Swerving 

10 

