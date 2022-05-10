# Zipf's Law

## Definition
Zipf's law is an empirical law formulated using mathematical statistics that refers to the fact that for many types of data studied in the physical and social sciences, the rank-frequency distribution is an inverse relation. It states that, for example, in the case of words in a linguistic corpus, the frequencies of certain words are inversely proportional to their ranks.

## Program
I wrote a program that creates a dictionary where every key: value pair is a word from the script of the [Bee Movie](https://www.imdb.com/title/tt0389790/) and its frequency in the entire script. I organize the dictionary in descending order in terms of values, take the top 20 words and plot a graph to see if Zipf's Law holds. I use the data visualization library called [Matplotlib](https://matplotlib.org). You can install the library through pip using the following terminal command:

```pip install matplotlib```<br><br>
or you can download it from [here](https://pypi.org/project/matplotlib/) and install it manually.

## Output
The graph I receive in the output is attached below, feel free to modify the code to read whatever text file you want.

<img width="636" alt="Screenshot 2022-05-10 at 8 12 56 PM" src="https://user-images.githubusercontent.com/64619851/167719267-5c4ded44-8072-40ad-8c75-8dd38ca9ab53.png">
