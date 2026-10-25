
import csv
import time
import argparse

FIELDS = [
    "book_id", "title", "authors", "publisher",
    "published_date", "categories", "page_count",
    "average_rating", "language"
]


def load_books(csv_path):
    books = []

    with open(csv_path, "r", encoding="utf-8-sig",
              newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row.get("book_id") and row.get("title"):
                book = {
                    key: row.get(key, "")
                    for key in FIELDS
                }
                books.append(book)

    # Binary Search membutuhkan data yang terurut.
    books.sort(key=lambda book: book["book_id"])
    return books


def linear_search(books, key):
    comparisons = 0

    for book in books:
        comparisons += 1

        if book["book_id"] == key:
            return book, comparisons

    return None, comparisons


def binary_search(books, key):
    low = 0
    high = len(books) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        mid_key = books[mid]["book_id"]

        if mid_key == key:
            return books[mid], comparisons
        elif mid_key < key:
            low = mid + 1
        else:
            high = mid - 1

    return None, comparisons


def show_result(book, comparisons, elapsed):
    if book is None:
        print("Data buku tidak ditemukan.")
    else:
        print("\nData buku ditemukan:")
        for key, value in book.items():
            print(f"{key}: {value}")

    print(f"Jumlah perbandingan: {comparisons}")
    print(f"Waktu pencarian: {elapsed:.9f} detik")


def benchmark(books):
    print("\n=== HASIL PENGUJIAN ===")
    print(
        f"{'n':>6} {'Algoritma':<15} "
        f"{'Skenario':<18} {'Perbandingan':>13} "
        f"{'Waktu (detik)':>16}"
    )

    for n in (100, 1000, 10000):
        subset = books[:min(n, len(books))]

        if not subset:
            continue

        middle = len(subset) // 2

        cases = [
            ("Awal", subset[0]["book_id"]),
            ("Tengah", subset[middle]["book_id"]),
            ("Akhir", subset[-1]["book_id"]),
            ("Tidak ditemukan", "__ID_TIDAK_ADA__")
        ]

        algorithms = [
            ("Linear Search", linear_search),
            ("Binary Search", binary_search)
        ]

        for name, algorithm in algorithms:
            for scenario, key in cases:
                start = time.perf_counter()
                _, comparisons = algorithm(subset, key)
                elapsed = time.perf_counter() - start

                print(
                    f"{len(subset):>6} {name:<15} "
                    f"{scenario:<18} {comparisons:>13} "
                    f"{elapsed:>16.9f}"
                )


def main():
    parser = argparse.ArgumentParser(
        description="Perbandingan Linear Search dan Binary Search"
    )

    parser.add_argument(
        "--csv",
        default="google_books_dataset.csv"
    )
    parser.add_argument("--key")
    parser.add_argument(
        "--algorithm",
        choices=["linear", "binary", "both"],
        default="both"
    )
    parser.add_argument("--benchmark", action="store_true")

    args = parser.parse_args()
    books = load_books(args.csv)

    print(f"Jumlah data buku valid: {len(books)}")

    if args.key is not None:
        algorithms = []

        if args.algorithm in ("linear", "both"):
            algorithms.append(("Linear Search", linear_search))

        if args.algorithm in ("binary", "both"):
            algorithms.append(("Binary Search", binary_search))

        for name, algorithm in algorithms:
            start = time.perf_counter()
            book, comparisons = algorithm(books, args.key)
            elapsed = time.perf_counter() - start

            print(f"\n=== {name} ===")
            show_result(book, comparisons, elapsed)

    if args.benchmark:
        benchmark(books)

    if args.key is None and not args.benchmark:
        print(
            "Gunakan --key ID_BUKU untuk mencari atau "
            "--benchmark untuk menguji algoritma."
        )


if __name__ == "__main__":
    main()
