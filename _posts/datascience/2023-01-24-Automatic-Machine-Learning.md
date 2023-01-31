---
date: 2023-01-31T19:36:35.969875Z
layout: post
title: Automatic Machine Learning
subtitle: Generate Python code to solve a certain task
description: Generate Python code to solve a certain task
image: /assets/img/blogtitleimages/AutomaticMachineLearning.webp
optimized_image: /assets/img/blogtitleimages/AutomaticMachineLearning.webp
category: datascience
tags:
  - datascience
  - python
  - chatprompts
  - workflow
  - machine learning
author: rene
---

## Prompt

  <div class='promptinnerdivtop'>
    <div class='prompttextdiv'>
    <p>I want you to act as an automatic machine learning (AutoML) bot using TPOT for me. I am working on a model that predicts [...]. Please write python code to find the best classification model with the highest AUC score on the test set.</p>
    </div>
  </div>


## Example answer
  <div class='promptinnerdivbottom' >

  </div>
  
    from tpot import TPOTClassifier
    import pandas as pd
    from sklearn.model_selection import train_test_split
    # load data and split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=0.25)
    tpot = TPOTClassifier(verbosity=2, scoring='roc_auc', random_state=42)
    tpot.fit(X_train, y_train)
    print("Best AUC score on the test set: %f" % tpot.score(X_test, y_test))