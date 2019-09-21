var sql = require("mssql");

// Create a configuration object for our Azure SQL connection parameters
var dbConfig = {
 server: "polysqlsrvrpiyush.database.windows.net", // Use your SQL server name
 database: "AdventureWorks", // Database to connect to
 user: "testuser", // Use your username
 password: "TestPa$$w0rd", // Use your password
 port: 1433,
 // Since we're on Windows Azure, we need to set the following options
 options: {
       encrypt: true
   }
};


sql.connect(dbConfig).then(() => {
    return sql.query`SELECT * FROM Products`
}).then(result => {
    console.dir(result.recordset)
    sql.close()
}).catch(err => {
    // ... error checks
    console.log(err);
})
