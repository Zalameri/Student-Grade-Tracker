import pytest

import main


def test_total_adds_the_three_grades():
    assert main.calculate_total(20, 25, 40) == 85


@pytest.mark.parametrize(
    "total, expected",
    [(85, "Pass"), (60, "Pass"), (59.9, "Fail"), (0, "Fail")],
)
def test_status_uses_pass_mark_of_60(total, expected):
    assert main.get_status(total) == expected


@pytest.mark.parametrize("text, expected", [("20", 20.0), (" 17.5 ", 17.5), ("0", 0.0)])
def test_parse_grade_accepts_valid_numbers(text, expected):
    assert main.parse_grade(text) == expected


@pytest.mark.parametrize("text", ["abc", "", "-5", "nan", "inf"])
def test_parse_grade_rejects_invalid_input(text):
    with pytest.raises(ValueError):
        main.parse_grade(text)


def test_summarize_handles_empty_and_normal_lists():
    assert main.summarize([]) == (0, 0.0, 0)
    assert main.summarize([("A", 80, "Pass"), ("B", 40, "Fail")]) == (2, 60.0, 1)


def run_program(monkeypatch, capsys, answers):
    feed = iter(answers)
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(feed))
    main.main()
    return capsys.readouterr().out


def test_program_matches_readme_example(monkeypatch, capsys):
    out = run_program(monkeypatch, capsys, ["Sarah", "20", "25", "40", "n"])
    assert "Student Name: Sarah" in out
    assert "Total Grade: 85.0" in out
    assert "Status: Pass" in out


def test_program_reprompts_after_bad_input(monkeypatch, capsys):
    out = run_program(monkeypatch, capsys, ["", "Lina", "abc", "-1", "10", "10", "10", "n"])
    assert "Name cannot be empty." in out
    assert out.count("Invalid input") == 2
    assert "Total Grade: 30.0" in out
    assert "Status: Fail" in out


def test_program_handles_several_students_and_shows_summary(monkeypatch, capsys):
    answers = ["A", "30", "30", "30", "y", "B", "10", "10", "10", "n"]
    out = run_program(monkeypatch, capsys, answers)
    assert "Students: 2 | Average: 60.0 | Passed: 1/2" in out
