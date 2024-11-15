import streamlit as st

def faq():
    st.markdown(
        """
# FAQ
## What is Entropix?
Entropix is an open-source AI-powered search engine inspired by Perplexity AI. It leverages advanced machine learning algorithms to provide concise and accurate answers to user queries, ensuring transparency and user control over data. Entropix utilizes the [Llama-3.1-405B model](https://nebius.com/studio/inference?utm_medium=cpc&utm_source=chesscompetition&utm_campaign=Network_en_all_lgen_inference_cloud&utm_term=chesscompetition) from Nebius AI Studio, enhancing its language understanding capabilities.

## How does Entropix work?
Entropix utilizes large language models and real-time web data to understand and respond to user questions. By employing techniques like similarity searching and embeddings, it refines search results and delivers clear answers with cited sources. The integration of [Llama-3.1-405B](https://nebius.com/studio/inference?utm_medium=cpc&utm_source=chesscompetition&utm_campaign=Network_en_all_lgen_inference_cloud&utm_term=chesscompetition) from Nebius AI Studio allows Entropix to process complex queries more effectively.

## Is Entropix always accurate?
While Entropix aims to provide precise and relevant information, it may occasionally produce responses that lack accuracy or contextual relevance. As with any AI system, continuous updates and user feedback are essential to enhance its performance.

## Can I rely on Entropix for critical information?
Entropix is designed to assist users in finding information efficiently. However, for critical or sensitive matters, it's advisable to consult multiple sources or seek professional advice to ensure the accuracy and reliability of the information.
"""
    )
