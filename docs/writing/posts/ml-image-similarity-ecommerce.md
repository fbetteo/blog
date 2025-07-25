---
authors:
- fbetteo
categories:
- AI
- Machine Learning 
comments: true
date: 2025-02-21
description: E-commerce Image Similarity via Visual Embeddings
draft: false
slug: image-similarity-ecommerce
tags:
- Machine Learning
---
# E-commerce Image Similarity via Visual Embeddings

How I implemented an API to retrieve similar images from an E-commerce in 3 steps

In this post, we explore a system to identify similar articles solely based on e-commerce images. The approach is designed with two primary objectives in mind:

Do you want to see how it looks? Check [my portfolio example](https://huggingface.co/spaces/fbetteo/fashion_similarity)!

## Objectives

1. **Catalog Similarity:**  
	Determine which items in the client's catalog resemble each other using only their photos.

2. **External Querying:**  
    Although not implemented in the current API, the plan is to eventually allow querying with external images. The envisioned workflow is to source images from suppliers, compare them with the client's catalog, and perform this embedding generation locally to keep the API lightweight.


## Proposed Solution

The core idea is to use a pretrained image model to extract embeddings from each photo. Once these embeddings are available, we can perform similarity searches to find items that are visually alike.

For our implementation, we experimented with both OpenAI's **clip-ViT-B-32** and **ResNet**. In general, both models produced comparable results, though we opted for CLIP in our main experiments.

## Implementation Steps

### Step 1: Download Catalog Images

- **Script:** `embeddings/download_images/get_images.py`
- **Details:**  
    This script downloads all catalog images from the e-commerce using a `ThreadPool` to speed up the process.

### Step 2: Generate and Index Embeddings

- **Script:** `embeddings/clip_faiss.py`
- **Details:**  
    The script generates embeddings for each photo and stores them in a Faiss index, which is saved under `embeddings/faiss_index/`.  
    **Note:** Since the process is deterministic, a simple overwrite will not impact the results. Idempotent as they call it.

Additional notebooks are available to illustrate the process, check results, and experiment with alternative models and tests.

### Step 3: Query the Faiss Index

- **API Functionality:**  
    The Faiss index is already built. We expose an API endpoint where you can pass an `article_id` (used during the embedding generation) and retrieve the most similar items.  
    **Validation:**  
    As a sanity check, querying an article should return itself as the top match with a distance of 0.

## Conclusion

By leveraging pretrained image models and efficient similarity search with Faiss, this approach provides a scalable method for identifying visually similar items in an e-commerce catalog. This system not only improves internal catalog management but also sets the groundwork for integrating external image queries in the future.