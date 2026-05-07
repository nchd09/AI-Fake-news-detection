fake["label"] = 0
true["label"] = 1
df = pd.concat([fake, true])

df = df[["title", "text", "label"]]