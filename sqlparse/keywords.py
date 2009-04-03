from sqlparse.tokens import *

KEYWORDS = {
    'ABORT': Keyword,
    'ABS': Keyword,
    'ABSOLUTE': Keyword,
    'ACCESS': Keyword,
    'ADA': Keyword,
    'ADD': Keyword,
    'ADMIN': Keyword,
    'AFTER': Keyword,
    'AGGREGATE': Keyword,
    'ALIAS': Keyword,
    'ALL': Keyword,
    'ALLOCATE': Keyword,
    'ANALYSE': Keyword,
    'ANALYZE': Keyword,
    'AND': Keyword,
    'ANY': Keyword,
    'ARE': Keyword,
    'AS': Keyword,
    'ASC': Keyword,
    'ASENSITIVE': Keyword,
    'ASSERTION': Keyword,
    'ASSIGNMENT': Keyword,
    'ASYMMETRIC': Keyword,
    'AT': Keyword,
    'ATOMIC': Keyword,
    'AUTHORIZATION': Keyword,
    'AVG': Keyword,

    'BACKWARD': Keyword,
    'BEFORE': Keyword,
    'BEGIN': Keyword,
    'BETWEEN': Keyword,
    'BITVAR': Keyword,
    'BIT_LENGTH': Keyword,
    'BOTH': Keyword,
    'BREADTH': Keyword,
    'BY': Keyword,

    'C': Keyword,
    'CACHE': Keyword,
    'CALL': Keyword,
    'CALLED': Keyword,
    'CARDINALITY': Keyword,
    'CASCADE': Keyword,
    'CASCADED': Keyword,
    'CASE': Keyword,
    'CAST': Keyword,
    'CATALOG': Keyword,
    'CATALOG_NAME': Keyword,
    'CHAIN': Keyword,
    'CHARACTERISTICS': Keyword,
    'CHARACTER_LENGTH': Keyword,
    'CHARACTER_SET_CATALOG': Keyword,
    'CHARACTER_SET_NAME': Keyword,
    'CHARACTER_SET_SCHEMA': Keyword,
    'CHAR_LENGTH': Keyword,
    'CHECK': Keyword,
    'CHECKED': Keyword,
    'CHECKPOINT': Keyword,
    'CLASS': Keyword,
    'CLASS_ORIGIN': Keyword,
    'CLOB': Keyword,
    'CLOSE': Keyword,
    'CLUSTER': Keyword,
    'COALSECE': Keyword,
    'COBOL': Keyword,
    'COLLATE': Keyword,
    'COLLATION': Keyword,
    'COLLATION_CATALOG': Keyword,
    'COLLATION_NAME': Keyword,
    'COLLATION_SCHEMA': Keyword,
    'COLUMN': Keyword,
    'COLUMN_NAME': Keyword,
    'COMMAND_FUNCTION': Keyword,
    'COMMAND_FUNCTION_CODE': Keyword,
    'COMMENT': Keyword,
    'COMMIT': Keyword,
    'COMMITTED': Keyword,
    'COMPLETION': Keyword,
    'CONDITION_NUMBER': Keyword,
    'CONNECT': Keyword,
    'CONNECTION': Keyword,
    'CONNECTION_NAME': Keyword,
    'CONSTRAINT': Keyword,
    'CONSTRAINTS': Keyword,
    'CONSTRAINT_CATALOG': Keyword,
    'CONSTRAINT_NAME': Keyword,
    'CONSTRAINT_SCHEMA': Keyword,
    'CONSTRUCTOR': Keyword,
    'CONTAINS': Keyword,
    'CONTINUE': Keyword,
    'CONVERSION': Keyword,
    'CONVERT': Keyword,
    'COPY': Keyword,
    'CORRESPONTING': Keyword,
    'COUNT': Keyword,
    'CREATEDB': Keyword,
    'CREATEUSER': Keyword,
    'CROSS': Keyword,
    'CUBE': Keyword,
    'CURRENT': Keyword,
    'CURRENT_DATE': Keyword,
    'CURRENT_PATH': Keyword,
    'CURRENT_ROLE': Keyword,
    'CURRENT_TIME': Keyword,
    'CURRENT_TIMESTAMP': Keyword,
    'CURRENT_USER': Keyword,
    'CURSOR': Keyword,
    'CURSOR_NAME': Keyword,
    'CYCLE': Keyword,

    'DATA': Keyword,
    'DATABASE': Keyword,
    'DATETIME_INTERVAL_CODE': Keyword,
    'DATETIME_INTERVAL_PRECISION': Keyword,
    'DAY': Keyword,
    'DEALLOCATE': Keyword,
    'DECLARE': Keyword,
    'DEFAULT': Keyword,
    'DEFAULTS': Keyword,
    'DEFERRABLE': Keyword,
    'DEFERRED': Keyword,
    'DEFINED': Keyword,
    'DEFINER': Keyword,
    'DELIMITER': Keyword,
    'DELIMITERS': Keyword,
    'DEREF': Keyword,
    'DESC': Keyword,
    'DESCRIBE': Keyword,
    'DESCRIPTOR': Keyword,
    'DESTROY': Keyword,
    'DESTRUCTOR': Keyword,
    'DETERMINISTIC': Keyword,
    'DIAGNOSTICS': Keyword,
    'DICTIONARY': Keyword,
    'DISCONNECT': Keyword,
    'DISPATCH': Keyword,
    'DISTINCT': Keyword,
    'DO': Keyword,
    'DOMAIN': Keyword,
    'DYNAMIC': Keyword,
    'DYNAMIC_FUNCTION': Keyword,
    'DYNAMIC_FUNCTION_CODE': Keyword,

    'EACH': Keyword,
    'ELSE': Keyword,
    'ENCODING': Keyword,
    'ENCRYPTED': Keyword,
    'END': Keyword,
    'END-EXEC': Keyword,
    'EQUALS': Keyword,
    'ESCAPE': Keyword,
    'EVERY': Keyword,
    'EXCEPT': Keyword,
    'ESCEPTION': Keyword,
    'EXCLUDING': Keyword,
    'EXCLUSIVE': Keyword,
    'EXEC': Keyword,
    'EXECUTE': Keyword,
    'EXISTING': Keyword,
    'EXISTS': Keyword,
    'EXTERNAL': Keyword,
    'EXTRACT': Keyword,

    'FALSE': Keyword,
    'FETCH': Keyword,
    'FINAL': Keyword,
    'FIRST': Keyword,
    'FOR': Keyword,
    'FORCE': Keyword,
    'FOREIGN': Keyword,
    'FORTRAN': Keyword,
    'FORWARD': Keyword,
    'FOUND': Keyword,
    'FREE': Keyword,
    'FREEZE': Keyword,
    'FROM': Keyword,
    'FULL': Keyword,
    'FUNCTION': Keyword,

    'G': Keyword,
    'GENERAL': Keyword,
    'GENERATED': Keyword,
    'GET': Keyword,
    'GLOBAL': Keyword,
    'GO': Keyword,
    'GOTO': Keyword,
    'GRANT': Keyword,
    'GRANTED': Keyword,
    'GROUP': Keyword,
    'GROUPING': Keyword,

    'HANDLER': Keyword,
    'HAVING': Keyword,
    'HIERARCHY': Keyword,
    'HOLD': Keyword,
    'HOST': Keyword,

    'IDENTITY': Keyword,
    'IF': Keyword,
    'IGNORE': Keyword,
    'ILIKE': Keyword,
    'IMMEDIATE': Keyword,
    'IMMUTABLE': Keyword,

    'IMPLEMENTATION': Keyword,
    'IMPLICIT': Keyword,
    'IN': Keyword,
    'INCLUDING': Keyword,
    'INCREMENT': Keyword,
    'INDEX': Keyword,

    'INDITCATOR': Keyword,
    'INFIX': Keyword,
    'INHERITS': Keyword,
    'INITIALIZE': Keyword,
    'INITIALLY': Keyword,
    'INNER': Keyword,
    'INOUT': Keyword,
    'INPUT': Keyword,
    'INSENSITIVE': Keyword,
    'INSTANTIABLE': Keyword,
    'INSTEAD': Keyword,
    'INTERSECT': Keyword,
    'INTO': Keyword,
    'INVOKER': Keyword,
    'IS': Keyword,
    'ISNULL': Keyword,
    'ISOLATION': Keyword,
    'ITERATE': Keyword,

    'JOIN': Keyword,

    'K': Keyword,
    'KEY': Keyword,
    'KEY_MEMBER': Keyword,
    'KEY_TYPE': Keyword,

    'LANCOMPILER': Keyword,
    'LANGUAGE': Keyword,
    'LARGE': Keyword,
    'LAST': Keyword,
    'LATERAL': Keyword,
    'LEADING': Keyword,
    'LEFT': Keyword,
    'LENGTH': Keyword,
    'LESS': Keyword,
    'LEVEL': Keyword,
    'LIKE': Keyword,
    'LILMIT': Keyword,
    'LISTEN': Keyword,
    'LOAD': Keyword,
    'LOCAL': Keyword,
    'LOCALTIME': Keyword,
    'LOCALTIMESTAMP': Keyword,
    'LOCATION': Keyword,
    'LOCATOR': Keyword,
    'LOCK': Keyword,
    'LOWER': Keyword,

    'M': Keyword,
    'MAP': Keyword,
    'MATCH': Keyword,
    'MAX': Keyword,
    'MAXVALUE': Keyword,
    'MESSAGE_LENGTH': Keyword,
    'MESSAGE_OCTET_LENGTH': Keyword,
    'MESSAGE_TEXT': Keyword,
    'METHOD': Keyword,
    'MIN': Keyword,
    'MINUTE': Keyword,
    'MINVALUE': Keyword,
    'MOD': Keyword,
    'MODE': Keyword,
    'MODIFIES': Keyword,
    'MODIFY': Keyword,
    'MONTH': Keyword,
    'MORE': Keyword,
    'MOVE': Keyword,
    'MUMPS': Keyword,

    'NAMES': Keyword,
    'NATIONAL': Keyword,
    'NATURAL': Keyword,
    'NCHAR': Keyword,
    'NCLOB': Keyword,
    'NEW': Keyword,
    'NEXT': Keyword,
    'NO': Keyword,
    'NOCREATEDB': Keyword,
    'NOCREATEUSER': Keyword,
    'NONE': Keyword,
    'NOT': Keyword,
    'NOTHING': Keyword,
    'NOTIFY': Keyword,
    'NOTNULL': Keyword,
    'NULL': Keyword,
    'NULLABLE': Keyword,
    'NULLIF': Keyword,

    'OBJECT': Keyword,
    'OCTET_LENGTH': Keyword,
    'OF': Keyword,
    'OFF': Keyword,
    'OFFSET': Keyword,
    'OIDS': Keyword,
    'OLD': Keyword,
    'ON': Keyword,
    'ONLY': Keyword,
    'OPEN': Keyword,
    'OPERATION': Keyword,
    'OPERATOR': Keyword,
    'OPTION': Keyword,
    'OPTIONS': Keyword,
    'OR': Keyword,
    'ORDER': Keyword,
    'ORDINALITY': Keyword,
    'OUT': Keyword,
    'OUTER': Keyword,
    'OUTPUT': Keyword,
    'OVERLAPS': Keyword,
    'OVERLAY': Keyword,
    'OVERRIDING': Keyword,
    'OWNER': Keyword,

    'PAD': Keyword,
    'PARAMETER': Keyword,
    'PARAMETERS': Keyword,
    'PARAMETER_MODE': Keyword,
    'PARAMATER_NAME': Keyword,
    'PARAMATER_ORDINAL_POSITION': Keyword,
    'PARAMETER_SPECIFIC_CATALOG': Keyword,
    'PARAMETER_SPECIFIC_NAME': Keyword,
    'PARAMATER_SPECIFIC_SCHEMA': Keyword,
    'PARTIAL': Keyword,
    'PASCAL': Keyword,
    'PENDANT': Keyword,
    'PLACING': Keyword,
    'PLI': Keyword,
    'POSITION': Keyword,
    'POSTFIX': Keyword,
    'PRECISION': Keyword,
    'PREFIX': Keyword,
    'PREORDER': Keyword,
    'PREPARE': Keyword,
    'PRESERVE': Keyword,
    'PRIMARY': Keyword,
    'PRIOR': Keyword,
    'PRIVILEGES': Keyword,
    'PROCEDURAL': Keyword,
    'PROCEDURE': Keyword,
    'PUBLIC': Keyword,

    'RAISE': Keyword,
    'READ': Keyword,
    'READS': Keyword,
    'RECHECK': Keyword,
    'RECURSIVE': Keyword,
    'REF': Keyword,
    'REFERENCES': Keyword,
    'REFERENCING': Keyword,
    'REINDEX': Keyword,
    'RELATIVE': Keyword,
    'RENAME': Keyword,
    'REPEATABLE': Keyword,
    'REPLACE': Keyword,
    'RESET': Keyword,
    'RESTART': Keyword,
    'RESTRICT': Keyword,
    'RESULT': Keyword,
    'RETURN': Keyword,
    'RETURNED_LENGTH': Keyword,
    'RETURNED_OCTET_LENGTH': Keyword,
    'RETURNED_SQLSTATE': Keyword,
    'RETURNS': Keyword,
    'REVOKE': Keyword,
    'RIGHT': Keyword,
    'ROLE': Keyword,
    'ROLLBACK': Keyword,
    'ROLLUP': Keyword,
    'ROUTINE': Keyword,
    'ROUTINE_CATALOG': Keyword,
    'ROUTINE_NAME': Keyword,
    'ROUTINE_SCHEMA': Keyword,
    'ROW': Keyword,
    'ROWS': Keyword,
    'ROW_COUNT': Keyword,
    'RULE': Keyword,

    'SAVE_POINT': Keyword,
    'SCALE': Keyword,
    'SCHEMA': Keyword,
    'SCHEMA_NAME': Keyword,
    'SCOPE': Keyword,
    'SCROLL': Keyword,
    'SEARCH': Keyword,
    'SECOND': Keyword,
    'SECURITY': Keyword,
    'SELF': Keyword,
    'SENSITIVE': Keyword,
    'SERIALIZABLE': Keyword,
    'SERVER_NAME': Keyword,
    'SESSION': Keyword,
    'SESSION_USER': Keyword,
    'SETOF': Keyword,
    'SETS': Keyword,
    'SHARE': Keyword,
    'SHOW': Keyword,
    'SIMILAR': Keyword,
    'SIMPLE': Keyword,
    'SIZE': Keyword,
    'SOME': Keyword,
    'SOURCE': Keyword,
    'SPACE': Keyword,
    'SPECIFIC': Keyword,
    'SPECIFICTYPE': Keyword,
    'SPECIFIC_NAME': Keyword,
    'SQL': Keyword,
    'SQLCODE': Keyword,
    'SQLERROR': Keyword,
    'SQLEXCEPTION': Keyword,
    'SQLSTATE': Keyword,
    'SQLWARNINIG': Keyword,
    'STABLE': Keyword,
    'START': Keyword,
    'STATE': Keyword,
    'STATEMENT': Keyword,
    'STATIC': Keyword,
    'STATISTICS': Keyword,
    'STDIN': Keyword,
    'STDOUT': Keyword,
    'STORAGE': Keyword,
    'STRICT': Keyword,
    'STRUCTURE': Keyword,
    'STYPE': Keyword,
    'SUBCLASS_ORIGIN': Keyword,
    'SUBLIST': Keyword,
    'SUBSTRING': Keyword,
    'SUM': Keyword,
    'SYMMETRIC': Keyword,
    'SYSID': Keyword,
    'SYSTEM': Keyword,
    'SYSTEM_USER': Keyword,

    'TABLE': Keyword,
    'TABLE_NAME': Keyword,
    ' TEMP': Keyword,
    'TEMPLATE': Keyword,
    'TEMPORARY': Keyword,
    'TERMINATE': Keyword,
    'THAN': Keyword,
    'THEN': Keyword,
    'TIMESTAMP': Keyword,
    'TIMEZONE_HOUR': Keyword,
    'TIMEZONE_MINUTE': Keyword,
    'TO': Keyword,
    'TOAST': Keyword,
    'TRAILING': Keyword,
    'TRANSATION': Keyword,
    'TRANSACTIONS_COMMITTED': Keyword,
    'TRANSACTIONS_ROLLED_BACK': Keyword,
    'TRANSATION_ACTIVE': Keyword,
    'TRANSFORM': Keyword,
    'TRANSFORMS': Keyword,
    'TRANSLATE': Keyword,
    'TRANSLATION': Keyword,
    'TREAT': Keyword,
    'TRIGGER': Keyword,
    'TRIGGER_CATALOG': Keyword,
    'TRIGGER_NAME': Keyword,
    'TRIGGER_SCHEMA': Keyword,
    'TRIM': Keyword,
    'TRUE': Keyword,
    'TRUNCATE': Keyword,
    'TRUSTED': Keyword,
    'TYPE': Keyword,

    'UNCOMMITTED': Keyword,
    'UNDER': Keyword,
    'UNENCRYPTED': Keyword,
    'UNION': Keyword,
    'UNIQUE': Keyword,
    'UNKNOWN': Keyword,
    'UNLISTEN': Keyword,
    'UNNAMED': Keyword,
    'UNNEST': Keyword,
    'UNTIL': Keyword,
    'UPPER': Keyword,
    'USAGE': Keyword,
    'USER': Keyword,
    'USER_DEFINED_TYPE_CATALOG': Keyword,
    'USER_DEFINED_TYPE_NAME': Keyword,
    'USER_DEFINED_TYPE_SCHEMA': Keyword,
    'USING': Keyword,

    'VACUUM': Keyword,
    'VALID': Keyword,
    'VALIDATOR': Keyword,
    'VALUES': Keyword,
    'VARIABLE': Keyword,
    'VERBOSE': Keyword,
    'VERSION': Keyword,
    'VIEW': Keyword,
    'VOLATILE': Keyword,

    'WHEN': Keyword,
    'WHENEVER': Keyword,
    'WHERE': Keyword,
    'WITH': Keyword,
    'WITHOUT': Keyword,
    'WORK': Keyword,
    'WRITE': Keyword,

    'YEAR': Keyword,

    'ZONE': Keyword,


    'ARRAY': Name.Builtin,
    'BIGINT': Name.Builtin,
    'BINARY': Name.Builtin,
    'BIT': Name.Builtin,
    'BLOB': Name.Builtin,
    'BOOLEAN': Name.Builtin,
    'CHAR': Name.Builtin,
    'CHARACTER': Name.Builtin,
    'DATE': Name.Builtin,
    'DEC': Name.Builtin,
    'DECIMAL': Name.Builtin,
    'FLOAT': Name.Builtin,
    'INT': Name.Builtin,
    'INTEGER': Name.Builtin,
    'INTERVAL': Name.Builtin,
    'NUMBER': Name.Builtin,
    'NUMERIC': Name.Builtin,
    'REAL': Name.Builtin,
    'SERIAL': Name.Builtin,
    'SMALLINT': Name.Builtin,
    'VARCHAR': Name.Builtin,
    'VARYING': Name.Builtin,
    'INT8': Name.Builtin,
    'SERIAL8': Name.Builtin,
    'TEXT': Name.Builtin,
    }


KEYWORDS_COMMON = {
    'SELECT': Keyword.DML,
    'INSERT': Keyword.DML,
    'DELETE': Keyword.DML,
    'UPDATE': Keyword.DML,
    'DROP': Keyword.DDL,
    'CREATE': Keyword.DDL,
    'ALTER': Keyword.DDL,

    'WHERE': Keyword,
    'FROM': Keyword,
    'INNER': Keyword,
    'JOIN': Keyword,
    'AND': Keyword,
    'OR': Keyword,
    'LIKE': Keyword,
    'ON': Keyword,
    'IN': Keyword,

    'BY': Keyword,
    'GROUP': Keyword,
    'ORDER': Keyword,
    'LEFT': Keyword,
    'OUTER': Keyword,

    'IF': Keyword,
    'END': Keyword,
    'THEN': Keyword,
    'LOOP': Keyword,
    'AS': Keyword,
    'ELSE': Keyword,
    'FOR': Keyword,

    'CASE': Keyword,
    'WHEN': Keyword,
    'MIN': Keyword,
    'MAX': Keyword,
    'DISTINCT': Keyword,

    }
