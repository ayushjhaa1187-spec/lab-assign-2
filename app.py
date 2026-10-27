import csv
import sys
import matplotlib.pyplot as plt


def error_page():
    html = '''<!DOCTYPE html>
<html>
<body>
<h1>Wrong Input</h1>
<p>Something went wrong</p>
</body>
</html>
'''
    with open('output.html', 'w') as f:
        f.write(html)


if len(sys.argv) != 3:
    error_page()
    sys.exit()

flag = sys.argv[1]
value = sys.argv[2]

try:
    with open('data.csv', 'r') as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        headers = reader.fieldnames
        student_key = headers[0]
        course_key = headers[1]
        marks_key = headers[2]
        data = list(reader)
except Exception:
    error_page()
    sys.exit()

if flag == "-s":
    records = []
    for row in data:
        if row[student_key] == value:
            records.append(row)
    if len(records) == 0:
        error_page()
        sys.exit()
    total = 0
    html = """<!DOCTYPE html>
<html>
<body>
<h1>Student Details</h1>
<table border="1">
    <tr>
        <th>Student ID</th>
        <th>Course ID</th>
        <th>Marks</th>
    </tr>"""
    for row in records:
        total += int(row[marks_key])
        html += f"""
    <tr>
        <td>{row[student_key]}</td>
        <td>{row[course_key]}</td>
        <td>{row[marks_key]}</td>
    </tr>"""
    html += f"""
    <tr>
        <td colspan="2">Total Marks</td>
        <td>{total}</td>
    </tr>
</table>
</body>
</html>
"""
    with open('output.html', 'w') as f:
        f.write(html)

elif flag == "-c":
    marks = []
    for row in data:
        if row[course_key] == value:
            marks.append(int(row[marks_key]))
    if len(marks) == 0:
        error_page()
        sys.exit()
    average = sum(marks) / len(marks)
    maximum = max(marks)
    plt.hist(marks)
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig('histogram.png')
    plt.close()
    html = f"""<!DOCTYPE html>
<html>
<body>
<h1>Course Details</h1>
<table border="1">
    <tr>
        <th>Average Marks</th>
        <th>Maximum Marks</th>
    </tr>
    <tr>
        <td>{average}</td>
        <td>{maximum}</td>
    </tr>
</table>
<img src="histogram.png" alt="Histogram">
</body>
</html>
"""
    with open('output.html', 'w') as f:
        f.write(html)

else:
    error_page()
    sys.exit()