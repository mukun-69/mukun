import random

nama = input("Masukkan nama petualang: ")

level = 1
hp = 150
exp = 0
attack = 50

print("\n==== SIMPLE RPG ====")
print(f"Selamat datang, {nama}!")
print(f"Level: {level}")
print(f"HP: {hp}")
print(f"EXP: {exp}")
print(f"Attack: {attack}")

print("\n==== Monster Muncul! ====")

monster = random.choice(["Goblin", "Orc", "Slime"])
hp_monster = random.randint(60, 100)
attack_monster = random.randint(35, 56)

print(f"Monster: {monster}")
print(f"HP Monster: {hp_monster}")
print(f"Attack Monster: {attack_monster}")

print("\n==== BATTLE IS STARTING! ====")

damage = random.randint(attack - 10, attack + 15)
print(f"{nama} menyerang {monster}")
print(f"Damage: {damage}")

hp_monster = hp_monster - damage
print(f"HP Monster now: {hp_monster}")

if hp_monster <= 0:
    print(f"{monster} died!")
else:
    print(f"{monster} still alive!")

    print("\n==== MONSTER'S TURN =====")

    if hp_monster > 0:
        print(f"{monster} attack {nama}! ")

        damage_monster = random.randint(50, 85)
        hp = hp - damage_monster
        print(f"you receive a {damage_monster} damage!")
        print(f"your HP now: {hp}")

        if hp <= 0:
            print(f"You died! Your hp is gone!")
        else:
            print(f"You still alive!")