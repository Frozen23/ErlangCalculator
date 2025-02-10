def erlang_b_recursive(traffic, channels):
    """
    Oblicza prawdopodobieństwo blokady (Erlang B) rekurencyjnie.
    traffic: intensywność ruchu (w Erlangach)
    channels: liczba kanałów
    """
    if channels == 0:
        return 1.0
    else:
        prev = erlang_b_recursive(traffic, channels - 1)
        return (traffic * prev) / (traffic * prev + channels)

def minimal_channels(users, avg_call_time, target_blocking_prob):
    """
    Oblicza minimalną liczbę kanałów przy zadanym prawdopodobieństwie blokady.
    users: liczba użytkowników
    avg_call_time: średni czas rozmowy (w godzinach)
    target_blocking_prob: docelowe prawdopodobieństwo blokady (np. 0.01 )
    """
    # Obliczenie intensywności ruchu w Erlangach
    traffic = users * avg_call_time

    channels = 1
    while True:
        blocking_prob = erlang_b_recursive(traffic, channels)
        if blocking_prob <= target_blocking_prob:
            return channels
        channels += 1

# Przykład użycia
if __name__ == "__main__":
    users = int(input("Podaj liczbę użytkowników: "))
    avg_call_time = float(input("Podaj średni czas rozmowy (w godzinach): "))
    target_blocking_prob = float(input("Podaj docelowe prawdopodobieństwo blokady (np. 0.01 dla 1%): "))

    minimal_channels_needed = minimal_channels(users, avg_call_time, target_blocking_prob)
    print(f"Minimalna liczba kanałów: {minimal_channels_needed}")