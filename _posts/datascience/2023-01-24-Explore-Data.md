---
date: 2023-01-31T19:38:22.697568Z
layout: post
title: Explore Data
subtitle: A prompt to accelerate your datascience
description: Prompt to help you with datascience 
image: /assets/img/blogtitleimages/ExploreData.webp
optimized_image: /assets/img/blogtitleimages/ExploreData.webp
category: datascience
tags:
  - datascience
  - python
  - chatprompts
  - workflow
  - explore
author: rene
---

## Prompt

  <div class='promptinnerdivtop'>
    <div class='prompttextdiv'>
    <p>I want you to act as a data scientist and code for me. I have a dataset of [describe dataset]. Please write code for data visualisation and exploration.</p>
    </div>
  </div>


## Example answer
  <div class='promptinnerdivbottom' >
    <div class='prompttextdiv'>
    <p>

<ol>
  <li>Import the necessary libraries (e.g. pandas, matplotlib, seaborn, etc.)</li>
  <pre><code>
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns</code></pre>
  
  <li>Read the data into a dataframe</li>
  <pre><code>
df = pd.read_csv('[file path]')</code></pre>
  
  <li>Explore the data using head(), info() and describe() methods</li>
  <pre><code>
df.head()  # to view first 5 rows of the dataframe
df.info()  # to get information about the dataframe columns
df.describe()  # to view summary statistics of numerical columns</code></pre>

  <li>Plot histograms for each column in your dataframe to visualise the distribution of values within each column</li>
  <pre><code>
df.hist(figsize=(20,15))
plt.show()</code></pre>

  <li>Use Seaborn library to create countplots for categorical variables in the dataset.</li>
  <pre><code>
for col in df.columns:   # loop through</p>
    </div>
  </div>
