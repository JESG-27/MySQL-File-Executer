import os
import sqlalchemy
from splitQuery import SplitInsertQuery

class DataBase:
    def __init__(self, username, password, host, database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.engine = sqlalchemy.create_engine(f"mysql://{self.username}:{self.password}@{self.host}/{self.database}")

path = ""

DataBaseEngine = DataBase(username="", 
                          password="", 
                          host="",
                          database="")

filesInPath = os.listdir(path)
fileCount = len(filesInPath)

for i in range (0, fileCount):

    file = path + "\\" + str(i) + ".sql"
    isInsertTo = False

    if os.path.isfile(file):
        print(f"File: {file}")

        with open(file, "r", errors="ignore") as f:
            sqlFile = f.read()

            if "INSERT INTO" in sqlFile:
                firstLine = sqlFile.split('\n', 1)[0]
                tableName, valuesToInsert = SplitInsertQuery(firstLine)
                for value in valuesToInsert:
                    sql = sqlalchemy.text(f"INSERT INTO `{tableName}` VALUES {value};")
                    
                    try:
                        with DataBaseEngine.engine.connect() as con:
                            con.execute(sql)
                            con.commit()

                    except Exception as e:
                        print(f"File {file} failed to execute")
                        print(e)
                        os.system("pause")
                
                print(f"File {file} executed successfully")
            
            else:
                try:
                    with DataBaseEngine.engine.connect() as con:
                        con.execute(sqlalchemy.text(sqlFile))

                except Exception as e:
                    print(f"File {file} failed to execute")
                    print(e)
                    os.system("pause")

            # try:
            #     with DataBaseEngine.engine.connect() as con:
            #         con.execute(sqlalchemy.text(sql))
            #         print(f"File {file} executed successfully")

            # except Exception as e:
            #     print(f"File {file} failed to execute")
            #     print(e)
    else:
        print(f"{path}\{i}.sql not found")

    os.system("cls")