import os
import re

def SplitInsertQuery(sqlQuery):
    tableName = re.search("\`(.*?)\`", sqlQuery).group(1)

    values = sqlQuery.split("VALUES ")
    values.pop(0)
    values = values[0].split("),")

    for i in range(0, len(values)):
        if (values[i][-1] == ";"):
            values[i] = values[i][:-1]
        else:
            values[i] += ")"

    return tableName, values