import csv

rows=[]

with open('filter_stars.csv', mode = 'r') as f:
    csv_reader=csv.reader(f)
    
    for row in csv_reader:
        rows.append(row)

stars_data=[]

headers=rows[0]
star_data_rows=rows[1:]

final_star_list = []

for star_data in star_data_rows:
  temp_dict = {
                  "name": star_data[2],
                  "distance": star_data[3],
                  "mass": star_data[4],
                  "radius": star_data[5],
                  "gravity": star_data[6]
              }
  final_star_list.append(temp_dict)

print(final_star_list)