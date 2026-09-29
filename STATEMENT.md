# STATEMENT.md

## PROBLEM STATEMENT
In educational environments, managing student academic records manually using paper registers or simple spreadsheets is inefficient, time-consuming, and prone to human error. Manual calculation of class statistics—such as individual letter grades or class averages—increases administrative workload and leads to inconsistency in evaluation. Furthermore, without validation checks, there is a constant risk of recording invalid marks, making it difficult to maintain accurate and reliable student performance data.

## SCOPE OF PROJECT
The scope of this project focuses on developing a lightweight, terminal-based Python application designed for basic academic record management.

### In-Scope:
*   **CLI Interface:** Interactive command-line interface driven by user menu options.
*   **CRUD Operations:** Ability to Add, Update, Delete, and View student records.
*   **Automated Grading:** Logic to automatically map numerical marks (out of 100) to letter grades (`A`, `B`, `C`, `D`, `F`).
*   **Data Validation:** Score boundary enforcement ($0 \le \text{marks} \le 100$) to prevent invalid entries.
*   **Class Analytics:** Aggregate statistical calculation to determine class-wide average marks and average grade.

### Out-of-Scope:
*   Graphical User Interface (GUI) or web interface (focused purely on CLI).
*   Persistent database storage (records reside in in-memory dictionary during runtime).
*   Multi-subject or multi-semester grade tracking per student.

## TARGET USERS
*   **Teachers & Instructors:** Who need a quick, distraction-free tool to input marks and automatically calculate grades for a class.
*   **Academic Tutors:** Looking to track individual student progress and overall batch averages.
*   **Students & Python Beginners:** Studying CLI-based application design, data structures (dictionaries), and modular programming concepts.

## HIGH LEVEL FEATURES
*   **Interactive Menu System:** Loop-driven terminal menu allowing continuous operations until exit.
*   **Automated Grade Assignment:** Instant conversion of numeric scores into standard letter grades based on predefined boundary criteria.
*   **Data Guardrails:** Built-in checks to reject marks outside the standard 0–100 scale.
*   **Individual & Group Record Lookup:** Options to view the entire class roster or query specific individual results.
*   **Dynamic Class Performance Metric:** Real-time class average calculation updated dynamically as records are modified.
