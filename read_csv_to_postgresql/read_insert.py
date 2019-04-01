import csv
from postgres_connect import connect

"""
This scripts reads from a csv file and inserts into postgresql
It inserts a client portfolio apparently
Try experimenting, changing, optimizing, break and break,, salute
"""

def add_client_data_loan():
    try:
        conn = connect()
        if conn is None:
            print('PostgreSQL Connection Error')
        else:
            cur = conn.cursor()
            print("Creating SQL Query")
            print("")
            query = "INSERT INTO res_partner(name, phone, mobile, email,  street, street2, city, country, is_company) VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}')"
            # Open csv file to read from, add read mode if you feel it.
            with open("YOUR_CAV_FILE") as csv_file:
                data = csv.DictReader(csv_file)
                print("Attempting to Write to Database")
                # loop through the data. pass column names as keys to row
                for row in data:
                    print("")
                    # get each column and replace ' with empty string .. add to Database
                    cur.execute(query.format(row['Name'].replace("\'", ""), row['Phone1'].replace("\'", ""), row['Phone2'].replace("\'", ""), row['Email'].replace("\'", ""), row['Address1'].replace("\'", ""), row['Address2'].replace("\'", ""), row['City'].replace("\'", ""), row['CountryID'].replace("\'", ""), False))
                cur.close()
                print("Finished Writing to Database")
                print("")
                conn.commit()
                print("Saving Changes to Database")
                print("")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')
            print("")

if __name__ == '__main__':
    add_client_data_loan()
