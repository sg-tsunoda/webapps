
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    roll_no = Column(String(50), unique=True, nullable=False)
    class_name = Column(String(50), nullable=False)

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(10), nullable=False)
    student = relationship('Student', backref='attendance_records')

class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

def main():
    engine = create_engine('sqlite:///attendance.db')
    Base.metadata.create_all(engine)
    print("✅ Database and tables created successfully as attendance.db")

if __name__ == '__main__':
    main()
