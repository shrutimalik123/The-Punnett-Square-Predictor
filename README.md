# 🧬 The Punnett Square Predictor - Genetic Logic Sim

A biological simulation that calculates the probability of inherited traits. You play as a Geneticist analyzing the genotypes of two parents to predict the physical appearance of their offspring. This project demonstrates the "Law of Dominance," where a single capital-letter allele (Dominant) can mask the presence of a lowercase-letter allele (Recessive).

This project focuses on teaching:
* **Nested Loop Combinations:** Using a `for` loop inside another `for` loop to generate all 4 possible genetic outcomes.
* **String Parsing:** Checking for the existence of specific characters (Alleles) within a string to determine a physical trait.
* **Data Normalization:** Using `sorted()` to ensure that a "b" and a "B" always result in "Bb" rather than "bB" for consistent data tracking.
* **Phenotype vs. Genotype:** Distinguishing between the underlying code and the visible result.

---

## ✨ Features

* **Procedural Parent Generation:** Randomly assigns genotypes (Homozygous Dominant, Heterozygous, or Homozygous Recessive) to the parents.
* **Dominance Logic:** Automatically calculates how many offspring will express the dominant trait based on the presence of at least one 'B'.
* **Probability Accuracy:** Mirrors real-world Mendelian genetics with 0%, 25%, 50%, 75%, or 100% frequency results.
* **Error Handling:** Validates numeric input to ensure the simulation doesn't crash during the prediction phase.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `punnett_predictor.py`.
2.  **Open Terminal:** Navigate to the folder containing the file.
3.  **Run the Script:**
    ```bash
    python punnett_predictor.py
    ```

### 3. Gameplay Instructions
1.  **Analyze the Parents:** Note the two letters for each parent (e.g., **Bb** and **bb**).
2.  **Calculate the Cross:** Combine the first letter of Parent 1 with both letters of Parent 2, then repeat for the second letter.
3.  **Count the Dominant Traits:** Identify how many of the 4 combinations contain at least one **'B'**.
4.  **Enter Your Prediction:** See if your manual calculation matches the computer's genetic analysis!



---

## 🧠 Code Structure Highlights

### Simulating the $2 \times 2$ Grid
The core of the Punnett Square is a grid. In code, we simulate this by iterating through every character in `parent1` and pairing it with every character in `parent2`.

```python
# The Nested Loop Cross
for gene1 in parent1:
    for gene2 in parent2:
        # result = gene1 + gene2

