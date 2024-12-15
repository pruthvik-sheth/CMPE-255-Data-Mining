# Short Story Assignment: CMPE 255

## Topic

**Research Paper:** [Distributional Reduction: Unifying Dimensionality Reduction and Clustering with Gromov-Wasserstein](https://arxiv.org/abs/2402.02239)  
**Authors:** Hugues Van Assel, Cédric Vincent-Cuaz, Nicolas Courty, Rémi Flamary, Pascal Frossard, Titouan Vayer.  
**Summary:** This research paper introduces "Distributional Reduction" (DistR), a novel unified framework that combines dimensionality reduction (projecting data to lower dimensions) and clustering (organizing data into groups) into a single optimization problem. The method leverages optimal transport theory, specifically the Gromov-Wasserstein framework, to find a reduced distribution that best represents the original data distribution while preserving its underlying structure. The key innovation is that DistR constructs an input similarity matrix that is matched with an embedding similarity through an optimal transport coupling matrix, allowing it to simultaneously handle both dimensionality reduction and clustering tasks. When tested on multiple image and genomic datasets, DistR demonstrated superior performance in identifying low-dimensional prototypes and showed better trade-offs between local and global structure preservation compared to traditional sequential approaches, while being computationally efficient using GPU acceleration.

## Deliverables

### 1. Medium Article

- **Link:** [Medium Article](https://medium.com/@pns00911/distributional-reduction-a-novel-framework-unifying-dimensionality-reduction-and-clustering-0a5b3430d0bf)
- **Overview:** The Medium article summarizes the research paper's key contributions, focusing on the architecture, methodology, ablation studies, metrics, and experimental results. It also includes visualizations to enhance understanding.

### 2. Slide Presentation

- **Link:** [Slideshare Presentation](https://www.slideshare.net/slideshow/distributional-reduction-unifying-dimensionality-reduction-and-clustering-d489/274093326)
- **Overview:** A concise presentation covering the core ideas of the research, designed for a 10–15 minute video recording. The slides emphasize visuals and high-level insights from the paper.

### 3. Video Presentation

- **Link:** [YouTube Video](https://youtu.be/8yKBuL4tgFw)
- **Overview:** A recorded video presentation that explains the paper and its relevance to data mining, clustering, and dimensionality reduction in an accessible and engaging manner.
