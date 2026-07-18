# Machine Learning for High Schoolers — Syllabus

**Format:** ~14 weeks, one unit per week
**Approach:** Dataset/project-first — every concept is introduced through a real (or realistic) dataset students can load, explore, and model in Python.
**Relationship to RL course:** This course covers the supervised/unsupervised ML foundations that make a natural prerequisite (or parallel companion) to the Reinforcement Learning course — e.g. gradient descent here directly prepares students for TD updates and policy gradients there, and the neural network units here set up Deep Q-learning and PPO.

---

## Week 1 — What is Machine Learning?
- **Concepts:** ML vs. traditional programming, supervised vs. unsupervised vs. reinforcement learning (brief contrast), training/test splits, the idea of "learning from data"
- **Dataset:** a simple, visual dataset (e.g. Iris, or a hand-labeled toy dataset students help create in class)
- **Activity:** manually write a rule-based classifier, then compare against a trained model on the same data
- **Deliverable:** short reflection on where hand-written rules broke down

## Week 2 — Linear Regression
- **Concepts:** features, targets, model as a function, mean squared error, the idea of "fitting a line"
- **Dataset:** a simple 1–2 feature regression dataset (e.g. house size vs. price)
- **Activity:** fit a line by hand/eyeballing it, then fit with `numpy.polyfit` or closed-form least squares, compare
- **Deliverable:** plotted regression line + MSE on a held-out test set

## Week 3 — Gradient Descent
- **Concepts:** loss surfaces, gradients, learning rate, iterative optimization
- **Dataset:** same regression dataset as Week 2
- **Activity:** implement gradient descent from scratch for linear regression, visualize loss decreasing over iterations; experiment with learning rate (too small, too large, "just right")
- **Deliverable:** from-scratch gradient descent implementation + loss curve plot

## Week 4 — Classification and Logistic Regression
- **Concepts:** decision boundaries, sigmoid function, cross-entropy loss, classification metrics (accuracy, precision, recall)
- **Dataset:** a binary classification dataset (e.g. spam/not-spam, or a simple medical/synthetic dataset)
- **Activity:** implement logistic regression, visualize the decision boundary on 2D data
- **Deliverable:** trained classifier + confusion matrix

## Week 5 — Decision Trees and Random Forests
- **Concepts:** splits, information gain/Gini impurity, overfitting a single tree, ensembling
- **Dataset:** a tabular dataset with mixed feature types (e.g. Titanic survival)
- **Activity:** grow a decision tree by hand on a tiny example, then use scikit-learn to fit a tree and a random forest, compare
- **Deliverable:** feature importance plot + comparison of tree vs. forest accuracy

## Week 6 — Overfitting, Regularization, and Model Evaluation
- **Concepts:** bias-variance tradeoff, train/validation/test splits, L1/L2 regularization, cross-validation
- **Dataset:** revisit Week 5's dataset or a new one with more features than examples
- **Activity:** deliberately overfit a model (e.g. a high-degree polynomial or unpruned tree), then regularize it back down; plot train vs. validation error as model complexity increases
- **Deliverable:** train/validation error curve showing the overfitting "sweet spot"

## Week 7 — Introduction to Neural Networks
- **Concepts:** perceptrons, activation functions, layers, forward pass, why nonlinearity matters
- **Dataset:** a dataset not linearly separable (e.g. two-moons or XOR-like synthetic data)
- **Activity:** show logistic regression failing on the non-separable data, then fit a small neural net (2 layers) that succeeds; visualize the learned decision boundary
- **Deliverable:** small neural net trained from scratch (numpy) or with a minimal framework

## Week 8 — Backpropagation and Training Neural Networks
- **Concepts:** chain rule, backprop as gradient computation, batches, epochs, weight initialization
- **Dataset:** same as Week 7, or a slightly larger tabular dataset
- **Activity:** implement backprop by hand for a tiny 2-layer network (no autograd), then verify against PyTorch/TensorFlow's automatic gradients
- **Deliverable:** hand-derived backprop implementation matching framework output

## Week 9 — Convolutional Neural Networks and Image Data
- **Concepts:** convolutions, pooling, why CNNs exploit spatial structure, basic architectures
- **Dataset:** MNIST or Fashion-MNIST
- **Activity:** build and train a small CNN in PyTorch/Keras, visualize learned filters and misclassified examples
- **Deliverable:** trained CNN + accuracy report + a few visualized filters

## Week 10 — Unsupervised Learning: Clustering
- **Concepts:** k-means, cluster assignment, choosing k, when there's no ground-truth label
- **Dataset:** an unlabeled dataset with natural groupings (e.g. customer segmentation data, or color-based image pixel clustering)
- **Activity:** implement k-means from scratch, visualize clusters forming over iterations
- **Deliverable:** clustered visualization + discussion of how to choose k (elbow method)

## Week 11 — Dimensionality Reduction
- **Concepts:** curse of dimensionality, PCA, variance explained, visualization of high-dimensional data
- **Dataset:** a high-dimensional dataset (e.g. MNIST pixels, or a gene expression / wide tabular dataset)
- **Activity:** apply PCA to reduce to 2D and visualize; compare to a raw random 2-feature projection to show PCA isn't arbitrary
- **Deliverable:** 2D PCA visualization + explained-variance plot

## Week 12 — Introduction to NLP and Embeddings
- **Concepts:** text as data, bag-of-words vs. embeddings, word similarity, basic sentiment analysis
- **Dataset:** a small text classification dataset (e.g. movie review sentiment)
- **Activity:** build a bag-of-words classifier, then compare against pretrained word embeddings for the same task
- **Deliverable:** sentiment classifier + a short exploration of nearest-neighbor words in embedding space

## Week 13 — ML Ethics, Fairness, and Failure Modes
- **Concepts:** bias in data and models, fairness metrics, dataset shift, real-world failure case studies
- **Dataset:** a dataset with a known documented bias issue (e.g. COMPAS recidivism, or a hiring/lending toy dataset)
- **Activity:** measure a model's performance disparities across subgroups; discuss mitigation strategies and their tradeoffs
- **Deliverable:** written analysis of a fairness metric applied to the dataset

## Week 14 — Final Projects
- **Concepts:** end-to-end ML workflow — problem framing, data cleaning, model selection, evaluation, communication of results
- **Dataset:** student's choice
- **Activity:** final project — students pick a dataset/problem, apply techniques from the course, and present results
- **Deliverable:** final project presentation/report

---

## Anchor Tools & Libraries
- **NumPy** — from-scratch implementations (linear regression, gradient descent, k-means, backprop) to build real understanding before reaching for frameworks
- **scikit-learn** — standard models (trees, forests, logistic regression) and evaluation utilities
- **PyTorch or Keras** — neural networks from Week 7 onward (pick one and stay consistent)
- **Matplotlib / Seaborn** — visualization throughout; decision boundaries, loss curves, and cluster plots are used repeatedly across units
- **Pandas** — dataset loading and cleaning, introduced informally starting Week 1

## Structural Notes
- Weeks 2–3 (regression → gradient descent) and Weeks 7–8 (neural nets → backprop) are natural candidates for extending to 1.5–2 weeks each, since the "implement it from scratch" activities take real time to debug.
- Consider running this course **before or alongside** the RL course: Week 3's from-scratch gradient descent directly prepares students for the incremental-update math in RL's bandit and TD-learning units, and Weeks 7–9 (neural networks, backprop, CNNs) are a direct prerequisite for Deep Q-learning (RL Week 10) and policy gradients (RL Week 11).
- As with the RL course, keep early units light on formalism and lean into visual, hands-on intuition (decision boundaries, loss curves, cluster animations) before introducing heavier notation.