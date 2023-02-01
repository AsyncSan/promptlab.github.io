---
date: 2023-02-01T20:43:21.965650Z
layout: post
title: Find mistakes in code
subtitle: A prompt to accelerate your webdevelopment
description: Prompt to help you with webdevelopment 
image: /assets/img/blogtitleimages/Findmistakesincode.webp
optimized_image: /assets/img/blogtitleimages/Findmistakesincode.webp
category: webdevelopment
tags:
  - Web Development
  - Javascript
  - chatprompts
  - workflow
author: rene
---

## Prompt

  <div class='promptinnerdivtop'>
    <div class='prompttextdiv'>
    <p>Help me find mistakes in the following code <paste code below>.</p>
    </div>
  </div>


## Example answer
  <div class='promptinnerdivbottom' >
    <div class='prompttextdiv'>
    <p>

<code>
int main()
{
    int x = 0;
    double y = 0.0;

    cout << x + y;
    return 0;
}
</code>

<ul>
  <li>No header file for <code>cout</code>, should include <code>#include &lt;iostream&gt;</code></li>
  <li>Missing semicolon after <code>cout << x + y</code></li>
  <li>Missing parentheses after <code>main</code></li>
</ul></p>
    </div>
  </div>
