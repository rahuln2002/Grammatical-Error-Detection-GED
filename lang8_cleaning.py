# Importing necessary libraries
import torch  # PyTorch library for deep learning, tensor manipulation, and model inference
import Levenshtein  # Library for calculating Levenshtein distance (edit distance) between strings
import regex as re  # Regular expression library for text processing, used here for advanced regex operations
import unicodedata  # Library for Unicode character processing, e.g., for normalizing text


# Function to handle contractions in text (e.g., "can't" -> "cannot")
def handle_contractions(df, cn):
    # Dictionary of common contractions and their expanded forms
    contractions_dict = {
    "ain't": "am not",
    "aren't": "are not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'd've": "he would have",
    "he'll": "he will",
    "he'll've": "he will have",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'd've": "I would have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so is",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you would",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have"
    }

    # Regular expression to match contractions in the text
    contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()))

    # Function to replace matched contractions with their expanded forms
    def replace(match):
        return contractions_dict[match.group(0)]
    
    # Apply the contraction replacement to the specified column of the DataFrame
    df[cn] = df[cn].apply(lambda sent: contractions_re.sub(replace, sent))
    return df

# Function to normalize text (e.g., handling unicode normalization)
def normalize_text(df, cn):

    # Function to normalize a single sentence (handle unicode normalization and punctuation spacing)
    def normalize_single_text(text):
        text = unicodedata.normalize('NFKC', text)  # Normalize unicode characters
        text = re.sub(r'([.,!?;:])', r'\1 ', text)   # Add spaces after punctuation marks
        return text
    
    # Apply the normalization function to the column
    df[cn] = df[cn].apply(normalize_single_text)
    
    # Replace specific apostrophes (e.g., `’` or `‘`) with standard apostrophe
    df[cn] = df[cn].str.replace("[’‘`]", "'", regex=True)

    return df

# Function to convert all text in the specified column to lowercase
def lowercase(df, cn):
    df[cn] = df[cn].str.lower()
    return df

# Function to remove extra spaces from text (and fix common contractions)
def removesp(df, n1, n2="new"):
    # Remove extra spaces between words, fixing specific contractions like 's, 've, etc.
    df[n2] = df[n1].str.replace(r'\s+(\'s|n\'t|\'ve|\'re|\'d|\'ll)', r'\1', regex=True)
    df[n2] = df[n2].str.replace(r'\s+([.,!?;:\']|\'s)', r'\1', regex=True)
    df[n2] = df[n2].str.replace(r'\s{2,}', ' ', regex=True)  # Replace multiple spaces with a single space
    df[n2] = df[n2].str.strip()  # Remove leading and trailing spaces
    return df

# Function to remove punctuation from text
def removepunc(df, cn):
    # Function to remove all punctuation from a sentence
    def remove_punctuations(sentence):
        return sentence.replace(r'[^\w\s]', '', regex=True)  # Keep only alphanumeric characters and whitespace

    # Apply punctuation removal to the specified column
    df['new_' + cn] = remove_punctuations(df[cn])
    return df

# Function to remove rows with different sentences in two columns
def removesm(df, n1, n2):
    # Create a new column to track if the sentences in the two columns are the same
    df['IsSame'] = df[n1] == df[n2]
    df = df[df['IsSame'] == False]  # Keep only rows where the sentences are different
    df = df.drop(columns=['IsSame'])  # Drop the 'IsSame' column
    return df

# Function to filter out sentences with minor differences based on Levenshtein distance
def minordist(df, n1, n2, levenshtein_threshold=5):
    # Compute the Levenshtein distance between the two sentence columns
    df.loc[:, 'LevenshteinDistance'] = df.apply(lambda row: Levenshtein.distance(row[n1], row[n2]), axis=1)
    
    # Create a column to check if the Levenshtein distance is within the threshold
    df.loc[:, 'IsSimilar'] = df['LevenshteinDistance'] <= levenshtein_threshold

    # Count the number of similar sentences
    num_similar_sentences = df['IsSimilar'].sum()
    print(f"Number of sentences with minor differences (Levenshtein distance within {levenshtein_threshold}): {num_similar_sentences}")

    # Keep only rows with significant differences
    df = df[df['IsSimilar'] == False]
    df = df.drop(columns=['IsSimilar'])  # Drop the similarity check column
    return df
