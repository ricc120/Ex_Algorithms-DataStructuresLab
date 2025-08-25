import os
import pandas as pd
import matplotlib.pyplot as plt


def structure_graphics(csv_file="benchmark_results.csv", output_dir="graphs"):
    # Create directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load results
    df = pd.read_csv(csv_file)

    # List of structures in .csv
    structures = df["structure"].unique()

    # Comparative graph
    plt.figure(figsize=(8, 6))
    for structure in structures:
        res = df[df["structure"] == structure]
        plt.plot(
            res["n_nodes"], res["avg_time_sec"],
            marker="o", label=structure
        )
    plt.title("Confronto tra strutture disgiunte al variare dei nodi")
    plt.xlabel("Numero di nodi")
    plt.ylabel("Tempo medio (s)")
    plt.legend()
    plt.grid(True)

    filepath = os.path.join(output_dir, "confronto_strutture.png")
    plt.savefig(filepath, bbox_inches="tight")
    plt.close()
    print(f"Comparative graph saved in {filepath}")

    # Single graph
    for structure in structures:
        res = df[df["structure"] == structure]

        plt.figure(figsize=(8, 6))
        plt.plot(
            res["n_nodes"], res["avg_time_sec"],
            marker="o", color="blue"
        )
        plt.title(f"Andamento {structure} al variare dei nodi")
        plt.xlabel("Numero di nodi")
        plt.ylabel("Tempo medio (s)")
        plt.grid(True)

        filename = f"{structure}_andamento.png"
        filepath = os.path.join(output_dir, filename)
        plt.savefig(filepath, bbox_inches="tight")
        plt.close()
        print(f"Single graph saved in {filepath}")


if __name__ == "__main__":
    structure_graphics()
