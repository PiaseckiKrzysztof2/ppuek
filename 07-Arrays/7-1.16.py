# Zadanie 7-1.16 - Sortowanie funkcją sorted()
# Co robi: sortuje gotową funkcją sorted: odległości rosnąco, temperatury malejąco,
#          nazwy plików alfabetycznie.

distances_traveled = [120, 150, 180, 90, 200, 175, 160]
print('Distances ascending:', sorted(distances_traveled))                    # rosnąco

daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
print('Temperatures descending:', sorted(daily_temperatures, reverse=True))  # reverse=True - malejąco

file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]
print('File names ascending:', sorted(file_names))                           # napisy - alfabetycznie
