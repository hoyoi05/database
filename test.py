import sys

from Parser.mssql import MSSQL
from Parser.mssql import MSSQLRecovery

def main():
    print('MSSQL Record Recovery Tool (version 1.0)')
    mssql_class = MSSQL()
    mssql_class.open(sys.argv[1])
    mssql_class.read(0, 512)
    mssql_recovery = MSSQLRecovery(mssql_class)
    #### Meta data parsing
    mssql_recovery.scanPages()
    mssql_recovery.getSystemTableColumnInfo()
    if mssql_recovery.getTableInfo() != True:
        sys.exit()
    mssql_recovery.getColumnInfo()
    mssql_recovery.getKeyColumnInfo()
    mssql_recovery.getPageObjectId() ## 이 부분 오류

    #### Recovery
    mssql_recovery.recovery()

if __name__ == "__main__":
    main()
