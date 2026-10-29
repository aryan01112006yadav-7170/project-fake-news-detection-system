# 📰 Fake News Generator and Detector using GenAI & NLP

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aryan01112006yadav-7170/project-fake-news-detection-system/blob/main/Fake_News_Generator_and_Detector_Colab.ipynb)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange.svg)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)
![Gradio](https://img.shields.io/badge/Gradio-Web%20UI-ff5252.svg)

> **Industrial Training Report Project (BCS752) — Academic Session 2026-2027**  
> **Student:** ARYAN (Roll No: **2300640100026**)  
> **Department:** Department of Computer Science & Engineering  
> **College:** Hindustan College of Science & Technology (HCST), Farah, Mathura  
> **Training Organization:** IBM Developer Skills Network (*PBELGEN221IN / IBM & NASSCOM*)  
> **Course Incharge:** Mr. Diwakar Shrivastava | **HOD CSE:** Dr. Shankar Thawkar  

---

## 🚀 Live Showcase: Run Directly in Google Colab

Click the badge above or use the link below to launch the complete working project in **Google Colab** with free GPU acceleration:

👉 **[Launch in Google Colab](https://colab.research.google.com/github/aryan01112006yadav-7170/project-fake-news-detection-system/blob/main/Fake_News_Generator_and_Detector_Colab.ipynb)**

### ✨ One-Click Execution in Colab:
1. Open the notebook in Google Colab.
2. In the top menu, go to **Runtime** ➔ **Change runtime type** ➔ select **T4 GPU** (optional, runs on CPU too).
3. Click **Runtime** ➔ **Run all** (or press `Ctrl + F9`).
4. Scroll down to the final cell: an interactive **Gradio Web Interface** will launch directly inside Colab, along with a shareable public link (`https://xxxx.gradio.live`) to open in full screen on any phone, tablet, or faculty screen!

---

## 🎯 Project Overview & Objectives

In today's digital media landscape, synthetic disinformation spreads rapidly across social networks. This project investigates the **dual role of Artificial Intelligence** in digital information integrity:

1. **Generative AI (Creation Module):** Leverages **GPT-2** with structured **Prompt Engineering** to synthesize contextually coherent, realistic fake news articles based on user-defined parameters (*Keywords, Theme/Angle, and Tone: Alarmist, Clickbait, Biased, Sensational*).
2. **Transformer Classification (Defense Module):** Employs **BERT (Bidirectional Encoder Representations from Transformers)** to analyze input news articles, classify veracity (**REAL** vs. **FAKE**), provide a calibrated confidence score, and generate **Explainable AI (XAI)** linguistic justifications.
3. **Interactive Gradio Application:** A unified dual-tab web application matching **Figure 3.7** of the project report for live classroom and faculty demonstration.

---

## 🏗️ System Architecture

```
                  +-----------------------------------------+
                  |           User Input Interface          |
                  +-----------------------------------------+
                               /                   \
        [Generator Path]      /                     \     [Detector Path]
                             v                       v
               +---------------------------+   +---------------------------+
               |    Prompt Engineering     |   |    Text Preprocessing     |
               | (Topic, Tone, Angle, Temp)|   | (Tokenization, Attention) |
               +---------------------------+   +---------------------------+
                             |                               |
                             v                               v
               +---------------------------+   +---------------------------+
               |  Generative AI Model      |   |  Discriminative Model     |
               |   (Hugging Face GPT-2)    |   |     (BERT Classifier)     |
               +---------------------------+   +---------------------------+
                             |                               |
                             v                               v
               +---------------------------+   +---------------------------+
               | Synthetic Fake Article    |   |  Veracity Score & Verdict |
               | - Sensational Headline    |   |  - REAL vs FAKE           |
               | - Fabricated Body Text    |   |  - Confidence Percentage  |
               | - Plausible Source Tip    |   |  - Explainable Justification
               | - Deceptive Image Prompt  |   |    (Linguistic Cues & XAI)|
               +---------------------------+   +---------------------------+
                             \                       /
                              \                     /
                               v                   v
                  +-----------------------------------------+
                  |    Dual-Tab Gradio Web Demonstration    |
                  |     (Matches Report Figure 3.7)         |
                  +-----------------------------------------+
```

---

## 📸 Report Implementation Verification (Figures 3.1 - 3.7)

This project strictly reproduces all implementation stages described in **Chapter 3** of the submitted report:

| Report Reference | Description | Code / Module Implementation |
|---|---|---|
| **Figure 3.1** | Install Libraries | `transformers`, `gradio`, `datasets`, `torch`, `accelerate`, `scikit-learn` |
| **Figure 3.2** | Uploading Datasets | Automated loader for `Fake.csv` & `True.csv` (ISOT benchmark) |
| **Figure 3.3** | Dataset Cleaning & Splitting | 80/20 stratified `train_test_split` |
| **Figure 3.4** | BERT Tokenization | `bert-base-uncased` tokenizer with PyTorch `NewsDataset` |
| **Figure 3.5** | Model Training | Hugging Face `Trainer` & `TrainingArguments` |
| **Figure 3.6** | Evaluation Metrics & GPT-2 | Accuracy, Precision, Recall, F1 score logging & GPT-2 setup |
| **Figure 3.7** | Gradio Output UI | Dual-tab interface (`Generate Fake News` & `Detect News`) |

---

## 💻 Local Installation & Execution (Optional Offline Mode)

If you wish to run the project locally on your machine rather than in Google Colab:

```bash
# 1. Clone the repository
git clone https://github.com/aryan01112006yadav-7170/project-fake-news-detection-system.git
cd project-fake-news-detection-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Gradio Web App
python app.py
```

The web application will launch at `http://127.0.0.1:7860` and display a public `gradio.live` link in the terminal.

---

## 🧪 Live Faculty Demonstration Test Cases

During your 10-minute presentation, you can copy-paste these exact samples to demonstrate real-time classification:

### Sample 1: Authentic Real News (Reuters Wire)
> `WASHINGTON (Reuters) - The U.S. Senate Judiciary Committee on Thursday approved several federal judicial nominations following hours of debate over constitutional interpretations and bipartisan procedures. Committee leadership confirmed the votes will proceed to the full Senate floor for final confirmation next week.`
> 
> **Expected Verdict:** `✅ REAL / VERIFIED NEWS` (Confidence: 96%+)  
> **Justification:** Neutral journalistic register, standard news agency attribution `(Reuters) -`, absence of sensational hyperbole.

### Sample 2: Fabricated Fake News (Conspiracy Clickbait)
> `SHOCKING: Secret Government Documents Expose Cover-up of Miraculous Energy Device! Unbelievable leaked documents from unnamed deep-state insiders prove that a miraculous zero-point energy generator was suppressed by globalist oligarchs! The mainstream media refuses to broadcast this undeniable truth! Share this before it gets deleted!`
> 
> **Expected Verdict:** `⚠️ FAKE NEWS DETECTED` (Confidence: 97%+)  
> **Justification:** Tabloid sensationalism, emotive trigger words (*SHOCKING, cover-up, deep-state, suppressed*), excessive exclamation marks, lack of verifiable wire source.

### Sample 3: Project Report Benchmark Sample (Figure 3.7)
> `bomb blast at the headquarters of the Russian-backed government in Chechnya. The U.S. and its allies have failed to ensure that the Russians are not behind this attack. A U.S. official said the Russian military had not been involved in the attack and that Russia would not provide further details...`
> 
> **Expected Verdict:** Directly loads via the pre-set in Tab 2 matching Figure 3.7.

---

## 🎓 Faculty Viva / Q&A Preparation Cheat Sheet

Here are the most common questions faculty (e.g., Dr. Shankar Thawkar & Mr. Diwakar Shrivastava) ask during BCS752 presentations, along with concise, technically rigorous answers:

<details>
<summary><b>Q1: Why did you use both GPT-2 and BERT in this project?</b></summary>
<b>Answer:</b> "Sir, this project demonstrates the dual dynamic of AI in misinformation. GPT-2 is an autoregressive decoder-only Large Language Model optimized for natural language generation, which we use to generate synthetic fake news for controlled research. BERT is a bidirectional encoder-only transformer optimized for natural language understanding and contextual classification, which we fine-tune to detect and verify news veracity."
</details>

<details>
<summary><b>Q2: What dataset did you use and what was its structure?</b></summary>
<b>Answer:</b> "We used the ISOT Fake and Real News dataset consisting of real articles collected from Reuters and fabricated articles gathered from verified misinformation websites. The data is preprocessed into two columns: the text content and binary labels (0 for Fake, 1 for Real)."
</details>

<details>
<summary><b>Q3: How does your system explain WHY an article is classified as fake (Explainable AI)?</b></summary>
<b>Answer:</b> "In addition to the raw softmax probability logits from BERT, our system incorporates linguistic feature extraction that analyzes stylistic cues such as emotive superlatives, clickbait punctuation, all-caps emphasis, and verified journalistic wire headers (e.g. Reuters / AP). It outputs a clear bulleted justification alongside the verdict."
</details>

<details>
<summary><b>Q4: What hyperparameters did you use for training BERT?</b></summary>
<b>Answer:</b> "We trained using the AdamW optimizer with a learning rate of 2e-5, weight decay of 0.01, sequence length of 256 tokens, and evaluated using cross-entropy loss along with Accuracy, Precision, Recall, and F1-score."
</details>

---

## 👥 Acknowledgements

- **IBM Developer Skills Network & NASSCOM** for providing the *Generative AI Virtual Internship (PBELGEN221IN)* framework.
- **Dr. Shankar Thawkar** (Head of Department, CSE) and **Mr. Diwakar Shrivastava** (Course Incharge) at **Hindustan College of Science and Technology (HCST)** for guidance and academic supervision.

---
*Created by Aryan (2300640100026) | HCST Mathura | 2026-2027*
