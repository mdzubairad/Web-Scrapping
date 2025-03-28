# Web Scraping  Project

## 📌 Overview
This project provides a local HTML webpage and Python script for practicing web scraping techniques using Selenium. It includes various HTML elements commonly encountered in real-world scraping scenarios.
It is Scrapping the Product name and their price.

## 🛠️ Features
- **Webpage** with:
  - Product listings with prices, ratings, and stock status
  - Tables with customer reviews
  - Lists with weekly specials
  - Pagination elements
  - Hidden data attributes
- **Selenium script** demonstrating:
  - Automatic ChromeDriver management
  - Multiple element location strategies
  - Robust error handling
  - Local file loading

## ⚙️ Setup

### Prerequisites
- Python 3.8+
- Google Chrome installed
- Basic Python knowledge

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/web-scraping-practice.git
   cd web-scraping-practice
   ```

2. Install dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```

## 🚀 Usage

1. Run the scraping script:
   ```bash
   python main.py
   ```

2. The script will:
   - Automatically download the correct ChromeDriver
   - Load the local practice webpage
   - Extract and display product information
   - Clean up resources when done

## 🏗️ Project Structure
```
web-scraping-practice/
│
├── index.html          # Webpage HTML
├── main.py             # Main scraping script
├── README.md           # This file
└── chromedriver.exe    # (Auto-downloaded by script)
```

## 🎯 Learning Objectives
Practice scraping:
- Text content from various HTML elements
- Attributes and data properties
- Table data extraction
- Handling pagination
- Dealing with hidden elements
- Managing different selector strategies (XPath, CSS)

## 🛠️ Customizing
1. Edit `index.html` to add more complex scraping challenges
2. Modify `main.py` to:
   - Try different selector strategies
   - Extract different data elements
   - Implement more advanced scraping patterns

## 🤝 Contributing
Contributions welcome! Please:
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request



## ✉️ Contact
For questions or feedback, please open an issue on GitHub.

Happy Scraping! 🕷️