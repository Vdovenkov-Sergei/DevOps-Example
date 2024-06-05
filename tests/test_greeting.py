from src.greeting import greeting


def test_greeting(capsys):
    greeting("Sergei")
    out, _ = capsys.readouterr()
    assert out == "Hello, Sergei!\nOkey. Let me try to calculate examples!\n\n"
