# Das einfachste Spiel der Welt

1. Geht ins Terminal.

1. Erstellt einen Ordner namens "simple-game" (`mkdir` steht für `make directory`, erstellt Verzeichnis)

    ```bash
    mkdir simple-game
    ```

1. Geht in den Ordner `simple-game` (`cd` steht für `change directory`, wechselt Verzeichnis)

    ```bash
    cd simple-game
    ```

1. Erstellt eine Python-Umgebung. Sonst könnt ihr den Python Code nicht ausführen

    ```bash
    python3 -m venv .
    source ./bin/activate
    ```

1. Erstellt eine neue Datei namens `game.py` (`touch` steht für `touching a file`, eine Datei "berühren")

    ```bash
    touch game.py
    ```

1. Öffnet die Datei `game.py` im Editor (`open` öffnet eine Datei).

    ```bash
    open game.py
    ```

1. Öffnet in eurem Editor die kürzlich erstellte Datei und schreibt den folgenden Code hinein. 💾 Speichert die Datei mit der Tastenkombination `command + s`. Merkt euch diese Tastenkombination, wir werden sie jetzt öfter brauchen.

    ```python
    import curses

    def main(stdscr):
        stdscr.clear()

    curses.wrapper(main)
    ```

1. 🎮 Führt die Datei in eurem Terminal aus. Ihr werdet sehen, dass der Bildschirm kurz blinkt, was eine Ausführung von `clear` ist.

    ```bash
    python game.py
    ```

1. ☝️ Meldet euch beim Lehrenden, damit dieser euch den Code erklären kann.

1. 👩‍💻 Geht zurück zum Editor und verändert den Code wie folgt. 💾 Speichern nicht vergessen.

    ```python
    import curses

    def main(stdscr):
        stdscr.clear()
        while True:
            key = stdscr.getch()
            if key == ord('q'):
                break

    curses.wrapper(main)
    ```

1. 💬 Besprecht den neuen Code im Team und versucht die neuen Zeilen zu verstehen. 🎮 Was passiert nun, wenn der Code erneut ausgeführt wird?

    ```bash
    python game.py
    ```

1. ☝️ Meldet euch beim Lehrenden, damit dieser euch den Code erklären kann.

1. 👩‍💻 Geht zurück zum Editor und verändert den Code wie folgt.

    ```python
    import curses

    def main(stdscr):
        stdscr.clear()

        x = 0
        y = 0

        while True:
            stdscr.addstr(y, x, 'X')
            key = stdscr.getch()
            if key == ord('q'):
                break

    curses.wrapper(main)
    ```

1. 💬 Besprecht wieder den neuen Code im Team und versucht die neuen Zeilen zu verstehen. 🎮 Was passiert nun, wenn der Code erneut ausgeführt wird? (☝️ Meldet euch beim Lehrenden, wenn ihr Probleme habt, den Code zu verstehen.). 💾 Denkt ans Speichern.

    ```bash
    python game.py
    ```

1. 👩‍💻 Geht zurück zum Editor und verändert den Code wie folgt.

    ```python
    import curses

    def main(stdscr):
        stdscr.clear()
        screen_height, screen_width = stdscr.getmaxyx()

        x = screen_width
        y = screen_height

        while True:
            stdscr.addstr(y, x, 'X')
            key = stdscr.getch()
            if key == ord('q'):
                break

    curses.wrapper(main)
    ```

1. 💾 💬 Besprecht den neuen Code wieder und 🎮 führt ihn aus. Was passiert nun? ☝️ Meldet euch beim Lehrenden.

    ```bash
    python game.py
    ```

1. 👩‍💻 Geht zurück zum Editor und verändert den Code wie folgt.

    ```python
    import curses

    def main(stdscr):
        stdscr.clear()
        screen_height, screen_width = stdscr.getmaxyx()

        x = screen_width - 2
        y = screen_height - 1

        while True:
            stdscr.addstr(y, x, 'X')
            key = stdscr.getch()
            if key == ord('q'):
                break

    curses.wrapper(main)
    ```

1. 👩‍💻 Geht zurück zum Editor. Jetzt fügen wir weitere Tasten hinzu. (💾 / 🎮)

    ```python
    import curses

    def main(stdscr):
        stdscr.clear()
        screen_height, screen_width = stdscr.getmaxyx()

        x = screen_width - 2
        y = screen_height - 1

        while True:
            stdscr.addstr(y, x, 'X')
            key = stdscr.getch()
            if key == ord('q'):
                break
            if key == curses.KEY_UP:
                y = y - 1

    curses.wrapper(main)
    ```

1. 💬 Besprecht den neuen Code und führt ihn aus. Welche Taste haben wir hinzugefügt? Beobachtet, was passiert. Wie kann man das Programm nun verbessern? (💾 / 🎮)

1. ☝️ Meldet euch beim Lehrenden.

1. 👩‍💻 Geht zurück zum Editor und fügt die unten markierte Zeile hinzu. Führt den Code nach erneut aus.

    ```python
    import curses

    def main(stdscr):
        stdscr.clear()
        screen_height, screen_width = stdscr.getmaxyx()

        x = screen_width - 2
        y = screen_height - 1

        while True:
            stdscr.addstr(y, x, 'X')
            key = stdscr.getch()
            stdscr.addstr(y, x, ' ')  # <--- Diese Zeile hinzufügen
            if key == ord('q'):
                break
            if key == curses.KEY_UP:
                y = y - 1

    curses.wrapper(main)
    ```

1. 💬 Was passiert nun, wenn ich die `KEY_UP` Taste ganz oft drücke? Versucht einen Fehler zu produzieren. Warum entsteht dieser Fehler? (💾 / 🎮)

1. 👩‍💻 Geht zurück zum Editor. Um den Fehler zu verhindern, müssen wir die unten markierte Zeile verändern. Führt den Code erneut aus und schaut, was passiert. (💾 / 🎮)

    ```python
    import curses

    def main(stdscr):
        stdscr.clear()
        screen_height, screen_width = stdscr.getmaxyx()

        x = screen_width - 2
        y = screen_height - 1

        while True:
            stdscr.addstr(y, x, 'X')
            key = stdscr.getch()
            stdscr.addstr(y, x, ' ')
            if key == ord('q'):
                break
            if key == curses.KEY_UP and y > 0:   # <--- Diese Zeile hinzufügen
                y = y - 1

    curses.wrapper(main)
    ```

1. 💬 Besprecht nun, was nun bei dem Programm fehlt? Wenn ihr Fragen habt, könnt ihr euch gern beim Lehrenden melden. ☝️

1. 👩‍💻 Geht zurück zum Editor. Schaut euch den Code an und versucht zu verstehen was passiert. (💾 / 🎮)

    ```python
        import curses

        def main(stdscr):
            stdscr.clear()
            screen_height, screen_width = stdscr.getmaxyx()

            x = screen_width - 2
            y = screen_height - 1

            while True:
                stdscr.addstr(y, x, 'X')
                key = stdscr.getch()
                stdscr.addstr(y, x, ' ')
                if key == ord('q'):
                    break
                if key == curses.KEY_UP and y > 0:
                    y = y - 1
                # 👇 Fügt folgenden Code ab hier zu eurem Programm hinzu
                if key == curses.KEY_DOWN and y < screen_height - 1:
                    y = y + 1
                if key == curses.KEY_LEFT and x > 0:
                    x = x - 1
                if key == curses.KEY_RIGHT and x < screen_width - 2:
                    x = x + 1

        curses.wrapper(main)
    ```

1. 💬 Nun solltet ihr den Cursor über das gesamte Spielfeld bewegen können, ohne dass es einen Fehler gibt.

1. Als nächstes stellen wir das Programm so ein, dass der Cursor seine Anfangsposition in der Mitte des Bildfeldes hat.

1. 👩‍💻 Geht zurück zum Editor und verändert die folgenden 2 Zeilen. (💾 / 🎮 / ☝️)

    ```python
    x = screen_width // 2
    y = screen_height // 2
    ```

1. Wir haben es vorerst einmal geschafft. Überlegt euch doch mal, wie man das einfache Spiel erweitern kann.

## Ressourcen

* [Curses](https://docs.python.org/3/howto/curses.html)
