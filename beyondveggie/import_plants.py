import pandas

from planting_table.models import Plant


def import_data(file, sheet):
    csv_df = pandas.read_csv(file, sheet_name=sheet)
    plants_json = csv_df.to_json()

    for plant in plants_json:
        plant = Plant(plant_name=['name'], plant_type=['type'],
                      seeding_time=['seed_time'], planting_date=['plant_date'],
                      plant_spacing=['spacing'], days_till_harvest=['harvest'],
                      yield_size=['yield'])
        plant.save()
