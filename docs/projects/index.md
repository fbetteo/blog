---
title: AI and Machine Learning Projects
description: Selected AI, machine learning, and software projects by Franco Betteo, with details on the problem, implementation, and evidence.
---

# Selected projects

Much of my client work is private. The examples below describe the problem and approach without exposing client data, code, or unverified results. A public demo is available for some projects, but it is not a requirement for the work to be relevant to your team.

## Selected private client work

### Demand forecasting

I have built models to predict future demand using gradient-boosted trees, including LightGBM. The business question is how to turn a forecast into a better planning decision. A useful engagement defines the forecast horizon, a simple baseline, the cost of errors, and how the forecast will be used before choosing a model. 
Working properly with features, creating relevant ones and knowing best practices (with sources backing up) is where the distinctive value comes from, aka: experience. 
Good evaluations in testing ensuring no form of leakage is present is also important. That's not big news, but you would be surprised how common it is and then reality doesn't match your expected values.

### Decisions under constraints

I have used linear optimization with PuLP to generate optimal assormtnet allocations across stores. The useful output is a feasible recommendation and a clear explanation of which constraints drive it. The right formulation depends on the decisions, tradeoffs, and data available to the team. For instance, we had first a demand forecast model to predict future sales and that was an input for the allocation. Simpler alternatives can be done too.

### Pricing and segmentation

I have worked on price elasticity analysis and clustering with methods including k-means and DBSCAN. Pricing work needs careful attention to what the data can support; segments should be judged by whether they help people make different decisions, not only by a clustering score.

### Ecommerce image similarity

A catalog search system that retrieves visually similar products using image embeddings, FAISS, and an API. The client implementation is private; the linked demo is a portfolio example of the approach.

[Read the project](ecommerce-image-similarity.md) · [Read the technical article](../writing/posts/ml-image-similarity-ecommerce.md) · [Try the demo](https://huggingface.co/spaces/fbetteo/fashion_similarity)

## Public products and analysis

### Download YouTube Transcripts

A product I build and operate for extracting available transcripts from individual YouTube videos, channels, and playlists. It supports bulk jobs and programmatic access through an API. This is a public product you can inspect directly.

[Visit Download YouTube Transcripts](https://www.downloadyoutubetranscripts.com/)

- [Sportsjobs Online](https://sportsjobs.online): a job board for sports analytics and data roles that I build and operate.
- [NBA salaries model](../nba_salaries/index.html): an interactive legacy modeling project.

If one of these resembles a problem your team has, [see how we can work together](../services.md) or [email me](mailto:francobetteo@gmail.com).
