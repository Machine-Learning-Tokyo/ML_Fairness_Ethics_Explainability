# Fairness, Ethics, Explainability in AI and ML

This repository provides resources, tools and notebooks for Fairness, Ethics, Explainability in AI and ML.

## Contents

- [Resources](#resources)
  - [Fairness and machine learning](#fairness-and-machine-learning)
  - [Video tutorials](#video-tutorials)
  - [Courses](#courses)
  - [Blog posts](#blog-posts)
- [Tools](#tools)
  - [Lime](#lime)
  - [Captum](#captum)
  - [AllenNLP Interpret](#allennlp-interpret)
  - [ELI5](#eli5)
  - [ML Fairness Gym](#ml-fairness-gym)
 - [Notebooks](https://github.com/Machine-Learning-Tokyo/ML_Fairness_Ethics_Explainability/tree/master/notebooks)


# Resources

## Fairness and machine learning
### By Solon Barocas, Moritz Hardt, Arvind Narayanan

[Online text book [WIP]](https://fairmlbook.org/)

1.	Introduction
2.	Classification
3.	Legal background and normative questions	
4.	Causality
5.	Testing discrimination in practice
6.	A broader view of discrimination	
7.	Measurement	
8.	Algorithmic interventions		
- Appendix: Technical background


## Video tutorials
- [Fairness in machine learning (NIPS 2017)](https://fairmlbook.org/tutorial1.html)
- [21 fairness definitions and their politics (FAT* 2018)](https://fairmlbook.org/tutorial2.html)

## Courses
- [Berkeley CS 294 (2017): Fairness in machine learning](https://fairmlclass.github.io/)
- [Cornell INFO 4270 (2017): Ethics and policy in data science](https://docs.google.com/document/d/1GV97qqvjQNvyM2I01vuRaAwHe9pQAZ9pbP7KkKveg1o/edit)
- [Princeton COS 597E (2017): Fairness in machine learning](https://docs.google.com/document/d/1XnbJXELA0L3CX41MxySdPsZ-HNECxPtAw4-kZRc7OPI/edit)

## Blog posts

### Distill

- [The Building Blocks of Interpretability – distill.pub (2018)](https://distill.pub/2018/building-blocks/)

"Interpretability techniques are normally studied in isolation.
We explore the powerful interfaces that arise when you combine them — 
and the rich structure of this combinatorial space."

[<p align="center"><img src="https://github.com/Machine-Learning-Tokyo/ML_Fairness_Ethics_Explainability/blob/master/images/distillpub.png" width="600"></p>](https://distill.pub/2018/building-blocks/)

### OpenAI Microscope

OpenAI introduced Microscope – a collection of visualizations of layers and neurons of several common deep learning models that are often studied in interpretability. Microscope makes it easier to analyze the features that form inside these neural networks.

Source: [OpenAI](https://microscope.openai.com/about)

[<p align="center"><img src="https://github.com/Machine-Learning-Tokyo/AI-ML-Newsletter/blob/master/images/openai_microscope.png" width="600"></p>](https://microscope.openai.com/models)


# Tools

## Lime

Lime is about explaining what machine learning models are doing. It supports explaining individual predictions for text classifiers or classifiers that act on tables (numpy arrays of numerical or categorical data) or images, with a package called lime (short for **local interpretable model-agnostic explanations**). Lime is based on the work presented in the paper ["Why Should I Trust You?": Explaining the Predictions of Any Classifier" (2016)](https://arxiv.org/abs/1602.04938) by Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin. 

Source: [Lime, GitHub](https://github.com/marcotcr/lime)

[<p align="center"><img src="https://github.com/Machine-Learning-Tokyo/ML_Fairness_Ethics_Explainability/blob/master/images/lime.png" width="600"></p>](https://github.com/marcotcr/lime
)

## Captum
Model Interpretability for PyTorch. [[Tutorials]](https://captum.ai/tutorials/IMDB_TorchText_Interpret)

- Supports interpretability of models across modalities including vision, text, and more
- Supports most types of PyTorch models and can be used with minimal modification to the original neural network
- Open source, generic library for interpretability research. Easily implement and benchmark new algorithms

Source: [Captum](https://captum.ai/tutorials/Bert_SQUAD_Interpret)

[<p align="center"><img src="https://github.com/Machine-Learning-Tokyo/ML_Fairness_Ethics_Explainability/blob/master/images/captum.png" width="600"></p>](https://captum.ai/tutorials/IMDB_TorchText_Interpret)

## AllenNLP Interpret
A Framework for Explaining Predictions of NLP Models by Eric Wallace, Jens Tuyls, Junlin Wang, Sanjay Subramanian,
Matt Gardner, and Sameer Singh

AllenNLP Interpret is a toolkit built on top of AllenNLP for interactive model interpretations. The toolkit makes it easy to apply gradient-based saliency maps and adversarial attacks to new models, as well as develop new interpretation methods. It contains three components: a suite of interpretation techniques applicable to most models, APIs for developing new interpretation methods (e.g., APIs to obtain input gradients), and reusable front-end components for visualizing the interpretation results.

Source: [AllenNLP Interpret](https://allennlp.org/interpret)

[<p align="center"><img src="https://github.com/Machine-Learning-Tokyo/ML_Fairness_Ethics_Explainability/blob/master/images/allennlp.png" width="600"></p>](https://allennlp.org/interpret)

## ELI5
ELI5 is a Python library which allows to visualize and debug various Machine Learning models using unified API. It has built-in support for several ML frameworks and provides a way to explain black-box models.

- Source: [ELI5 Documentation](https://eli5.readthedocs.io/en/latest/index.html)
- Tutorials: [Notebook](https://nbviewer.jupyter.org/github/danbochman/Open-Source-Spotlight/blob/master/ELI5/ELI5.ipynb)

[<p align="center"><img src="https://github.com/Machine-Learning-Tokyo/ML_Fairness_Ethics_Explainability/blob/master/images/eli.png" width="600"></p>](https://allennlp.org/interpret)

## ML Fairness Gym

Google released the ML Fairness Gym (2020), a set of components for building simple simulations that explore potential long-run impacts of deploying machine learning-based decision systems in social environments.

- "Fairness is not Static: Deeper Understanding of Long Term Fairness via Simulation Studies" [[Paper]](https://github.com/google/ml-fairness-gym/blob/master/papers/acm_fat_2020_fairness_is_not_static.pdf)
- [[ML Fairness GitHub repository]](https://github.com/google/ml-fairness-gym/)

[<p align="center"><img src="https://github.com/Machine-Learning-Tokyo/ML_Fairness_Ethics_Explainability/blob/master/images/fairness_gym.gif" width="600"></p>](https://ai.googleblog.com/2020/02/ml-fairness-gym-tool-for-exploring-long.html)
