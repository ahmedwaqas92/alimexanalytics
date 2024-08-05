import sys
sys.path.append("../../")
from libraries.libraries import *
from processes.datafetch.datafetch import data
from schema.connectionstring.connection import databaseString


class dataPush():
    def __init__(self):
        pass
    def toDatabase(self):
        connectionString = sqlite3.connect(databaseString)
        try:
            link = connectionString.cursor()
            drop_workorders = "DROP TABLE IF EXISTS workorders"
            link.execute(drop_workorders)
            
            create_table_sql = """
                CREATE TABLE IF NOT EXISTS workorders (
                    running_number INTEGER PRIMARY KEY,
                    record_id TEXT,
                    cutplan TEXT,
                    heat_lot_no TEXT,
                    work_order TEXT,
                    customer_name TEXT,
                    need_by_date_24h TEXT,
                    need_by_date_ampm TEXT,
                    status_from TEXT,
                    status_to_work TEXT,
                    comment_from_qc TEXT,
                    picture_from_qc TEXT,
                    time_created_24h TEXT,
                    planner_comment TEXT,
                    part_name TEXT,
                    quantity TEXT,
                    quantity_left TEXT,
                    so_num TEXT,
                    po_num TEXT,
                    width TEXT,
                    length TEXT,
                    thickness TEXT,
                    weight TEXT,
                    offcut TEXT,
                    starting_machine TEXT,
                    finishing_machine TEXT,
                    only_machine TEXT,
                    done_status TEXT,
                    sequence TEXT,
                    deleted TEXT,
                    rework_comment TEXT,
                    qc_name TEXT,
                    qc_review TEXT,
                    planner_name TEXT,
                    qc_percentage TEXT,
                    notified_qc TEXT,
                    packaging_comment TEXT
                )
                """
                
            link.execute(create_table_sql)
            
            insert_sql = """
                INSERT INTO workorders (
                    running_number, record_id, cutplan, heat_lot_no, work_order, customer_name, 
                    need_by_date_24h, need_by_date_ampm, status_from, status_to_work, 
                    comment_from_qc, picture_from_qc, time_created_24h, planner_comment, 
                    part_name, quantity, quantity_left, so_num, po_num, width, length, 
                    thickness, weight, offcut, starting_machine, finishing_machine, 
                    only_machine, done_status, sequence, deleted, rework_comment, 
                    qc_name, qc_review, planner_name, qc_percentage, notified_qc, 
                    packaging_comment
                ) VALUES (
                    :index, :record_id, :cutplan, :heat_lot_no, :work_order, :customer_name, 
                    :need_by_date_24h, :need_by_date_ampm, :status_from, :status_to_work, 
                    :comment_from_qc, :picture_from_qc, :time_created_24h, :planner_comment, 
                    :part_name, :quantity, :quantity_left, :so_num, :po_num, :width, :length, 
                    :thickness, :weight, :offcut, :starting_machine, :finishing_machine, 
                    :only_machine, :done_status, :sequence, :deleted, :rework_comment, 
                    :qc_name, :qc_review, :planner_name, :qc_percentage, :notified_qc, 
                    :packaging_comment
                )
                """
            
            for record in data:
                print(f"Inserting record: {record}")
                link.execute(insert_sql, record)
                

            connectionString.commit()
            print("Data successfully pushed to database.")
            connectionString.close()
  
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            

dataPush().toDatabase()