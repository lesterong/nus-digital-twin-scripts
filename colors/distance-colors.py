import seaborn as sns

### CONTROLS ###
STEP_SIZE = 0.0005
START = 0
END = 0.0155
#################

colors = sns.color_palette("GnBu", int(END / STEP_SIZE)).as_hex()

res = []

for i, color in enumerate(colors):
  res.append([f"${{distance}} > {((i + 1) * STEP_SIZE):.4f}", f"color('{color}')"])

res.reverse()

print(res)