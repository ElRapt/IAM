# "I am" : Twitter bot

## Introduction

This Twitter bot is designed to periodically tweet phrases that begin with "I am" followed by a word from a predefined dictionary. The bot is implemented in Python and uses the Tweepy library for interacting with the Twitter API. It leverages Python's `asyncio` library for efficient IO-bound operations and incorporates best practices like logging, error handling, and thread safety.

## Features

- **Asynchronous Operations**: Uses `asyncio` for non-blocking operations.
- **Thread-Safe Counter**: Utilizes `threading.Lock` for a thread-safe counter.
- **Robust Error Handling**: Gracefully handles errors and logs them for debugging.
- **Extensible**: Easy to extend for more complex functionalities.

## Prerequisites

- Python 3.7 or higher
- Tweepy library
- Twitter Developer Account and API credentials

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Create a Twitter Application on [Twitter's Developer Portal](https://developer.twitter.com/en)

2. Create a `credentials.json` with your Twitter API credentials.
  
3. Update the `dictionary.json` with the list of words you'd like to tweet.

4. Run the bot:
    ```bash
    python main.py
    ```

## Contributing

Feel free to fork the project, open a pull request, or submit suggestions and bugs as GitHub issues.

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
