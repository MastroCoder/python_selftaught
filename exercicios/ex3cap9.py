import csv

l = [["Top Gun", "Risky Business", "Minority Report"],
     ["Titanic", "The Revenant", "Inception"],
     ["Training Day", "Man On Fire", "Flight"]]

with open("ex3.csv", "w") as f:
    w = csv.writer(f, delimiter = ",")
    for i in l:
        w.writerow(i)
