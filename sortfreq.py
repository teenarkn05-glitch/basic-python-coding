st = "aabacbd"
for i in set(st):
    print(sorted(f"{i}"*st.count(i)))
