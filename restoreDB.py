import os
import sqlalchemy

path = ""
engine = sqlalchemy.create_engine("mysql://username:password@host")

filesInPath = os.listdir(path)
fileCount = len(filesInPath)

for i in range (0, fileCount):
    file = path + "\\" + str(i) + ".sql"
    if os.path.isfile(file):
        print(f"File: {file}")

        with open(file, "r") as f:
            sql = f.read()
            try:
                with engine.connect() as con:
                    con.execute(sqlalchemy.text(sql))
                    print(f"File {file} executed successfully")
            except Exception as e:
                print(f"File {file} failed to execute")
                print(e)
    else:
        print(f"{path}\{i}.sql not found")

    os.system("cls")

print("All files executed successfully")