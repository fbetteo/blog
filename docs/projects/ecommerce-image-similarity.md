---
title: Ecommerce Image Similarity Project
description: How Franco Betteo built a visual product similarity system for an ecommerce catalog using image embeddings, FAISS, and an API.
---

# Ecommerce product similarity from catalog images

## The problem

A retailer needed a way to find related products within a catalog using product photos. A useful result would help staff locate alternatives when responding to customers and could support other product discovery workflows.

## My role and approach

I built the image retrieval pipeline and API. The implementation had three parts:

1. Collect the catalog images.
2. Generate visual embeddings and index them with FAISS. I compared CLIP and ResNet representations during development.
3. Expose an API that takes an article ID and returns similar catalog items.

The [technical article](../writing/posts/ml-image-similarity-ecommerce.md) describes the implementation in more detail. A [portfolio demo](https://huggingface.co/spaces/fbetteo/fashion_similarity) lets you explore a related example; it is not the client's system or data.

## What this demonstrates

The system made it possible to retrieve visually similar catalog items through an API. The project was used to help customer support find alternatives for customers. I have not published measured effects on sales, response time, or retrieval quality, so those should not be inferred from this example.

The planned ability to search with new supplier images was outside the initial API scope.

## Could this apply to your catalog?

The first step would be to define what “similar” means for your customers and staff, then test retrieval quality on representative products. We would also check image coverage, catalog updates, integration needs, and whether the results improve a real workflow.

[Discuss a product discovery project](https://calendar.google.com/calendar/appointments/schedules/AcZssZ0JQSYOeX4y5slQlDYH66ugJq05Yx9Mj2gwfAOam5kfXNTRJZIZZUuJoHT-BsbKS-HgIM7M67ij?gv=true){ .md-button .md-button--primary } [See consulting services](../services.md){ .md-button }
