# Alpha Solution for Robust FST

### Algorithm

:fire: **preliminary**

Filtered Image A - Content Image B $\rightarrow$ Filtered Image B

<img src="C:\Users\ZenMoore\AppData\Roaming\Typora\typora-user-images\image-20210713163317743.png" alt="image-20210713163317743" style="zoom:67%;" />

`intra-image semantic correlation : modeling the relation between difference semantic objects in one image `

`inter-image semantic correspondence : modeling the consistency between similar semantic objects between image pairs` 

:fire: **basic FST algorithm**

paper : [photoFST](https://arxiv.org/abs/2007.07925)

<img src="C:\Users\ZenMoore\AppData\Roaming\Typora\typora-user-images\image-20210713163640598.png" alt="image-20210713163640598" style="zoom:67%;" />

:fire: **semantic enhancement** (analyze and experiment in order)

​	:one: sort out semantic-related images

- [x] (search online) organize semantically related images at the beginning of dataset construction (c.f. [dataset construction section of this paper](https://www.sciencedirect.com/science/article/pii/S0925231220305920))
- [ ] (search online) use existing algorithms to calculate the semantic similarity of each image pair and then organize pairs of highly similar images together

​	:two: semantic segmentation and matching

- [x] (search online) use existing algorithm for semantic segmentation and semantic correspondence
- [ ] an advanced algorithm for segmentation (c.f. [the survey](https://ieeexplore.ieee.org/document/9356353)) or matching (e.g. [Hiperpixel Flow](https://arxiv.org/pdf/1908.06537.pdf), [COTR](https://arxiv.org/abs/2103.14167), etc.)

​	:three: semantic-aware generator

There are overall four types of semantic-aware strategies : masking out (c.f. [this paper](http://www.bmva.org/bmvc/2016/papers/paper008/index.html)), semantic-aware feature (c.f. [this paper](https://www.sciencedirect.com/science/article/pii/S0893608020301982)), semantic channel (c.f. [Semantic GAN](https://ieeexplore.ieee.org/document/8784957)), semantic-aware loss (mainly, c.f. [this paper](https://www.sciencedirect.com/science/article/pii/S0925231220305920 ))

- [x] semantic channel and semantic-aware loss
- [ ] semantic-aware feature
- [ ] masking out

​	:four: inter-image semantic correspondence

The former method uses semantic information instead of correspondence information because the correspondence feature is learned during the semantic-aware training process. Intuitively, this slows down the training speed and increases instability. Therefore, we explore a method that directly use correspondence information instead of only semantic information.

- [x] add up the semantic channel and correspondence channel and redefine the loss if necessary
- [ ] replace the semantic channel by the correspondence channel and redefine the loss if necessary
- [ ] correspondence map facilitates the masking out, just show it
- [ ] don't know how to improve it if it uses semantic-aware feature...

### Task

:fire: **work pipeline**

:a: implementation of basic FST algorithm (runnable) $\to$ :b: improvement by semantic guidance $\to$ :bulb:experiment by other ideas (listed in the work detail section)

:fire: **work matrix**

| member          | :a:                          | :b:                                                          | :bulb:          |
| --------------- | ---------------------------- | ------------------------------------------------------------ | --------------- |
| Zekun           | guidance                     | guidance                                                     | decision        |
| Zizhao          | with Yakun                   | with Ruiqi                                                   | coding          |
| Yakun           | with Zizhao                  | with Ruiqi                                                   | coding          |
| Ruiqi           | fondamental image processing | semantic trick adding                                        | coding (assist) |
| **description** | pure basic FST algorithm     | according to the methodology introduced in the semantic ST papers | enrichment      |

`FST : Filter Style Transfer; ST : Style Transfer`

:fire: **work detail**

:a: : how to re-produce the algorithm introduced in [photoFST](https://arxiv.org/abs/2007.07925)

- :star2: *Zizhao* does work related to <u>defilterization, filter style estimation, filtered image generation</u>.
- *Yakun* does work related to <u>filter adaptation (i.e. alignment), dataset, metric (i.e. evaluation)</u>. *Yakun* is doing the work the other two members do, hence acts as an <u>intermediary</u> and <u>coordinator</u>.
- *Ruiqi* does work related to <u>data pre-processing, data post-processing, dataset, data augmentation, etc.</u>, and <u>quickly finish the paper reading/code learning tasks about semantic (i.e. how to use semantic segmentation techniques to guide the style transfer)</u>.
- :star2: *Zekun* makes <u>work evaluation, decision, debug guidance, work guidance, etc</u>.

:b: : how to improve the performance by semantic style transfer methods

- *Zizhao* <u>modifies</u> the work that have been done to adapt to the improvement (semantic-wise).
- *Yakun* <u>modifies</u> the filter adaptation according to the PSGAN Morphing Module method (i.e. assign some fondamental landmarks for each semantic (or only the main semantic) and design the morphing module in the way of one-model-for-all (or one-model-for-main)).
- :star2: *Ruiqi* gives the <u>semantic segmentation</u> method, and cooperates to give a method to <u>fuse the semantic information</u> into all/some parts of the whole pipeline.
- :star2: *Zekun* makes <u>work evaluation, decision, debug guidance, work guidance, etc</u>.

:bulb: : how to enrich originality and further improve performance

A better performance lies in the three-way trade-off between speed, flexibility and quality (c.f. [the survey](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8732370&tag=1)).

​	:smile: enhance with spatial correlation and logical correlation between semantics (i.e. intra-image semantic correlation). (Prof.Yu)

- [x] combine Graph (semantic correlation graph) with GAN
- [ ] combine Graph (semantic correlation graph) with vanilla model

`intra-image semantic correlation : modeling the relation between difference semantic objects in one image `

`inter-image semantic correspondence : modeling the consistency between similar semantic objects between image pairs` 

​	:smile: GANization

- [x] (search online) simply add a discriminator, which is implemented on github
- [ ] not only add a discriminator but also replace the style estimation strategy and generation strategy by generator strategy, which can be [AdaIN](https://arxiv.org/pdf/1703.06868.pdf), another encoder (e.g. [this paper](https://www.sciencedirect.com/science/article/pii/S0925231220305920?via%3Dihub), [StyleBank](https://arxiv.org/pdf/1703.09210.pdf), etc. c.f. [the survey](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8732370&tag=1)) , style-based generator (c.f. [StyleGAN](https://ieeexplore.ieee.org/document/8953766)), or other generator ([TransGAN](https://arxiv.org/abs/2102.07074), [Semantic GAN](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8784957), [PSGAN](https://arxiv.org/abs/1909.06956), [AnimeGANv2](https://tachibanayoshino.github.io/AnimeGANv2/), etc.)

​	:question: interpretation and solution to adversarial examples (c.f. [the survey](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8732370&tag=1)).

​	:question: other semantic-aware generator or inter-image semantic correspondence-aware generator

​	:question: apply hot spot model, e.g., MLP, Vision Transformer, etc.

​	:question: focus on some perceptual factors (stroke/edge, colour, etc.).

​	:question: using IN/CIN/AdaIN (i.e. three kinds of instance normalization), or even further, create another way of instance normalization (e.g. logistic IN), interpret it !

​	:question: deal with the portrait specifically (we can also use PSGAN methods, or gain maps (c.f. [the survey](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8732370&tag=1))).

​	:question: innovative style representation (channel-wise ? feature statistics ? Bolei Zhou's method (c.f. [role of 		individual unit](https://www.pnas.org/content/117/48/30071)) !). Or rather disentangled methods (c.f. [the survey](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8732370&tag=1)).

​	:question: controllable perceptual factors ? real-time ? video ?

​	:question: ++photorealistic style transfer

​	:thinking: to be continued...