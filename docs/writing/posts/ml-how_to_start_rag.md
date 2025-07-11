---
authors:
- fbetteo
categories:
- AI
- Machine Learning 
comments: true
date: 2025-07-10
description: Llama Index and RAG starter point
draft: false
slug: llama-index-and-rag-starter-point
tags:
- Machine Learning
---
# Llama Index and RAG starter point

This is me trying and playing a bit with the [starter guide](https://docs.llamaindex.ai/en/stable/getting_started/customization/#frequently-asked-questions-faq) of Llama Index. Basic discovery of how to use this. Actually their starter is more complex, goes into agents right away, so this was more what I was looking for.

## Creating the environment 
Poetry already installed and configured in windows to use Conda environments. Not sure how?[Look here](https://fbetteo.com/writing/2025/07/10/how-to-use-poetry-with-conda-environments/)

```bash
conda create --name rag python=3.12

conda activate rag
poetry init
poetry add llama-index
poetry add sentence-transformers
poetry add llama-index-embeddings-huggingface
```

llama-index uses by default embedding from OpenAI. It requires the API key (and paying of course.)
Should be cheap but I'll try using local embeddings to see how it goes, using Huggingface as I used for other projects via sentence-transformers.

For local embedding model, we load the model from hugging face and we update the embed_model in Settings.

```python 
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5",
    device="cpu",
    embed_batch_size=8,
)

Settings.embed_model = embed_model
```

I think this could work alright in terms of speed for now.
## Ollama
I installed Ollama from their website
Added Ollama to Environment Variables

```bash
ollama pull gemma3
ollama pull gemma3:4b
```

I've been using them in the llama_index_starter.py to avoid using any API.
but with my cpu only computer (32gb ram) everything was really slow.
gemma3 in the terminal was super slow (~30s) , gemma3:4b much faster (~2s) but when integrating into llama index with the retrieval, it was slow too

I feel like there is no usage for local LLMs in my current computer. Maybe if I use a server or collab this could work.

## Groq
I found that they have a generous free tier (500k tokens per day for some models) that should be enough to test things and do some minimum POC. I can top up later or use another provider, that's the magic of Llama-index, it should be easy to change the provider.

Also, Groq onboarding couldn't be easier. Log in, they give you API key, and that's it.


`poetry add llama-index-llms-groq`

```python
from llama_index.llms.groq import Groq
Settings.llm = Groq(model="llama-3.1-8b-instant",
                api_key=GROQ_API_KEY,
                request_timeout=360.0)
```

That's it, I'm using Groq. In the [Dashboard](https://console.groq.com/dashboard/metrics) we can see usage, logs, etc, super cool.