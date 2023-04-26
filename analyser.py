import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# 138536499
# 96685108
# 105563156
# 39562616

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")

product_code = input("Podaj kod produktu: ")

opinions = pd.read_json(f"./opinions/{product_code}.json")
# opinions.score = opinions.score.map(lambda x: float(x[:-2].replace(",",".")))
opinions.score = opinions.score.map(lambda x: float(x.split("/")[0].replace(",",".")))

opinion_count = len(opinions.index)
# opinion_count = opinions.shape[0]
# pros_count = sum([False if len(p)==0 else True for p in opinions.pros])
# cons_count = sum([False if len(c)==0 else True for c in opinions.cons])
# pros_count = opinions.pros.map(lambda p: False if len(p)==0 else True).sum()
# cons_count = opinions.cons.map(lambda c: False if len(c)==0 else True).sum()

pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.pros.map(bool).sum()
avg_score = opinions.score.mean().round(2)

print(f"""For product with product code: {product_code} are {opinion_count} opinions,
for {pros_count} opinions is available pros list,
for {cons_count} opinions is available cons list.
Average product evaluation: {avg_score}""")
# print(opinion_count)
# print(pros_count)
# print(cons_count)
# print(avg_score)

# histogram czestotliwosci wystepowania poszczegolnych ocen
score = opinions.score.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
# print(score)
score.plot.bar(color="blue")
plt.title("Histogram evaluation")
plt.xlabel("Number of stars")
plt.ylabel("Number of opinions")
plt.xticks(rotation=0)
# plt.ylim([0, 90])
for index, value in enumerate(score):
    plt.text(index, value+1.5, str(value), ha="center")
# plt.show()

try:
    os.mkdir("./plots")
except FileExistsError:
    pass

plt.savefig(f"./plots/{product_code}_score.png")
plt.close()



# udzial poszczegolnych rekomendacji w ogolnej liczbie opini
recommendation = opinions["recommendation"].value_counts(dropna = False).sort_index()
print(recommendation)
recommendation.plot.pie(
    label="", 
    autopct="%1.1f%%",
    labels = ["No recommend", "Recommend", "Neutral"],
    colors = ["crimson", "forestgreen", "gray"]
)


# plt.labels(["No recommend", "Recommend", "Neutral"])
# plt.colors(["crimson", "forestgreen", "gray"])
plt.legend(bbox_to_anchor=(1.0,1.0))
plt.savefig(f"./plots/{product_code}_recommendation.png")
plt.close()
