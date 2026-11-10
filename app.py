from pkg import book_tools

def main():
    input_file = "books.json"
    output_file = "output.json"
    try:
        books = book_tools.read_books(input_file)
    except FileNotFoundError:
        print(f"找不到書籍資料檔案 {input_file}。")
        return
    except ValueError:
        print(f"{input_file} 的 JSON 格式錯誤，請確認檔案為 UTF-8。")
        return
    except OSError as error:
        print(f"無法讀取 {input_file}：{error}")
        return

    while True:
        print("""\n--- 簡易書籍管理系統 ---\n1. 顯示全部書籍\n2. 新增書籍\n3. 查詢書籍\n4. 變更借閱狀態\n5. 顯示最後 3 筆書籍與統計\n6. 匯出書籍資料\n7. 離開系統\n------------------------""")
        choice = book_tools.check_input("請選擇功能：")

        if choice == "1":
            print("\n--- 全部書籍 ---")
            book_tools.show_books(books)
        elif choice == "2":
            book_tools.add_book(books)
        elif choice == "3":
            keyword = book_tools.check_input("請輸入書名關鍵字：")
            matches = book_tools.search_books(books, keyword)
            if matches:
                print("\n--- 查詢結果 ---")
                book_tools.show_books(matches)
            else:
                print("查無符合的書籍")
        elif choice == "4":
            book_tools.change_borrowed(books)
        elif choice == "5":
            book_tools.show_recent_and_status(books)
        elif choice == "6":
            try:
                book_tools.write_books(books, output_file)
            except OSError as error:
                print(f"無法匯出 {output_file}：{error}")
            else:
                print(f"已匯出 {len(books)} 筆書籍資料至 {output_file}。")
        elif choice == "7":
            print("系統已退出。")
            break
        else:
            print("請輸入 1～7 的功能編號。")


if __name__ == "__main__":
    main()
