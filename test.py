
price = int(input("値段をいれてちょ: "))
ans = input("お持ち帰りですか？: ")

if ans == "●":
    result = price * 1.1 # type: ignore
else:
    result = price * 1.08 # type: ignore

print("値段は" + str(int(result)) + "円です")