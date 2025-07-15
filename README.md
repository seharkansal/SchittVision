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


