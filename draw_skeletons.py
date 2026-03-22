def draw_human_skeleton():
    print("  O ") # Cap
    print(" /|\ ") # Gat si umeri
    print(" / \ ") # Corp si picioare

n = int(input("How many skeletons should I draw? "))

for i in range(n):
    #draw_human_skeleton()
    print("   o   ", end="")
print()
for i in range(n):
    print("  /|\  ", end="")
print()
for i in range(n):
    print("  / \  ", end="")
print()