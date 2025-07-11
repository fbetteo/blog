---
authors:
- fbetteo
categories:
- AI
- Machine Learning 
comments: true
date: 2025-07-10
description: How to use Poetry with Conda environments
draft: false
slug: how-to-use-poetry-with-conda-environments
tags:
- Machine Learning
---

# How to use Poetry with Conda environments

Poetry uses by default the system installed python and creates a new environment using that one. I prefer creating a new env with conda, install whatever python version I want and work in there.

1) Create an environment with Conda and activate it

2) Have setup (once, globally) that Poetry uses the current environment python version
```bash
poetry config virtualenvs.create false
```