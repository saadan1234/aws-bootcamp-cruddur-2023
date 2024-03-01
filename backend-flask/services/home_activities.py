from datetime import datetime, timedelta, timezone
from lib.db.py import pool

class HomeActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    span.set_attribute("app.now", now.isoformat())

    sql = """ SELECT * FROM activities;"""

    with pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
        # this will return a tuple
        # the first field being the data
        json = cur.fetchall()
    return json[0]
    
    