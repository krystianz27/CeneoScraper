import os
import pandas as pd

# 138536499
# 96685108

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")

opinion_count = len(opinions.index)
# opinion_count = opinions.shape[0]
# pros_count = sum([False if len(p)==0 else True for p in opinions.pros])
# cons_count = sum([False if len(c)==0 else True for c in opinions.cons])
pros_count = opinions.pros.map(lambda p: False if len(p)==0 else True).sum()
cons_count = opinions.cons.map(lambda c: False if len(c)==0 else True).sum()

avg_scoe = 0

print(opinion_count)
print(pros_count)
print(cons_count)