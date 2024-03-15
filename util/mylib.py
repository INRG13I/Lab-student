def sort_apartments(all_apartments):
    all_apartments = sorted(all_apartments, key=lambda i: i["number"])
    return all_apartments