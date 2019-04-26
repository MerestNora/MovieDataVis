import pymongo
import datetime

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['movie_db']

col_wl = db['weekly']
col_bg = db['budget']

def weeklyGrossTrendByYear():
    years = ["2015", "2016", "2017", "2018"]
    for year in years:
        for record in col_wl.find({"Year": year}):
            print(record["Week#"])

def updateBudgetWeek():
    for record in col_bg.find():
        tt = record['title']
        rd = record['ReleaseDate']
        rd = str(rd).strip('00:00:00')
        rd = rd.split('-')
        print(rd)
        dt = datetime.date(int(rd[0]), int(rd[1]), int(rd[2]))
        wk = dt.isocalendar()[1]
        print(wk)
        col_bg.find_one_and_update({"title": tt},
                            {"$set": {"week#": wk}})


if __name__ == "__main__":
    # weeklyGrossTrendByYear()
    updateBudgetWeek()