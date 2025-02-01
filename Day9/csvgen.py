arr = ["bananas","apples","oranges","grapes","pears"]
with open("Day9/fruits.csv", "w") as f:
    f.write(",".join(arr) + "\n")