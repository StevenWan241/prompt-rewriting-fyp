"""Draw the pilot tasks by seeded random sample (decision D18)."""
import random

from datasets import load_dataset

SEED = 42
N_PER_SET = 5


def draw(task_ids, n, seed):
    """Return n task ids chosen at random, the same way every time."""
    rng = random.Random(seed)
    ordered = sorted(task_ids)
    return rng.sample(ordered, n)


def main():
    humaneval = load_dataset("openai/openai_humaneval")["test"]
    mbpp = load_dataset("google-research-datasets/mbpp", "sanitized")["test"]

    he_ids = [row["task_id"] for row in humaneval]
    mbpp_ids = [row["task_id"] for row in mbpp]

    he_pilot = draw(he_ids, N_PER_SET, SEED)
    mbpp_pilot = draw(mbpp_ids, N_PER_SET, SEED)

    print("HumanEval:", he_pilot)
    print("MBPP:", mbpp_pilot)


if __name__ == "__main__":
    main()