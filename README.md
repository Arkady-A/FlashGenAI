
# From MD to Brain by Anki

This project integrates OpenAI's GPT-3 model for generating Anki flashcards from provided text files.

Please, **read usage section**

## Getting Started

### 1. Obtaining an OpenAI Access Token

To use OpenAI's API, you need to obtain an API key. Follow these steps:

- Visit [OpenAI API](https://beta.openai.com/signup/).
- Sign up or log in to create an API key.
- Once logged in, navigate to the API section to find your API key.

### 2. Defining the API Key in .env File

After obtaining your API key, you need to store it in an environment file:

- Create a file named `.env` in your project's root directory.
- Add the following line to the file:
  
  ```
  OPENAI_API_KEY=Your_API_Key
  ```

Replace `Your_API_Key` with the key you obtained from OpenAI.

### 3. Filelist.txt

The `filelist.txt` should contain the paths to the markdown files you want to process, listed one per line. For example:

```
/home/[full_path_to_md]/LSTM models.md
/home/[full_path_to_md]/Azure fundamentals.md
```

### 4. Manual Adjustments in Code

You may need to make manual adjustments in the following files:

- `main.py`: Modify the `initial_prompt` or any other logic as per your requirement.
- `to_anki.py`: Adjust the Anki card model or format in the `add_qa_pairs_to_deck` function as needed.

## Project Structure

The root directory of the project contains:

- `results/`: Directory where results are stored
- `.env`: Environment variable file
- `.gitignore`: Git ignore file
- `filelist.txt`: List of files to be processed
- `main.py`: Main script for processing files
- `pyvenv.cfg`: Python virtual environment configuration
- `requirements.txt`: List of Python dependencies
- `to_anki.py`: Script for creating Anki cards

## Installation

Install the required dependencies by running:

```
pip install -r requirements.txt
```

## Usage

Run the main script to start processing files:

```
python main.py
```

**Adjust parameters** marked "ADJUST" in `to_anki.py`
## Contributing

Contributions are welcome. Please fork the repository and submit a pull request for any enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
