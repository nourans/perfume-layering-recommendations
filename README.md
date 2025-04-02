# Perfume Layering Recommendation System

Perfume lovers know the joys of perfume layering: it creates different concoctions of scents and emphasize certain notes in perfumes you already own, making your perfume collection virtually infinite!

As a fragrance lover myself, this is a passion project, where I help users discover beautiful perfume combinations and analyze their scent preferences. Users input perfumes they own, and the system uses GPT-4o to suggest creative layering ideas and uncover trends in their taste—turning their collection into an aromatic mood board. Have fun transforming your perfume game!


---

## 🚀 Features

- ✅ Add, view, and manage your personal perfume collection via a terminal interface
- 🔮 GPT-powered scent layering recommendations
- 🔍 Analysis of your most common scent notes and pairings
- 🔄 Local storage of perfumes in a JSON file
- 🚀 Modular design for easy scaling to a web or mobile app

---

## 📂 Project Structure

```
src/
├── app.py            # Main CLI menu
├── gpt_notes.py      # GPT-4o interaction logic
├── split.py          # Splits GPT response into recs & analysis
├── utils.py          # Handles loading and saving perfumes
├── data/
│   └── perfume_input.json  # Locally stored perfume list
```

---

## 🧠 How It Works

1. Run the CLI program from your terminal
2. Add perfumes you own (brand + name)
3. Select one of two GPT-powered options:
   - **Get recommendations** for perfume layering
   - **Analyze** your collection to discover your scent profile
4. GPT-4o processes your collection and returns:
   - Suggested layering combinations with reasoning
   - Most common notes and note combinations in your perfumes

---

## 🌳 Getting Started

### Requirements
- Python 3.9+
- OpenAI SDK: `pip install openai python-dotenv`

### Setup
```bash
git clone https://github.com/nouransakr/perfume-layering-guru.git
cd perfume-layering-guru

# Create a .env file with your OpenAI API key
echo "OPENAI_API_KEY=your-api-key-here" > .env

python src/app.py
```

---

## 🌟 Sample Output

```
️ Layering Combos for Your Collection ️

1. Zara Rose Gourmand + Lattafa Mazaaji
   - Order: Rose Gourmand, then Mazaaji
   - Reason: Floral meets rich gourmand for an elegant sweetness

2. Gucci Flora + Kenzo Flower
   - Order: Flora, then Flower
   - Reason: Powdery softness meets vibrant petals

️ Here is what you like ️

Top 5 notes:
1. Floral
2. Musky
3. Woody
4. Sweet
5. Citrus

Most common note combos:
- Floral + Woody
- Citrus + Floral
- Sweet + Musky
```

---

## 🚡 Future Ideas

- 📈 Visualize your scent profile using bar graphs or radar charts
- 🌟 Build a recommendation engine for new perfume purchases
- 🚀 Launch a Streamlit-powered web app
- ✨ Add mood-based suggestions (e.g. "Date night", "Power scent")

---

## 👩‍💼 Author

Crafted with fragrance geekery & code by [Nouran S](https://github.com/nourans)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

