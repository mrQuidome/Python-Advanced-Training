movies = {
    "tomorrow_never_dies": {"name": "Tomorrow Never Dies", "genre": "Action"},
    "robin_hood": {"name": "Robin Hood", "genre": "Adventure"},
    "pulp_fiction": {"name": "Pulp Fiction", "genre": "Crime"},
}


def invoice(movie, tickets):
    if tickets == 0:
        raise ValueError("Cannot calculate price for 0 tickets")

    if movie not in movies:
        raise LookupError("Movie not available")

    price = 10
    if movies[movie]["genre"] == "Action":
        price = 12

    return tickets * price - discount(tickets)


def discount(tickets):
    if tickets >= 5:
        return  10

    return 0


print(invoice("pulp_fiction", 6))