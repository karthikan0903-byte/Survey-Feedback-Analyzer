# Survey Feedback Analyzer

## Project Overview
This Python-based analysis tool processes customer support tickets by standardizing issue descriptions, evaluating keyword occurrences, performing priority distribution analysis, and extracting key text analytics.

## Features
- **Data Ingestion**: Processes baseline support data and accepts dynamic user inputs with priority validation.
- **Text Cleaning Pipeline**: Converts strings to lowercase, removes punctuation, normalizes spacing, and maps shorthand text (e.g., "ok" -> "okay").
- **Keyword Analyzer**: Function `count_tickets_with_word()` performs targeted keyword metrics extraction.
- **Dataset Metrics**: Identifies the longest feedback description, measures unique vocabulary metrics, and computes priority breakdowns.

## Repository Contents
- `Main.py`: Full executable Python solution script.
- `Summary_Report.pdf`: One-page executive summary document covering key operational insights.
- `README.md`: System documentation and setup details.

## Run Instructions
Run the main script using Python 3:
```bash
python Main.py
