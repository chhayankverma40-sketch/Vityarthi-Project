# DNA Analyser Architecture

```text
                 +----------------+
                 |    main.py     |
                 |   CLI / Menu   |
                 +-------+--------+
                         |
              +----------+----------+
              |                     |
              v                     v
       +--------------+      +--------------+
       | sequence.py  |      | analysis.py  |
       | validate     |      | transcription|
       | count        |      | translation  |
       | GC/AT        |      | motif search |
       | complement   |      | comparison   |
       +--------------+      +--------------+
              |                     |
              +----------+----------+
                         v
                   +-----------+
                   | quiz.py   |
                   +-----+-----+
                         v
                questions.json
```
