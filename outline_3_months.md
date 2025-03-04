## Further Exploration (3 Months of Time)
If given 3 months to improve the system, here are some possible next steps:

### Data Preprocessing & Clean-Up:
* _Message Parsing_: Clean and preprocess messages to remove punctuation, typos, or abbreviations. This will help improve the accuracy of model predictions.
* _Text Normalization_: Apply NLP preprocessing (stemming/lemmatization) to make sure queries are normalized. This will help the model retrieve the right results even if terms are worded slightly differently.
* _Fine-Tuning a Model_:
    * Fine-Tune GPT: Train a domain-specific model with the JuniorGPT transcripts to improve accuracy in generating search queries. This would allow the model to better understand the specific language used in investment research.
    * Entity Recognition: Train an entity recognition model that focuses specifically on investment-related entities (companies, stock tickers, market trends, etc.).
* _Performance Evaluation_:
    * A/B Testing: Test different versions of the search queries against a large set of transcripts. Measure performance based on metrics such as relevance and ranking accuracy of quotes.
* _User Feedback Integration_: Implement a feedback system where analysts and managers can rank the relevance of the search results. A Streamlit app could be an effective way to build a simple interactive UI for this and allow users to rate the results (Thumbs up/down, star rating, or dropdown selection).
* _Search Ranking Improvements_:
    * Search Ranking Optimization: Implement a ranking algorithm that ranks the search results based on their relevance to the semantic query. Potentially could use learned ranking models such as BERT to rank based on similarity scores.
### Possible Long-Term Improvements:
* _Multimodal Search_: Extend the search to support multimodal inputs, such as visual data or charts from investment reports, in addition to text.
* _Personalized Queries_: Build personalized search models that tailor search queries based on the user’s previous behavior or preferences.