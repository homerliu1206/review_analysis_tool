## **Review Analysis Tool**

### Overview

This Python script analyzes a dataset of reviews stored in a text file named `reviews.txt`. It provides various functionalities to perform statistical analysis on the reviews, including calculating average review length, counting reviews with lengths less than 100 characters, identifying reviews containing specific keywords (e.g., "good"), and generating word frequency statistics.

### Features

1. **Read File:** The script reads the `reviews.txt` file and stores the reviews in memory for analysis.
2. **Average Review Length:** Calculates and displays the average length of the reviews in terms of characters.
3. **Reviews Length Check:** Counts and displays the number of reviews with lengths less than 100 characters.
4. **Keyword Search:** Identifies and counts the number of reviews containing specific keywords (e.g., "good").
5. **Word Frequency Analysis:** Generates word frequency statistics, counting the occurrence of each word in the reviews and displaying words with frequencies exceeding a certain threshold.
6. **Word Count:** Displays the total number of unique words found in the reviews.
7. **Word Query:** Allows users to input a word and retrieves its frequency in the reviews.

### Usage

1. Ensure the `reviews.txt` file is in the same directory as the script.
2. Run the script in a Python environment.
3. Follow the prompts to perform various analysis operations:
    - Enter `q` to quit the program.
    - Enter a word to query its frequency in the reviews.
