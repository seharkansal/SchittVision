This project brings Schitt’s Creek characters to life through an emotionally adaptive chatbot, capable of detecting user emotions and responding in character-specific styles. Leveraging the power of PyTorch and NLP techniques, this chatbot combines BERT for nuanced emotion detection and GPT-3 for generating tailored responses. As users interact, the chatbot adapts its tone and dialogue, delivering responses true to beloved Schitt’s Creek personalities like Moira, David, and Alexis. With a robust pipeline of data pre-processing, sentiment analysis, and response generation, this project blends machine learning with a touch of humor and drama.
Perfect — here's a **comprehensive, beginner-friendly summary** of your data collection phase for both:

---

# 📥 Data Collection – *Schitt's Creek Dialogue Dataset*

## 📌 Overview

This phase focused on **collecting episode transcripts** from publicly available sources to build a clean dataset of **character-wise dialogue lines** from the TV show *Schitt’s Creek*. The primary source was [ForeverDreaming.org](https://transcripts.foreverdreaming.org), a forum that hosts fan-transcribed scripts of various shows.

---

## 🔧 Tools & Libraries Used

* `requests` – to send HTTP requests and fetch web page content.
* `BeautifulSoup` – to parse HTML and extract structured text data.
* `csv` – to save the extracted dialogues in a structured format for future processing and training.

---

## 🌐 Data Source

We used URLs of all episodes across the show's six seasons from:

```
https://transcripts.foreverdreaming.org/
```

Each URL corresponds to a specific episode thread containing HTML-based script text.

---

## 🧠 Scraping Strategy

### ✅ Step-by-Step Breakdown:

1. **Loop Through URLs**
   Each episode transcript URL was loaded one by one using the `requests` library.

2. **Parse HTML with BeautifulSoup**
   The page content was parsed using `html.parser` to extract speaker names and dialogues.

3. **Identify Character Names**

   * Speaker names were found inside `<strong class="text-strong">` tags.
   * When such a tag appeared, the current speaker was updated.

4. **Capture Dialogues**

   * Dialogue lines were located using `<br>` tags.
   * If the text before a `<br>` was plain text, it was treated as part of the speaker’s current dialogue.

5. **Store Speaker–Line Pairs**

   * For each episode, all `(character, dialogue)` pairs were collected in a list.
   * After processing all episodes, these were compiled into a single list covering the entire show.

6. **Save as CSV**
   The final structured dataset was saved in:

   ```
   schitts_creek_combined_dialogues.csv
   ```

   With columns:

   * `Character`
   * `Dialogue`

---

## 🧹 Data Format

Sample output (CSV):

```
Character,Dialogue
David,You're embarrassing me.
Moira,Well I’m sorry for trying to elevate the conversation!
Johnny,Let’s keep it down, kids.
```

---

## ⚠️ Error Handling

If any page failed to load (e.g. due to a 404 error), the script printed a clear error message and continued scraping the remaining episodes.

---

## 💡 Key Challenges & Solutions

| Challenge                     | Solution                                                                                                                |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Inconsistent HTML formatting  | Focused only on specific tags (`<strong>`, `<br>`) and checked data types using `isinstance()` to avoid parsing errors. |
| Speaker switching mid-episode | Buffered lines under the current speaker and flushed them when a new speaker tag was found.                             |
| Potential data loss           | Final buffer (`current_dialogue`) was saved after finishing tag traversal to ensure no dialogue lines were skipped.     |

---

## ✅ Final Output

A structured, episode-spanning dataset of Schitt’s Creek character dialogues.

🧠 Why Create Input–Target Pairs?
Input–target pairs are created because most NLP tasks are framed as prediction problems — we want the model to predict something (target) given some text (input).

📌 My project Context (Schitt’s Creek Dialogue)
I collected and cleaned dialogues. Now what?

To use them in machine learning or deep learning models (e.g., for chatbots, character recognition, emotion tagging, etc.), I needed to transform the raw text into a supervised learning format — typically:
Input:  [some text]
Target: [some label or expected output]
📊 Example Tasks & Why You Need Input–Target Pairs
1. 💬 Chatbot / Dialogue Generation (next-line prediction)
Goal: Given a character’s line, predict what the next character might say.

Input	Target
David: You're embarrassing me.	Alexis: Can you just step outside?

This helps train a seq2seq model or transformer decoder.

Emotion Detection Labeling in Dialogue Dataset
After generating the input-target dialogue pairs from the cleaned transcript dataset, the next key step was to enrich the data by attaching emotion labels. These emotion labels provide additional context to each dialogue line, helping the model understand not just what is said but how it is said, which is essential for tasks like emotionally aware conversational AI or sentiment-sensitive text generation.

Overview of the Process
Emotion Detection on Dialogue Lines
Each dialogue line—both inputs and targets—was analyzed using an emotion detection method:

Using BERT pre-trained emotion classification models 

Assigning one or more emotion categories such as joy, anger, sadness, fear, surprise, and neutral to each dialogue.

Attaching Emotion Labels
The detected emotion(s) were appended or associated with each dialogue in the input-target pairs dataset. This are embedded within the input text as special tokens to signal emotional tone to downstream models

Benefits of Emotion Labeling

Richer training data: Emotion labels provide a semantic layer beyond plain text, which improves the model's ability to generate contextually appropriate and emotionally consistent responses.

Improved conversational AI: Models trained on emotion-enriched data can better capture the nuance and emotional dynamics of dialogues.

Analytical insights: Emotion labels allow for analysis of emotional trends in the dialogue, helpful for further research or application development.

Dataset Format After Labeling
The final dataset format included, for each dialogue pair:

Input dialogue text (possibly concatenated context)

Target dialogue text

Emotion label(s) for input and target dialogues


