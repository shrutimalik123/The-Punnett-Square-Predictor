import random

def punnett_square_game():
    # 1. Genetic Setup
    # Capital = Dominant (Blue Eyes), Lowercase = Recessive (Brown Eyes)
    traits = {
        "B": "Blue Eyes",
        "b": "Brown Eyes"
    }
    
    # Generate random genotypes for parents
    # Options: BB (Homozygous Dom), Bb (Heterozygous), bb (Homozygous Rec)
    parent1 = random.choice(["BB", "Bb", "bb"])
    parent2 = random.choice(["BB", "Bb", "bb"])
    
    print("--- 🧬 THE PUNNETT SQUARE PREDICTOR 🧬 ---")
    print(f"Parent 1 Genotype: {parent1}")
    print(f"Parent 2 Genotype: {parent2}")
    print("\nRule: 'B' (Dominant) hides 'b' (Recessive).")
    print("Example: 'Bb' results in Blue Eyes.")

    # 2. Calculation Logic
    # We combine every letter from Parent 1 with every letter from Parent 2
    offspring_possibilities = []
    for gene1 in parent1:
        for gene2 in parent2:
            # Sort them so "bB" always becomes "Bb" for consistency
            combination = "".join(sorted([gene1, gene2]))
            offspring_possibilities.append(combination)

    # 3. Game Challenge
    print("\nChallenge: Out of the 4 possible offspring combinations...")
    try:
        user_guess = int(input("How many will have BLUE EYES? (0-4): "))
    except ValueError:
        print("❌ Please enter a number!")
        return

    # 4. Phenotype Calculation
    # Blue eyes happen if there is at least one 'B'
    blue_eyes_count = 0
    for child in offspring_possibilities:
        if "B" in child:
            blue_eyes_count += 1

    # 5. Result Validation
    print(f"\n--- GENETIC ANALYSIS ---")
    print(f"Combinations: {', '.join(offspring_possibilities)}")
    
    if user_guess == blue_eyes_count:
        print(f"✅ EXCELLENT! {blue_eyes_count}/4 offspring carry the dominant trait.")
        print("Your pedigree chart is perfectly calculated.")
    else:
        print(f"❌ CALCULATION ERROR. The correct count was {blue_eyes_count}.")
        print("Remember: Even one 'B' results in the dominant phenotype!")

punnett_square_game()
