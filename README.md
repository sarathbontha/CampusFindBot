# CampusFind Bot

## Project Overview

CampusFind Bot is a traditional rule-based chatbot developed using Python and the Microsoft Bot Framework. The chatbot is designed to assist students with common lost-and-found questions on a university campus.

Unlike AI-powered chatbots, this chatbot uses predefined rules and keyword matching to respond to user requests. It does not use machine learning or large language models.

## Features

- Greets users
- Displays available services
- Helps report lost items
- Helps report found items
- Provides guidance for lost laptops, wallets, and ID cards
- Displays office hours
- Provides contact information
- Handles unsupported questions
- Ends the conversation politely

## Technologies

- Python 3.8
- Microsoft Bot Framework SDK
- Bot Framework Emulator
- Visual Studio Code
- Git and GitHub

## Project Structure

```
CampusFindBot/
│
├── app.py
├── bots/
├── config.py
├── requirements.txt
└── README.md
```

## How to Run

Activate the environment:

```bash
conda activate campusfind
```

Install packages:

```bash
pip install -r requirements.txt
```

Run the chatbot:

```bash
python app.py
```

Open Bot Framework Emulator and connect to:

```
http://localhost:3978/api/messages
```

## Future Improvements

- Add database support
- Store lost-item reports
- Generate tracking numbers
- Add Natural Language Processing
- Integrate AI services

## Author

Sarath Bontha

MSAI-631

University of the Cumberlands
