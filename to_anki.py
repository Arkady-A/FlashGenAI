import os
import genanki
import re

def parse_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    qa_pairs = re.findall(r'Q: (.*?)\nA: (.*?)\n', content, re.DOTALL)
    return qa_pairs

def add_qa_pairs_to_deck(deck, qa_pairs):
    model = genanki.Model(
        1607392319,
        'Simple Model',
        fields=[{'name': 'Question'}, {'name': 'Answer'}],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])
    for question, answer in qa_pairs:
        note = genanki.Note(
            model=model,
            fields=[question, answer]
        )
        deck.add_note(note)

def create_anki_package(deck, output_path):
    package = genanki.Package(deck)
    package.write_to_file(output_path)

def main():
    results_dir = 'results'
    date = "03_12_2023" # ADJUST
    time = '224351' # ADJUST
    dir = os.path.join(results_dir, date, time)

    deck_name = "REPLACE_ME"  # ADJUST  Name for the combined deck
    deck_id = abs(hash(deck_name)) % (10 ** 10)  # Unique deck ID
    combined_deck = genanki.Deck(deck_id, deck_name)

    for file in os.listdir(dir):
        if file.endswith('.md'):
            file_path = os.path.join(dir, file)
            qa_pairs = parse_markdown_file(file_path)
            add_qa_pairs_to_deck(combined_deck, qa_pairs)

    output_path = os.path.join(dir, deck_name + '.apkg')
    create_anki_package(combined_deck, output_path)
    print(f'Created Anki package: {deck_name}')

if __name__ == "__main__":
    main()
