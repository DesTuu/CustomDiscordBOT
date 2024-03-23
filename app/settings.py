import pathlib

COMMAND_PREFIX = f"$"

BASE_DIR = pathlib.Path(__file__).parent

COG_DIR = BASE_DIR / "cogs"

QUEUE_MESSAGE = """Graczu!
Dokładamy wszelkich starań, żeby nas server i organizowane na nim gry były dopasowane dla każdego dlatego pamiętaj!

- Kolejka mieszana przeznaczona jest dla każdego gracza, możesz tu spotkać zarówno graczy z Ironem i Challenerów. Bądź wyrozumiały.
- Kolejka D+ to kolejka wysokich lotów - tutaj dajemy z siebie 100%! Spraw by drużyna była z Ciebie zadowolona!

Niezależnie od kolejki, w której grasz, pamiętaj - jeśli widzisz lub słyszysz zachowania, które obniżają jakość rozgrywek poprzez np. negatywne nastawienie, obrażanie itp.
Daj nam znać na kanale https://discord.com/channels/979427975692947546/1154079685760794664
## no to jak? SKALUJEMY czy NIE SKALUJEMY?"""

WERYFIKACJA_MESSAGE = """Weryfikacje przejść można za pomocą linku: [LINK](https://orianna.molenzwiebel.xyz/login-fail)
By przejść pozytywnie weryfikację zaloguj się za pomocą powyższego linku kontem z discorda, po czym kliknij "add new" i zaznacz region, wpisując przy tym swoją nazwę przywoływacza. 
Zostaniesz poproszony o ustawienie jednego z dostępnych od pierwszego lvl avataru na swoim koncie z ligi."""


def get_guild_names(bot):
    for i in bot.guilds:
        yield i.name


def on_ready_message(bot):
    print("Załadowano wszystkie komendy z folderu cogs i zalogowano pomyślnie!")
    if len(set(get_guild_names(bot))) >= 2:
        print(f"Bot znajduje się na takich serwerach jak: {', '.join(get_guild_names(bot))}")
    else:
        print(f"Bot znajduje się na tylko na jednym serwerze: {', '.join(get_guild_names(bot))}")
