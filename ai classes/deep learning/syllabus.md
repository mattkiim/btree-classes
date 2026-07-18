# Deep Learning for High Schoolers — Syllabus

**Format:** ~14 weeks, one unit per week
**Approach:** Project-first, using PyTorch throughout — every concept is introduced by training a real model on a real (or realistic) dataset. 

**Prerequisite:** The Machine Learning course (specifically Weeks 7–9: intro to neural networks, backpropagation, CNNs). This course assumes students can already build and train a basic feedforward/CNN model and understand gradient descent and backprop at a conceptual and mathematical level — it does not re-derive those from scratch. 

---

## Week 1 — Review and the Deep Learning Toolkit
- **Concepts:** quick recap of forward pass/backprop from the ML course, moving from from-scratch NumPy to PyTorch, autograd, `nn.Module`, GPUs and why they matter
- **Project:** reimplement Week 7–8 of the ML course (a small classifier) in idiomatic PyTorch instead of from-scratch NumPy
- **Deliverable:** PyTorch training loop template students will reuse for the rest of the course

## Week 2 — Optimization in Practice
- **Concepts:** SGD vs. momentum vs. Adam, learning rate schedules, batch size effects, loss landscapes, vanishing/exploding gradients
- **Dataset:** CIFAR-10 (or Fashion-MNIST for a lighter-weight version)
- **Activity:** train the same architecture with different optimizers/learning rates side by side, compare convergence curves
- **Deliverable:** report comparing 3+ optimizer configurations on the same model

## Week 3 — Regularization and Generalization at Scale
- **Concepts:** dropout, batch normalization, weight decay, data augmentation, why deep nets overfit differently than shallow models
- **Dataset:** CIFAR-10
- **Activity:** train an intentionally overfit model, then apply regularization techniques one at a time and measure the effect on the train/validation gap
- **Deliverable:** ablation table showing accuracy with/without each regularization technique

## Week 4 — Convolutional Architectures in Depth
- **Concepts:** stacking conv layers, receptive fields, residual connections (ResNet), why depth alone doesn't help without skip connections
- **Dataset:** CIFAR-10 or a subset of ImageNet (e.g. Imagenette)
- **Activity:** build a plain deep CNN and a ResNet of similar depth, compare training stability and final accuracy
- **Deliverable:** trained ResNet + comparison plot vs. plain CNN

## Week 5 — Transfer Learning and Fine-Tuning
- **Concepts:** pretrained models, feature extraction vs. fine-tuning, why transfer learning works, freezing layers
- **Dataset:** a small custom image dataset (students can collect their own — e.g. classifying objects around school)
- **Activity:** fine-tune a pretrained ResNet/EfficientNet on the small custom dataset, compare to training from scratch on the same small dataset
- **Deliverable:** fine-tuned model + writeup on why transfer learning outperforms training from scratch here

## Week 6 — Recurrent Neural Networks and Sequence Modeling
- **Concepts:** sequential data, hidden state, vanishing gradients over time, LSTM/GRU gating intuition
- **Dataset:** a character-level text dataset (e.g. generating text in a chosen author's style) or a simple time series
- **Activity:** train a vanilla RNN and an LSTM on the same sequence task, compare their ability to capture longer dependencies
- **Deliverable:** trained LSTM that generates plausible sequences + comparison to vanilla RNN failure cases

## Week 7 — Attention Mechanisms
- **Concepts:** the limitation of fixed hidden-state bottlenecks in RNNs, attention as a learned weighted lookup, query/key/value intuition
- **Dataset:** a sequence-to-sequence task (e.g. simple translation or date-format conversion) small enough to train in-class
- **Activity:** implement additive or dot-product attention on top of an RNN encoder-decoder, visualize attention weights as a heatmap over the input sequence
- **Deliverable:** attention heatmap visualization + short explanation of what the model is "looking at"

## Week 8 — Transformers
- **Concepts:** self-attention, multi-head attention, positional encoding, why transformers parallelize better than RNNs
- **Dataset:** same or similar sequence task as Week 7
- **Activity:** implement a minimal transformer encoder block from the building blocks covered (attention, layer norm, feedforward), or walk through and modify a minimal reference implementation
- **Deliverable:** working transformer block trained on the sequence task, benchmarked against the RNN from Week 6

## Week 9 — Large Language Models: How They Work
- **Concepts:** tokenization, next-token prediction, scaling laws (conceptually), pretraining vs. fine-tuning, why "next-token prediction" produces surprisingly general capability
- **Dataset:** a small text corpus for a mini GPT-style model (e.g. character-level Shakespeare, following the classic nanoGPT-style exercise)
- **Activity:** train a small decoder-only transformer to generate text, inspect outputs at different training checkpoints
- **Deliverable:** trained mini-GPT + generated samples at multiple checkpoints showing progression

## Week 10 — Generative Models I: Autoencoders and VAEs
- **Concepts:** encoder/decoder architectures, latent space, reconstruction loss, the "variational" idea (sampling from a learned distribution)
- **Dataset:** MNIST or Fashion-MNIST
- **Activity:** train a plain autoencoder, then a VAE; compare latent space interpolations between the two
- **Deliverable:** latent space visualization + interpolated image sequence

## Week 11 — Generative Models II: GANs
- **Concepts:** generator/discriminator adversarial training, mode collapse, why GANs are notoriously hard to train
- **Dataset:** MNIST or a small curated image dataset
- **Activity:** train a simple GAN, observe and diagnose training instability (e.g. discriminator overpowering generator)
- **Deliverable:** generated image samples + a short writeup diagnosing at least one training pathology observed

## Week 12 — Generative Models III: Diffusion Models
- **Concepts:** forward noising process, learning to denoise, why diffusion models produce more stable training than GANs, connection back to the score/gradient intuition from Week 2
- **Dataset:** MNIST or a small image dataset (full-scale diffusion training is expensive — use a minimal/toy diffusion implementation)
- **Activity:** implement or adapt a minimal diffusion model, visualize the denoising process step by step
- **Deliverable:** visualization of the reverse diffusion process generating an image from noise

## Week 13 — Efficiency, Scaling, and Practical Constraints
- **Concepts:** model size vs. compute tradeoffs, quantization, distillation, why training large models is expensive, practical debugging of training runs (loss spikes, NaNs, data pipeline bottlenecks)
- **Dataset:** revisit any prior project
- **Activity:** apply quantization or distillation to a previously trained model, measure the size/speed/accuracy tradeoff
- **Deliverable:** before/after comparison table (model size, inference speed, accuracy)

## Week 14 — Final Projects
- **Concepts:** end-to-end deep learning workflow — problem framing, architecture choice, training, evaluation, and communicating results
- **Dataset:** student's choice
- **Activity:** final project — students pick a problem (image, text, generative, or otherwise) and apply techniques from the course
- **Deliverable:** final project presentation/report

---

## Anchor Tools & Libraries
- **PyTorch** — used exclusively from Week 1 onward for consistency; the ML course's NumPy-first approach is intentionally left behind here
- **torchvision / torchtext** — pretrained models and standard datasets (CIFAR-10, Imagenette)
- **Weights & Biases or TensorBoard** — training curve logging, introduced early (Week 2) so students get used to monitoring runs rather than just reading final accuracy numbers
- **Google Colab** (or equivalent free GPU access) — essential from Week 4 onward once CIFAR-10/ImageNet-scale training makes CPU-only training impractical

## Structural Notes
- Weeks 6–9 (RNNs → attention → transformers → LLMs) form the single biggest conceptual arc in the course and are natural candidates for extending to 1.5–2 weeks each if time allows — attention in particular is worth slowing down for, since it's the hardest single idea in the course to build real intuition for quickly.
- Weeks 10–12 (generative models) can be compressed to two weeks (VAE+GAN combined, diffusion separate) if the course needs to run shorter than 14 weeks — diffusion is the most conceptually rich of the three and worth keeping as its own week if anything has to give.
- This course assumes GPU access (Colab or school-provided) starting Week 4 — flag this as a logistics dependency early in the term, since CIFAR-10/ImageNet-scale training on CPU alone will frustrate students.
- As with the RL course, keep visualizations central: attention heatmaps, latent space interpolations, and denoising sequences are often more illuminating to students than loss curves alone.