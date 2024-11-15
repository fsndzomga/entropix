import streamlit as st


def overview(search_results: list[dict]) -> None:
    # Extract the 'news_results' field from the SerpApi results
    news_items = []
    for result in search_results:
        if "news_results" in result:
            news_items.extend(result["news_results"])

    # Display the top 4 news links in columns
    st.markdown("## Relevant News")
    columns = st.columns(4)  # Create 4 columns for displaying the news items

    # Loop through the first 4 news items and display each in a column
    for i, news in enumerate(news_items[:4]):
        with columns[i]:
            # Display the image (thumbnail preview) if available
            if "thumbnail" in news:
                st.image(news["thumbnail"], use_container_width=True)
            # Display the title as a clickable link
            st.markdown(f" **[{news['title']}]**({news['link']})")
            # Display the source if available
            source_name = news.get("source", {}).get("name", "Unknown Source")
            st.write(f"Source: {source_name}")

            # Optional date information
            if "date" in news:
                st.write(f"Date: {news['date']}")
