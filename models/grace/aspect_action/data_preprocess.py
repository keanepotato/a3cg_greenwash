import json
import spacy
import os

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def tokenize(sentence):
    return [token.text for token in nlp(sentence)]

def find_positions(tokens, aspect):
    aspect_tokens = tokenize(aspect)
    positions = []
    for i in range(len(tokens) - len(aspect_tokens) + 1):
        if tokens[i:i + len(aspect_tokens)] == aspect_tokens:
            positions.append((i, i + len(aspect_tokens) - 1))
    return positions

def generate_bio_tags(tokens, aspects):
    bio_tags = ['O'] * len(tokens)
    action_labels = ['O'] * len(tokens)
    collapsed_labels = ['O'] * len(tokens)
    
    for aspect, actions in aspects.items():
        # if there is no aspect, skip 
        # the iteration and we should just
        # have all 'O' tags
        if aspect == 'no aspect':
            break
        for action in actions:
            positions = find_positions(tokens, aspect)
            for start, end in positions:
                bio_tags[start] = 'B_AP'
                action_labels[start] = action
                collapsed_labels[start] = f'B_AP+{action}'
                for i in range(start + 1, end + 1):
                    bio_tags[i] = 'I_AP'
                    action_labels[i] = action
                    collapsed_labels[i] = f'I_AP+{action}'
    
    return bio_tags, action_labels, collapsed_labels

def process_data(data):
    processed_lines = []
    for entry in data:
        sentence = entry['text']
        tokens = tokenize(sentence)
        aspects = entry['aspects']
        
        bio_tags, action_labels, collapsed_labels = generate_bio_tags(tokens, aspects)
        
        for token, bio_tag, action_label, collapsed_label in zip(tokens, bio_tags, action_labels, collapsed_labels):
            processed_lines.append(f"{token} POS CHUNK {bio_tag} {action_label} {collapsed_label}")
        
        # Add a blank line to separate sentences
        processed_lines.append("")
    
    return processed_lines

def write_to_file(lines, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main(input_file, output_file):
    data = load_json(input_file)
    processed_lines = process_data(data)
    write_to_file(processed_lines, output_file)

def process_directory(input_dir, output_dir):
    """
    Process JSON files in the specified directory and save them to mapped output files.

    Args:
        input_dir (str): Directory containing JSON files.
        output_dir (str): Directory to save the output text files.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)


    # Process files in the directory
    add_folder = False
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".json"):
            input_file = os.path.join(input_dir, file_name)

            # Determine the output file name based on keywords in the file name
            if "unseen" in file_name.lower() and "test" in file_name.lower():
                output_file = "disclosures_test.gold.txt"
                add_folder = "unseen"
            elif "seen" in file_name.lower() and "test" in file_name.lower():
                output_file = "disclosures_test.gold.txt"
                add_folder = "seen"
            elif "train" in file_name:
                output_file = "disclosures_train.txt"
            elif "val" in file_name:
                output_file = "disclosures_trial.txt"
            elif "test" in file_name:
                output_file = "disclosures_test.gold.txt"
            else:
                continue

            if add_folder:
                # make dir
                os.makedirs(os.path.join(output_dir, add_folder), exist_ok=True)
                output_path = os.path.join(output_dir, add_folder, output_file)
                add_folder = False
            else:
                output_path = os.path.join(output_dir, output_file)
            print(f"Processing {input_file} -> {output_path}")
            main(input_file, output_path)

if __name__ == "__main__":
    
    # input_file = '/home/esg_acaa/code/data/texts/final/all/sentence_id_split__final_annotation_train.json'
    # output_file = '/home/esg_acaa/code/data/texts_sota/grace/all/disclosures_train.txt'
    # main(input_file, output_file)
    
    input_dir = "/home/esg_acaa/code/data/texts/final/folds/fold_3"

    output_dir = "/home/esg_acaa/code/data/texts_sota/grace/fold_3"

    process_directory(input_dir, output_dir)