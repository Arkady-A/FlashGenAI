import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
import logging
import coloredlogs


def setup_logger():
    """
    Set up the logger for the application.

    Returns:
        logger: A configured logging instance.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    coloredlogs.install(level='DEBUG', logger=logger, fmt=log_format)
    logger.addHandler(console_handler)
    return logger


def load_api_key():
    """
    Load the OpenAI API key from the .env file.

    Returns:
        str: The API key.

    Raises:
        Exception: If the API key is not found in the environment variables.
    """
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key is None:
        raise Exception("OPENAI_API_KEY environment variable is not set.")
    return api_key


def read_filelist(filelist_path='filelist.txt'):
    """
    Read the list of files to be processed from a specified file.

    Args:
        filelist_path (str, optional): Path to the file containing the list of files. Defaults to 'filelist.txt'.

    Returns:
        list: A list of file paths.
    """
    with open(filelist_path, 'r') as f:
        files = f.read()
    return [x.strip() for x in files.split('\\n')]


def process_files(files, client, logger, initial_prompt):
    """
    Process each file in the provided list, generating responses from OpenAI and saving them.

    Args:
        files (list): List of file paths to process.
        client (OpenAI): OpenAI client instance.
        logger (logging.Logger): Logger instance.
        initial_prompt (str): The initial prompt template for generating responses.
    """
    today_date = datetime.today().strftime("%d_%m_%Y")
    time_hms = datetime.now().strftime("%H%M%S")
    for i, file in enumerate(files):
        logger.debug(f"Working on file: {file}")
        with open(file, 'r') as f:
            file_content = f.read()

        user_prompt = initial_prompt.format(file_content)
        response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=[{"role": "system",
                                                             "content": "Only response with what user asks. Nothing else. Instructions ends after CONTENT:\""},
                                                            {"role": "user", "content": user_prompt}])
        logger.debug("Got response from OpenAI")

        save_path = f'./results/{today_date}/{time_hms}'
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        filename_save = os.path.join(save_path, os.path.split(file)[-1])
        with open(filename_save, 'w') as f:
            f.write(response.choices[0].message.content)
        logger.debug(f"Saved response to {filename_save}")
        logger.debug(f"{i + 1}/{len(files)} ({((i + 1) / len(files)) * 100}%)")


def main():
    """
    Main function to execute the script.
    """
    logger = setup_logger()
    api_key = load_api_key()
    client = OpenAI(api_key=api_key)
    files = read_filelist()
    initial_prompt = "INSTRUCTION: write anki questions based on the content of the note in the format Q: [QUESTION] (linebreak) A: [ANSWER] (2 linebreaks)\\n\\n CONTENT:\\n\"{}\""
    process_files(files, client, logger, initial_prompt)


if __name__ == "__main__":
    main()
