import json

def read_books(file_name: str) -> list:
    with open(file_name, encoding="utf-8") as file:
        return json.load(file)


def write_books(b: list, file_name: str) -> None:
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(b, file, ensure_ascii=False, indent=4)
        file.write("\n")


def search_books(b: list, key: str) -> list:
    key = key.lower()
    return [book for book in b if key in book["title"].lower()]


def show_books(books: list) -> None:
    if not books:
        print("目前沒有書籍資料")
        return

    print("編號  書籍編號  書名                作者                價格  狀態")
    for number, book in enumerate(books, 1):
        status = "已借出" if book["borrowed"] else "可借閱"
        print(
            f"{number:>4}  {book['id']:<8}  {book['title']:<16}  {book['author']:<8}  {book['price']:>10,}   {status}"
        )


def check_input(n: str) -> str:
    while True:
        x = input(n).strip()
        if x:
            return x
        print("輸入不可為空，請重新輸入。")


def add_book(b: list) -> None:
    while True:
        book_id = check_input("請輸入書籍編號：")
        for books in b:
            if books["id"] == book_id:
                print("書籍編號已存在，請重新輸入。")
                break
        else:
            break

    title = check_input("請輸入書名：")
    author = check_input("請輸入作者：")

    while True:
        try:
            price = int(check_input("請輸入價格："))
        except ValueError:
            print("價格須為大於 0 的整數，請重新輸入。")
            continue

        if price > 0:
            break
        print("價格須為大於 0 的整數，請重新輸入。")

    b.append({
        "id": book_id,
        "title": title,
        "author": author,
        "price": price,
        "borrowed": False,
    })
    print("新增成功。")


def change_borrowed(b: list) -> None:
    book_id = check_input("請輸入書籍編號：")
    for books in b:
        if books["id"] == book_id:
            books["borrowed"] = not books["borrowed"]
            status = "已借出" if books["borrowed"] else "可借閱"
            print(f"「{books['title']}」的狀態已變更為：{status}")
            return

    print("查無此書籍編號")


def show_recent_and_status(b: list) -> None:
    print("\n--- 最後 3 筆書籍 ---")
    show_books(b[-3:])

    if not b:
        return

    total = len(b)
    count = 0
    total_p = 0
    for book in b:
        if book["borrowed"]:
            count += 1
        total_p += book["price"]

    print("\n--- 書籍統計 ---")
    print(f"書籍總數：{total}")
    print(f"可借閱：{total - count}")
    print(f"已借出：{count}")
    print(f"價格合計：{total_p:,} 元")
    print(f"平均價格：{total_p / total:.2f} 元")
