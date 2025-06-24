CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE class (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES user(id)
);

CREATE TABLE student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES class(id)
);

CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    class_id INTEGER,
    student_id INTEGER,
    status TEXT,
    FOREIGN KEY (class_id) REFERENCES class(id),
    FOREIGN KEY (student_id) REFERENCES student(id)
);