numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 5:
        print("Encountered 5. Breaking the loop.")
        break
    if num == 3:
        print("Encountered 3. Skipping to the next iteration.")
        continue
    print("Current number:", num)
print("Loop finished.")

